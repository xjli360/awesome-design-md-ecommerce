---
version: alpha
name: "HKS USA"
source_url: "https://hksusa.com"
captured_at: "2026-09-29T04:19:16.096843+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  HKS USA's storefront evidence shows a dark-leaning performance-parts UI built on
  Next.js, using a small saturated teal (#00cea8) as the primary accent against
  near-black chrome (#101010, #1b1c1b) and neutral card surfaces (#e8e8e8, #eeeeee).
  A secondary teal (#00b194) and a purple-to-teal gradient border variable
  (#430f77 → #00cea8) appear in CSS custom properties, suggesting a motorsport
  gradient accent used sparingly on CTAs or dividers; this gradient usage is
  inferred from the variable definition, not confirmed as rendered on a visible
  element. A red (#ff253a) is available for alerts or discontinued/sale badges,
  inferred from category naming ("discontinued products") rather than observed
  styling. Typography relies on two Next.js-optimized local font tokens present
  in the CSS — a condensed sans (__Roboto_Condensed) for headings and a humanist
  sans (__Open_Sans) for body copy — kept as their literal observed family
  identifiers since the underlying licensed typeface cannot be verified from
  static CSS alone. The interpretation favors a dense, catalog-driven layout:
  dark navigation chrome, light product-card surfaces, pill-shaped buttons
  (border-radius:9999px observed on Slider_exploreButton), and rounded
  floating-nav pills, extended here into a full component system for a
  parts-and-vehicle-fitment storefront.

colors:
  primary: "#00cea8"
  accent-teal: "#00b194"
  accent-purple: "#430f77"
  danger: "#ff253a"
  ink: "#1b1c1b"
  body: "#1d1d1d"
  canvas: "#ffffff"
  muted: "#9ca3af"
  hairline: "#dfdfdf"
  surface-soft: "#eeeeee"
  surface-card: "#e8e8e8"
  surface-dark: "#101010"
  surface-dark-alt: "#121e22"
  scroll-track: "#202020"
  scroll-thumb: "#555555"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "\"__Roboto_Condensed_a1f95a\", \"__Roboto_Condensed_Fallback_a1f95a\", sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"__Roboto_Condensed_a1f95a\", \"__Roboto_Condensed_Fallback_a1f95a\", sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "\"__Roboto_Condensed_a1f95a\", \"__Roboto_Condensed_Fallback_a1f95a\", sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "\"__Open_Sans_908882\", \"__Open_Sans_Fallback_908882\", sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "\"__Open_Sans_908882\", \"__Open_Sans_Fallback_908882\", sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "\"__Open_Sans_908882\", \"__Open_Sans_Fallback_908882\", sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"__Open_Sans_908882\", \"__Open_Sans_Fallback_908882\", sans-serif", fontSize: 17px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    accentBorder: "linear-gradient(90.13deg, {colors.accent-purple} 20%, {colors.primary} 55%)"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed `#00cea8` primary token against a light `on-primary` text color, in a fully rounded pill shape mirroring the `Slider_exploreButton` (`border-radius:9999px`) and the `#00b194` floating-nav CTA variant. **button-secondary** is a proposed outline treatment for lower-emphasis actions (e.g. "Reset" in the quick search), using the observed hairline gray border rather than an invented color. **text-input** models quick-search fields (Make/Model/Year, Category/Sub-Category) with a light canvas background and hairline border; focus/error states are proposed, not observed. **nav-bar** reflects the dark `#101010` chrome seen on `#floatNav .btnLink`, including its teal hover state, extended to a full top navigation bar. **product-card** is inferred from the repeated product-listing text pattern (name, part number, fitment, MSRP) and uses the neutral card surface `#e8e8e8` for visual separation from the white canvas. **hero** proposes a dark banner treatment using the CSS-variable gradient border (purple-to-teal) as an accent rule beneath a large condensed headline, since no hero markup/CSS was directly captured. **footer** reuses the dark surface and muted text color, sized for the observed address/newsletter/social block. **badge** applies the red (`#ff253a`) token, present in the palette but unconfirmed in role, to "NEW"/discontinued flags seen in the product feed. **search** and **vehicle-fitment-selector** are category-specific components proposed for the Make/Model/Year/Engine and Category/Sub-Category quick-search UI referenced in the page text, styled with body typography and hairline borders for consistency with the input pattern.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Width      | Behavior (proposed) |
|-----------|-----------|----------------------|
| xs        | <480px    | Single-column product cards; nav collapses to hamburger; vehicle selector stacks vertically |
| sm        | 480–768px | 2-column product grid; quick-search fields wrap 2-per-row |
| md        | 768–1024px| 3-column product grid; nav-bar shows inline links; floating nav pill remains edge-docked |
| lg        | 1024px+   | 4+ column product grid; full mega-menu nav; hero at full display-xl scale |

Touch targets should be a minimum 44px hit area for buttons and nav pills, especially the floating vertical `#floatNav` control observed in CSS. Mobile nav collapse and mega-menu behavior are proposed patterns for a vehicle-fitment catalog site, not confirmed interactions.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, DOM structure, or interaction states (hover/focus/active, mobile menu open/close) were directly observed. The two font tokens (`__Roboto_Condensed_*`, `__Open_Sans_*`) are Next.js local-font-optimization identifiers; their actual licensed typeface identity, weights available, and legal usage are unverified and reused verbatim rather than renamed. Font sizes, line-heights, and letter-spacing in the typography scale beyond the two explicitly observed CSS values (`1.1rem`/`1.2rem` on nav buttons) are proposed estimates, not measured. The gradient CSS variable (`--theme-primary-border-color`) is confirmed to exist but its actual applied element and visual prominence on the live site were not observed. Color-role assignments (e.g. red as "danger/badge", purple as "accent") are inferred from typical e-commerce conventions and adjacent variable naming, not confirmed usage. Responsive breakpoints and touch-target sizing are industry-standard recommendations, not measured from the source. Component definitions beyond `#floatNav` and `.Slider_exploreButton` are inferred from page-text structure (product listings, quick-search fields, footer contact block) rather than captured selectors.
