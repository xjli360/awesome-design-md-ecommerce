---
version: alpha
name: "Walnut Studiolo"
source_url: "https://walnutstudiolo.com"
captured_at: "2026-09-28T05:06:26.024601+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Walnut Studiolo's storefront CSS centers on a single dark olive-brown ink
  (#413500, also declared as --color-body-text and reused on outlined
  product-option pills) set against a plain white canvas (--color-body /
  --color-bg: #ffffff). Light neutral grays (#f1f1f1, #eeeeee) appear as
  sticky-header and secondary surface tones, while a warm gold (#f1bf3f)
  marks link hover states in the announcement bar. Third-party review-widget
  variables surface a muted blue (#6796b7) and a star-rating gold (#f1c712),
  and a soft red (#d54d4d) is used for price/total-add text, which this
  interpretation extends to sale badges. Roboto appears explicitly for the
  uppercase top-bar label; Avenir, Nunito Sans, and Open Sans are present in
  the font stack but their applied roles are not confirmed by the supplied
  rules, so headline/body assignments below are inferred pairings rather
  than observed facts. Border-radius values of 4px and 8px are directly
  observed (option pills, chat widget) and anchor the rounded scale. The
  resulting interpretation favors a restrained, workshop-craft tone: dark
  olive ink, unbleached white space, and a single warm accent, consistent
  with a small-batch leather goods maker.

colors:
  primary: "#413500"
  ink: "#413500"
  canvas: "#ffffff"
  body: "#413500"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f1f1f1"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-hover: "#f1bf3f"
  accent-alert: "#d54d4d"
  accent-info: "#6796b7"
  accent-star: "#f1c712"
  surface-dark: "#271d00"
typography:
  display-xl: {fontFamily: "Avenir Next, Avenir, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Avenir Next, Avenir, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px, textTransform: uppercase}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 1px, textTransform: uppercase}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    hoverColor: "{colors.accent-hover}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.accent-alert}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    linkHoverColor: "{colors.accent-hover}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-option-pill:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.sm}"

## Components

**button-primary** uses the observed dark-olive ink (#413500) as its fill, matching the `add-to-cart` and pill-selected backgrounds seen in the option CSS, with white text for contrast; hover/focus/disabled states are proposed, not observed.

**button-secondary** is an outline variant sharing the same olive border and text color, intended for lower-emphasis actions like "View Details"; its structure mirrors the observed 1px `#413500` borders on option pills but the outline-button application itself is inferred.

**text-input** is proposed using the neutral canvas background and a light hairline border; no explicit input-field CSS was supplied, so sizing and border color are inferred from the general neutral palette.

**nav-bar** reflects the directly observed top-bar rule: olive background, white link text, and gold (#f1bf3f) hover — this is one of the more strongly evidenced components, though only the bar itself (not a full primary nav) was captured.

**product-card** is proposed for the leather-goods catalog grid: a light gray surface card with a hairline border, product title in a mid-weight display font, and price shown in the observed alert-red (#d54d4d), reused from the `avp-productoption-totalpriceadd` rule.

**hero** proposes a plain white full-bleed section with large display type in ink color, appropriate to the brand's plain-materials, workshop-photography aesthetic; no hero markup or imagery CSS was supplied.

**footer** uses a darker, near-black brown (#271d00) as an inferred "deep wood" surface distinct from the lighter olive header, with white text and gold link hovers for consistency; footer layout itself was not observed.

**badge** (e.g., "Sale," "Made in Oregon") uses the alert-red fill with white caption text, sized for small inline labels; exact badge markup was not present in the supplied CSS.

**search** proposes the light gray sticky-header tone (#f1f1f1, observed on `.is-sticky .header`) as a search-field background, keeping it visually distinct from card surfaces.

**product-option-pill** is the most directly evidenced custom component: strap/size/finish selectors with a 1px `#413500` border, 4px radius, and 8px padding that invert to a solid olive fill with white text on hover/checked — taken essentially verbatim from the `.avp-option` pill CSS.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column stacking; nav collapses to a disclosure/menu button; touch targets ≥44px. |
| Tablet | 600–999px | Two-column product grid; sticky header condenses per observed `.is-sticky` background swap. |
| Desktop | 1000px+ | Multi-column grid; full horizontal nav bar visible. |

This table is a recommendation based on common patterns for Shopify-based storefronts, not measured breakpoints from the supplied evidence. Interactive/mobile menu behavior (e.g., the `.mobile-menu--opened` state) is referenced in CSS but its visual layout was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, spacing rhythm, or imagery was observed. Font-family roles (Avenir, Nunito Sans, Open Sans) are inferred pairings from the raw font-stack list — only Roboto's role (top-bar label) and the 14px size on `.avp-productdescfont` are directly evidenced. Custom font licensing and self-hosting availability were not verified. Several colors (muted, hairline, surface-card, surface-dark) are inferred semantic assignments from a broader observed palette rather than colors with confirmed roles in the source CSS. Component states such as hover, focus, disabled, and error are proposed, not confirmed via interaction testing. Spacing-scale values beyond the observed 8px padding are proposed conventions, not measured from the site.
