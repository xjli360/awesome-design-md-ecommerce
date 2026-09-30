---
version: alpha
name: "Nuna"
source_url: "https://nunababy.com/usa/"
captured_at: "2026-09-29T03:58:43.387546+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the Nuna USA storefront (nunababy.com/usa/), an official Magento-based
  parent-site presentation of Nuna's car seats, strollers, and baby-gear catalog. The observed palette centers
  on a deep navy (#051d49, #102c61) against white canvas, with charcoal-to-mid-gray text tones (#333333,
  #363636, #767676) carried over from Magento/Klevu search-result styling rather than confirmed brand
  marketing components. Light neutral surfaces (#f5f5f5, #f8f8f8, #e4e4e4) and a thin #cccccc hairline
  recur across quick-search and hover states, suggesting a restrained, editorial layout consistent with
  premium juvenile-products merchandising. Two font families are directly observed: "New Transport" (likely
  a licensed/branded display face used for headings) and "Lexend" alongside system fallbacks Helvetica Neue,
  Arial, and Open Sans for body and UI copy — assignment of which family serves headings vs. body is inferred
  from typical pairing conventions, not confirmed from layout evidence. Accent blue (#1979c3) and red (#cc0000)
  are present in Magento default styling and are treated here as inferred link/alert accents rather than
  confirmed brand accents. All component patterns below are proposed interpretations built from these
  fragments, not reconstructions of measured site behavior.

colors:
  primary: "#051d49"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#363636"
  muted: "#767676"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  secondary-navy: "#102c61"
  accent-blue: "#1979c3"
  alert: "#cc0000"
  border-soft: "#e4e4e4"
  neutral-black: "#000000"
typography:
  display-xl: {fontFamily: "'New Transport', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'New Transport', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Lexend, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lexend, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lexend, sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.border-soft}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    hoverBackground: "{colors.surface-card}"
    border: "1px solid {colors.border-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.secondary-navy}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    resultHoverBackground: "{colors.surface-soft}"
    linkColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  stroller-feature-card:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"

## Components
**button-primary** renders calls-to-action such as "Shop Now" using the observed deep navy as fill with white
text; proposed as the highest-emphasis interactive element on hero and category modules.

**button-secondary** is an outline treatment for lower-emphasis actions (e.g., "Learn About Us"), sharing the
primary navy as border/text color on a transparent field — proposed, not confirmed from captured markup.

**text-input** models a standard form field (newsletter signup, search) using the hairline border color and
light canvas fill observed generally across Magento-based storefronts; padding and radius are proposed.

**nav-bar** is inferred from the "Skip to Content / Explore / Sign In / Show search" text sequence, rendered
as a white bar with dark text and a soft bottom hairline; no direct nav CSS was supplied, so spacing and
alignment are proposed.

**product-card** draws directly from the Klevu quick-search hover rule (`background-color:#f8f8f8`) and
default `#333` text, extended into a full product-tile pattern for category/PLP use with proposed border and
padding.

**hero** proposes the "BIRTH TO 65 LBS" / car-seat-stroller-system banner as a full-bleed navy panel with
large display type in white — a plausible reading of the excerpted copy, not a captured layout.

**footer** models the long link list (About, Registry, Careers, Legal, etc.) on the deeper navy tone as a
dark footer band with light text — proposed pattern; actual footer background was not confirmed in CSS.

**badge** generalizes the discount/sale badge styling seen in Klevu no-results markup, remapped to the
observed alert red for stock/sale flags since the original yellow value fell outside the supplied palette.

**search** reconstructs the quick-search dropdown using the confirmed `#333` link color, `#f5f5f5` hover
state, and thin gray divider — this is the most directly evidenced component in the supplied CSS.

**stroller-feature-card** is a category-appropriate proposed component for surfacing stroller attributes
(terrain tires, suspension, fold type) in a soft-surface card, aligning with the "Made for adventures" copy
block; typography and spacing are proposed, not measured.

## Responsive Behavior
Recommended (not measured) breakpoints:

| Range | Layout intent |
|---|---|
| ≤480px | Single-column stack, nav collapses to hamburger/search icon, hero type drops to `display-md` scale |
| 481–768px | Two-column product grids, sticky search bar, buttons retain full-width on primary CTAs |
| 769–1024px | Three-column product/category grids, inline nav links replace collapsed menu |
| ≥1025px | Four-column grids, full desktop nav, hero uses `display-xl` |

Touch targets should maintain a minimum 44×44px hit area for nav, search, and button components. Collapse the
primary nav into a drawer or overlay below 768px, and stack hero copy above imagery on narrow viewports. This
table is a design recommendation only and does not reflect measured breakpoints from the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction; no rendered layout, grid structure, or breakpoint behavior was
  directly observed.
- Semantic color roles (primary, alert, accent) are inferred from Magento/Klevu default class usage, not
  confirmed brand style-guide assignments.
- Font-family-to-role mapping (New Transport for display, Lexend for body) is inferred from naming
  convention and common pairing practice, not confirmed from computed styles on headings/body text.
- Type scale sizes beyond the small Klevu-search values (10px/12px/13px) are proposed, not measured.
- Interaction states (focus rings, active/disabled buttons, form validation) were not present in supplied
  CSS and are marked proposed throughout.
- Mobile/tablet layout, nav collapse pattern, and touch-target sizing are recommendations, not observed
  site behavior.
- Availability, licensing, and web-font delivery of "New Transport" were not verified; treat as an
  observed-but-unconfirmed brand asset.
