#!/usr/bin/env python3
"""Read-only recovery capture in fresh anonymous browser contexts.

Install optional dependencies with `uv run --with pyyaml --with playwright`.
Input is a JSON list of site metadata. No logins, challenge solving, clicks,
form submissions, or existing browser profiles are used.
"""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone
from playwright.async_api import async_playwright
from design_system import atomic_write
from extract_site import capture, source_problem, BLOCKED
from capture_state import begin, finish
from measurements import collect as collect_measurements

STYLES = """() => {
 const props=['color','background-color','border-top-color','font-family'];
 const nodes=[...document.querySelectorAll('body,header,nav,main,footer,h1,h2,h3,p,a,button,input,label,section,article')]
   .filter(e=>{const r=e.getBoundingClientRect();const s=getComputedStyle(e);return r.width&&r.height&&s.visibility!=='hidden'&&s.display!=='none'}).slice(0,500);
 return nodes.map((e,i)=>`.sample-${i}-${e.tagName.toLowerCase()}{${props.map(p=>p+':'+getComputedStyle(e).getPropertyValue(p)).join(';')}}`).join('\\n');
}"""

async def one(browser,site,root):
    directory=root/'_state/evidence'/site['slug'];directory.mkdir(parents=True,exist_ok=True)
    attempt=begin(directory,site['url'])
    context=await browser.new_context(viewport={'width':1440,'height':1000})
    page=await context.new_page();responses=[]
    page.on('response',lambda response: responses.append(response) if response.request.resource_type=='stylesheet' and response.ok else None)
    try:
        response=await page.goto(site['url'],wait_until='domcontentloaded',timeout=35000)
        try:await page.wait_for_load_state('networkidle',timeout=6000)
        except Exception:pass
        title=await page.title();body=await page.locator('body').inner_text(timeout=3000)
        html=await page.content();final=page.url
        problem=source_problem({'title':title,'final_url':final,'page_text_excerpt':body})
        if not problem and len(body.strip())<40:problem='RENDERED_EMPTY_BODY'
        if problem or BLOCKED.search(html[:150000]) or not response or not response.ok:
            result={'slug':site['slug'],'status':'hold','reason':problem or 'HTTP_OR_CHALLENGE','source_url':site['url'],'final_url':final,'http_status':response.status if response else None,'title':title,'checked_at':datetime.now(timezone.utc).isoformat()}
            finish(directory,attempt,reason=result['reason'])
            atomic_write(directory/'browser-result.json',json.dumps(result,indent=2)+'\n')
            return result
        styles=[];seen=set()
        for resource in responses[:24]:
            if resource.url in seen:continue
            seen.add(resource.url)
            try:content=await resource.text()
            except Exception:continue
            if len(content)>2000000:continue
            styles.append(dict(url=resource.url,final_url=resource.url,status=resource.status,content_type='text/css',body=content))
        computed=await page.evaluate(STYLES)
        styles.append(dict(url=final+'#computed-style-snapshot',final_url=final+'#computed-style-snapshot',status=None,content_type='text/css; derived-from=getComputedStyle',body=computed))
        html_response=dict(ok=True,status=response.status,url=site['url'],final_url=final,content_type='text/html; rendered-dom',body=html)
        evidence=await asyncio.to_thread(capture,site,root,html_response,styles)
        evidence['title']=title[:250];evidence['page_text_excerpt']=body[:10000]
        evidence['viewport']={'width':1440,'height':1000}
        screenshot=directory/'desktop.png'
        try:
            await page.screenshot(path=str(screenshot),timeout=5000)
            evidence['screenshots']=[dict(snapshot='desktop.png',sha256=hashlib.sha256(screenshot.read_bytes()).hexdigest())]
        except Exception:pass
        if not evidence.get('failure'):
            measured,images=await collect_measurements(page,directory)
            evidence['measurements']=measured
            evidence.setdefault('screenshots',[]).extend(images)
        finish(directory,attempt,evidence,evidence.get('failure'))
        return {'slug':site['slug'],'status':'hold' if evidence.get('failure') else 'captured','reason':evidence.get('failure'),'title':title[:200],'final_url':final,'colors':len(evidence['colors']),'fonts':len(evidence['font_families'])}
    except Exception as e:
        result={'slug':site['slug'],'status':'hold','reason':str(e).split('Call log:')[0][:500],'source_url':site['url'],'checked_at':datetime.now(timezone.utc).isoformat()}
        finish(directory,attempt,reason=result['reason'])
        atomic_write(directory/'browser-result.json',json.dumps(result,indent=2)+'\n')
        return result
    finally:await context.close()

async def main(args):
    rows=json.loads(args.input.read_text());out=args.root/'results.json'
    results=json.loads(out.read_text()) if out.exists() else {}
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,**({'executable_path':args.browser_executable} if args.browser_executable else {}))
        limit=asyncio.Semaphore(3)
        async def run(site):
            if site['slug'] in results and not args.retry:return
            async with limit:
                result=await one(browser,site,args.root);results[site['slug']]=result
                atomic_write(out,json.dumps(results,ensure_ascii=False,indent=2)+'\n')
                print(json.dumps(result,ensure_ascii=False),flush=True)
        await asyncio.gather(*(run(site) for site in rows));await browser.close()

if __name__=='__main__':
    p=argparse.ArgumentParser(__doc__);p.add_argument('input',type=Path);p.add_argument('--root',type=Path,required=True);p.add_argument('--browser-executable');p.add_argument('--retry',action='store_true')
    asyncio.run(main(p.parse_args()))
