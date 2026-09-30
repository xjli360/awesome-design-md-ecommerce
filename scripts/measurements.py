"""Read-only component measurements. Screenshot capture is not reconstruction QA."""
import hashlib
import json
from design_system import atomic_write
VIEWPORTS=[{'name':'desktop','width':1440,'height':1000},{'name':'tablet','width':768,'height':1024},{'name':'mobile','width':390,'height':844}]
SAMPLE=r'''() => {
 const props=['color','background-color','font-family','font-size','font-weight','line-height','letter-spacing','padding-top','padding-right','padding-bottom','padding-left','margin-top','margin-bottom','border-radius','border-top-width','border-top-color','display','gap','row-gap','column-gap','max-width'];
 const isWidget=e=>{for(let n=e;n;n=n.parentElement){if(n.tagName!=='BODY'&&n.tagName!=='HTML'&&/cookie|consent|onetrust|judge|jdgm|trustpilot/i.test(n.id+' '+String(n.className)))return true}return false};
 const visible=e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'&&!isWidget(e)};
 const locator=e=>{let a=[];for(let n=e;n&&n.nodeType===1;n=n.parentElement){if(n.id){a.unshift('#'+CSS.escape(n.id));break}let i=1;for(let p=n.previousElementSibling;p;p=p.previousElementSibling)if(p.tagName===n.tagName)i++;a.unshift(n.tagName.toLowerCase()+':nth-of-type('+i+')')}return a.join(' > ')};
 const groups=[['body','body'],['header','header'],['navigation','header nav, nav'],['heading','main h1, h1'],['section-heading','main h2'],['body-copy','main p'],['candidate-cta','main button, main a'],['product-card','main [class*="product-card"], main [class*="productCard"], main article'],['footer','footer']];
 const samples=[];let used=new Set();
 for(const [role,query] of groups){let candidates=[...document.querySelectorAll(query)].filter(visible);
 if(role==='candidate-cta')candidates=candidates.filter(e=>/shop|buy|add|cart|discover|collection|learn/i.test((e.innerText||'').trim())&&(e.innerText||'').length<90);
 for(const e of candidates.slice(0,role==='candidate-cta'?2:1)){if(used.has(e))continue;used.add(e);const r=e.getBoundingClientRect(),cs=getComputedStyle(e),hit=document.elementFromPoint(Math.max(0,Math.min(innerWidth-1,r.x+r.width/2)),Math.max(0,Math.min(innerHeight-1,r.y+r.height/2)));samples.push({role,selector:locator(e),label:(e.getAttribute('aria-label')||e.innerText||'').trim().slice(0,60),box:{x:r.x,y:r.y,width:r.width,height:r.height},styles:Object.fromEntries(props.map(k=>[k,cs.getPropertyValue(k)])),occluded:!!hit&&!e.contains(hit)&&hit!==e});}}
 return {samples,assets:[...document.images].filter(e=>e.currentSrc.startsWith('http')).slice(0,12).map(e=>({url:e.currentSrc,alt:e.alt.slice(0,60),width:e.naturalWidth,height:e.naturalHeight})),document_width:document.documentElement.scrollWidth};
}'''

async def collect(page,directory):
    result={'schema_version':1,'source_url':page.url,'method':'browser-computed-components','viewports':[],'visual_validation':{'status':'not_performed','reason':'No implementation generated from DESIGN.md has been compared with the reference.'}}
    screenshots=[]
    for viewport in VIEWPORTS:
        await page.set_viewport_size({k:viewport[k] for k in ('width','height')})
        await page.evaluate('() => window.scrollTo(0,0)')
        await page.evaluate('() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))')
        observed=await page.evaluate(SAMPLE)
        observed.update(viewport=viewport,states={'initial':'observed','hover':'not_measured','focus':'not_measured','menu_open':'not_measured'})
        cta=next((x for x in observed['samples'] if x['role']=='candidate-cta' and not x['occluded'] and x['box']['y']>=0 and x['box']['y']+x['box']['height']<=viewport['height']),None)
        if cta:
            target=page.locator(cta['selector'])
            for state in ('hover','focus'):
                try:
                    await getattr(target,state)(timeout=2000)
                    observed['states'][state]={'selector':cta['selector'],'styles':await target.evaluate("e => {const s=getComputedStyle(e); return {color:s.color,backgroundColor:s.backgroundColor,borderColor:s.borderColor,outline:s.outline}}")}
                except Exception:observed['states'][state]='unavailable'
            await page.evaluate('() => document.activeElement?.blur()');await page.mouse.move(0,0)
        name='viewport-'+viewport['name']+'.png'
        try:
            await page.screenshot(path=str(directory/name),timeout=5000)
            digest=hashlib.sha256((directory/name).read_bytes()).hexdigest();screenshots.append({'snapshot':name,'sha256':digest});observed['screenshot']={'snapshot':name,'sha256':digest}
        except Exception:observed['screenshot']=None
        result['viewports'].append(observed)
    atomic_write(directory/'measurements.json',json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return result,screenshots
