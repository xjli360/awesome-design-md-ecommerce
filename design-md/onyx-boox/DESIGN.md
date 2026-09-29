---
version: alpha
name: "Onyx Boox"
source_url: "https://shop.boox.com"
captured_at: "2026-09-28T04:56:59.651398+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from the BOOX Shop storefront, the official e-commerce site for Onyx's E Ink tablets, e-readers, and accessories. The observed palette is dominated by neutral grays and near-blacks (#000000, #232323, #3c3c3c, #333333, #787878) against white and off-white surfaces (#ffffff, #f9f9f9, #f8f8f8, #fafafa), consistent with a photography-led product catalog that lets device screens and hardware carry visual weight. A warm red-orange (#ff674b) appears in the supplied palette and is assigned here as the primary accent/CTA color, since no button-specific rule confirmed its role in the extracted CSS; this mapping is inferred, not observed. A darker neutral (#3c3c3c) is confirmed as the header-top background with white text, so it is retained as a "dark-surface" utility for top bars or footers. Placeholder and helper text use a mid-gray (#787878), and hairlines/dividers are proposed from light grays present in the palette (#e6e6e6, #cccccc). Typography uses the observed system-font stack (Roboto, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif) with FontAwesome for iconography; no proprietary display typeface was present in the evidence, so all type sizing below is a proposed scale layered onto the confirmed family. Layout components (nav, hero, product card, spec table) are proposed patterns appropriate to an E Ink device storefront, not measured DOM structures.

colors:
  primary: "#ff674b"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#787878"
  hairline: "#e6e6e6"
  surface-soft: "#f9f9f9"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  dark-surface: "#3c3c3c"
  on-dark: "#ffffff"
  border-strong: "#cccccc"
  danger: "#e95144"
typography:
  display-xl: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    iconColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    hairline: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.lg}"

## Components

**button-primary** is the main commerce action (Add to Cart, Check Out) and uses the inferred accent red-orange against white text, since no explicit button rule was present in the supplied CSS but a vivid accent color exists in the palette. Hover/active states are proposed, not observed.

**button-secondary** covers lower-emphasis actions (Continue Shopping, Explore Now variants) as an outlined style on white, using the neutral border color confirmed in dropdown-separator CSS. This keeps secondary CTAs visually quiet against product photography.

**text-input** models the account/login fields (Email Address, Password) and newsletter signup, using the confirmed placeholder gray (#787878) and a light card background consistent with the observed search-bar background.

**nav-bar** represents the sticky header (`.sticky-wrapper.is-sticky`), which is confirmed to shift from off-white (#f9f9f9) to pure white (#fff) on scroll. Logo and icon colors are confirmed black (#000000); the utility bar above it uses the dark-surface tone.

**product-card** is a proposed pattern for the "Popular Products" grid (Note Air6 C accessories, BOOX Picco, Palma 3) inferred from the page text listing product names and prices; no card DOM/CSS was supplied, so spacing and border are proposed.

**hero** models the large narrative sections ("From Chaos to Clarity," "The Outside Office") with a plain white canvas and dark ink text, reflecting the site's photography-forward, editorial tone; exact hero background treatment (image/gradient) was not observed.

**footer** uses the confirmed dark-surface color (#3c3c3c) with white text and links, matching the `.header-top` rule, extended here to the footer utility links (Guide, FAQ, Return, Policies) shown in the page text.

**badge** is proposed for "Sold Out" labeling seen on BOOX Picco, using a warning-red pulled from the palette (#e95144); exact badge shape/placement is not observed and is a UI convention proposal.

**search** models the header search overlay, using the confirmed search-bar background (#f8f8f8), placeholder gray, and black icon fill from `.icon-search`.

**product-spec-table** is a category-appropriate addition for E Ink device spec sheets (screen size, resolution, OS, formats supported) referenced in the page copy ("26 Digital Formats," "Open Android OS"); no table markup was supplied, so this is a proposed structural pattern only.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column product grid, collapsed nav into a hamburger/search icon row |
| tablet | 600–1023px | 2-column product grid, sticky header remains condensed |
| desktop | 1024–1439px | 3–4 column product grid, full horizontal nav |
| wide | 1440px+ | Max-width content container, hero imagery scales up |

Touch targets for buttons and nav icons should be at least 44×44px. The header's language/currency dropdown and cart drawer should collapse into a full-screen overlay below the tablet breakpoint. Sticky-header background transition (`#f9f9f9` → `#fff`) should be preserved across breakpoints since it is a confirmed CSS state.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or JavaScript-driven interactions (cart drawer, dropdowns, sticky scroll thresholds) were directly observed beyond the literal selectors supplied. The assignment of `primary` to `#ff674b` is inferred from palette presence, not from a confirmed button/link rule. Font sizes, weights, letter-spacing, spacing scale, and rounded-corner values are proposed defaults layered onto the one confirmed font stack (Roboto/system sans-serif); no custom or licensed webfont was found in the evidence, and no font-loading/licensing was verified. Component definitions (product-card, hero, footer, badge, spec-table) are conventional e-commerce patterns proposed for this category and are not drawn from actual markup or component CSS. Mobile/tablet layout, breakpoint values, and touch-target sizing are recommendations only and were not measured on the live site. Color roles beyond the four explicitly confirmed in the supplied CSS (`.header-top` dark surface, `.search-bar` light surface, black icon/text, white sticky background) are inferred from general palette plausibility, not from direct role evidence.
