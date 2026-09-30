---
version: alpha
name: "Little Spoon"
source_url: "https://littlespoon.com"
captured_at: "2026-09-28T04:24:16.544986+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Little Spoon's observed evidence points to a bright, food-forward identity built on
  a saturated teal (#00e3cd) paired with a warm cream canvas (#fbf7e8), suggesting an
  organic, appetite-friendly palette rather than a clinical one. Supporting neutrals
  (#141414, #424242, #757575, #e0e0e0) carry body copy and hairlines, while a wide set
  of pastel and saturated accents (coral, purple, lime, blue, mint) appear throughout
  the palette and are inferred here as illustration/tag accents for meal categories,
  stages, or promotional badges rather than core UI colors. Typography is directly
  evidenced: headings use Mulish at weight 900, and buttons/inputs use Lato with a
  0.4px letter-spacing, giving a friendly-but-confident voice — bold rounded display
  type over a plainer, highly legible interface font. Slick-carousel dot styling
  (gray inactive, darker active, circular, 1rem) confirms a pattern of soft circular
  controls, which this spec generalizes into a rounded, pill-leaning component
  language (buttons, badges, dots) appropriate for a parent-facing food-delivery
  brand. All sizing, spacing, and weight values not explicitly present in the CSS
  evidence are marked as proposed/inferred and should be validated against live
  rendering before implementation.

colors:
  primary: "#00e3cd"
  ink: "#141414"
  canvas: "#fbf7e8"
  body: "#424242"
  muted: "#757575"
  hairline: "#e0e0e0"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#004039"
  accent-coral: "#ff9779"
  accent-purple: "#dc7bff"
  accent-lime: "#c2ff7f"
  accent-blue: "#18a7ff"
  accent-mint: "#b8f7f1"
  deep-navy: "#2a313f"
  overlay-transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Mulish, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Mulish, sans-serif", fontSize: 32px, fontWeight: 900, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Mulish, sans-serif", fontSize: 22px, fontWeight: 800, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.4px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.surface-card}"
    linkColor: "{colors.accent-mint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  plan-selector:
    backgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.accent-mint}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is the core conversion control (e.g. "Get Started," "Build a Plan"), using the observed brand teal as fill with a dark teal-green ink for legible on-primary contrast. Hover/focus/disabled states are not observed and are proposed as standard opacity/darken treatments.

**button-secondary** provides a lower-emphasis outline pattern for secondary actions (e.g. "Learn More"), using a card-white background and hairline border consistent with the neutral values present in the CSS.

**text-input** follows the button/input font declaration (Lato, 0.4px letter-spacing) directly observed in the CSS, styled as a bordered field with a muted placeholder color; focus-ring styling is proposed, not observed.

**nav-bar** is inferred as a cream-canvas header bar with dark text and teal hover states, generalized from the `.hDrAWn:hover` rule that sets link/button color to black on hover — the base (non-hover) state is assumed to be a neutral ink tone.

**product-card** represents meal/product tiles in a grid (e.g. baby blends, toddler meals), using a white surface, subtle border, and Mulish title over Lato body copy; shadow and hover elevation are proposed conventions, not measured.

**hero** is the top-of-page introductory band, using the cream canvas as a warm, food-appropriate backdrop with large Mulish display type and a primary CTA button; exact hero imagery and layout were not observed.

**footer** uses the darkest observed neutral (#2a313f) as a grounding surface with light text and mint-tinted links, proposed to house navigation, legal, and newsletter content typical of a DTC food brand.

**badge** models small tags (e.g. "Organic," "New," age-stage labels) using one of the bright pastel accents (lime) with dark ink text and a fully rounded pill shape, consistent with the soft, circular dot styling observed in the slick-carousel rules.

**search** and **plan-selector** are category-appropriate additions: search reflects a soft, pill-shaped filter/search affordance for browsing meals; plan-selector models the subscription/plan-picker pattern common to meal-delivery flows (e.g. selecting baby/toddler stage or delivery frequency), using the mint accent to indicate an active state. Both are proposed patterns inferred from brand category, not from directly observed markup.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not a measurement of live site behavior:

| Breakpoint | Width      | Notes                                      |
|-----------|-----------|---------------------------------------------|
| mobile    | 0–599px   | Single-column stacking, nav collapses to menu icon |
| tablet    | 600–959px | 2-column product grids, nav may remain inline |
| desktop   | 960–1279px| 3–4 column grids, full nav bar |
| wide      | 1280px+   | Max-width container, generous section spacing |

Touch targets should be a minimum of 44×44px for buttons, badges, and dot controls (the observed slick-dots use 1rem/20px hit areas, which should be enlarged for touch accessibility). Navigation is assumed to collapse into a hamburger/drawer pattern below the tablet breakpoint; this collapse behavior was not observed in the supplied evidence and should be confirmed against the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/color/font extraction only; no live rendering, DOM structure, or interaction states (hover, focus, active, error, loading) were observed beyond the two hover/active rules explicitly present (`.hDrAWn:hover`, `.slick-dots li.slick-active`). Semantic role assignments — which colors serve as "primary" vs. decorative/illustration accents — are inferred from color prominence and typical DTC food-brand conventions, not confirmed usage. All numeric type sizes, spacing scale values, rounded-corner scale, and breakpoints are proposed defaults, since the evidence contained no explicit font-size, spacing, or media-query values apart from the slick-dot dimensions. Mobile/responsive layout behavior was not observed. Availability, licensing, and exact weight range of Mulish and Lato (both are typically Google Fonts) were not verified against Little Spoon's actual font-loading configuration.
