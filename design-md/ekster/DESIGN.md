---
version: alpha
name: "Ekster"
source_url: "https://ekster.com"
captured_at: "2026-09-28T05:04:56.370566+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ekster's storefront evidence points to a high-contrast, monochrome-first
  system typical of premium EDC/travel-goods brands: black (#000000) and
  near-black (#1a1a1a, #252525) drive primary actions, navigation chrome,
  and review widgets (jdgm-primary-color), while white (#ffffff) and soft
  off-white greys (#f8f8f8, #eeeeee, #e7e7e7) form the canvas and card
  surfaces. Hairlines and dividers use light greys (#dddddd, #cccccc,
  #e7e7e7). A small set of saturated accents appears in isolated contexts:
  a deep red (#87040c) drives the ".highlighter" promo text (e.g. sale
  banners), brighter reds (#f61f1f, #df2630) and an amber-gold (#fbcd0a)
  likely flag sale pricing and "New Release" badges, and a forest green
  (#0f6722) is inferred for sustainability/B-Corp messaging given the
  page's "Certified B Corp / Recycled materials" copy. Button radii are
  inconsistent across the codebase (0px on native Shopify Wave tokens vs.
  12px on third-party bundle/loyalty widgets); this interpretation treats
  0px/small-radius as the native brand language and 12px as an
  app-widget exception, both are labeled inferred. Typography combines a
  grotesk workhorse (Nunito Sans) for UI and body copy with "Replica" as
  the likely display/headline face based on font-stack presence; sizes
  and weights beyond the single observed h1 rule (800 weight, 2.25em) are
  proposed, not measured.

colors:
  primary: "#000000"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#252525"
  muted: "#7b7b7b"
  hairline: "#dddddd"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-subtle: "#e7e7e7"
  accent-highlight: "#87040c"
  accent-sale: "#f61f1f"
  accent-gold: "#fbcd0a"
  accent-success: "#0f6722"
  accent-info: "#474be4"
typography:
  display-xl: {fontFamily: "Replica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Replica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-subtle}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"

## Components

**button-primary** models the black-fill/white-label pattern confirmed by the loyalty-widget rule (`background:#000;color:#fff;border-radius:12px`) and the Wave theme token `--wk-color-accent-1: 0,0,0`; used here for primary CTAs like "Shop Sale" and "Add to Cart," with a smaller radius applied for native theme consistency (proposed).

**button-secondary** is an inferred outline variant (black border, transparent fill) drawn from the observed `.rivo-aw-mini-modal__content button span:first-child` rule pairing `border:1px solid #000` with `color:#000` — a plausible secondary-action pattern (e.g., "View Details") though not confirmed on core product pages.

**text-input** uses the flat, square-cornered treatment implied by `--wk-input-border-radius: 0px` and hairline greys for borders; field states such as focus/error are proposed, not observed.

**nav-bar** reflects the white-canvas, black-text header implied by `:root` token usage across the theme, with the announcement bar height (`--announcement-height: 2rem`) and header offset (`--header-offset: 3rem`) confirming a two-tier header (promo strip + primary nav), though exact nav item styling is inferred.

**product-card** is inferred from catalog copy showing dense product grids (wallets, bundles, trackers) with price, color-variant, and badge overlays; card radius and padding follow the theme's conservative geometry rather than a directly observed card rule.

**hero** is proposed as a full-bleed dark section for campaign moments like "Early Holiday Sale" and the Steven Bartlett collaboration banner, using ink background and white type for contrast; no hero-specific CSS was supplied.

**footer** is inferred as a dark, high-contrast band consistent with the brand's black/white primary pairing; trust markers ("Free shipping," "Lifetime warranty," "Certified B Corp") likely live here based on page-text ordering.

**badge** covers the frequent "New Release," "Sale," and percentage-off labels seen throughout the excerpt; the sale-red (#f61f1f) is proposed as the badge fill given its presence in the broader palette, paired with a pill radius for scannability.

**search** is a proposed light-grey input treatment consistent with `surface-soft`/`hairline` tokens; no search-bar-specific selector was present in evidence.

**color-swatch-selector** is a category-specific component addressing Ekster's heavy use of leather/metal color variants (e.g., "Tan, Navy, Apple Skin, Black, Flare Red"); modeled as small circular swatches with an active-state ring in primary black, entirely proposed since no swatch CSS was captured.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width | Layout notes |
|---|---|---|
| Mobile | <640px | Single-column product grid, collapsed hamburger nav, sticky announcement bar |
| Tablet | 640–1024px | 2-column product grid, condensed header |
| Desktop | >1024px | 3–4 column grid, full mega-menu (Wallets/Travel/Accessories) |

Touch targets should target a minimum 44–45px height, consistent with the observed `--wk-button-min-height: 45px` / `min-height: 45px` widget rules. Mega-menu collapse into an accordion on mobile is a standard Shopify pattern assumption, not confirmed by supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered layout, hover/focus states, animation, or actual mobile breakpoints were observed. Font role assignments (Replica for display, Nunito Sans for body) are inferred from font-stack presence, not confirmed usage on specific elements — licensing/availability of "Replica" as a custom font is unverified. Color-to-role mapping (e.g., which red is "sale" vs. "highlight") is inferred from class-name hints and general palette frequency, not direct visual confirmation. Border-radius values are inconsistent across the source CSS (0px native theme vs. 12px third-party widgets); this spec's `rounded` scale is a proposed reconciliation. Spacing scale beyond `--header-offset` and `--announcement-height` is entirely proposed. No product imagery, iconography, or component screenshots were available for review.
