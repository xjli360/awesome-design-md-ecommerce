---
version: alpha
name: "Stiletto"
source_url: "https://stiletto.com"
captured_at: "2026-09-29T04:06:33.743985+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Stiletto's site presents a professional-tools identity built on a Bootstrap 5
  foundation, with body copy inheriting a system sans-serif stack (Helvetica,
  Helvetica Neue, Arial) and headings referencing a licensed-looking condensed
  family ("55 Roman"/"65 Medium") that renders with sans-serif fallback since
  licensing was not verifiable from static CSS. A muted bronze/tan accent
  (#c5a37a) appears on a search icon, suggesting a small warm accent role
  distinct from the neutral grayscale system (#000000, #333333, #777777,
  #dddddd, #eeeeee, #f8f9fa) used for text, borders, and surfaces. The broader
  supplied palette is dominated by Bootstrap's default utility colors (danger,
  success, warning, info shades), which are inferred as system/alert tokens
  rather than brand colors, since no dedicated brand primary was observed.
  This interpretation treats #c5a37a as the closest available accent for
  primary actions, #000000/#212529 for ink, and #ffffff/#f8f9fa for canvas
  and soft surfaces, reflecting a utilitarian, high-contrast trade-tool
  aesthetic. All semantic role assignments below are inferred from limited
  evidence, not confirmed brand guidelines.

colors:
  primary: "#c5a37a"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f8f9fa"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  danger: "#dc3545"
  success: "#198754"
  warning: "#ffc107"
  info: "#0dcaf0"
  border-strong: "#adb5bd"
  text-secondary: "#495057"
typography:
  display-xl: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    headerTypography: "{typography.body-sm}"
    cellTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** uses the observed bronze/tan accent as a call-to-action fill; this is proposed since no confirmed CTA background color was captured in the evidence. **button-secondary** is an outlined variant using the neutral hairline border, proposed for secondary actions like "Learn More" links seen in the source text. **text-input** reflects standard Bootstrap-style form field conventions inferred from the framework's presence, not a directly observed input capture. **nav-bar** models the header/menu structure implied by the extensive "Show submenu" navigation text, using neutral ink-on-white styling consistent with the grayscale system. **product-card** is proposed for the "Best Sellers" grid (e.g., TIBONE™ hammers, carpenter squares), using a soft card surface and hairline border for separation. **hero** proposes a dark, high-contrast banner treatment for the "THE ORIGINAL TITANIUM FRAMING HAMMER" statement, using ink background with white text for a rugged, industrial tone appropriate to the trade-tool category. **footer** mirrors the dark hero treatment for consistency across the page's terminal sections (copyright, legal links). **badge** is proposed for labels like "Limited Edition Colors" or best-seller flags, using the accent color pill shape. **search** describes the observed desktop search affordance, directly reflecting the captured icon color (#c5a37a) and gray placeholder text (#858585, approximated to muted). **spec-table** is proposed for tool specification displays (weight, material, dimensions) common to hand-tool product pages, using neutral surface-soft background for readability.

## Responsive Behavior
This is a recommendation, not measured site behavior. Proposed breakpoints follow Bootstrap 5 defaults referenced in the CSS variables:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| xs | 0px | Single-column stack, collapsed nav behind toggle |
| sm | 576px | Two-column product grids begin |
| md | 768px | Nav submenus may expand inline; three-column grids |
| lg | 992px | Full desktop nav bar with dropdown submenus |
| xl | 1200px | Four-column product/category grids |
| xxl | 1400px | Max-width content container, generous gutters |

Touch targets should maintain a minimum 44px height for buttons and nav links on mobile. Submenus (e.g., "Hammers & Axes," "Squares") should collapse into accordions below the md breakpoint given their nested structure in the observed markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, live interaction states (hover, focus, active), or mobile behavior were observed. The heading font ("55 Roman"/"65 Medium") could not be verified as a licensed brand font and is not asserted as available; sans-serif fallback is used throughout. Color role assignments (primary, muted, hairline, etc.) are inferred from limited CSS selector context (mostly a search icon and Bootstrap utility defaults) rather than confirmed brand style guides. Typography sizes, spacing scale, and rounded-corner values are proposed conventions, not measured from the source. Bootstrap's default alert/status colors (danger, success, warning, info) are included for completeness but are not confirmed as intentionally chosen brand colors. Component definitions (product-card, spec-table, hero, etc.) are reasonable proposals for a hand-tools e-commerce site but do not reflect verified DOM structure or class names beyond the header/search selectors supplied.
