---
version: alpha
name: "Tinycottons"
source_url: "https://tinycottons.com"
captured_at: "2026-09-28T04:53:17.691435+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Tinycottons presents itself as a Barcelona-based ethical kids' and women's
  apparel label, and the extracted stylesheet evidence points to a lean,
  utilitarian Shopify (Dawn-derived) build rather than a heavily custom
  storefront. The observed palette is dominated by near-black ink tones
  (#030303, #121212, #202223) against white canvas, with a soft pale-yellow
  (#fff5cd) likely reserved for the announcement bar or seasonal callouts,
  and a cyan-blue pair (#1990c6 / #136f99) sourced from Shopify's native
  accelerated-checkout button — treated here as the closest available
  primary/interactive accent since no other brand accent color was supplied.
  Neutral grays (#e2e2e2, #f6f6f7, #f1f2f3, #6d7175) form hairlines and card
  surfaces typical of a minimal product-grid layout. Typography is limited to
  two observed sans-serif families, DM Sans and Mulish, at notably compact
  root sizes (11–18px), suggesting a dense, editorial navigation system
  (the multi-level WOMAN/KIDS/BABY mega-menu) rather than an oversized
  display-type identity; larger display sizes below are proposed
  extrapolations for hero/marketing use, not measured. Border-radius is
  explicitly 0px on the observed checkout button, reinforcing a square,
  minimal-ornament aesthetic carried through this interpretation's near-zero
  default rounding.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#030303"
  ink-soft: "#121212"
  canvas: "#ffffff"
  body: "#202223"
  muted: "#6d7175"
  hairline: "#e2e2e2"
  surface-soft: "#f6f6f7"
  surface-card: "#f1f2f3"
  on-primary: "#ffffff"
  accent-cream: "#fff5cd"
  error: "#d72c0d"
  success: "#008060"
typography:
  display-xl: {fontFamily: "DM Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "DM Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "DM Sans, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Mulish, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Mulish, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Mulish, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "DM Sans, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.xl}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    hairline: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  age-size-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.base}"
    border: "1px solid {colors.hairline}"

## Components

**button-primary** uses the checkout-derived cyan (#1990c6) as the only strong accent found in the evidence, with a darker hover state (#136f99) also observed directly in the CSS. Square corners (0px) match the explicit `border-radius:0` on the source button.

**button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g. "View All"), using ink text on white with a hairline border; no secondary button was directly observed, so styling is inferred from the overall minimal aesthetic.

**text-input** proposes a compact bordered field sized to the small observed base font (12px/0.75rem), suited to newsletter and search fields referenced in the page text ("Subscribe", "Search").

**nav-bar** reflects the evidenced CSS grid template (`--header-grid: "logo primary-nav secondary-nav"`) and logo widths (75px mobile-inferred, 120px desktop-inferred) from the header custom properties, with caption-scale type matching the dense multi-level WOMAN/KIDS/BABY menu.

**product-card** is a proposed pattern for the collection grids (DRESSES, TEES, OUTERWEAR, etc.) using the light card surface (#f1f2f3) and a hairline border; card content, badges, and hover states were not directly observed.

**hero** proposes a full-bleed dark banner for homepage promotion blocks referenced in the text ("SHOP THE NEW COLLECTION"), defaulting to ink background since no hero-specific color was in evidence.

**footer** maps to the observed link groups (About, Information, Policies) using the muted surface tone (#f6f6f7) for visual separation from the main canvas.

**badge** reflects Shopify's native sale/sold-out badge tokens in the CSS (`--on-sale-badge-background`, `--sold-out-badge-background`), approximated here with the closest observed near-black (#121212) since the exact RGB triplet (31 31 31) wasn't in the supplied hex list.

**search-overlay** is a proposed full-panel search pattern consistent with the "Search" nav item; no overlay-specific styling was captured.

**age-size-filter-chip** is a category-appropriate proposed component for kids/baby apparel, supporting age-range or size filtering across the BODIES/PANTS/OUTERWEAR taxonomy visible in the navigation; pill shape and muted surface are inferred, not observed.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | single-column product grid, collapsed hamburger nav, header logo ~75px per observed `--header-logo-width` |
| tablet | 640–1024px | 2–3 column grid, mega-menu collapses to accordion |
| desktop | 1024–1440px | full mega-menu per `--header-grid`, logo ~120px per observed value, 3–4 column grid |
| wide | >1440px | container gutter caps at observed `--container-gutter: 3rem` |

Touch targets are recommended at a minimum 44px height (aligned with the observed Shopify accelerated-checkout button clamp of 25–55px). Mega-menu collapse behavior, sticky-header transitions (`--header-is-sticky: 1` was observed as a flag but its visual effect was not), and cart-drawer interactions are proposed patterns only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Color-to-role mapping (e.g. treating the Shopify checkout-button blue as the brand primary) is inferred, since no explicit brand accent was present in the evidence. The badge background (RGB 31,31,31) does not exactly match any supplied hex and was approximated to the nearest observed value. All display/title/body font sizes above rem-based root values (0.6875–1.125rem) are proposed extrapolations, not measured. Mobile menu behavior, hover/focus/active states, product-card content, and cart-drawer layout were not observed. Availability, weights, and licensing of DM Sans and Mulish as loaded webfonts were not verified beyond their appearance in the font-family stack.
