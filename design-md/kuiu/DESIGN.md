---
version: alpha
name: "Kuiu"
source_url: "https://www.kuiu.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A backcountry-hunting brand that uses a muted sage #aaccaa as its primary identifier — not camouflage green or blaze orange, but a dry, alpine-lichen tone that signals the Sierra Nevada palette rather than the bass-pro-shop aisle. The brand's visual system runs on high-contrast dark ink (#202020) against a near-white canvas (#f8f8f8), with a secondary accent of deep crimson (#970c11) reserved for sale badges, cart indicators, and urgent CTAs. Typography defaults to system sans-serif stacks (Arial, Helvetica Neue, Roboto) at moderate weights — no proprietary typeface, no display faces; the brand lets product photography and technical copy carry the authority. Cards and buttons use soft rounding ({rounded.sm} ~8px) that reads as utilitarian rather than friendly, and the nav bar sits at a compact 64px with a sticky white background and a single search icon. The checkout flow introduces a warm olive (#6f6c42) and a muted gold (#dbbb07) for progress indicators and trust badges, but the core shopping experience is deliberately austere: white space, grid product tiles, and a persistent "shop by category" mega-menu that reveals the full catalog without page reloads. The brand's design ethos is "performance first, decoration never" — every visual decision serves legibility in field conditions and fast load times on satellite internet.

colors:
  primary: "#aaccaa"
  primary-active: "#8fb88f"
  primary-disabled: "#d4e6d4"
  ink: "#202020"
  body: "#3a3a3a"
  muted: "#6f6f6f"
  muted-soft: "#949494"
  hairline: "#dedede"
  hairline-soft: "#e8e9eb"
  canvas: "#f8f8f8"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#202020"
  accent-red: "#970c11"
  accent-red-active: "#7a0a0e"
  accent-olive: "#6f6c42"
  accent-gold: "#dbbb07"
  accent-steel: "#4c6e87"
  accent-steel-light: "#436076"
  dark-canvas: "#121212"
  dark-surface: "#222222"
  dark-hairline: "#262626"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica Neue, Roboto, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-text-only:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-text-only-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-icon-square:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  button-quantity:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
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
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-logo:
    height: 28px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  nav-mega-menu-column:
    padding: "{spacing.md} {spacing.lg}"
  nav-mega-menu-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  nav-mega-menu-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} 0"
  nav-mega-menu-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid transparent"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  search-icon:
    height: 20px
    width: 20px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  product-card-price-sale:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-red}"
    fontWeight: 600
  product-card-compare-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-quick-add:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  product-card-quick-add-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "rgba(0,0,0,0.3)"
  hero-banner-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-banner-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.canvas}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  hero-banner-cta-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  category-tile-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  category-tile-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
  filter-group:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  filter-group-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  filter-checkbox:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} 0"
  filter-checkbox-active:
    textColor: "{colors.primary}"
  filter-color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "1px solid {colors.hairline}"
  filter-color-swatch-active:
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-newsletter-input:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.dark-hairline}"
  footer-newsletter-input-focus:
    border: "1px solid {colors.primary}"
  footer-newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  footer-social-icon:
    height: 24px
    width: 24px
    textColor: "{colors.muted-soft}"
  footer-social-icon-hover:
    textColor: "{colors.canvas}"
  footer-bottom-bar:
    borderTop: "1px solid {colors.dark-hairline}"
    padding: "{spacing.lg} 0"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.muted}"
  breadcrumb-link-hover:
    textColor: "{colors.ink}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  pagination-inactive-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.ink}"
  accordion:
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
  accordion-icon:
    height: 16px
    width: 16px
    textColor: "{colors.ink}"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTopColor: "{colors.primary}"
    height: 24px
    width: 24px
    rounded: "{rounded.full}"
  loading-spinner-lg:
    border: "4px solid {colors.hairline-soft}"
    borderTopColor: "{colors.primary}"
    height: 40px
    width: 40px
    rounded: "{rounded.full}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill-accent:
    backgroundColor: "{colors.accent-gold}"
    height: 4px
    rounded: "{rounded.full}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  trust-badge-icon:
    height: 20px
    width: 20px
    textColor: "{colors.accent-olive}"
  cart-icon:
    height: 24px
    width: 24px
    textColor: "{colors.ink}"
  cart-icon-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  wishlist-icon:
    height: 20px
    width: 20px
    textColor: "{colors.muted}"
  wishlist-icon-active:
    textColor: "{colors.accent-red}"
  rating-stars:
    textColor: "{colors.accent-gold}"
    height: 16px
  rating-stars-empty:
    textColor: "{colors.hairline}"
    height: 16px
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    minWidth: 40px
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  size-selector-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    height: 44px
    width: 44px
  quantity-selector-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: center
    height: 44px
    width: 48px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.hairline}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-low-stock:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-free-shipping:
    backgroundColor: "{colors.accent-steel}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  alert-success:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.primary}"
  alert-error:
    backgroundColor: "#fce4e4"
    textColor: "{colors.accent-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.accent-red}"
  alert-info:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's sage green (#aaccaa) with dark ink text. Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, shifts to a deeper sage (#8fb88f). Disabled state uses a pale sage (#d4e6d4) with muted text to signal inactivity without visual noise.

