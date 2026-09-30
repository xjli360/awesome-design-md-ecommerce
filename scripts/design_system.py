"""Shared strict parsing, validation, safe writes and canonical site identities."""
from __future__ import annotations
import csv
import json
import os
import re
import tempfile
from pathlib import Path
from urllib.parse import urlsplit
import yaml
from css_values import validate_styles

ROOT = Path(__file__).resolve().parent.parent
BLOCKS = ('colors', 'typography', 'rounded', 'spacing', 'components')
HEADINGS = ('## Components', '## Responsive Behavior', '## Known Gaps')
REF = re.compile(r'\{(colors|typography|rounded|spacing)\.([^{}]+)\}')
HEX = re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$')

class StrictLoader(getattr(yaml, 'CSafeLoader', yaml.SafeLoader)):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        try:
            duplicate = key in result
        except TypeError:
            raise yaml.constructor.ConstructorError(None, None, 'non-scalar mapping key', k.start_mark)
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f'duplicate key: {key}', k.start_mark)
        result[key] = loader.construct_object(v, deep=deep)
    return result

StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def canonical_url(url):
    p = urlsplit(normalize_url(url))
    return (p.hostname or '').lower().removeprefix('www.') + p.path.rstrip('/')

def normalize_url(url):
    url = url.strip()
    return url if '://' in url else 'https://' + url

def load_sites(root=ROOT):
    source = next((root / p for p in ('data/sites.csv', '_state/selected.csv', 'data/brands.csv') if (root / p).exists()), None)
    if source is None:
        raise ValueError('No metadata; provide data/sites.csv')
    with source.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    slugs = set()
    for r in rows:
        r['url'] = normalize_url(r.get('url', ''))
        slug = r.get('slug', '')
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', slug) or slug in slugs:
            raise ValueError(f'Invalid or duplicate slug: {slug}')
        if urlsplit(r.get('url', '')).scheme not in ('http', 'https') or not urlsplit(r['url']).hostname:
            raise ValueError(f'Invalid URL: {slug}')
        slugs.add(slug)
    return rows

def atomic_write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix='.' + path.name, dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)

def parse_document(text):
    if not text.startswith('---\n'):
        raise ValueError('File must start with ---')
    match = re.search(r'^## ', text, re.M)
    if not match:
        raise ValueError('Missing Markdown sections')
    data = {}
    for doc in yaml.load_all(text[:match.start()], Loader=StrictLoader):
        if doc is None:
            continue
        if not isinstance(doc, dict):
            raise ValueError('YAML document must be a mapping')
        overlap = set(data) & set(doc)
        if overlap:
            raise ValueError(f'Duplicate keys across documents: {sorted(overlap)}')
        data.update(doc)
    return data

