---
version: alpha
name: "Lesser Evil"
source_url: "https://lesserevil.com"
captured_at: "2026-09-28T04:31:05.013372+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  LesserEvil's public CSS surfaces a deep navy pair (#001824, #002a3a) used as the review-widget's
  primary button and border color, against warm cream neutrals (#fbf6ee, #f6efe5, #faf5ed, #f0e6d8)
  that read as a snack-food pantry palette rather than a stark white system. A cluster of saturated
  accents — pink #f57eb6, orange #ff6a39, gold #f0b323, teal #3bbfad, purple #c98bdb, plus signal
  colors #e40014 (red), #00a544 (green), #00a3e0 (blue) — appear alongside a Shopify accelerated-
  checkout blue (#1990c6 / hover #136f99). These are treated here as an inferred flavor/variant-tag
  system, since no selector ties them to specific product lines. Typography is limited to two named
  families, "Good Sans" and "canada-type-gibson", both falling back to sans-serif; we assign Good
  Sans to display/heading roles and canada-type-gibson to body copy as an inferred pairing, since no
  rule confirms which carries headlines. The review widget's 35px button radius and 700-weight,
  14–15px button/body text are the only concretely observed typographic and shape values; all other
  sizes, weights, and letter-spacing are proposed extrapolations sized for a warm, snack-brand DTC
  storefront. Component definitions below extend this evidence into a cohesive, restrained system.

colors:
  primary: "#001824"
  ink: "#002a3a"
  canvas: "#ffffff"
  body: "#335561"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f6efe5"
  surface-card: "#fbf6ee"
  on-primary: "#ffffff"
  accent-pink: "#f57eb6"
  accent-orange: "#ff6a39"
  accent-gold: "#f0b323"
  accent-teal: "#3bbfad"
  accent-purple: "#c98bdb"
  signal-red: "#e40014"
  signal-green: "#00a544"
  signal-blue: "#00a3e0"
  link-blue: "#1990c6"
  link-blue-hover: "#136f99"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "Good Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Good Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Good Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "canada-type-gibson, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Good Sans, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-tag:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components
**button-primary** uses the dark navy (#001824) and white text combination that is directly observed
as the okeReviews `--oke-button-*` custom properties, including its 700 weight and pill-like 35px
radius, generalized here to the site's full-width `{rounded.full}` token; hover/active state colors
are proposed to shift toward `{colors.link-blue-hover}`-style darkening but no hover token was
captured outside the review widget.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More"),
reusing the primary ink color for border and text with a transparent fill, consistent with the
single dark accent observed in the review-widget button tokens.

**text-input** is proposed for newsletter and search fields; it borrows the neutral `#dedede`
hairline (seen as the Shopify skeleton-loader background) as a plausible border color and keeps
corners minimal (`{rounded.sm}`) to contrast with the pill-shaped buttons.

**nav-bar** is an inferred header treatment on white canvas with ink-colored wordmark/links; no
selector evidence describes site chrome, so height, sticky behavior, and link states are proposed.

**product-card** proposes the warm cream `#fbf6ee` surface (present in the palette but not tied to a
selector) as a card background to differentiate snack-photography tiles from the white page canvas,
with a soft hairline border and medium radius for a friendly, food-brand feel.

**hero** is a proposed full-bleed section using the softer cream `#f6efe5` tone, intended for a
lifestyle/product photography banner with large display type; no hero markup was present in the
supplied evidence.

**footer** reuses the observed dark navy as an inverted-color band, consistent with how the same
color anchors the primary button, giving the footer visual weight as a closing brand element.

**badge** and **flavor-tag** are proposed small components for callouts like "Vegan," "Keto," or
flavor variants, drawing on the brand's brighter accent hues (gold, teal) which appear in the palette
but whose actual product-tagging usage was not observed in the supplied CSS.

**search** is a proposed pill-shaped input pattern matching the button radius language, for product
or FAQ search; no search markup was present in evidence.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <768px | Single-column product grid; nav collapses to a hamburger/drawer pattern |
| tablet | 768–1023px | 2-column product grid; nav shows condensed inline links |
| desktop | 1024–1279px | 3–4 column product grid; full nav bar |
| wide | ≥1280px | Max-width content container; hero imagery scales up |

Touch targets should be a minimum of 44×44px, matching the `clamp(25px, …, 55px)` range observed in
the Shopify accelerated-checkout button CSS. Primary navigation and filter controls are recommended
to collapse into an overlay/drawer below the tablet breakpoint; no such collapse behavior was
actually observed in the supplied static CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/JSON evidence (Shopify theme assets, an Okendo
reviews widget, and a checkout wallet stylesheet); no rendered page layout, component hierarchy, or
responsive breakpoints were directly observed. Color-to-role mappings (e.g., cream surfaces, accent
hues as flavor tags) are inferred from palette presence, not confirmed selector usage on marketing
pages. Most typography sizes, weights, and letter-spacing beyond the review widget's 14–15px/700
values are proposed placeholders. Interaction states (hover, focus, active) outside the Okendo button
tokens and the Shopify payment button are not observed. Mobile/responsive layout, navigation
collapse, and grid behavior are recommendations only. "Good Sans" and "canada-type-gibson" are
referenced by name in the CSS, but licensing, hosting, and availability for production use were not
verified.
