---
version: alpha
name: "NIS America Store"
source_url: "https://store.nisamerica.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's marketplace that wears its fandom on its sleeve through a high-contrast palette anchored on #ffb600 — a marigold yellow that reads as both premium and playful, the kind of accent that makes a limited-edition steelbook or art book feel like a treasure rather than a transaction. The storefront runs on a near-black foundation (#1d1d1d for the top chrome, #121212 for deep backgrounds) with #345caa as a secondary blue that recalls classic RPG UI elements — think menu screens from a 90s JRPG, but rendered in clean DM Sans and Roboto Condensed. Product cards use #dedede borders on #f6f6f6 surfaces with {rounded.sm} corners, while the primary CTA button (#ffb600 on #1d1d1d) carries {rounded.xs} — deliberately less rounded than the {rounded.md} of search inputs, as if to say "this is the action that matters." The cart badge (#d10000) and sale flags (#ffb600 on #282828) introduce urgency without breaking the system's two-color accent discipline. Shopify's platform constraints are visible in the checkout flow (where #005eff appears as a payment-widget blue), but the brand's own territory — pre-order banners, edition counters, and genre tags — stays firmly in the yellow-blue-near-black triangle. The overall feel is a game collector's shelf: dark wood, yellowed spine labels, and the occasional red "sold out" sticker.

