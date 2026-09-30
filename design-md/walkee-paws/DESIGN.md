---
version: alpha
name: "Walkee Paws"
source_url: "https://walkeepaws.com"
captured_at: "2026-09-28T09:53:46.485987+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Walkee Paws presents a clean, high-contrast e-commerce interface built on Shopify's standard theme conventions. The observed palette centers on near-black ink (#202020) against a pure white canvas (#ffffff), with a saturated cyan-blue (#0db7e8, alongside close variants #00a9ca and #00b1e6) as the dominant brand accent, likely used for links, icons, and interactive highlights given its repeated appearance. A coral-red (#ff7163) and a muted navy (#3e5c9a) also recur and are inferred as secondary accents for promotional badges or alternate CTAs, while status-like colors (#108043 green, #f5a623 amber, #de3618 red) are inferred as form/feedback states common to Shopify checkout components. Typography pairs Nunito (weight 800) for headings and titles with Nunito Sans (weight 400) for body copy and form controls; a single observed instance of "jost" at 900-weight drives a specific calculator-modal button, which we generalize cautiously into a bold, uppercase-leaning button style. Layout patterns (hero, product card, breed-fit finder) are inferred from page text mentioning breed selectors, sizing tools, and boot-leggings product categories, not from measured DOM structure. Rounded corners default to a soft, moderate scale consistent with the one observed 10px checkout-button radius. All roles below are semantic inferences from the supplied CSS/text evidence.

colors:
  primary: "#0db7e8"
  secondary: "#3e5c9a"
  accent-coral: "#ff7163"
  success: "#108043"
  warning: "#f5a623"
  error: "#de3618"
  mint-soft: "#d3f9f1"
  ink: "#202020"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#797979"
  hairline: "#dde0e4"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "Nunito, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0px}
  display-md: {fontFamily: "Nunito, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Nunito, sans-serif", fontSize: 22px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  button-md: {fontFamily: "jost, sans-serif", fontSize: 16px, fontWeight: 900, lineHeight: 1.2, letterSpacing: 0px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
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
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  breed-fit-finder:
    backgroundColor: "{colors.mint-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** — The bright cyan accent (#0db7e8) on white text is proposed as the primary call-to-action treatment (e.g. "Shop Now", "Find"), drawn from the site's dominant blue accent presence across the palette. Bold jost typography is observed on one modal button and generalized here.

**button-secondary** — An outlined, ink-colored variant is proposed for lower-emphasis actions (e.g. "See All", "Learn More") to preserve hierarchy against the primary CTA. Border and text use ink; background stays transparent. This pattern is inferred, not directly observed.

**text-input** — A white field with a light hairline border, matching Shopify-default form conventions. Used for search, sizing-tool inputs, and newsletter capture. Focus/error states are proposed, not observed in the supplied CSS.

**nav-bar** — A white, sticky-feeling header inferred from the page-text listing (currency switcher, search, login, cart, mega-menu items like "Dog Boot Leggings", "Sizing Guide"). Typography uses the smaller Nunito Sans body style; a thin hairline likely separates it from content below.

**product-card** — A white surface with soft rounded corners, housing product imagery, an 800-weight Nunito title, and a smaller price line. Rounded value follows the moderate `md` token given the one observed 10px checkout-button radius as a loose reference point.

**hero** — A large banner area is inferred from copy such as "Say Goodbye to Lost Dog Boots & Hello to Style," pairing a large Nunito display headline with body copy and a primary CTA button. Background uses the light neutral surface-soft tone rather than pure white, for visual separation.

**footer** — A simple, text-forward footer inferred from the extensive link list (FAQ, Blogs, Ambassador Program, Returns). Uses body-sm typography and the same hairline color as the nav to bookend the page.

**badge** — A coral pill badge (#ff7163) is proposed for promotional flags such as "25% off Clearance Sale," using the caption typography scale and full rounding for a soft, friendly shape consistent with a pet-product brand.

**search** — A soft-gray input field styled distinctly from the white page background, referencing the repeated overlay/search UI text in the evidence ("Search Search our store"). Placeholder text uses the muted gray tone.

**breed-fit-finder** — A category-specific component proposed for the observed breed-selector and paw-measurement tools ("Select your dog's breed," "How to measure PAW WIDTH/HEIGHT"). A mint-tinted card (#d3f9f1) with the primary cyan as an interactive accent distinguishes this instructional module from standard content blocks.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width       | Notes                                      |
|-----------|-------------|---------------------------------------------|
| mobile    | 0–599px     | Single-column stacking; nav collapses to a hamburger/drawer menu |
| tablet    | 600–959px   | Two-column product grids; hero text/image may stack |
| desktop   | 960–1279px  | Full nav with mega-menu; multi-column product grids |
| wide      | 1280px+     | Max-width content container; generous section padding |

Touch targets for buttons and nav items should maintain a minimum 44px height (aligned with the observed `--shopify-accelerated-checkout-button-block-size: 44px` token). Mobile navigation is expected to collapse into a drawer given the long link list in the evidence, though this collapse behavior is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed layout, or DOM structure was observed. Component boundaries, spacing values, and breakpoints are proposed conventions based on common Shopify-theme patterns, not measured pixel values. Color-role assignments (e.g. which blue is "primary" vs. a decorative variant, or whether coral/navy are truly secondary brand colors vs. incidental UI states) are inferred from frequency and context, not confirmed via rendered screenshots. The "jost" font family was observed in a single, narrow selector (a calculator modal button) and its generalization to a button-md typography token is an extrapolation. Font licensing and self-hosting/webfont availability for Nunito, Nunito Sans, and jost were not verified. Interaction states (hover, focus, active, disabled) and actual mobile/responsive layout behavior were not observed and are marked proposed throughout. The breed-fit-finder and other category-specific components are inferred entirely from page copy, not from any captured selector or class evidence.
