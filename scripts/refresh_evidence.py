#!/usr/bin/env python3
"""Recapture existing entries without changing token values or asserting fidelity."""
import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from design_system import ROOT, BLOCKS, atomic_write, attach_evidence, load_sites, parse_document
from extract_site import capture, norm_hex

def refresh(row):
    path=ROOT/'design-md'/row['slug']/'DESIGN.md'
    data=parse_document(path.read_text()); evidence=capture(row); tokens={};observed=0;total=0
    for block in BLOCKS:
        for key,value in data[block].items():
            label=f'{block}.{key}'
            if block=='colors':
                total+=1
                matched=isinstance(value,str) and value.startswith('#') and norm_hex(value) in evidence['colors']
                observed+=matched
                tokens[label]=dict(value_status='observed_in_css' if matched else 'unverified',role_status='inferred')
                if matched:tokens[label]['sources']=evidence['colors'][norm_hex(value)]['sources']
            elif block=='typography':
                stack={x.strip().strip('"\'').casefold() for x in str(value['fontFamily']).split(',')}
                seen=stack & {x.casefold() for x in evidence['font_families']}
                tokens[label]=dict(font_family_status='partial_observed_match' if seen else 'unverified',measurements_status='unverified')
            else:tokens[label]=dict(status='unverified')
    evidence.update(schema_version=1,design_origin='historical',tokens=tokens,confidence='historical_partial_css_evidence' if observed else 'historical_unverified',observed_color_tokens=observed,total_color_tokens=total)
    atomic_write(path.parent/'SOURCE.json',json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    atomic_write(path,attach_evidence(path.read_text(),evidence))
    return dict(slug=row['slug'],observed_color_tokens=observed,total_color_tokens=total,status=evidence['confidence'],capture_failure=evidence.get('failure'))

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('slugs',nargs='+');args=p.parse_args()
    rows={r['slug']:r for r in load_sites()};results=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures={pool.submit(refresh,rows[s]):s for s in args.slugs}
        for future in as_completed(futures):
            result=future.result();results.append(result);print(json.dumps(result),flush=True)
    path=ROOT/'_state/evidence_refresh.json'
    prior=json.loads(path.read_text()) if path.exists() else []
    merged={r['slug']:r for r in prior}
    merged.update({r['slug']:r for r in results})
    atomic_write(path,json.dumps(list(merged.values()),indent=2)+'\n')

if __name__=='__main__':main()
