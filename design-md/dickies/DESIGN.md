---
version: alpha
name: "Dickies"
source_url: "https://dickies.com"
captured_at: "2026-09-28T04:52:04.991588+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Dickies' Shopify-hosted CSS custom properties rather than live visual review. The root theme defines an explicit "brand" border color of #622714, a deep rust-brown, which is treated here as the primary brand color since no other hex is labeled as brand in the evidence. Neutral scaffolding is built from near-black (#111111, #000000) text tones, mid-grays (#848484, #757575, #6d6d6d) for secondary text and borders, and light grays (#f2f2f2, #f9f9f9, #c9c9c9) for surfaces and hairlines — consistent with a utilitarian, high-contrast workwear catalog rather than a decorative retail site. A Shopify-default interactive blue (#1990c6, hover #136f99) appears in accelerated-checkout button CSS and is mapped here as a functional accent for payment/interactive affordances, distinct from the brand primary. Status colors (#d92d20 error, #f79009 warning, #12b76a success) come from what reads as a standard design-token error/warning/success triad. Typography is anchored to the site's own custom properties: IBM Plex Sans for display, heading, subheading, and body; IBM Plex Mono reserved for accent/mono use. Corner radii are nearly square (0–2px), reflecting a squared-off, functional workwear aesthetic; larger radii and spacing values are proposed extrapolations, not observed.

colors:
  primary: "#622714"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6d6d6d"
  hairline: "#c9c9c9"
  surface-soft: "#f2f2f2"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  border-dark: "#3a1a1a"
  interactive: "#1990c6"
  interactive-hover: "#136f99"
  success: "#12b76a"
  error: "#d92d20"
  warning: "#f79009"
  navy-accent: "#204387"
typography:
  display-xl: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: "65px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "0px"}
  display-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: "46px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: "30px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "'IBM Plex Mono', monospace", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.3px"}
  button-md: {fontFamily: "'IBM Plex Sans', sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.border-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary** uses the observed `--border-color-brand` rust-brown (#622714) as its fill, mapped here as the site's primary action color; hover/active state variables exist in the CSS (`--btn-primary-bg-color-hover`) but their resolved hex is not present in evidence, so hover treatment is proposed as a darkened variant.

**button-secondary** is an outline variant proposed for lower-emphasis actions (e.g., "Shop All," filter toggles), reusing the primary brown for border and label text on a white fill — not directly observed, but consistent with the squared, low-radius button geometry seen in `.button`.

**text-input** is proposed for search and form fields, using the light hairline gray (#c9c9c9) border and near-square 2px radius consistent with `--border-radius-50`.

**nav-bar** reflects the multi-level mega-menu structure evident in the page text (Men/Women/Scrubs/Off The Clock with dense subcategories), styled with a white background and hairline-gray dividers; actual sticky/scroll behavior is not observed.

**product-card** is inferred from typical Shopify PDP/PLP grid patterns and the `--product-image-ratio: 1` token, implying square product imagery; card surface uses the near-white `#f9f9f9` tone for subtle separation from pure white canvas.

**hero** is proposed using the large display type scale (65px/75px) actually defined in root CSS, on a dark ink background for high-contrast campaign banners; exact hero copy/imagery treatment is not observed.

**footer** is proposed dark to match common utility-brand footer conventions and to contrast the light body; the deep brown-black `#3a1a1a` (`--border-color-dark`) is used as a footer hairline divider.

**badge** uses the observed status-red (#d92d20) for sale/clearance flagging, drawing on the evidenced error-token family; success/warning tokens are available for stock or promo badges but their live use is not confirmed.

**search** reuses the light-gray surface token for the predictive search panel implied by "Popular Searches / Recent Searches / View All Results" in the extracted page text.

**size-selector** is a category-appropriate addition for a workwear retailer with extensive Big & Tall, Plus, and standard sizing across pants/shirts/coveralls; swatch-style selectable chips with a brand-brown selected border are proposed, not observed.

## Responsive Behavior

Proposed breakpoints (not measured):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | single-column nav collapses to hamburger + slide-out mega-menu |
| tablet | 600–1023px | 2-column product grid, condensed nav |
| desktop | 1024–1439px | full mega-menu, 3–4 column product grid |
| wide | 1440px+ | max-width content container, 4+ column grid |

Touch targets should meet a 44px minimum height, aligning with the observed `--shopify-accelerated-checkout-button-block-size` default of 44px clamped between 25–55px. Mega-menu categories (Men/Women/Scrubs) should collapse to accordions below tablet width. This table is a design recommendation only; no live responsive layout was captured.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built entirely from static CSS custom properties and a page-text excerpt, not from rendered/visual inspection, so no layout, spacing rhythm, hover/focus states, or actual mobile behavior were observed. The primary brand color is inferred from a single `--border-color-brand` token; it is not confirmed as the literal button/link brand color since `--btn-primary-bg-color` itself resolves to a CSS variable with no captured hex value. Spacing scale values are entirely proposed, since only variable names (e.g., `--spacing-400`, `--spacing-700`) appear without resolved pixel values. Rounded `sm`/`md`/`lg` values beyond the observed 2px/100% are proposed extrapolations. IBM Plex Mono's applied role is inferred as caption/accent only; Bureau Grot Cond and Bureau Grot Medium appear in the site's font list but have no CSS rule tying them to a specific selector, so they are omitted from the typographic scale pending further evidence. Font licensing/self-hosting status for IBM Plex and Bureau Grot was not verified. Interaction states (focus rings, disabled styling, cart/checkout flows) beyond the two captured Shopify payment-button rules are not observed.
