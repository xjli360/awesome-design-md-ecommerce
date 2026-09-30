---
version: alpha
name: "DUC Woodworks"
source_url: "https://ducwoodworks.com"
captured_at: "2026-09-28T04:38:31.656358+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed CSS surfaces a dark neutral core — #32373c and #181d23 — used
  for primary buttons and implied heading ink, paired with a lighter body
  gray (#55595c) and a muted blue-gray (#69727d) likely used for secondary
  text or icon fills. Pill-shaped buttons (border-radius: 9999px) and a solid
  black (#000000) circular scroll-to-top control are the only concretely
  observed interactive shapes. A red (#d9534f) appears solely on the cart
  count bubble, suggesting a reserved alert/badge role rather than a brand
  color. The remaining palette entries (bright blues, greens, oranges,
  purples) are typical WordPress/Gutenberg and Elementor-kit default swatch
  libraries bundled with the theme and plugins, not confirmed brand choices;
  they are treated here as available-but-unassigned rather than load-bearing.
  Font evidence points to Archivo and Inter as the active webfont stack, with
  Font Awesome/eicons/jkiticon as icon fonts only.

  This interpretation proposes a restrained, trade-craftsman aesthetic: dark
  charcoal neutrals for structure and text, off-white/light-gray surfaces for
  cards and sections, and a single warm yellow (#ffc402, present in the raw
  palette) reserved as an inferred accent evoking finished wood — a semantic
  assignment not confirmed by the supplied CSS rules.

colors:
  primary: "#32373c"
  ink: "#181d23"
  canvas: "#ffffff"
  body: "#55595c"
  muted: "#69727d"
  hairline: "#d5d5d7"
  surface-soft: "#f7f7f7"
  surface-card: "#eaeaeb"
  on-primary: "#ffffff"
  accent: "#ffc402"
  danger: "#d9534f"
  dark-surface: "#000000"
typography:
  display-xl: {fontFamily: "Archivo, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Archivo, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Archivo, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: "18px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.2px"}
rounded:
  none: "0px"
  xs: "2px"
  sm: "4px"
  md: "8px"
  lg: "16px"
  full: "9999px"
spacing:
  none: "0px"
  xxs: "2px"
  xs: "4px"
  sm: "8px"
  md: "12px"
  base: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "64px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    typography: "{typography.body-md}"
  project-gallery-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    caption: "{typography.caption}"
    padding: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** renders as a dark charcoal pill matching the observed `.wp-block-button__link` rule (`background-color:#32373c`, `border-radius:9999px`, white text). It is the sole button pattern with direct CSS evidence.

**button-secondary** is a proposed outline variant using the same ink color for border and text on a transparent field, intended for lower-emphasis actions (e.g., "View Portfolio") alongside the solid primary CTA. Not directly observed.

**text-input** is inferred from general WordPress form conventions; no explicit `<input>` styling was present in the supplied CSS, so border, radius, and padding are proposed defaults consistent with the site's hairline gray and small radius scale.

**nav-bar** assumes a light canvas header with dark ink text and a hairline bottom rule, appropriate for a header-footer-elementor–built site; actual header markup/behavior was not captured in the evidence.

**product-card** and **project-gallery-tile** are proposed patterns for a woodworking business: the former for any shop/catalog items (paired with the observed cart-icon widget), the latter as a category-specific tile for finished-project photography, using a softer surface and small radius to keep imagery prominent.

**hero** proposes a dark ink background with large Archivo display type and white text, giving the homepage title ("Custom Woodworking to Transform Your Space") strong contrast; this treatment is speculative, not measured from the live layout.

**footer** reuses the primary dark surface for brand consistency with the button color, an inferred choice since no footer-specific background rule was supplied.

**badge** directly reflects the observed `.hfe-menu-cart__toggle` counter bubble: red background, white text, fully rounded, small font-size — used here as the canonical alert/notification indicator.

**search** is a proposed light-field pattern derived from the `.hfe-search-form__container` selectors present in the evidence, which confirm a clear-button and toggle mechanism but not full visual styling.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 600px | Single-column stacks; nav collapses to a toggled menu; hero type drops to `{typography.display-md}` scale. |
| Tablet | 600–959px | Two-column card grids; nav-bar may remain horizontal or collapse depending on menu item count. |
| Desktop | ≥ 960px | Full multi-column layout; hero at `{typography.display-xl}`; footer columns expand. |

Touch targets should be at least 44×44px, particularly for the pill buttons and the fixed scroll-to-top control, which the evidence shows rendered at 50×50px. Navigation collapse thresholds, menu behavior, and actual grid column counts were not observed and are recommendations only, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text evidence and a title string; no rendered page, computed layout, or interaction states were observed. Color-to-role assignments (e.g., accent = #ffc402, ink = #181d23) are inferred from likely usage patterns, not confirmed by selectors targeting those hexes. Most typography sizes beyond the button's `1.125em` are proposed, not measured. Component states (hover, focus, active, disabled), mobile menu behavior, and responsive breakpoints are not present in the supplied evidence. Availability and licensing of Archivo and Inter as self-hosted or third-party webfonts were not verified. The large residual color list is treated as unassigned theme/plugin defaults rather than deliberate brand palette.
