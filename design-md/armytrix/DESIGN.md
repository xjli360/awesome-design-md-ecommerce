---
version: alpha
name: "Armytrix"
source_url: "https://armytrix.com"
captured_at: "2026-09-28T10:18:33.986230+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in the ARMYTRIX Bootstrap-derived stylesheet, which exposes a
  neutral, utilitarian base (white canvas, black ink, a run of mid-to-light grays for chrome and
  hairlines) accented by one clearly branded color: the teal-green `#11b79c` used on `.btn-default`.
  That teal is treated here as the primary action color, since it is the only hex tied to an actual
  interactive component in the evidence. A warm orange (`#ff7105`) present in the palette is proposed
  as a secondary/high-energy accent for "Weaponize" style calls to action, matching the site's
  aggressive, performance-tuning tone; this mapping is inferred, not confirmed by a selector. Grays
  (`#f5f5f5`, `#eeeeee`, `#dddddd`, `#999999`, `#333333`) supply soft surfaces, card backgrounds,
  hairlines, muted text, and body copy, mirroring standard Bootstrap table/alert states seen in the CSS.
  Typography draws on the observed custom family names (Roboto weights, RobotoCondensed-Regular,
  Open Sans, Helvetica Neue) rather than any invented font, pairing a condensed bold display face for
  aggressive headlines with a plain sans body for legibility across specs and product copy.

colors:
  primary: "#11b79c"
  accent: "#ff7105"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#dddddd"
  hairline-strong: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  surface-dark: "#222222"
  on-primary: "#ffffff"
  danger: "#a94442"
  danger-bg: "#f2dede"
  success: "#3c763d"
  success-bg: "#dff0d8"
  info: "#31708f"
  info-bg: "#d9edf7"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
typography:
  display-xl: {fontFamily: "RobotoCondensed-Regular, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "RobotoCondensed-Regular, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto-Bold, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "RobotoCondensed-Regular, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    labelTypography: "{typography.caption}"
    controlTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the one brand-confirmed action color, teal `#11b79c`, matching `.btn-default` in the source CSS; intended for primary conversions such as "Weaponize Now" or "Add to Cart." States beyond the base fill (hover/active/disabled) are proposed, following the Bootstrap `.btn.disabled` opacity pattern observed in the CSS.

**button-secondary** is a low-emphasis outline button for filter/reset actions in the vehicle selector, using ink text on a hairline border; hover and focus treatments are proposed, not observed.

**button-accent** applies the inferred orange accent for high-intensity merchandising moments (collab drops, limited kits), separating them visually from standard commerce actions; this role assignment is a design proposal, not a captured usage.

**text-input** models a generic form field (e.g., contact, order-status lookup) using canvas background and hairline borders drawn from the neutral gray family present in the palette; focus-ring styling is not observed and is left undefined.

**nav-bar** represents the top-level navigation implied by the page text ("Dealer Login," "Check Cart," "Find a Dealer"), rendered on white with black text; sticky/scroll behavior is not verified from static CSS.

**product-card** supports the merchandise grid (tees, snapbacks, stickers) with a soft card surface and hairline edge; grid density and hover elevation are proposed conventions, not measured.

**fitment-selector** is a category-specific component modeling the "Select Brand / Model / Engine" vehicle picker central to an exhaust-systems storefront; it uses the surface-soft background to visually separate it as a utility panel distinct from marketing content.

**hero** reflects the campaign-style banners referenced in the text (Revuelto, LC500, GT3), assumed dark-surfaced with reversed type for contrast against product photography; exact hero background is not confirmed from CSS alone.

**footer** groups the extensive link list (Warranty, FAQs, Sponsorship, Collaborate) on a dark surface with muted gray text, consistent with the dark utility tones present in the palette.

**badge** proposes a rounded accent label for stock/status or "New" flags on product and news cards; no badge selector was present in the supplied CSS.

**search** models the "Check Order Status" lookup field referenced in the page text, styled as a compact bordered input consistent with the neutral input treatment used elsewhere.

## Responsive Behavior

Recommended breakpoints (proposed, not measured): `sm` 480px, `md` 768px, `lg` 1024px, `xl` 1280px. Below `md`, the nav-bar should collapse into a hamburger/off-canvas pattern and the fitment-selector's three dropdowns should stack vertically at full width. Touch targets for button-primary, button-accent, and fitment-selector controls should maintain a minimum 44px hit area. Product-card grids should reduce from multi-column to single or two-column layouts under `md`. This section is a recommendation only; no live responsive behavior was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and page-text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, loading, error) were observed. Color-to-role mapping beyond `.btn-default`'s teal is inferred from general palette presence, not confirmed component usage — notably the orange accent role is speculative. Font family names (Roboto weights, RobotoCondensed-Regular, gill-sans-mt-bold) are taken verbatim from the source but their `@font-face` sourcing, licensing, and actual on-page availability were not verified. All spacing and radius scale values follow a standard proposed system rather than measured site metrics. Mobile navigation collapse, carousel (slick) behavior, and cart/drawer interactions mentioned in the page text were not observed and are excluded from firm claims.
