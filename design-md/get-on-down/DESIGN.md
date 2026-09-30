---
version: alpha
name: "Get On Down"
source_url: "https://www.getondown.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-red record crate dropped into the browser — #231f20 ink wraps the entire viewport edge-to-edge, while #ff1716 acts as the storefront's sole voltage, a stop-sign red that fires on "Add to Cart," sale badges, and the site's own logo mark. The brand treats its product grid like a wall of album covers: each vinyl, cassette, and box set sits on a #fafafa canvas card with soft shadows, the cover art doing all the emotional work while the type stays out of the way. Jost runs the interface at modest weights (400–600), never competing with the sleeve photography. The top nav is a thin black strip with white links and a search icon that opens a full-screen overlay — the red reappears only on the cart icon dot and the checkout button. Badges for "Limited Edition," "Pre-Order," and "Exclusive" use #ff1716 backgrounds with white type, cut at {rounded.sm} corners, while genre tags (Rock, Hip-Hop, Jazz) are rendered as #e7e7e7 pills with #4a4a4a text. The footer collapses into a dense black column of links, social icons (each in its own brand color — #3b5998 Facebook, #1da1f2 Twitter, #bd081c Pinterest), and a newsletter signup with a red submit button. Every interaction feels like flipping through bins at a record store: the product card hover lifts the image 2px, the add-to-cart button pulses red, and the cart drawer slides in from the right with a #231f20 backdrop. The brand's voice is direct, collector-focused, and unapologetically physical — this is a store that sells objects, not streams.

colors:
  primary: "#ff1716"
  primary-active: "#c90100"
  primary-disabled: "#dedede"
  ink: "#231f20"
  body: "#4a4a4a"
  muted: "#696969"
  muted-soft: "#8a9297"
  hairline: "#b4b4b4"
  hairline-soft: "#dadada"
  canvas: "#fafafa"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  badge-red: "#ff1716"
  badge-green: "#00aa00"
  badge-sold-out: "#c11e23"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#bd081c"
  social-instagram: "#d83776"
  social-youtube: "#fd355a"
  social-soundcloud: "#ff5500"
  social-tumblr: "#35465c"
  social-spotify: "#1ab7ea"
  star-rating: "#f5dc30"
  newsletter-bg: "#212121"
  footer-bg: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.primary}"

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
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 15px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 32px 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-link:
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    padding: 16px 12px
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-bar-icon:
    textColor: "{colors.on-ink}"
    height: 24px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  search-input-overlay:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.full}"
    padding: 16px 24px
    height: 56px
    border: "none"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  product-card-badge-preorder:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  genre-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  genre-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-ink}"
    textTransform: uppercase
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.on-ink}"
  newsletter-input:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm} 0 0 {rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.muted}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "0 {rounded.sm} {rounded.sm} 0"
    padding: 10px 16px
    height: 44px
  social-icon:
    height: 20px
    width: 20px
  cart-icon-dot:
    backgroundColor: "{colors.primary}"
    height: 8px
    width: 8px
    rounded: "{rounded.full}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: 360px
  cart-drawer-header:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base}"
  cart-item-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  cart-item-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  cart-item-quantity:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 32px
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    color: "{colors.ink}"
    fontWeight: 600
  loading-spinner:
    color: "{colors.primary}"
    height: 24px
    width: 24px
  star-rating:
    color: "{colors.star-rating}"
    height: 16px
  review-count:
    typography: "{typography.caption}"
    color: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The store's primary call-to-action, a #ff1716 red rectangle with white uppercase Jost at 14px/600. Used for "Add to Cart," "Checkout," and "Subscribe." On hover, the background shifts to `{colors.primary-active}` (#c90100) with no scale or shadow change — the color darkens just enough to signal pressability. Disabled state uses `{colors.primary-disabled}` (#dedede) with `{colors.muted}` text, appearing on sold-out items or during processing.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping." White background with `{colors.ink}` text and a `{colors.hairline}` border. Active state swaps the border to `{colors.ink}` and the background to `{colors.surface-soft}`. Used in product cards and cart drawers.

