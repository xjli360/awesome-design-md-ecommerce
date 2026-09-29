#!/usr/bin/env python3
"""
Build the public collection artifacts from the generated DESIGN.md files.

Outputs:
  INDEX.md          full, browsable index of every brand, grouped by category
  data/brands.csv   slug,category,brand_name,url for every completed brand
  _state/_featured.md     (dev) featured-brand bullets, for hand-assembling README
  _state/_categories.md   (dev) marquee-category <details> blocks, for README

Source of truth: public data/sites.csv, plus explicit URL aliases and source holds.
"""

import csv
import io
import json
from collection import reconcile
from design_system import atomic_write, parse_document
import re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parent.parent
DESIGN_DIR = ROOT / "design-md"
SELECTED = ROOT / "_state" / "selected.csv"
BRANDS_CSV = ROOT / "data" / "brands.csv"
INDEX = ROOT / "INDEX.md"
FEAT_OUT = ROOT / "_state" / "_featured.md"
CATS_OUT = ROOT / "_state" / "_categories.md"

DESC_RE = re.compile(r"^description:\s*(.+?)(?=\n[a-z_-]+:|\n---|\n## )", re.MULTILINE | re.DOTALL)

# Instantly-recognizable names to spotlight on the README front page.
# Any slug not present in the collection is silently skipped.
FEATURED = [
    "glossier", "aesop", "the-ordinary", "ordinary", "drunk-elephant", "fenty-beauty",
    "rare-beauty", "merit", "kosas", "saie", "tower-28", "youth-to-the-people",
    "summer-fridays", "topicals", "starface", "caraway", "our-place", "hexclad",
    "made-in", "great-jones", "smithey", "material-kitchen", "brooklinen", "parachute",
    "buffy", "casper", "cozy-earth", "quince", "saatva", "hay", "muuto", "blueland",
    "ritual", "hims", "peloton", "dyson", "roborock", "eufy", "coyuchi", "jones-road",
    "milk-makeup", "ilia-beauty",
]

# Marquee consumer-DTC categories to surface in the README "browse by category"
# section. The long tail (tech, gaming, music, books, ...) lives in INDEX.md.
MARQUEE_CATS = [
    "Skincare", "Makeup", "Haircare", "Body Care", "Bath", "Fragrance", "Oral Care",
    "Men's Grooming", "Cookware", "Kitchen Tools", "Dinnerware", "Bedding", "Decor",
    "Furniture", "Candles & Scent", "Vitamins & Supplements",
]

