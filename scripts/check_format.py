#!/usr/bin/env python3
"""Strict DESIGN.md audit. Invalid YAML/schema/references exit nonzero."""
import argparse
import json
from pathlib import Path
from design_system import ROOT, atomic_write, load_sites, validate

def audit_file(path, expected_name=None):
    r = validate(path.read_text(encoding='utf-8'), expected_name)
    return dict(slug=path.parent.name, valid=r['valid'], errors=r['errors'], warnings=r['warnings'])

def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('paths', nargs='*')
    parser.add_argument('--report', type=Path, default=ROOT / '_state/quality_format.json')
    args = parser.parse_args()
    names = {r['slug']: r['brand_name'] for r in load_sites()}
    files = [Path(p) for p in args.paths] or sorted((ROOT / 'design-md').glob('*/DESIGN.md'))
    results = [audit_file(p, names.get(p.parent.name)) for p in files]
    summary = dict(audited=len(results), passing=sum(r['valid'] for r in results), failing=sum(not r['valid'] for r in results), warnings=sum(bool(r['warnings']) for r in results))
    atomic_write(args.report, json.dumps(dict(summary=summary, files=results), ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({**summary, 'report': str(args.report)}))
    return 1 if summary['failing'] or not results else 0

if __name__ == '__main__':
    raise SystemExit(main())
