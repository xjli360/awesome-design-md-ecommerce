---
version: alpha
name: "Lukie Games"
source_url: "https://www.lukiegames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A retro game marketplace that wears its Bootstrap heritage like a worn-in cartridge — #337ab7 as the primary blue across every link and CTA, #777777 for body text that reads like a price tag, and a sprawling palette of status badges (#3c763d green for "In Stock", #a94442 red for "Sold Out", #8a6d3b amber for "Rare") that give the storefront the visual density of a cluttered game shop shelf. The site runs on a system of tight horizontal rows and compact product cards with {rounded.sm} corners, each card holding a thumbnail, title, and price in Arial at 14-16px — no hero imagery, no lifestyle photography, just rows of inventory. The top navigation bar uses #080808 as a near-black background with white text and a dropdown system for console categories (NES, SNES, Genesis, etc.), while the search bar sits prominently in the header as a full-width text input with a #337ab7 submit button. What makes Lukie Games feel like a genuine retro operation is the absence of polish: the design prioritizes information density over whitespace, uses #f5f5f5 and #e7e7e7 as alternating row backgrounds for table-like product lists, and relies on Bootstrap's default alert colors (#dff0d8 success, #fcf8e3 warning, #f2dede error) for order status messages. The footer is a dense column of links in #555555 on #f8f8f8, and the checkout flow uses #5cb85c green for "Add to Cart" buttons — a pragmatic, no-nonsense system built for collectors who know exactly what they want.

