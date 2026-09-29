"""Build canonical progress manifest without deleting historical duplicate files."""
import csv
import io
import json
from collections import defaultdict
from design_system import ROOT, atomic_write, canonical_url, load_sites, validate

def reconcile(root=ROOT):
    rows=load_sites(root); groups=defaultdict(list); records=[]
    alias_path=root/'data/url_aliases.json'
    aliases=json.loads(alias_path.read_text()) if alias_path.exists() else {}
    hold_path=root/'data/source_holds.json'
    holds=json.loads(hold_path.read_text()) if hold_path.exists() else {}
    def identity(url):
        key=canonical_url(url);seen=set()
        while key in aliases:
            if key in seen:raise ValueError(f'URL alias cycle: {key}')
            seen.add(key);key=aliases[key]
        return key
    for row in rows:
        slug=row['slug']; path=root/'design-md'/slug/'DESIGN.md'; exists=path.exists()
        result=validate(path.read_text(),row['brand_name']) if exists else None
        source=root/'design-md'/slug/'SOURCE.json'
        evidence=json.loads(source.read_text()) if source.exists() else None
        record={**row,'canonical_url':identity(row['url']),'generated':exists,'validated':bool(result and result['valid']),'evidence_status':evidence['confidence'] if evidence else 'historical_unverified' if exists else 'not_captured','captured_at':evidence.get('captured_at') if evidence else None,'errors':result['errors'] if result else []}
        if row['slug'] in holds:record['source_hold']=holds[row['slug']]
        records.append(record);groups[record['canonical_url']].append(record)
    known={r['slug'] for r in rows};orphans={p.parent.name for p in (root/'design-md').glob('*/DESIGN.md')}-known
    if orphans:raise ValueError(f'Files missing metadata: {sorted(orphans)}')
    for url,group in groups.items():
        primary=next((r for r in group if r['validated']),group[0])
        categories=sorted({r['category'] for r in group})
        hold=next((r['source_hold'] for r in group if 'source_hold' in r),None)
        for r in group:
            r['canonical_slug']=primary['slug'];r['categories']=categories
            r['alias_of']=primary['slug'] if r is not primary else None
            r['coverage_status']='documented' if r['validated'] else 'covered_by_alias' if primary['validated'] else 'source_hold' if hold else 'pending'
            if hold and not primary['validated']:r['source_hold']=hold
    generated=[r for r in records if r['generated']];valid=[r for r in records if r['validated']]
    done_urls={r['canonical_url'] for r in valid};generated_urls={r['canonical_url'] for r in generated}
    counts=dict(target_records=len(rows),target_sites=len(groups),generated_records=len(generated),validated_records=len(valid),generated_sites=len(generated_urls),validated_sites=len(done_urls),remaining_records=len(rows)-len(generated),remaining_sites=len(groups)-len(generated_urls),categories=len({c for r in generated for c in r['categories']}),generated_record_categories=len({r['category'] for r in generated}),target_categories=len({r['category'] for r in rows}))
    manifest=dict(schema_version=1,identity_rule='lowercase host without www plus path without trailing slash; missing scheme normalized to https; only evidence-backed redirects in data/url_aliases.json are consolidated',counts=counts,sites=records)
    atomic_write(root/'data/manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    atomic_write(root/'_state/done.txt','\n'.join(sorted(r['slug'] for r in valid))+'\n')
    failed=root/'_state/failed.txt'
    if failed.exists():
        latest={}; resolved=[]
        for line in failed.read_text().splitlines():
            slug=line.split('\t')[0]
            if slug in {r['slug'] for r in valid}:resolved.append(line)
            else:latest[slug]=line
        if resolved:
            history=root/'_state/resolved_failures.txt'
            old=history.read_text() if history.exists() else ''
            atomic_write(history,old+'\n'.join(resolved)+'\n')
        atomic_write(failed,'\n'.join(latest.values())+ ('\n' if latest else ''))
    return manifest

if __name__=='__main__':print(json.dumps(reconcile()['counts'],indent=2))
