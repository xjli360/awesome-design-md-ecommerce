---
version: alpha
name: "Star City Games"
source_url: "https://www.starcitygames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A competitive gaming marketplace that signals authority through a deep navy-and-steel palette — #313440 for the persistent top bar, #005586 for primary action surfaces, and #f1a500 as the single voltage accent that marks inventory status, sale badges, and price drops. The brand uses two typefaces — Montserrat for display and navigation (clean, geometric, slightly condensed) and Karla for body copy (a humanist sans with generous x-height that stays legible at 14px in dense card grids). Buttons carry {rounded.sm} corners and a 48px height that feels substantial without heaviness; the search bar is a full-width white field with a #007dc6 CTA orb, not a pill. Product cards stack on a #f5f5f5 canvas with #ffffff surfaces, using #e5e5e5 hairline borders and #8f8f8f muted text for secondary info — the effect is a trading-card binder translated into a clean, information-dense grid. The brand trusts color over typographic hierarchy: a #008a06 green for "In Stock" badges, #cc4749 red for "Sold Out" overlays, and #ff7600 orange for pre-order flags create a traffic-light system that lets players scan inventory at a glance. The footer runs dark (#313440 background, #8dc6e7 link color) — a rare inversion that bookends the experience with a sense of closure.

colors:
  primary: "#005586"
  primary-active: "#063f8a"
  primary-disabled: "#8dc6e7"
  ink: "#313440"
  body: "#474747"
  muted: "#757575"
  muted-soft: "#8f8f8f"
  hairline: "#e5e5e5"
  hairline-soft: "#dfdfdf"
  canvas: "#f5f5f5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f1a500"
  accent-orange: "#ff7600"
  accent-green: "#008a06"
  accent-red: "#cc4749"
  accent-blue: "#007dc6"
  accent-purple: "#221155"
  link-blue: "#476bef"
  link-blue-hover: "#0f7fff"
  footer-bg: "#313440"
  footer-link: "#8dc6e7"
  badge-in-stock: "#d5ffd8"
  badge-in-stock-text: "#008a06"
  badge-sold-out: "#ffdddd"
  badge-sold-out-text: "#cc4749"
  badge-preorder: "#fffdea"
  badge-preorder-text: "#f1a500"
  star-rating: "#f1a500"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Karla', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Karla', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Karla', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Karla', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Karla', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'Karla', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  nav-link-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-accent-gold-active:
    backgroundColor: "#d49400"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 16px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 32px 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  top-nav-link-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-primary}"
  secondary-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-sm}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
  secondary-nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link-sm}"
    padding: 8px 12px
  secondary-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 700
  product-card-price-sale:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-red}"
    fontWeight: 700
  product-card-price-original:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  badge-in-stock:
    backgroundColor: "{colors.badge-in-stock}"
    textColor: "{colors.badge-in-stock-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.badge-sold-out-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.badge-preorder-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-link}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.md}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    width: 36px
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "#006d05"
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.primary}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 600
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Buy Now," and checkout flows. Rendered on a #005586 blue background with white text in Montserrat 14px/600. On hover, shifts to #063f8a; disabled state uses #8dc6e7. Height is a consistent 48px with {rounded.sm} corners — substantial enough for a gaming marketplace where precision matters.

**`button-secondary`** — Used for "View Details," "Compare," and secondary actions within product cards. White background with a 1px #e5e5e5 border and #313440 text. Active state swaps to #fafafa background with #757575 border. Same 48px height and {rounded.sm} as primary for visual alignment.

**`button-accent-gold`** — Reserved for high-visibility actions like "Pre-Order Now" and "Flash Sale" CTAs. Uses #f1a500 gold background with dark #313440 text. Active state darkens to #d49400. This is the brand's voltage button — used sparingly to signal urgency or exclusivity.

**`button-accent-orange`** — Used for "Subscribe & Save" and promotional checkout options. #ff7600 background with white text. Same dimensions as primary. The orange sits between the gold accent and the red error/sold-out signals in the brand's traffic-light system.

**`button-ghost`** — A text-only button for inline actions like "Clear Filters," "Cancel," or "Remove." Transparent background with #005586 text. Active state adds a #fafafa background. No border, no padding beyond 14px 16px — the lightest touch in the button system.

**`button-sm`** — Compact button for pagination, filter bars, and mobile contexts. 32px height with 8px 16px padding. Uses the same #005586 primary but with 12px/600 Montserrat. {rounded.sm} corners maintained for consistency.

### Cards
**`product-card`** — The core inventory unit: a white card on #f5f5f5 canvas with 12px padding and {rounded.md} corners. Each card contains a square-ratio image, card title in Karla 15px/700, price in Karla 16px/700, and a status badge. Hover state adds a subtle box-shadow and darkens the border from #dfdfdf to #e5e5e5. Cards stack in a responsive grid — 2 columns on mobile, 3 on tablet, 4-5 on desktop.

**`product-card-price-sale`** — When a card shows a sale price, the current price renders in #cc4749 red at 16px/700, with the original price struck through in #8f8f8f 13px/400 below it. A red "SALE" badge overlays the top-right of the image.

