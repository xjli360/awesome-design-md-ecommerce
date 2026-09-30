---
version: alpha
name: "Tea Collection"
source_url: "https://teacollection.com"
captured_at: "2026-09-28T09:39:00.275892+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Tea Collection's observed CSS points to a warm, editorial identity built around a
  deep espresso-brown ink (#3e1a04, mapped to --color-tea-brown) used for both body
  copy and headings against a white or cream canvas. A muted teal (#108474) appears
  as the review-widget primary color and is proposed here as the site's functional
  accent for links, focus states, and secondary CTAs, since no other single accent
  recurs as consistently in the supplied variables. Neutral warm creams (#f6f3eb,
  #fffcf4, #f8f4e9) and greys (#cccccc, #dddddd, #666666) round out a soft, paper-like
  surface system typical of a children's lifestyle brand. Two font families are
  confirmed in the CSS: Recoleta, a serif used for display/heading tokens, and
  Nunito Sans, a rounded sans used for body and UI text; both get standard fallbacks
  since no license or hosting details were supplied. Buttons and inputs are defined
  with an explicit 0px border radius (--wk-button-border-radius, --jdgm-border-radius),
  so the interpretation keeps interactive elements square rather than pill-shaped.
  Bright accent hexes (pink, gold, coral) found in the palette are treated as
  seasonal/promo badge colors rather than core brand colors, since their semantic
  role could not be confirmed from static rules alone.

colors:
  primary: "#108474"
  ink: "#3e1a04"
  canvas: "#ffffff"
  body: "#3e1a04"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f6f3eb"
  surface-card: "#fffcf4"
  on-primary: "#ffffff"
  border-input: "#cccccc"
  focus-ring: "#405fa8"
  black: "#000000"
  disabled-bg: "#cccccc"
  badge-pink: "#ff1493"
  badge-gold: "#fbcd0a"
  badge-coral: "#ed5052"
  brown-hover: "#4a2915"
typography:
  display-xl: {fontFamily: "Recoleta, serif", fontSize: 90px, fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.01em"}
  display-md: {fontFamily: "Recoleta, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.01em"}
  title-md: {fontFamily: "Recoleta, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.01em"}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0"}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0"}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: "0.02em"}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-input}"
    selectedBorderColor: "{colors.ink}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
**button-primary** uses the confirmed espresso-brown ink as its fill with white text, echoing the `.button--brown` rule observed in global.min.css; a proposed darker hover state (`brown-hover`) is inferred from the `--color-brown-700` reference, though its exact hex was not supplied. **button-secondary** is a proposed outline variant for lower-emphasis actions like "View Details," sharing the same square corner treatment. **text-input** and **search** both reflect the observed `--wk-input-border-radius: 0px` and `min-height: 45px` tokens, rendered here as flat-edged fields with a light grey border; focus behavior is proposed using the `focus-ring` color inferred from the palette's blue tones, since no `--color-focus` hex was directly supplied. **nav-bar** is a proposed flat white header with hairline dividers, consistent with the deep, multi-tier menu structure (Girl/Boy/Baby & Toddler/Sale) described in the page text, though exact height and sticky behavior were not measured. **product-card** proposes a warm cream card surface for listing children's apparel, pairing a body-weight title with a smaller price line; card imagery aspect ratio is not confirmed from static CSS. **hero** models the homepage banner ("Made for childhood. Inspired by the world.") using the largest confirmed heading size token (90px) on a soft cream background. **footer** groups informational links (About Us, Giving Back, Our Boutiques) on the same soft surface, with hairline separators between sections, proposed for visual rhythm rather than observed directly. **badge** represents promotional flags such as "20-25% Off Bundles" or "New," using a bright accent pulled from the palette; color choice among pink/gold/coral is inferred, not confirmed by role. **size-selector** is a category-appropriate proposed component for baby/toddler size chips (0-2T, 2-4T, newborn), styled with the same square, bordered treatment as other inputs to match the site's non-rounded interactive language.

## Responsive Behavior
This is a proposed breakpoint structure, not measured from live rendering:

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | 0–599px   | Single-column nav collapses to hamburger + drawer menu |
| tablet    | 600–1023px| 2-column product grid; sticky promo bar height reserved via `--promo-bar-height` |
| desktop   | 1024px+   | Multi-level mega menu (New/Girl/Boy/Baby & Toddler/Sale) shown inline |

Touch targets for buttons and size-selector chips should maintain a minimum 44px hit area, consistent with the observed `--wk-button-min-height: 45px` and `--wk-input-min-height: 45px` tokens. Mega-menu collapse into an accordion-style drawer below 1024px is a reasonable proposal given the deep category nesting in the evidence, but actual collapse behavior was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, selector fragments, and page text only; no rendered layout, computed styles, or interaction states were observed. The mapping of `#108474` to a primary/functional accent role is inferred from its use in the Judge.me review widget, not from confirmed brand usage elsewhere on the site. The `--color-brown-700` hover value and `--color-focus` outline color have no confirmed hex in the supplied evidence; both are approximated from nearby palette entries. Letter-spacing values for `display-*` typography are carried over from `--font-block-heading` tokens and may not apply identically to all heading contexts. Button, input, and badge rounding follow the confirmed `0px` radius tokens, but card and hero radii are proposed defaults, not observed. Font licensing and self-hosting status for Recoleta and Nunito Sans were not verified. Mobile menu behavior, cart drawer interactions, and product-card hover states are proposed patterns only and were not confirmed through live interaction testing.
