---
version: alpha
name: "Spector"
source_url: "https://www.spectorbass.com"
captured_at: "2026-09-28T05:07:29.835701+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Spector Bass's storefront runs on a Shopify base with a lean, high-contrast
  palette: near-black ink (#211f1f) on white canvas (#ffffff), a warm brass
  accent (#bf9c5c) used as the primary button/interactive color, and a
  utilitarian blue (#1990c6, hover #136f99) reserved for Shopify's accelerated
  checkout button. Supporting neutrals (#f3f3f3, #efefef, #dedede, #d1d5d7,
  #666666) suggest a restrained grayscale system for cards, dividers, and
  secondary text, though their exact UI roles are inferred rather than
  directly observed in layout. Typography is set entirely in Figtree with a
  sans-serif fallback; both body and heading styles share a consistent
  positive letter-spacing (~0.06rem, scaled for headings), giving the brand a
  slightly technical, engineered feel appropriate to a 45-year-old instrument
  maker.
  This interpretation treats the brass tone as the brand's signature accent
  against an otherwise monochrome, editorial-leaning UI, with the blue
  checkout color isolated to transactional elements rather than promoted as a
  brand color. Component patterns below (cards, hero, spec table) are proposed
  conventions consistent with the evidence, not verified live captures.

colors:
  primary: "#bf9c5c"
  ink: "#211f1f"
  canvas: "#ffffff"
  body: "#211f1f"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#fefefe"
  on-primary: "#211f1f"
  accent: "#1990c6"
  accent-hover: "#136f99"
  dark: "#121212"
  border-strong: "#2a2f31"
  neutral-border: "#d1d5d7"
typography:
  display-xl: {fontFamily: "Figtree, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Figtree, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: "0.03rem"}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.04rem"}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04rem"}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: "0.06rem"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
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
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.border-strong}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.neutral-border}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** uses the observed brass button color (`--color-button: 191,156,92`) with dark text, matching Spector's CTA affordances (Add to Cart, Shop Now). Hover state (proposed) would darken slightly, consistent with the general `.button:hover` rule shifting toward black/white seen elsewhere in the CSS.

**button-secondary** is a white-fill, ink-bordered variant, mirroring the `--color-secondary-button` and `--color-secondary-button-text` tokens defined at root, used for lower-emphasis actions like "Continue Shopping."

**text-input** follows the light hairline-bordered convention typical of Shopify Dawn-family themes; exact border and radius values were not directly observed and are proposed defaults.

**nav-bar** is inferred from the presence of a persistent header with cart, search, account, and country/currency selector text in the page excerpt; no direct nav CSS was supplied, so background and spacing are proposed.

**product-card** draws on `.product-card-wrapper .card` custom-property scaffolding (border radius, shadow, image padding all theme-variable driven), which confirms a card system exists but not its resolved values; padding and colors here are proposed within the observed neutral palette.

**hero** is a proposed full-bleed banner pattern using the darkest observed neutral (#121212) as background, appropriate for showcasing bass photography; this is not confirmed from the evidence, which only shows a slideshow section selector.

**footer** uses ink-on-canvas inverted (or vice versa) coloring consistent with the brand's grayscale system; structure (multi-column links, legal text) is proposed and not verified from supplied CSS.

**badge** is a small pill component for tags like "Custom Shop" or "Signature," styled from the observed `--color-badge-*` tokens (background white, border/foreground ink).

**search** and **spec-table** are proposed, category-appropriate components: search reflects the site's visible search affordance, and spec-table addresses the instrument domain (scale length, neck construction, pickups) using the muted surface and hairline/border neutrals from the palette, though no literal spec-table markup was present in evidence.

## Responsive Behavior
This is a recommendation, not measured site behavior (no breakpoints were present in supplied CSS).

| Breakpoint | Width       | Layout guidance (proposed)                  |
|------------|-------------|----------------------------------------------|
| xs         | <480px      | Single-column, stacked nav, full-width cards |
| sm         | 480–767px   | Single-column, larger touch targets          |
| md         | 768–1023px  | 2-column product grid, condensed nav         |
| lg         | 1024–1439px | 3–4 column product grid, full nav bar        |
| xl         | ≥1440px     | Max-width container, 4+ column grid          |

Touch targets should be at least 44px in height (matching the accelerated-checkout button's clamp(25px, 44px, 55px) pattern observed in CSS). Navigation should collapse to a hamburger/menu pattern below `md`; the currency/country selector (confirmed extensive in page text) should collapse into a dropdown on narrow viewports.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, interaction states, or mobile behavior were observed. Root font-size (rem basis) was not confirmed, so absolute pixel sizes in typography are proposed estimates layered onto the observed relative units (rem, letter-spacing). Several color-role assignments (surface-soft, surface-card, neutral-border, dark) are inferred from generic-sounding hex values without confirmed selector usage tying them to specific UI elements. Button, card, and container border-radius values reference CSS custom properties (`--buttons-radius-outset`, `--product-card-corner-radius`) whose resolved pixel values were not supplied, so rounded-token assignments in components are proposed defaults. Figtree's licensing/self-hosting status was not verified. No hover, focus, active, or error states were directly observed beyond the single `.button:hover` and payment-button hover rules; all other states are proposed and labeled as such.
