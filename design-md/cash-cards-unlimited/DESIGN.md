---
version: alpha
name: "Cash Cards Unlimited"
source_url: "https://cashcardsunlimited.com"
captured_at: "2026-09-28T04:44:47.610816+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cash Cards Unlimited runs on a dark Shopify theme (`colorBody:#000000`,
  `colorDrawers:#000000`, `colorFooter:#000000`) with white and off-white
  text (`colorDrawerText:#ffffff`, `colorFooterText:#ffffff`), a lime-green
  action color (`colorBtnPrimary:#0db300`, `colorAnnouncement:#0db300`) paired
  with black button text (`colorBtnPrimaryText:#000000`), and a secondary
  cobalt blue (`#2c4acc`, `--jdgm-primary-color`) used by the review widget
  and likely echoed in other links or badges. A navy (`#122582`) and a softer
  green (`#56ba48`) appear as additional theme-builder color slots whose
  exact usage is inferred rather than directly observed in layout. Headings
  use Anton at 42px/400/1.2 line-height with 0.05em tracking (`:root`
  typography variables); body copy computes to ~16.56px from an Anton base
  size, though Anton as a body font is unusual and its rendering fidelity is
  unverified. Poppins appears explicitly on button elements. Two divergent
  button-radius systems exist in the CSS — a 50px pill radius on theme
  buttons versus a 0% radius on theme-builder buttons — both preserved here
  as distinct proposed components. This spec renders a dark, high-contrast,
  collector-marketplace aesthetic: black canvas, bright green CTAs, red sale
  accents, and dense card-grid merchandising suited to trading-card and
  sports-memorabilia browsing.

colors:
  primary: "#0db300"
  ink: "#ffffff"
  canvas: "#000000"
  body: "#eeeeee"
  muted: "#999999"
  hairline: "#2b2a27"
  surface-soft: "#111111"
  surface-card: "#222222"
  on-primary: "#000000"
  accent: "#2c4acc"
  secondary: "#122582"
  danger: "#d02e2e"
  success: "#56ba48"
  highlight: "#fbcd0a"
typography:
  display-xl: {fontFamily: "Anton, sans-serif", fontSize: 72px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.02em}
  display-md: {fontFamily: "Anton, sans-serif", fontSize: 42px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.05em}
  title-md: {fontFamily: "Anton, sans-serif", fontSize: 23px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.025em}
  body-md: {fontFamily: "Anton, sans-serif", fontSize: 16.56px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.025em}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0em}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.02em}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    overlayColor: "{colors.canvas}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  sale-price-display:
    regularPriceColor: "{colors.muted}"
    salePriceColor: "{colors.danger}"
    saveBadgeColor: "{colors.highlight}"
    typography: "{typography.body-md}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** uses the observed lime green (`#0db300`) with black text, matching `colorBtnPrimary`/`colorBtnPrimaryText` exactly, and the pill shape reflects the `--buttonRadius: 50px` variable, generalized here to `rounded.full`. Hover/active states are not observed and are proposed as a standard opacity-dim treatment.

**button-secondary** models the alternate theme-builder button rule (`.ecom-builder button`), which uses navy (`#122582`) fill, white text, and a flat `border-radius: 0%`. This is preserved as a distinct, squarer secondary action style for promotional or section-embedded CTAs rather than global theme buttons.

**text-input** is proposed using the dark surface tone and drawer border color for a low-contrast dark-mode form field, consistent with the site's black body background. Focus and error states are not observed and are proposed conventions.

**nav-bar** reflects the black background/white text scheme used across header, drawer, and footer color variables, with an extensive megamenu implied by the category list (Magic, Pokemon, Sports, Other TCGs, Accessories). Sticky behavior and dropdown mechanics are not observed.

**product-card** is proposed with a slightly lifted surface (`#222222`) against the black canvas to separate merchandising tiles, sized around the observed `--grid-gutter: 22px` (approximated to `spacing.lg`). Title uses the collection-title size token (23px) and price uses body typography.

**hero** applies the larger theme-builder heading scale (72px/600/-0.02em) over the black canvas, consistent with slideshow/announcement content described in the page text (e.g., "PREMIUM TRADING CARD & COLLECTIBLES EXPERIENCE"). Slide transition and overlay opacity are proposed, not measured.

**footer** carries the black background/white text footer variables directly, with generous vertical padding proposed for the long link list (Community, Retail Stores, social icons) evident in the page text.

**badge** is proposed in the observed red (`#d02e2e`) for "Sale" flags seen throughout the product excerpt ("Sale", "Sold Out"), sized small per caption typography.

**search** is a proposed pill-shaped dark field consistent with the icon-search UI element referenced in the page text, using muted gray for the icon.

**sale-price-display** directly reflects the page text's regular/sale/save pricing pattern (e.g., "Regular price $15.00 Sale price $8.99 Save $6.01"), pairing a muted strikethrough-style regular price with a red sale price and a yellow save-amount badge.

## Responsive Behavior

This is a recommendation based on common e-commerce patterns, not measured site behavior:

| Breakpoint | Width      | Nav behavior            | Grid columns |
|-----------|------------|--------------------------|--------------|
| mobile    | <768px     | hamburger + drawer menu  | 1–2          |
| tablet    | 768–1023px | condensed horizontal nav | 2–3          |
| desktop   | ≥1024px    | full megamenu            | 3–5          |

Touch targets should be at least 44px, with button-primary/secondary padding sufficient at default sizes. The megamenu (Magic, Pokemon, Sports, Other TCGs, Accessories) should collapse into an accordion-style drawer below tablet width. Cart and search icons should remain persistently visible in the compact header per the observed icon-driven header markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, hover states, animations, or actual mobile breakpoints were observed. Several theme-builder color variables (e.g., `#122582`, `#56ba48`, hashed slots like `--ecom-global-colors-BBUDPw2G`) have unclear semantic roles and their component usage here is inferred, not confirmed. The base body font resolving to Anton at ~16.56px is unusual for long-form text and its real-world legibility/rendering is unverified. Two conflicting button-radius systems (50px pill vs. 0% flat) were both preserved as separate components rather than resolved, since the CSS does not indicate which governs primary storefront CTAs. Font availability and licensing for Anton, Poppins, and Nunito Sans were not verified beyond their appearance in `font-family` declarations. All spacing values beyond the explicitly observed `--grid-gutter: 22px` and `--drawer-gutter: 30px` are proposed scale conventions, not measured site spacing.
