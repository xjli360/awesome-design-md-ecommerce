---
version: alpha
name: "Lloyd Mats"
source_url: "https://lloydmats.com"
captured_at: "2026-09-28T10:00:50.583653+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lloyd Mats Store runs on a Magento/Luma-derived storefront, evidenced by class patterns like `.abs-action-link-button`, `luma-icons`, and Bootstrap-style alert classes (`.alert-success`, `.alert-danger`). The observed palette is a standard Luma default set: neutral grays (#ffffff, #333333, #cccccc, #dddddd, #f5f5f5) carry body text and surfaces, while #1979c3 and #006bb4 appear as the theme's blue action/link colors — here interpreted (inferred) as the brand primary, since no vehicle-specific brand color was distinguishable in the evidence. #ff5501/#ff5216 orange values are treated as an accent for promotional or CTA emphasis, and the Bootstrap alert quartet (#5cb85c/#3c763d success, #d9534f/#a94442 danger, #f0ad4e/#8a6d3b warning, #5bc0de/#31708f info) is retained for system messaging. Typography is Open Sans with Helvetica Neue/Helvetica/Arial/sans-serif fallback, per `body` and heading rules; no display or brand-specific webfont was observed. Given the category — made-to-order automotive floor mats sold by vehicle fitment — the interpretation favors a utilitarian, catalog-dense layout: clear hairlines, muted grays for secondary UI (filters, breadcrumbs, vehicle pickers), and the blue/orange pair reserved for primary actions and configurator highlights. All spacing, radius, and most component states are proposed, not measured.

colors:
  primary: "#1979c3"
  primary-dark: "#006bb4"
  accent: "#ff5501"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  border-strong: "#a6a7ab"
  link: "#337ab7"
  link-hover: "#286090"
  success: "#3c763d"
  success-bg: "#dff0d8"
  danger: "#a94442"
  danger-bg: "#f2dede"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  info: "#31708f"
  info-bg: "#d9edf7"
typography:
  display-xl: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.42857143, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.6rem, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.accent}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.body-sm}"
    activeStateColor: "{colors.primary}"

## Components

**button-primary** is proposed for primary calls to action (Add to Cart, Configure Mats), using the theme's blue as background per the observed `#1979c3`/`#006bb4` action-link pattern; hover/active darkening to `primary-dark` is proposed, not measured.

**button-secondary** mirrors the observed native `button` rule (`background:#eeeeee; border:1px solid #cccccc; color:#333333`) for lower-emphasis actions like filters or "Compare," with hover/focus states (`#e1e1e1`/`#e2e2e2`) taken directly from CSS.

**text-input** is a proposed generic form field style using the observed hairline gray border and body font, intended for search, account, and configurator fields; no dedicated input CSS was supplied.

**nav-bar** reflects the header structure implied by `.nav-sections .header.links .minicart-wrapper` selectors (Sign In, Cart, category menu); background and hairline are inferred from the neutral canvas/border palette, not directly observed layout metrics.

**product-card** is proposed for the vehicle/category grid (e.g., "CAMARO FLOOR MATS," "CORVETTE FLOOR MATS") implied by the navigation text; card border and radius are proposed defaults, with price optionally using the accent orange for emphasis.

**hero** is a proposed banner treatment for the homepage's "Factory-Direct Custom Fit" messaging referenced in the text excerpt; no hero-specific CSS was in evidence, so background/typography choices are inferred from general surface and heading rules.

**footer** is proposed from the excerpt's link list (Shipping, Tracking, Returns, Privacy, Terms, FAQs, Contact Us) and uses muted text on a soft surface, consistent with typical Luma footer conventions; exact footer CSS was not supplied.

**badge** is proposed for "Made In America" or "Employee Owned" trust markers and sale flags, using the accent orange observed in the palette (`#ff5501`) for visibility against neutral surfaces.

**search** is proposed for a header search field, styled consistently with text-input; no search-bar CSS was present in evidence.

**vehicle-fitment-selector** is a category-appropriate, proposed component representing the make/model/year picker implied by extensive vehicle-specific navigation (Acura, Chevy, Honda Civic/Accord, Jeep, etc.); it uses the card surface and primary color for the active selection state, though no configurator markup was observed.

## Responsive Behavior

Proposed breakpoint table (not measured from live site):

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | 0–599px | Single-column product grid, collapsed nav behind toggle (`Toggle Nav` text observed in header markup) |
| tablet | 600–1023px | 2-column product grid, condensed vehicle-selector |
| desktop | 1024–1439px | Full nav bar, multi-column category grid |
| wide | 1440px+ | Max-width content container, generous section spacing |

Touch targets should be minimum 44×44px for buttons and nav toggles. The header's "Toggle Nav" text suggests a collapsible mobile menu, but its exact collapse behavior, breakpoint, and animation were not observed. All values above are recommendations only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed styles, or DOM screenshots were available. Color-to-role mapping (e.g., primary vs. link vs. accent) is inferred from common Luma/Bootstrap theme conventions and may not reflect actual brand intent. Spacing and radius scales are proposed defaults, not measured from the site. No proprietary or licensed font was observed — Open Sans with system fallbacks is used as-is, and its licensing/self-hosting status was not verified. Interaction states (hover/focus/active) are only confirmed for native `button` elements; all other component states are proposed. Mobile/responsive layout behavior, breakpoints, and touch interactions were not observed and are estimated. The vehicle-fitment-selector component is a category-informed inference with no corresponding CSS evidence supplied.
