#!/usr/bin/env python3
"""Find measured/component or CSS references; historical drafts require opt-in."""
import argparse,json
from design_system import ROOT

def select(manifest,query='',include_historical=False):
    results=[]
    for row in manifest['sites']:
        if row.get('alias_of') or not row.get('admitted') or row.get('coverage_status')=='source_hold':continue
        if query.casefold() not in (' '.join([row['brand_name'],row['slug'],*row['categories']])).casefold():continue
        target=row.get('recommended_reference')
        if not target and include_historical and row.get('admitted'):target='design-md/'+row['slug']+'/DESIGN.md'
        if target:results.append({'brand':row['brand_name'],'category':row['category'],'reference':target,'tier':'measured_components' if target.endswith('/MEASURED.md') else row['quality_tier'],'recreation_verified':False})
    return sorted(results,key=lambda r:(r['tier']!='measured_components',r['brand'].casefold()))

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('query',nargs='?',default='');p.add_argument('--include-historical',action='store_true');a=p.parse_args()
    print(json.dumps(select(json.loads((ROOT/'data/manifest.json').read_text()),a.query,a.include_historical),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
