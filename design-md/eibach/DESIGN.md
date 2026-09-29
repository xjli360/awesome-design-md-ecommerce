---
version: alpha
name: "Eibach"
source_url: "https://eibach.com"
captured_at: "2026-09-28T04:28:50.058823+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Eibach's stylesheet centers on a high-contrast performance palette: a saturated red (#ed1c24, darkening to #c61017 on hover) as the primary accent against near-black ink (#2c2c2c, hovering to #131313) and clean white canvas. Supporting neutrals span a tight grey ramp (#969696, #d9d9d9, #f2f2f2, #cccccc) used for muted labels, hairlines, and soft surfaces in table striping and light buttons. A stray blue (#5897fb) appears only incidentally and is treated here as an inferred focus/link accent rather than a brand color. Typography draws on "Industry" for bold display headlines — fitting an industrial suspension brand — paired with Inter/Inter Tight for body copy and UI, falling back to Arial/Helvetica. Buttons are uppercase, bold, and rectangular with minimal rounding, reflecting a utilitarian, motorsport-adjacent tone. This interpretation extends observed button and table treatments into a fuller system: card surfaces, navigation, and a fitment/spec-table pattern, all flagged as proposed where the source CSS did not directly confirm layout or state.

colors:
  primary: "#ed1c24"
  primary-hover: "#c61017"
  ink: "#2c2c2c"
  ink-hover: "#131313"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#969696"
  hairline: "#d9d9d9"
  surface-soft: "#f2f2f2"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  border-subtle: "#cccccc"
  focus: "#5897fb"
  success: "#359e37"
  alert: "#bb2124"
typography:
  display-xl: {fontFamily: "Industry, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Industry, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter Tight, Inter, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter Tight, Inter, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    hover: {backgroundColor: "{colors.primary-hover}", textColor: "{colors.on-primary}"}
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
    hover: {backgroundColor: "{colors.hairline}", textColor: "{colors.ink-hover}"}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    focus: {border: "1px solid {colors.focus}"}
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
    accent: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    accent: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    linkColor: "{colors.on-primary}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
  spec-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-md}"
    rowStripeColor: "{colors.surface-soft}"
    rowTextColor: "{colors.body}"
    padding: "{spacing.sm}"

## Components

**button-primary** reflects the observed `.btn-primary` rule directly: red fill (#ed1c24), white text, uppercase bold weight, and a darker red hover (#c61017). It is the primary call-to-action for "Shop Now" or "Find Fitment" actions.

**button-secondary** is proposed from the `.btn-light` pattern, using the soft grey surface with dark ink text for lower-emphasis actions like "Learn More," with a hairline border added for definition on white backgrounds not explicitly present in the source.

**text-input** is a proposed pattern for search and fitment forms; no input-specific CSS was supplied, so border, padding, and focus ring (using the incidental #5897fb blue) are inferred conventions rather than observed styles.

**nav-bar** proposes a dark ink header with red accent details, consistent with the brand's dark-button vocabulary, though actual header markup and behavior were not present in the evidence.

**product-card** is an inferred container for spring/kit listings, pairing a light card surface with hairline borders and title/body type scale; card elevation and imagery treatment are not confirmed by CSS.

**hero** proposes a dark, full-width banner using display typography and the red accent for a headline underline or CTA, extrapolated from the brand's contrast pattern rather than a captured hero selector.

**footer** uses the dark ink background with muted grey text, matching the site's overall dark/light button duality; link and column structure are proposed, not observed.

**badge** is a small red pill for labels like "New" or "Made in USA," built from the primary color and full rounding; no badge selector was present in the source CSS.

**search** proposes a bordered white field for the vehicle fitment lookup common to suspension retailers, styled with hairline borders and muted icon color; interaction states are unverified.

**spec-table** is grounded directly in the observed `.ers-table` header rule — red background, white text, 1.125rem sizing — extended here with a striped body using the observed `#f2f2f2` zebra row color for technical fitment/spec tables.

## Responsive Behavior

The following breakpoint table is a **recommendation** based on common Bootstrap-derived conventions (the `--bs-breakpoint-*` custom properties were observed in `:root`), not measured site behavior:

| Breakpoint | Width | Behavior |
|---|---|---|
| xs | 0px | Single-column stacking, full-width buttons, collapsed nav |
| sm | 576px | Two-column card grids begin |
| md | 768px | Nav bar expands from hamburger to inline links |
| lg | 992px | Three/four-column product and spec grids |
| xl | 1200px | Max-width content container, hero side-by-side layout |
| xxl | 1400px | Additional gutter, no new column behavior |

Touch targets should be at least 44px in height for buttons and nav links; the nav-bar is expected to collapse into a hamburger menu below `md`. These are proposed guidelines only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction only; no live rendering, DOM screenshots, or interaction testing were performed. Component states beyond `:hover` (e.g., `:active`, `:focus-visible`) are proposed, not observed. Layout structure (grid columns, hero composition, nav collapse mechanics, footer columns) was not present in the supplied evidence and is inferred from conventional e-commerce/automotive-parts patterns. The semantic role of several near-duplicate greys (#d9d9d9 vs #dddddd vs #dfdfdf) is uncertain and may reflect incidental third-party component styles rather than deliberate brand tokens. The blue (#5897fb) and green (#359e37, #28782a) values are unexplained by the supplied rules and are treated as inferred utility colors (focus/success) rather than confirmed brand accents. Font availability, licensing, and exact loading method for "Industry" and "Inter"/"Inter Tight" were not verified — generic sans-serif fallbacks are specified accordingly. All pixel sizes in the typography and spacing scales beyond those explicitly present in `.ers-table` (1.125rem) are proposed values for consistency, not measured from rendered pages.
