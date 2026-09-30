---
version: alpha
name: "Moonkie"
source_url: "https://moonkieshop.com"
captured_at: "2026-09-28T04:53:37.063086+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Moonkie's storefront CSS shows a warm, muted palette built around a taupe-brown
  (#917b69) used for the mini-cart checkout button and inline text links, paired
  with soft cream/blush surfaces (#f5f2ed) and light neutral cards (#f9f9f9).
  Body copy renders in dark grays (#333333, #666666, #444444) rather than pure
  black, and hairlines/borders appear in light grays (#dedede, #ececec). A small
  cluster of platform-native colors (Trustpilot green #00b67a, Amazon-style link
  blue #007185/#008296) appear in third-party widget selectors and are treated
  here as incidental, not brand colors. Heading scale variables (h1 48-56px, h2
  38-48px, down to h6 18px) and button/input heights (52px, 44px) are directly
  observed custom properties. Font stacks include Outfit and Inter alongside
  system UI fallbacks (Helvetica Neue, Arial, Roboto, Segoe UI); Outfit is
  proposed here as the display/heading family and Inter as the body family,
  since both are observed in the font list and Outfit's geometric character
  suits a soft, rounded baby-goods brand voice. Rounded corners are inferred
  from the observed 12px radius on the product-media-review gradient panel and
  extended into a general radius scale. Semantic role assignments (primary,
  ink, muted, hairline) are inferred mappings onto observed hex values, not
  extracted role names.

colors:
  primary: "#917b69"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f5f2ed"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  accent-warm: "#9f7958"
  border-strong: "#cccccc"
  badge-bg: "#ececec"
  focus-ring: "#007185"
  success: "#00b67a"
  danger: "#dc3545"
typography:
  display-xl: {fontFamily: "Outfit, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Outfit, sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Outfit, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Outfit, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: "52px"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: "44px"
    padding: "{spacing.xs} {spacing.base}"
  gift-set-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    accentColor: "{colors.accent-warm}"
    padding: "{spacing.base} {spacing.lg}"

## Components

**button-primary** maps directly to the observed `.mini-cart__drawer-footer .checkout-button` rule (`background:#917B69; color:#fff`), used here as the canonical filled call-to-action for checkout and add-to-cart actions. Hover/active states are not observed and are proposed as a slight opacity or darken treatment.

**button-secondary** is a proposed outline variant reusing the same primary taupe for text and border on a white background, intended for secondary actions like "View Details" or "Add to Wishlist" that were not directly styled in the supplied CSS.

**text-input** derives its 52px height from the observed `--form-input-field-height` custom property, with hairline borders and dark ink text; focus-ring color is proposed but references the observed `#007185` outline color found on a climate-partner focus-visible rule, reused here for general input focus states.

**nav-bar** is inferred from the presence of an extensive mega-menu text list (Shop by Stage, Shop by Solution, Shop by Budget) in the page text; no nav container CSS was supplied, so background, spacing, and border are proposed defaults on a white canvas.

**product-card** is a proposed pattern for the large catalog grid implied by the product-name/price pairs in the page text excerpt (e.g., "Silicone Training Cup with Straw – $12.99"). Card surface, radius, and typography are inferred; no `.product-card` selector was present in the supplied CSS.

**hero** is proposed as the top-of-page banner area implied by the tagline "One Moment at a Time" and large heading tokens (`--heading-h1-font-size: 56px`), using the soft cream surface color as an inferred background rather than an observed hero-specific rule.

**footer** is inferred from the long link list (About Us, Rewards, Blog, Contact) in the page text, styled with muted body copy on the soft cream surface; no footer selector was supplied.

**badge** is a proposed small pill component for labels like "New Arrival," "Best Seller," or percentage-off tags (several products show strikethrough compare-at pricing, e.g., "$74.99 $127.99"), using the light gray `#ececec` as an inferred neutral badge fill.

**search** is proposed for the "Quick Search" feature named in the page text, styled as a full-radius pill input; no dedicated search-bar CSS was supplied.

**gift-set-panel** is a category-specific proposed component for the multiple "Gift Set" product groupings (Journal Luxe, First Bites, Deluxe Playtime), using the observed gradient-adjacent soft cream tone and the `.product_feature .content` bullet-dot accent color (`#997558`, rounded here to the nearest palette entry `#9f7958`) for iconography.

## Responsive Behavior

Recommended breakpoints (proposed, not measured):

| Breakpoint | Width | Layout notes |
|---|---|---|
| Mobile | <768px | Single-column product grid, collapsed hamburger nav, sticky bottom add-to-cart proposed |
| Tablet | 768–1023px | 2–3 column product grid, mega-menu collapses to accordion |
| Desktop | 1024–1439px | Full mega-menu, 4-column product grid, `--container-gutter: 40px` observed |
| Wide | ≥1440px | Larger heading scale (`--heading-h1-font-size: 56px` observed variant), 20-column grid system per `--grid-column-count: 20` |

Touch targets should meet a minimum 44px height, matching the observed `--button-small-height: 44px`; primary buttons use the observed 52px height at all sizes. Mega-menu collapse into an accordion or drawer on mobile is a standard proposal, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot; no rendered layout, hover state, animation, or JavaScript-driven interaction (mini-cart drawer open/close, mega-menu expansion, quick-search overlay) was observed. Several supplied colors (Trustpilot green, Amazon-style checkout blues, credit-card brand colors) originate from third-party embedded widgets and are excluded from the core brand palette as likely non-brand. Semantic role names (ink, muted, hairline, surface-soft/card) are inferred groupings of observed hex values, not extracted CSS variable names. Typography sizes for display-md and title-md are proposed interpolations between two conflicting `:root` blocks (mobile vs. desktop heading scales) rather than a single confirmed value. Font availability, licensing, and whether Outfit/Inter are self-hosted or third-party-served were not verified. Responsive breakpoints and the entire Responsive Behavior table are proposed conventions, not measured from a live viewport. Border radius values are extrapolated from a single observed 12px radius on one promotional panel.
