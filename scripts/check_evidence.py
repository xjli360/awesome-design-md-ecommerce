#!/usr/bin/env python3
"""Validate public SOURCE.json claims and available local snapshot hashes."""
import hashlib
import json
from design_system import ROOT, load_sites, validate
from worker_claude import evidence_check

def main():
    names={r['slug']:r['brand_name'] for r in load_sites()}; errors=[];checked=0;snapshots=0;missing_snapshots=0
    for path in sorted((ROOT/'design-md').glob('*/SOURCE.json')):
        slug=path.parent.name;source=json.loads(path.read_text());checked+=1
        result=validate((path.parent/'DESIGN.md').read_text(),names.get(slug))
        if not result['valid']:errors.append(dict(slug=slug,errors=result['errors']));continue
        for key in ('source_url','final_url','captured_at','confidence','pages','tokens'):
            if key not in source:errors.append(dict(slug=slug,error=f'Missing provenance: {key}'))
        if source.get('design_origin')!='historical':
            failures=evidence_check(result['data'],source)
            if failures:errors.append(dict(slug=slug,errors=failures))
            if source.get('failure'):errors.append(dict(slug=slug,error='New file has failed capture'))
        for page in source.get('pages',[])+source.get('screenshots',[]):
            name=page.get('snapshot','')
            if not name or '/' in name or '\\' in name or name in ('.','..'):
                errors.append(dict(slug=slug,error='Unsafe snapshot name'));continue
            snapshot=ROOT/'_state/evidence'/slug/name
            if snapshot.exists():
                snapshots+=1
                if hashlib.sha256(snapshot.read_bytes()).hexdigest()!=page['sha256']:
                    errors.append(dict(slug=slug,error=f'Snapshot hash mismatch: {name}'))
            else:missing_snapshots+=1
    summary=dict(source_files=checked,local_snapshots_verified=snapshots,local_snapshots_unavailable=missing_snapshots,errors=errors)
    print(json.dumps(summary,ensure_ascii=False,indent=2));return int(bool(errors))

if __name__=='__main__':raise SystemExit(main())
