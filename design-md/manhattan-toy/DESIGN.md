---
version: alpha
name: "Manhattan Toy"
source_url: "https://manhattantoy.com"
captured_at: "2026-09-28T04:23:40.848132+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The evidence shows a warm, muted neutral palette (--color-foreground: 93 88 81 → #5d5851) set against a white background (--color-background: 255 255 255), with a secondary warm charcoal (#3e3b36) appearing in the raw color list. Grays (#999999, #dedede, #e5e5e5, #333333) recur in utility UI—SKU labels, slider controls (.flickity-button background #ffffffbf, text #333)—suggesting a restrained, text-forward system rather than a saturated brand palette. A single soft blue (#a0d9e4) appears among the extracted colors and is treated here as an inferred accent for badges or highlights, since no CSS rule ties it to a specific role. The many additional bright hues (payment-network reds, blues, greens) are third-party checkout icons, not brand colors, and are excluded from the design system. Typography uses Nunito for body/UI text (confirmed via font-family evidence) with system monospace stacks reserved for code-like or tabular fragments (inferred, not confirmed in visible copy). Heading sizes are driven by CSS custom properties (--text-h1..h6, --title-lg/xl) built on a spacing-unit scale; exact pixel values are not resolvable from static extraction, so all typographic sizes below are proposed approximations consistent with the ratios implied by the --sp-* tokens. The overall interpretation favors a soft, editorial, baby-goods aesthetic: warm neutrals, generous whitespace, and minimal chroma reserved for small functional accents.

colors:
  primary: "#5d5851"
  ink: "#3e3b36"
  canvas: "#ffffff"
  body: "#5d5851"
  muted: "#999999"
  hairline: "#dedede"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#a0d9e4"
  overlay-light: "#ffffffbf"
  text-secondary: "#333333"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Nunito, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Nunito, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Nunito, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Consolas, Menlo, Monaco, \"Liberation Mono\", \"Courier New\", ui-monospace, monospace", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
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
    textColor: "{colors.primary}"
    height: "{spacing.xxl}"
    padding: "0 {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    skuTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkTypography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
  age-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
    typography: "{typography.body-sm}"

## Components
**button-primary** uses the observed muted-brown foreground (#5d5851) as its fill with white text, matching the body text color used site-wide as `--color-foreground`; hover/pressed states are proposed, not observed. **button-secondary** is an outlined variant using the hairline gray border, intended for lower-emphasis actions like "Add to Wishlist"; its states are proposed. **text-input** follows the same hairline border and canvas background pattern seen in the slider/lightbox controls, extrapolated to form fields since no explicit input CSS was captured. **nav-bar** is inferred from the `#shopify-section...header` block's white background and foreground color variables, sized against the `--topbar-height` custom property (sp-12/sp-14); exact height in px is not confirmed. **product-card** reuses the SKU styling directly observed (`.product__sku { color:#999; font-size:.9em }`) for its caption row, with card chrome (border, radius, padding) proposed to match toy-catalog conventions. **hero** is a proposed full-width banner pattern using the soft gray surface tone and largest display type scale (`--title-xl`/`--text-h1` tokens), since no hero-specific selector was present in the evidence. **footer** inverts to the darker ink tone (#3e3b36) for contrast, a common pattern though not directly confirmed by footer-specific CSS. **badge** applies the single light-blue accent color (#a0d9e4) as a pill for tags such as "New" or age ranges; this color's role is inferred, not confirmed. **search** and **age-filter-chip** are proposed baby-toy-category-appropriate components (age/stage filtering is common in this vertical) styled consistent with the pill/rounded-full patterns seen in `.pswp__button` (rounded-full, translucent background) from the lightbox module.

## Responsive Behavior
Recommended, not measured, breakpoints:
| Breakpoint | Width | Notes |
|---|---|---|
| sm | ≤480px | Single-column product grid, nav collapses to hamburger menu |
| md | 481–768px | 2-column product grid, condensed nav |
| lg | 769–1024px | 3-column grid, full nav visible |
| xl | ≥1025px | Page container capped via `--page-container` (min of viewport and max(--page-width,1280px)) |

Touch targets should be at least 44×44px for primary buttons and nav icons. Navigation is expected to collapse into a drawer/menu below `md`; this behavior is proposed based on common Shopify theme conventions and is not directly observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/color/font extraction only; no rendered page, interaction states (hover/focus/active), or mobile layouts were observed. Semantic role assignments (e.g., treating #5d5851 as "primary" and #3e3b36 as "ink") are inferred from variable naming (`--color-foreground`) and frequency, not confirmed brand documentation. Numeric type scale values (font sizes for display/title/body tokens) are proposed approximations of the `--text-h*`/`--title-*` custom-property scale, since the underlying `--sp-*` unit values were not resolvable from the supplied evidence. The single accent blue (#a0d9e4) and its use as a "badge" color is speculative — no selector ties it to a UI role. Nunito's licensing/self-hosting status and any additional weights are not verified beyond its appearance in the font-family list. Bright multi-hue colors (payment network icons: Visa, Mastercard, PayPal-adjacent brands) were deliberately excluded from the design system as third-party assets, not site branding.
