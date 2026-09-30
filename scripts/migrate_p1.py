#!/usr/bin/env python3
"""One-time, locally evidenced migration. Never invent observations or promote legacy tokens."""
import hashlib,json,re,sys
from pathlib import Path
from datetime import datetime,timezone
from design_system import ROOT,atomic_write,parse_document,load_sites
from css_values import normalize_color,GENERIC_FONTS
from evidence import required_values,token_records
from source_proofs import collect_proofs

POLICY={'historical_archive':('inspiration_only','Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.'),'css_reference':('style_reference_only','Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.')}

def annotate(text,tier):
    scope,note=POLICY[tier]
    for key,value in [('quality_tier',tier),('usage_scope',scope),('layout_status','proposed_not_measured'),('recreation_verified',False)]:
        line=key+': '+json.dumps(value)
        if re.search('^'+key+':',text,re.M):text=re.sub('^'+key+':.*$',lambda _:line,text,flags=re.M)
        else:text=text.replace('description:',line+'\ndescription:',1)
    text=re.sub(r'^- \*\*Agent usage policy:\*\*.*\n','',text,flags=re.M)
    text=text.replace('## Known Gaps\n','## Known Gaps\n\n- **Agent usage policy:** '+note+'\n',1)
    return text

def main():
    root=ROOT;legacy={};changes=[];failures=[];rows={r['slug']:r for r in load_sites()}
    baseline_path=root/'_state/p1-pre-migration.json'
    if not baseline_path.exists():atomic_write(baseline_path,json.dumps({p.parent.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'design-md').glob('*/DESIGN.md')},indent=2)+'\n')
    baseline=json.loads(baseline_path.read_text())
    for path in sorted((root/'design-md').glob('*/DESIGN.md')):
        slug=path.parent.name;sp=path.parent/'SOURCE.json';source=json.loads(sp.read_text()) if sp.exists() else None
        historical=not source or source.get('design_origin')=='historical'
        content=annotate(path.read_text(),'historical_archive' if historical else 'css_reference')
        if historical:
            atomic_write(path,content);legacy[slug]={'sha256':hashlib.sha256(content.encode()).hexdigest(),'pre_policy_sha256':baseline[slug],'reason':'Pre-existing unverified or partially verified historical reference; excluded from recommendations.'};continue
        data=parse_document(content)
        if source.get('schema_version')==2 and all(source.get('tokens',{}).get(b+'.'+str(k),{}).get('value')==v for b in ('colors','typography','rounded','spacing','components') for k,v in data[b].items()):
            atomic_write(path,content);changes.append(slug);continue
        colors,fonts=required_values(data)
        needed_fonts={f for f in fonts if f.casefold() not in GENERIC_FONTS or f in source.get('font_families',{})}
        # Search exact used values and opaque bases for explicitly proposed alpha derivatives.
        needed_colors=colors|{c[:7] for c in colors if len(c)==9}
        proofs=collect_proofs(source,root/'_state/evidence'/slug,needed_colors,needed_fonts)
        observed=set(proofs['colors']);derived={};missing=[]
        for color in colors-observed:
            if len(color)==9 and color[:7] in observed:derived[color]={'base':color[:7],'status':'proposed_opacity','alpha':int(color[-2:],16)/255}
            elif len(color)==9 and color.endswith('00'):pass
            else:missing.append(color)
        missing_fonts=needed_fonts-set(proofs['font_families'])
        if missing or missing_fonts:
            failures.append({'slug':slug,'colors':sorted(missing),'fonts':sorted(missing_fonts)});continue
        source['schema_version']=2;source['observations']=proofs
        source['colors']={c:{'count':source.get('colors',{}).get(c,{}).get('count',1),'sources':[p['url']]} for c,p in proofs['colors'].items()}
        source['font_families']={f:[p['url']] for f,p in proofs['font_families'].items()}
        if derived:source['derived_colors']=derived
        source['tokens']=token_records(data,source)
        source['layout_status']='proposed_not_measured';source['recreation_verified']=False
        atomic_write(sp,json.dumps(source,ensure_ascii=False,indent=2)+'\n');atomic_write(path,content);changes.append(slug)
        if len(changes)%50==0:print('migrated',len(changes),flush=True)
    atomic_write(root/'data/legacy_documents.json',json.dumps({'schema_version':1,'baseline_commit':'a548c451ef8bc25f1f1d4f6c566223d3daf9a0cf','policy':'Frozen archive exemptions; no additions or silent hash changes. Updated historical tokens require new evidence.','documents':legacy},indent=2)+'\n')
    result={'historical_archive':len(legacy),'source_migrations':len(changes),'failures':failures}
    atomic_write(root/'_state/p1-migration-report.json',json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
    return int(bool(failures))

if __name__=='__main__':raise SystemExit(main())
