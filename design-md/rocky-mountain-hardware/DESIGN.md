---
version: alpha
name: "Rocky Mountain Hardware"
source_url: "https://rockymountainhardware.com"
captured_at: "2026-09-28T04:50:11.450523+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Rocky Mountain Hardware's public site evidence centers on a warm, artisanal
  bronze identity layered over a standard WordPress theme foundation. The only
  brand-specific accent confirmed in the CSS is a warm bronze/gold, "#B38B4D",
  which appears on the lead-capture CTA button, the careers apply button's
  border and hover fill, the custom search title, and social-share icon color.
  A dark warm charcoal, "#3C403D"/"#3D403D", is used for heading and button
  text near that bronze accent, suggesting an ink role distinct from pure
  black. A separate near-black slate, "#32373c", is the default WordPress
  button background used broadly for generic CTAs and file-download buttons;
  it is treated here as a secondary neutral action color since its brand
  intent is unconfirmed. Two custom-adjacent typefaces are observed:
  "brandon-grotesque" for display headings and buttons (uppercase, light
  weights), and an inherited sans-serif stack (likely "Source Sans Pro",
  present in the font list) for body copy. Neutral grays ("#eee", "#f5f5f5",
  "#dddddd", "#959595") are inferred as surface, hairline, and muted-text
  roles based on conventional WordPress utility class naming, not measured
  usage. All rounding, spacing, and several component states below are
  proposed conventions layered onto this limited evidence, not verified
  visual measurements.

colors:
  primary: "#B38B4D"
  ink: "#3C403D"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#959595"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary-action: "#32373c"
  section-dark: "#313131"
  section-light: "#eeeeee"
  border-subtle: "#cccccc"
typography:
  display-xl: {fontFamily: "brandon-grotesque, sans-serif", fontSize: "42px", fontWeight: 300, lineHeight: 1.1, letterSpacing: "0px"}
  display-md: {fontFamily: "brandon-grotesque, sans-serif", fontSize: "32px", fontWeight: 300, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "brandon-grotesque, sans-serif", fontSize: "20px", fontWeight: 300, lineHeight: 1.2, letterSpacing: "0.01em"}
  body-md: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.55, letterSpacing: "0px"}
  caption: {fontFamily: "'Source Sans Pro', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "brandon-grotesque, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0.03em"}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-generic:
    backgroundColor: "{colors.secondary-action}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.section-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.lg}"
  finish-swatch:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.section-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.display-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"

## Components

**button-primary** reflects the bronze CTA seen on the lead-capture modal (uppercase brandon-grotesque, solid bronze fill, square corners in that instance). It is proposed as the primary conversion action (e.g., "Request a Brochure," "Find a Dealer").

**button-secondary** mirrors the observed careers "apply" button: a bronze-bordered, transparent-fill button with dark ink text that inverts to a bronze fill on hover (hover state is CSS-confirmed for this specific component only).

**button-generic** captures the site-wide default WordPress button treatment (`.wp-element-button`), a dark slate pill used for block-editor buttons and file downloads; its brand significance versus bronze CTAs is unconfirmed, so it is kept as a distinct, lower-emphasis action style.

**text-input** is proposed for search and form fields (newsletter signup, dealer locator); no input CSS was present in evidence, so styling follows conservative neutral defaults.

**nav-bar** is inferred from the large, multi-level navigation text listed in page content (Products, Collections, Finish Options, Resources, etc.); no header CSS (height, sticky behavior, dropdown styling) was observed, so this remains a structural proposal only.

**hero** is modeled on the homepage's promotional banner rotation ("Explore the Cirque Collection," "It's all in the details") using the light neutral section background and large display type; exact hero CSS (image treatment, overlay) was not present in evidence.

**product-card** is proposed for collection/category tiles (Element, Edge, Metro, etc.); card elevation, image aspect ratio, and hover motion are not observed and are treated as reasonable e-commerce defaults.

**finish-swatch** is a category-appropriate proposed component representing the "Craft Your Perfect Fit" finish-selection UI referenced in copy; no swatch markup or CSS was captured, so shape and sizing are inferred conventions.

**footer** uses the dark neutral section background documented via the `.has-very-dark-gray-background-color` utility class, extended here as a plausible footer treatment though no footer-specific selector was captured.

**badge** and **search** are lower-confidence proposals: badge is a generic bronze pill for labeling ("New," "RMH Express"), while search directly reuses the one confirmed rule for `.custom-search-title` (bronze, light-weight, letter-spaced heading).

## Responsive Behavior

Recommended, not measured, breakpoints: mobile up to 599px, tablet 600-959px, desktop 960-1279px, wide 1280px+. Navigation is expected to collapse into a hamburger/off-canvas menu below tablet width given the density of the listed menu taxonomy (8+ top-level items, 25+ collections). Touch targets should be a minimum of 44x44px for buttons and swatches. Product/collection grids are recommended to reflow from 4-column (desktop) to 2-column (tablet) to 1-column (mobile). None of this responsive behavior was observed in the supplied static CSS; it is a standard-practice recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS excerpts, a page-text crawl, and a partial color/font inventory only — no live rendering, computed layout, DOM interaction, or viewport testing was performed. The primary bronze ("#B38B4D") and ink ("#3C403D") roles are extrapolated from a small number of matching selectors (modal, careers button, search title) and may not represent the full site's color system. The "#32373c" default WordPress button color and dark/light neutral section backgrounds are template-level utility classes whose brand intent is unconfirmed. "brandon-grotesque" appears only in a third-party lead-capture modal's inline styles; its use elsewhere on the site, its licensing, and web-font availability are unverified. "Source Sans Pro" is inferred as the probable body font from the supplied font-family list but no selector confirms its application. All spacing, rounding scale, hover/focus/active states (aside from the one confirmed careers-button hover), form-field styling, mobile navigation pattern, and card/grid layouts are proposed conventions, not observed evidence.
