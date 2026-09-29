---
version: alpha
name: "Vinyl Tap"
source_url: "https://www.vinyltap.co.uk"
captured_at: "2026-09-28T05:08:56.493273+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Vinyl Tap is a Shopify-powered independent record store serving UK/EU customers,
  evidenced by its theme CSS custom properties (--color-button, --color-foreground,
  --font-heading-family) and standard cart/checkout flow. The measured palette centers
  on a cyan-blue accent (#15b6da from --color-button, with #37b5d1 appearing in a promo
  banner and #1990c6/#136f99 as accelerated-checkout button states) against a
  high-contrast white canvas (#ffffff) and near-black foreground (#121212). Supporting
  greys (#f4f4f4, #fafafa, #dedede, #666666, #444444) come from card, skeleton-loader,
  and body-text contexts and are repurposed here as surface, hairline, and muted-text
  roles — this mapping is inferred, since no selector explicitly labels "surface" or
  "hairline." Four font families were observed in the stylesheet payload: Open Sans and
  Roboto Condensed (utility/body-leaning sans faces) and Kollektif and Nickainley
  (a display script). No CSS rule ties a specific family to heading vs. body; this
  document infers Nickainley for expressive display treatment (fitting an independent
  record-store identity) and Open Sans for body copy, with Kollektif/Roboto Condensed
  as UI/caption alternates. All sizes, spacing, and radius values are proposed design-
  system defaults unless an exact CSS value is cited.

colors:
  primary: "#15b6da"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent: "#37b5d1"
  accent-strong: "#136f99"
  accent-alt: "#1990c6"
  highlight: "#ffde59"
  dark-surface: "#1c1c1c"
  border-strong: "#bcbcbc"
typography:
  display-xl: {fontFamily: "'Nickainley', cursive", fontSize: 56px, fontWeight: 400, lineHeight: 1.1, letterSpacing: "0.06rem"}
  display-md: {fontFamily: "'Nickainley', cursive", fontSize: 36px, fontWeight: 400, lineHeight: 1.2, letterSpacing: "0.06rem"}
  title-md: {fontFamily: "'Kollektif', sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.3, letterSpacing: "0.06rem"}
  body-md: {fontFamily: "'Open Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.04rem"}
  caption: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04rem"}
  button-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: "0.04rem"}
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    border: "1px solid {colors.hairline}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  preorder-ribbon:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** uses the theme's measured `--color-button` (#15b6da) with white text, matching the accelerated-checkout button treatment seen in the Shopify CDN CSS. Hover/active darkening is proposed, referencing the observed `#136f99` payment-button hover state as a plausible darker step.

**button-secondary** is inferred from the `--color-secondary-button` variable (white background, dark text) and is proposed for "Add to wishlist" or filter-toggle actions; no secondary-button hover state was observed.

**text-input** styling (border, radius, padding) is a proposed pattern for search and account forms; only the hairline grey (#dedede) and canvas white are grounded in evidence, border-radius and padding are design-system defaults.

**nav-bar** reflects the visible menu items (Home, Browse, Genres, Collections, Latest Arrivals, Pre-orders, We Buy, Fairs, About) as plain text links on white, consistent with `--color-link: 18,18,18`. Sticky/scroll behavior is not observed and is not claimed.

**product-card** is proposed for release listings, using the light card surface (#fafafa) and hairline border seen in `.product-card-wrapper .card` custom properties (corner-radius, border-width vars exist but concrete pixel values were not resolved in the supplied CSS).

**hero** is a proposed full-width banner pattern for featured releases/collections, using a dark surface (#1c1c1c) for contrast with the display-xl script typography; no hero markup or imagery was present in the supplied evidence.

**footer** mirrors the dark-surface treatment for site-wide links (FAQ, Contact, Country/region selector) implied by the large country/currency list in the page text; layout of columns is proposed, not observed.

**badge** covers small labels such as "New Release," "Pre-order," or format tags, using the neutral badge tokens (`--color-badge-background`, `--color-badge-foreground`) directly from `:root`.

**search** is a proposed overlay/input pattern for the "Search" link seen in the nav; exact placement (modal vs. inline) was not observable from static CSS.

**preorder-ribbon** is a category-specific component addressing the store's visible "Pre-orders" and "New Releases / 20% off" merchandising language, using the accent teal (#37b5d1) drawn from the observed promo-banner rule (`#shopify-section-... h2`).

## Responsive Behavior
Recommended breakpoints (not measured from live layout): mobile ≤599px, tablet 600–989px, desktop ≥990px, matching common Shopify Dawn-family theme conventions implied by the `.color-scheme` and grid-based `body` rule. Nav items should collapse into a hamburger/drawer below tablet width; product-card grids should step from 2 columns (mobile) to 3–4 (desktop). All interactive targets should maintain a minimum 44×44px hit area. This section is a recommendation only; no responsive CSS or viewport behavior was present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, a partial rule excerpt, and page text; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed. Font-family-to-role mapping (heading vs. body vs. UI) is inferred from typical usage patterns, not from a direct selector-to-family CSS rule. Numeric typography sizes, spacing scale, and corner-radius values are proposed design defaults, not measured pixel values, since the source CSS referenced theme variables (e.g., `--font-heading-scale`, `--product-card-corner-radius`) without resolved values in the supplied evidence. Licensing and web-font availability for Nickainley and Kollektif were not verified. Colors associated with third-party payment-network logos (e.g., red/orange/blue combinations typical of card-brand marks) were deliberately excluded from brand token roles despite appearing in the raw palette. Mobile menu behavior, search interaction, and cart-drawer visuals were described only insofar as text content confirmed their existence, not their visual styling.
