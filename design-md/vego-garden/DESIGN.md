---
version: alpha
name: "Vego Garden"
source_url: "https://vegogarden.com"
captured_at: "2026-09-28T04:04:23.773829+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Vego Garden's public CSS evidence centers on a deep forest green (#3a5b39) paired
  with a warm cream (#fef9eb), forming the dominant brand-and-background pairing seen
  across headers, review sections, and primary CTAs. Body copy and form controls are
  set in Manrope, a geometric sans-serif, while headline elements (h1–h5) load Moret,
  a serif-leaning display face, at generous sizes (56px observed in a review headline).
  Secondary palette entries — a muted sage (#88937c), a softened olive-green
  (#bfcd89), and a terracotta/rust family (#cc6228, #9a4a27) — are inferred as
  supporting accents for badges, secondary buttons, and seasonal callouts, since no
  selector confirms their exact usage. A warm yellow (#ffdd81) and a red (#d02e2e)
  appear in the palette and are treated as inferred highlight/alert tones pending
  confirmation. Buttons use a fully rounded pill radius (200px, mapped to
  rounded.full) with bold 14px Manrope labels. This interpretation proposes a warm,
  garden-and-earth system — cream canvas, forest-green ink and primary actions,
  terracotta accents — built conservatively from measured selectors rather than
  assumed brand memory.

colors:
  primary: "#3a5b39"
  ink: "#3d3d3d"
  canvas: "#fef9eb"
  body: "#3d3d3d"
  muted: "#88937c"
  hairline: "#e0e0e0"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#fef9eb"
  secondary: "#bfcd89"
  accent: "#cc6228"
  highlight: "#ffdd81"
  disabled-text: "#b6b6b6"
  alert: "#d02e2e"
typography:
  display-xl: {fontFamily: "Moret, serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.0, letterSpacing: "0px"}
  display-md: {fontFamily: "Moret, serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "Moret, serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Manrope, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Manrope, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Manrope, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Manrope, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.42, letterSpacing: "0px"}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  bed-configurator-panel:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.lg}"
    titleTypography: "{typography.title-md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the forest-green pill CTA confirmed by observed selectors (`.seed-starting-v2 .vego-featuredProducts-btn`, generic `.btn`), using cream text on a green fill with a fully rounded corner. **button-secondary** is a proposed outline variant for lower-emphasis actions such as "learn more" links, inverting the fill to transparent while retaining the green ink and pill shape. **text-input** is inferred from the general form-control font stack (Manrope) and a conservative hairline border, since no dedicated input-border color was captured in evidence. **nav-bar** assumes a cream header consistent with the `.announcement-link` cream text color, though the header's own background was not directly captured and is treated as inferred. **product-card** is a proposed pattern for the raised-bed/greenhouse catalog grid, pairing a white surface with a Moret title and Manrope price line — card elevation and shadow were not observed and are omitted. **hero** reflects the large 56px Moret headline confirmed in the review-header rule, set against the cream canvas with green ink, appropriate for a garden-lifestyle landing section. **footer** is proposed as a green-on-cream inversion of the header treatment, a common pattern for earthy e-commerce sites, but its exact background was not directly observed. **badge** is inferred to use the sage-green secondary tone for labels like "Best Seller" or "New," appropriate to the softer olive entries in the palette. **search** is a proposed pill-shaped input consistent with the button radius system. **bed-configurator-panel** is a category-specific proposed component for the raised-bed/greenhouse sizing or add-to-cart configurator, using the terracotta accent to distinguish interactive selection controls from standard content cards.

## Responsive Behavior

The following breakpoints are a **recommendation**, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column stacking, nav collapses to a hamburger/drawer pattern (proposed) |
| Tablet | 600–1024px | Two-column product grids, condensed nav |
| Desktop | 1024–1440px | Full multi-column grids, inline nav |
| Wide | >1440px | Max-width content container, generous section padding |

Touch targets should be no smaller than 44×44px for buttons and nav items (proposed, WCAG-aligned convention). Primary nav is expected to collapse into a drawer or accordion below the tablet breakpoint; this has not been observed in live markup. Product-card grids are expected to reflow from 4 → 2 → 1 columns across desktop → tablet → mobile as a conservative default.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/color/font extraction supplied as evidence; no live page render, DOM structure, or JavaScript-driven interaction was inspected. Semantic color-role mapping (e.g., which greens serve as "primary" vs. "muted" vs. "secondary") is inferred from selector context and frequency, not confirmed design tokens — Vego Garden's theme uses CSS custom properties (`--primaryColor`, `--thirdColor`, `--colorBtnPrimary`) whose resolved values were not directly captured for every instance. Type sizes beyond the single confirmed 56px headline are proposed estimates following common editorial scale ratios, not measured. Moret's availability, license terms, and exact weight range were not verified; it is used here only because it appears in the supplied `font-family` declarations. Mobile menu behavior, hover/focus states beyond the two `.announcement-link` and `.btn:hover` rules, form validation states, and product-configurator interaction flows were not observed and are marked proposed throughout.