**`button-secondary`** — A white button with a single hairline border, used for "View Details", "Learn More", and secondary actions. On hover, the border darkens to ink and the background shifts to surface-soft (#f4f4f4). Pairs naturally alongside the primary button in checkout and product-detail flows.

**`button-accent-red`** — The urgent-action button, using the brand's deep crimson (#970c11) on white. Reserved for clearance sales, limited-time offers, and cart-urgency prompts. On hover, deepens to #7a0a0e. Never used for standard add-to-cart — only for time-sensitive or high-discount scenarios.

**`button-text-only`** — A borderless, backgroundless button for tertiary actions like "Clear Filters", "Cancel", and "Remove". On hover, text shifts to the primary sage to indicate interactivity. Uses the same button-md typography as other buttons for consistent vertical rhythm.

**`button-icon-square`** — A 40x40px square button with a single hairline border, used for wishlist toggles, share actions, and quick-view triggers. The icon sits centered with no label. On hover, the border darkens to ink.

**`button-quantity`** — A compact 36x36px button used in the quantity selector for increment/decrement actions. Uses xs rounding and a hairline border. The plus/minus icon sits centered.

### Cards
**`product-card`** — A clean white card with soft 8px rounding, no shadow, and a 1:1 product image that fills the top. Below the image, the product title uses title-sm typography, the price uses body-md with 600 weight, and sale prices render in accent-red with a line-through compare price. Badges (Sale, New, Sold Out) sit as overlays on the image, positioned top-left with xs rounding and uppercase badge typography. A "Quick Add" button appears on hover, rendered as a secondary-style button with a hairline border.

**`category-tile`** — A bordered card (1px hairline-soft) used for department navigation on the homepage and collection pages. Contains a category image with top-only rounding and a title-md label below. On hover, the border shifts to primary sage and a subtle box-shadow lifts the tile.

### Navigation
**`nav-bar`** — A sticky 64px white bar with the KUIU logo (28px height) left-aligned, a full-width mega-menu triggered by "Shop" and category links, a search bar (40px pill with surface-soft background), and a cart icon with a red badge. The nav uses uppercase nav-link typography at 14px with 600 weight. On scroll, a thin bottom border and a 2px box-shadow appear.

**`nav-mega-menu`** — A full-width dropdown panel triggered by top-level nav items. Contains columns of category links with heading labels in title-sm and body-sm links below. The panel sits flush below the nav bar with a bottom border. Links hover to primary sage.

### Forms
**`text-input`** — A 48px tall input with 8px rounding, a hairline border, and body-md typography. On focus, the border shifts to primary sage. Error state uses a red border (#970c11). Used for email, password, search, and address fields.

**`select-input`** — Matches text-input dimensions and styling but includes a custom dropdown arrow. Used for size selection, sorting, and filter dropdowns.

**`textarea`** — Matches text-input styling but with a flexible height. Used for product reviews and contact forms.

### Footer
**`footer`** — A dark-section footer on a near-black canvas (#121212) with surface-dark (#222222) newsletter input fields and hairline-dark (#262626) dividers. Links render in muted-soft (#949494) and hover to white. The footer includes a newsletter signup with a primary sage button, social icons, and a bottom bar with copyright and legal links.

### Badges & Indicators
**`product-card-badge`** — Small uppercase badges (11px, 700 weight) with xs rounding, used for Sale (red background), New (sage background), and Sold Out (muted background). Positioned as overlays on product images.

**`badge-sold-out`**, **`badge-low-stock`**, **`badge-free-shipping`** — Standalone badges used in product detail pages and cart summaries. Sold out uses muted gray, low stock uses gold (#dbbb07), and free shipping uses steel blue (#4c6e87).

### Alerts
**`alert-success`** — A pale sage background with a sage border, used for "Added to Cart" confirmations and successful form submissions. Uses body-sm typography with 12px padding.

**`alert-error`** — A pale red background (#fce4e4) with a crimson border, used for validation errors, out-of-stock messages, and payment failures. Text renders in accent-red.

**`alert-info`** — A surface-soft background with a hairline border, used for informational messages like shipping thresholds and size-guide prompts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; mega-menu becomes full-screen drawer; product grid goes to 1 column; hero banner height reduces to 320px; footer stacks vertically; filter panel becomes a bottom sheet; search bar collapses to icon-only |
| Tablet | 744–1128px | Nav shows top-level links but mega-menu becomes a dropdown panel; product grid uses 2 columns; filter panel slides in from left; hero banner at 400px; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with mega-menu; product grid uses 3 columns; filter panel is persistent sidebar; hero banner at 480px; footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px centered; product grid uses 4 columns; hero banner at 520px; all layouts remain desktop pattern but with more whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile
- Product card quick-add buttons are 36px tall but padded within a 44px touch zone
- Quantity selector buttons are 44x44px on mobile (reduced to 36x36px on desktop)
- Filter checkboxes have 44px tap zones with 16px padding
- Nav hamburger icon is 44x44px
- Cart icon badge is 18px but sits within a 44px icon touch zone

### Collapsing Strategy
- Top nav collapses to a hamburger menu at < 744px; the logo remains centered, cart icon stays visible
- Mega-menu collapses to a full-screen drawer with accordion-style category expansion
- Product filters collapse to a bottom sheet with a "Apply Filters" button
- Footer columns collapse to a single column with accordion-style section headers
- Search bar collapses to a search icon that expands to a full-width input on tap
- Product image galleries collapse from thumbnail strip to swipeable carousel
- Size selector collapses from grid to horizontal scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family extraction returned only system fallbacks (Arial, Helvetica Neue, Roboto, etc.) — no proprietary or custom typeface was detected. The brand may use a licensed font that wasn't present in the extracted CSS. All typography tokens use the system stack as a fallback.
- Hover and active states for many components (filter checkboxes, breadcrumb links, accordion headers) were inferred from common patterns rather than extracted from the live site.
- Error, success, and info alert colors were not extracted from the live site — the error red (#fce4e4 background) and success green (#d4e6d4 background) are best guesses based on the brand's palette.
- Dark mode colors (dark-canvas, dark-surface, dark-hairline) were inferred from the footer background (#121212) and may not represent a full dark-mode system.
- The accent-gold (#dbbb07) and accent-steel (#4c6e87) colors appeared in the extracted list but their specific usage (trust badges, progress indicators, rating stars) was inferred from common ecommerce patterns.
- No animation or transition timing values were extracted — all hover transitions should default to 200ms ease-in-out.
- Box-shadow values for cards and modals were not extracted — the category-tile shadow (0 4px 12px rgba(0,0,0,0.08)) is an estimate based on common ecommerce patterns.
- No focus-ring styles were extracted — accessibility focus indicators should default to a 2px primary-color outline with 2px offset.
- The brand's checkout flow (Shopify-powered) may introduce additional colors (Afterpay, Klarna, PayPal badges) that were filtered from the extracted
