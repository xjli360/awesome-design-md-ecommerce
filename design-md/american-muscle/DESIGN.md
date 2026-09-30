---
version: alpha
name: "American Muscle"
source_url: "https://americanmuscle.com"
captured_at: "2026-09-28T09:41:56.263244+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  AmericanMuscle.com is a high-density e-commerce catalog for muscle-car and truck performance parts, organized around large mega-navigation, product grids, and fitment-driven badges. The observed CSS exposes a signature cyan-blue (#1891cd) used repeatedly for links, hover states, badge text, and tooltip borders, functioning as the de facto primary/interactive color. Body and price text render in near-black grayscale tokens (#212121, #414042), with a secondary muted gray (#797979) for fitment labels, review counts, and struck-through original prices. Surfaces lean on whites and very light grays (#ffffff, #f9fafa, #f5f5f5, #eceeef) for cards and panels, with hairline dividers in soft blue-gray (#e2e5e7). Status colors are drawn directly from evidence: green (#0cc000) for "saved"/success states, red (#cc0000) for warnings/error borders, and orange (#f5821f) reserved as an inferred accent for promotional callouts. Typography combines "Inter" for prices and numeric UI, "Roboto Flex" for emphasis labels (save-for-later, badges), and system Arial/Helvetica fallbacks elsewhere — all observed families, with sizes above 18px extrapolated for headings since only small UI text sizes (12–18px) were present in evidence. Layout, spacing rhythm, and breakpoints below are proposed conventions for a dense automotive-parts storefront, not measured observations.

colors:
  primary: "#1891cd"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#414042"
  muted: "#797979"
  hairline: "#e2e5e7"
  surface-soft: "#f9fafa"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  success: "#0cc000"
  danger: "#cc0000"
  accent: "#f5821f"
  border-strong: "#a0a9b1"
typography:
  display-xl: {fontFamily: "Roboto Flex, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto Flex, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  button-md: {fontFamily: "Roboto Flex, sans-serif", fontSize: 16px, fontWeight: 900, lineHeight: 1.2, letterSpacing: 0.25px}
  price-lg: {fontFamily: "Inter, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    priceTypography: "{typography.price-lg}"
    captionTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    overlay: "rgba(255,255,255,.32)"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accent: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed cyan-blue (#1891cd) as an inferred call-to-action fill, since evidence shows this hue driving hover links, badge text, and tooltip accents throughout the UI — a plausible extension to a solid CTA. **button-secondary** proposes an outline variant sharing the same blue for text/border on a white ground, useful for lower-emphasis actions like "Add to Garage." **text-input** and **search** are proposed patterns using the muted hairline/border-strong grays observed on tooltip and card borders; no live input styling was captured. **nav-bar** is inferred from the extensive mega-menu category list in the page text, styled with light canvas and hairline dividers consistent with the light card backgrounds seen in CSS. **product-card** directly reflects observed rules: 12px caption-weight fitment text in muted gray, a bold 18px Inter price, and a strikethrough 12px original-price treatment — this is the most evidence-grounded component. **hero** is proposed, using the one captured overlay treatment (`rgba(255,255,255,.32)` ghost-button hover) as a cue for a dark hero with translucent CTA. **footer** and **badge** are inferred layout conventions; the badge component pulls its neutral gray fill and pill radius from the observed `.wheel_tire_kit_badge` rule. **fitment-selector** is a category-appropriate proposed component representing AmericanMuscle's core "select your vehicle" interaction pattern implied by the extensive make/model navigation, though no selector-specific CSS was observed.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Width       | Behavior (proposed) |
|-----------|-------------|----------------------|
| mobile    | <480px      | Single-column product grid, collapsed hamburger nav, sticky fitment bar |
| tablet    | 480–1024px  | Two-column product grid, condensed mega-menu accordions |
| desktop   | 1024–1440px | Full mega-nav flyouts, 3–4 column product grid |
| wide      | >1440px     | 4–5 column grid, persistent sidebar filters |

Touch targets should maintain a minimum 44px hit area for nav and filter controls; mega-menu categories should collapse into accordions below tablet width. This table is a proposed convention for a parts-catalog site, not a measured layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Role assignments (primary, muted, hairline, surface tokens) are inferred from selector context (e.g., `.tooltip`, `.price_container`) rather than verified design-system documentation. All font sizes above 18px, spacing scale, rounded scale, and breakpoint table are proposed conventions, not measured values. Hover/focus/active states beyond the single captured `.button_container .main_btn.ghost:hover` overlay are unverified. Mobile navigation collapse, fitment-selector interaction, and cart/checkout flows were not observed. Availability and licensing of "Roboto Flex" and "Inter" as custom web fonts on this domain were not verified beyond their appearance in CSS `font-family` declarations.
