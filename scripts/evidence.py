"""One admission policy for workers, indexes and public CI.

Published declaration excerpts are independently parseable. Local snapshots,
when available, additionally prove their membership and content hashes.
"""
import hashlib
import json
import re
from datetime import datetime,timezone,timedelta
from pathlib import Path
from urllib.parse import urlsplit
from css_values import color_literals,normalize_color,font_families,GENERIC_FONTS,style_leaves,property_key,resolve_local_variables,style_color_literals
from design_system import ROOT,BLOCKS,canonical_url,parse_document,validate
from extract_site import source_problem,Page

SHA=re.compile(r'^[0-9a-f]{64}$')

def valid_url(value):
    if not isinstance(value,str):return False
    try:
        p=urlsplit(value)
        return p.scheme in ('http','https') and bool(p.hostname) and not p.username and not p.password
    except ValueError:return False

def valid_date(value):
    try:
        d=datetime.fromisoformat(value.replace('Z','+00:00'))
        return d.tzinfo is not None and d<=datetime.now(timezone.utc)+timedelta(minutes=5)
    except (ValueError,TypeError,AttributeError):return False

def manual_hold(root,slug):
    p=root/'data/source_holds.json'
    h=json.loads(p.read_text()).get(slug) if p.exists() else None
    return h if h and h.get('manual_review_required',True) else None

def evidence_check(data,evidence):
    errors=[]
    if not isinstance(evidence,dict):return ['Source must be an object']
    palette={normalize_color(x) for x in evidence.get('colors',{})}
    allowed={x.casefold() for x in evidence.get('font_families',{})}
    problem=source_problem(evidence)
    if problem:errors.append('Invalid source page: '+problem)
    for block in BLOCKS:
        for path,value in style_leaves(data.get(block,{}),block):
            for literal,color in style_color_literals(path,value):
                if color not in palette and not (block!='colors' and color.endswith('00') and len(color)==9):
                    derived=evidence.get('derived_colors',{}).get(color)
                    if not (derived and derived.get('status')=='proposed_opacity' and color[:7] in palette and len(color)==9 and derived.get('base')==color[:7]):
                        errors.append(f'Unobserved color at {path}: {literal}')
            if property_key(path.rsplit('.',1)[-1])=='fontfamily' and isinstance(value,str):
                stack={f.casefold() for f in font_families(value)}
                if not stack&allowed:errors.append('No observed family at '+path)
                if stack-allowed-GENERIC_FONTS:errors.append('Unobserved family at '+path+': '+str(sorted(stack-allowed-GENERIC_FONTS)))
    return errors

def required_values(data):
    colors=set();fonts=set()
    for b in BLOCKS:
        for path,value in style_leaves(data.get(b,{}),b):
            colors.update(c for _,c in style_color_literals(path,value))
            if property_key(path.rsplit('.',1)[-1])=='fontfamily':fonts.update(font_families(value))
    return colors,fonts

def proof_matches(kind,value,proof):
    if not isinstance(proof,dict) or not isinstance(proof.get('declaration'),str) or not isinstance(proof.get('property'),str):return False
    bindings=proof.get('bindings',{})
    if not isinstance(bindings,dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in bindings.items()):return False
    if kind=='colors':return value in {v for _,v in color_literals(resolve_local_variables(proof['declaration'],proof.get('bindings',{})))}
    return value.casefold() in {f.casefold() for f in font_families(proof['declaration'])} and 'font' in proof['property'] and ('family' in proof['property'] or proof['property']=='font')

