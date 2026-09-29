---
version: alpha
name: "Rugs USA"
source_url: "https://www.rugsusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Rugs USA is a value-driven home decor brand that makes style accessible through an extensive catalog of rugs at every price point. The brand's visual language is anchored on a clean white canvas (`#ffffff`) with a neutral ink (`#404040`) that carries body copy and headings, creating a calm, approachable foundation for product photography. The primary brand voltage is a confident blue (`#0051c3`) that appears in key CTAs, navigation elements, and promotional badges, supported by a secondary blue (`#2f7bbf`) and a lighter accent (`#62a1d8`) that add depth without competing for attention. A warm orange (`#f68b1f`) and its lighter variant (`#f9b169`) serve as energetic accent tones for sale badges and limited-time offers, while a restrained red (`#bd2426`) and its softer counterpart (`#de5052`) are reserved for clearance markers and error states. The palette is grounded by a range of grays — from the softest surface (`#ebebeb`) through mid-tones (`#999999`, `#bfbfbf`) to a deep charcoal (`#272727`) — that create hierarchy through subtle contrast rather than aggressive color blocking. Typography relies on a system font stack (`-apple-system, Arial, BlinkMacSystemFont, Helvetica Neue, Oxygen, Roboto, Segoe UI, Ubuntu`) that feels native and performant, with generous whitespace and soft corners (`{rounded.sm}` on cards, `{rounded.md}` on buttons) that keep the experience friendly and unpretentious. The brand trusts product imagery and clear pricing over decorative flourishes, resulting in a straightforward, shoppable interface that puts the rug — not the chrome — front and center.

colors:
  primary: "#0051c3"
  primary-active: "#2f7bbf"
  primary-disabled: "#62a1d8"
  ink: "#404040"
  body: "#595959"
  muted: "#999999"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#f68b1f"
  accent-sale-light: "#f9b169"
  accent-clearance: "#bd2426"
  accent-clearance-light: "#de5052"
  accent-green: "#9bca3e"
  accent-green-dark: "#516b1d"
  badge-new: "#bada7a"
  badge-sale: "#ee730a"
  star-rating: "#f68b1f"
  footer-bg: "#272727"
  footer-text: "#737373"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    padding: 12px 24px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-sale-active:
    backgroundColor: "{colors.accent-sale-light}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.accent-clearance}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.sm} 0"
  product-card-price:
    typography: "{typography.price-md}"
    color: "{colors.ink}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm}"
  product-card-price-sale:
    typography: "{typography.price-md}"
    color: "{colors.accent-clearance}"
  product-card-price-original:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    textDecoration: "line-through"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-clearance:
    backgroundColor: "{colors.accent-clearance}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-free-shipping:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: "400px"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  category-tile-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,81,195,0.1)"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    borderRight: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  filter-label:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    textTransform: "uppercase"
    letterSpacing: "0.5px"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm} 0 0 {rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "none"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "0 {rounded.sm} {rounded.sm} 0"
    padding: "12px 20px"
    height: 48px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  review-count:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    border: "1px solid {colors.hairline}"
    height: 44px
  size-selector-active:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-button:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "8px 12px"
    height: 44px
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"
    position: "sticky"
    bottom: "0"
  loading-spinner:
    color: "{colors.primary}"
    size: "24px"
  error-message:
    backgroundColor: "{colors.accent-clearance-light}"
    textColor: "{colors.accent-clearance}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  success-message:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.accent-green-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand blue (`#0051c3`) with white text. Used for "Add to Cart," "Shop Now," and primary navigation actions. On hover, shifts to `{colors.primary-active}` (`#2f7bbf`). Disabled state uses `{colors.primary-disabled}` (`#62a1d8`) with reduced opacity. All variants share `{rounded.sm}` (8px) and 48px height for consistent tap targets.

**`button-secondary`** — An outlined button with white fill, `{colors.ink}` text, and a 2px `{colors.hairline}` border. Used for "View Details," "Clear Filters," and secondary actions. Active state darkens the border to `{colors.ink}` and adds a light gray background. Maintains the same 48px height and `{rounded.sm}` as primary for visual consistency.

**`button-sale`** — A high-energy orange button (`#f68b1f`) reserved for sale promotions, clearance events, and limited-time offers. Uses white text and the same 48px height and `{rounded.sm}` as other buttons. Active state lightens to `{colors.accent-sale-light}` (`#f9b169`). This button should be used sparingly to maintain its urgency signal.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.sm}` and no padding at the container level. The image area occupies the top with a 1:1 aspect ratio and rounded top corners only. Title uses `{typography.title-sm}` in `{colors.ink}`, price uses `{typography.price-md}`. Sale prices render in `{colors.accent-clearance}` with the original price struck through in `{colors.muted}`. On hover, a subtle box shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card. Badges overlay the top-left corner of the image.

**`category-tile`** — A navigational card for browsing rug categories (e.g., "Living Room," "Outdoor," "Runner"). White background with a 1px `{colors.hairline-soft}` border and `{rounded.sm}`. On hover, the border shifts to `{colors.primary}` with a faint blue shadow. Contains a category image and title in `{typography.title-md}`.

### Navigation
**`nav-bar`** — The persistent top navigation bar at 64px height, white background with a subtle bottom border (`1px solid {colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — 14px, uppercase, 600 weight, with 0.5px letter spacing. Active links render in `{colors.primary}` with a 2px bottom border in the same blue. The bar contains the logo, category links, search icon, and cart icon.

**`breadcrumb`** — Secondary navigation showing the current page path (e.g., "Home > Rugs > Living Room > 5x8"). Uses `{typography.caption}` in `{colors.muted}` with the final active segment in `{colors.ink}`. Segments are separated by a ">" character in `{colors.muted-soft}`.

### Forms
**`text-input`** — Standard text input with white background, `{colors.ink}` text, 48px height, and `{rounded.sm}`. Default border is 1px `{colors.hairline}`. On focus, the border becomes 2px `{colors.primary}` with no outline. Error state uses a 2px `{colors.accent-clearance}` border.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) at 48px height with white background and 1px `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.primary}`. Contains a search icon on the left and optional clear button on the right.