colors:
  primary: "#337ab7"
  primary-active: "#286090"
  primary-disabled: "#9d9d9d"
  ink: "#080808"
  body: "#777777"
  muted: "#555555"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#ececec"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#e7e7e7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#3c763d"
  success-bg: "#dff0d8"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  error: "#a94442"
  error-bg: "#f2dede"
  info: "#31708f"
  info-bg: "#d9edf7"
  stock-green: "#5cb85c"
  stock-green-active: "#449d44"
  stock-green-hover: "#398439"
  info-blue: "#5bc0de"
  warning-amber: "#f0ad4e"
  error-red: "#d9534f"
  link-hover: "#23527c"
  link-visited: "#2b542c"
  footer-text: "#555555"
  footer-bg: "#f8f8f8"
  nav-bg: "#080808"
  dropdown-bg: "#ffffff"
  dropdown-hover: "#f5f5f5"
  dropdown-divider: "#e5e5e5"
  badge-rare: "#8a6d3b"
  badge-rare-bg: "#fcf8e3"
  badge-soldout: "#a94442"
  badge-soldout-bg: "#f2dede"
  badge-instock: "#3c763d"
  badge-instock-bg: "#dff0d8"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 6px 12px
    height: 34px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.link-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-success:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-success-hover:
    backgroundColor: "{colors.stock-green-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-success-active:
    backgroundColor: "{colors.stock-green-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-danger:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-warning:
    backgroundColor: "{colors.warning-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-info:
    backgroundColor: "{colors.info-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  button-link-hover:
    backgroundColor: transparent
    textColor: "{colors.link-hover}"
    typography: "{typography.link}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 5px 10px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 8px rgba(51, 122, 183, 0.6)"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
    borderColor: "{colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 50px
  nav-dropdown:
    backgroundColor: "{colors.dropdown-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
  nav-dropdown-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 3px 20px
  nav-dropdown-item-hover:
    backgroundColor: "{colors.dropdown-hover}"
    textColor: "{colors.ink}"
  nav-dropdown-divider:
    backgroundColor: "{colors.dropdown-divider}"
    height: 1px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
    borderColor: "{colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  product-card-hover:
    borderColor: "{colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    height: 150px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
    marginTop: "{spacing.xs}"
  badge-instock:
    backgroundColor: "{colors.badge-instock-bg}"
    textColor: "{colors.success}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-soldout:
    backgroundColor: "{colors.badge-soldout-bg}"
    textColor: "{colors.error}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-rare:
    backgroundColor: "{colors.badge-rare-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 15px
    borderColor: "{colors.success}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 15px
    borderColor: "{colors.info}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 15px
    borderColor: "{colors.warning}"
  alert-danger:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 15px
    borderColor: "{colors.error}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.link-hover}"
  breadcrumb:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 15px
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  breadcrumb-active:
    textColor: "{colors.muted}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    borderColor: "{colors.hairline}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
  pagination-disabled:
    textColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline-soft}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    fontWeight: 700
    padding: 8px
    borderBottom: "2px solid {colors.hairline}"
  table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 8px
    borderBottom: "1px solid {colors.hairline}"
  table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  table-row-hover:
    backgroundColor: "{colors.dropdown-hover}"
  label:
    typography: "{typography.body-md}"
    fontWeight: 700
    textColor: "{colors.ink}"
    marginBottom: "{spacing.xs}"
  help-block:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  has-error:
    borderColor: "{colors.error}"
    boxShadow: "inset 0 1px 1px rgba(0,0,0,0.075), 0 0 6px #ce8483"
  has-success:
    borderColor: "{colors.success}"
    boxShadow: "inset 0 1px 1px rgba(0,0,0,0.075), 0 0 6px #67b168"
  has-warning:
    borderColor: "{colors.warning}"
    boxShadow: "inset 0 1px 1px rgba(0,0,0,0.075), 0 0 6px #c0a16b"
  jumbotron:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.lg}"
    rounded: "{rounded.lg}"
  page-header:
    borderBottom: "1px solid {colors.hairline-soft}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  well:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  list-group:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
  list-group-item:
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  list-group-item-hover:
    backgroundColor: "{colors.dropdown-hover}"
  list-group-item-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
  panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
  panel-heading:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  panel-body:
    padding: "{spacing.base}"
  panel-footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  modal-backdrop:
    backgroundColor: "{colors.ink}"
    opacity: 0.5
  modal-dialog:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 0
  modal-header:
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  modal-body:
    padding: "{spacing.base}"
  modal-footer:
    padding: "{spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  progress-bar:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    height: 20px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  progress-bar-success:
    backgroundColor: "{colors.stock-green}"
  progress-bar-info:
    backgroundColor: "{colors.info-blue}"
  progress-bar-warning:
    backgroundColor: "{colors.warning-amber}"
  progress-bar-danger:
    backgroundColor: "{colors.error-red}"
  badge-count:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 7px
  label-tag:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  label-default:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
  label-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  label-success:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
  label-info:
    backgroundColor: "{colors.info-blue}"
    textColor: "{colors.on-primary}"
  label-warning:
    backgroundColor: "{colors.warning-amber}"
    textColor: "{colors.on-primary}"
  label-danger:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
  thumbnail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
    borderColor: "{colors.hairline}"
  thumbnail-caption:
    padding: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Bootstrap's default blue (#337ab7) with white text and a 4px border-radius. Used for "Search", "Submit", and primary form actions. Hover state darkens to #286090, active state deepens further to #23527c, and disabled state fades to #9d9d9d. Height is 34px with 6px vertical and 12px horizontal padding.

**`button-success`** — The "Add to Cart" and checkout button, using #5cb85c green to signal positive action. Hover shifts to #398439, active to #449d44. Same 34px height and 4px border-radius as the primary button, maintaining visual consistency across the action hierarchy.

**`button-danger`** — Used for destructive actions like "Remove from Cart" or "Cancel Order", rendered in #d9534f red. Follows the same sizing and padding as other Bootstrap-style buttons.

**`button-warning`** — Amber #f0ad4e button for cautionary actions like "Flag Item" or "Report Issue". Matches the standard button dimensions.

**`button-info`** — Light blue #5bc0de button for informational actions like "View Details" or "Learn More". Standard sizing applies.

**`button-link`** — A text-only button styled as a link, using #337ab7 color with no background or border. Hover state shifts to #23527c. Used for "Cancel" actions and secondary navigation within forms.

