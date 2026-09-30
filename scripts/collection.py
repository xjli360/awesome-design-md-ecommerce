"""Build canonical progress manifest without deleting historical duplicate files."""
import csv
import io
import json
from collections import defaultdict
from design_system import ROOT, atomic_write, canonical_url, load_sites, validate
from evidence import assess
from check_measurements import validate_measurements

def reconcile(root=ROOT):
    rows=load_sites(root); groups=defaultdict(list); records=[]
    lp=root/"data/legacy_documents.json"
    legacy=json.loads(lp.read_text()).get("documents",{}) if lp.exists() else {}
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
        policy=assess(row,path.read_text(),evidence,root,legacy) if exists else None
        record={**row,'canonical_url':identity(row['url']),'generated':exists,'validated':bool(result and result['valid']),'evidence_status':evidence.get('confidence','invalid_source') if evidence else 'historical_unverified' if exists else 'not_captured','captured_at':evidence.get('captured_at') if evidence else None,'errors':policy['errors'] if policy else [],'admitted':bool(policy and policy['admitted']),'evidence_backed':bool(policy and policy['evidence_backed']),'quality_tier':policy['quality_tier'] if policy else 'not_documented','recreation_verified':False}
        mp=path.parent/'MEASUREMENTS.json'
        measured=False
        if mp.exists():
            problems=validate_measurements(json.loads(mp.read_text()),row)
            if problems:
                record['errors'].extend(problems);record['admitted']=False;record['evidence_backed']=False;record['quality_tier']='needs_review'
            else:measured=True
        record['measurements_available']=measured
        record['recommended_reference']=('design-md/'+slug+'/MEASURED.md') if measured and record['admitted'] else ('design-md/'+slug+'/DESIGN.md') if record['evidence_backed'] else None
        if row['slug'] in holds:record['source_hold']=holds[row['slug']]
        records.append(record);groups[record['canonical_url']].append(record)
    known={r['slug'] for r in rows};orphans={p.parent.name for p in (root/'design-md').glob('*/DESIGN.md')}-known
    if orphans:raise ValueError(f'Files missing metadata: {sorted(orphans)}')
    for url,group in groups.items():
        primary=next((r for r in group if r['measurements_available'] and r['admitted']),next((r for r in group if r['evidence_backed']),next((r for r in group if r['admitted']),group[0])))
        categories=sorted({r['category'] for r in group})
        hold=next((r['source_hold'] for r in group if 'source_hold' in r and r['source_hold'].get('manual_review_required',True)),next((r['source_hold'] for r in group if 'source_hold' in r),None))
        if hold and hold.get('manual_review_required',True):
            for r in group:
                r['admitted']=False;r['evidence_backed']=False;r['recommended_reference']=None
                if r['generated']:
                    r['quality_tier']='needs_review';r['errors'].append('Manual source HOLD on canonical URL: '+hold.get('reason','review required'))
        for r in group:
            r['canonical_slug']=primary['slug'];r['categories']=categories
            r['alias_of']=primary['slug'] if r is not primary else None
            r['coverage_status']='source_hold' if hold and hold.get('manual_review_required',True) else 'documented' if r['admitted'] else 'covered_by_alias' if primary['admitted'] else 'needs_review' if r['generated'] else 'source_hold' if hold else 'pending'
            if hold and not primary['validated']:r['source_hold']=hold
    generated=[r for r in records if r['generated']];valid=[r for r in records if r['validated']]
    admitted=[r for r in records if r['admitted']]; backed=[r for r in records if r['evidence_backed']]
    done_urls={r['canonical_url'] for r in admitted};generated_urls={r['canonical_url'] for r in generated}
    counts=dict(target_records=len(rows),target_sites=len(groups),generated_records=len(generated),validated_records=len(valid),generated_sites=len(generated_urls),validated_sites=len(done_urls),remaining_records=len(rows)-len(generated),remaining_sites=len(groups)-len(done_urls),categories=len({c for r in generated for c in r['categories']}),generated_record_categories=len({r['category'] for r in generated}),target_categories=len({r['category'] for r in rows}))
    counts.update(admitted_records=len(admitted),admitted_sites=len(done_urls),evidence_backed_records=len(backed),evidence_backed_sites=len({r['canonical_url'] for r in backed}),historical_archive_records=sum(r['quality_tier']=='historical_archive' for r in records),needs_review_records=sum(r['generated'] and not r['admitted'] for r in records))
    counts.update(measured_references=sum(r['measurements_available'] for r in records),recommended_sites=len({r['canonical_url'] for r in records if r['recommended_reference']}),reconstruction_verified_sites=0)
    manifest=dict(schema_version=2,identity_rule='lowercase host without www plus path without trailing slash; missing scheme normalized to https; only evidence-backed redirects in data/url_aliases.json are consolidated',counts=counts,sites=records)
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
