---
version: alpha
name: "Art of Tea"
source_url: "https://artoftea.com"
captured_at: "2026-09-28T05:00:25.491270+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Art of Tea's storefront CSS shows a warm, editorial palette built on near-black
  ink (#231f20), soft warm off-whites (#f8f7f5, #f0eee9, #f4eee7) and a small set
  of accent tones: an organic green (#0f8354), a tea-amber (#c8894b), and two
  muted blues (#1990c6, #136f99) that likely serve informational or link states.
  A bright #155dfc appears only in the raw palette and is treated as an inferred
  framework/focus color rather than a brand color. Typography pairs Cormorant
  (serif) for headings/subheadings/accents with proxima-nova (sans-serif) for
  body copy and UI text; "Artifex Hand CF" is present in the font stack but its
  application is unobserved, so it is not assigned to any token here. Buttons
  and form inputs are defined with border-radius: 0, indicating a squared,
  minimal interface rather than rounded pill or card shapes.

  This interpretation treats the warm off-whites as section/card surfaces, the
  ink tone as primary text, and Cormorant serif display type as the vehicle for
  the brand's "hand-crafted, small-batch" tone against a restrained sans-serif
  utility layer for navigation, pricing, and forms. Rounded and spacing scales
  below are proposed conventions layered onto the observed square-cornered,
  compact-padding foundation.

colors:
  primary: "#0f8354"
  accent: "#c8894b"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#1a1a1a"
  muted: "#6a7282"
  hairline: "#dedede"
  surface-soft: "#f8f7f5"
  surface-card: "#f4eee7"
  on-primary: "#ffffff"
  border-subtle: "#cccccc"
  focus: "#155dfc"
  info: "#1990c6"
  info-deep: "#136f99"
  overlay: "#000000cc"
typography:
  display-xl: {fontFamily: "Cormorant, serif", fontSize: 50px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  display-md: {fontFamily: "Cormorant, serif", fontSize: 34px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Cormorant, serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "proxima-nova, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "proxima-nova, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 1px}
  button-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 1px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  subscription-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed dark-green tone as a solid fill with uppercase, letter-spaced button text matching the site's `text-transform: uppercase; letter-spacing: 1px` button rule, and square corners per the observed `border-radius: 0` declarations. It is the proposed treatment for primary CTAs like "Shop Now" and "Take the Quiz."

**button-secondary** is an outlined variant on white, reusing ink for border/text, for lower-emphasis actions (e.g., "See More," secondary nav CTAs). Its square radius and typography are grounded in the same button CSS; the outline pattern itself is a proposed convention, not directly observed.

**text-input** reflects the observed form-input variables: no rounding, compact padding, and small body typography. Hairline gray borders are inferred from the palette's light grays since no explicit input border color was isolated.

**nav-bar** is proposed as a white bar with ink text and hairline dividers, sized to the small caption typography seen in menu/header custom-text rules (14–16px, uppercase in places). Sticky/scroll behavior is not observed and is not asserted here.

**product-card** draws on the warm surface tone (#f4eee7) as a card background, pairing Cormorant title-md for product names with sans-serif body-sm for pricing, consistent with the heading/body font split in `:root`. Hover and quick-add states are proposed, not observed.

**hero** uses the lighter warm off-white as a full-bleed section background with the largest Cormorant display size (50px) for headline text, matching the site's h1 token, and body-md for supporting copy. Section height is inferred from the `--section-height-*` custom properties but exact hero cropping is not confirmed.

**footer** is proposed as a dark ink-background band with white text, inverting the primary palette for contrast; this inversion is a design proposal rather than a confirmed footer treatment.

**badge** (e.g., "best seller," review counts) uses the amber accent as a small pill, sized to caption typography; pill shape (`rounded.full`) is a proposed stylistic choice since observed radii elsewhere are 0.

**search** mirrors the text-input pattern with a soft warm background for the overlay/panel context implied by the site's search drawer copy ("Search Search Suggestions").

**subscription-card** is a category-specific component for the "Tea Club" subscription flow, using the card surface and primary green as an accent stripe/icon color to visually anchor recurring-order messaging.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | Single-column, nav collapses to drawer (menu markup suggests a mobile drawer pattern) |
| tablet | 640–1024px | 2-column product grids, header condenses |
| desktop | 1024–1280px | Full nav bar, multi-column grids |
| wide | >1280px | Max content width ~82rem per `--theme-page-width-custom` |

Touch targets should be at least 44px tall for buttons and nav items; the mobile drawer menu (`mobile_drawer_menu` selectors present in CSS) implies a slide-in panel pattern, though its exact animation/interaction is not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and page text only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven behavior (cart, search drawer, quiz modal) were observed. Color-to-role mapping (e.g., which tone is truly "primary" versus decorative) is inferred from frequency and typical e-commerce conventions, not confirmed brand guidelines. Rounded-corner tokens beyond `none` are proposed extensions; the only directly observed radius value is 0 (square buttons/inputs). Spacing scale values are proposed multiples consistent with the site's `--spacing` calc pattern but the base unit itself was not numerically confirmed in the supplied evidence. "Artifex Hand CF" appears in the font-family list but no selector tying it to a specific role was supplied, so it is omitted from typography tokens. Font licensing/availability for Cormorant and proxima-nova was not verified. Mobile menu, quiz modal, and cart drawer interactions are referenced in page text but their visual/interaction design is not observed.
