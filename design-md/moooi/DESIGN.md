---
version: alpha
name: "Moooi"
source_url: "https://moooi.com"
captured_at: "2026-09-28T04:20:42.949300+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Moooi's captured stylesheet is built on a restrained neutral scale (white, near-black,
  and a family of warm beiges such as #f8f4ed and #f1ece2) punctuated by a small set of
  saturated accents (#208649 green, #d24532 red-orange, #fbe839 yellow) that surface in a
  "theme-festive" class, suggesting seasonal or promotional overlays rather than a core
  brand color. Typography runs through several Next.js-optimized font slots: a Gill Sans
  variant is directly used for body copy, buttons, and uppercase micro-labels (12px,
  letter-spacing .1em, confirmed in CSS); Brown, SangBleu Sans, and two Tiempos cuts
  (Fine/Text) are present in the font manifest but their applied selectors were not
  captured, so their editorial/display roles below are inferred from typical serif+sans
  pairing conventions in design-object retail. Interactive chrome (close buttons, back
  buttons, modal shells) shows soft box-shadows, transparent buttons with inherited
  color, and dark/light theme variants toggled via class modifiers. This interpretation
  treats Gill Sans as the confirmed workhorse for UI and body text, reserves the serif
  Tiempos family for occasional editorial emphasis, and keeps corners near-square and
  spacing generous, matching a minimal, product-forward lighting catalogue.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  hairline: "#e0e0e0"
  surface-soft: "#f8f4ed"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  surface-dark: "#0e131a"
  border-dark: "#1f2735"
  accent-forest: "#208649"
  accent-terracotta: "#d24532"
  accent-gold: "#fbe839"
typography:
  display-xl: {fontFamily: "__TYPE_SANGBLEU_SANS_069a48, __TYPE_SANGBLEU_SANS_Fallback_069a48, sans-serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "__TYPE_TIEMPOS_FINE_375fe6, __TYPE_TIEMPOS_FINE_Fallback_375fe6, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "__TYPE_BROWN_8c6aef, __TYPE_BROWN_Fallback_8c6aef, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "__TYPE_GILL_SANS_0505e8, __TYPE_GILL_SANS_Fallback_0505e8, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0px}
  body-sm: {fontFamily: "__TYPE_GILL_SANS_0505e8, __TYPE_GILL_SANS_Fallback_0505e8, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0px}
  caption: {fontFamily: "__TYPE_GILL_SANS_0505e8, __TYPE_GILL_SANS_Fallback_0505e8, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1em, letterSpacing: 1.2px}
  button-md: {fontFamily: "__TYPE_GILL_SANS_0505e8, __TYPE_GILL_SANS_Fallback_0505e8, sans-serif", fontSize: 18px, fontWeight: 200, lineHeight: 1, letterSpacing: 0px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hoverColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.border-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  lightbox-modal:
    backgroundColor: "{colors.canvas}"
    closeButtonSize: "38px"
    closeButtonBackground: "{colors.on-primary}"
    closeButtonColor: "{colors.ink}"
    shadow: "3px 3px 8px rgb(from {colors.ink} r g b / 20%)"
    rounded: "{rounded.none}"

## Components
**button-primary** carries the dark, near-black `{colors.primary}` fill observed on the site's `button` reset (transparent background overridden per-instance) paired with the confirmed Gill Sans button typography (18px/weight 200). **button-secondary** proposes an outline treatment using the observed hairline grey for contexts needing lower visual weight. **text-input** is a proposed pattern, inheriting body typography and a light hairline border consistent with the site's minimal neutral palette. **nav-bar** uses the caption-scale uppercase Gill Sans styling directly evidenced in `.styles_back-button-label`, extended here to a top-level navigation bar (proposed extension of an observed pattern). **product-card** is inferred for a lighting catalogue context, using the light card surface `#f3f3f3` seen in the palette and hairline dividers matching the `table>tbody>tr:nth-of-type(2n)` beige striping rule. **hero** is proposed, applying the warm beige surface (`#f8f4ed`) and the largest display type as an editorial full-bleed introduction. **footer** proposes the darkest captured surface (`#0e131a`) with its paired border tone (`#1f2735`), inferred from the theme-dark class family present in the CSS. **badge** repurposes the festive-theme green accent for status or "new" labels, explicitly inferred since the source class name references a festive/seasonal theme rather than confirmed permanent UI. **search** is a proposed compact input variant. **lightbox-modal** is the most directly evidenced component: the 38px close button, white background, and soft black-derived box-shadow are taken verbatim from `.styles_is-bottom-on-mobile__UI5PJ .styles_close-button___CaGt`.

## Responsive Behavior
This is a proposed recommendation, not measured site behavior: a compact breakpoint table of mobile (< 600px), tablet (600–1024px), and desktop (> 1024px) is suggested. Below 600px, navigation should collapse into a drawer or bottom sheet — consistent with the observed `.styles_is-bottom-on-mobile` modal variant, which repositions the close control for small screens. Touch targets should stay at or above the observed 38px close-button dimension. Font sizing in the captured body rule uses viewport-relative units (`1.0666666667vw`) alongside a fixed 16px fallback, implying fluid type scaling on larger viewports that should be clamped for accessibility on very small or very large screens (proposed, not confirmed).

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and a font/color inventory only; no rendered layout, breakpoint behavior, hover/focus states beyond the few captured selectors, or actual mobile navigation pattern were observed. The semantic roles of Brown, SangBleu Sans, and both Tiempos cuts are inferred from font-manifest presence alone, since no selector in the supplied evidence applies them — their assignment to display/title roles here is a plausible but unverified pairing. Festive-theme accent colors (green, red-orange, yellow) are assumed seasonal rather than core brand colors based solely on the `theme-festive` class name. All spacing, rounding, and non-Gill-Sans typographic sizes are proposed design-system values, not measured. Licensing and availability of the custom font families (Brown, Gill Sans, SangBleu Sans, Tiempos Fine/Text) were not verified and would require confirmation before implementation.
