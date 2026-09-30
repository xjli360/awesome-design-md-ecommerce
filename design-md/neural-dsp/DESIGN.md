---
version: alpha
name: "Neural DSP"
source_url: "https://www.neuraldsp.com"
captured_at: "2026-09-28T04:42:17.291860+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Neural DSP's storefront presents a dark, studio-like surface built almost entirely from near-black tones (#121212, #101010, #0a0a0a, #161616, #1a1a1a, #1e1e1e) layered to separate hero, card, and section depth, with white and light-gray text (#ffffff, #dddddd) carrying body copy. The observed palette also contains a distinct set of saturated accents — green (#45f862), yellow (#ffd236), red (#ff2727/#f00a05), orange (#ff7000), and two blues (#3500f1, #1a3af8) plus an explicit swiper-theme blue (#007aff) tied to carousel controls in the stylesheet. These saturated hues most plausibly serve as status/badge accents (e.g. "bestseller," "compatible," "desktop only" tags visible in the page copy) rather than a single brand color; this mapping is inferred, not confirmed. This interpretation elects the green as the primary interactive accent for buttons and highlights, since it reads as the most CTA-appropriate hue against the dark canvas, while treating the swiper blue as a secondary/interactive-control accent. Typography is IBM Plex Sans (with monospace as a technical/spec fallback); all sizes below are proposed, as no computed type scale was captured. Layout, spacing, and component states are inferred design proposals appropriate to a plugin/hardware storefront, not measured observations.

colors:
  primary: "#45f862"
  ink: "#ffffff"
  canvas: "#121212"
  body: "#dddddd"
  muted: "#959595"
  hairline: "#373737"
  surface-soft: "#1a1a1a"
  surface-card: "#1e1e1e"
  on-primary: "#121212"
  accent-blue: "#007aff"
  accent-violet: "#3500f1"
  accent-yellow: "#ffd236"
  accent-red: "#ff2727"
  accent-orange: "#ff7000"
  border-strong: "#454545"
  surface-alt: "#f4f4f4"
typography:
  display-xl: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "IBM Plex Sans, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
  mono-spec: {fontFamily: "monospace", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    hairline: "{colors.hairline}"
---

## Components

**button-primary** is proposed for "Add to cart," "Buy now," and "Free trial" actions seen in the page text. The green fill is an inferred brand-CTA choice against the dark canvas, with a dark on-primary label for contrast; hover/active/disabled states are not observed and should be treated as proposed (e.g., a slightly desaturated fill on hover).

**button-secondary** covers lower-emphasis actions like "Learn more" and "Find a dealer," using an outlined style against the dark surface so it doesn't compete with primary CTAs. Border and text colors reuse the neutral palette rather than introducing new hues.

**text-input** models account/login and newsletter fields implied by an e-commerce flow with cart and checkout language ("VAT included," "taxes calculated at checkout"). No form markup was present in the evidence, so field states (focus, error) are proposed only.

**nav-bar** represents the top-level "Plugins / Hardware / intl" navigation referenced in the page text, using the darkest canvas tone with hairline separation from content below it. Sticky behavior and active-link styling are not confirmed by the evidence.

**product-card** is the repeating unit for each Archetype/plugin listing (image, title, tagline, price, badge, CTA row) implied by the repeated bestseller/compatible product blocks in the text excerpt. Card elevation is expressed only through a slightly lighter surface tone, since no shadow values were captured.

**hero** covers the top marketing banner (e.g., "CorOS 4.1.0," "Darkglass Ultimate," "Archetype: John Mayer X") using the largest display type on the dark canvas; carousel/slider mechanics are inferred from the swiper-related CSS variable but specific transition/animation behavior was not observed.

**footer** is proposed as a muted, secondary-tone band for legal, dealer, and support links, consistent with the darker neutral end of the palette.

**badge** models the small status labels seen throughout the copy — "bestseller," "COMPATIBLE," "DESKTOP ONLY," and award callouts like "Editor's Pick." Colors are drawn from the accent set (yellow shown; red, orange, and blue are viable alternates per status) since no single mapping between label text and color was confirmed in the evidence.

**search** is a proposed pill-shaped input for product/plugin discovery, styled consistently with text-input but rounded fully to suggest a lighter-weight, header-embedded control.

**spec-panel** is a category-specific component for hardware/amp-modeler technical specs (e.g., Quad Cortex, Nano Cortex feature lists), using the monospace fallback font to visually differentiate tabular/technical content from marketing prose, echoing the swiper/monospace font entries in the supplied evidence.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| mobile | <480px | Single-column stack; nav collapses to a hamburger/menu drawer; product cards full-width |
| tablet | 480–1024px | 2-column product grids; hero type scales down one step |
| desktop | 1024–1440px | 3–4 column product/plugin grids; full nav bar visible |
| wide | >1440px | Max content width with additional side padding; hero imagery may scale further |

Touch targets should be at least 44×44px for buttons and nav items; badges and inline tags can remain smaller since they are non-interactive. Primary/secondary buttons should stack full-width below tablet width.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed styles, or interaction states (hover, focus, active, loading, error) were observed. The semantic mapping of the primary brand accent to green (#45f862) versus the alternate blues (#007aff, #3500f1, #1a3af8) is an inferred judgment call, not a confirmed brand-color designation — the source only confirms #007aff as an explicit swiper/carousel theme variable. Badge-to-color pairing (yellow/red/orange/blue for bestseller/compatible/desktop-only/etc.) is likewise inferred, not evidenced by a direct selector-to-label match. All numeric type scale values, spacing, and radius tokens are proposed conventions, not measured from the site's computed styles. Mobile/responsive layout, breakpoints, and grid behavior were not observed and are offered only as reasonable defaults. Font availability, licensing terms, and full weight range for IBM Plex Sans were not verified against the live site or a font-serving license.
