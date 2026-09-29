---
version: alpha
name: "Canada Pooch"
source_url: "https://canadapooch.com"
captured_at: "2026-09-28T09:53:37.859386+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Canada Pooch presents a utilitarian, gear-forward retail aesthetic built around a
  cool blue accent against neutral grays and near-black text. The evidenced palette
  centers on a functional blue (#1990c6, darkening to #136f99 on hover) used for the
  Shopify accelerated-checkout button, paired with a broader blue family
  (#005c88, #0a5593, #032e51, #4d8cab) that likely supports secondary UI and links;
  this secondary-blue role is inferred, not directly observed on primary CTAs.
  Body and label copy consistently render in dark neutrals (#3d4246, #69727b,
  #231f20) against white and light-gray surfaces (#f4f4f4, #f8f8f8, #e6e6e6),
  consistent with a clean product-carousel and catalog layout. Headings are forced
  to "Maison Neue Bold" at font-weight 400 across all heading and title-class
  elements, while smaller UI text uses "Maison Neue Book"; Maison Neue Medium and
  Light are present in the font stack but their applied roles are inferred from
  naming convention rather than captured selectors. Small red tones (#b0060a,
  #dc3737, #8b0000) appear in the palette and are treated as inferred sale/badge
  accents given the brand's frequent "NEW!" and promotional messaging. Rounded
  pill shapes (border-radius 20px, 50%) recur in carousel navigation and swatch
  overlays, informing the proposed rounded scale.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#3d4246"
  muted: "#69727b"
  hairline: "#e6e6e6"
  surface-soft: "#f4f4f4"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-sale: "#b0060a"
  footer-deep: "#032e51"
typography:
  display-xl: {fontFamily: "Maison Neue Bold, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Maison Neue Bold, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Maison Neue Medium, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Maison Neue Book, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Maison Neue Book, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Maison Neue Book, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Maison Neue Medium, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.muted}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-deep}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    columnGap: "{spacing.lg}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** reflects the one concretely evidenced CTA in the source (the Shopify accelerated-checkout button), using the blue #1990c6 background with a #136f99 hover state and a default 0px radius; this is treated as the closest available ground truth for primary actions across the storefront.

**button-secondary** is proposed as an outlined counterpart using the same primary blue for border and text on a white field, intended for lower-emphasis actions like "Shop All" links; no outlined button was directly observed.

**text-input** is inferred from the presence of a site search field in navigation text; border, radius, and padding are proposed defaults using the observed hairline gray and near-black ink.

**nav-bar** represents the mega-menu structure implied by the categorized text (Gear, Apparel, PlayStack, Best Sellers); background and hairline are grounded in observed neutrals, but exact height, sticky behavior, and dropdown mechanics are not observed.

**product-card** is grounded directly in the `.ai-product-carousel` rules: a light-gray image well (#f4f4f4), a 16px medium-weight title in near-black, and a 14px price in #3d4246, matching the "Waterproof Sport Puffer," "Soho Sweater," etc. listings in the evidence.

**hero** is a proposed promotional banner pattern reflecting the "Gear Up For The Season" and marquee messaging (BOGO, free shipping, sign-up offer); background, spacing, and CTA placement are inferred, not measured.

**footer** uses the confirmed multi-column CSS variables (`--footer-nav-columns-*`) for a 2-column mobile / 3-column desktop link layout; the dark navy background (#032e51) is a proposed treatment drawn from the palette, not a confirmed footer color.

**badge** is proposed for "NEW!" and sale-flag labels seen throughout the catalog ("NEW! PlayStack," "NEW! Waterproof Slush Suit"), using one of the observed red tones as an inferred accent; no badge markup was directly captured.

**search** models the on-site search field referenced in the page text ("Search by product type, collection, name..."), styled with neutral border and muted placeholder text; exact field styling is unconfirmed.

**swatch-selector** is grounded in the `.ai-product-carousel__swatches` rule: a pill-shaped, semi-opaque white overlay (rounded.full, 8–12px padding) showing color options, directly relevant to this apparel brand's multi-color product listings (e.g., "+6 colors").

## Responsive Behavior

Proposed breakpoints (not measured from the live site):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | Footer nav collapses to `--footer-nav-columns-mobile: 2`; nav-bar likely becomes a hamburger/drawer pattern (not observed). |
| tablet | 640–1024px | Footer nav at `--footer-nav-columns-tablet: 3`; product-card grid likely 2–3 columns (proposed). |
| desktop | >1024px | Footer nav at `--footer-nav-columns-desktop: 3`; full mega-menu nav-bar assumed. |

Touch targets for button-primary and swatch-selector should maintain a minimum 44px hit area, consistent with the `.ai-product-carousel__nav` 44px button dimension observed in CSS. Mobile menu collapse behavior, drawer transitions, and swatch hover-to-tap conversion are recommendations only and were not observed in interaction traces.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, form validation) were observed beyond the two hover/loading rules present in the accelerated-checkout CSS. Semantic role assignment for the multi-blue palette (#005c88, #0a5593, #4d8cab, #032e51) is inferred from color proximity and typical footer/link usage, not confirmed by selector context. The footer background color, hero layout, badge markup, and text-input styling are proposed patterns, not measured site behavior. Font availability, weighting fidelity, and licensing for "Maison Neue" and "Trade Gothic" families were not verified; fallback to generic sans-serif is assumed per observed `!important` declarations. Mobile and tablet layouts, breakpoint pixel values, and touch interaction behavior are recommendations only.
