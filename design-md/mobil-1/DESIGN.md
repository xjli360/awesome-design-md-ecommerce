---
version: alpha
name: "Mobil 1"
source_url: "https://mobil.com"
captured_at: "2026-09-29T04:29:43.522880+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from static CSS evidence for mobil.com, the corporate ExxonMobil site housing the Mobil™ and Mobil 1™ lubricants business. The observed palette is narrow and utilitarian: a single saturated blue (#0e469b) alongside a grayscale ink range (#333333, #454545, #848484) and white (#ffffff). No secondary brand accent, warning, or success colors were present in the supplied evidence, so status and decorative colors are proposed as reuses of the existing grayscale/blue values rather than invented.

  Typography is built on a proprietary "EMprint" family (Light, Regular, Semibold, Bold, Bold Italic, Italic weights) with Helvetica Neue, Helvetica, Arial, and Lucida Grande as observed fallbacks; a "Lato" reference also appears in the font-family list but its selector scope was not captured, so it is treated as a secondary/legacy fallback rather than a primary display face. Semibold is used for buttons, section titles, and navigation labels per the CSS; Bold appears in product-detail and benefit text; Light appears in placeholder/search text.

  The interpretation favors a dense, industrial-technical tone — flat surfaces, hairline dividers, semibold labels, and a single confident blue call-to-action color — consistent with a fuels/lubricants B2B-and-consumer hybrid site rather than a soft lifestyle retail brand.

colors:
  primary: "#0e469b"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#454545"
  muted: "#848484"
  hairline: "#848484"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "EMprintBold, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "EMprintSemibold, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "EMprintSemibold, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "20px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "EMprint, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "EMprint, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "EMprintLight, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.1px"}
  button-md: {fontFamily: "EMprintSemibold, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.2px"}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  oil-finder-tool:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    resultTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the solid blue call-to-action used for primary conversions such as "Find a Product" or "Shop Now"-style prompts; the blue is the only saturated hue in the observed palette, so it is proposed as the sole primary-action color. Hover/active states (e.g., darkening or underline) are not observed and are proposed as standard darken-on-hover behavior.

**button-secondary** is an outlined variant using the same primary blue for border and text on a white background, intended for secondary actions (e.g., "Learn More") alongside a primary button. This pairing pattern is inferred, not confirmed by layout screenshots.

**text-input** reflects the light placeholder styling (EMprintLight) and muted gray placeholder color found in the search/placeholder CSS selectors, with a hairline border and minimal corner rounding consistent with the site's flat, technical aesthetic.

**nav-bar** is inferred from the mega-menu and dropdown selectors (`.icon-nav-header`, `.nav-meganav-subitem`), which indicate a multi-level navigation system with a white background and small semibold/normal labels; actual sticky/collapse behavior was not observed in the CSS.

**product-card** is proposed for Mobil 1 product/SKU listings (e.g., viscosity-grade tiles), using a card surface with a hairline border, semibold titles, and smaller body copy — a reasonable pattern for an industrial product catalog though no specific card selector was captured.

**hero** proposes a dark, ink-colored full-width band with large bold display type in white, matching the tone of the homepage's "Welcome to Mobil™" messaging; specific hero background imagery or gradients were not present in the supplied CSS and are not assumed.

**footer** is inferred from the extensive `.footer-nav-*` and `.footer-top .nav-country` selectors indicating a large multi-region footer (evidenced by the long country/language list in the page text); a dark ink background with white text is proposed for contrast, though the actual observed footer color was not isolated in the supplied CSS rules.

**badge** is a small pill-shaped label using the primary blue, proposed for callouts like "New" or certification marks (e.g., API/ILSAC endorsement chips common to motor-oil product pages); no badge-specific selector was present in the evidence.

**search** reflects the `#gs-search`, `.CoveoSearchInterface`, and `.magic-box-input` selectors, indicating an embedded Coveo-powered search widget; the visual treatment (soft background, hairline border) is proposed since exact search-box chrome was not fully specified.

**oil-finder-tool** is a category-appropriate proposed component representing a "find the right oil for your vehicle" lookup widget, styled with a soft surface background and primary-blue accents for result highlighting — a common pattern for motor-oil sites though not directly observed in the supplied CSS.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <576px | Single-column stacks; nav collapses to hamburger/off-canvas |
| Tablet | 576–991px | Two-column product grids; mega-menu likely condensed |
| Desktop | 992–1439px | Full mega-navigation, multi-column footer |
| Wide | ≥1440px | Max-width content container, generous side margins |

Touch targets are recommended at a minimum 44×44px for buttons and nav items. The multi-level mega-menu (`.dropdown-submenu`, `.nav-meganav-subitem`) should collapse into an accordion pattern on narrow viewports. This table is a recommendation based on common responsive conventions, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS selector/declaration fragments and a text excerpt; no rendered page, computed styles, or interaction states were observed. Color-role assignments (e.g., treating #848484 as both muted text and hairline) are inferred from typical usage patterns, not confirmed against specific selectors. Font-size, line-height, and letter-spacing values in the typography tokens are proposed defaults, not extracted CSS measurements, since only font-family/weight declarations were supplied. Component states (hover, focus, active, disabled) are proposed and unverified. Mobile/responsive layout, breakpoint values, and navigation collapse behavior were not observed and are recommendations only. Availability and licensing of the proprietary "EMprint" font family were not verified; system fallbacks (Helvetica Neue, Helvetica, Arial, sans-serif) should be assumed for any reproduction. The "Lato" font reference in the evidence could not be mapped to a specific selector and its role in the live design is unknown.
