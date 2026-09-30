---
version: alpha
name: "Raaka"
source_url: "https://raakachocolate.com"
captured_at: "2026-09-28T09:45:00.353891+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Raaka's evidence points to a bean-to-bar chocolate maker whose site pairs a deep cacao-brown
  (#351503) with near-black ink (#171c23) against warm off-white canvases (#fbfbf5, #f0f0e6).
  This brown appears repeatedly as the border/outline color on primary buttons and review
  widgets, so it is treated here as the primary brand color rather than a decorative accent.
  A warm gold (#e6bb68) and an orange (#f47532) surface as secondary call-to-action colors on
  buttons, consistent with a food brand's seasonal/limited-batch merchandising. Additional
  warm browns, terracotta, blush, and rust tones in the palette are inferred to support
  flavor-variant badges and imagery accents (e.g. seasonal collections), since their exact
  usage context wasn't captured. Two font families are observed directly in the CSS: "Alku"
  and "Sul Sans," alongside "Origin Super Condensed." Alku is interpreted as a display/serif
  headline face (its name and pairing suggest editorial character), Sul Sans as the workhorse
  body/UI sans, and Origin Super Condensed as a compressed label/eyebrow face — all inferred
  role assignments, not confirmed by usage selectors. Observed button CSS (2px border,
  uppercase, 900 weight, 2px letter-spacing, square corners) strongly shapes the button
  component below. Layout, breakpoints, and hover states are proposed conventions, not
  measured from a live render.

colors:
  primary: "#351503"
  ink: "#171c23"
  canvas: "#fbfbf5"
  body: "#171c23"
  muted: "#62666c"
  hairline: "#dddddd"
  surface-soft: "#f0f0e6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#e6bb68"
  accent-orange: "#f47532"
  accent-brown-soft: "#6a4e43"
  accent-terracotta: "#c88576"
  accent-blush: "#f7a5b6"
  accent-rust: "#9c3437"
  slate: "#676986"
typography:
  display-xl: {fontFamily: "Alku, serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Alku, serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "Origin Super Condensed, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 1px}
  body-md: {fontFamily: "Sul Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Sul Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Sul Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Sul Sans, sans-serif", fontSize: 16px, fontWeight: 900, lineHeight: 1.2, letterSpacing: 2px}
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
    padding: "{spacing.lg} {spacing.xl}"
    border: "2px solid {colors.primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.xl}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
  subscription-panel:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-orange}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.xl}"
    rounded: "{rounded.sm}"

## Components

**button-primary** reflects observed CSS most directly: a 2px solid border in the primary
brown, 900-weight uppercase label text with 2px letter-spacing, and square (non-rounded)
corners, matching `.button__primary` rules in base.css. An offset-border hover/active effect
(via `::before` pseudo-elements) was present in the CSS but its exact visual timing is
proposed as a general interaction pattern, not confirmed by rendering.

**button-secondary** is a proposed outline variant using the same border and typography as
primary but with a transparent fill, intended for lower-emphasis actions (e.g. "Learn More")
seen in the page copy.

**text-input** is inferred from generic Shopify base-CSS resets (`font-family:inherit` on
form elements) with a conservative hairline border and canvas-card background; no unique
input styling was captured in evidence.

**nav-bar** is proposed based on the multi-level category copy (Shop, Discover, Visit) found
in page text; a light canvas background with a hairline bottom border keeps it visually quiet
against product imagery.

**product-card** anticipates the dense bar/mini/gift grid implied by the best-seller listing
in page text, using a card surface, hairline border, and condensed title styling to fit many
SKUs per row.

**hero** is proposed for the seasonal banner content ("Pumpkin Crunch," "Date-sweetened
minis") using the display-xl headline face against a soft warm surface, with a primary CTA
button.

**footer** uses the primary brown as a dark closing band with white text, a common DTC
pattern; this color/role pairing is inferred, not measured on the live footer.

**badge** supports short labels like "Organic," "Vegan," or "Limited Batch" referenced
repeatedly in the source copy, using the gold accent for warmth without competing with the
primary CTA color.

**subscription-panel** is a category-specific component for the "Monthly Chocolate
Subscription" callout, using the orange accent (matching the observed `.button__primary.orange`
variant) to differentiate it from standard product CTAs.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|---|---|---|
| Mobile | < 640px | Single-column stacks; nav collapses to a hamburger/drawer; hero CTA full-width. |
| Tablet | 640–1024px | 2-column product grids; nav remains condensed. |
| Desktop | > 1024px | 3–4 column product grids; full horizontal nav. |

Touch targets should be a minimum of 44px in height, particularly for `button-primary` given
its padding is already generous (~20–32px). Navigation should collapse to a drawer/menu below
tablet width. This table is a general recommendation based on typical ecommerce patterns, not
measured breakpoints from the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only; no live rendering,
computed styles, or DOM screenshots were available. Semantic color roles (primary vs. accent,
footer background, badge background) are inferred from limited selector context (mostly
button and third-party review-widget CSS) and may not match actual brand usage elsewhere on
the site. Typography sizes beyond the observed `button-md` values (16px/900/2px
letter-spacing) are proposed, not measured. Component layouts (nav-bar, product-card, hero,
footer, search) are conventional ecommerce patterns inferred from page copy, not observed
markup or layout. Interaction states (hover, focus, active) beyond the button's documented
`::before` border-offset trick are proposed conventions. Mobile/responsive layout was not
observed in any evidence. Availability, licensing, and web-font loading for "Alku," "Sul
Sans," and "Origin Super Condensed" were not verified.
