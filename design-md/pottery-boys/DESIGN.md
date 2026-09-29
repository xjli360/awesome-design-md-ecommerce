---
version: alpha
name: "Pottery Boys"
source_url: "https://potteryboys.com"
captured_at: "2026-09-29T04:29:03.714716+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pottery Boys Clay Studios presents a handmade-goods storefront built on a
  standard e-commerce template (editmysite/Weebly-family CSS), so most visual
  structure is inferred rather than directly observed. The supplied palette is
  dominated by neutral grays (#ffffff, #f4f4f4, #dddddd, #333333, #2a2a2a) with
  a warm clay-brown link color (#8d5024) and a muted gold hover state
  (#dab844) — both plausibly intentional nods to the studio's earthen,
  porcelain-and-glaze subject matter, though this brand intent is inferred,
  not confirmed. Observed type stacks include "Lora" on headline/paragraph
  header elements and "Lato" on product titles and #wsite-content headings,
  with letter-spacing:1px applied to Lato usage. Proxima Nova appears in the
  raw font list (as ProximaNova-Semibold) and is treated here as the probable
  interaction/button typeface used by the underlying template framework.
  The interpretation pairs Lora for expressive display moments (evoking the
  handcrafted, artisanal tone of the "About the Artists" copy) with Lato for
  functional UI text — product names, navigation, labels — matching the
  observed selector split. Surfaces stay light and neutral to let photography
  of glazed ceramics carry visual weight; the brown/gold pair is reserved for
  links, price emphasis, and primary actions.

colors:
  primary: "#8d5024"
  ink: "#2a2a2a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-gold: "#dab844"
  border-strong: "#cccccc"
  text-faint: "#999999"
  price-ink: "#000000"
typography:
  display-xl: {fontFamily: "Lora, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lora, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Lato, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 1px}
  body-md: {fontFamily: "Lato, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Proxima Nova, Lato, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-strong}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.price-ink}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.base}"
  glaze-swatch:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"

## Components
**button-primary** carries the clay-brown link color forward into a solid call-to-action fill, intended for "Shop Now" and checkout actions; hover/focus states are proposed, not observed. **button-secondary** is an outlined, low-emphasis variant for filters or secondary navigation actions, using the same brown text on a light card surface. **text-input** models search and email-signup fields (the footer's "Help us keep you informed" form) with a plain hairline border and generous padding for touch usability. **nav-bar** reflects the observed top-level structure (Home, Pottery Store, About, Art Fairs, Video, Blog) rendered in the Lato/letter-spacing title style seen on product headings. **product-card** groups thumbnail, title, and price for catalog items (Ornaments, Vases, Bottles, Jars, Mugs, Bowls, Plates), with price styled bold and black per the observed `.product-long-price` rule. **hero** proposes a full-width introductory band using the soft gray surface and Lora display type to introduce the "Handmade Pottery by Glenn Woods and Keith Herbrand" narrative. **footer** consolidates contact info, email signup, and secondary links, matching the observed dark-gray (#2a2a2a) footer text color. **badge** is a small pill for tags like "New" or "One-of-a-Kind," using the gold hover-accent color for differentiation. **search** proposes a rounded search field consistent with the site's "Search by typing & pressing enter" prompt. **glaze-swatch** is a category-specific component for presenting the two glaze families (Matte Crystalline, Gloss Crystalline) as small labeled cards, supporting the site's educational content about glaze types.

## Responsive Behavior
Recommended breakpoints (proposed, not measured): mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. Below tablet, the nav-bar should collapse into a hamburger/menu toggle and product-card grids should reduce from multi-column to single or two-column layout. All interactive targets (button-primary, button-secondary, search, nav links) should maintain a minimum 44×44px touch area on mobile. This section is a design recommendation only; no actual responsive/mobile behavior was observed from static CSS extraction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven behavior were observed. Color-to-role mapping (e.g., treating #8d5024 as "primary" and #dab844 as "accent-gold") is inferred from link/hover selectors and may not reflect actual brand intent. Typography sizes, weights, and letter-spacing values beyond the explicitly observed 1px/0px letter-spacing rules are proposed defaults, not measured. Font availability, licensing, and exact weight files for Lora, Lato, and Proxima Nova were not verified. Breakpoints, touch-target sizing, and mobile collapse behavior are proposed conventions, not observed site behavior. Component states (hover, focus, disabled, active) are proposed and unobserved.
