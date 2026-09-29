---
version: alpha
name: "Jinx"
source_url: "https://www.thinkjinx.com/"
captured_at: "2026-09-29T03:58:33.545662+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Jinx's Shopify-hosted storefront at thinkjinx.com, a direct-to-consumer pet-food brand also distributed through Walmart, Chewy, and Amazon. The CSS exposes a custom heading/body font pairing (GTWalsheimBold for display, GTWalsheimMedium for body and navigation) layered over a neutral white-and-charcoal base, with a deep teal (#1a8168) explicitly named as an accent-alternative token, suggesting it functions as a secondary or supporting brand color rather than a dominant one. A near-black forest green (#051a17/#17554b) and a high-contrast lime (#b0ff73) also appear, consistent with a "natural, whole-food" visual register common to premium pet nutrition brands; these are treated here as inferred accent roles since no explicit semantic label was supplied for them. A cream tone (#efe0d0) is proposed as a warm surface option for ingredient or nutrition callouts. Utility colors observed in Shopify wallet/checkout components (blues #1990c6/#136f99, an announcement-bar blue #5070c4, and standard alert red/pink #721c24/#f8d7da) are preserved as functional, non-brand system colors. Layout metrics (radius values, header heights) reference CSS custom properties without resolved pixel values in the supplied evidence, so spacing and radius scales below are proposed conventions, not measured output.

colors:
  primary: "#1a8168"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#696969"
  hairline: "#dbdbdb"
  surface-soft: "#fafafa"
  surface-card: "#f9f8f4"
  on-primary: "#ffffff"
  accent-bright: "#b0ff73"
  accent-deep: "#17554b"
  accent-deepest: "#051a17"
  cream: "#efe0d0"
  announcement-bg: "#5070c4"
  error-bg: "#f8d7da"
  error-text: "#721c24"
  link-checkout: "#1990c6"
  link-checkout-hover: "#136f99"
typography:
  display-xl: {fontFamily: "GTWalsheimBold, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "GTWalsheimBold, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "GTWalsheimBold, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "GTWalsheimMedium, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "GTWalsheimMedium, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "GTWalsheimRegular, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "GTWalsheimMedium, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.3px}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  hero:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-bright}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.accent-deepest}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-bright}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-deep}"
    rounded: "{rounded.md}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"

## Components

**button-primary** proposes the deep teal (`#1a8168`) as the principal call-to-action fill, since it is the only color explicitly declared as an accent token in the site's CSS variables; hover/active states are not observed and are marked proposed.

**button-secondary** is an outline variant intended for lower-emphasis actions (e.g., "Learn More" links seen in the page copy), using the same teal for border and label text on a white ground; this pairing is inferred, not measured.

**text-input** anticipates form fields (sign-in, account, newsletter) using a soft off-white background and hairline border drawn from the observed `#dbdbdb`/`#fafafa` values; no live form screenshots were supplied.

**nav-bar** reflects the top navigation implied by the page text ("Dog / Cat / Why Jinx / Where to Buy / Sign In / Cart"), rendered on white with hairline dividers; exact header height variables (`--HEADER-HEIGHT: 77px`) were observed but internal item spacing is proposed.

**hero** models the homepage banner referencing "Ciara Miller & Jasper" and "Shop bone broth-infused, gourmet feline cuisine," using the cream surface as a warm, food-adjacent background with the bright lime as an inferred energetic accent; actual hero background color was not confirmed in the CSS evidence.

**product-card** supports SKU tiles across Dry Food/Wet Food/Treats categories mentioned in the footer sitemap, using a light card surface with generous internal padding for imagery and short descriptive copy.

**footer** uses the darkest observed green (`#051a17`) as an inferred footer background to anchor the site's "give back"/mission messaging, with the lime accent reserved for link hover states; this color-role pairing is inferred from palette contrast, not confirmed via screenshot.

**badge** proposes a small pill treatment (e.g., "1% with Every Purchase" or "Picky Eater Approved 80%") in the bright lime, matching the celebratory, stat-driven callouts seen in the page text under "Backed by Science."

**search** and **testimonial-card** are additional proposed patterns: search reflects a standard rounded input pattern common to Shopify themes (not directly observed here), and testimonial-card supports the customer-quote blocks (Tammy Merecka, Shadriana & Branden, Gaby Monterrey) referenced in the page content, using a soft card surface with a teal accent rule.

## Responsive Behavior

This is a recommended breakpoint system, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column stacking; nav collapses to hamburger; header height ~60px per `--HEADER-HEIGHT-MOBILE` |
| Tablet | 600–1024px | Two-column product grids; header ~66px per `--HEADER-HEIGHT-MEDIUM` |
| Desktop | >1024px | Multi-column grids, full nav bar at 77px per `--HEADER-HEIGHT` |

Touch targets should target a minimum of 44px height (matching the Shopify accelerated-checkout button's `clamp(25px, …, 55px)` sizing observed in vendor CSS). Navigation collapse and carousel/flickity behavior (prev/next buttons at 40px) are proposed conventions inferred from theme CSS, not confirmed via live interaction testing.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is built from static CSS/text extraction only; no rendered screenshots, computed layout, or JavaScript-driven states were available.
- Semantic color roles (e.g., which teal/green serves as "primary" vs. accent) are inferred from variable naming and typical pet-food brand convention, not confirmed visual hierarchy.
- All typography sizes, weights beyond the declared `500` heading weight, letter-spacing, and line-heights are proposed defaults, not measured from rendered pages.
- Spacing and radius scales are conventional proposals; the only concrete radius reference in evidence is an unresolved `var(--RADIUS)` token with no pixel value supplied.
- Mobile/tablet layout, menu collapse behavior, and hover/focus/active interaction states were not observed and are marked proposed throughout.
- Custom font availability, licensing, and exact GTWalsheim weight files were not verified; generic sans-serif fallbacks are assumed for implementation.
- Utility colors sourced from third-party Shopify checkout/wallet CSS (blues, alert red/pink) are preserved as functional system colors and should not be treated as core brand palette.
