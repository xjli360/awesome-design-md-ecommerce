---
version: alpha
name: "Dragonfire Tools"
source_url: "https://www.dragonfiretools.com"
captured_at: "2026-09-28T04:05:27.216292+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dragonfire Tools sells premium garage workbenches, tool boxes, and wall
  cabinets through a Shopify storefront. The observed CSS shows a
  high-contrast industrial palette: near-black ink (#111111) and pure
  black/white extremes paired with a saturated red accent family
  (#ff3333, #ff4747, #ff1f1f) used on hero call-to-action buttons, plus a
  neutral gray secondary button (#4d4d4d, hover #717171). Numerous
  additional hex values in the evidence (#0071ce, #eb001b, #f79e1b,
  #ff5f00, #142fbd, #1532cb) belong to third-party payment-method icons
  (Visa, Mastercard, PayPal, Diners) and are excluded from the brand
  token set. Typography combines a condensed header face (Teko) with
  Oswald for headings (weight 500, +0.02em tracking) and a plain
  sans-serif/IBM Plex Sans stack for body and form text — a pairing
  consistent with a rugged, mechanical-shop identity.

  This specification interprets that evidence into a design system for a
  tool-storage retailer: bold condensed display type for hero banners,
  assertive red primary actions, and neutral gray/white surfaces that
  let product photography (steel cabinets, workbenches) read cleanly.
  Component states beyond documented hover rules (e.g., focus, disabled)
  and all spacing/radius scales are proposed, not measured.

colors:
  primary: "#ff3333"
  primary-hover: "#ff4747"
  secondary: "#4d4d4d"
  secondary-hover: "#717171"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#434343"
  muted: "#818181"
  hairline: "#dddddd"
  surface-soft: "#f3f3f3"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  border-dark: "#1c1c1c"
  alert: "#e10600"
  success: "#51a551"
  tint-red: "#fce2e2"
  overlay: "#0000004d"
typography:
  display-xl: {fontFamily: "Teko, sans-serif", fontSize: 56px, fontWeight: 500, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 38px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0.02em}
  title-md: {fontFamily: "Oswald, sans-serif", fontSize: 26px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.02em}
  body-md: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0}
  body-sm: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0}
  caption: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0}
  button-md: {fontFamily: "Oswald, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.02em}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.overlay}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.tint-red}"
    textColor: "{colors.alert}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-list:
    backgroundColor: "{colors.surface-card}"
    dividerColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the site's red call-to-action (observed hero button `background:#f33` with a `#FF4747` hover), sized for touch and desktop click targets. **button-secondary** reflects the documented gray variant (`#4d4d4d` base, `#717171` hover) used for lower-emphasis actions like "Learn More." **text-input** is a proposed pattern for search and checkout fields, using the light hairline border and dark ink text seen across the theme's neutral grays. **nav-bar** is inferred from the header's Teko font-family declaration and dark surface convention typical of industrial-tool retailers; exact height and sticky behavior are not confirmed. **product-card** proposes a white/near-white card (`#f6f6f6`) with Oswald title and plain body pricing, suited to displaying workbench and cabinet SKUs. **hero** interprets the banner wrapper evidence (`.ls-header-wrapper-title`, white text on dark background) into a full-bleed section with a large condensed headline. **footer** assumes a dark ink background with muted gray text, consistent with the site's black/white/gray dominant scheme; content structure is proposed. **badge** uses the soft red tint (`#fce2e2`) with alert-red text (`#e10600`) for callouts such as "Sale" or "Made in USA" labels — a proposed, unverified pattern. **spec-list** is a category-appropriate component for steel-gauge, drawer-count, or capacity specifications common to tool-storage product pages, styled with hairline dividers and caption-weight labels; this pairing is proposed, not observed in the supplied CSS.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not measured site behavior:

| Breakpoint | Width      | Notes                                  |
|-----------|------------|-----------------------------------------|
| mobile    | < 480px    | Single-column product grid, stacked nav |
| tablet    | 480–1024px | Two-column product grid                 |
| desktop   | > 1024px   | Multi-column grid, persistent nav bar   |

Touch targets should be at least 44×44px for buttons and form controls. Navigation is expected to collapse into a hamburger/drawer pattern below the tablet breakpoint; this has not been observed in the supplied evidence and should be verified against the live site before implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/HTML evidence and title metadata; no live rendering, DOM interaction, or visual screenshot was captured. Semantic role assignments (e.g., which red is "primary" vs. "alert," which gray is "body" vs. "muted") are inferred from selector context and may not match the brand's internal design intent. Font sizes for `display-xl` and component paddings/spacing scale are proposed conventions layered onto the smaller set of `--font-size-*` custom properties actually observed. Hover/active states are confirmed only for the two hero button variants documented in the evidence; focus, disabled, and error states are proposed. Mobile navigation, carousel/slideshow behavior, and checkout flow layout were not observed. Availability and licensing of Teko, Oswald, and IBM Plex Sans (likely served via Google Fonts or a Shopify font CDN) were not verified in this evidence set.
