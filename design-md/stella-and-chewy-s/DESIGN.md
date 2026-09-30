---
version: alpha
name: "Stella & Chewy's"
source_url: "https://stellaandchewys.com"
captured_at: "2026-09-29T03:54:31.056909+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Shopify theme CSS variables and observed
  hex values for Stella & Chewy's, a freeze-dried raw pet food brand. The
  storefront's color system defines a warm, appetite-driven palette: a deep
  barn-red (#a60800) drives buttons and highlights against a clean white
  canvas, with black used for headings and body text per the theme's
  color-scheme variables. A warm off-white (#f5f2f0) and softer neutrals
  (#ede9e6, #f2e8da) are inferred as card and section backgrounds to keep the
  raw-food imagery warm rather than clinical. A muted umber (#594841) is
  proposed for secondary text, and a plum-red (#62001a), observed on hero
  caption text, is retained as an accent for editorial headlines. Two custom
  display faces (CCThisManThisMonster, SancySlab) appear alongside DM Sans as
  the workhorse body/UI font; their pairing suggests a rustic-meets-modern
  tone appropriate to "farm to bowl" messaging, though exact usage per
  heading level is not verifiable from static CSS. Border-radius tokens
  observed range from 0em (buttons) to 0.4em (featured-product blocks),
  supporting a mostly-flat, occasionally-rounded card system. All interactive
  states beyond the documented hover values are proposed, not observed.

colors:
  primary: "#a60800"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#594841"
  hairline: "#dedede"
  surface-soft: "#f5f2f0"
  surface-card: "#ede9e6"
  surface-alt: "#f2e8da"
  on-primary: "#ffffff"
  accent-plum: "#62001a"
  accent-gold: "#d4af37"
  link: "#1990c6"
  link-hover: "#136f99"
  success: "#00792e"
  border-subtle: "#cccccc"
typography:
  display-xl: {fontFamily: "CCThisManThisMonster, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "CCThisManThisMonster, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-lg: {fontFamily: "SancySlab, serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "DM Sans, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "DM Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "DM Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "DM Sans, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-plum}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  subscription-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** renders the barn-red fill (`#a60800`) with white label text, matching the theme's `--scheme-buttons-background` variable; used for primary CTAs like "Add to cart" and promo actions. Hover states are proposed to darken toward `accent-plum` since no hover-fill value was captured for this element.

**button-secondary** is an outline variant using the same red for border and label on a transparent field, mirroring the theme's documented `--scheme-buttons-background2: transparent` / `--scheme-buttons-label2: #a60800` pairing — an observed token, though its exact on-page usage is inferred.

**text-input** proposes a flat white field with a light gray border (`#cccccc`), sized for filters or email capture forms; no live input styling was present in the extracted CSS, so padding and radius are proposed defaults.

**nav-bar** reflects the `.header-outer` variables showing a large logo width (16–26rem depending on breakpoint) and generous vertical margin, suggesting a spacious, logo-forward header; link weight (400) and letter-spacing (0) are taken directly from CSS custom properties.

**hero** uses the plum-red caption color (`#62001a`) observed on the homepage hero banner text, set against the warm off-white surface; text width is constrained per the `--text-width: 40em` variable, proposed here as a max-width guide for hero copy blocks.

**product-card** adopts the soft neutral surface and the `0.4em` border-radius found on the featured-products section, rounding it to the nearest token (`{rounded.md}`); price text is set in primary red to echo the site's promotional pricing emphasis.

**badge** is proposed as a pill using primary red and white text for merchandising labels like "Best Seller" and "Picky-Eater Approved," which appear repeatedly in the product excerpt text; exact styling of these badges was not present in the supplied CSS.

**search** is inferred as a pill-shaped field consistent with the site's rounded interactive elements; no search-specific selectors were captured, so this pattern is a proposed convention rather than an observed one.

**footer** uses a warm cream surface (`#f2e8da`) with muted brown text, extending the earthy palette; layout, column count, and link styling were not present in the extracted CSS and are therefore not specified.

**subscription-selector** is a category-appropriate component representing the "Choose Frequency" subscribe-and-save control referenced in the page text; it borrows the product-card surface and primary accent color, though no dedicated CSS for this control was captured.

## Responsive Behavior

A compact, proposed breakpoint table (not measured from live rendering):

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | up to 599px | Single-column stacking, header logo shrinks per observed `--header-logo-width: 16rem` variant |
| Tablet | 600–999px | Two-column product grid; nav links collapse behind a menu (proposed) |
| Desktop | 1000px+ | Full header with `--header-logo-width: 26rem`, multi-column grids, `--container-width: 130rem` cap |

Touch targets should be at least 44px in height, consistent with the `--shopify-accelerated-checkout-button-block-size` default of 44px seen in checkout button CSS. Navigation collapse into a hamburger/drawer pattern is a standard proposal for the smaller breakpoint and was not directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived entirely from static CSS custom properties, a handful of hard-coded selectors, and page-text excerpts; no rendered layout, computed styles, or interactive states were observed. Semantic color roles (e.g., `muted`, `hairline`, `surface-card`) are inferred mappings from a much larger raw palette and may not match the brand's actual design-system naming. Font usage per heading level (CCThisManThisMonster vs. SancySlab vs. DM Sans) is proposed based on typical display/body pairing conventions, not confirmed per-element. Custom font licensing, availability, and fallback behavior were not verified. All spacing, radius, and breakpoint values beyond the few explicit `rem`/`em` variables captured are proposed conventions for a typical Shopify storefront, not measurements of the live site. Hover, focus, active, and error states are not documented in the source CSS and are marked proposed throughout.
