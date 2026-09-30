---
version: alpha
name: "Mandarake"
source_url: "https://order.mandarake.co.jp/order/"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep red (#9e1d22) anchors Mandarake’s digital storefront like a vintage lacquer box, the brand’s primary voltage appearing on every add-to-cart button, price tag, and category badge. This is not a shy accent — it’s a declaration of the store’s specialty in rare collectibles, manga, and anime memorabilia, where urgency and authenticity matter. The secondary red (#d03b40) adds a slightly brighter pulse for hover states and active links, keeping the interface from feeling flat. Type runs Hiragino Kaku Gothic ProN with meiryo fallback, a pragmatic Japanese sans-serif stack that prioritizes legibility over fashion — no variable font, no experimental weight. The canvas is pure white (#ffffff), creating a high-contrast stage for product photography and the crimson brand marks. Navigation is dense and utilitarian: a top bar with category dropdowns, a persistent search field, and a cart counter that never leaves the viewport. Buttons are softly squared (`{rounded.xs}`), not pill-shaped, reinforcing a no-nonsense transaction feel. The overall mood is that of a well-organized auction house — red stamps, white paper, black ink — where the design steps back to let the inventory speak.

colors:
  primary: "#9e1d22"
  primary-active: "#d03b40"
  primary-disabled: "#e8b4b6"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  price-red: "#9e1d22"
  badge-new: "#d03b40"
  badge-sale: "#9e1d22"
  link-blue: "#0066cc"

typography:
  display-xl:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'メイリオ', meiryo, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    textTransform: uppercase

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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.1)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.price-red}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-condition:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  category-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.ink}"
    padding: "8px 12px"
  category-link-active:
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  cart-counter:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 4px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Confirm Order". Rendered in the brand's deep red (`{colors.primary}`) with white text and a subtle `{rounded.xs}` corner. On hover or active press, the background shifts to `{colors.primary-active}` for a brighter, more urgent state. The disabled variant fades to a soft pink (`{colors.primary-disabled}`), signaling the action is unavailable (e.g., out-of-stock items). All primary buttons maintain a consistent 40px height and 10px 20px padding for comfortable tap targets.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Add to Wishlist". Uses a white background with a 1px solid border in `{colors.primary}` and red text. On hover, the background tints to `{colors.surface-soft}` and the border shifts to `{colors.primary-active}`. This button sits alongside the primary in product cards and modals, offering a clear visual hierarchy without competing for attention.

**`button-tertiary-text`** — A text-only button for low-emphasis actions like "Cancel", "Clear Filters", or "See More". No background or border — just the `{colors.primary}` text on a transparent base. The active state darkens the text to `{colors.primary-active}`. Used sparingly in forms and filter panels to keep the interface clean.

### Cards
**`product-card`** — The core inventory display unit, used in grid and list views across search results, category pages, and related items. A white card with a `{rounded.xs}` corner containing a product image, title, condition label, and price. The price is always rendered in `{colors.price-red}` at `{typography.title-md}` weight, making it the most prominent text element on the card. The condition label uses `{typography.caption}` in `{colors.muted}`, sitting below the title. The card itself has no shadow or border — it relies on the white canvas and consistent spacing to create rhythm. On hover, a subtle `{colors.surface-soft}` background tint may be applied.

**`product-card-image`** — The image container within a product card. Uses `{rounded.xs}` to match the card's corner radius. Images are typically 1:1 or 4:3 aspect ratio, cropped to focus on the item. No border or overlay — the image is the hero element.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 60px tall with a white background and a 1px bottom border in `{colors.hairline}`. Contains the brand logo (left), category dropdown links (center), and utility icons — search, cart, account — (right). The sticky variant (`nav-bar-sticky`) gains a subtle box shadow on scroll to separate it from page content. Category links use `{typography.nav-link}` at 14px weight 600, with the active state colored `{colors.primary}`.

**`category-link`** — Individual navigation link within the top bar or sidebar category menus. Rendered as inline text with 8px 12px padding for touch-friendly spacing. The active state (`category-link-active`) switches text color to `{colors.primary}`, indicating the current section. No underline or background change — the color shift is the only indicator.

### Forms
**`text-input`** — Standard text input field for search, checkout forms, and account settings. A white background with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. On focus, the border switches to `{colors.primary}` for clear visual feedback. Error states use the same red border (`{colors.primary}`) with an optional error message below in `{colors.primary}` text. Height is 40px with 8px 12px padding for comfortable typing.

