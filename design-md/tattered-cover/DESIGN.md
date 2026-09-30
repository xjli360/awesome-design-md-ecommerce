---
version: alpha
name: "Tattered Cover"
source_url: "https://www.tatteredcover.com"
captured_at: "2026-09-28T10:32:51.043760+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Tattered Cover's storefront CSS exposes a restrained neutral palette anchored
  by near-black ink (#1c1c1c), off-white surfaces (#f5f5f5, #ffffff), and a
  cluster of mid-grey borders and dividers (#cccccc, #dddddd, #bbbbbb, #c1c1c1,
  #c4c4c4, #696969, #757575, #767676). Two dark forest-green values (#1f4324,
  #204325) and a dark slate (#21282d) appear in the theme variables; because no
  selector confirms their applied role, this spec treats #1f4324 as the
  inferred brand primary (buttons, links, accents) and #21282d as a secondary
  ink for header/footer surfaces, reusing greys for hairlines and muted text.
  Font stacks list Figtree, Figtree_Medium and Muli as the sans-serif working
  families, with DellaRobbia and Poynter present as likely licensed
  display/serif faces suited to a literary retailer's headline voice, and
  Georgia as the serif fallback. A monospace stack (Consolas, SFMono, Menlo,
  etc.) is present but unassigned to any observed element and is treated as a
  system utility fallback rather than brand typography. Sizing tokens
  (--text-xs through --text-xl, 0.75rem–1.25rem) and section spacing (4rem,
  3rem gutter) are taken directly from :root and mapped into the scale below;
  larger display sizes are proposed extrapolations, not measured values.

colors:
  primary: "#1f4324"
  primary-alt: "#204325"
  secondary: "#21282d"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-subtle: "#cccccc"
  border-strong: "#bbbbbb"
  neutral-200: "#c4c4c4"
  neutral-300: "#c1c1c1"
  neutral-400: "#696969"
  neutral-500: "#757575"
typography:
  display-xl: {fontFamily: "DellaRobbia, Georgia, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poynter, Georgia, serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Muli, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree_Medium, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.3px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-subtle}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-subtle}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  staff-pick-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary-alt}"
    titleTypography: "{typography.title-md}"
    noteTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** — Solid forest-green fill (#1f4324) with white text, intended for primary calls to action such as "Add to Cart" or "Subscribe." The CSS confirms a generic `.button` pattern with border-radius and a background/hover gradient swap, but the exact hover color is not resolvable from static evidence, so hover state is proposed.

**button-secondary** — An outline variant derived from the theme's `.button--outline` rule, which explicitly borrows `--text-color`/`--border-color` custom properties. Mapped here to the primary green on a transparent background; used for lower-emphasis actions like "View all."

**text-input** — A plain bordered field using the light grey hairline for its outline and near-black ink for typed text, proposed for the email subscribe field and search box since no dedicated input styling was captured.

**nav-bar** — Reflects the observed header grid (`--header-grid`, logo/primary-nav/secondary-nav areas) and padding tokens (1rem–1.6rem). Background is treated as white/canvas with a hairline separator (`--header-separation-border-color: 28 28 28 / 0.15`), consistent with the greys in the palette.

**product-card** — Structured for the repeating "Books of the Month," "Bestsellers," and "New Releases" carousels described in the page text (title, format, sale price). Uses title-md for the book title and body-sm for price, with a thin hairline border; card imagery and hover elevation are not observed and are proposed.

**hero** — A full-width promotional band for the rotating "Books of the Month" carousel, using the soft off-white surface and a large display heading. Copy hierarchy (title/subtitle) is proposed since no hero-specific selector or measured type scale was present in evidence.

**footer** — Maps to the dark slate (#21282d) as an inferred footer background with white text, covering the store-locations grid (Colfax Ave., Aspen Grove, Stanley Marketplace, Union Station) and newsletter form visible in the page text. Actual footer background color is not directly confirmed by a selector.

**badge** — Represents on-sale/sold-out/custom labels referenced only as RGB custom properties in `:root` (e.g., `--on-sale-badge-background`, `--custom-badge-background: 28 28 28`). Since these are expressed as RGB triples rather than hex values in the supplied palette, the badge token here substitutes the confirmed hex primary rather than inventing a new red hex.

**search** — A compact input/button pairing for the header's "Open search" control, styled with the soft surface background and standard border-radius token; icon and focus-ring behavior are not observed.

**staff-pick-card** — A category-appropriate component for an independent bookstore, surfacing staff recommendations or book-club picks (the page text references "Book Clubs" and curated lists). Uses the alternate green as an accent rule or corner tag, with a slightly larger corner radius to differentiate it from standard product cards; this pattern is proposed, not observed.

## Responsive Behavior

Recommended, not measured — the source CSS confirms only root-level spacing/typography tokens, not live breakpoint behavior.

| Breakpoint | Width      | Layout guidance (proposed) |
|-----------|-----------|------------------------------|
| Mobile    | <640px    | Single-column carousels, collapsed hamburger nav, stacked footer columns |
| Tablet    | 640–1024px| 2-column product grids, condensed header nav areas |
| Desktop   | >1024px   | Full 3-area header grid (`primary-nav logo secondary-nav`), multi-column carousels and footer |

Touch targets should be a minimum 44×44px for buttons and nav links per general accessibility guidance (not verified against this site). Primary navigation is expected to collapse into a slide-out or accordion menu below tablet width, consistent with the "Open navigation menu" control referenced in the page text, though the actual collapse mechanism was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a font-family list, and page text only — no rendered layout, hover states, animations, or actual mobile behavior were observed. The mapping of #1f4324/#204325 to "primary" and #21282d to "secondary/footer" is an inferred role assignment; no selector in the supplied evidence directly ties these hex values to specific UI elements. Badge/sale/error colors are defined in the source only as RGB triples (e.g., `227 44 43`) rather than supplied hex values, so they were intentionally excluded from the color tokens rather than converted. DellaRobbia and Poynter appear as font-family names in the CSS but their licensing, availability, and actual applied elements are unverified; they may be proprietary or self-hosted assets not confirmed as brand-approved. Display-scale font sizes above the confirmed `--text-xl` (1.25rem/20px) are proposed extrapolations. Component padding, hover/focus states, card imagery treatment, and the staff-pick-card pattern are proposed design suggestions grounded in bookstore convention and the page's textual content, not evidence of built UI.
