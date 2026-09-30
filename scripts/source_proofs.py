"""Build and verify minimal declaration proofs against retained snapshot hashes."""
import hashlib
from css_values import declarations,color_literals,font_families,normalize_color,resolve_local_variables
from extract_site import Page

def iter_snapshot_declarations(raw,name):
    text=raw.decode('utf-8','replace')
    if name.endswith('.css'):yield from declarations(text)
    elif name.endswith('.html'):
        parser=Page();parser.feed(text)
        for part in parser.styles:yield from declarations(part,inline='{' not in part)

def collect_proofs(source,directory,colors=None,fonts=None):
    wanted_colors=set(colors or source.get('colors',{}));wanted_fonts={}
    for f in (fonts or source.get('font_families',{})):wanted_fonts.setdefault(f.casefold(),set()).add(f)
    found={'colors':{},'font_families':{}}
    for page in source.get('pages',[]):
        path=directory/page['snapshot']
        if not path.is_file():continue
        raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=page['sha256']:raise ValueError('Changed evidence: '+str(path))
        rows=list(iter_snapshot_declarations(raw,path.name));bindings={}
        for sel,prop,val in rows:
            if prop.startswith('--'):bindings.setdefault(sel,{})[prop]=val
        for selector,prop,value in rows:
            proof={'selector':selector[:300],'property':prop,'declaration':value,'url':page['final_url'],'snapshot':page['snapshot'],'sha256':page['sha256']}
            local=bindings.get(selector,{})
            needed={k:v for k,v in local.items() if k in value}
            if needed:proof['bindings']=needed
            for _,color in color_literals(resolve_local_variables(value,local)):
                if color in wanted_colors and color not in found['colors']:found['colors'][color]=proof
            if prop=='font-family' or prop.startswith('--') and 'font' in prop and 'family' in prop:
                for family in font_families(value):
                    for key in wanted_fonts.get(family.casefold(),[]):
                        if key not in found['font_families']:found['font_families'][key]=proof
        if wanted_colors<=set(found['colors']) and set().union(*wanted_fonts.values())<=set(found['font_families']):break
    return found

def verify_source_proofs(source,directory):
    groups=source.get('observations',{});needed={}
    for kind in ('colors','font_families'):
        for value,proof in groups.get(kind,{}).items():needed.setdefault(proof.get('snapshot'),[]).append((kind,value,proof))
    errors=[]
    for name,items in needed.items():
        if not isinstance(name,str) or '/' in name or '\\' in name or name in ('.','..'):continue
        p=directory/name
        if not p.exists():continue # Public CI verifies excerpts; strict-local also requires raw files.
        actual={(selector[:300],prop,value) for selector,prop,value in iter_snapshot_declarations(p.read_bytes(),name)}
        for kind,value,proof in items:
            if (proof.get('selector'),proof.get('property'),proof.get('declaration')) not in actual:errors.append('Declaration absent from snapshot: '+value)
            for key,val in proof.get('bindings',{}).items():
                if (proof.get('selector'),key,val) not in actual:errors.append('Variable binding absent from snapshot: '+key)
    return errors
