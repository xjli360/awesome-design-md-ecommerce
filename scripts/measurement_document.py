"""Deterministic, evidence-bound public measurement reference."""
def render(data,row):
    lines=[f"# {row['brand_name']} — measured component reference",'',f"Source: {data['source_url']}",f"Captured: {data['captured_at']}",'','These are observed initial-state component styles, not a complete reconstruction. Candidate CTA roles are heuristic; occluded samples must not be used as visual proof. Legacy DESIGN.md tokens, if present, remain separately graded. No global spacing scale is inferred from these samples.','', 'Whole-site reconstruction / visual comparison: **not performed**. Asset URLs below do not bundle font/image files.','']
    for view in data['viewports']:
        vp=view['viewport'];lines += [f"## {vp['name']} — {vp['width']} × {vp['height']}",'','| Component | Size (px) | Font / size / weight | Padding (T R B L) | Radius | Colors (text / background) | Occluded |','|---|---|---|---|---|---|---|']
        for sample in view['samples']:
            st=sample['styles'];box=sample['box'];vals=[sample['role'],f"{box['width']:.1f} × {box['height']:.1f}",f"{st['font-family']} / {st['font-size']} / {st['font-weight']}",' '.join(st['padding-'+k] for k in ('top','right','bottom','left')),st['border-radius'],st['color']+' / '+st['background-color'],str(sample['occluded'])]
            lines.append('| '+' | '.join(str(v).replace('|','\\|').replace('\n',' ') for v in vals)+' |')
        lines+=['',f"[Reference screenshot](./{view['screenshot']['public_path']})",'','Measured interaction states: '+', '.join(k for k,v in view['states'].items() if isinstance(v,dict))+'. Menu-open behavior is not measured.','']
    lines+=['## Evidence','', '[MEASUREMENTS.json](./MEASUREMENTS.json) provides locators, geometry, computed styles, image URLs, viewport/state scope and screenshot hashes. CSS families are computed declarations; actual glyph substitution and licensing are not verified.','']
    return '\n'.join(lines)