colors:
  primary: "#ffb600"
  primary-active: "#e5a300"
  primary-disabled: "#b38000"
  ink: "#121212"
  body: "#282828"
  muted: "#7c7c7c"
  muted-soft: "#a0a0a0"
  hairline: "#dfdfdf"
  hairline-soft: "#d0d0d0"
  canvas: "#f6f6f6"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#121212"
  accent-blue: "#345caa"
  accent-blue-active: "#2a4a8a"
  badge-red: "#d10000"
  badge-red-active: "#a80000"
  checkout-blue: "#005eff"
  sale-tag-bg: "#282828"
  sale-tag-text: "#ffb600"
  top-bar: "#1d1d1d"
  top-bar-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'DM Sans', 'Roboto Condensed', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-blue-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-badge-red:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  button-badge-red-active:
    backgroundColor: "{colors.badge-red-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-red}"
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-nav-bar:
    backgroundColor: "{colors.top-bar}"
    textColor: "{colors.top-bar-text}"
    typography: "{typography.nav-link}"
    height: 56px
  top-nav-link:
    textColor: "{colors.top-bar-text}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  top-nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    color: "{colors.badge-red}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-tag-bg}"
    textColor: "{colors.sale-tag-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 36px
  footer:
    backgroundColor: "{colors.top-bar}"
    textColor: "{colors.top-bar-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  cart-icon-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 12px"
  pre-order-banner:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    padding: "{spacing.sm} {spacing.base}"
  edition-counter:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The marigold CTA (#ffb600 on #121212) that drives every purchase action: "Add to Cart," "Pre-Order Now," "Checkout." Uses {rounded.xs} for a crisp, game-menu feel. On hover, shifts to {colors.primary-active} (#e5a300); disabled state drops to {colors.primary-disabled} (#b38000) with reduced opacity. **`button-secondary`** — A white button with a {colors.hairline} border and {colors.ink} text, used for "View Details," "Continue Shopping," and secondary checkout actions. Active state swaps the border to {colors.ink}. **`button-accent-blue`** — The blue variant (#345caa on #f6f6f6) reserved for "Learn More" links on pre-order banners and edition info panels. Active state darkens to #2a4a8a. **`button-badge-red`** — A compact red button (#d10000) for "Sold Out" or "Notify Me" actions, using {typography.button-sm} and tighter padding.

### Cards
**`product-card`** — The primary product display unit: a white card on {colors.canvas} with a 1px {colors.hairline} border and {rounded.sm} corners. The image area uses {rounded.sm} on top corners only, creating a subtle visual break between photo and text. Title uses {typography.title-sm} at 16px/600 weight; price uses {typography.price} at 20px/700. Sale items show {typography.price-sale} in {colors.badge-red} alongside a {typography.price-compare} with strikethrough. Badges (red for "Sold Out," dark with yellow text for "Sale") sit as overlays on the image area with {rounded.xs}. The "Add to Cart" button sits at the bottom of the card, using {typography.button-sm} and {rounded.xs}.

### Navigation
**`top-nav-bar`** — A 56px near-black (#1d1d1d) bar spanning the full viewport width. Links use {typography.nav-link} (14px/600 weight, 0.5px letter-spacing, uppercase) in white. The active/current link switches to {colors.primary} (#ffb600). The cart icon carries a {colors.badge-red} circular badge with {rounded.full} and {typography.caption-sm}. A secondary utility bar (search, account, currency) may sit below on desktop, using {colors.canvas} background and {colors.body} text.

### Forms
**`text-input`** — Standard text fields use a white background, {colors.hairline} border, {rounded.md} (12px), and {typography.body-md}. Focus state swaps the border to {colors.primary}. Error state uses {colors.badge-red} border. **`search-input`** — Identical styling to text-input but with a magnifying-glass icon inset on the left. **`quantity-selector`** — A compact horizontal control with a {colors.canvas} background, {colors.hairline} border, and {rounded.xs}. Increment/decrement buttons sit on either side with transparent background and {colors.body} text.

### Footer
**`footer`** — A full-width near-black (#1d1d1d) section with {spacing.xxl} vertical padding. Links use {typography.link} (14px/500) in {colors.muted-soft} (#a0a0a0), switching to {colors.primary} on hover. The footer typically includes columns for "Support," "About NIS America," "Community," and "Legal," plus social media icons (which may introduce their own brand colors — these are not part of the NIS palette).

### Badges & Tags
**`product-card-badge`** — Red (#d10000) badge with white text, {rounded.xs}, and {typography.badge} (11px/700 uppercase). Used for "Sold Out," "Out of Stock." **`product-card-sale-badge`** — Dark (#282828) badge with yellow (#ffb600) text, same shape and typography. Used for "Sale," "Clearance," "Limited Offer." **`pre-order-banner`** — A full-width blue (#345caa) strip with white text, using {typography.badge} and {spacing.sm} vertical padding. Typically sits above the product title on pre-order items. **`filter-tag`** — Pill-shaped ({rounded.full}) tags for category or genre filtering. Default state: {colors.canvas} background, {colors.body} text, {colors.hairline} border. Active state: {colors.primary} background, {colors.on-primary} text, no border.

### Breadcrumbs
**`breadcrumb-link`** — A muted (#7c7c7c) 13px/500 weight link using {typography.caption}. The active (current page) link switches to {colors.ink} (#121212). Separators are typically a simple ">" character in {colors.muted-soft}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack single-column; filter tags become a horizontal scrollable strip; footer stacks vertically; search bar moves to a full-width overlay; quantity selector becomes full-width. |
| Tablet | 744–1128px | Top nav shows limited links (Home, Store, Support) with hamburger for rest; product cards in 2-column grid; filter tags remain scrollable; footer shows 2-column layout. |
| Desktop | 1128–1440px | Full top nav with all links visible; product cards in 3-column grid; filter tags as a sidebar or top row; footer in 4-column layout; search bar in top utility bar. |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; additional whitespace on sides; footer remains 4-column. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch compliance.
- Icon buttons (cart, search, account) use 44x44px tap targets even if the visible icon is smaller.
- Filter tags use 36px height with 14px horizontal padding — acceptable for touch but borderline; consider 40px on mobile.
- Quantity selector buttons use 40px height.

### Collapsing Strategy
- Top nav collapses to a hamburger menu at < 744px; the hamburger icon sits in the top bar alongside the logo and cart.
- Product card grids collapse from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile).
- Footer collapses from 4 columns → 2 columns → single column stacked.
- Filter sidebar (if present on desktop) collapses to a horizontal scrollable tag strip on tablet and mobile.
- Breadcrumbs truncate on mobile, showing only the current page and a "Back" link.
- Search bar collapses from a visible input on desktop to an icon-triggered overlay on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (beyond primary/secondary buttons) could not be reliably extracted from the live site; the system assumes a simple opacity or color shift where not specified.
- Error states for forms (validation messages, input error borders) are inferred from common Shopify patterns rather than extracted.
- The checkout flow (#005eff) uses Shopify's default payment-widget colors; the brand's own palette may not extend into that flow.
- Sub-brand or collection-specific palettes (e.g., limited edition releases, franchise-specific theming) were not extracted.
- Dark mode is not supported; the brand uses a near-black top bar and footer but a light canvas for content.
- Loading states (skeleton screens, spinners) were not observed and are not defined.
- Focus-visible styles (keyboard navigation outlines) were not extracted; a 2px {colors.primary} outline is recommended for accessibility.
- The extracted hex list includes #005eff (Shopify Pay blue) and #dedede/#dfdfdf/#d0d0d0 (likely border/divider variants); the true brand palette is narrower than the full extraction suggests.
- Font weights beyond 400, 500, 600, 700 were not confirmed; DM Sans and Roboto Condensed may support additional weights not used on the live site.
- The exact line-height and letter-spacing values for typography tokens are inferred from common web standards for these font sizes; the live site may use slightly different values.
