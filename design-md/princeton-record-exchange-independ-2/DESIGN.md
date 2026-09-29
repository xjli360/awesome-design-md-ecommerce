---
version: alpha
name: "Princeton Record Exchange"
source_url: "https://www.prex.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated #1f1f1f ink anchors Princeton Record Exchange, a used-and-new vinyl institution that treats its website like a crate-digging session — dense, rewarding, and punctuated by flashes of signal. The primary voltage is #ffdd00, a marigold yellow that appears on the site's header banner, sale tags, and call-to-action buttons, cutting through the dark canvas with the same urgency as a "New Arrivals" sticker on a store shelf. A secondary accent of #f58220 (burnt orange) and #d94a00 (rust red) handle secondary actions and price highlights, while #ee2200 serves as a pure alert red for sold-out badges and limited-stock warnings. The typography stack defaults to system fonts — `-apple-system`, `Arial`, `Helvetica Neue`, `Segoe UI` — a pragmatic choice that prioritizes load speed and readability over brand typography, reflecting the store's no-frills, music-first ethos. Cards and buttons use `{rounded.sm}` (8px) corners, a subtle softening that keeps the interface approachable without undermining the utilitarian grid. The layout is columnar and text-heavy, with a two-tier navigation bar that stacks categories (Vinyl, CDs, Turntables) above utility links (Cart, Account), all set against a `{colors.canvas}` of #fefefe. Product listings favor density over whitespace: thumbnails sit at 150px square, prices are bolded in `{colors.ink}`, and condition notes (Mint, VG+, etc.) appear in `{colors.muted}` #777777. The footer is a wall of links — shipping policies, genre guides, store hours — all in `{colors.body}` #555555, a quiet acknowledgment that this is a real shop with real inventory, not a lifestyle brand. The overall feel is of a well-organized record bin: everything has its place, nothing is precious, and the yellow tags make sure you don't miss the good stuff.

