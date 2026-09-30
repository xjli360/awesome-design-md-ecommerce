---
version: alpha
name: "Tortuga"
source_url: "https://tortugabackpacks.com"
captured_at: "2026-09-28T10:07:51.398112+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Tortuga's evidence shows a restrained, editorial travel-gear palette anchored by a deep forest green (#01462b), confirmed as the brand's primary color through the Judge.me review-widget variables (--jdgm-primary-color, --jdgm-star-color, --jdgm-write-review-bg-color), all pointing to the same hex. Near-black (#1d2226) and true black (#000000) supply ink and high-contrast UI states, while a wide bank of near-white grays (#fcfcfc, #f7f7f7, #f8f7f6, #f4f4f4) suggests layered card and section surfaces rather than a single flat background. Hairline grays (#dddddd, #cccccc, #d9d9d9) imply subtle borders typical of a minimal e-commerce theme. A small set of warm/earth accents — brown (#79341b), gold (#e1c16e), red (#b32428), teal (#108474), and a high-visibility lime (#cdff00) — appear positioned for badges, sale flags, and "New" tags; their exact usage is inferred, not confirmed in layout. Typography draws on "Owners" (a licensed display family) for headings and "Nunito Sans" for body/UI text, with Arial/Helvetica/sans-serif as fallbacks; JudgemeIcons/JudgemeStar are third-party icon fonts, not brand type. Border-radius evidence (--jdgm-border-radius: 0) points to a squared, low-ornament aesthetic. This interpretation proposes a functional, trust-forward outdoor/travel UI built around that green, generous whitespace, and clear product/quiz-driven navigation.

colors:
  primary: "#01462b"
  ink: "#1d2226"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent-gold: "#e1c16e"
  accent-brown: "#79341b"
  accent-teal: "#108474"
  accent-lime: "#cdff00"
  sale-red: "#b32428"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "'Owners', sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Owners', sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'OwnersNarrow', 'Owners', sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "80px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    saleColor: "{colors.sale-red}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fit-quiz-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaComponent: "button-primary"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the forest-green (#01462b) call-to-action, matching the confirmed Judge.me primary/write-review button color; white text sits on top for contrast. Hover/active states are proposed, not observed.

**button-secondary** is an outlined variant using the same green on a transparent field, intended for tertiary actions like "Read Tortuga's Story" alongside a primary "Shop" CTA; this pairing is inferred from page copy, not measured CSS.

**text-input** proposes a plain white field with a light hairline border and sharp corners, consistent with the zero-radius signal from `--jdgm-border-radius: 0`. Focus-ring color would draw on the CSS `--accent` outline variable observed in the theme stylesheet, though its resolved value was not supplied.

**nav-bar** reflects the measured `--HEADER-HEIGHT: 80px` (76px medium, 54px mobile) and logo width tokens (200px desktop / 120px mobile) found in the CSS, giving a real structural anchor for the header component even though its color usage is inferred from the general canvas/ink pairing.

**product-card** is modeled on the "Shop Best Sellers" grid (Pro Backpack 40L, Expandable Backpack, Daily Carry Pro) referenced in page text, using a soft card surface, hairline border, and a sale-red price treatment for discounted items like the "$41 off" packing cubes.

**hero** proposes a light, full-width banner using large display type for messaging such as "Travel Light in Comfort," paired with a primary button; layout proportions are not measured and are treated as a standard e-commerce hero pattern.

**footer** uses an inverted ink background with white text, referencing the newsletter, policy links (Shipping, Returns, Warranty, FAQs), and social icons found in the page text; this dark-footer treatment is a proposed convention, not confirmed styling.

**badge** applies the high-visibility lime accent (#cdff00) for tags like "Best Seller," "New," or "Final Sale," rounded as a pill; color role is inferred from the color's outlier saturation relative to the rest of the muted palette.

**search** models the site's persistent search/clear affordance noted repeatedly in page text, using a soft surface and muted placeholder text; no interaction states were observed.

**fit-quiz-card** is a category-appropriate component representing Tortuga's "Take the Quiz" / Bag Finder feature, a recurring, prominent CTA throughout the page text; it uses the primary green as an accent stripe or icon color with a card layout to visually differentiate it from standard product cards.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | <768px | Single-column product grid; header height 54px (CSS-confirmed); nav collapses to menu icon (proposed). |
| Tablet | 768–1024px | Two-column product grid; header height 76px (CSS-confirmed medium value). |
| Desktop | >1024px | Multi-column grid; header height 80px (CSS-confirmed); logo at 200px width. |

Touch targets should be at least 44×44px for buttons and quiz CTAs (proposed, not verified). Navigation collapse behavior, menu animation, and mobile card stacking were not observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS variables, page text, and a supplied color/font list only; no live rendering, computed layout, or interaction states were captured. Semantic color roles (surface-soft vs. surface-card, badge vs. accent assignments) are inferred from typical e-commerce patterns and the palette's relative saturation/lightness, not from confirmed component usage. Typography sizes beyond generic fallbacks are proposed estimates, since no explicit font-size declarations for headings or body text were included in the evidence. The licensing and technical availability of the "Owners"/"OwnersNarrow"/"OwnersWide" font family were not verified. Border-radius values follow a standard proposed scale, tempered by the single confirmed zero-radius signal from the Judge.me widget variable; actual card/button corner rendering was not observed. Mobile menu behavior, hover/focus states beyond the generic `--accent` outline rule, and real breakpoint values were not measured and are marked as recommendations only.
