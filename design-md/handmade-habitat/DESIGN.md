---
version: alpha
name: "Handmade Habitat"
source_url: "https://handmadehabitat.co"
captured_at: "2026-09-28T04:41:16.045561+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Handmade Habitat's storefront evidence shows a warm, muted palette built from
  a soft blush pink (#edbcb5), a terracotta/rose button and link color
  (#c16f64), a deeper clay accent (#854435), and a warm off-white canvas
  (#faf8f5) paired with a near-black foreground text color (#232323, derived
  from the rgb(51,51,51) CSS custom property). A teal/blue (#1990c6, darkening
  to #136f99 on hover) appears only on Shopify's accelerated-checkout button
  and is treated as a vendor-controlled utility color rather than a brand
  color. The only evidenced font family is "Cormorant," a serif, used site-wide
  per the CSS variables for both heading and body font-family declarations; no
  second family was observed, so body and caption sizes reuse Cormorant with a
  generic serif fallback, labeled inferred for weight/size scaling. Buttons
  render with sharp/minimal radius per observed CSS (border-radius largely
  unset or 0), so the interpretation favors restrained, low-radius geometry
  with soft-goods warmth: gentle blush surfaces, terracotta calls-to-action,
  and generous letter-spacing consistent with the 0.06rem tracking rule found
  in base.css. All layout, spacing, and breakpoint values below are proposed
  conventions, not measured observations.

colors:
  primary: "#c16f64"
  ink: "#232323"
  canvas: "#faf8f5"
  body: "#1c1c1c"
  muted: "#854435"
  hairline: "#dedede"
  surface-soft: "#edbcb5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#1990c6"
  accent-teal-hover: "#136f99"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "Cormorant, serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Cormorant, serif", fontSize: 34px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Cormorant, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.06rem}
  body-md: {fontFamily: "Cormorant, serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Cormorant, serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  caption: {fontFamily: "Cormorant, serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.08rem}
  button-md: {fontFamily: "Cormorant, serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.06rem}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
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
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.muted}"
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
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  scent-swatch:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xs}"

## Components
**button-primary** uses the observed rose/terracotta button color (rgb 193,111,100 → #c16f64) with a white-ish text color, matching the `--color-button` and `--color-button-text` variables; radius is set to none since the shared `.button` rule shows no explicit radius token evidenced beyond a generic `--buttons-radius-outset` variable, so sharp edges are the safer default.

**button-secondary** mirrors Shopify's `.button--secondary` pattern (swapping to `--color-secondary-button`/text), rendered here as an outlined terracotta-on-cream style; the border-only treatment is proposed since no fill was evidenced for secondary actions.

**text-input** is a proposed pattern for newsletter/search fields; only a hairline border color (#dedede) and card-white background are evidenced from the skeleton/payment CSS, so field chrome itself is inferred from general Shopify theme conventions.

**nav-bar** reflects the site's flat, cream-background header implied by `--color-background: 250,248,245`; the multi-market/currency selector text seen in the excerpt suggests a compact, small-type utility row above the main nav, proposed as body-sm scale.

**product-card** follows the `.product-card-wrapper .card` custom-property scaffold (border-radius, border-width, shadow, image-padding all theme-driven but unset numerically in evidence), so a light border and minimal radius are proposed defaults for the candle/soap grid seen in the text excerpt (e.g., "Lavender Eucalyptus Soy Wax Candle Jar").

**hero** uses the blush surface-soft tone as a full-bleed banner background behind seasonal campaigns like "Fresh Air & Flowers in Bloom," with display-xl Cormorant serif type; exact hero height/typography scale is not measured and is proposed.

**footer** is proposed with the deeper clay (#854435) as a grounding background for the "Subscribe to our emails" and payment-icon row referenced in the text; contrast with white text is inferred, not confirmed by direct footer CSS.

**badge** covers "Sold out" / "Going Going Gone" labeling implied by the product excerpt; pill shape and outlined ink border reuse the `--color-badge-*` variables from `:root`.

**search** is a proposed pill-style search affordance consistent with the header's "Search" link seen repeatedly in the nav text; no search-input CSS was directly evidenced.

**scent-swatch** is a category-appropriate proposed component for displaying candle/soap scent options (e.g., "Rosemary Mint," "Geranium Lavender") as small circular color chips using the blush palette, since swatch-specific CSS was not present in evidence.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column product grid, stacked nav collapses to hamburger/drawer |
| Tablet | 600–959px | 2-column product grid, condensed nav |
| Desktop | 960–1279px | 3–4 column product grid, full nav visible |
| Wide | 1280px+ | Max-width content container, generous side padding |

Touch targets should be at least 44×44px for buttons and nav links, consistent with the accelerated-checkout button's `clamp(25px, …, 55px)` sizing hint found in evidence. Mobile nav collapse into a drawer/hamburger pattern is standard for this Shopify theme family but was not directly observed in the supplied CSS or markup, so it is a recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, interaction states (hover/focus/active beyond the one evidenced checkout-button hover), or mobile layout were directly observed. Only one font family ("Cormorant") was present in evidence, so body, caption, and button typography all reuse it with an inferred generic serif fallback rather than a confirmed separate body font — actual live typography may differ. All pixel sizes, spacing scale values, radius values, and breakpoints are proposed conventions, not measured from the live site. The teal accent (#1990c6/#136f99) originates from Shopify's portable-wallets CSS and is treated as vendor UI, not confirmed brand color. Custom font licensing/hosting for Cormorant was not verified. Semantic color role mapping (e.g., which hex serves "muted" vs "surface-soft") is inferred from variable names and usage context, not confirmed via visual inspection.
