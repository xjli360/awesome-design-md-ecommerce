---
version: alpha
name: "Invidia"
source_url: "https://invidia-usa.com"
captured_at: "2026-09-29T04:03:51.641324+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from a supplied color list and font-family names for
  invidia-usa.com; no CSS selectors or component rules were provided, so all layout,
  spacing, and role assignments below are inferred rather than observed. The palette
  is dominated by neutrals (#000000, #ffffff, #333333, #6f6f6e, #ced4da, #e7e7e7,
  #ededed, #aaaaaa) consistent with an automotive-parts catalog that lets product
  photography carry visual weight. Among the warmer/brighter values, #ed5d43
  (orange-red) is proposed as the primary accent for calls-to-action and links,
  echoing the brand's language of heat, exhaust, and performance; this is an
  inferred semantic mapping, not a confirmed brand color. #c69a02 is proposed for
  premium/warranty badges, and #ff0000 is reserved for error/alert states rather
  than decoration. Of the supplied font families, "Inter" and "Kanit" are usable
  text typefaces; "Feather," "feather," "icomoon," and "wpbingofont" read as icon
  glyph sets and are excluded from body/heading typography. Kanit is proposed for
  headings for its condensed, technical character; Inter is proposed for body copy
  for legibility in spec-heavy product listings. Sizes, weights, and spacing scales
  are proposed defaults, not measured values.

colors:
  primary: "#ed5d43"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6f6f6e"
  hairline: "#ced4da"
  surface-soft: "#ededed"
  surface-card: "#e7e7e7"
  on-primary: "#ffffff"
  accent-gold: "#c69a02"
  alert: "#ff0000"
  border-strong: "#aaaaaa"
typography:
  display-xl: {fontFamily: "Kanit, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Kanit, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Kanit, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Kanit, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-strong}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"

## Components

**button-primary** — Proposed for "Shop Now" and add-to-cart actions, using the orange-red accent against white text to draw attention on otherwise neutral catalog pages. State: default only; hover/focus/disabled states not observed.

**button-secondary** — Proposed outline style for secondary actions such as "Find a Dealer" or "Contact Us," keeping the neutral hairline border so it doesn't compete with primary CTAs.

**text-input** — Proposed baseline for contact forms and any dealer-locator/search fields, using a light hairline border and neutral body color; no focus-ring color was observed, so one is not specified.

**nav-bar** — Proposed top navigation bar carrying category links (Axle-Back, Cat Back, Titanium Exhausts, etc.) on a white background with a thin bottom hairline; mobile collapse behavior is not observed and is addressed only in Responsive Behavior below.

**product-card** — Proposed card for exhaust-system listings (e.g., Catted Downpipe, Headers & Manifolds), using the light card-surface color and a hairline border to separate cards in a grid; title/body typography pairs a Kanit heading with Inter body copy.

**hero** — Proposed full-width intro band using the ink/black background suggested by the palette's strong black value, with large Kanit display type for the "Feel it. See it. Hear it." brand statement; actual homepage hero styling was not measured.

**footer** — Proposed dark footer matching the ink color, housing address, phone, product-category links, and legal links (Terms, Privacy). Typography drops to body-sm for dense link lists.

**badge** — Proposed small pill for labeling items such as "Titanium," "304 Stainless," or "Racing/Off-Road Only" callouts, using the gold accent as a premium/warning marker; this is a proposed convention, not confirmed brand usage.

**search / fitment-selector** — Search is a generic proposed input pattern for a future site search. The fitment-selector is a category-appropriate proposed component for a make/model/year picker, common to exhaust e-commerce, styled with the soft surface and stronger border to visually separate it as a tool rather than content.

## Responsive Behavior
This is a recommendation only; no live responsive behavior was observed.

| Breakpoint | Range        | Notes (proposed)                              |
|-----------|--------------|------------------------------------------------|
| mobile    | 0–480px      | Single-column product grid; nav collapses to a hamburger/drawer pattern (not observed). |
| tablet    | 481–1024px   | 2-column product grid; nav-bar links may wrap or condense. |
| desktop   | 1025–1439px  | Full horizontal nav-bar; 3–4 column product grid. |
| wide      | 1440px+      | Max-width content container centered on canvas background. |

Touch targets should be at least 44x44px for buttons and nav items on mobile; the fitment-selector's dropdowns should stack vertically below tablet width. None of this spacing or collapse logic was measured from the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- No CSS rules, selectors, or computed styles were supplied (`css_rules` was empty); all component structure, spacing scale, and rounding values are proposed conventions, not extracted measurements.
- Color-to-role mapping (primary, alert, badge, etc.) is inferred from a flat hex list with no usage context (no selector-to-color pairing was provided), so actual brand-critical colors could differ.
- "Feather," "feather," "icomoon," and "wpbingofont" are treated as icon-glyph fonts and excluded from text typography; this assumption is not independently verified.
- Font pairing (Kanit for display, Inter for body) is a plausible but unverified assignment; no font-weight, size, or usage rules were observed in CSS.
- Responsive breakpoints, mobile navigation collapse, hover/focus/active states, and touch interactions are not observed and are presented strictly as proposals.
- Licensing/availability of Kanit and Inter for production use was not verified in this exercise.
