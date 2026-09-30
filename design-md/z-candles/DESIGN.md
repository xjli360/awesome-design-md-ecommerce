---
version: alpha
name: "Z Candles"
source_url: "https://zcandlestudio.com"
captured_at: "2026-09-28T10:09:46.731748+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Z Candles is a Shopify storefront for a hand-poured soy candle and soap
  brand, evidenced by copy describing amber glass vessels, cotton wicks and
  a Lake Oswego "Boutique + Lab." The supplied CSS is theme-driven, routing
  most color and type through custom properties (--color-body,
  --color-btn-primary, --font-stack-header, --font-stack-body) rather than
  literal values, so this spec maps those roles onto the strongest signals
  in the observed palette: a broad neutral scale from near-white
  (#f4f4f4, #f7f7f7) through mid grays (#606060, #685858) to near-black
  (#1c1c1c, #121212), plus a small cluster of deep reds (#651818, #d20000,
  #ea0606) that are the only saturated brand-plausible hues once third-party
  payment/social icon colors (PayPal blue, Mastercard orange/red, Amex teal,
  Pinterest/Facebook marks) are excluded as non-brand.
  Typography is inferred: the single concrete family stack in the CSS is
  HelveticaNeue/Helvetica Neue/Helvetica/Arial/sans-serif, applied here to
  body copy; "Abel" appears in the supplied font list and is treated, as
  inferred, as the probable header/display face for a warm, boutique tone.
  Buttons show a real 2px corner radius and uppercase, letter-spaced labels,
  which this spec generalizes into a restrained, minimally rounded system
  across cards, inputs, and badges.

colors:
  primary: "#651818"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#606060"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#d20000"
  overlay: "#00000099"
typography:
  display-xl: {fontFamily: "Abel, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Abel, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Abel, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Abel, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.08em}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md}"
  scent-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** is proposed as the solid, dark-red call-to-action used for "Add to cart," newsletter submit, and other primary actions, echoing the theme's `--color-btn-primary` variable and observed 2px radius and uppercase, letter-spaced label style.

**button-secondary** is an outlined variant for lower-priority actions ("Continue shopping," "View cart"), sharing the primary's border-radius and type scale but inverting fill, matching the `.btn--secondary` rule's transparent background and inherited border color.

**text-input** covers search and newsletter email fields; background, border, and padding values are proposed defaults consistent with the theme's minimal-radius button system, since no distinct input CSS was supplied.

**nav-bar** represents the sticky/static header holding the "Z CANDLES" wordmark, shop dropdown, search, and cart icon; background-on-canvas and hairline separation are inferred from `.site-header`'s plain background-color rule.

**product-card** is the repeating grid unit for candles, soaps, gift sets, and diffusers; card surface, subtle border, and title/price type pairing are proposed conventions for a Shopify collection grid, not directly observed in the CSS.

**hero** models the homepage "modern candles for cozy spaces" banner, using the soft neutral surface and largest display type; exact hero markup and imagery were not present in the supplied evidence.

**footer** groups newsletter signup, payment-method icons, and social links; muted text on canvas background with hairline dividers is proposed, informed by the generally low-contrast neutral palette.

**badge** (proposed) is a small pill for the cart item count or "sale/new" flags, generalizing the observed `.site-header__cart-count` circular badge (primary background, on-primary text) into a reusable token.

**scent-tag** is a category-specific, fully proposed component for labeling fragrance notes (e.g., "Fig," "Grapefruit," "White Hibiscus") on product detail pages, using a soft neutral pill consistent with the brand's restrained, non-shouty visual tone.

## Responsive Behavior

Recommended, not measured, breakpoints: mobile ≤599px, tablet 600–899px, desktop ≥900px, wide ≥1200px. Nav collapses to a hamburger/drawer pattern below tablet, consistent with the theme's `.site-header__mobile-nav` rule, though exact trigger width was not observed. Product grids are proposed to step from 1 column (mobile) to 2–3 (tablet) to 3–4 (desktop). All interactive targets (buttons, nav links, cart icon) should maintain a minimum 44×44px touch target regardless of the compact 2px button radius. This section is a design recommendation only; no live responsive behavior was captured from the source.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This spec is built from static CSS and text excerpts only; no rendered screenshots, computed styles, or DOM layout were observed. Header/body font stacks rely on Shopify theme CSS variables (`--font-stack-header`, `--font-stack-body`) whose resolved values were not directly supplied — "Abel" is inferred as the header face from the font list, and its licensing/availability as a webfont on this store is unverified. All non-primary/secondary color roles (accent, overlay, surface variants) are semantic inferences from a shared neutral/red palette, not confirmed brand-color declarations. Numeric type sizes beyond the two literal CSS values (cart-count `calc(11em/16)` and button `calc((base-2)/base)`) are proposed, not measured. Hover, focus, active, error, and disabled states for buttons and inputs are proposed conventions, not confirmed via interaction testing. Mobile menu, cart drawer, and grid collapse behavior were not observed in the supplied evidence.
