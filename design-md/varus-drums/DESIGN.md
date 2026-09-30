---
version: alpha
name: "Varus Drums"
source_url: "https://www.varusdrums.com"
captured_at: "2026-09-28T10:10:53.880470+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Varus Drums is a custom drum-building workshop selling handmade snares and
  full kits (Mantovani Custom, Morpheus Wood/Acrylic, Power, Agile series) via
  a WooCommerce/WordPress storefront. The supplied CSS evidence is dominated by
  WordPress/Gutenberg default tokens (--wp-admin-theme-color, block-editor
  palette swatches) rather than bespoke brand styling, so most color-to-role
  assignments below are inferred rather than observed in a rendered layout.
  Confirmed functional values include a light neutral surface (#f2f2f2), a
  dark neutral surface (#313131/#eeeeee pairing from has-very-light/dark-gray
  utility classes), a near-black icon tone (#333333), an orange icon accent
  (#e67e22) used on a floating add-to-cart/mini-cart plugin, and transparent
  fills (#ffffff00) on hover states. Typography evidence is limited to "Open
  Sans" and Arial with sans-serif fallback, consistent with a WooCommerce
  theme default stack rather than a custom brand typeface.
  This interpretation treats the orange as the brand accent (workshop/craft
  warmth fitting hand-built instruments), pairs it with dark charcoal ink and
  clean white/light-gray surfaces for a workshop-catalog feel, and reserves the
  observed reds/blues as secondary status colors. All spacing, radius, and
  component sizing values are proposed conventions, not measured from the
  live site.

colors:
  primary: "#e67e22"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#878787"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-dark: "#313131"
  danger: "#bf0000"
  link: "#0c4da2"
  transparent: "#ffffff00"
typography:
  display-xl: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: "0px"}
  caption: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: "0.4px"}
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
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  finish-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** uses the orange accent (`#e67e22`) as a call-to-action fill, the only accent color tied to an observed interactive rule (icon/hover state on the site's add-to-cart plugin). Proposed for "Add to cart," "Quote," and "Order" actions.

**button-secondary** is a transparent/outline treatment reflecting the observed `background-color:#fff0` and `border-color:#fff0` hover pattern on plugin buttons, reinterpreted here as a low-emphasis outlined button using the hairline gray border. Proposed, not confirmed as a general site pattern.

**text-input** is a proposed neutral field style (white background, light hairline border) for search, quote-request, and account forms; no input-specific CSS was present in evidence.

**nav-bar** models the multi-level menu structure implied by the page text (About Us, Artist, Snares, Drums, Shop, How to Order, Official Partners), using white canvas and dark ink text with an orange hover state; exact bar height/behavior is not observed.

**product-card** represents the shop grid items visible in the text excerpt (Purple Lava Drumkit, Ocean Exotic Kit, snares with EUR pricing), using a light card surface and hairline border; imagery, spacing, and hover elevation are proposed.

**hero** proposes a dark full-bleed band (`accent-dark` background) for the "We build your dreams" tagline area, using the large display type scale; actual hero background/imagery was not observed.

**footer** reuses the same dark surface for the footer region (Shop Policies, Business Information, social links, currency selector), with orange used sparingly for links; content list is drawn from the page-text excerpt, not from styled CSS.

**badge** is a proposed sale/status indicator using the strongest observed red (`#bf0000`) from the palette, useful for "Sold," "New," or currency/region flags; no badge markup was present in evidence.

**search** models the "Products search" field referenced in the page text, using the light gray surface tone observed on the plugin popup header background.

**finish-swatch** is a category-specific component proposed for selecting shell/finish/hardware options central to the Mantovani Custom and Morpheus series ("100% customizable... variety of shell configurations"); rendered as a circular swatch selector with an orange selected-state ring. This pattern is not present in the supplied CSS and is a functional recommendation only.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | 0–599px     | Single-column product grid, collapsed hamburger nav, stacked filters |
| tablet    | 600–959px   | 2-column product grid, nav collapses secondary levels into accordions |
| desktop   | 960–1279px  | 3-column product grid, full mega-menu nav |
| wide      | 1280px+     | 4-column product grid, max content width constrained |

Touch targets should be at least 44×44px for cart/quote buttons and swatch selectors. Multi-level menus (Artist, Drums, Snares sub-items) should collapse to expandable accordions below tablet width. All of the above is a UX recommendation, not an observation of the live responsive implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically; no rendered layout, computed spacing, or true breakpoints were observed.
- The majority of the supplied color palette matches default WordPress/Gutenberg editor swatches (e.g. `#cf2e2e`, `#ff6900`, `#fcb900`, `#7a00df`, `#00d084`) rather than confirmed brand colors; only `#e67e22`, `#333333`, `#515151`, `#f2f2f2`, `#313131`/`#eeeeee` and `#ffffff00` had direct functional CSS rules, and even those originate from a cart/popup plugin rather than core brand chrome.
- Typography is limited to two generic families (`Open Sans`, `Arial`) with no evidence of a licensed or custom display typeface; heading/body size values are proposed, not measured.
- Component states (hover, focus, disabled, error) beyond the transparent-background hover rule are proposed conventions.
- Mobile menu behavior, cart drawer interaction, and finish-swatch/configurator UI are inferred from page-text content (mentions of customization and shop categories), not from observed markup or scripts.
- Font licensing/availability for "Open Sans" was not verified against the live site's font-loading method (self-hosted vs. Google Fonts vs. system fallback).