colors:
  primary: "#ffdd00"
  primary-active: "#e6c700"
  primary-disabled: "#fff4b3"
  ink: "#1f1f1f"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#e4e4e4"
  hairline-soft: "#eeeeee"
  canvas: "#fefefe"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#1f1f1f"
  accent-orange: "#f58220"
  accent-rust: "#d94a00"
  alert-red: "#ee2200"
  link-blue: "#0089ec"
  link-visited: "#0059bc"
  sold-out: "#ee2200"
  condition-mint: "#1f1f1f"
  condition-vg: "#555555"
  condition-g: "#777777"
  badge-new: "#ffdd00"
  badge-sale: "#f58220"
  star-rating: "#ffdd00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-rust:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
    padding: 0
  button-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "2px solid {colors.alert-red}"
    backgroundColor: "{colors.canvas}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-sub:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    height: 150px
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-condition:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
  product-card-badge-sold:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xl} {spacing.base}"
    minHeight: 200px
  hero-banner-accent:
    color: "{colors.primary}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-link:
    color: "{colors.body}"
    padding: "{spacing.sm} {spacing.md}"
  category-link-active:
    color: "{colors.ink}"
    fontWeight: 700
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  alert-banner:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (#ffdd00) with `{colors.on-primary}` (#1f1f1f) text. Used for "Add to Cart", "Checkout", and "Search" actions. On hover/active, shifts to `{colors.primary-active}` (#e6c700). Disabled state uses `{colors.primary-disabled}` (#fff4b3) with `{colors.muted}` text. Height is 40px with `{rounded.sm}` corners.

**`button-secondary`** — An outlined variant with a white background and `{colors.ink}` text, bordered by `{colors.hairline}` (#e4e4e4). Used for "Cancel", "Clear Filters", and secondary form actions. Active state fills with `{colors.surface-soft}` (#f5f5f5) and a `{colors.muted}` border.

**`button-accent-orange`** and **`button-accent-rust`** — Used for sale-related CTAs and promotional badges. Orange (#f58220) signals a discount or clearance item; rust (#d94a00) marks limited-time offers or high-demand restocks. Both use white text and `{rounded.sm}`.

**`button-link`** — A text-only link styled as a button, using `{colors.link-blue}` (#0089ec). Used for "View Details", "Read More", and "Track Order" links within product cards and order history.

**`button-cart`** — A compact version (36px height) used in the mini-cart dropdown and quick-add panels. Shares the primary yellow but uses `{typography.button-sm}` for tighter spacing.

### Cards
**`product-card`** — The core inventory unit. A white card (`{colors.canvas}`) with `{rounded.sm}` and 8px padding. Contains a 150px-square thumbnail with `{rounded.xs}`, a title in `{typography.title-sm}` (#1f1f1f), a price in `{typography.price-sm}` (#1f1f1f), and a condition label in `{typography.caption-sm}` (#777777). Badges overlay the top-left corner of the image: yellow for "New Arrival", orange for "Sale", red for "Sold Out". Cards stack in a responsive grid (2 columns on mobile, 3-4 on desktop) with 16px gaps.

**`product-card-badge`** — Small uppercase labels (11px, 700 weight) with 2px/6px padding and `{rounded.xs}`. Three variants: `badge-new` (yellow), `badge-sale` (orange with white text), `badge-sold` (red with white text). Positioned absolutely over the card image.

### Navigation
**`nav-bar`** — The primary top bar, a 48px strip of `{colors.ink}` (#1f1f1f) with white text. Contains the store logo (left), main category links (center: Vinyl, CDs, Turntables, Accessories, Sale), and utility icons (right: Search, Cart, Account). Active link underlined with 2px `{colors.primary}`. Hover state highlights in yellow.

**`nav-bar-sub`** — A secondary white bar below the primary nav, 40px tall with a `{colors.hairline}` bottom border. Contains subcategories (e.g., under Vinyl: New Arrivals, Used, Rare, Box Sets) and a breadcrumb trail. Links are `{colors.ink}` with `{colors.primary}` hover.

**`category-strip`** — A horizontal scrollable strip of genre/category links (Rock, Jazz, Classical, etc.) used on the homepage and browse pages. Links are `{colors.body}` (#555555) with 12px horizontal padding. Active category is bolded in `{colors.ink}`.

### Forms
**`text-input`** — Standard input field with white background, `{colors.hairline}` border, and `{rounded.sm}`. 40px height with 8px/12px padding. Focus state gains a 2px `{colors.primary}` border. Error state uses 2px `{colors.alert-red}` (#ee2200). Used for email signup, address forms, and checkout fields.

**`search-input`** — A pill-shaped search bar (`{rounded.full}`) with `{colors.surface-soft}` (#f5f5f5) background and `{colors.hairline}` border. 40px height. Focus state switches to white background with 2px `{colors.primary}` border. Used in the header and on the search results page.

**`quantity-selector`** — A compact 36px-high control with a white background, `{colors.hairline}` border, and `{rounded.sm}`. Contains a decrement button, a numeric display, and an increment button. Buttons use `{colors.surface-soft}` background.

### Footer
**`footer`** — A full-width dark band (`{colors.ink}`) with `{colors.muted-soft}` (#aaaaaa) text. Organized into columns: About, Customer Service, Genres, Connect. Links are `{colors.muted-soft}` with white hover. Includes store address, hours, and social icons. Padding is 48px top/bottom, 16px sides.

### Misc
**`hero-banner`** — A dark background (`{colors.ink}`) with white text and a yellow accent (`{colors.primary}`) for the headline. Minimum height 200px, padding 32px/16px. Used on the homepage for featured collections and seasonal promotions. The yellow accent is applied to key phrases (e.g., "New Arrivals", "Sale").

**`breadcrumb`** — A thin trail of `{colors.muted}` (#777777) links separated by `{colors.hairline}` slashes. Active page is `{colors.ink}`. Used on product detail and category pages.

**`pagination`** — Page number links in `{colors.body}` (#555555). Active page gets a yellow (`{colors.primary}`) background with `{colors.on-primary}` text and `{rounded.sm}`. Hover state uses `{colors.surface-soft}` background.

**`filter-chip`** — Pill-shaped chips (`{rounded.full}`) with `{colors.surface-soft}` background, `{colors.hairline}` border, and `{colors.ink}` text. Active chip fills with `{colors.primary}` and `{colors.on-primary}` text. Used in the sidebar filter panel for genre, condition, and price range.

**`alert-banner`** — A red (`{colors.alert-red}`) banner with white text, used for urgent messages: "Limited Stock", "Shipping Delays", "Store Closure". Padding 8px/16px, `{rounded.sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns for vinyl thumbnails). Nav collapses to hamburger menu. Category strip becomes horizontally scrollable. Footer stacks into single column. Search bar moves to top of page. |
| Tablet | 744–1128px | Two-column product grid. Nav shows all top-level categories. Category strip remains scrollable. Footer shows 2-column layout. Sidebar filters collapse into a top "Filter" button. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with subcategories. Sidebar filters visible. Footer shows 4-column layout. Breadcrumb trail fully visible. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centered. Sidebar filters remain fixed. Footer shows 4-column layout with additional legal links. |

### Touch Targets
- All buttons and links: minimum 44px height (40px buttons with 4px padding to meet accessibility)
- Filter chips: 32px height (acceptable for secondary touch targets)
- Quantity selector buttons: 36px height
- Search bar: 40px height
- Nav links: 48px height (full nav bar height)

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Sub-navigation hides entirely on mobile; breadcrumb trail remains
- Sidebar filter panel collapses to a "Filter" button that opens a modal/drawer on mobile and tablet
- Product grid reduces from 4 columns to 2 columns on tablet, 1 column on mobile (vinyl thumbnails remain 2 columns)
- Footer collapses from 4 columns to 2 columns on tablet, 1 column on mobile
- Hero banner reduces padding and font size on mobile (28px to 22px display)
- Search bar moves from nav bar to a prominent position below the hero on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary/secondary button hover states were reliably extracted. Hover states for links, filter chips, and pagination are inferred from common patterns.
- **Error styling**: Text input error state (red border) is assumed from `{colors.alert-red}` presence; no specific error message styling was found.
- **Dark mode**: No dark mode implementation detected. The site uses a light canvas with dark ink throughout.
- **Typography scale**: Font sizes were not explicitly extracted from CSS; the scale above is reconstructed from common system font patterns and the site's visual density. Actual sizes may vary by 1-2px.
- **Font weights**: The extracted font-family list did not include specific weights. Weights are inferred from common system font usage (400 for body, 600-700 for headings/buttons).
- **Spacing scale**: Spacing values are reconstructed from visual inspection of the site's density. Actual padding/margin values may differ.
- **Component states**: Disabled states for inputs, selectors, and chips are not documented. Sold-out badge styling is assumed from `{colors.alert-red}`.
- **Animation/transition**: No transition durations or easing functions were extracted. The site appears to use minimal animation (simple hover color changes).
- **Sub-brand palettes**: The site may use distinct palettes for different genres or eras (e.g., jazz vs. rock), but these were not extracted.
- **Checkout flow**: Checkout-specific components (payment forms, shipping selectors) were not analyzed. The site may use a third-party checkout (Shopify, etc.) with its own design system.
- **Accessibility**: Focus ring styles, ARIA labels, and keyboard navigation patterns were not extracted. The site's high contrast (yellow on black) suggests reasonable accessibility, but this is unverified.
- **Social media icons**: Colors for social icons (Facebook blue, Twitter blue, Instagram gradient) were filtered from the extracted palette. These are not part of the brand's core design system.
