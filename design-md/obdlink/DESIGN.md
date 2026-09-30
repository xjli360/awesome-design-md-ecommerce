---
version: alpha
name: "OBDLink"
source_url: "https://obdlink.com"
captured_at: "2026-09-29T04:04:26.006516+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  OBDLink's storefront evidence centers on a WordPress/Gutenberg-based theme with a
  restrained, technical palette rather than an expressive brand system. The only
  consistently-styled interactive element observed is the block button
  (`.wp-block-button__link`), which uses a dark slate background (#32373c) with
  white text and a fully-rounded pill radius (9999px) — this is treated as the
  primary CTA pattern. Supporting neutrals (#eeeeee, #dddddd, #313131, #202020,
  #444444, #c9c9c9) are drawn from the theme's default gray utility classes and
  are mapped here to body text, hairlines, and soft surfaces; these role
  assignments are inferred, not measured from rendered pages. A blue accent
  family (#007cba, #006ba1, #005a87) appears only as WordPress admin/editor theme
  variables, not confirmed storefront UI, so it is proposed here as a secondary
  link/focus accent rather than a proven brand color. Typography is limited to
  Poppins (assumed heading face per common WP theme pairing) and a generic
  sans-serif stack for body copy, with 16px and 42px as the only concrete
  observed type sizes. The resulting interpretation favors a utilitarian,
  garage-tool aesthetic: dark neutral CTAs, light gray section breaks, and
  minimal color accenting, consistent with a diagnostics-hardware catalog site.

colors:
  primary: "#32373c"
  ink: "#202020"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#c9c9c9"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#313131"
  accent: "#007cba"
  accent-hover: "#006ba1"
  accent-active: "#005a87"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 42px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1, letterSpacing: 0px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    linkColor: "{colors.muted}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  diagnostic-feature-list:
    backgroundColor: "{colors.surface-soft}"
    itemTextColor: "{colors.body}"
    itemTypography: "{typography.body-sm}"
    iconColor: "{colors.accent}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components

**button-primary** reflects the one concrete interaction pattern in the evidence: the Gutenberg `.wp-block-button__link` style, with a dark slate fill, white text, and a full pill radius. It is proposed for "Shop Now," "Add to Cart," and similar catalog CTAs.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More"), reusing the primary color as border/text on a transparent field since no distinct secondary button style was observed.

**text-input** is a proposed field style for search or checkout forms; no input styling was present in the supplied CSS, so border, radius, and padding are inferred defaults consistent with the theme's neutral palette.

**nav-bar** represents the header/menu row implied by the "Products / OBD Apps / Support / Company" navigation text. Background and text colors are inferred from the light canvas and dark ink neutrals; hover state uses the admin-theme blue as a proposed accent, not a confirmed link color.

**product-card** models the repeated product listings (OBDLink MX+, Carbyte, CX, EX, LX) seen in the page text, each with a name and price. Card chrome (border, radius, padding) is proposed; the price color reuses the primary dark neutral for consistency with button styling.

**hero** is a proposed top-of-page banner treatment for messaging like "Beyond Diagnostics," using the light-gray surface and largest observed type size (42px) as the headline scale.

**footer** uses the dark-gray utility background (#313131) observed in the theme's color classes, paired with white/muted text for copyright and policy links ("Privacy Policy," "Contact Us," "© 2026 OBD Solutions, LLC").

**badge** is a proposed small label component (e.g., "Free OEM Add-ons," "180-Day Guarantee") using the accent blue as an unverified but plausible highlight color, since no badge styling was present in the CSS.

**search** is a proposed header search affordance; no explicit search-input CSS was supplied, so styling mirrors the general input/pill conventions used elsewhere.

**diagnostic-feature-list** is a category-specific component for the feature groupings visible in the content ("Live Data," "Coding," "Diagnostics," "Service"), rendering short bulleted capability lists on a soft-gray background with an accent-colored icon slot — proposed to fit a scan-tool feature comparison layout.

## Responsive Behavior

The following breakpoint table is a recommendation only; no responsive CSS or rendered mobile layout was included in the supplied evidence.

| Breakpoint | Width       | Behavior (proposed)                              |
|------------|-------------|---------------------------------------------------|
| mobile     | <600px      | Single-column stack; nav collapses to menu icon   |
| tablet     | 600–959px   | 2-column product grid; hero text reduces to display-md |
| desktop    | 960–1279px  | 3-column product grid; full nav visible           |
| wide       | ≥1280px     | Max-width content container with fixed gutters    |

Touch targets should be at least 44px in height for buttons and nav links; the primary button's pill radius and padding already exceed this if applied at button-md sizing. Navigation collapse into a hamburger/off-canvas menu on mobile is proposed, not confirmed by any supplied mobile markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS/text extraction; no rendered screenshots, computed styles, or interaction states (hover, focus, active, disabled) were observed.
- Several palette entries (e.g., #ff6900, #cf2e2e, #9b51e0) are generic Gutenberg default swatches rather than confirmed brand colors, and are intentionally excluded from the token set to avoid misrepresenting brand identity.
- The blue accent family (#007cba/#006ba1/#005a87) originates from WordPress admin/editor theme variables; its use as a storefront link/accent color is inferred, not verified against live front-end styling.
- Poppins is assumed as the heading font based on common WP theme pairing conventions; body font is treated as a generic sans-serif stack since no explicit body font-family rule was supplied. Font licensing/self-hosting was not verified.
- All spacing, rounded-corner, and responsive breakpoint values beyond the pill radius (9999px) and button padding formula are proposed defaults, not measured from the site.
- Component states (loading, error, empty cart beyond the observed "Your cart is empty" text) are not covered by the supplied evidence.
