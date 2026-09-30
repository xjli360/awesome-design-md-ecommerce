---
version: alpha
name: "Brave + Kind Bookshop"
source_url: "https://www.braveandkindbooks.com"
captured_at: "2026-09-28T04:43:18.237357+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Brave + Kind Bookshop is a Shopify-built independent children's bookstore
  presenting a calm, ink-and-paper palette against a warm off-white canvas
  (#fcfcfc). The CSS custom properties define a deep teal-navy
  (#103948) as the dominant foreground, button, and shadow color, paired
  with a lighter slate-teal (#18566c) that is inferred here as a secondary
  or muted accent. A warm terracotta (#bc5631) appears in the observed
  palette and is treated as a proposed accent for callouts or seasonal
  badges, since no selector confirms its exact usage. Two saturated blues
  (#1990c6, #136f99) are confirmed on the accelerated-checkout button and
  its hover state, so they are mapped to an informational/interactive role
  rather than brand identity. Neutral grays (#ebeced, #dedede) support
  hairlines and soft surfaces. The only observed font family across the
  CSS evidence is "Manuale," used for both body and heading contexts per
  the site's variable-driven type system; no secondary or serif family was
  present in the evidence, so headings and body text share the same family
  with weight and size differentiation proposed rather than measured.
  Corner radii and shadows are Shopify theme variables without resolved
  pixel values, so this spec proposes a restrained, low-radius system
  consistent with the flat button styling observed in base.css.

colors:
  primary: "#103948"
  ink: "#103948"
  canvas: "#fcfcfc"
  body: "#103948"
  muted: "#18566c"
  accent: "#bc5631"
  hairline: "#dedede"
  surface-soft: "#ebeced"
  surface-card: "#ffffff"
  on-primary: "#fcfcfc"
  info: "#1990c6"
  info-hover: "#136f99"
  overlay: "#00000080"
  dark: "#121212"
  black: "#000000"
typography:
  display-xl: {fontFamily: "Manuale, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.96px}
  display-md: {fontFamily: "Manuale, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0.96px}
  title-md: {fontFamily: "Manuale, sans-serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.96px}
  body-md: {fontFamily: "Manuale, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0.96px}
  body-sm: {fontFamily: "Manuale, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.5px}
  caption: {fontFamily: "Manuale, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Manuale, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.96px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    shadow: "0 1px 2px {colors.overlay}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    accentButton: "{colors.info}"
    accentButtonHover: "{colors.info-hover}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the deep teal foreground color as background with the light canvas tone as text, matching the `--color-button` / `--color-button-text` pair defined in the theme root; hover/focus states are proposed, not observed.

**button-secondary** inverts the primary treatment to a white/card surface with teal text and a hairline border, mirroring the `--color-secondary-button` variables; this state styling is proposed.

**text-input** is a proposed pattern for search and account forms, using the neutral hairline border and card background observed elsewhere in the palette; no explicit input selector was present in the evidence.

**nav-bar** reflects the site's header/menu structure implied by the extensive navigation text (Books, Shop, Gift Registry, etc.) sitting on the canvas background; exact height and collapse behavior are not observed.

**product-card** is inferred from the `.product-card-wrapper .card` selector, which exposes CSS variables for radius, border, shadow, and padding without resolved values; this spec proposes a light card with soft shadow.

**hero** is a proposed section for the "WELCOME TO OUR LITTLE INDIE BOOKSHOP" homepage message, using the soft gray-blue surface and largest display type; no hero-specific CSS was supplied.

**footer** is proposed as a dark-teal band using the primary color inverted, consistent with the brand's confirmed foreground/background pairing; footer content and columns are not observed.

**badge** draws on `--color-badge-foreground/background/border`, all mapped to the same teal-on-white pairing observed in the root variables.

**search** proposes a simple bordered field consistent with the extensive country/currency selector text present in the evidence, though its exact visual form is not confirmed.

**cart-drawer** is grounded in the observed "Your cart is empty / Continue shopping / Check out" copy and the accelerated-checkout button CSS, which confirms the blue `#1990c6` / `#136f99` hover pair for payment actions inside the cart panel.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column nav collapses to a menu icon; cart becomes full-height drawer. |
| Tablet | 600–1024px | Two-column product grids; nav may remain horizontal. |
| Desktop | >1024px | Multi-column grids; full horizontal nav and country/currency selector visible inline. |

Touch targets should be at least 44px in height, matching the `clamp(25px, …, 55px)` range seen in the accelerated-checkout button CSS. Navigation collapse and drawer animation timing are proposed using the theme's observed duration tokens (0.2s–0.6s) but exact easing behavior on mobile was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived solely from static CSS and text evidence; no live rendering, computed layout, or interaction testing was performed. Font weight and style values for both body and heading contexts rely on unresolved CSS variables (`--font-body-weight`, `--font-heading-weight`), so all weights above 400/500/600 are proposed, not confirmed. Corner-radius and shadow values for buttons and product cards use unresolved custom properties (`--buttons-radius-outset`, `--product-card-corner-radius`, etc.), so the `rounded` scale here is a proposed system, not extracted from resolved output. The `--color-link` value (rgb 5,44,70) does not match any hex in the supplied observed palette and was therefore omitted rather than approximated. Mobile menu behavior, cart-drawer animation, and hover/focus states are inferred from Shopify theme conventions, not observed on the live site. Availability and licensing of the "Manuale" font were not verified.
