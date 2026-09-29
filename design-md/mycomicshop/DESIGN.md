---
version: alpha
name: "MyComicShop"
source_url: "https://www.mycomicshop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dense, inventory-first marketplace built for collectors who know exactly what they want — a tabular grid of back-issue listings, variant covers, and graded slabs that prioritizes information density over editorial whitespace. The palette is utilitarian: a cool off-white canvas (#f5f5f5) that reads like newsprint under fluorescent light, with primary action surfaces in a flat, uninflected blue (#0066c0) that carries the brand’s search, add-to-cart, and checkout buttons. There is no hero imagery, no lifestyle photography — the product is the page, and every square pixel is loaded with a cover thumbnail, price, condition grade, and stock status badge. Typography runs system-native (Arial, Helvetica, sans-serif) at modest sizes — body copy at 13px, captions at 11px — because the interface must fit 20+ line items above the fold on a 1366px screen. Corners are almost entirely square (`{rounded.none}`), with only the rare badge or filter pill taking a 4px radius (`{rounded.xs}`). The search bar is the single most prominent interactive element: a full-width text input with a magnifying-glass icon, sitting below a horizontal category strip (New Arrivals, Back Issues, Variants, etc.) that collapses into a hamburger on mobile. Status badges — "In Stock," "Low Stock," "Sold Out" — use a three-color system: green (#008000) for available, orange (#ff8c00) for warning, red (#d9534f) for sold. The overall feeling is that of a well-organized warehouse catalog rendered in HTML: no friction, no flourish, just the fastest path from query to checkout.

colors:
  primary: "#0066c0"
  primary-active: "#004b8d"
  primary-disabled: "#99badd"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#f5f5f5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  stock-green: "#008000"
  stock-orange: "#ff8c00"
  stock-red: "#d9534f"
  badge-new: "#0066c0"
  badge-sale: "#cc0000"
  link-blue: "#0066c0"
  link-visited: "#551a8b"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
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
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 7px 15px
    height: 36px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 4px 0
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    height: 28px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 6px 10px
    height: 32px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
  product-card-thumbnail:
    width: 100px
    height: 150px
    rounded: "{rounded.none}"
  stock-badge:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  stock-badge-low:
    backgroundColor: "{colors.stock-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  stock-badge-sold:
    backgroundColor: "{colors.stock-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-lg}"
  price-display-sm:
    textColor: "{colors.ink}"
    typography: "{typography.price-sm}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    height: 28px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    height: 28px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: 24px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
  pagination:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    height: 32px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    height: 32px
  dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 6px 10px
    height: 32px
  checkbox:
    rounded: "{rounded.none}"
    size: 16px
  radio:
    rounded: "{rounded.full}"
    size: 16px
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    padding: 6px 8px
  table-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 6px 8px
  table-row-striped:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 6px 8px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 12px 8px
  cart-total:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 12px 16px
  checkout-button:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  quantity-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 4px 6px
    width: 60px
    height: 32px
  wishlist-icon:
    textColor: "{colors.muted}"
    size: 20px
  wishlist-icon-active:
    textColor: "{colors.stock-red}"
    size: 20px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 40px
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  mobile-hamburger:
    textColor: "{colors.ink}"
    size: 24px
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    size: 24px
  error-message:
    backgroundColor: "{colors.stock-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
  success-message:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Flat blue rectangle with white bold text, used for "Add to Cart," "Checkout," and "Search." No border radius, no shadow. On hover, darkens to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with no pointer events.

**`button-secondary`** — Outlined alternative for "Cancel," "Clear Filters," and "View Details." White background with a 1px `{colors.hairline}` border and `{colors.ink}` text. Hover adds a subtle `{colors.hairline-soft}` background.

**`button-tertiary-text`** — Link-styled text button for "See All," "More Info," and "Remove." No background, blue link color (`{colors.link-blue}`), underlined on hover. Used in dense table layouts where a full button would consume too much space.

**`button-small`** — Compact variant for inline actions like "Add to Wishlist" or "Quick View." Same flat blue treatment as primary but at 28px height with 8px horizontal padding.

### Cards
**`product-card`** — The fundamental listing unit. A white rectangle (`{colors.surface-card}`) containing a 100x150px thumbnail, title, condition grade, price, and stock badge. No border radius, no shadow — relies on the `{colors.hairline}` grid for separation. On hover, the background shifts to `{colors.surface-soft}` for a subtle lift.

**`product-card-thumbnail`** — Fixed-ratio cover image container. Square corners, no border. The image is centered and cropped to fill the 100x150px frame.

### Navigation
**`nav-bar`** — Top-level navigation strip at 48px height. Contains the brand logo (left), category links (center), and account/cart icons (right). Background is `{colors.canvas}` with a 1px `{colors.hairline}` bottom border. Active category link gets a 2px `{colors.primary}` underline.

**`category-strip`** — Secondary horizontal strip below the nav bar, listing comic categories (New Arrivals, Back Issues, Variants, etc.) as text links. 40px height, scrollable horizontally on mobile. Active tab gets the same blue underline treatment.

**`breadcrumb`** — Lightweight path indicator in the page header. Gray `{colors.muted}` text for parent levels, bold `{colors.ink}` for the current page. No separators beyond a simple ">" character.

### Forms
**`text-input`** — Standard single-line input for search, login, and checkout forms. White background, 1px `{colors.hairline}` border, 32px height. Focus state adds a 2px `{colors.primary}` border. No border radius.

