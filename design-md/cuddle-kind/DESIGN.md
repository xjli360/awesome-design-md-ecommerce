---
version: alpha
name: "Cuddle + Kind"
source_url: "https://cuddleandkind.com"
captured_at: "2026-09-28T04:25:11.772111+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cuddle + Kind presents as a warm, quietly minimal nursery-goods storefront built on a Shopify theme with CSS custom properties driving a near-monochrome base: a soft off-white canvas (#fcfbfc) paired with a slate-gray foreground (#54585a) used consistently for body text, links, and default buttons. Deeper charcoal (#303030) and pure black (#000000) appear in nested cart/upsell widgets for higher-contrast titles and buttons, suggesting a secondary "dark" button treatment. A dusty rose (#cf6d82) is explicitly reserved for sale pricing, while a teal (#1cadc0) and a green (#24b263) surface as functional accents in promotional widgets (add-to-cart CTA, discount price). A cluster of pale, nursery-appropriate tints (blush #feebe7, seafoam #eaf5f3, lavender #e7dbe3, mint #cdfee1) likely originates from product color-swatch options for the hand-knit dolls rather than core UI, and is treated here as an optional accent set. Typography combines Lora (serif, for display/heading warmth), Montserrat (sans, for body and UI text per the root font-body-family), and Moontime (a script face) inferred for a logo or decorative flourish. Layout specifics, hover states, and responsive breakpoints are not observed and are proposed below as reasonable defaults for a soft, artisanal e-commerce brand.

colors:
  primary: "#54585a"
  ink: "#303030"
  canvas: "#fcfbfc"
  body: "#54585a"
  muted: "#757575"
  hairline: "#e0e0e0"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#1cadc0"
  success: "#24b263"
  sale: "#cf6d82"
  badge-bg: "#ebe9f1"
  surface-blush: "#feebe7"
  surface-mint: "#cdfee1"
  border-subtle: "#dedede"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lora, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.02em}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.04em}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.04em}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.08em}
  script-accent: {fontFamily: "Moontime, cursive", fontSize: 28px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    salePriceColor: "{colors.sale}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-blush}"
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
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    swatchBorder: "1px solid {colors.hairline}"
    swatchBorderActive: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xxs}"

## Components
- **button-primary**: The dominant CTA style, matching the theme's `--color-button` slate gray with white text, used for "Add to Cart" and primary form submissions across the storefront.
- **button-secondary**: An outlined, low-contrast variant proposed for tertiary actions (e.g., "View Details"), reusing the primary slate for border and text on a white/canvas fill.
- **text-input**: A minimal bordered field for search, newsletter, and checkout forms; hairline border and generous padding suit the brand's soft, unhurried tone. States (focus, error) are proposed, not observed.
- **nav-bar**: A light, canvas-toned header bar inferred from the root color scheme; assumed sticky behavior and mobile hamburger collapse are proposed, not confirmed in the evidence.
- **product-card**: Displays hand-knit doll products with title, price, and optional sale-price styling in dusty rose; card border and radius are proposed defaults consistent with a soft, tactile brand feel.
- **hero**: A large, emotionally warm banner using a blush background tint (from the observed pale swatch cluster) with serif display type, appropriate for storytelling around the brand's "1 doll = 10 meals" mission.
- **footer**: A dark, high-contrast footer using the observed charcoal/black tones seen in nested widget buttons, providing visual grounding beneath a mostly light-toned site.
- **badge**: Small pill labels (e.g., "New," "Bestseller," or charity messaging) using the lavender-toned `#ebe9f1` background observed in the free-gift widget header.
- **search**: A rounded, soft-bordered search affordance consistent with the theme's understated aesthetic; icon and dropdown behavior are proposed.
- **color-swatch-selector**: A category-specific pattern for selecting doll/yarn color variants, drawing on the cluster of pale, nursery-friendly hues (blush, mint, seafoam, lavender) present in the palette; active-state ring uses the primary slate color.

## Responsive Behavior
This is a proposed structure, not measured site behavior.

| Breakpoint | Range | Layout notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column stacking, nav collapses to hamburger/drawer, product grid 2-up |
| Tablet | 600–959px | Product grid 2–3 up, hero text scales down one step |
| Desktop | 960–1279px | Product grid 3–4 up, full nav bar visible |
| Wide | 1280px+ | Max content width constrained, additional whitespace at edges |

Touch targets for buttons and swatches should be at minimum 44×44px. Nav collapse and drawer/menu interaction patterns are inferred conventions for Shopify-based storefronts and have not been observed directly.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, hardcoded widget colors, and a font list; no rendered page, DOM structure, or interaction states were observed. The mapping of `--color-background-contrast` (rgb 197,178,197) could not be resolved to an exact palette hex and was omitted rather than approximated. Font role assignments (Lora for display, Montserrat for body, Moontime for script accents) are inferred from naming/style conventions, not confirmed CSS usage on specific elements. All pixel sizes in typography, spacing, and rounding scales are proposed defaults, not measured values, except where explicitly noted as observed (e.g., root font-size and letter-spacing declarations). Hover, focus, active, and error states for all components are proposed and unverified. Mobile menu, cart drawer, and checkout flow layouts were not observed. Availability and licensing of the Moontime typeface for production use has not been verified.
