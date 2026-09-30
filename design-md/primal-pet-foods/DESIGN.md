---
version: alpha
name: "Primal Pet Foods"
source_url: "https://primalpetfoods.com"
captured_at: "2026-09-29T03:57:39.273374+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Primal Pet Foods presents a rustic, appetite-forward palette anchored by a warm
  butterscotch brown (#653818) used for links, badges, and body copy, paired with a
  saturated barn-red (#d22730/#d72830 family) reserved for primary calls-to-action and
  the Okendo review-widget buttons. Canvas surfaces read as warm off-whites (#ffffff,
  #f9f9f3, #f4f4ea) rather than clinical white, suiting a farmhouse/ancestral-diet raw
  pet food brand. A soft mint green (#70c497) and a cream button-text tone (#f1f1de)
  appear as supporting accents; their exact usage context is inferred from palette
  adjacency, not confirmed component evidence. Typography is condensed and utilitarian:
  the CSS explicitly names "interstate" as the working UI family (Okendo loyalty title
  rule) alongside a 1.5rem/0.06em body baseline captured directly from the body
  selector. Two display accents carry concrete size evidence — a 6rem "pf-fuel-grime"
  grunge display face for case-study headers and a 5rem cursive "ArtheloRegular" script
  for testimonial headers — both treated here as rare, high-impact flourishes rather
  than default heading fonts. The Okendo review widget's 50px pill buttons and 12/24px
  padding directly informed the rounded and spacing scales below.

colors:
  primary: "#d22730"
  ink: "#653818"
  canvas: "#ffffff"
  body: "#5c332a"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f9f9f3"
  surface-card: "#f4f4ea"
  on-primary: "#f1f1de"
  accent-green: "#70c497"
  accent-yellow: "#fede00"
  surface-cream: "#fff4dc"
  shadow: "#121212"
  focus: "#272d45"
typography:
  display-xl: {fontFamily: "pf-fuel-grime, serif", fontSize: 96px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "ArtheloRegular, cursive", fontSize: 80px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0px}
  title-md: {fontFamily: "interstate-condensed, interstate, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.4px}
  body-md: {fontFamily: "interstate, Assistant, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.53, letterSpacing: 0.96px}
  body-sm: {fontFamily: "interstate, Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.3px}
  caption: {fontFamily: "interstate, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "interstate, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: normal, letterSpacing: 0.4px}
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
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focusBorderColor: "{colors.focus}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-cream}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    cta: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    placeholderColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  subscribe-save-banner:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"

## Components

**button-primary** uses the barn-red (#d22730) directly evidenced by `--color-button` and the Okendo `--oke-button-backgroundColor`, paired with the cream `--color-button-text` (#f1f1de). Pill shape (`rounded.full`) is evidenced by Okendo's 50px `--oke-button-borderRadius`, extended here as the brand's default primary-button radius (proposed extension).

**button-secondary** is a text-forward outline button interpreting the `.buttons span` rule, which shows red (#d22730), 20px, 700-weight, uppercase text — likely a link-style or outline CTA on light backgrounds. Border and pill radius are proposed for visual parity with button-primary.

**text-input** is proposed; no form-field CSS was supplied. Colors are drawn from the neutral surface/hairline tokens for plausibility; focus ring color is inferred from the unused navy (#272d45) in the palette, not confirmed against any observed `:focus` rule.

**nav-bar** reflects the header/menu structure implied by the page text (Shop, Learn, Rewards, country selector) using canvas background and ink text consistent with `--color-foreground`. Sticky behavior and exact height are not observed and are proposed.

**product-card** proposes a warm off-white card (`surface-card`) for dog/cat recipe and treat listings, with price rendered in the primary red to match the button system. Card border and radius are proposed; no `.card` selector was present in evidence.

**hero** proposes a cream (`surface-cream`) banner section using the cursive display accent for a seasonal or testimonial-style headline, echoing the `.testimonial-header__text h2` rule's 5rem cursive treatment, though its actual placement (homepage hero vs. testimonial block only) is not confirmed.

**footer** inverts the palette (ink background, cream text) as an inferred pattern common to earthy/kraft brand footers; no footer-specific selector was supplied, so background choice is a stylistic proposal rather than an observation.

**badge** is the most directly evidenced component: `--color-badge-foreground`, `--color-badge-background`, and `--color-badge-border` map exactly to ink-on-white with an ink border, likely used for trust marks (e.g., "Free Shipping," "USDA," ingredient callouts).

**search** proposes a pill-shaped input consistent with the country/currency selector list visible in the page text; no dedicated search-bar CSS was supplied.

**subscribe-save-banner** is the category-specific component, reflecting the observed promo copy ("HELLO20," "Free Shipping on Orders Over $50," "Subscribe & Save") common to raw pet food replenishment models. Yellow (#fede00) is proposed as an attention accent since it appears in the palette but was not tied to a specific promo-banner selector in the supplied CSS.

## Responsive Behavior

This table is a recommendation based on standard e-commerce patterns; no media queries or breakpoint values were present in the supplied CSS evidence.

| Breakpoint | Width      | Nav behavior              | Grid              |
|------------|------------|----------------------------|-------------------|
| Mobile     | <768px     | Collapsed hamburger menu   | 1-column stacks   |
| Tablet     | 768–1023px | Condensed horizontal nav   | 2-column product grid |
| Desktop    | ≥1024px    | Full mega-menu (Shop/Learn)| 3–4 column product grid |

Touch targets should be a minimum of 44×44px for cart, quantity, and nav controls; this is a general accessibility recommendation, not a measured site value. Mobile filter/sort controls are assumed to collapse into a drawer or accordion, consistent with common Shopify-theme conventions, but this was not observed in the supplied markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS custom-property and selector evidence only; no rendered layout, DOM structure, or interaction states (hover, focus, active, disabled) were directly observed beyond the Okendo widget's documented hover/active variables. Font availability and licensing for "interstate," "pf-fuel-grime," "ArtheloRegular," and "brother-1816" were not verified — these may be paid/licensed fonts (e.g., interstate is a well-known commercial typeface) and are named here only because they appear in the supplied `font-family` values. Most spacing values beyond the Okendo-derived 12px/24px padding are proposed defaults, not measured. Component definitions for footer, hero, search, and text-input are largely inferred from category convention and the limited palette/typography evidence, and should be validated against live rendered pages before implementation. Color role assignments (e.g., which off-white is "canvas" vs. "surface-soft") are best-effort groupings of visually similar hex values, not confirmed against explicit CSS variable names in all cases.
