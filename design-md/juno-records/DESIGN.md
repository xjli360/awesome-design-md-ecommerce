---
version: alpha
name: "Juno Records"
source_url: "https://www.juno.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dense, information-rich marketplace for dance music vinyl and digital, built on a single high-contrast axis: #313131 ink on white canvas, with no decorative color system to soften the transaction. The site reads like a warehouse racking system — every page is a grid of small cover thumbnails, price tags, genre badges, and stock-status indicators, all set in the system sans-serif stack at modest sizes (13–14px body). There are no hero images, no lifestyle photography, no brand illustrations; the product jacket is the hero. The search bar sits permanently at the top with a dropdown that surfaces genres, labels, and artists before you finish typing — a power-user tool, not a discovery portal. Buttons are tight rectangles (`{rounded.xs}` ~4px) with #313131 fill and white text, and the same shape is reused for genre pills, cart actions, and filter toggles, creating a consistent mechanical rhythm. The only visual relief comes from the record sleeves themselves — a thousand different colors fighting for attention in a 4-column grid — and from the yellow "SALE" badges and orange "NEW RELEASES" tags that break the monochrome with urgency signals. The typography is purely functional: weight 400 body, weight 600 for headings, no display sizes above 24px, no letter-spacing tricks. This is a site built for people who already know what they want — crate diggers, DJs, collectors — and it optimizes for scan speed over persuasion. The footer is a dense column of links, payment icons, and social handles, with no decorative dividers; the hairline is a thin #dcdcdc line that separates sections without ceremony. Juno Records doesn't sell a vibe — it sells records, and the design gets out of the way.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#888888"
  ink: "#313131"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#dcdcdc"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#ffcc00"
  new-release-badge: "#ff6600"
  preorder-badge: "#3399ff"
  stock-in: "#2ecc71"
  stock-low: "#ff9900"
  stock-out: "#cc0000"
  link: "#0066cc"
  link-visited: "#551a8b"
  star-rating: "#ffcc00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.sale-badge}"

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
    padding: 10px 20px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
  button-pill-genre:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 28px
  button-pill-genre-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 28px
  button-cart-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  button-cart-added:
    backgroundColor: "{colors.stock-in}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    fontWeight: 700
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  product-card-thumbnail:
    width: "100%"
    aspectRatio: "1/1"
    objectFit: "cover"
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    height: 18px
  product-card-badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.ink}"
  product-card-badge-new:
    backgroundColor: "{colors.new-release-badge}"
    textColor: "{colors.on-primary}"
  product-card-badge-preorder:
    backgroundColor: "{colors.preorder-badge}"
    textColor: "{colors.on-primary}"
  product-card-stock:
    typography: "{typography.caption-sm}"
    marginTop: "{spacing.xs}"
  product-card-stock-in:
    textColor: "{colors.stock-in}"
  product-card-stock-low:
    textColor: "{colors.stock-low}"
  product-card-stock-out:
    textColor: "{colors.stock-out}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    borderRight: "1px solid {colors.hairline}"
  filter-section-header:
    typography: "{typography.title-sm}"
    paddingBottom: "{spacing.sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} 0"
  filter-checkbox-active:
    textColor: "{colors.primary}"
    fontWeight: 600
  genre-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    height: 24px
  genre-badge-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    height: 24px
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    fontWeight: 700
    rounded: "{rounded.xs}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    textColor: "{colors.link}"
    typography: "{typography.caption}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 600
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-section-header:
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  social-icon-link:
    textColor: "{colors.muted}"
    height: 24px
  payment-icon:
    height: 20px
    opacity: 0.6
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-item-title:
    typography: "{typography.title-sm}"
  cart-item-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  cart-item-price:
    typography: "{typography.price}"
  cart-item-quantity:
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "4px 8px"
    height: 32px
  cart-total:
    typography: "{typography.title-md}"
    paddingTop: "{spacing.md}"
    borderTop: "2px solid {colors.primary}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
    width: "100%"
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 32px
  quantity-stepper-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: "0 8px"
    height: 30px
  quantity-stepper-input:
    typography: "{typography.body-md}"
    textAlign: center
    width: 40px
    height: 30px
    borderLeft: "1px solid {colors.hairline}"
    borderRight: "1px solid {colors.hairline}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginLeft: "{spacing.xs}"
  product-detail-page:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.base}"
  product-detail-title:
    typography: "{typography.display-md}"
    marginBottom: "{spacing.sm}"
  product-detail-artist:
    typography: "{typography.title-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.base}"
  product-detail-label:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-detail-catno:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  product-detail-description:
    typography: "{typography.body-md}"
    lineHeight: 1.6
    marginTop: "{spacing.lg}"
  product-detail-tracklist:
    typography: "{typography.body-sm}"
    lineHeight: 1.5
  product-detail-track:
    padding: "{spacing.xs} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  product-detail-track-number:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    width: 24px
  product-detail-track-title:
    typography: "{typography.body-sm}"
  product-detail-track-duration:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    marginLeft: auto
  product-detail-actions:
    marginTop: "{spacing.lg}"
    padding: "{spacing.base} 0"
    borderTop: "1px solid {colors.hairline}"
  product-detail-format-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    height: 22px
  product-detail-format-badge-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — The primary action button, used for "Add to Cart", "Checkout", and "Search". Filled with `{colors.primary}` (#313131) and white text, with tight `{rounded.xs}` corners and compact 10px/20px padding. On hover, shifts to `{colors.primary-active}` (#1a1a1a). Disabled state uses `{colors.primary-disabled}` (#888888). No icon, no shadow — purely functional.

**`button-secondary`** — Outline variant for secondary actions like "View Details" or "Cancel". White background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Same dimensions as primary. Hover state adds a subtle border darkening to `{colors.muted}`.

**`button-tertiary-text`** — Text-only link-style button for actions like "Clear Filters" or "Remove". Uses `{colors.link}` blue, no background, no border. Hover state underlines.

**`button-pill-genre`** — Genre filter pills used in the browse strip and sidebar. Soft gray background (`{colors.surface-soft}`) with `{rounded.full}` pill shape, compact 6px/14px padding. Active state flips to `{colors.primary}` fill with white text. Used for "House", "Techno", "Drum & Bass", etc.

**`button-cart-add`** — Compact add-to-cart button on product cards and detail pages. Smaller than primary (32px height), with `{button-sm}` typography. After adding, transitions to `button-cart-added` with green background (`{colors.stock-in}`) and "Added" text.

### Cards
**`product-card`** — The core listing unit across browse, search, and category pages. A simple white rectangle with no border or shadow — the record cover thumbnail provides the visual boundary. Contains thumbnail (1:1 aspect ratio, `{rounded.xs}`), title, artist name, price, and optional badges. Stock status appears as colored text below the price: green for "In Stock", orange for "Low Stock", red for "Out of Stock".

**`product-card-badge`** — Small uppercase labels overlaid on or beside the thumbnail. Three variants: `sale-badge` (yellow `{colors.sale-badge}` background, black text), `new-release-badge` (orange `{colors.new-release-badge}` background, white text), `preorder-badge` (blue `{colors.preorder-badge}` background, white text). 11px bold, 2px/6px padding.

### Navigation
**`top-nav`** — A 48px sticky bar with the Juno logo left, primary nav links center (Vinyl, CD, Digital, Equipment, Charts, New Releases, Pre-Orders), and search/user/cart icons right. White background with a single `{colors.hairline}` bottom border. Links use `{nav-link}` typography (13px, weight 600). Active page link gets `{colors.primary}` text color and weight 700.

**`search-bar`** — A 40px text input with `{rounded.xs}` corners and a 1px `{colors.hairline}` border. On focus, border thickens to 2px `{colors.primary}`. Typing triggers a `search-dropdown` panel with autocomplete results grouped by Artists, Labels, and Releases.

**`breadcrumb`** — Simple text navigation path (e.g. "Home > Vinyl > House > New Releases"). Uses `{caption}` size (12px) with `{colors.muted}` for separators and `{colors.link}` blue for clickable segments. Current page is `{colors.ink}` weight 600.

### Forms & Filters
**`text-input`** — Standard form input for checkout fields (name, address, payment). 36px height, `{rounded.xs}`, 1px `{colors.hairline}` border. Focus state uses 2px `{colors.primary}` border. No placeholder styling beyond system default.

**`filter-sidebar`** — Left-hand filter panel on browse pages, with sections for Genre, Format, Price Range, Label, and Release Year. Each section has a `filter-section-header` with a bottom hairline. Checkboxes use `filter-checkbox` styling — active items get `{colors.primary}` text and weight 600.

**`genre-badge`** — Clickable genre tags in the filter area. Same pill shape as `button-pill-genre` but slightly larger (24px height). Active state uses `{colors.primary}` fill.

### Cart & Checkout
**`cart-item`** — Line item in the shopping cart dropdown or full cart page. Shows thumbnail, title, artist, format, price, and a `quantity-stepper`. Items separated by `{colors.hairline-soft}` borders.

**`quantity-stepper`** — A compact 32px control with decrement button, numeric input (40px wide), and increment button. All three elements share a 1px `{colors.hairline}` border and `{rounded.xs}` container. The input has left/right inner borders separating it from the buttons.

**`checkout-button`** — Full-width primary button (48px height) at the bottom of the cart. Same styling as `button-primary` but wider. On hover, shifts to `{colors.primary-active}`.

### Product Detail
**`product-detail-page`** — Full product view with large thumbnail, title, artist, label, catalog number, format badges, price, stock status, add-to-cart button, description, and tracklist. The tracklist uses `product-detail-track` rows with track number, title, and duration — a compact, scannable list with `{colors.hairline-soft}` separators.

**`product-detail-format-badge`** — Small tags indicating available formats (12" Vinyl, CD, MP3, WAV, FLAC). Gray background with `{rounded.xs}` corners. Active/selected format gets `{colors.primary}` fill.

### Footer
**`footer`** — A dense multi-column footer with `{colors.surface-soft}` background and `{colors.hairline}` top border. Contains sections for Customer Service, About Juno, Community, and Social Links. Links are `{colors.muted}` 13px text. Payment icons appear at the bottom at 20px height with 0.6 opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes a bottom sheet or accordion; top-nav collapses to hamburger menu; search bar shrinks to icon-only; product detail page stacks vertically; quantity stepper becomes full-width |
| Tablet | 744–1128px | 2-column product grid; filter sidebar remains visible but collapsible; top-nav shows abbreviated links (Vinyl, CD, Digital); search bar shows full width |
| Desktop | 1128–1440px | 3-4 column product grid; full filter sidebar; complete top-nav with all links; product detail page shows 2-column layout (thumbnail left, info right) |
| Wide | > 1440px | 4-5 column product grid; max-width container (1440px) centered; filter sidebar width increases to 280px; product detail page uses wider layout with larger thumbnail |

### Touch Targets
- All buttons and clickable elements: minimum 36px height (primary buttons 36px, checkout button 48px)
- Genre pills and filter badges: minimum 28px height
- Quantity stepper buttons: 30px height, 16px width minimum
- Top-nav links: 48px tap area (full nav height)
- Search bar: 40px height
- Product card thumbnails: tap target is the full card area

### Collapsing Strategy
- Top-nav links: On mobile (< 744px), all nav links collapse into a hamburger menu. The logo and cart icon remain visible.
- Filter sidebar: On mobile, the sidebar becomes a "Filters" button that opens a bottom sheet or full-screen overlay. On tablet, the sidebar can be toggled open/closed with a "Show Filters" button.
- Product grid: Columns reduce from 4-5 on wide desktop to 1 on mobile. The grid uses CSS grid with `auto-fill` and `minmax(160px, 1fr)` on desktop, dropping to `minmax(140px, 1fr)` on mobile.
- Search dropdown: On mobile, the search bar expands to full width below the top-nav when focused, pushing content down.
- Product detail page: On mobile, the tracklist collapses to show only first 5 tracks with a "Show all N tracks" toggle.
- Footer: On mobile, footer sections collapse into accordion panels with expand/collapse toggles.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site. The full color palette (badge colors, stock indicators, link colors, star rating) has been inferred from common Juno Records patterns and standard e-commerce conventions, but has not been verified against the live site's CSS.
- No secondary or accent brand color could be extracted. The site appears to be intentionally monochrome, with color introduced only through product imagery and status badges.
- Font-family declarations returned only system font stacks. Juno Records likely uses the system sans-serif stack without a custom typeface — this has been preserved faithfully.
- Hover, focus, active, and disabled states for all components are inferred from standard web patterns, not extracted from the live site.
- Error styling (form validation, 404 pages, empty states) could not be extracted.
- Dark mode is not supported and likely not implemented.
- Animation and transition durations/easings could not be extracted.
- Box shadows and elevation levels could not be extracted (only one shadow value inferred for the search dropdown).
- The checkout flow may use a third-party payment gateway (Stripe, PayPal, etc.) with its own design system — those components are not captured here.
- Mobile navigation patterns (hamburger menu, bottom sheets) are inferred from common responsive patterns, not extracted from the live mobile site.
- The exact product grid column count and breakpoints are estimated based on common e-commerce patterns and may differ from the live responsive implementation.