# High-level domains for the README overview table. Order matters (first match wins
# only for exact category names listed here; everything else rolls up to "More").
THEME_MAP = {
    "Beauty & Personal Care": [
        "Skincare", "Makeup", "Haircare", "Body Care", "Bath", "Bath/Shower",
        "Fragrance", "Men's Grooming", "Oral Care", "Feminine Care",
    ],
    "Health & Wellness": [
        "Vitamins & Supplements", "Wellness", "Women's Health", "Men's Health",
        "OTC/Wellness", "Tools/Devices", "Elderly Care",
    ],
    "Kitchen & Cookware": [
        "Cookware", "Kitchen Tools", "Dinnerware", "Small Kitchen Appliances",
        "Espresso Machines", "Grills/BBQ", "Pizza ovens", "Microwaves/Toaster Ovens",
        "Ranges/Cooktops/Ovens",
    ],
    "Home & Living": [
        "Bedding", "Decor", "Furniture", "Office Chairs", "Desks", "Organization",
        "Cleaning Supplies", "Laundry Products", "Vacuums", "Robotic Cleaners",
        "Air Purifiers", "Water Filtration/Dispensers", "Refrigerators", "Dishwashers",
        "Washers/Dryers", "HVAC/Portable AC/Heaters", "Smart Home & Appliances",
        "Candles & Scent", "Office Storage & Filing", "Office Specialty",
    ],
    "Outdoor & Garden": [
        "Outdoor furniture", "Outdoor", "Outdoor Apparel", "Outdoor Accessories",
        "Camping & Hiking Gear", "Hunting & Fishing", "Patio dining",
        "Fire pits/outdoor heaters", "Outdoor lighting", "Garden tools",
        "Lawn care equipment/mowers", "Seeds/plants nurseries", "Urban gardening",
        "Greenhouses/raised beds", "Pools/hot tubs/swim spas", "Planters/Pots",
        "Garden decor", "Outdoor rugs/textiles", "Wooden",
    ],
    "Sport & Fitness": [
        "Fitness & Gym", "Cycling", "Running", "Yoga", "Climbing", "Watersports",
        "Winter Sports", "Team Sports",
    ],
    "Baby & Kids": [
        "Baby Care", "Baby Clothing", "Baby/Infant", "Baby Toys", "Nursery Furniture",
        "Nursery Decor", "Strollers", "Carriers", "Feeding", "Educational", "STEM",
    ],
    "Stationery & Desk": [
        "Stationery & Paper", "Notebooks & Journals", "Pens & Writing",
        "Desk Accessories & Organizers", "Planners", "Paper Goods",
        "Labels & Markers & Highlighters", "Whiteboards & Cork boards",
        "Specialty Paper & Cards", "Monitor Arms & Stands", "Shredders & Calculators",
        "Printing services (DTC)", "Printer & Ink", "Arts & Crafts",
    ],
    "Tech & Computing": [
        "Cell Phones & Accessories", "Keyboards", "Mice", "Laptops",
        "Desktops/PCs/Builders", "Monitors", "Networking", "Docking stations/hubs",
        "Storage/SSDs", "Cables/Adapters", "Cooling/PC Parts", "Graphics Tablets",
        "Webcams", "Laptop Bags", "Measurement & Test Instruments",
        "Lab Equipment & Supplies", "Accessories",
    ],
    "Gaming & Collectibles": [
        "Board Games", "Card Games", "Tabletop RPG", "Trading Cards", "Controllers",
        "Gaming Chairs", "Gaming Desks", "VR Hardware", "Retro Game Retailer",
        "Arcade Maker", "AAA Publisher Store", "Indie Studio Merch", "Puzzles",
        "Action Figures", "Plush", "Collectibles", "Gear/Playmats",
    ],
    "Music & Instruments": [
        "Independent Record Store - US", "Independent Record Store - UK/EU",
        "Independent Record Store - Asia/Other", "Record Label with Shop",
        "Audiophile/Hi-Res Label", "Vinyl Pressing Plant", "DJ Gear",
        "Studio Monitors", "Wind Instruments", "Orchestral", "Ukuleles",
        "Audiobook DTC",
    ],
    "Books & Media": [
        "Independent Bookstore", "Specialty Bookstore", "Children's Bookstore",
        "Used/Rare Bookseller", "Comic Book Store", "Small Press Publisher",
        "Academic/University Press", "Zine/Art Book Publisher", "Book Subscription Box",
        "Movies & TV", "Niche Genre Store", "Import Shop",
    ],
}


_DANGLING = re.compile(r"[\s—,;:]+(?:of|and|with|in|on|to|a|an|the|that|by|as|for|from)"
                       r"\s*([.!?])\s*$", re.IGNORECASE)


def _polish(s: str) -> str:
    s = re.sub(r"\s*—\s*([.!?])", r"\1", s)   # trailing dash before period
    s = _DANGLING.sub(r"\1", s)                # drop dangling preposition+period
    s = re.sub(r"\s*—\s*$", "", s).strip(" —,;:")
    return s


