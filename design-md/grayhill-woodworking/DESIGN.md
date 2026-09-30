---
version: alpha
name: "Grayhill Woodworking"
source_url: "https://grayhillwoodworkingllc.com"
captured_at: "2026-09-28T09:13:34.317603+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed palette is entirely neutral/grayscale — no chromatic brand
  color was present in the supplied evidence (#222222, #333333, #666666,
  #aaaaaa, #dddddd, #f5f5f5, #ffffff). This interpretation treats the
  darkest neutral, #333333, as the primary action color (inferred role,
  since no accent hue exists in the source), reserving #222222 for
  highest-contrast headings/ink and #666666 for secondary body copy.
  #f5f5f5 and #ffffff distinguish soft section backgrounds from card
  surfaces, #dddddd serves as the hairline/divider tone, and #aaaaaa is
  reserved for placeholder or disabled-state text — an inferred,
  unobserved-in-context mapping.

  Typography pairs Gilda Display, a serif with classical proportions
  suited to an artisanal, handcrafted-goods brand, for headlines and
  product names, with PT Serif for body copy, labels, and UI text — both
  observed font families, generic serif fallbacks applied. The overall
  interpretation leans toward a quiet, gallery-like presentation: warm
  neutral surfaces, thin hairlines, generous spacing, and restrained
  typographic contrast that lets photography of turned-wood pieces and
  natural grain carry the visual weight. No layout, spacing, or
  interaction states were observed directly; all sizing and component
  behavior below are proposed conventions consistent with the supplied
  evidence.

colors:
  primary: "#333333"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  subtle: "#aaaaaa"
typography:
  display-xl: {fontFamily: "'Gilda Display', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  display-md: {fontFamily: "'Gilda Display', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Gilda Display', serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'PT Serif', serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'PT Serif', serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "'PT Serif', serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'PT Serif', serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.subtle}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  custom-order-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"

## Components

**button-primary** anchors calls to action such as "Shop the Latest Creations" and "Design Your Dream Piece." It uses the darkest neutral as an inferred primary fill with white text; hover/active states were not observed and are proposed as a modest darken or opacity shift.

**button-secondary** provides an outlined alternative for lower-emphasis actions (e.g., "Read more →" links styled as buttons), keeping the same ink tone for border and label so it reads as a quieter sibling to the primary button.

**text-input** covers newsletter, contact, and custom-order form fields. A light hairline border and white surface keep forms visually calm; focus-state styling (e.g., border darkening) is proposed, not observed.

**nav-bar** represents the top utility/menu bar implied by the "Home / Shop / Gift Guide / About" navigation list. A white background with a thin hairline divider separates it from page content; mobile collapse behavior is inferred, not measured.

**product-card** models the repeating shop-grid items seen in the text excerpt (turned-wood vases, boxes) — title in the display serif, price and dimensions in body/caption weights, on a white card with a light hairline edge to keep focus on product photography.

**hero** reflects the homepage introductory section ("Bridging Artistry & Sustainability…") with a soft neutral background, large serif headline, and supporting body copy; exact height and image treatment are proposed conventions.

**footer** groups secondary links (Testimonials, FAQ, Shows & Events) implied by the site menu, using muted text on a soft surface to sit visually beneath primary content.

**badge** supports small trust markers referenced in the text — "Sustainably Sourced," "Made in New Jersey," "Family-Owned Business" — as pill-shaped neutral chips.

**search** is a proposed pattern for product discovery within the Shop section; no search UI was directly observed, so styling follows the same neutral, hairline-bordered convention as other inputs.

**custom-order-cta** is a category-specific component for the "Design Your Dream Piece" custom-commission flow distinctive to bespoke woodworking, using the darkest ink tone as a contrasting panel to separate commission requests from standard shop browsing.

## Responsive Behavior

Recommended, unmeasured breakpoints: mobile ≤480px (single-column product grid, nav collapses to a hamburger menu implied by the "Open Menu/Close Menu" labels in the source), tablet 481–1024px (two-column product grid), desktop ≥1025px (three- to four-column grid, persistent nav). Touch targets should be at least 44×44px for menu items and buttons. This table is a design recommendation only and does not reflect measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static text/CSS evidence only; no rendered layout, computed styles, spacing, or breakpoints were observed. The single non-neutral role (primary) is an inferred substitution from a grayscale palette — no accent/brand hue was present in the supplied colors. Component states (hover, focus, active, disabled), responsive collapse behavior, and actual grid structure are proposed, not verified. Font availability, licensing, and exact weights for Gilda Display and PT Serif were not verified beyond their names appearing in the supplied evidence. All pixel sizes in typography, spacing, and rounded scales are proposed conventions unless explicitly present in supplied CSS, which contained no rules in this evidence set.
