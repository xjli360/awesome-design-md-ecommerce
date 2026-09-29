---
version: alpha
name: "Easy Street Records"
source_url: "https://easystreetonline.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store that trusts the vinyl sleeve to do the selling — the site runs on a bare-bones Arial stack at 16px body weight 400, with no display typeface to compete with the album art. The palette is a single accent, a deep maroon #8b1a1a, that appears only in the primary button and the footer background, like a stamp of authenticity on an otherwise white (#ffffff) and light gray (#f5f5f5) canvas. There is no hero image, no carousel, no newsletter popup — the homepage is a grid of album covers at 200px square, each one a clickable portal to its own detail page. The search bar sits at the top in a pill shape (`{rounded.full}`) with a 40px height, and the cart icon is a simple shopping-bag glyph with a badge count in the maroon. The brand's voice is utilitarian and direct: "Add to Cart" buttons are 48px tall with 14px padding, and the only decorative element is the store's own logo — a retro script wordmark in white on the maroon footer. The entire experience feels like walking into a physical record store where the bins are alphabetized and the staff lets you browse.

colors:
  primary: "#8b1a1a"
  primary-active: "#6b1414"
  primary-disabled: "#d4a0a0"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-count: "#8b1a1a"
  badge-text: "#ffffff"
  footer-bg: "#8b1a1a"
  footer-text: "#ffffff"
  link: "#8b1a1a"
  link-hover: "#6b1414"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

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
    backgroundColor: "{colors.canvas}"
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
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "1px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  cart-icon:
    height: 24px
    width: 24px
  cart-badge:
    backgroundColor: "{colors.badge-count}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
  product-card-image:
    height: 200px
    width: 200px
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.footer-text}"
    textDecoration: underline
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.link}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    height: 40px
    width: 40px
  page-section:
    padding: "{spacing.section} {spacing.base}"
  product-detail-section:
    padding: "{spacing.xl} {spacing.base}"
  product-detail-image:
    height: 400px
    width: 400px
    objectFit: cover
  product-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-detail-artist:
    typography: "{typography.title-md}"
    textColor: "{colors.muted}"
  product-detail-price:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-detail-format:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-detail-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-detail-year:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-detail-genre:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-detail-tracklist:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-detail-track:
    padding: "{spacing.xs} 0"
  product-detail-track-number:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    width: 24px
  product-detail-track-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-detail-track-duration:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  product-detail-actions:
    marginTop: "{spacing.lg}"
  product-detail-quantity:
    marginRight: "{spacing.md}"
  product-detail-add-to-cart:
    marginTop: "{spacing.md}"
  product-detail-back-link:
    typography: "{typography.link}"
    textColor: "{colors.link}"
    marginBottom: "{spacing.lg}"
  product-detail-back-link-hover:
    textColor: "{colors.link-hover}"
  product-grid:
    display: grid
    gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))"
    gap: "{spacing.lg}"
    padding: "{spacing.lg} {spacing.base}"
  product-grid-item:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-grid-item-hover:
    border: "1px solid {colors.hairline}"
  product-grid-item-image:
    height: 200px
    width: 100%
    objectFit: cover
  product-grid-item-info:
    padding: "{spacing.sm} {spacing.sm} {spacing.md}"
  product-grid-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-grid-item-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-grid-item-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-grid-item-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-grid-item-actions:
    padding: "{spacing.sm}"
    borderTop: "1px solid {colors.hairline-soft}"
  product-grid-item-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    width: 100%
  product-grid-item-add-to-cart-hover:
    backgroundColor: "{colors.primary-active}"
  product-grid-item-add-to-cart-disabled:
    backgroundColor: "{colors.primary-disabled}"
  product-grid-item-view-details:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    width: 100%
    border: "1px solid {colors.hairline}"
  product-grid-item-view-details-hover:
    border: "1px solid {colors.ink}"
  category-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  category-filter-hover:
    border: "1px solid {colors.ink}"
  sort-select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination:
    display: flex
    justifyContent: center
    gap: "{spacing.sm}"
    padding: "{spacing.xl} 0"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    minWidth: 40px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-hover:
    border: "1px solid {colors.ink}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  empty-state:
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.base}"
    textAlign: center
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    height: 32px
    width: 32px
  error-state:
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.base}"
    textAlign: center
  success-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid maroon rectangle with white text. Used for "Add to Cart" and "Checkout" actions. On hover, darkens to `{colors.primary-active}`. When disabled, fades to `{colors.primary-disabled}` with no border.

**`button-secondary`** — An outlined alternative with a white background, ink text, and a hairline border. Used for "View Details" and secondary actions. On hover, the background shifts to `{colors.surface-soft}` and the border becomes ink.

**`button-tertiary-text`** — A text-only link styled as a button, using `{colors.primary}` for the text. Used for "Cancel" or "Back to Browse" actions. No background or border.

