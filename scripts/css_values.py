"""CSS declaration/value parsing shared by capture and validation."""
import math
import re
from urllib.parse import unquote
from xml.etree import ElementTree
import tinycss2
from coloraide import Color

REF_RE=re.compile(r'\{(?:colors|typography|rounded|spacing)\.[^{}]+\}')
GENERIC_FONTS={'serif','sans-serif','monospace','system-ui','-apple-system','blinkmacsystemfont','cursive','fantasy','emoji','ui-serif','ui-sans-serif','ui-monospace','ui-rounded'}
COLOR_FUNCTIONS={'rgb','rgba','hsl','hsla','hwb','lab','lch','oklab','oklch','color'}

def normalize_color(value):
    try:
        color=Color(str(value).strip()).convert('srgb').clip()
        if not all(math.isfinite(x) for x in color.coords()+[color.alpha()]):return None
        return color.to_string(hex=True,compress=False).lower()
    except (ValueError,TypeError):return None

def color_literals(value):
    """Return actual CSS color tokens; never selector IDs, strings or URL fragments."""
    if not isinstance(value,str):return []
    value=REF_RE.sub('var(--design-reference)',value)
    result=[]
    def walk(tokens):
        for t in tokens:
            if t.type=='url' or t.type=='function' and t.lower_name=='url':
                uri=t.value if t.type=='url' else next((x.value for x in t.arguments if x.type=='string'),'')
                if re.match(r'^data:image/svg\+xml(?:;charset=[\w-]+|;utf8)?,',uri,re.I) and len(uri)<100000:
                    try:
                        svg=unquote(uri.split(',',1)[1])
                        if '<!DOCTYPE' in svg.upper():continue
                        for node in ElementTree.fromstring(svg).iter():
                            for prop in ('fill','stroke','color'):
                                if prop in node.attrib:
                                    color=normalize_color(node.attrib[prop])
                                    if color:result.append((node.attrib[prop],color))
                    except (ValueError,ElementTree.ParseError):pass
            if t.type in ('hash','ident') or t.type=='function' and t.lower_name in COLOR_FUNCTIONS:
                literal=t.serialize();normalized=normalize_color(literal)
                if normalized:result.append((literal,normalized))
            elif t.type=='function' and t.lower_name=='var':
                comma=next((i for i,x in enumerate(t.arguments) if x.type=='literal' and x.value==','),None)
                if comma is not None:walk(t.arguments[comma+1:])
            elif t.type=='function' and t.lower_name!='url':
                walk(t.arguments)
    walk(tinycss2.parse_component_value_list(value,skip_comments=True))
    return result

def declarations(css, inline=False):
    """Yield (selector, property, value) for real declarations, including nested rules."""
    def walk(nodes,selector='inline-style'):
        for n in nodes:
            if n.type=='declaration':yield selector,n.lower_name,tinycss2.serialize(n.value).strip()
            elif n.type in ('qualified-rule','at-rule') and n.content is not None:
                label=tinycss2.serialize(n.prelude).strip() if n.type=='qualified-rule' else '@'+n.lower_at_keyword
                yield from walk(tinycss2.parse_blocks_contents(n.content,skip_whitespace=True,skip_comments=True),label)
    nodes=tinycss2.parse_blocks_contents(css,skip_whitespace=True,skip_comments=True) if inline else tinycss2.parse_stylesheet(css,skip_whitespace=True,skip_comments=True)
    yield from walk(nodes)

def font_families(value):
    if not isinstance(value,str) or 'var(' in value or REF_RE.search(value):return []
    tokens=tinycss2.parse_component_value_list(re.sub(r'!important\s*$','',value,flags=re.I),skip_comments=True)
    result=[];part=[]
    for t in tokens+[None]:
        if t is None or t.type=='literal' and t.value==',':
            clean=[x for x in part if x.type!='whitespace']
            family=clean[0].value if len(clean)==1 and clean[0].type=='string' else ''.join(t.serialize() for t in part).strip()
            if family and family.lower() not in ('inherit','initial','unset','revert','revert-layer'):result.append(family)
            part=[]
        else:part.append(t)
    return result

def property_key(key):return re.sub(r'[-_]','',str(key)).lower()

