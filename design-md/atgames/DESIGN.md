---
version: alpha
name: "AtGames"
source_url: "https://www.atgames.us"
captured_at: "2026-09-28T04:43:54.779188+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  AtGames' storefront pairs a saturated brand yellow (#fbcd0a) with a near-black
  ink (#171d21) and clean white canvas, evoking an arcade cabinet's marquee
  lighting against dark hardware. The palette is otherwise neutral and
  utilitarian: mid grays (#333333, #666666) for body copy, light grays
  (#eeeeee, #f2f2f2, #dddddd) for card surfaces and hairlines, consistent with
  a Shopify Online Store 2.0 theme. A muted teal (#108474) appears in the
  observed palette and is inferred here as a secondary accent for
  success/status badges, distinct from the primary yellow CTA color. Several
  brand-specific hues (payment-network and social-icon colors such as
  #1990c6, #3b5998, #dd4b39) are excluded from the core design system, as they
  are third-party icon colors rather than AtGames brand tokens.

  Typography is inferred from the observed font-family stack: Barlow is
  assigned to display/heading roles and Nunito Sans to body/UI text, both
  common Shopify pairings; this mapping to specific selectors is not directly
  observed. Numeric scale values (72/56/44/32/28/22/20/17/15/13px) come
  directly from the site's CSS custom properties (--text-h0 … --text-xs). The
  interpretation favors a bold, high-contrast marquee treatment for hero
  moments and dense, grid-based product carousels appropriate to a
  multi-category hardware/software catalog (pinball cabinets, arcade
  machines, downloadable game packs).

colors:
  primary: "#fbcd0a"
  ink: "#171d21"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#eeeeee"
  on-primary: "#171d21"
  accent-teal: "#108474"
  surface-dark: "#1c1c1c"
  border-subtle: "#cccccc"
  overlay-scrim: "#00000066"
typography:
  display-xl: {fontFamily: "Barlow, sans-serif", fontSize: 72px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow, sans-serif", fontSize: 44px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    border: "1px solid {colors.border-subtle}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    ratingAccent: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    overlay: "{colors.overlay-scrim}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaButton: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    hairline: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  carousel-controls:
    backgroundColor: "{colors.canvas}"
    iconColor: "{colors.ink}"
    activeColor: "{colors.primary}"
    rounded: "{rounded.full}"
    hitArea: "44px"

## Components

**button-primary** is the yellow-on-dark CTA used for "Add to cart," "Subscribe," and primary catalog actions; hover/focus states are proposed, not observed, and should lighten or shift opacity per the theme's `--button-background-opacity` custom property noted in CSS.

**button-secondary** provides an outlined, low-emphasis alternative for actions like "Continue shopping" or "View all," using ink text on white with a subtle border rather than a filled background.

**text-input** covers newsletter signup, search fields, and form inputs, styled with a light hairline border and generous padding to remain touch-friendly; error/focus ring states are proposed and not verified from the CSS.

**nav-bar** reflects the sticky header pattern evidenced by `--sticky-header-enabled` and the `header-grid-template` rules (logo, main-nav, secondary-nav regions); exact breakpoint switching between stacked and inline nav layouts is inferred from the multiple grid-template variants, not visually confirmed.

**product-card** is the core catalog unit for pinball machines, arcade cabinets, and game packs, showing title, price ("Sale price"), and a star rating; the rating-star color is proposed as primary yellow for brand consistency, though actual widget styling (JudgemeStar font) was not fully resolved from evidence.

**hero** models the homepage banner ("Welcome to a new world of Virtual Pinball") as a dark, full-bleed section with light text and a primary CTA, appropriate for showcasing flagship 4K pinball hardware; exact imagery and layout are not observed.

**footer** consolidates the extensive navigation taxonomy (Pinball, Arcade, Games & Services, Customer Support) seen in the page text, using dark ink background with light text links; column layout and responsive stacking are proposed.

**badge** is a small pill component proposed for status labels such as "Preorder," "New Arrival," or "Sale," using the secondary teal accent to differentiate from the primary yellow CTA color and avoid visual competition.

**search** models the "Open search" control referenced in the page text as an expandable search field or overlay; exact interaction (modal vs. inline) is not observed.

**carousel-controls** is a category-appropriate component directly motivated by the CSS evidence of multiple `product-list` carousel configurations (`--product-list-carousel-item-width`, items-per-row 1/2/4); it represents the prev/next affordances needed for the "Legends 4K Pinball Machines," "New Arrivals," and "Legends HD" horizontal product rails.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Nav | Product grid | Carousel items/row |
|---|---|---|---|---|
| Mobile | <749px | Collapsed hamburger | 1 column | 1 (74vw card, per observed CSS) |
| Tablet | 750–999px | Inline compressed | 2 columns | 2 (36vw card, per observed CSS) |
| Desktop | 1000–1399px | Full inline nav | 3–4 columns | 4 |
| Wide | ≥1400px | Full inline nav, wider logo | 4+ columns | 4 |

Touch targets should be at least 44px for carousel arrows, cart/search icons, and nav toggles. Header logo scaling (170×28px mobile to 300×50px desktop) and grid-template reflow ("logo main-nav secondary-nav" to stacked "logo . secondary-nav / main-nav") are drawn from observed CSS custom properties, but the pixel breakpoints at which they switch were not present in the supplied evidence and are therefore estimated.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties and page text only; no rendered screenshots, computed styles, or interaction states (hover, focus, active, disabled, error) were observed. Font-family-to-role mapping (Barlow for headings, Nunito Sans for body) is inferred from the presence of these families in the stylesheet, not from confirmed selector usage — actual heading/body assignment may differ. Rounded and spacing scales follow a standard proposed system rather than resolved `--spacing-N` / radius values, since the underlying pixel values for those custom properties were not present in the supplied evidence. Several palette entries (Mastercard/Visa-like blues and oranges, Facebook/Twitter/Pinterest/LinkedIn brand colors) are third-party icon colors incidentally present in the CSS and were deliberately excluded from semantic design roles. The `JudgemeIcons`/`JudgemeStar` fonts are a third-party review-widget icon font, not a brand typeface, and are excluded from the typography system. Mobile menu behavior, cart drawer layout, and carousel drag/swipe interaction are not observed. Font licensing and self-hosting status for Barlow and Nunito Sans were not verified.
