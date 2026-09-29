---
version: alpha
name: "Carl Friedrik"
source_url: "https://carlfriedrik.com"
captured_at: "2026-09-28T09:30:14.361791+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Carl Friedrik's supplied evidence shows a neutral, editorial luggage-brand palette built on white canvas (#ffffff), near-black ink (#000000) and a warm mushroom/stone neutral (#dbd5cd) used for borders and soft framing. A rust-orange accent (#c56710) appears as the named `--color-rust` button background paired with white text, making it the clearest observed primary-action color. Secondary UI chrome (from the Okendo reviews widget) contributes a cool slate-blue system — #676986, #272d45, #dbdde4, #e5e5eb, #f7f7f8 — used here for muted text, hairlines and soft surfaces, since no other structural chrome colors were exposed. Product-collection names ("Heritage Cognac," dark olive Ayrton pieces) justify treating #5f261b and #273816 as inferred accent tones for material/colorway badges, not primary UI colors. Typography is the `grotesk` / `grotesk-condensed` family (with generic fallbacks); no numeric type scale was exposed beyond `leading-tight` headings and a ~1.35rem base line-height, so the scale below is proposed and labeled accordingly. Layout is unmeasured from static CSS; the interpretation favors a spacious, full-bleed product-photography grid typical of premium travel-goods retail, with restrained borders (--oke-border-width:1px) and a small 4px corner radius carried from the only observed border-radius token.

colors:
  primary: "#c56710"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#393939"
  muted: "#676986"
  hairline: "#e5e5eb"
  surface-soft: "#f7f7f8"
  surface-card: "#faf8f5"
  on-primary: "#ffffff"
  border-strong: "#dbdde4"
  mushroom: "#dbd5cd"
  heritage-brown: "#5f261b"
  olive: "#273816"
  ink-soft: "#272d45"
typography:
  display-xl: {fontFamily: "grotesk, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "grotesk, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "grotesk-condensed, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "grotesk, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0px}
  body-sm: {fontFamily: "grotesk, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0px}
  caption: {fontFamily: "grotesk, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "grotesk, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    borderColor: "{colors.mushroom}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
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
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  variant-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.muted}"
    activeTextColor: "{colors.on-primary}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** uses the observed rust background/white-text pairing (`.btn-rust`) as the storefront's clearest call-to-action treatment, proposed for "Add to bag" and checkout actions.

**button-secondary** mirrors the observed `.btn-white` rule (white fill, mushroom-toned 1px border, black text), suitable for "Shop now" or filter-toggle actions alongside the primary rust button.

**text-input** is a proposed pattern: full-reset inputs were observed (`border-radius:0`, inherited font), so a sharp-cornered field with a light hairline border is used for newsletter and search fields, consistent with the reset styles.

**nav-bar** is proposed layout scaffolding — no header CSS was captured beyond a `--header-height` custom property reference, so a simple white bar with a bottom hairline is assumed for primary navigation (Luggage / Bags / Accessories).

**product-card** is inferred from the page-text product grid (e.g., "Granville Weekender Sonder Chocolate $945"), using the warm off-white surface-card tone with a condensed title and small price line; no card CSS was directly observed.

**hero** reflects large campaign moments described in page text ("Grand tours await," "The Aluminium"); treated as a dark, full-bleed section with large display type, though imagery and exact copy placement are not confirmed from CSS alone.

**footer** groups the observed COMPANY / CUSTOMER CARE / CONNECT link columns from page text into a plain white footer with muted body text and a top hairline, typography scale proposed.

**badge** is proposed for labeling new colorways (e.g., "New: Olive") using the olive accent pulled from product-name evidence, rendered as a small pill.

**search** is a proposed lightweight input variant using the softer widget-derived surface tone, intended for a header search affordance not directly observed in the supplied CSS.

**variant-swatch-selector** is a category-specific proposed component for the Weekender/Aluminium/Carry-on product options seen in page text (e.g., "Silver / Cognac," "Chocolate / Chocolate"), styled as small rounded chips using the muted slate tone for the active state.

## Responsive Behavior
Proposed breakpoint recommendation (not measured from live rendering):
| Breakpoint | Range | Notes |
|---|---|---|
| sm | 0–639px | Single-column product grid, stacked nav, full-width buttons (`.btn { width:100% }` was observed). |
| md | 640–1023px | Two-column product grid, condensed nav links visible. |
| lg | 1024–1439px | Three/four-column product grid, full header nav. |
| xl | 1440px+ | Max-width content container, generous section padding (`{spacing.section}`). |

Touch targets should target a minimum 44px height for buttons and swatch chips; the `.btn` full-width mobile pattern suggests primary actions collapse to full-bleed on small screens. Navigation collapse (hamburger vs. inline) was not observed and is assumed standard for a Shopify Oxygen storefront.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, active, disabled) were observed beyond the few explicit `:hover`/`:active` custom properties in the Okendo widget block. The `--color-rust`, `--color-mushroom`, `--color-black`, and `--color-white` Tailwind theme variables were referenced by name but not resolved to hex in the supplied evidence; hex mappings above (e.g., primary #c56710, mushroom #dbd5cd) are best-fit inferences from the surrounding palette and product-name context, not confirmed token values. Numeric type scale, spacing scale, and card/hero layout are proposed, not measured. The `bau-medium` font referenced inside the Okendo widget variables belongs to a third-party review widget and was excluded from the brand typography set. Custom font (`grotesk`, `grotesk-condensed`) availability, weights, and licensing were not verified. Mobile navigation, cart drawer, and gallery/carousel behavior were not observed in the supplied evidence.
