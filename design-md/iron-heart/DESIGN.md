---
version: alpha
name: "Iron Heart"
source_url: "https://ironheart.jp"
captured_at: "2026-09-28T04:15:55.052563+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Iron Heart's public CSS shows a stark, high-contrast palette built from
  near-black (#221e1f, #000000) foregrounds against white (#ffffff) and
  off-white (#f9f9f9) surfaces, consistent with a heritage-denim retailer
  that prioritizes product photography over decorative color. Grays
  (#979797, #dddddd, #b5b5b5) appear as supporting neutrals for hairlines
  and muted text. A small set of saturated accents (#db0000, #ed6000,
  #ff7c00) surface in the palette and are treated here as inferred
  sale/badge/hover accents, since their exact usage was not confirmed in
  layout. Two font families are observed: "Fjalla One", a condensed
  display face suited to a rugged, industrial headline voice, and "Noto
  Sans Japanese" for body copy and UI text, reflecting the site's
  Japanese-first audience. This interpretation assigns Fjalla One to
  display/heading roles and Noto Sans Japanese to body, button, and
  caption roles. Buttons are modeled as solid black-on-white with a
  hover-outline treatment matching the observed `:hover:after` box-shadow
  border pattern. Component structure (cards, nav, footer) is proposed
  and not confirmed via rendered layout.

colors:
  primary: "#000000"
  ink: "#221e1f"
  canvas: "#ffffff"
  body: "#221e1f"
  muted: "#979797"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#db0000"
  accent-warm: "#ed6000"
  border-strong: "#b5b5b5"
typography:
  display-xl: {fontFamily: "Fjalla One, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Fjalla One, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Fjalla One, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "Noto Sans Japanese, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.6px}
  body-sm: {fontFamily: "Noto Sans Japanese, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.5px}
  caption: {fontFamily: "Noto Sans Japanese, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Noto Sans Japanese, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.6px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
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
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fabric-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    labelTypography: "{typography.caption}"

## Components

**button-primary** models the observed `.button` rule (`background-color: rgb(var(--color-button))`, `color: rgb(var(--color-button-text))`, `padding:0 3rem`), interpreted as solid black on white with generous horizontal padding for a denim-brand's rugged, utilitarian CTAs. The hover state (proposed) reflects the observed `:hover:after` box-shadow outline rather than a color swap.

**button-secondary** follows the `.button--secondary` variable swap (`--color-button: var(--color-secondary-button)`), producing an inverted white-background/black-text button, useful for "add to wishlist" or secondary catalog actions. Border-only tertiary variants (proposed, not detailed here) would set background alpha to 0 as seen in `.button--tertiary`.

**text-input** is a proposed pattern for search and account forms; no explicit input CSS was supplied, so border and radius values are inferred from the general hairline/rounded-sm system rather than measured.

**nav-bar** is proposed as a white header bar with hairline bottom border, appropriate for a product-photography-forward storefront; sticky/mega-menu behavior was not observed in the supplied CSS.

**product-card** draws on the `.product-card-wrapper .card` rule, which exposes CSS custom properties for radius, border, shadow, and image padding — confirming a card system exists, though exact resolved values were not supplied, so radius/spacing here are proposed defaults.

**hero** is proposed as a dark, full-bleed banner using the ink color and display typography, matching the presence of slideshow sections (`#shopify-section-...__slideshow`) confirmed in the CSS, though their visual composition was not observed.

**footer** is proposed as a dark band mirroring the hero treatment for visual bookending; no footer-specific selectors were supplied.

**badge** reflects the observed `--color-badge-*` variables (`badge-foreground/background/border: 18,18,18 / 255,255,255 / 18,18,18`), giving a pill-shaped outline badge for stock/sale labels.

**search** is a proposed lightweight overlay/bar pattern; not directly evidenced.

**fabric-swatch** is a category-appropriate proposed component for a denim retailer, presenting small bordered material/wash swatches with a caption label; not observed in the supplied CSS.

## Responsive Behavior
This is a recommendation, not measured site behavior — no breakpoints or viewport rules were present in the supplied evidence.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | < 480px    | single-column product grid, nav collapses to hamburger |
| tablet    | 480–959px  | 2-column product grid |
| desktop   | 960–1279px | 3–4 column grid, full nav visible |
| wide      | ≥ 1280px   | max-width content container, 4+ column grid |

Touch targets should be at least 44px in height for buttons and nav links (proposed). Navigation collapse into an off-canvas/hamburger menu below tablet width is a standard Shopify pattern but was not confirmed via observed markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom-property and selector extraction only; no rendered page, computed styles, or DOM screenshots were available. Semantic role assignments (e.g., mapping "#221e1f" to `ink`, or "#db0000"/"#ed6000" to badge/accent roles) are inferred from typical usage patterns and palette proximity to the CSS variable `--color-foreground: 18,18,18`, not confirmed against actual rendered elements. All pixel font sizes are proposed approximations from the observed `1.5rem` body font-size and heading scale variables, since root font-size (rem base) was not confirmed. No interaction states (focus, active, disabled) beyond the single documented button hover box-shadow were observed. Mobile/tablet layout, navigation collapse behavior, and grid column counts were not observed and are proposed conventions only. Availability and licensing of "Fjalla One" and "Noto Sans Japanese" for reuse have not been verified beyond their appearance as declared font-family values in the site's CSS.
