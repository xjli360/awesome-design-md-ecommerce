---
version: alpha
name: "DashMat"
source_url: "https://dashmat.com"
captured_at: "2026-09-29T04:21:56.926545+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from CSS and content captured on Covercraft's own storefront category page (covercraft.com/c/dash-covers), which is the current parent-company presentation of the DashMat product line rather than an independent dashmat.com reconstruction. The evidence shows a utilitarian auto-parts commerce UI: Montserrat for product names and dialog headings, with Open Sans/Arial-family fallbacks implied for body copy. The palette is dominated by neutral grays and near-black text (#222222, #212529) on white, with a small set of blues (#0070f2, #167ac6, #1f7bc0) that most plausibly serve as link, primary-action, and info accents, and a red family (#c7000b, #db0002, #ff0000) plausibly reserved for alerts, sale badges, or destructive actions. Green (#38871f) and amber (#ffc107) appear as likely status/success and warning tones. All role assignments (primary vs. accent vs. status) are inferred from typical e-commerce conventions, not confirmed from DashMat-specific brand guidelines. Layout structure (grid columns, breakpoints, hover/focus states) is not observed in the supplied CSS and is proposed here as reasonable defaults for a fitment-driven vehicle-accessory catalog.

colors:
  primary: "#0070f2"
  primary-dark: "#0064d9"
  accent-blue: "#167ac6"
  ink: "#222222"
  body: "#212529"
  canvas: "#ffffff"
  muted: "#6c7079"
  hairline: "#d3d6db"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#38871f"
  warning: "#ffc107"
  info: "#17a2b8"
  danger: "#ff0000"
  danger-deep: "#c7000b"
  badge-bg: "#deeffe"
  badge-warn-bg: "#fff5df"
  badge-danger-bg: "#fff1f1"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 20px, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0.5px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    titleTypography: "{typography.body-sm}"
    ratingTypography: "{typography.caption}"
  vehicle-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.primary-dark}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"

## Components

**button-primary** is proposed for primary calls to action such as "Add to Cart" or "Shop Now," using the strongest observed blue (#0070f2) as background. State-specific hover/active styling was not present in the supplied CSS and is proposed only.

**button-secondary** covers lower-emphasis actions like "Compare" or "View Details," using a hairline border rather than fill so it can sit beside a primary button without competing for attention.

**text-input** models search or fitment-entry fields (year/make/model dropdowns implied by the page text). Border and radius are proposed conventions; no input-specific CSS was captured in evidence.

**nav-bar** represents the top category navigation implied by the "SHOP / SEAT COVERS / CAR COVERS / FLOOR MATS / SUN SHADES / DASH COVERS / CAR BRAS" text list. Visual treatment (background, spacing) is inferred, not measured.

**product-card** is grounded directly in the observed `.custom-product-card` rule: bordered container, Montserrat 700/14px product name, and a smaller caption-weight rating line, matching the `.cx-product-rating` styles in evidence.

**vehicle-selector** is a category-appropriate component reflecting the extensive Year/Make/Model/Category filter UI described in the page text. No layout or interaction CSS was supplied for this control, so its container treatment is proposed.

**hero** proposes a dark banner introducing the DashMat category page, echoing the dark neutrals (#222222, #212529) present in the palette; no hero-specific CSS was in evidence.

**footer** is proposed using the same dark-neutral treatment as hero for visual consistency, since no footer-specific selectors were captured.

**badge** models the small colored labels implied by categorical/status text ("Best," UV Protection, review counts), using the light blue tint (#deeffe) observed in the palette as a plausible badge background.

**search** proposes a pill-shaped search field consistent with the rounded, full-radius styling seen elsewhere in the compare-dialog "remove" control (`border-radius:50%`), generalized here as a soft, rounded search affordance.

## Responsive Behavior

This table is a recommendation only; no live breakpoint or resize behavior was observed in the supplied static CSS.

| Breakpoint | Width      | Layout notes (proposed)                         |
|-----------|------------|--------------------------------------------------|
| mobile    | < 600px    | Single-column product grid; nav collapses to menu |
| tablet    | 600–959px  | 2-column product grid; vehicle-selector stacks    |
| desktop   | 960–1279px | 3–4 column product grid; inline filter sidebar    |
| wide      | ≥ 1280px   | 4+ column product grid; persistent sidebar filters |

Touch targets should be at least 44×44px for buttons and filter chips. Filter/category navigation is proposed to collapse into an accordion or drawer below tablet width. None of this collapse or touch behavior was measured on the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is drawn from a static CSS/content capture of Covercraft's parent-site DashMat category page, not from dashmat.com itself; this is explicitly a parent-site presentation, not a reconstruction of a former independent DashMat site.
- No hover, focus, active, or disabled interaction states were observed; all such states in this spec are proposed conventions.
- No responsive/mobile layout, breakpoint values, or collapse behavior were present in the supplied CSS; the responsive table above is a recommendation only.
- Role assignments for colors (e.g., which blue is "primary" vs. "info," which red is "danger" vs. brand accent) are inferred from common e-commerce patterns, not confirmed from a DashMat style guide.
- Several typography sizes (display-xl, display-md, title-md, body-md) are proposed defaults, not values captured directly from the supplied CSS; only body-sm (14px/700/Montserrat) and caption-scale rating text (10–12px) are directly evidenced.
- Availability, licensing, and web-font delivery of Montserrat and Open Sans for DashMat specifically were not verified; system font fallbacks are included per best practice.
- Component structures (hero, footer, search, vehicle-selector) are proposed based on page-text content and general category conventions, since no corresponding CSS selectors for these regions were supplied.
