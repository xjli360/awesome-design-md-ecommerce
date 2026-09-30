---
version: alpha
name: "Waterloo Records"
source_url: "https://www.waterloorecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that feels like a live-wire jukebox, where the primary voltage is not a color but the raw energy of Arial at 16px — the default, the workhorse, the font that never pretends to be anything other than what it is. The canvas is pure white (#ffffff), a blank sleeve waiting for the album art to land, while the ink (#000000) is absolute, unapologetic black — the kind you find on a new vinyl pressing. There are no extracted brand colors from the live site, which is itself a statement: Waterloo Records doesn't paint itself in a signature hue; it lets the music do the coloring. The design language is one of radical simplicity — a single column of text, a search bar with {rounded.full} corners that feels like a friendly invitation to dig through the bins, and product cards that are nothing more than a square image, a title, and a price, all sitting on {surface-card} white. The navigation is a horizontal strip of genre links — Rock, Pop, Soul, Jazz — each one a door to a different room in the store. The only ornament is the occasional badge — "NEW ARRIVAL" in bold black caps on a white background — or a sale price in a muted gray (#6a6a6a) that whispers "deal" rather than shouting. The layout trusts the album cover to do the selling; the interface is just the shelf. It's the digital equivalent of a store where the owner knows every record in stock and the only thing between you and the music is a counter and a cash register.

