---
version: alpha
name: "Covercraft"
source_url: "https://covercraft.com"
captured_at: "2026-09-28T09:25:08.273797+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Covercraft's storefront CSS evidence shows a utilitarian e-commerce system built on Angular/SAP Commerce Cloud component patterns (custom-product-card, product-compare-dialog) rather than a heavily styled marketing skin. The observed palette centers on a neutral ink-on-white base (#212529, #54575e, #ffffff) with a saturated blue (#0070f2 / #0064d9) appearing in interactive contexts, a red (#db0002) likely reserved for promotional messaging such as the "20% OFF" banner, and a green (#38871f) used for a confirmation checkmark icon. Grays (#f4f4f4, #d3d6db, #dee2e6) form card borders and soft surfaces. Montserrat is the only font family explicitly tied to product-card typography in the supplied CSS; Effra, Open Sans, and system sans-serif stacks are present in the font manifest and are treated here as inferred body/UI candidates since no body-text rule was captured. This interpretation proposes a functional, catalog-dense design language: dense product grids, compact uppercase labels, and small-scale metadata text (10–14px), reflecting the brand's large SKU catalog across automotive, marine, RV, and patio categories. Semantic color-to-role assignments (primary action, success, alert) are inferred from usage context, not confirmed brand guidelines.

colors:
  primary: "#0070f2"
  link: "#0064d9"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#54575e"
  muted: "#6c7079"
  hairline: "#d3d6db"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-alert: "#db0002"
  success: "#38871f"
  warning: "#ffc107"
  info: "#17a2b8"
  navy-deep: "#14293a"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "Effra, Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Effra, Open Sans, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Effra, Open Sans, sans-serif", fontSize: 10px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    accentIcon: "{colors.success}"
  hero:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the primary blue call-to-action (e.g. "Explore Deals," "Sign In") using the observed interactive blue against white text; uppercase button styling is drawn from the dialog-header button pattern in the compare tool.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g. "Create an account"), reusing the primary blue as border/text on a white field since no distinct secondary color was captured in evidence.

**text-input** covers search and form fields; border and radius are inferred from general gray hairline tokens since no explicit input CSS was supplied.

**nav-bar** represents the mega-menu header implied by the extensive "SHOP / Products / Featured Brands" text hierarchy; background and hairline are inferred, not measured from a captured header rule.

**product-card** is directly grounded in the supplied `.custom-product-card` rule: a bordered white card, Montserrat bold 14px product name, a green checkmark craft-name icon, and small compare/rating metadata at 10–12px.

**hero** is a proposed full-width banner using the deep navy tone observed in the palette (#14293a), intended for category or seasonal promotion imagery; no hero layout was directly observed.

**footer** reuses the navy-deep background with white text and blue links, following common dark-footer conventions; not confirmed from captured footer selectors.

**badge** models the "20% OFF" promo tag and compare-count indicators using the alert red against white text in a pill shape; the compare-dialog's yellow button (#ffcb5b) was seen in raw CSS but excluded here since it falls outside the supplied palette array.

**search** is a proposed autocomplete field based on the "autocomplete results" text cue in page copy; no direct search-bar styling was in the CSS evidence.

**vehicle-fitment-selector** is a category-appropriate proposed component reflecting Covercraft's core "custom-fit by vehicle" shopping flow (year/make/model lookup implied by "Shop by Vehicle" navigation), styled as a soft-surface panel consistent with other card surfaces.

## Responsive Behavior

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <576px | Single-column product grid; nav collapses to hamburger/off-canvas (proposed) |
| tablet | 576–991px | 2-column product grid; mega-menu condenses to accordion |
| desktop | 992–1279px | 3–4 column product grid; full mega-nav visible |
| wide | ≥1280px | 4+ column grid; hero and footer gain max-width containers |

Touch targets should be a minimum 44×44px for nav and cart controls. This table is a recommendation derived from typical commerce-grid conventions, not a measured breakpoint set from the supplied CSS, which contained no `@media` evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static, partial CSS/text extraction and does not include measured page layout, computed breakpoints, or verified interaction states (hover, focus, active, disabled). Several color-to-role assignments (primary action blue, alert red, success green, navy hero/footer) are inferred from limited class context and should be validated against live rendering. Body and UI font family (Effra/Open Sans) is inferred from the font manifest since no body-text CSS rule was captured; only the product-card's Montserrat usage is directly evidenced. All font availability, weights (e.g. Montserrat-Bold, Montserrat-SemiBold, Montserrat-XBold), and licensing were not verified. Spacing and rounded-corner scales are proposed conventions, not extracted values, apart from the compare-dialog's observed pixel figures. Mobile menu structure, hero content, and footer composition were not directly observed and are marked as inferred/proposed throughout.
