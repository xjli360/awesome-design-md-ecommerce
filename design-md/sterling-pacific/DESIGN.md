---
version: alpha
name: "Sterling Pacific"
source_url: "https://sterlingpacific.com"
captured_at: "2026-09-29T04:18:15.450627+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sterling Pacific's evidence reflects a restrained, engineering-led aesthetic consistent with a premium hard-shell luggage manufacturer. The observed palette is dominated by near-neutral darks (#212121, #303030) against white canvas, with light greys (#f7f7f7, #f6f6f6, #f1f1f1) used for cards and secondary surfaces, and a muted mid-grey (#616161) for de-emphasized text such as struck-through prices. A small green (#24b263) appears tied to discount/price-success states, and a purple (#7367f0) appears on a third-party "free gifts" widget button; both are treated here as secondary accents rather than core brand color, since their functional scope in the source CSS is narrow. Two custom font families are declared — BioSans (Bold/ExtraBold/Regular) and Montserrat — with BioSans inferred as the display/heading face given its weight variants, and Montserrat inferred as a supporting body/UI face; this pairing assignment is a reasonable but unverified interpretation. The resulting system favors dark-on-white headers, minimal rounding, and generous whitespace to echo the brand's language of aluminum, rivets, and Italian leather — precision materials rendered in a quiet, confident interface rather than a decorative one.

colors:
  primary: "#212121"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#303030"
  muted: "#616161"
  hairline: "#e0e0e0"
  surface-soft: "#f7f7f7"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  border-light: "#f1f1f1"
  accent-success: "#24b263"
  accent-purple: "#7367f0"
typography:
  display-xl: {fontFamily: "BioSans-ExtraBold, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "BioSans-Bold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "BioSans-Bold, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "BioSans-Regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "BioSans-Bold, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    mutedPriceColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  material-spec-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.border-light}"

## Components

**button-primary** uses the dark near-black `#212121` observed on header/cart buttons and freegifts CTAs, paired with white text; this is the highest-confidence interactive color pairing in the evidence, directly sourced from `.button` and `.bogos-bundles-button-add` rules.

**button-secondary** is a proposed outline treatment for lower-emphasis actions (e.g., "Continue browsing"), using canvas background and hairline border since no dedicated secondary-button CSS was supplied — this pattern is inferred, not observed.

**text-input** is a proposed field style for search/cart quantity inputs; border and radius values are estimated from the general hairline/rounded scale since no input-specific CSS was in evidence.

**nav-bar** reflects the observed `--header-background: #212121` with white menu-link text (`color: #ffffff !important`), giving a dark persistent header — a fairly confident mapping from `:root` and `.site-nav .menu-link` rules.

**product-card** is inferred from product-listing text ("40L Cabin Travel Case… Titanium $4,200 $5,250… 5.0/5") paired with the light card surface `#f6f6f6` and border `#f1f1f1` seen in `--cart-image-border`; struck-through original prices use the muted `#616161` tone observed on `.sca-gift-product-original-price`.

**hero** is a proposed full-width introductory block using canvas background and the largest display type scale; no hero-specific selector was present in evidence, so sizing is proposed.

**footer** reuses the dark header color for visual bookend consistency (an inferred pattern), containing the observed link list (Store, Reviews, About, Returns, Press, Careers) and warehouse address text.

**badge** models the discount/price-success green `#24b263` seen on `.sca-gift-product-discount-price`, proposed as a pill for savings callouts like "$4,200 $5,250."

**search** is a proposed lightweight overlay field using the soft grey surface `#f7f7f7`, styled consistent with the "Open search" control referenced in page text; exact search UI was not observed.

**material-spec-block** is a category-appropriate proposed component for surfacing engineering claims (5052/A380 aluminum, SAE 304 rivets, SATRA testing) in a bordered, softly-shaded panel — reflecting the brand's emphasis on material specification copy, though no dedicated spec-block CSS was supplied.

## Responsive Behavior

Recommended, not measured:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <480px | Single-column product grid, collapsed nav behind menu icon (site text references "Open menu"/"Close sidebar") |
| tablet | 480–960px | 2-column product grid, condensed header |
| desktop | 960–1280px | 3-column product grid, full nav-bar |
| wide | >1280px | Max-width content container, generous section spacing |

Touch targets for buttons and nav links should be at least 44px tall. The observed "Open menu"/"Close sidebar" text strongly suggests an off-canvas mobile menu pattern, but its transition, width, and trigger styling were not present in the supplied CSS and are therefore not specified here.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS custom properties, isolated selector/declaration pairs, and page text — no rendered layout, computed box model, animation, or JS-driven interaction was observed. Font weights, sizes, and line-heights for BioSans/Montserrat are proposed defaults, not extracted from source stylesheets (no `font-size` or `font-weight` declarations were supplied for these families). The role of `#7367f0` (purple) and several near-identical greys (`#f0f0f0`, `#f1f1f1`, `#f3f3f3`, `#f5f5f5`, `#f6f6f6`, `#f7f7f7`) is inferred by proximity to third-party widget code (freegifts/bogos apps) and may not reflect core storefront design intent. Hairline/border colors were approximated from the closest observed hex since the true header/body border values are rgba-alpha tokens (`rgba(33,33,33,0.08)`) not expressible as flat hex without invention. Mobile menu behavior, hover/focus states, cart drawer layout, and breakpoint pixel values are proposed conventions, not measured. Licensing and availability of the proprietary BioSans font family were not verified; a sans-serif fallback should be assumed in production until confirmed.
