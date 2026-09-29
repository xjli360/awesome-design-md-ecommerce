---
version: alpha
name: "Bronwen Jewelry"
source_url: "https://bronwenjewelry.com"
captured_at: "2026-09-28T04:37:34.249583+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Bronwen Jewelry's storefront draws from a warm, editorial palette anchored by a
  soft gold accent (#e1ac64) against neutral off-whites and warm dark grays. The
  observed CSS shows a white (#ffffff) header background with a light gray
  hairline border, dark warm-gray body copy (#4c4848), and a muted secondary
  gray (#707070) for supporting text. A deep navy (#1d2135) appears in the
  palette and is inferred here as a footer or dark-surface color, while a warm
  cream (#fbf9f2) is proposed as a soft card surface consistent with a
  handmade-jewelry aesthetic. Typography combines Tenor Sans for display and
  heading roles with Open Sans/Helvetica Neue for body copy, and Dosis for
  small uppercase, letter-spaced labels such as buttons and eyebrow captions —
  this pairing is inferred from font list co-occurrence with heading and
  button CSS variables, not confirmed per-element. Heading sizes are taken
  directly from the site's `--heading-*-font-size` custom properties. Rounded
  corners and spacing scales are proposed conventions sized to match the
  site's 52px input/button height and 40–48px vertical breather variables.
  Semantic color roles (primary, ink, muted, hairline, surface) are inferred
  groupings of the raw observed hex values; no proprietary font license or
  live rendered layout has been verified.

colors:
  primary: "#e1ac64"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#4c4848"
  muted: "#707070"
  hairline: "#dedede"
  border-strong: "#cccccc"
  surface-soft: "#f9f9f9"
  surface-card: "#fbf9f2"
  on-primary: "#ffffff"
  surface-dark: "#1d2135"
  alert: "#ec4048"
typography:
  display-xl: {fontFamily: "Tenor Sans, sans-serif", fontSize: "56px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Tenor Sans, sans-serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "Tenor Sans, sans-serif", fontSize: "24px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Dosis, sans-serif", fontSize: "12px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "1.5px"}
  button-md: {fontFamily: "Dosis, sans-serif", fontSize: "13px", fontWeight: 600, lineHeight: 1, letterSpacing: "1px"}
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
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: "52px"
    padding: "{spacing.none} {spacing.lg}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.caption}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: "52px"
    padding: "{spacing.none} {spacing.lg}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** is the main call-to-action treatment (e.g. "Add to Cart"), using the gold accent as background with white text and the site's uppercase, letter-spaced button typography; hover/active states are proposed, not observed. **button-secondary** offers an outlined alternative on white surfaces for lower-emphasis actions such as "View Details." **text-input** models the form field styling directly evidenced by the theme's `.input__field` rules (52px height, hairline border, focus ring switching to the ink color). **nav-bar** reflects the sticky white header with a light bottom hairline, consistent with the `--header-background` and `--header-border-color` variables observed. **product-card** is a proposed pattern for jewelry listings, pairing a soft cream card surface with Tenor Sans product titles and Open Sans pricing. **hero** proposes a light, spacious banner section using the large display heading size scaled from the desktop `--heading-h1-font-size` variable. **footer** is inferred to use the deep navy tone from the palette as a dark background with white text and small caption-style headings, matching the uppercase accordion header style seen in `.footer .accordion-item-header-title`. **badge** is a small pill label (e.g. "New" or "Sale") using the primary accent color, proposed for promotional tagging. **search** mirrors the text-input pattern for the site's search field. **material-tag** is a category-specific component proposed for jewelry metal/material labels (e.g. "14k Gold Fill"), styled subtly with muted text and a thin border to sit unobtrusively near product titles.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column stacking, nav collapses to a hamburger/drawer (not observed) |
| Tablet | 600–999px | 2-column product grids, condensed header padding |
| Desktop | 1000–1439px | Matches `--heading-*` desktop custom properties observed in CSS |
| Wide | ≥1440px | Max-width container using `--container-gutter` and 20-column grid variable |

Touch targets should be a minimum of 44px, aligning with the observed `--button-small-height: 44px`. Primary buttons and inputs already meet this via the 52px height variable. Navigation is assumed to collapse into an off-canvas or accordion menu on mobile; this interaction was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and a color/font inventory only; no rendered page, computed layout, or interaction state was observed. Semantic role assignments (e.g. treating `#e1ac64` as primary, `#1d2135` as a footer background, or `#fbf9f2` as a card surface) are inferred from limited selector context and may not match actual usage. Heading and body font-family pairings (Tenor Sans for display, Open Sans/Helvetica Neue for body, Dosis for labels) are inferred from co-occurrence in the font list, not from confirmed `--heading-font-family`/`--text-font-family` values. Spacing, rounded-corner, and component padding values beyond the explicitly observed 52px form height and 40–48px breather variables are proposed conventions. Mobile navigation collapse, hover/focus micro-interactions beyond the documented input focus ring, and actual grid/column behavior were not observed. Availability and licensing of Tenor Sans, Dosis, and Open Sans for production use have not been verified.
