---
version: alpha
name: "Jackpot Records"
source_url: "https://www.jackpotrecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that wears its red like a neon sign over a damp Portland sidewalk — #dc0000 is the primary voltage, pulled from the meta theme-color and splashed across the top nav bar, sale badges, and the site's single persistent CTA. The canvas is a cool off-white #f3f5f6, not pure white, giving the page a slightly aged paper stock feel that suits a shop selling used vinyl and new releases side by side. The ink is a near-black #1e1e1b, dense and warm, with body text in #677279 — a muted slate that keeps reading comfortable across long browsing sessions. Product cards sit on white `{colors.surface-card}` with `{rounded.sm}` corners and a thin `{colors.hairline}` border, letting album art do all the emotional work. The typeface is Instrument Sans, a clean geometric sans with a touch of warmth, set at modest weights — display headlines at 500, body at 400 — never competing with the record covers. A secondary green accent #008a00 appears in stock indicators and "Add to Cart" states, while #ffbd00 marks sale prices and limited-edition drops. The overall feeling is that of a well-organized bin at your favorite shop: nothing precious, everything findable, and the red keeps pulling your eye to what matters.

colors:
  primary: "#dc0000"
  primary-active: "#900000"
  primary-disabled: "#dedede"
  ink: "#1e1e1b"
  body: "#677279"
  muted: "#696969"
  muted-soft: "#8a9297"
  hairline: "#dedede"
  hairline-soft: "#f3f5f6"
  canvas: "#f3f5f6"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#008a00"
  accent-green-active: "#00a500"
  accent-yellow: "#ffbd00"
  accent-red-dark: "#900000"
  badge-new: "#dc0000"
  badge-sale: "#ffbd00"
  stock-in: "#008a00"
  stock-low: "#ffbd00"
  stock-out: "#dc0000"

