# Contributing to awesome-design-md-ecommerce

This collection documents the design systems of e-commerce storefronts across many categories as plain-text `DESIGN.md` token files that AI agents can read to generate consistent UI with explicit evidence limits.

The format follows the [`awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) specification.

## Adding a New Brand

1. Pick a brand that is genuinely DTC (sells directly to consumer, not just a marketplace listing).
2. Create a folder under `design-md/` using a lowercase, hyphenated slug derived from the brand name (e.g. `our-place`, `caraway`, `nothing`).
3. Add a `DESIGN.md` plus schema-version-2 `SOURCE.json`, following the structure and evidence rules below.
4. Open a PR. One brand per PR.

## DESIGN.md Structure

Every `DESIGN.md` must contain these nine sections, in this order:

| Section | Content |
|---|---|
| YAML frontmatter | `version`, `name`, `description` (evidence-grounded brand-design summary) |
| `colors:` | Semantic token names → hex values. Include neutrals, surfaces, accents, semantic roles. |
| `typography:` | Each scale step has `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`. |
| `rounded:` | Border-radius scale (`xs`, `sm`, `md`, `lg`, `xl`, `full`). |
| `spacing:` | Spacing scale (`xxs`–`section`). |
| `components:` | Buttons, cards, inputs, navigation, etc. Each with token references in `{namespace.key}` form. |
| `## Components` (Markdown) | Prose descriptions of each component with state variants. |
| `## Responsive Behavior` | Breakpoint table + touch target + collapse strategy notes. |
| `## Known Gaps` | What couldn't be extracted reliably (hover states, error states, sub-brands, etc.). |

## Quality Bar

- **Real tokens, not invented ones.** New colors and font stacks must be sampled from the live site; inferred roles and historical gaps must be labelled.
- **Description must capture brand voice**, not just list visual attributes. Read like editorial copy, not a tech spec.
- **Slug is canonical**: `airbnb`, not `Airbnb` or `air-bnb`.

## License

By contributing, you agree your work is licensed under the project's MIT License.

## Validation and evidence

Run `uv run --with-requirements requirements.txt python scripts/check_format.py` before submitting. The
check exits nonzero for invalid YAML, duplicate keys, missing fields, empty
sections, malformed values, name mismatches or unresolved token references.
Descriptions must use an indented YAML block scalar (`description: |-`). Quote a
whole CSS shorthand as one scalar, e.g. `padding: "{spacing.sm} {spacing.lg}"`.
A small genuine palette is acceptable; never add colors just to reach a quota.

Add the canonical URL to `data/sites.csv`, then run `scripts/build_index.py` in the
same Python environment. URLs are deduplicated across categories; preserve old
slug files and record aliases through the generated manifest. Metadata and
README counts are generated together. Do not hand-edit the generated markers.

New automated entries include `SOURCE.json`: capture time, URLs, HTTP status,
content hashes, palette/font evidence and per-token evidence status. CSS presence
only establishes the value, not its semantic role or computed appearance.
Components, roles, measurements and responsive behavior remain inferred unless
separately measured. Historical files are marked `historical_unverified`.

Every new or changed reference must pass `scripts/check_format.py`, `scripts/check_evidence.py`, `scripts/check_measurements.py` and the unit tests. SOURCE.json is mandatory unless the document exactly matches the frozen `data/legacy_documents.json` archive. Do not extend that registry or rewrite its hashes to bypass validation. Manual source HOLDs block workers, admission and default recommendations until the source review is resolved.

Each observed color/font needs a parseable declaration excerpt bound to a source-page URL and snapshot hash. Every token record includes its exact current value. CI verifies published excerpts; `check_evidence.py --require-snapshots` additionally requires retained raw evidence and checks its hashes and declaration membership. These checks establish provenance consistency, not independent site authenticity. Explicit opacity derivatives must retain their observed base and be labelled as proposals.

Quality tiers are separate: `historical_archive` is inspiration only; `css_reference` establishes values while roles/layout remain proposed; `MEASURED.md` records sampled component geometry/styles at three viewports. Measured sibling files do not upgrade historical DESIGN.md tokens. Full-site recreation verification remains false until an independently rendered implementation has been reviewed against source screenshots. Fonts and product assets are not included by this collection.
