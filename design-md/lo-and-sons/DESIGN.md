---
version: alpha
name: "Lo & Sons"
source_url: "https://loandsons.com"
captured_at: "2026-09-28T09:29:23.807309+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lo & Sons presents as a family-run, design-forward travel and bag brand built on a
  restrained black-and-white foundation. The only font family present in evidence is
  Geist, used across navigation, announcement bars, and buttons, paired here with a
  system sans-serif fallback. The observed palette is dominated by true black (#000000)
  and white (#ffffff), with soft off-white surfaces (#f2f2f2, #f8f8f8) and light gray
  hairlines (#e6e6e6, #dedede) suggesting a minimal, editorial retail aesthetic typical
  of premium DTC luggage brands. A secondary set of saturated colors (#ebfa8a, #e0001a,
  #3ed660, #ee9441, #1990c6, #0a142f) appears in the raw CSS but is not tied to any
  labeled component in the supplied evidence; these are treated as inferred utility
  colors — sale/alert, success, warning, and informational states — commonly needed by
  a Shopify-based storefront with sale banners and form validation. Button and header
  color variables (white background, black foreground, hover to #f2f2f2) are directly
  observed and used to define the primary button and top navigation. All layout,
  spacing, and component sizing beyond these tokens are proposed conventions suited to
  a bag/backpack product catalog, not measured page geometry.

colors:
  primary: "#000000"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#262626"
  muted: "#00000066"
  hairline: "#e6e6e6"
  border-subtle: "#dedede"
  surface-soft: "#f2f2f2"
  surface-card: "#f8f8f8"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  overlay: "#00000026"
  accent: "#ebfa8a"
  sale: "#e0001a"
  success: "#3ed660"
  warning: "#ee9441"
  info: "#1990c6"
  info-hover: "#136f99"
  deep-navy: "#0a142f"
typography:
  display-xl: {fontFamily: "Geist, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Geist, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Geist, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Geist, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Geist, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Geist, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Geist, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    hoverBackgroundColor: "{colors.surface-soft}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    border: "1px solid {colors.border-subtle}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    overlayColor: "{colors.overlay}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  spec-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.border-subtle}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
    typography: "{typography.caption}"

## Components
**button-primary** models the observed header CTA pattern: a solid button with a white background and black text (`--button-background-color: rgb(255 255 255)`, `--button-color: rgb(0 0 0)`), hovering to `#f2f2f2`. Here it is generalized to a black-on-white primary action for add-to-cart and shop-now CTAs; the exact inverse (black bg / white text) is proposed for light-canvas contexts.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Compare," "Learn more") using the same ink/canvas pair without a filled background, inferred from the brand's minimal two-tone system.

**text-input** covers search and account/login fields; border and radius are proposed conventions since no explicit input CSS was supplied, using the confirmed hairline gray for borders.

**nav-bar** reflects the observed `.color-custom-top-sections` and header-menu rules: white background, black foreground, generated from directly measured `--color-background: #ffffff` and `--color-foreground: #000000` declarations.

**announcement-bar** is directly grounded in the `header_announcements` selector, which sets `--color-background: #000000` with light (palette-lightest) foreground text — modeled here as white-on-black for promotional messaging like "Extra 15% OFF."

**product-card** is proposed for grid listings of backpacks, weekenders, and laptop bags; surface and border tokens draw from the observed light neutrals (`#f8f8f8`, `#dedede`) to keep cards subtly separated on a white canvas.

**hero** is inferred for the homepage banner ("Stylish, versatile bags..."); no hero-specific CSS was supplied, so dark-surface and overlay treatment is a proposed pattern for full-bleed lifestyle imagery with white type.

**footer** is inferred as a dark, black-background band consistent with the brand's black/white system and typical Shopify footer conventions; no footer-specific selectors were present in evidence.

**badge** models sale/promo labeling (e.g., "SALE," "NEW") using the observed red (`#e0001a`) as a plausible sale-state color pulled from the raw palette, though no selector confirmed this exact usage.

**search** and **spec-chip** are proposed: search reuses the light-canvas/hairline-border input pattern; spec-chip is a category-appropriate proposed component for surfacing laptop-compatibility or capacity details (e.g., "Fits 15" laptop") as small rounded pills on product pages.

## Responsive Behavior
Recommended, not measured breakpoints:

| Range | Target | Notes (proposed) |
|---|---|---|
| ≤480px | Mobile | Single-column product grid, collapsed hamburger nav, stacked hero text |
| 481–768px | Large mobile/small tablet | 2-column product grid, sticky search icon |
| 769–1024px | Tablet | 2–3 column grid, horizontal nav may remain collapsed |
| 1025–1440px | Desktop | Full horizontal nav-bar, 3–4 column product grid |
| >1440px | Wide desktop | Max-width content container, 4+ column grid |

Touch targets should be at least 44×44px for nav and button-primary/button-secondary. Navigation is assumed to collapse into a drawer/hamburger below ~1024px, consistent with common Shopify theme behavior, but this was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variable dumps and page text, not a rendered or interactive audit. Several palette entries (`#ebfa8a`, `#8b0000`, `#006400`, `#3ed660`, `#ee9441`, `#1990c6`, `#136f99`, `#0a142f`, `#121212`) appeared in raw custom-property blocks without a clearly labeled component role and have been mapped to plausible utility functions (sale, success, warning, info) as an inferred best guess, not confirmed usage. Typography sizes, weights, letter-spacing, spacing scale, and rounded-corner values are proposed conventions layered onto the single confirmed font family (Geist); no font-size or spacing values were present in the supplied CSS. Hover/focus/active states beyond the one documented button hover (`#f2f2f2`) are proposed. No mobile layout, breakpoint behavior, animation, or interaction states were observed directly. Availability, licensing, and self-hosting terms for the Geist font on this storefront were not verified.
