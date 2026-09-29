---
version: alpha
name: "Kicker"
source_url: "https://kicker.com"
captured_at: "2026-09-28T09:44:23.552267+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The KICKER site runs on a Bootstrap 3 foundation, so the observed palette is dominated by
  Bootstrap's stock utility colors (grays #333/#777/#999, contextual state colors like
  #5cb85c, #337ab7, #f0ad4e, #d9534f, and their state-background tints such as #dff0d8 and
  #f2dede). Layered on top is a small set of brand-distinct values not part of Bootstrap's
  defaults: #ffde00 and #ffd11b (a saturated yellow) and near-black tones (#080808, #222222).
  These are inferred here as KICKER's primary brand accent and ink, since they diverge from
  the surrounding Bootstrap defaults and are the only colors that read as intentional brand
  choices rather than framework scaffolding.

  Typography is anchored by the observed body rule ("Helvetica Neue", Helvetica, Arial,
  sans-serif at 14px/1.4286), while Gotham-Black and Open Sans / Open Sans Condensed appear
  in the font stack without a confirmed selector binding; they are treated as inferred
  display/heading and caption faces respectively, consistent with a performance-audio brand
  wanting a bolder, condensed treatment for headlines and specs.

  The resulting interpretation favors a high-contrast, black/yellow industrial system:
  dark ink surfaces, white/light-gray content panels, and yellow reserved for primary calls
  to action and emphasis, echoing the aftermarket-electronics category.

colors:
  primary: "#ffde00"
  primary-alt: "#ffd11b"
  ink: "#080808"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#080808"
  border: "#cccccc"
  overlay: "#222222"
  info: "#337ab7"
  success: "#5cb85c"
  warning: "#f0ad4e"
  danger: "#d9534f"
  success-bg: "#dff0d8"
  danger-bg: "#f2dede"
typography:
  display-xl: {fontFamily: "Gotham-Black, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Gotham-Black, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.42857143, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans Condensed, Helvetica Neue, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.3px}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    hairline: "{colors.overlay}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    stripeColor: "{colors.surface-soft}"
    hoverColor: "{colors.surface-soft}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components
button-primary uses the inferred brand yellow as its fill with dark ink text for contrast, sized for prominent calls to action like "Shop Now" or "Find a Dealer." button-secondary proposes a dark, ink-filled alternative for lower-emphasis actions such as "Learn More," reusing the same button typography token.

text-input follows Bootstrap's default light-canvas field styling observed in the base stylesheet, with a light gray border and standard body typography; focus/active states are proposed, not observed.

nav-bar is modeled as a dark ink bar given the deep near-black values (#080808/#222222) present in the palette, appropriate for the site's multi-level category navigation (Car Audio, Marine, Powersports, etc.) described in the page text; collapse behavior for the toggle navigation is proposed, not confirmed from static CSS.

product-card is a light card on white canvas with a hairline border, sized to present product name, category, and short spec copy consistent with the deeply categorized product taxonomy (subwoofers, amplifiers, speakers) in the evidence.

hero proposes a dark, full-width band with yellow accent typography for headline moments, reflecting the brand's likely emphasis on bold product imagery; no hero markup was directly observed.

footer is modeled as a dark band matching the nav-bar tone, holding legal links (Privacy Policy, Terms & Conditions, Return and Refund) referenced in the page text, using muted gray body copy against ink.

badge is a small yellow pill for labels such as "New" or category flags, reusing the primary/on-primary pairing; no badge markup was directly observed in the evidence.

search proposes a light, bordered input matching the site's "Search" overlay referenced in the navigation text, using surface-soft background to visually separate it from the page canvas.

spec-table is a category-appropriate component directly grounded in the observed Bootstrap table rules (striped/hover backgrounds, contextual success/info/warning/danger row tints) — well suited to presenting technical specifications (power handling, impedance, dimensions) typical of car-electronics product pages.

## Responsive Behavior
Recommended, not measured: a compact three-tier breakpoint scale — mobile up to 767px (single-column stacks, collapsed nav-bar behind a toggle), tablet 768–1023px (two-column product grids), and desktop 1024px+ (multi-column grids, expanded nav-bar). Touch targets should be at least 44px in height for buttons and nav items; the nav-bar toggle described in the page text ("Toggle navigation") should collapse into a full-height drawer or accordion below the tablet breakpoint. All figures are proposed defaults, not observed from live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and text extraction only; no live rendering, computed layout, or DOM interaction was observed. Font-role bindings (Gotham-Black, Open Sans, Open Sans Condensed to headings/captions) are inferred from the presence of font-family names in the stylesheet, not confirmed selector usage — actual usage, weights, and web-font licensing/availability are unverified. The designation of #ffde00/#ffd11b as "primary brand" color is an interpretive inference based on their divergence from Bootstrap defaults, not a confirmed brand-guideline source. All component states (hover, focus, active, disabled), responsive breakpoints, and mobile navigation behavior are proposed patterns, not measured from the live site. Spacing and rounded-corner scales are conventional proposals, not extracted from observed CSS custom properties.
