---
version: alpha
name: "Enkei Wheels"
source_url: "https://enkei.com"
captured_at: "2026-09-28T10:00:22.795155+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Enkei's public site runs on a WordPress/Divi stack, and the extracted CSS shows a restrained, utilitarian palette rather than a bold automotive brand system. Body copy renders in Open Sans (Arial, sans-serif fallback) at 14px, medium weight, with a loose 1.7em line-height typical of Divi's default theme styles. Headings (h1-h6) stay in the same body font family but shift to a darker ink (#333333) at weight 500, with no distinct display typeface confirmed. The one clear accent is a bright link/hover blue (#2ea3f2), used for search icons, social hovers, and light-background button text — this is treated as the primary brand accent. A secondary deeper blue (#006799) appears in the palette and is inferred as a hover/pressed variant. Buttons observed via `.et_pb_button` use a 2px bordered, transparent-fill pattern with a dark slate fallback background (#32373c) for `.wp-element-button`, suggesting two coexisting button conventions (Divi module buttons vs. block-editor buttons). Neutral grays (#eeeeee, #f4f4f4, #dddddd, #f7f7f7, #fafafa) are common Divi framework fills and are mapped here as inferred surface/hairline tokens, not confirmed from live layout screenshots. No proprietary racing/motorsport typeface or color system was detected in the evidence.

colors:
  primary: "#2ea3f2"
  secondary: "#006799"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  dark-surface: "#32373c"
  border-light: "#e5e5e5"
typography:
  display-xl: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6em, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary** is proposed as the primary call-to-action treatment (e.g. "Find a Dealer", "Read Press Release"), using the observed accent blue as fill; this exact fill-button pattern was not directly observed, since the CSS only shows a bordered/transparent `.et_pb_button` style and a dark solid `.wp-element-button` style. **button-secondary** mirrors the bordered convention seen in `.et_pb_button` (2px border, transparent background, color transition on hover) and is a closer match to observed markup. **text-input** is proposed for dealer-locator or search fields; no input-specific styling was present in the evidence, so padding and border are inferred from general theme neutrals. **nav-bar** reflects the site's flat top navigation (Wheels, Racing, Drivers, News, Merch, Downloads, Find a Dealer) implied by page text, styled with the light canvas background and blue hover state confirmed in CSS (`#et_search_icon:hover` etc.). **product-card** is proposed for wheel-style listings (Racing Series, Tuning Series, etc.) using the light gray surface-card fill common to Divi grids; card structure itself is not confirmed from layout evidence. **hero** is proposed for the homepage banner ("High Quality Wheels" / McLaren press release), using the dark slate surface as an inferred dramatic background suited to automotive imagery, though the live hero background was not captured in CSS. **footer** uses the same dark surface for a grounded, workshop-like close to the page, consistent with copyright/legal text seen at the bottom of the excerpt. **badge** is proposed for labeling new wheel styles or "2024" release callouts, using the accent blue as a small pill treatment; unobserved but stylistically consistent with the accent's existing hover/link role. **search** reflects the confirmed `#et_search_icon:hover` selector, styled with the accent blue icon and light neutral field. **fitment-selector** is a category-appropriate proposed component for wheel/tire fitment lookup (size, bolt pattern, offset), not evidenced in the CSS but recommended given the product category and existing neutral surface tokens.

## Responsive Behavior
This is a recommendation, not measured site behavior; no media queries or breakpoint values were present in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column stacking, nav collapses to a toggled menu |
| Tablet | 480–980px | Two-column product grids; hero text scales down from display-xl to display-md |
| Desktop | 980–1280px | Matches the theme's `--wp--style--global--content-size: 823px` and `wide-size: 1080px` container constraints |
| Wide | > 1280px | Content remains capped at the wide-size container with generous side margins |

Touch targets should be at least 44px tall for nav links and buttons; the observed button padding (`0.667em`/`1.333em`) roughly supports this at body font sizes but was not verified against rendered pixel heights. Mobile nav collapse behavior (hamburger menu, dropdown mechanics) was not observed and is a standard proposed pattern only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS and page-text extraction only; no rendered screenshots, computed styles, or interaction states (hover/focus/active, form validation, mobile menu behavior) were observed. The font list includes several families (Lato, Montserrat, Roboto, Lucida, Courier New, FontAwesome, ETmodules) that appear in the raw evidence but are not tied to confirmed selectors for body or heading text; only Open Sans/Arial/sans-serif is used here as the confirmed base stack. Many supplied hex values match default WordPress block-editor and Divi framework palettes rather than confirmed brand-specific accents; only colors tied to actual selectors (`#2ea3f2` links/hovers, `#333` headings, `#666` body, `#32373c` buttons, `#fff` background) are treated as reliably observed, while neutral grays used for surfaces/hairlines are inferred common-framework fills. All typography sizes beyond the confirmed 14px body and 20px button text are proposed, not measured. Font licensing/availability for Open Sans (Google Fonts, generally open-licensed) was not independently verified against Enkei's actual font-loading method. Component visual details (card shadows, exact spacing, grid columns) are proposed conventions suited to a wheels/tires storefront, not confirmed layout observations.
