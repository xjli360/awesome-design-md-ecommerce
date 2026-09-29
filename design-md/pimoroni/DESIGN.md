---
version: alpha
name: "Pimoroni"
source_url: "https://shop.pimoroni.com"
captured_at: "2026-09-28T04:27:47.930982+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pimoroni's shop front presents as a clean, high-contrast maker storefront: a near-black
  ink (#17171f, mapped from an inferred `--black` variable) on white canvas, with a single
  saturated magenta (#ff2bd6, inferred `--magenta`) used sparingly as the primary interactive
  color for active filter pills and selection states. A softer violet (#b026ff) appears on
  hover/link states and is treated here as a secondary accent, distinct from magenta. Neutral
  greys (#8a8a8a, #dedede, #bac0ca) carry secondary text, hairlines, and disabled/pale
  affordances, while very light panels (#f6f7fa, #f5f5f5) suggest soft surface fills for
  hover backgrounds and cards. A wider set of highly saturated hues (cyan, green, orange,
  yellow, red, teal, blue) is present in the palette without confirmed usage; these are
  interpreted as inferred category/badge colors typical of a component-catalog storefront,
  not as core brand chrome. Typography is Roboto throughout, with a confirmed heavy (900)
  weight for heading text and a bold (700) weight for buttons/toggles; all pixel sizes beyond
  the observed 32px heading are proposed. Rounded pill shapes (~1.25rem) recur on buttons and
  filters, informing a pill-forward interaction language.

colors:
  primary: "#ff2bd6"
  ink: "#17171f"
  canvas: "#ffffff"
  body: "#3d3d3d"
  muted: "#8a8a8a"
  hairline: "#dedede"
  surface-soft: "#f6f7fa"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent: "#b026ff"
  pale: "#bac0ca"
  dark-surface: "#1a1c3d"
  cyan-fill: "#00b2ca"
  warning: "#ffc300"
  success: "#10c46e"
  danger: "#ff2d55"
  info: "#1990c6"

typography:
  display-xl: {fontFamily: "Roboto, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto, sans-serif", fontSize: 32px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.3px}
  title-md: {fontFamily: "Roboto, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}

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
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.pale}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  category-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xs} {spacing.base}"
    typography: "{typography.button-md}"

## Components

**button-primary** uses the observed magenta as a solid fill with white text, echoing the
`[aria-current]` filter-pill treatment. Hover/focus states are proposed as a slight opacity
or shade shift, not directly observed.

**button-secondary** is a light, low-emphasis alternative using the soft surface fill and a
hairline border, intended for secondary actions like "View all" or filter resets; states are
proposed.

**text-input** is inferred from general storefront conventions (search, quantity fields) using
canvas background, hairline border, and small radius; focus-ring styling is not observed and
is proposed as an accent-colored outline.

**nav-bar** represents the top-level shop navigation on white canvas with ink text; the
breadcrumb (`.path`) evidence confirms bold heading-weight links separated by pale slashes,
which this component generalizes into a header pattern.

**product-card** is a proposed catalog tile: white/light surface, hairline border, rounded
corners, title in title-md and price in body-md. Hover elevation and stock badges are proposed,
not observed.

**hero** is a proposed dark-surface banner (using the dark navy tone present in the palette)
for homepage promotional content, pairing large display type with light text; this section's
existence and exact styling are not confirmed by the supplied CSS.

**footer** mirrors the hero's dark surface for brand consistency at page end, with muted pale
links; content structure is proposed.

**badge** repurposes one of the palette's saturated hues (yellow) as a small pill label for
stock/category tags — a common maker-store pattern — though no badge markup was present in
evidence.

**search** and **category-filter-pill** are directly informed by the `.market-panel li >button`
rules: pill radius, grid layout for icon/label/check, magenta active fill, and light hover
background. The `category-filter-pill` active/inactive contrast is the most strongly evidenced
interactive pattern in this spec.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width      | Layout notes (proposed) |
|------------|-----------|--------------------------|
| compact    | <600px    | Single-column product list, filter pills collapse into a sheet/drawer (consistent with `.menu-sheet` evidence) |
| medium     | 600–960px | Two-column product grid, nav condenses to icon buttons |
| wide       | 960–1280px| Multi-column grid, persistent filter sidebar |
| xwide      | >1280px   | Max-width content container, increased gutters |

Touch targets should be at least 44px; the observed `.market-panel` button `min-height: 2.25rem`
(36px) suggests a slightly smaller baseline that should be enlarged for touch contexts. Filter
and sort controls are recommended to collapse into a bottom sheet or modal below the medium
breakpoint, consistent with the `.sheet-header .close` pattern found in evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/selector evidence only; no rendered layout, responsive
behavior, or interaction states (hover/focus/active beyond declared CSS, animations, loading
states) were directly observed. Several semantic role assignments — including `body`,
`surface-card`, `dark-surface`, `warning`, `success`, `danger`, and `info` — are inferred from
palette availability and general storefront conventions, not confirmed component usage. All
typography sizes except the 32px/900-weight heading are proposed estimates. The `letter-spacing:
-1%` value on headings was approximated as a pixel value for token purposes. Font availability,
licensing, and fallback rendering for Roboto were not verified. Mobile navigation, cart, and
checkout flows were not present in the supplied evidence and are therefore not covered.
