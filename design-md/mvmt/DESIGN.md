---
version: alpha
name: "MVMT"
source_url: "https://mvmt.com"
captured_at: "2026-09-28T04:16:24.396337+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  MVMT's storefront CSS shows a high-contrast, editorial palette built from near-black text (#1c1c1c, #232323), true black (#000000, #121212) and white (#ffffff), with soft neutrals (#efefef, #dedede) used for panels and hairlines. The only saturated brand-adjacent color found in functional UI (not payment-network logos) is a teal-blue pair (#1990c6 default, #136f99 hover) drawn from the Shopify accelerated-checkout button, which we treat as the interactive accent. A warm taupe (#b9b3a8) appears in the palette and is proposed as a secondary, lower-emphasis accent. Payment-icon colors (#eb001b, #f79e1b, #ff5f00, #0071ce, #142fbd, #1532cb) are excluded from brand roles since they belong to third-party wallet marks, not MVMT's own system.

  Typography evidence shows a two-family system: "ivypresto-headline" (serif) for display/heading moments and "brandon-grotesque" (sans) for body, UI and eyebrow text, both with named CSS fallback fonts before generic serif/sans-serif. Root custom properties define a clear heading scale (h1 64px down to h6 20px) plus utility sizes (xs–xl) and an explicit eyebrow size, all reused below. Border-radius on primary checkout buttons is 0px, suggesting a squared, minimal-radius aesthetic; rounded values below are a proposed restrained scale rather than measured across all components.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#6a6f75"
  hairline: "#dedede"
  surface-soft: "#efefef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  deep-black: "#121212"
  sand: "#b9b3a8"
  divider-soft: "#0000000d"
  border-soft: "#c8c8c833"
  scrim: "#00000033"
  overlay: "#00000066"
typography:
  display-xl: {fontFamily: "ivypresto-headline, IvyPresto Headline Fallback, serif", fontSize: 64px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "ivypresto-headline, IvyPresto Headline Fallback, serif", fontSize: 40px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "brandon-grotesque, Brandon Grotesque Fallback, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "brandon-grotesque, Brandon Grotesque Fallback, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "brandon-grotesque, Brandon Grotesque Fallback, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "brandon-grotesque, Brandon Grotesque Fallback, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "brandon-grotesque, Brandon Grotesque Fallback, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 1px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-soft}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.deep-black}"
    overlay: "{colors.overlay}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  review-rating:
    starColor: "{colors.ink}"
    countTypography: "{typography.caption}"
    textColor: "{colors.muted}"
    layout: "inline stars + review count, left-aligned"

## Components
**button-primary** uses the teal accent found in the accelerated-checkout CSS as its background, with a darker hover state; it is the proposed default for "Add to Cart" and primary CTAs, though the exact production hover behavior is not verified beyond the wallet-button rule it was sourced from.

**button-secondary** is a squared, outlined ink-on-white button for lower-priority actions (e.g., "View Details"), inferred from the general squared-corner aesthetic (0px radius on primary checkout buttons) rather than direct observation of a secondary style.

**text-input** proposes a hairline-bordered field with generous padding, suited to search and account forms; border color and radius are proposed defaults, not confirmed from captured form CSS.

**nav-bar** reflects the header grid evidence (`primary-nav logo secondary-nav` columns, sticky behavior, logo widths of 80–130px) with a white background and ink text; the transparent-header text-color variable (white) suggests an alternate state over hero imagery, proposed as a variant.

**product-card** is a minimal white card with a soft border, using the two-column grid signal (`--product-list-items-per-row: 2`) as loose guidance for density; card shadow/hover states are proposed, not observed.

**hero** assumes a dark, full-bleed banner with a semi-opaque black overlay (matching the `--page-overlay` token) and large serif display type, appropriate for lifestyle watch photography; exact hero copy/layout was not observed.

**footer** is proposed as a dark ink panel with white text and sans-serif links, consistent with the site's dark/light contrast pattern; column structure is not confirmed from evidence.

**badge** covers sale/sold-out/custom labels referenced in root variables (e.g., custom badge background near-black, sold-out gray); rendered here generically since precise badge colors are exposed as unconverted rgb() triples outside the supplied hex palette.

**review-rating** reflects the "95K+ 5-Star Reviews" title signal and a dedicated `--star-color` token; treated as a proposed compact inline component pairing a star glyph color with muted caption text for review counts.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed nav to hamburger, sticky header retained per `--header-is-sticky` |
| tablet | 640–1024px | 2-column product grid matches `--product-list-items-per-row: 2` signal |
| desktop | >1024px | Full 3-part header grid (`primary-nav logo secondary-nav`), larger logo (130px) |

Touch targets should be at least 44px tall, matching the accelerated-checkout button's `clamp(25px, 44px, 55px)` sizing pattern found in evidence. Nav collapse to an off-canvas/hamburger menu below tablet is a standard proposal, not confirmed via captured mobile markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/JS extraction only; no live rendering, viewport testing, or interaction recording was performed. Several badge and status colors (sale, sold-out, success/warning/error) exist only as unconverted `rgb()` triples in custom properties and were intentionally excluded from the hex-only color tokens above, so badge semantics are approximated using existing palette entries. The mapping of "brandon-grotesque"/"ivypresto-headline" to specific heading/body roles is inferred from naming and CSS variable structure, not a confirmed style guide. Payment-network colors (Mastercard, Amex, Visa, PayPal blues/reds/oranges) were deliberately excluded from brand roles. All spacing, rounded-corner, and component states (hover, focus, disabled, mobile nav) beyond the single documented checkout-button radius (`0px`) and hover color are proposed, not observed. Licensing and availability of "brandon-grotesque" and "ivypresto-headline" as web fonts were not verified.
