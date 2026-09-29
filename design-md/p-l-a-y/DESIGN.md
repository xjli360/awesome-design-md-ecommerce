---
version: alpha
name: "P.L.A.Y."
source_url: "https://petplay.com"
captured_at: "2026-09-28T09:53:46.489814+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  P.L.A.Y. (Play Pet Brands) presents as a warm, craft-driven pet lifestyle
  storefront selling beds, toys and outdoor gear. The observed palette pairs
  a deep warm brown ("#402b24"), reused across many alpha-opacity variants in
  the supplied CSS, with a near-black text color ("#000000") explicitly set
  on heading elements and a soft off-white canvas ("#f9f8f7", "#ffffff").
  This brown is treated here as the inferred primary brand color rather than
  the cooler blue-gray ("#919da9") that appears only inside generic
  page-builder button classes (the "__pf" utility system), which is mapped
  instead to a secondary/neutral button role. Accent hues drawn from the
  palette - teal ("#339985"), amber ("#eca730") and orange ("#f05123") -
  are assigned to enrichment, promotional and sale contexts, matching the
  site's seasonal-savings and collection-launch copy.
  Typography leans on the observed "Manrope" and "Lato" sans-serif families
  for UI and body text, with the custom-named "CooperBTLight" reserved for
  display headlines as a proposed, licensing-unverified brand face, falling
  back to Georgia/serif. Heading sizes (32/24/20/18/16px) and button padding
  (12px 20px, letter-spacing:0) are taken directly from supplied CSS; all
  other spacing, radii and component states are proposed interpretations for
  a warm, tactile pet-goods retail experience.

colors:
  primary: "#402b24"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#555555"
  hairline: "#e4e4e4"
  surface-soft: "#f9f8f7"
  surface-card: "#f4f4f3"
  on-primary: "#ffffff"
  secondary: "#919da9"
  accent-teal: "#339985"
  accent-amber: "#eca730"
  accent-orange: "#f05123"
  accent-red: "#d12328"
  border-strong: "#a7a7a7"
typography:
  display-xl: {fontFamily: "CooperBTLight, Georgia, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Manrope, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Manrope, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Manrope, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.0, letterSpacing: 0px}
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
    textColor: "{colors.secondary}"
    border: "1px solid {colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.border-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
    typography: "{typography.body-sm}"

## Components

**button-primary** uses the warm brown fill as the main call-to-action treatment (e.g. "Shop Fall Favorites," "Shop the Trailblazing Coat"). Hover/disabled states are proposed, not observed.

**button-secondary** mirrors the outlined pattern explicitly present in the supplied CSS (`.pf-gs-button-2`, `.pf-button-3`) using the blue-gray "#919da9" border/text, treated here as a secondary or utility action (e.g. filters, "Read more").

**text-input** is a proposed pattern for the site's search and newsletter fields; no input styling was present in the supplied CSS, so border, radius and padding are inferred defaults consistent with the surrounding component system.

**nav-bar** represents the top utility/menu row implied by the page text ("Log in Search Contact ... Shop by Brand Store Locator"); a plain white bar with a hairline divider is proposed since no nav-specific CSS was supplied.

**product-card** is inferred for toy/bed listing grids implied by category navigation (Plush Toys, Tough Toys, Beds by Size). Card background and radius are proposed; typography sizes reuse the observed heading scale for product titles.

**hero** models the homepage banner pattern suggested by repeated promotional copy blocks ("Fall Fun Starts Here," "Turn Up Playtime"). The soft off-white background and large display type are proposed since no hero-specific CSS rules were supplied.

**footer** is proposed as a dark brown band using the primary color inverted with white text, a common ecommerce pattern; no footer CSS was present in evidence.

**badge** covers promotional/sale labeling implied by "Labor Day Savings," "25% off" and "Sale" navigation entries, using the orange accent as an attention color; exact badge styling is not confirmed by CSS.

**search** is a proposed pill-shaped field matching the rounded button-radius pattern (40px) observed in the CSS for other controls, applied here to the search affordance referenced in page text.

**size-selector** is a category-specific proposed component for the bed-size navigation (Small/Medium/Large/Cat) and collection filters, using an active/inactive state pair; no selector CSS was supplied, so states are inferred.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior.

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | <480px | Single-column stacking, nav collapses to a hamburger/menu icon, hero text-first with stacked CTA |
| Small tablet | 480–767px | Two-column product grids, search expands as an overlay |
| Tablet | 768–1023px | Three-column product grids, persistent top nav with condensed labels |
| Desktop | 1024–1439px | Four-column product grids, full mega-menu navigation |
| Wide | ≥1440px | Max-width content container with generous section padding ("{spacing.section}") |

Touch targets should maintain a minimum 44px height for buttons and size-selector chips. Navigation collapse and menu interaction states were not observed and are proposed for accessibility consistency.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS declarations and page text only; no rendered layout, hover/focus states, animation, or actual mobile breakpoints were observed. The primary brand color mapping (warm brown "#402b24" vs. the plugin-scoped blue-gray "#919da9") is an inferred judgment based on frequency of alpha-variant reuse, not a confirmed brand guideline. Font-to-role assignments (Manrope for UI, CooperBTLight for display, Lato for body) are proposed pairings based on the supplied font-family list; actual usage per element was not confirmed, and the custom-named "CooperBTLight" font's licensing/availability is unverified. All spacing values, border-radius scale, card/hero/footer patterns, and component interaction states are proposed conventions for the category and are not drawn from measured site behavior.