**`size-selector`** — A dropdown-style selector for rug dimensions (e.g., 5'x8', 8'x10'). White background, 44px height, `{rounded.sm}`, with a 1px `{colors.hairline}` border. Active selection shows a 2px `{colors.primary}` border with light blue background.

### Badges
**`badge-sale`** — Orange badge (`#f68b1f`) with white text, `{rounded.xs}`, and uppercase 11px bold type. Used to flag percentage-off promotions. Positioned at the top-left of product card images.

**`badge-clearance`** — Red badge (`#bd2426`) with white text, same styling as sale badge. Used for clearance items with deeper discounts. Should not appear alongside `badge-sale` on the same product.

**`badge-new`** — Light green badge (`#bada7a`) with dark text (`{colors.ink}`). Used to flag newly added products. Same sizing and positioning as other badges.

**`badge-free-shipping`** — Green badge (`#9bca3e`) with white text. Used to highlight free shipping eligibility. Same styling as other badges.

### Footer
**`footer`** — A dark footer section with `{colors.footer-bg}` (`#272727`) background and `{colors.footer-text}` (`#737373`) body text. Contains multiple columns with headings in white (`{colors.canvas}`), uppercase, `{typography.title-sm}` with 0.5px letter spacing. Links are `{colors.footer-text}` and hover to white. Includes a newsletter signup form with an inline input and button combination.

**`newsletter-input`** and **`newsletter-button`** — An inline form combination where the input has `{rounded.sm}` on left corners only and the button has `{rounded.sm}` on right corners only, creating a seamless joined appearance. Both are 48px tall. The button uses `{colors.primary}` with white text.

### Feedback & Status
**`loading-spinner`** — A 24px circular spinner in `{colors.primary}`. Used during product loading, search, and add-to-cart operations. Centered within its container with no background.

**`error-message`** — A light red background (`#de5052` at ~20% opacity) with `{colors.accent-clearance}` text, `{rounded.sm}`, and 8px/16px padding. Used for form validation errors, API failures, and out-of-stock notifications.

**`success-message`** — A light green background (`#9bca3e` at ~20% opacity) with `{colors.accent-green-dark}` text, `{rounded.sm}`, and 8px/16px padding. Used for add-to-cart confirmations, newsletter signup success, and form submission confirmations.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), hamburger navigation, stacked filter panel as drawer, reduced hero height (250px), sticky add-to-cart bar at bottom, font sizes scale down one step |
| Tablet | 744–1128px | Two-column product grid, horizontal top nav with dropdowns, filter panel as sidebar (collapsible), hero at 350px, 3-4 footer columns |
| Desktop | 1128–1440px | Three-column product grid, full top nav, persistent filter sidebar, hero at 400px, 4-5 footer columns, max-width container |
| Wide | > 1440px | Four-column product grid, same nav and filter layout, hero at 450px with optional full-bleed imagery, max-width 1440px with centered content |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets extend to full card area
- Filter checkboxes have 24px minimum touch area
- Pagination buttons are minimum 40px x 40px
- Mobile nav hamburger icon is 44px x 44px
- Quantity selector buttons are 44px tall with 40px width

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Filter panel becomes a slide-in drawer on mobile, triggered by a "Filters" button
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack vertically below 744px
- Hero banner text overlay collapses to single column on mobile
- Breadcrumb truncates to "Home > ... > Current Page" on mobile
- Size selector becomes a full-width select dropdown on mobile
- Newsletter form stacks vertically below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom effect, color swatch reveal) could not be reliably extracted
- Error styling for specific form patterns (radio buttons, file uploads, multi-select) is undocumented
- Sub-brand or collection-specific palettes (e.g., "Rugs USA x Designer Collection") may exist but were not detected
- Dark mode or high-contrast mode styles are not present in the extracted data
- Animation timing and easing curves for transitions (card hover, modal open, drawer slide) are unknown
- Focus ring styles for keyboard navigation (outline color, offset, width) were not captured
- Loading skeleton patterns for product grids and search results are not defined
- Print stylesheet behavior is undocumented
- Internationalization text overflow handling for non-English languages is unknown
- Third-party widget styling (reviews, payment icons, social share) may deviate from system tokens
- Specific modal/dialog component styling (overlay opacity, close button placement, animation) is not captured
- Tooltip and popover component specifications are missing
- Accordion and tab component interaction states are not defined
- Video player styling and controls are undocumented
- Cookie consent banner styling is not captured
