---
version: alpha
name: "De Wine Spot"
source_url: "https://dewinespot.co"
captured_at: "2026-09-28T04:14:35.302603+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  De Wine Spot's supplied CSS points to a Shopify storefront built around a deep
  wine-toned header (rgb 56 29 29, "#381d1d") paired with a warm gold accent
  (rgb 203 178 107, "#cbb26b") — a palette consistent with a rare-spirits and
  collectibles retailer. A saturated orange (#f48c06, hover #d67a05) is
  confirmed as the interactive/primary color via the age-verification button
  and the Judge.me review-widget custom properties. The remainder of the
  palette (grays from #333333 through #f9f9f9, plus isolated hues like
  #108474, #e32b2b, #621979, #fbcd0a) appears largely utilitarian —
  borders, form backgrounds, status text, and third-party widget colors —
  and is mapped here to muted/hairline/surface roles rather than treated as
  brand color. Observed font families include Nunito Sans, Barlow, DIN Next,
  Avenir/Avenir Next, and Baskerville; this interpretation assigns Baskerville
  (a classic serif) to display headings to suit a heritage spirits brand, and
  Nunito Sans/Barlow to body and UI text, though this pairing is an inferred
  editorial choice, not a captured rendering. Border-radius is treated as
  restrained (0–4px observed), reinforcing a formal, label-like aesthetic.

colors:
  primary: "#f48c06"
  primary-hover: "#d67a05"
  ink: "#381d1d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-gold: "#cbb26b"
  accent-deep: "#4c3434"
  accent-teal: "#108474"
  accent-purple: "#621979"
  alert: "#e32b2b"
  highlight: "#fbcd0a"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "DIN Next, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Barlow, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 1px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  collector-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.accent-gold}"
    borderColor: "{colors.accent-gold}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the confirmed orange accent (#f48c06) with a white label, matching the observed age-verification CTA; a darker hover state (#d67a05) is directly evidenced in the source CSS. Focus and disabled states are proposed, not observed.

**button-secondary** is an outlined variant inferred from the theme's `.btn--secondary` rule, which sets a transparent background and text color equal to the button's base color — here mapped to the primary orange on a bordered, transparent surface.

**text-input** represents search and form fields. The theme's `--input-bg-color`/`--input-text-color` custom properties bind directly to the scheme's background/text tokens, so this component reuses `canvas` and `body` with a light hairline border; focus-ring styling is proposed.

**nav-bar** reflects the `.header` block's explicit `--nav-bg-color`/`--nav-text-color` values (the deep wine ink at rgb 56 29 29 with white text), with the gold `--header-accent-color` reserved for active/hover underlines or dividers — a proposed usage, not a captured state.

**product-card** is a proposed pattern for the catalog grid appropriate to a spirits e-commerce theme; it pairs a soft card surface with hairline borders and a title/price type pairing, since no card-specific selector was present in the supplied evidence.

**hero** uses the same ink background as the header for visual continuity, with a large serif headline (display-xl) — an inferred pairing intended to evoke label/heritage typography for rare whiskey and allocated bourbon messaging.

**footer** reuses the ink/gold combination for brand consistency across top and bottom of page; link and heading treatments are proposed defaults rather than measured footer markup.

**badge** models a small labeling chip (e.g., "New," "Sold Out") using the gold accent already tied to header emphasis; this generalizes the header's accent role into a reusable UI element.

**search** maps the theme's dedicated `--search-bg-color: #4c3434` directly to a distinct, slightly warmer dark surface than the main header/nav ink, suggesting the design intentionally differentiates the search affordance.

**collector-badge** is the category-appropriate component: a small bordered tag (e.g., "Allocated," "Limited Release," "Single Cask") styled in ink-and-gold to signal scarcity and provenance, consistent with the site's rare-spirits/collectibles positioning. This is a proposed pattern, not an observed selector.

## Responsive Behavior

This is a recommendation based on Shopify-theme gutter variables found in the CSS (`--gutter-sm: 20px`, `--gutter-md: 32px`, `--gutter-lg: 80px`), not measured breakpoint behavior.

| Breakpoint | Width      | Gutter (observed var) | Notes (proposed) |
|-----------|------------|------------------------|-------------------|
| sm        | ≤767px     | 20px                   | Single-column nav collapses to a hamburger/off-canvas menu; search bar becomes full-width. |
| md        | 768–1023px | 32px                   | Product grid moves to 2–3 columns; nav-bar may remain collapsed. |
| lg        | 1024–1439px| 80px                   | Full horizontal nav-bar; product grid at 3–4 columns. |
| xl        | ≥1440px    | 80px                   | Max content width constrained; hero and section padding increase toward `{spacing.section}`. |

Touch targets should be a minimum of 44×44px for buttons and nav items on compact widths; collapse patterns (accordion filters, off-canvas cart/nav) are standard Shopify-theme conventions but were not directly observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/JS extraction only; no rendered page, DOM screenshot, or interaction trace was available. The mapping of the ink (#381d1d), gold (#cbb26b), and search (#4c3434) colors to nav/header/search roles is directly evidenced via CSS custom properties, but their extension to hero, footer, and badge components is inferred for consistency, not separately confirmed. Font-size values in the typography table are proposed defaults layered onto the theme's fluid `--h1`–`--h6` scale variables; exact rendered sizes were not captured. Hover/focus/disabled/error states beyond the single confirmed button hover are proposed. Availability, licensing, and web-font loading for Baskerville, DIN Next, Avenir/Avenir Next, and Barlow were not verified — some may be system-font fallbacks rather than licensed webfonts. Mobile menu behavior, cart drawer layout, and product-grid column counts were not observed and are marked as proposed recommendations only.
