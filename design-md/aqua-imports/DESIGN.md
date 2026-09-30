---
version: alpha
name: "Aqua Imports"
source_url: "https://aqua-imports.com"
captured_at: "2026-09-28T09:54:51.337002+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Aqua Imports presents a WordPress/WooCommerce storefront built on a
  utilitarian system-font stack (-apple-system, BlinkMacSystemFont, Segoe UI,
  Roboto, Helvetica Neue, sans-serif) with no custom webfont declared in the
  supplied CSS. Body copy renders at 17px/1.6 in a slate gray (#4a5568), while
  h1 headings use a darker near-black (#1a202c) at 32px/1.5, 700 weight —
  both values pulled directly from the theme's global-palette custom
  properties. A 42px "huge" preset size is available for hero-scale display
  type. The interpretation designates #007cba (the theme's own admin/action
  blue, observed as --wp-admin-theme-color) as the primary interactive color,
  with its documented darker variant #006ba1 as a hover/pressed state — both
  are literal observed values, not invented. #34e2e4, an aqua/cyan tone
  present in the raw palette, is assigned an inferred accent role fitting the
  "Aqua Imports" brand name for badges and highlights on livestock cards.
  Warm orange (#f76a0c) and green (#2fa84f) are reused from the palette for
  secondary alert and guarantee/success badges respectively (e.g. "Arrive
  Alive Guarantee"). Rounded corners default to a pill shape (9999px) as seen
  on .wp-block-button__link, softened to smaller radii for cards and inputs.
  Fully-rounded pill buttons and a dense, deeply-nested mega-menu (observed
  submenu font-size 12px) both point to a catalog-heavy, navigation-first
  retail experience.

colors:
  primary: "#007cba"
  primary-hover: "#006ba1"
  ink: "#1a202c"
  canvas: "#ffffff"
  body: "#4a5568"
  muted: "#718096"
  hairline: "#e5e7eb"
  surface-soft: "#f7fafc"
  surface-card: "#edf2f7"
  on-primary: "#ffffff"
  accent: "#34e2e4"
  accent-warm: "#f76a0c"
  success: "#2fa84f"
  danger: "#cc1818"
  dark-surface: "#313131"
  border-strong: "#333333"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.5, letterSpacing: 0px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica Neue, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hoverTextColor: "{colors.accent-warm}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    accentColor: "{colors.accent}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaBackground: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  shipping-guarantee-callout:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.success}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** is the pill-shaped call-to-action (add-to-cart, "Shop Freshwater Fish") built on the observed `border-radius:9999px` pattern from `.wp-block-button__link`, using the theme's admin-blue as background. **button-secondary** proposes an outline variant for lower-emphasis actions like "View All New Arrivals," reusing the same primary color as border/text with a transparent fill; this variant is not directly observed and is proposed. **text-input** covers search and account fields with a light hairline border and sharp-but-slightly-rounded corners; padding and focus states are proposed. **nav-bar** reflects the deeply nested mega-menu structure evidenced by `.header-navigation ... ul ul li.menu-item > a` (12px submenu items, hover color shift to an accent tone on a dark background) — the hover-to-warm-accent mapping is inferred from the available orange in the palette. **product-card** models the repeating livestock tiles (name, price range, "Select options") seen in the New Arrivals grid, using a soft card surface and an aqua accent for stock/new badges — card chrome details are proposed, not measured. **hero** represents the homepage banner introducing "Freshwater Fish & Aquatic Plants... Shipped Nationwide," using the large 42px preset size and a dark ink background; exact hero styling is inferred from typographic presets only. **footer** is proposed as a dark surface (reusing the theme's `--wp-editor-canvas-background`-adjacent dark gray) since no footer-specific CSS was supplied. **badge** generalizes small status labels (e.g., stock/guarantee indicators) using the observed green from the palette. **search** is proposed styling for the header "Products search" field noted in page text, no dedicated CSS observed. **shipping-guarantee-callout** is a category-specific component modeling the "Arrive Alive Guarantee / Expert Packing / Fast Shipping" trio of value props visible in the page text, styled with a soft surface and success-green accenting; entirely proposed, no direct CSS backing.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤599px (single-column product grid, collapsed hamburger nav replacing the multi-level mega-menu), tablet 600–959px (2-column grid, condensed nav), desktop ≥960px (full mega-menu with flyout submenus as suggested by the nested `ul ul li` selectors, 3–4 column product grid). Touch targets should be at least 44×44px for cart/select-option controls given the dense catalog of price-range products. This is a design recommendation only; no actual responsive/mobile layout was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom-property dumps and a single page-text excerpt, not a rendered or interactive site capture. `--global-heading-font-family` and `--global-body-font-family` were referenced but never resolved to concrete values in the supplied evidence, so all typography uses the observed system-font list rather than a confirmed brand typeface — no custom/licensed font was found or assumed. Numerous `--global-palette*` custom properties (e.g., blues, oranges, and an amber at `#f5a524`) appear in `:root` but were not included in the separately supplied observed-colors array and have therefore been excluded from this palette entirely, even though they exist in the raw CSS. Component states (hover, focus, disabled, mobile menu open/close) are proposed conventions, not confirmed interactions. Spacing scale values beyond the two explicit `--global-content-boxed-padding` entries (2rem/1.5rem) and the button padding formula are estimated design-system conventions, not measured pixel values throughout the site. Card, hero, and footer visual treatments are inferred from typographic and color tokens only; no screenshot or rendered layout was reviewed.
