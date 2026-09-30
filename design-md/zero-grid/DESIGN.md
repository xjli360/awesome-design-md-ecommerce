---
version: alpha
name: "Zero Grid"
source_url: "https://zerogrid.com"
captured_at: "2026-09-29T04:04:49.522086+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Zero Grid's site evidence shows a travel-security brand anchored by a deep
  navy (#0e2a47) used for the solid header state, page-title headings, and
  the Judge.me review widget's primary/star color. A warm gold (#ffc857)
  appears specifically on header search-submit icons, suggesting an accent
  reserved for small interactive affordances rather than large surfaces.
  The Shopify theme's own color variables define a neutral, ink-on-white
  button system (--color-button: 18,18,18 / --color-button-text: white),
  which is treated here as the default button pairing, distinct from the
  navy brand color used in navigation and headings. Product cards use an
  observed light-gray card surface (#ededed) with a white inner image tile,
  both carrying unusually large corner radii (33px / 30px) captured
  directly from theme CSS. Typography is anchored by an observed
  'Handelson' display face (Impact fallback) used for large policy/page
  titles, and 'Proxima Nova' for navigation links and product titles at
  small, uppercase, wide-tracked sizes. Body copy typeface is not tied to a
  specific selector in the evidence and is therefore treated as inferred.
  This interpretation proposes a restrained, trust-driven system fitting a
  security/RFID accessories category: navy for authority, gold as a sparing
  accent, and neutral grays for card surfaces and secondary text.

colors:
  primary: "#0e2a47"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#4a4a4a"
  muted: "#6b7280"
  hairline: "#e6e6e6"
  surface-soft: "#f5f5f5"
  surface-card: "#ededed"
  on-primary: "#ffffff"
  accent: "#ffc857"
  accent-strong: "#dca72a"
  danger: "#e93c3c"
  success: "#228b22"
typography:
  display-xl: {fontFamily: "'Handelson', Impact, sans-serif", fontSize: "42px", fontWeight: 900, lineHeight: 1.15, letterSpacing: "0.05em"}
  display-md: {fontFamily: "'Handelson', Impact, sans-serif", fontSize: "30px", fontWeight: 900, lineHeight: 1.2, letterSpacing: "0.04em"}
  title-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.05em"}
  body-md: {fontFamily: "'Assistant', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.02em"}
  body-sm: {fontFamily: "'Assistant', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.02em"}
  caption: {fontFamily: "'Proxima Nova', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04em"}
  button-md: {fontFamily: "'Proxima Nova', sans-serif", fontSize: "13px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.15em"}
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
    backgroundColor: "{colors.ink}"
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
  cta-hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    accent: "{colors.accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColorTransparent: "transparent"
    backgroundColorScrolled: "{colors.primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    hairline: "1px solid rgba(255,255,255,0.05)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    innerTileColor: "{colors.canvas}"
    rounded: "33px"
    innerTileRounded: "30px"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.primary}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    accent: "{colors.accent}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "transparent"
    fieldBorder: "1px solid rgba(255,255,255,0.2)"
    submitIconColor: "{colors.accent}"
    typography: "{typography.body-sm}"
  rating-stars:
    activeColor: "{colors.primary}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"
  trust-icon-tile:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.primary}"
    labelColor: "{colors.ink}"
    valueAccent: "{colors.accent}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** reflects the theme's literal default button color variables (ink background, white text), used for primary commerce actions like "ADD TO CART." **button-secondary** inverts this pairing for lower-emphasis actions and is a proposed complement, not separately observed. **cta-hero** is an inferred brand-forward variant using the navy primary with a gold accent, intended for prominent calls like "FIND YOUR GEAR," since the hero itself was not captured in measurable CSS. **text-input** proposes a neutral bordered field for newsletter/search forms using the observed hairline gray. **nav-bar** directly reflects the observed transparent-to-navy scroll transition and uppercase white link styling captured in `.zg-header-wrapper` and `.zg-header-nav a`. **product-card** is grounded in exact observed selectors: a light-gray card shell at 33px radius containing a white 30px-radius image tile, with a small uppercase navy title. **hero** and **footer** are proposed structural containers; their colors are inferred from the broader palette since no hero/footer-specific selectors were supplied. **badge**, **search**, **rating-stars**, and **trust-icon-tile** are category-appropriate proposals for RFID/travel-security messaging (e.g., "RFID BLOCKING," "TRIP ASSURANCE $300," "LIFETIME GUARANTEE" feature tiles seen in the page text), styled from the neutral/soft-surface and primary/accent tokens; their exact states are not verified live and should be treated as proposed patterns.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | <600px      | Single-column stacking; nav collapses to a hamburger/menu control; search expands full-width. |
| tablet    | 600–959px   | Two-column product grids; header remains fixed with solid navy on scroll. |
| desktop   | 960–1279px  | Multi-column product grid (3–4 up); nav links inline as observed in header CSS. |
| wide      | ≥1280px     | Max-width content container; increased section spacing (`{spacing.section}`). |

Touch targets should be at least 44px in height for buttons and nav items. Header search-expand and mobile menu collapse behavior are proposed conventions based on the presence of `.zg-mobile-search-field-container` and `.zg-search-inline-expand-tray` selectors, not confirmed interaction traces. This table is a recommendation derived from typical e-commerce patterns, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no live rendering, computed layout, or interaction testing was performed. The body's true font-family (`var(--font-body-family)`) was not resolved in the supplied evidence, so `body-md`/`body-sm` use an inferred candidate ('Assistant') from the observed font list rather than a confirmed selector mapping. Hero and footer background/text colors are inferred from the general palette, not tied to dedicated selectors. Product-card corner radii (33px/30px) are observed exact values but fall outside the standard `rounded` token scale, so they are referenced as literals in `product-card`. Trust-icon-tile, badge, search, and rating-stars components are proposed interpretations of features named in page text (RFID Blocking, Trip Assurance, ReturnMe, Lifetime Guarantee) without corresponding structural CSS. Mobile menu, cart drawer, and hover/focus states were not observed and are marked proposed throughout. Custom font ('Handelson') availability, licensing, and exact weight/style variants were not verified.
