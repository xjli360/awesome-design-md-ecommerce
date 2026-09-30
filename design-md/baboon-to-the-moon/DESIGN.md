---
version: alpha
name: "Baboon to the Moon"
source_url: "https://baboontothemoon.com"
captured_at: "2026-09-28T04:34:51.685636+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Baboon to the Moon presents as a direct-to-consumer bag brand built on a
  stark black-and-white foundation punctuated by a warm orange accent
  (#fa6831) and a soft off-white canvas (#fafaf8). Body copy runs in
  Moderat, a humanist sans, at a compact 16px/1.4, while the single
  observed heading rule sets Moderat at 55px with tight -1.1px tracking
  and capitalized casing — treated here as the display-xl anchor. The
  "Add to Cart" button is the only fully specified component: a
  black-outlined pill (border-radius 50px, uppercase 'SW Baboon Type' at
  15–17px/700) that inverts to a solid black fill with white text on
  hover. This suggests a restrained, high-contrast interaction language
  reused across primary actions. Secondary and status colors (error
  #fc0000, warning #b60003, success #039f41, info #68b5ff) are drawn
  directly from declared CSS custom properties and are mapped to
  feedback UI, not decoration. Additional palette entries (yellow
  #ffd634, cream #efede3, blue-gray #d1d5db) are inferred as
  supporting surfaces and badge accents for an outdoor-adventure retail
  context; no multi-page layout, imagery, or mobile behavior was
  observed.

colors:
  primary: "#fa6831"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#202020"
  muted: "#a6a6a6"
  hairline: "#eeeeee"
  surface-soft: "#fafaf8"
  surface-card: "#efede3"
  on-primary: "#ffffff"
  accent: "#ffd634"
  accent-alt: "#68b5ff"
  success: "#039f41"
  success-text: "#000904"
  warning: "#b60003"
  warning-text: "#1d0000"
  error: "#fc0000"
  error-text: "#630000"
  review-stars-base: "#d1d5db"
typography:
  display-xl: {fontFamily: "Moderat, sans-serif", fontSize: 55px, fontWeight: 400, lineHeight: 1.0, letterSpacing: -1.1px}
  display-md: {fontFamily: "Moderat, sans-serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.6px}
  title-md: {fontFamily: "Moderat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Moderat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Moderat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Moderat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'SW Baboon Type', sans-serif", fontSize: 17px, fontWeight: 700, lineHeight: 1.45, letterSpacing: 0px, textTransform: uppercase}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  bag-color-swatch:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** renders the solid, filled state observed on `.button-atc:hover` — black background, white text, full pill radius — proposed here as the resting state for the site's primary calls to action (e.g. "Add to Bag," "Shop Now").

**button-secondary** mirrors the default (non-hover) `.button-atc` styling: transparent fill, black border and text. This outlined treatment is proposed for lower-emphasis actions like "Learn More" or filter toggles.

**text-input** is a proposed pattern for search and account forms, using the light hairline border and canvas background implied by the neutral gray tokens; no live input styling was captured.

**nav-bar** is inferred from the presence of `--header-height` and `--announcement-bar-height` custom properties, indicating a stacked header with an announcement strip; exact colors and content were not observed.

**product-card** proposes a warm cream (`surface-card`) container for duffel bag listings, giving product photography a neutral, gallery-like backdrop distinct from the pure-white canvas.

**hero** uses the observed display-xl heading style (55px Moderat, tight tracking, capitalized) atop the soft off-white surface, intended for landing and campaign pages.

**footer** is proposed as a dark, ink-colored band with inverted (white) text, a common DTC pattern; no footer-specific CSS was supplied.

**badge** applies the yellow accent as a small pill label (e.g. "Lifetime Warranty," "Bestseller"); this color-role pairing is inferred, not confirmed from component markup.

**search** proposes a rounded, hairline-bordered field consistent with the pill language established by the button component.

**bag-color-swatch** is a category-specific, unobserved pattern: a small circular selector for choosing duffel bag colorways, styled with a soft background and thin hairline ring to indicate selection — standard for bag/apparel PDPs but not verified on this site.

## Responsive Behavior

Recommendation only — not measured from live rendering:

| Breakpoint | Width | Notes |
|---|---|---|
| xs | up to 560px | inferred from `--layout-page-width-xs` |
| sm | 560–1020px | inferred from `--layout-page-width-sm` |
| md | 1020–1520px | inferred from `--layout-page-width-md` |
| lg | 1520px+ | inferred from `--layout-page-width-lg` |

Nav and hero elements likely collapse to a single column below `sm`. Touch targets on `button-primary`/`button-secondary` should maintain the observed 50–55px minimum height. Product grids are assumed to reflow from multi-column to single-column below `sm`, though this was not directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties and a small set of selector rules; no rendered page, DOM structure, or interaction states beyond `.button-atc` hover were observed. Font role assignments (Moderat for body/display, 'SW Baboon Type' for buttons) are drawn from actual `font-family` declarations, but weight and size choices for title-md, body-sm, caption, and display-md are proposed extrapolations, not measured values. Color role assignments (e.g., surface-card, accent, badge) are inferred pairings based on typical e-commerce patterns and are not confirmed against live component usage. Mobile layout, navigation behavior, cart/checkout flows, and product gallery interactions were not observed. Availability and licensing of 'SW Baboon Type' and 'Moderat'/'Moderat Condensed' as custom or licensed fonts were not verified.
