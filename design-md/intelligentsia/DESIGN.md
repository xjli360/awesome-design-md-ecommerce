---
version: alpha
name: "Intelligentsia"
source_url: "https://intelligentsia.com"
captured_at: "2026-09-29T04:00:30.301967+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Intelligentsia's storefront CSS shows a warm, editorial palette built around a near-black ink (#2e2925) for body copy and default button fills, a saturated red (#d42927) reserved for primary calls-to-action, and soft cream/parchment surfaces (#faf6f2, #fcf4ed) that suggest a paper-like, coffee-bag aesthetic against a plain white canvas. Typography splits cleanly by role: rotunda-variable (with sans-serif fallback) sets running body text, while urw-din (with sans-serif fallback) drives headings and all button labels, giving a condensed, confident display voice against a humanist reading face. Muted taupe tones (#7c6e65, #92867e) and a light hairline gray (#e0e0e0) appear in disabled and secondary-label states, indicating a restrained secondary palette rather than bright accents. Other palette values (yellows, teals, deep reds) appear in the extracted swatch list but have no confirmed selector role in the supplied CSS, so they are treated here only as optional, inferred accent candidates for badges or seasonal callouts. This interpretation extends the two confirmed button treatments (solid ink, solid red) into a fuller system — cards, nav, forms, hero, footer — using only the observed hex values and font stacks, with layout, spacing, and radii proposed rather than measured.

colors:
  primary: "#d42927"
  primary-hover: "#2e2925"
  ink: "#2e2925"
  canvas: "#ffffff"
  body: "#2e2925"
  muted: "#7c6e65"
  hairline: "#e0e0e0"
  surface-soft: "#faf6f2"
  surface-card: "#fcf4ed"
  on-primary: "#ffffff"
  disabled-bg: "#e0e0e0"
  disabled-text: "#92867e"
  disabled-text-alt: "#666360"
  border-secondary: "#2e2925"
  accent-warm: "#f9bf3a"
typography:
  display-xl: {fontFamily: "urw-din, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "urw-din, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "urw-din, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "rotunda-variable, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "rotunda-variable, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "rotunda-variable, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "urw-din, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 18px, letterSpacing: 0.5px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.border-secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** reflects the confirmed `.btn--primary` rule: red fill, white text, with a documented hover state that swaps to the ink color rather than a red tint — this hover behavior is directly observed in the CSS. **button-secondary** mirrors `.btn--secondary`: transparent background, ink border and text, inverting to a solid ink fill on hover/focus, also directly observed. **text-input** is proposed; no input styling was supplied, so border, radius, and padding follow the site's flat, square-cornered button aesthetic (`border-radius:0` on buttons) as a stylistic cue rather than a measured field. **nav-bar** is inferred from the header markup structure (logo, primary nav, cart, search) described in the page text, using canvas background and ink text consistent with body defaults; no header CSS rules were supplied. **product-card** and **subscription-card** are proposed compositions built to house the "Shop All Coffee" and "Customize / Edit Anytime / Enjoy" subscription content blocks named in the page text, using the cream surface tones observed in the palette. **hero** is proposed as a dark, full-bleed ink section for the "Explore the world through coffee" banner language, using the display typography scale inferred from the `h1–h6` `urw-din` rule. **footer** uses the ink background/white text pairing by analogy with the hero, sized for the extensive link list (About, Wholesale, Help, legal links) present in the page text; the actual footer background color was not supplied. **badge** and **search** are proposed utility components: badge borrows the palette's warm yellow swatch (`#f9bf3a`), whose functional role is unconfirmed, as a plausible "New" or "Seasonal" tag color; search follows the flat input treatment used for text-input.

## Responsive Behavior
The following breakpoint table is a recommendation only; no responsive CSS or viewport behavior was supplied in the evidence.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | <600px      | Single-column stacking; nav collapses to a hamburger/drawer implied by "Open Navigation / Close Navigation" strings in page text. |
| tablet    | 600–1024px  | Two-column product grids; sticky simplified header. |
| desktop   | >1024px     | Full horizontal nav with dropdown submenus (Coffee, Goods, Subscribe, etc., as named in page text). |

Touch targets on mobile should be at least 44px tall, matching the padding proposed for `button-primary`/`button-secondary`. Cart and search overlays (referenced in the page text as "Your Cart," "Search coffee, etc…") are assumed to render as full-screen or slide-in panels on small viewports, but this is not confirmed by any supplied layout CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from a static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Several palette colors (e.g. `#ec4442`, `#cc2027`, `#f9bf3a`, `#1990c6`, `#2e8b57`) appear in the raw swatch list without an attached selector, so any use of them here (such as `accent-warm`) is explicitly inferred, not confirmed. Font availability, licensing, and variable-font axes for `rotunda-variable`, `urw-din`, `alternate-gothic-atf`, and `mixta-pro` were not verified — they are third-party/foundry fonts referenced by class names only. All spacing values, border radii, breakpoints, and component paddings are proposed design defaults, not measurements taken from the live site. Mobile navigation, cart-drawer, and search-overlay interaction patterns are named in the extracted page text but their visual/motion behavior was not observed. No product photography, imagery treatment, or grid measurements were available in the supplied evidence.
