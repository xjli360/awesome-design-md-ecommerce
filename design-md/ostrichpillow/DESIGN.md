---
version: alpha
name: "Ostrichpillow"
source_url: "https://ostrichpillow.com"
captured_at: "2026-09-28T05:05:40.030267+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ostrichpillow's storefront is built on Shopify's Dawn-derived CSS custom-property system, exposing an explicit foreground/background pair (rgb 18,18,18 on white) and a saturated blue button token (#0f32c3) used for primary CTAs and mega-menu buttons. A darker slate blue (#53607b) appears as a secondary/upsell button fill, alongside a muted grey (#585858) used near form controls and select arrows. Neutral surfaces (#f1f2f4, #f9fafb, #d9dee1) suggest card and section backgrounds versus the pure white canvas. The confirmed body typeface is "SharpSans" with sans-serif fallback at a 1.5rem base size and slight positive letter-spacing; "Montserrat" is also present in the stylesheet and is inferred here as a possible heading face, though no heading-specific rule was supplied, so that mapping is explicitly inferred rather than observed. Rounded pill buttons (25px radius, hover-to-black) and a circular wishlist counter badge point to a soft, rounded, low-drama interface consistent with a sleep/wellness brand. This specification treats layout, spacing, and breakpoints as proposed conventions layered onto the observed color and type tokens, not as measured page geometry.

colors:
  primary: "#0f32c3"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#585858"
  hairline: "#d9dee1"
  surface-soft: "#f1f2f4"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  accent: "#53607b"
  accent-secondary: "#464e64"
  border-strong: "#c6c6c6"
  contrast-grey: "#b7b7b7"
typography:
  display-xl: {fontFamily: "SharpSans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "SharpSans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "SharpSans, sans-serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0.02rem}
  body-sm: {fontFamily: "SharpSans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.01rem}
  caption: {fontFamily: "SharpSans, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.03rem}
  button-md: {fontFamily: "SharpSans, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.02rem}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: "130px-150px (observed --header-height values)"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  wishlist-indicator:
    iconStroke: "{colors.ink}"
    counterBackground: "{colors.canvas}"
    counterText: "{colors.ink}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"

## Components
**button-primary** reflects the directly observed `--color-button: 15,50,195` and mega-menu `.button` rule using `#0F32C3` with white text; the pill shape approximates the observed 25px radius via the `full` token. **button-secondary** mirrors the `.buy-button-extra` rule (white fill, blue border, blue text) with its documented hover-to-black state proposed as an interaction cue rather than newly invented. **text-input** is a proposed pattern for search/newsletter fields; no dedicated input CSS was supplied, so sizing and border color are inferred from the neutral hairline token. **nav-bar** uses the two conflicting `--header-height` values (130px/150px) actually present in the stylesheet, presented together since the responsive rule that selects between them was not captured. **product-card** is inferred from repeated product-grid text patterns (name, variant, price, "Add to cart") paired with the neutral surface tokens; card padding and radius are proposed. **hero** is a proposed full-bleed banner pattern sized for the "PUT REST ON YOUR TRIP ITINERARY" messaging, using display typography and a primary CTA; exact hero layout was not measured. **footer** is a proposed compact link list using muted body text on white, consistent with the minimal footer text captured ("Reviews / About us / Log in"). **badge** models the "New" and "New colors" flags seen throughout the catalog copy, using the primary blue for emphasis; exact badge styling was not present in the supplied CSS. **wishlist-indicator** is drawn directly from the `.wishlist-header-link` and `.wkh-counter` rules (22px icon, white circular counter with black text), making it the one component with near-literal CSS support alongside the buttons.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column product grid, collapsed nav to hamburger, header height likely reduced from the 130-150px desktop tokens (not confirmed). |
| Tablet | 768-1024px | Two-column product grid, condensed mega-menu. |
| Desktop | >1024px | Multi-column grid, full mega-menu with `.mega-menu__right-item` panels as observed in CSS selectors. |

Touch targets should be a minimum 44px hit area for cart, wishlist, and search icons. Mega-menu items and buy buttons should collapse to accordions/stacked lists below tablet width. This table is a recommendation based on common Shopify theme conventions, not measured breakpoint behavior of the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or responsive DOM behavior was observed. Header height is ambiguous (two conflicting `--header-height` declarations were both supplied with no confirmed media-query trigger). The Montserrat/SharpSans heading-vs-body split is inferred, not confirmed by any heading-specific selector in the evidence. All typography sizes beyond the one confirmed body rule (1.5rem/SharpSans) are proposed defaults, not measured. Component states such as focus rings, form validation, disabled buttons, and mobile navigation drawer behavior were not present in the supplied CSS and are labeled proposed. Font licensing and availability of "SharpSans" as a web-safe or licensed asset were not verified. Color role assignments (e.g., which greys serve as body vs. muted vs. border) are inferred from selector context, not confirmed via visual rendering.
