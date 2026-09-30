---
version: alpha
name: "XS Power"
source_url: "https://4xspower.com/"
captured_at: "2026-09-29T03:59:02.248457+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the public 4xspower.com Shopify storefront for
  XS Power Batteries (AGM, Lithium, SuperBANK ultracapacitors). The observed
  palette is dominated by neutral grays and near-blacks (#000000, #1a1a1a,
  #282828, #f4f4f4, #ffffff) paired with a warm safety-orange accent
  (#ff9900, #f49701, #e4893a) that appears directly in the fitment-search
  "Search" button and in the Judge.me review-widget primary color. A teal
  (#108474) and a small set of status reds/greens appear in the palette but
  their exact on-page role is not confirmed from static evidence, so they are
  treated as secondary/status accents, labeled inferred. Headings use a
  custom-hosted @font-face, Tomorrow, at weight 700; body and UI text draw
  from the observed sans stack (Barlow, Barlow Condensed, Rubik, Noto Sans,
  system-ui), with exact body-copy family unconfirmed and therefore inferred.
  Layout tokens (container gutter, heading scale, button/input heights) come
  from the site's own CSS custom properties. The design system below proposes
  a rugged, high-contrast industrial-automotive UI: dark charcoal chrome,
  bright orange calls-to-action, and a YMM (year/make/model) fitment finder as
  the primary category-specific component, consistent with a performance
  battery retailer.

colors:
  primary: "#ff9900"
  primary-strong: "#f49701"
  accent-teal: "#108474"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#6d6d6d"
  hairline: "#dddddd"
  hairline-dark: "#303030"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  header-surface: "#282828"
  danger: "#ea3335"
  success: "#428445"
typography:
  display-xl: {fontFamily: "Tomorrow, sans-serif", fontSize: "50px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Tomorrow, sans-serif", fontSize: "36px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Barlow Condensed, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Rubik, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Rubik, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: "11px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: "12px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.5px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: "52px"
  nav-bar:
    backgroundColor: "{colors.header-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    borderColor: "{colors.hairline-dark}"
    height: "99.5px"
  hero:
    backgroundColor: "{colors.header-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  fitment-finder:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    submitButtonColor: "{colors.primary}"
    resetButtonColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.primary-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

**button-primary** is the orange (#ff9900) filled action used for the fitment
search "Search" control observed in CSS; proposed for primary storefront CTAs
like "Add to Cart" and "Shop AGM/Lithium/SuperBANK" links.

**button-secondary** is an outlined black-on-white variant, proposed for
lower-emphasis actions (e.g., "Compare All Three", "Reset"), inferred from the
cookie-banner's own outlined accept/decline buttons, which use a black
1px border on white.

**text-input** models the 52px form field height defined in the site's
`--form-input-field-height` variable, styled with a light hairline border on
white; used for email signup and search fields. States (focus, error) are
proposed, not observed.

**nav-bar** reflects the sticky header's own custom properties: background
rgb(40,40,40) mapped to `header-surface`, white text, and a measured
99.5px height. Border color is approximated to the nearest palette hairline
since the exact header border hex was not in the supplied swatch list.

**hero** is a full-bleed dark section for the "Powering the Impossible Since
2005" banner, using the Tomorrow display face at the largest heading scale;
background and copy treatment are proposed extensions of the header surface.

**fitment-finder** is the category-specific Year/Make/Model/Engine search
widget (`#ymm_searchbox`) explicitly observed in CSS, with an orange submit
button (#ff9900/border #ff9900) and a light-gray reset button (#dddddd
background, #3d4246 text) — a core battery-fitment lookup pattern.

**product-card** is proposed for battery SKU listings (e.g., "XS Power D3400
Group 34 12V AGM Battery") referenced in review text; layout, elevation, and
hover state are not confirmed from static CSS and are inferred conventions.

**badge** covers small labels such as chemistry tags (AGM/Lithium/SuperBANK)
or review-star accents, using the Judge.me widget's own primary color
(#f49701) as the closest observed reference point.

**search** models a general on-site search input distinct from the fitment
finder, sharing the same input styling tokens; presence of a global search
box is inferred from typical Shopify theme structure, not directly observed.

**footer** uses a near-black background consistent with the page's dark
navigation chrome, holding the Company/Applications/Support link columns and
newsletter form visible in the extracted footer text.

## Responsive Behavior

Recommended, not measured, breakpoint table:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <750px | Single-column stacking; nav collapses to a toggled menu; fitment-finder fields stack vertically. |
| Tablet | 750–999px | `--heading-h1-font-size` steps to 50px per observed variable tier; grid narrows to fewer columns. |
| Desktop | ≥1000px | Full `--grid-column-count: 20` layout; sticky header at measured 99.5px height. |

Touch targets should be at least 44px (matching the observed
`--button-small-height: 44px`); primary buttons use the observed 52px
`--button-height`. Mobile nav collapse, sticky-header behavior on scroll,
and fitment-finder responsive stacking are proposed conventions and were not
interactively verified.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered
screenshots, computed layouts, or interactive states (hover, focus, active,
form validation) were observed. Semantic color roles (e.g., which orange
variant is "primary" vs. "hover") are inferred from limited context (the
YMM search button and Judge.me widget variables) and may not match the
live design system exactly. Typography role assignments (body vs. heading
family) are inferred from the available font-family list; only the Tomorrow
@font-face weight (700) and hosting were directly confirmed — its licensing
and availability for reuse are not verified, and generic sans-serif
fallbacks are assumed for all other listed families. Spacing and rounding
scales follow a proposed general system rather than measured site values,
aside from the explicit `--form-input-field-height`, `--button-height`, and
`--header-height` variables. Mobile menu behavior, product grid structure,
and cart/checkout UI were not present in the supplied evidence and are
therefore omitted or only generically proposed.
