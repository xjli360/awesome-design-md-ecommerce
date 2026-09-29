---
version: alpha
name: "N-FAB"
source_url: "https://n-fab.com"
captured_at: "2026-09-28T09:09:13.413146+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from CSS custom properties served on N-FAB's
  brand page at realtruck.com, the manufacturer platform behind N-FAB steps,
  running boards, and nerf bars. The evidence shows a utilitarian retail
  system: a near-black header (#1e1e1e) paired with a saturated yellow
  accent (#ffc600) used for cart and icon states, plus an informational
  blue (#057dbc) shared between links and action states. Body copy relies
  on a neutral dark gray (#333333) against white and light-gray surfaces
  (#f3f3f3, #fafafa), consistent with a dense industrial-parts catalog
  needing high scan-ability across a large mega-menu of exterior
  accessories. Two custom font tokens, PlatformFont and PlatformBrandFont,
  are declared but not verified for licensing or webfont delivery, so
  fallbacks are specified. Semantic roles below (on-primary, surface-card,
  hairline) are inferred from variable naming and typical e-commerce
  header/footer patterns visible in the selectors, not from rendered
  screenshots. Success, warning, and danger hues map directly to declared
  UI state variables. The resulting system favors legibility and dense
  navigation over decorative flourish, appropriate for a fitment-driven
  truck-accessory storefront.

colors:
  primary: "#ffc600"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#d5d5d5"
  surface-soft: "#f3f3f3"
  surface-card: "#fafafa"
  on-primary: "#1e1e1e"
  action: "#057dbc"
  action-dark: "#23889b"
  info-tint: "#ecf6fd"
  danger: "#e50000"
  success: "#15884f"
  warning: "#fa6400"
typography:
  display-xl: {fontFamily: "'PlatformBrandFont', sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'PlatformBrandFont', sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'PlatformFont', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'PlatformFont', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "'PlatformFont', sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.action}"
    borderColor: "{colors.action}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.danger}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.info-tint}"
    textColor: "{colors.action-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.action}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"

## Components

**button-primary** uses the declared `--colorPrimary` yellow with a dark ink label, matching the observed cart/icon accent usage; hover and disabled states are proposed, not observed.

**button-secondary** is an outline treatment using the informational blue token (`--colorInfo`), suited for secondary CTAs like "Shop at a Dealer" links seen in the header text; interaction states are proposed.

**text-input** applies the neutral gray-light hairline border and white canvas seen across form-related variables; focus-ring color is not evidenced and is left as a proposed extension of `{colors.action}`.

**nav-bar** mirrors the `.or-header` and `.or-mobile-header` selectors, both set to dark/black backgrounds with white text and primary-yellow icon color — this is a direct mapping, not an inference.

**product-card** is a proposed pattern for the mega-menu's dense catalog (Steps, Tonneau Covers, etc.), using the light `#fafafa` surface and hairline border; the sale-price color directly reuses `--colorDangerDark`-equivalent `#e50000` per the `.or-product-listing-sale-price` rule.

**hero** proposes a dark ink banner with large brand-font display type, appropriate for a manufacturer landing page, though no hero markup was present in the supplied CSS.

**footer** reuses the dark header palette for visual continuity, with the subscribe button referencing `--colorSecondary` (unresolved in evidence, so mapped to `{colors.action}` as nearest observed analogue) per `.or-footer-subscribe-button`.

**badge** is a proposed small-label component for tags like "Free Shipping $100+," using the light info tint background not directly tied to a named selector but consistent with the blue family present in the palette.

**search** and **fitment-selector** are proposed, industry-appropriate components: N-FAB and RealTruck pages emphasize vehicle-fitment tools ("Build Your Truck in 3D"), so a distinct fitment selector pattern is included, styled with the observed action-blue border and soft surface background; no direct selector evidence for this component was supplied.

## Responsive Behavior

This is a recommendation, not measured site behavior, since no breakpoint or viewport CSS was included in the supplied evidence.

| Breakpoint | Width | Behavior (proposed) |
|---|---|---|
| Mobile | <640px | Single-column product grid, collapsed nav to hamburger menu (`.or-mobile-header` suggests a distinct mobile header already exists) |
| Tablet | 640–1024px | Two-column product grid, condensed mega-menu |
| Desktop | >1024px | Full mega-menu with multi-column category flyouts |

Touch targets should be at least 44px in height for buttons and nav items; mega-menu categories should collapse into accordions below 1024px. None of this was directly observed in static CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to CSS custom properties and selector declarations extracted statically; no rendered screenshots or DOM layout were available.
- Several CSS variables (`--colorSecondary`, `--colorDangerDark`, `--colorInfoLight`) were referenced but not fully resolved in the supplied excerpt; nearest observed hex values were substituted where reasonable and flagged inline.
- Semantic role assignments (e.g., `on-primary`, `surface-card`, `info-tint`) are inferred from variable naming conventions and typical retail UI patterns, not confirmed via visual inspection.
- Font rendering, weight availability, and licensing for `PlatformFont` and `PlatformBrandFont` are unverified; system sans-serif fallbacks are specified for safety.
- Interaction states (hover, focus, active, disabled) and mobile-specific layouts are proposed based on common e-commerce conventions, not observed in the supplied CSS.
- Spacing and rounding scales follow a standard proposed system rather than measured values, since no explicit spacing/radius tokens were present in the evidence.
