"""Read-only HTTP/CSS evidence capture. No claims about computed layout or states."""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from design_system import ROOT, atomic_write, normalize_url

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/131.0 Safari/537.36'
COLOR = re.compile(r'#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b')
FONT = re.compile(r'font-family\s*:\s*([^;{}]+)', re.I)
GENERIC = {'inherit','initial','unset','revert','serif','sans-serif','monospace','system-ui','-apple-system','blinkmacsystemfont','cursive','fantasy','emoji'}
BLOCKED = re.compile(r'<title[^>]*>\s*(?:just a moment|access denied|attention required|robot or human|security check|challenge validation|pardon our interruption|request rejected|human verification|checking your browser)|cf-chl-|verify you are human|captcha-container', re.I)

def source_problem(evidence):
    title=evidence.get('title','')
    excerpt=evidence.get('page_text_excerpt','').strip()
    if urlsplit(evidence.get('final_url','')).path.rstrip('/').endswith('/password'):
        return 'PASSWORD_GATE'
    if evidence.get('failure'):
        return evidence['failure']
    if 'page_text_excerpt' in evidence and not title.strip() and not evidence['page_text_excerpt'].strip():
        return 'INSUFFICIENT_SITE_IDENTITY'
    if re.search(r'challenge validation|client challenge|pardon our interruption|access denied|request rejected|human verification|checking your browser|just a moment|security verification|robot or human|404\s*(?:page )?not found|403 forbidden',title,re.I):
        return 'CHALLENGE_OR_ERROR_PAGE'
    if re.search(r'domain (?:is )?(?:for sale|reserved|parked)|buy this domain|website (?:is )?coming soon|domain name (?:is )?for sale|sedo domain parking',title,re.I):
        return 'PARKED_OR_PLACEHOLDER'
    if re.search(r'^[\w.-]+\.[a-z]{2,}\s*[-–:]?\s*(?:is\s+)?for sale|is registered at (?:namecheap|godaddy)',title,re.I):
        return 'PARKED_OR_PLACEHOLDER'
    if len(excerpt)<1500 and re.search(r"(?:this page is currently unavailable|we.re sorry.{0,40}page.{0,40}unavailable)",excerpt,re.I|re.S):
        return 'SITE_UNAVAILABLE'
    if len(excerpt)<3000 and re.search(r'is parked free, courtesy of|available on GoDaddy Auctions|^This domain has expired|^This domain is registered, but may still be available|recently registered with namecheap',excerpt,re.I):
        return 'PARKED_OR_PLACEHOLDER'
    if re.fullmatch(r'coming (?:soon|in \d{4})',title.strip(),re.I):return 'PARKED_OR_PLACEHOLDER'
    if len(excerpt)<1500 and re.search(r'download audio captcha|enter the characters seen in the image',excerpt,re.I):return 'CHALLENGE_OR_ERROR_PAGE'
    if re.search(r'is retiring, but check out our partners|has officially pressed pause on our operations',excerpt[:5000],re.I):return 'INACTIVE_STOREFRONT_NOTICE'
    return None

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.styles=[]; self.title=[]; self.in_style=False; self.in_title=False; self.in_head=False; self.in_script=False; self.visible=[]; self.description=''
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='head':self.in_head=True
        if tag=='script':self.in_script=True
        if tag=='meta' and a.get('name','').lower()=='description':self.description=a.get('content','')
        if tag=='link' and 'stylesheet' in (a.get('rel') or '').lower() and a.get('href'): self.links.append(a['href'])
        if a.get('style'): self.styles.append(a['style'])
        if tag=='style': self.in_style=True
        if tag=='title' and self.in_head: self.in_title=True
    def handle_endtag(self,tag):
        if tag=='style':self.in_style=False
        if tag=='title':self.in_title=False
        if tag=='head':self.in_head=False
        if tag=='script':self.in_script=False
    def handle_data(self,data):
        if self.in_style:self.styles.append(data)
        if self.in_title:self.title.append(data)
        if not self.in_style and not self.in_script and not self.in_head and data.strip() and len(self.visible)<300:self.visible.append(data.strip())

def fetch(url, timeout=25):
    try:
        p=subprocess.run(['curl','-sS','-L','--compressed','--proto','=http,https','--proto-redir','=http,https','--max-redirs','6','--max-time',str(timeout),'-A',UA,'-w','\n__FETCH_META__%{http_code}\t%{url_effective}\t%{content_type}',url],capture_output=True,timeout=timeout+5)
        body,sep,meta=p.stdout.rpartition(b'\n__FETCH_META__')
        fields=meta.decode('utf-8','replace').split('\t')
        code=int(fields[0]) if fields and fields[0].isdigit() else 0
        return dict(ok=p.returncode==0 and 200<=code<300, status=code, url=url, final_url=fields[1] if len(fields)>1 else url, content_type=fields[2] if len(fields)>2 else '', body=body.decode('utf-8','replace'))
    except (subprocess.TimeoutExpired,OSError) as e:
        return dict(ok=False,status=0,url=url,final_url=url,content_type='',body='',error=type(e).__name__)

def norm_hex(value):
    v=value.lstrip('#').lower()
    if len(v) in (3,4):v=''.join(c*2 for c in v)
    return '#'+v

