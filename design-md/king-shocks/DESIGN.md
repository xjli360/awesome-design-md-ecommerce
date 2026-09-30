---
version: alpha
name: "King Shocks"
source_url: "https://kingshocks.com"
captured_at: "2026-09-28T09:24:54.037398+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  King Shocks' storefront evidence is dominated by a legacy cart/catalog module (wsm_base.css) built on a dark, utilitarian palette: near-black headers (#333, #3d3d3d, #111), white canvas, and a single explicit accent, #005cb8, applied to the site search button. Bootstrap-style contextual colors (success #5cb85c, warning #f0ad4e, danger #d9534f, info #5bc0de) appear throughout the swatch list, consistent with form validation and alert states rather than brand identity. A recurring red family (#cc0000, #dd0000, #cd0a0a, #990000, #ed2424) is present but its role is not confirmed by any supplied selector, so it is treated here as an inferred accent suited to a racing/performance brand rather than a proven primary.

  This interpretation keeps #005cb8 as the sole verified interactive color, reserves the red family for secondary emphasis (badges, alerts, limited CTAs), and builds structure from the dark #333/#3d3d3d header tones already used for navigation and panel headers in the evidence. Typography draws on the observed font stack: Montserrat is assigned to display/heading roles and Open Sans to body copy as an inferred pairing, since the CSS confirms both families exist in the font list but does not confirm their applied roles; Verdana/Arial/Helvetica remain as the legacy cart module's confirmed fallback stack. Layout, spacing, and component states below are proposed conventions for a vehicle-fitment parts catalog, not measured observations.

colors:
  primary: "#005cb8"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-surface: "#333333"
  darker-surface: "#3d3d3d"
  accent-red: "#cc0000"
  danger: "#d9534f"
  success: "#5cb85c"
  warning: "#f0ad4e"
  info: "#5bc0de"
typography:
  display-xl: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.darker-surface}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.body-sm}"
    actionTypography: "{typography.button-md}"

## Components

**button-primary** uses the one CSS-confirmed accent, `#005cb8`, matching the `.Sui-SearchBar--search-button` rule found in evidence; this is proposed as the primary call-to-action treatment across "Learn More," "Add to Quote," and checkout actions.

**button-secondary** is a proposed outline variant for lower-priority actions (e.g. "View Details") that keeps the same accent color without competing visually with primary actions; no outline button was directly observed.

**text-input** follows the `#eee`-bordered, white-background pattern seen in `.wsm_cart_total_wrapper` styling, extended here (inferred) to vehicle-year/model dropdowns and quote-form fields.

**nav-bar** is modeled on the dark header treatment confirmed in `.wsm_header`, `#wsm_table div#header`, and `ul.wsmdt_left_menu li.menu_header` (`#333`/`#3d3d3d` backgrounds, white text); proposed for the main site navigation and mega-menu categories (OEM Performance, Off-Road, UTV, Springs).

**product-card** is a proposed container for featured-product tiles (e.g. the 4Runner coilover, sway-bar-link listings) using the neutral hairline and card-surface tokens; no card-specific selector was present in evidence.

**hero** is a proposed full-width banner treatment reusing the dark-surface/on-primary pairing for the homepage's King of the Hammers narrative section; exact hero markup was not present in the supplied CSS.

**footer** is proposed using the darkest observed neutral (`ink`) for a closing brand band; footer-specific selectors were not included in evidence.

**badge** repurposes the red family (`#cc0000`) as an inferred "New," "Excludes Overtrail," or fitment-alert label, since red values exist in the palette without a confirmed selector role.

**search** directly reflects the observed `.Sui-SearchBar--search-button` rule (`background-color:#005cb8 !important; color:#fff !important`) and is the single most evidence-backed component in this spec.

**vehicle-fitment-selector** is a category-appropriate proposed component for the "Find Parts For Your Vehicle" flow referenced in the page text, using the soft-surface background to visually separate the fitment tool from surrounding content; no fitment-widget CSS was supplied.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <640px | Single-column product grid; nav collapses to a hamburger/off-canvas menu; fitment selector stacks vertically. |
| tablet | 640–1024px | Two-column product grid; mega-menu may condense to accordion categories. |
| desktop | 1024–1440px | Full mega-menu nav-bar; multi-column featured-product grid. |
| wide | >1440px | Max-width content container with increased section padding (`{spacing.section}`). |

Touch targets should be a minimum of 44px, with `button-primary`/`search` padding (`{spacing.md} {spacing.lg}`) satisfying this at desktop scale but requiring vertical padding increases on touch devices. Mega-menu categories (OEM Performance, Off-Road, UTV brand sub-lists) should collapse into an accordion pattern below `tablet`. This table is a design recommendation only; no live responsive behavior was observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This spec is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were captured. The dominant color evidence comes from a legacy cart module (`wsm_base.css`) and Bootstrap-style contextual colors (success/warning/danger/info), so their applied role on the live marketing pages is inferred, not confirmed. Only `#005cb8` (search button) has a direct, unambiguous selector-to-color mapping; all other role assignments (primary vs. accent, dark-surface usage, red badge usage) are best-effort inferences from a large, mixed swatch list. Font-role assignment (Montserrat for display, Open Sans for body) is inferred from a shared font-family list without confirming which selectors use which family; Verdana/Arial/Helvetica are the only families with confirmed selector usage, in the cart module. No hover, focus, active, error, or disabled states were observed. Mobile/tablet layout, breakpoints, spacing scale, and corner-radius values are proposed conventions, not measured from the site. Availability and licensing of Montserrat/Open Sans/Lato for production use were not verified.
