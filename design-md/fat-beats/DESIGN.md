---
version: alpha
name: "Fat Beats"
source_url: "https://www.fatbeats.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store's digital storefront that wears its hip-hop heritage in a single marigold accent — #ffb800 — a color that reads as both a vintage sticker on a crate and a highlighter on a rare 12-inch. The site runs on a near-monochrome palette of #dedede, #e1e1e1, and #121212, with the yellow appearing only on the primary CTA button and the "Add to Cart" pill, making each click feel like a purchase of something singular. The typography is Inter at modest weights (400–600), with product titles at 16px and prices at 14px — no display hero, no oversized headlines, just a clean, utilitarian grid that lets the album art do the talking. The navigation is a simple left-aligned logo and right-aligned cart icon, with a search bar that uses {rounded.full} and a soft gray border. Product cards are flat white rectangles with {rounded.sm} corners, a 1px hairline, and a hover state that subtly lifts the image. The footer is dense with links, divided into columns, and uses {colors.muted} for secondary text. The overall feel is that of a well-organized crate — everything has its place, the yellow tab tells you where to act, and the rest is quiet, letting the vinyl speak.

colors:
  primary: "#ffb800"
  primary-active: "#e6a600"
  primary-disabled: "#ffe080"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e1e1e1"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  badge-new: "#b3efb9"
  badge-sale: "#f1c3c6"
  badge-preorder: "#f8e1cb"
  star-rating: "#ffb800"
  link: "#121212"
  link-hover: "#ffb800"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-pill-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-logo:
    height: 32px
  nav-cart-icon:
    height: 24px
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  footer-link-hover:
    textColor: "{colors.ink}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    textColor: "{colors.ink}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"

## Components

### Buttons
**`button-primary`** — The single most important action on the page, filled with the brand's marigold accent (#ffb800) and dark ink text. On hover, it deepens to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}`. Used for "Add to Cart", "Checkout", and primary form submissions.
**`button-secondary`** — A white button with a 1px hairline border, used for secondary actions like "View Details" or "Continue Shopping". On hover, the border turns to ink and the background shifts to `{colors.surface-soft}`.
**`button-pill-cart`** — A compact, fully rounded pill used for inline cart additions (e.g., on product listing pages). Shares the primary yellow but with smaller padding and font size.

### Cards
**`product-card`** — A white rectangle with a 1px soft hairline border and `{rounded.sm}` corners. The image sits at a 1:1 aspect ratio with `{rounded.xs}`. Title is `{typography.title-sm}`, price is `{typography.body-sm}` in body gray. On hover, the border becomes a stronger hairline and a subtle shadow lifts the card. Badges (New, Sale, Preorder) sit in the top-left corner of the image, using soft pastel backgrounds from the extracted palette.
**`product-card-badge`** — Small uppercase labels in `{typography.badge}` with `{rounded.xs}`. Three variants: `badge-new` (green-tinted #b3efb9), `badge-sale` (pink-tinted #f1c3c6), and `badge-preorder` (peach-tinted #f8e1cb).

### Navigation
**`nav-bar`** — A simple 64px white bar with the Fat Beats logo on the left and a cart icon on the right. No dropdowns, no mega-menu — just a clean header that stays out of the way. The cart icon uses `{colors.ink}` and links to the Shopify cart.
**`breadcrumb`** — Light gray caption text with `{colors.muted-soft}`, used on product detail pages to show the category path. The active (last) crumb uses `{colors.ink}`.

### Forms
**`text-input`** — A standard input with a 1px hairline border and `{rounded.sm}`. On focus, the border switches to `{colors.ink}`. Used for email signups, search, and checkout fields.
**`search-bar`** — A fully rounded pill input with a 1px hairline border, used in the header for product search. Same height as the nav bar (44px) for visual alignment.
**`filter-dropdown`** — A compact dropdown with `{rounded.sm}` and a hairline border, used on collection pages to sort by artist, genre, or price.

### Footer
**`footer`** — A dense, multi-column footer on a `{colors.surface-soft}` background. Each column has a `{typography.title-sm}` heading and a list of `{typography.link}` items in muted gray. On hover, links turn to `{colors.ink}`. The footer includes links to About, Shipping, Returns, and social media.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 items per row), nav bar collapses to hamburger menu, footer stacks vertically, search bar moves below logo |
| Tablet | 744–1128px | Two-column product grid, nav bar remains horizontal but with reduced padding, footer splits into two rows of columns |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with logo and cart icon, footer in full multi-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, increased whitespace on sides |

### Touch Targets
- All buttons and links have a minimum tap target of 44x44px
- Cart icon has a 48x48px touch area (padding inside nav bar)
- Filter dropdowns are 40px tall with 44px touch area
- Product card images are tappable with a minimum 120x120px area

### Collapsing Strategy
- On mobile, the nav bar collapses to a hamburger menu with a slide-out drawer
- The footer collapses from 4 columns to 2, then to a single vertical stack on mobile
- The product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- The search bar collapses from a full-width pill to a compact icon that expands on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hover states for buttons, links, or cards (assumed from common patterns)
- No extracted focus or active states for form inputs
- No extracted error styling for form validation
- No extracted dark mode or high-contrast mode
- No extracted sub-brand or seasonal color palettes
- No extracted typography scale beyond Inter (weights, line heights, letter spacing are inferred from common Inter usage)
- No extracted spacing or rounded values (these are standard design system defaults)
- No extracted component-specific tokens (e.g., product card shadow, badge padding)
- The extracted hex list includes several pastel tones (#f1c3c6, #fcecec, #eefcef, #f8e1cb, #d2e4ff, #b3efb9) that may be Shopify widget defaults or stock image tones — the brand's true palette is likely the marigold (#ffb800) and grayscale (#dedede, #e1e1e1, #121212)
- No extracted logo or icon specifications
- No extracted animation or transition timing
- No extracted z-index or stacking context
