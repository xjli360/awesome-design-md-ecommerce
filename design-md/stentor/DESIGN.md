---
version: alpha
name: "Stentor"
source_url: "https://www.stentor-music.com"
captured_at: "2026-09-28T04:09:23.294049+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Stentor's public stylesheet is a stock Bootstrap 2.x build: a 14px Helvetica
  Neue/Helvetica/Arial sans-serif body at 20px line-height, bold heading
  weights inheriting body color, and a muted #999999 used for de-emphasized
  small text. The palette is dominated by Bootstrap's default UI system
  colors — near-white surfaces (#ffffff, #f9f9f9, #f5f5f5), mid-grey borders
  (#cccccc, #dddddd), dark body ink (#333333), plus the stock alert/button
  accent set (blue #0088cc, orange #f89406, green #62c462, red #ee5f5b,
  info #5bc0de). None of these read as a bespoke Stentor brand identity;
  they are inferred as functional UI tokens rather than confirmed brand
  marks. This interpretation treats #0088cc as the primary interactive
  color (the only saturated hue tied to link/button conventions in the
  observed CSS), #333333 as body ink, and the grey/white surface family as
  the structural backbone for a catalog-style layout suited to browsing
  instrument families (violin, viola, cello, bass). Accent colors are
  retained for status/badge use only, not for primary branding, since no
  logo or hero-specific color evidence was supplied.

colors:
  primary: "#0088cc"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  accent-warm: "#f89406"
  success: "#62c462"
  danger: "#ee5f5b"
  info: "#5bc0de"
  border-light: "#dddddd"
typography:
  display-xl: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 20px, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 20px, letterSpacing: 0px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-light}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  family-nav:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** uses the sole saturated brand-adjacent hue (#0088cc) against white text, matching Bootstrap's default link/anchor color convention; proposed as the main call-to-action for dealer/retailer or catalog actions.

**button-secondary** mirrors the observed `.btn` gradient-free flat state (#f5f5f5 background, #ccc-family border) for lower-emphasis actions like "view range" or "download catalog."

**text-input** is proposed from the shared `input,button,select,textarea` font-family rule; border and radius are inferred defaults since no form-field CSS was supplied.

**nav-bar** is proposed as a light, bordered horizontal bar for top-level navigation across instrument families (Violin / Viola / Cello / Bass); no header markup was observed, so structure is inferred.

**product-card** (instrument listing) uses the striped-table surface tone (#f9f9f9) as a card background with a hairline border, suited to grid displays of instrument models and student/intermediate/professional tiers.

**family-nav** is the category-specific component for Stentor's instrument-family browsing (strings by type and level), styled as a soft-grey pill/tab row; entirely proposed, not observed in markup.

**hero** is proposed as a dark full-bleed introductory band using the darkest observed neutral (#222222) for contrast with white display type; no hero section markup was supplied as evidence.

**footer** reuses the dark ink tone with muted (#999999) secondary text, echoing the `h6 small { color:#999 }` de-emphasis pattern seen in the base stylesheet.

**badge** repurposes the Bootstrap info blue (#5bc0de) for small status labels (e.g., "New," "Outfit"), rounded fully; a proposed, non-branded utility pattern.

**search** follows the same bordered, flat-surface treatment as text-input, proposed for a product/model-number lookup field appropriate to a catalog site.

## Responsive Behavior

Recommendation only — no responsive behavior was observed in the supplied evidence.

| Breakpoint | Width      | Layout guidance (proposed) |
|-----------|------------|------------------------------|
| Mobile    | <576px     | Single-column stack, nav collapses to a toggled menu |
| Tablet    | 576–991px  | Two-column product grids, family-nav becomes horizontal scroll |
| Desktop   | ≥992px     | Multi-column grids, persistent nav-bar |

Touch targets should be at least 40px tall (spacing.xl-adjacent) for buttons and nav items; collapse pattern for nav-bar is a standard hamburger/disclosure proposal, not confirmed from markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS text and a color/font inventory; no rendered page, DOM, or interaction states were observed. The color palette is Bootstrap 2.x's default UI/alert system, so brand-specific hue assignments (primary, accent-warm) are inferred rather than confirmed against an actual logo or hero image. Font sizes beyond the observed 14px/20px body pair (display, title, caption scales) are proposed design values, not measured. No hover/focus/active states beyond the generic `.btn:hover` gradient shift were evidenced, and no mobile navigation, modal, or form validation behavior was captured. Font Awesome icon families are present in the evidence but their usage context on-page is unknown. Licensing and web-font availability for "Helvetica Neue" are not verified; system fallbacks (Helvetica, Arial, sans-serif) should be assumed the practical rendering path.
