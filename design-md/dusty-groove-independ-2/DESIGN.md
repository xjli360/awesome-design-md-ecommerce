---
version: alpha
name: "Dusty Groove"
source_url: "https://www.dustygroove.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, vinyl-first marketplace where a single dark gray `#313131` anchors the entire interface — not as a background but as the primary color for buttons, links, and key interactive elements, giving the site the weight and permanence of a record shelf. The typography stack defaults to system fonts (`-apple-system`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `sans-serif`), a pragmatic choice that lets the product photography — album covers in all their original art — carry the visual personality. Product listings stack in dense, text-heavy grids with minimal whitespace, prioritizing information density over editorial breathing room. Search is the dominant navigation pattern, with a full-width bar at the top that accepts artist, label, or catalog queries. The checkout flow introduces a secondary accent in `#007bff` (a standard blue) for actionable links and form elements, creating a subtle but clear distinction between browsing mode and transaction mode. Cards use `{rounded.sm}` corners, just enough to soften the edge without competing with the album art's own geometry. The overall mood is utilitarian and knowledgeable — a record store that trusts its inventory and its customers' patience over visual seduction.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#888888"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link-blue: "#007bff"
  link-blue-hover: "#0056b3"
  price-green: "#2d8a2d"
  stock-green: "#28a745"
  out-of-stock: "#dc3545"
  badge-new: "#ffc107"
  badge-sale: "#dc3545"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 4px 8px
  button-link-hover:
    textColor: "{colors.link-blue-hover}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-add-to-cart-active:
    backgroundColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.primary}40"
  text-input-error:
    border: "1px solid {colors.out-of-stock}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-link:
    color: "{colors.body}"
    padding: "0 {spacing.base}"
  nav-bar-link-active:
    color: "{colors.primary}"
    fontWeight: 700
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.price-green}"
    fontWeight: 600
  product-card-stock:
    typography: "{typography.caption}"
    color: "{colors.stock-green}"
  product-card-out-of-stock:
    color: "{colors.out-of-stock}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
  badge-out-of-stock:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
    borderTop: "1px solid {colors.hairline-soft}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.link-blue}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-disabled:
    color: "{colors.muted-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    padding: "0 {spacing.sm}"
    height: 34px
  quantity-selector-button-hover:
    backgroundColor: "{colors.hairline-soft}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-item-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  cart-item-price:
    typography: "{typography.body-md}"
    color: "{colors.price-green}"
    fontWeight: 600
  checkout-button:
    backgroundColor: "{colors.price-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  checkout-button-hover:
    backgroundColor: "#237a23"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline-soft}"
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Search", and key form submissions. Rendered in `{colors.primary}` (`#313131`) with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (`#1a1a1a`). Disabled state uses `{colors.primary-disabled}` (`#888888`). Height is compact at 36px to match the dense information layout.

**`button-secondary`** — Outline variant for secondary actions like "View Details" or "Clear Filters". White background with `{colors.primary}` text and a `{colors.hairline}` border. Active state darkens the border to `{colors.primary}` and adds a light gray background.

**`button-link`** — Text-only link styled in `{colors.link-blue}` (`#007bff`), used for "Learn More", "View All", and navigation within product listings. Hover shifts to `{colors.link-blue-hover}` (`#0056b3`). No background or border.

**`button-add-to-cart`** — A slightly taller (40px) variant of `button-primary` specifically for the product detail page's add-to-cart action. More padding (10px 20px) to accommodate longer text like "Add to Cart" or "Pre-Order".

### Forms
**`text-input`** — Standard input field for search, checkout forms, and account pages. White background, `{colors.body}` text, `{rounded.sm}` corners, and a `{colors.hairline}` border. Focus state adds a `{colors.primary}` border with a subtle 2px outline at 25% opacity. Error state uses `{colors.out-of-stock}` red border.

**`search-bar`** — The primary navigation search, wider and taller (44px) than standard inputs, placed prominently in the header. Same styling as `text-input` but with larger padding for longer queries. Focus state mirrors `text-input-focus`.

### Navigation
**`nav-bar`** — A compact 48px header bar with white background and a subtle `{colors.hairline-soft}` bottom border. Links use `{typography.nav-link}` at 14px weight 600. Active link is bolded and colored `{colors.primary}`. No dropdowns — navigation is flat and text-driven.

