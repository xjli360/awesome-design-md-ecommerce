---
version: alpha
name: "Noted Candles"
source_url: "https://notedcandles.com"
captured_at: "2026-09-28T09:51:04.058872+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Noted Candles' storefront runs on a Shopify theme with multiple pre-built
  color schemes; the surveyed CSS custom properties define a warm, neutral
  base (white and near-white backgrounds, black text and buttons) accented by
  an rgb(214,58,47) "primary" variable used sparingly for sale badges and
  price callouts. That exact hex was not present in the captured swatch list,
  so the primary role here is mapped, as an inferred approximation, to the
  closest observed rust/terracotta swatch, #8e1f0b, consistent with the
  brand's handmade, warm-toned candle imagery. Secondary schemes introduce
  deep browns (used for the classroom/workshop sections) and a muted taupe,
  represented here by the observed #8a5a46 and #c5ada3 swatches. Typography
  combines Poppins for headings/buttons with Nunito Sans for body copy,
  matching the two named webfonts in the evidence; system-ui and Helvetica
  Neue serve as fallbacks. The resulting interpretation favors generous
  whitespace, soft neutral card surfaces, and restrained use of the rust
  accent for calls-to-action, badges, and scent-category highlights, fitting
  a small-batch, woman-owned gift-and-candle retailer with an in-store
  classroom and curated shop.

colors:
  primary: "#8e1f0b"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#ededed"
  surface-soft: "#f2f2f2"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-earth: "#8a5a46"
  accent-warm: "#c5ada3"
  alert: "#d00000"
  success: "#15803d"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.accent-earth}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  scent-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** is proposed as a solid black button with white text, matching the `--color-button: 0,0,0` / `--color-button-text: 255,255,255` pairing seen across most schemes, used for "Add to Cart" and primary CTAs.

**button-secondary** uses a white/canvas fill with a hairline border, mirroring `--color-secondary-button` and `--color-secondary-button-border` values; proposed for lower-emphasis actions like "View full details."

**text-input** is proposed with a light soft-gray fill (`--color-field: 245,245,245` equivalent) and dark text, used for search boxes, quantity fields, and the "Ask a question" form fields referenced in the page content.

**nav-bar** is inferred as a white top bar with black wordmark/link text and a hairline bottom border, consistent with the default `color-scheme-1` background/border pairing; dropdown mega-menu states (Shop by Scent, Shop by Category) are proposed, not observed in static CSS.

**product-card** groups a soft off-white or white surface with an 8px radius, used for candle/diffuser listings and the "New in the Shop" grid; hover elevation is proposed, not verified.

**hero** is modeled on the brown-toned `desktop-color-scheme-2`/`6` variables (background rgb 110,51,26 and 88,44,25, approximated here via the observed `#8a5a46` swatch) with white heading/body text, suited to the "made here. discovered here. created by you." banner section.

**footer** uses a soft neutral background distinct from pure white, holding contact details (address, phone, email) and social links in small body copy; multi-column layout is proposed, not measured.

**badge** applies the primary rust/red accent for SALE labels and scent tags such as "NEW!", using small caption-weight type and a tight radius.

**search** is a pill-shaped input proposed for the header search affordance, using the same soft field background as text-input but with a fully rounded corner for visual distinction.

**scent-chip** is a category-specific component representing the extensive "Shop by Scent" list (Cedar Vetiver, Meyer Lemon, Sea Salt Sage, etc.) as rounded pill filters or tags, using hairline borders and muted body text on a white ground.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column product grid, collapsed hamburger nav, stacked hero text over image. |
| Tablet | 600–1023px | Two-column product/scent grids, nav collapses into a condensed bar with a search icon. |
| Desktop | 1024px+ | Multi-column mega-menu navigation, 3–4 column product grids, side-by-side hero text/image. |

Touch targets are recommended at a minimum 44×44px for nav links, scent chips, and cart controls. Mega-menu categories (Shop by Scent, Shop by Category, Shop by Values) should collapse into accordions on mobile. This table is a recommendation based on common e-commerce patterns and the theme's multi-scheme structure; it is not a measurement of the live responsive implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a text excerpt, and a color/font list, not from a rendered or interactive session. The exact hex for the theme's `--color-primary` (rgb 214,58,47) was not present in the supplied swatch array, so `colors.primary` is an approximated mapping to the closest observed hex (`#8e1f0b`) and should be re-verified against a live inspection. Role assignments for muted text, hairline borders, and soft surfaces are inferred from likely usage patterns rather than confirmed selector-to-role bindings. Layout structure (grid columns, mega-menu behavior, card hover states, mobile navigation collapse) is proposed based on typical Shopify theme conventions and is not confirmed from DOM/layout observation. Font availability, licensing, and exact weight/size values for Poppins and Nunito Sans were not verified beyond their appearance in the font-family list; declared type sizes are proposed defaults, not measured computed styles.
