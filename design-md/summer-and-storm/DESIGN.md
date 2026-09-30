---
version: alpha
name: "Summer and Storm"
source_url: "https://summerandstorm.com"
captured_at: "2026-09-29T04:12:42.541081+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Summer and Storm presents as a minimal, editorial baby/kids/womenswear brand, and the
  observed CSS supports a restrained, near-monochrome system. Body copy and headings both
  render in HelveticaNowText with a serif fallback, giving a clean sans-serif voice with a
  quiet backup. The dominant ink tone is a soft near-black (#232222) rather than true black,
  paired with a pure white canvas (#ffffff) and true black (#000000) reserved for active/
  pressed button states. Grays (#f6f6f6, #eeeeee, #e5e5e5, #a4a4a4, #bbbbbb, #888888) form a
  tonal scale used inferentially here for surfaces, hairlines, and muted text, since the
  source CSS does not label these roles explicitly. Primary buttons use the near-black ink
  as background with white text; a secondary gray button variant is also observed. No accent
  brand color is confirmed from component CSS — occasional saturated hues in the palette
  (e.g. #cb4242, #514bb9, #56ad6a) appear to be swatch/variant chips rather than UI theme
  colors, so they are treated as inferred product-swatch accents, not brand accents. Layout
  proposals (spacing, radius scale, card and hero patterns) are original interpretations
  fitted to the evidence, not measured observations, and are flagged accordingly throughout.

colors:
  primary: "#232222"
  ink: "#232222"
  canvas: "#ffffff"
  body: "#232222"
  muted: "#888888"
  hairline: "#e5e5e5"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  active: "#000000"
  disabled-bg: "#f6f6f6"
  disabled-text: "#b6b6b6"
  secondary-bg: "#bbbbbb"
  secondary-hover: "#a2a2a2"
  secondary-active: "#888888"
  hover-tint: "#a4a4a4"
  swatch-red: "#cb4242"
  swatch-indigo: "#514bb9"
  swatch-green: "#56ad6a"
  warm-canvas: "#faf7f5"
typography:
  display-xl: {fontFamily: "HelveticaNowText, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "HelveticaNowText, serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0px}
  title-md: {fontFamily: "HelveticaNowText, serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "HelveticaNowText, serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "HelveticaNowText, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "HelveticaNowText, serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "HelveticaNowText, serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.307, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xl}"
    states: "hover:#090909 (observed); active/focus:#000000 (observed); disabled:#f6f6f6 bg / #b6b6b6 text (observed)"
  button-secondary:
    backgroundColor: "{colors.secondary-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
    states: "hover:{colors.secondary-hover} (observed); active/focus:{colors.secondary-active} (observed)"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    note: "proposed; no dedicated input CSS observed"
  nav-bar:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    hoverColor: "{colors.hover-tint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    note: "home-template nav renders white text over hero per .template-index .nav__link rule; standard-page nav color not observed"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    imageAspect: "proposed 4:5 portrait"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    sizeChipRounded: "{rounded.xs}"
    note: "size badges (2-3y, 3-4y, etc.) and 'Add to Bag' action inferred from page text; visual card structure proposed"
  hero:
    backgroundColor: "{colors.warm-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    note: "hero copy color inferred white from .template-index nav_link rule implying dark/photo background; warm-canvas is a proposed placeholder, not confirmed as hero bg"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    note: "footer contains About, Stockists, Customer care, Instagram, Subscribe per page text; layout proposed"
  badge:
    backgroundColor: "{colors.disabled-bg}"
    textColor: "{colors.disabled-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    note: "modeled on observed disabled-button token pair; used here for NEW/SALE tags, proposed"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    note: "no search-specific CSS observed; styled consistent with text-input"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    note: "category-appropriate component for kidswear size runs (2-3y through 10-11y) seen in page text; interaction states proposed"

## Components

**button-primary** reflects directly observed `.btn` CSS: near-black background, white text, no radius, uppercase-weight bold label, with confirmed hover (#090909) and active/focus (#000000) states, plus a confirmed disabled state (light gray bg, mid-gray text).

**button-secondary** mirrors the observed `.btn--secondary` rule set (#bbb background, darker grays on hover/active), used here for lower-emphasis actions like "Continue shopping."

**text-input** is a proposed pattern; no input-specific selectors were supplied, so styling is inferred from the general canvas/hairline/body tokens to stay consistent with the button system.

**nav-bar** is partly observed: on the homepage template, nav links and account/cart icons render white with a light-gray hover (#a4a4a4), implying a transparent nav over a hero image or dark band. Behavior on interior pages is not confirmed and is labeled proposed.

**product-card** is inferred from repeated page-text patterns (product name, size run, price, "Add to Bag") typical of the kids-clothing category; no card CSS was supplied, so visual structure (borders, spacing, image ratio) is proposed.

**hero** is a proposed full-bleed section using the section-scale spacing token; only the white nav-text clue supports a dark/photographic hero, so background color is placeholder, not confirmed.

**footer** groups the observed navigation-adjacent text (About, Stockists, Customer care, Instagram, Subscribe) into a conventional footer layout; color roles are inferred from the neutral gray scale.

**size-selector** is a category-specific proposed component for age-based sizing (2-3y–10-11y) referenced throughout the page text, styled to match the button system's selected/unselected states.

## Responsive Behavior
Recommended (not measured) breakpoints:
| Breakpoint | Width | Layout |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, drawer cart (`.drawer__close` observed) |
| Tablet | 600–1024px | 2-column product grid, condensed nav |
| Desktop | >1024px | 3–4 column product grid, full horizontal nav |

Touch targets should be ≥44px, matching the observed `.mobile-menu_bottom .checkout-btn button` height of 43px. Nav collapses to a drawer/mobile menu pattern, consistent with observed `.drawer__close` and `.mobile-menu_bottom` selectors. This table is a design recommendation only; no live responsive behavior was inspected.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and page-text extraction only; no rendered layout, real breakpoints, or interaction states (focus rings, transitions, animations) were observed beyond the explicit hover/active/disabled rules listed. Many color-role assignments (canvas vs. surface-soft vs. hairline) are inferred from a flat gray palette without confirmed usage context. Typography sizes beyond the base 13px body rule are proposed, not measured. The custom font "HelveticaNowText" availability, licensing, and fallback behavior were not verified — only its declared use with a `serif` fallback is confirmed. Saturated palette colors (red, indigo, green) are assumed to be product-swatch variants rather than theme accents, but this mapping is inferential. Mobile menu, search, and product-card structures are proposed patterns fitted to category convention, not extracted from supplied component CSS.
