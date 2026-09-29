---
version: alpha
name: "Onyx Coffee Lab"
source_url: "https://onyxcoffeelab.com"
captured_at: "2026-09-28T10:04:05.062175+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Onyx Coffee Lab's observed CSS points to a warm, editorial coffee-brand system built on a near-black/cream duality. Header tokens explicitly define --header-primary (#000) and --header-secondary (#FCFAF2), which invert on light/dark/scroller header states, so black and a warm cream (#FCFAF2/#FBFAF3) are treated here as the primary ink and canvas pair. Supporting neutrals (#EAE8DF, #EEE9DF, #F0EFE5, #7D7D7A, #CBCBC8, #DEDEDE) suggest a soft, paper-like surface system layered under a black-and-cream frame. A small set of warmer accents — an aged gold (#AF8E38/#AE841F), a clay/terracotta (#D28467), and a peach tint (#F5D8C2) — appear alongside cooler teal-blues (#1990C6/#136F99) and a single red (#B00923); these are inferred as product/badge/CTA accents rather than confirmed brand primaries, since role attribution from static CSS is limited. Typography exposes several named families (Room-205, Bajern, Kapra, Andale) plus Montserrat and generic sans-serif; Montserrat is treated as the workhorse body face, with the others assigned inferred display/title/button roles based on typical editorial hierarchy. Swiper's default #007AFF is excluded from brand color roles as a library default. Layout, spacing, and radii below are proposed conventions grounded in observed nav/button/cart-count metrics, not measured page geometry.

colors:
  primary: "#000000"
  ink: "#191919"
  canvas: "#fcfaf2"
  body: "#333333"
  muted: "#7d7d7a"
  hairline: "#dedede"
  surface-soft: "#eae8df"
  surface-card: "#fbfaf3"
  on-primary: "#fcfaf2"
  accent-gold: "#af8e38"
  accent-clay: "#d28467"
  accent-peach: "#f5d8c2"
  accent-teal: "#1990c6"
  accent-teal-dark: "#136f99"
  accent-red: "#b00923"
  border-soft: "#cccccc"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "Room-205, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Bajern, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Kapra, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Andale, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 2px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlay: "{colors.overlay-scrim}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-teal}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders as a solid black button with cream text and wide letter-spacing, matching the observed email-popup submit button (`background:#000; color:var(--color-creme)`) and uppercase text-transform pattern. Used for primary CTAs like "Shop Now" and "Explore This Offering."

**button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g. "Learn More," "See Locations"), inferred from the site's dual-header light/dark inversion logic rather than a directly observed bordered button rule.

**text-input** is a proposed form field style (email signup, search) using the cream card surface and a light hairline border; no explicit input CSS was supplied, so padding and radius are conventions.

**nav-bar** reflects the observed `header .menu-nav a` rule: 14px text, 2px letter-spacing, and a color driven by the `--header-primary`/`--header-secondary` variable pair that flips between light and dark header states, plus a `header.scroller` sticky variant with a `--color-creme` background.

**product-card** is a proposed pattern for the coffee/tea/chocolate grid (e.g. "Doyenne," "Well Met," "Kenya Kamunyaka AA"); layout is inferred from commerce norms, not measured, using card surface and hairline border tokens.

**hero** models the homepage banner pattern seen in the supplied JSON block (headline, tasting-note copy, single image, button), using the cream canvas and a proposed dark overlay for image legibility.

**footer** is inferred as a black band echoing `--header-primary:#000`, carrying utility links (Wholesale, Locations, Learn, Support) in cream body-sm text; exact footer markup was not supplied.

**badge** covers small labels such as "Free Shipping" ticker items or roast/limited-offering tags; the gold accent is proposed rather than confirmed as the badge color, since no badge-specific CSS was in evidence.

**search** is a proposed pill-shaped input for the "GO" search affordance referenced in page text, styled with hairline border and muted placeholder text.

**subscription-card** is a category-specific component for Onyx's subscription/roaster's-choice offerings (Circadian, Echelon, Roaster's Choice), using the softer cream surface and a teal accent inferred from the observed `#1990c6`/`#136f99` pair, distinct from the swiper-library blue.

## Responsive Behavior
This is a proposed, non-measured breakpoint recommendation:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column stacking, nav collapses to a hamburger/mobile-login pattern per `header .mobile-login` |
| Tablet | 600–1024px | Two-column product grids, header remains fixed-height per `--dynamic-nav-menu-height` |
| Desktop | >1024px | Multi-column grids, full horizontal nav-bar |

Touch targets should be at least 44px, matching the swiper navigation-size convention (`--swiper-navigation-size:44px`). Mobile nav collapse and menu height (`--dynamic-nav-menu-height: 65svh`) suggest a slide-down/overlay pattern, though its visual behavior was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS/text extraction only; no rendered layout, breakpoints, hover/focus states, or JavaScript-driven interactions (cart drawer, mobile menu, carousels) were observed. Color-to-role mapping (e.g. gold, clay, teal, red accents) is inferred from typical usage patterns, not confirmed component-level CSS. Font role assignments (Room-205, Bajern, Kapra, Andale vs. Montserrat) are inferred from naming/hierarchy conventions, not measured computed styles; availability, licensing, and web-font loading for the four non-Montserrat families were not verified. All typographic sizes/weights beyond the 14px nav link and 12px cart-count text are proposed, not measured. Spacing and radius scales are conventional defaults, not extracted from the supplied CSS. The `#007aff` swiper theme color was excluded as a third-party library default rather than a brand token.
