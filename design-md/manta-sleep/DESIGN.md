---
version: alpha
name: "Manta Sleep"
source_url: "https://mantasleep.com"
captured_at: "2026-09-28T10:08:55.108525+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Manta Sleep's evidence shows a neutral, editorial base (#ffffff, #161616,
  #f7f5f0) paired with a warm coral-red accent family (#ff4551, #ff5859,
  #ff4451) used for announcement bars and scheme-2 header buttons. Three
  header/drawer "color schemes" were observed in the CSS variables (light,
  cream, and dark #161616), suggesting the brand toggles between light and
  dark section themes rather than using a single fixed palette — this
  multi-scheme pattern is inferred as a modular theming system, not a fixed
  brand rule. Typography uses Poppins for headings/alt and Montserrat for
  body text, both with sans-serif fallbacks; no proprietary font was
  confirmed. Button geometry is loosely evidenced (13px/20px padding,
  1.42 line-height, skewed pseudo-element accents), pointing to a
  slightly editorial, travel-and-wellness aesthetic rather than a purely
  clinical one. This interpretation treats #161616 as primary ink, #ff5859
  as the primary interactive accent (drawn from the scheme-2 button token),
  and #f7f5f0/#eeeadf as warm off-white surfaces for cards and soft
  sections, since no dedicated "brand color" token was labeled in the
  supplied evidence. All hex values below are reused directly from the
  observed palette; no colors were invented.

colors:
  primary: "#ff5859"
  accent: "#ff4551"
  ink: "#161616"
  canvas: "#ffffff"
  body: "#282828"
  muted: "#6b6b6b"
  hairline: "#dad8d2"
  surface-soft: "#f7f5f0"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  success: "#56ad6a"
  dark-surface: "#161616"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 13px, fontWeight: 600, lineHeight: 1.42, letterSpacing: 0.3px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  quiz-callout:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** is the coral (#ff5859) filled call-to-action for "Shop All," "Find Your Mask Quiz," and add-to-cart actions, using the observed 13px/20px padding ratio and 1.42 line-height from the submit-button CSS. **button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Compare Masks") sharing the same type scale but with an ink border and transparent fill. **text-input** is proposed for search and account forms, using the neutral hairline border since no dedicated input CSS was supplied. **nav-bar** reflects the light header scheme (#ffffff background, #161616 text/links) with a thin #949494/#dad8d2 border, consistent across the announcement-bar-plus-mega-menu structure implied by the navigation text. **product-card** is proposed for mask, pillow, and bundle tiles, using the light card surface (#f2f2f2) and hairline border to separate cards on a white or cream page background. **hero** is proposed as the cream (#f7f5f0) full-width banner style matching the scheme-2 tokens, appropriate for lifestyle/travel imagery framing. **footer** uses the dark scheme (#161616 background, white text) drawn directly from the scheme-3 tokens observed in the drawer/header variables. **badge** is a small pill using the accent red for "Bestseller"/"New" style labels implied by "Bestsellers" copy, though no literal badge markup was confirmed. **search** is a pill-shaped proposed field for the site's multiple "Search" entries in the nav text. **quiz-callout** is a category-specific component tailored to the repeated "Find Your Mask Quiz" CTA, using soft cream surfaces and the primary accent button to drive quiz engagement — a pattern common to sleep-accessory guided-selling flows.

## Responsive Behavior
Recommended, not measured, breakpoints: sm ≤480px (single-column stack, full-width buttons, collapsed hamburger nav), md 481–768px (two-column product grids, condensed nav links), lg 769–1024px (three-column grids, inline nav), xl ≥1025px (four-column grids, full mega-menu). Touch targets should be at least 44×44px for buttons and nav items; the mega-menu (Sleep Masks, White Noise, Earplugs, Bundles, Accessories) should collapse into an accordion drawer below md. This table is a proposed responsive strategy only; no live breakpoint, mobile menu, or JavaScript behavior was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variables, a text excerpt, and a partial color/font list — no rendered layout, spacing, real breakpoints, or interaction states (hover/focus/active/disabled) were directly observed. Role assignments (e.g., primary vs. accent, body vs. muted) are inferred from variable names such as `--header-color-button` and `--header-color-announcement`, not confirmed visual usage. Typography sizes, letter-spacing, and line-heights beyond the single button rule (13px/20px padding, 1.42 line-height) are proposed estimates, not measured values. Font availability, weights, and licensing for Poppins and Montserrat were not verified beyond their appearance in the `--font-stack` declarations. Component structures (product-card, hero, quiz-callout, etc.) are reasonable proposals for a sleep-mask/travel-pillow storefront but do not reflect confirmed DOM or visual QA. Mobile navigation, cart drawer, and search UI behavior were not observed and are extrapolated from menu-text content only.
