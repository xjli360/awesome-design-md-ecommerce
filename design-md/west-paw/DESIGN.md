---
version: alpha
name: "West Paw"
source_url: "https://westpaw.com"
captured_at: "2026-09-28T09:17:34.356949+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  West Paw's storefront CSS exposes a bright, workshop-friendly palette built around a cyan-blue brand color (#09bcef) paired with a warm orange-red accent (#f04824/#f04824-family) used for active button states and promotional badges. Neutral ink and body tones (#2d2d2d, #4c4c4e) sit on a white canvas, with soft cyan-tinted surfaces (#eff8fa, #f1f8fa) evidenced in section backgrounds and badge fills (#fdede9). Two font stacks are declared in :root: a heading family "mindset" (rendered at regular weight per --font-heading-bold-weight:400) and a body family "akzidenz-grotesk" (bold weight 600), both falling back to Helvetica/Arial/sans-serif since neither is confirmed as licensed or locally available.
  This interpretation treats #09bcef as primary brand color and #1f76a5 as a secondary/outline accent, both directly observed in button custom properties. Rounded corners are inferred from a single observed 6px radius on collection-nav buttons, generalized into a broader proposed scale. Layout, spacing rhythm, and responsive breakpoints are not present in the supplied CSS and are proposed conventions for a durable-goods pet product catalog, not measured observations.

colors:
  primary: "#09bcef"
  ink: "#2d2d2d"
  canvas: "#ffffff"
  body: "#4c4c4e"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#eff8fa"
  surface-card: "#f7f7f8"
  on-primary: "#ffffff"
  accent: "#f04824"
  accent-alt: "#1f76a5"
  badge-bg: "#fdede9"
  badge-text: "#f04925"
  highlight-soft: "#ceeef9"
  tooltip-bg: "#252525"
typography:
  display-xl: {fontFamily: "mindset, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "mindset, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "mindset, Helvetica, Arial, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "akzidenz-grotesk, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "akzidenz-grotesk, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "akzidenz-grotesk, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "mindset, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1, letterSpacing: 0px}
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
    textColor: "{colors.accent-alt}"
    borderColor: "{colors.accent-alt}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hoverAccent: "{colors.accent}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-card:
    backgroundColor: "{colors.highlight-soft}"
    accentColor: "{colors.accent}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** maps to the observed `--button-dark` custom properties (#09bcef background, white text, orange-red #f04824 active state), used for primary calls to action like "Shop Now" and "Subscribe Now."

**button-secondary** reflects the observed `--button-outline` variables, using #1f76a5 as both text and border color with a transparent fill — proposed for secondary actions such as "Learn More."

**text-input** is a proposed pattern for search and account forms; no explicit input styling was present in the supplied CSS, so border and padding values are inferred from general form conventions.

**nav-bar** represents the persistent header/menu system referenced in the page text (Shop, Toys, Treats, Feeding, Recipes, About). The #F04B23 hover border-color rule on `[data-dropdown-link]` confirms an orange hover accent on navigation items.

**product-card** is a proposed container for toy/treat listings (e.g., Toppl, Qwizl, Tux, Feast Mat) using the soft card surface and hairline border; no explicit card CSS was supplied, so this pattern is inferred from typical catalog layout needs.

**hero** corresponds to the homepage banner content ("Spooky Season is Here," "Dog toys that do good") and uses the soft cyan surface tone with the heading display type; exact hero CSS was not present in evidence.

**footer** is proposed as a dark-ink band consistent with typical e-commerce footers containing social links (Facebook, Instagram, YouTube) and region selector, though footer-specific styling was not in the supplied rules.

**badge** models the `.collection-nav-link.dark` treatment (#FDEDE9 background, #f04925 text, 6px radius) observed directly in CSS, appropriate for promotional labels like "Halloween Colors" or "New."

**search-bar** is inferred from the repeated "Enter Search Keywords" placeholder text; no search input styling was included in the CSS evidence, so shape and color are proposed.

**subscription-card**, the category-appropriate component, reflects the "Never Run Out of Treats Again" subscribe-and-save module described in the page text, using the light cyan highlight tone (#ceeef9) and orange accent for savings messaging — a proposed pattern, not a directly styled selector.

## Responsive Behavior
Recommended, not measured: mobile <480px (single-column, stacked nav collapsing into a drawer using the observed `--drawer-max-width: 375px`), tablet 480–1024px (two-column product grids), desktop >1024px (multi-column grids, persistent top nav). Touch targets should be at least 44px; navigation dropdowns collapse to an accordion pattern on touch devices. This table is a proposed convention based on common e-commerce breakpoints, not observed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and a single page-text excerpt; no rendered layout, computed styles, or interaction states (hover/focus/active beyond the declared button variables) were observed. Semantic role assignments (e.g., which cyan or orange shade is "primary" vs. "accent") are inferred from variable naming, not visual hierarchy confirmation. Rounded and spacing scales are proposed conventions extrapolated from a single 6px radius data point. The "mindset" and "akzidenz-grotesk" font families are referenced in CSS but their licensing, self-hosting, or availability could not be verified; fallback stacks are assumed to render. Mobile menu behavior, cart drawer interaction, and product-page layout were not present in the supplied evidence.
