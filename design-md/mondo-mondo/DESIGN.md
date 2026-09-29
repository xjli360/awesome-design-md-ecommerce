---
version: alpha
name: "Mondo Mondo"
source_url: "https://mondo-mondo.com"
captured_at: "2026-09-29T03:56:35.212519+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Mondo Mondo's storefront CSS (Shopify Timber base plus a custom "mondo.scss"
  layer) shows a stark black-and-white foundation: white canvas (#ffffff),
  black body text and primary buttons (#000000), and a light gray disabled/
  surface state (#f6f6f6). Headings and nav links are forced into AGMed, an
  uppercase, weight-400 display face, while body copy runs on a HelveticaNeue/
  Helvetica/Arial stack at 14px/1.6 with a lighter 300 weight — a deliberate
  contrast between blocky uppercase titles and softer running text.
  A small warm-neutral family (#faf7f5, #f9f6f6, #fff6f6) and a red (#d02e2e)
  and blush (#ffdcdc) pairing appear alongside a green (#56ad6a) and mint
  (#ecfef0) pairing; these are not documented as brand colors in the CSS but
  are inferred here as a romantic/gift accent (tied to the "Queen of Hearts"
  copy) and an availability/stock-status accent respectively, reused sparingly
  against the black-and-white base rather than treated as primary brand hues.
  This interpretation keeps the minimal monochrome jewelry-editorial tone
  dominant, using color only as restrained, secondary signal.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#b6b6b6"
  hairline: "#e6e6e6"
  surface-soft: "#f6f6f6"
  surface-card: "#faf7f5"
  on-primary: "#ffffff"
  border-strong: "#333333"
  accent: "#d02e2e"
  accent-soft: "#ffdcdc"
  success: "#56ad6a"
  success-soft: "#ecfef0"
typography:
  display-xl: {fontFamily: "AGMed, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0.5px}
  display-md: {fontFamily: "AGMed, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0.5px}
  title-md: {fontFamily: "AGMed, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  body-md: {fontFamily: "HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "AGMed, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.42, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** mirrors the observed `.btn` rule: solid black background, white text, 700-weight uppercase-feeling label, and a small 3px-radius approximated here as `{rounded.sm}`. Hover/active states in CSS keep the same black fill, so no color-shift feedback is defined; a proposed subtle opacity or outline change on hover is not confirmed by the evidence.

**button-secondary** follows `.btn--secondary`: white fill with the same label style, gaining a light gray hover (#e6e6e6) and pressed (#ccc-adjacent) state per source rules. Used here for "View All" and filter actions seen in the nav text.

**text-input** is a proposed pattern for search and account fields; no explicit input CSS was supplied, so border, radius, and padding are inferred from the general hairline/spacing scale rather than measured.

**nav-bar** represents the header/mobile-nav row implied by `.mobile-nav__item a` styling (15px padding, dark hover text, light active background #e9e9e9). Desktop nav-bar layout is proposed, not observed, since only mobile-nav selectors were present.

**product-card** is a proposed jewelry-listing card using the warm off-white `surface-card` tone, intended for necklace/ring/earring grid tiles implied by the category text (Necklaces, Rings, Earrings). No card-specific CSS was in evidence; padding and radius are inferred.

**hero** reflects the homepage copy blocks ("Shop the Queen of Hearts," "SHOP FINE," "MONDO CLASSICS") using the large uppercase AGMed display style for titles and the lighter Helvetica body style for supporting lines. Exact hero layout/imagery is not confirmed by CSS.

**footer** is inferred from the footer-like text list (Account, Information, Connect, Contact, Careers, copyright) using small body typography and hairline dividers; no footer-specific selector was supplied.

**badge** is a proposed "In Stock" / availability indicator using the green/mint pairing (#56ad6a on #ecfef0) suggested by stock-related copy ("In Stock Items"); this color-to-meaning mapping is inferred, not verified in CSS.

**search** proposes a simple inset field style using the light gray surface tone for the search affordance referenced in the nav text; no dedicated search-input CSS rule was supplied.

**swatch-selector** is directly grounded in the observed `.swatch-container>.header` rule (AGMed, 12px, uppercase label); the swatch control itself (e.g., color/material dots for jewelry variants) is a proposed circular pattern appropriate to a handmade-jewelry catalog, not a measured component.

## Responsive Behavior

Proposed breakpoints (not measured from live site):

| Breakpoint | Width      | Notes                                  |
|-----------|------------|-----------------------------------------|
| mobile    | 0–599px    | Single-column, mobile-nav drawer active |
| tablet    | 600–899px  | 2-column product grid                   |
| desktop   | 900–1199px | Full nav-bar, 3-column product grid     |
| wide      | 1200px+    | 4-column product grid, max-width shell  |

Touch targets are recommended at a minimum 44×44px for cart, search, and swatch controls. The mobile-nav drawer (evidenced by `.mobile-nav__item`/`.drawer__close` rules) should collapse the primary nav into an off-canvas panel below the tablet breakpoint. This table is a recommendation only; no responsive/media-query behavior was present in the supplied CSS evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Color-to-role mapping (e.g., red/blush as a gift accent, green/mint as a stock badge) is inferred from adjacent copy, not confirmed by selector naming. Font roles for AGMed and the HelveticaNeue stack are directly evidenced; other listed families (EB Garamond, PlantLig, Cossette Titre, Kosugi, Xanh Mono) appeared in the raw font list but had no associated selector/role in the supplied CSS and are therefore excluded from the typography scale. All pixel sizes beyond the confirmed 14px body/12px caption are proposed, not measured. Border-radius values (e.g., the observed 3px button radius) are approximated to the nearest token in the fixed rounded scale. Mobile drawer visuals, hover/focus states beyond the button rules, and grid/column counts are not observed and are marked proposed throughout. Font licensing and self-hosted availability for AGMed/PlantLig were not verified.
