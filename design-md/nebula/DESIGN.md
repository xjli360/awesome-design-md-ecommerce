---
version: alpha
name: "Nebula"
source_url: "https://seenebula.com"
captured_at: "2026-09-28T04:55:45.938068+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from CSS captured across soundcore.com's Nebula
  projector storefront, a subline of Anker's unified soundcore brand. The
  observed palette centers on a cyan-blue brand accent (#17bbef, reinforced by
  a near-identical --btn-bg-active-color of #00a7e1) set against a near-black
  ink (#1d1d1f) and white canvas, with layered neutral surfaces (#f5f6f7,
  #eaeaec, #f7f8f9) used for cards and section backgrounds. Hairlines and
  muted text draw from the grayscale run (#dddddd, #999999, #767880, #86868c).
  Status colors (success #3adb67, error #ff4d4d) appear in the CSS variable
  set and are retained here as inferred badge/alert accents rather than
  confirmed UI states.
  Typography uses the brand-licensed "Mont"/"MontForAnker" family for display
  and heading roles, falling back to Nunito Sans and system sans-serif stacks
  for body copy, matching the observed font-family declarations. Radius
  tokens draw directly from :root variables (--box-radius:16px,
  --box-radius-small:8px), while pill-shaped buttons are inferred from the
  24px --btn-radius and circular icon buttons (border-radius:50%). Layout
  proportions, spacing scale, and responsive breakpoints are proposed
  conventions for a projector/TV storefront, not measured from a live
  viewport, and are labeled accordingly throughout.

colors:
  primary: "#17bbef"
  ink: "#1d1d1f"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767880"
  hairline: "#dddddd"
  surface-soft: "#f5f6f7"
  surface-card: "#f7f8f9"
  on-primary: "#ffffff"
  accent-alt: "#00a9e1"
  ink-deep: "#080a0f"
  surface-dark: "#1e2024"
  success: "#3adb67"
  error: "#ff4d4d"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Mont, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Mont, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Mont, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Mont, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-compare-table:
    backgroundColor: "{colors.surface-card}"
    hairline: "{colors.hairline}"
    headerTypography: "{typography.title-md}"
    cellTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** renders the cyan brand accent (#17bbef) as a filled, fully-rounded pill, matching the observed --btn-radius:24px variable and --btn-bg-active-color token. Used for "Buy Now" and primary CTAs; hover/pressed states are proposed, not observed.

**button-secondary** is an outlined variant on the same pill shape, using the ink color for text and a hairline border, intended for "Learn More" or filter-toggle actions alongside primary CTAs.

**text-input** covers search fields and any form controls (e.g., email capture); rounded.sm and a hairline border are proposed defaults since no explicit input CSS was captured.

**nav-bar** reflects the flat white header pattern implied by the category navigation list (Headphones, Earbuds, Speakers, Projectors, etc.); a bottom hairline separates it from page content, consistent with the --stroke-primary-color pattern in the variable set.

**product-card** is the repeating unit for the 31-item Nebula projector grid, using the 16px --card-radius observed in :root and a light card surface distinct from the page's off-white background, holding a title, price (with strike-through original price implied by "$X OFF" badges), and CTA.

**hero** is a dark, full-bleed banner (e.g., "Meet the New Nebula X1S") using the darkest observed neutral (#080a0f) as background, sized for the large display-xl typography scale; exact hero height/imagery is not observed.

**footer** uses a dark surface tone (#1e2024) distinct from the hero, for utility links and legal text at body-sm scale; column layout is proposed, not measured.

**badge** models the recurring "$X OFF," "New Release," and "Recommended" labels seen throughout the product listing; color choice (error red) is one inferred option among the palette's small accent set — actual badge colors per label were not distinguished in the evidence.

**search / category filter** reflects the "Shop by Price," "Category," and "Sort by" controls described in the page text; rendered as a pill-shaped, soft-surface input consistent with the neutral surface tokens.

**spec-compare-table** is a category-specific addition for TVs & Projectors, proposed to present resolution, laser type, brightness, and battery specs (e.g., 4K vs. 1080p, laser vs. LED) in a bordered, card-radius table, since projector shoppers commonly compare technical specs before purchase.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed nav into a menu icon, sticky "Buy Now" bar |
| tablet | 640–1024px | 2-column product grid, category filters as a horizontal scroll strip |
| desktop | 1024–1440px | 3–4 column product grid, persistent left filter sidebar |
| wide | >1440px | Max content width with additional gutter, unchanged column count |

Touch targets for buttons and filter chips should be at least 44px tall given the pill-shaped button pattern; the category/price filter list likely collapses into an accordion or drawer on mobile. This table is a recommendation based on common e-commerce patterns and the observed component inventory — it is not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions were observed. Font availability for "Mont" and "MontForAnker" is inferred from font-family declarations only — licensing and actual glyph rendering were not verified. Semantic color roles (e.g., which exact hex powers primary buttons vs. active nav states) are inferred from CSS custom-property names and likely reuse; two near-identical blues (#17bbef and #00a9e1) may represent the same brand color at different points in the build. Badge, hero, and footer color assignments are proposed pairings drawn from the available neutral/accent set, not confirmed from screenshots. All spacing and breakpoint values are conventional proposals for e-commerce product-grid patterns and were not measured from the live site.
