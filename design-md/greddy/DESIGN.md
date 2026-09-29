---
version: alpha
name: "GReddy"
source_url: "https://greddy.com"
captured_at: "2026-09-29T04:17:35.122575+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  GReddy's storefront CSS exposes a strict black-and-white foundation (#000000, #ffffff, #121212, #1c1c1c) layered with neutral grays (#333333, #666666, #dddddd, #f5f5f5) for body copy, hairlines, and soft surfaces. A small set of blues (#1672b0, #105888) appear in the palette outside of checkout-specific selectors and are interpreted here as the site's interactive accent for links, focus states, and secondary emphasis; a warm tan (#f8ca79) is treated as a sparing highlight for badges or sale callouts. Payment-network colors (Visa/Mastercard/Shop Pay blues, oranges, and reds) were excluded from the brand role mapping since their selectors tie them explicitly to third-party checkout widgets.
  Typography is drawn from the observed font stack: Barlow is proposed for display/heading roles given its presence alongside a condensed, motorsport-oriented nav structure (engine-code categories like RB26, 2JZ, SR20), while Open Sans/system sans-serif covers body text. The CSS's zero border-radius on the accelerated-checkout button and the brand's industrial parts-catalog content suggest a squared, technical aesthetic rather than soft rounded UI — reflected here in a mostly sharp-cornered rounded scale. Header grid variables confirm a centered-logo, sticky-header structure at multiple breakpoints; all spacing/radius pixel values beyond that are proposed defaults, not measured.

colors:
  primary: "#000000"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1c1c1c"
  on-primary: "#ffffff"
  accent: "#1672b0"
  accent-dark: "#105888"
  highlight: "#f8ca79"
  danger: "#f44336"
  success: "#4caf50"
typography:
  display-xl: {fontFamily: "Barlow, sans-serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Barlow, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Barlow, sans-serif", fontSize: 26px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Barlow, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    position: "sticky"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-filter:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
    optionTypography: "{typography.body-sm}"
    accentColor: "{colors.accent}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components

**button-primary** renders as a solid black rectangle with white text, matching the zero-radius checkout button observed in the Shopify accelerated-checkout CSS; hover/pressed states are proposed inversions (outline + transparent fill), not confirmed by supplied selectors.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g., "View Details"), using the same square corners for visual consistency with the primary button. Hover state (fill-on-hover) is proposed based on common outline-button patterns, not observed here.

**text-input** covers search boxes, email/text-chain signup fields, and account forms. Border and radius are proposed since no explicit input CSS was supplied; the hairline gray keeps inputs visually quiet against the white canvas.

**nav-bar** reflects the confirmed sticky header (`position: sticky; top: 0; z-index: 10`) with a three-column grid (`main-nav logo secondary-nav`) and logo dimensions that scale from 125×51px to 235×96px at wider viewports — this scaling is directly observed in the CSS custom properties.

**product-card** is proposed for the deep catalog structure (exhausts, turbo kits, cooling, etc.); a bordered white card keeps focus on product imagery, consistent with the neutral surface-card/hairline combination in the palette.

**hero** uses the dark surface (#1c1c1c) with white text and the largest display typography scale (`--text-h0`), appropriate for a motorsport brand's full-bleed banner imagery; exact hero copy/image treatment is not observed and is proposed.

**footer** reuses the dark surface for a grounded, industrial close to the page, with accent-blue links for wayfinding to partner brands (Rocket Bunny/Pandem, Boost Brigade) and legal/support content — content structure is proposed, not observed.

**badge** is proposed for "SALE" / "NEW" flags seen in the nav text (Online Garage Sale, New), using the warm highlight tan against dark ink text for contrast without introducing an unobserved brand color.

**search** proposes a soft-gray field for the "Open search" control referenced in the nav text; no field styling was supplied, so treatment mirrors the text-input component.

**vehicle-fitment-filter** is a category-appropriate proposed component for filtering parts by engine platform (RB26, 2JZ, SR20, 13B, etc.) as enumerated under "FEATURED VEHICLES" — a common and expected pattern for a fitment-driven performance-parts catalog, though no filter UI was directly observed in the supplied CSS.

## Responsive Behavior

Recommended breakpoints (proposed, not measured beyond the header logo-size change confirmed in CSS):

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | < 750px | Single-column product grid, collapsed hamburger nav, logo ~125×51px (confirmed variable) |
| Tablet | 750–999px | 2-column product grid, condensed nav |
| Desktop | 1000–1439px | Full grid nav (`logo main-nav secondary-nav`), logo ~235×96px (confirmed variable), product-list up to 5 items/row per observed `--product-list-items-per-row` |
| Wide | ≥ 1440px | Increased section spacing per larger `--section-*` spacing tokens observed at wider root scopes |

Touch targets should be at least 44×44px for nav and filter controls; the mobile nav is expected to collapse into a hamburger/drawer pattern given the "Open navigation menu" text reference, though the actual collapse mechanism and animation were not observed. This table is a design recommendation, not a measurement of live site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a subset of selectors, and page text — not from rendered screenshots or interaction testing. Semantic color roles (primary, accent, highlight) are inferred from an undifferentiated hex list and may not match GReddy's actual brand guidelines. Font weights, exact heading sizes at each breakpoint, and letter-spacing values are proposed, not extracted from computed styles. Payment-network colors (Visa/Mastercard/Shop Pay blues and oranges) were deliberately excluded from brand roles based on their selector context but their presence confirms only checkout-widget styling, not overall brand palette. Mobile menu behavior, hover/focus/active states, product-card layout, and search UI were not observed and are proposed patterns only. Availability and licensing of Barlow and Open Sans for production use have not been verified against the live site's actual @font-face declarations, which were not present in the supplied evidence.