typography:
  display-xl:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
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
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-ghost-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  button-cart:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-cart-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.on-primary}"
  button-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.none}"
  top-nav-link-active:
    backgroundColor: "{colors.accent-red-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  top-nav-search-icon:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    margin: "{spacing.sm} 0 {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-stock:
    typography: "{typography.caption-sm}"
    textColor: "{colors.stock-in}"
  product-card-stock-low:
    typography: "{typography.caption-sm}"
    textColor: "{colors.stock-low}"
  product-card-stock-out:
    typography: "{typography.caption-sm}"
    textColor: "{colors.stock-out}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "6px 16px"
    rounded: "{rounded.full}"
  category-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "4px 0"
  footer-link-hover:
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 500
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-disabled:
    textColor: "{colors.muted-soft}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-sm:
    color: "{colors.muted}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "4px"
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 28px
    width: 28px
  quantity-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textAlign: center
    width: 40px
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  filter-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    margin: "0 0 {spacing.sm}"
  filter-option:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "4px 0"
  filter-option-active:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
    fontWeight: 500
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 16px
    width: 16px
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  sort-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  sort-dropdown-focus:
    border: "1px solid {colors.primary}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 360px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  cart-item-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  cart-checkout-button:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
  cart-checkout-button-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — The primary call to action across the store. Rendered in `{colors.primary}` with white text and `{rounded.sm}` corners. Used for "Add to Cart" on product pages, "Shop Now" on hero banners, and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#900000) — a deeper, more urgent red. Disabled state drops to `{colors.primary-disabled}` (#dedede) with `{colors.muted}` text, signaling the action is unavailable.
**`button-secondary`** — Outlined alternative for secondary actions like "View Details" or "Pre-Order". Uses a white background with `{colors.ink}` text and a 1px `{colors.hairline}` border. On hover, the background fills with `{colors.hairline-soft}` (#f3f5f6) for a subtle lift. Same 44px height and `{rounded.sm}` as the primary button for visual consistency.
**`button-ghost`** — Text-only button for tertiary actions like "Clear Filters" or "Cancel". No background, `{colors.ink}` text, with a hover state that adds a `{colors.hairline-soft}` background. Minimal footprint, used where visual weight would compete with the primary action.
**`button-cart`** — Dedicated "Add to Cart" button in `{colors.accent-green}` (#008a00) — a deliberate departure from the red system to signal a positive, confirmatory action. Active state shifts to `{colors.accent-green-active}` (#00a500). Same dimensions as `button-primary` for consistent layout.
**`button-sale`** — Small, high-visibility badge-button for sale prices and limited drops. Uses `{colors.accent-yellow}` (#ffbd00) background with `{colors.ink}` text. Tight padding (6px 12px) and `{typography.button-sm}` sizing keeps it compact on product cards.

### Navigation
**`top-nav`** — The persistent header bar, a solid band of `{colors.primary}` (#dc0000) at 56px height. Navigation links use `{typography.nav-link}` — 14px uppercase with 0.5px letter spacing — in white. The active link state gets a `{colors.accent-red-dark}` (#900000) background with `{rounded.sm}` for a subtle tab-like feel. A search icon button sits at the right edge, rendered as a `{rounded.full}` circle for quick access.
**`top-nav-link`** — Individual navigation items within the top bar. Transparent background by default, white text. Hover adds a slight opacity shift. Active state uses the darker red background to indicate current section.
**`category-nav`** — Secondary navigation strip below the hero or above product grids. Links are rendered as pills with `{rounded.full}` — the active category gets a `{colors.primary}` background with white text, while inactive links stay in `{colors.body}` with transparent background. This creates a clear visual hierarchy between the persistent top nav and the contextual category filter.
**`breadcrumb`** — Standard breadcrumb trail using `{typography.caption}` (13px). Current page is bolded in `{colors.ink}`, while parent links use `{colors.body}`. Separators are implied by spacing and a muted slash character.

### Cards
**`product-card`** — The core product display unit. A white card on `{colors.canvas}` (#f3f5f6) with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. On hover, the border shifts to `{colors.primary}` — a subtle red outline that signals interactivity without overwhelming the album art. The card image uses `{rounded.sm}` and a 1:1 aspect ratio with `object-fit: cover` for consistent framing. Title sits below in `{typography.title-sm}` (16px, weight 500), with price in `{typography.price}` (16px, weight 500) in `{colors.body}`. Sale prices swap to `{typography.price-sale}` (weight 600) in `{colors.primary}`.
**`product-card-badge`** — Small uppercase label overlaid on the card image, typically "NEW" or "PRE-ORDER". Uses `{colors.badge-new}` (#dc0000) background with white text, `{typography.badge}` (11px, weight 600, 0.5px letter spacing), and `{rounded.xs}` corners. Sale badges use `{colors.badge-sale}` (#ffbd00) with `{colors.ink}` text.
**`product-card-stock`** — Inline stock indicator below the price. Uses `{typography.caption-sm}` (12px). Color shifts by status: `{colors.stock-in}` (#008a00) for "In Stock", `{colors.stock-low}` (#ffbd00) for "Low Stock", and `{colors.stock-out}` (#dc0000) for "Sold Out".

### Forms & Inputs
**`search-bar`** — The primary search input, rendered on `{colors.canvas}` with `{colors.body}` text and a 1px `{colors.hairline}` border. `{rounded.md}` (8px) corners and 40px height keep it compact. On focus, the border swaps to `{colors.primary}` for clear visual feedback. Used in the top nav and on search results pages.
**`newsletter-input`** — Email input for the footer signup form. Matches the search bar in height (44px) and styling, but sits alongside a `{colors.primary}` submit button. The submit button uses `{typography.button-sm}` (13px) for a tighter fit.
**`quantity-selector`** — Compact control for adjusting item quantities in the cart. A bordered container with `{rounded.sm}` houses two small square buttons (28px) flanking a centered text input (40px wide). Buttons use `{colors.hairline-soft}` background with `{rounded.xs}` for a nested, tactile feel.
**`sort-dropdown`** — Standard select dropdown for sorting product lists. Matches the search bar in height (40px) and border styling. On focus, the border shifts to `{colors.primary}`. The dropdown arrow is implied by browser default or a custom chevron icon.

### Footer
**`footer`** — A dark band of `{colors.ink}` (#1e1e1b) at the bottom of every page. Links render in `{colors.muted-soft}` (#8a9297) and shift to white on hover. The newsletter signup form sits prominently in the footer, with the input on a white background and the submit button in `{colors.primary}`. Padding is generous at `{spacing.xxl}` (48px) top and bottom, with `{spacing.lg}` (24px) side padding.

### Miscellaneous
**`hero-banner`** — Full-width promotional banner, typically at the top of the homepage. Uses a `{colors.ink}` background with white text for high contrast. Title uses `{typography.display-xl}` (32px, weight 500), subtitle uses `{typography.body-md}` (16px) in `{colors.muted-soft}`. The CTA button matches `button-primary` styling. Padding is `{spacing.section}` (64px) vertical for a spacious, immersive feel.
**`pagination`** — Page navigation at the bottom of product lists. Individual page numbers are rendered as `{rounded.sm}` pills. The active page uses `{colors.primary}` background with white text; inactive pages use transparent background with `{colors.body}` text. Disabled pages (e.g., "previous" on page 1) drop to `{colors.muted-soft}`.
**`loading-spinner`** — A 24px circular spinner in `{colors.primary}` for primary loading states. A smaller 16px variant in `{colors.muted}` is used for inline loading indicators (e.g., within a button or filter panel).
**`divider`** — A 1px horizontal rule in `{colors.hairline}` (#dedede) for separating sections. A softer variant in `{colors.hairline-soft}` (#f3f5f6) is used within cards or tight layouts where a lighter touch is needed.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product grid goes single-column (1 col); search bar moves to a toggleable overlay; category nav becomes a horizontal scrollable strip; footer stacks vertically; hero banner reduces padding to 32px; product card badges scale down to 10px font |
| Tablet | 744–1128px | Top nav shows 4-5 links with overflow menu; product grid uses 2 columns; category nav shows as pills in a scrollable row; search bar remains visible but compact; hero banner uses 48px padding; footer splits into 2 columns |
| Desktop | 1128–1440px | Full top nav with all links visible; product grid uses 3-4 columns; category nav shows as a horizontal row of pills; search bar full width in nav; hero banner uses 64px padding; footer uses 3-4 columns |
| Wide | > 1440px | Max content width of 1440px with centered layout; product grid uses 4-5 columns; category nav remains horizontal; hero banner expands to full width with max-width content container; footer columns increase spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (search, cart, hamburger) use 36px minimum touch area
- Category nav pills use 40px height for easy tapping
- Quantity selector buttons are 28px — slightly below the 44px recommendation but acceptable for the compact control
- Filter checkboxes use 16px with surrounding padding to reach 44px touch area
- Pagination pills use 36px height with 8px padding for comfortable tapping

### Collapsing Strategy
- Top nav links collapse into a hamburger menu below 744px; the hamburger icon remains in the red nav bar
- Search bar collapses to an icon-only trigger on mobile; tapping expands a full-width overlay
- Category nav collapses from a multi-row layout to a single horizontal scrollable strip on mobile and tablet
- Product grid collapses from 4-5 columns on wide screens to 1 column on mobile
- Footer columns collapse from 3-4 on desktop to a single stacked column on mobile
- Filter panel collapses to a toggleable drawer on mobile, with a "Filters" button that opens an overlay
- Cart drawer remains a slide-in panel on all breakpoints but shifts to full-width on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components are inferred from common patterns; actual extracted hover colors are not available
- Error styling for form inputs (validation, error messages) is not present in the extracted data
- The extracted color list is heavily polluted with social media brand colors (#3b5998 Facebook, #1da1f2 Twitter, #bd081c Pinterest, #d83776 Instagram, #fd355a, #1ab7ea, #0077b5 LinkedIn, #f5dc30, #35465c, #494e58, #f26522, #ee0000) — these are likely from share buttons or checkout widgets, not the brand palette
- The green family (#008a00, #00aa00, #00a500) appears multiple times and is used as a secondary accent, but exact usage context (stock indicators vs. buttons vs. links) is inferred
- Font weights beyond 500 and 400 are not confirmed; Instrument Sans may support additional weights not present in extracted CSS
- Dark mode is not supported; no extracted styles suggest a dark theme variant
- Sub-brand or seasonal color palettes (Record Store Day, exclusive drops) are not captured
- Animation and transition durations/easings are not extracted
- Shadow tokens (box-shadow, drop-shadow) are not present in the extracted data
- The exact spacing between product cards in grid layouts is inferred from common e-commerce patterns
- Mobile navigation drawer (hamburger menu) styling is not extracted; the overlay behavior is assumed
- Checkout flow styling (Shopify checkout) is not included as it typically uses Shopify's own design system
- The extracted font-family list includes "monospace" and "object-fit: cover" which are likely CSS property values rather than font declarations
- Social icon colors are excluded from the primary palette; the brand's true accent colors are #dc0000 (red), #008a00 (green), and #ffbd00 (yellow)
