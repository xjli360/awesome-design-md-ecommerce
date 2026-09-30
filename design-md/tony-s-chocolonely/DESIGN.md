---
version: alpha
name: "Tony's Chocolonely"
source_url: "https://tonyschocolonely.com"
captured_at: "2026-09-28T09:26:16.024014+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from the site's own CSS custom-property palette,
  which names each hue after a chocolate ingredient (tonys-red, caramel-orange,
  hazelnut-green, pretzel-purple, and so on) — evidence that color is used
  brand-wide to distinguish product variants, not just for UI accents. Tony's
  red (#EB0000) and Tony's blue (#006BE1) are treated as primary/secondary
  brand colors since they lead the token list before the flavor colors; this
  role assignment is inferred from naming order, not a measured layout.
  Tony's yellow (#FFED00) appears in an observed selected-radio-button state,
  so it is kept as an interactive accent. Neutral roles (ink, canvas, muted,
  hairline, soft surface) are drawn from the plain black/white/gray/off-white
  values present in the palette, since no other neutrals were supplied.
  Typography mixes an observed system serif, "American Typewriter" (forced
  with !important in the source, suggesting deliberate brand styling), for
  display and heading roles, with the observed ui-sans-serif/system-ui stack
  for body copy. A custom "Chocolate letter" family is referenced in the
  evidence but its glyph coverage and licensing are unverified, so it is noted
  only as a possible logotype face. Button typography (18px/24px, weight 700)
  and the pill-shaped radius (9999px) come directly from the `.apply-button`
  rules. All other spacing, radii, and component states are proposed
  conventions layered onto this evidence, not observed interactions.

colors:
  primary: "#eb0000"
  secondary: "#006be1"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#9ca3af"
  hairline: "#e5e7eb"
  surface-soft: "#f1f1ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffed00"
  accent-orange: "#ff7400"
  accent-green: "#78c828"
  accent-pink: "#ff60a6"
  flavor-purple: "#6464be"
  flavor-teal: "#00afbe"
  flavor-deep-pink: "#d7005a"
  flavor-lime: "#dce10a"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "'American Typewriter', ui-sans-serif, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'American Typewriter', ui-sans-serif, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'American Typewriter', ui-sans-serif, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "ui-sans-serif, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "ui-sans-serif, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "ui-sans-serif, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "ui-sans-serif, system-ui, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 24px, letterSpacing: 0px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  button-round:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: "28px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  flavor-swatch:
    shape: "{rounded.full}"
    size: "16px"
    colors: ["{colors.accent-orange}", "{colors.accent-green}", "{colors.flavor-purple}", "{colors.flavor-teal}", "{colors.accent-pink}", "{colors.flavor-deep-pink}", "{colors.flavor-lime}"]
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
    overlay: "{colors.overlay-scrim}"

## Components
**button-primary** carries the observed `.apply-button` geometry (18px/24px 700-weight type, 2px transparent border, pseudo-element background swap) mapped onto the brand red; hover/disabled tints are proposed since no hover values were captured. **button-secondary** is an inferred outline variant for secondary calls-to-action like "find out more," reusing the primary red as text/border on white. **button-round** reflects the literal `.apply-button-round` rule (28px circle, yellow fill, full radius) seen in the CSS, likely used for compact icon actions. **text-input** and **search** are proposed patterns for the newsletter/email field and site search referenced in the page text, styled with neutral hairline borders since no focus-state colors were observed. **nav-bar** is inferred from the extensive menu structure in the text excerpt (home, choco shop, our promise, news, contact) and kept on a white canvas with black text for legibility. **product-card** and **flavor-swatch** are proposed together to represent the many named chocolate bars (32%, 70%, caramel sea salt, etc.); the swatch uses the flavor-named custom-property colors directly as small identity dots, a pattern consistent with how the brand names each hex value after an ingredient. **hero** proposes a full-bleed red band for the "serious about people, crazy about chocolate" statement, an unverified layout guess based on prominent mission copy. **footer** and **badge** are proposed low-emphasis components for the link-heavy footer (terms, FAQ, jobs, social icons) and for labeling limited editions or campaign tags.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | ≤480px | Single-column stack, nav collapses to a drawer/menu icon |
| tablet | 481–1024px | 2-column product grid, condensed nav |
| desktop | ≥1025px | Multi-column grid, full horizontal nav |

Touch targets should be at least 44px per side, consistent with the `--swiper-navigation-size: 44px` value observed in the CSS. Navigation collapse, drawer transitions, and exact grid column counts are recommendations only; no responsive or interaction behavior was directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and a text excerpt only; no rendered layout, computed styles, hover/focus states, or mobile breakpoints were observed. Role assignments for primary/secondary colors, neutrals, and surface tones are inferred from token naming order and general contrast conventions, not confirmed usage in context. Typography sizes beyond the button rule are proposed, not measured. The "American Typewriter" and "Chocolate letter" font entries are taken from the raw font-family evidence, but their actual application scope, web-font delivery, and licensing were not verified. Spacing, radius, and component padding values beyond the `.apply-button` rule are conventional proposals layered onto the brand's observed color and button tokens.
