---
version: alpha
name: "Yakima"
source_url: "https://yakima.com"
captured_at: "2026-09-28T04:29:14.092266+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Evidence points to a utilitarian, high-contrast outdoor-gear system built on black, white, and a small set
  of grays, with red used sparingly as an accent. Observed hex values include a strong near-black (#000000)
  confirmed as the add-to-cart hover background, a mid-dark gray (#1f1f1f-adjacent, represented here by
  #202020/#231f20) for default button states, and a slate-navy (#1f292e) used for the mobile navigation
  panel background. Reds (#ab2328, #d20000, #fa363a, #811a1e) appear across the palette but their exact
  UI role is inferred rather than confirmed; here #ab2328 is treated as an accent for sale/highlight
  moments, a common role for a secondary brand red in outdoor retail. Judge.me review variables confirm
  black as the primary interactive color and a 0px border-radius preference for that widget.
  Typography evidence is strong for "Mark OT" as the button/UI font family (declared with !important on
  the add-to-cart control), while "Yakima Hand" is treated as an inferred display font for hero headlines
  given its brand-specific naming. "Work Sans" is inferred as the general body/reading font, a common
  Shopify-theme pairing alongside Helvetica Neue/Arial fallbacks. The overall proposed interpretation is a
  rugged, functional interface: black CTAs, light neutral surfaces, restrained red accenting, and generous
  whitespace suited to product photography of racks and outdoor accessories.

colors:
  primary: "#000000"
  accent: "#ab2328"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#717171"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#1f292e"
  success: "#1f873d"
  danger: "#d20000"
  info: "#2673bf"
  border-subtle: "#e8e9eb"
typography:
  display-xl: {fontFamily: "'Yakima Hand', sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Mark OT', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Mark OT', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Work Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Work Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Work Sans', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "'Mark OT', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    hoverBackgroundColor: "{colors.ink}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    mobileBackgroundColor: "{colors.surface-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fit-finder:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses a black background matching the observed add-to-cart hover state, with white text set in the "Mark OT" button typography confirmed in the source CSS. Default and hover backgrounds are both dark, differentiated by the ink token; a proposed focus ring is not observed and should be validated.

**button-secondary** is a white/outline treatment for lower-emphasis actions such as "View details" or "Compare," using the hairline gray border. Hover and active states are proposed, not observed.

**text-input** models a light-bordered field for search, newsletter, and account forms. Border color draws from the light hairline gray family seen across the palette; focus-state border color is proposed as the accent red but unverified.

**nav-bar** reflects the observed transparent site-header background with white icon/text color (`#fff` on search icon and mobile toggle), and a dark slate mobile panel background (`#1f292e`) taken directly from the mobile-nav CSS rule. Desktop dropdown styling is inferred.

**product-card** is a proposed pattern for the exterior-accessories catalog (racks, carriers, tie-downs), using a plain white surface and subtle border, since no direct product-card CSS was supplied.

**hero** proposes a dark, full-bleed banner treatment for category or campaign imagery, using the ink-dark surface with white display type in the inferred "Yakima Hand" headline font. This is a stylistic proposal, not a captured layout.

**footer** mirrors the dark surface treatment for site-wide closing content, with smaller body typography for links and legal text; column structure is not observed and is proposed only.

**badge** represents sale/notification chips (e.g., "New," "Sale") using the accent red with white text and a fully rounded shape, consistent with the small circular badge selectors seen in the discount-widget CSS (`limoniapps-trigger-button-badge`).

**search** is a proposed compact input/icon combination for the header, based on the confirmed white search-icon color; exact field width and expanded-state behavior were not observed.

**fit-finder** is a category-appropriate proposed component for an exterior-accessories retailer: a vehicle/rack compatibility selector styled with the soft surface gray and accent-red highlight for the active step, since Yakima's core commerce need is helping shoppers find compatible rack fits. No direct evidence of this tool's markup was supplied.

## Responsive Behavior

The following breakpoint table is a **recommendation only**, not a measured observation of the live site:

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column, collapsed nav to slide-out panel (`#1f292e` background as observed for mobile nav) |
| Tablet | 600–1023px | Two-column product grids, condensed header |
| Desktop | 1024–1439px | Full nav bar, multi-column grids |
| Wide | 1440px+ | Max-width content container, larger hero type |

Touch targets should be a minimum 44×44px for primary buttons and nav toggles. The mobile nav should collapse behind a hamburger control (an open-state class, `js-nav-open`, was observed, confirming a slide/toggle pattern exists, though its exact animation and breakpoint trigger were not captured).

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/JS evidence only; no rendered page, computed layout, or interaction states were observed. Several color-role assignments (e.g., which reds map to "sale" versus "error" versus decorative accent) are inferred from convention, not confirmed usage. Font sizes, weights, and line-heights in the typography table are proposed defaults since no explicit `font-size` values were present in the supplied CSS beyond family declarations. Component states such as hover, focus, active, and disabled are largely proposed and unverified except where a hover rule was explicitly supplied (button-atc hover to black). Mobile menu behavior, breakpoints, and responsive grid structure were not observed and are recommendations only. Availability and licensing of "Mark OT" and "Yakima Hand" as custom/commercial fonts have not been verified; system fallbacks (`sans-serif`) should be used until confirmed.
