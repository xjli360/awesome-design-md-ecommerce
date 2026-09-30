---
version: alpha
name: "Secretly Store"
source_url: "https://www.secretlystore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record label’s storefront that treats its catalog like a library of artifacts, not a discount bin. The palette is anchored on a near-black ink (#1e1e1e) and a warm off-white canvas (#f5f5f5), with a single high-voltage accent in signal red (#ea3927) that appears only on the primary CTA, sale badges, and the cart count — never decorative. A secondary accent in marigold (#f39b1e) surfaces on pre-order badges and limited-edition flags, giving the shop a collector’s-market feel rather than a clearance-aisle one. Type runs Jost at display sizes and Karla for body text, both geometric sans-serifs with humanist warmth; the contrast between Jost’s tight letter-spacing at 26px display and Karla’s open 16px body creates a reading rhythm that feels editorial, not transactional. Product cards use a soft 8px radius ({rounded.sm}) and a 1px hairline (#dedede) that lets the album art — often vivid, textured, or photographic — carry the visual weight. The top nav is a full-width bar at 48px height, with a search icon that expands into a text field, preserving the clean grid until the user needs it. There is no hero carousel, no auto-playing video; the brand trusts its inventory photography and a single marquee row of featured releases. The footer collapses into a dense, monochrome block of links and social icons, signaling that the store is a utility, not a destination. Every interaction — hover states on buttons, underline on nav links, badge color shifts — is subtle, never animated for its own sake. The design system reads as a quiet, confident container for music discovery, where the product is the star and the interface steps back.

colors:
  primary: "#ea3927"
  primary-active: "#c92e1e"
  primary-disabled: "#f5a89e"
  ink: "#1e1e1e"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f5f5f5"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#f39b1e"
  accent-marigold-active: "#d48514"
  badge-sale: "#ea3927"
  badge-preorder: "#f39b1e"
  badge-limited: "#1e1e1e"
  badge-new: "#555555"
  star-rating: "#f39b1e"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Karla', 'Jost', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Karla', 'Jost', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Karla', 'Jost', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Karla', 'Jost', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Karla', 'Jost', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'Karla', 'Jost', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Karla', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
    padding: 10px 24px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
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
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  icon-button-circle-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.ink}"
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    height: 20px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-artist:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-social-icon:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 24px
  footer-social-icon-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 32px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 32px
    width: 32px
  quantity-selector-button-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 32px
    width: 32px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-chip-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.ink}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    backgroundColor: transparent
    textColor: "{colors.hairline}"
    typography: "{typography.caption}"
  pagination-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 32px
    minWidth: 32px
  pagination-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 32px
    minWidth: 32px
  pagination-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 32px
    minWidth: 32px
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    height: 24px
    width: 24px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  marquee-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0"
  marquee-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Subscribe". Uses the signal red (#ea3927) background with white text. On hover, shifts to a deeper red (#c92e1e). Disabled state uses a pale red (#f5a89e) to indicate inactivity without confusion with the active state.
