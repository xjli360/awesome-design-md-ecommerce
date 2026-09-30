#!/usr/bin/env python3
"""Validate versioned component measurements, without claiming whole-site fidelity."""
import json,math,hashlib
from pathlib import Path
from design_system import ROOT,load_sites,canonical_url
from evidence import valid_url,valid_date,SHA
from measurement_document import render

def validate_measurements(data,row,directory=None):
    errors=[]
    if data.get('schema_version')!=1:errors.append('Invalid measurements schema')
    if not valid_url(data.get('requested_url')) or canonical_url(data.get('requested_url',''))!=canonical_url(row['url']):errors.append('Measurement URL differs from site metadata')
    if not valid_url(data.get('source_url')) or not valid_date(data.get('captured_at')):errors.append('Missing measurement provenance')
    if data.get('visual_validation',{}).get('status')!='not_performed':errors.append('Whole-site visual validation is not established by measurements')
    review=data.get('brand_review',{})
    if review.get('decision')!='matched_brand' or review.get('expected_brand')!=row['brand_name'] or review.get('capture_id')!=data.get('capture_id') or review.get('final_url')!=data.get('source_url'):errors.append('Missing/mismatched brand review')
    views=data.get('viewports',[])
    if len(views)!=3 or {v.get('viewport',{}).get('name') for v in views}!={'desktop','tablet','mobile'}:errors.append('Require desktop, tablet and mobile measurements')
    for view in views:
        vp=view.get('viewport',{})
        if not all(isinstance(vp.get(k),int) and vp[k]>0 for k in ('width','height')):errors.append('Invalid viewport')
        samples=view.get('samples')
        if not isinstance(samples,list) or not samples:errors.append('Empty component measurements');continue
        for sample in samples:
            if not sample.get('selector') or not sample.get('role'):errors.append('Missing component locator')
            box=sample.get('box',{});styles=sample.get('styles',{})
            if not all(isinstance(box.get(k),(int,float)) and math.isfinite(box[k]) for k in ('x','y','width','height')):errors.append('Invalid geometry')
            elif box['width']<=0 or box['height']<=0:errors.append('Empty geometry')
            for key in ('font-family','font-size','font-weight','line-height','padding-top','border-radius'):
                if not isinstance(styles.get(key),str) or not styles[key]:errors.append('Missing measured style: '+key)
        shot=view.get('screenshot')
        if not isinstance(shot,dict) or not SHA.fullmatch(shot.get('sha256','')):errors.append('Missing viewport screenshot hash')
        elif Path(shot.get('snapshot','')).name!=shot.get('snapshot') or shot['snapshot'] in ('','.', '..'):errors.append('Unsafe screenshot name')
        elif directory and (directory/shot['snapshot']).exists() and hashlib.sha256((directory/shot['snapshot']).read_bytes()).hexdigest()!=shot['sha256']:errors.append('Screenshot hash mismatch')
    return sorted(set(errors))

def main():
    rows={r['slug']:r for r in load_sites()};errors=[];count=0
    for p in (ROOT/'design-md').glob('*/MEASUREMENTS.json'):
        count+=1;data=json.loads(p.read_text())
        result=validate_measurements(json.loads(p.read_text()),rows[p.parent.name],ROOT/'_state/p1-measured/_state/evidence'/p.parent.name)
        for view in data['viewports']:
            shot=view.get('screenshot') or {};public=shot.get('public_path','')
            if public!='evidence/'+shot.get('snapshot','') or not (p.parent/public).is_file():result.append('Missing public screenshot')
            elif hashlib.sha256((p.parent/public).read_bytes()).hexdigest()!=shot['sha256']:result.append('Public screenshot hash mismatch')
        document=p.parent/'MEASURED.md'
        if not result and (not document.is_file() or document.read_text()!=render(data,rows[p.parent.name])):result.append('Measured document differs from JSON evidence')
        if result:errors.append({'slug':p.parent.name,'errors':result})
    print(json.dumps({'measured_references':count,'errors':errors},indent=2));return int(bool(errors))
if __name__=='__main__':raise SystemExit(main())
