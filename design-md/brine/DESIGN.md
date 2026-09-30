---
version: alpha
name: "Brine"
source_url: "https://www.brine.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep red #ee283b — the color of a lacrosse ball fresh from the box — anchors every primary CTA, cart button, and scoreboard-style badge across Brine's digital presence. This is a brand built for the field, not the sideline: the palette draws from team uniforms (#cc0000, #008827) and game-day equipment (#b79e69 for leather, #141414 for cleats and padding), with a secondary green #008827 that appears on add-to-cart actions and category tags. The typography stack leans on Proxima Nova W01 as the workhorse display face, paired with system fallbacks that keep the site fast on mobile browsers during game-day traffic spikes. Navigation is lean — a single top bar with logo, search, cart, and account icons — and product cards use a clean white canvas (#ffffff) with subtle hairline borders (#d9d9d9) to separate items in grid views. The brand's voice is direct and competitive: headlines in bold weight, body copy in regular, and every button carries a full-radius pill shape (`{rounded.full}`) that echoes the silhouette of a goalie's chest pad. There is no decorative flourish — no gradient, no illustration, no hero video — just clear hierarchy, high-contrast CTAs, and photography of athletes in motion. The extracted palette includes a cluster of warm pinks (#fbcdd2, #f8abb2, #f79ea7) that likely belong to seasonal or clearance-banner treatments, and a set of teal tones (#0c5460, #abdde5) that may be checkout-widget or social-icon defaults. The core identity, however, is unmistakable: red and green on white, built for speed and clarity.

colors:
  primary: "#ee283b"
  primary-active: "#cc0000"
  primary-disabled: "#f8abb2"
  ink: "#141414"
  body: "#444444"
  muted: "#565656"
  muted-soft: "#8c8c8c"
  hairline: "#d9d9d9"
  hairline-soft: "#b9bbbe"
  canvas: "#ffffff"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  green-primary: "#008827"
  green-active: "#005518"
  green-disabled: "#a7d6b4"
  leather: "#b79e69"
  error: "#6a0000"
  warning-bg: "#ffe8a1"
  info-bg: "#abdde5"
  badge-red: "#7c151f"
  badge-green: "#004714"

typography:
  display-xl:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Proxima Nova W01', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-green:
    backgroundColor: "{colors.green-primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-green-active:
    backgroundColor: "{colors.green-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-green-disabled:
    backgroundColor: "{colors.green-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 1:1
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-md}"
    textColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.green-primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-section-title:
    typography: "{typography.caption-bold}"
    textColor: "{colors.ink}"
    textTransform: uppercase
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for add-to-cart, checkout, and submit actions. Rendered as a full-radius pill in Brine red (#ee283b) with white text and 14px vertical padding. On hover, shifts to a deeper red (#cc0000); disabled state uses a pale pink (#f8abb2) to signal inactivity. **`button-secondary`** — An outlined variant with white fill and dark text (#141414), used for secondary actions like "View Details" or "Continue Shopping". Shares the same pill shape and 48px height as the primary button. **`button-green`** — A green variant (#008827) used for positive confirmations like "Add to Cart" on PDPs where the primary red is reserved for checkout. Active state deepens to #005518; disabled fades to a muted green (#a7d6b4). **`button-sm`** — A compact 36px version of the primary button, used in cart line items and quick-add dropdowns. Uses 14px bold text with 10px vertical padding.

### Navigation
**`nav-bar`** — A fixed 64px top bar with white background, containing the Brine logo (left), category links (center), and utility icons for search, account, and cart (right). Category links use uppercase 14px bold text with 0.5px letter spacing. The bar carries a subtle bottom border (#d9d9d9) to separate it from page content. On mobile, category links collapse into a hamburger menu, and the logo reduces to a compact wordmark.

### Product Cards
**`product-card`** — A clean white card with 8px rounded corners, containing a 1:1 product image, product name (body-sm), price (title-md), and optional sale badge. The card has no shadow — hierarchy is established through the image and typography alone. On hover, the image may scale subtly (1.02x) to indicate interactivity. **`badge-sale`** — A small red badge (#ee283b) with uppercase 11px bold white text, positioned at the top-left of product images to flag discounts. **`badge-new`** — A green badge (#008827) with the same styling, used for new arrivals. **`badge-category`** — A pill-shaped tag with light gray background (#ececf6) and muted text (#565656), used in filter strips and category navigation.

### Forms & Inputs
**`text-input`** — A standard 48px input field with white background, 8px rounded corners, and 16px horizontal padding. On focus, the border switches to a 2px red (#ee283b) stroke. Used for search, email signup, and checkout fields. **`search-bar`** — A full-radius pill input with a light gray background (#ececf6), used in the top nav and mobile search overlays. Contains a magnifying glass icon on the left and placeholder text in body color.

### Footer
**`footer-link`** — Standard 14px link in muted gray (#565656), used in footer columns for support, about, and legal pages. Hover state shifts to ink (#141414). **`footer-section-title`** — Uppercase 13px bold headings for footer columns, using the same muted gray as links but with heavier weight to establish hierarchy.

### Quantity Selector
**`quantity-selector`** — A compact 40px control with minus/plus buttons flanking a numeric display, used in cart and PDP quantity fields. White background with 8px rounded corners and 12px horizontal padding. The numeric value uses body-md weight; buttons use the same red (#ee283b) on hover for interactive feedback.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves to overlay; footer stacks vertically; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but truncated (top 4 categories); search bar remains in nav but shrinks to icon |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; search bar expanded with placeholder text; footer in 4-column layout |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; nav remains unchanged; footer expands to 5 columns |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav icons (search, account, cart) are 44x44px tap targets
- Quantity selector buttons are 40x40px with 8px internal padding
- Product card tap targets span the full card area

### Collapsing Strategy
- Category nav links collapse to hamburger menu below 744px
- Secondary nav items (sale, clearance) collapse into "More" dropdown on tablet
- Product filters collapse to a single "Filter" button on mobile, opening a slide-in panel
- Footer columns collapse to accordion sections on mobile, with the first column expanded by default

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is unusually large (30+ hex values), suggesting the live site may include third-party widget colors (Klarna, Afterpay, Shopify Pay) and stock-image dominant tones. The primary red (#ee283b) and green (#008827) are confidently identified as brand colors, but the leather tone (#b79e69) and several pink/teal values may be incidental rather than intentional design tokens.
- No meta theme-color was found in the page head — the browser chrome/taskbar color is unset.
- Hover and focus states for most components (beyond buttons) could not be reliably extracted from static CSS analysis.
- Error state styling for form inputs (validation messages, error borders) is not present in the extracted data.
- Dark mode is not detected — the site appears to be light-mode only.
- Font weights beyond the extracted declarations (e.g., 300, 800, 900 for Proxima Nova) may exist but were not found in the page CSS.
- The exact spacing scale (padding, margin values) is inferred from common e-commerce patterns rather than extracted from the live site.
- Sub-brand or collection-specific palettes (e.g., for "Brine Women's" or "Brine Goalie") are not represented in the extracted data.
- Animation durations, easing curves, and transition properties are not captured.
