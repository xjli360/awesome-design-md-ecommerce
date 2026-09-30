---
version: alpha
name: "Viva Raw"
source_url: "https://vivarawpets.com"
captured_at: "2026-09-28T05:09:04.503375+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Viva Raw's storefront pairs a warm, natural neutral base with a single
  saturated accent, reflecting the brand's "fresh, human-grade" positioning.
  The dominant surface is white (#ffffff) with a softer warm off-white
  (#f9f8f4) used for section backgrounds, alongside a body-copy gray
  (#404040) and a darker near-black (#222222) reserved for headings —
  both inferred from generic text-color usage rather than directly
  labeled. A muted gray (#8e8e8e) and light hairline (#d6d6d6) support
  secondary text and dividers. The clearest observed accent is a plum
  purple (#8d67ac), confirmed by the Judge.me review-widget variables
  (--jdgm-primary-color, --jdgm-write-review-bg-color), which this
  document treats as the primary interactive color; a pale lavender tint
  (#efe4fb) is proposed as its complementary card/surface background. A
  warm coral (#ee6c4d) appears explicitly on checkout-related buttons and
  is treated as a secondary/CTA accent, while a golden yellow (#fbcd0a)
  is confirmed as the star-rating color. A soft blue (#1990c6) and cream
  (#fdf5e3) round out supporting neutrals. Typography is built on two
  observed font families — Qanelas (bold, used on interactive elements
  like the back-button at weight 900) for display/heading roles, and
  Cabin for body copy — both with sans-serif fallbacks. Payment-brand
  colors (Visa/Mastercard/PayPal blues, reds, oranges) were excluded from
  the brand palette as they belong to third-party badges, not the site's
  identity.

colors:
  primary: "#8d67ac"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#404040"
  muted: "#8e8e8e"
  hairline: "#d6d6d6"
  surface-soft: "#f9f8f4"
  surface-card: "#efe4fb"
  on-primary: "#ffffff"
  accent-coral: "#ee6c4d"
  accent-blue: "#1990c6"
  highlight-yellow: "#fbcd0a"
  cream: "#fdf5e3"
typography:
  display-xl: {fontFamily: "'Qanelas', sans-serif", fontSize: 60px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Qanelas', sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Qanelas', sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Cabin', sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Cabin', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Cabin', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Qanelas', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.accent-coral}"
    borderColor: "{colors.accent-coral}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.highlight-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"

## Components
**button-primary** — the plum purple (#8d67ac) fill is the only confirmed brand-interactive color, sourced from the Judge.me review-widget variables (`--jdgm-write-review-bg-color`, `--jdgm-primary-color`). Proposed as the default CTA for actions like "Start Now" and "Build Meal Plan."

**button-secondary** — an outline treatment using the coral (#ee6c4d) observed explicitly on `.button--outline` checkout links (`color:#ee6c4d!important;box-shadow:inset 0 0 0 2px`). Proposed for lower-emphasis actions such as "Learn More."

**text-input** — proposed pattern using the hairline gray (#d6d6d6) border and white canvas, consistent with the site's light, airy neutral palette; no explicit input styling was captured in evidence.

**nav-bar** — inferred from `--header-grid-template` and `--header-padding-block` variables showing a three-column sticky header (logo, main nav, secondary nav) with responsive logo sizing (100–120px). Background and text colors are proposed defaults on white canvas.

**product-card** — proposed component for the Dog/Cat/Pure recipe tiles referenced in page text ("View Recipes," "97% meat ingredients"). Uses the lavender surface-card tint to visually separate cards from the white page background.

**hero** — proposed full-width intro section styled after the homepage's "your food for life" headline, using the largest display typography scale (`--text-h0`/`--text-h1` observed in `:root`) on a soft warm background.

**footer** — proposed dark-ink footer for contrast and closure, consistent with common ecommerce patterns; not directly observed in the supplied CSS.

**badge** — the golden yellow (#fbcd0a) is confirmed as `--jdgm-star-color`, used here as a small pill badge for ratings/promo flags (e.g., "50% off" announcement bar), rounded fully.

**search** — proposed pill-shaped input, unobserved in evidence but consistent with the rounded, friendly visual language implied by the review widget's 10px border-radius token.

**subscription-card** — a category-appropriate component reflecting the site's subscribe/one-time recipe-plan flow ("Choose from 5 single protein recipes. Subscribe for convenience or try a one-time order!"), styled with the primary purple as an accent stroke or ribbon.

## Responsive Behavior
Proposed breakpoint recommendation (not measured from live rendering):

| Breakpoint | Width      | Notes                                           |
|-----------|-----------|--------------------------------------------------|
| sm        | ≤ 599px   | Single-column stacking; nav collapses to menu icon |
| md        | 600–959px | Two-column product grids; header logo ~100px    |
| lg        | 960–1279px| Three-column grids; header logo grows to ~120px (per observed CSS custom property step) |
| xl        | ≥ 1280px  | Max-width containers using `--container-gutter` / `--section-outer-spacing-block` steps observed in `:root` |

Touch targets are recommended at a minimum 44×44px for buttons and nav items. Mobile nav is assumed to collapse into a hamburger/drawer pattern given the "Open navigation menu" text in the evidence, though the actual collapsed markup and interaction were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, color values, and font-family declarations only; no live rendering, computed layout, or DOM screenshots were available. Semantic color roles (ink vs. body vs. surface-soft) are inferred from generic naming conventions and typical usage patterns, not confirmed via inspected selectors applying them to text or backgrounds. Rounded and spacing scales follow a standard proposed token system rather than fully-confirmed site measurements (only the Judge.me widget's `--jdgm-border-radius: 10` was directly observed). Button, card, nav, and footer states (hover, focus, active, disabled) beyond the single confirmed `.button:hover` opacity rule (`--button-background-opacity: 0.85`) are proposed, not verified. Mobile/responsive breakpoints are estimated industry defaults, not measured from the site. Font availability, licensing, and exact weight/style ranges for Qanelas and Cabin were not verified beyond their appearance in `font-family` declarations.
