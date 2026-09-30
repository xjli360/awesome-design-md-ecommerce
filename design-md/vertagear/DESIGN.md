---
version: alpha
name: "Vertagear"
source_url: "https://www.vertagear.com"
captured_at: "2026-09-28T04:10:39.984222+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Vertagear's storefront (built on a Shopify "Timber"-derived theme) presents a
  restrained, neutral base: white canvas, dark gray body copy (#333), and
  black (#000) used for primary call-to-action buttons and strong text. The
  supplied palette is dominated by grayscale steps (#f6f6f6 through #222222)
  used for surfaces, hover states, and disabled controls, with a single
  saturated accent, #4e4cf7 (violet-blue), standing out against the grays —
  its exact usage was not confirmed in the supplied rules, so it is treated
  here as an inferred accent/link/focus color rather than a primary action
  color, since the only observed button background is solid black. A muted
  red (#d02e2e) is retained for potential sale/alert badges, also inferred.
  Typography is confirmed as Poppins for body copy, form controls, and all
  heading levels (h1–h6), set at 15px/1.6 for body text with 400 weight
  headings at 1.4 line-height. Other font names present in the font stack
  evidence (Oxanium, TeXGyreAdventor, ProximaNovaLight) could not be tied to
  specific selectors, so any display-face usage below is explicitly labeled
  inferred. The design system below favors flat rectangular buttons
  (border-radius: 0 observed), light-gray hover/disabled surfaces, and a
  compact, utilitarian layout consistent with a technical/gaming-hardware
  retailer.

colors:
  primary: "#4e4cf7"
  ink: "#000000"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#8e8e8e"
  hairline: "#e6e6e6"
  surface-soft: "#f6f6f6"
  surface-card: "#f2f2f2"
  surface-alt: "#e3e3e3"
  on-primary: "#ffffff"
  danger: "#d02e2e"
  accent-warm: "#f26c4f"
typography:
  display-xl: {fontFamily: "Oxanium, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.42, letterSpacing: 0.3px}
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
    padding: "{spacing.sm} {spacing.md}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    hoverBackground: "{colors.surface-card}"
    activeTextColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    surface: "{colors.surface-alt}"
    textColor: "{colors.body}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  product-recommended-panel:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
---

## Components

**button-primary** — Modeled directly on the observed `.btn` rule: solid black background, white text, 700-weight label type, no corner radius, and generous horizontal padding. Hover/focus states were observed to retain the same black background rather than shifting shade, so no separate hover token is proposed.

**button-secondary** — The source CSS shows `.btn--secondary` sharing the identical black-on-white styling as primary. To give the system a usable hierarchy, a bordered variant (hairline outline, same ink background) is proposed here as a design extension; this divergence from the literal source is intentional and labeled proposed.

**text-input** — Not directly observed in the supplied rules; proposed as a white field with a light hairline border and standard body typography, consistent with the theme's flat, low-radius visual language.

**nav-bar** — Inferred from `.mobile-nav__item a` styles: dark body-colored links on a white bar, with a light-gray (#f2f2f2) hover/focus background matching the observed mobile navigation and drawer-close interactions. Desktop nav layout was not present in the evidence and is treated as proposed.

**product-card** — Draws on the `.product-recommened` background (#e3e3e3) and its `#3e3e3e` info text, reused here as a general card surface for product tiles, with muted gray for secondary specs (weight/height info) as seen in the source selectors.

**hero** — Proposed section using the display-xl token; no hero-specific CSS was supplied, so typography scale and spacing are proposed rather than measured.

**footer** — Proposed light-surface footer using `surface-soft` (#f6f6f6, an observed disabled/background gray) with body-sm text and hairline dividers; footer-specific rules were not present in the evidence.

**badge** — Proposed sale/status indicator using the observed `#d02e2e` red on white, pill-shaped; exact badge styling and the cart-indicator's original orange dot color were not confirmed against the supplied palette, so this token substitutes the closest observed red.

**search** — Proposed light input field consistent with the theme's flat, hairline-bordered form control pattern; no dedicated search-bar CSS was supplied.

**product-recommended-panel** — A category-specific component reflecting the observed `.product-recommened` block used for chair specs (height/weight info), styled with the `surface-alt` background and muted secondary text directly evidenced in the source.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile up to 599px, tablet 600–959px, desktop 960px+. Touch targets should be a minimum 44×44px, with the mobile navigation collapsing into the drawer/toggle pattern implied by `.mobile-nav__toggle` and `.drawer__close` selectors. Product-card grids are recommended to reflow from a single column on mobile to 3–4 columns on desktop. This section is a proposed convention only; no actual responsive layout or media-query behavior was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from a static CSS/selector sample and a title string, not a rendered or interactive audit of vertagear.com. Several palette entries (e.g., #4e4cf7, #d02e2e, #f26c4f) appear in the observed color list but their functional role (link, alert, accent) could not be confirmed against a specific selector, so their mapping here is inferred. The cart-indicator's true color (#f68e56, seen in one rule) fell outside the supplied palette array and was therefore not used; a nearby observed red/orange was substituted instead. Font names Oxanium, TeXGyreAdventor, and ProximaNovaLight appear in the raw font-family list but were not attached to any selector in the evidence, so their proposed use (e.g., display-xl) is speculative and unverified; licensing/availability of any non-Poppins face is unconfirmed. All component padding, radii beyond the flat 0px button, hover/focus colors outside those explicitly shown, and all responsive/mobile interaction behavior are proposed design conventions, not observed measurements.
