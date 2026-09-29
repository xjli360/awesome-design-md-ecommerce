#!/usr/bin/env python3
"""Read back an expansion's evidence; exclude redirect aliases from its target."""
import argparse
import json
import shutil
from collections import Counter
from design_system import ROOT, atomic_write, canonical_url, load_sites, validate
from worker_claude import evidence_check

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('batch_id');p.add_argument('--reconcile-aliases',action='store_true');args=p.parse_args()
    path=ROOT/'_state/batches'/f'{args.batch_id}.json';state=json.loads(path.read_text())
    rows={r['slug']:r for r in load_sites()};base=set(state['baseline_slugs'])
    alias_path=ROOT/'data/url_aliases.json'
    identities=json.loads(alias_path.read_text()) if alias_path.exists() else {}
    observations=ROOT/'_state/alias_observations.json'
    if observations.exists():identities.update({k:v['canonical_target'] for k,v in json.loads(observations.read_text()).items()})
    def identity(url):
        key=canonical_url(url);seen=set()
        while key in identities:
            if key in seen:raise ValueError(f'URL alias cycle: {key}')
            seen.add(key);key=identities[key]
        return key
    holds_path=ROOT/'data/source_holds.json'
    holds=json.loads(holds_path.read_text()) if holds_path.exists() else {}
    covered={}
    for slug in rows:
        if slug in base:covered.setdefault(identity(rows[slug]['url']),slug)
    errors=[];aliases=[];valid=[]
    for slug,result in state['results'].items():
        if result['status']!='done':continue
        folder=ROOT/'design-md'/slug
        if slug in base or not (folder/'DESIGN.md').exists() or not (folder/'SOURCE.json').exists():
            errors.append(dict(slug=slug,error='missing/newness check'));continue
        source=json.loads((folder/'SOURCE.json').read_text());checked=validate((folder/'DESIGN.md').read_text(),rows[slug]['brand_name'])
        issues=checked['errors']
        if slug in holds and holds[slug].get('manual_review_required',True):issues.append('Source identity hold: '+holds[slug]['reason'])
        if checked['valid']:issues+=evidence_check(checked['data'],source)
        if source.get('batch_id')!=args.batch_id:issues.append('batch provenance mismatch')
        if issues:errors.append(dict(slug=slug,errors=issues));continue
        final=identity(source['final_url']);requested=identity(source['source_url'])
        target=covered.get(final) or covered.get(requested)
        if target:
            aliases.append(dict(slug=slug,target_slug=target,source_url=source['source_url'],target_url='https://'+identity(rows[target]['url'])))
        else:
            covered[requested]=slug;covered[final]=slug;valid.append(slug)
    if args.reconcile_aliases:
        if state['status']=='running':raise SystemExit('Wait for the original worker to exit before reconciling')
        ap=ROOT/'data/url_aliases.json';redirects=dict(identities)
        for alias in aliases:
            slug=alias['slug'];dest=ROOT/'_state/redirect_alias_outputs'/args.batch_id/slug
            dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists():raise SystemExit(f'Refusing to overwrite quarantine: {slug}')
            shutil.move(str(ROOT/'design-md'/slug),str(dest))
            state['results'][slug]={**alias,'status':'alias_existing'}
            if canonical_url(alias['source_url'])!=canonical_url(alias['target_url']):
                redirects[canonical_url(alias['source_url'])]=canonical_url(alias['target_url'])
        for error in errors:
            slug=error['slug'];folder=ROOT/'design-md'/slug
            if slug in base:raise SystemExit('Refusing to quarantine a baseline file')
            if folder.exists():
                dest=ROOT/'_state/rejected_source_outputs'/args.batch_id/slug
                dest.parent.mkdir(parents=True,exist_ok=True)
                if dest.exists():raise SystemExit(f'Refusing to overwrite source quarantine: {slug}')
                shutil.move(str(folder),str(dest))
            state['results'][slug]={'slug':slug,'status':'hold','reason':'SOURCE_REVIEW: '+json.dumps(error,ensure_ascii=False)}
        state['completed']=len(valid)
        if aliases or errors:
            state['status']='reviewed' if state.get('all_remaining') else 'needs_backfill'
            state.pop('verified_at',None);state.pop('verification',None)
        atomic_write(ap,json.dumps(redirects,indent=2)+'\n');atomic_write(path,json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    report=dict(batch_id=args.batch_id,valid_new_sites=len(valid),target=state['target'],aliases=aliases,errors=errors,slugs=valid)
    atomic_write(ROOT/'_state/batches'/f'{args.batch_id}-verification.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='slugs'},ensure_ascii=False,indent=2))
    return int(bool(errors) or bool(aliases) or (not state.get('all_remaining') and len(valid)!=state['target']))

if __name__=='__main__':raise SystemExit(main())
