---
version: alpha
name: "JL Audio"
source_url: "https://jlaudio.com"
captured_at: "2026-09-29T04:07:38.213567+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from JL Audio's current product presentation on Garmin's
  commerce platform (garmin.com/en-US/c/jlaudio/), reflecting Garmin's ownership of the
  brand rather than a reconstruction of any former independent JL Audio storefront. The
  observed palette is dominated by neutral blacks, whites, and grays (#000000, #ffffff,
  #1a1a1a, #eeeeee, #d8d8d8, #333333, #666666), consistent with a technical, product-photo-
  forward catalog layout. A cooler blue family (#106fad, #6dcff6, #60cff6, #3d6d8f) appears
  in the shared Garmin design-system CSS and is inferred here as the primary interactive/
  link color. A dark red (#920000) and warm amber tones (#ff9b00, #f0c36d, #af7501) are
  present in the evidence and are proposed for alert, sale, and focus states, not confirmed
  as JL Audio brand colors. Typography relies on Garmin's platform stack: Oswald and
  Roboto Condensed for condensed display headings, Roboto/Arial for body copy, and a
  proprietary "Knockout-JuniorWelterwt" family observed in the font list, used here for a
  bold hero display role. Layout guidance uses Garmin's own CSS breakpoint and spacing
  custom properties where available, with intermediate values proposed for finer control.
  All semantic color-to-role and radius assignments are inferred, not measured.

colors:
  primary: "#106fad"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#d8d8d8"
  surface-soft: "#f2f2f2"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-alert: "#920000"
  accent-highlight: "#ff9b00"
  tooltip-bg: "#f9edbe"
  link-active: "#6dcff6"
  focus-ring: "#af7501"
typography:
  display-xl: {fontFamily: "Knockout-JuniorWelterwt, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
  section: 80px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusRing: "{colors.focus-ring}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.link-active}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  compare-tray:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** proposes a solid blue call-to-action (Shop, Add to Cart) using the inferred `primary` blue against white text, sized for touch with generous horizontal padding; hover/active states are not observed and are proposed only.

**button-secondary** is an outlined variant sharing the primary hue for text and border on a white background, intended for secondary actions like "Compare" or "Find a Dealer" links seen in the source text; state transitions are unverified.

**text-input** models search and account fields with a light hairline border and a proposed amber focus ring (`focus-ring`), since no explicit focus-state CSS was present in the supplied evidence.

**nav-bar** is inferred as a dark, near-black bar carrying the category links observed in the text excerpt (SMARTWATCHES, AUTO & HOME, MARINE, SALE, etc.), with condensed body typography and a lighter blue hover state for wayfinding.

**product-card** reflects the repeating "Shop All / Marine / Motorsports / Car / Home" grid pattern from the excerpt: a light gray card surface, hairline border, condensed title, and plain-black price line, with rounded corners proposed for a modern catalog feel.

**hero** is a full-bleed dark band using the bold Knockout-style display face for the "JL AUDIO®" brand statement and body copy for the descriptive paragraph, matching the long-form brand intro text present in the evidence.

**footer** consolidates the extensive Customer Service/Company/Platforms link columns visible in the excerpt onto a black background with muted gray body text and white link text, typical of the parent Garmin site architecture.

**badge** is proposed for "SALE" or feature callouts using the dark red accent color at full pill radius, since a sale category link is present in the navigation text though no badge CSS was directly observed.

**search** models a soft-gray input field consistent with the neutral surface tones in the palette; no explicit search-bar selector was present in evidence, so styling is proposed by extension of the input pattern.

**compare-tray** is a category-specific proposed component supporting the "COMPARE" feature referenced in the source text, using the same soft-surface treatment as product cards to visually group selected items for side-by-side review.

## Responsive Behavior

Recommended breakpoints, adapted directly from the observed `--g-breakpoint-*` custom properties in the supplied CSS:

| Token | Value | Notes |
|---|---|---|
| xs | 480px | phone |
| sm | 768px | tablet portrait (also `standard`) |
| md | 1024px | tablet landscape |
| lg | 1200px | small desktop |
| xl | 1350px | desktop |
| xxl | 1440px | large desktop |
| xxxl | 1824px | ultra-wide |

Below `sm`, navigation is proposed to collapse into a hamburger/off-canvas menu, and product-card grids proposed to drop from multi-column to single/double column. Touch targets are recommended at a minimum 44×44px for buttons and nav items. This table is a recommendation based on the observed CSS variables, not measured interactive site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, color/font lists, and page text supplied as evidence, not from live rendering or interaction testing. The page evidence originates from Garmin's product-category template (garmin.com), the current parent-site presentation of JL Audio; no independent former JL Audio site was observed or reconstructed. Color-to-role mapping (e.g., which blue is truly "primary" versus decorative) is inferred, since no selector-level evidence ties specific hexes to buttons or links. Font sizes, weights, line-heights, and letter-spacing are proposed values, not confirmed via computed-style CSS. The `rounded` scale is entirely proposed, as no border-radius values appeared in evidence. Spacing values for `xxs`, `md`, and `xxl` are interpolated; only `xs`, `sm`, `base`(1rem), `lg`, `xl`, and `section`(5rem) trace to observed `--g-spacing-*` variables. Mobile layout, hover/focus states, and component interactions were not observed and are labeled proposed throughout. Availability and licensing of "Knockout-JuniorWelterwt" and other listed fonts have not been verified for reuse outside this evidence context.
