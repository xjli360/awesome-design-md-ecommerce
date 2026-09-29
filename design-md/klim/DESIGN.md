---
version: alpha
name: "Klim"
source_url: "https://klim.com"
captured_at: "2026-09-28T09:44:31.005279+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Klim's storefront CSS shows a stark, high-contrast performance-gear aesthetic: pure black (#000000) and white (#ffffff) carry primary actions and inverse states, with a tight family of light grays (#ebebeb, #f9f9f9, #f5f5f5, #e2e2e2) forming soft surfaces and hairlines against a white canvas. Headings, titles, and the .button/.title selector group are set in "Industry Ultra" with "Cabin" and sans-serif fallbacks, a condensed, technical display face suited to a motorsport/outdoor-gear brand. Interactive controls (native buttons, inputs) instead resolve to Roboto at font-weight 500, so body copy and button labels are treated here as an inferred Roboto role, while Industry Ultra/Bold is reserved for display and heading roles. All observed buttons use border-radius:0, so the design system's "none" radius token is treated as the default for interactive shapes, a deliberate squared-off, utilitarian look. A small set of saturated accents (#d32d2d red, #f6a529 orange, #108043 green) appear in the palette and are inferred as status/badge colors (sale, warning, in-stock) rather than confirmed UI roles, since no selector evidence ties them to specific components. Layout metrics (grid, breakpoints, spacing rhythm) are not present in the supplied CSS and are proposed defaults only.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#737373"
  hairline: "#e2e2e2"
  surface-soft: "#f9f9f9"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  border-strong: "#bfbfbf"
  accent-red: "#d32d2d"
  accent-orange: "#f6a529"
  accent-green: "#108043"
  tertiary-bg: "#ebebeb"
typography:
  display-xl: {fontFamily: "'Industry Ultra', 'Cabin', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Industry Ultra', 'Cabin', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Industry Bold', 'Cabin', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1em, letterSpacing: 0px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  button-tertiary:
    backgroundColor: "{colors.tertiary-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "{colors.border-strong}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  gallery-viewer:
    backgroundColor: "{colors.tertiary-bg}"
    iconColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs}"

## Components
**button-primary** mirrors the observed `.btn.btn--primary` rule: solid black fill, white text, zero border-radius, and a hover state that inverts to white-on-black (proposed transition timing follows the 0.1s observed elsewhere). **button-secondary** reflects `.btn.btn--secondary`: white fill with black border/text, inverting to black on hover/active as coded. **button-tertiary** matches the light-gray `.btn.btn--tertiary` treatment used for lower-emphasis actions, with a smaller caption-scale label. **text-input** is proposed by extension of the button border/radius language, since no dedicated input-field selector was supplied; hairline border and zero radius are inferred for visual consistency. **nav-bar** is a proposed container for the multi-level mega-menu implied by the extensive category text (Snow, Motorcycle, SxS, Everyday); no header layout or scroll behavior was observed. **product-card** is proposed for PLP/PDP listings, using the surface-hairline pairing seen in card-style modal selectors (`store-availabilities-modal`). **hero** is proposed from the `.testimonial__button-wrapper` full-bleed image pattern (`--full-url` background-image variable), suggesting large dark-overlay banner sections. **footer** is a proposed dark-mode inversion consistent with the black/white contrast system; no footer selector was directly supplied. **badge** is inferred from the accent-orange/red/green palette entries, proposed for "New," "Sale," or "In Stock" labels common to gear retail, not confirmed by selector evidence. **search** is proposed using the soft-surface tone family (`#f9f9f9`, `#ebebeb`) seen in gallery/modal chrome. **gallery-viewer** directly reflects the observed `.gallery-viewer__button` rule (gray background, black icon, zero radius, 8px padding), a category-appropriate component for zoomable product photography of moto/snow gear.

## Responsive Behavior
Proposed breakpoint table (not measured from live site):

| Breakpoint | Width      | Notes (proposed) |
|---|---|---|
| Mobile     | <768px    | Single-column nav collapses to hamburger; mega-menu becomes accordion |
| Tablet     | 768–1023px| 2-column product grid; sticky search icon-only |
| Desktop    | 1024–1439px| Full mega-menu with country/currency selector visible |
| Wide       | ≥1440px   | 3–4 column product grid; hero at full section height |

Touch targets should meet a 44px minimum (buttons currently show 8–14px vertical padding plus border, which is likely below this on mobile and would need proposed enlargement). Mega-menu collapse behavior for the long Snow/Motorcycle/SxS/Everyday hierarchy is not observed and should be validated against live interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS/text extraction only; no rendered layout, computed grid, JavaScript-driven interaction, or actual mobile viewport was observed. Font-size, line-height, and letter-spacing values for headings (display-xl/md, title-md) are proposed estimates, not measured, since only button/input font-size (16px, 13px) appeared in the evidence. The apparent conflict between the `.button` selector under the Industry Ultra heading-font rule and the later `.button,.btn,button{font-family:Roboto}` rule could not be resolved from static specificity alone; Roboto was assumed for interactive button-md based on the more specific, button-scoped declaration. Accent colors (red/orange/green) are inferred as status/badge roles from common retail convention, not confirmed by any supplied selector tying them to sale/stock states. Spacing scale and section rhythm are proposed conventions, not extracted from layout CSS. Availability, licensing, and web-font loading for "Industry," "Industry Bold," and "Industry Ultra" were not verified and may require confirmation before implementation.
