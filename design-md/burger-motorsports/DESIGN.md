---
version: alpha
name: "Burger Motorsports"
source_url: "https://burgertuning.com/"
captured_at: "2026-09-29T04:12:04.903827+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from static CSS/color extraction of burgertuning.com,
  the current Shopify-based storefront for Burger Motorsports Inc. (JB4 tuners,
  intakes, oil catch cans, flex-fuel sensors). The observed palette centers on a
  high-contrast black/white base (#000000, #ffffff, #1a1a1a) with a saturated red
  (#dd2525, #b52727, #d2354f, #f4534d) used across sale badges and fitment-fail
  states, and a green (#11ae66) used for fitment-success states in the vehicle
  search widget. Grays (#333333–#f7f7f7) form body text, muted copy, hairlines,
  and card surfaces. A blue (#0288d1) appears in interactive/info contexts.
  Font evidence includes Arial, Helvetica, Open Sans, Inter, Montserrat,
  GTStandard-M, and Corben; GTStandard-M is treated here as an inferred
  display/heading candidate given its distinct non-generic name, Montserrat and
  Inter as inferred UI/button faces, and Open Sans/Arial as inferred body
  fallbacks. Corben's usage is unverified and not assigned a role. The resulting
  system favors a utilitarian, parts-catalog aesthetic: dense product grids,
  red accent-driven urgency (sale pricing), and a vehicle-fitment search
  pattern as the primary category-specific interaction surface. All sizing,
  spacing, and component states below are proposed unless explicitly tied to
  supplied CSS.

colors:
  primary: "#dd2525"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e6e6e6"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  success: "#11ae66"
  danger: "#f4534d"
  sale: "#b52727"
  accent-blue: "#0288d1"
  border-strong: "#1a1a1a"
  divider: "#dcdcdc"
typography:
  display-xl: {fontFamily: "GTStandard-M, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GTStandard-M, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.4px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border-strong}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.divider}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.divider}"
    padding: "{spacing.sm} {spacing.md}"
  fitment-widget:
    backgroundColor: "{colors.surface-soft}"
    successColor: "{colors.success}"
    failColor: "{colors.danger}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** — The red-on-white call-to-action button (e.g., "Add to Cart," "Search") using the observed `#dd2525` primary red against a white label, sized for a comfortable click/tap target. Hover/active darkening is proposed, not observed.

**button-secondary** — An outlined black-on-white button for secondary actions ("View More," "Contact"), using the ink border color against the canvas background. States beyond default (hover, disabled) are proposed.

**text-input** — Form fields for search, email signup, and vehicle-fitment selects, using a light hairline border and body typography. Focus-ring styling is not observed in the supplied CSS and is proposed as a thin accent-blue outline.

**nav-bar** — A white top navigation housing make-based category links (BMW, VW/AUDI, etc.) and the "Search by vehicle" tool. Sticky/scroll behavior is not confirmed from static evidence.

**product-card** — The repeating grid unit for JB4 tuners, intakes, and catch cans, pairing a title, price (with optional strikethrough regular price and sale badge), and category label. Card elevation/shadow is proposed, not measured.

**hero** — A dark, full-bleed introductory band (e.g., "JB4 = FASTEST") using inverted (light-on-dark) type per the ink/canvas contrast pattern. Imagery treatment is not verified from CSS alone.

**footer** — A dark footer block listing informational links (FAQ, dealer program, return policy) and the VIP email signup, mirroring the hero's inverted color logic for brand consistency.

**badge** — A small pill label for "Sale" pricing states, using the deeper sale-red (#b52727) distinct from the primary red to differentiate promotional flags from primary actions.

**fitment-widget** — A category-specific component reflecting the "Search by vehicle" and fitment-check pattern: success messaging in green (#11ae66) and failure/incompatibility messaging in red (#f4534d), directly observed in the supplied EasySearch selectors.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| sm | 375px | Single-column product grid, stacked nav collapses to menu icon |
| md | 768px | 2-column product grid, vehicle search widget may expand inline |
| lg | 1024px | 3–4 column product grid, full horizontal nav |
| xl | 1280px+ | Max content width with side margins, hero at full scale |

Touch targets for buttons and select inputs should maintain a minimum 44px height. Below `md`, the make-based navigation is recommended to collapse into a disclosure/hamburger pattern, and the vehicle fitment search should stack its Make/Model/Year selects vertically. This table is a recommendation based on common e-commerce patterns, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS rules, a color list, and page-text excerpts only; no live rendering, computed styles, or DOM layout were observed. Semantic color roles (e.g., which red is "primary" versus "sale" versus generic error) are inferred from usage context in the supplied selectors, not confirmed via design documentation. Typography sizes, weights, and letter-spacing in the `typography` block are proposed conventions, not extracted pixel values, except where a font-family name itself was directly present in evidence. The role and availability of `GTStandard-M` and `Corben` as licensed, deployed fonts is unverified. No interaction states (hover, focus, active, disabled) were observed beyond the two Shopify payment-button hover rules noted in evidence, and mobile/responsive layout behavior was not captured from the static source. Component paddings, radii, and shadows are proposed defaults consistent with the observed flat, high-contrast aesthetic, not measured values.