def source_errors(data,source,row,root=ROOT,require_snapshots=False):
    errors=[]
    if not isinstance(source,dict):return ['Missing SOURCE.json']
    for key in ('colors','font_families','tokens','observations','derived_colors'):
        if not isinstance(source.get(key,{}),dict):errors.append('Invalid source object: '+key)
    if not isinstance(source.get('screenshots',[]),list):errors.append('Invalid screenshots')
    if errors:return errors
    for color,item in source.get('colors',{}).items():
        if not isinstance(item,dict) or not isinstance(item.get('sources'),list):errors.append('Invalid color observation: '+str(color))
    for font,urls in source.get('font_families',{}).items():
        if not isinstance(urls,list):errors.append('Invalid font sources: '+str(font))
    for kind in ('colors','font_families'):
        if not isinstance(source.get('observations',{}).get(kind,{}),dict):errors.append('Invalid proof mapping: '+kind)
    for color,item in source.get('derived_colors',{}).items():
        if not isinstance(color,str) or len(color)!=9 or normalize_color(color)!=color or not isinstance(item,dict) or item.get('base')!=color[:7] or item.get('status')!='proposed_opacity' or item.get('alpha')!=int(color[-2:],16)/255:errors.append('Invalid opacity proposal: '+str(color))
    if errors:return errors
    for key in ('source_url','final_url'):
        if not valid_url(source.get(key)):errors.append('Invalid source URL: '+key)
    if valid_url(source.get('source_url')) and canonical_url(source['source_url'])!=canonical_url(row['url']):errors.append('Source URL differs from site metadata')
    if not valid_date(source.get('captured_at')):errors.append('Invalid capture date')
    if source.get('schema_version')!=2:errors.append('Source requires schema_version 2')
    if source.get('confidence')!='css_values_observed_roles_inferred':errors.append('Unsupported verified source confidence')
    for key in ('source_url','captured_at','evidence_status'):
        expected=source.get('confidence' if key=='evidence_status' else key)
        if data.get(key)!=expected:errors.append('Document/source mismatch: '+key)
    for key,expected in {'quality_tier':'css_reference','usage_scope':'style_reference_only','layout_status':'proposed_not_measured','recreation_verified':False}.items():
        if data.get(key)!=expected:errors.append('Invalid usage/measurement claim: '+key)
    pages=source.get('pages')
    if not isinstance(pages,list) or not pages:return errors+['Missing source pages']
    page_map={};raw={}
    for item in pages+source.get('screenshots',[]):
        if not isinstance(item,dict):errors.append('Invalid page record');continue
        name=item.get('snapshot','');digest=item.get('sha256','')
        if not isinstance(name,str) or Path(name).name!=name or name in ('','.', '..') or '\\' in name or not isinstance(digest,str) or not SHA.fullmatch(digest):errors.append('Invalid snapshot metadata');continue
        if name in page_map:errors.append('Duplicate snapshot: '+name)
        page_map[name]=item
        if item in pages and (not valid_url(item.get('url')) or not valid_url(item.get('final_url'))):errors.append('Invalid page URL')
        if item in pages and not (isinstance(item.get('http_status'),int) and 200<=item['http_status']<300 or item.get('http_status') is None and 'derived-from=' in item.get('content_type','')):errors.append('Unsuccessful source page: '+name)
        snapshot=root/'_state/evidence'/row['slug']/name
        if snapshot.is_file():
            content=snapshot.read_bytes()
            if hashlib.sha256(content).hexdigest()!=digest:errors.append('Snapshot hash mismatch: '+name)
            else:raw[name]=content.decode('utf-8','replace') if not name.endswith('.png') else ''
        elif require_snapshots:errors.append('Missing raw snapshot: '+name)
    if isinstance(pages[0],dict) and pages[0].get('final_url')!=source.get('final_url'):errors.append('Landing page URL differs from final_url')
    tokens=source.get('tokens');required={b+'.'+str(k) for b in BLOCKS for k in data.get(b,{})}
    if not isinstance(tokens,dict) or set(tokens)!=required:errors.append('Token evidence mapping is incomplete or stale')
    else:
        for key,item in tokens.items():
            if not isinstance(item,dict):errors.append('Invalid token evidence: '+key);continue
            b,k=key.split('.',1)
            if item.get('value')!=data[b][k]:errors.append('Token value/evidence mismatch: '+key)
            if b=='colors' and (item.get('role_status')!='inferred' or item.get('value_status')!=('observed_in_css' if normalize_color(data[b][k]) in source.get('colors',{}) else 'derived_opacity')):errors.append('Unsubstantiated color role: '+key)
            if b in ('spacing','rounded','components') and item.get('status')!='inferred':errors.append('Unmeasured token promoted: '+key)
            if b=='typography' and item.get('measurements_status')!='inferred':errors.append('Unmeasured typography promoted: '+key)
    observations=source.get('observations',{})
    for kind,values in [('colors',source.get('colors',{})),('font_families',source.get('font_families',{}))]:
        if not isinstance(values,dict) or not values:errors.append('Missing observed '+kind);continue
        for value in values:
            proof=observations.get(kind,{}).get(value) if isinstance(observations,dict) else None
            if not proof_matches(kind,value,proof):errors.append('Missing/mismatched declaration proof: '+value);continue
            item=page_map.get(proof.get('snapshot'))
            if proof.get('url') not in (source[kind][value].get('sources',[]) if kind=='colors' else source[kind][value]):errors.append('Observation/source URL mismatch: '+value)
            if not item or proof.get('sha256')!=item.get('sha256') or proof.get('url')!=item.get('final_url'):errors.append('Declaration proof has no matching page: '+value)
            # Membership in the original declaration is audited by verify_source_proofs,
            # rather than a substring search that ignores CSS tokenization/escaping.
    if not errors:errors.extend(evidence_check(data,source))
    return sorted(set(errors))

def token_records(data,source):
    records={}
    for block in BLOCKS:
        for key,value in data[block].items():
            item={'value':value}
            if block=='colors':
                color=normalize_color(value);base=source.get('derived_colors',{}).get(color,{}).get('base',color)
                item.update(value_status='observed_in_css' if color in source['colors'] else 'derived_opacity',role_status='inferred',sources=source['colors'][base]['sources'])
            elif block=='typography':item.update(font_family_status='observed_family_with_fallbacks',measurements_status='inferred')
            else:item['status']='inferred'
            records[block+'.'+str(key)]=item
    return records

def assess(row,text,source,root=ROOT,legacy=None,require_snapshots=False):
    checked=validate(text,row['brand_name']);errors=list(checked['errors'])
    hold=manual_hold(root,row['slug'])
    if hold:errors.append('Manual source HOLD: '+hold.get('reason','review required'))
    legacy=legacy if legacy is not None else (json.loads((root/'data/legacy_documents.json').read_text()).get('documents',{}) if (root/'data/legacy_documents.json').exists() else {})
    historical=legacy.get(row['slug'])
    legacy_match=historical and historical.get('sha256')==hashlib.sha256(text.encode()).hexdigest()
    if legacy_match:
        if checked['data'].get('evidence_status') not in ('historical_unverified','historical_partial_css_evidence'):errors.append('Historical document claims verified evidence')
        if canonical_url(checked['data'].get('source_url',''))!=canonical_url(row['url']):errors.append('Historical source URL differs from metadata')
        tier='historical_archive'
    else:
        if checked['valid']:errors+=source_errors(checked['data'],source,row,root,require_snapshots)
        tier='css_reference'
    return {'format_valid':checked['valid'],'admitted':not errors,'evidence_backed':not errors and tier=='css_reference','quality_tier':tier if not errors else 'needs_review','errors':sorted(set(errors)),'data':checked['data']}