**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Save for Later". White background with a 1px hairline border. On hover, the border becomes the full ink color, and the background shifts to surface-soft.
**`button-tertiary-text`** — A text-only button for inline actions like "Clear filters" or "Cancel". No background or border. On hover, text color shifts to the primary red, providing a subtle visual cue without adding visual weight.
**`button-pill-accent`** — A pill-shaped button reserved for promotional or limited-time actions like "Pre-order Now" or "Shop Limited Edition". Uses the marigold accent (#f39b1e) to differentiate from the primary red.

### Cards
**`product-card`** — The primary container for album, EP, and merchandise listings. A white card with a 1px hairline border and 8px rounded corners. The card contains a square aspect-ratio image at the top, followed by the title, artist name, and price. On hover, the border becomes the full ink color, signaling interactivity without a lift effect.
**`product-card-image`** — The image area of the product card, with top corners rounded to match the card and a 1:1 aspect ratio. Uses `object-fit: cover` to ensure album art fills the space without distortion.

### Badges
**`badge-sale`** — A small, uppercase badge for sale items. Uses the primary red background. Positioned at the top-left corner of product card images.
**`badge-preorder`** — A marigold badge for pre-order items, visually distinct from sale badges.
**`badge-limited`** — A black badge for limited edition releases, signaling scarcity.
**`badge-new`** — A muted gray badge for new arrivals, the most understated of the badge set.

### Navigation
**`top-nav`** — A full-width, 48px-high navigation bar with a white background and a 1px bottom hairline. Contains the store logo, navigation links in uppercase Jost, a search icon, and a cart icon with a red count badge. The nav is intentionally compact to maximize vertical space for product content.
**`nav-link`** — Navigation links in uppercase, 13px Jost with 0.5px letter-spacing. Active state shows a 2px red bottom border. Hover state shifts text to red.
**`search-bar`** — A compact search field that expands from a search icon. Uses a surface-soft background with a hairline border. On focus, the border becomes the ink color and the background becomes white.

### Forms
**`text-input`** — Standard text input for forms like account creation and checkout. White background with a hairline border. Focus state uses an ink-colored border. Error state uses a red border.
**`select-dropdown`** — A dropdown selector for filtering by genre, format, or sort order. Matches the text-input styling for visual consistency.
**`quantity-selector`** — A compact control for adjusting item quantities in the cart. Contains a minus button, the quantity number, and a plus button, all within a surface-soft container with a hairline border.

### Footer
**`footer`** — A dense, full-width footer with an ink (#1e1e1e) background and white text. Contains links to label pages, customer service, social media icons, and legal information. Links shift to red on hover. Social icons are simple monochrome SVGs that also shift to red on hover.

### Filters
**`filter-chip`** — A pill-shaped filter for browsing by genre, format, or price range. Uses a surface-soft background with a hairline border. Active state inverts to an ink background with white text. Hover state shows a stronger border.

### Pagination
**`pagination-button`** — Square buttons for navigating between pages of search results or category listings. Default is transparent with ink text. Active state inverts to ink background with white text. Hover state uses a surface-soft background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row). Top nav collapses to hamburger menu. Search bar becomes a full-width expandable field. Filter chips stack vertically. Footer links collapse into accordion sections. Product card images remain square but at full width. |
| Tablet | 744–1128px | Two-column product grid. Top nav shows limited links (logo, search, cart, hamburger for rest). Filter chips wrap to two rows. Footer shows all links in a two-column layout. |
| Desktop | 1128–1440px | Three-column product grid. Full top nav with all links visible. Filter chips in a single horizontal row. Footer in a four-column layout. Product cards show hover states. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centers content. Additional whitespace around the grid. Marquee strip spans full width. |

### Touch Targets
- All interactive elements (buttons, links, chips) have a minimum touch target of 44x44px.
- Product card tap area includes the entire card, not just the text.
- Quantity selector buttons are 32x32px with 44x44px tap areas via padding.
- Filter chips have 8px padding around text to ensure adequate tap area.
- Cart icon and search icon have 44x44px tap areas.

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px, with a slide-out drawer for all links.
- Product grid collapses from 4 columns to 1 column at mobile.
- Filter chips collapse from a horizontal row to a vertical stack at mobile, with a "Filters" button that opens a modal.
- Footer links collapse from a multi-column layout to accordion sections at mobile.
- Marquee strip hides entirely at mobile to save vertical space.
- Search bar collapses from a visible field to an icon that expands on tap at mobile.
- Breadcrumbs truncate to show only the current page and a "Back" link at mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (e.g., zoom, color shift) could not be reliably extracted from the live site.
- Error styling for form validation (error messages, error icon placement) was not visible in the extracted data.
- Dark mode or high-contrast mode variants are not present in the extracted styles.
- Sub-brand palettes for individual labels (Secretly Canadian, Jagjaguwar, Dead Oceans) were not distinguishable from the main store palette.
- Checkout flow styling (Shopify checkout pages) was not extracted; the extracted colors may include Shopify Pay widget colors that are not part of the brand system.
- Loading states (skeleton screens, shimmer effects) were not observed in the extracted data.
- The exact font weights used for Jost and Karla could not be confirmed beyond the extracted declarations; the weights in this document are inferred from common usage patterns.
- Animation durations and easing curves were not extractable from the static CSS.
- Focus ring styling for keyboard navigation was not visible in the extracted data.
- The marquee strip's scroll behavior (automatic vs. manual) could not be determined.
