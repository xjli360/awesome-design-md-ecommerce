---
version: alpha
name: "Herschel"
source_url: "https://herschel.com"
captured_at: "2026-09-28T05:04:14.205270+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Shopify theme CSS (app.css) for Herschel's
  US storefront, a bag-and-luggage retailer whose Weekender/duffle line sits
  inside the "Bags" and "Luggage & Travel" navigation. The observed palette is
  neutral-forward: true black (#000000), warm near-blacks (#2d2926, #413e3d),
  and a family of light greys/off-whites (#f4f4f4, #f3f5f5, #dddddd) that
  suggest a restrained, editorial product-photography aesthetic rather than a
  saturated brand color. No single accent hex recurs enough across the
  evidence to confirm a "brand color," so primary is inferred as black,
  consistent with common minimalist DTC bag-brand conventions and the site's
  heavy reliance on var(--text-color)/var(--bg-color-base) custom properties.
  Status colors (red #d60a0a, green #448a10, amber #ffcc44, blue #007aff) are
  treated as functional (error/success/warning/link), not brand accents.
  Typography combines CheltenhamBdCnBT, a condensed serif, for headings
  (h1–h3 use var(--font-heading)) with Graphik for body copy and UI text
  (var(--font-body), 1.6rem base), and QuadrantTextMono appears in the font
  stack, inferred here for price/SKU-style mono labels. Layout tokens
  (--iam-spacing-*, --button-spacing) confirm a spacing-variable system exists,
  though exact pixel values are not exposed in the supplied rules and are
  therefore proposed.

colors:
  primary: "#000000"
  ink: "#2d2926"
  canvas: "#ffffff"
  body: "#413e3d"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#f3f5f5"
  on-primary: "#ffffff"
  backdrop: "#0000004d"
  error: "#d60a0a"
  error-bg: "#f8d7da"
  success: "#448a10"
  success-bg: "#d1e7dd"
  warning: "#ffcc44"
  warning-bg: "#fff3cd"
  link: "#007aff"
typography:
  display-xl: {fontFamily: "CheltenhamBdCnBT, serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "CheltenhamBdCnBT, serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "CheltenhamBdCnBT, serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Graphik, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Graphik, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Graphik, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Graphik, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
  mono-label: {fontFamily: "QuadrantTextMono, monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleColor: "{colors.ink}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.mono-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** is the solid black call-to-action pattern proposed for "Add to Cart" / "Shop Now" actions, mirroring the site's black-on-white checkout-button styling referenced in the rebuy cart CSS (`background`, `border:0`, `font-weight:var(--font-weight-medium)`). State transitions (hover/active) are not observed and are proposed as a subtle opacity or fill shift.

**button-secondary** is an outlined variant using ink-colored text and border for lower-emphasis actions (e.g., "Learn More," filter toggles). It is inferred from the presence of paired primary/secondary action patterns typical of Shopify themes; no distinct secondary-button rule was present in the supplied CSS.

**text-input** covers search fields, newsletter signup, and form fields. Border and radius are proposed defaults consistent with the site's flat, hairline-bordered aesthetic (`--border`, `--border-color-dark` custom properties referenced in cart-item buttons).

**nav-bar** represents the top navigation shown in the page-text evidence (Bags, Luggage & Travel, Accessories, Apparel & Headwear, Kids submenus). Background/text colors are inferred as canvas/ink for a light, standard header; the multi-level submenu structure is confirmed by content but its visual treatment is not.

**product-card** is proposed for grid listings (e.g., Weekender duffle tiles), pairing a body-weight Graphik title with a monospace price label, since QuadrantTextMono is present in the font stack and monospace figures are a common pattern for price/SKU display in this type of theme; this pairing is inferred, not directly observed on a product tile.

**hero** models large campaign banners referenced in text content ("Quilted Capsule – Shop Now," "Heritage Hardshell Large Carry-On – Shop Now"), using the large clamp-based `h1` heading rule observed in CSS (`clamp(3.2rem,...,6.8rem)`) as the basis for display-xl sizing.

**footer** is proposed as a dark, black-background section for consistency with the primary token, though no footer-specific selectors were present in the supplied evidence; this is a stylistic extrapolation, not a confirmed observation.

**badge** covers "Sale," "New," and promotional tags implied by the "Sale" and "New Arrivals" menu items; the red/error token is used as a plausible sale-badge color, though no badge-specific CSS rule was supplied.

**search** and **announcement-bar** round out the header region. The announcement-bar directly reflects observed page copy ("Free Ground Shipping* Enjoy free ground shipping on all orders +$75"), styled here as a full-width black bar with light text.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width       | Nav                          | Grid columns |
|------------|-------------|-------------------------------|--------------|
| sm         | 0–599px     | Collapsed hamburger menu      | 1–2          |
| md         | 600–959px   | Collapsed hamburger menu      | 2            |
| lg         | 960–1279px  | Full horizontal nav w/ submenus | 3          |
| xl         | 1280px+     | Full horizontal nav w/ submenus | 4          |

Touch targets should be a minimum of 44×44px for cart, quantity, and remove-item controls, consistent with the `min-height:36px;min-width:36px` values seen on rebuy cart buttons (rounded up here for accessibility). Multi-level category submenus (Bags, Luggage & Travel, etc.) should collapse into an accordion/drill-down pattern on narrow viewports; this collapse behavior is proposed and was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and page-text extraction only; no live rendering, computed styles, or DOM interaction states were captured. Custom property values (`--text-color`, `--bg-color-base`, `--border-color-dark`, `--font-heading`, `--font-body`, `--font-weight-regular/medium/bold`, `--iam-spacing-*`, `--button-spacing`) are referenced throughout the CSS but their resolved values were not present in the supplied evidence, so all hex-to-role mappings, spacing scale values, and font-weight numerics above are inferred/proposed rather than confirmed. No brand accent color could be confirmed beyond black/neutral tones; status colors (red/green/amber/blue) are assumed functional rather than decorative. Hover, focus, active, and disabled states were only partially referenced (e.g., `:focus-visible` on modal close buttons) and are otherwise proposed. Mobile/tablet layout, menu collapse behavior, and product-card responsive reflow were not observed and are recommendations only. Availability and licensing of CheltenhamBdCnBT, Graphik, and QuadrantTextMono for reuse outside Herschel's own site were not verified.