**`button-tertiary-text`** — A text-only button for inline actions like "Clear Filters" or "Remove." No background, `{colors.ink}` text. On hover, the text turns `{colors.primary}` — a subtle red underline would also be appropriate but wasn't confirmed from extraction.

**`button-pill-red`** — A fully rounded pill for compact contexts like sale banners, promo bars, or mobile sticky CTAs. Uses `{typography.button-sm}` (12px uppercase) with 8px vertical padding. The pill shape (`{rounded.full}`) makes it feel more promotional and urgent than the standard rectangle.

**`button-pill-outline`** — The inverse pill for filter tags or "Clear All" actions. Transparent background with a `{colors.hairline}` border. Used alongside genre tags in the collection sidebar.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.md}` corners and no border — the card relies on the `{colors.canvas}` page background for separation. The image fills the top with `{rounded.md} {rounded.md} 0 0` corner clipping, and the info section below uses `{spacing.md}` horizontal padding. On hover, the entire card lifts 2px with a subtle box-shadow (not captured in extraction but standard for the pattern). The title uses `{typography.title-sm}` (14px/600), the artist uses `{typography.body-sm}` (14px/400) in `{colors.muted}`, and the price uses `{typography.price}` (16px/600). Sale prices render in `{colors.primary}`.

**`product-card-badge`** — A small uppercase label pinned to the top-left of the product image. Three variants: red for "Limited Edition" or "Exclusive," green for "Pre-Order" or "Back in Stock," and dark red for "Sold Out." Each uses `{typography.badge}` (11px/600 uppercase) with 2px vertical and 8px horizontal padding, cut at `{rounded.sm}`.

### Navigation
**`nav-bar`** — A fixed 56px black strip (`{colors.ink}`) spanning the full viewport width. Contains the logo (left-aligned, red), navigation links (center, white uppercase), and icon group (right: search, account, cart). Links use `{typography.nav-link}` (14px/500 uppercase) with 16px vertical and 12px horizontal padding. The active link or current section uses `{colors.primary}` text. The cart icon includes a small red dot (`{colors.primary}`, 8px circle) as a count indicator.

**`search-overlay`** — A full-screen overlay triggered by the search icon. The background is `{colors.canvas}` with a centered search input styled as a large pill (`{rounded.full}`, 56px height) using `{colors.surface-soft}` background and `{typography.display-md}` font size. Below the input, a grid of popular genres or recent searches appears as `{genre-tag}` pills.

### Forms
**`text-input`** — Standard form input for checkout fields, newsletter, and account forms. White background with `{colors.hairline}` border, `{rounded.sm}` corners, 44px height. Focus state swaps the border to `{colors.ink}`. Error state uses `{colors.primary}` border — the red is reserved for validation failures.

**`select-dropdown`** — A styled select element for sorting (Price, Artist, Release Date) and filtering (Format, Genre). Same dimensions as `text-input` but with 32px right padding for the dropdown arrow. The arrow icon is `{colors.ink}`.

**`newsletter-input`** — A split-field input for the footer newsletter signup. The text input uses `{colors.ink}` background with `{colors.on-ink}` text and a `{colors.muted}` border, left corners rounded. The submit button uses `{colors.primary}` background with `{colors.on-primary}` text, right corners rounded. Together they form a single 44px bar.

### Footer
**`footer-section`** — A dense black column (`{colors.footer-bg}` #121212) with white headings and gray links. Headings use `{typography.title-sm}` (14px/600 uppercase). Links use `{typography.link}` (14px/400) in `{colors.muted-soft}` (#8a9297) and lighten to white on hover. Social icons appear in their respective brand colors (Facebook blue, Twitter blue, Pinterest red, etc.) at 20px each. The newsletter signup sits at the top of the footer, followed by link columns (Customer Service, About, Genres, Connect), then a copyright line.

### Cart
**`cart-drawer`** — A 360px slide-in panel from the right edge. The header is a `{colors.ink}` strip with white "Your Cart" text and a close icon. Each cart item shows the album thumbnail, title (14px/600), artist (14px/400 muted), price (16px/600), and a quantity selector (32px height, `{colors.surface-soft}` background). The checkout button at the bottom is `{button-primary}` full-width. Below it, payment icons for Shopify Pay, PayPal, and credit cards appear in grayscale.

### Badges & Tags
**`genre-tag`** — A pill-shaped filter tag for collection pages. Light gray background (`{colors.surface-soft}` #f3f3f3) with `{colors.body}` (#4a4a4a) text. Active state inverts to `{colors.ink}` background with white text. Used in a horizontal scrollable strip above the product grid.

**`star-rating`** — A 16px gold star (`{colors.star-rating}` #f5dc30) for product reviews. The count appears next to it in `{typography.caption}` (12px) in `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu + logo + cart icon. Product grid goes single-column. Genre tag strip becomes horizontally scrollable. Cart drawer becomes full-width overlay. Footer columns stack vertically. Search overlay uses full viewport height. |
| Tablet | 744–1128px | Nav bar shows all links (may truncate to "Shop" + dropdown). Product grid uses 2–3 columns. Genre tags wrap to 2 rows. Footer uses 2-column layout. Cart drawer remains 360px. |
| Desktop | 1128–1440px | Full nav bar with all links visible. Product grid uses 3–4 columns. Genre tags display in a single row. Footer uses 4-column layout. Cart drawer is 360px. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product grid uses 4–5 columns. All elements scale proportionally but maintain max-width constraints. |

