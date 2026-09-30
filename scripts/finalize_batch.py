#!/usr/bin/env python3
"""Finish an exited expansion with exact-count and evidence readback checks."""
import argparse
import fcntl
import hashlib
import json
import subprocess
import sys
import shutil
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from design_system import ROOT, atomic_write, attach_evidence, load_sites, validate
from extract_site import Page

PUBLIC_ARTIFACTS=('README.md','INDEX.md','STATUS.md','RECOMMENDED.md','HISTORICAL.md','MEASURED.md','data/brands.csv','data/manifest.json','assets/hero.svg')

def run(script,*args):
    subprocess.run([sys.executable,str(ROOT/'scripts'/script),*args],check=True,cwd=ROOT)

def main():
    parser=argparse.ArgumentParser(__doc__)
    parser.add_argument('batch_id')
    parser.add_argument('--report-dir',type=Path,required=True)
    args=parser.parse_args()
    with (ROOT/'_state/worker.lock').open('a+') as lock:
        try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:raise SystemExit('Worker still running; wait for its original process')
        state_path=ROOT/'_state/batches'/f'{args.batch_id}.json';state=json.loads(state_path.read_text())
        exhaustive=state.get('all_remaining',False)
        if state['status']!=('reviewed' if exhaustive else 'complete'):raise SystemExit('Batch is not complete')
        if exhaustive and {r['slug'] for r in state['queue']}-set(state['results']):raise SystemExit('Unattempted queue entries remain')
        # Palette/proof mappings are produced atomically by the worker; do not mutate
        # published evidence independently during finalization.
        run('verify_batch.py',args.batch_id)
        all_slugs={p.parent.name for p in (ROOT/'design-md').glob('*/DESIGN.md')}
        new_slugs=all_slugs-set(state['baseline_slugs'])
        done={s for s,r in state['results'].items() if r['status']=='done'}
        if (not exhaustive and len(new_slugs)!=state['target']) or new_slugs!=done:
            raise SystemExit('Exact file-delta check failed')
        rows={r['slug']:r for r in load_sites()}
        frozen=json.loads((ROOT/'data/legacy_documents.json').read_text()).get('documents',{})
        for slug in state['baseline_slugs']:
            if slug in frozen:continue
            folder=ROOT/'design-md'/slug
            if not (folder/'SOURCE.json').exists():
                path=folder/'DESIGN.md'
                source={'source_url':rows[slug]['url'],'captured_at':None,'confidence':'historical_unverified'}
                content=attach_evidence(path.read_text(),source,source_available=False)
                if not validate(content,rows[slug]['brand_name'])['valid']:raise ValueError(f'Invalid historical metadata: {slug}')
                atomic_write(path,content)
        for source_path in (ROOT/'design-md').glob('*/SOURCE.json'):
            if source_path.parent.name in frozen:continue
            source=json.loads(source_path.read_text());path=source_path.parent/'DESIGN.md'
            snapshot=ROOT/'_state/evidence'/path.parent.name/'homepage.html'
            if snapshot.exists():
                parsed=Page();parsed.feed(snapshot.read_text())
                if parsed.title:
                    source['title']=' '.join(parsed.title).strip()[:250]
                    atomic_write(source_path,json.dumps(source,ensure_ascii=False,indent=2)+'\n')
            content=attach_evidence(path.read_text(),source)
            checked=validate(content,rows[path.parent.name]['brand_name'])
            if not checked['valid']:raise ValueError(checked['errors'])
            atomic_write(path,content)
        run('check_format.py')
        run('check_evidence.py')
        run('check_measurements.py')
        run('build_index.py')
        first={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in PUBLIC_ARTIFACTS}
        run('build_index.py')
        second={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in PUBLIC_ARTIFACTS}
        if first!=second:raise SystemExit('Generated artifacts are not deterministic')
        # Prove the public input is sufficient without ignored author state.
        tracked=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).split(b'\0')
        extra=subprocess.check_output(['git','ls-files','--others','--exclude-standard','-z'],cwd=ROOT).split(b'\0')
        with tempfile.TemporaryDirectory(prefix='design-md-portability-') as temp:
            clean=Path(temp)
            for raw in set(tracked+extra):
                if not raw:continue
                rel=Path(raw.decode());src=ROOT/rel
                if not src.is_file():continue
                dest=clean/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
            for script in ('check_format.py','check_evidence.py','check_measurements.py','build_index.py'):
                subprocess.run([sys.executable,str(clean/'scripts'/script)],check=True,cwd=clean)
            clean_hashes={p:hashlib.sha256((clean/p).read_bytes()).hexdigest() for p in PUBLIC_ARTIFACTS}
            if clean_hashes!=second:raise SystemExit('Clean-copy outputs differ from the working collection')
        subprocess.run([sys.executable,'-m','unittest','discover','-s','tests'],cwd=ROOT,check=True)
        subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
        counts=json.loads((ROOT/'data/manifest.json').read_text())['counts']
        state['final_counts']=counts;state['verified_at']=datetime.now(timezone.utc).isoformat();state['verification']='exact-new-file-delta, canonical/redirect dedupe, YAML/schema/references, CSS evidence, snapshot hashes, deterministic indexes'
        atomic_write(state_path,json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        entries=[]
        for slug in sorted(new_slugs):
            source=json.loads((ROOT/'design-md'/slug/'SOURCE.json').read_text())
            entries.append({**rows[slug],'final_url':source['final_url'],'captured_at':source['captured_at'],'evidence_status':source['confidence'],'path':f'design-md/{slug}/DESIGN.md'})
        result_counts=dict(Counter(r['status'] for r in state['results'].values()))
        refresh=json.loads((ROOT/'_state/evidence_refresh.json').read_text()) if (ROOT/'_state/evidence_refresh.json').exists() else []
        baseline_path=args.report_dir/'baseline.json'
        baseline=json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
        retained_changes=[slug for slug,expected in baseline.get('design_sha256',{}).items() if hashlib.sha256((ROOT/'design-md'/slug/'DESIGN.md').read_bytes()).hexdigest()!=expected]
        summary=dict(batch_id=args.batch_id,status=state['status'],baseline_entries=len(state['baseline_slugs']),new_entries=len(entries),counts=counts,attempt_results=result_counts,retained_file_changes=retained_changes,old_evidence_refresh=refresh,entries=entries)
        args.report_dir.mkdir(parents=True,exist_ok=True)
        atomic_write(args.report_dir/'new-entries.json',json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
        listing=['# 本批新增网站','',f'已验收：{len(entries)} 个；原有文件与跳转别名不计入新增。','', '| 品牌 | 分类 | DESIGN.md | 来源 |','|---|---|---|---|']
        for r in entries:
            name=r['brand_name'].replace('|','\\|');cat=r['category'].replace('|','\\|')
            listing.append(f"| {name} | {cat} | [{r['slug']}]({ROOT / r['path']}) | [官网]({r['final_url']}) |")
        atomic_write(args.report_dir/'NEW-SITES.md','\n'.join(listing)+'\n')
        backup=next((p.name for p in (args.report_dir/'before-expansion.tar.gz',args.report_dir/'before-optimization.tar.gz') if p.exists()),None)
        backup_link=f'- [修改前备份](./{backup})' if backup else ''
        report=f'''# 新增批次验收

状态：**{'队列已全部处理，未通过的来源仍不计完成' if exhaustive else '完成'}**。批次 `{args.batch_id}`，核验时间 `{state['verified_at']}`。

| 指标 | 结果 |
|---|---:|
| 本批开始时已有文件 | {len(state['baseline_slugs']):,} |
| 本次有效新增网站/文件 | {len(entries)} |
| 本地 DESIGN.md 总数 | {counts['generated_records']:,} |
| 严格格式校验通过 | {counts['validated_records']:,} |
| 去重后已覆盖网站 URL | {counts['generated_sites']:,} |
| 去重后目标 URL | {counts['target_sites']:,} |
| 剩余未覆盖 URL | {counts['remaining_sites']:,} |
| 剩余无文件的原始任务记录 | {counts['remaining_records']:,} |
| 覆盖分类标签 | {counts['categories']} |

实际文件增量与批次成功名单完全一致；跳转别名已移至本地隔离目录保留，不计入新增。网址口径采用域名、路径规范化加本次实测跳转别名；未声称完成全网品牌身份去重。

## 本批处理

- 沿用前次优化后的校验与采集流程，优先处理尚未尝试的网站。此前的受阻/失败候选保留为后备队列。
- 校验真实 YAML、重复键、结构和值类型、空章节、品牌名、未定义与循环引用；错误返回非零退出码。单色/少色设计不再被迫凑满十种颜色。
- 生成器保存 HTTP/CSS 证据并限定色值与字体来源；采集受阻、证据不足、模型生成未观测色值的条目不计成功。最多五路、有限重试、进程锁、原子写入、批次断点与成功数量上限均已落实。
- manifest 统一网址、历史别名、多分类、验证及证据状态；README、索引、CSV、SVG 数量统一生成。
- 历史证据复采记录继续保留，未把前次复采或已存在文件计为本批新增。
- 本批基线 DESIGN.md 内容变化数：{len(retained_changes)}。与基线的差异清单见机器可读结果中的 retained_file_changes。
- 带来源的 DESIGN.md 已加入采集时间、URL、证据状态及 SOURCE.json 链接。

## 验证

- 全量严格格式检查与本批次精确增量、唯一网址、来源色值和字体对账通过。
- 可用本地 HTML/CSS 快照的 SHA-256 回读验证通过。
- 回归测试通过，包含错误退出码、引用错误、循环引用、描述保真、网址/跳转去重、验证页/占位页识别、失败补足及成功数量不超额。
- 索引连续生成两次内容哈希一致，git diff --check 通过。
- 不含作者本地队列和采集快照的干净副本也能通过格式/公开证据检查并生成完全相同的索引；快照哈希核验仅在原本地仓库执行。
- 本批任务结果分布：`{json.dumps(result_counts,ensure_ascii=False)}`。

## 证据边界与文件

新资料基于真实网页 HTML/CSS 采集，必要时补充匿名浏览器渲染和计算样式。色值/字体出现过并不等于组件语义或屏幕呈现已验证；布局、尺寸、交互和响应式行为仍按 inferred/unverified 标记，不作像素级复刻保证。原始采集快照在项目 `_state/evidence/`，公开证据摘要在各目录 SOURCE.json。

- [新增网站清单](./NEW-SITES.md)
- [机器可读结果](./new-entries.json)
{backup_link}
- 项目：`{ROOT}`

本报告核验本地文件；远端发布状态以另行生成的 publication-receipt.json 为准。
'''
        atomic_write(args.report_dir/'REPORT.md',report)
        print(json.dumps({'report':str(args.report_dir/'REPORT.md'),'new_entries':len(entries),'counts':counts},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