def first_sentence(text: str) -> str:
    text = text.strip().replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"`[^`]+`", "", text)        # strip inline-code tokens
    text = re.sub(r"\{[^}]+\}", "", text)       # strip token refs
    text = re.sub(r"\([^)]*\b(?:meta|theme-color|token|var)\b[^)]*\)", "", text)  # stripped-token parens
    text = re.sub(r"\(\s*\)", "", text)         # collapse empty parens left behind
    text = re.sub(r"\s*—\s*—\s*", " — ", text)  # collapse doubled em-dash
    text = re.sub(r"\s+([,.;:])", r"\1", text)  # tighten punctuation
    text = re.sub(r"\s+", " ", text).strip()
    m = re.match(r"^(.{40,180}?[.!?])\s", text)
    out = m.group(1).strip() if m else ((text[:180].rstrip() + "…") if text else "")
    return _polish(out)


def read_hook(slug: str) -> str:
    p = DESIGN_DIR / slug / "DESIGN.md"
    if not p.exists():
        return ""
    return first_sentence(parse_document(p.read_text(encoding="utf-8"))["description"])


def load_rows():
    src = SELECTED if SELECTED.exists() else BRANDS_CSV
    with src.open(newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f)]


def theme_for(cat: str) -> str:
    for theme, cats in THEME_MAP.items():
        if cat in cats:
            return theme
    return "More"


