---
version: alpha
name: "Tula"
source_url: "https://babytula.com"
captured_at: "2026-09-28T04:54:22.224510+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Baby Tula's storefront CSS exposes a high-contrast, editorial system built on pure black (#000000) and white (#ffffff), with a supporting family of warm off-white and cream neutrals (#f7f7f7, #f2ede5, #f8f1e5, #fffbf4, #fffdf4) that likely stage soft section backgrounds behind product photography of printed carrier fabrics. Border and divider grays (#dbdbdb, #eaeaea, #cccccc) are inferred hairline tones from the CSS custom-property border variables. A small saturated cluster — pink/red (#dd4056), orange (#ee9441), green (#3ed660), and blues (#00bbff, #1990c6, #136f99) — appears in root variables but its product role (sale badges, size/fit indicators, seasonal callouts) is not confirmed by markup, so these are treated as inferred accent and status colors. Typography relies on named custom fonts (Tula Header, Tula Serif, Tula Body Regular, Tula Body Bold) layered over a standard system-font stack fallback; exact weights/sizes are not exposed in the evidence, so the scale below is proposed. The overall interpretation favors a monochrome, gallery-like frame — black text on white/cream — that lets the bold printed-fabric product photography (the brand's stated differentiator) carry the visual energy, with sharp/minimal corner radii matching the observed 0px resource-card token.

colors:
  primary: "#000000"
  ink: "#262626"
  canvas: "#ffffff"
  body: "#4d4d4d"
  muted: "#8a8a8a"
  hairline: "#dbdbdb"
  surface-soft: "#f2ede5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#dd4056"
  warning: "#ee9441"
  success: "#3ed660"
  info: "#00bbff"
  deep-navy: "#07202c"
typography:
  display-xl: {fontFamily: "'Tula Header', sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Tula Header', sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Tula Body Bold', sans-serif", fontSize: "20px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Tula Body Regular', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Tula Body Regular', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Tula Body Regular', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Tula Body Bold', sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.5px"}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
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
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.title-md}"
    labelTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fabric-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** is proposed as solid black on white, matching the observed `--cart-bubble-background-fallback: #000000` token, used for primary CTAs like "SHOP NOW" and add-to-cart actions. **button-secondary** proposes an outlined inverse treatment for lower-emphasis actions such as "Explore" links, using the same ink border/text with a white fill. **text-input** covers search and form fields, styled with the light hairline border family observed in the `--color-border` variable chain, on a white background. **nav-bar** represents the persistent header row (Shop, About, Learn, Last Chance) with black text on white and a bottom hairline, per the header section's color-custom variables. **product-card** models the repeated carrier tiles seen in the text excerpt (image, name, print/fabric label, price), using a plain white surface and no rounding to keep a catalog-like grid. **hero** proposes the top banner ("MEET THE NEW TULA") on a warm cream surface-soft background to separate it from the pure-white body, with large display typography. **footer** is proposed inverted (black background, white text) for contrast at the page end, echoing the black CTA color rather than an observed footer screenshot. **badge** covers sale/new-drop labels ("NEW DROP"), using the accent pink as an inferred promotional color since no swatch-to-role mapping was confirmed. **search** proposes the region/language and product search affordance referenced in the page text, styled like text-input but pill-rounded for a lighter touch. **fabric-swatch-selector** is a category-specific proposed component for choosing between the carrier's many named prints (e.g., "Shadow Petals," "Willow Grove Check"), rendered as small circular swatches with a black ring indicating selection.

## Responsive Behavior
The following breakpoints are a **recommendation**, not measured site behavior, since no media-query evidence was supplied:

| Breakpoint | Width       | Layout guidance                                   |
|-----------|-------------|----------------------------------------------------|
| mobile    | 0–599px     | Single-column product grid, collapsed hamburger nav |
| tablet    | 600–1023px  | 2-column product grid, condensed nav labels        |
| desktop   | 1024–1439px | 3–4 column product grid, full nav bar               |
| wide      | 1440px+     | 4+ column grid, wider section padding (`{spacing.section}`) |

Touch targets should be a minimum 44×44px for nav, cart, and swatch controls. Header navigation should collapse into a drawer/menu below tablet width; the region/language selector (seen as a long list in evidence) should become a searchable modal rather than an inline dropdown on small screens.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, a text excerpt, and a color/font list — no rendered screenshots, computed layout, or interaction states were observed. Role assignments for saturated palette entries (pink, orange, green, blues, navy) are inferred guesses based on typical ecommerce usage (badges, status, links) and are not confirmed against actual markup usage. All typography sizes, weights, and line-heights are proposed defaults since no explicit `font-size`/`font-weight` values were present in the supplied CSS rules for the named Tula font families. The custom font families ("Tula Header," "Tula Serif," "Tula Body Regular," "Tula Body Bold") are proprietary and their licensing/availability for reuse is unverified; generic sans-serif/serif fallbacks are included per requirements. Component states (hover, focus, disabled, error) are proposed patterns only, not extracted from interaction traces. Mobile menu behavior, cart drawer design, and actual grid column counts were not observed and are marked as recommendations above.
