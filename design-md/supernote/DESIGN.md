---
version: alpha
name: "Supernote"
source_url: "https://supernote.com"
captured_at: "2026-09-28T09:08:20.163749+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Shopify-hosted theme CSS for Supernote's e-notebook storefront. The observed palette is a restrained neutral-gray system: `#efefef` as the primary page background (--color-background), `#e5e5e5` as a secondary surface, `#000000` for text (--color-text/--color-body-text), and `#919da9` as the dominant interactive/button color across multiple button variants (pf-gs-button-1 through pf-button-8). A near-black `#050504` appears as --color-accent, and `#dc0000` is explicitly reserved for sale pricing (--color-sales-price). White (`#ffffff`) and off-white tones (`#f5f5f5`, `#fafafb`) round out light surfaces; `#e1e1e1`/`#d8d8d8` read as plausible hairline/border tones given the stated --color-borders-opacity of .46 against dark text, though exact border colors are not directly declared and are therefore inferred.

  Typography centers on two confirmed heading families: Shippori Mincho (serif, --font-stack-headings) for primary display use, and BigCaslon at 56px for a secondary large-heading variant. No body-copy font is explicitly bound to a body selector in the supplied CSS; sans-serif body typography (using Inter, present in the observed font stack) is therefore an inferred pairing, not a confirmed observation. All sizing beyond the two confirmed heading rules (56px, 24px, 20px) is proposed to fill out a usable type scale.

colors:
  primary: "#919da9"
  ink: "#000000"
  canvas: "#efefef"
  body: "#444749"
  muted: "#8a8a8a"
  hairline: "#e1e1e1"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-dark: "#050504"
  sale: "#dc0000"
  background-secondary: "#e5e5e5"
typography:
  display-xl: {fontFamily: "BigCaslon, serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Shippori Mincho', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.0, letterSpacing: 0px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 40px
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.sale}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.background-secondary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairlineTop: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.base}"
  device-spec-block:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the observed `#919da9` fill seen across `pf-gs-button-1`/`pf-button-2` rules, paired with white text, matching the site's consistent use of this gray-blue as the primary interactive color. Proposed states (hover/active/disabled) are not present in the static CSS.

**button-secondary** mirrors the `pf-gs-button-2`/`pf-button-3` outline pattern: transparent fill, `#919da9` text and border, used for lower-emphasis actions like "Help Me Choose" or filter toggles. Interaction behavior is proposed.

**button-pill** reflects the `border-radius:40px` seen on `pf-gs-button-3`/`pf-button-4`, suggesting a rounded pill treatment for select CTAs (e.g., "Shop Now"). Usage context is inferred, not confirmed from layout.

**text-input** is proposed for search and account/cart forms; no explicit input CSS was supplied, so border, radius, and padding follow the general hairline/spacing system rather than observed input rules.

**nav-bar** represents the top utility/menu bar implied by the page text (Devices, Accessories, Blog, Community, Support, country selector). Background and hairline are inferred from the canvas/border palette; exact height, sticky behavior, and mobile collapse are not observed.

**product-card** supports device and accessory listings (Manta, Nomad, LAMY set, folios). The sale-price color `#dc0000` is directly confirmed via `--color-sales-price`; card border, radius, and padding are proposed layout conventions.

**hero** is proposed for the homepage headline area ("For Those Who Write"), using the confirmed BigCaslon display style at large scale against the canvas background. Actual hero imagery, overlay, and CTA placement are not observed.

**footer** is proposed using the secondary background tone (`#e5e5e5`) and body-sm typography for link lists (Support, Solutions, About); no footer-specific selector was supplied.

**badge** applies the confirmed sale-price red as a promotional/sale flag (e.g., price-increase notices, discount labels), consistent with the site's banner text about a Nomad price change.

**search** is proposed as a pill-shaped overlay/input matching the site's "Search" menu item, using surface-soft background and hairline border; no search-bar CSS was directly supplied.

**device-spec-block** is a category-appropriate component for presenting e-reader/tablet specifications (screen size, storage, battery) in a card layout, using title-md for values and caption for labels; this pattern is proposed for the product category, not confirmed from evidence.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <640px | Collapsed/hamburger | 1 column |
| Tablet | 640–1024px | Condensed horizontal | 2 columns |
| Desktop | >1024px | Full horizontal | 3–4 columns |

Touch targets should be at least 44px in the smallest dimension for buttons and nav items. Product grids are proposed to collapse from multi-column to single-column below 640px, with the nav bar assumed to collapse into a hamburger/drawer pattern at the mobile breakpoint; none of this was directly observed in the supplied static CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction only; no rendered layout, computed styles, hover/focus states, or mobile viewport behavior were observed. Only two heading rules (BigCaslon 56px, and generic 24px/20px heading sizes) and one accent-color role (`--color-sales-price: #dc0000`) are directly confirmed; all other type sizes, the body font pairing (Inter), spacing scale, and rounded-corner scale beyond the observed 40px pill buttons are proposed conventions for usability, not measurements. Border/hairline colors (`#e1e1e1`, `#d8d8d8`) are inferred from the neutral palette and stated border-opacity variable rather than from an explicit border-color declaration. Component existence (nav-bar, footer, search, product-card, device-spec-block) is inferred from page text and common e-commerce patterns, not from confirmed DOM/CSS selectors for those regions. Availability, licensing, and web-embedding rights for Shippori Mincho, BigCaslon, and Inter were not verified from the supplied evidence.
