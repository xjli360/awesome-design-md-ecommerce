---
version: alpha
name: "Romina Furniture"
source_url: "https://rominafurniture.com"
captured_at: "2026-09-29T03:53:18.396904+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Romina Furniture's public site presents an heirloom-nursery-furniture brand: solid hardwood cribs and dressers made in Europe, positioned around safety certifications (Greenguard Gold, CPSC) and long-term durability. The captured palette is dominated by near-black and warm neutral text tones (#1a1a1a, #222222, #3a3a3a) against white and off-white surfaces (#ffffff, #f7f7f7, #eef1ee, #f4f7f5), which this spec treats as ink, body, canvas, and soft/card surface roles. A deep forest green family (#285649, #234b40, #104a3b, #2b7c66) recurs across the token set, including alpha-blended variants, and is interpreted here as the primary brand accent — fitting the brand's organic, Greenguard-certified positioning — though its literal on-page usage (buttons vs. text vs. background) is not confirmed by static extraction. A muted red (#d02e2e) and a blue (#2693cf) are reserved for alert/sale and link states respectively, both inferred. Typography is drawn from the observed font stack: Poppins for display/heading weight and Archivo for running text, both present in the site's font-family declarations; Avenir Next and Helvetica Neue are treated as system fallbacks. Heading sizes (72/60/48px) and a fluid `--font-*` scale are taken directly from `:root` custom properties; all other sizes are proposed extrapolations for a coherent scale.

colors:
  primary: "#285649"
  primary-deep: "#104a3b"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#747474"
  hairline: "#e5e5e5"
  surface-soft: "#f7f7f7"
  surface-card: "#eef1ee"
  surface-card-alt: "#f4f7f5"
  on-primary: "#ffffff"
  accent-alert: "#d02e2e"
  accent-success: "#56ad6a"
  link: "#2693cf"
  control-dark: "#262626"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 72px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -1.44px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 60px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -1.2px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.9px}
  body-md: {fontFamily: "Archivo, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Archivo, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Archivo, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Archivo, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "{colors.hairline}"
    height: "proposed 72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.control-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    borderTop: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  finish-swatch-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    swatchSize: "proposed 32px"
    labelTypography: "{typography.caption}"

## Components
**button-primary** is proposed as the brand's core call-to-action (Add to Cart, checkout), using the deep green primary token against white text, matching the dark-button pattern seen in the site's `.oke-button` review-widget styling (`background-color:#262626`), here reinterpreted with the brand green for storefront consistency; the review widget's own dark neutral button is preserved separately as `control-dark`.

**button-secondary** covers lower-emphasis actions (Find a Store, View Collection) with a white fill and hairline border, keeping text in ink for legibility; hover/active states are not observed and are proposed as a background shift to `surface-soft`.

**text-input** models search and account-form fields with a light hairline border and minimal radius, consistent with the site's restrained, utilitarian control styling seen in the reviews widget's shared border tokens.

**nav-bar** represents the persistent header with logo, mega-menu categories (Cribs, Dressers, Collections) and cart — CSS confirms a `--LOGO-WIDTH: 200px` and a transparent/backdrop header state on load, but full collapse and scroll-behavior are not measured.

**product-card** is proposed for PLP/collection grids showing crib and dresser SKUs with finish-option indicators, using the soft green-tinted card surface (`#eef1ee`) to differentiate from the plain white canvas.

**hero** reflects the homepage's large certification-led messaging ("100% Real Wood," "Safe & Sound") using the largest display type on a deep primary-green field; actual hero background color is not directly observed and is treated as a brand-consistent inference.

**footer** groups support/utility links (Assembly Manuals, Warranty, Order Status) on a dark neutral field, proposed to match the reviews-widget dark button color for tonal consistency, though the live footer background was not directly captured.

**badge** is proposed for trust markers such as "Greenguard Gold" or "In Stock," using the success green already present in the palette; pill shape and placement are inferred conventions for this product category.

**finish-swatch-selector** is a category-specific component: cribs and dressers offer 10–13 wood-finish options per the product copy, so a circular swatch picker with a primary-colored active ring is proposed to represent this configurator pattern; exact swatch rendering was not observed in static CSS.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior — the evidence shows three separate `:root` font-scale blocks (implying at least three width tiers) but no explicit media-query widths.

| Tier | Width | Notes |
|---|---|---|
| Mobile | < 480px | Single-column, stacked nav, swatches wrap 5/row |
| Tablet | 480–1024px | 2-column product grid, condensed nav |
| Desktop | > 1024px | Container capped at observed `1200px`, full mega-menu |

Touch targets should be a minimum of 44×44px for swatches and nav items; the header mega-menu is expected to collapse into an accordion/drawer pattern on mobile, based on the "Expand menu / Hide menu" text pairs seen in the page copy, though the interaction mechanics themselves were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions were observed. Semantic color-role assignments (primary, accent, link, alert) are inferred from token frequency and naming context, not confirmed usage on live elements. Font sizes for body-md, body-sm, caption, and button-md are proposed approximations built from the `--font-*` scale variables rather than directly bound declarations. Letter-spacing values for display tokens are computed conversions from `em` to `px` and are approximate. Mobile menu behavior, cart-drawer interaction, finish-swatch UI, and carousel (Flickity) behavior are referenced in the markup/CSS but not visually verified. Availability and licensing of Poppins and Archivo for production use were not verified from this evidence.
