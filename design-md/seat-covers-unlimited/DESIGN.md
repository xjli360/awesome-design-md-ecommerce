---
version: alpha
name: "Seat Covers Unlimited"
source_url: "https://seatcoversunlimited.com"
captured_at: "2026-09-29T03:59:02.970642+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Seat Covers Unlimited's storefront runs on a Shopify theme whose root
  variables define a restrained, high-contrast base: near-black
  (#121212) for foreground text, buttons and links, set against a pure
  white (#ffffff) canvas. This near-monochrome foundation is typical of
  a utilitarian, trust-driven auto-parts retailer where product photos
  and fit-by-vehicle tooling carry the visual weight rather than a
  colorful brand system. The wider observed palette contains several
  cool grays and blue-grays (#58606b, #7e858e, #99a1aa, #e6eaef,
  #f8fafc) that are inferred here as secondary text, muted copy and
  hairline/border tones, plus a cluster of darker slate tones
  (#20262c, #242833, #171d23) inferred as a dark footer or overlay
  surface. Several saturated colors in the evidence (#da323a, #ff0030,
  #08c67c, #0051b2) are inferred as sale-badge, alert and confirmation
  accents consistent with "Sale," "Top Seller" and stock-status labels
  seen in the page text; their exact component usage is not directly
  observable in the supplied CSS rules. Typography evidence lists
  Gobold alongside Inter, Open Sans and Roboto; Gobold is treated as
  the likely display/heading face (bold, condensed retail branding),
  while Inter is treated as the probable body face, both with
  sans-serif fallback. Arial/Verdana appear only inside a third-party
  jQuery UI stylesheet and are excluded from brand typography roles.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#58606b"
  muted: "#7e858e"
  hairline: "#e6eaef"
  surface-soft: "#f8fafc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#da323a"
  accent-strong: "#ff0030"
  accent-info: "#0051b2"
  accent-success: "#08c67c"
  dark-surface: "#20262c"
  overlay: "#00000080"
  border-strong: "#20262c"
typography:
  display-xl: {fontFamily: "Gobold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gobold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Gobold, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  vehicle-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** models the site's near-black CTA buttons (`--color-button: 18,18,18` / white text), used for "Add to Cart," "Check out," and vehicle-select actions; hover/active states are proposed and not directly observed.

**button-secondary** is an outline variant inferred for lower-priority actions ("Continue shopping," "View cart") using the same ink tone as a border on a white fill, mirroring the theme's `--color-secondary-button` pairing.

**text-input** represents search and form fields (country/region selector, contact form); border and radius are proposed defaults consistent with the theme's light, flat aesthetic, since no explicit input CSS was supplied.

**nav-bar** covers the persistent top navigation (Home, Products, About Us, FAQ, Contact Us) plus the utility row (phone number, country/currency, search, cart); a light hairline division from page content is proposed, not measured.

**product-card** represents catalog tiles such as the "Leatherette Custom Seat Covers" and "Neo-Sport" listings, pairing a white surface with a subtle border and compact price/sale typography; swatch and badge placement are proposed layout only.

**vehicle-selector** is a category-specific component modeling the Make/Model/Year fitment widget prominent in the page content; it uses a soft background to visually separate the fitment tool from surrounding product content, an inferred treatment.

**hero** models the top promotional band (e.g., "Fall Road Trip Sale") using a dark surface tone drawn from the observed slate colors, with large display type; exact hero background and imagery are not confirmed by the supplied CSS.

**footer** is inferred as a dark section (consistent with the dark palette cluster) containing social links (Facebook, Instagram, YouTube) and secondary navigation, using reduced-emphasis body type.

**badge** covers "Sale," "Top Seller," and "Water Resistant" labels seen in the product grid, using an accent red pulled from the observed palette; pill shape and exact color-to-label mapping are proposed.

**search** models the header search control; visually aligned with text-input but treated separately since it appears as a distinct icon-triggered affordance in the page content.

## Responsive Behavior
| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column product grid; vehicle selector collapses to stacked Make/Model/Year fields; nav collapses to a hamburger/menu icon. |
| Tablet | 600–959px | Two-column product grid; utility bar wraps; touch targets remain ≥44px. |
| Desktop | 960px+ | Multi-column product grid; full horizontal nav and utility bar as text-described in page content. |

All touch targets are recommended at a minimum 44×44px hit area, and the vehicle-selector dropdowns should collapse into an accordion or modal on narrow viewports. This table is a design recommendation only; no responsive CSS or breakpoints were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed layout, or JavaScript-driven interaction (e.g., cart drawer, vehicle-fitment filtering, slick carousel behavior) was observed. Several palette entries originate from a generic third-party jQuery UI "smoothness" theme file rather than confirmed brand-authored CSS, so their assignment to brand roles (sale/alert/success accents) is an inference, not a verified brand decision. The mapping of Gobold/Inter to display/body roles is inferred from the font list order and common theme conventions, not from explicit `font-family` declarations tied to those names in the supplied rules. Root body font-size (1.5rem) and its relationship to `--font-body-scale` could not be resolved to an exact pixel value, so all typographic sizes beyond what's explicitly shown are proposed defaults. Rounded and spacing scales are proposed conventions, not measured from the source. Font licensing/availability for Gobold was not verified and should be confirmed before implementation.
