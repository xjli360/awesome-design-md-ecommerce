---
version: alpha
name: "Stokke"
source_url: "https://stokke.com"
captured_at: "2026-09-28T09:20:46.216270+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evidence from the Stokke US storefront shows a Chakra UI–based design system layered on top of custom brand fonts ("Stokke", "Stokke-Light", "Stokke-Regular", "Stokke-SemiBold") with "circularProBook" and system sans-serif as reading fallbacks, indicating a display/body font split typical of a premium juvenile-products retailer. The observed palette is broad and includes a saturated green family (#21ad5e, #218b4d, #21cb6d) used near the cookie-consent "Accept" affordance, suggesting green is the primary interactive/brand accent rather than a decorative color. Neutrals (#ffffff, #f5f5f5, #cccccc, #2d2d2d, #000000) form the structural basis for backgrounds, hairlines, and text, consistent with "stokkeCore-black/white" tokens referenced in the CSS. Warmer tones (#ee8443, #1353b4, #cd0707, #e4c900) appear plausible as promotional-badge, link, error, and sale accents given the surrounding sale-banner copy, but their exact component roles are inferred, not confirmed by layout screenshots. This interpretation proposes a clean, high-contrast retail system: white/near-white canvases, dark neutral body copy, green primary actions, and warm accents reserved for sparing promotional emphasis — appropriate for a nursery-furniture brand emphasizing safety, craftsmanship, and Scandinavian restraint.

colors:
  primary: "#21ad5e"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#2d2d2d"
  muted: "#666666"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent-blue: "#1353b4"
  accent-orange: "#ee8443"
  danger: "#cd0707"
  warning: "#e4c900"
  success: "#21cb6d"
typography:
  display-xl: {fontFamily: "Stokke, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Stokke, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Stokke-SemiBold, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "circularProBook, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "circularProBook, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "circularProBook, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Stokke-Regular, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "4rem"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  stage-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    borderColor: "{colors.hairline}"

## Components

**button-primary** is the principal call-to-action treatment (e.g. "Add to Cart", "Sign Up"), using the green primary token against white text; this maps to the accent color observed near the cookie-consent "Accept" control, so its extension to commerce CTAs is inferred.

**button-secondary** proposes an outlined variant for lower-emphasis actions ("View Details", "Learn More"), reusing the primary green as text/border on a transparent field to preserve brand consistency without competing with primary CTAs.

**text-input** covers newsletter and account-form fields referenced in the page text (email/first/last name capture); border and background use neutral tokens since no focus-state styling was captured in the evidence.

**nav-bar** is inferred from the `--header-bar-content-block-size: 4rem` custom property, giving a fixed-height header; visual content (logo placement, link styling) is proposed, not observed.

**hero** represents the auto-rotating carousel described in the page text ("This is a carousel with auto-rotating slides"), using a soft neutral background and the largest display type for promotional messaging like the "Up to 20% off" banner.

**product-card** is a proposed pattern for listing nursery furniture (highchairs, cribs, strollers) with a card surface, hairline border, and title/price typography split; no product-grid CSS was directly supplied.

**badge** models the promotional/sale labeling implied by "Sale", "Last Chance" navigation entries, using the warm orange accent for visibility against neutral card backgrounds.

**search** proposes the "Search Products" affordance seen in the page copy, styled as a pill-shaped, low-contrast field consistent with the muted neutral surface tokens.

**footer** is proposed as a dark, high-contrast band housing the newsletter signup and legal/privacy links referenced in the evidence (Privacy Policy, unsubscribe language).

**stage-filter-chip** is a category-appropriate component for nursery furniture, supporting age/stage-based browsing (e.g. infant, toddler) common to Stokke's product line (Tripp Trapp, cribs); this is a proposed pattern, not confirmed by supplied markup.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| sm | 0–599px | Single-column stack, nav collapses to hamburger, hero text reduces to `display-md` |
| md | 600–959px | Two-column product grids, sticky search bar |
| lg | 960–1279px | Three-column product grids, persistent nav links |
| xl | 1280px+ | Four-column grids, max-width content container centered per `--max-viewport-width` token |

Touch targets should maintain a minimum 44×44px hit area for buttons and chips; the header's fixed `4rem` block size should collapse or reduce on scroll for mobile per common pattern, though no scroll-behavior CSS beyond `scroll-padding-top` was observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a page-text excerpt, and a color/font extraction — no rendered screenshots, computed layout, or interaction states were available. Semantic color-role assignments (e.g. danger, warning, accent-blue) are inferred from adjacency to promotional/error-sounding context and are unverified against actual component usage. All typography sizes, weights, and letter-spacing values are proposed defaults, not measured from computed styles, aside from the font-family names themselves, which are directly observed in the CSS. The "Stokke" and "circularProBook" custom font families' licensing, weights, and true availability are unverified; generic sans-serif fallbacks are assumed safe. Mobile navigation collapse, carousel interaction, hover/focus states, and grid column counts were not observed and are marked proposed throughout.
