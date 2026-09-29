---
version: alpha
name: "Gunner"
source_url: "https://gunner.com"
captured_at: "2026-09-28T09:16:46.306636+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Gunner's public storefront reads as a rugged, utility-first outdoor brand
  layered over a clean e-commerce shell. The observed palette centers on a
  saturated safety-orange (#e9522e) used for hover states, active nav
  underlines, and CTA emphasis, paired with a cool slate ink (#4a4e58,
  #1e2939) for navigation text and body copy on a white canvas. A soft
  warm-tinted surface (#fef5f2) and light neutral grays (#f6f6f8, #e5e7eb)
  appear to support card and section backgrounds, though exact component
  usage is inferred rather than directly observed. An olive tone (#6a6a45)
  hints at camo/Mossy Oak product tie-ins but is not confirmed as a UI
  color. Typography draws from Avenir/Avenir Next for body and UI text,
  with the distinctive "Have Heart" family family reserved here for large
  display headlines, consistent with an outdoor-gear brand voice; licensing
  and actual weight availability are unverified. Layout tokens (--text-h0
  through --text-h6, --spacing-*, --container-gutter) confirm a fluid,
  breakpoint-responsive type and spacing system, but pixel-level component
  behavior is not measured from static CSS alone.

colors:
  primary: "#e9522e"
  ink: "#1e2939"
  canvas: "#ffffff"
  body: "#4a4e58"
  muted: "#8c94a1"
  hairline: "#e5e7eb"
  surface-soft: "#f6f6f8"
  surface-card: "#fef5f2"
  on-primary: "#ffffff"
  accent-olive: "#6a6a45"
  border-subtle: "#4a4e5880"
  surface-neutral: "#f0f0f0"
typography:
  display-xl: {fontFamily: "'Have Heart One', sans-serif", fontSize: 64px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Have Heart One', sans-serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Avenir Next', Avenir, sans-serif", fontSize: 26px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Avenir, 'Avenir Next', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Avenir, 'Avenir Next', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Avenir, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Avenir, 'Avenir Next', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.body}"
    border: "1px solid {colors.border-subtle}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
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
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  trust-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.lg}"

## Components

**button-primary** uses the observed safety-orange (#e9522e) as its resting or hover-emphasis fill, matching the header's `.primary_btn:hover` rule; proposed as the default add-to-cart/CTA treatment across the site.

**button-secondary** mirrors the observed `.primary_btn` default state (white background, slate text, semi-transparent border) seen in the header, repurposed here as a general outline button for secondary actions like "Shop All."

**text-input** is a proposed pattern for search fields, quantity selectors, and forms; border and radius are inferred defaults since no explicit input CSS was supplied.

**nav-bar** reflects the header's observed link coloring: muted slate text (#4a4e58) with an orange active/hover state and bottom border, as seen in `.header__wrapper li a:hover`.

**product-card** is inferred for kennel/bed/food-storage listings, using the light warm surface tint (#fef5f2) to differentiate cards from the pure-white canvas; no direct card CSS was observed, so structure is proposed.

**hero** is proposed for full-bleed campaign banners (e.g., "Flyway Series," "Long Haul Bed") using the darker ink tone as an overlay background so white display type remains legible over photography; not a measured layout.

**footer** uses the soft neutral background to separate it from body content, consistent with the light-gray tones present in the palette; content structure (columns, links) is proposed, not observed.

**badge** models the "5 Star Crash Tested" and promotional callouts using the primary orange as a pill, a proposed treatment since no badge-specific CSS was in evidence.

**search** is a proposed lightweight input variant for the header's "Open search" control; visual treatment unverified.

**trust-bar** addresses the category-relevant USP strip ("OVERBUILT IN THE USA™ / 30-Day Returns / Fast Shipping from Nashville") visible in page text; styled here as a dark, condensed-caption bar, proposed rather than measured.

## Responsive Behavior

Recommended (not measured) breakpoints, inferred from the presence of multiple `:root` token blocks scaling type and spacing:

| Breakpoint | Width      | Notes |
|---|---|---|
| Mobile | 0–639px | Single-column stacks, nav collapses to a hamburger/off-canvas menu, header logo shrinks (observed token shift from 155×38px to 130×32px). |
| Tablet | 640–1023px | Two-column product grids, header padding reduces per observed `--header-padding-block` variants. |
| Desktop | 1024–1439px | Three/four-column grids, full inline nav with underline hover states. |
| Wide | 1440px+ | Larger display type scale (`--text-h0` up to 5rem), increased section spacing (`--spacing-24`). |

Touch targets should be at least 44px in height for buttons and nav items on mobile. Navigation collapse, sticky header behavior (`--sticky-header-enabled:1` is present in CSS, confirming stickiness is configured but not confirming exact scroll behavior), and menu interaction patterns are proposed conventions, not verified from rendered/interactive testing.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variable declarations, a text excerpt, and a color/font inventory only; no rendered DOM, computed styles, or interaction states were observed. Semantic color roles (ink vs. body vs. muted, surface-card vs. surface-soft) are inferred from limited header-scoped selectors and may not match actual usage elsewhere on the site. Pixel sizes for the spacing scale and rounded-corner scale are proposed defaults, not extracted from the CSS custom properties (`--spacing-*` values themselves were not resolved to pixel numbers in the supplied evidence). The "Have Heart" display font family's availability, weights, and licensing are unverified; fallback to system sans-serif should be assumed until confirmed. Mobile menu behavior, hover/focus states beyond the header link and button rules shown, form validation styling, and product-card/hero layouts are not observed and are marked proposed throughout. Additional palette colors (e.g., #1990c6, #b1a688, #a55b3b) exist in the source data but were not confidently mapped to a role and were omitted to avoid speculative assignment.