**`badge-in-stock`** — A green pill badge (#d5ffd8 background, #008a06 text) positioned at the top-left of product card images. Uses Montserrat 11px/700 uppercase. The badge system is the brand's primary scannability tool — players filter by stock status before reading card names.

**`badge-sold-out`** — Red badge (#ffdddd background, #cc4749 text) that overlays the entire product image with 50% opacity scrim. The badge text reads "SOLD OUT" in the same uppercase Montserrat. The card remains clickable for back-in-stock notifications.

**`badge-preorder`** — Gold-tinted badge (#fffdea background, #f1a500 text) for upcoming releases. Reads "PRE-ORDER" and sits alongside the add-to-cart button rather than on the image, since pre-order cards are still purchasable.

### Navigation
**`top-nav`** — A persistent 48px dark bar (#313440) spanning the full viewport width. Contains the Star City Games logo (left), primary category links (center: "Singles," "Sealed," "Accessories," "Events"), and account/cart icons (right). Links are white Montserrat 14px/600 with 12px 16px padding; active state adds a subtle white overlay at 10% opacity. The cart icon carries a gold #f1a500 badge showing item count.

**`secondary-nav`** — A 40px white bar below the top nav, separated by a #e5e5e5 bottom border. Contains subcategory links (e.g., "Magic: The Gathering," "Lorcana," "Pokémon," "Flesh and Blood") in Montserrat 12px/600. Active link has a 2px #005586 bottom border. This nav collapses into a horizontal scroll on mobile.

**`search-bar`** — A full-width white input field with 40px height and {rounded.sm} corners. The search submit button is a 40px square in #007dc6 blue with a white magnifying-glass icon — the only place this specific blue appears in the UI, making it a recognizable search affordance. Focus state adds a 2px #8dc6e7 ring.

### Forms
**`text-input`** — Standard form input for checkout fields, account forms, and deck builder tools. 40px height, white background, 1px #e5e5e5 border, Karla 14px text. Focus state swaps border to #005586 with a #8dc6e7 ring. Used in shipping, billing, and search filters.

**`select-input`** — Dropdown select for sorting (Price Low-High, Set, Rarity, etc.). Same dimensions as text-input but with a 32px right-side chevron area. The chevron uses #757575 muted color.

**`quantity-selector`** — A compact 40px-high control with decrement/increment buttons (36px wide each, #fafafa background) flanking a central numeric display. Used on product detail pages and cart line items. The buttons use #313440 icons.

### Footer
**`footer`** — A dark inversion of the site: #313440 background with #8f8f8f body text and #8dc6e7 link color. Organized in a 4-column grid with Montserrat 15px/700 headings in white. Contains links to "About Us," "Sell to Us," "Events," "Support," and social icons. The bottom bar includes copyright text and payment method icons in grayscale. Section padding is 48px top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 551px | Single-column product grid; top nav collapses to hamburger + logo + cart; secondary nav becomes horizontal scroll; search bar moves below nav; filter sidebar becomes bottom sheet; footer stacks to single column |
| Tablet | 551–1024px | 2-column product grid; secondary nav fully visible; filter sidebar collapses to dropdowns; footer renders in 2-column layout |
| Desktop | 1024–1261px | 3-column product grid; full top nav visible; filter sidebar persistent on left; footer in 4-column grid |
| Wide | 1261–1681px | 4-column product grid; max-width container at 1681px; additional whitespace around product cards; filter sidebar wider |
| Ultra Wide | > 1681px | 5-column product grid; container centered with max-width; product cards have increased padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height on mobile
- Filter chips are 40px tall with 14px horizontal padding
- Quantity selector buttons are 44px wide on mobile (up from 36px on desktop)
- Product card tap targets (entire card) are minimum 120px tall
- Bottom nav bar (mobile) has 56px height for thumb reach
- Search bar submit button remains 44px on mobile

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 551px; secondary nav becomes a horizontal scrollable strip
- Filter sidebar collapses to a "Filters" button that opens a bottom sheet on mobile and tablet
- Product grid reduces from 5 columns (ultra wide) to 1 column (mobile)
- Footer navigation collapses from 4 columns to 1 column, with accordion-style expandable sections
- Breadcrumb trail truncates to show only current page on mobile, with a "Back" link
- Product card price and badge layout shifts from horizontal to vertical stack on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components were inferred from common patterns; the live site may use different transitions or box-shadows
- Error state styling for form inputs (red borders, error messages) could not be extracted — assumed standard #cc4749 treatment
- Dark mode is not present on the live site; no dark palette was extracted
- Sub-brand palettes for specific game categories (Magic: The Gathering vs. Lorcana vs. Pokémon) may exist but were not distinguishable in extraction
- Font weights beyond 400, 600, and 700 were not confirmed — Karla may use 500 for some body text
- The exact line-height values for body text are estimated from common web ratios; the live site may use slightly different values
- Animation durations and easing curves were not extractable
- The "Deck Builder" tool may have its own component system not reflected in the main site CSS
- Checkout flow components (Shopify Pay, Afterpay, Klarna) were filtered from extraction; their styling may conflict with the brand system
- The extracted color list includes many grays and blues that may belong to third-party widgets rather than the brand itself — the true brand palette may be more restrained than what extraction returned