def capture(site, root=ROOT, page_override=None, style_overrides=None):
    url=normalize_url(site['url']); slug=site['slug']
    now=datetime.now(timezone.utc).isoformat()
    page=page_override if page_override is not None else fetch(url)
    evidence=dict(source_url=url, final_url=page['final_url'], captured_at=now, method='static-html-css', pages=[], colors={}, font_families={}, css_rules=[], confidence='unverified', limitations=['CSS value presence does not verify semantic role, visibility or computed styles.','Layout, typography sizes, spacing, radii, interactions and responsive behavior are inferred unless explicitly evidenced.'])
    directory=root/'_state/evidence'/slug; directory.mkdir(parents=True,exist_ok=True)
    def save(response,name):
        body=response['body']; atomic_write(directory/name,body)
        evidence['pages'].append(dict(url=response['url'],final_url=response['final_url'],http_status=response['status'],content_type=response['content_type'],sha256=hashlib.sha256(body.encode()).hexdigest(),snapshot=name))
    save(page,'homepage.html')
    if not page['ok'] or BLOCKED.search(page['body'][:150000]):
        evidence['failure']='HTTP_OR_CHALLENGE';atomic_write(directory/'capture.json',json.dumps(evidence,indent=2)+'\n');return evidence
    parser=Page();parser.feed(page['body']);evidence['title']=' '.join(parser.title).strip()[:250]
    evidence['page_text_excerpt']=(parser.description+'\n'+' '.join(parser.visible))[:5000]
    problem=source_problem(evidence)
    if problem:
        evidence['failure']=problem;atomic_write(directory/'capture.json',json.dumps(evidence,indent=2)+'\n');return evidence
    sources=[(page['final_url'],'\n'.join(parser.styles))]
    if page_override is not None:
        evidence['method']='rendered-html-computed-css'
        evidence['limitations'].append('Rendered capture is one desktop viewport and initial state only; computed style snapshot selectors are sampling identifiers, not original site selectors.')
    for i,response in enumerate(style_overrides or []):
        save(response,f'rendered-style-{i+1}.css')
        sources.append((response['final_url'],response['body']))
    seen=set()
    # Theme CSS and web fonts often follow many plugin stylesheets.
    links=sorted(parser.links,key=lambda u:('/plugins/' in u or 'font-awesome' in u, not ('/themes/' in u or 'fonts.googleapis' in u)))
    for href in ([] if style_overrides is not None else links):
        css_url=urljoin(page['final_url'],href)
        if css_url in seen or urlsplit(css_url).scheme not in ('http','https'):continue
        seen.add(css_url)
        response=fetch(css_url,15)
        if response['ok'] and 'html' not in response['content_type'] and not BLOCKED.search(response['body'][:10000]):
            save(response,f'stylesheet-{len(seen)}.css');sources.append((css_url,response['body'][:1500000]))
        if len(seen)>=12:break
    # Follow a bounded number of explicit CSS imports, including web font sheets.
    for source,blob in list(sources):
        for match in re.finditer(r'@import\s+(?:url\(\s*)?[\"\x27]([^\"\x27]+)[\"\x27]',blob,re.I):
            css_url=urljoin(source,match[1])
            if css_url in seen or urlsplit(css_url).scheme not in ('http','https') or len(seen)>=16:continue
            seen.add(css_url);response=fetch(css_url,15)
            if response['ok'] and 'html' not in response['content_type']:
                save(response,f'import-{len(seen)}.css');sources.append((css_url,response['body'][:1500000]))
    color_counts=Counter(); colors=defaultdict(list); fonts=defaultdict(list)
    for source,blob in sources:
        blob=re.sub(r'/\*.*?\*/','',blob,flags=re.S)
        for m in COLOR.finditer(blob):
            value=norm_hex(m[0]);color_counts[value]+=1
            if source not in colors[value]:colors[value].append(source)
        for m in re.finditer(r'rgba?\(\s*(\d+)\s*[, ]\s*(\d+)\s*[, ]\s*(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)',blob,re.I):
            rgb=[int(m[i]) for i in (1,2,3)]
            if max(rgb)>255 or m[4] not in (None,'1','1.0'):continue
            value='#'+''.join(f'{x:02x}' for x in rgb);color_counts[value]+=1
            if source not in colors[value]:colors[value].append(source)
        for match in FONT.finditer(blob):
            stack=re.sub(r'\s*!important\s*$','',match[1].strip(),flags=re.I)
            if 'var(' in stack:continue
            for family in stack.split(','):
                family=family.strip().strip('"\'').strip()
                if family and len(family)<80 and family.lower() not in ('inherit','initial','unset','revert') and '$' not in family:
                    if source not in fonts[family]:fonts[family].append(source)
        for match in re.finditer(r'([^{}]{1,200})\{([^{}]{1,2000})\}',blob):
            selector,decl=match.groups()
            if re.search(r'body|button|h1|:root|\.btn|header|product',selector,re.I) and re.search(r'color\s*:|font-family\s*:|--[\w-]+\s*:',decl):
                evidence['css_rules'].append(dict(source=source,selector=selector.strip()[:160],declarations=decl.strip()[:700]))
    # Retain every observed literal for validation, while the prompt selects a
    # bounded palette. Less frequent values may still appear in supplied rules.
    evidence['colors']={k:dict(count=color_counts[k],sources=colors[k]) for k,_ in color_counts.most_common()}
    evidence['font_families']=dict(sorted(fonts.items()))
    evidence['css_rules']=evidence['css_rules'][:30]
    evidence['confidence']='css_values_observed_roles_inferred' if len(colors)>=2 and fonts else 'insufficient_evidence'
    if evidence['confidence']=='insufficient_evidence':evidence['failure']='INSUFFICIENT_EVIDENCE'
    atomic_write(directory/'capture.json',json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    return evidence
