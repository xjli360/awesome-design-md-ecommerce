---
version: alpha
name: "Spearmint Love"
source_url: "https://spearmintlove.com"
captured_at: "2026-09-29T04:08:16.596158+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Spearmint Love's storefront CSS exposes a restrained neutral-gray system (#333333, #6a6a6a,
  #7a7a7a, #292929, #dddddd) layered over a white canvas, consistent with a product-detail-led
  Shopify build using a variant swatch selector (jdgm review theming, swatch-preset button
  states). Pastel accents (#efa2a4, #fad5d4, #b9d2ee, #e9dacd, #d5c0aa) and a warm off-white
  (#f8f3ef) appear in the palette and are interpreted here as soft nursery-toned surface and
  accent colors appropriate to a baby-apparel brand, though their exact UI usage is not
  confirmed in the supplied rules. #de3618/#bf2710 are treated as sale/error signal colors.
  Font-family values in the evidence are CSS custom-property labels ("Body", "Heading",
  "Medium", "Semibold") rather than resolved typeface names, so this spec treats the actual
  brand typeface as unverified and falls back to system sans-serif for rendering safety.
  The proposed system favors a soft, low-contrast neutral base with restrained pastel accents,
  compact swatch-driven product selection UI (sizes/colors), and a flat, low-radius geometry
  consistent with the observed --jdgm-border-radius: 0 token. Layout structure (grid-based
  body, header/footer regions) is inferred from generic Shopify theme conventions, not directly
  observed spacing values.

colors:
  primary: "#333333"
  ink: "#292929"
  canvas: "#ffffff"
  body: "#6a6a6a"
  muted: "#7a7a7a"
  hairline: "#dddddd"
  surface-soft: "#f8f3ef"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-pink: "#efa2a4"
  accent-pink-soft: "#fad5d4"
  accent-blue: "#b9d2ee"
  accent-tan: "#e9dacd"
  accent-tan-deep: "#d5c0aa"
  sale: "#de3618"
  sale-deep: "#bf2710"
  link: "#005bd3"
  border-light: "#e5e5e5"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "Heading, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Heading, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Heading, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Body, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.53, letterSpacing: "0px"}
  body-sm: {fontFamily: "Body, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "Body, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.35, letterSpacing: "0.02em"}
  button-md: {fontFamily: "Medium, sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.02em"}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderBottom: "1px solid {colors.border-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  size-swatch-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    selectedTextColor: "{colors.ink}"
    priceColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
**button-primary** renders as a solid dark neutral (#333333) call-to-action, matching the review-widget's write-review button color observed in the evidence; used for primary cart/checkout actions (proposed).

**button-secondary** is an outlined variant using the same ink tone on a white ground, for lower-emphasis actions like "View details" (proposed pairing, not directly observed).

**text-input** uses a light hairline border and body-gray text, suited to newsletter/email capture and account forms; focus state is not observed and would need verification.

**nav-bar** is inferred from the extensive mega-menu text content (New, Girls, Boys, Baby Essentials, Nursery, Collections) implying a multi-level dropdown header; visual chrome (height, shadow) is unobserved.

**product-card** applies the neutral body/muted price coloring seen in the swatch CSS (#6a6a6a title, #7a7a7a price) to a generic product tile, with a light border for separation on white canvas.

**hero** uses the warm off-white surface (#f8f3ef) as a soft, nursery-appropriate backdrop for a seasonal banner (e.g., Fall/Winter, Halloween shop), with display typography; actual hero markup was not present in evidence.

**footer** groups secondary navigation and legal/copyright text on a light gray surface (#f5f5f5), consistent with typical Shopify footer treatment; exact content blocks are inferred from site menu data, not footer-specific CSS.

**badge** repurposes the sale-red tone (#de3618) for promotional or "Sale" labeling, a reasonable inference given the presence of that hue alongside pastel product-adjacent colors.

**size-swatch-selector** is grounded directly in the supplied swatch-preset CSS: unselected options show #6a6a6a title text over white with a #7a7a7a price line; the selected state darkens the title to #292929 while the price stays #6a6a6a. This component is the most evidence-backed pattern in the document and should govern any size/color variant picker for baby apparel.

## Responsive Behavior
Recommended (not measured) breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | single-column nav collapses to hamburger/drawer (proposed) |
| tablet | 600–959px | 2-column product grid (proposed) |
| desktop | 960–1279px | mega-menu dropdowns, 3–4 column grid (proposed) |
| wide | 1280px+ | max-width container, 4+ column grid (proposed) |

Touch targets for swatches and nav items should be at minimum 44px; the mega-menu's deep category nesting (New/Girls/Boys/Halloween/Christmas etc.) suggests a collapsible accordion pattern on mobile, which is a proposed UX pattern, not an observed mobile layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, DOM structure, hover/focus states, or actual mobile breakpoints were observed. Font family values in the evidence ("Body", "Heading", "Medium", "Semibold") are CSS custom-property labels, not resolved typeface names — actual brand fonts, weights, and licensing are unverified, and generic sans-serif fallback is assumed. Pastel colors (#efa2a4, #b9d2ee, #e9dacd, etc.) appear in the palette but their specific UI role (accent chips, seasonal theming, size-color swatches) is inferred, not confirmed by selector context. Spacing and rounded-corner scales are proposed conventions, not measured from site CSS (only --jdgm-border-radius: 0 was directly observed). Interaction states beyond the swatch-selector (hover, focus, disabled) are partially evidenced for swatches only; all other component states are proposed placeholders pending live-site verification.
