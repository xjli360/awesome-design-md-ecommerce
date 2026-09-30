---
version: alpha
name: "Burlap & Barrel"
source_url: "https://burlapandbarrel.com"
captured_at: "2026-09-28T04:32:13.044446+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Burlap & Barrel positions itself as a premium single-origin spice brand, and the
  extracted evidence supports a warm, editorial identity built on a deep maroon
  (#7f2629, with a darker hover/shade at #781c1f) as the inferred primary brand
  color, paired with a warm off-white (#f9f8f4) and clean white (#ffffff) for
  content surfaces. A muted slate (#3d4246) is the observed header text color,
  with a mid-gray (#777777) used as a documented header accent, and a light
  gray (#ececed) reserved for the search field background per the site's own
  CSS custom properties. An orange pairing (#f6a430 / #e88800) appears in the
  palette and is inferred here as a spice-toned secondary accent for badges or
  highlights, while #a2252a offers a brighter red for emphasis states.
  Typography evidence shows Poppins (sans-serif) alongside a serif labeled
  "Recoleta DEMO," which this document interprets as the display/heading face
  for editorial warmth, with Poppins carrying UI and body text. A third family
  group, "Monthoers," appears in the CSS but its role, licensing, and rendering
  are unverified and are treated as decorative/unused pending confirmation.
  Hero and slideshow markup (Flickity-based) with transparent, white-bordered
  buttons is directly observed and informs the hero component below; all other
  layout, spacing, and interaction states are proposed interpretations, not
  measured observations.

colors:
  primary: "#7f2629"
  primary-hover: "#781c1f"
  accent: "#f6a430"
  accent-dark: "#e88800"
  highlight: "#a2252a"
  ink: "#121212"
  body: "#3d4246"
  muted: "#777777"
  canvas: "#ffffff"
  surface-soft: "#f9f8f4"
  surface-alt: "#f5f5f5"
  surface-card: "#ffffff"
  hairline: "#e6e6e6"
  search-bg: "#ececed"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Recoleta DEMO', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Recoleta DEMO', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Poppins', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Poppins', sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Poppins', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Poppins', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "'Poppins', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    accentColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlayColor: "#0000001a"
    ctaComponent: "button-secondary"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.search-bg}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  origin-badge:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** is proposed as the solid-fill call-to-action (e.g. "Shop Now," "Add to Cart") using the inferred maroon primary against white text; hover/active states are not observed and would proposed-darken toward `{colors.primary-hover}`.

**button-secondary** mirrors the transparent, white-bordered button style directly observed on hero slide markup (`#DP--slide_* .dsgn-pck__button`), with a thin `1px` border, transparent background, and a subtle `rgba(255,255,255,0.1)` hover fill confirmed in the supplied CSS — this pattern is grounded, though its exact use outside the slider is proposed.

**text-input** is proposed for search and form fields, reusing the observed `--search-bg-color: #ececed` token from the header's CSS custom properties as its resting background.

**nav-bar** reflects the `.header` block's own CSS variables almost verbatim: white background, slate-gray text (#3d4246), and a documented `--header-accent-color: #777777`, giving high confidence to this mapping relative to other proposed components.

**hero** is inferred from the presence of Flickity-based slideshow markup (`.flickity-button`, `.dsgn-pck__inner-content--slideshow`) with dark imagery implied by white text/button treatments; exact imagery, copy, and slide count are not observed.

**product-card** is a fully proposed pattern appropriate to a spice e-commerce catalog, using a white surface, light hairline border, and the title/body type pair for product name and short description.

**footer** is proposed using the warm off-white surface (#f9f8f4) to visually distinguish it from the pure-white header/body, with hairline dividers between link columns.

**badge** and **origin-badge** are category-specific proposals: a general accent-colored pill (e.g. "As Seen on Shark Tank") using the orange accent, and a single-origin country/flavor tag using an outlined primary style, reflecting Burlap & Barrel's single-origin sourcing narrative implied by the page title.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column stacking; nav collapses to a hamburger/off-canvas menu |
| Tablet | 600–959px | Two-column product grids; hero retains full-bleed slideshow |
| Desktop | ≥960px | Multi-column grids; persistent horizontal nav |

Touch targets should measure at least 44×44px for buttons and nav items; search and form inputs should retain a minimum 40px height. This table and its guidance are recommendations for implementation and are **not** derived from measured responsive behavior of the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered screenshots, computed styles, or DOM layout were observed, so actual spacing, grid structure, and breakpoints are proposed, not measured. Several CSS declarations in the source evidence contained empty or templated values (e.g. blank `color:`/`background-color:` on `.dsgn-pck__button`, and an incomplete `border-radius: px;`), meaning real button colors and corner radii could not be confirmed and are treated as inferred design choices. Semantic color-to-role mapping (e.g. which hex is "primary" vs. accent) is inferred from frequency and context, not from labeled design tokens. The "Monthoers" font family group appears in the CSS but its intended usage, rendering, and licensing status are unverified and are excluded from the proposed type scale. "Recoleta DEMO" is explicitly a demo build and its production licensing is unconfirmed. No interaction states (hover/focus/active beyond the one observed slideshow-button hover), mobile menu behavior, or cart/checkout flows were observed. Social-icon brand colors (e.g. Facebook blue, Instagram gradient) present in the raw palette were excluded from design tokens as third-party icon colors rather than brand palette.