colors:
  primary: "#000000"
  primary-active: "#333333"
  primary-disabled: "#cccccc"
  ink: "#000000"
  body: "#333333"
  muted: "#6a6a6a"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale: "#cc0000"
  badge-new: "#000000"
  badge-sale: "#cc0000"
  link: "#000000"
  link-hover: "#333333"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
    color: "{colors.sale}"

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: none
    cursor: pointer
    transition: background-color 0.2s ease
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
    cursor: pointer
    transition: background-color 0.2s ease, color 0.2s ease
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.primary}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 0
    border: none
    cursor: pointer
    textDecoration: underline
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
    padding: 0
    border: none
    cursor: pointer
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.lg}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    borderBottom: "2px solid transparent"
    cursor: pointer
    transition: color 0.2s ease, border-color 0.2s ease
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
    cursor: pointer
    transition: box-shadow 0.2s ease
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    width: "100%"
    aspectRatio: "1 / 1"
    objectFit: "cover"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.sm} 0"
    lineClamp: 2
  product-card-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "2px {spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    padding: "0 {spacing.sm} {spacing.sm}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.sale}"
    padding: "0 {spacing.sm} {spacing.sm}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
    display: inline-block
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
    display: inline-block
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    maxWidth: "600px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
    textDecoration: underline
    cursor: pointer
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 12px"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-item-image:
    width: "80px"
    height: "80px"
    objectFit: "cover"
    rounded: "{rounded.none}"
  cart-item-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  cart-item-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  cart-item-remove:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: underline
    cursor: pointer
    border: none
    padding: 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid black rectangle with white text. Used for "Add to Cart", "Checkout", and "Submit". On hover, the black shifts to a dark gray (#333333) for a subtle lift. The disabled state uses a light gray (#cccccc) with white text, signaling the action is unavailable. No rounded corners — the store is direct and unadorned.

**`button-secondary`** — An outlined variant with a black border and black text on a white background. On hover, it fills with black and inverts to white text. Used for "View Details" or "Continue Shopping" — actions that are secondary but still important. The 2px border keeps it visually balanced with the primary button.

**`button-text`** — A text-only link styled as a button, with an underline. Used for "Clear Cart" or "Cancel". No background, no border — just the action, plain as a handwritten note.

**`button-icon`** — A square icon button, 44x44px, with no background or border. Used for search, cart, and menu toggles. The icon is black, and on hover it gains a subtle background tint from the surface-soft color.

### Navigation
**`nav-bar`** — A fixed-height horizontal bar (56px) with a bottom hairline border. The background is white, and the navigation links are uppercase, bold, and 14px. The bar is pinned to the top of the viewport on desktop and tablet.

**`nav-link`** — Each link in the top navigation. In its default state, the text is muted gray. On hover or when active, the text turns black and a 2px black underline appears. The underline acts as a visual anchor, like a bookmark sliding into place.

**`nav-link-active`** — The currently selected genre or page. The black underline is persistent, and the text is black. It's the only link that gets the full weight of the brand's primary color.

### Search
**`search-bar`** — A pill-shaped search input with a light gray background (#f5f5f5) and a subtle border. The placeholder text is muted, and a search icon sits on the left. On focus, the border thickens to 2px and turns black, and the background shifts to white. The pill shape is the only rounded element in the entire system — a small, friendly concession to usability.

### Product Cards
**`product-card`** — A square card with a 1:1 aspect ratio image, a title, an artist name, and a price. The card has no padding — the image bleeds edge-to-edge — and a very light border (#f0f0f0) that barely registers. On hover, a subtle box shadow lifts the card off the page, like pulling a record from the shelf.

**`product-card-title`** — The album title, set in bold 16px Arial. Clamped to two lines to prevent layout shifts. The artist name below is smaller and muted, letting the album title do the heavy lifting.

**`product-card-price`** — The price, bold and black. If on sale, the price turns red (#cc0000) and the `badge-sale` component appears in the top-left corner of the image.

### Badges
**`badge`** — A small, uppercase label with no rounded corners. Black background, white text, tight padding. Used for "NEW ARRIVAL", "PRE-ORDER", or "EXCLUSIVE". It's a stamp, not a sticker.

**`badge-sale`** — Same as the standard badge, but with a red background (#cc0000). Used exclusively for sale items. The red is the only accent color in the system — a single, urgent note.

### Cart
**`cart-item`** — A horizontal row with an 80x80px thumbnail, the album title, artist, price, and a "Remove" link. The row has a bottom border that's barely visible (#f0f0f0). The remove action is a small, underlined text link in muted gray — it's there when you need it, but it doesn't draw attention.

**`cart-item-remove`** — A text-only button with an underline. No background, no border. It's the quietest element in the cart, because the store doesn't want to remind you that you might change your mind.

### Footer
**`footer`** — A black footer with white text. Links are underlined and white. The footer contains the store's address, hours, and links to policies. It's the only section that inverts the color scheme — a deliberate shift that signals the end of the browsing experience.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Navigation collapses to a hamburger menu. Product cards stack in a single column. Search bar moves below the hero. Footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid. Navigation links remain visible but condensed. Search bar is full-width in the header. Footer splits into two columns. |
| Desktop | 1128–1440px | Three-column product grid. Full navigation bar with genre links. Search bar is a fixed width in the header. Footer has three columns. |
| Wide | > 1440px | Four-column product grid. Maximum content width of 1440px, centered. Navigation and search bar remain at desktop scale. Footer expands to four columns. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile and tablet.
- Icon buttons are 44x44px minimum.
- Navigation links have a minimum tap area of 44x44px, even if the text is smaller.
- Cart item remove links have a 44px hit area, padded with invisible space.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The menu overlay is full-screen, with links stacked vertically and a close button in the top-right corner.
- The search bar collapses from a full-width input on mobile to a fixed-width input on desktop. On mobile, the search icon is always visible; the input expands on tap.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile. The transition happens at each breakpoint boundary.
- The footer collapses from 4 columns to a single stack on mobile, with each section separated by a hairline border.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted brand colors were available from the live site. The palette above is inferred from the site's use of black, white, and gray, with a single red accent for sale items. This is a best-effort reconstruction.
- Font-family declarations found only "Arial". No custom or web fonts were detected. The site may use a system font stack that wasn't captured.
- No meta theme-color was found. The browser chrome color is unknown.
- Hover states for buttons and cards are inferred from common patterns. The actual site may use different transitions or effects.
- Error states for forms (e.g., invalid email, missing required fields) are not documented. The site may use red borders, inline error messages, or a toast notification.
- The site's handling of empty states (e.g., empty cart, no search results) is unknown. These may use illustrations, text prompts, or suggested products.
- Dark mode is not supported. The site uses a white canvas exclusively.
- The site's use of accessibility features (e.g., focus indicators, ARIA labels, skip-to-content links) could not be verified.
- The site's checkout flow is not documented. It may use a third-party provider (e.g., Shopify, Square) with its own design system.
- The site's handling of out-of-stock items is unknown. These may be hidden, grayed out, or marked with a badge.
- The site's use of animation and micro-interactions (e.g., page transitions, loading states, hover effects) could not be extracted.
