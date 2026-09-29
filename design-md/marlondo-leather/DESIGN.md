---
version: alpha
name: "Marlondo Leather"
source_url: "https://marlondoleather.com"
captured_at: "2026-09-28T10:08:03.777372+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Marlondo Leather's observed CSS shows a restrained, utilitarian retail system built on Open Sans for body copy (15px/1.6, color #585858) and Montserrat (700 weight) for headings and buttons, both falling back to Helvetica Neue/sans-serif. The measured interaction chain on `.btn` — base state unspecified in evidence, hover `#20585d`, active `#19464a` — establishes a dark teal family as the functional accent; `#266a70` from the same palette cluster is inferred here as the resting primary brand color since no unhovered button background was captured. Secondary buttons use a neutral gray ramp (`#dcdcdc` → `#cfcfcf` → `#c3c3c3`), and disabled states use `#f6f6f6`/`#b6b6b6`. Header and cart chrome sit on off-white surfaces (`#f2f2f2`, `#e5e5e5`) against a white canvas, with heading text at `#333` and body copy at `#585858`. A cluster of warm brown tones (`#8d5f3d`, `#6a472e`, `#9f6b45`) appears in the palette and is treated as an inferred leather-material accent for imagery framing and material swatches, not confirmed as a UI color. This interpretation extends the observed 2px button radius and teal/neutral system into a full component library for a duffel-bag-focused storefront, flagging all unmeasured values as proposed.

colors:
  primary: "#266a70"
  primary-hover: "#20585d"
  primary-active: "#19464a"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#585858"
  muted: "#999999"
  hairline: "#e5e5e5"
  surface-soft: "#f2f2f2"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  secondary-bg: "#dcdcdc"
  secondary-bg-hover: "#cfcfcf"
  secondary-bg-active: "#c3c3c3"
  disabled-bg: "#f6f6f6"
  disabled-text: "#b6b6b6"
  accent-leather: "#8d5f3d"
  danger: "#dc0000"
  success: "#0a942a"
typography:
  display-xl: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, HelveticaNeue, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.42, letterSpacing: 0.5px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
    hover: {backgroundColor: "{colors.primary-hover}"}
    active: {backgroundColor: "{colors.primary-active}"}
  button-secondary:
    backgroundColor: "{colors.secondary-bg}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
    hover: {backgroundColor: "{colors.secondary-bg-hover}"}
    active: {backgroundColor: "{colors.secondary-bg-active}"}
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  duffel-spec-panel:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.accent-leather}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components
**button-primary** applies the observed hover/active teal ramp (`#20585d`, `#19464a`) to a resting state inferred as `{colors.primary}`, since the CSS evidence only captured `.btn` interaction states, not the base background. Uppercase Montserrat text (observed in `.btn` rules) is retained as proposed styling.

**button-secondary** mirrors the observed `.btn-secondary` gray progression (`#dcdcdc` → `#cfcfcf` → `#c3c3c3`) exactly as measured, making it the most evidence-grounded component in the set.

**text-input** is proposed from general Shopify-theme conventions paired with the observed hairline gray (`#e5e5e5`) and body typography; no explicit input border-color rule was present in evidence.

**nav-bar** reflects the observed `.site-header` white background and `#585858` link color; spacing and layout are proposed since no measured breakpoint or height was in evidence.

**product-card** is proposed to house the many SKU listings (briefcases, duffels, wallets) implied by the page text; card surface and border colors are drawn from the neutral palette, not directly observed on a card selector.

**hero** is a proposed landing element using the soft surface tone (`#f2f2f2`) and the Montserrat display scale for a category headline (e.g., "Leather Travel Gear").

**footer** is inferred to use a dark ink background for contrast with the site's link-heavy footer content ("Quick Links", social icons); no footer background color was directly captured in evidence.

**badge** is proposed for "Sold Out" / "Save $X" labels seen in the page text, using the observed red (`#dc0000`) as a plausible sale/alert color.

**search** reuses the observed `.search-bar` text color (`#585858`) and the `#f2f2f2` surface tone from the cart button for visual consistency; exact search-bar background was not captured.

**duffel-spec-panel** is a category-specific proposed component for displaying duffel bag dimensions/material (e.g., Weekender Duffle, Zipper Top Duffle), using the inferred leather-brown accent to tie material callouts to the product's craft narrative.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Nav | Product Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger | 1 column |
| Tablet | 600–1024px | Condensed text links | 2 columns |
| Desktop | >1024px | Full text-link nav (as in `.site-header--text-links`) | 3–4 columns |

Touch targets for `.btn`/`.header-cart-btn` should maintain a minimum 44px tap height; the observed `padding:8px 20px` on buttons likely needs vertical padding increases on touch devices. Category flyouts ("More leather briefcases ›") should collapse into accordions below tablet width. None of this responsive behavior was directly observed in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or DOM screenshots were available. The resting (non-hover) background of `.btn` was never captured, so `{colors.primary}` is an inferred value from the surrounding teal cluster, not a directly observed rule. Brown/leather tones (`#8d5f3d`, `#6a472e`, etc.) appear in the palette but their actual UI usage (swatches, imagery overlays, or unrelated icon assets) is unconfirmed. All spacing, rounded, and breakpoint values beyond the two directly observed (`border-radius:2px`, `padding:8px 20px`) are proposed conventions, not measurements. Montserrat and Open Sans are used as declared font-family values only; no confirmation of licensing, self-hosting, or web-font-loading behavior was available. Mobile menu behavior, hover/focus states beyond `.btn`/`.btn-secondary`/`.header-cart-btn`, and any JavaScript-driven interactions (cart drawer, ajaxify behavior referenced in filenames) were not observed or verified.
