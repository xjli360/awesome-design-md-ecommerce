---
version: alpha
name: "Christy Dawn"
source_url: "https://christydawn.com"
captured_at: "2026-09-28T04:15:45.522062+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Christy Dawn's public CSS evidence points to a warm, earth-toned palette built
  from unbleached linens (#faf8f4, #f9f7f3, #fbf8f4), clay and rust browns
  (#89685c, #6b5147, #853423), and muted sage greens (#5e755d, #478947),
  anchored by near-black ink (#000000) and a deep grounding tone (#0d0e07)
  observed on at least one full-bleed section. A single saturated red (#c31818)
  is reserved for sale pricing per the theme.css evidence. Typography pairs a
  serif display family (garamond-premier-pro / ajensonpro-lt, with Garamond,
  Hoefler Text, Times New Roman, Times, serif fallbacks) for headings and
  uppercase product titles with a plain-spoken sans-serif (Maison Neue Book,
  Helvetica Neue, Helvetica, Arial) for buttons and UI copy — consistent with
  the brand's "regenerative, ethical, timeless" positioning.
  Roles below such as ink, muted, hairline, surface-soft, and surface-card are
  inferred groupings of the observed neutral swatches; the CSS does not label
  these as design tokens. Border-radius evidence (--rivo-aw-border-radius: 0px)
  suggests a largely square-cornered interface, applied here as a proposed
  system default rather than a confirmed sitewide rule. No live layout,
  breakpoints, or interaction states beyond the documented button hover were
  observed.

colors:
  primary: "#89685c"
  accent-hover: "#6b5147"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#707070"
  hairline: "#dedede"
  border-subtle: "#e2dedd"
  surface-soft: "#f9f7f3"
  surface-card: "#fcfaf8"
  on-primary: "#fbf8f4"
  accent-clay: "#853423"
  accent-sage: "#5e755d"
  accent-success: "#478947"
  accent-sale: "#c31818"
  accent-error: "#a70100"
  ground-dark: "#0d0e07"
typography:
  display-xl: {fontFamily: "garamond-premier-pro-display, Garamond, Hoefler Text, Times New Roman, Times, serif", fontSize: 61px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "garamond-premier-pro, Garamond, Hoefler Text, Times New Roman, Times, serif", fontSize: 35px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "ajensonpro-lt, garamond-premier-pro, Garamond, Hoefler Text, Times New Roman, Times, serif", fontSize: 20px, fontWeight: 300, lineHeight: 1.3, letterSpacing: 0.04em}
  body-md: {fontFamily: "Maison Neue Book, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Maison Neue Book, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "ajensonpro-lt, garamond-premier-pro, Garamond, Hoefler Text, Times New Roman, Times, serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.04em}
  button-md: {fontFamily: "Maison Neue Book, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.04em}
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
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.xxl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    saleColor: "{colors.accent-sale}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    overlayColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ground-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    inputComponent: "text-input"
    resultTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** reflects the observed `.btn-lg.rust` rule: a clay-brown fill (`#89685c`) with off-white text (`#fbf8f4`), wide letter-spacing, and a documented hover shift to a darker rust (`#6b5147`). Corner radius is set to none per the sitewide `--rivo-aw-border-radius: 0px` evidence.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More"), using ink-colored text and border on a transparent field; no matching CSS rule was found, so its states are inferred from the primary button's structure.

**text-input** is proposed for forms and search fields, using the hairline neutral for borders and canvas white for background; focus and error states were not observed and are marked proposed.

**nav-bar** assumes a white header with uppercase caption-weight labels, matching the ajensonpro-lt uppercase treatment seen on product titles; exact height, sticky behavior, and mobile menu markup were not present in the supplied evidence.

**product-card** is grounded in `.frenzy_product_item_detail h3 a` and `.frenzy_product_price_sale`, giving uppercase serif titles in black and a red sale price (`#c31818`) against a soft off-white card surface.

**hero** is a proposed full-width introductory section using the warm surface tone as backdrop and the largest display type scale (`display-xl`) drawn directly from the `--font-size-heading-display-1` custom property; imagery, overlay opacity, and copy placement are not confirmed.

**footer** uses the darker ground tone (`#0d0e07`) found in an ambiguous section rule as an inferred footer/newsletter background, paired with off-white text for contrast; actual footer markup and column layout were not observed.

**badge** models the `.product-badge[data-handle="..."]` fabric/material tags (e.g., alpaca, regenerative) as small pill labels in black text on a soft neutral background — a category-relevant pattern for communicating sustainable-material claims.

**search** and **size-selector** are both proposed, apparel-specific patterns: search reuses the text-input component in an overlay context, while size-selector models the swatch/size-chip pattern common to women's apparel PDPs, using hairline borders with an ink-colored selected state.

## Responsive Behavior
This is a recommended breakpoint scheme, not a measured site behavior:

| Breakpoint | Width       | Notes                                  |
|-----------|-------------|-----------------------------------------|
| mobile    | 0–599px     | Single-column, stacked nav, full-width cards |
| tablet    | 600–1023px  | 2-column product grid, condensed nav   |
| desktop   | 1024–1439px | 3–4 column grid, full nav bar           |
| wide      | 1440px+     | Max content width with generous margins |

Touch targets should be at minimum 44×44px for buttons and size-selector chips. Nav-bar is expected to collapse into a hamburger/drawer pattern below 1024px, and search should convert to a full-screen overlay on mobile — both proposed, unverified interaction patterns.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS extraction only; no rendered page, computed layout, or interaction was directly observed. The dark background (`#0d0e07`) was found on a selector with truncated/obscured context, so its assignment to "footer" is an inference, not a confirmed usage. Neutral roles (ink, muted, hairline, surface-soft, surface-card) are grouped from repeated palette values rather than explicit CSS variable names. Font sizes for display/heading tokens are converted from rem custom properties assuming a 16px root and may not match actual rendered sizes if the root font-size differs. Hover/focus states beyond `.btn-lg.rust:hover` were not present in evidence and are proposed by analogy. Mobile navigation, search overlay, and size-selector interaction patterns are proposed, not observed. Availability and licensing of the custom fonts (ajensonpro-lt, garamond-premier-pro family, Maison Neue Book) were not verified and should be confirmed before implementation. Spacing and rounded scales beyond the observed `0px` border-radius are proposed defaults, not extracted values.
