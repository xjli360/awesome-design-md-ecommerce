---
version: alpha
name: "Schlage"
source_url: "https://schlage.com"
captured_at: "2026-09-28T09:19:04.918579+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Schlage's residential site pairs a clinical, safety-grade visual system with warm
  accent color used sparingly for calls to action. The observed CSS is dominated by a
  Bootstrap-derived utility palette (grays, semantic reds/greens/yellows) alongside two
  brand-specific blues: a primary action blue (#0072bc) used on filled CTA buttons and
  a secondary outline blue (#0081c6) used on tertiary buttons, with a deep navy
  (#003767) appearing only on hover states for carousel and tertiary links. Body copy
  renders in the Bootstrap system font stack; brand-authored font families in the
  stylesheets are the Avenir family (Light/Book/Medium/Black variants) and the Stag
  family (Stag Web, Stag-Book, Stag-light, Stag-SemiboldItalic), which are inferred
  here to serve display/heading roles given their distinct naming from the utility
  body stack, though this mapping is not directly confirmed by layout evidence. Buttons
  consistently use full pill radii (40px) per two observed CTA rules, generalized here
  into a `full` token. Card and surface neutrals draw from the Bootstrap gray scale
  (#f8f9fa, #e9ecef, #dee2e6, #ced4da). This interpretation proposes a restrained,
  security-hardware-appropriate system: crisp whites, deep blue actions, and neutral
  gray surfaces, with sizing, spacing, and component states marked proposed where not
  directly measured.

colors:
  primary: "#0072bc"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#0081c6"
  accent-deep: "#003767"
  border-light: "#ced4da"
  surface-alt: "#e9ecef"
  danger: "#dc3545"
  success: "#198754"
  warning: "#ffc107"
  info: "#0dcaf0"
typography:
  display-xl: {fontFamily: "'Stag Web', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Stag Web', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Avenir-Medium', sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Avenir-Book', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Avenir-Book', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Avenir-Light', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Avenir-Medium', sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.primary}"
    hover:
      backgroundColor: "transparent"
      textColor: "{colors.primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
    border: "1px solid {colors.accent}"
    hover:
      backgroundColor: "{colors.accent}"
      textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
    focus:
      border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "proposed: 0 1px 3px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlay: "proposed: rgba(0,0,0,0.35) on image heroes for text contrast"
  footer:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkHover:
      textColor: "{colors.accent}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
  finish-swatch:
    shape: "circle, proposed 32px diameter"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    label: "{typography.caption}"

## Components
**button-primary** is the filled pill CTA seen on homepage promo blocks (`#pt .cta-button`), using the brand primary blue with a matching border and full pill radius; hover inverts to an outline treatment per the observed `:hover` rule.

**button-secondary** mirrors the `#cta2 .btn` pattern: an outlined pill button in the lighter accent blue that fills solid on hover. Proposed as the secondary action style for less prominent CTAs like "Learn More."

**text-input** is a proposed pattern for search and form fields, using Bootstrap-derived neutral border and focus-to-primary border color; no live form screenshots were available to confirm padding or focus ring.

**nav-bar** is inferred from the presence of a persistent product/style/support menu structure in the page text (All Products, Style, Support); visual treatment (white background, hairline bottom border) is proposed, not measured.

**product-card** models the repeating "Shop Smart Locks" / "Shop Handlesets" carousel items (product name, trim, "From $" price) evident in the page text; card chrome (border, radius, shadow) is proposed since no card-specific CSS was supplied.

**hero** represents the rotating homepage banner ("Introducing Sense Pro™," "Simplicity has arrived") implied by carousel copy and the `.aplus__carousel` / `#carousel` selectors; overlay and exact type scale are proposed.

**footer** uses the deep navy (#003767) observed only as a hover background, repurposed here as a plausible footer/dark-section color per common hardware-brand footer conventions; this mapping is inferred, not confirmed.

**badge** is a proposed component for labeling new/limited releases (e.g., "The Aspect Collection" limited release copy), using the warning-yellow token for visibility; no badge-specific CSS was observed.

**search** is proposed for the "Press enter to search" affordance mentioned in page text; exact chrome unmeasured.

**finish-swatch** is a category-appropriate component for the "Shop our best sellers by finish" (Matte Black, Satin Nickel, Aged Bronze, etc.) selector implied by page text; visual form (circle swatches) is proposed, not observed in CSS.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| xs | <576px | Single-column product grids, stacked nav collapses to hamburger (proposed) |
| sm | 576–767px | 2-column product cards |
| md | 768–991px | 2–3 column grids, nav remains collapsed |
| lg | 992–1199px | Full horizontal nav, 3–4 column grids |
| xl | ≥1200px | Max-width content container, 4+ column grids |

Touch targets should be at minimum 44×44px for CTA buttons and finish swatches. Primary nav is assumed to collapse into a drawer/hamburger below `md`, consistent with Bootstrap-based breakpoint conventions found in the shared CSS variables, but this collapse behavior was not directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered screenshots, computed layout, or interaction states were captured. Font-role assignments (Stag Web/Stag-Book for display, Avenir for body) are inferred from naming conventions in the stylesheet, not confirmed heading/body usage in rendered markup. All typography sizes except where noted are proposed, not measured. Component states (hover/focus) beyond the two explicitly supplied button rules are proposed patterns for consistency, not observed CSS. Mobile/responsive layout, nav collapse behavior, and card/grid breakpoints were not observed and are recommendations only. Availability and licensing of the Stag and Avenir font families for web use were not verified from the supplied evidence.
