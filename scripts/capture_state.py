"""A failed/incomplete latest attempt must never select an older capture implicitly."""
import json
import uuid
import hashlib
from datetime import datetime,timezone
from pathlib import Path
from design_system import atomic_write,canonical_url

def begin(directory,url):
    directory.mkdir(parents=True,exist_ok=True)
    state={'capture_id':uuid.uuid4().hex,'source_url':url,'started_at':datetime.now(timezone.utc).isoformat(),'status':'running'}
    atomic_write(directory/'attempt.json',json.dumps(state,indent=2)+'\n')
    return state

def finish(directory,state,evidence=None,reason=None):
    latest=json.loads((directory/'attempt.json').read_text())
    if latest.get('capture_id')!=state.get('capture_id'):raise ValueError('Capture attempt was superseded')
    state={**state,'status':'hold' if reason else 'ready','completed_at':datetime.now(timezone.utc).isoformat()}
    if reason:state['reason']=reason
    else:
        evidence['capture_id']=state['capture_id']
        atomic_write(directory/'capture.json',json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
        state['capture_sha256']=hashlib.sha256((directory/'capture.json').read_bytes()).hexdigest()
    atomic_write(directory/'attempt.json',json.dumps(state,indent=2)+'\n')

def load_capture(directory,url):
    pointer=directory/'attempt.json'
    if not pointer.is_file():raise ValueError('Capture has no attempt identity; recapture it explicitly')
    attempt=json.loads(pointer.read_text())
    if attempt.get('status')!='ready':raise ValueError('Latest capture is not ready: '+attempt.get('status','unknown'))
    raw=(directory/'capture.json').read_bytes();data=json.loads(raw)
    if data.get('capture_id')!=attempt.get('capture_id') or hashlib.sha256(raw).hexdigest()!=attempt.get('capture_sha256'):raise ValueError('Capture does not match the latest successful attempt')
    if canonical_url(data.get('source_url',''))!=canonical_url(url):raise ValueError('Retained capture URL mismatch')
    for item in data.get('pages',[])+data.get('screenshots',[]):
        name=item.get('snapshot','')
        if Path(name).name!=name or name in ('','.', '..') or '\\' in name:raise ValueError('Unsafe snapshot path')
        if hashlib.sha256((directory/name).read_bytes()).hexdigest()!=item.get('sha256'):raise ValueError('Retained snapshot hash mismatch')
    return data
