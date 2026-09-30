---
version: alpha
name: "Kavee"
source_url: "https://kavee.com"
captured_at: "2026-09-28T04:19:21.527068+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kavee's evidence points to a warm, editorial palette built around a deep
  forest green (#1a4b3d) used as the sticky header and primary action color,
  paired with an off-white, paper-like canvas (#f8f5eb) rather than pure
  white. Near-black text (#232323/#262626) carries body copy, while a soft
  yellow (#fee452) and a clay red (#d12913) appear positioned for badges,
  sale flags, and promotional accents. A cluster of muted pastels
  (#acd3ec, #b59887, #e3a6a6, #ffc074, #8a9d7b, #76938b) is inferred to
  represent product/fabric color swatches for cage covers and accessories,
  consistent with a pet-habitat retailer. Typography combines Instrument
  Serif for display headlines with Manrope for body and UI text, following
  the site's own --text-h0…h6 scale and line-height custom properties.
  Payment-network colors (PayPal blue, Mastercard red/orange, Apple Pay
  black) are excluded from the brand palette as they are third-party icon
  colors, not brand marks. This interpretation proposes a soft-card,
  generous-whitespace layout with a sticky green header, rounded product
  cards on a paper-toned canvas, and pastel swatch chips for configurable
  habitat products — all component shapes, sizes, and states below are
  proposed unless explicitly cited from the supplied CSS.

colors:
  primary: "#1a4b3d"
  ink: "#232323"
  canvas: "#f8f5eb"
  body: "#262626"
  muted: "#737373"
  hairline: "#dedede"
  surface-soft: "#f3f2ed"
  surface-card: "#ffffff"
  on-primary: "#fffffe"
  accent-yellow: "#fee452"
  accent-red: "#d12913"
  accent-sage: "#8a9d7b"
  accent-teal: "#76938b"
  swatch-blue: "#acd3ec"
  swatch-tan: "#b59887"
  swatch-pink: "#e3a6a6"
  swatch-orange: "#ffc074"
  overlay-scrim: "#00000066"
typography:
  display-xl: {fontFamily: "Instrument Serif, serif", fontSize: 120px, fontWeight: 400, lineHeight: 1, letterSpacing: -1px}
  display-md: {fontFamily: "Instrument Serif, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.167, letterSpacing: 0px}
  title-md: {fontFamily: "Manrope, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.333, letterSpacing: 0px}
  body-md: {fontFamily: "Manrope, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Manrope, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Manrope, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Manrope, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    position: "sticky"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.canvas}"
    overlay: "{colors.overlay-scrim}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  swatch-selector:
    backgroundColor: "{colors.surface-card}"
    optionShape: "circle"
    optionColors: ["{colors.swatch-blue}", "{colors.swatch-tan}", "{colors.swatch-pink}", "{colors.swatch-orange}", "{colors.accent-sage}"]
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** renders the forest-green header background color as a solid fill with off-white text, intended for primary calls to action like "Add to Cart" or "Shop Now"; hover state (proposed) reduces opacity per the site's `--button-background-opacity: 0.85` custom property. **button-secondary** is an outlined variant using the same green for border and label on a transparent field, for lower-emphasis actions. **text-input** uses a white card surface with a light hairline border, proposed for search fields and account/checkout forms; focus-ring styling is not observed. **nav-bar** reflects the sticky header evidence (`position: sticky; top: 0`) with the dark green background and off-white logo/nav text, sized around the observed 75–90px logo box across breakpoints. **product-card** is a white rounded panel for guinea-pig cage and accessory listings, pairing a serif-adjacent or Manrope title with body-weight pricing; proposed hover/lift state not observed. **hero** proposes a full-bleed banner on the warm canvas tone with a large serif display headline (Instrument Serif) sized near the site's `--text-h0` token, optionally with a dark scrim overlay for text legibility over imagery. **footer** repeats the primary green with off-white text for navigation links and trust badges. **badge** and **badge-sale** are compact pill/rect labels — yellow for general highlights (e.g., "New," "Bestseller") and red for discount/sale flags, both inferred from palette proximity to promotional UI patterns. **search** proposes a pill-shaped, soft-surface input for the site search bar. **swatch-selector** is a category-specific proposed component: a row of pastel circular swatches (blue, tan, pink, orange, sage) representing configurable cage cover/fabric colors, common to habitat/accessory product pages, with the selected state ringed in the primary green.

## Responsive Behavior
This is a recommended structure, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column stacks, nav collapses to a menu icon, header padding uses the smaller `--spacing-3`-scale value observed at narrow widths |
| Tablet | 640–1024px | 2-column product grids (matches observed `--product-list-items-per-row: 2` and carousel item widths of ~36–74vw) |
| Desktop | 1024–1440px | 3-column product grids (`--product-list-items-per-row: 3`), larger header logo (~90px, per observed rule) |
| Wide | >1440px | Max-width container with increased section spacing per the larger `--section-outer-spacing-block` steps observed in `:root` |

Touch targets for buttons and nav items should be at least 44px tall (proposed). Mobile navigation is assumed to collapse into a slide-out or dropdown menu; no such interaction was observed in the supplied static CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, color extraction, and font-family declarations only — no rendered page, computed layout, or JavaScript-driven interaction was observed. Semantic role assignments (e.g., which grays are "muted" vs "hairline," which pastels map to product swatches) are inferred from typical e-commerce/pet-retail patterns and color proximity, not confirmed from markup. Numeric type sizes below `h6` (body, caption, button) and all spacing/rounded scale values are proposed conventions, not sourced from the site's actual `--spacing-N` or radius tokens, whose pixel values were not present in the supplied evidence. Hover, focus, active, and error states are proposed and unverified. Mobile menu behavior, carousel interaction, and swatch-selector functionality were not observed. Font availability and licensing for "Instrument Serif" and "Manrope" (e.g., self-hosted vs. Google Fonts, weight range) were not verified; system/monospace fallbacks in the supplied list (Arial, Calibri, Consolas, Helvetica, Menlo, Monaco, etc.) appear to be default OS/browser fallback stacks rather than intentional brand typefaces.
