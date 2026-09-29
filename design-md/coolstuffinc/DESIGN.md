---
version: alpha
name: "CoolStuffInc"
source_url: "https://www.coolstuffinc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A trading card marketplace that wears its inventory density like a badge of honor, CoolStuffInc runs on a deep teal primary (#008cba) that feels more like a vintage game-store awning than a standard e-commerce blue. The palette is built for information hierarchy at scale: #222222 ink on #ffffff canvas for product titles, #555555 body for prices and condition notes, and a constellation of accent colors — #990000 for sold-out badges, #f1da36 for star-rating highlights, #43ac6a for in-stock indicators, #f04124 for clearance flags — that turn the page into a trading-floor ticker. Navigation bars sit in #00303f, a near-black teal that grounds the header without competing with product imagery. The typography stack is a pragmatic mix of AppleGothic for system-level headers, Arial for body copy, and Century Gothic for display moments, all set against a canvas of #ebebeb and #eeeeee that softens the high-density grid. Buttons use {rounded.sm} corners — functional, not decorative — and the primary CTA (#008cba on #ffffff) carries the same weight as a "Buy Now" on a sealed booster box. The search bar, a full-width field with a #008cba border, is the most prominent interactive element, reflecting a site built for collectors who know exactly what they want. Badges are sharp: #990000 for "Sold Out", #43ac6a for "In Stock", #cf2a0e for "Clearance", each with {rounded.xs} and white text. The footer collapses into a dense stack of #014459 links on #00303f, a final dark anchor that signals the end of the browsing session. This is not a brand that whispers; it's a brand that tags, prices, and ships.

colors:
  primary: "#008cba"
  primary-active: "#007095"
  primary-disabled: "#61b6d9"
  ink: "#222222"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#b9b9b9"
  hairline-soft: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-bg: "#00303f"
  nav-bg-hover: "#014459"
  badge-soldout: "#990000"
  badge-instock: "#43ac6a"
  badge-clearance: "#cf2a0e"
  badge-comingsoon: "#f08a24"
  star-rating: "#f1da36"
  link-default: "#008cba"
  link-hover: "#0e809b"
  footer-bg: "#00303f"
  footer-link: "#a0d3e8"
  error: "#cf2a0e"
  success: "#43ac6a"
  warning: "#f08a24"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Century Gothic', AppleGothic, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Century Gothic', AppleGothic, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "AppleGothic, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "AppleGothic, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "AppleGothic, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "AppleGothic, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "AppleGothic, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Century Gothic', AppleGothic, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
    borderColor: "{colors.primary}"
    borderWidth: 2px
  search-bar-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-hover:
    backgroundColor: "{colors.nav-bg-hover}"
    textColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
  product-card-hover:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  product-card-image:
    rounded: "{rounded.xs}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-instock:
    backgroundColor: "{colors.badge-instock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-clearance:
    backgroundColor: "{colors.badge-clearance}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-comingsoon:
    backgroundColor: "{colors.badge-comingsoon}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  star-rating:
    color: "{colors.star-rating}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-link}"
    typography: "{typography.link}"
    padding: 24px 16px
  footer-link:
    color: "{colors.footer-link}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-dark}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and "Checkout". Rendered in {colors.primary} (#008cba) with white text and {rounded.sm} corners. On hover, shifts to {colors.primary-active} (#007095). Disabled state uses {colors.primary-disabled} (#61b6d9) with white text. Height is 40px with 10px 20px padding.
