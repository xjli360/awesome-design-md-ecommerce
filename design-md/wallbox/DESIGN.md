---
version: alpha
name: "Wallbox"
source_url: "https://wallbox.com"
captured_at: "2026-09-28T09:26:10.513799+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wallbox's public site presents a technical, sustainability-oriented identity built on a dark neutral ink (#202124) against white canvas, with a saturated teal (#009b86) as the primary action color and a deeper teal (#085d52) for hover states, both drawn directly from observed button rules. Secondary and tertiary buttons rely on near-white and light-gray fills (#ffffff, #f0eeee) with dark borders, suggesting a restrained, engineering-catalog tone rather than a decorative consumer aesthetic. A soft teal tint (#ecf5f4) and a pale mint (#b4e5dd) appear in the palette without observed component usage; here they are inferred as background-card and badge/accent tints to extend the teal system for product cards and status chips. A red (#dd3b3b) is present in the palette and is inferred as a danger/alert color for form validation or fault states, though no such usage was captured. Neutral grays (#626467, #999999, #adadad, #d4d4d4, #e5e5e5) are inferred as muted text and hairline/border roles based on typical disabled-state patterns seen in the button CSS. The typeface HeyWallbox is a proprietary/custom family observed only by name; all sizing, weights, and additional colors (#2a394f, #1e1f22, #000000) are proposed interpretations layered onto this evidence, not measured page observations.

colors:
  primary: "#009b86"
  primary-hover: "#085d52"
  ink: "#202124"
  canvas: "#ffffff"
  body: "#202124"
  muted: "#626467"
  hairline: "#e5e5e5"
  surface-soft: "#f0eeee"
  surface-card: "#ecf5f4"
  on-primary: "#ffffff"
  danger: "#dd3b3b"
  accent-tint: "#b4e5dd"
  surface-dark: "#2a394f"
  border-strong: "#adadad"
  disabled-text: "#999999"
typography:
  display-xl: {fontFamily: "HeyWallbox, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "HeyWallbox, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "HeyWallbox, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "HeyWallbox, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "HeyWallbox, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "HeyWallbox, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "HeyWallbox, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    hover: {backgroundColor: "{colors.primary-hover}"}
    disabled: {backgroundColor: "{colors.hairline}", textColor: "{colors.disabled-text}", opacity: 0.6}
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-tertiary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focus: {border: "1px solid {colors.primary}"}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaSpacing: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-tint}"
    textColor: "{colors.primary-hover}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  charger-spec-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.title-md}"
    accentColor: "{colors.primary}"

## Components

**button-primary** is the sole interaction color directly observed in the CSS, using teal fill with a deeper teal hover; it should carry primary CTAs like "Get in charge" or "Buy now." **button-secondary** and **button-tertiary** are also observed, providing outlined and flat-gray alternatives for lower-emphasis actions such as "Learn more." **text-input** is proposed, inferring a hairline border and teal focus ring consistent with the button palette, used for country/language selection or contact forms. **nav-bar** is proposed as a white bar with a thin hairline bottom border, holding logo, product/solutions menus, and the country-selector link referenced in the page text. **product-card** is inferred to use the untested mint-tinted background (#ecf5f4) to visually group charger SKUs, with title and spec text in the observed ink color. **hero** is proposed as a full-width white section pairing a large display headline with the primary CTA button, matching the marketing copy's "cutting-edge EV charging solutions" framing. **footer** is inferred to use a dark navy surface (#2a394f, unobserved in components but present in palette) with white text for contrast, typical of global site footers though not confirmed here. **badge** is proposed as a pill using the pale mint accent tint to flag product attributes (e.g., "Smart," "Fast") echoing the marketing language. **search** is a proposed pill-shaped filter/finder field for locating chargers by country or power spec. **charger-spec-card**, the category-specific component, is proposed as a bordered panel highlighting technical specs (kW output, connector type) using the teal accent for numeric emphasis, appropriate for an EV hardware catalog though no such module was captured in the evidence.

## Responsive Behavior

Recommended, not measured: mobile (<600px) single-column stacking with nav collapsing to a hamburger menu; tablet (600–1024px) two-column product grids; desktop (≥1024px) three- to four-column grids with the nav bar fully expanded. Touch targets should be at least 44px tall, matching the padding scale of `button-primary`. Navigation and search are assumed to collapse into an overlay or drawer below 600px. All breakpoints and collapse behavior are proposed conventions, not confirmed via observed responsive CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, responsive breakpoints, animations, or interaction states (hover/focus beyond the two captured button rules, form validation, disabled inputs) were directly observed. Semantic role assignments for hairline, muted, surface-card, surface-dark, and accent-tint are inferred from typical UI patterns and palette proximity, not confirmed CSS selectors. All typography sizes, weights, and line-heights are proposed defaults since only the font-family and body color were captured; the HeyWallbox typeface's licensing, weight availability, and web-font delivery were not verified. Mobile/tablet layout, grid structure, and footer content are assumed conventions for an e-commerce hardware brand, not scraped evidence.
