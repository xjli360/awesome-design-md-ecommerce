#!/usr/bin/env python3
"""Index used color literals verified in retained CSS but omitted by top-N hints.

Never changes DESIGN.md or invents a value. Missing evidence is reported, not
filled. Historical unverified specs are not promoted by this migration.
"""
import argparse
import hashlib
import json
from design_system import ROOT, BLOCKS, atomic_write, parse_document, walk_values
from extract_site import COLOR, Page, norm_hex

def main():
    parser=argparse.ArgumentParser(__doc__);parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    updated=[];missing=[]
    for path in sorted((ROOT/'design-md').glob('*/SOURCE.json')):
        evidence=json.loads(path.read_text());slug=path.parent.name
        if evidence.get('design_origin')=='historical':continue
        data=parse_document((path.parent/'DESIGN.md').read_text())
        used={norm_hex(m[0]) for b in BLOCKS for text in walk_values(data.get(b,{})) for m in COLOR.finditer(text)}
        needed=used-set(evidence['colors'])
        if not needed:continue
        found={}
        for page in evidence['pages']:
            snap=ROOT/'_state/evidence'/slug/page['snapshot']
            if not snap.exists():continue
            raw=snap.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=page['sha256']:raise ValueError(f'Changed snapshot: {slug}/{snap.name}')
            text=raw.decode('utf-8')
            if snap.suffix=='.html':
                parsed=Page();parsed.feed(text);text='\n'.join(parsed.styles)
            elif snap.suffix!='.css':continue
            for match in COLOR.finditer(text):
                color=norm_hex(match[0])
                if color not in needed:continue
                entry=found.setdefault(color,{'count':0,'sources':[]})
                entry['count']+=1
                if page['url'] not in entry['sources']:entry['sources'].append(page['url'])
        if found:
            evidence['colors'].update(found)
            evidence['retained_css_palette_extension']=sorted(set(evidence.get('retained_css_palette_extension',[]))|set(found))
            if args.apply:atomic_write(path,json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
            updated.append({'slug':slug,'added':sorted(found)})
        if needed-set(found):missing.append({'slug':slug,'unobserved':sorted(needed-set(found))})
    report={'applied':args.apply,'updated':updated,'missing':missing}
    atomic_write(ROOT/'_state/retained_color_audit.json',json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
