#!/usr/bin/env python3
"""Export unresolved source reviews after an exhaustive batch has exited.

Public output contains URLs, dates, HTTP status and hashes, not local snapshots
or runtime logs. Temporary access failures remain retryable; identity decisions
require explicit review. Build the index again after this command.
"""
import argparse
import fcntl
import json
from pathlib import Path
from collection import reconcile
from design_system import ROOT, atomic_write
from extract_site import source_problem

def main():
    p=argparse.ArgumentParser(__doc__);p.add_argument('batch_id');p.add_argument('--capture-root',type=Path,action='append',default=[]);p.add_argument('--notes',type=Path)
    args=p.parse_args()
    with (ROOT/'_state/worker.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        state=json.loads((ROOT/'_state/batches'/f'{args.batch_id}.json').read_text())
        if state['status']!='reviewed' or {r['slug'] for r in state['queue']}-set(state['results']):raise SystemExit('Exhaustive review is not finished')
        manifest=reconcile();notes=json.loads(args.notes.read_text()) if args.notes else {};holds={}
        for row in manifest['sites']:
            if row['generated'] and row['slug'] not in state['baseline_slugs'] and row['slug'] in notes and notes[row['slug']].get('manual_review_required',True):
                raise ValueError(f"Generated file still has a manual source hold: {row['slug']}; reconcile the batch before exporting")
        for row in manifest['sites']:
            if row['alias_of'] or row['generated']:continue
            slug=row['slug'];result=state['results'].get(slug)
            if not result:raise ValueError(f'Unreviewed canonical source: {slug}')
            attempts=[];titles=[];problems=[]
            for root in [ROOT,*args.capture_root]:
                directory=root/'_state/evidence'/slug;cp=directory/'capture.json';bp=directory/'browser-result.json'
                if cp.exists():
                    source=json.loads(cp.read_text());page=source.get('pages',[{}])[0];problem=source_problem(source)
                    attempts.append(dict(method=source['method'],source_url=source['source_url'],final_url=source['final_url'],checked_at=source['captured_at'],http_status=page.get('http_status'),capture_result=problem or 'retrieved',snapshot_sha256=page.get('sha256')))
                    if source.get('title'):titles.append(source['title'])
                    if problem:problems.append(problem)
                if bp.exists():
                    source=json.loads(bp.read_text());reason=source.get('reason','')
                    problem='TLS_OR_NETWORK_ERROR' if 'ERR_' in reason or 'Timeout' in reason else reason
                    attempts.append(dict(method='anonymous-browser',source_url=source.get('source_url',row['url']),final_url=source.get('final_url'),checked_at=source.get('checked_at'),http_status=source.get('http_status'),capture_result=problem))
                    if source.get('title'):titles.append(source['title'])
                    problems.append(problem)
            unique={json.dumps(a,sort_keys=True):a for a in attempts};attempts=sorted(unique.values(),key=lambda a:a.get('checked_at') or '')
            checked=max((a['checked_at'] for a in attempts if a.get('checked_at')),default=None)
            if not checked:raise ValueError(f'No dated evidence for {slug}')
            reason=result.get('reason','');manual=False
            if slug in notes:
                status=notes[slug]['status'];reason=notes[slug]['reason'];manual=notes[slug].get('manual_review_required',True)
            elif result['status']=='failed':status='generation_validation_failed';reason='Page evidence was retrieved, but the generated document did not pass validation.'
            elif any(x=='PARKED_OR_PLACEHOLDER' for x in problems):status='parked_or_placeholder';reason='An attempted source is a domain parking, expiry, sale, or launch placeholder page.';manual=True
            elif 'REJECT_SOURCE' in reason:status='needs_source_review';reason='The captured page did not establish a matching active brand/product site. Review the source identity or category before generating.';manual=True
            elif any(x in ('PASSWORD_GATE','CHALLENGE_OR_ERROR_PAGE') for x in problems) or any(a.get('http_status') in (401,403,429) for a in attempts):status='access_blocked';reason='Anonymous capture encountered an access challenge, password gate, or HTTP access/rate restriction.'
            elif any(a.get('http_status') in (404,410) for a in attempts):status='source_not_found';reason='The requested page returned HTTP 404 or 410; a current official URL is needed.'
            elif any(x=='TLS_OR_NETWORK_ERROR' for x in problems) or all(a.get('http_status') in (0,None) for a in attempts):status='network_unavailable';reason='The page could not be retrieved through the attempted HTTP/browser connections. This does not establish that the business is closed.'
            else:status='insufficient_evidence';reason='The retrieved page did not provide sufficient brand content, palette or font evidence for a reliable addition.'
            holds[slug]=dict(status=status,reason=reason,manual_review_required=manual,source_url=row['url'],checked_on=checked[:10],observed_title=titles[-1] if titles else None,attempts=attempts)
        if len(holds)!=manifest['counts']['remaining_sites']:raise ValueError('Remaining URL count mismatch')
        atomic_write(ROOT/'data/source_holds.json',json.dumps(holds,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'reviewed_without_document':len(holds),'batch_id':args.batch_id},indent=2))

if __name__=='__main__':main()
