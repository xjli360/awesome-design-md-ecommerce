---
version: alpha
name: "Rains"
source_url: "https://rains.com"
captured_at: "2026-09-28T10:22:42.894674+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Rains presents a minimalist, monochrome-led storefront built around a near-black ink (#10100f) paired with pure white and a tight run of warm-to-cool grays (#f9f9f9, #f5f5f5, #e5e5e5, #dedede, #cfcfcf, #797979). These neutrals dominate the observed CSS and read as the functional backbone for text, hairlines, and surface layering rather than decoration. A secondary cluster of muted earth and slate tones (#938b78, #2e5579, #a45b55, #7d6660, #5e473d, #b18a51, #c5ad89, #019e81, #d29c84) appears alongside product-variant language in the page text ("2 colors", "6 colors") and is treated here as inferred swatch/variant chip colors for bags, not core brand color. Bright hues (#eb001b, #ff5f00, #0071ce, #2563eb, #ffc500) map to payment-method iconography (Visa/Mastercard/Amex/Apple Pay) and are explicitly excluded from the brand palette.
  Typography draws on two observed custom families, EuropaGroNr2SB and EuropaGroNr2SH, layered over the system sans-serif stack as fallback; weight and usage split (display vs. body) is inferred from naming, not measured. The interpretation favors tight letter-spacing on display sizes, generous whitespace, and a restrained button/border system consistent with a technical-outerwear-and-bags retailer. No button color, radius, or interaction state was directly observed in the supplied CSS beyond the hero button's translucent white overlay, so primary CTA styling below is a grounded but inferred proposal using the dominant ink/white pairing.

colors:
  primary: "#10100f"
  ink: "#10100f"
  canvas: "#ffffff"
  body: "#555554"
  muted: "#797979"
  hairline: "#e5e5e5"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  border-strong: "#cfcfcf"
  border-subtle: "#dedede"
  divider-alt: "#efefef"
  surface-page: "#f9f9f9"
  surface-panel: "#f2f2f2"
  overlay-scrim: "#00000000"
  swatch-taupe: "#938b78"
  swatch-slate: "#2e5579"
  swatch-clay: "#a45b55"
  swatch-moss: "#019e81"
  swatch-sand: "#c5ad89"
  swatch-blush: "#d29c84"
typography:
  display-xl: {fontFamily: "EuropaGroNr2SB, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "EuropaGroNr2SB, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "EuropaGroNr2SB, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "EuropaGroNr2SH, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "EuropaGroNr2SH, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "EuropaGroNr2SH, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "EuropaGroNr2SB, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    overlayColor: "{colors.overlay-scrim}"
    titleTypography: "{typography.display-xl}"
    ctaBackground: "{colors.canvas}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-panel}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  device-fit-badge:
    backgroundColor: "{colors.surface-panel}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** is proposed as a solid ink-on-white CTA for primary actions such as "Add to bag" or "Quick add," since no explicit CTA background was captured in the supplied CSS beyond a translucent hero overlay; the ink/white pairing is the strongest directly observed contrast pair.

**button-secondary** offers an outlined variant for lower-priority actions (e.g., "View details," "Compare"), using the observed mid-gray border tone (#cfcfcf) against white, consistent with the site's restrained neutral system.

**text-input** covers search and form fields (newsletter, checkout) using a light border and white background; no focus-state color was observed, so focus treatment is left undefined pending live inspection.

**nav-bar** reflects the flat, white, black-text header implied by `#shopify-section-header .underline { color: #000000 }` and related selectors, styled as a slim horizontal bar with hairline division from content below.

**product-card** is a proposed pattern for backpack/laptop-bag listings: white/near-white card, subtle hairline border, title in title-md, price in body-md — inferred from typical Shopify PLP conventions, not directly measured.

**hero** models the large banner sections referenced by selectors like `hero_media_zcLiGA`/`hero_media_pWMk3D`, which show a translucent white button (`hsla(0,0%,89%,0.52)`) over imagery; background and overlay tokens are approximated from that one observed value.

**footer** is proposed as a dark, ink-toned band with white text for contrast, following the site's monochrome hierarchy; no footer-specific CSS was supplied, so this is an inferred convention.

**badge** and **device-fit-badge** are category-specific proposals: the page text explicitly lists device-capacity filters ("Fits 13″ device," "Fits 15″ device," "Fits 16″ device") for the Bags/Backpacks category, so a small pill-shaped badge is proposed to surface laptop-fit compatibility on product cards and filter chips — content is grounded in evidence, styling is inferred.

## Responsive Behavior
This is a recommended, unmeasured breakpoint scheme, not observed site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–479px | Single-column PLP, collapsed nav behind menu icon (observed "Menu" label in page text) |
| tablet | 480–959px | 2-column product grid, sticky search bar |
| desktop | 960–1279px | 3–4 column grid, full horizontal nav with mega-menu (category depth implied by extensive nav text) |
| wide | 1280px+ | 4+ column grid, max-width content container |

Touch targets for buttons/badges should be at least 44×44px; nav mega-menu items and device-fit badges should collapse into an accordion or drawer below the tablet breakpoint. All values above are proposed defaults, not extracted from live layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus/active states, or JavaScript-driven interactions were observed. Color-to-role mapping (primary, body, muted, etc.) is inferred from selector context and general minimalist-retail convention, not confirmed against live component screenshots. The earth-toned "swatch-*" colors are inferred as product-variant options based on nearby "N colors" text but were not directly tied to bag SKUs in the supplied evidence. EuropaGroNr2SB/SH are treated as the brand's custom typeface family names as they appeared in `font_families`, but weight assignment (SB vs. SH), licensing, and web-font availability/fallback behavior were not verified. Spacing and radius scales are proposed conventions, not measured from CSS. Payment-brand colors (Visa/Mastercard/Amex/etc.) were identified by hue association and excluded from the brand palette, but this exclusion is a judgment call, not a certainty. Mobile menu, cart drawer, and search overlay behavior were not observed and are described only as proposed patterns.
