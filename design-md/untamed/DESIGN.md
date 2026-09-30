---
version: alpha
name: "Untamed"
source_url: "https://untamedcatfood.com"
captured_at: "2026-09-28T09:16:30.758451+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Untamed's evidence shows a cream-and-forest-green brand core (#fcf5e3, #2e4740) paired with a
  playful, high-saturation accent set (#91dae0, #fdafcd, #c292ff, #ffab8c, #e56b5a, #5bcf98, #c772d6,
  #f19b9e) — consistent with a menu that spans many wet-food formats (Gravy, Jelly, Pâté, Broth) and
  protein variants needing visual differentiation. Header CSS confirms two typefaces: "Quincy CF" for
  headings (font-heading-family) and "Poppins" for body/UI text (font-body-family), plus a third,
  non-typographic "swiper-icons" font used only for carousel controls. The only precisely observed
  component is the header's pill button (btn__rounded): 100px radius, 2px solid #2e4740 border, #91dae0
  fill, hover to #59bac2, Poppins 16px/20px/500. A second observed button pattern is Shopify's
  accelerated-checkout button, filled #1990c6 with #136f99 hover and a variable (default 0px) radius.
  All other roles — canvas, ink, muted text, hairlines, card surfaces, and the mapping of accent hues to
  specific categories or flavor badges — are inferred from the palette and general e-commerce/DTC
  conventions, not from measured layout. No live rendering, spacing rhythm, or responsive behavior was
  observed; sizes beyond the two confirmed rules are proposed.

colors:
  primary: "#2e4740"
  ink: "#060807"
  canvas: "#fcf5e3"
  body: "#2e4740"
  muted: "#c0c6bf"
  hairline: "#dedede"
  surface-soft: "#e6e2d1"
  surface-card: "#ffffff"
  on-primary: "#fcf5e3"
  accent-sky: "#91dae0"
  accent-sky-hover: "#59bac2"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  accent-pink: "#fdafcd"
  accent-purple: "#c292ff"
  accent-magenta: "#c772d6"
  accent-peach: "#ffab8c"
  accent-red: "#e56b5a"
  accent-salmon: "#f19b9e"
  accent-mint: "#5bcf98"
  accent-teal-deep: "#10707b"
  green-deep-2: "#234b38"
  green-deep-3: "#0f2922"
typography:
  display-xl: {fontFamily: "'Quincy CF', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Quincy CF', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Quincy CF', serif", fontSize: 24px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
  body-md: {fontFamily: "'Poppins', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Poppins', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 20px, letterSpacing: 0.02em}
  caption: {fontFamily: "'Poppins', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "'Poppins', sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 20px, letterSpacing: 0px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    hoverBackgroundColor: "{colors.accent-sky-hover}"
  button-checkout:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"
    hoverBackgroundColor: "{colors.accent-blue-hover}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaVariant: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  trial-box-card:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-peach}"
    priceTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.green-deep-3}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.green-deep-3}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** — A solid, dark-green pill CTA proposed for primary conversion actions ("Try for £7 today"). Not directly observed in the supplied CSS; the fill (#2e4740) and cream text (#fcf5e3) are inferred from the brand's dominant ink/canvas pairing to contrast with the observed lighter secondary button.

**button-secondary** — Directly grounded in `header .btn__rounded`: 100px radius, 2px solid #2e4740 border, #91dae0 fill, Poppins 16px/20px/500, hover state to #59bac2. This is the only button with a fully observed rest+hover pair and is treated as the canonical secondary/header action style.

**button-checkout** — Based on Shopify's accelerated-checkout CSS (`shopify-payment-button__button--unbranded`): #1990c6 fill, #136f99 hover, white text, default square corners (radius token defaults to 0). Reserved for wallet/express-checkout contexts, distinct from the brand's own pill buttons.

**text-input** — No form-field CSS was supplied; styling (white surface, 1px hairline border, small radius) is a proposed convention consistent with the cream/white surface pairing observed elsewhere.

**nav-bar** — Header link typography (14px/20px, 0.02em tracking, Poppins) and black/cream color utilities are observed; overall bar layout, sticky behavior, and spacing are inferred.

**hero** — Cream background and display heading in Quincy CF are inferred from font-family variables and the copy-heavy landing hero; exact hero sizing, imagery treatment, and layout are not observed.

**product-card** — Proposed pattern for the "Mightiest Meals" grid (Gravy, Jelly, Pâté, Broth; multiple protein SKUs). White surface with hairline border and title in Quincy CF is inferred to give the flavor grid visual structure; no card CSS was supplied.

**trial-box-card** — Category-appropriate component for the "£7 Trial Box" offer, using a soft cream surface (#e6e2d1) and a peach accent (#ffab8c) pulled from the observed accent set; pricing display size is proposed.

**badge** — Proposed chip for claims like "B-Corp certified," "Human-grade," "No grains, no greens," using the mint accent (#5bcf98) against a deep-green text for legibility; not present in supplied CSS.

**footer** — Inferred dark-green (#0f2922) footer against cream text, following the brand's ink/canvas inversion pattern seen nowhere explicitly in footer selectors but consistent with the dark-green swatches in the palette.

## Responsive Behavior
Proposed breakpoints (not measured):
| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacks; nav collapses to a menu icon (proposed) |
| tablet | 600–959px | Two-column product/trial-box grids (proposed) |
| desktop | 960–1279px | Full nav visible; multi-column flavor grid (proposed) |
| wide | 1280px+ | Max-width content container, generous section spacing |

Touch targets should be ≥44px, matching the Shopify accelerated-checkout button's `--shopify-accelerated-checkout-button-block-size` default of 44px (observed variable). Header pill buttons (btn__rounded) already meet this via 12px vertical padding plus line-height. All collapse/stacking behavior and actual breakpoint values are recommendations, not observed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction only; no rendered layout, real breakpoints, or interaction states (hover/focus/active) beyond the two explicitly declared hover rules were observed.
- Role assignment for many palette colors (accent-pink, accent-purple, accent-magenta, accent-salmon, teal-deep, etc.) is inferred from general category/flavor-tagging conventions, not confirmed usage.
- `ink` vs `body` vs `muted` distinctions are inferred; only `--color-black (#060807)` and `--primary-white (#FCF5E3)` were explicitly named as CSS variables.
- Typography scale beyond `title-md` (24px/1, Quincy CF) and `button-md`/`body-sm` (Poppins 16px/20px/500 and 14px/20px/0.02em) is proposed, not measured.
- Border-radius values beyond the observed 100px (header pill) and 0px (checkout button default) are proposed conventions.
- Mobile navigation, collapse behavior, and card/grid responsive rules were not present in the supplied CSS and are marked proposed.
- Custom font availability, licensing, and self-hosting/CDN delivery of "Quincy CF" were not verified; fallback to generic serif is assumed for safety.
