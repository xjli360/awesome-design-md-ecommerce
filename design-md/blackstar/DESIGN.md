---
version: alpha
name: "Blackstar"
source_url: "https://www.blackstaramps.com"
captured_at: "2026-09-29T04:09:59.592257+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is built from a WordPress/WooCommerce-driven storefront for
  Blackstar Amplification, a UK amp and cabinet manufacturer. The supplied CSS
  exposes very little brand-specific styling beyond WooCommerce and plugin
  defaults, so most semantic color and type assignments here are inferred
  rather than directly observed on the live layout. Structural tones are drawn
  from the neutral end of the palette (#000000, #191919, #333333, #767676,
  #dddddd, #f6f6f6, #f4f4f4) to model a dark-leaning, tone-focused product site
  consistent with a pro-audio catalogue. The only concretely observed
  interactive surface is the WordPress button style (`#32373c` fill, white
  text, pill radius), which is promoted here to the primary action color.
  A red (#bd151d) and status colors (#007518 success, #ffba00 warning,
  #2ea2cc info, #cc1818 destructive) come from WooCommerce theme tokens and
  are repurposed as accent/badge/status colors — their appearance on the
  actual rendered site is not confirmed. Typography uses the two real font
  families present in the evidence, Lato and Open Sans, with an inferred
  heading/body split, since no selector-to-font mapping was supplied. Layout,
  breakpoints and hover states below are proposed conventions for an amp
  catalogue, not measured observations.

colors:
  primary: "#32373c"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent: "#bd151d"
  success: "#007518"
  warning: "#ffba00"
  info: "#2ea2cc"
  destructive: "#cc1818"
  deep-ink: "#000000"
typography:
  display-xl: {fontFamily: "Lato, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lato, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Lato, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.deep-ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.deep-ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  amp-finder-cta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    buttonRounded: "{rounded.full}"
    padding: "{spacing.xl}"

## Components

**button-primary** models the one concrete interactive style in the evidence: a dark slate (`#32373c`) pill-shaped fill with white text, drawn from the WordPress `.wp-block-button__link` rule. Used for primary CTAs like "Electric Amps" or "Amp Finder." Hover/active states are proposed, not observed.

**button-secondary** is an inferred outline variant using the primary color as border and text, for lower-emphasis actions ("Learn more," "See All Series") alongside primary buttons in hero and content blocks.

**text-input** covers newsletter/search/account fields. Border color and 4px radius reference the observed `--wc-form-border-radius: 4px` WooCommerce token; padding and typography are proposed for usability.

**nav-bar** represents the mega-menu header (Products, Amp Finder, Instrument, Series, Support, Dealers, Blog). Background is set to near-black as a plausible dark header treatment; actual header background color was not confirmed in the supplied CSS, only link-color placeholders with empty `color: !important` values.

**product-card** supports catalogue grids (e.g., "Most Popular Products": Beam Mini, Fly 3 High Gain, Artisan 30). Uses the light neutral `surface-card` tone and an 8px radius taken from the observed `--wc-card-border-radius`.

**hero** models the homepage banner pattern (e.g., "Beam Mini," "Doug Aldrich DA5 Ruby") with a dark background and large display type, appropriate for product-hero imagery; exact hero background and image treatment were not present in the evidence and are proposed.

**footer** reflects the multi-column footer content (Amp Finder links, About, Contact, Dealers, social icons, VIP signup form) using the darkest ink tone for strong contrast with white text.

**badge** is proposed for "New" or "Sale" labels on product tiles (e.g., "NEW DOUG ALDRICH DA5 RUBY"), using the accent red pulled from the supplied palette; this red's actual on-site usage is unconfirmed.

**search** models the "open search box" toggle referenced in the nav, styled as a pill input consistent with the button radius token.

**amp-finder-cta** is a category-specific component for the prominent "AMP FINDER" tool repeated in the header, hero, and footer, packaged as a distinct callout block with its own title/body/button treatment.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger, mega-menu becomes accordion | 1-column product cards |
| Tablet | 600–1024px | Condensed horizontal nav, search icon-only | 2-column product/amp grids |
| Desktop | >1024px | Full mega-menu with series/instrument columns | 3–4 column grids |

Touch targets should be at least 44×44px for nav items and buttons given the pill button pattern. Mega-menu columns (Instrument, Product Type, Series) should collapse into stacked accordions below tablet width. None of this was directly observed; it follows standard WordPress mega-menu conventions.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static: no rendered layout, spacing, hover/focus states, or mobile breakpoints were actually observed.
- Most brand colors (accent red, success/warning/info/destructive) originate from WooCommerce default theme tokens, not confirmed brand styling; their real on-site application is unverified.
- Header/nav background, hero background, and footer background colors are inferred from generic dark neutrals in the palette, not confirmed against a captured screenshot.
- Font-to-role mapping (Lato for headings, Open Sans for body) is inferred from the font list; no selector explicitly ties either family to headings or body text.
- Type scale (px sizes, weights, letter-spacing) is proposed, not measured, except for button padding derived from `calc(.667em + 2px)` patterns.
- Custom font licensing/availability was not verified; only generic sans-serif fallbacks are guaranteed.
- Rounded values of 4px and 8px are directly observed (WooCommerce form/card tokens); xs (2px) and lg (16px) are proposed to fill out the scale.
- Spacing scale is a proposed convention, not derived from measured layout gaps.
