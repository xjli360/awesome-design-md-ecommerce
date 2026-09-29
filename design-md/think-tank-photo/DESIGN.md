---
version: alpha
name: "Think Tank Photo"
source_url: "https://thinktankphoto.com"
captured_at: "2026-09-28T09:31:08.608546+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Think Tank Photo's storefront evidence shows a neutral, utilitarian palette built around near-black text (#121212, #2f2b2b), white/off-white surfaces (#ffffff, #f8f8f8, #fcfcfc), and a single saturated interactive blue (#1990c6, hover #136f99) drawn from the Shopify accelerated-checkout button styles. Skeleton-loading and border grays (#dedede, #e6e6e6, #00000033) round out a restrained, functional UI consistent with a technical gear retailer. Several palette entries (#eb001b, #f79e1b, #ff5f00, #0071ce, #142fbd, #1532cb) are standard payment-network brand marks (Mastercard/Visa-style) rather than site design colors and are excluded from role assignment here.

  Typography uses Montserrat and Nunito as the only clearly observed web fonts, with Roboto Mono present (likely for SKUs, prices, or code-like labels) and "slick" referring to the Slick carousel plugin's icon font rather than a display typeface. This interpretation assigns Montserrat to headings/buttons (geometric, technical) and Nunito to body copy (rounded, readable), both inferred pairings based on common usage patterns for this font combination, not confirmed computed styles.

  Corner radii are mostly small (2px on Bold app buttons) suggesting a squared, functional aesthetic; larger radii here are proposed for future card/pill use. Spacing and most component states are proposed scaffolding, not measured layout.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#121212"
  ink-secondary: "#2f2b2b"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#818181"
  hairline: "#e6e6e6"
  surface-soft: "#f8f8f8"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  border-soft: "#00000033"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.ink-secondary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-secondary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  quick-view-overlay:
    backgroundColor: "{colors.canvas}"
    overlayScrim: "{colors.border-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"

## Components
**button-primary** renders the checkout/CTA action using the one confirmed accent blue (#1990c6, hover #136f99) from the Shopify accelerated-checkout CSS, with white text and a tight 2px radius matching the Bold-app button radius observed in the CSS.

**button-secondary** is a proposed outline treatment for lower-emphasis actions (e.g. "Shop Turnstyle"), using a white background, dark ink text, and a soft semi-transparent border echoing the `rgba(0,0,0,.3)` borders seen on Bold upsell buttons. Hover/active states are not observed and are proposed.

**text-input** proposes a plain white field with a light hairline border for search or account forms; no input CSS was present in evidence, so sizing and focus states are inferred conventions.

**nav-bar** reflects the observed `.overlay-header.force-hover` white background rule and the deep, multi-level category structure (Rollers, Backpacks, Bags, Modular Belt System, Collections). Mobile collapse behavior is proposed, not observed.

**product-card** is grounded in `.bold-product__title` (15px, #121212 text) and the repeated "QUICK VIEW" label pattern seen across new-arrival and Backlight listings; card chrome (border, radius, padding) is proposed.

**hero** models the large promotional banners implied by repeated "INTRODUCING FOCUSPOINT" and "Shop Now" copy blocks; dark background and light text are inferred from the site's dark-neutral palette entries, not a captured hero screenshot.

**footer** is proposed using the same dark ink-secondary tone as hero, appropriate for a utility-heavy footer (Warranty, Replacement Parts, Store Locator) but not confirmed by footer-specific CSS.

**badge** proposes a pill treatment for stock/status labels such as "Coming Soon" and "Special Edition," using the primary blue as an inferred accent since no badge-specific styling was in evidence.

**quick-view-overlay** is a category-appropriate component for the repeated "QUICK VIEW" interaction pattern found on every listed product (FocusPoint, Turnstyle, BackLight items), modeled as a light modal card; actual modal chrome, animation, and z-index are not observed.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤599px, tablet 600–959px, desktop ≥960px. Touch targets should be a minimum 44px height, matching the `clamp(25px, …, 55px)` range seen in the Shopify accelerated-checkout button CSS. The deep multi-level nav (Rollers/Backpacks/Bags/Modular Belt System/Collections/Support) should collapse into an accordion or drawer below tablet width. This section is a design recommendation only; no live responsive behavior, viewport screenshots, or media-query CSS were supplied.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived entirely from static CSS/text extraction; no rendered screenshots, computed styles, or interaction states (hover, focus, active, error) were observed beyond the few pseudo-class rules present in the evidence (e.g. `.shopify-payment-button__button--unbranded:hover`). Semantic role assignment for colors such as body/muted/ink-secondary is inferred from typical usage patterns, not confirmed CSS selectors for body text. All typography sizes outside the two confirmed values (15px product title, 12px modal header) are proposed. Font availability, licensing, and whether Montserrat/Nunito are self-hosted or third-party embeds were not verified. Mobile navigation, cart drawer, and quick-view modal behavior were not observed and are proposed conventions only. Payment-network palette entries (Mastercard/Visa-style hexes) were excluded from role mapping as they represent third-party marks, not brand design tokens.
