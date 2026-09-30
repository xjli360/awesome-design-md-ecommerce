---
version: alpha
name: "Bessie + Barnie"
source_url: "https://bessieandbarnie.com"
captured_at: "2026-09-28T10:32:59.079809+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bessie + Barnie is a Shopify-based storefront for custom-made, hand-stitched
  dog beds and pet furnishings. The observed CSS exposes a neutral Dawn-theme
  foundation (near-black foreground, white background, Bootstrap-style utility
  colors for alerts and form states) layered with a single warm brand accent:
  the review-widget gold, #ffc500, reused here as the primary interactive
  color since no other saturated hue recurs with comparable weight. Ink and
  body tones are inferred from the theme's foreground/muted grays rather than
  a bespoke palette, reflecting a utilitarian Shopify build rather than a
  fully custom brand system.
  Typography draws on two observed font families: Platypi (Regular,
  SemiBold, ExtraBold) for headings, giving the plush, "luxury pet product"
  positioning a soft serif-adjacent display voice, and Poppins (Light,
  Regular, Medium, SemiBold, Bold) for body copy, UI labels, and buttons.
  Open Sans and Assistant appear in the evidence but are treated as secondary
  fallbacks since their usage context is not confirmed. Font sizes beyond the
  observed 1.5rem body base and letter-spacing 0.06rem are proposed to build
  a coherent scale. All colors below are drawn directly from the supplied
  palette; no brand hue has been assumed from outside evidence.

colors:
  primary: "#ffc500"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#000000"
  accent-navy: "#1e4455"
  accent-clay: "#30291c"
  warning: "#ffc107"
  danger: "#dc3545"
  success: "#198754"
  focus-ring: "#86b7fe"
  border-strong: "#adb5bd"
typography:
  display-xl: {fontFamily: "Platypi-ExtraBold, serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Platypi-SemiBold, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Platypi-Regular, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins-Regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.3px}
  body-sm: {fontFamily: "Poppins-Regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  caption: {fontFamily: "Poppins-Light, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Poppins-SemiBold, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    focusBorder: "{colors.focus-ring}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    overlayColor: "{colors.accent-navy}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  fabric-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    activeBorder: "{colors.primary}"
    rounded: "{rounded.xs}"
    swatchSize: "{spacing.xl}"
    labelTypography: "{typography.caption}"

## Components
**button-primary** is proposed for primary conversion actions (Add to Cart, Check Out), using the review-widget gold as the sole saturated accent against dark on-primary text; hover/active states are proposed, not observed. **button-secondary** offers an outlined ink-on-white variant for tertiary actions like "Shop Collection," matching the theme's `--color-secondary-button` pairing seen in the CSS variables. **text-input** follows the Bootstrap-derived form palette (hairline border, blue-tinted focus ring at `#86b7fe`) implied by the alert/validation colors present in the evidence, though no live form markup was inspected. **nav-bar** is inferred from the extensive mega-menu text content (Dog Beds, Accessories, Harnesses, Collections) and assumes a white bar with ink text and a bottom hairline; sticky/collapse behavior is not confirmed. **product-card** proposes a bordered, softly padded card for bed/collection tiles referenced in the copy ("Bagel Beds," "Rectangle Beds"), using theme border-radius variables (`--product-card-corner-radius`) as directional evidence that cards are intentionally styled, though the radius value itself was not resolved. **hero** models the homepage banner ("Plush, Comfortable, & Durable Dog Beds") using the black `.banner__buttons` background rule as the closest observed evidence of a dark hero treatment. **footer** is proposed as a light, muted-text region housing Support/Care links, consistent with the large footer link list in the page text. **badge** supports trust markers such as "Free U.S. Shipping," "10,000+ happy customers," and "Machine Washable," styled as a pill outline per the badge CSS variables (`--color-badge-*`) defined at root. **search** is a proposed lightweight input matching the text-input treatment. **fabric-swatch-selector** is a category-specific proposed component for the site's core customization workflow (matching bed/blanket/pillow fabrics, monogram add-ons); its active state uses the primary gold as a selection indicator, since no swatch-specific CSS was present in the evidence.

## Responsive Behavior
This is a proposed breakpoint table, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <750px | Single-column product grid, nav collapses to hamburger + drawer menu |
| Tablet | 750–989px | 2-column product grid, mega-menu may remain collapsed |
| Desktop | ≥990px | Full mega-menu nav, 3–4 column product grid, sticky header optional |

Touch targets should maintain a minimum 44×44px hit area for buttons and swatches, consistent with the `clamp(25px, ..., 55px)` button sizing observed in the accelerated-checkout CSS. Mobile nav is assumed to collapse into a drawer given the extensive multi-level menu content (Dog Beds, Accessories, Harnesses, Collections); no mobile interaction was directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were observed. The mapping of Platypi to headings and Poppins to body/button text is inferred from font-family naming conventions and typical Shopify theme pairing, not from confirmed selector-to-element bindings. The primary accent (#ffc500) is sourced from the Judge.me review-widget variables and may not represent the brand's actual primary CTA color elsewhere on the site. All pixel sizes in the typography scale beyond the observed `1.5rem` body base and `0.06rem` letter-spacing are proposed, not measured. Rounded and spacing scales are template defaults, not extracted radius/spacing values (theme radius variables like `--product-card-corner-radius` exist but their resolved values were not in evidence). Mobile layout, hover/focus states, and swatch/selector interactions are entirely proposed. Font licensing and availability for Platypi and Aeonik Pro were not verified and may require confirmation before implementation.
