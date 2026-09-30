---
version: alpha
name: "Method Race Wheels"
source_url: "https://methodracewheels.com"
captured_at: "2026-09-29T04:08:35.731421+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Method Race Wheels' storefront CSS shows a compact, high-contrast palette built
  from near-black body text (#1d1d1d), white canvas (#ffffff), and a saturated
  safety-orange accent (#fd672e) used consistently as the primary call-to-action
  color on buttons and the "vehicle fitment" widget. Supporting neutrals
  (#f6f6f6, #f7f7f7, #e7e7e7, #eeeeee) appear as light section and card
  backgrounds, while #555555 marks disabled button text. Two secondary hues,
  a red (#ec1d24) and a blue (#197bbd), surface in the observed palette and are
  treated here as inferred accent/badge colors for filters or color-swatch
  chips, since their exact usage is not confirmed by the supplied rules.
  Typography is anchored on Rubik for body copy and buttons (confirmed via
  body and .button selectors); din-2014 and din-2014-narrow appear in the
  font-family evidence and are inferred here as the condensed display face for
  large hero headlines, matching the brand's motorsport tone, though this
  mapping is not directly observed on a heading selector. The interpretation
  favors a rugged, industrial UI: sharp 2px button radii (observed), dense
  uppercase button labels, and flat orange-on-white contrast for primary
  actions, with generous card spacing to support wheel/tire product imagery.

colors:
  primary: "#fd672e"
  ink: "#1d1d1d"
  canvas: "#ffffff"
  body: "#1d1d1d"
  muted: "#555555"
  hairline: "#e7e7e7"
  surface-soft: "#f6f6f6"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  disabled-bg: "#eeeeee"
  accent-red: "#ec1d24"
  accent-blue: "#197bbd"
  overlay-dark: "#00000080"
typography:
  display-xl: {fontFamily: "din-2014, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "din-2014, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "rubik, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "rubik, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "rubik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "rubik, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "rubik, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 17px, letterSpacing: 0.015em}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "79px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"

## Components

**button-primary** renders the confirmed `.button` pattern: orange (#fd672e) fill, white text, uppercase Rubik label, and a 2px radius observed directly in the CSS. Hover state (white background, dark border/text) is confirmed via `.button:hover`.

**button-secondary** mirrors the observed `.button-outline` rule — transparent background with an inherited text color and a 2px solid border — proposed here as the ink-colored outline variant for secondary actions like "Learn More."

**text-input** is a proposed pattern for search and vehicle-year/make/model fields; no dedicated input selector was supplied, so border, radius, and padding are inferred from the general neutral/hairline palette.

**nav-bar** uses the confirmed `--nav-height` custom properties (75–79px across breakpoints) and white canvas; the mega-menu category list (Wheels, UTV, Race, Accessories, Apparel) implies a multi-tier flyout, which is proposed layout behavior, not measured interaction.

**product-card** is a proposed component for wheel/tire listings, using the light surface-card background and hairline border to separate product tiles in a grid, consistent with the site's product-catalog navigation structure.

**hero** is inferred from banner copy ("HIGH PERFORMANCE WHEELS... LIGHTER. STRONGER. FASTER.") paired with vehicle gallery CTAs; a dark overlay on imagery with large display type is proposed to support text legibility over wheel/vehicle photography.

**footer** is proposed as a dark-ink band echoing the ink/ on-primary contrast pair, housing policy links (Returns, Shipping, Privacy, Warranty) and dealer/contact links present in the extracted navigation text.

**badge** is proposed for labeling states like "New Arrivals," "Markdown," or color-swatch tags (Bronze, Black Machined, Titanium, Gold, Blue, Red, Grey), using the accent-red as an attention color since no dedicated badge selector was supplied.

**search / vehicle-fitment-selector**: the fitment selector is a category-appropriate component built directly from evidence ("Add a Vehicle," "Verified ${customerVehicle.year}..."), a core wheel/tire-fitment UX pattern; styling (soft surface, orange accent) is proposed to align with the confirmed `.vehicle-info__button` orange/white treatment.

## Responsive Behavior

Recommended (not measured) breakpoint table:

| Breakpoint | Range | Nav | Grid |
|---|---|---|---|
| Mobile | <768px | Collapsed hamburger, stacked vehicle-fitment bar | 1-column product grid |
| Tablet | 768–1023px | Condensed horizontal nav | 2-column product grid |
| Desktop | ≥1024px | Full mega-menu nav (matches --nav-height tokens) | 3–4 column product grid |

Touch targets should be at least 44px, matching the Swiper `--swiper-navigation-size: 44px` token observed in vendor CSS. Mega-menu categories should collapse into an accordion on mobile. This table is a proposed recommendation; no live responsive layout was observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed layout, or JavaScript-driven interaction (cart drawer, mega-menu behavior, vehicle-fitment flow) was observed. Font role assignments — particularly din-2014/din-2014-narrow for display headings — are inferred from font-family evidence, not a confirmed heading selector. Spacing scale and most typography sizes beyond the confirmed 16px body and 14px/10px button values are proposed estimates, not measured. Component states (focus, error, loading) are proposed and unverified. Custom font (din-2014, Rubik) hosting, licensing, and availability were not verified. Color role assignments beyond the confirmed orange button and disabled-state greys are inferred from palette frequency and typical e-commerce conventions, not confirmed selectors.
