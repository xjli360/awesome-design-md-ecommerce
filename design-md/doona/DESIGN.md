---
version: alpha
name: "Doona"
source_url: "https://doona.com"
captured_at: "2026-09-28T09:06:02.501414+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Doona's evidence shows a strict black-and-white foundation: body copy renders in pure black (#000) on a white canvas, with primary calls-to-action using the same black/white pairing (button_default and filledBlackHover both set black background with white text). A cluster of neutral grays (#595959, #707070, #8f8f8f, #e5e7eb, #e0e0e0, #f7f5f4, #f8f8f8) supports secondary text, hairlines, and soft surfaces typical of a premium juvenile-products storefront. A small set of saturated hues (#fed100, #228b22, #ed0303, #deb887, #37504d) appear only in the raw palette without selector context; these are treated as inferred product/color-swatch values (e.g., "Midnight Edition" or accessory colorways) rather than core UI colors. #007aff is the Swiper carousel theme accent, retained here as an interactive accent. The only observed font family is "century-gothic-std" with a standard system-sans fallback stack, suggesting a clean, geometric, minimal-personality typographic voice consistent with a safety-focused baby-gear brand. All type sizes, weights, radii, and spacing below are proposed conventions layered onto this restrained observed palette, not measured values, since the CSS evidence exposes only resets, variables, and hover-state color swaps rather than a full type or spacing scale.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#3c3f41"
  muted: "#707070"
  hairline: "#e5e7eb"
  surface-soft: "#f8f8f8"
  surface-card: "#f7f5f4"
  on-primary: "#ffffff"
  accent: "#007aff"
  border-soft: "#e0e0e0"
  disabled: "#9ca3af"
  swatch-yellow: "#fed100"
  swatch-green: "#228b22"
  swatch-red: "#ed0303"
  swatch-tan: "#deb887"
  swatch-forest: "#37504d"
typography:
  display-xl: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "century-gothic-std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-filled-white-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    hoverBackgroundColor: "{colors.canvas}"
    hoverTextColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "6rem"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
  color-swatch-selector:
    backgroundColor: "{colors.canvas}"
    swatchSize: "{spacing.lg}"
    swatchRounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    availableColors: ["{colors.swatch-yellow}", "{colors.swatch-green}", "{colors.swatch-red}", "{colors.swatch-tan}", "{colors.swatch-forest}"]
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** renders the observed black-fill/white-text pattern seen in `.button_default__EXDu2` and the black hover variant, used for primary conversions such as "Explore with Doona." **button-secondary** is a proposed outline variant using the observed hairline gray for cases needing a lower-emphasis action beside a primary button; its exact visual treatment is not confirmed in the CSS. **button-filled-white-hover** documents the literal inverse hover behavior captured in `.button_filledWhiteHover__cQGLG:hover` and `.button_filledBlackHover__Z6c2d:hover`, where fill and text colors swap on interaction — a real observed state, not proposed. **text-input** is a proposed pattern for account, search, and newsletter fields; no dedicated input styling was present in the evidence beyond generic resets. **nav-bar** reflects the confirmed `--header: 6rem` CSS variable and the multi-tier navigation text (Doona Car Seat & Stroller, Liki Trike, Accessories, Doona's world) visible in the page content, styled with the neutral canvas/ink pairing. **hero** is proposed to carry the display-xl headline treatment for statements like "Wherever you go, Parenting made simple," paired with a primary CTA button. **product-card** is inferred to structure the accessory and product grid ("Doona X ISOFIX Base," "Liki Helmet," etc.) using the soft off-white surface tone for differentiation from the pure white canvas. **color-swatch-selector** is a category-appropriate addition for selecting product colorways (e.g., Midnight Edition), built from the palette's more saturated but unlabeled hues, since no swatch markup was directly present in the CSS excerpt. **footer** is proposed as a dark, ink-toned band to visually anchor the extensive legal/policy links (Privacy policy, Terms & conditions, Cookie notice) noted in the page text. **badge** and **search** are proposed low-emphasis utility components consistent with the neutral, minimal surface language observed throughout.

## Responsive Behavior
This breakpoint table is a recommendation based on common e-commerce patterns and is not measured from live site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| mobile | <640px | Collapsed hamburger, single-column stacked menu | 1-column product grid |
| tablet | 640–1024px | Condensed horizontal nav or hamburger | 2-column product grid |
| desktop | >1024px | Full mega-menu (matches multi-tier categories in page text) | 3–4 column product grid |

Touch targets are recommended at a minimum 44px hit area, consistent with the `.icon-button:after` rule's `width:max(44px,100%)` pseudo-element expansion, which is an actually observed accessibility affordance in the CSS. Collapse behavior for the mega-menu (Doona Car Seat & Stroller / Liki Trike / Accessories / Doona's world) on mobile is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS extraction and page-text evidence only; no rendered layout, computed styles, responsive breakpoints, or interaction states beyond the two hover rules noted above were observed. Semantic color-role assignments (primary, muted, surface-soft, swatch colors) are inferred from limited selector context and may not reflect actual brand usage. All typographic sizes, weights, and letter-spacing values are proposed conventions layered onto the single confirmed font-family declaration (`century-gothic-std` with system-sans fallbacks); no font-size or weight scale was present in the supplied CSS. Radius and spacing scales are proposed defaults, not extracted from site tokens. Mobile navigation collapse, cart drawer behavior, and product-swatch interaction were not present in the evidence and are marked proposed throughout. Availability, licensing, and web-delivery format of "century-gothic-std" were not verified from the supplied evidence.
