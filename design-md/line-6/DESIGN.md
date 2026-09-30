---
version: alpha
name: "Line 6"
source_url: "https://www.line6.com"
captured_at: "2026-09-28T04:41:29.381220+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Line 6's storefront pairs a near-black/white foundation with a dominant signal red (#c10000, with a brighter #ff3c3c accent used as a top-border highlight) that carries through primary buttons, price call-to-actions, and small store badges. A secondary cyan-blue (#00a5e1 over a deeper #007099 gradient base) appears on alternate "blue_button" CTAs, likely reserved for secondary or account-related actions versus the red "buy" actions. Neutral grays (#333333, #999999, #cccccc, #ebebeb, #f5f5f5) build body text, hairlines, and soft card surfaces, while flat dark buttons (#333333/#242424) serve as tertiary/outline actions seen in `.generic-button-2021` and `.find-a-dealer-button`.
  Typography is evidence-based on the TradeGothic family (TG-Bold, TG-Cond, TG-Light) for headings and product names, with Lucida Grande as a fallback/utility font for smaller buttons and legacy UI text; generic sans-serif fallbacks are added since no web-font loading or licensing was verified.
  This interpretation infers a utilitarian, gear-catalog aesthetic: dark hero bands with red accent borders, card-based product/preset modules with light gray fills and small radii, and a red-vs-blue-vs-dark three-tier button hierarchy. All spacing, exact type sizes, and interaction states beyond hover backgrounds are proposed, not measured.

colors:
  primary: "#c10000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#ebebeb"
  on-primary: "#ffffff"
  secondary: "#00a5e1"
  secondary-deep: "#007099"
  accent: "#ff3c3c"
  dark-surface: "#333333"
  dark-surface-strong: "#242424"
  disabled-bg: "#cccccc"
  disabled-text: "#aaaaaa"
typography:
  display-xl: {fontFamily: "TG-Bold, TradeGothic, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "TG-Bold, TradeGothic, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "TG-Cond, TradeGothic, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "TradeGothic, \"Lucida Grande\", sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "TradeGothic, \"Lucida Grande\", sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "\"Lucida Grande\", sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "TradeGothic, \"Lucida Grande\", sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.75, letterSpacing: 0.3px}
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
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  button-tertiary-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    accentBorder: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  pedal-preset-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    indicatorColor: "{colors.secondary}"
  hero:
    backgroundColor: "{colors.ink}"
    topBorderColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.dark-surface-strong}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** uses the observed `#c10000` red seen across `.red_button` and `.store_button`, with white text and a pill-like rounded corner (mapped to the `lg` token, close to the 15px radius in CSS). This is the primary "Buy"/commerce action.

**button-secondary** mirrors `.generic-button-2021`: transparent fill, black border, dark gray text, sharp corners, with an inferred hover state darkening to `{colors.dark-surface}` (proposed, based on the observed `:hover` rule turning background to `#333`).

**button-tertiary-dark** reflects `.find-a-dealer-button`, a solid dark-gray CTA reserved for lower-priority actions like dealer lookup; hover deepens to `#242424` per observed CSS.

**text-input** is a proposed pattern — no input styling was present in the supplied CSS, so border, radius, and padding are inferred from the site's general flat, low-radius button aesthetic.

**nav-bar** is inferred as a dark header consistent with the black hero backgrounds and the `#ff3c3c` top-border accent seen on the product-feedback module; exact nav markup/layout was not observed.

**product-card** generalizes `.newproducts_box`, which uses a light `#ebebeb` fill and a 9px radius (rounded here to the `md` token) for grouped product callouts.

**pedal-preset-card** is a category-specific proposed component for displaying guitar-pedal presets/patches (relevant to HX Effects, HX One, DL4 MkII), using the soft surface tone and the secondary blue as a status/indicator color; this pattern is not directly observed and is a design proposal only.

**hero** is inferred from the black `#000000` background and `#ff3c3c` top border found on the homepage feedback/promo module, extended here as a general hero treatment for large display type.

**footer** is proposed using the darkest observed dark-surface tone with muted gray text; no footer-specific CSS was supplied.

**badge** reuses the primary red for small labels (e.g., "New"), consistent with `.store_buttonsm`'s compact, colored pill treatment.

**search** is a proposed rounded field using neutral hairline/canvas tones; no search-input CSS was present in the evidence.

## Responsive Behavior
Recommended (not measured) breakpoints: mobile ≤480px, tablet 481–1024px, desktop ≥1025px. Nav should collapse to a hamburger/drawer below tablet width; product and preset cards should reflow from multi-column grids to single-column stacks. Touch targets for buttons and badges should maintain a minimum 44px height regardless of the compact padding shown in desktop CSS (`.store_buttonsm` at 1–6px padding is desktop-only and should be enlarged for touch).

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed layout, or responsive/mobile behavior was observed. Font availability, weights, and licensing for TradeGothic (TG-Bold/TG-Cond/TG-Light) were not verified and may require licensing confirmation or substitution. Several component definitions (text-input, search, footer, pedal-preset-card, hero) are proposed patterns inferred from adjacent CSS rather than direct observation. All typography sizes except where explicitly noted (16px button text, 1.75 line-height) are proposed, not measured. Interaction states beyond the explicitly supplied `:hover` rules are inferred/proposed.
