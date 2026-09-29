---
version: alpha
name: "Louise Goods"
source_url: "https://louisegoods.com"
captured_at: "2026-09-28T04:38:33.340934+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Louise Goods presents itself as a precise, workshop-grade leather brand
  ("In Leather We Trust"), and the extracted CSS supports a restrained,
  high-contrast system rather than a decorative one. The observed palette is
  built from true black (#000000) and white (#ffffff), with a soft near-black
  (#121212) used as running body text, and a single saturated accent,
  #1990c6, reserved for the checkout call-to-action, darkening to #136f99 on
  hover. Neutral overlays (#0000000d, #00000033, #00000066, #3636364d) appear
  in the source only as transparency layers — skeleton loaders, scrims, and
  hover tints — and are reinterpreted here as muted text, hairlines, and soft
  surface tints. Typography pairs Instrument Sans, the evidenced UI font,
  across headings and body copy, with the supplied monospace stack
  (Consolas/Menlo/Courier New) proposed for small technical captions such as
  material tags or batch labels, fitting a handcrafted-goods register. Font
  sizes at 12–20px (0.75–1.25rem) are directly observed theme tokens; larger
  display sizes are proposed extrapolations, not measured. Shopify's default
  0px button border-radius suggests the brand favors sharp, unornamented
  edges over rounded ones, so the rounding scale below stays minimal. All
  layout, spacing, and component states are inferred conventions for a
  leather-goods storefront, not confirmed from live rendering.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#00000066"
  hairline: "#dedede"
  surface-soft: "#0000000d"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  overlay: "#00000033"
  overlay-strong: "#3636364d"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Instrument Sans, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: "1.25rem", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: "0.875rem", fontWeight: 400, lineHeight: 1.65, letterSpacing: "0px"}
  body-sm: {fontFamily: "Instrument Sans, sans-serif", fontSize: "0.8125rem", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  caption: {fontFamily: "Consolas, Menlo, Monaco, 'Liberation Mono', 'Courier New', monospace", fontSize: "0.75rem", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: "0.875rem", fontWeight: 500, lineHeight: 1, letterSpacing: "0.2px"}
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
  section: 96px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlayColor: "{colors.overlay}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    borderColor: "{colors.overlay-strong}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  material-swatch-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"

## Components

**button-primary** carries the one evidenced brand color, #1990c6, matching the observed Shopify accelerated-checkout button, darkening to #136f99 on hover exactly as measured in the CSS. It is proposed as the site's main add-to-cart/checkout action.

**button-secondary** is inferred as an outlined, transparent-background counterpart for lower-priority actions ("View details," "Learn more"), keeping the sharp-edge convention (rounded.none) suggested by the checkout button's 0px default radius.

**text-input** proposes a plain white field with a light hairline border (#dedede, observed as the skeleton-loader/background neutral) and a solid ink-colored focus state; no live focus interaction was observed, so this state is proposed.

**nav-bar** is modeled from the header's grid variables (three-column primary-nav/logo/secondary-nav layout, sticky behavior, and generous 1.6rem block padding), all directly evidenced in the header selector, though the visual rendering itself was not captured.

**product-card** is a category-appropriate, un-evidenced pattern proposed for leather-goods listings: white surface, hairline border, product title in title-md and price in the smaller body-sm size, reflecting the theme's compact 13–14px base text scale.

**hero** is proposed as a full-bleed dark (ink) banner with white text and a translucent overlay (#00000033) sourced from the observed overlay/scrim palette, intended for lifestyle photography introducing the "In Leather We Trust" positioning.

**footer** reuses the ink background and a stronger translucent divider (#3636364d, observed as a border/overlay token) to separate link columns, with muted (#00000066) secondary text for legal/copyright lines — a common but unverified footer convention.

**badge** is a small pill using the softest observed tint (#0000000d) as background, intended for "New," "Limited," or "Handmade in NY" labels, set in the monospace caption style to echo a workshop/atelier tone.

**search** proposes a pill-shaped, softly tinted field consistent with the badge treatment, using muted text for the placeholder state; no live search UI was observed.

**material-swatch-card** is the category-specific component: a small bordered tile for selecting leather color/finish on product pages, with the primary accent color marking the selected state — a proposed pattern, not confirmed from the live site.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column stack, nav collapses to a hamburger/drawer, container-gutter reduces toward the observed 2rem token |
| Tablet | 600–1024px | Two-column product grids, header retains three-slot grid at reduced padding |
| Desktop | 1024–1440px | Full three-column header grid as evidenced, container-gutter at observed 3rem |
| Wide | >1440px | Content remains centered with a max-width container; spacing scales up to section (96px) between major blocks |

Touch targets should stay at a minimum 44px height, matching the Shopify accelerated-checkout button's clamp(25px, …, 55px) sizing observed in the CSS. Mobile nav collapse, drawer/menu interactions, and card grid wrapping are proposed conventions and were not observed in rendered layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and metadata only; no live page render, interaction, or DOM screenshot was captured. Color-role assignments (e.g., which neutral serves as "muted" vs. "hairline") are inferred from typical usage of transparency values (skeleton backgrounds, overlays) and are not confirmed semantic labels. Display typography sizes (display-xl, display-md) are proposed extrapolations beyond the observed 0.75–1.25rem theme scale. Instrument Sans is used as the evidenced UI font, but its licensing, weight availability, and actual loading behavior were not verified. The monospace stack's application to captions/badges is a stylistic proposal, not an observed usage. Component states (hover, focus, selected, error) beyond the one measured checkout-button hover are proposed and unverified. Mobile navigation, drawer, and grid-wrapping behavior were not observed and are recommendations only. A stray dark-theme color-scheme block (rgb triples, not hex) appeared in the raw evidence but was excluded from the palette since it falls outside the supplied hex list.
