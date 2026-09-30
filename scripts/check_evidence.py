#!/usr/bin/env python3
"""Validate every document's admission, provenance, declaration proofs and raw hashes."""
import argparse
import json
import subprocess
from pathlib import Path
from design_system import ROOT,load_sites
from evidence import assess
from source_proofs import verify_source_proofs

def audit(root=ROOT,require_snapshots=False):
    rows={r['slug']:r for r in load_sites(root)};errors=[];checked=0;legacy_count=0;raw_count=0;missing=0
    lp=root/'data/legacy_documents.json';legacy=json.loads(lp.read_text()).get('documents',{}) if lp.exists() else {}
    for path in sorted((root/'design-md').glob('*/DESIGN.md')):
        slug=path.parent.name
        if slug not in rows:errors.append({'slug':slug,'errors':['Document has no site metadata']});continue
        sp=path.parent/'SOURCE.json';source=json.loads(sp.read_text()) if sp.exists() else None
        result=assess(rows[slug],path.read_text(),source,root,legacy,require_snapshots)
        if result['errors']:errors.append({'slug':slug,'errors':result['errors']});continue
        if result['quality_tier']=='historical_archive':legacy_count+=1;continue
        checked+=1
        proof_errors=verify_source_proofs(source,root/'_state/evidence'/slug)
        if proof_errors:errors.append({'slug':slug,'errors':proof_errors})
        for page in source.get('pages',[])+source.get('screenshots',[]):
            if (root/'_state/evidence'/slug/page['snapshot']).exists():raw_count+=1
            else:missing+=1
    for p in (root/'design-md').glob('*/SOURCE.json'):
        if not (p.parent/'DESIGN.md').exists():errors.append({'slug':p.parent.name,'errors':['Orphan SOURCE.json']})
    return {'source_files':checked,'frozen_historical_documents':legacy_count,'local_snapshots_verified':raw_count,'local_snapshots_unavailable':missing,'errors':errors}

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('--require-snapshots',action='store_true');p.add_argument('--base-ref');args=p.parse_args()
    if args.base_ref and set(args.base_ref)!={'0'}:
        subprocess.run(['git','rev-parse','--verify',args.base_ref+'^{commit}'],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
        old=subprocess.run(['git','show',args.base_ref+':data/legacy_documents.json'],cwd=ROOT,capture_output=True)
        if old.returncode==0 and old.stdout!=(ROOT/'data/legacy_documents.json').read_bytes():raise SystemExit('Frozen historical exemptions cannot be extended or changed')
    result=audit(require_snapshots=args.require_snapshots);print(json.dumps(result,ensure_ascii=False,indent=2));return int(bool(result['errors']))

if __name__=='__main__':raise SystemExit(main())
