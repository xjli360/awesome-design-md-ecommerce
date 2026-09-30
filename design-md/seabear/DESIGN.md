---
version: alpha
name: "SeaBear"
source_url: "https://seabear.com"
captured_at: "2026-09-28T09:12:08.929566+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  SeaBear Smokehouse's observed CSS shows a Pacific Northwest smokehouse
  identity built on deep teal-navy (#134055, #0c2f40) as the primary action
  color, paired with a warm rust-brown secondary (#99521e) and a copper
  accent (#b44d0d) that echo smoked-wood and cured-fish tones. Body copy
  runs in a neutral charcoal (#454545) against a soft warm-gray canvas
  (#f0f0f0), with cream surfaces (#f7f5ed) inferred for card backgrounds
  and content blocks that need separation from the page without a hard
  white. White (#ffffff) serves as on-primary text and card surface.
  Headings use "interstate-condensed" at a bold, tightly-set weight
  (confirmed via the .rte h1 rule at 800/45px), while buttons and body
  text use "interstate" at 700/20px for CTAs. The font stack also lists
  "adobe-handwriting-ernie," suggesting a decorative script used
  somewhere for heritage/brand-mark flourishes ("Since 1957"), though no
  CSS rule ties it to a specific selector, so its role here is inferred
  and unmapped. Layout choices below (radius, spacing, card structure)
  are proposed conventions consistent with the button/skeleton evidence,
  not confirmed page measurements.

colors:
  primary: "#134055"
  primary-hover: "#0c2f40"
  secondary: "#99521e"
  ink: "#0c2f40"
  body: "#454545"
  canvas: "#f0f0f0"
  muted: "#4c6261"
  hairline: "#dedede"
  surface-soft: "#f7f5ed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#b44d0d"
  warm-tan: "#e4c9b4"
  disabled: "#454545"
typography:
  display-xl: {fontFamily: "'interstate-condensed', sans-serif", fontSize: "45px", fontWeight: 800, lineHeight: 1.11, letterSpacing: "0.45px"}
  display-md: {fontFamily: "'interstate-condensed', sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "0.2px"}
  title-md: {fontFamily: "'interstate', sans-serif", fontSize: "22px", fontWeight: 700, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "'interstate', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'interstate', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "'interstate', sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.3px"}
  button-md: {fontFamily: "'interstate', sans-serif", fontSize: "20px", fontWeight: 700, lineHeight: 1.25, letterSpacing: "0px"}
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
    hoverBackgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xxl}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    hoverBackgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xxl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    overlayColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  variant-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** renders the site's core call-to-action ("Add to Cart", "Shop Now") in the deep teal (#134055) confirmed by the `.btn` rule, with a darker hover state (#0c2f40) also observed. Square corners are proposed based on the absence of a border-radius declaration on `.btn` and the `0px` default seen in the checkout-widget CSS variable.

**button-secondary** reuses the same button shape and type but swaps in the rust-brown (#99521e) confirmed on `.btn--secondary`, useful for lower-emphasis actions like "Choose a variant" confirmations. Hover state is proposed to converge on the same dark teal for consistency.

**text-input** is a proposed pattern for search and account fields; no explicit input-styling rule was supplied, so border color, radius, and padding are inferred from the neutral hairline gray and general body typography.

**nav-bar** reflects the observed menu structure (Best Sellers, Seafood by Type, Meal Solutions, cart, search toggle) sitting on a white surface with charcoal ink text; exact height, sticky behavior, and mobile collapse are not observed and are proposed conventions.

**product-card** is inferred from the repeated "Add to Cart / $price / variant" pattern in the page text (e.g., Sockeye Salmon, Halibut Fillets, Crab Legs). A soft cream surface (#f7f5ed) is proposed to lift cards off the light-gray page background (#f0f0f0) confirmed on `body`.

**hero** is proposed for the top promotional band ("CHOWDERFEST… BUY 5+, SAVE 20%") using the canvas background and the large condensed display type confirmed via `.rte h1`. Overlay/scrim treatment for hero imagery is proposed, not measured.

**footer** is proposed as a dark ink-colored band for brand/story content ("Since 1957", wholesale inquiry), using inverted text color for contrast; no footer-specific CSS rule was supplied.

**badge** covers promotional callouts like "New Arrival" or percentage-off variant labels (10%/12%/15% off multipacks) seen throughout the product text; the copper accent (#b44d0d) is proposed for these small pill labels.

**search** is a proposed lightweight input matching the "Toggle Search Bar" text found in the evidence; exact expanded/collapsed states were not observed.

**variant-selector** directly reflects the repeated "Choose a variant" dropdown/button-group pattern seen across products (Single / 4-Pack / 8-Pack, etc.), with an active-state border in primary teal proposed for the selected option.

## Responsive Behavior

This is a proposed recommendation, not measured site behavior; no media queries were supplied in the evidence.

| Breakpoint | Width       | Notes (proposed) |
|------------|-------------|-------------------|
| mobile     | 0–599px     | Single-column product grid, nav collapses to a toggled menu/search icon pair as text hints ("Toggle Search Bar"), sticky add-to-cart bar suggested for long product pages. |
| tablet     | 600–959px   | Two-column product grid; hero retains full-bleed image with stacked text. |
| desktop    | 960–1279px  | Three to four-column product grid; persistent top nav with inline search toggle. |
| wide       | 1280px+     | Max-width content container (proposed ~1280–1440px) with increased section spacing (`{spacing.section}`). |

Touch targets for buttons and variant selectors should be a minimum 44px tall, consistent with the `.shopify-payment-button__button` min-height clamp seen in the accelerated-checkout CSS. Collapse of secondary nav items into a menu drawer below `tablet` is recommended but unverified.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was gathered from static CSS/text extraction; no rendered screenshots, computed styles, or DOM inspection were performed, so actual layout, spacing, and component placement are not confirmed.
- Several palette colors (e.g., #3498db, #1990c6, #136f99) originate from generic Shopify checkout/payment-widget CSS rather than SeaBear's own theme, so their brand relevance is uncertain and they were excluded from the semantic color set.
- The `adobe-handwriting-ernie` font is present in the font-family list but has no associated CSS rule in the supplied evidence; its use case (likely a decorative heritage accent) is inferred, not confirmed.
- Border-radius values for buttons and cards are proposed based on the absence of radius declarations on `.btn` and the `0px` default in checkout-widget variables; actual rendered corners were not observed.
- All spacing scale values, breakpoints, and component padding are proposed conventions for a Shopify-style seafood storefront, not measurements taken from the live site.
- Font licensing/availability for "interstate," "interstate-condensed," and "adobe-handwriting-ernie" has not been verified; production use would require confirming license terms.
- Mobile menu, cart-flyout, and search-toggle interaction behavior are referenced in page text but their visual/interactive states were not observed.
