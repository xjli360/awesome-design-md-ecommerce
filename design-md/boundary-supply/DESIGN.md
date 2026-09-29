---
version: alpha
name: "Boundary Supply"
source_url: "https://boundarysupply.com"
captured_at: "2026-09-29T04:14:00.801091+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Boundary Supply's storefront CSS evidence shows a high-contrast, utilitarian palette built on near-black (#121212, #000000) and white (#ffffff), with a warm amber accent (#fdc656) used consistently as the primary call-to-action color on hero and collection buttons. Supporting neutrals (#f5f5f5, #dedede, #efefef, #acacac, #555555) suggest a light canvas with soft card and hairline surfaces, appropriate for a technical outdoor/EDC gear brand. Typography is declared site-wide as "Univers LT Pro" for both headings and body paragraphs via CSS custom properties, giving a clean, condensed-adjacent industrial voice; "Univers LT Pro Condensed" is also loaded and is inferred here for compact labels/badges, though its applied selector was not captured. Other font families present in the asset list (Assistant, Instrument Sans, Inter, Josefin Sans, Roboto) are not tied to any captured selector and are treated as unused/unverified for primary UI roles.

  Button geometry is fully pill-shaped (border-radius: 100px) with a hover-state color inversion pattern (amber-to-ink swap) repeated across hero, collection, and text-block buttons. Card and product corner-radius custom properties (10px) were observed in root variables, informing the rounded-md token. Spacing, breakpoints, and non-button component visuals below are proposed conventions for a modular-backpack e-commerce layout and are explicitly marked inferred.

colors:
  primary: "#fdc656"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#434343"
  muted: "#acacac"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f7f7"
  on-primary: "#121212"
  overlay-scrim: "#00000033"
  overlay-strong: "#00000066"
  border-dark: "#000000"
  text-hover: "#555555"
typography:
  display-xl: {fontFamily: "'Univers LT Pro', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Univers LT Pro', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "'Univers LT Pro', sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'Univers LT Pro', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Univers LT Pro', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Univers LT Pro Condensed', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Univers LT Pro', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.0, letterSpacing: "0px"}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 10px
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
    rounded: "{rounded.full}"
    padding: "{spacing.base} {spacing.xl}"
    border: "1px solid {colors.ink}"
    hover:
      backgroundColor: "{colors.ink}"
      textColor: "{colors.primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.canvas}"
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focusBorder: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    hoverShadow: "0 4px 16px {colors.overlay-scrim}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    overlay: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  modular-config-panel:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    optionTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    selectedState:
      border: "2px solid {colors.primary}"

## Components
**button-primary** is the dominant CTA pattern directly observed across hero and collection buttons: a pill shape (100px radius), bold 16px type, amber fill with ink border, inverting to ink fill with amber text on hover — this inversion is an observed CSS `:hover` rule, not a live-interaction confirmation.

**button-secondary** is inferred for outline CTAs used on darker hero backgrounds (observed white-border/transparent-fill pattern from the collection-button selector), inverting to the primary amber on hover.

**text-input** is a proposed pattern for search, newsletter, and account forms; no input CSS was captured, so border, radius, and focus styling are inferred from the site's general hairline/ink conventions.

**nav-bar** is proposed based on the presence of a multi-level "Shop All / About / More" menu structure in page text; visual styling (background, hairline) is inferred from the neutral palette, not measured.

**product-card** is proposed for the backpack/module grid implied by "Rennen + Aux Compartment," "Errant + Stasis Pro," etc.; the 10px corner-radius is grounded in the observed `--card-corner-radius: 10px` root variable.

**hero** reflects the observed full-bleed promotional banner pattern ("CARRY AUTHENTICALLY YOU / EXPLORE NOW") with dark background and button-primary CTA; exact hero dimensions were not captured.

**footer** is proposed as a dark, muted-text band consistent with the ink/muted palette; no footer-specific selectors were supplied.

**badge** is proposed for labels like "New" or shipping-threshold banners ("Free Express 3-Day Shipping"), using the amber accent for visibility.

**search** is proposed for the account/cart header utilities implied by "Account / Orders / Profile" text; no search-input CSS was observed.

**modular-config-panel** is a category-specific proposed component representing the site's described modular bag-building UI (module combinations like "Rennen Pro + EXM"), styled with the observed primary-color selection border convention.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤480px, tablet 481–1024px, desktop ≥1025px. Nav collapses to a hamburger/drawer below 1024px; hero CTAs stack vertically below 480px. Touch targets for buttons should maintain a minimum 44px height, consistent with the observed 16px/32px button padding scaling up on touch devices. This section is a design recommendation, not an observation of live responsive markup or breakpoints.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no live DOM, computed styles, or rendered screenshots were reviewed. Color-role assignments (e.g., which neutral serves as body vs. muted vs. hairline) are inferred from value groupings, not confirmed usage sites. Font-family fallbacks are limited strictly to generic `sans-serif` because no specific fallback typefaces (e.g., Helvetica, Arial) appeared in the supplied font_families evidence. Typography sizes beyond what root variables implied are proposed, not measured. Interaction states beyond the two captured `:hover` button rules (nav dropdowns, form focus, mobile menu) were not observed. Availability, licensing, and web-font-loading status of "Univers LT Pro" / "Univers LT Pro Condensed" were not verified. The modular-config-panel component is a category-appropriate proposal inferred from repeated marketing copy, not from captured UI markup.
