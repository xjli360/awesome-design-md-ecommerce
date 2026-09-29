---
version: alpha
name: "Hori USA"
source_url: "https://stores.horiusa.com/"
captured_at: "2026-09-29T04:22:19.697061+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from the BigCommerce Stencil theme powering
  stores.horiusa.com, the official Hori USA controller storefront. The
  observed CSS shows a neutral, utilitarian palette: white (#ffffff) page
  background, dark-gray body copy (#333333) and heading color (#444444,
  mapped here to a slightly darker #222222 ink for hierarchy), with
  #757575 used for secondary text and pagination. A blue primary action
  color (#0067b3) drives the `.button--primary` component, swapping to a
  red (#ec193a) on hover/active — both are treated here as brand accent
  colors for a gaming-hardware retailer, though their emotional intent
  (calm blue commerce vs. energetic red emphasis) is inferred rather than
  documented. Panel and pagination surfaces use light grays (#e5e5e5,
  #cccccc, #fafafa) for cards, hairlines, and soft backgrounds. Typography
  is set in Lato with Arial/Helvetica/sans-serif fallback, weight 400
  throughout headings and body, with a small 0.25px letter-spacing on
  headings — no bold weight or display font was observed, so heavier
  weights below are proposed extrapolations for hierarchy, not confirmed
  CSS. Rounded corners on buttons (4px) and border radii are directly
  observed; larger radii are proposed for card/badge components by
  extension.

colors:
  primary: "#0067b3"
  accent: "#ec193a"
  ink: "#222222"
  body: "#333333"
  muted: "#757575"
  hairline: "#cccccc"
  surface-soft: "#e5e5e5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  border: "#999999"
  success: "#008a06"
  warning: "#f1a500"
typography:
  display-xl: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.25px}
  display-md: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.25px}
  title-md: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  body-sm: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: normal}
  button-md: {fontFamily: "Lato, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: normal, letterSpacing: normal}
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
    hoverBackgroundColor: "{colors.accent}"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  platform-tabs:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** reflects the directly observed `.button--primary` rule: blue (#0067b3) fill, white text, 4px radius, hover state swapping to red (#ec193a). This is the most reliably grounded component in this document.

**button-secondary** is a proposed outline treatment inferred from the base `.button` rule's transparent background and #ccc border; the original CSS pairs this with white text, which suggests it targets dark surfaces (e.g. hero banners) rather than the light-canvas usage assumed here — flagged as inferred repurposing.

**text-input** is proposed by convention; no explicit input CSS was supplied. Border and text colors borrow from the observed `.form-body` border (#999999) and body copy color for plausibility.

**nav-bar** models the top-level Controllers / Arcade Sticks / Accessories / Apparel navigation implied by page text. Colors and hairline are inferred from the light-canvas, gray-hairline pattern seen elsewhere in the theme; no nav-specific selector was in evidence.

**platform-tabs** is a category-appropriate component for a controller retailer, representing the Nintendo / PlayStation / Xbox / PC groupings mentioned in the page text. Active-state color reuses the primary blue; this pattern is proposed, not measured.

**product-card** is proposed using the light card/gray-surface convention (#fafafa, #cccccc hairline) seen in panel and pagination styling, extended to a plausible product-grid tile with title, price, and caption typography roles.

**hero** is proposed for the homepage carousel implied by "Previous / Next / 1 2 3 4 5" pagination text; dark background and large display type are stylistic assumptions since no hero-specific CSS was supplied.

**footer** draws its gray background (#e5e5e5) and muted text color (#757575) from the `.panel-header` and `.card-figcaption-body .card-text` rules respectively, applied to the observed footer content (Company, Quick Links, Contact, Newsletter).

**badge** and **search-bar** are proposed utility components — badge for sale/new-product flagging using the accent red, search-bar styled consistently with the proposed text-input to match the site's "SEARCH" header link.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| Mobile | up to 550px | Single-column stacking, nav collapses to menu icon, touch targets ≥44px |
| Small tablet | 551–800px | Two-column product grid, condensed nav |
| Tablet | 801–1260px | Three-column product grid, full horizontal nav |
| Desktop | 1261–1680px | Four-column product grid, full hero width |
| Wide | 1681px+ | Max-width content container, generous side margins |

These breakpoint ranges are extrapolated from CSS media-query boundaries present in the supplied evidence file names, but the actual responsive layout, stacking order, and collapse behavior were not observed and are recommendations only. Interactive touch-target sizing (44px minimum) is a general accessibility recommendation, not a measured site value.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS and text extraction only; no rendered page, DOM interaction, or JavaScript-driven state (menus, carts, carousels, search overlays) was observed. Hover, focus, active, and disabled states beyond the `.button` and `.button--primary` rules are proposed by extension, not confirmed. Several role assignments (ink vs. body, surface-soft vs. surface-card) are inferred groupings of a flat gray-scale palette rather than named theme tokens. Font sizes for all typography tokens except the base 16px `.button`/body values are proposed for hierarchy and not present in the supplied CSS. Mobile and tablet layouts, breakpoint-specific component behavior, and grid column counts are recommendations, not measured. Availability, licensing, and hosting of the Lato font family were not verified beyond its declaration in the theme's font stack; system fallbacks (Arial, Helvetica, sans-serif) are assumed to render if Lato is unavailable.
