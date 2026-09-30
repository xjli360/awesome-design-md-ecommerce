---
version: alpha
name: "Hamilton Book"
source_url: "https://www.hamiltonbook.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A discount retailer of books, DVDs, and CDs that wears its frugality like a badge of honor, anchored on a warm beige canvas (#f7f4ee) and a deep forest-green primary (#0f6730) that reads more like a used-bookstore sign than a tech brand. The palette is deliberately unpolished — muted olive (#a8a18a), brick red (#963231), and a single marigold accent (#fdce5c) for price tags and sale badges — creating a visual language that feels like a clearance table rather than a curated boutique. Navigation is utilitarian: a dense top bar with category dropdowns, a prominent search field with a green submit button, and product cards that stack three across with minimal whitespace. The typography stack defaults to system fonts (Arial, Helvetica, Georgia) with no custom typeface investment, reinforcing the no-frills ethos. Product cards show price in bold green (#0f6730) against the beige background, with original prices slashed in brick red (#963231) — the only two colors that carry semantic weight across the entire interface. Rounded corners are sparingly applied (`{rounded.sm}` on buttons, `{rounded.none}` on cards), keeping the feel functional rather than friendly. The overall impression is of a well-organized warehouse: everything is findable, nothing is precious.

colors:
  primary: "#0f6730"
  primary-active: "#096530"
  primary-disabled: "#55af4c"
  ink: "#1a291c"
  body: "#4a4a4a"
  muted: "#737373"
  muted-soft: "#a8a18a"
  hairline: "#d7d0c2"
  hairline-soft: "#e5e2dc"
  canvas: "#f7f4ee"
  surface-soft: "#fff3d7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-accent: "#fdce5c"
  sale-accent-active: "#ffce4c"
  price-original: "#963231"
  price-current: "#0f6730"
  badge-new: "#b94a48"
  badge-sale: "#fdce5c"
  link-default: "#003399"
  link-visited: "#443a21"
  footer-bg: "#1a291c"
  footer-text: "#d7d0c2"
  category-hover: "#fedd8e"
  search-bg: "#ffffff"
  search-border: "#d7d0c2"
  stock-badge: "#0d9446"
  out-of-stock: "#98312e"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
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
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
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
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
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
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 8px 16px
    height: 36px
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
    padding: 7px 15px
    height: 36px
    border: "1px solid {colors.primary}"
  button-sale:
    backgroundColor: "{colors.sale-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-sale-active:
    backgroundColor: "{colors.sale-accent-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.search-border}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-dropdown-item:
    padding: 6px 16px
  nav-dropdown-item-hover:
    backgroundColor: "{colors.category-hover}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.none}"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-lg}"
    color: "{colors.price-current}"
    marginTop: "{spacing.xs}"
  product-card-price-original:
    typography: "{typography.price-sm}"
    color: "{colors.price-original}"
    textDecoration: "line-through"
    marginRight: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.search-border}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
    height: 40px
  search-submit-hover:
    backgroundColor: "{colors.primary-active}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
    textDecoration: "underline"
  footer-link-hover:
    color: "{colors.sale-accent}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-item:
    padding: "{spacing.xs} {spacing.md}"
  category-item-hover:
    backgroundColor: "{colors.category-hover}"
    color: "{colors.ink}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    color: "{colors.link-default}"
    typography: "{typography.caption}"
  breadcrumb-current:
    color: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.lg} 0"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  stock-badge-instock:
    backgroundColor: "{colors.stock-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-outofstock:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 36px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 24px"
    height: 40px
  add-to-cart-button-hover:
    backgroundColor: "{colors.primary-active}"
  cart-count-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 6px"
    minWidth: "20px"
    height: "20px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Search Submit". Uses a deep forest green (#0f6730) background with white text, set in bold 14px Arial. On hover, shifts to a slightly darker green (#096530). Disabled state uses a lighter green (#55af4c) to indicate inactivity without losing brand identity.

**`button-secondary`** — Used for "View Details", "Continue Shopping", and secondary actions. Outlined variant with a white background, green text, and a 1px green border. Maintains the same 36px height and 4px border radius as the primary button for visual consistency.

**`button-sale`** — A high-visibility variant reserved for sale-related actions and promotional CTAs. Uses the marigold accent (#fdce5c) as background with dark ink text (#1a291c). Active state darkens to (#ffce4c). Typically appears on product cards with discounted pricing.

### Navigation
**`nav-bar`** — A compact 40px top navigation bar on the beige canvas (#f7f4ee), separated from content by a thin hairline (#d7d0c2). Category links use bold 13px Arial in dark ink (#1a291c). Dropdown menus appear on hover with a white background and subtle shadow, items highlighted with a warm beige hover state (#fedd8e).

**`search-bar`** — A standard text input with a green submit button, both at 40px height with 4px border radius. The input has a white background with a light beige border (#d7d0c2). The submit button uses the primary green (#0f6730) and darkens on hover. No pill shapes or rounded full variants — the design stays functional.

### Product Cards
**`product-card`** — A white card with no border radius, containing a product image, title, pricing, and optional badges. Cards stack in a grid with 12px padding and no visible border — the white against the beige canvas provides enough separation. On hover, a subtle box shadow lifts the card. Titles use bold 14px Arial, prices use bold 18px green (#0f6730), and original prices are struck through in brick red (#963231).

**`product-card-badge`** — Small rectangular badges (2px radius) that appear in the top-left corner of product images. "New" badges use brick red (#b94a48) with white text. "Sale" badges use marigold (#fdce5c) with dark ink text. Both use bold 11px Arial with 2px horizontal padding.

### Forms & Inputs
**`text-input`** — Standard form input at 36px height with 4px border radius. White background with a light beige border (#d7d0c2). On focus, the border thickens to 2px and turns green (#0f6730). Used for search, quantity selectors, and any text entry fields.

**`quantity-selector`** — A compact input for specifying item quantities, matching the 36px height of other form elements. Uses the same border and focus styles as the text input, with a beige background (#f7f4ee) to differentiate it from standard text fields.

### Footer
**`footer`** — A dark green (#1a291c) footer section with light beige text (#d7d0c2). Links are underlined and turn marigold (#fdce5c) on hover. The footer uses small body text (12px Arial) and generous padding (48px vertical, 64px horizontal) to create breathing room at the bottom of the page.

### Badges & Indicators
**`stock-badge-instock`** — A small green badge (#0d9446) with white text indicating in-stock status. Uses 2px border radius and bold 11px Arial. Appears on product detail pages and search results.

**`stock-badge-outofstock`** — A brick red badge (#98312e) with white text indicating out-of-stock status. Same dimensions as the in-stock badge but uses a darker, more urgent red.

**`cart-count-badge`** — A circular badge (full rounded) that displays the number of items in the shopping cart. Uses brick red (#b94a48) with white text, minimum 20px width and height. Positioned in the top-right corner of the cart icon in the navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar full-width; footer stacks vertically; category strip hidden; product card images reduce to 150px height |
| Tablet | 744–1128px | Two-column product grid; nav categories visible but condensed; search bar 60% width; footer two-column layout; category strip scrollable horizontally |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; search bar 40% width; footer three-column layout; category strip fully visible |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; search bar 30% width; footer four-column layout; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height on mobile for touch accessibility
- Search bar height increases to 48px on mobile
- Product card tap targets (title, price, add-to-cart) have minimum 48px touch area
- Nav hamburger icon has 48x48px touch target
- Category strip items have 44px minimum height for horizontal scrolling

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with full category list in a slide-out panel
- Category strip collapses to a horizontally scrollable row below 744px, with only top-level categories visible
- Product grid collapses from 3 columns to 2 at tablet, then 1 at mobile
- Footer collapses from 4 columns to 2 at tablet, then single column at mobile
- Search bar expands to full width on mobile, with the submit button becoming a magnifying glass icon
- Breadcrumb navigation truncates on mobile, showing only the current page and "Home"

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom effect, overlay) could not be reliably extracted
- Error state styling for forms (validation messages, error borders) not observed in extracted data
- Active/visited state colors for navigation links not confirmed from live site
- Sub-brand or seasonal color palettes (holiday, clearance events) not captured
- Dark mode or high-contrast mode variants not present on the live site
- Loading states (spinners, skeleton screens) not observed
- Focus ring styles for keyboard navigation not extracted
- Modal/dialog overlay styling (opacity, blur, close button) not confirmed
- Tooltip and popover styling not observed
- Animation durations and easing curves not extractable from static analysis
- Print stylesheet behavior not documented
- Internationalization (RTL support, language-specific font stacks) not confirmed
- The extracted color list is large (30+ hex values) and includes many muted tones — the true brand palette likely centers on the forest green (#0f6730), beige (#f7f4ee), brick red (#963231), and marigold (#fdce5c), with the remaining colors being product image dominants, checkout widget colors, or social media icon colors that should not be part of the core design system
