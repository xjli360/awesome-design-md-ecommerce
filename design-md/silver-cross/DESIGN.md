---
version: alpha
name: "Silver Cross"
source_url: "https://silvercrossbaby.com"
captured_at: "2026-09-28T10:15:16.320433+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is grounded in the CSS custom properties published on
  silvercrossbaby.com's root stylesheet, which define a purple primary
  (#633aa2), a warm off-white secondary (#f5f3ee), an olive accent (#555944),
  and a slate-blue text color (#3c4a53) against white and near-black surfaces.
  A pale lavender tint (#f5f2ff) and a light-grey utility scale (uiLightGrey,
  uiMidGrey, uiDarkGrey, uiBlack) round out the token set, suggesting a
  restrained, premium British-nursery aesthetic rather than a saturated
  e-commerce look. The purple primary is reserved here for calls-to-action and
  brand accents; the olive and lavender tones are treated as secondary/tertiary
  accents (inferred) for badges and soft card backgrounds, since no selector
  evidence ties them to specific components.
  Typography uses Poppins for display/heading roles and Roboto for body copy,
  both drawn from the observed font-family evidence; this pairing is an
  inferred convention, not a confirmed heading/body split, since no
  site-specific selector rules for headings were supplied. System-ui and
  sans-serif fallbacks are retained throughout. Rounded corners and spacing
  are proposed scales suited to a soft, family-friendly retail interface, not
  measured values. The result favors calm whitespace, clear product
  photography framing, and a single confident accent color for conversion
  moments (bundles, sale badges, primary buttons).

colors:
  primary: "#633aa2"
  ink: "#3c4a53"
  canvas: "#ffffff"
  body: "#3c4a53"
  muted: "#b9b9b9"
  hairline: "#e8e8e8"
  surface-soft: "#f5f3ee"
  surface-card: "#f5f2ff"
  on-primary: "#ffffff"
  accent-olive: "#555944"
  surface-dark: "#272727"
  ui-black: "#252525"
  ui-light-grey: "#fbfbfb"
  error: "#ca2003"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  bundle-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    badgeColor: "{colors.accent-olive}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.ui-light-grey}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** carries the purple brand color as a solid fill for primary conversion actions (Add to Basket, Shop Now). Hover/active states are proposed, not observed, and would typically darken the fill slightly.

**button-secondary** is an outline variant using the same purple for text and border on a transparent background, intended for lower-priority actions like "View more" links seen throughout the category navigation.

**text-input** models a standard form field (search box, newsletter signup) with a light hairline border and dark ink text; focus-ring styling is proposed, not confirmed from the CSS evidence.

**nav-bar** represents the top navigation and mega-menu shell implied by the extensive category structure (Pushchairs, Car Seats, Nursery, Feeding). White background with hairline dividers is inferred from the utility-grey token set.

**product-card** covers individual product tiles (e.g., Nia Stroller, Reef 2) using the pale lavender surface tint as a subtle differentiator from the white page background, with rounded corners for a soft, family-friendly feel.

**bundle-card** is a category-specific component for the site's distinctive "Travel System Bundles" and multi-piece sets, using the warm off-white secondary surface and an olive accent badge to signal piece-count or savings — a pattern proposed to match observed bundle-heavy merchandising language.

**hero** models the large banner sections (e.g., "Reef 2 Special Edition," "Nia Stroller") on a dark surface with white text, matching the dark background token observed in the root variables.

**footer** uses the same dark surface treatment for consistency with the hero, housing support/help links; exact footer layout is not observed and is proposed.

**badge** covers sale/error/validation indicators using the observed validation-error red, applied here to "Sale" and stock-alert style tags.

**search** models the header search affordance using the light-grey utility background for visual separation from white page chrome.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout intent |
|---|---|---|
| mobile | <480px | Single-column, stacked nav collapses to hamburger/menu drawer |
| tablet | 480–1024px | 2-column product grids, condensed mega-menu |
| desktop | 1024–1440px | Full mega-menu, 3–4 column product grids |
| wide | >1440px | Max-width content container, 4+ column grids |

Touch targets should be a minimum of 44×44px for nav and cart controls (proposed). Mega-menu categories (Pushchairs, Car Seats, Nursery, Feeding) should collapse into an accordion pattern below tablet width (proposed, not observed).

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, hover states, animations, or actual mobile breakpoints were observed. Font-family-to-role mapping (Poppins for display, Roboto for body) is an inferred pairing based on the observed font list, not a confirmed selector-level rule from the brand's own stylesheet. Several colors (e.g., curator.io widget colors like #ea6d6b, #fed136, #1b76f2) belong to a third-party social-feed plugin and were excluded from primary role assignment as they do not represent core brand chrome. Spacing and rounded-corner scales are proposed conventions, not measured values. Component states (hover, focus, disabled, error) are proposed and unverified. Custom font licensing/availability (Poppins, Roboto) was not verified for this brand's actual deployment and should be confirmed before implementation.
