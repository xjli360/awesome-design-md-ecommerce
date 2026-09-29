---
version: alpha
name: "Pakt"
source_url: "https://paktbags.com"
captured_at: "2026-09-29T04:05:13.516184+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pakt's evidence base shows a restrained black/white/gray system built around a single
  saturated accent, #ff5740, used on primary buttons and likely on sale/new badges. Ink
  is pure black (#000000) with a near-black variant (#111111) available for softer body
  copy; canvas is white with light-gray surfaces (#f5f5f5, #f8f8f8, #f7f6f4) used for
  product-image backgrounds and card fields per the observed .unicorn_product_image rule.
  A gray scale (#666666, #696969, #999999, #cccccc, #dddddd, #e1e1e1, #eeeeee) covers
  muted text, hairlines, disabled buttons, and compare-at pricing. Two outlier hues,
  #42c0ae (teal) and #e20dbb (magenta), appear in the raw palette without a confirmed
  role in the supplied rules; they are treated here as rare/tertiary accents, most
  plausibly sourced from a third-party review or promo widget rather than core brand
  usage — this mapping is inferred, not confirmed.
  Typography is anchored on Calibre-Regular/Calibre-Bold, a licensed sans-serif, with
  Helvetica Neue/Helvetica/Arial and system-ui/sans-serif as fallbacks. Heading scale
  values (48–90px display, 18–24px subheads) and button metrics (14px/11px, 1px
  letter-spacing) come directly from the supplied :root and .unicorn_button rules;
  body-copy sizing is proposed. Generous --container-gutter (40px) and
  --vertical-breather (64–90px) tokens imply a spacious, editorial travel-gear layout.

colors:
  primary: "#ff5740"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#111111"
  muted: "#696969"
  hairline: "#e1e1e1"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f6f4"
  on-primary: "#ffffff"
  text-secondary: "#666666"
  text-tertiary: "#999999"
  border-light: "#dddddd"
  disabled-bg: "#e1e1e1"
  disabled-text: "#6d6d6dff"
  accent-teal: "#42c0ae"
  accent-magenta: "#e20dbb"
typography:
  display-xl: {fontFamily: "'Calibre-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "64px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Calibre-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "38px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Calibre-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "24px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'Calibre-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Calibre-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Calibre-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "1px"}
  button-md: {fontFamily: "'Calibre-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1, letterSpacing: "1px"}
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
    padding: "{spacing.sm} {spacing.xl}"
    border: "2px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.xl}"
    border: "2px solid {colors.ink}"
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: "52px"
    padding: "{spacing.md} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    comparePriceColor: "{colors.muted}"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.text-tertiary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: "52px"
    padding: "{spacing.md} {spacing.base}"
  capacity-toggle:
    backgroundColor: "{colors.canvas}"
    selectedBackgroundColor: "{colors.ink}"
    textColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** carries the observed #ff5740 fill with white text, 2px matching border, and 0px radius, taken directly from `.unicorn_button_primary`; hover state reuses the same colors per the supplied rule, so no color shift is observed on hover.

**button-secondary** mirrors `.unicorn_button_secondary`: white background with black border/text, inverting to solid black on hover. This is an observed CSS pattern, not a live-interaction confirmation.

**text-input** is proposed for search, newsletter, and account forms, using the observed `--form-input-field-height: 52px` token and an inferred hairline border, since no explicit input-border color was supplied.

**nav-bar** is a proposed structural pattern (logo, primary links, cart) based on standard Shopify-style header conventions implied by the "Skip to content" and cart-drawer text in the evidence; exact layout, sticky behavior, and breakpoints are not observed.

**product-card** reflects the `.unicorn_product_image` (#f5f5f5 background, 0px radius, square aspect via padding-bottom 100%) and `.unicorn_product_price` / `_price_compare` rules, giving bold black current price and struck-through #696969 compare price — directly observed styling for PLP/collection grids.

**hero** is a proposed large-format banner using the display-xl scale (derived from the largest observed `--heading-large-font-size: 64px/90px` values) paired with a primary CTA button, consistent with the "Professional-Grade Travel Gear" hero copy in the evidence.

**footer** is proposed, using muted gray text and a hairline top border to house the newsletter, country selector, and policy links referenced in the page-text excerpt (Help Center, Returns, Jobs, etc.).

**badge** covers "NEW" and "40% off" labels seen in the navigation/collection copy; the primary-orange fill is inferred from the single strong accent color in the palette, since no dedicated badge CSS was supplied.

**search** is proposed for the "View all results" search overlay implied in the evidence, styled with the same 52px input height token and a light surface background for visual separation from the white canvas.

**capacity-toggle** is a category-specific proposed component for the recurring "35L / 45L" and liter-variant selectors seen across Pakt One, Cero, and Stash product listings — styled as a pill toggle with an inverted selected state; no selector CSS was supplied, so this pattern is inferred from typical travel-gear PDP conventions.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior, informed only by the presence of three tiered `:root` blocks in the evidence (implying at least a mobile/tablet/desktop split with escalating `--vertical-breather` and heading sizes):

| Breakpoint | Width | Container gutter | Heading-large |
|---|---|---|---|
| Mobile | <768px | 20px (proposed) | 52px |
| Tablet | 768–1199px | 40px (observed) | 64px |
| Desktop | ≥1200px | 40px (observed) | 90px |

Touch targets should be at least 44px (aligning with the observed `--button-small-height: 44px`); primary buttons meet this via the observed `--button-height: 52px`. Navigation should collapse to a hamburger/drawer pattern below 768px (proposed, not observed); product grids should reduce from a multi-column desktop layout to 2-column mobile (proposed).

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Semantic color roles (body, hairline, surface-card, badge, capacity-toggle background) are inferred from likely usage patterns, not confirmed selectors. The teal (#42c0ae) and magenta (#e20dbb) colors appear in the raw palette but have no confirmed selector role and may belong to third-party widgets (e.g., review stars) rather than core brand UI. Body-copy font size (16px) and most spacing/rounded values are proposed defaults, not measured. Hover/focus/active states beyond the two documented button rules are not observed. Mobile navigation, search overlay, and product-page gallery/interaction behavior were not observed. Calibre is a licensed commercial typeface; its availability, license terms, and exact weight files for production use are not verified here.
