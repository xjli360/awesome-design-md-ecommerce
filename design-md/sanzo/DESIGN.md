---
version: alpha
name: "Sanzo"
source_url: "https://drinksanzo.com"
captured_at: "2026-09-28T10:05:18.980838+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sanzo's public storefront evidence points to a bold, culturally-rooted beverage
  brand built around a deep magenta/burgundy announcement bar (#8d164e) paired
  with a brighter secondary pink (#d82061) used in interactive dropdown surfaces.
  Near-black (#050504) and dark charcoal (#353535) appear in social-icon
  treatments and are inferred here as primary ink and body-text roles, since no
  dedicated text-color rule was observed. A warm off-white (#f3eeeb) and light
  neutral (#f7f7f7) suggest soft section backgrounds distinct from pure white
  canvas. Deal-count and notice modules use a muted brown (#7d583b) on light
  gray (#e9e9e9), which this spec repurposes as a muted-text and hairline pair.
  Accent greens (#027326) and warm oranges (#f26722) are inferred as
  success/offer and sale-badge colors respectively, since the actual observed
  offer-price hex was outside the supplied palette and could not be used.
  Typography evidence lists Outfit alongside system fallbacks (Arial,
  Helvetica); Outfit is proposed for display/heading roles as the only
  distinctive observed family, with Arial/Helvetica retained for body copy.
  Layout, spacing, and interaction states below are proposed conventions for a
  DTC sparkling-beverage shop, not measured observations.

colors:
  primary: "#8d164e"
  accent: "#d82061"
  highlight: "#dec066"
  ink: "#050504"
  canvas: "#ffffff"
  body: "#353535"
  muted: "#7d583b"
  hairline: "#e9e9e9"
  surface-soft: "#f3eeeb"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  success: "#027326"
  danger: "#d02336"
  badge-sale: "#f26722"
typography:
  display-xl: {fontFamily: "Outfit, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Outfit, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Outfit, sans-serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Outfit, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.5px"}
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
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.success}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-variant-swatch:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the deep magenta announcement-bar color as its fill, since that hue is the only saturated brand color observed at high prominence (header banner). White text ensures contrast; hover/pressed states are proposed and not observed.

**button-secondary** proposes an outlined variant sharing the primary hue for text/border on a transparent field, useful for secondary CTAs like "Find In Store" alongside a filled "Shop Sparkling" button. Not observed as a distinct style in the CSS.

**text-input** is a proposed minimal-bordered field using the light hairline gray observed in deal-count backgrounds, appropriate for login/search forms referenced in the page text (Email, Password fields).

**nav-bar** is inferred from header-contact and social-icon rules; white canvas with dark ink text keeps the header legible above the colored announcement bar, though exact nav layout/height was not measured beyond the 40px announcement bar.

**product-card** models the flavor SKU tiles (Yuzu with Ginger, Lychee, Mandarin, etc.) using the light card surface and hairline border, with price rendered in the success green inferred as a stand-in for the unobserved offer-price hex.

**hero** proposes the warm off-white surface as a full-bleed section background for the "Explore Asian Flavor" / "Traditional Asian Flavors. Modern Taste." messaging, paired with the large Outfit display type.

**footer** is proposed as a dark, high-contrast band (using ink as background) to hold newsletter signup, social links, and legal text (Terms, Privacy, Refund policy) seen in the page copy; this inversion is a convention, not an observed rule.

**badge** covers promotional/sale labeling (e.g., "Free Shipping on All Orders $50+" callouts or sold-out states) using the observed orange tone; the specific sold-out red in the source CSS could not be reused because its hex was absent from the supplied palette, so a palette-safe warm accent was substituted.

**search** is a rounded, pill-shaped field inferred for the "Popular searches" feature, styled with neutral hairline borders rather than any brand color, since no search-specific color was observed.

**flavor-variant-swatch** is a category-appropriate proposed component for selecting among the six flavors and variety packs, using pill-shaped chips with the primary color indicating an active selection; entirely inferred to support the product-line browsing pattern implied by the text content.

## Responsive Behavior

Proposed breakpoints (not measured): mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. Navigation is expected to collapse into a hamburger/off-canvas menu below tablet width; the flavor grid likely reflows from a multi-column desktop layout to 2-column tablet and single-column mobile stacks. Touch targets for buttons and swatches should maintain a minimum 44px hit area. Announcement bar height (40px, observed) is likely fixed across breakpoints but may wrap text on narrow viewports. This section is a recommendation based on common ecommerce patterns, not verified against live responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were directly observed. Several semantic color roles — including body text, ink, muted, hairline, and surface tokens — are inferred from incidental UI-element rules (social icons, deal-count notices) rather than explicit typographic or background declarations. The original `.offer-price` and `.badge--sold-out` colors found in the CSS evidence were excluded because they did not appear in the supplied observed-palette array; palette-safe substitutes (success green, badge-sale orange) were used instead, so actual brand success/error colors may differ. Typography sizes, weights, and line-heights are proposed conventions, not measured from rendered pages. The listed "Outfit" and "Sharp Sans"/"Trump Gothic Pro" families appear in font-family evidence but their actual application (headings vs. body vs. unused theme defaults) and licensing/availability were not verified. Mobile menu behavior, product-card grid structure, and hero imagery were not observed and are proposed only.
