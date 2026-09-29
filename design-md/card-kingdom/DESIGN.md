---
version: alpha
name: "Card Kingdom"
source_url: "https://www.cardkingdom.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep charcoal #313131 anchors Card Kingdom’s interface — not as an accent but as the primary text color, the nav background, the footer fill, and the default button state, giving the entire marketplace the weight of a well-worn binder of Magic: The Gathering cards. The brand operates in a deliberately narrow value range: near-black ink on a white canvas, with no secondary brand color visible in the extracted palette, forcing every UI decision through contrast and typographic hierarchy rather than chromatic variety. Product photography — glossy foil cards, matte sleeves, sealed booster boxes — supplies the only color, and the layout trusts those images to carry emotional load. Buttons are compact and rectangular (`{rounded.sm}`), not pill-shaped; the search bar sits as a full-width field rather than an orb, suggesting a catalog-driven experience where precision matters over discovery. The type stack defaults to system fonts (San Francisco on Apple, Roboto on Android, Arial fallback), a pragmatic choice that prioritizes legibility at small sizes — card names, set symbols, and price tags are the real content, not brand typography. Navigation is dense: a top bar with account, cart, and search, plus a category mega-menu beneath it, all in the same `{colors.ink}` on `{colors.canvas}`. The site reads as a tool for collectors who know exactly what they want — search first, filter second, browse third — and the design gets out of the way.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#8c8c8c"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6e6e6e"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#2e7d32"
  error: "#c62828"
  warning: "#f9a825"
  foil-gold: "#c9a84c"
  stock-badge: "#1565c0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: 10px 20px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-add-to-cart-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 9px 11px
  text-input-error:
    border: "1px solid {colors.error}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    padding: 9px 15px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  top-nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  top-nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
  category-nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  category-nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.primary}"
  product-card-condition:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-stock:
    backgroundColor: "{colors.stock-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-foil:
    backgroundColor: "{colors.foil-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.price-lg}"
    textColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary action button across the site, used for "Add to Cart", "Checkout", and "Sign In". Renders as a solid `{colors.primary}` rectangle with white text, compact at 40px height with `{rounded.sm}` corners. On hover/active, shifts to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#8c8c8c) with white text, signaling the button is non-interactive without removing it from layout flow.

**`button-secondary`** — Used for "Cancel", "Clear Filters", and secondary checkout actions. A white button with a `{colors.hairline}` border and `{colors.primary}` text. On active, the border thickens to `{colors.primary}` and the background shifts to `{colors.surface-soft}`. Height matches `button-primary` at 40px for alignment in forms.

**`button-ghost`** — A text-only button with no background or border, used for inline actions like "Remove" in cart items or "View All" in category strips. On hover/active, gains a `{colors.surface-soft}` background. Padding is tighter at 10px 16px to keep the text close to adjacent content.

**`button-add-to-cart`** — The primary purchase CTA, slightly taller at 44px with 12px 24px padding for visual weight on product detail pages. Uses the same `{colors.primary}` / `{colors.primary-active}` state pattern but with more generous tap area.