### Touch Targets
- All buttons and links: minimum 44px height (buttons) or 44x44px (icon-only targets)
- Genre tags: minimum 32px height with 12px horizontal padding
- Quantity selector buttons: 32x32px minimum
- Cart drawer close icon: 44x44px tap area
- Search overlay close: 44x44px tap area
- Social icons: 44x44px tap area (icon is 20px with 12px padding)

### Collapsing Strategy
- Nav bar links collapse into hamburger menu below 744px
- Product grid reduces columns: 4→3→2→1 as viewport shrinks
- Genre tag strip becomes horizontally scrollable below 744px (no wrapping)
- Footer columns collapse from 4→2→1
- Cart drawer becomes full-width overlay on mobile (360px→100vw)
- Search overlay remains full-screen on all breakpoints
- Breadcrumb trail truncates to "Home > ... > Current Page" on mobile
- Pagination collapses to "Prev/Next" buttons on mobile (hides page numbers)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow/elevation values not extracted — assumed 2px lift with subtle shadow)
- Active/visited states for navigation links (only active state confirmed via red text)
- Error styling for form validation beyond red border (no error message typography or icon extracted)
- Focus ring styles (no `:focus-visible` or `outline` values extracted)
- Loading states for product grids, cart, and checkout (spinner color extracted but no size or animation data)
- Empty states (empty cart, no search results, no products in category)
- Success states (added to cart confirmation, order confirmation)
- Dark mode (no extracted values — site appears light-mode only)
- Sub-brand or collection-specific palettes (e.g., exclusive color vinyl editions might use different accent colors)
- Checkout flow styling (Shopify checkout may override brand styles — extracted colors include Shopify Pay blue/green)
- Mobile sticky header behavior (nav bar may become sticky on scroll — not confirmed)
- Product quick-add / variant selector (size/format dropdown styling not extracted)
- Image zoom/lightbox behavior on product pages
- Sale/compare-at price strikethrough styling (assumed standard `text-decoration: line-through` in `{colors.muted}`)
- Newsletter success/error messaging styling
- Cookie consent banner styling
- Accessibility: skip-to-content link, ARIA labels, focus order not extracted
- Font weights beyond 400/500/600 (700 may exist for headings but not confirmed in extraction)
- Line-height values for all typography tokens (assumed from standard Jost metrics — actual values may vary)
