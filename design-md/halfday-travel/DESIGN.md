---
version: alpha
name: "Halfday Travel"
source_url: "https://halfdaytravel.com"
captured_at: "2026-09-28T05:04:30.443725+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Halfday's storefront pairs a warm, tailored neutral palette with a single
  deep-forest accent (#013d1c), observed as the header's transparent-state
  text color and as an overlay text color on a featured-product section.
  Because the header/announcement-bar background and primary button color
  in the source CSS were expressed as raw RGB triplets outside the supplied
  hex palette, they are not reproduced here; #013d1c is used as the inferred
  primary brand color instead, a reasonable substitute given its confirmed
  presence in the palette and its brand-adjacent use. Canvas is pure white
  with soft cream/stone neutrals (#f5f5f5, #e8e1d6, #bcb5a6) suited to a
  premium travel-goods catalog, and a cluster of olive, marine, and amber
  tones (#5c5c42, #3e5165, #c8822d, #204e08) map to the brand's product
  color-swatch naming (Jet, Pacific, Olive, Marine, Stone, Golden Poppy).
  Typography uses Figtree for UI/body copy and a Roslindale display family
  (Display, DisplayCondensed, DeckNarrow, Text) for headlines, both directly
  observed as loaded font-family values; specific weights and tracking are
  proposed, not measured. Layout spacing follows the site's CSS custom
  property scale (spacing tokens derived from --spacing-N usage), applied
  here as an inferred, evidence-consistent system for cards, sections, and
  navigation.

colors:
  primary: "#013d1c"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#434144"
  muted: "#74787d"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#e8e1d6"
  on-primary: "#ffffff"
  accent-olive: "#5c5c42"
  accent-forest: "#204e08"
  accent-marine: "#3e5165"
  accent-slate: "#38424c"
  accent-amber: "#c8822d"
  accent-stone: "#bcb5a6"
  accent-tan: "#93816e"
  link: "#1990c6"
  error: "#e41111"
typography:
  display-xl: {fontFamily: "RoslindaleDisplay, serif", fontSize: "64px", fontWeight: 500, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "RoslindaleDisplay, serif", fontSize: "40px", fontWeight: 500, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "RoslindaleDisplayCondensed, serif", fontSize: "26px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: "11px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.4px"}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.3px"}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-stone}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch:
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"

## Components

**button-primary** is the primary call-to-action treatment ("Shop Now", "Add to cart"), using the inferred deep-forest primary color against white text; a hover-darkened or opacity-reduced state is proposed but not confirmed in captured CSS. **button-secondary** offers an outlined variant for lower-emphasis actions such as "Shop Bundles," reusing the primary color as border and text on a white field. **text-input** covers email capture (newsletter) and search fields, styled with a thin hairline border and compact body typography consistent with the dense, utilitarian header/footer copy observed. **nav-bar** reflects the sticky, three-column header grid pattern (`main-nav / logo / secondary-nav`) referenced in the CSS grid-template values, rendered here as a white bar with hairline underline; exact collapse into a mobile menu is proposed, not observed. **product-card** represents the repeating duffel/tote/garment-bag tiles seen in the featured-collection grid, using the warm cream surface-card tone and title/price typography pairing; swatch rows beneath each card use the **color-swatch** component, a category-specific pattern for the brand's named colorways (Jet, Pacific, Olive, Marine, Stone, etc.), rendered as small circular selectors with a primary-colored selected ring. **hero** models the large collection-intro banner ("Built-In Garment Bags for Wrinkle-Free Travel"), using a deep forest background with display-scale Roslindale type per the h0/h1 custom properties. **footer** consolidates the Company/Support/Policies link columns into a dark, ink-toned band with stone-tinted links, matching the multi-column footer content in the page text. **badge** covers recurring trust markers like "5,000+ Five Star Reviews" and "New"/"Bestseller" labels, using an amber pill for visual warmth against the neutral catalog. **search** is a proposed lightweight overlay/input pattern triggered from the header's "Search" affordance, styled consistently with text-input.

## Responsive Behavior

Proposed breakpoints (not measured): mobile ≤480px, tablet 481–1024px, desktop ≥1025px, matching the CSS's evidence of at least two responsive custom-property tiers (smaller `--text-h*`/spacing values at narrow widths, larger at wide widths, plus a header grid-template swap between stacked and inline logo/nav order). Navigation is expected to collapse to a hamburger/off-canvas menu below tablet width; the header's logo dimensions grow from 70×28px to 90×36px at larger breakpoints per observed custom properties. Product-list grids shift from a horizontal carousel (single-column-equivalent, ~74vw item width) on mobile to 2-up (~36vw) at mid-width and a fixed 3-up grid at desktop, per the `--product-list-items-per-row` values. Touch targets for buttons and swatches should target a minimum 44×44px hit area; this is a general accessibility recommendation, not a site-measured behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom-property dumps, class-selector fragments, and page text only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions were observed. The header background, announcement-bar background, and primary-button background appeared in the source as raw RGB triplets (e.g., "7 58 36", "254 208 12") rather than confirmed hex values in the supplied palette, so they were excluded from color roles rather than approximated. Font weights, letter-spacing, and the exact Roslindale sub-family used per heading level are inferred/proposed, not confirmed via computed style. Mobile menu behavior, cart-drawer interaction, and swatch selection states are proposed patterns based on typical e-commerce conventions, not observed DOM/interaction evidence. Availability, licensing, and web-font-loading status of the Roslindale family and Figtree were not verified.
