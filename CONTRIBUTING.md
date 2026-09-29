# Contributing to awesome-design-md-ecommerce

This collection documents the design systems of e-commerce storefronts across many categories as plain-text `DESIGN.md` token files that AI agents can read to generate consistent, brand-faithful UI.

The format follows the [`awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) specification.

## Adding a New Brand

1. Pick a brand that is genuinely DTC (sells directly to consumer, not just a marketplace listing).
2. Create a folder under `design-md/` using a lowercase, hyphenated slug derived from the brand name (e.g. `our-place`, `caraway`, `nothing`).
3. Inside that folder, add a `DESIGN.md` following the 9-section structure described below.
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

Run `uv run --with pyyaml python scripts/check_format.py` before submitting. The
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
