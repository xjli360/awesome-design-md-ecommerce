---
version: alpha
name: "Walrus Audio"
source_url: "https://www.walrusaudio.com"
captured_at: "2026-09-28T09:02:55.231231+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from Walrus Audio's observed storefront CSS: a
  near-black ink (#06070e) driving headings and the top promo bar, a clean
  white canvas, and a muted olive-gray body tone (#696d6a) for running copy.
  A soft seafoam accent (#a1d6ca) appears as a highlight chip inside the promo
  bar and is treated here as the brand's single distinguishing accent, used
  sparingly against dark or light grounds. A saturated red (#ff4b46) appears
  only on the cart-count badge and is mapped to a small notification/badge
  role rather than a primary action color, since no primary CTA background
  was directly observed. Headings use the observed condensed display face
  acumin-pro-condensed at weight 700, paired with Inter for body and UI text;
  a monospace stack observed on the cart badge is reserved for small numeric
  or technical labels. Grays across the palette (#e0e0e0, #f4f4f4, #999999)
  are consolidated into hairline, surface, and muted-text roles to keep the
  system restrained and reusable. Component states beyond what CSS confirms
  (hover, focus, error) are proposed and flagged accordingly, matching a
  product-forward, spec-driven guitar-pedal retailer.

colors:
  primary: "#06070e"
  ink: "#06070e"
  canvas: "#ffffff"
  body: "#696d6a"
  muted: "#999999"
  hairline: "#e0e0e0"
  surface-soft: "#f4f4f4"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent: "#a1d6ca"
  accent-deep: "#8fcec0"
  badge: "#ff4b46"
  border-dark: "#151932"
typography:
  display-xl: {fontFamily: "acumin-pro-condensed, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.3, letterSpacing: -0.5px}
  display-md: {fontFamily: "acumin-pro-condensed, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  title-md: {fontFamily: "acumin-pro-condensed, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.5, letterSpacing: 0.2px}
  mono-badge: {fontFamily: "\"Andale Mono WT\", \"Andale Mono\", \"Lucida Console\", monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.on-primary}"
    typography: "{typography.mono-badge}"
    rounded: "{rounded.full}"
    padding: "0 {spacing.xs}"
  search:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  sound-category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the dominant dark ink as its fill with white text, matching the weight and treatment seen on heading and promo-bar elements; no explicit primary-button background was captured in the evidence, so this fill is inferred from the site's dominant dark surface. **button-secondary** is a light, outlined variant using the observed hairline gray border for lower-emphasis actions such as "Find a Dealer." **text-input** mirrors the header search field's translucent light-gray background and transparent border, useful for search and email-signup fields. **nav-bar** reflects the white header with dark icon/text coloring seen outside the homepage template, plus a hairline bottom edge. **product-card** is proposed for pedal listings (e.g., Highpoint, Mantle, Canvas Expression Pedal), using a slightly off-white card surface, a hairline border, and the condensed display face for product names, since actual card markup was not directly supplied. **hero** models the homepage promo banner pattern (dark ink background, white text) scaled up for a full hero, using the display-xl heading style. **footer** extends the same dark ink treatment observed on the header-promo bar across the full footer region, which lists company, support, and social links. **badge** directly reflects the observed cart-count pill: red fill, white ring border, monospace numerals, and a fully-rounded pill shape. **search** is a proposed simplified input matching the header search bar's translucent gray fill. **sound-category-tile** is a category-appropriate proposed component for the "Shop by Sound" navigation grouping (Delay & Reverb, Modulation & Octave, etc.), using the seafoam accent as a subtle highlight against a soft surface.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed nav into a drawer/menu icon, stacked hero text |
| tablet | 600–1024px | Two-column product grid, condensed top promo bar retained |
| desktop | >1024px | Full mega-menu navigation (Core/Monarch/Mako/Fundamental/Canvas/Lab), multi-column product and category grids |

Touch targets should be a minimum of 44px in height, particularly for the header search and cart icons. Navigation submenus (observed as extensive category lists) should collapse into accordions on mobile. None of this layout behavior was directly observed; it is inferred from typical responsive patterns for the given markup structure.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and text extraction only; no rendered layout, hover/focus states, animation, or actual mobile breakpoints were observed. The semantic roles for primary, accent, and badge colors are inferred from usage context (heading/background prominence, promo-chip highlight, cart-count fill) rather than confirmed brand guidelines. Spacing and rounded-corner scales beyond the few directly observed values (e.g., 2px badge radius, 10px cart-count radius) are proposed conventions. Typography sizes for display and title levels are proposed extrapolations from the confirmed base font-size (16px body, 12px promo caption) and observed heading weight/line-height; the acumin-pro-condensed and Inter font families are used per CSS declarations, but licensing and actual availability/hosting were not verified. Component interaction states (hover, active, disabled, error) are proposed patterns, not confirmed from evidence.
