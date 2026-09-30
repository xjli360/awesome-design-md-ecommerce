---
version: alpha
name: "Monos"
source_url: "https://monos.com"
captured_at: "2026-09-28T05:02:59.868418+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Monos presents hard-shell luggage and travel goods through a restrained,
  neutral palette anchored by dark greys (#4d4d4d, #1a1a1a) against white and
  off-white surfaces (#ffffff, #f7f7f7, #f5f4f2). Observed CSS from the Okendo
  reviews widget confirms #4d4d4d as a functional button/text color and
  #e5e5eb / #dbdde4 as hairline/border tones, which this spec generalizes into
  a site-wide neutral system since no separate storefront theme CSS was
  supplied. Two font families are directly observed: Cabin (sans-serif,
  used for uppercase, letter-spaced buttons at font-weight 700) and Vollkorn
  (serif, present in the family list alongside Vollkorn SC and Baskerville).
  This spec assigns Cabin to UI, body, and button text — matching its
  confirmed observed usage — and infers Vollkorn as the editorial/display
  serif for headings, a common premium-DTC pairing but not directly proven
  from a heading selector in the evidence. Accent hues (#d02e2e red,
  #1e8f4b green, #ffb829 amber, #002e5c navy) appear in the raw palette
  without confirmed selectors; they are mapped here to sale, success,
  warning, and an accent/collection role respectively, labeled inferred.
  Corner radius (4px) and 1px borders are taken directly from Okendo button
  tokens and extended as the base rounding scale for the brand.

colors:
  primary: "#4d4d4d"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#4d4d4d"
  muted: "#6f7375"
  hairline: "#e5e5eb"
  surface-soft: "#f7f7f7"
  surface-card: "#f5f4f2"
  on-primary: "#ffffff"
  accent-sale: "#d02e2e"
  success: "#1e8f4b"
  warning: "#ffb829"
  accent-navy: "#002e5c"
  border-strong: "#dbdde4"
  text-secondary: "#676986"
typography:
  display-xl: {fontFamily: "Vollkorn, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Vollkorn, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Cabin, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Cabin, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Cabin, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Vollkorn SC, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.1em}
  button-md: {fontFamily: "Cabin, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2em, textTransform: uppercase}
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
    hover: "background-color darkens to {colors.ink}, proposed"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  color-swatch-selector:
    size: "24px, proposed"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedState: "2px ring in {colors.primary}, proposed"
    typography: "{typography.caption}"

## Components
**button-primary** is modeled directly on the Okendo review-widget button, which uses a `#4d4d4d` fill, white text, uppercase Cabin at 700 weight with wide letter-spacing, and a 4px radius — extended here as the storefront's primary call-to-action (e.g. "Add to Cart," "Shop the Collection").

**button-secondary** is a proposed outline variant using the same border tone (`#dbdde4`) seen in the Okendo border token, for lower-emphasis actions like "Compare Sizes" or filter toggles.

**text-input** is inferred for search fields, newsletter signup, and account forms; padding and radius are proposed since no explicit input CSS was captured.

**nav-bar** reflects the deep navigation structure evident in the page text (Luggage, Bags, Wallets, Sunglasses, Accessories mega-menus); a white background with dark-grey text and a thin hairline border is proposed as the resting state, with dropdown/mega-menu behavior not observed.

**product-card** is proposed for grid listings (Carry-On $275, Best Sellers, New Arrivals), using the softer `#f5f4f2` surface as a card background against the white page canvas to create separation, per common PDP-grid conventions rather than confirmed layout CSS.

**hero** uses the near-black `#1a1a1a` as a full-bleed background for campaign moments like "The journey ahead" video hero, with the large Vollkorn display type for tagline copy; video/media treatment is referenced in page text but not styled in supplied CSS.

**footer** groups store-locator and contact content (hello@monos.com, social links, multi-region store list) on the soft `#f7f7f7` surface with muted `#6f7375` text, matching the muted tone used in Okendo's date/helpful-vote text.

**badge** is proposed for promotional flags such as "15% off best sellers" or sale tags, using the observed red `#d02e2e` as an attention accent since it appears in the raw palette without a confirmed non-widget selector.

**color-swatch-selector** is a category-appropriate component for luggage/bag color options (evidenced by `.swatch__color[title^="Moss"]` targeting `#544F3A`); rendered as small circular swatches with a primary-color selection ring, sizing and states proposed.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Range | Nav | Grid |
|---|---|---|---|
| mobile | <768px | Hamburger + slide-out menu, proposed | 1-column product grid |
| tablet | 768–1199px | Condensed horizontal nav, proposed | 2-column product grid |
| desktop | ≥1200px | Full mega-menu nav, proposed | 3–4 column product grid |

Touch targets should be ≥44px for buttons and swatches. Mega-menu collapse to accordion on mobile is proposed given the deep category structure implied by the page text, but no responsive CSS or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from a partial CSS extraction dominated by the Okendo third-party reviews widget rather than Monos's core theme stylesheet; core layout, grid, and heading selectors were not directly observed. Font-role assignment (Vollkorn for display, Cabin for body/UI) is inferred from family-name presence and one confirmed Cabin button rule — actual heading font usage is unverified. Several palette colors (`#d02e2e`, `#1e8f4b`, `#ffb829`, `#002e5c`, `#544f3a`) lack confirmed component selectors and are mapped by plausible convention only. All spacing values, the responsive breakpoint table, hover/focus/active states beyond the Okendo button, and mobile navigation behavior are proposed, not measured. Custom font licensing and self-hosting/availability for Cabin and Vollkorn were not verified from the supplied evidence.
