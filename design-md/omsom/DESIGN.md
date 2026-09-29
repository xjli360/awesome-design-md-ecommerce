---
version: alpha
name: "Omsom"
source_url: "https://omsom.com"
captured_at: "2026-09-28T05:00:52.441231+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Omsom sells bold, chef-partnered Asian sauces and starters, and the observed
  palette reflects that "proud + loud" positioning: a dominant vivid purple
  family (#8b3dff and its darker/lighter relatives such as #612dae, #7731d8,
  #a370fc) paired with an aggressive red-pink accent range (#db142c, #fd4958,
  #b61629). These are treated as primary and secondary brand colors
  respectively; their exact UI roles (CTA vs. promotional badge vs. link) are
  not directly observable from the supplied CSS and are therefore inferred
  from frequency and contrast against near-black text tones (#0d1216, #18191b)
  on a white canvas. Neutral surfaces (#f0f1f5, #f6f7f8) and translucent
  black/white overlays (#0000004d, #ffffff26) suggest a system of soft card
  backgrounds and hairline dividers, mapped here as best-fit approximations.
  Font evidence points to a Noto Sans-led stack (with Vietnamese-subset
  support, fitting the brand's Southeast Asian focus) and Open Sans as a
  secondary body face; "Canva Sans" and "calibrate" appear in the stack but
  their origin (tooling artifact vs. brand asset) is unverified. This
  interpretation proposes a confident, high-contrast, condiment-aisle-ready
  system built strictly from these observed values.

colors:
  primary: "#8b3dff"
  secondary: "#db142c"
  accent: "#fd4958"
  ink: "#0d1216"
  canvas: "#ffffff"
  body: "#18191b"
  muted: "#3b3c3d"
  hairline: "#0000004d"
  surface-soft: "#f0f1f5"
  surface-card: "#f6f7f8"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  success: "#008008"
  highlight: "#e7dbff"
typography:
  display-xl: {fontFamily: "'Noto Sans', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Noto Sans', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Noto Sans', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spice-level-indicator:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components
**button-primary** is the vivid purple call-to-action (e.g., "Add to Cart," "Shop Now"), using white text for contrast; state is proposed since no hover/active CSS was supplied.

**button-secondary** is an outlined variant for lower-emphasis actions like "Learn More," reusing the primary purple as border and text color on a white background; this pairing is inferred, not measured.

**text-input** covers search and newsletter fields, using the soft card surface and a translucent hairline border; focus/error states are proposed and unobserved.

**nav-bar** is assumed to sit on a white canvas with dark ink text and a bottom hairline; sticky or transparent-on-scroll behavior is not confirmed by the evidence.

**hero** applies the bold purple field with large display type, matching the "proud + loud" copy tone found in the page text excerpt; this is a proposed treatment for a banner/landing section, not a captured layout.

**product-card** represents individual sauce/noodle-kit listings on an off-white card with a hairline border, title in title-md, and description in body-sm; imagery, pricing, and rating sub-elements are proposed additions.

**badge** uses the red-pink secondary color for promotional or "New" labels in pill form; this is inferred from the presence of strong red tones in the palette rather than a confirmed badge selector.

**footer** is proposed as a dark, near-black band using ink as background with white text, consistent with high-contrast brand pairing seen elsewhere in the palette.

**search** is a pill-shaped input on a light surface-soft background, intended for site/product search; icon placement and autocomplete are not observed.

**spice-level-indicator** is a category-specific proposal for sauces/condiments, using a light lavender highlight chip with red text to denote heat or flavor intensity; this component is entirely speculative and not evidenced in the supplied CSS.

## Responsive Behavior
This is a recommendation only; no live responsive/mobile layout was observed.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column product grid, nav collapses to a hamburger menu, hero text scales to display-md. |
| Tablet | 640–1024px | Two-column product grid, nav-bar remains horizontal with condensed spacing. |
| Desktop | >1024px | Three-to-four-column product grid, full nav-bar, hero retains display-xl sizing. |

Touch targets should be at least 44px in height for buttons and nav items; collapse nav into a slide-out or dropdown menu below the tablet breakpoint. These values are proposed defaults, not measured from the live site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was limited to a small CSS excerpt and hashed/obfuscated selectors (e.g., `._99eNQQ.gFh1Bw .SJUElg`), so exact component styling, spacing tokens, and hover/focus states could not be confirmed.
- Role assignment for colors (primary vs. secondary vs. accent) is inferred from frequency and typical usage patterns, not from confirmed CTA or link selectors.
- Font sizes, weights, and line-heights in the typography scale are proposed conventions, not values extracted from the supplied CSS.
- "Canva Sans" and "calibrate" appear in the observed font stack; their licensing, brand ownership, and actual rendering role are unverified and may be tooling artifacts rather than intentional brand fonts.
- No interaction states, animations, or mobile/responsive behavior were directly observed; all such guidance above is a design recommendation.
- Rounded and spacing scales follow a generic proposed system rather than values measured from the site.
