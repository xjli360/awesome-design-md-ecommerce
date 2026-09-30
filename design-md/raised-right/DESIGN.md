---
version: alpha
name: "Raised Right"
source_url: "https://raisedright.com"
captured_at: "2026-09-28T10:32:53.807385+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Raised Right's supplied CSS reflects a WordPress/WooCommerce build layered with a
  small set of brand-specific colors over default Gutenberg block-editor swatches.
  A recurring olive-green family (#b4be35, #a3a300, #b6bd00, #bec400) is treated as
  the brand primary, echoing the company's pasture-and-agriculture story; it pairs
  with a warm brown (#4c2b06) and an orange confirmed directly on the WooCommerce
  "Add to Cart" button (#da6226). A rose tone (#b33451) is confirmed on WooCommerce
  price text. Neutral structure comes from a dark warm-gray body color (#4c4841) on
  a light blue-gray surface tint (#f2f5f8) and white cards, with #e5e7eb/#cccccc for
  hairlines. Typography is built on the custom Pluto family: PlutoRegular is
  confirmed via CSS on body, h1, and button selectors; PlutoBold/PlutoMedium/
  PlutoCondBold variants are present in the loaded font stack but no supplied CSS
  rule ties them to specific selectors, so their use for display/title hierarchy
  here is inferred, not observed. Rounded corners follow the confirmed 9999px pill
  radius from `.wp-block-button__link`, extended into a generic scale. The overall
  interpretation favors an earthy, transparent, farm-to-bowl aesthetic consistent
  with the brand's human-grade, whole-food messaging, while default WordPress/
  Gutenberg palette entries are excluded from primary brand roles where possible.

colors:
  primary: "#a3a300"
  ink: "#2b2d2f"
  canvas: "#ffffff"
  body: "#4c4841"
  muted: "#8c8c8c"
  hairline: "#e5e7eb"
  surface-soft: "#f2f5f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cta: "#da6226"
  accent-price: "#b33451"
  nav-dark: "#32373c"
  brand-brown: "#4c2b06"
  ink-strong: "#111827"
  olive-deep: "#b6bd00"
  border-soft: "#cccccc"
typography:
  display-xl: {fontFamily: "PlutoCondBold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "PlutoBold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "PlutoMedium, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "PlutoRegular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "PlutoRegular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "PlutoRegular, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "PlutoRegular, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-cta:
    backgroundColor: "{colors.accent-cta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    heading: "{typography.display-xl}"
    body: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.accent-price}"
    padding: "{spacing.base}"
  recipe-selector-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.olive-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components
**button-primary** uses the confirmed pill radius (9999px) seen on `.wp-block-button__link`, mapped to the inferred olive primary color; state changes (hover/active/disabled) are proposed, not observed. **button-secondary** proposes an outline treatment consistent with the `.is-style-outline` rule that sets a transparent background and `currentColor` text. **button-cta** isolates the one directly confirmed action color in the evidence, `#da6226`, taken from `button.single_add_to_cart_button.button.alt`, and is intended for primary commerce actions like "Add to Cart." **text-input** is a proposed pattern; no input-specific CSS was supplied, so border, radius, and padding are inferred from the surrounding design system for consistency. **nav-bar** is inferred from the presence of a repeated menu structure in the page text (Home, Buy a Box, Recipes, Treats, Store Locator, Reviews) but no nav-specific CSS rules were included, so colors and spacing are proposed. **hero** reflects the homepage copy block ("HUMAN-GRADE PET FOOD") and uses the light surface tint `#f2f5f8` as a plausible section background; exact hero layout was not observed. **product-card** and **recipe-selector-card** are category-appropriate proposals for displaying dog/cat food recipes and treats; the price color (`#b33451`) is directly confirmed from `.woocommerce div.product span.price`, while card borders, radius, and spacing are inferred. **badge** proposes a small pill label (e.g., "Human-Grade," "Vet Formulated") using an olive accent, styled to match confirmed pill-button radius conventions; no badge CSS was supplied. **search** and **footer** are proposed patterns: footer uses the confirmed dark neutral `#32373c` seen on default button backgrounds, repurposed as a footer surface, which is a reasonable but unverified extension.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior; no media queries were present in the supplied evidence.

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | up to 599px | Single-column stacking; nav collapses to a menu toggle (proposed) |
| Tablet | 600–1023px | Two-column product/recipe grids proposed |
| Desktop | 1024px+ | Multi-column grids, persistent top nav proposed |

Touch targets should be at minimum 44×44px for buttons like `button-primary` and `button-cta`. Navigation collapse behavior, sticky headers, and mobile menu treatment are proposed conventions only, not derived from observed JavaScript or responsive CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered layout, hover states, animations, or interaction behavior were observed.
- Several supplied hex values (e.g., `#2563eb`, `#cf2e2e`, `#fcb900`, `#0693e3`, `#9b51e0`, `#f78da7`, `#7bdcb5`, `#00d084`, `#8ed1fc`, `#abb8c3`) match the default WordPress/Gutenberg editor color palette and were deliberately excluded from primary brand-role mapping, though they remain available in the raw palette if needed.
- The olive-green family selected as `primary` is an inferred brand color based on recurrence across near-duplicate hex values; no single CSS rule in the evidence explicitly labels it as the brand's primary action color.
- Only `PlutoRegular` is confirmed via CSS declarations (`body`, `h1`, `button` selectors). Assignment of `PlutoBold`, `PlutoMedium`, and `PlutoCondBold` to specific display/title roles is inferred from font-family names present in the loaded font list, not from selector-level CSS evidence.
- Custom font availability, licensing, and actual rendering fallback behavior for the Pluto family were not verified.
- All font sizes, letter-spacing, and line-height values are proposed defaults, not measured from rendered typography.
- Spacing and rounded-corner scales beyond the one confirmed `9999px` pill radius are proposed conventions for internal consistency, not observed measurements.
- Component states (hover, focus, disabled, active) are proposed and unverified except where explicitly noted (e.g., `button.button.alt.disabled` background `#000000`).
- Mobile/responsive layout, breakpoints, and navigation collapse behavior were not present in the supplied evidence and are recommendations only.
