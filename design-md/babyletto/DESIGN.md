---
version: alpha
name: "Babyletto"
source_url: "https://babyletto.com"
captured_at: "2026-09-28T04:22:55.739142+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Babyletto's storefront pairs a warm, papery canvas (#FBF9F7 / #F9F4EE) with a
  terracotta-brown accent (#853A2D, deepening to #81321C on some button text)
  and near-black ink (#000 body text, #1A172C as a darker "color-dark" token).
  This reads as an earthy, nursery-appropriate palette rather than a clinical
  e-commerce scheme — warm neutrals dominate, with brown/gold (#E5B878) used
  sparingly for outlined buttons and small accents. Typography is anchored by
  GT Walsheim, a geometric sans used site-wide at a small 14px base size with
  a 500-weight header; Baskerville (serif) and a script family, "Nothing You
  Could Do," are present in the font stack and are interpreted here as
  inferred decorative/display pairings for hero or note-style copy — their
  actual usage and licensing are not verified from static CSS alone.
  Radius language leans toward soft, pill-shaped buttons (200px observed on
  the newsletter CTA), contrasted with at least one squared-corner button
  variant, suggesting a design system that mixes rounded-friendly and
  structural corners intentionally. Grays (#B7B7B7, #666666, #999999) supply
  hairlines and muted text. Roles below are semantic inferences built on
  directly observed hex values and CSS custom properties.

colors:
  primary: "#853A2D"
  ink: "#1A172C"
  canvas: "#FBF9F7"
  body: "#000000"
  muted: "#666666"
  hairline: "#B7B7B7"
  surface-soft: "#F9F4EE"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  accent-gold: "#E5B878"
  terracotta-deep: "#81321C"
  cream: "#F2E8DF"
  success: "#157347"
  danger: "#B42318"
  dark-navy: "#131121"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "GT Walsheim, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: normal}
  body-md: {fontFamily: "GT Walsheim, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  body-sm: {fontFamily: "GT Walsheim, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: normal}
  caption: {fontFamily: "GT Walsheim, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "GT Walsheim, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: normal}
  script-accent: {fontFamily: "Nothing You Could Do, cursive", fontSize: 24px, fontWeight: 400, lineHeight: 1.3, letterSpacing: normal}
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
    padding: "{spacing.sm} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.terracotta-deep}"
    borderColor: "{colors.accent-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.terracotta-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    size: "{spacing.xl}"
    rounded: "{rounded.full}"
    backgroundColor: "{colors.surface-card}"

## Components

**button-primary** is the pill-shaped CTA style directly observed on the newsletter signup (200px radius, `#853A2D` fill, `#FBF9F7`/white text). It is proposed as the default action button across the storefront (add-to-cart, subscribe, checkout).

**button-secondary** mirrors the observed `.button-square-corner` pattern: white/cream fill, terracotta text (`#81321C`), and a gold hairline border (`#E5B878`). Original CSS squares only the bottom-right corner; here it is generalized to a uniform small radius as a proposed simplification.

**text-input** is not directly observed but is inferred from the neutral hairline (`#B7B7B7`) and card-white background used elsewhere, giving a soft, low-contrast form field consistent with the brand's warm minimalism. Focus/error states are proposed, not verified.

**nav-bar** uses the observed `--header-background-color` (`#F9F4EE`) and the documented header heights (50px mobile / 115px desktop) and 500-weight label type. Sticky behavior and scroll transitions are not observed.

**product-card** reflects the observed `.card-product` title styling (GT Walsheim, 14px) and black body text on a white card. Image treatment, hover zoom, and quick-add interactions are proposed, not confirmed from static CSS.

**hero** is inferred as a full-width, canvas-toned section using the site's warm off-white background, since no hero-specific selector was supplied. Headline typography borrows the serif stack present in the font list as a plausible display treatment.

**footer** proposes a darker, ink-navy close to the page (`#131121`) for contrast, a common e-commerce pattern; this specific footer background was not present in the supplied evidence and is clearly speculative.

**badge** (e.g., "New," "Bestseller," or sale tags) reuses the gold/terracotta pairing already present in the button system, keeping new UI in-palette rather than introducing unobserved colors.

**search** is styled as a soft, low-emphasis input consistent with the header's cream background, using the same hairline and radius conventions as text-input.

**finish-swatch** is a category-appropriate addition for nursery furniture: circular selectors for wood finish or color options, bordered in hairline gray by default and in the primary terracotta when selected — a common pattern for furniture PDPs, proposed rather than observed.

## Responsive Behavior

| Breakpoint | Width | Notes |
|---|---|---|
| sm | ≤480px | Single-column, stacked nav, collapsed search |
| md | 481–767px | Two-column product grids |
| lg (observed) | 768–1024px | `--screen-break: 1024px` marks primary layout shift |
| xl | ≥1025px | Desktop header height 115px (observed); full multi-column grids |

Touch targets should be at least 44px in height, exceeding the observed 24px `--icon-size`, which likely needs padding to meet accessibility guidance. Mobile navigation is assumed to collapse into a hamburger/drawer pattern given the `--hambourger-icon-size` and `--drawer-menu-icon-size` custom properties, though the actual open/close behavior was not observed. This table is a recommendation for implementation, not a measurement of Babyletto's live responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, selector fragments, and a color/font inventory only — no rendered layout, computed styles, or DOM screenshots were available. Semantic color roles (e.g., mapping `#1A172C` to "ink," `#131121` to a proposed footer background) are inferred and may not match the site's actual token naming or usage. Rounded and spacing scales follow common conventions and are only partially anchored to evidence (the 200px pill radius and small button paddings are observed; the rest of the scale is proposed). Hover, focus, active, and error states were not present in the supplied CSS and are marked proposed throughout. Mobile menu behavior, product-card interactions, and hero content were not observed and are structurally inferred from generic e-commerce patterns. Font availability and licensing for GT Walsheim, Columbia Sans, Futura, Baskerville, and "Nothing You Could Do" have not been verified; generic fallbacks are included per family but actual embedding/licensing status is unknown.
