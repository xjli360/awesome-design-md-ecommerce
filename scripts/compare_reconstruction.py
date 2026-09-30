#!/usr/bin/env python3
"""Compare an implementation screenshot to an explicitly selected reference viewport.

This is a bounded pixel check, not an automatic brand/asset authenticity score.
A candidate must be produced independently from the MD; reference hashes alone
cannot qualify a document as recreation-verified.
"""
import argparse,json,hashlib
from pathlib import Path
from PIL import Image,ImageChops,ImageStat

def compare(reference,candidate,tolerance=0.02):
    with Image.open(reference) as a,Image.open(candidate) as b:
        a=a.convert('RGB');b=b.convert('RGB')
        if a.size!=b.size:return {'passed':False,'reason':'viewport_size_mismatch','reference_size':a.size,'candidate_size':b.size}
        diff=ImageChops.difference(a,b);mae=sum(ImageStat.Stat(diff).mean)/(3*255)
        return {'passed':mae<=tolerance,'normalized_mean_absolute_error':mae,'tolerance':tolerance,'viewport':a.size}

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('reference',type=Path);p.add_argument('candidate',type=Path);p.add_argument('--report',type=Path,required=True);p.add_argument('--tolerance',type=float,default=.02);a=p.parse_args()
    if not 0<=a.tolerance<=.1:p.error('Tolerance must be between 0 and 0.1')
    result=compare(a.reference,a.candidate,a.tolerance)
    result.update(reference_sha256=hashlib.sha256(a.reference.read_bytes()).hexdigest(),candidate_sha256=hashlib.sha256(a.candidate.read_bytes()).hexdigest(),scope='single-viewport screenshot comparison; no automatic corpus promotion')
    a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));return int(not result['passed'])
if __name__=='__main__':raise SystemExit(main())
