---
version: alpha
name: "Blunt Umbrellas"
source_url: "https://bluntumbrellas.com"
captured_at: "2026-09-28T04:37:27.157291+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Blunt Umbrellas' storefront draws from a restrained neutral system anchored by a dark charcoal
  (#262525) body-text color and near-black (#232323) button surfaces, set against white and
  light-grey (#F1F1F1) canvases, with thin (#CACACA, #EBEBEB) hairlines separating content — all
  directly observed as CSS custom properties in the theme's main.css. Interactive elements use a
  firm, squared-corner button (5px radius) that inverts from dark-on-light to light-on-dark on
  hover, suggesting a confident, engineering-forward tone consistent with the site's "Engineering
  joy" tagline. Typography is set in a proprietary "Blunt" family (declared via --font-blunt)
  falling back to sans-serif, rendered at medium (500) body weight and semi-bold (600) for buttons
  and headings; the 14px/18px button spec is directly observed, while other sizes are proposed and
  not measured. The broader supplied palette contains a wide spread of saturated hues (yellows,
  blues, reds, greens, purples) that most plausibly represent product/umbrella-canopy color
  swatches rather than core UI chrome; these are treated here as accent/swatch tokens, inferred,
  not brand primaries. The resulting interpretation favors a monochrome, editorial UI shell —
  charcoal ink, white/light-grey surfaces, hairline dividers — that lets colorful umbrella imagery
  and swatches supply visual vibrancy against a quiet, functional interface.

colors:
  primary: "#232323"
  ink: "#262525"
  canvas: "#ffffff"
  body: "#262525"
  muted: "#777c79"
  hairline: "#cacaca"
  hairline-soft: "#ebebeb"
  surface-soft: "#f1f1f1"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-yellow: "#facc52"
  accent-blue: "#1a428a"
  accent-red: "#da1f2b"
  overlay-scrim: "#00000040"
typography:
  display-xl: {fontFamily: "Blunt, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Blunt, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Blunt, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Blunt, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Blunt, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Blunt, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Blunt, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 18px, letterSpacing: 0.2px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    swatchSize: "32px"
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    gap: "{spacing.sm}"

## Components

button-primary is the site's principal call-to-action (add-to-cart, checkout), directly modeled on the observed `.button` / `.primary-button--dark` rules: a solid near-black fill, white text, 5px rounding (approximated here to `rounded.sm`), and an observed hover state that flips to a white background with charcoal text. This inversion pattern is confirmed in CSS and can be reused across all solid buttons.

button-secondary reflects the observed `.secondary-button--outline-dark` rule: a transparent fill with a light hairline border and charcoal text, intended for lower-emphasis actions (e.g., "learn more," size guide). Its hover treatment is proposed, not observed, but likely mirrors the primary button's fill-on-hover convention.

text-input is a proposed pattern for search fields, forms, and newsletter capture, inferring a white background, hairline border, and charcoal text consistent with the theme's neutral CSS variables; no explicit form-input CSS was supplied.

nav-bar reflects the observed `--nav-main-height: 60px` variable, implying a fixed-height header; background and hairline-bottom treatment are inferred from the theme's light-grey/hairline palette rather than directly observed nav styles.

product-card is a proposed container for umbrella listings, using a white surface, thin hairline border, and generous internal padding to let product photography and colorful canopy swatches stand out against the neutral shell.

hero is a proposed full-width introductory section using the light-grey surface and largest display type, intended to carry brand messaging such as "Engineering joy"; no hero-specific CSS was supplied, so structure and copy treatment are inferred from general Shopify-theme conventions.

footer is proposed as a dark, ink-colored band with white text and small body type, contrasting the otherwise light UI to anchor the page and house secondary navigation/legal links; not directly observed.

badge is a small pill-shaped label using the accent-yellow swatch color, proposed for "new," "sale," or "bestseller" tags; color choice is inferred from the palette's most saturated warm accent rather than confirmed brand usage.

search is a proposed input variant styled like text-input but embedded in the nav-bar, using the light-grey surface to differentiate it from the page background.

color-swatch-selector is a category-specific, proposed component for choosing umbrella canopy colors: small circular swatches with a hairline border that thickens/darkens to the ink color when selected, sized for comfortable tap targets; swatch fill colors are drawn from the broader saturated palette (yellow, blue, red, green, purple) observed in the raw CSS extraction.

## Responsive Behavior

The following breakpoint table is a proposed recommendation only; no responsive/mobile layout was directly observed in the supplied CSS.

| Breakpoint | Width       | Behavior (proposed)                                  |
|------------|-------------|-------------------------------------------------------|
| mobile     | < 480px     | Single-column stacking; nav collapses to hamburger menu |
| tablet     | 480–1024px  | Two-column product grids; nav-bar remains fixed at 60px |
| desktop    | > 1024px    | Multi-column grids; full horizontal nav-bar with inline search |

Touch targets should maintain a minimum of 44px in the tallest dimension, consistent with the accelerated-checkout button's `clamp(25px, …, 55px)` sizing observed in Shopify's payment-button CSS. Navigation collapse behavior, swatch-selector tap sizing, and card-grid column counts are proposed conventions, not measured from live site rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction only; no rendered page, viewport, or interaction was observed. The proprietary "Blunt" font's availability, licensing, weights, and fallback rendering were not verified beyond its declaration in `--font-blunt`. Most typography sizes (display, title, body scale) beyond the confirmed 14px/18px button spec are proposed placeholders, not measured values. The wide array of saturated colors in the supplied palette (yellows, blues, reds, greens, purples) is inferred to represent product/umbrella-canopy swatches rather than core brand UI colors, but this mapping is not confirmed by selector context. Hover, focus, active, disabled, and error states for inputs, nav, and search are proposed and unobserved. Mobile menu behavior, breakpoint values, and grid column counts are recommendations only. Border-radius on buttons (5px observed) was approximated to the nearest token in the proposed rounded scale rather than added as a bespoke value.