**`breadcrumb`** — Secondary navigation for product categories and search results. Uses `{typography.caption}` at 12px in `{colors.muted}`. Links are `{colors.link-blue}` with `{colors.muted-soft}` separators. No hover effects beyond the link color change.

### Cards
**`product-card`** — The core content unit for album listings. White background with a `{colors.hairline-soft}` border and `{rounded.sm}` corners. Contains a square album art thumbnail (`{rounded.xs}`), artist name in `{colors.muted}`, album title in `{colors.ink}`, and price in `{colors.price-green}`. Hover adds a subtle shadow and darkens the border. Stock status is shown as a colored caption — green for in-stock, red for out-of-stock.

### Badges
**`badge`** — Small uppercase labels for "New Arrival", "Sale", or "Out of Stock". Default is `{colors.badge-new}` yellow with dark text. Sale variant uses `{colors.badge-sale}` red with white text. Out-of-stock uses `{colors.out-of-stock}` red. All use `{rounded.xs}` corners and tight 2px 6px padding.

### Footer
**`footer`** — A light gray (`{colors.surface-soft}`) section with `{colors.muted}` text and a `{colors.hairline-soft}` top border. Links are `{colors.muted}` on default, shifting to `{colors.primary}` on hover. Contains site map, contact info, and social links in a multi-column layout.

### Cart & Checkout
**`cart-item`** — Individual line item in the shopping cart. White background with a `{colors.hairline-soft}` bottom border between items. Title uses `{typography.title-sm}`, price uses `{typography.body-md}` in green. Quantity selector sits beside the item with increment/decrement buttons.

**`checkout-button`** — The final purchase action, styled in `{colors.price-green}` (`#2d8a2d`) to signal completion and financial transaction. Taller at 44px with more padding. Hover darkens to `#237a23`. This green is the only color that breaks from the `{colors.primary}` gray system, creating a clear visual distinction between browsing and buying.

### Filters & Pagination
**`category-filter`** — Pill-shaped filter chips for genre, format, and condition. Default is light gray (`{colors.surface-soft}`) with a subtle border. Active state fills with `{colors.primary}` and white text. Uses `{rounded.full}` for a friendly, touchable appearance.

**`pagination`** — Numbered page links at the bottom of search results. Active page gets a `{colors.primary}` background with white text in a `{rounded.sm}` box. Disabled pages are `{colors.muted-soft}`. Previous/Next arrows use `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, search bar collapses to icon, nav links hidden behind hamburger, filters stack vertically, pagination reduces to "Prev/Next" only |
| Tablet | 744–1128px | Two-column product grid, search bar full-width but condensed, category filters wrap to two rows, breadcrumb truncates |
| Desktop | 1128–1440px | Three-column product grid, full search bar with autocomplete, category filters in single row, breadcrumb full path |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, additional whitespace on sides, category filters expand to show more options |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height on mobile
- Search bar expands to full viewport width on mobile for easier tapping
- Category filter chips are minimum 36px tall with 14px horizontal padding
- Quantity selector buttons are 44px × 44px on touch devices
- Hamburger menu icon is 44px × 44px tap target

### Collapsing Strategy
- Top navigation collapses to hamburger menu on mobile (< 744px)
- Breadcrumb truncates to "Home > ... > Current Page" on tablet and mobile
- Product grid reduces columns from 4 to 1 on mobile
- Category filters collapse to a "Filter" button that opens a modal on mobile
- Footer multi-column layout stacks to single column on mobile
- Search autocomplete dropdown hides on mobile to save screen space
- Sidebar (if present) moves below main content on tablet and mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most components were inferred from common patterns; actual hover colors may differ on the live site
- **Error styling** for forms (validation messages, error icons) could not be extracted
- **Dark mode** — no evidence of dark mode support; all extracted colors assume light theme
- **Sub-brand palettes** — the site may use different colors for different genres (jazz, soul, funk) but this wasn't detectable from the extracted data
- **Animation/transition** durations and easing curves are unknown
- **Typography weight/line-height** values are estimated from common system font defaults; the live site may use different values
- **Checkout flow colors** (payment form, shipping options) may differ from the browsing experience
- **Accessibility contrast ratios** have not been verified against WCAG standards
- **Icon set** — the site likely uses custom or Font Awesome icons, but specific icon styles and sizes were not extracted
- **The extracted color palette is sparse** — only one distinctive color (`#313131`) was found, with the rest being standard web defaults. The brand's true secondary palette may be richer than what was captured.