**`search-bar`** — The primary search input, wider than standard text inputs at 40px height. Placed below the nav bar on desktop, full-width on mobile. Includes a magnifying-glass icon inside the input on the left side.

**`dropdown`** — Select-style dropdown for sorting (Price Low-High, Issue Date, etc.) and filtering (Condition, Publisher). Same styling as text-input with a down-arrow icon.

**`checkbox`** / **`radio`** — Square checkbox (16px) and circular radio (16px). Unchecked: 1px `{colors.hairline}` border on white. Checked: `{colors.primary}` fill with white checkmark/dot.

### Badges
**`stock-badge`** — Inline status indicator, 4px radius. Three variants: green (`{colors.stock-green}`) for "In Stock," orange (`{colors.stock-orange}`) for "Low Stock," red (`{colors.stock-red}`) for "Sold Out." Bold 11px white text on a colored background.

**`badge-new`** / **`badge-sale`** — Promotional badges overlaid on product thumbnails. Blue for "New This Week," red for "Sale." Same styling as stock badges but positioned absolutely at the top-left of the thumbnail.

### Tables
**`table-header`** — Column header row in listing tables. Light gray background (`{colors.surface-soft}`), bold 11px uppercase text, 6px vertical padding. Used in back-issue grids and order history.

**`table-row`** / **`table-row-striped`** — Alternating row colors for readability. Even rows use `{colors.surface-card}`, odd rows use `{colors.canvas}`. 13px body text, 6px vertical padding.

### Cart & Checkout
**`cart-item`** — Line item in the shopping cart. White background, 12px vertical padding, contains thumbnail, title, variant info, quantity input, price, and remove button. Separated by `{colors.hairline}` borders.

**`cart-total`** — Summary section at the bottom of the cart. Light gray background, bold 14px text for subtotal, shipping, and total. The "Proceed to Checkout" button uses `{colors.stock-green}` to signal a positive action.

**`quantity-input`** — Narrow text input (60px wide) for adjusting item quantities. Same styling as text-input but with +/- buttons on either side.

### Pagination
**`pagination`** — Page number links at the bottom of listing pages. White background, 32px height, 8px horizontal padding. Active page gets `{colors.primary}` background with white text. Previous/Next arrows are text links.

### Feedback
**`loading-spinner`** — 24px circular spinner with a `{colors.primary}` top border and `{colors.hairline}` rest. Used during search and checkout processing.

**`error-message`** / **`success-message`** — Full-width notification bars. Red background for errors (e.g., "Item out of stock"), green for success (e.g., "Added to cart"). 8px padding, white text, no border radius.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; category strip becomes horizontally scrollable; nav bar collapses to hamburger menu; product cards stack vertically; search bar goes full-width; table views switch to stacked card layout; pagination reduces to "Prev/Next" only |
| Tablet | 744–1128px | Two-column product grid; nav bar shows abbreviated category links; sidebar filters collapse into a top "Filter" button; search bar remains full-width but gains a filter dropdown |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all categories; persistent sidebar filters; search bar is centered with category strip below; table views show 5+ columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; additional whitespace on sides; sidebar filters expand to show more options; table views show 8+ columns |

### Touch Targets
- All buttons and links: minimum 44x44px tap target (enforced via padding on small buttons)
- Search bar: 40px height (below 44px but acceptable for text input)
- Filter pills: 28px height with 8px horizontal padding (effective tap area ~44px)
- Category tabs: 40px height with 16px horizontal padding
- Hamburger icon: 44x44px tap area
- Quantity +/- buttons: 32x32px tap area

### Collapsing Strategy
- Nav bar links collapse into a hamburger menu on mobile (below 744px)
- Sidebar filters collapse into a top "Filter" button on tablet and mobile
- Product grid reduces from 4 columns to 1 column on mobile
- Table views (back-issue listings, order history) collapse to stacked card layout on mobile
- Category strip becomes horizontally scrollable on mobile (no wrapping)
- Footer links collapse into accordion sections on mobile
- Search bar remains full-width at all breakpoints but loses the filter dropdown on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors or font families were available from the live site — the palette and typography above are inferred from the brand's category (comic book e-commerce) and common patterns in the space. The primary blue (#0066c0) is a reasonable guess for a comic shop's CTA color but may differ from the actual site.
- Hover and focus states for all components are estimated — actual site may use different transitions, shadows, or color shifts.
- Error and success message styling is speculative — the site may use inline form validation or modal dialogs instead.
- No data on dark mode, high-contrast mode, or reduced-motion preferences.
- Stock badge colors (green/orange/red) are common conventions but may differ in hue or saturation on the live site.
- Font stack (Arial, Helvetica, sans-serif) is a safe system-font fallback — the actual site may use a custom web font (e.g., Roboto, Open Sans) that wasn't detected.
- No information on iconography style (line vs. filled, custom vs. icon library).
- Checkout flow may use a third-party provider (Shopify, WooCommerce) with its own styling that overrides the brand's design system.
- No data on mobile app or tablet-specific navigation patterns (e.g., bottom tab bars, swipe gestures).
- Loading states (skeleton screens, shimmer animations) are not documented — the site may use simple text placeholders or spinner overlays.
- Print styles and accessibility (ARIA labels, focus outlines, skip links) are not captured.
