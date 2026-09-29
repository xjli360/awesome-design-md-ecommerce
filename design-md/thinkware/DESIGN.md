---
version: alpha
name: "Thinkware"
source_url: "https://thinkware.com"
captured_at: "2026-09-29T04:04:06.967249+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Thinkware's storefront CSS centers on a compact design-token system exposed via
  root custom properties: a white surface (#ffffff), near-black ink (#1a1c1c), a
  muted secondary text tone (#666666), and a saturated automotive red (#bc001f,
  with a brighter #eb0029 variant) used for calls-to-action, active nav states,
  and sale/featured badges. Supporting neutrals (#f6f6f6, #f9f9f9, #dddddd,
  #e6e8eb) structure cards, panels, and hairline dividers. A secondary heading
  color (#192b3e) appears only as a CSS-variable fallback and is treated here as
  an inferred "heading" role rather than a confirmed brand color. Inter is the
  confirmed body/UI typeface across nav, search, and product-mega-menu
  components; Montserrat, Open Sans, and Roboto are present in the evidence but
  read as third-party/plugin font-stacks (e.g. WooCommerce) rather than
  intentional brand typography, so they are excluded from the proposed scale.
  Radii lean toward soft rounding (4–10px) with a fully pill-shaped primary CTA
  (999px), reinforcing a technical, product-catalog-driven retail interface
  typical of a dash-cam specialist rather than a lifestyle brand.

colors:
  primary: "#bc001f"
  primary-bright: "#eb0029"
  ink: "#1a1c1c"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  heading: "#192b3e"
  border-soft: "#e6e8eb"
  accent-teal: "#448a85"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 16.8px, fontWeight: 700, lineHeight: 1.3, letterSpacing: -0.2px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 15.2px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 11.5px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.16px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: -0.16px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.primary}"
    activeBackground: "{colors.surface-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-soft}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.heading}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-panel:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  series-filter-nav:
    backgroundColor: "{colors.canvas}"
    activeBackground: "{colors.surface-soft}"
    activeBorderColor: "{colors.primary}"
    textColor: "{colors.heading}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** reflects the observed `.tw-products-mega-all-products` element: a gradient-capable, fully pill-shaped red CTA with white text, `999px` radius, and `48px` minimum height, used for primary shop/catalog actions.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Compare Dash Cams"), using the same hairline border tone seen on search inputs and cards, not directly observed as a distinct class.

**text-input** is grounded in `.tw-products-mega-search input`: white background, `1px` hairline border, `4px` radius, and a muted placeholder color, sized for a `36px` minimum height.

**nav-bar** generalizes `.tw-products-mega-category-link`: flex row with `8px` radius, bold `0.95rem` label, and an active state that switches text to primary red — category/series navigation pattern only, not a full top-nav observation.

**product-card** is proposed for the dense product-catalog grid implied by the page text (dozens of dash-cam models/bundles); it borrows the mega-menu's card-like `product-name` and `product-flag` styling as its closest observed analog.

**hero** is a proposed pattern for the homepage banner ("See Beyond the Darkness", "Shop Now") referenced in page text; no hero-specific CSS was supplied, so background/typography choices here are inferred from brand tone, not measured.

**footer** is proposed using the muted/surface-soft/hairline trio observed elsewhere in the token set; no footer-specific selectors were present in the evidence.

**badge** reflects `.tw-products-mega-product-flag` (pill, small bold caption, primary-red text) but substitutes an observed neutral background since the exact `#ffe7ed` tint fell outside the supplied palette.

**search-panel** and **series-filter-nav** are both grounded directly in supplied selectors (`tw-products-mega-search`, `tw-products-mega-series-nav .tw-products-mega-model-filter`), including the left-border active-state indicator switching to primary red.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column product grid; mega-menu collapses behind the observed "Open menu" toggle |
| Tablet | 641–1024px | 2-column product grid; search panel likely full-width overlay |
| Desktop | 1025–1400px | Matches observed `--tw-container:1400px`; multi-panel mega menu |
| Wide | >1400px | Container gutter (`--tw-container-gutter:2.5rem`) caps content width |

Touch targets should meet the observed `48px` minimum height used on the primary CTA and `36px` on inputs; anything smaller should be enlarged for mobile. Mobile menu collapse, hamburger interaction, and mega-menu panel behavior are **not observed** — this table is a recommendation derived from container/gutter variables, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered layout, computed styles, or interaction states were captured. The `heading` (#192b3e), `accent-teal` (#448a85), and several unused palette entries (e.g. #720eec, #958e09, #0073aa, #31856c) appear in the raw evidence without a clear semantic role and may belong to unrelated embedded widgets, charts, or third-party scripts rather than core brand usage — they are flagged, not asserted. Hero, footer, and product-card components are proposed patterns inferred from page text and general e-commerce structure, not confirmed selectors. Mobile navigation collapse, hover/focus states, and breakpoint values are proposed, not measured. Inter is confirmed as the primary UI font family in supplied CSS, but exact weight availability, self-hosting, and licensing were not verified from this evidence.
