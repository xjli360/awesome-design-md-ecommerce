---
version: alpha
name: "Fox Racing"
source_url: "https://foxracing.com"
captured_at: "2026-09-29T04:06:35.148373+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from the official foxracing.com storefront, confirmed by page copy referencing Moto, Mountain Bike, and Clothing shopping paths, dirt bike helmets, motocross jerseys, and MTB gear — consistent with the Motorcycle Apparel & Helmets category.
  The supplied palette mixes true brand-adjacent tones (black, white, near-black grays, and a muted racing red) with numerous utility colors traceable to the OneTrust cookie-consent widget and generic UI frameworks (e.g. #33c3f0, #68b631, #6c757d, #e9ecef). Those consent/utility hexes are excluded from brand role assignment; only tones plausible as storefront chrome (blacks, whites, grays, one red, and fluorescent yellow/lime commonly seen in moto/MTB gear photography) are mapped to design roles below. All color-to-role pairings are inferred, not measured from rendered brand assets.
  Typography favors the observed "rift" family for large condensed display headings — a face historically associated with action-sports branding — paired with the observed "archia" weights (bold/medium/regular) for UI text and body copy, falling back to system sans-serif. Font availability and licensing for rift/archia are unverified. Sizes, weights, and spacing/radius scales are proposed conventions, not extracted layout measurements.

colors:
  primary: "#bf242b"
  ink: "#0c0a08"
  ink-strong: "#000000"
  canvas: "#ffffff"
  body: "#2b2b2a"
  muted: "#595959"
  hairline: "#d6d6d6"
  surface-soft: "#f8f8f8"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  accent-yellow: "#ffff00"
  accent-lime: "#99ff00"
typography:
  display-xl: {fontFamily: "rift, Arial, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "rift, Arial, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "archia-bold, Helvetica Neue, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "archia-regular, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "archia-regular, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "archia-regular, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "archia-medium, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.accent-yellow}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink-strong}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-filter-panel:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the muted racing red (`{colors.primary}`) as a solid fill with white text, intended for primary calls to action such as "Shop Now" or "Add to Cart." This is a proposed treatment; no rendered button state was directly observed.

**button-secondary** is an outlined variant on white with a hairline border, suited to secondary actions like "Explore" links seen in the page copy. Hover/focus states are proposed, not observed.

**text-input** models a soft-gray field for search or account forms, using the light surface tone and a thin hairline border to stay legible against the mostly white/black storefront chrome.

**nav-bar** represents the top navigation implied by the "Moto / Mountain Bike / Clothing / Fox LAB" menu items and login/cart icons in the page text. A white background with dark ink text is proposed for legibility; actual sticky/scroll behavior was not observed.

**product-card** is inferred from the "Featured Products" grid described in the page text (e.g. DNGR Heavyweight Fleece Pullover Hoodie, $159.95). A card layout with title, price, and an optional "New" badge is proposed, using a near-white card surface against the canvas.

**hero** models the large promotional banner referenced by "MX27 Racewear Shop Collection" and "Founder's Helmet — Shop Now." A near-black background with a fluorescent-yellow accent nods to motocross gear photography conventions; this pairing is inferred, not measured.

**footer** is proposed as a dark ink band carrying the "Shop Moto / Shop MTB / Shop Clothing / Product Help / Support" link columns visible in the page text, set in small body type on a dark background for contrast.

**badge** represents the recurring "New" label seen throughout the featured-products list. A lime-green pill is proposed as a high-visibility accent consistent with fluorescent tones commonly used in the moto/MTB gear space; the exact rendered color was not confirmed.

**search** models the "What are you looking for?" prompt found in the page text, styled as a soft, low-emphasis input consistent with the rest of the light-surface UI.

**category-filter-panel** is a category-appropriate proposed component for gear-heavy taxonomies (Dirt Bike Helmets, Motocross Jerseys, MTB Pads, etc.), using the primary red to indicate an active filter chip against a white panel.

## Responsive Behavior

| Breakpoint | Width        | Notes (proposed) |
|---|---|---|
| Mobile | up to 599px | Single-column product grid; nav collapses to a hamburger/menu icon; search and cart icons remain visible in a condensed top bar. |
| Tablet | 600–1023px | Two-column product grid; primary nav items may wrap into a secondary row or overflow menu. |
| Desktop | 1024px+ | Full horizontal nav (Moto / Mountain Bike / Clothing / Fox LAB); multi-column product and hero layouts. |

Touch targets are recommended at a minimum of 44×44px for nav, cart, and filter controls. This table is a general responsive recommendation based on common e-commerce patterns, not a measurement of foxracing.com's actual rendered breakpoints or JavaScript behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered screenshots, computed layout, or interaction states (hover, focus, open menus, cart drawer) were observed. The supplied color palette contains a large number of values traceable to the OneTrust cookie-consent widget and generic UI/utility frameworks (e.g. #33c3f0, #68b631, #6c757d, #e9ecef, #212529); these were deliberately excluded from brand-role mapping, but the remaining "brand" colors (black, white, grays, red, yellow, lime) are still inferred assignments, not confirmed against live brand style guides. Font roles assigned to "rift" and "archia" variants are based on observed font-family declarations in the site's CSS bundle; actual licensing, weight availability, and correct fallback stacks were not verified. All typography sizes, spacing values, radius scale, and component states (hover/active/disabled) are proposed conventions rather than measured site behavior. Mobile/tablet layout and menu-collapse behavior were not observed and are recommendations only.
