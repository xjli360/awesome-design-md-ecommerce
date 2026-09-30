---
version: alpha
name: "Tektronix"
source_url: "https://www.tek.com"
captured_at: "2026-09-28T04:04:24.972772+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed evidence shows a technical, engineering-grade palette anchored by a
  deep teal-blue (#035e7c) used as the default button background, paired with a
  brighter cyan (#1cb5d8) that appears on hover states and bullet glyphs. A lime
  green (#73bf44) marks promotional "NEW!" labels and a green CTA border/button,
  while a darker olive-green (#a5ce39) appears only on active button text,
  suggesting a secondary accent for pressed/interactive states. Neutrals range
  from near-black (#0f1b24, #17222c) through mid grays (#666666, #758491,
  #8899a8) to light surfaces (#f5f5f5, #f9f9f9, #ffffff), consistent with a dense,
  data-oriented industrial site. Button typography uses Helvetica Neue/Helvetica/
  Arial with uppercase, letter-spaced, small (12px) labels and pill-shaped
  (20px radius) corners — this is an observed pattern, not merely presence.
  Monospace families (Consolas, Courier New, Fira Code, Source Code Pro) are
  present in the evidence and are interpreted here as inferred usage for
  code/command or measurement-readout contexts typical of test-and-measurement
  documentation, though no such component was directly observed. Semantic color
  roles below (ink, muted, hairline, surface tiers) are inferred groupings of the
  observed neutral palette, not confirmed design-token names from the source.

colors:
  primary: "#035e7c"
  primary-hover: "#1cb5d8"
  accent-green: "#73bf44"
  accent-green-active: "#a5ce39"
  ink: "#17222c"
  ink-deep: "#0f1b24"
  body: "#333333"
  muted: "#666666"
  muted-cool: "#758491"
  slate: "#8899a8"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#f9f9f9"
  surface-tint: "#edf6fb"
  on-primary: "#ffffff"
  disabled-bg: "#cccccc"
  disabled-text: "#000000"
  danger: "#b30000"
  alert-orange: "#f05a22"
  active-dark: "#353b43"
typography:
  display-xl: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.6px}
  code-md: {fontFamily: "Consolas, Fira Code, Source Code Pro, Courier New, monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.accent-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
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
    hoverBackground: "{colors.primary}"
    hoverText: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-soft}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.primary-hover}"
    displayTypography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.slate}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted-cool}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-readout:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.code-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"

## Components

**button-primary** reflects the directly observed `.btn` rule: a teal (#035e7c) pill
button with white uppercase text, 20px border-radius, and a cyan (#1cb5d8) hover
background paired with dark-ink text — this hover color swap is observed in the
supplied CSS. **button-secondary** is a proposed lighter-weight action using the
green outline pattern seen on `.btn-buy-now-exp`, filling solid green on hover
(proposed hover state, not shown in evidence for this exact class). **text-input**
is a proposed pattern inferred from general form conventions; no input-field CSS
was supplied. **nav-bar** draws on the `header--redesign` selectors showing a
white/teal hover treatment on submenu links; overall nav layout is inferred.
**product-card** is a proposed container for equipment listings, using the
lighter card surface and soft hairline border consistent with the neutral
palette. **hero** is a proposed full-bleed introductory band using the darkest
observed ink tone with the cyan accent for emphasis text; no hero markup was in
the evidence. **footer** is proposed, using the darker ink neutral with muted
slate-gray links, consistent with the site's dark-on-light neutral system.
**badge** models the observed "NEW!" green label pattern from the nav-item
pseudo-element rule. **search** is a proposed rounded search field using the
soft surface tone. **spec-readout** is an inferred, category-appropriate
component for displaying instrument specifications or command syntax using the
monospace font stack found in the evidence, styled with the tinted blue surface
color; its visual treatment is proposed, not observed.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | 0–599px   | Single column, nav collapses to hamburger, buttons full-width where primary |
| tablet    | 600–959px | Two-column product grids, nav condenses submenus |
| desktop   | 960–1279px| Full nav bar, multi-column grids |
| wide      | 1280px+   | Max-width container, generous section spacing |

Touch targets should be at minimum 44x44px for primary buttons and nav items
(proposed guidance). Navigation and submenu collapse behavior, hover-to-tap
conversion, and mobile menu structure are not observed in the supplied evidence
and are proposed based on common patterns for dense technical sites.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static, partial CSS/color extraction and does
not reflect live rendering, JavaScript-driven states, or full stylesheet
coverage. Several semantic role assignments (ink, muted, hairline, surface
tiers) are inferred groupings of the observed neutral palette rather than
confirmed token names from Tektronix's source. Font sizes, spacing scale, and
border-radius values beyond those explicitly present in the `.btn` rule (12px
text, 20px radius) are proposed defaults, not measured. Hero, footer, nav
collapse, product-card, search, and spec-readout components are proposed
interpretations for a measurement-instrument brand and were not directly
observed in markup or layout. The custom `tek` icon font referenced in the
evidence is an icon glyph font, not a text typeface, and its availability,
licensing, and character set were not verified. Mobile/responsive layout,
interaction states beyond the documented button hover/active rules, and any
JavaScript-driven behavior are not observed and remain assumptions for future
verification against the live site.
