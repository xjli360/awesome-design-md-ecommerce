---
version: alpha
name: "Maker Wine"
source_url: "https://makerwine.com"
captured_at: "2026-09-28T10:06:11.758885+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Maker Wine's observed palette centers on a deep navy-blue pair (#193f61, #0c3254) with a
  supporting mid-blue (#2a679e), set against warm off-white canvases (#fffcfa, #fff8f3) rather
  than pure white. A coral-red accent pair (#f05c5c, #d35252) and a handful of soft pastel
  tints (peach #ffebde, sky #e4f5ff, green #d9ead3) appear in the CSS and are inferred here as
  category or seasonal-pack accent backgrounds, consistent with the site's rotating "packs"
  merchandising. Body copy is inferred to run in dark charcoal (#333333) and muted grey
  (#5f626c), with near-black (#11172b, #060606) reserved for high-contrast headline or footer
  treatment. Two typefaces are declared: Blacker Pro, a serif likely used for display headlines
  to signal craft/heritage positioning, and FF DIN Pro, a condensed-leaning sans used for UI,
  navigation, and body text; Georgia and Arial/system-ui serve as fallbacks. The interpretation
  below proposes a warm, editorial-leaning DTC layout: a serif-led hero over tinted content
  bands, sans-serif utility chrome (nav, cart, buttons), and rounded pill/card surfaces echoing
  the carousel dot geometry (border-radius: 50%) observed in the supplied CSS. All color and
  font choices below reuse only the supplied evidence; semantic roles (primary vs. accent vs.
  tint) are inferred, not confirmed from live rendering.

colors:
  primary: "#193f61"
  primary-deep: "#0c3254"
  secondary: "#2a679e"
  accent: "#f05c5c"
  accent-deep: "#d35252"
  ink: "#11172b"
  body: "#333333"
  muted: "#5f626c"
  canvas: "#fffcfa"
  surface-soft: "#fff8f3"
  surface-card: "#f6f6f5"
  surface-alt: "#f0f0f1"
  hairline: "#dcd9d8"
  border: "#d0d3d8"
  tint-peach: "#ffebde"
  tint-sky: "#e4f5ff"
  tint-green: "#d9ead3"
  sale: "#dd0000"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "'Blacker Pro', Georgia, serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Blacker Pro', Georgia, serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'FF DIN Pro', Arial, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'FF DIN Pro', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'FF DIN Pro', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'FF DIN Pro', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'FF DIN Pro', Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  maker-story-card:
    backgroundColor: "{colors.tint-peach}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the deep navy (`{colors.primary}`) sourced from the observed
`.slick-active` dot color, proposed here as the brand's primary interactive color for
add-to-cart and CTA actions; hover/focus states are not observed and are proposed as a
darkening to `primary-deep`.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g. "Read their
story" links), reusing the primary navy for border and text on a transparent background;
this pairing is inferred, not measured.

**text-input** is a minimal bordered field for email capture (club sign-up, newsletter),
using the warm canvas background and neutral border-gray; no focus-ring color was observed,
so none is specified.

**nav-bar** is proposed as a light, canvas-toned bar with a thin hairline divider, matching
the site's stated multi-item navigation (Home, Shop, Join Club, Gifts, Reviews, About) and
sub-navigation dropdown behavior described in the page text; dropdown open/close styling is
not observed.

**product-card** represents a can/pack listing tile on a soft neutral surface
(`{colors.surface-card}`) with generous internal padding, intended for the "Best Sellers" and
mixed-pack grid content referenced in the source text.

**hero** proposes a warm-tinted full-width band using `surface-soft`, pairing the serif
display type for headline copy ("Premium wine any damn time") with sans body copy for
supporting text and CTA buttons.

**footer** is proposed in the darkest observed ink tone for contrast, carrying legal links,
social, and secondary navigation; this treatment is inferred from common DTC patterns, not
confirmed by supplied CSS.

**badge** uses the coral accent for short labels such as "Best Seller" or "New Pack," in a
pill shape consistent with the rounded, dot-like geometry seen in the carousel CSS.

**search** is a rounded, pill-shaped affordance for future product/site search; no search UI
was present in the supplied evidence, so this is fully proposed.

**maker-story-card** is a category-specific component for the "Meet Our Makers" carousel,
using a peach tint background to visually separate winemaker bios from standard product
cards, reflecting the page's emphasis on individual producer storytelling.

## Responsive Behavior
This is a proposed recommendation only; no live breakpoint or mobile behavior was observed.

| Breakpoint | Width         | Layout guidance                                   |
|-----------|---------------|----------------------------------------------------|
| mobile    | < 480px       | Single-column stack; nav collapses to hamburger    |
| tablet    | 480–1024px    | 2-column product/story grids; nav remains condensed |
| desktop   | > 1024px      | 3–4 column grids; full horizontal nav with dropdown |

Touch targets should be at least 44×44px for buttons and carousel dots (the observed dot
button is 24×28px and should be enlarged for touch accessibility). Sub-navigation ("About"
with 4 items) should collapse into an accordion on mobile rather than a hover dropdown.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed
styles, or interaction states were observed. Semantic color roles (primary vs. accent vs.
tint) are inferred from limited usage context (e.g., one carousel dot rule) and may not
reflect actual brand usage elsewhere on the site. All typographic sizes, weights, and
letter-spacing values are proposed defaults, not measured from live CSS, aside from the
confirmed font-family names (Blacker Pro, FF DIN Pro, Georgia, Arial). Hover, focus, active,
and error states for all components are proposed, not verified. Mobile/responsive layout
behavior is not observed and is a recommendation only. Availability, licensing, and web-font
loading of Blacker Pro and FF DIN Pro were not verified from the supplied evidence.
