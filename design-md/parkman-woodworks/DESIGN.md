---
version: alpha
name: "Parkman Woodworks"
source_url: "https://parkmanwoodworks.com"
captured_at: "2026-09-28T10:09:22.789218+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Parkman Woodworks' visible CSS is a spare, workshop-honest system exposed
  as Shopify theme custom properties, not a decorative wood-tone palette.
  Ink (#1c1d1d) and near-black (#111111/#040404) drive buttons, links, and
  body text against a plain white canvas (#ffffff), with warm off-white
  borders (#e8e8e1) and dim surfaces (#f2f2f2, #f6f6f6) standing in for
  material-adjacent neutrals. A single warm accent (#ff4f33) is observed
  only on the cart-count dot; this interpretation extends it, inferred, to
  urgency CTAs like the repeated "Get My Custom Quote" prompts.

  Headings use a custom-declared display face, "Hannik" (with Poppins
  declared earlier in the same block and then overridden — availability
  and licensing of either are unverified), set at the one observed size of
  35px/1.2. Body copy runs in Open Sans at 17px/1.6 with slight tracking,
  a legible pairing suited to product specs and material sourcing stories.
  Buttons are hard-cornered (radius:0) while carousel controls are fully
  circular (radius:50%) — a deliberate contrast this spec preserves as the
  primary geometric signature: rectangular structure for commerce, circular
  affordances for navigation. All sizes beyond the two CSS-declared type
  tokens are proposed, not measured, and layout/interaction states are
  inferred from component naming conventions in the theme CSS.

colors:
  primary: "#111111"
  primary-dim: "#040404"
  ink: "#1c1d1d"
  canvas: "#ffffff"
  body: "#1c1d1d"
  muted: "#444444"
  hairline: "#e8e8e1"
  surface-soft: "#f2f2f2"
  surface-card: "#f6f6f6"
  input-bg-dark: "#e6e6e6"
  on-primary: "#ffffff"
  accent: "#ff4f33"
  overlay: "#000000"
typography:
  display-xl: {fontFamily: "Hannik, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  display-md: {fontFamily: "Hannik, sans-serif", fontSize: 35px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Hannik, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.025em}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.025em}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.03em}
  button-md: {fontFamily: "Hannik, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.42, letterSpacing: 0px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    hoverBorderColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    backgroundColorDisabled: "{colors.input-bg-dark}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottomColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.ink}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    controlBackground: "{colors.primary}"
    controlIconColor: "{colors.on-primary}"
    controlRounded: "{rounded.full}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTopColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    iconWeight: 3px
    padding: "{spacing.sm} {spacing.base}"
  quote-request-panel:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent}"
    textColor: "{colors.ink}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components
**button-primary** renders solid-black (#111111) fills with white text, matching the observed `--colorBtnPrimary`/`--colorBtnPrimaryText` pair and the theme's `.btn` rule (radius:0, padding 11px 20px). Hover state reuses the same background per the observed `:hover` rule (no separate hover token was exposed).

**button-secondary** mirrors the observed `.btn--tertiary` class: transparent background, 1px hairline border, 12px caption type, with border darkening to ink on hover — a quiet outline style for secondary actions like "View Collection."

**text-input** is proposed from the `--colorInputBg*` tokens: white default, dim gray (#f2f2f2) and darker gray (#e6e6e6) states for disabled/filled variants, ink text, square corners consistent with button radius.

**nav-bar** uses the observed `.site-header` bottom hairline and `--colorNav`/`--colorNavText` white-on-white-with-ink-text scheme; sticky behavior and mobile collapse are proposed, not confirmed.

**product-card** is inferred from the "Quick view" product-grid text pattern; it pairs a soft card surface (#f6f6f6) with hairline borders and header-font product titles over body-font pricing, typical of the collection grids described in the evidence.

**hero** is inferred from the homepage slideshow copy ("Custom Wood Furniture…") and the observed `--colorHeroText` (white) plus `.hero .flickity-button` circular, white-on-white-shadow control styling distinct from the black default carousel buttons.

**footer** is proposed from `--colorFooter`/`--colorFooterText` (white-on-white theme tokens) and the visible address/phone block ("160 S Mission Rd, Los Angeles, CA"), styled in small body type above a hairline rule.

**badge** models the observed `--colorSaleTag`/`--colorSaleTagText` pair (ink background, white text) for sale or "New" labeling on product cards.

**quote-request-panel** is a category-specific component proposed for Parkman's custom-order business model (repeated "Get My Custom Quote" CTAs and trade/custom-order navigation). It borrows the surface-card background and primary button styling, with the cart-accent red (#ff4f33) used sparingly to draw attention to the quote CTA — an inferred, not observed, accent application.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Nav behavior | Grid |
|---|---|---|---|
| mobile | <600px | Hamburger/off-canvas nav (cart/menu icons observed in markup) | 1-column product grid |
| tablet | 600–959px | Condensed horizontal nav | 2-column product grid |
| desktop | ≥960px | Full mega-menu (Shop by Type / Shop by Room) | 3–4 column product grid |

Touch targets should be at least 44px for cart, search, and menu icons; carousel controls (`.flickity-button`, radius:50%) should maintain a minimum 32–40px hit area. Mobile filter/collection navigation is expected to collapse into an accordion or drawer, consistent with the deep category taxonomy (Shop Furniture > Shop By Type / Shop by Room) visible in the text evidence, though no mobile layout was directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, a theme stylesheet, and page text only — no rendered layout, responsive states, hover/focus transitions, or JavaScript-driven interactions (cart drawer, quick-view modal, mega-menu) were directly observed. The heading font "Hannik" appears as a literal CSS custom-property value; it is treated as a custom/unverified font with unknown licensing, and Poppins (declared then overridden in the same `:root` block) is included only for transparency, not use. All typographic sizes beyond the two CSS-declared values (17px body, 35px header) are proposed for scale completeness. Color-to-role mapping for non-button surfaces (cards, footer, search) is inferred from token naming rather than confirmed visual placement. Several palette entries in the source evidence (e.g., #0071ce, #eb001b, #f79e1b, #ff5f00) resemble third-party payment-brand colors (Visa/Mastercard) rather than site branding and were intentionally excluded from role assignment. Spacing and rounded scales beyond radius:0/50% are proposed conventions, not extracted values.