def style_leaves(value,path=''):
    if isinstance(value,dict):
        for k,v in value.items():yield from style_leaves(v,path+'.'+str(k) if path else str(k))
    elif isinstance(value,list):
        for i,v in enumerate(value):yield from style_leaves(v,path+f'[{i}]')
    else:yield path,value

LENGTH=re.compile(r'^-?(?:\d+(?:\.\d*)?|\.\d+)(?:px|r?em|%|[sld]?v[wh]|vmin|vmax|ch|ex|cap|ic|lh|rlh|cm|mm|in|pt|pc)?$')

def valid_length(value,negative=True,unitless=False):
    if isinstance(value,(int,float)) and not isinstance(value,bool):return math.isfinite(value) and (negative or value>=0)
    if not isinstance(value,str) or not value.strip():return False
    if REF_RE.fullmatch(value):return True
    if value in ('normal','inherit','initial','unset','revert','auto','min-content','max-content','fit-content'):return True
    if re.fullmatch(r'(?:calc|clamp|min|max|var)\(.+\)',value):
        def expression_ok(tokens):
            for token in tokens:
                if token.type=='error':return False
                if token.type=='ident' and not token.value.startswith('--'):return False
                if token.type=='function' and (token.lower_name not in ('calc','clamp','min','max','var') or not expression_ok(token.arguments)):return False
                if token.type=='() block' and not expression_ok(token.content):return False
                if token.type=='dimension' and not LENGTH.fullmatch(token.serialize()):return False
            return True
        return expression_ok(tinycss2.parse_component_value_list(value)) and not re.search(r'\b(?:nan|infinity)\b',value,re.I)
    if not LENGTH.fullmatch(value):return False
    number=float(re.match(r'^-?[\d.]+',value)[0])
    return (negative or number>=0) and (unitless or number==0 or not re.fullmatch(r'-?[\d.]+',value))

def validate_styles(data):
    errors=[]
    for path,value in style_leaves({k:data.get(k,{}) for k in ('colors','typography','rounded','spacing','components')}):
        key=property_key(path.rsplit('.',1)[-1].split('[')[0])
        if isinstance(value,float) and not math.isfinite(value):errors.append('Non-finite style value: '+path);continue
        if isinstance(value,str) and REF_RE.fullmatch(value):continue
        if key.endswith('color') or key=='colors' or path.startswith('colors.'):
            if not (isinstance(value,str) and (normalize_color(value) or value in ('currentColor','inherit','initial','unset') or re.fullmatch(r'var\(--[\w-]+(?:,[^;]+)?\)',value))):errors.append('Invalid CSS color: '+path)
        if key=='fontfamily' and (not isinstance(value,str) or not value.strip() or (not font_families(value) and 'var(' not in value)):errors.append('Invalid font family: '+path)
        if key=='fontsize' and not valid_length(value,negative=False):errors.append('Invalid font size: '+path)
        if key=='fontweight':
            numeric=isinstance(value,(int,float)) and not isinstance(value,bool) or isinstance(value,str) and re.fullmatch(r'\d+(?:\.\d+)?',value)
            if not (numeric and 1<=float(value)<=1000 or value in ('normal','bold','bolder','lighter','inherit','initial','unset')):errors.append('Invalid font weight: '+path)
        if key=='lineheight' and not valid_length(value,negative=False,unitless=True):errors.append('Invalid line height: '+path)
        if key=='letterspacing' and not valid_length(value):errors.append('Invalid letter spacing: '+path)
        if path.startswith(('rounded.','spacing.')) and not valid_length(value,negative=path.startswith('spacing.'),unitless=True):errors.append('Invalid dimension: '+path)
    return errors

def resolve_local_variables(value,bindings):
    pattern=re.compile(r'var\(\s*(--[\w-]+)\s*(?:,\s*([^()]*))?\)')
    for _ in range(12):
        updated=pattern.sub(lambda m:bindings.get(m[1],m[2] if m[2] is not None else m[0]),value)
        if updated==value:break
        value=updated
    return value


def style_color_literals(path,value):
    key=property_key(path.rsplit('.',1)[-1])
    if 'font' in key:return []
    literals=color_literals(value)
    if path.startswith('colors.') or any(p in key for p in ('color','background','border','shadow','outline','fill','stroke')):return literals
    return [(literal,color) for literal,color in literals if literal.startswith('#') or '(' in literal]
