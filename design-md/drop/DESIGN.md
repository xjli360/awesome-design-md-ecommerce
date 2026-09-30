---
version: alpha
name: "Drop"
source_url: "https://drop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A community-driven marketplace for mechanical keyboards and enthusiast gear, Drop uses a dark, high-contrast canvas (#0f0f0f) as its primary backdrop — an unusual choice for a DTC brand that signals seriousness and technical depth rather than retail warmth. The brand's signature voltage is a vibrant cyan (#00bcd4) that appears on primary CTAs, active navigation states, and product badges, cutting through the dark surface like a soldering iron tip. Product photography — close-ups of keycap texture, switch internals, and PCB traces — does the heavy lifting of conveying quality, while typography runs a clean sans-serif stack at modest weights (400–600) to keep the focus on the gear. Cards use sharp corners (`{rounded.none}`) for a precision-tool feel, while dropdowns and modals soften to `{rounded.sm}`. The color palette is deliberately restrained: ink (#1a1a1a) for text on light surfaces, body (#333333) for secondary copy, and a single accent green (#4caf50) for stock-available indicators. This is a brand that trusts its community's expertise — the design recedes to let the products and user reviews command attention.

colors:
  primary: "#00bcd4"
  primary-active: "#0097a7"
  primary-disabled: "#4dd0e1"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#2a2a2a"
  hairline-soft: "#3a3a3a"
  canvas: "#0f0f0f"
  surface-soft: "#1a1a1a"
  surface-card: "#222222"
  on-primary: "#ffffff"
  accent-green: "#4caf50"
  accent-orange: "#ff9800"
  accent-red: "#f44336"
  star-rating: "#ffc107"
  badge-new: "#00bcd4"
  badge-sale: "#ff9800"
  link: "#00bcd4"
  link-hover: "#4dd0e1"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  price-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-icon-square:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
  product-card-price:
    typography: "{typography.price-sm}"
    color: "{colors.on-primary}"
  product-card-rating:
    color: "{colors.star-rating}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  search-icon:
    color: "{colors.muted}"
    size: 16px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-out-of-stock:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  dropdown-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  dropdown-item:
    padding: "{spacing.sm} {spacing.base}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  slider:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    thumbColor: "{colors.primary}"
    height: 4px
    thumbSize: 16px
  checkbox:
    borderColor: "{colors.hairline}"
    checkedColor: "{colors.primary}"
    checkmarkColor: "{colors.on-primary}"
    size: 18px
    rounded: "{rounded.xs}"
  radio:
    borderColor: "{colors.hairline}"
    checkedColor: "{colors.primary}"
    dotColor: "{colors.on-primary}"
    size: 18px
  toggle:
    backgroundColor: "{colors.hairline}"
    activeColor: "{colors.primary}"
    thumbColor: "{colors.on-primary}"
    height: 20px
    width: 36px
    rounded: "{rounded.full}"
  pagination:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    activeBackgroundColor: transparent
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
    spacing: "{spacing.xxs}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  review-card-author:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  review-card-date:
    typography: "{typography.caption-sm}"
    color: "{colors.muted-soft}"
  community-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  filter-chip-hover:
    border: "1px solid {colors.primary}"
  sort-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 10px"
    height: 36px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  add-to-cart-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  wishlist-button-active:
    textColor: "{colors.accent-red}"
  cart-icon:
    color: "{colors.on-primary}"
    size: 20px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"
  cart-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  cart-item:
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-item-title:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
  cart-item-price:
    typography: "{typography.price-sm}"
    color: "{colors.on-primary}"
  cart-item-quantity:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  cart-total:
    typography: "{typography.price}"
    color: "{colors.on-primary}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
  logo:
    height: 24px
    color: "{colors.on-primary}"
  logo-hover:
    color: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.on-primary}"
    padding: "{spacing.lg} 0"
  section-subheader:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "{spacing.sm} 0"
  empty-state:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "{spacing.section} {spacing.lg}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loader:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    height: 16px
  skeleton-loader-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    height: 200px
  notification-toast:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  notification-toast-success:
    borderLeft: "4px solid {colors.accent-green}"
  notification-toast-error:
    borderLeft: "4px solid {colors.accent-red}"
  notification-toast-info:
    borderLeft: "4px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action on a dark canvas. Uses the brand cyan (#00bcd4) as a high-contrast accent. On hover, shifts to `{colors.primary-active}` (#0097a7). Disabled state uses `{colors.primary-disabled}` (#4dd0e1) with reduced opacity. Text is always white. **`button-secondary`** — An outlined button on a dark card background. Uses a 1px hairline border and white text. On hover, the border becomes the brand cyan. **`button-tertiary-text`** — A text-only link styled as a button, using the brand cyan for the text. No background or border. **`button-icon-square`** — A small square icon button for actions like add to wishlist or share. Uses a card background with a hairline border.

### Cards
**`product-card`** — The core product display unit. Sharp corners (`{rounded.none}`) for a precision-tool feel. On hover, the background shifts to `{colors.surface-soft}` and a hairline border appears. Contains a full-bleed image, title, price, rating stars, and optional badges. **`review-card`** — A review entry with author, date, and text. Uses a card background with a bottom hairline divider. No rounded corners. **`community-badge`** — A pill-shaped badge indicating community status (e.g., "Top Contributor"). Uses a soft background with cyan text.