**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Wishlist". White background with {colors.primary} text and a 1px {colors.primary} border. Hover state fills with {colors.primary} and white text. Same 40px height as primary.
**`button-danger`** — Reserved for destructive actions like "Remove from Cart" or "Cancel Order". Uses {colors.error} (#cf2a0e) background with white text. Hover darkens to #b32505.
**`button-tertiary-text`** — A text-only button for inline actions like "Clear Filters" or "Show More". Transparent background, {colors.primary} text, no border. Hover adds underline.

### Badges
**`badge-soldout`** — A compact, uppercase label for out-of-stock items. {colors.badge-soldout} (#990000) background, white text, {rounded.xs} corners, 2px 6px padding. Positioned top-right on product card images.
**`badge-instock`** — Green indicator for available inventory. {colors.badge-instock} (#43ac6a) background. Same sizing as soldout badge.
**`badge-clearance`** — Red-orange badge for discounted items. {colors.badge-clearance} (#cf2a0e) background. Same sizing.
**`badge-comingsoon`** — Amber badge for pre-order items. {colors.badge-comingsoon} (#f08a24) background. Same sizing.

### Cards
**`product-card`** — The core product display unit in grid and list views. White background, {rounded.sm} corners, 1px {colors.hairline-soft} (#e7e7e7) border, 12px padding. On hover, border switches to 2px {colors.primary} (#008cba). Contains an image area with {rounded.xs}, a title in {typography.title-sm}, and price in {typography.price-md}.
**`product-card-image`** — The image container within a product card. {rounded.xs} corners, {colors.surface-soft} (#ebebeb) background as placeholder while images load. Aspect ratio maintained at 1:1 for trading cards.

### Navigation
**`nav-bar`** — The primary site header. {colors.nav-bg} (#00303f) background, white text, 56px height. Contains logo, category links, and search bar. Sticky on scroll.
**`nav-link`** — Navigation items within the header. White text on {colors.nav-bg}, 8px 16px padding. Hover state uses {colors.nav-bg-hover} (#014459) background.
**`footer`** — Site footer with links, contact info, and legal text. {colors.footer-bg} (#00303f) background, {colors.footer-link} (#a0d3e8) link color, 24px 16px padding. Links lighten to white on hover.

### Forms & Inputs
**`text-input`** — Standard text input for forms (search, account, checkout). White background, {colors.ink} (#222222) text, 1px {colors.hairline} (#b9b9b9) border, {rounded.sm} corners, 8px 12px padding, 40px height. On focus, border becomes 2px {colors.primary} (#008cba).
**`search-bar`** — The primary search input, more prominent than standard inputs. 2px {colors.primary} (#008cba) border, 44px height, 8px 16px padding. Paired with a {colors.primary} search button of matching height.
**`category-filter`** — Filter chips for browsing by category (e.g., "Pokémon", "Magic: The Gathering", "Yu-Gi-Oh!"). {colors.surface-soft} (#ebebeb) background, {colors.body} (#555555) text, 1px {colors.hairline} border, {rounded.sm} corners, 6px 12px padding. Active state uses {colors.primary} background and white text.

### Pagination
**`pagination-button`** — Page navigation buttons at the bottom of search results. White background, {colors.primary} text, 1px {colors.hairline} border, {rounded.sm} corners, 6px 12px padding. Active page uses {colors.primary} background and white text.

### Loading
**`loading-spinner`** — A circular progress indicator in {colors.primary} (#008cba), 24px diameter. Used during product list loading, search, and checkout processing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, stacked filters, hamburger nav, search bar collapses to icon, footer links stack vertically, badges become full-width |
| Tablet | 744–1128px | Two-column product grid, horizontal filter strip with scroll, nav links collapse to dropdown, search bar remains full-width |
| Desktop | 1128–1440px | Three-column product grid, full nav visible, filters in sidebar, search bar prominent in header, footer in two columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, filters in persistent sidebar, additional whitespace around cards |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets
- Product card tap targets: entire card is clickable, minimum 120px height
- Category filter chips: 36px minimum height, 12px horizontal padding
- Pagination buttons: 36px minimum height and width
- Nav links: 44px minimum tap area (56px nav bar accommodates this)
- Search bar: 44px height, full-width on mobile

### Collapsing Strategy
- Primary nav: On mobile (< 744px), full nav links collapse into a hamburger menu; category dropdowns become accordion panels
- Filter sidebar: On mobile and tablet, filters collapse into a "Filter" button that opens a full-screen overlay
- Product grid: Collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer: Collapses from 2 columns (desktop) to stacked single column (mobile)
- Search bar: On mobile, collapses to a search icon that expands to full-width on tap
- Category strip: On mobile, becomes horizontally scrollable with snap points

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from common patterns; exact hex values for hover backgrounds (beyond primary-active) were not extracted from the live site
- Error state styling for form inputs (border color, error message typography) not extracted; assumed {colors.error} (#cf2a0e) based on badge usage
- Dark mode is not supported; no extracted colors suggest a dark theme
- Sub-brand or promotional palettes (e.g., holiday sales, special editions) not captured
- Font weights beyond 400, 600, 700 are not confirmed; extracted font-family declarations did not include weight-specific variants
- Line-height and letter-spacing values are estimated based on standard web typography; exact values from the live site were not extractable
- The extracted hex list is heavily weighted toward grays (#ebebeb, #eeeeee, #555555, #aaaaaa, #888888, #ececec, #b9b9b9, #777777, #e7e7e7, #efefef) and blues (#008cba, #0e809b, #006782, #007095, #61b6d9, #0a829a, #5897fb, #a0d3e8, #014459), with a few accent colors (#990000, #f1da36, #f04124, #cf2a0e, #cf6e0e, #368a55, #008000, #43ac6a, #f08a24). The true primary (#008cba) was selected as the most distinctive blue that appears in navigation and CTAs. The remaining blues may represent hover states, secondary links, or footer backgrounds.
- The extracted font-family list includes system fonts (AppleGothic, Arial, Century Gothic, Consolas, Courier) and Font Awesome icon fonts. No custom web fonts were detected; the brand likely relies on system font stacks. Century Gothic is used for display headings based on its presence in the extracted list and common usage in trading card marketplaces.
- Checkout flow components (payment forms, address validation, order summary) not extracted; may use third-party widgets with their own styling
- Animation and transition durations (hover effects, page loads, modal opens) not extracted
- Focus-visible styles for keyboard navigation not extracted
- Print stylesheet behavior not extracted
