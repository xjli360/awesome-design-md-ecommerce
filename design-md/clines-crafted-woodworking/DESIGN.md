---
version: alpha
name: "Clines Crafted Woodworking"
source_url: "https://clinescraftedwoodworking.com"
captured_at: "2026-09-28T10:23:50.922500+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from Shopify (Dawn-theme) CSS custom properties captured on the
  live storefront. The root palette defines `--color-foreground: 18,18,18` (#121212) against a
  white `--color-background`, with `--color-button` and `--color-link` both set to rgb(240,0,0),
  approximated here from the nearest observed hex, #ff0000, used as the primary action color.
  A secondary teal, #108474, appears in the Judge.me review-widget variables and is treated as an
  inferred accent for trust/social-proof elements (ratings, badges) rather than a core brand hue.
  Heading elements reference `--font-heading-family` and body text `--font-body-family`; the
  supplied font list includes Baskerville and Nunito Sans, which are mapped here as heading (serif,
  evoking traditional joinery and farmhouse craft) and body (humanist sans for readability) — this
  pairing is inferred from the font list, not confirmed by a rendered screenshot. Neutral grays
  (#333333, #666666, #dddddd, #f3f3f3) are reused for body copy, muted text, hairlines, and soft
  surfaces. Buttons appear square per `--jdgm-border-radius: 0` and Dawn's default outset radius
  variables, so the interpretation favors minimal rounding, consistent with a handcrafted,
  utilitarian furniture brand.

colors:
  primary: "#ff0000"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  badge-fg: "#121212"
  badge-bg: "#ffffff"
  badge-border: "#121212"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Baskerville, serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.5px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
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
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-fg}"
    borderColor: "{colors.badge-border}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  wood-species-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** uses the red rgb(240,0,0) value captured in `--color-button`/`--color-link`, rendered here as flat, square (unrounded) fills suited to calls-to-action like "SHOP NOW" and "Schedule Your Call Back." A hover/pressed state is proposed but not observed, likely a darkened or opacity-reduced variant.

**button-secondary** inverts the primary treatment — white fill, red text/border — for lower-emphasis actions such as "Continue shopping." Border and radius are proposed to match the primary button's square geometry for visual consistency.

**text-input** covers newsletter signup, search, and cart quantity fields. A light hairline border (#dddddd) on white is inferred from the neutral palette; focus-ring styling referenced by `--focused-base-outline` in the CSS suggests a foreground-tinted outline, proposed here as a subtle border-color shift rather than a measured value.

**nav-bar** reflects the header structure implied by the page text (Home, Build Your Dining Table, Rolling Pins, About, Blog, Contact, FAQ) sitting on a white background with dark-ink link text. Sticky/scroll behavior is not confirmed by static CSS and is marked proposed.

**product-card** models the repeating collection-grid items (e.g., "Farmhouse Dining Table," "Tapered French Rolling Pin") using the `.product-card-wrapper .card` custom-property scaffold observed in base.css, with a soft border and modest corner radius standing in for the theme's configurable `--product-card-corner-radius`.

**hero** represents the homepage banner ("Handmade Tables Made For Your Family") — a soft neutral background with a large serif headline and a primary-colored CTA. Overlay/scrim values are proposed for legibility over imagery, not confirmed from a rendered screenshot.

**footer** is inferred as a dark, ink-toned band (common in Dawn-theme builds) holding social links (Facebook, Pinterest, Instagram, YouTube), newsletter signup, and policy links; the specific footer background was not directly captured and is treated as a proposed inversion of the ink/canvas pair.

**badge** covers sale/sold-out labels seen in product listings (e.g., "Sale," "Sold out"), styled from the theme's `--color-badge-*` variables — white background, near-black text and border, unrounded per the Judge.me `--jdgm-border-radius: 0` convention echoed sitewide.

**search** is a proposed overlay/input pattern for the header "Search" affordance, sharing the text-input treatment on a slightly softened background to differentiate it from standard form fields.

**wood-species-selector** is a category-specific proposed component for choosing rolling-pin or table materials (Walnut, Maple, Cherry, Oak) referenced in the product copy — rendered as small bordered swatch/chip buttons that highlight with the primary red on selection, since no swatch markup or colors were captured in the evidence.

## Responsive Behavior
Recommended breakpoints (not measured from live rendering): mobile ≤599px, tablet 600–989px, desktop ≥990px, aligning with common Shopify Dawn-theme conventions implied by the theme's asset paths. Navigation is expected to collapse into a hamburger/drawer pattern below the tablet breakpoint, and the multi-item product grids ("View all," "1 / of 2," "1 / of 6") likely reflow from 3–4 columns on desktop to 1–2 on mobile with horizontal-scroll or stacked carousels. Touch targets for buttons and swatch selectors should maintain a minimum 44×44px hit area. This section is a design recommendation only; no interaction, resize, or mobile-viewport behavior was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS custom properties, a text excerpt, and a color/font list — no rendered screenshots, computed layouts, or DOM structure were available. The mapping of `rgb(240,0,0)` to the listed hex `#ff0000` is an approximation, not an exact match found in the supplied palette. Semantic assignment of body/muted/hairline/surface grays (#333333, #666666, #dddddd, #f3f3f3) is inferred from typical usage patterns, not confirmed CSS selectors tying them to those exact roles. Font pairing (Baskerville for headings, Nunito Sans for body) is inferred from the presence of both names in the font-family list, not from resolved `--font-heading-family`/`--font-body-family` values. All pixel sizes in typography tokens beyond the observed `1.5rem` body base are proposed. Component states (hover, focus, disabled, active) and mobile navigation/drawer behavior are proposed, not observed. Custom font licensing/self-hosting and actual availability of Baskerville/Nunito Sans on the live site were not verified.