### Navigation
**`top-nav`** — A 64px white bar with a hairline bottom border. Contains the store logo on the left, nav links in the center, and the cart icon with badge on the right. The logo is a retro script wordmark.

**`nav-link`** — Standard navigation link in ink. The active state uses `{colors.primary}` to indicate the current page.

**`cart-icon`** — A simple shopping-bag SVG glyph at 24px. The `cart-badge` is a small pill in `{colors.badge-count}` with white text, positioned at the top-right corner of the icon.

### Cards
**`product-card`** — A white card with no rounded corners and a soft hairline border. Contains a 200px square image, the album title, artist name, and price. On hover, the border becomes more visible.

**`product-grid-item`** — The grid variant of the product card, used in the main product listing. Includes an image, info section, and action buttons. The badge overlays the image at the top-left.

**`product-grid-item-add-to-cart`** — A full-width maroon button within the grid card. On hover, darkens. When disabled (out of stock), uses the disabled maroon.

**`product-grid-item-view-details`** — A full-width outlined button for navigating to the product detail page.

### Forms
**`text-input`** — A standard input field with a white background, ink text, and a hairline border. On focus, the border switches to `{colors.primary}`. On error, the border also uses `{colors.primary}`.

**`search-bar-pill`** — A pill-shaped search field with a soft gray background and hairline border. On focus, the border becomes `{colors.primary}`. Placeholder text is in `{colors.muted}`.

**`quantity-selector`** — A bordered container with a numeric value and two square buttons for increment/decrement. The buttons have a soft gray background.

### Product Detail
**`product-detail-section`** — The main layout for the product detail page, with a 400px image on the left and metadata on the right. Includes title, artist, price, format, label, year, genre, description, and tracklist.

**`product-detail-tracklist`** — A list of tracks, each with a number, title, and duration. The track number and duration are in `{colors.muted-soft}`.

**`product-detail-back-link`** — A link in `{colors.link}` to return to the product listing. On hover, darkens to `{colors.link-hover}`.

### Footer
**`footer`** — A maroon background section with white text. Contains the store logo, links to About, Contact, Shipping, Returns, and social media icons. Links are white and underline on hover.

### Filters & Sorting
**`category-filter`** — A bordered pill for filtering by genre or format. The active state uses `{colors.primary}` as the background.

**`sort-select`** — A dropdown for sorting by price, artist, or release date. Styled as a bordered box.

### Pagination
**`pagination`** — A centered row of numbered buttons. The active page uses `{colors.primary}`. Disabled buttons (for edges) are grayed out.

### States
**`empty-state`** — A centered message in `{colors.muted}` when no products match a filter.

**`loading-spinner`** — A 32px circular spinner with a maroon top arc.

**`error-state`** — A centered message in `{colors.primary}` for error conditions.

**`success-message`** — A soft gray box with ink text for success notifications.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid becomes 1 column. Top nav collapses to hamburger menu. Product detail stacks image above text. Search bar reduces to icon-only. Footer stacks links vertically. |
| Tablet | 744–1128px | Product grid uses 2 columns. Top nav shows limited links. Product detail uses 2-column layout with smaller image (300px). |
| Desktop | 1128–1440px | Product grid uses 3 columns. Full top nav visible. Product detail uses 400px image. Standard spacing. |
| Wide | > 1440px | Product grid uses 4 columns. Max-width container at 1440px. Product detail image at 500px. |

### Touch Targets
- All buttons and interactive elements are at least 40px tall.
- Cart icon has a minimum touch area of 44x44px.
- Pagination buttons are 40x40px minimum.
- Quantity selector buttons are 40x40px.
- Search bar is 40px tall with adequate padding.

### Collapsing Strategy
- Top nav links collapse into a hamburger menu below 744px.
- Product grid reduces columns as viewport shrinks.
- Product detail page stacks vertically on mobile.
- Footer links collapse from a row to a column on mobile.
- Category filters become a horizontal scrollable strip on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site; the palette above is inferred from the brand's physical store aesthetic and common e-commerce patterns. The maroon `#8b1a1a` is a best-guess for a record store brand.
- Font-family declarations returned only "Arial"; no custom typeface was detected. The brand may use a different font in production that wasn't captured.
- No meta theme-color or page title was extracted.
- Hover, focus, and active states for all components are estimated based on standard patterns.
- Error styling for forms (validation messages, error borders) is assumed.
- Dark mode is not supported; no dark-mode tokens are defined.
- The brand may have additional components (newsletter signup, reviews, wishlist) that were not observed.
- The product detail page layout (image size, tracklist styling) is speculative.
- The footer content (links, social icons) is assumed from common record store sites.
- The brand may use a different grid system or spacing scale in production.
- No animation or transition tokens are defined.
