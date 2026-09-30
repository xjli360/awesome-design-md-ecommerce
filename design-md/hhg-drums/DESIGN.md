---
version: alpha
name: "HHG Drums"
source_url: "https://www.hhgdrums.com"
captured_at: "2026-09-28T10:32:51.038849+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  HHG Drums presents a dark, workshop-inspired storefront for Haggerty Hollow
  Guild, a maker of handmade snare drums. The observed Shopify theme runs on
  a near-black canvas (#1f1f21) with white foreground text and a single
  high-contrast accent, an acid yellow-green (#e3fc02), explicitly wired to
  buttons, links, and secondary-button text via CSS custom properties. This
  reads as a confident, craft-forward palette: dark ground lets close-up
  product photography of copper, ash, and mahogany shells carry visual
  weight, while the yellow-green accent punches through for calls to action.
  Supporting neutrals (#1c1c1c, #232323, #121212, #dedede) are inferred as
  layered surface and skeleton-loading tones rather than confirmed brand
  colors. Typography pairs EB Garamond, a serif likely reserved for display
  and heading roles given the theme's heading font-family variable, with
  Figtree, a grotesque sans inferred for body copy and UI text based on the
  base font-size/letter-spacing rules on body and .text-body. Several bright
  hues in the raw palette (blues, reds, oranges) correspond to third-party
  payment-method icons, not brand colors, and are excluded from the system
  below. Rounded corners and spacing follow conventional Shopify-theme
  defaults since no explicit pixel radii were present in the evidence.

colors:
  primary: "#e3fc02"
  ink: "#ffffff"
  canvas: "#1f1f21"
  body: "#ffffff"
  muted: "#dedede"
  hairline: "#00000080"
  surface-soft: "#232323"
  surface-card: "#1c1c1c"
  surface-deep: "#121212"
  on-primary: "#1f1f21"
  accent-secondary: "#00fced"
typography:
  display-xl: {fontFamily: "'EB Garamond', serif", fontSize: "48px", fontWeight: 500, lineHeight: 1.15, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'EB Garamond', serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "'EB Garamond', serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.06rem"}
  body-md: {fontFamily: "'Figtree', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "'Figtree', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0.04rem"}
  caption: {fontFamily: "'Figtree', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.04rem"}
  button-md: {fontFamily: "'Figtree', sans-serif", fontSize: "15px", fontWeight: 500, lineHeight: 1, letterSpacing: "0.06rem"}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    shadow: "none (proposed)"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  drum-spec-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    typography: "{typography.body-sm}"

## Components

**button-primary** renders the theme's explicit `--color-button`/`--color-button-text` pair (yellow-green on near-black), matching the "Buy This Drum" and checkout actions seen in the evidence. Hover/active states were not observed and are proposed as a slight opacity or darken shift.

**button-secondary** inverts the primary pattern using the theme's `--color-secondary-button` variables (dark fill, accent text/border), suitable for "Continue shopping" or tertiary catalog actions. Border treatment is proposed since no explicit secondary-button border width was captured.

**text-input** is a proposed pattern for the email subscribe field and any account/login forms, using a slightly lighter surface than canvas so fields remain legible against the dark theme; focus ring styling is inferred from the site's generic `--focused-base-outline` custom property but exact color/width was not directly observed on inputs.

**nav-bar** covers the top utility/header row (Home, Catalog, Contact, Gallery, About, cart, search, login) implied by the page-text excerpt. Layout, sticky behavior, and mobile-menu treatment are proposed, not measured.

**product-card** models the catalog grid tiles (e.g., "14x5 ash stave snare drum…") using the theme's `.product-card-wrapper .card` custom-property hooks for radius/border/shadow, none of which had concrete pixel values in evidence, so card elevation is proposed as flat/borderless on the dark surface.

**hero** represents the homepage banner carousel ("1 / of 5", "Handmade Drums with Character and Presence") referenced in the text excerpt. Image treatment, overlay, and carousel controls were not present in the supplied CSS and are proposed.

**footer** covers the newsletter signup, social links, and payment-method row. Payment icon marks (Visa, Amex, PayPal, etc.) are excluded from the brand palette per Known Gaps but their presence confirms a standard Shopify footer pattern.

**badge** is proposed for stock/sale or "handmade" labeling, reusing `--color-badge-*` variables (white border/foreground on dark background) defined at the root level, though no rendered badge markup was captured.

**search** models the header search/cart interaction implied by "Search / Log in / Cart" text; exact overlay or drawer styling was not observed.

**drum-spec-card** is a category-appropriate component proposed for presenting each drum's build specification (shell material, dimensions, finish, hardware) as seen in product titles like "14x7 mahogany stave snare drum with black glass glitter inlay…". It uses the accent color sparingly to highlight key spec labels against dark card surfaces.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width | Behavior (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column catalog, collapsed nav to hamburger, stacked hero text |
| Tablet | 480–989px | 2-column product grid, condensed nav |
| Desktop | ≥ 990px | Full nav row, multi-column catalog grid (3–4 cards) |

Touch targets should be at least 44×44px for buttons and nav links, consistent with the theme's `clamp(25px, …, 55px)` accelerated-checkout button sizing observed in the payment-wallet CSS. Navigation is assumed to collapse into a drawer/menu below tablet width; this is a convention inference, not a confirmed site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, hover/focus states, animations, or actual mobile breakpoints were observed. The heading-vs-body assignment of EB Garamond and Figtree is inferred from theme variable naming conventions, not confirmed rendering. Several palette hex values (#eb001b, #f79e1b, #ff5f00, #0071ce, #142fbd, #1532cb, #1990c6, #136f99) correspond to third-party payment-method iconography (card networks, wallets) and were deliberately excluded from the brand color system. The role of #00fced could not be tied to a specific CSS property and is labeled uncertain/decorative. Border-radius and spacing scales use conventional defaults, as no explicit pixel values for `--buttons-radius-outset` or card corner radii were present in evidence. Font licensing/availability for EB Garamond and Figtree as used by this specific site was not verified beyond the `font-family` declarations shown.
