---
version: alpha
name: "88 Films"
source_url: "https://88-films.myshopify.com/"
captured_at: "2026-09-29T04:11:34.667107+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the live 88 Films Shopify storefront
  (88-films.myshopify.com), a UK-based distributor of 4K UHD, Blu-ray and
  DVD releases spanning American slashers, Italian exploitation, Kung-Fu
  classics, British chillers and Japanese cult cinema. The site's CSS
  custom properties define a strict black-on-white base scheme
  (--color-foreground: 0,0,0 / --color-background: 255,255,255), with
  primary buttons rendered solid black on white text and secondary
  buttons inverted with a mid-grey (#808080) label and border, matching
  the observed --color-secondary-button-text and --color-link tokens.
  Supporting neutrals (#252525, #6a6a6a, #777777, #dedede, #1c1c1c,
  #232323, #121212) are treated as inferred surface, hairline and
  muted-text variants layered onto the same black/white foundation,
  since no distinct section backgrounds were captured. A small accent
  cluster (#fb8077, #716a56, #f70505) is present in the palette but its
  functional use (sale flags, "Coming Soon" tags, hover states) is
  unconfirmed and marked inferred; payment-icon colors (Visa/Mastercard/
  PayPal blues, reds, oranges) are excluded from brand roles. Typography
  uses the observed Archivo / Archivo Narrow sans-serif stack for body
  and UI text, with GTStandard-M applied to headings as a proposed
  display treatment — its licensing and full character set are not
  verified from static CSS alone.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#252525"
  muted: "#808080"
  hairline: "#dedede"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#fb8077"
  accent-olive: "#716a56"
  alert: "#f70505"
  scheme-dark: "#1c1c1c"
  scheme-dark-alt: "#232323"
  true-black: "#121212"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "GTStandard-M, Archivo, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.3px}
  display-md: {fontFamily: "GTStandard-M, Archivo, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Archivo, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.4px}
  body-md: {fontFamily: "Archivo, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.6px}
  body-sm: {fontFamily: "Archivo, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  caption: {fontFamily: "Archivo Narrow, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.8px}
  button-md: {fontFamily: "Archivo, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.6px}
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
    textColor: "{colors.muted}"
    borderColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
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
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.true-black}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  media-format-badge:
    backgroundColor: "{colors.scheme-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** — Solid black fill with white label, matching the root `--color-button: 0,0,0` / `--color-button-text: 255,255,255` tokens; used for "Add to cart," "Pre-order here" and "Subscribe" actions. Hover state (border glow via `box-shadow`) is present in CSS but its visual result is not confirmed from static extraction.

**button-secondary** — White fill with a grey (#808080) label and border, mirroring `--color-secondary-button-text`. Proposed for "View all," "Check for updates" and other lower-priority calls to action seen in the release grid.

**text-input** — Minimal bordered field on white, used for the newsletter "Email" capture and any account/login forms. Border and focus-ring colors are inferred from the generic `--focused-base-outline` token rather than a captured input screenshot.

**nav-bar** — Top utility row carrying social icons, country/currency selector, login and cart, plus a primary category row (New Releases, UHD, Blu-ray, DVD, Offers). Sticky behavior and dropdown styling are proposed, not observed.

**product-card** — Vertical card for release tiles (title, format, regular price, optional "Coming Soon" flag) as seen repeated across New Releases and Coming Soon sections. Card border/radius values are inferred defaults since the theme exposes them as unset custom properties (`--product-card-corner-radius`, etc.).

**hero** — Full-width promotional banner for lead titles (e.g., "The Mothman Prophecies 4K UHD + Blu-ray"). A dark/true-black background is proposed to give large-format cover art contrast; actual hero background color was not directly observed.

**footer** — Multi-column white footer with social links, country/currency selector, payment-method icons, and legal links (Refund/Privacy/Terms/Shipping). Payment-badge colors (Visa blue, Mastercard red/orange, PayPal blues) are excluded from the brand palette and treated purely as third-party marks.

**badge** — Small pill/outline label for status flags such as "Website Exclusive," "New," or "Last Chance." Styling is proposed from the theme's generic `--color-badge-*` tokens (black border/text on white).

**search** — Predictive search input styled consistent with `text-input`, assumed present in the header per standard Shopify theme structure; no distinct search-result layout was captured.

**media-format-badge** — Category-specific dark tag distinguishing UHD / Blu-ray / DVD / 3D Blu-ray variants on product cards and titles (e.g., "Gamer [4K UHD + 3D Blu-ray + Blu-ray]"). This is a proposed pattern to visually separate format SKUs, not a captured design element.

## Responsive Behavior

| Breakpoint | Range | Layout guidance (proposed) |
|---|---|---|
| Mobile | < 600px | Single-column product grid, collapsed hamburger nav, stacked footer columns, full-width buttons. |
| Tablet | 600–989px | 2–3 column product grid, condensed top utility bar, nav collapses into a drawer. |
| Desktop | ≥ 990px | Full horizontal nav with category row, 4+ column product grid, multi-column footer. |

Minimum touch targets are recommended at 44×44px for cart, nav and format-badge controls. This table is a design recommendation only; no live breakpoint or mobile interaction behavior was measured from the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS and a text excerpt only; no rendered screenshots, hover states, animations, or JavaScript-driven interactions (cart drawer, predictive search results, mobile nav) were observed.
- `--font-heading-family` and `--font-body-family` custom-property *values* were not resolved in the supplied CSS; Archivo/Archivo Narrow and GTStandard-M assignments to heading vs. body roles are inferred from the available `font_families` list, and GTStandard-M's licensing/availability as a web font is unverified.
- Several palette entries (#eb001b, #f79e1b, #ff5f00, #0071ce, #16803c, #142fbd, #1532cb, #1990c6, #136f99) closely match standard payment-network branding (Visa/Mastercard/PayPal) and were deliberately excluded from the design token set rather than mapped to brand roles.
- Accent colors #fb8077, #716a56 and #f70505 appear in the raw palette but their functional use on-site (sale tags, hover, alerts) could not be confirmed and are labeled inferred.
- Product-card border radius, shadow, and image-padding values reference unset theme custom properties (`--product-card-*`); numeric values in this spec are proposed defaults, not extracted measurements.
- Hero, search-results, and cart-drawer layouts are proposed patterns based on typical Shopify theme structure, not confirmed from this page's captured markup.
