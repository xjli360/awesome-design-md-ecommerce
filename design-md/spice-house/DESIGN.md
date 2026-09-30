---
version: alpha
name: "The Spice House"
source_url: "https://thespicehouse.com"
captured_at: "2026-09-28T09:27:16.616831+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Spice House's observed markup centers on a warm, kitchen-market palette:
  a terracotta/orange accent (#d24602) drives promotional bars and primary
  calls-to-action, paired with a muted sage green (#627261/#627361) used for
  secondary buttons and a login-prompt bubble. Body copy and headings share a
  near-black charcoal (#3d4047) rather than true black, set against a warm
  off-white canvas (#ffffff) and a slightly warmer header surface (#f5f5f3).
  Typography splits cleanly: Canela (serif) is reserved for h1-h3 headings,
  while body copy, buttons, and search use Venus URW with Helvetica/sans-serif
  fallback — a classic "editorial serif + utilitarian sans" pairing suited to
  a specialty-foods retailer that blends recipe content with e-commerce.
  Buttons are observed as squared-off (border-radius:0) with bold, tracked-out
  uppercase-style labels (19px/700/.08em), which this spec preserves as the
  literal button-md scale while offering a softened radius token as an
  inferred, brand-safe alternative for smaller UI chrome. Additional palette
  entries (teal #108474, yellow #fbcd0a, dusty purple #a89cc8, pale cyan
  #c1e6e6) appear alongside social/review-widget colors and are treated as
  inferred category/flavor accent swatches rather than confirmed brand colors,
  since their exact usage context wasn't captured in the evidence.

colors:
  primary: "#d24602"
  secondary: "#627261"
  ink: "#3d4047"
  canvas: "#ffffff"
  body: "#3d4047"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f3"
  surface-card: "#f8f8f7"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-yellow: "#fbcd0a"
  accent-lilac: "#a89cc8"
  accent-cyan: "#c1e6e6"
  overlay: "#00000080"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "Canela, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Canela, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Canela, serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Venus URW, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Venus URW, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "Venus URW, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.08em}
  button-md: {fontFamily: "Venus URW, Helvetica, sans-serif", fontSize: 19px, fontWeight: 700, lineHeight: 1.21, letterSpacing: 0.08em}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    buttonBackground: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  spice-category-tile:
    backgroundColor: "{colors.surface-card}"
    accentBar: "{colors.accent-teal}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components
**button-primary** reflects the observed `.btn--orange` rule (`#d24602` fill, white text, bold tracked-out label) and is proposed as the default add-to-cart / primary CTA treatment; the squared corner (`rounded.none`) matches the literal `border-radius:0` seen on `.btn`.

**button-secondary** mirrors the observed `.btn--green` variant, reusing the sage `secondary` color for lower-emphasis actions such as "Continue Shopping"; hover/focus states are proposed, not observed.

**text-input** is inferred from generic form-field conventions since no explicit input border/background rule was captured; it reuses the observed hairline gray and body-sm type for consistency with the rest of the system.

**nav-bar** is grounded in `#shopify-section-header` and `.header__inner`, both set to the warm off-white `surface-soft`; sticky positioning is observed (`position:sticky`) but full nav interaction (mega-menu open/close) is proposed only.

**product-card** is an inferred pattern for a spice/blend listing tile; no explicit product-card selector was in evidence, so background, border, and spacing are proposed defaults using observed neutrals.

**hero** is proposed as a promotional band using the same `surface-soft` header tone and the Canela display type observed on headings, appropriate for seasonal or collaboration banners (e.g., "Now at Costco", "Top Chef" callouts) referenced in the page text.

**footer** is inferred; no footer-specific CSS was supplied, so the dark ink background with white text is a proposed high-contrast convention, not a confirmed observation.

**badge** is derived from the observed `.login__prompt` bubble (`#627361`/`secondary`, white text, rounded pill-like corner) and repurposed as a general small-label component (e.g., "New", "Best Seller").

**search** reflects the `.form-search-mega #search_form .btn` rule (uppercase, 14px, tracked button) combined with an inferred bordered input field, matching the site's visible header search affordance.

**spice-category-tile** is a category-appropriate, inferred component for "Explore by Cuisine/Diet/Use" grid entries referenced in the page text; it borrows the unexplained teal (`#108474`) as a decorative accent bar since its literal usage context wasn't in the CSS evidence.

## Responsive Behavior
This is a recommendation only; no breakpoints, media queries, or mobile layout were present in the supplied evidence.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | 0–599px    | Single-column stacking; nav collapses to slide-in `.nav__content` panel (selector observed, behavior inferred). |
| tablet    | 600–959px  | 2-column product/category grids. |
| desktop   | 960–1279px | 3–4 column grids; sticky header remains (observed `position:sticky`). |
| wide      | 1280px+    | Max-width content container, larger hero display type. |

Touch targets should be at least 44px; the observed `.btn` padding (`11px 20px 16px`) roughly satisfies this at desktop but should be re-verified on touch devices. Mega-menu and mobile drawer collapse behavior is proposed based on the presence of `.nav__wrapper`/`.nav__content` selectors, not confirmed animation or trigger logic.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from static CSS/text extraction only; no rendered layout, hover/focus states, animation timing, or actual responsive breakpoints were observed. Several palette entries (teal, yellow, lilac, cyan, social-brand colors like `#3b5998`, `#1da1f2`) could not be confidently mapped to a specific UI role and are treated as inferred accents rather than confirmed brand colors. Font availability and licensing for Canela and Venus URW were not verified — both should be confirmed as licensed/self-hosted or replaced with system equivalents before production use. Spacing and rounded-corner scales beyond the literal `border-radius:0` on `.btn` are proposed conventions, not measured values. Component patterns without a matching selector in evidence (text-input, product-card, hero, footer, spice-category-tile) are marked inferred and should be validated against the live site's actual DOM/CSS before implementation.
