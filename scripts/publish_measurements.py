#!/usr/bin/env python3
"""Publish selected current captures as measured references, preserving legacy tokens."""
import argparse,json,shutil
from pathlib import Path
from design_system import ROOT,load_sites,atomic_write
from capture_state import load_capture
from check_measurements import validate_measurements
from measurement_document import render

def publish(row,source,folder,capture_directory):
    data={**source['measurements'],'requested_url':row['url'],'captured_at':source['captured_at'],'capture_id':source['capture_id'],'landing_page_sha256':source['pages'][0]['sha256']}
    errors=validate_measurements(data,row)
    if errors:raise ValueError(errors)
    for view in data['viewports']:
        shot=view['screenshot'];target=folder/'evidence'/shot['snapshot'];target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(capture_directory/shot['snapshot'],target);shot['public_path']='evidence/'+shot['snapshot']
    atomic_write(folder/'MEASUREMENTS.json',json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    atomic_write(folder/'MEASURED.md',render(data,row))

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('capture_root',type=Path);a=p.parse_args();rows={r['slug']:r for r in load_sites()};out=[]
    approvals=json.loads((a.capture_root/'brand-review.json').read_text())
    for slug,result in json.loads((a.capture_root/'results.json').read_text()).items():
        if result['status']!='captured' or slug not in approvals:continue
        source=load_capture(a.capture_root/'_state/evidence'/slug,rows[slug]['url'])
        if approvals[slug].get('capture_id')!=source.get('capture_id') or approvals[slug].get('decision')!='matched_brand':raise ValueError('Brand review does not match capture')
        source['measurements']['brand_review']=approvals[slug]
        publish(rows[slug],source,ROOT/'design-md'/slug,a.capture_root/'_state/evidence'/slug);out.append(slug)
    print(json.dumps({'published_measured_references':len(out),'slugs':out},indent=2))
if __name__=='__main__':main()
