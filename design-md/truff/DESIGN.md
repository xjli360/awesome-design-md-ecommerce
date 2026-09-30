---
version: alpha
name: "Truff"
source_url: "https://truff.com"
captured_at: "2026-09-28T09:46:13.903721+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Truff's storefront runs on a Shopify/Oxygen stack with "Brown" as the sole
  declared brand typeface (sans-serif fallback), paired with system fonts for
  code/mono contexts only. The observed CSS exposes a compact, disciplined
  palette: a bronze-gold (#88723a) drives primary buttons and borders, with a
  deep green (#00694f) reserved for hover/active states — together evoking the
  truffle-and-luxury-condiment positioning implied by the page copy ("Luxury
  Condiments"). Neutrals range from near-black ink (#1a1a1a) through mid grays
  (#6f6f70, #e6e7e9) to off-white surfaces (#f5f5f5, #fbfbfb, #ffffff),
  supporting a light, editorial canvas. Additional gold/tan tones (#cab683,
  #cdaf62, #c6b377) appear in the palette and are inferred here as decorative
  accents (badges, dividers, gift/luxury callouts) rather than primary UI
  color, since no selector evidence ties them to specific components. A red
  (#ac1b2e) is treated as an inferred promo/alert tone given the visible
  "25% OFF" banner text. Typography scale, spacing, and radii below extend the
  two hard CSS values observed (2rem uppercase h1, .25rem button radius) into
  a fuller system for a food/condiment DTC storefront; all extended values are
  explicitly proposed, not measured.

colors:
  primary: "#88723a"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#1a1a1a"
  muted: "#6f6f70"
  hairline: "#e8e8e8"
  surface-soft: "#f5f5f5"
  surface-card: "#fbfbfb"
  on-primary: "#ffffff"
  accent-green: "#00694f"
  accent-gold: "#cab683"
  accent-gold-deep: "#b58d28"
  gray-disabled-bg: "#e6e7e9"
  alert: "#ac1b2e"
  black: "#000000"
typography:
  display-xl: {fontFamily: "Brown, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Brown, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0.02em, textTransform: uppercase}
  title-md: {fontFamily: "Brown, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Brown, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Brown, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Brown, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "Brown, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 20px, letterSpacing: 0.05em, textTransform: uppercase}
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
    hoverBackgroundColor: "{colors.accent-green}"
    border: "1px solid {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.canvas}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkHoverColor: "{colors.accent-gold}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spice-level-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.alert}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components
**button-primary** reflects observed CSS directly: bronze-gold (#88723a) fill, white text, `.25rem` radius, uppercase bold button typography, with a green (#00694f) hover fill — both states are directly evidenced in the `.btn-primary` rules.

**button-secondary** mirrors the observed `.btn-secondary` pattern: white background/border with gold text at rest, inverting to gold fill with white text on hover. This combination (white-on-white) suggests it is designed for use over imagery or dark sections; that placement context is inferred, not confirmed.

**text-input** is proposed. No form-field CSS was supplied, so hairline border, card-surface background, and body-md typography are extrapolated from the neutral palette and general Shopify theme conventions.

**nav-bar** is proposed from page-text evidence (Shop, Explore, Account, Cart links, promo ticker) rather than measured layout CSS. A light canvas background with hairline divider is assumed consistent with the rest of the light-surface system.

**promo-banner** reflects the visible "GET 25% OFF" / "FREE SHIPPING" ticker text; color mapped to primary gold as a brand-consistent, proposed treatment since no banner-specific selector was supplied.

**product-card** is proposed for the "Shop Hot Sauce / Oil / Salt / Aioli" grid implied by navigation and tasting-menu copy; card surface, hairline border, and radius follow the neutral/radius tokens already observed elsewhere in the theme.

**hero** corresponds to the "Try TRUFF Hot Sauce" banner copy; large display typography and a primary CTA button are proposed groupings, not a captured hero-section stylesheet.

**footer** is proposed as a dark-ink footer given the long link list (Company, Explore, Social, legal pages) in the page text; no footer background color was present in supplied CSS, so this mapping is explicitly inferred.

**badge / spice-level-tag** are category-appropriate proposals for a hot-sauce brand (e.g., heat-level or "new" flags), built from palette colors not otherwise tied to a confirmed component role.

## Responsive Behavior
Recommended, not measured from live rendering:

| Breakpoint | Width       | Notes                                  |
|-----------|-------------|-----------------------------------------|
| sm        | 0–639px     | single-column, nav collapses to menu icon |
| md        | 640–1023px  | 2-column product grid                   |
| lg        | 1024–1279px | 3-column product grid, full nav visible |
| xl        | 1280px+     | 4-column grid, max-width container      |

Touch targets should maintain a minimum 44×44px hit area for buttons and nav icons (proposed, aligned with the observed 3.125rem/50px button height). Mobile nav is assumed to collapse into a hamburger/drawer pattern; this is a common Shopify theme behavior but was not directly observed in the supplied CSS or DOM.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from static CSS/text extraction only; no rendered layout, computed breakpoints, or interaction states (focus rings, active/pressed styles, form validation, cart drawer behavior) were observed. Font "Brown" is asserted only as declared in `font-family`; its license, weights, and availability were not verified. Several palette entries (e.g., #cab683, #cdaf62, #c6b377, #b58d28, #189cc5, #4a69d4) had no accompanying selector evidence, so their component roles here (accents, links) are inferred by plausibility rather than confirmed usage. Spacing scale, typography sizes beyond h1/btn-text/body, radii beyond the observed `.25rem`, and all "proposed" component states are extrapolated for design-system completeness and should be validated against production markup before implementation.
