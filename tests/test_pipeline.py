import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from design_system import canonical_url, parse_document, repair_syntax, validate
from extract_site import Page, source_problem, capture
import extract_site
import worker_claude as worker
from collection import reconcile

VALID='''---
version: alpha
name: Example
description: |-
  Restrained grayscale reference.
colors:
  primary: "#111111"
  canvas: "#ffffff"
typography:
  body: {fontFamily: Arial, fontSize: 16px, fontWeight: 400, lineHeight: 1.5}
rounded:
  none: 0px
spacing:
  sm: 8px
components:
  button:
    backgroundColor: "{colors.primary}"
    padding: "{spacing.sm}"
## Components
Proposed button.
## Responsive Behavior
Unmeasured layout; proposed mobile stacking.
## Known Gaps
Interaction states are unverified.
'''

class ValidationTests(unittest.TestCase):
    def test_small_palette_not_rejected(self):
        r=validate(VALID,'Example');self.assertTrue(r['valid']);self.assertTrue(r['warnings'])
    def test_duplicate_key_and_broken_reference_rejected(self):
        self.assertFalse(validate(VALID.replace('  canvas:', '  primary:'))['valid'])
        self.assertFalse(validate(VALID.replace('{spacing.sm}','{spacing.missing}'))['valid'])
        cycle=VALID.replace('primary: "#111111"','primary: "{colors.canvas}"').replace('canvas: "#ffffff"','canvas: "{colors.primary}"')
        self.assertFalse(validate(cycle)['valid'])
    def test_plain_description_hex_is_not_lost_as_yaml_comment(self):
        original=VALID.replace('description: |-\n  Restrained grayscale reference.','description: Ink #111111 and canvas #ffffff are observed.')
        fixed=repair_syntax(original,'Example')
        self.assertEqual(parse_document(fixed)['description'],'Ink #111111 and canvas #ffffff are observed.')
    def test_description_colon_and_css_shorthand_repair(self):
        broken=VALID.replace('description: |-\n  Restrained grayscale reference.','description: A palette: dark ink.').replace('padding: "{spacing.sm}"','padding: "{spacing.sm}" 0')
        fixed=repair_syntax(broken,'Example');r=validate(fixed,'Example')
        self.assertTrue(r['valid'],r['errors']);self.assertEqual(r['data']['description'],'A palette: dark ink.')
        self.assertEqual(r['data']['components']['button']['padding'],'{spacing.sm} 0')
        self.assertEqual(repair_syntax(fixed,'Example'),fixed)
    def test_cli_returns_failure(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'DESIGN.md';p.write_text(VALID.replace('{spacing.sm}','{spacing.missing}'))
            result=subprocess.run([sys.executable,str(Path(worker.ROOT)/'scripts/check_format.py'),str(p),'--report',str(Path(t)/'report.json')],capture_output=True)
            self.assertEqual(result.returncode,1)
    def test_url_identity_and_link_attribute_order(self):
        self.assertEqual(canonical_url('www.example.com/'),canonical_url('https://example.com'))
        p=Page();p.feed('<link href="/style.css" media="all" rel="stylesheet">')
        self.assertEqual(p.links,['/style.css'])
    def test_http_200_interstitials_and_parked_domains_rejected(self):
        for title in ('Challenge Validation','Pardon Our Interruption MSCDirect.com','STRATO - Domain reserved STRATO'):
            self.assertIsNotNone(source_problem({'title':title,'final_url':'https://example.com'}))
        self.assertEqual(source_problem({'title':'J!NX','final_url':'https://example.com/password'}),'PASSWORD_GATE')
        self.assertIsNone(source_problem({'title':'Home Security Systems | Ring','final_url':'https://ring.com'}))
        self.assertEqual(source_problem({'title':'Tire Rack','page_text_excerpt':"We're sorry. This page is currently unavailable."}),'SITE_UNAVAILABLE')
        self.assertEqual(source_problem({'title':'Flyte.com for sale'}),'PARKED_OR_PLACEHOLDER')
        self.assertEqual(source_problem({'title':'Discount Tire Direct','page_text_excerpt':'Discount Tire Direct is retiring, but check out our partners at Tire Rack!'}),'INACTIVE_STOREFRONT_NOTICE')
    def test_svg_titles_do_not_pollute_page_identity(self):
        p=Page();p.feed('<html><head><title>Example Store</title></head><body><svg><title>Cart icon</title></svg></body></html>')
        self.assertEqual(p.title,['Example Store'])
    def test_theme_after_plugins_and_css_import_font_are_captured(self):
        html='<head><title>Example Store</title>'+''.join(f'<link rel="stylesheet" href="/plugins/{i}.css">' for i in range(6))+'<link rel="stylesheet" href="/themes/store.css"></head><body>Example products</body>'
        def fetch(url,timeout=25):
            body=html if url=='https://example.com' else '@import "https://example.com/font.css";body{color:#111;background:#fff}' if '/themes/' in url else 'body{font-family:ExampleSans, sans-serif !important}' if url.endswith('/font.css') else 'button{color:#111}'
            return dict(ok=True,status=200,url=url,final_url=url,content_type='text/html' if url=='https://example.com' else 'text/css',body=body)
        with tempfile.TemporaryDirectory() as t,patch.object(extract_site,'fetch',side_effect=fetch):
            evidence=capture({'slug':'example','url':'https://example.com'},Path(t))
            self.assertNotIn('failure',evidence)
            self.assertIn('ExampleSans',evidence['font_families'])
            self.assertNotIn('sans-serif !important',evidence['font_families'])
            self.assertTrue(any(p['snapshot'].startswith('import-') for p in evidence['pages']))
    def test_parked_domain_body_is_rejected_even_without_title(self):
        self.assertEqual(source_problem({'title':'','page_text_excerpt':'example.com\nis parked free, courtesy of GoDaddy.com.'}),'PARKED_OR_PLACEHOLDER')
    def test_unobserved_color_and_font_rejected(self):
        data=parse_document(VALID)
        errors=worker.evidence_check(data,{'colors':{'#ffffff':{}},'font_families':{'Helvetica':[]}})
        self.assertTrue(any('Unobserved color' in e for e in errors));self.assertTrue(any('Unobserved family' in e for e in errors))
    def test_component_placeholder_color_rejected(self):
        broken=VALID.replace('    padding: "{spacing.sm}"','    colors: ["#111111", "#e8d419-placeholder"]')
        self.assertFalse(validate(broken)['valid'])
    def test_inline_component_hex_requires_evidence(self):
        data=parse_document(VALID.replace('backgroundColor: "{colors.primary}"','backgroundColor: "#123456"'))
        errors=worker.evidence_check(data,{'colors':{'#111111':{},'#ffffff':{}},'font_families':{'Arial':[]}})
        self.assertTrue(any('Unobserved inline color' in e for e in errors))
    def test_candidate_dedupe_and_covered_alias(self):
        sites=[dict(slug='a',canonical_url='a.com',category='A',generated=True),dict(slug='a-alias',canonical_url='a.com',category='B',generated=False),dict(slug='b',canonical_url='b.com',category='B',generated=False),dict(slug='b-alias',canonical_url='b.com',category='C',generated=False)]
        self.assertEqual([r['slug'] for r in worker.choose_pending({'sites':sites})],['b'])
    def test_temporary_access_hold_remains_retryable(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'data').mkdir()
            (root/'data/source_holds.json').write_text(json.dumps({'temporary':{'manual_review_required':False},'wrong-brand':{'manual_review_required':True}}))
            sites=[dict(slug=s,canonical_url=s+'.com',category='A',generated=False) for s in ('temporary','wrong-brand')]
            with patch.object(worker,'ROOT',root):
                self.assertEqual([r['slug'] for r in worker.choose_pending({'sites':sites})],['temporary'])
                self.assertEqual(len(worker.choose_pending({'sites':sites},include_held=True)),2)
    def test_redirect_alias_preserves_records_but_deduplicates_target(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'data').mkdir();(root/'design-md/example').mkdir(parents=True)
            (root/'design-md/example/DESIGN.md').write_text(VALID)
            (root/'data/sites.csv').write_text('slug,category,brand_name,url\nexample,A,Example,https://example.com\nold-example,B,Example,https://old-example.com\n')
            (root/'data/url_aliases.json').write_text(json.dumps({'old-example.com':'example.com'}))
            manifest=reconcile(root)
            self.assertEqual(manifest['counts']['target_records'],2)
            self.assertEqual(manifest['counts']['target_sites'],1)
            self.assertEqual(manifest['counts']['remaining_sites'],0)
            self.assertEqual(manifest['sites'][1]['alias_of'],'example')
    def test_exact_success_target_replaces_failed_attempt_without_overshoot(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'_state').mkdir()
            sites=[dict(slug=f's{i}',url=f'https://s{i}.com',brand_name=f'S{i}',canonical_url=f's{i}.com',category='A',generated=False) for i in range(6)]
            manifest={'sites':sites,'counts':{'generated_records':0}}
            def process(site,args):return dict(slug=site['slug'],status='hold' if site['slug']=='s0' else 'done')
            args=SimpleNamespace(batch_id='test',target=2,workers=3,model='unused',retry_failed=False)
            with patch.object(worker,'ROOT',root),patch.object(worker,'reconcile',return_value=manifest),patch.object(worker,'process',side_effect=process) as call,patch.object(worker.subprocess,'run'):
                self.assertEqual(worker.run(args),0)
                self.assertEqual(call.call_count,3)
            state=json.loads((root/'_state/batches/test.json').read_text())
            self.assertEqual(state['completed'],2)

    def test_exhaustive_queue_keeps_holds_distinct_from_completed(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'_state').mkdir()
            sites=[dict(slug=f's{i}',url=f'https://s{i}.com',brand_name=f'S{i}',canonical_url=f's{i}.com',category='A',generated=False) for i in range(4)]
            manifest={'sites':sites,'counts':{'generated_records':0}}
            def process(site,args):return dict(slug=site['slug'],status='hold' if site['slug']=='s0' else 'done')
            args=SimpleNamespace(batch_id='all',target=1,workers=2,model='unused',retry_failed=False,all_remaining=True)
            with patch.object(worker,'ROOT',root),patch.object(worker,'reconcile',return_value=manifest),patch.object(worker,'process',side_effect=process) as call,patch.object(worker.subprocess,'run'):
                self.assertEqual(worker.run(args),0)
                self.assertEqual(call.call_count,4)
            state=json.loads((root/'_state/batches/all.json').read_text())
            self.assertEqual(state['status'],'reviewed')
            self.assertEqual(state['completed'],3)
            self.assertEqual(state['results']['s0']['status'],'hold')

if __name__=='__main__':unittest.main()
