---
version: alpha
name: "Petguin"
source_url: "https://petguin.com"
captured_at: "2026-09-28T09:53:18.110935+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Petguin is a Shopify-hosted storefront for handmade cat and dog furniture (cat towers, dog crate furniture, indoor dog houses, dog beds). The theme's CSS exposes a small set of concrete, rendered hex values against a much larger design-token palette that resolves through unresolved CSS custom properties (--text-color, --heading-color, --button-background), so most "brand" colors could not be directly confirmed from selectors and are treated as inferred.
  Confirmed values include a slideshow button using near-black (#363636) text on a white (#ffffff) outline, and an accelerated-checkout button using a teal-blue (#1990c6, hover #136f99) fill with white text. These two form the basis of the proposed primary action color. Warm palette entries (#f6a429, #e98422) and status-like reds/greens (#cb2b2b, #307a07) appear in the supplied palette without direct selector evidence; they are mapped here as inferred accent/sale and success/error roles, reusable across badges and stock states.
  Typography is Poppins with sans-serif fallback for both body and heading tokens (--text-font-family, --heading-font-family both point to Poppins in the surrounding theme). Buttons are explicitly uppercase, 0.2em letter-spaced, with border-radius:0 — this square, label-like button treatment anchors the proposed rounded scale toward sharp corners for primary actions and softer radii elsewhere.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  accent: "#f6a429"
  ink: "#1c1b1b"
  body: "#363636"
  muted: "#6a6a6a"
  hairline: "#dedede"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  success: "#307a07"
  error: "#cb2b2b"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.65, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.05em}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.2em}
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
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.error}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.ink}"
    ctaButton: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  shipping-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** is proposed for checkout, add-to-cart, and "View the Product" CTAs, built on the confirmed teal-blue accelerated-checkout fill (#1990c6) with white text; the sharp corner (rounded.none) matches the observed .Button border-radius:0 rule.

**button-secondary** covers outline-style actions (e.g. slideshow "View" links), reusing the confirmed white-border/dark-text pattern from `#section...__slideshow .Button` with an inverted hover state proposed but not observed.

**text-input** is a proposed pattern for newsletter, search, and account forms; no form-field CSS was supplied, so border, radius, and padding are inferred from the theme's general spacing rhythm.

**nav-bar** represents the header housing Dog/Cat/Blog/Account/Cart navigation implied by the page text ("Skip to content Dog... Cat... Account Cart"); layout and sticky behavior are inferred from `--use-sticky-header` variables present in the CSS but not measured visually.

**product-card** models the recurring sale-tile pattern seen in the text excerpt (product name, struck-through original price, sale price, "On sale (X% off)" badge), using the error-red token for discounted pricing as an inferred convention.

**hero** is proposed for the homepage slideshow region (`#section-template--16465124098305__slideshow`), using dark ink background and white text consistent with the one confirmed slideshow button treatment; exact imagery and copy layout are not observed.

**footer** is proposed for the site-wide footer (Our Story, Blogs, Contact, worldwide/regional buy links); dark background and muted link color are inferred, not confirmed by supplied selectors.

**badge** covers "On sale," "Sold out," and category tags visible in the page text; the accent orange is an inferred role since no badge-specific selector was supplied.

**search** is a proposed pattern for the header search affordance; no dedicated search CSS was present in the evidence.

**shipping-banner** models the observed copy "Spend $100.00 more and get free shipping!" / "FREE SHIPPING ON ALL ORDERS IN THE US" as a persistent top banner using the primary blue fill; the component's existence in the DOM is confirmed by text content, but its exact markup and styling are inferred.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | 0–599px | single-column product grid, collapsed nav behind menu icon |
| tablet | 600–999px | 2-column product grid, nav bar remains inline |
| desktop | 1000–1439px | 3–4 column product grid, full nav with dropdowns |
| wide | 1440px+ | max-width content container, extra whitespace |

Touch targets for `button-primary`/`button-secondary` should maintain a minimum 44px tap height, consistent with the `.shopify-payment-button__button` clamp(25px, …, 55px) rule observed in the accelerated-checkout CSS. Navigation collapse into a hamburger/off-canvas pattern below the tablet breakpoint is a recommendation only; no mobile menu markup or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from static CSS/text extraction only; no rendered screenshots, computed styles, or interaction states (hover/focus/active, mobile menu behavior, cart drawer) were observed. Many theme colors resolve through CSS custom properties (--text-color, --heading-color, --button-background, --button-text-color) whose final hex values were not exposed in the supplied evidence, so `ink`, `body`, `surface-soft`, `accent`, `success`, and `error` role assignments are inferred from the broader supplied palette rather than confirmed by selector-level proof. Font availability, licensing, and whether Poppins is self-hosted or third-party loaded were not verified. All spacing, rounded (aside from `none`, which reflects the observed `border-radius:0` on `.Button`), and typographic size values are proposed conventions, not measured layout. Breakpoints and touch-target guidance are recommendations based on common e-commerce patterns, not measured site behavior.
