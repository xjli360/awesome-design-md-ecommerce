---
version: alpha
name: "Away"
source_url: "https://awaytravel.com"
captured_at: "2026-09-28T04:34:39.495447+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed evidence shows a Shopify-based storefront (theme variables such as
  --color-foreground, --wk-color-accent-1, and CSS custom properties) built around a
  near-monochrome system: pure ink (#111111) and white (#ffffff), with warm off-white
  surfaces (#faf9f6, #f7f4f1, #f8f8f8) suggesting a paper/canvas-like product context
  suited to a hard-shell luggage brand. Buttons default to solid black on white
  (--color-button, --wk-color-accent-1), with squared corners (--wk-button-border-radius:
  0px) rather than rounded pills, indicating a utilitarian, editorial aesthetic. Two
  fonts are observed in font-family stacks: Graphik (sans, likely UI/body) and Lyon
  Display (serif, likely headline/display), plus Replica Mono appearing as a possible
  accent/mono typeface. A small set of functional colors appear only in checkout/payment
  widgets (#1990c6 accelerated-checkout blue, #dedede skeleton gray) and are treated here
  as system rather than brand colors, though reused sparingly for informational states.
  Reds (#d31b3b, #ea1e42) and a soft pink/maroon pair (#f5d5db, #58162a) are inferred as
  sale/badge and warm accent roles since no direct usage context was supplied. All
  semantic role assignments beyond --color-* variables are inferred from naming
  conventions and general e-commerce patterns, not confirmed page renders.

colors:
  primary: "#111111"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#2a2a2a"
  muted: "#666666"
  hairline: "#e2e1e1"
  surface-soft: "#faf9f6"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  border-subtle: "#dedede"
  accent-sale: "#d31b3b"
  accent-alert: "#ea1e42"
  accent-info: "#1990c6"
  accent-info-hover: "#136f99"
  accent-success: "#25b900"
  surface-blush: "#f5d5db"
  accent-maroon: "#58162a"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Lyon Display, Georgia, serif", fontSize: 56px, fontWeight: 500, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lyon Display, Georgia, serif", fontSize: 36px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "Graphik, system-ui, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Graphik, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Graphik, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Graphik, system-ui, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.05em}
  button-md: {fontFamily: "Graphik, system-ui, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.05em}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    minHeight: 45px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 80px
    borderBottom: "{colors.hairline}"
    padding: "{spacing.none} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    surface: "{colors.surface-soft}"
    textColor: "{colors.body}"
    priceColor: "{colors.ink}"
    secondaryTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    resultLinkColor: "{colors.ink}"
    resultSecondaryColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    surface: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 24px
    padding: "{spacing.xxs}"

## Components

**button-primary** renders the solid black-on-white call to action derived directly from `--color-button` (17,17,17) and `--color-button-text` (255,255,255). Corners are squared per `--wk-button-border-radius: 0px`, giving a utilitarian, non-rounded feel consistent with a hard-shell product line. Hover/focus states are proposed, not observed.

**button-secondary** mirrors the observed `--color-secondary-button` (white fill, black text, presumably bordered) for outline-style actions such as "Learn more." Border color and hover treatment are inferred, since no explicit secondary-button CSS rule was supplied.

**text-input** uses the measured `--wk-input-min-height: 45px` and `--wk-input-border-radius: 0px` to define a flat, full-height field for newsletter/search/account forms. Border and focus-ring colors are inferred from the neutral hairline palette.

**nav-bar** is based on `#main-header`, which is fixed-position, full-width, and transitions `transform` on scroll (`translateY`), implying a hide-on-scroll pattern. Height and horizontal padding are proposed since no explicit spacing tokens were supplied for the header shell.

**product-card** is inferred from `.product-tile-search__link`, `__price`, and `__colors` rules: primary text uses `--color-foreground`, secondary text (e.g., color-option labels) uses a lighter `--color-foreground-secondary`. Layout (image, title, price, swatches) is a proposed e-commerce pattern, not a captured DOM screenshot.

**hero** is proposed as a full-bleed introductory section using the warm off-white surface (`#faf9f6`) and the Lyon Display headline style, consistent with lifestyle/product photography typical of a DTC luggage brand; no hero markup was directly supplied.

**footer** is proposed as an inverted (dark-on-light-text) block using the primary ink tone, a common Shopify-theme footer treatment; no footer-specific selectors were present in evidence.

**badge** reflects `.product-badge` (uppercase, 0.05em letter-spacing, 500 weight, absolute-positioned) and `.product-tile-in-cart-badge--below-badges` (foreground-on-background inverse chip), used for labels like "New," "Sale," or "In Cart."

**search** is a proposed overlay/panel pattern built from the `.product-tile-search__*` classes, styling result rows with the same foreground/secondary text hierarchy as product cards.

**color-swatch-selector** is a category-specific, proposed component for luggage color options (a common pattern for hard-shell cases sold in multiple finishes), using a circular swatch with a hairline border and an ink-colored selected state; no direct swatch CSS was present in evidence.

## Responsive Behavior

The following breakpoints are a **recommendation** based on common Shopify-theme conventions, not measured from the live site:

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| Mobile    | 0–767px    | Single-column product grid; nav collapses to `.mobile-menu__store-button` pattern implied by CSS. |
| Tablet    | 768–1023px | Two-column product grid; header remains fixed per `#main-header`. |
| Desktop   | 1024–1439px| Full nav visible; hero and product-card grids expand to 3–4 columns. |
| Wide      | 1440px+    | Max-width content container, increased section padding (`{spacing.section}`). |

Touch targets should meet a **minimum 44–45px** height, aligning with the observed `--wk-button-min-height: 45px` and `--wk-input-min-height: 45px` tokens. Mobile navigation collapse behavior is inferred from the presence of `.mobile-menu__store-button` but its actual open/close interaction was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a partial rule set, and a color/font inventory — no live DOM, computed layout, or interaction states were captured. Semantic role assignments (e.g., which hex maps to "primary" vs. "accent") are inferred from variable naming (`--color-button`, `--wk-color-accent-1`) and general e-commerce conventions, not confirmed visually. Several palette colors (e.g., `#0038ff`, `#c0c2c8`, `#8ca691`) had no accompanying selector context and were intentionally excluded from role assignment rather than guessed. Typography sizes, line-heights, and letter-spacing outside the two directly observed rules (`.product-badge`, checkout button) are proposed defaults, not measured values. Hover, focus, active, and error states for all components are proposed and unverified. Mobile menu behavior, swatch interaction, and hero/footer markup were not present in the supplied evidence. Availability, weights, and licensing of Graphik, Lyon Display, and Replica Mono are unverified and should be confirmed with Away/foundry licensing before implementation.
