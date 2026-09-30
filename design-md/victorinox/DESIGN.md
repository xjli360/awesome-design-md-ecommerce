---
version: alpha
name: "Victorinox"
source_url: "https://victorinox.com"
captured_at: "2026-09-28T04:34:39.541172+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from static CSS extraction of victorinox.com's Next.js bundles, not live rendering. Font families surface only as compiled local-font identifiers (__primary_de0095 and __secondary_ff92be plus their _Fallback variants), so the actual typeface names, weights available, and licensing are unverified; sizes, weights, and line-heights below are proposed unless a rule explicitly set them. The color evidence includes a strong red (#b10034) used near button/hover variable names, a near-black ink (#000000), warm neutral grays (#959499, #707070, #343434, #292929), light surfaces (#ffffff, #f2f2f2, #f0f0f0), hairline grays (#dadada, #aeaeae), and a large ramp of pink/magenta and gray tint steps likely reserved for imagery, promotional badges, or swatch UI rather than core brand chrome. A blue (#2299dd) and amber (#ffc107) appear but are treated as inferred utility/status colors given no confirming selector context. The design system below assumes a restrained, editorial luggage retailer aesthetic: dark ink text on white/light-gray surfaces, the red reserved for primary actions and brand accents, generous whitespace, and squared-to-soft rounded corners consistent with the near-zero border-radius reset observed on form controls.

colors:
  primary: "#b10034"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#343434"
  muted: "#959499"
  hairline: "#dadada"
  surface-soft: "#f2f2f2"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  border-strong: "#707070"
  text-secondary: "#292929"
  accent-info: "#2299dd"
  accent-warning: "#ffc107"
  accent-success: "#699769"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "__primary_de0095, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "__primary_de0095, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "__primary_de0095, sans-serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "__secondary_ff92be, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "__secondary_ff92be, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "__secondary_ff92be, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "__primary_de0095, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.4px"}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.text-secondary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineTop: "{colors.border-strong}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-gallery:
    backgroundColor: "{colors.canvas}"
    thumbBorder: "{colors.hairline}"
    thumbBorderActive: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"

## Components
**button-primary** carries the red accent as the sole strong call-to-action fill, using on-primary white text; hover/active states in the CSS swap toward white background with primary-colored text, so an inverted hover treatment is proposed here as a state, not fully re-specified. **button-secondary** is an outlined variant for lower-emphasis actions like "add to wishlist," proposed to inherit the same red on a white field. **text-input** uses the near-zero border-radius reset seen on native form elements, paired with a light hairline border; focus-ring styling was not observed and is proposed. **nav-bar** is a light, hairline-bottomed bar assumed from the white/gray palette balance; sticky behavior is not confirmed. **product-card** targets soft-luggage listings, using the slightly darker off-white surface-card tone to separate cards from the page canvas, with title and price typography scaled for scanability. **hero** assumes a dark, full-bleed banner suited to travel/luggage photography, with a scrim overlay token available for text legibility; this composition is proposed, not measured. **footer** uses the darker neutral (#292929) as an inferred footer background, a common pattern for retail sites, though the source CSS did not confirm this section's colors directly. **badge** repurposes the amber tint for promotional or "new" labels since no dedicated badge selector was found; role is inferred. **search** proposes a soft-gray input field consistent with the neutral surface tones. **product-gallery** is grounded directly in observed CSS (`.product-gallery_root__8n0lk`, swiper thumb-active border-color:black), representing the image swiper used on product detail pages for soft luggage items.

## Responsive Behavior
The following breakpoints are a recommendation only; no responsive/mobile layout was observed in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | 0–599px | Single-column stacking, nav collapses to a menu icon |
| tablet | 600–959px | Two-column product grids, condensed nav |
| desktop | 960–1279px | Full nav bar, multi-column grids |
| wide | 1280px+ | Max-width content container, larger hero imagery |

Touch targets should be at least 44×44px for buttons and nav items (proposed). Navigation is assumed to collapse into a hamburger/drawer pattern below tablet width; this has not been verified against actual markup or breakpoints in the site's CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/JS bundle extraction; no rendered page, DOM, or JavaScript-driven interaction was observed. Font family tokens (__primary_de0095, __secondary_ff92be) are Next.js compiled local-font identifiers — the underlying typeface design, weight availability, and licensing terms are unverified and must be confirmed against actual @font-face declarations before production use. Semantic color roles (primary action, footer background, badge/status colors) are inferred from typical retail-site conventions and variable-name context (e.g., `--color-primary`, `--color-white`) rather than confirmed visual screenshots. All typographic sizes, weights, and line-heights beyond generic resets are proposed placeholders, not measured values. Hover/active states for buttons are partially evidenced (white-fill/primary-text swap) but full interaction states, focus rings, and transitions are not observed. Mobile/responsive layout, breakpoint values, and navigation collapse behavior are entirely proposed and require validation against live rendering and design review.
