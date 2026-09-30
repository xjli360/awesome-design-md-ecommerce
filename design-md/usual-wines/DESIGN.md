---
version: alpha
name: "Usual Wines"
source_url: "https://usualwines.com"
captured_at: "2026-09-28T09:47:12.474797+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Usual Wines presents itself through a warm, paper-like canvas (#fffcf0) paired
  with near-black ink and charcoal buttons (#252525), evidence from the theme's
  root CSS variables (--color-background: 255,252,240; --color-button: 37,37,37;
  --color-button-text: 255,255,255). The palette otherwise draws from a cluster
  of soft creams (#f6f6ed, #f2efe4, #eeeeee) for section backgrounds, cool grays
  (#cccccc, #dedede, #e9e9e2) for hairlines and skeleton loading states, and a
  small set of saturated accents — a warm gold pair (#fade9a, #f8ddb0), a coral
  pair (#ff3d3d, #ff5c60), a deep red (#9b2121), and a blue pair (#1990c6,
  #136f99) used on Shopify's native accelerated-checkout button. None of these
  accents is explicitly labeled "brand primary" in the CSS, so their assignment
  to badges, sale states, and secondary CTAs below is inferred from typical
  Shopify Dawn-theme usage, not confirmed styling.
  Typography relies on the single observed family "Assistant" with sans-serif
  fallback; JudgemeStar is a review-widget icon font, not a text typeface, and
  is excluded from prose typography. All pixel sizes, weights, rounding, and
  spacing values below are proposed conventions unless the CSS literally states
  them (e.g., body font-size 1.5rem, button font-size 1.5rem), since root
  font-size scaling was not confirmed.

colors:
  primary: "#252525"
  ink: "#121212"
  canvas: "#fffcf0"
  body: "#252525"
  muted: "#cccccc"
  hairline: "#dedede"
  surface-soft: "#f2efe4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#ff3d3d"
  accent-alt: "#ff5c60"
  sale: "#9b2121"
  badge-warm: "#fade9a"
  badge-warm-soft: "#f8ddb0"
  link-blue: "#1990c6"
  link-blue-hover: "#136f99"
  navy: "#242833"
  cream-alt: "#f6f6ed"
  border-soft: "#e9e9e2"
typography:
  display-xl: {fontFamily: "Assistant, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Assistant, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.96px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0.96px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  caption: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.5px}
  button-md: {fontFamily: "Assistant, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.96px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "{colors.hairline}"
    height: "72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    newVariant:
      backgroundColor: "{colors.badge-warm}"
      textColor: "{colors.ink}"
    soldOutVariant:
      backgroundColor: "{colors.sale}"
      textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  review-rating:
    starColor: "{colors.badge-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconFont: "JudgemeStar"
  single-serve-info-chip:
    backgroundColor: "{colors.cream-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** reflects the theme's `--color-button` (#252525) and `--color-button-text` (white) variables, used for calls-to-action such as "Shop best sellers." Hover/active shading is proposed, not observed.

**button-secondary** mirrors the theme's `--color-secondary-button` pairing (canvas background, dark border/text), intended for lower-emphasis actions like "Log in." Border opacity follows the `--alpha-button-border` pattern present in base.css but exact percentage is not confirmed.

**text-input** is a proposed pattern for search/email capture (the mailing-list signup mentioned in copy). Border and radius values are inferred defaults, not measured from a rendered form.

**nav-bar** assumes a canvas-colored sticky header consistent with the flat, cart-drawer-driven navigation implied by the "Shop All / Our wines / New Arrivals / Last Chance" menu structure in the evidence; sticky behavior is proposed.

**product-card** is inferred from `.product-card-wrapper .card` custom-property hooks (corner radius, border, shadow, image padding) in base.css, applied to bottle SKUs like "Select Rosé" and "Brut Bottle," including a review count line.

**hero** proposes a full-width introductory section using the canvas/gradient-background color and a large display heading, matching the tagline "Wine you can feel good about."

**footer** groups About/Blog/Reviews/Policy links and social icons noted in the page text, set on a soft cream surface for visual separation from the main canvas; exact column layout is not observed.

**badge** covers "NEW" and "SOLD OUT" labels seen repeatedly in navigation and product-list copy; warm gold signals novelty while the deep red communicates unavailability, both inferred pairings.

**review-rating** supports the frequent "4.87 / 5.0 … total reviews" strings, using the observed JudgemeStar icon font for star glyphs alongside numeric caption text.

**single-serve-info-chip** is a category-specific proposal for recurring product claims ("0g of sugar," "Only 100 calories," "Sustainably farmed") rendered as small inline chips near product cards or the hero.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsible hamburger nav, cart as full-screen drawer |
| tablet | 600–1023px | 2-column product grid, nav links may wrap into a secondary row |
| desktop | ≥1024px | 3–4 column product grid, persistent horizontal nav with mega-menu dropdowns |

Touch targets for buttons and nav items should be at least 44×44px. Mega-menu categories ("Our wines," "New Arrivals," "Last Chance") should collapse into accordions below tablet width. All figures are proposed conventions.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- This document is derived from static CSS/text extraction only; no rendered layout, animation, or interaction was observed.
- The true `--color-foreground` value (rgb 10,10,10 / #0a0a0a) is not present in the supplied palette; `ink` (#121212) is an approximate substitute from the nearest observed swatch.
- Root font-size (and therefore all rem-derived pixel values, including body-md at 1.5rem) is assumed at a 16px baseline; the theme may override this via a percentage-based root font-size that was not confirmed in evidence.
- Border-radius values for buttons and cards rely on CSS custom properties (`--buttons-radius-outset`, `--product-card-corner-radius`) whose resolved pixel values were not supplied; the `rounded` scale here is a proposed convention only.
- Accent color roles (accent, sale, badge-warm, link-blue) are inferred from common Shopify Dawn-theme usage patterns and general context clues in the page copy (e.g., "SOLD OUT," "NEW"), not from confirmed component screenshots.
- Font weights for headings and buttons are not explicitly numbered in the supplied CSS beyond variable references (`--font-heading-weight`, `--font-body-weight`); numeric values used here are proposed.
- Custom font availability, licensing, and full character support for "Assistant" were not verified; "JudgemeStar" is a third-party review-widget icon font, not applicable to running text.
- Mobile menu, cart-drawer, and skeleton-loading interaction states are inferred from CSS class names (e.g., accelerated-checkout skeleton styles) rather than observed runtime behavior.
