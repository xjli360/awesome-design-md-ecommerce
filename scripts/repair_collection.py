#!/usr/bin/env python3
"""Repair deterministic serialization defects, validating before each atomic write."""
import argparse
import json
from design_system import ROOT, atomic_write, load_sites, repair_syntax, validate

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('--apply',action='store_true');args=p.parse_args()
    changed=[]; failed=[]
    for row in load_sites():
        path=ROOT/'design-md'/row['slug']/'DESIGN.md'
        if not path.exists():continue
        text=path.read_text(); before=validate(text,row['brand_name'])
        if before['valid']:continue
        fixed=repair_syntax(text,row['brand_name'])
        if row['slug'] in ('mott-and-bow','rylee-cru'):
            fixed=fixed.replace('padding: "{spacing.none}"','padding: 0px')
        if row['slug']=='staber':
            fixed=fixed.replace('#e8a c2a','#e8ac2a')
        after=validate(fixed,row['brand_name'])
        if not after['valid']:
            failed.append(dict(slug=row['slug'],errors=after['errors']));continue
        changed.append(dict(slug=row['slug'],old_errors=before['errors']))
        if args.apply:atomic_write(path,fixed)
    report=dict(applied=args.apply,changed=len(changed),failed=len(failed),changes=changed,unresolved=failed)
    atomic_write(ROOT/'_state/repair_report.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('applied','changed','failed','unresolved')},ensure_ascii=False,indent=2))
    return int(bool(failed))

if __name__=='__main__':raise SystemExit(main())
