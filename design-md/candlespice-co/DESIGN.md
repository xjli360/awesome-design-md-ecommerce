---
version: alpha
name: "Candlespice Co."
source_url: "https://candlespice.com"
captured_at: "2026-09-28T09:14:09.187203+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Candlespice Co. is a Cincinnati-area maker of small-batch soy candles, wax
  bars, room sprays, and pottery vessels, sold through a Shopify storefront.
  The observed theme CSS defines a warm, understated palette: a near-black
  ink (#201c22) for text and links, a soft cream (#f7ede2) as the primary
  button, border, and announcement-bar color, and white (#ffffff) as the
  page and footer background. A muted coral (#ef6461) is reserved for sale
  price and cart-dot accents, giving the otherwise neutral system a single
  warm highlight. Two greys (#f2f2f2, #f6f6f6) round out dimmed surfaces and
  disabled states.

  Typography pairs Poppins (headers, buttons) with Montserrat (body text),
  both sans-serif with generic fallback declared in the CSS custom
  properties. Only one header size (28px) and one base size (14px) are
  present in the evidence; larger display sizes below are proposed
  extrapolations for a hero/landing hierarchy, not measured values. Buttons
  are flat (border-radius: 0 observed), so the rounded scale here is offered
  as an optional, unobserved refinement rather than a documented pattern.
  Component definitions below (product cards, collection tiles, hero,
  footer) are inferred from page-text content and typical Shopify theme
  structure, since no layout/box-model CSS beyond buttons and type was
  supplied.

colors:
  primary: "#f7ede2"
  primary-dim: "#f1e1ce"
  ink: "#201c22"
  canvas: "#ffffff"
  body: "#201c22"
  muted: "#444444"
  hairline: "#f7ede2"
  surface-soft: "#f2f2f2"
  surface-card: "#f6f6f6"
  surface-image: "#f4f4f4"
  input-bg-dark: "#e6e6e6"
  on-primary: "#201c22"
  on-dark: "#ffffff"
  accent: "#ef6461"
  black: "#000000"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: "40px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0em"}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: "28px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0em"}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: "20px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0em"}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.025em"}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.025em"}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.025em"}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.42, letterSpacing: "0em"}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
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
    borderBottomColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-image}"
    textColor: "{colors.body}"
    priceColor: "{colors.accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTopColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  scent-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    activeBorderColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** uses the observed `--colorBtnPrimary` cream fill with dark ink text, flat corners (border-radius: 0 was explicitly observed on `.btn`), and Poppins per the header font variable applied to buttons. Hover state reuses the same fill (observed), so no distinct hover treatment is documented; a subtle opacity or padding shift is proposed but unverified.

**button-secondary** mirrors the observed `.btn--tertiary`: transparent background, a 1px border in the hairline cream, 12px caption-weight type, and a hover state that darkens the border to ink (observed in CSS). Padding is approximated from the observed 6px/10px values to the nearest spacing tokens.

**text-input** is not present in the supplied CSS; background, border, and radius are proposed conventions consistent with the neutral palette, since no input styling was included in the evidence.

**nav-bar** is inferred from the page-text navigation list (Products, Signature Collection, City Lights, About Us, Connect, Cart, Search) and the observed `--colorNav`/`--colorNavText` variables (white background, ink text) plus the `.site-header` bottom border in cream.

**product-card** is proposed to hold candle/soap imagery against the observed light-grey `--colorSmallImageBg`, with sale pricing in the observed coral accent color, matching `--colorSalePrice`.

**collection-tile** is a category-appropriate component for the site's named collections (City Lights, Noire, Blanc, Pottery). Its soft-grey surface and title-scale type are proposed, not measured.

**hero** is inferred from the large banner copy ("100% All Natural Soy Candles," "Special Release Pumpkin Collection") and the observed `--colorHeroText: #ffffff`, implying a dark image or ink-toned background beneath white hero text; the exact hero background photograph/overlay was not supplied.

**footer** uses the observed `--colorFooter`/`--colorFooterText` pairing (white on ink text) and the hairline border color for a top divider, holding the resource/legal links and newsletter form visible in the page text.

**badge** is proposed for sale/new-arrival tags, drawing on the observed `--colorSaleTag`/`--colorSaleTagText` pairing (white tag, coral text) rather than a directly observed badge component.

**search / scent-selector** are proposed utility components: search reflects the "Search Site navigation" text found in the evidence, while scent-selector is a category-specific pattern for filtering by the many named scent notes (Agave, Cedar Vanilla + Cinnamon, etc.) listed in the page text; neither's visual styling was present in the supplied CSS.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width       | Nav behavior                | Grid columns |
|-----------|-------------|------------------------------|--------------|
| Mobile    | <600px      | Collapsed/hamburger menu     | 1            |
| Tablet    | 600–959px   | Condensed inline nav         | 2            |
| Desktop   | ≥960px      | Full horizontal nav          | 3–4          |

Touch targets on primary/secondary buttons should maintain a minimum 44px hit area even though the observed `.btn` padding (11px 20px at 16px type) yields a smaller visual box; add invisible padding on touch devices. Product-card and collection-tile grids should collapse to a single column below 600px, per typical Shopify-theme convention, though this was not confirmed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from a static CSS/text snapshot: no rendered layout, JavaScript-driven interaction (cart drawer, search overlay, menu animation), or responsive breakpoints from the live theme were observed, so all grid, breakpoint, and touch-target guidance above is proposed. Only two font-size variables (28px header, 14px base) and one explicit button font-size (16px) were present; every other typography size (display-xl/md, title-md, body-sm, caption) is an inferred extrapolation for hierarchy, not a measured value. Rounded-corner tokens beyond the observed `0px` on buttons are proposed and unverified against other UI elements. Spacing tokens map only approximately to the two observed padding pairs (11px/20px and 6px/10px); exact pixel-for-pixel button padding was rounded to the nearest scale step. Color roles for hero, product-card, and badge components are inferred from CSS custom-property names (e.g., `--colorHeroText`, `--colorSaleTag`) rather than directly observed rendered elements. Font licensing/self-hosting status for Poppins and Montserrat was not verified beyond their appearance in the `:root` font-family declarations.