**`button-sm`** — Compact button variant at 28px height with 5px vertical and 10px horizontal padding. Uses 12px bold font and 2px border-radius. Used for inline actions within product cards and table rows.

### Navigation
**`nav-bar`** — The top navigation bar at 50px height with #080808 near-black background and white text. Contains dropdown menus for console categories (NES, SNES, Genesis, PlayStation, etc.) and utility links (My Account, Cart, Wishlist). The brand name "Lukie Games" sits on the left as a white text link.

**`nav-dropdown`** — Dropdown menus triggered from the nav bar, using white background (#ffffff) with a #e5e5e5 border and 4px border-radius. Items are 14px Arial with 3px vertical and 20px horizontal padding. Hover state uses #f5f5f5 background. Dividers between categories are 1px #e5e5e5 lines.

### Cards
**`product-card`** — The core product display unit, a white card with 4px border-radius, 16px padding, and a #e5e5e5 border. Contains a 150px thumbnail image, the game title in 16px bold, and the price in 16px bold. Hover state highlights the border to #337ab7 blue. Badges overlay on the card for stock status.

**`product-card-badge`** — Small 11px bold labels with 2px horizontal and 6px vertical padding and 2px border-radius. Three variants: green (#3c763d on #dff0d8) for "In Stock", red (#a94442 on #f2dede) for "Sold Out", and amber (#8a6d3b on #fcf8e3) for "Rare".

### Forms
**`text-input`** — Standard 34px tall input field with 4px border-radius, 6px vertical and 12px horizontal padding, and a #e5e5e5 border. Focus state gains a #337ab7 border with an 8px blue box-shadow glow. Disabled state uses #f5f5f5 background with #9d9d9d text.

**`select-input`** — Dropdown select matching the text-input dimensions and styling. Uses the same 34px height, 4px border-radius, and #e5e5e5 border.

**`textarea`** — Multi-line text input with the same styling as text-input but without a fixed height. Used for customer notes and contact forms.

**`has-error`**, **`has-success`**, **`has-warning`** — Form validation states that apply colored borders (#a94442 red, #3c763d green, #8a6d3b amber) and inner box-shadows to input fields. Used alongside `help-block` text for validation feedback.

### Alerts
**`alert-success`** — Green alert box with #dff0d8 background, #3c763d text, and a #3c763d border. 15px padding and 4px border-radius. Used for "Item added to cart" confirmations.

**`alert-info`** — Blue alert with #d9edf7 background, #31708f text, and #31708f border. Used for informational messages like "Free shipping on orders over $50".

**`alert-warning`** — Amber alert with #fcf8e3 background, #8a6d3b text, and #8a6d3b border. Used for "Limited stock remaining" notices.

**`alert-danger`** — Red alert with #f2dede background, #a94442 text, and #a94442 border. Used for "Item out of stock" or payment failures.

### Tables
**`table-header`** — Table header row with #f5f5f5 background, bold 14px text, and a 2px #e5e5e5 bottom border. 8px padding on all sides.

**`table-row`** — Standard table row with white background, 14px #777777 text, and 1px #e5e5e5 bottom border. Alternating rows use #f5f5f5 background. Hover state uses #f5f5f5 background. Used for product listings, order history, and inventory tables.

### Footer
**`footer`** — Full-width footer with #f8f8f8 background, #555555 text in 12px Arial, and a 1px #e5e5e5 top border. Contains columns of links for categories, customer service, account management, and company information. Links use #337ab7 blue with #23527c hover state.

### Pagination
**`pagination`** — Page navigation with white background, #337ab7 blue text, 4px border-radius, and #e5e5e5 border. Active page uses #337ab7 background with white text. Disabled pages use #9d9d9d text with #ececec border. Used on product listing pages and search results.

### Panels
**`panel`** — Content container with white background, 4px border-radius, and #e5e5e5 border. Contains a `panel-heading` with #f5f5f5 background and 16px bold title, a `panel-body` with 16px padding, and an optional `panel-footer` with #f5f5f5 background. Used for "Recently Viewed", "Related Products", and "Customer Reviews" sections.

### Labels
**`label-tag`** — Small inline labels with 11px bold font, 2px border-radius, and 2px vertical / 6px horizontal padding. Six color variants: default (#9d9d9d), primary (#337ab7), success (#5cb85c), info (#5bc0de), warning (#f0ad4e), and danger (#d9534f). Used for condition tags (New, Used, Loose, Complete, New Sealed) and format indicators (Cartridge, Disc, Digital).

### Progress Bars
**`progress-bar`** — Horizontal progress indicator at 20px height with #f5f5f5 background and 4px border-radius. The fill uses `progress-bar-fill` with #337ab7 color and matching border-radius. Color variants include success (green), info (blue), warning (amber), and danger (red). Used for "Condition Rating" and "Stock Level" indicators.

### Modal
**`modal-dialog`** — Overlay dialog with white background, 12px border-radius, and a semi-transparent black backdrop (#080808 at 50% opacity). Contains a `modal-header` with 16px padding and a #e5e5e5 bottom border, a `modal-body` with 16px padding, and a `modal-footer` with 16px padding and a #e5e5e5 top border. Used for "Quick View", "Add to Cart Confirmation", and "Contact Us" forms.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Navigation collapses to hamburger menu; product cards stack in single column; tables convert to stacked layout; search bar becomes full-width; footer links stack vertically |
| Tablet | 768–992px | Navigation remains horizontal but dropdowns become click-to-open; product cards display in 2-column grid; tables remain horizontal but with reduced padding; sidebar content moves below main content |
| Desktop | 992–1200px | Full navigation with hover dropdowns; product cards in 3-column grid; tables at full width with all columns visible; sidebar remains in position |
| Wide | > 1200px | Maximum container width of 1170px; product cards in 4-column grid; additional whitespace around content; navigation remains unchanged |

### Touch Targets
- All buttons and links maintain minimum 34px height for touch interaction
- Navigation dropdowns require click (not hover) on touch devices
- Product card tap targets include the entire card area, not just the title
- Pagination links are minimum 34px × 34px for finger tapping
- Form inputs maintain 34px height for easy touch entry

### Collapsing Strategy
- Top navigation collapses to a hamburger icon at < 768px, revealing a vertical menu on tap
- Product filters sidebar collapses to a toggle button at < 768px, sliding in from the left
- Multi-column product grids reduce columns progressively: 4 → 3 → 2 → 1
- Table columns hide progressively: least important columns (Condition, SKU) hide first on tablet, remaining columns stack vertically on mobile
- Footer link columns stack vertically on mobile, with category headers acting as expandable accordion toggles
- Breadcrumb navigation truncates to show only the current page and "Home" on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily dominated by Bootstrap framework defaults (blues, grays, greens, reds, ambers). The brand's true primary identity color could not be isolated — #337ab7 is the most distinctive blue in the list and is used as the primary, but this may be Bootstrap's default rather than a brand choice. The brand may have a custom accent color not captured in the extraction.
- No custom font family was found beyond system fonts (Arial, Helvetica). The brand may use a custom typeface that wasn't loaded in the extracted CSS.
- Hover, active, and focus states for interactive elements are inferred from Bootstrap conventions rather than extracted from the live site.
- Error message styling, form validation patterns, and empty state designs could not be extracted.
- Dark mode support is not present in the extracted data.
- The checkout flow and payment form styling (Shopify Pay, Klarna, Afterpay widgets) were not captured.
- Mobile navigation patterns (hamburger menu animation, mobile menu overlay) are inferred from common Bootstrap patterns rather than extracted.
- The brand's logo and icon system (favicon, social media icons, payment method icons) could not be extracted.
- Loading states, skeleton screens, and transition animations are not documented.
- The brand's email template and print stylesheet designs are unknown.
- Accessibility patterns (focus outlines, skip navigation, ARIA labels) could not be verified from the extraction.
