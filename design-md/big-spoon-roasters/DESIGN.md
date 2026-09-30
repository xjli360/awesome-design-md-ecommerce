---
version: alpha
name: "Big Spoon Roasters"
source_url: "https://bigspoonroasters.com"
captured_at: "2026-09-28T05:01:51.009207+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Big Spoon Roasters is a Hillsborough, NC maker of handcrafted nut butters, snack bars, and a dog-safe "Wag Butter" line, sold through a Shopify storefront with a clean, ingredient-forward aesthetic. The measured CSS custom properties show a near-neutral system: near-black text and primary actions (#222222), a white canvas (#ffffff), and light gray surfaces (#f0f0f0, #eeeeee, #ededed) used for section backgrounds, borders, and secondary buttons. A muted slate tone (#676986) appears in the third-party review widget for secondary metadata text. A warm tan (#a38a66) is present in the broader palette and is inferred here as a roasted-nut accent for labels or swatches rather than a confirmed brand color, since its role was not explicitly declared. Typography is split between a heading family (interpreted as GothaSemNarMed, observed in the codebase) and DM Sans for body copy, with gotham-bold explicitly used for button labels in the reviews widget. This interpretation favors generous whitespace, jar-like rounded product cards, and restrained sans-serif type to reflect a small-batch, kitchen-crafted food brand rather than a loud e-commerce template. All sizes not explicitly present in the supplied CSS are proposed and marked accordingly.

colors:
  primary: "#222222"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#676986"
  hairline: "#eeeeee"
  surface-soft: "#f0f0f0"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  btn-secondary-bg: "#ededed"
  hover-dark: "#000000"
  accent-warm: "#a38a66"
  alert: "#dc2626"
typography:
  display-xl: {fontFamily: "GothaSemNarMed, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GothaSemNarMed, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "GothaSemNarMed, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "DM Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "DM Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "gotham-bold, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.btn-secondary-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** uses the observed near-black `--color-btn-bg` (#222222) with white text, darkening to pure black (#000000) on hover per the `--color-btn-bg-hover` token; used for "Shop Now," "Choose Options," and cart actions. **button-secondary** reflects the observed `--color-btn-secondary-bg` (#ededed) light-gray fill with dark text, suited to "Quick View" or filter toggles; hover state is proposed. **text-input** is inferred from the general field-color tokens (`--color-field-bg`, `--color-field-text`) and given a light hairline border for search and newsletter forms; focus-ring styling is proposed, not observed. **nav-bar** models the sticky header implied by the "Skip to content" and mega-menu label structure (Shop, Collections, Discover, Learn, Wholesale); collapse behavior into a mobile drawer is proposed. **product-card** groups the repeated title/price/quick-view pattern seen in the product grid (e.g., Cherry Pie Cashew & Almond Butter, Lemon Cookie Cashew Butter), applying the light card surface and standard hairline border. **hero** is proposed for the banner announcing "ELEVATE YOUR TOAST" and the Wag Butter promotion, using the soft gray section background for visual separation from the white body. **footer** is proposed as an inverse dark-on-light-text zone to anchor secondary navigation (FAQ, Press, Wholesale Inquiry, social links); the dark fill is inferred from the ink color rather than a directly observed footer rule. **badge** is proposed for promotional flags like "FREE shipping on orders of $70+" or "Summer Limited Batch," using the warm tan accent as a food-craft cue. **search** styling is inferred from generic field tokens since no dedicated search-bar CSS was supplied. **subscription-toggle** is a category-appropriate proposed component for the site's "Subscriptions" collection, letting shoppers choose one-time vs. recurring nut-butter delivery with an active state in the primary ink color.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Width | Behavior |
|---|---|---|
| Mobile | <600px | Single-column product grid, nav collapses to a hamburger/drawer, hero stacks text above image. |
| Tablet | 600–959px | Two-column product grid, condensed nav with mega-menu simplified to accordions. |
| Desktop | 960–1279px | Three to four-column product grid, full horizontal nav with mega-menu dropdowns. |
| Wide | ≥1280px | Max content width with increased section padding (`{spacing.section}`). |

Touch targets should be at least 44px tall (matching the observed 44px height on `.oke-button`). Mobile nav collapse, sticky-header behavior, and cart-drawer interactions are proposed patterns only; no interaction states were captured from the static evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a text excerpt, and a partial color/font inventory — no live rendering, computed layout, or DOM screenshots were available. Font-family assignments for headings (GothaSemNarMed) and buttons (gotham-bold) are taken directly from class references in the CSS but their license/hosting status was not verified, and fallback rendering may differ from the brand's intended look. The `--font-body-family` and `--font-heading-family` variables were referenced but not resolved to literal values in the supplied evidence, so DM Sans/GothaSemNarMed assignments are best-effort inference from the broader font list, not confirmed computed styles. Several palette entries (e.g., payment-icon colors like #eb001b, #0071ce, #f79e1b) appear to belong to third-party payment badges or the Okendo reviews widget rather than the core brand system and were intentionally excluded from primary role assignments. All pixel sizes, spacing scale, rounded-corner values, hover/focus states, and mobile-menu behavior are proposed conventions for a food/DTC storefront and have not been visually confirmed against the live site.
