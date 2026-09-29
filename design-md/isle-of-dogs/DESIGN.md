---
version: alpha
name: "Isle of Dogs"
source_url: "https://iodogs.com"
captured_at: "2026-09-29T03:57:41.664371+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Isle of Dogs presents as a Shopify-based grooming storefront blending a clinical,
  salon-grade palette with a signature teal accent. The observed body copy sits on
  a white canvas (#ffffff) in a dark charcoal (#262626), while headings, the logo
  wordmark, and section titles consistently use a softer graphite (#494949) set in
  Questrial, a rounded geometric sans. Buttons and interface labels are set in
  Figtree at medium weight, giving commerce controls a slightly friendlier tone
  than the editorial headings. A recurring teal (#00bbb4, with brighter #3cfff8 and
  deeper #005552 variants) is treated here as the brand's primary accent, likely
  used for links, active states, and small brand marks, though its exact UI role
  is inferred rather than confirmed. Muted grays (#939393, #656565) appear on
  secondary text like prices. A blue pairing (#1990c6/#136f99) belongs to Shopify's
  native accelerated-checkout button and is kept distinct from brand teal rather
  than merged into it. Card and hairline surfaces are drawn from the theme's light
  gray family (#e4e4e4, #f7f7f7, #eeeeee). This interpretation favors clean product
  grids, coat-type/coat-need filtering, and a calm, professional-salon aesthetic
  over decorative flourish.

colors:
  primary: "#00bbb4"
  ink: "#262626"
  canvas: "#ffffff"
  body: "#494949"
  muted: "#939393"
  hairline: "#e4e4e4"
  surface-soft: "#f7f7f7"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-bright: "#3cfff8"
  accent-deep: "#005552"
  link: "#1990c6"
  link-hover: "#136f99"
  alert: "#d60000"
  success: "#108144"
typography:
  display-xl: {fontFamily: "Questrial, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Questrial, sans-serif", fontSize: 30px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Questrial, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Source Sans Pro, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Source Sans Pro, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Source Sans Pro, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 15px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.caption}"
    priceColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  coat-finder-card:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders commerce actions such as "Add to Cart" against the teal accent, an inferred elevation of the brand's recurring #00bbb4 into a call-to-action role; no live hover/focus state was observed, so those remain proposed.

**button-secondary** is a bordered, transparent alternative for lower-priority actions (e.g. "View cart"), using the graphite body color on a white ground with the same Figtree button typography.

**text-input** covers search boxes and account/checkout fields, following the theme's light hairline border and body-copy color; padding and radius are proposed conventions, not measured from markup.

**nav-bar** models the header/mega-nav structure implied by the large "By Collection / By Coat Type / By Coat Need" menu list, using the graphite logo/heading color on white with a hairline division; height and collapse behavior are proposed.

**product-card** represents shampoo/supplement listings ("No. 12 Triple Strength...", "Silky Oatmeal Shampoo") with a Questrial-derived title and a small muted price line matching the observed 13px/#939393 price rule.

**hero** proposes the "where every dog shines" brand statement treatment: a soft gray section background, large Questrial display type, and body copy in the observed sans body font; exact hero markup was not inspected.

**footer** is inferred as a dark-ink band echoing the site's charcoal body color inverted for contrast, carrying secondary navigation (Distributors, Guarantee, Affiliate Program) in small body type; this contrast direction is proposed, not confirmed from footer-specific CSS.

**badge** covers sale/notification chips, using the observed alert red (#d60000) as a plausible sale-tag color pulled from the palette; no badge markup was directly evidenced.

**search** mirrors text-input styling for the header search affordance referenced by `.header-search-button` selectors in the theme CSS, using the chiko-icons glyph font noted in the evidence.

**coat-finder-card** is a category-specific component proposed for the site's "Coat Check" quiz and "By Coat Type / By Coat Need" filtering system, a distinguishing feature of this grooming brand; styling borrows the primary teal as an accent and surface-card gray, but the actual quiz UI was not observed in the supplied CSS.

## Responsive Behavior
This is a recommendation, not measured site behavior; no breakpoints, media queries, or mobile markup were present in the supplied evidence.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| sm        | 0–599px    | Single-column product grid, collapsed hamburger nav, stacked hero |
| md        | 600–959px  | Two-column product grid, condensed mega-nav |
| lg        | 960–1279px | Three/four-column grid, full horizontal nav with mega-menu flyouts |
| xl        | 1280px+    | Max-width content container, four+ column grid |

Touch targets on buttons and nav items should be at least 44px tall per the `--shopify-accelerated-checkout-button-block-size` default observed in the checkout CSS; mega-nav dropdowns should collapse into accordions below `md`.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/text extraction and carries the following limitations: no DOM screenshots, computed layout, or responsive breakpoints were captured, so all spacing scale values, the responsive table, and component padding/radii are proposed conventions rather than measured facts. The semantic role of the teal accent family (#00bbb4, #3cfff8, #005552) as "primary brand color" is inferred from repetition, not from an explicit brand style guide. Colors such as #7e57c5 (purple), #ffff00, and additional grays present in the raw palette were not confidently mapped to a role and were omitted rather than guessed. Font weights/sizes for Questrial and Figtree beyond the two explicitly observed rules (h1 ~2.14rem, price 13px) are estimated. Source Sans Pro's use as the body font is inferred from the palette of font families supplied alongside Arial/Helvetica fallbacks; it was not directly tied to a body-text CSS rule in the evidence. No hover, focus, active, or error states were observed for inputs or cards. Custom font licensing/self-hosting (Questrial, Figtree) was not verified beyond their appearance in `@font-face`-adjacent theme CSS references. Mobile navigation collapse, drawer behavior, and touch interactions were not observed and are presented only as proposed guidance.
