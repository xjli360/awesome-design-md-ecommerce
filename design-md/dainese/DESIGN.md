---
version: alpha
name: "Dainese"
source_url: "https://dainese.com"
captured_at: "2026-09-28T10:02:31.781400+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dainese's storefront evidence shows a technical, high-contrast system built on a
  near-black/white base with a single saturated red (#e30613) as the brand accent,
  consistent with the marque's motorsport racing-red identity. The observed palette
  also carries a secondary alert red (#b6050f), a safety green (#33a22a), and a
  caution yellow (#ffef39), which are treated here as inferred status/badge colors
  (stock, promo, warning) rather than confirmed UI states, since no component-level
  usage was captured. Body copy uses Mulish, a humanist sans-serif, while buttons
  are explicitly set in Source Code Pro (monospace), a deliberate technical/
  data-sheet accent echoing motorsport telemetry and spec-sheet aesthetics — this
  pairing is observed directly in the critical CSS button rules. Headings share a
  500 weight and 1.2 line-height per the CSS h1–h6 rule. Layout grid, hero
  composition, and card geometry are not present in the supplied CSS and are
  therefore proposed conventions for a performance-gear e-commerce site: dense
  product grids, bold full-bleed hero imagery, and a dark, technical footer.
  Rounded corners and spacing are proposed scales, not measured values, chosen to
  stay conservative and sharp-edged in keeping with a racing/technical brand.

colors:
  primary: "#e30613"
  ink: "#191919"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#33a22a"
  warning: "#ffef39"
  danger: "#b6050f"
  border-strong: "#9d9d9c"
  neutral-dark: "#343a40"
  accent-steel: "#83acbb"
typography:
  display-xl: {fontFamily: "Mulish, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Mulish, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Mulish, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Mulish, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Mulish, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Mulish, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Source Code Pro, monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.body}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.neutral-dark}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"

## Components

**button-primary** uses the racing red as a solid fill with white text, reflecting the single accent color visible in the palette; the Source Code Pro button typography is directly observed in the critical CSS (`--bs-btn-font-family: Source Code Pro, monospace`). Hover/active states referenced by the CSS variables (`--bs-btn-hover-bg`, `--bs-btn-active-bg`) exist structurally but their resolved colors were not captured, so hover/active fills are proposed as a darkened primary.

**button-secondary** is an outline treatment on a transparent background, proposed to pair with button-primary for "Add to Cart" vs. "Wishlist"-style secondary actions common to apparel PDPs; border and hover states are inferred, not observed.

**text-input** assumes a white field with a light hairline border and body-sm type, standard for checkout, login, and newsletter forms referenced in the page text ("This field is required", newsletter signup); no focus-ring color was captured, so focus treatment is proposed.

**nav-bar** is modeled as a white, low-contrast header given the light canvas colors dominating the palette, carrying the deep multi-level category structure evident in the text (Motorbike/Bike/Ski verticals with nested subcategories). Sticky/scroll behavior is not observed.

**product-card** proposes a white card with a thin hairline border, sized for the dense PLP/PDP grids implied by repeated "NEW IN" product tiles (jackets, boots, helmets) in the page text; spacing and shadow are proposed, not measured.

**hero** is proposed as a full-bleed dark panel with large display type, matching the "Born for speed / Track-ready gear" promotional copy; the ink/near-black background is inferred from the palette's dominant near-black tones rather than a captured hero background rule.

**footer** uses the darker neutral gray as background with white text, sized to accommodate the extensive footer link taxonomy (Customer Care, Corporate, Legal) visible in the page text; this is a proposed dark-footer pattern, not a confirmed observation.

**badge** applies the observed success green as a small pill, proposed for stock-availability or promotional flags (e.g. "EXTRA 20% OFF") rather than a captured badge component.

**search** is modeled as a soft-gray input consistent with the light surface tones in the palette; no search-bar markup was present in the supplied evidence, so this is fully proposed.

**size-selector** (category-specific) addresses Dainese's protective-apparel sizing needs (jackets, gloves, boots) with a bordered swatch/chip pattern and a primary-red selected-state border; no size-grid markup was observed, so this component is proposed based on product-category conventions.

## Responsive Behavior

| Breakpoint | Value | Source |
|---|---|---|
| xs | 0px | observed (`--bs-breakpoint-xs`) |
| md | 768px | observed (`--bs-breakpoint-md`) |
| xl | 1440px | observed (`--bs-breakpoint-xl`) |
| sm, lg (proposed fill) | ~576px, ~1024px | proposed, not present in supplied CSS |

This is a recommendation, not measured site behavior. Below `md`, navigation is assumed to collapse into a hamburger/off-canvas menu given the deep multi-level category taxonomy in the page text; category flyouts likely become accordions. Touch targets should be at least 44×44px for primary buttons and size-selector chips. Product grids are assumed to step from a single column below `md` to multi-column above `xl`, but no grid CSS was captured to confirm column counts or gutter values.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static critical-CSS and page-text extraction only; no rendered layout, hover/focus states, or JavaScript-driven interactions were observed. Color-to-role mapping (e.g., which grays serve as `muted` vs `hairline` vs `border-strong`) is inferred from typical UI conventions, not confirmed by selector-level usage. All spacing and rounded-corner values are proposed defaults, except the button padding (`0.6rem`) and button line-height/weight, which are directly observed. Breakpoints beyond `xs`/`md`/`xl` are proposed. Mulish and Source Code Pro are used as observed font-family declarations; actual license/self-hosting/web-font-loading status was not verified. Mobile menu behavior, cart/checkout flows, and product-card imagery treatment were not present in the supplied evidence and are marked proposed throughout.