def anchor(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def write_status(manifest):
    counts=manifest['counts']
    pending=[r for r in manifest['sites'] if not r['alias_of'] and not r['generated']]
    reasons=Counter(r.get('source_hold',{}).get('status','pending_review') for r in pending)
    lines=['# Collection status','', '[← README](./README.md) · [Full index](./INDEX.md)','',
           f"{counts['generated_sites']:,} unique URLs have documents; {counts['remaining_sites']:,} remain without a valid source-backed addition.", '',
           'A reviewed hold is not a completed DESIGN.md. Historical files may be unverified; format validation is separate from visual fidelity. Counts include preserved historical URL aliases and do not claim global brand deduplication.','',
           '## Evidence coverage','','| Evidence status | DESIGN.md files |','|---|---:|']
    for status,n in sorted(Counter(r['evidence_status'] for r in manifest['sites'] if r['generated']).items()):lines.append(f'| {status} | {n} |')
    lines+=['','## Unresolved sources','','| Remaining status | Unique URLs |','|---|---:|']
    for status,n in sorted(reasons.items()):lines.append(f'| {status} | {n} |')
    lines+=['','## Sites without documents','','| Brand | Source | Status | Checked | Reason |','|---|---|---|---|---|']
    def cell(s):return str(s).replace('|','\\|').replace('\n',' ')
    for r in sorted(pending,key=lambda r:r['brand_name'].lower()):
        h=r.get('source_hold',{})
        values=[r['brand_name'],f"[website]({r['url']})",h.get('status','pending_review'),h.get('checked_on','—'),h.get('reason','No completed review recorded.')]
        lines.append('| '+' | '.join(cell(v) for v in values)+' |')
    lines+=['','Detailed provenance: [source holds](./data/source_holds.json), [source corrections](./data/source_corrections.json), [manifest](./data/manifest.json).','']
    atomic_write(ROOT/'STATUS.md','\n'.join(lines))


def main():
    manifest = reconcile()
    counts = manifest["counts"]
    if counts["generated_records"] != counts["validated_records"]:
        raise SystemExit("Collection has invalid generated files; run check_format.py before indexing")
    write_status(manifest)
    completed = [r for r in manifest["sites"] if r["validated"]]
    primary = sorted((r for r in completed if not r["alias_of"]), key=lambda r: r["brand_name"].lower())
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(["slug", "category", "brand_name", "url", "canonical_slug", "evidence_status"])
    for row in sorted(completed, key=lambda r: r["brand_name"].lower()):
        writer.writerow([row[k] for k in ("slug", "category", "brand_name", "url", "canonical_slug", "evidence_status")])
    atomic_write(BRANDS_CSV, buf.getvalue())
    by_cat = defaultdict(list)
    for row in primary:
        for category in row["categories"]:
            by_cat[category].append(row)
    order = sorted(by_cat, key=lambda c: (-len(by_cat[c]), c.lower()))
    total = len(primary)
    lines = ["# Full Collection Index", "", "[← Back to README](./README.md)", "",
             f"**{total:,} unique website URLs · {counts['generated_records']:,} DESIGN.md files · {len(by_cat)} categories.**", "",
             "Canonical entries are listed under all their category tags. Historical duplicate files are retained; aliases and evidence status are recorded in [data/manifest.json](./data/manifest.json). Format validation does not establish visual fidelity.", "",
             " · ".join(f"[{c}](#category-{i+1})" for i, c in enumerate(order)), ""]
    for i, category in enumerate(order):
        lines += [f'<a id="category-{i+1}"></a>', f"## {category} ({len(by_cat[category])})", ""]
        for row in by_cat[category]:
            hook = read_hook(row["slug"])
            lines.append(f"- [**{row['brand_name']}**](./design-md/{row['slug']}/DESIGN.md) — {hook}")
        lines.append("")
    atomic_write(INDEX, "\n".join(lines))
    readme = ROOT / "README.md"
    text = readme.read_text()
    stats = ("<!-- collection-stats:start -->\n"
             f"**{total:,} unique website URLs · {counts['generated_records']:,} DESIGN.md files · {len(by_cat)} categories.**\n\n"
             f"Target: {counts['target_sites']:,} unique URLs from {counts['target_records']:,} selected records; "
             f"**{counts['remaining_sites']:,} unique URLs remain**. Historical aliases are preserved. "
             "See [collection status](./STATUS.md) for unresolved sources and [the manifest](./data/manifest.json) for canonical IDs, category tags, validation and evidence status.\n"
             "<!-- collection-stats:end -->")
    text = re.sub(r"<!-- collection-stats:start -->.*?<!-- collection-stats:end -->", lambda _: stats, text, flags=re.S)
    # Keep badges and every generated count under one source of truth.
    text = re.sub(r"badge/brands-[^-]+-0a0a0a", f"badge/sites-{total:,}".replace(",", "%2C") + "-0a0a0a", text)
    text = re.sub(r"badge/sites-[^-]+-0a0a0a", f"badge/sites-{total:,}".replace(",", "%2C") + "-0a0a0a", text)
    text = re.sub(r"badge/categories-\d+-444444", f"badge/categories-{len(by_cat)}-444444", text)
    text = re.sub(r"Browse all [\d,]+ brands", f"Browse all {total:,} canonical websites", text)
    text = re.sub(r"Browse all [\d,]+ canonical websites", f"Browse all {total:,} canonical websites", text)
    themes = defaultdict(int)
    for row in primary:
        themes[theme_for(row["category"])] += 1
    table = "| Domain | Unique websites |\n|---|--:|\n" + "\n".join(f"| {name} | {count} |" for name, count in sorted(themes.items(), key=lambda kv: -kv[1]))
    text = re.sub(r"<!-- domain-table:start -->.*?<!-- domain-table:end -->", lambda _: "<!-- domain-table:start -->\n" + table + "\n<!-- domain-table:end -->", text, flags=re.S)
    atomic_write(readme, text)
    banner = ROOT / "assets/hero.svg"
    if banner.exists():
        svg = banner.read_text()
        svg = re.sub(r"across [\d,]+ brands and \d+ categories", f"across {total:,} unique website URLs and {len(by_cat)} category tags", svg)
        svg = re.sub(r"across [\d,]+ unique website URLs and \d+ category tags", f"across {total:,} unique website URLs and {len(by_cat)} category tags", svg)
        svg = re.sub(r"[\d,]+ brands · \d+ categories · \d+ domains", f"{total:,} sites · {len(by_cat)} categories · evidence-labelled", svg)
        svg = re.sub(r"[\d,]+ sites · \d+ categories · evidence-labelled", f"{total:,} sites · {len(by_cat)} categories · evidence-labelled", svg)
        atomic_write(banner, svg)
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
