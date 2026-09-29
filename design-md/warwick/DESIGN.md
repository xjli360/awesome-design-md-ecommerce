---
version: alpha
name: "Warwick"
source_url: "https://www.warwick.de/en/Warwick.html"
captured_at: "2026-09-29T04:11:45.141343+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Warwick's markup exposes a dark, utilitarian visual system: html/body is set
  to pure black (#000000) with white (#ffffff) text at a compact 11px base
  size, rendered in Verdana with 'Open Sans' as a fallback (Arial/Helvetica
  appear only inside a third-party Facebook dialog widget and are treated as
  external, not brand type). A saturated gold/amber accent — #ffc611 for the
  cookie-consent button and #ffcc00 ("#fc0") for hover states and callout
  links — is the strongest chromatic signal against the black-and-white base,
  so it is interpreted here as the primary brand accent for buttons, active
  navigation states, and highlighted links. Supporting grays (#333333,
  #666666, #999999, #cccccc) are inferred as hairlines, muted text, and
  borders; near-black tones (#212121, #373737) are inferred as elevated
  surfaces on the black canvas.

  Because the sampled CSS is dominated by legacy fixed-width layout classes
  (product_series_overview_menue_*, four/five_col_design__button_link,
  custom_galerie_product_title) with pixel-based absolute positioning, this
  interpretation treats spacing, corner radii, and larger display type sizes
  as proposed, modern approximations rather than measured values — applied to
  convey a dark, product-photography-forward bass-guitar catalog rather than
  to reproduce the legacy table-like structure directly.

colors:
  primary: "#ffc611"
  accent-hover: "#ffcc00"
  ink: "#ffffff"
  canvas: "#000000"
  body: "#ffffff"
  muted: "#999999"
  hairline: "#333333"
  border: "#cccccc"
  surface-soft: "#212121"
  surface-card: "#373737"
  on-primary: "#000000"
typography:
  display-xl: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 10px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Verdana, 'Open Sans', sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.border}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.accent-hover}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelColor: "{colors.muted}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.accent-hover}"
    typography: "{typography.caption}"
    padding: "{spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** renders the site's one confirmed interactive color pairing — gold background (`#ffc611`) with black text — as observed on the cookie-consent control, generalized here to primary calls to action such as "Shop" or "Add to Cart." Hover/active states are proposed, not observed.

**button-secondary** is an inferred outline variant for lower-emphasis actions (e.g. "Compare," "More Info"), using the observed light gray border color against the black canvas so it reads on a dark page without competing with the gold primary.

**text-input** is a proposed dark-mode form field (search boxes, dealer locator, newsletter signup) matching the black canvas and light gray border already used for the legacy `.warwick_search_button`, since no dedicated input styling was present in the sampled CSS.

**nav-bar** generalizes the observed pattern from `.product_series_overview_menue_link a` and its `:hover` state (white text shifting to `#fc0`/`#ffcc00` gold) into a full top or side navigation bar for sections like Products, Company, Support, and Shop.

**product-card** is a proposed container for individual bass models, informed by `.custom_galerie_product_title` (white, centered caption overlay on product imagery) and the dark surface tones (`#373737`) inferred as card backgrounds against the pure black page.

**spec-table** is a category-appropriate addition for bass-guitar technical specs (tonewoods, pickups, scale length), using the muted gray label color and hairline dividers inferred from the grayscale portion of the palette; no literal spec-table markup was present in the evidence.

**hero** is a proposed large-format header treatment for product-series landing pages, pairing the display type scale with the black canvas; exact hero copy, imagery, and layout were not present in the supplied CSS/text.

**footer** reflects the observed footer text content (Imprint / Contact / Privacy Policy, copyright line) styled with muted gray body text and gold-on-hover links, consistent with the accent-hover behavior seen elsewhere in the stylesheet.

**badge** and **search** are proposed small-scale UI elements (e.g. "New," "In Stock" tags; a compact search trigger) derived from the compact caption-sized, bold, uppercase treatment observed in `.cookie-notice button` and `.warwick_search_button a`.

## Responsive Behavior

This is a recommended breakpoint scheme, not a measured behavior of the live site (no media queries or responsive layout evidence were supplied):

| Breakpoint | Range | Notes |
|---|---|---|
| Compact | <600px | Single-column stack; nav collapses to a toggled menu; product cards full-width. |
| Medium | 600–1024px | Two-column product grids; nav remains visible or condenses to icons. |
| Wide | >1024px | Multi-column product/category grids; full horizontal nav bar. |

Touch targets should be at least 44×44px for buttons and nav items (proposed, not observed). Navigation collapse behavior, menu animation, and any legacy fixed-width breakpoints implied by the `four_col_design`/`five_col_design` class names were not confirmed in a live rendered layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Roles for canvas, ink, surface-soft, and surface-card are inferred from a grayscale/black palette rather than confirmed brand documentation. Larger display type sizes, spacing scale, and corner radii are proposed values, since the sampled CSS shows only small utility font sizes (10–15px) and legacy pixel-based absolute positioning rather than a modern spacing/radius system. Hover, focus, active, and disabled states beyond the single documented `:hover` link-color change are proposed, not observed. Mobile/responsive layout, menu collapse behavior, and touch interactions were not present in the evidence and are marked as recommendations. Font availability, licensing, and exact rendering of Verdana/"Open Sans" across platforms were not verified; Arial/Helvetica rules originate from a third-party Facebook dialog widget and are excluded from the brand type system.
