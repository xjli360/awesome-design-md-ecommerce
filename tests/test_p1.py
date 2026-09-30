"""Regression cases from the P1 audit: admission, stale evidence and quality tiers."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from test_pipeline import VALID
from design_system import parse_document, validate
from evidence import assess, token_records
from capture_state import begin, finish, load_capture
from collection import reconcile
from check_evidence import audit
from css_values import declarations, color_literals, font_families
from recommend import select
from compare_reconstruction import compare
from check_measurements import validate_measurements

ROW=dict(slug='example',brand_name='Example',url='https://example.com',category='A')
DATE='2026-09-28T00:00:00+00:00'
TEXT=VALID.replace('description:',f'source_url: https://example.com\ncaptured_at: "{DATE}"\nevidence_status: css_values_observed_roles_inferred\nquality_tier: css_reference\nusage_scope: style_reference_only\nlayout_status: proposed_not_measured\nrecreation_verified: false\ndescription:',1)

def fixture(root):
    (root/'data').mkdir();directory=root/'design-md/example';directory.mkdir(parents=True)
    (root/'data/sites.csv').write_text('slug,category,brand_name,url\nexample,A,Example,https://example.com\n')
    directory.joinpath('DESIGN.md').write_text(TEXT)
    raw=b'body{color:#111111;background:#ffffff;font-family:Arial}'
    rawdir=root/'_state/evidence/example';rawdir.mkdir(parents=True);(rawdir/'page.css').write_bytes(raw)
    digest=hashlib.sha256(raw).hexdigest()
    page=dict(url=ROW['url'],final_url=ROW['url'],snapshot='page.css',sha256=digest,http_status=200,content_type='text/css')
    def proof(prop,value):return dict(selector='body',property=prop,declaration=value,url=ROW['url'],snapshot='page.css',sha256=digest)
    source=dict(schema_version=2,source_url=ROW['url'],final_url=ROW['url'],captured_at=DATE,confidence='css_values_observed_roles_inferred',title='Example store',pages=[page],colors={c:dict(sources=[ROW['url']]) for c in ('#111111','#ffffff')},font_families={'Arial':[ROW['url']]},observations={'colors':{'#111111':proof('color','#111111'),'#ffffff':proof('background','#ffffff')},'font_families':{'Arial':proof('font-family','Arial')}})
    source['tokens']=token_records(parse_document(TEXT),source)
    (directory/'SOURCE.json').write_text(json.dumps(source))
    return source

class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);self.source=fixture(self.root)
    def admission(self,text=TEXT,source=None):return assess(ROW,text,self.source if source is None else source,self.root)
    def test_valid_source_and_local_proofs_pass(self):
        self.assertTrue(self.admission()['admitted']);self.assertEqual(audit(self.root,True)['errors'],[])
    def test_missing_source_and_spoofed_historical_flag_rejected(self):
        (self.root/'design-md/example/SOURCE.json').unlink()
        self.assertTrue(audit(self.root)['errors'])
        self.assertFalse(assess(ROW,TEXT.replace('css_values_observed_roles_inferred','historical_unverified'),None,self.root)['admitted'])
    def test_legacy_exemption_is_exact_content_only(self):
        text=TEXT.replace('css_values_observed_roles_inferred','historical_unverified')
        legacy={'example':{'sha256':hashlib.sha256(text.encode()).hexdigest()}}
        self.assertTrue(assess(ROW,text,None,self.root,legacy)['admitted'])
        self.assertFalse(assess(ROW,text+'changed',None,self.root,legacy)['admitted'])
    def test_invalid_provenance_and_mapping_rejected(self):
        for key,value in [('source_url','http://'),('final_url','http://['),('captured_at','not-a-date'),('pages',[]),('tokens',{}),('colors',[]),('observations',{'colors':[]}),('screenshots',{})]:
            with self.subTest(key=key):
                src=copy.deepcopy(self.source);src[key]=value
                self.assertFalse(self.admission(source=src)['admitted'])
        for key,value in [('source_url','https://other.com'),('captured_at','2099-01-01T00:00:00Z')]:
            src=copy.deepcopy(self.source);src[key]=value;self.assertFalse(self.admission(source=src)['admitted'])
    def test_token_edit_and_unsupported_claim_rejected(self):
        self.assertFalse(self.admission(TEXT.replace('fontSize: 16px','fontSize: 99px'))['admitted'])
        self.assertFalse(self.admission(TEXT.replace('recreation_verified: false','recreation_verified: true'))['admitted'])
        src=copy.deepcopy(self.source);src['observations']['colors']['#111111']['declaration']='#123456'
        self.assertFalse(self.admission(source=src)['admitted'])
    def test_manual_hold_blocks_audit_index_and_recommendation(self):
        (self.root/'data/source_holds.json').write_text(json.dumps({'example':{'manual_review_required':True,'reason':'wrong brand'}}))
        self.assertFalse(self.admission()['admitted']);self.assertTrue(audit(self.root)['errors'])
        manifest=reconcile(self.root)
        self.assertEqual(manifest['counts']['needs_review_records'],1)
        self.assertEqual(manifest['sites'][0]['coverage_status'],'source_hold')
        self.assertEqual(select(manifest,include_historical=True),[])
    def test_manual_hold_cannot_be_bypassed_through_alias(self):
        with (self.root/'data/sites.csv').open('a') as f:f.write('example-alias,B,Example,https://example.com/\n')
        (self.root/'data/source_holds.json').write_text(json.dumps({'example-alias':{'manual_review_required':True,'reason':'identity review'}}))
        manifest=reconcile(self.root)
        self.assertEqual(manifest['counts']['admitted_records'],0)
        self.assertEqual(manifest['counts']['recommended_sites'],0)
        self.assertEqual(select(manifest),[])

    def test_css_component_values_and_nested_fonts_checked(self):
        from evidence import evidence_check
        for value in ['rgb(18, 52, 86)','hsl(210 65% 20%)']:
            data=parse_document(TEXT.replace('backgroundColor: "{colors.primary}"',f'backgroundColor: "{value}"'))
            self.assertTrue(evidence_check(data,self.source))
        data=parse_document(TEXT);data['components']['button']['hover']={'fontFamily':'Imaginary, Arial'}
        self.assertTrue(evidence_check(data,self.source))
    def test_malformed_css_dimensions_and_nonfinite_values_rejected(self):
        for before,after in [('fontSize: 16px','fontSize: banana'),('fontSize: 16px','fontSize: calc(banana)'),('fontWeight: 400','fontWeight: 1001'),('lineHeight: 1.5','lineHeight: .nan'),('lineHeight: 1.5','lineHeight: -.inf')]:
            self.assertFalse(validate(TEXT.replace(before,after))['valid'])
    def test_historical_requires_opt_in_but_measured_reference_is_preferred(self):
        row={**ROW,'categories':['A'],'admitted':True,'quality_tier':'historical_archive','recommended_reference':None}
        self.assertEqual(select({'sites':[row]}),[])
        self.assertEqual(len(select({'sites':[row]},include_historical=True)),1)
        row['recommended_reference']='design-md/example/MEASURED.md'
        result=select({'sites':[row]});self.assertEqual(result[0]['tier'],'measured_components');self.assertFalse(result[0]['recreation_verified'])

class CaptureTests(unittest.TestCase):
    def test_failed_or_incomplete_recapture_never_reuses_old_success(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);state=begin(root,ROW['url']);finish(root,state,{'source_url':ROW['url']})
            self.assertEqual(load_capture(root,ROW['url'])['capture_id'],state['capture_id'])
            newer=begin(root,ROW['url'])
            with self.assertRaises(ValueError):load_capture(root,ROW['url'])
            finish(root,newer,reason='challenge')
            with self.assertRaises(ValueError):load_capture(root,ROW['url'])
            with self.assertRaises(ValueError):finish(root,state,{'source_url':ROW['url']})
    def test_capture_identity_url_and_hash_must_match(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);state=begin(root,ROW['url']);finish(root,state,{'source_url':ROW['url']})
            with self.assertRaises(ValueError):load_capture(root,'https://other.com')
            data=json.loads((root/'capture.json').read_text());data['capture_id']='older';(root/'capture.json').write_text(json.dumps(data))
            with self.assertRaises(ValueError):load_capture(root,ROW['url'])

class MeasurementAndParsingTests(unittest.TestCase):
    def test_css_selectors_are_not_palette_values(self):
        values=[value for _,_,value in declarations('#add-item-form{color:rgb(17,17,17);background:var(--surface,#fff)}')]
        colors={color for v in values for _,color in color_literals(v)}
        self.assertEqual(colors,{'#111111','#ffffff'})
        self.assertEqual(font_families('"Inter 18pt", "Knockout No.67", sans-serif'),['Inter 18pt','Knockout No.67','sans-serif'])
    def test_measurements_cannot_claim_whole_site_validation(self):
        data={'schema_version':1,'requested_url':ROW['url'],'source_url':ROW['url'],'captured_at':DATE,'visual_validation':{'status':'passed'},'viewports':[]}
        errors=validate_measurements(data,ROW)
        self.assertTrue(any('Whole-site' in e for e in errors));self.assertTrue(any('desktop' in e for e in errors))
    def test_pixel_check_detects_changes_and_viewport_mismatch(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);a=root/'a.png';b=root/'b.png'
            Image.new('RGB',(20,20),'white').save(a);Image.new('RGB',(20,20),'white').save(b)
            self.assertTrue(compare(a,b)['passed'])
            Image.new('RGB',(20,20),'black').save(b);self.assertFalse(compare(a,b)['passed'])
            Image.new('RGB',(21,20),'white').save(b);self.assertEqual(compare(a,b)['reason'],'viewport_size_mismatch')

if __name__=='__main__':unittest.main()
