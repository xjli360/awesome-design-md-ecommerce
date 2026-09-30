---
version: alpha
name: "JHS Pedals"
source_url: "https://www.jhspedals.info"
captured_at: "2026-09-28T09:33:05.111640+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  JHS Pedals presents a functional, product-forward storefront for a Kansas
  City guitar-effects manufacturer, built on a Shopify theme with CSS custom
  properties for color and spacing rather than fixed literal values. The
  observed palette is dominated by neutrals — near-black text (#000000,
  #3a3a3a), white and off-white surfaces (#ffffff, #f7f7f7, #fbfbfb), and
  cool grays for borders and secondary text (#d7d9dc, #737b83, #b3b3b3) —
  consistent with a catalog-heavy site where hundreds of individual pedal
  photos supply the color energy. A small set of saturated accent hexes
  (#ea005c magenta, #b74737 rust, #0066cc blue) appear in the palette without
  a clear declared role in the supplied CSS; they are mapped here, as
  inferred, to primary action, alert/sold-out badging, and link states
  respectively, since no rule explicitly ties a hex to a button or link
  selector. Typography draws from the supplied family list — Figtree,
  Avenir/Avenir Next, and Helvetica Neue/Arial fallbacks — with Avenir Next
  proposed for display weight and Figtree for body/UI text, both unverified
  as licensed webfonts. Spacing and radius scales are proposed conventions
  layered onto the theme's own responsive custom-property steps for gutter,
  outer margin, and vertical rhythm.

colors:
  primary: "#ea005c"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#737b83"
  hairline: "#d7d9dc"
  surface-soft: "#f7f7f7"
  surface-card: "#fbfbfb"
  on-primary: "#ffffff"
  ink-dark: "#10141b"
  badge-alert: "#b74737"
  link: "#0066cc"
  border-strong: "#b3b3b3"
typography:
  display-xl: {fontFamily: "Avenir Next, Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Avenir Next, Avenir, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    height: "114px"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.badge-alert}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  product-media-gallery:
    backgroundColor: "{colors.canvas}"
    controlBackground: "{colors.surface-card}"
    controlColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"

## Components

**button-primary** is the principal call-to-action style (e.g. "Check Out", "Add to Cart"), using the inferred accent magenta against a white label; the flat rounded-sm corner follows the theme's plain, borderless button reset (`border:none;background:none` in the base `button` rule) rather than an observed radius.

**button-secondary** proposes an outlined variant for lower-emphasis actions such as "Keep Shopping," sharing the neutral hairline border color observed across the theme's gray palette.

**text-input** covers search and account fields; background and border are drawn from the light neutral tones (`#ffffff`, `#d7d9dc`) since no dedicated input selector was supplied.

**nav-bar** reflects the one concretely measured layout token in the evidence, `--menu-height: calc(114px)`, used here as a fixed header height; background and text colors are inferred as light/dark defaults, not confirmed by a header-specific rule.

**product-card** models the repeated pedal-tile pattern implied by the page text (name, price, "Sold Out" state) using a soft card surface and mid-radius corners; no explicit card CSS was in evidence, so padding and radius are proposed.

**hero** is a proposed introductory banner treatment; the dark ink-dark background is inferred from the palette's darker neutrals (`#10141b`, `#0f141c`) which plausibly serve full-bleed or overlay sections given the `[data-overlay-header].has-overlay` rule referencing `--menu-height`.

**footer** reuses the same dark neutral for a site-wide footer band containing the extensive link list seen in the page text (About, Support, How To, Blog, Contact); typography and spacing are proposed, not measured.

**badge** represents the "Sold Out" label seen on products like Barrel Aged Moonshine V2 and Coyote; the rust accent (`#b74737`) is inferred as a status/alert color since it appears in the palette without a bound selector.

**search** models the header "Search" affordance referenced in the page text, using the soft surface tone for a lightweight, low-contrast field treatment.

**product-media-gallery** is a category-appropriate component for pedal photo carousels/lightboxes, grounded in the observed `.flickity-button` (carousel arrows) and `.pswp__button` (photo-swipe lightbox, 2rem/32px controls) rules; colors and radius are inferred defaults since only structural sizing was in evidence.

## Responsive Behavior

| Breakpoint (proposed) | Target       | Notes |
|---|---|---|
| ≥1200px | Desktop | Full gutter/outer spacing scale (`--LAYOUT-GUTTER`, `--LAYOUT-OUTER` at 1x, per evidence) |
| 768–1199px | Tablet | Spacing scaled ~0.8x, matching the theme's second `:root` step (`--vertical:40px; --inner:18px; --base:15px`) |
| <768px | Mobile | Spacing scaled ~0.6x, matching the theme's third `:root` step (`--vertical:24px; --inner:16px; --base:14px`) |

The three spacing steps above are drawn directly from supplied `:root` custom-property blocks and indicate the theme does adjust rhythm at some breakpoints, but the pixel breakpoint values themselves were not supplied and are proposed conventions. Touch targets for buttons and nav items should be sized at minimum 44px in any mobile implementation; the header/menu is expected to collapse into a disclosure or slide-out pattern below tablet width, consistent with the "Show menu / Exit menu" toggle text present in the page content, though the actual collapsed layout was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and text extraction only; no rendered page, computed styles, or JavaScript-driven states were observed. Several theme variables (`--text`, `--bg`, `--COLOR-A50`, `--FONT-STACK-BODY`, `--FONT-WEIGHT-BODY`) are referenced in the CSS but never resolved to literal values in the supplied evidence, so their mapping to specific hex/typography tokens above is inferred, not confirmed. The assignment of accent hexes (`#ea005c`, `#b74737`, `#0066cc`) to primary/badge/link roles is a best-effort inference from an unordered color list, not a proven selector-to-color binding. All font sizes, the display scale, spacing scale, and radius scale are proposed design conventions, not measured from rendered output. Hover, focus, active, and error states for inputs, buttons, and the product gallery were not observed and are proposed only. Mobile menu behavior, cart drawer interaction, and gallery/lightbox interaction were referenced in text/selectors but not visually confirmed. Availability and licensing of Avenir, Avenir Next, and Figtree as served webfonts versus system fallbacks were not verified.
