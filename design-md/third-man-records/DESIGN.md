---
version: alpha
name: "Third Man Records"
source_url: "https://www.thirdmanrecords.com"
captured_at: "2026-09-28T04:12:19.629360+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Third Man Records presents itself through a stark, high-contrast identity built on
  true black (#0b0d0f), a deeper off-black (#13171a), and a saturated signature
  yellow (#ffd200), set against a white canvas (#ffffff) with dark gray body copy
  (#333333). These four values are explicitly declared as CSS custom properties
  (--tmr-black, --tmr-off-black, --tmr-yellow, --color-foreground) and confirm the
  brand's core palette. The yellow is used functionally as a circular notification
  badge with black text, suggesting its role as an accent/alert color rather than a
  primary call-to-action fill; this interpretation extends that role to buttons and
  highlights as an inferred pattern. Bootstrap 5.3.6 utility colors (grays, danger,
  success, warning, info) are present in the evidence as framework defaults and are
  mapped here to muted text, hairlines, form borders, and system-feedback states —
  their brand significance is inferred, not confirmed. Typography is set in Inter
  with system sans-serif fallback; only body weight (400) and heading weight (500)
  are observed, so all sizes below are proposed. Border radius is minimal (4px on
  inputs, 0px on buttons per --wk-button-border-radius), reinforcing an industrial,
  no-frills record-shop aesthetic suited to a label rooted in analog/vinyl culture.

colors:
  primary: "#ffd200"
  ink: "#0b0d0f"
  off-black: "#13171a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#eeeeee"
  on-primary: "#0b0d0f"
  link: "#0d6efd"
  danger: "#dc3545"
  success: "#198754"
  warning: "#ffc107"
  info: "#0dcaf0"
  border-input: "#ced4da"
  text-secondary: "#495057"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 11px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    height: "72px"
    iconColor: "{colors.canvas}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.off-black}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    size: "1.2rem"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  vinyl-release-tile:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    formatBadgeBackground: "{colors.primary}"
    formatBadgeText: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    artistTypography: "{typography.caption}"

## Components

**button-primary** uses the near-black ink tone as a solid fill with white label text, echoing the site's dominant black/white contrast; this is a proposed default action style, not a confirmed button screenshot. **button-secondary** proposes an outlined variant sharing the same ink color for border and text on a transparent background, useful for lower-emphasis actions like "add to wishlist." **text-input** reflects the confirmed `--style-border-radius-inputs: 4px` token and a neutral bootstrap-style border, proposed for search and account forms. **nav-bar** is inferred from the `.header-icons` and `#header-icons` rules, which confirm white icon color and a 2.5rem touch target for cart/account icons on a presumed white header bar; overall header layout is not directly observed. **product-card** is a proposed pattern for shop listings, using a light card surface and hairline border consistent with the neutral bootstrap palette present in evidence. **hero** proposes an off-black banner section using the darker `--tmr-off-black` token with yellow accent text, suited to a record label's editorial/announcement banners, though no hero markup was captured. **footer** proposes an ink-black footer with yellow link accents, mirroring the confirmed badge color pairing (yellow background, black text) inverted for dark-surface legibility. **badge** is the most directly observed component: the CSS confirms a circular yellow badge (`--tmr-yellow` background, `--tmr-black` text, 1.2rem size, 700 weight, .7rem font-size) used for cart item counts. **search** is a proposed light-surface input variant for a persistent search affordance common to e-commerce headers. **vinyl-release-tile** is a category-specific proposed component for displaying records, pairing a format badge (reusing the confirmed yellow/black badge treatment) with tile-based artist/title text, appropriate for a label-and-shop hybrid catalog.

## Responsive Behavior

The following breakpoint table is a recommendation based on Bootstrap 5.3.6's declared `--bs-breakpoint-*` custom properties found in evidence; actual responsive behavior on thirdmanrecords.com was not observed.

| Breakpoint | Width   | Layout guidance (proposed) |
|-----------|---------|------------------------------|
| xs        | 0       | Single-column stack, collapsed nav to hamburger/drawer |
| sm        | 576px   | 2-column product grid |
| md        | 768px   | 3-column product grid, inline search |
| lg        | 992px   | Full nav bar visible, 4-column grid |
| xl        | 1200px  | Max content width approaching `--page-width: 90rem` |
| xxl       | 1400px  | Wide layout with increased gutter (`--page-margin: 20px` as baseline) |

Touch targets should follow the confirmed 2.5rem (40px) icon button size from `.icon-link`. Below the `md` breakpoint, primary navigation is assumed to collapse into a drawer or hamburger menu; this collapse pattern is proposed and not confirmed by captured markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a Bootstrap 5.3.6 stylesheet, and a small set of component-level rules; no rendered page, DOM structure, or interaction states were observed. Bootstrap's default utility colors (grays, danger, success, warning, info, link blue) appear in evidence as framework defaults and have been mapped to plausible system-feedback and neutral roles, but their actual in-product usage is inferred, not confirmed. All typography sizes beyond the badge's `.7rem`/700-weight and the button's `1rem`/400-weight are proposed, not measured. Layout structure (grid columns, hero composition, footer content) is inferred from category convention (record label + shop) rather than observed markup. Hover, focus, active, and error states for inputs and buttons are proposed defaults, not verified interactions. Mobile navigation collapse behavior was not observed. Font availability is limited to the single declared family, Inter, with no evidence of licensing terms, additional weights, or custom/proprietary display fonts; any such usage on the live site is unconfirmed.