### Navigation
**`nav-bar`** — A fixed top bar on the dark canvas, 56px tall, with a bottom hairline border. Contains the logo, navigation links, search bar, and cart icon. Active links get a cyan underline. **`tab-active` / `tab-inactive`** — Used for product category filtering and page sections. Active tab has a cyan bottom border and cyan text. Inactive tab uses muted gray. **`breadcrumb`** — A simple breadcrumb trail using muted gray text and a separator.

### Forms
**`text-input`** — A dark card background input with a hairline border. On focus, the border becomes cyan. Error state uses red border. **`select-input`** — A dropdown selector matching the text input styling. **`checkbox`** / **`radio`** — Small interactive elements with hairline borders. Checked state fills with cyan. **`toggle`** — A pill-shaped toggle switch. Active state uses cyan. **`filter-chip`** — A pill-shaped filter option. Active state fills with cyan. **`sort-dropdown`** — A compact dropdown for sorting options. **`quantity-selector`** — A compact input for selecting item quantity.

### Search
**`search-bar`** — A pill-shaped search input on the dark canvas. Uses a card background with a hairline border. On focus, the border becomes cyan. Contains a search icon in muted gray.

### Footer
**`footer`** — A dark footer section with a top hairline divider. Links use muted gray text and turn cyan on hover. Contains legal text, community links, and social icons.

### Modals & Overlays
**`modal-overlay`** — A semi-transparent black overlay (60% opacity) behind modals. **`modal-content`** — A dark card modal with `{rounded.md}` corners and generous padding. **`tooltip`** — A small dark tooltip with `{rounded.sm}` corners.

### Progress & Sliders
**`progress-bar`** — A thin progress bar with a cyan fill. **`slider`** — A range slider with a cyan track fill and cyan thumb.

### Cart & Checkout
**`cart-icon`** — A simple cart icon in white. **`cart-badge`** — A small cyan badge showing item count. **`cart-dropdown`** — A dropdown cart preview with items, totals, and a checkout button. **`add-to-cart-button`** — A prominent cyan button for adding items to cart. **`checkout-button`** — A full-width cyan button for proceeding to checkout.

### States & Feedback
**`loading-spinner`** — A cyan spinning indicator. **`skeleton-loader`** — A placeholder for loading content, using hairline gray. **`notification-toast`** — A floating notification with a colored left border (green for success, red for error, cyan for info). **`empty-state`** — A centered message for empty lists or search results. **`pagination`** — A set of page number links. Active page uses cyan text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), hamburger menu replaces top nav, search bar collapses to icon, footer stacks vertically, hero banner reduces padding to 32px, product card images become full-width, filter sidebar becomes a bottom sheet, cart dropdown becomes full-screen overlay |
| Tablet | 744–1128px | Two-column product grid (2 items per row), top nav shows limited links with "More" dropdown, search bar remains visible but narrower, footer splits into two columns, hero banner uses 48px padding, filter sidebar becomes a collapsible panel |
| Desktop | 1128–1440px | Three-column product grid (3 items per row), full top nav with all links visible, search bar at full width, footer in four columns, hero banner uses 64px padding, filter sidebar is always visible |
| Wide | > 1440px | Four-column product grid (4 items per row), max-width container at 1440px centered, hero banner uses 80px padding, additional whitespace around product cards, filter sidebar remains visible |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile.
- Icon buttons (wishlist, cart, search) are 36x36px minimum with adequate padding.
- Filter chips and badges are at least 32px tall.
- Dropdown items have a minimum height of 40px.
- Slider thumbs are 16px minimum (20px recommended on mobile).

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px).
- Product grid collapses from 4 columns (wide) to 1 column (mobile).
- Filter sidebar collapses to a bottom sheet or collapsible panel on tablet and mobile.
- Footer collapses from 4 columns (desktop) to 1 column (mobile).
- Search bar collapses to an icon on mobile, expanding on tap.
- Cart dropdown becomes a full-screen overlay on mobile.
- Hero banner reduces padding and font size on smaller screens.
- Breadcrumbs truncate on mobile, showing only the current page and a back link.
- Tab bars may scroll horizontally on mobile if there are many tabs.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography block uses a generic sans-serif stack (Inter, system-ui) as a reasonable default for a tech/community brand. The actual brand font may differ.
- No hex colors were extracted from the live site (the extraction returned empty). The color palette is inferred from the brand's known dark theme and community-visible assets. The actual primary, secondary, and accent colors should be verified against the brand's official design tokens.
- Hover, active, and focus states for many components (e.g., dropdown items, filter chips, tabs) are inferred from common patterns and may not match the exact implementation.
- Error styling for forms (text-input-error) is assumed to use the accent red (#f44336). The actual error color and iconography should be verified.
- Dark mode is the default (and only) theme observed. A light mode variant may exist but is not documented here.
- Sub-brand palettes for collaborations (e.g., with specific keyboard manufacturers) are not captured.
- The star-rating color (#ffc107) is a common yellow and may not be the exact shade used.
- The accent-green (#4caf50) and accent-orange (#ff9800) are Material Design defaults and may be placeholders.
- The logo component assumes a white logo on dark background. The actual logo format (SVG, text, etc.) is unknown.
- Animation durations, easing curves, and transition properties are not documented.
- The notification toast system may have additional variants (e.g., warning, loading) not captured here.
- The skeleton loader dimensions are generic and may not match the actual layout grid.
- The responsive breakpoints (744px, 1128px, 1440px) are common industry standards and may not match the brand's exact breakpoints.
- The touch target sizes (44x44px) follow WCAG guidelines but may differ from the brand's specific accessibility requirements.
