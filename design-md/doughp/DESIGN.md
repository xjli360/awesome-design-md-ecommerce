---
version: alpha
name: "Doughp"
source_url: "https://doughp.com"
captured_at: "2026-09-28T04:31:12.450007+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Doughp's extracted CSS is a Shopify theme built on Poppins as the sole
  declared body and component font, paired with a large neutral gray
  system (Tailwind-style gray scale) and a set of semantic utility colors
  (error, warning, success, info) rather than a distinct brand palette.
  Among the raw swatches, several values are payment-network badge colors
  (PayPal blue, Mastercard red/orange, Amex/Discover blues) and are
  excluded from the interpreted brand roles below as untrusted noise.
  The remaining warm tones — a caramel/gold (#ae792d, #ce9440), a deep
  warm brown-black (#230d0d), and a cream (#fff1e3) — are the most
  plausible confectionery-appropriate accents and are used here as
  inferred brand primary and canvas-adjacent tones, since no explicit
  `--color-primary` token was present in evidence. Golden yellow
  (#ffcc33) is explicitly declared as `--color-review-stars`/`--color-warning`
  and is reused here for rating and highlight accents. Layout tokens
  (rounded-theme scale, 1440px page width, large section paddings) are
  directly observed and preserved. Typography sizes below are drawn from
  named component variables (product card, article card, cart, breadcrumbs)
  where available; larger display sizes are proposed extrapolations, not
  observed at those sizes.

colors:
  primary: "#ae792d"
  ink: "#230d0d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ffcc33"
  cream: "#fff1e3"
  caramel-deep: "#ce9440"
  success: "#00c064"
  error: "#e20f28"
  info: "#0082fb"
  dark: "#1a1a1a"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.5, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.7, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.35, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.5, letterSpacing: 0px}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    borderColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    borderColor: "{colors.hairline}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    borderColor: "{colors.hairline}"

## Components

**button-primary** is the main call-to-action style (e.g. "Add to Cart", "Shop Now"), using the inferred caramel primary against a white label, sized from the observed 700-weight, 15px product-price/button scale. Hover/active states were not observed and are proposed as a slight darken or opacity shift.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g. "Learn More"), sharing the primary's border and text color on a white fill; state transitions are proposed, not measured.

**text-input** covers form fields (email capture, quantity, checkout), using a soft off-white fill and light hairline border consistent with the neutral gray tokens present in the evidence; focus-ring styling is proposed and unobserved.

**nav-bar** represents the top site navigation strip, using a white background and dark ink text; no scroll-state or mobile-menu behavior was present in the supplied CSS, so its collapse pattern is proposed.

**product-card** models the cookie-dough product tiles, directly grounded in the observed `--font-product-card-title` (14–16px, weight 600) and `--font-product-price` (15px, weight 700) variables, on a white card with a light hairline border and moderate corner rounding.

**hero** is the top-of-page banner, proposed as a warm cream backdrop carrying the largest display type; no hero-specific CSS was present in evidence, so both background and copy scale are inferred from brand tone rather than measured.

**footer** is proposed as a dark, near-black band with white text for contrast, matching common confectionery-brand footer conventions; no footer-specific selectors were present in the supplied evidence.

**badge** renders small labels such as "Best Seller" or review-star counts, using the explicitly declared `--color-review-stars`/`--color-warning` gold on a pill shape; this directly reuses an observed CSS custom property rather than an inferred color.

**search** is a pill-shaped input for site search, styled consistently with text-input but rounded fully; no search-specific selectors were observed, so this pattern is proposed.

**cart-drawer** is a category-appropriate slide-out cart panel, grounded in the observed `--font-cart-title` (18px, weight 600) variable, using a white surface with hairline dividers between line items; open/close animation was not observed and is proposed.

## Responsive Behavior
This is a recommended, non-measured breakpoint scheme, since no media-query behavior was captured in evidence:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 768px | Single-column stacking; nav collapses to a hamburger/drawer |
| Tablet | 768–1199px | Two-column product grids; cart becomes a drawer overlay |
| Desktop | 1200–1440px | Matches observed `--layout-page-width: 1440px` max container |
| Wide | > 1440px | Content centers within the 1440px container with side gutters |

Touch targets should be at least 44px in the proposed scheme; primary/secondary buttons and search inputs should use `{spacing.md}`–`{spacing.lg}` padding to satisfy this on mobile. Navigation collapse, drawer transitions, and any hover-only affordances are proposed conventions only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom-property and selector extraction only; no rendered page, computed layout, or interaction states were observed. Color roles (primary, ink, muted, hairline, etc.) are inferred by matching swatches to plausible semantic use — the supplied palette contains no explicit `--color-primary` or `--color-brand` token, so the caramel/gold assignment is a best-effort inference, not a confirmed brand color. Several palette entries (e.g. #eb001b, #f79e1b, #ff5f00, #0071ce, #1990c6) are recognizable third-party payment-badge colors (Mastercard, PayPal, etc.) and were deliberately excluded from brand role assignment. Font stacks referencing Nunito Sans, Open Sans, and Roboto appear in evidence but were not tied to any selector used on doughp.com and are treated as unused/third-party fallbacks; only Poppins is confirmed via `body` and component `--font-*-family` variables. The spacing scale is a proposed general-purpose scale and does not match the much larger observed `--section-padding-*` values (24–240px), which are reserved for macro section rhythm. All hover, focus, error, and mobile-menu states, along with any imagery or iconography choices, are proposed and not verified against a live render. Licensing and self-hosted availability of Poppins were not verified from this evidence.