**`search-bar`** — The dedicated search input, visually distinct from standard text inputs by using a `{colors.surface-soft}` background. This subtle gray tint signals "search here" without needing a magnifying glass icon (though one may be present). On focus, the border shifts to `{colors.primary}` and the background returns to white. Height and padding match `text-input` for consistency.

### Badges
**`badge-new`** — A small, uppercase label used to flag newly listed items. Background is `{colors.badge-new}` (the brighter red), text is white, with `{rounded.xs}` corners and tight 2px 6px padding. Rendered at `{typography.badge}` (11px, weight 700) for maximum readability at small sizes. Typically positioned in the top-left corner of product card images.

**`badge-sale`** — Identical in structure to `badge-new` but using the deeper `{colors.badge-sale}` red. Used for discounted or sale items. The two badge colors create a subtle visual distinction: bright red for new, deep red for sale.

### Footer
**`footer`** — The site-wide footer, using a `{colors.surface-soft}` background to visually close the page. Contains columns of links (About, Help, Categories, Social), a copyright notice, and language/currency selectors. Text is `{colors.muted}` at `{typography.body-sm}`. Links (`footer-link`) inherit the muted color and shift to `{colors.primary}` on hover. Padding is generous at `{spacing.xl}` vertical and `{spacing.base}` horizontal.

### Cart
**`cart-counter`** — A small circular badge on the cart icon in the navigation bar. Background is `{colors.primary}` with white text, rendered at `{typography.caption}` size. The circle is `{rounded.full}` with a minimum 20px diameter and horizontal padding to accommodate double-digit counts. Positioned at the top-right corner of the cart icon.

### Breadcrumbs
**`breadcrumb`** — Navigation breadcrumbs for category and product pages. Uses `{typography.caption}` in `{colors.muted}` for all links, with the current page (`breadcrumb-active`) in `{colors.ink}`. Separators are typically ">" or "/" in `{colors.muted-soft}`. No background or border — just inline text.

### Pagination
**`pagination-button`** — Page number buttons at the bottom of search results and category listings. A white background with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. The active page (`pagination-button-active`) uses `{colors.primary}` background with white text and border. Disabled buttons (`pagination-button-disabled`) fade to `{colors.surface-soft}` background and `{colors.muted-soft}` text, indicating no further pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 items per row), nav bar collapses to hamburger menu, search bar moves below logo, footer stacks vertically, category links become a scrollable horizontal strip |
| Tablet | 744–1128px | Two-column product grid (3-4 items per row), nav bar shows limited category links with "More" dropdown, search bar remains in nav, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (4-5 items per row), full nav bar with all category links visible, search bar in nav, footer uses 3-4 column layout |
| Wide | > 1440px | Four-column product grid (5-6 items per row), max-width container (1440px) centered, nav bar expands to full width, footer uses 4-column layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 40px height for comfortable touch targets on mobile.
- Product card tap targets are the entire card surface, not just the title or price.
- Category links in the mobile horizontal strip have 12px horizontal padding for finger-friendly spacing.
- Cart counter badge is at least 20px diameter, with the cart icon itself being 40x40px.

### Collapsing Strategy
- On mobile (< 744px), the top nav bar collapses to a hamburger menu icon on the left, brand logo centered, and cart icon on the right.
- Category dropdowns become a full-screen overlay menu triggered by the hamburger icon.
- The search bar moves from the nav bar to a dedicated row below the logo, spanning full width.
- Footer columns stack vertically, with each section (About, Help, etc.) becoming an accordion that expands on tap.
- Product filters (on category pages) collapse into a "Filter" button that opens a bottom sheet or modal.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is minimal (only two reds and white). Additional brand-specific colors (e.g., secondary accents, success/error states, social media icons) could not be reliably determined from the live site extraction. The `link-blue` and `badge-new` colors are inferred from common e-commerce patterns, not confirmed from the site.
- Font weights beyond 400, 600, and 700 are speculative. The extracted font stack (`Hiragino Kaku Gothic ProN, meiryo, sans-serif, メイリオ`) does not include variable font declarations or specific weight ranges.
- Hover and focus states for most components (e.g., product cards, footer links, breadcrumbs) are inferred from common patterns, not extracted from the live site.
- Error styling for form inputs (e.g., validation messages, error icon placement) is not documented from the site.
- Dark mode or high-contrast mode variants are not available.
- The site may use additional interactive components (e.g., modals, tooltips, dropdown menus) that were not captured in the extraction.
- Spacing values (padding, margins, grid gaps) are estimated based on common e-commerce layouts, not extracted from CSS.
- The `rounded` scale is a standard system; the actual corner radii used on the site may differ slightly.
- No animation or transition timing data (e.g., hover fade duration, dropdown animation) was extracted.
