---
version: alpha
name: "Pimax"
source_url: "https://pimax.com"
captured_at: "2026-09-28T04:10:28.660264+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pimax's marketing site runs on a light paper canvas (#f2f2f2) with near-black
  ink (#1a1a1a) for primary text, paired with a cool sky-blue accent (#6193f6)
  used for links, active nav states, and filled buttons (--accent, --btn-accent).
  A darker accent variant (#4f7ef0) appears on hover states, and a saturated
  blue (#345dff) is present in the palette as a secondary accent, inferred here
  for emphasis or link-visited states. Dark gradient surfaces (#141416, #22222c,
  #2c2c43) suggest hero or video-panel backgrounds distinct from the paper body.
  Type is set in "HarmonyOS Sans" for all UI and body copy, with "Arcline" bound
  to --mono/--number-mono for spec figures and technical callouts, and "Arcline
  Inline" available for large monogram-style numerals (observed on product-menu
  card badges). Radii are small and utilitarian (2-8px per --r-xs..--r-lg),
  reinforcing a technical, hardware-catalog tone rather than a soft consumer
  aesthetic. Card surfaces (#f7f7f4-adjacent, approximated here with #f2f2f2)
  sit on the paper background with subtle borders. Semantic groupings below
  (muted text, hairlines, dark surfaces) are inferred from CSS custom-property
  names and usage context, not confirmed brand guidelines.

colors:
  primary: "#6193f6"
  primary-strong: "#345dff"
  primary-hover: "#4f7ef0"
  ink: "#1a1a1a"
  canvas: "#f2f2f2"
  body: "#1a1a1a"
  muted: "#7a7a7a"
  hairline: "#d8d6d2"
  surface-soft: "#f2f2f2"
  surface-card: "#141416"
  surface-card-alt: "#22222c"
  surface-card-deep: "#2c2c43"
  border-dark: "#2a2a2a"
  cool-gray: "#9ca3af"
  alert: "#ff8e8e"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.06, letterSpacing: -0.8px}
  display-md: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.4px}
  title-md: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 19px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.38px}
  body-md: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.65, letterSpacing: 0px}
  body-sm: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  button-md: {fontFamily: "\"HarmonyOS Sans\", sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
  spec-mono: {fontFamily: "Arcline, monospace", fontSize: 13px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  data-mono-lg: {fontFamily: "\"Arcline Inline\", monospace", fontSize: 42px, fontWeight: 600, lineHeight: 1, letterSpacing: -2px}
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
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    monogramTypography: "{typography.data-mono-lg}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.surface-card-alt}"
    textColor: "{colors.cool-gray}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.section}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-sheet:
    backgroundColor: "{colors.surface-card-deep}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.spec-mono}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components

**button-primary** renders the site's accent-blue call-to-action (matching the observed `.btn-accent` rule), used for purchase and configure actions; hover swaps to `#4f7ef0` per CSS, and a disabled/muted state is proposed but not observed.

**button-secondary** mirrors the observed `.btn` outline style (1px border in a mid-ink tone, transparent fill), intended for secondary actions like "Learn more"; the hover-to-filled-dark transition is directly observed, focus-ring styling is proposed.

**text-input** is inferred for search or account forms; no input-specific CSS was supplied, so border, padding, and radius follow the site's small-radius, hairline-bordered convention seen elsewhere.

**nav-bar** generalizes the observed `.product-menu-group` pattern (flex row, active/hover shifts text to accent color and nudges content 4px); a sticky/fixed behavior is proposed, not confirmed from static CSS.

**product-card** is modeled directly on `.product-menu-card` and its title/copy/monogram children — a soft off-white card containing a bold title, muted description, and an oversized mono numeral or letter mark used as a device badge.

**hero** is inferred from the `--dark-grad` gradient variable and `.hero-h1` typography rule; it proposes a full-bleed dark gradient panel behind large display type, though no hero markup/layout was directly captured.

**footer** is a proposed dark, low-contrast band using the cooler gray text token, consistent with the site's dark-surface gradient stops; column structure and link groupings are not observed.

**badge** is a small pill using the accent fill and caption type, proposed for "new," "in stock," or spec highlight tags common to hardware product listings; not directly observed in the supplied rules.

**search** is proposed for a header search affordance typical of e-commerce hardware sites; styling follows the same hairline/canvas convention as text-input since no dedicated search CSS was supplied.

**spec-sheet** is a category-appropriate component for VR hardware: a dark card pairing caption-weight labels with monospace (`Arcline`) values for FOV, resolution, refresh rate, etc., reflecting the site's dedicated `--mono`/`--number-mono` variables intended for numeric data display.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | single-column product cards, nav collapses to a toggled menu, `--px` shrinks toward the observed 20px root value |
| tablet | 640-1024px | two-column product grid, nav-bar remains horizontal with condensed spacing |
| desktop | 1024-1440px | full grid layouts, `--px:64px` gutter as observed in the root variable |
| wide | >1440px | max-width content container, additional whitespace, no new components |

Touch targets should be at least 40-44px tall for buttons and nav items; the observed `.btn` padding (10px 16px) is close to this and should be increased slightly on touch devices. Collapse patterns (hamburger menu, accordion product menu) are proposed conventions, not confirmed from captured markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and a title/color/font extraction only; no live rendering, DOM structure, or interaction states (hover/focus/active beyond the few rules supplied) were observed. Several semantic role assignments — canvas vs. surface-soft, dark-surface tiers, and hairline color — are inferred from variable naming and usage context rather than confirmed visually. Font sizes for display-xl, display-md, caption, and several component paddings are proposed estimates, not measured values, since only a subset of type rules (h1 weight/line-height/letter-spacing, card titles, body copy) were present in the evidence. Mobile layout, navigation collapse behavior, and any JavaScript-driven interactions are not observed. "Arcline," "Arcline Inline," and "HarmonyOS Sans" are used strictly as named in the supplied font_families list; their licensing, hosting, and actual glyph availability for production use have not been verified.
