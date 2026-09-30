---
version: alpha
name: "Health-Ade"
source_url: "https://health-ade.com"
captured_at: "2026-09-29T04:10:06.548961+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Health-Ade's storefront CSS exposes a navy-on-white brand core: root
  variables set `--color-foreground`, `--color-button`, and `--color-link`
  to rgb(0,31,92) — hex #001f5c — against a white (#ffffff)
  `--color-background`, with button text set to a near-white. This navy is
  treated here as the primary brand color and is reused for ink, links, and
  primary actions. Two proprietary display faces, GT-Flexa-Cond-Medium and
  GT-Flexa-Cond-Regular, are confirmed in use on `.learn-link`/
  `.product-category-link` title and description elements, with explicit
  22px/14px sizes; these are adopted as the heading and small-label
  families. Body copy inherits a Shopify theme variable
  (`--font-body-family`) whose resolved value wasn't captured, so the
  Bootstrap-loaded system sans stack (-apple-system, Segoe UI, Roboto,
  Helvetica Neue, Arial) is used as an inferred fallback, matching the
  observed 1.5rem base size and 0.06rem tracking. A large residual palette
  of Bootstrap defaults (grays, blues, semantic reds/greens/yellows) is
  present from a loaded bootstrap.min.css and is treated as
  framework-inherited rather than confirmed brand color; a small set of
  non-Bootstrap hexes (#bc5631, #18566c, #8cd5fb, #e83e8c) stands out as
  likely flavor/illustration accent colors and is mapped as such, inferred.

colors:
  primary: "#001f5c"
  ink: "#001f5c"
  canvas: "#ffffff"
  body: "#495057"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#ced4da"
  accent-terracotta: "#bc5631"
  accent-teal: "#18566c"
  accent-sky: "#8cd5fb"
  accent-pink: "#e83e8c"
  success-soft: "#b1dfbb"
  danger-soft: "#f1b0b7"
typography:
  display-xl: {fontFamily: "GT-Flexa-Cond-Medium, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GT-Flexa-Cond-Medium, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: normal}
  title-md: {fontFamily: "GT-Flexa-Cond-Medium, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: normal, letterSpacing: normal}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "GT-Flexa-Cond-Regular, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: normal}
  caption: {fontFamily: "GT-Flexa-Cond-Regular, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "GT-Flexa-Cond-Medium, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.04em}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeColor: "{colors.accent-terracotta}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** maps to the navy `--color-button` variable seen at the
root, with a near-white text color; this is the highest-confidence
component since both values come directly from CSS custom properties.

**button-secondary** is a proposed outline/ghost variant using the same
navy on a white fill, inferred from the `--color-secondary-button` /
`--color-secondary-button-text` pair present in the root variables, which
swap background and foreground relative to the primary button.

**text-input** is a proposed form field style using the Bootstrap-derived
hairline gray for its border, since no dedicated input CSS was captured;
its exact focus/error states are not observed.

**nav-bar** is inferred from the presence of "Shop," "Learn," and "Rewards"
menu text in the page copy alongside `.learn-link`/`.product-category-link`
title typography; the 22px medium-weight label style is applied here as
the nav's dropdown-category heading style, though the nav's own container
CSS was not directly captured.

**product-card** is proposed for the kombucha 12-pack tiles referenced in
the page text (variety packs, prices, "Add To Cart"); card chrome
(background, border, radius) is inferred defaults, not measured, since no
`.product-card`-style selector was supplied.

**hero** is proposed for the "Your New Favorite Kombucha" flavor-launch
section, using the light neutral surface and display type; background and
exact padding are inferred, not observed.

**footer** is a proposed navy-fill footer, reusing the primary brand color
inverted, consistent with the site's link/button color reuse pattern; no
footer-specific selector was present in evidence.

**badge** is proposed for callouts like "Organic," "Non-GMO," "Gluten
free," and "Vegan" mentioned in the page text; pill shape and outline style
are inferred, not confirmed by CSS.

**search** is proposed for the header "Search" affordance mentioned in
content; styling is inferred from generic input conventions, not captured
CSS.

**subscription-toggle** is a category-appropriate proposed component for
the observed "One-Time Purchase" vs. "Subscribe & Save (15%)" pricing
toggle seen in the page copy; it borrows the terracotta accent as an active
state, which is an inferred, unverified color role.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| xs | <576px | Single-column product grid, stacked nav collapses to hamburger, hero text left-aligned. |
| sm | 576–767px | 2-up product cards, subscription toggle stacks below price. |
| md | 768–991px | 2–3 up product grid, nav shows top-level items with dropdown menus. |
| lg | 992–1199px | Full horizontal nav, 3–4 up product grid, hero side-by-side. |
| xl | ≥1200px | Max-width content container, 4-up grid, generous section spacing. |

Breakpoint values reuse Bootstrap's default `--breakpoint-*` variables
found in evidence (576/768/992/1200px) but the actual responsive grid,
collapse behavior, and touch targets were not measured on the live site.
Touch targets for buttons/badges should target a minimum 44px hit area per
common accessibility guidance; this is a recommendation only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live
rendering, computed styles, or DOM screenshots were available. The
resolved value of `--font-body-family` was never observed, so the
Bootstrap system-font stack is used as an inferred stand-in for body copy.
GT-Flexa-Cond-Medium/Regular availability, licensing, and full weight
range are unverified — only 500-weight medium and one regular usage were
seen. Most neutral grays (e.g., #6c757d, #dee2e6, #f8f9fa) originate from a
loaded Bootstrap stylesheet and may not reflect intentional brand choices
versus unused framework defaults. The four non-Bootstrap accent hexes
(#bc5631, #18566c, #8cd5fb, #e83e8c) are assumed brand/illustration accents
but their actual usage context (flavor labels, blob shapes, etc.) was not
directly confirmed against a specific selector. All component paddings,
radii, breakpoints, and hover/focus/error states are proposed design
conventions, not measured site behavior, and mobile layout/interaction was
not observed in any form.
