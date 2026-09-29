---
version: alpha
name: "Redbarn Pet Products"
source_url: "https://redbarn.com"
captured_at: "2026-09-28T09:16:28.197671+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Redbarn's storefront is built on a Shopify Dawn-derived theme layered with a
  saturated barn-red identity (#ae2227, reinforced by #b2282d, #ad2227 and
  #c93b42 variants) against a warm cream/white base (#ffffff, #f9f3e9,
  #f8f2e9). Foreground text uses a near-black (#090909) rather than pure
  black, and a soft cream (#efe9e0) is used as a border/hairline tone in the
  loyalty-widget CSS. Custom display faces (NovecentoSlabDemiBold,
  ITCFranklinGothicLTProDemi/Book) point to a rugged, slab-serif-adjacent
  headline system paired with a plainer sans body, though Heebo and Libre
  Franklin also appear and may serve as loaded fallbacks — their exact
  application to headings vs. body is inferred, not confirmed by observed
  DOM. A secondary blue (#1990c6/#136f99) appears only inside a third-party
  Shopify accelerated-checkout button and is treated as a vendor-injected
  utility color, not a brand color. Small amounts of purple (#6a5caf,
  #887cc1) and soft pink/red tints (#edbcb8, #ebc8c9, #f3dedf) suggest
  supporting badge or highlight states rather than primary UI. This
  interpretation proposes a warm, farm-to-bowl retail system: red CTAs on
  cream/white surfaces, generous letter-spacing on body copy (per observed
  0.06rem tracking), and card-based merchandising suited to treats/food SKUs
  with review counts and subscription pricing.

colors:
  primary: "#ae2227"
  primary-deep: "#881b1e"
  accent-red: "#c93b42"
  ink: "#090909"
  canvas: "#ffffff"
  body: "#090909"
  muted: "#303030"
  hairline: "#efe9e0"
  surface-soft: "#f9f3e9"
  surface-card: "#ffffff"
  surface-alt: "#f8f2e9"
  on-primary: "#ffffff"
  border-gray: "#dedede"
  tint-pink: "#edbcb8"
  tint-pink-soft: "#f3dedf"
  accent-purple: "#6a5caf"
  utility-link: "#1990c6"
  utility-link-hover: "#136f99"
typography:
  display-xl: {fontFamily: "NovecentoSlabDemiBold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "NovecentoSlabDemiBold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "ITCFranklinGothicLTProDemi, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "ITCFranklinGothicLTProBook, Heebo, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.6px}
  body-sm: {fontFamily: "ITCFranklinGothicLTProBook, Heebo, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "ITCFranklinGothicLTProBook, Heebo, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "ITCFranklinGothicLTProDemi, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 1px}
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
    borderWidth: "3px"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
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
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    priceColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  quiz-cta-card:
    backgroundColor: "{colors.surface-alt}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"

## Components
**button-primary** carries the observed `--color-button` red (#ae2227) with white text, matching the CSS custom-property pairing found in the site's `:root` and repeated in the featured-collection override (#b3282d family). Used for "Shop Now" and add-to-cart actions.

**button-secondary** reflects the outline pattern seen on `.rebuy-product-actions` buttons: white fill, red 3px border and red text — an existing upsell/cart-drawer pattern generalized here as the secondary CTA style.

**text-input** is a proposed pattern; no explicit input CSS was supplied, so border and radius values are inferred from the theme's general hairline/border-radius tokens (`--rivo-aw-border-color`, `--rivo-aw-border-radius`).

**nav-bar** is inferred from the mega-menu-style content (Dog Food, Treats & Chews, Cat Food, Build A Routine, About) implied by the page text; exact visual styling, sticky behavior, and dropdown treatment were not observed and are proposed.

**product-card** draws directly on the `.rivo-product-price` red text color and the `.contains-card--product` border-radius/shadow custom properties, applied to the bestseller grid (First-Five Kibble, Bully Stick, Collagen Stick, Braided Bully Stick) with star-rating and price display.

**hero** is proposed for the "Redbarn Bully Sticks — Single-ingredient Chews Dogs Love" banner; the cream background (#f9f3e9/#f8f2e9) is observed elsewhere as a section background, applied here by inference since hero-specific CSS was not supplied.

**footer** is proposed; only global foreground/background tokens were observed, so a dark inverse treatment is suggested but not confirmed by supplied footer CSS.

**badge** generalizes the "BESTSELLER" label seen repeatedly in the product grid; pill shape and red fill are proposed, exact source styling not supplied.

**search** is proposed based on the presence of a "Search" nav item; no search-bar CSS was included in evidence.

**quiz-cta-card** is a category-appropriate component modeled on the "Build A Routine / Take the Quiz" and "Redbarn Routine" content, using the cream surface and red accent to distinguish this interactive nutrition-finder module from standard product cards.

## Responsive Behavior
Proposed breakpoints (not measured from live layout): mobile ≤599px (single-column, stacked nav collapsing to a hamburger/drawer, full-width product cards), tablet 600–989px (2-column product grids, condensed nav), desktop ≥990px (multi-column mega-menu nav, 3–4 column product grids, hero at full section height). Touch targets should be a minimum 44px height, matching the observed Shopify accelerated-checkout button's `clamp(25px, …, 55px)` sizing pattern. Nav mega-menus are assumed to collapse into an accordion on mobile. All breakpoint values, collapse thresholds, and touch-target sizing beyond the checkout-button clamp are recommendations, not observed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions (cart drawer, quiz flow, mega-menu behavior) were observed. Font-role assignments (which faces apply to headings vs. body vs. buttons) are inferred from filenames and general theme conventions, not confirmed via computed `font-family` on specific elements — Heebo and Libre Franklin's actual usage is unverified. Pixel sizes for all typography tokens beyond the single confirmed `1.5rem` body rule are proposed estimates assuming a 10px root font-size, not directly measured. The muted/gray and hairline color role assignments are best-fit choices among several similar grays/creams in the observed palette (e.g., #dedede, #d6d6d6, #dadada, #efe9e0) and could be swapped without contradicting evidence. Mobile menu structure, search UI, and footer composition were not present in supplied CSS and are marked proposed. Custom font licensing and self-hosting terms for ITCFranklinGothicLTPro and NovecentoSlabDemiBold were not verified and must be confirmed with Redbarn/foundry before reuse.
