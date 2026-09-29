---
version: alpha
name: "Spicewalla"
source_url: "https://spicewallabrand.com"
captured_at: "2026-09-28T09:10:38.709612+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Spicewalla's storefront runs on a Shopify theme whose CSS custom properties define
  a warm, high-key palette: a pale chartreuse-cream canvas (#fcfdeb), a deep navy-ink
  foreground (#0c2038), and a saturated magenta-pink action color (#d71773) used for
  buttons, links, and review-widget accents. White (#ffffff) serves as the on-primary
  text color and card surface. A secondary tier of hot spice-inspired hues — gold
  (#ffc810), orange (#f1a12e), red (#ca2026), and green (#84cb96) — appears in
  merchandising/promo contexts such as announcement bars and star ratings, and is
  treated here as accent/status color, inferred rather than confirmed as a formal
  brand system. Typography draws on an "Assistant" sans-serif for body copy and a
  distinct "Cassannet" family referenced in the heading font-stack; since no weight,
  size, or licensing detail is exposed beyond the CSS variable names, heading usage
  is labeled inferred. Multiple observed button and badge rules set border-radius to
  0, suggesting a squared, utilitarian visual language that this spec extends
  cautiously into a restrained rounded-corner scale for cards only. Spacing values
  are proposed, not measured, since no explicit spacing scale was present in the
  supplied CSS.

colors:
  primary: "#d71773"
  ink: "#0c2038"
  canvas: "#fcfdeb"
  body: "#4a4a4a"
  muted: "#6d6d6d"
  hairline: "#eeeeee"
  surface-soft: "#f9f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-berry: "#991e5c"
  accent-gold: "#ffc810"
  accent-orange: "#f1a12e"
  accent-green: "#84cb96"
  alert-red: "#ca2026"
  link-blue: "#4466ad"
  info-blue: "#1990c6"
  info-blue-hover: "#136f99"
  tint-pink: "#ffeaf3"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Cassannet, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Cassannet, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Assistant, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.9px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.5px}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
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
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  heat-level-indicator:
    backgroundColor: "{colors.tint-pink}"
    accentColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** maps to the observed `--color-button` (#d71773) and `--color-button-text` (#ffffff) variables that drive the theme's primary CTA styling (add-to-cart, checkout). Radius is set to none, mirroring the 0-radius defaults seen on the gift-button and accelerated-checkout CSS. Hover/disabled states were not present in the supplied CSS and are proposed only.

**button-secondary** inverts the primary pairing using `--color-secondary-button` and `--color-secondary-button-text`, both resolving to canvas and primary-pink respectively — an observed variable pattern used for outline-style CTAs such as "Continue shopping."

**text-input** is proposed; no explicit form-field CSS was supplied, so surface, border, and radius values are inferred from the general card/hairline palette to keep fields visually consistent with product cards.

**nav-bar** reflects the canvas background and ink foreground pairing used site-wide (per `:root` color variables), supporting the extensive mega-menu structure implied by the page text (Spices and Herbs, Blends, Pantry & Snacks, etc.). Sticky/scroll behavior is not observed.

**product-card** is inferred from the `.product-card-wrapper .card` rule, which exposes CSS custom properties for border-radius, border-width, and shadow but not their resolved values; a small radius and white surface are proposed as a neutral default consistent with the theme's card-shadow variables.

**hero** is a proposed composition combining the display typography scale with the canvas background, intended for homepage banners referencing content like "What I'd Cook First" and the cookbook bundle promotion described in the page text; no hero-specific CSS was supplied.

**footer** inverts to the ink color for contrast, a pattern proposed rather than observed, since no footer-specific selector was present in the supplied CSS; link color borrows the gold accent used elsewhere for review stars.

**badge** draws directly from the observed `--color-badge-foreground`, `--color-badge-background`, and `--color-badge-border` variables (ink-on-canvas with an ink border), likely used for tags such as "Sale" or "Sold out" seen in the product listings.

**search** is proposed using the soft off-white surface tone (#f9f9fa) observed in skeleton/loading states, paired with muted placeholder text; no search-input CSS was directly supplied.

**heat-level-indicator** is a category-specific, fully proposed component for a spice-heat or flavor-profile chip, using the soft pink tint (#ffeaf3) and orange accent (#f1a12e) drawn from the observed palette to visually flag chili/heat intensity on product cards — not present in any supplied selector.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column nav collapses to a hamburger/drawer; product grid 1–2 columns; touch targets minimum 44px. |
| Tablet | 600–989px | Product grid 2–3 columns; nav mega-menu may collapse to accordion. |
| Desktop | 990px+ | Full horizontal nav with mega-menu dropdowns; product grid 3–4 columns. |

Buttons and search inputs should maintain a minimum 44×44px touch target on mobile. Mega-menu collapse behavior and any sticky-header interaction were not observed and are proposed for accessibility consistency only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction and a single page-text excerpt; no rendered layout, hover/focus states, animation timing beyond the declared duration tokens, or actual mobile behavior were observed. The heading font (`Cassannet`) and an additional stack entry (`Affogato`) appear only as font-family tokens with no accompanying weight, size, or license metadata — their use, availability, and legal status as custom/purchased fonts are unverified. The mapping of `--color-foreground` (rgb 6,35,57) to the closest supplied hex (`#0c2038`) is an approximation, not an exact match. Spacing scale values, rounded-corner sizes beyond the observed `0` defaults, and several typography sizes are proposed placeholders rather than measured CSS values. Component states (hover, active, disabled, error) are not present in the supplied evidence and are marked proposed throughout.