### Text Inputs
**`text-input`** — Standard form input for checkout fields (name, address, payment). White background, `{colors.ink}` text, `{rounded.sm}` corners, and a `{colors.hairline}` border. On focus, the border doubles to 2px `{colors.primary}` and padding adjusts by 1px to prevent layout shift. Error state swaps the border to `{colors.error}` (#c62828). Height is 40px to match button heights.

**`search-input`** — The primary search field, slightly taller at 44px with a `{colors.surface-soft}` background and `{rounded.md}` corners — the only component with medium rounding, distinguishing it from form inputs. On focus, background returns to white and border becomes 2px `{colors.primary}`. This is the most important interaction on the site; the visual treatment signals that search is a distinct, elevated action.

### Navigation
**`top-nav`** — A 48px dark bar (`{colors.primary}` background) spanning the full viewport width. Contains account links, cart icon with badge count, and a search toggle. Links render in white with `{typography.nav-link}` (14px/600 weight). Active page indicator is a 2px white underline.

**`category-nav`** — A 44px white bar directly below the top nav, separated by a `{colors.hairline}` border. Contains game/category links (Magic: The Gathering, Pokémon, Yu-Gi-Oh!, etc.) in `{colors.ink}`. Active category gets a 2px `{colors.primary}` underline. This nav is horizontally scrollable on mobile.

### Product Cards
**`product-card`** — The core content unit for search results and category listings. A white card with `{rounded.sm}` corners and a `{colors.hairline-soft}` border. On hover, the border darkens to `{colors.hairline}` and a subtle shadow appears (0 2px 8px rgba(0,0,0,0.08)). The card image has top-only rounding (`{rounded.sm} {rounded.sm} 0 0`). Below the image: card title in `{typography.title-sm}`, condition in `{typography.caption}` (`{colors.muted}`), and price in `{typography.price-md}` (`{colors.primary}`).

### Badges
**`badge-stock`** — Blue badge (#1565c0) for "In Stock" indicators. Uppercase 11px/700 weight text, `{rounded.xs}` corners, 2px 6px padding. Appears on product cards and detail pages.

**`badge-foil`** — Gold badge (#c9a84c) for foil/rare card variants. Dark text on gold background, same sizing as stock badge. Used to differentiate premium card treatments in listings.

**`badge-sale`** — Red badge (#c62828) for sale/discount items. White text, same sizing. Appears on product cards with reduced prices.

### Filters & Pagination
**`filter-panel`** — Sidebar filter container on search/category pages. White background, `{rounded.sm}`, `{colors.hairline-soft}` border. Contains checkboxes for condition, set, price range, and rarity. Checkboxes use `{rounded.xs}` with `{colors.hairline}` border; checked state fills with `{colors.primary}`.

**`pagination-button`** — Page number buttons at the bottom of search results. 32px height, `{rounded.sm}`, `{colors.hairline}` border. Active page uses `{colors.primary}` fill with white text. Disabled buttons (for first/last page boundaries) use `{colors.surface-soft}` background with `{colors.muted-soft}` text.

### Footer
**`footer`** — Full-width dark footer matching the top nav in `{colors.primary}`. Contains link columns (About, Help, Policies, Social) with white text at 85% opacity, increasing to 100% on hover. Padding is generous at 48px vertical, 64px horizontal. Links use `{typography.link}` (14px/400 weight) for readability against the dark background.

### Cart Components
**`quantity-selector`** — A compact 36px control for adjusting item quantities in the cart. White background, `{colors.hairline}` border, `{rounded.sm}`. Contains a decrement button, the quantity value, and an increment button. Buttons use `{colors.surface-soft}` background.

**`cart-item`** — Individual line item in the shopping cart. White background, bottom border of `{colors.hairline-soft}`. Contains product image, name, condition, quantity selector, and price. Prices use `{typography.price-md}`.

**`cart-total`** — The order subtotal/total display. Uses `{typography.price-lg}` (20px/700 weight) in `{colors.primary}` to emphasize the final cost.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 cards), hamburger menu replaces top nav links, category nav becomes horizontally scrollable, filter panel collapses to a bottom sheet or modal, search input becomes full-width below nav, product card images stack vertically, footer links collapse to accordion |
| Tablet | 744–1128px | Two-column product grid (3-4 cards), top nav shows limited links (Account, Cart), category nav remains visible with horizontal scroll, filter panel slides in from left as overlay, search input is full-width in nav |
| Desktop | 1128–1440px | Three-column product grid (4-5 cards), full top nav with all links, category nav shows all top-level categories, filter panel is persistent sidebar, search input is inline in top nav |
| Wide | > 1440px | Four-column product grid (5-6 cards), max-width container (1440px) centered, filter panel remains sidebar, search input expands to accommodate longer queries, product cards may show additional metadata (set symbol, artist) |

### Touch Targets
- All buttons and links: minimum 44x44px tap area on mobile
- Quantity selector buttons: 44x44px minimum (wrapped in 36px visible button with 4px padding)
- Category nav links: 44px height with 16px horizontal padding
- Filter checkboxes: 44x44px tap area (checkbox itself is 20x20px with 12px padding)
- Pagination buttons: 44x44px minimum (visible button is 32px with 6px padding)
- Cart item remove link: 44x44px minimum tap area

### Collapsing Strategy
- Top nav account links collapse into hamburger menu on mobile (< 744px)
- Category nav collapses to a "Browse Categories" dropdown or horizontal scroll on mobile
- Filter panel collapses to a "Filters" button that opens a bottom sheet on mobile and tablet
- Product card image and details stack vertically on mobile (image full-width, details below)
- Footer link columns collapse to accordion sections on mobile
- Search input collapses to an icon button on mobile, expanding to full-width on tap
- Cart summary collapses to a sticky bottom bar on mobile with total and checkout button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one extracted hex color (#313131) was available from the live site — the full palette above is inferred from common trading card marketplace patterns and the single extracted value. The brand may use additional accent colors (e.g., a specific green for "In Stock", red for "Sold Out", gold for foil variants) that could not be verified.
- No secondary brand color was extracted — the site may use a specific accent color for promotions, sales, or category highlights that wasn't captured.
- Hover and active states for all components are estimated based on common darkening patterns (10-15% darker for active, 50-60% opacity for disabled). Actual brand hover colors may differ.
- Error state styling (form validation, out-of-stock messaging, payment failures) could not be extracted — colors and iconography are inferred.
- Font sizes and weights are estimated from the system font stack and common e-commerce patterns. The actual site may use different sizes for headings, body text, and buttons.
- Rounded corner values are estimated from typical trading card site patterns. Actual border-radius values may differ.
- Spacing values (padding, margins, gaps) are estimated from common grid systems. Actual spacing may use different increments.
- Dark mode styling is not present in the extracted data — the site may or may not support it.
- Animation and transition durations/easings could not be extracted.
- Iconography style (custom vs. system icons, stroke weights, sizes) could not be determined.
- The "Just a moment..." page title suggests the site may use Cloudflare or similar protection, which could affect initial page load styling.