def walk_values(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from walk_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_values(child)
    elif isinstance(value, str):
        yield value

def validate(text, expected_name=None):
    errors, warnings = [], []
    try:
        data = parse_document(text)
    except (ValueError, yaml.YAMLError) as e:
        return dict(valid=False, errors=[str(e)], warnings=[], data={})
    for key in ('version', 'name', 'description'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f'Missing/non-string {key}')
    if expected_name is not None and data.get('name') != expected_name:
        errors.append(f'Brand name mismatch: expected {expected_name!r}')
    positions = [text.find('\n' + b + ':') for b in BLOCKS]
    if any(p < 0 for p in positions) or positions != sorted(positions):
        errors.append('Token blocks missing or out of order')
    for block in BLOCKS:
        if not isinstance(data.get(block), dict) or not data[block]:
            errors.append(f'Missing/empty mapping: {block}')
    for h in HEADINGS:
        m = re.search(r'^' + re.escape(h) + r'\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
        if not m or not m[1].strip():
            errors.append(f'Missing/empty section: {h}')
    hp = [text.find(h) for h in HEADINGS]
    if hp != sorted(hp):
        errors.append('Markdown sections out of order')
    if errors:
        return dict(valid=False, errors=errors, warnings=warnings, data=data)
    errors.extend(validate_styles(data))
    for key, color in data['colors'].items():
        if not isinstance(color, str) or not (HEX.fullmatch(color) or re.fullmatch(r'(?:rgba?|hsla?)\([^\n]+\)|transparent|currentColor|\{colors\.[^{}]+\}', color)):
            errors.append(f'Invalid color: {key}={color!r}')
    for key, style in data['typography'].items():
        if not isinstance(style, dict):
            errors.append(f'Typography {key} must be mapping')
            continue
        for prop in ('fontFamily', 'fontSize', 'fontWeight', 'lineHeight'):
            if prop not in style or style[prop] is None:
                errors.append(f'Typography {key} lacks {prop}')
            elif not isinstance(style[prop], (str, int, float)) or isinstance(style[prop], bool):
                errors.append(f'Typography {key}.{prop} must be scalar')
        if not isinstance(style.get('fontFamily'), str):
            errors.append(f'Typography {key}.fontFamily must be a string')
    for block in ('rounded', 'spacing'):
        for key, value in data[block].items():
            if not isinstance(value, (str, int, float)) or isinstance(value, bool):
                errors.append(f'Invalid {block}.{key}')
    for key, value in data['components'].items():
        if not isinstance(value, dict) or not value:
            errors.append(f'Component {key} must be nonempty mapping')
    def component_colors(value, key=''):
        if isinstance(value, dict):
            for child_key, child in value.items():component_colors(child, str(child_key))
        elif isinstance(value, list):
            for child in value:component_colors(child, key)
        elif isinstance(value, str) and (key.lower().endswith('color') or key.lower()=='colors'):
            if value.startswith('#') and not HEX.fullmatch(value):
                errors.append(f'Invalid component color literal: {value}')
    component_colors(data['components'])
    for value in walk_values({key: data[key] for key in BLOCKS}):
        for scope, key in REF.findall(value):
            if key not in data[scope]:
                errors.append(f'Undefined token: {{{scope}.{key}}}')
    graph = {}
    for block in BLOCKS[:-1]:
        for key, value in data[block].items():
            graph[f'{block}.{key}'] = {f'{s}.{k}' for text in walk_values(value) for s, k in REF.findall(text)}
    visited, active = set(), set()
    def visit(key):
        if key in active:
            errors.append(f'Cyclic token reference: {key}')
            return
        if key in visited:
            return
        active.add(key)
        for child in graph.get(key, ()):
            visit(child)
        active.remove(key)
        visited.add(key)
    for key in graph:
        visit(key)
    if len(set(str(v).lower() for v in data['colors'].values())) < 10:
        warnings.append('Fewer than 10 distinct colors; do not invent colors to pass')
    return dict(valid=not errors, errors=sorted(set(errors)), warnings=warnings, data=data)

def repair_syntax(text, expected_name=None):
    """Serialization repair only: preserve prose and token values."""
    text = text.strip().removeprefix('\ufeff')
    if text.startswith('```'):
        text = re.sub(r'^```\w*\s*\n|\n```\s*$', '', text)
    lines = text.splitlines()
    if expected_name:
        lines = ['name: ' + json.dumps(expected_name, ensure_ascii=False) if l.startswith('name:') else l for l in lines]
    start = next((i for i, l in enumerate(lines) if l.startswith('description:')), None)
    end = next((i for i, l in enumerate(lines) if l.startswith('colors:')), None)
    if start is not None and end is not None and start < end:
        region = lines[start:end]
        closing = '---' in region
        first = lines[start].split(':', 1)[1].strip()
        try:
            # A plain YAML scalar treats ` #abcdef` as a comment. The original
            # prose contains literal palette hexes, so never round-trip that
            # form through a parser which would silently truncate the text.
            if first not in ('|', '|-', '>', '>-') and not (len(first) > 1 and first[0] in ('"', "'") and first[-1] == first[0]):
                raise ValueError('preserve plain prose literally')
            desc = yaml.safe_load('\n'.join(l for l in region if l != '---'))['description']
            if not isinstance(desc, str):
                raise ValueError('not string')
        except (yaml.YAMLError, TypeError, KeyError, ValueError):
            if first in ('|', '|-', '>', '>-'):
                first = ''
            desc = '\n'.join([first] + [l.strip() for l in lines[start + 1:end] if l != '---']).strip()
        replacement = ['description: |-'] + ['  ' + l if l else '' for l in desc.rstrip().splitlines()] + ['']
        if closing:
            replacement += ['---', '']
        lines[start:end] = replacement
    for i, line in enumerate(lines):
        m = re.match(r'^(\s+[A-Za-z][A-Za-z0-9_-]*:)\s+(.+)$', line)
        if not m or not REF.search(m[2]):
            continue
        try:
            value = yaml.safe_load('value: ' + m[2])['value']
            invalid = isinstance(value, dict)
        except yaml.YAMLError:
            invalid = True
        if invalid:
            value = re.sub(r'[\"\'](\{(?:spacing|rounded|colors|typography)\.[^}]+\})[\"\']', r'\1', m[2])
            if re.fullmatch(r'(?:\{(?:spacing|rounded|colors|typography)\.[^}]+\}|[0-9.]+(?:px|rem|em|%)?)(?:\s+(?:\{(?:spacing|rounded|colors|typography)\.[^}]+\}|[0-9.]+(?:px|rem|em|%)?))*', value):
                lines[i] = m[1] + ' ' + json.dumps(value)
    return '\n'.join(lines).rstrip() + '\n'

def attach_evidence(text, source, source_available=True):
    """Make provenance discoverable to readers who open only DESIGN.md."""
    for key, value in [('source_url', source['source_url']), ('captured_at', source['captured_at']), ('evidence_status', source['confidence'])]:
        line = key + ': ' + json.dumps(value, ensure_ascii=False)
        if re.search(r'^' + key + ':', text, re.M):
            text = re.sub(r'^' + key + r':.*$', lambda _: line, text, flags=re.M)
        else:
            text = text.replace('description:', line + '\ndescription:', 1)
    historical=source.get('design_origin')=='historical' or source['confidence'].startswith('historical_')
    for key,value in [('quality_tier','historical_archive' if historical else 'css_reference'),('usage_scope','inspiration_only' if historical else 'style_reference_only'),('layout_status','proposed_not_measured'),('recreation_verified',False)]:
        line=key+': '+json.dumps(value)
        if re.search('^'+key+':',text,re.M):text=re.sub('^'+key+':.*$',lambda _:line,text,flags=re.M)
        else:text=text.replace('description:',line+'\ndescription:',1)
    if source_available:
        text = re.sub(r'^- \*\*Historical provenance:\*\*.*\n', '', text, flags=re.M)
    if source_available and '[SOURCE.json](./SOURCE.json)' not in text:
        note = '- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.\n'
        text = text.replace('## Known Gaps\n', '## Known Gaps\n\n' + note, 1)
    elif not source_available and '**Historical provenance:**' not in text:
        note = '- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.\n'
        text = text.replace('## Known Gaps\n', '## Known Gaps\n\n' + note, 1)
    return text
