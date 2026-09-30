---
version: alpha
name: "BetaFPV"
source_url: "https://betafpv.com"
captured_at: "2026-09-28T04:56:20.842282+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  BetaFPV's storefront evidence points to a utilitarian ecommerce build (Shopify-pattern class names, a Judge.me review widget, and a `ba-products-box` merchandising plugin) rather than a heavily custom brand skin. The confirmed palette is dominated by neutral grays and near-blacks (#111111, #222222, #555555, #666666, #999999) against a white canvas, with a recurring cyan/teal family (#54cce9, #3dc5e6, #81d9ef, #95d5df, #08a8cf) that appears often enough across otherwise-unrelated rules to be treated as an inferred accent group, likely used for links, highlights, or informational tags. A single concrete branded interactive color was observed: #616669 on a hero `.btn`. Red (#d02e2e) and teal-green (#108474) are proposed for sale/alert and "new" signaling respectively, since ecommerce sites in this category commonly need such states, though their exact usage was not directly observed. Typography is grounded in "Work Sans" for UI chrome and buttons (explicitly set on `.ba-products-box` and `.ba-product-addtocart`), with Montserrat proposed for larger display headings since it appears in the font stack evidence. Rounding is conservative: an explicit `border-radius:0` on a select control suggests a squared, technical aesthetic appropriate for a specs-heavy drone-parts catalog, so the rounded scale below leans toward smaller values.

colors:
  primary: "#54cce9"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-alert: "#d02e2e"
  accent-success: "#108474"
  accent-new: "#efe70f"
  border-strong: "#555555"
  muted-alt: "#999999"
  button-alt: "#616669"
  overlay: "#00000033"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Work Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Work Sans, \"Helvetica Neue\", Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Work Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 22px, letterSpacing: 0px}
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
  button-hero:
    backgroundColor: "{colors.button-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  variant-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    mutedPriceColor: "{colors.muted-alt}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    ctaComponent: "button-hero"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.border-strong}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-new}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the cyan accent group as an inferred call-to-action color; since no literal primary CTA rule was captured, this mapping is proposed based on the accent color's repeated presence in the palette.

**button-secondary** is a low-emphasis outline treatment for tertiary actions (e.g. "compare," "wishlist"), proposed to pair with product cards; no such button was directly observed.

**button-hero** is grounded in a real rule: `.hero--...  .btn { background:#616669 }`. This is the only concrete branded button color captured, so it is used here for hero-banner CTAs specifically rather than generalized across the whole UI.

**text-input** and **variant-selector** both derive from the observed `select.ba-product-variant-select` rule (white background, black text, 1px `#e8e9eb`-family border approximated to the closer palette hairline, explicit `border-radius:0`). This squared-off input style is treated as representative of form controls sitewide, though only the variant selector was directly evidenced — relevant for drone/FPV-kit pages with motor, battery, and video-system option pickers.

**nav-bar** is proposed as a light, white-background bar given the canvas-dominant palette and the large multi-level category menu described in the page text (Drones, FPV Gear, Parts & Spares, etc.), which implies a mega-menu structure; exact nav styling was not measured.

**product-card** reflects observed typographic rules: `h3.ba-product_title { color:#111111 }` and `.ba-product-oldprice { color:#999; text-decoration:line-through }`, giving a dark title over a muted strikethrough compare-at price — common for the sale-heavy catalog (e.g. "30% OFF" batteries).

**hero** is proposed as a soft neutral banner background (`surface-soft`) housing rotating campaign messages (Meteor75 Pro II, Pavo20 Pro II, Aquila20 HD) with a `button-hero` CTA; banner background color itself was not captured in evidence.

**footer** is proposed as a dark, ink-colored band (inverting the light UI) to host the Explore/Support link columns and social icons noted in the page text; no footer-specific CSS was supplied.

**badge** and **badge-sale** are proposed merchandising labels for "NEW" and "% OFF" flags, which the page text confirms exist ("NEW", "30% OFF") though their exact colors were not in the CSS evidence — accent-new and accent-alert are inferred assignments from the broader palette.

**search** is proposed as a bordered, white input consistent with the text-input pattern, supporting the "Search" affordance referenced in the page text.

## Responsive Behavior

This is a recommendation, not measured site behavior — no media queries or breakpoint values were present in the supplied evidence.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | <480px     | Single-column product grid; nav collapses to hamburger + drawer cart |
| tablet    | 480–1024px | 2-column product grid; mega-menu condenses to accordion categories |
| desktop   | 1024–1440px| 3–4 column product grid; full mega-menu on hover |
| wide      | >1440px    | Max-width content container, extra gutter spacing |

Touch targets on `button-primary`, `button-hero`, and `variant-selector` should maintain a minimum 44×44px hit area on mobile, achieved by padding rather than font-size changes to preserve the observed 14px button typography. Mega-menu categories (Drones, RTF Kits, Radio Controllers, FPV Gear, Parts & Spares) should collapse into an accordion pattern below tablet width given the depth of the category tree in the page text.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live rendering, computed styles, or interaction states (hover, focus, active, disabled) were observed beyond the two explicit `:hover` background rules captured for add-to-cart buttons. Several colors in the CSS evidence (e.g. `#B12704` price text, `#212121` description text, `#e8e9eb` input border) fell outside the supplied observed palette array and were substituted with the nearest in-palette hex, which introduces mapping uncertainty. The assignment of the cyan accent group to `primary`, and of `#d02e2e`/`#108474`/`#efe70f` to alert/success/new roles, is inferred from general ecommerce convention, not confirmed usage. Montserrat's role as a display font is inferred from its presence in the font-family list, not from a captured heading rule; actual heading font, custom webfont licensing, and availability were not verified. No mobile menu, cart drawer, or checkout flow markup was supplied, so those layouts are entirely proposed. Spacing and rounding scales follow a conventional design-system default rather than measured site values, aside from the explicit `border-radius:0` on the variant selector.
