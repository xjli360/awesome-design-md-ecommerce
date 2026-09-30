---
version: alpha
name: "Bushwacker"
source_url: "https://bushwacker.com"
captured_at: "2026-09-28T10:18:47.587708+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bushwacker is presented through RealTruck's shared commerce platform, so the
  observed tokens describe a functional, parts-catalog aesthetic rather than a
  bespoke Bushwacker identity. The palette centers on a near-black header
  (#1e1e1e) with a saturated golden-yellow accent (#ffc600) used for cart and
  action icons, paired with a cooler action/link blue (#057dbc) and a
  restrained neutral scale (#333333, #767676, #d5d5d5, #f3f3f3, #fafafa) for
  body copy and surfaces. Status colors (danger #e50000, success #15884f,
  warning #fa6400, info-dark #23889b) appear as CSS custom properties intended
  for pricing, alerts, and form validation. Typography relies on two generic,
  platform-scoped families, "PlatformFont" and "PlatformBrandFont"; no
  proprietary Bushwacker typeface was observed, so both are mapped to
  sans-serif fallbacks. Font sizes follow a defined scale from 12px to 96px.
  The interpretation below infers a dark-header, high-contrast-CTA pattern
  typical of RealTruck-family storefronts, with light neutral cards for
  product listings. Component states, spacing rhythm, and responsive
  collapse points are proposed conventions for an automotive-accessory
  catalog, not measurements taken from a rendered page.

colors:
  primary: "#ffc600"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#d5d5d5"
  surface-soft: "#f3f3f3"
  surface-card: "#fafafa"
  on-primary: "#1e1e1e"
  action: "#057dbc"
  action-dark: "#23889b"
  danger: "#e50000"
  success: "#15884f"
  warning: "#fa6400"
  surface-tint-blue: "#ecf6fd"
  surface-tint-gold: "#fff8de"
  gray-dark: "#6c6c6c"
typography:
  display-xl: {fontFamily: "'PlatformBrandFont', sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'PlatformBrandFont', sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'PlatformFont', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'PlatformFont', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focusRing: "{colors.action}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.danger}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.action}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-tint-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.gray-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    ctaBackground: "{colors.action}"
    ctaTextColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components
**button-primary** uses the observed golden accent (#ffc600) as a high-visibility call-to-action fill, with dark ink text for contrast since no explicit on-primary color was supplied; this pairing is inferred from typical yellow-on-dark accessibility needs. **button-secondary** is a proposed outline style using the canvas background and hairline border for lower-emphasis actions like "View Details." **text-input** and **search** share a light bordered treatment appropriate to catalog filtering and site search, with the action-blue reserved for a proposed focus ring — no focus state was directly observed. **nav-bar** reflects the dark header/link-bar pattern seen in the CSS (`--colorBlack`, `--colorWhite` background/text), with the primary yellow reserved for cart and item icons as in the supplied rules. **product-card** is a proposed pattern for the large catalog (fender flares, bumpers, etc.), using the sale-price danger color rule that was explicitly present in the CSS (`.or-product-listing-sale-price`). **hero** infers a dark, full-width banner consistent with the header treatment, intended for category or model-fitment promotion. **footer** mirrors the dark header styling and reuses the action-blue for links, plus a proposed subscribe button drawing on the CSS-referenced (but unresolved) secondary color slot. **badge** is a proposed small tag component (e.g., "New," "Free Shipping") using the warm tint background found in the palette. **fitment-selector** is a category-specific proposed component for year/make/model truck selection, a standard pattern for exterior-accessory retailers, styled with the light surface and action-blue CTA.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| sm | 0–639px | Single-column nav collapses to hamburger; product grid 1 col |
| md | 640–1023px | Product grid 2 col; fitment-selector stacks fields vertically |
| lg | 1024–1279px | Product grid 3 col; full nav bar visible |
| xl | 1280px+ | Product grid 4 col; max content width per `--container-7xl` (80rem) token observed |

Touch targets should be a minimum 44px height for buttons and nav items on sm/md. Mobile header is expected to collapse category mega-menu into an accordion or drawer, consistent with the `.or-mobile-header` selector observed in CSS, though its expanded/collapsed visual behavior was not captured.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and a page-text excerpt, not a rendered or interactively tested page. The exact roles of several custom properties (e.g., `--colorSecondary`, `--colorDangerDark`, `--colorInfoLight`) were referenced but not fully resolved in the supplied evidence, so mappings for footer CTA and badge tint are inferred best-guesses. No component states (hover, focus, active, disabled, error) were observed; all are proposed. Mobile menu behavior, breakpoint pixel values, and grid column counts are proposed conventions, not measured. "PlatformFont" and "PlatformBrandFont" are platform-level (RealTruck) font tokens of unknown license/availability and unverified actual typeface; generic sans-serif fallback is assumed. Spacing scale and rounded-corner values are proposed defaults, not extracted from layout measurements. Because Bushwacker's storefront is served through RealTruck's shared platform, brand-specific visual distinction beyond the yellow accent could not be confirmed from the supplied evidence.
