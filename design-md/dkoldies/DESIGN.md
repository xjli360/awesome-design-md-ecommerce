---
version: alpha
name: "DKOldies"
source_url: "https://www.dkoldies.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A retro game retailer that wears its primary red #e03e2d like a neon sign above an arcade cabinet — the same voltage that fills every "Add to Cart" button, sale badge, and category header, set against a deep purple-black #221155 that reads as a CRT screen after the power cuts off. The brand pairs Press Start 2P (a pixel-perfect bitmap font for display headlines) with Roboto for body copy, creating a deliberate friction: the chunky 8-bit nostalgia of the former versus the clean, utilitarian readability of the latter. Product cards sit on a white canvas with soft `{rounded.sm}` corners, but the real visual punch comes from the green #28a300 — used for "In Stock" badges and price drops — which against the purple backdrop feels like a power-up mushroom appearing in a dark dungeon. The top navigation bar is a solid band of #221155 with white text, and the search bar echoes the same purple fill with a white placeholder, making the entire header feel like a game console's dashboard. Buttons are squat and chunky (48px tall, `{rounded.sm}`), and the primary CTA's red-on-white contrast is aggressive enough to survive any CRT scanline. The overall mood is less "curated nostalgia" and more "the back room of a 90s rental store that still smells like cardboard and victory."

colors:
  primary: "#e03e2d"
  primary-active: "#c23426"
  primary-disabled: "#f5a098"
  ink: "#221155"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  stock-green: "#28a300"
  stock-green-active: "#1f7d00"
  sale-badge-bg: "#e03e2d"
  sale-badge-text: "#ffffff"
  price-drop: "#28a300"
  nav-bg: "#221155"
  nav-text: "#ffffff"
  search-bg: "#221155"
  search-text: "#ffffff"
  search-placeholder: "#b0a0c0"
  footer-bg: "#221155"
  footer-text: "#d0c0e0"

typography:
  display-xl:
    fontFamily: "'Press Start 2P', 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  display-lg:
    fontFamily: "'Press Start 2P', 'Courier New', monospace"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  display-md:
    fontFamily: "'Press Start 2P', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-display-sm:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  product-name:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-stock-green:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-stock-green-active:
    backgroundColor: "{colors.stock-green-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-default:
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  search-bar:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.search-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    placeholderColor: "{colors.search-placeholder}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(34, 17, 85, 0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-name:
    typography: "{typography.product-name}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-display}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-display}"
    color: "{colors.price-drop}"
  product-card-original-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    textDecoration: "line-through"
  badge-sale:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-in-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
    padding: "4px 0"
  category-link-hover:
    textColor: "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
    padding: "4px 0"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: "300px"
  hero-headline:
    typography: "{typography.display-lg}"
    color: "{colors.on-primary}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.search-placeholder}"
    marginTop: "{spacing.md}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    color: "{colors.body}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
    height: 36px

## Components

### Buttons
**`button-primary`** — The main call-to-action, filled with the brand red #e03e2d and white text. On hover, it darkens to #c23426. Disabled state uses a washed-out pink #f5a098. All primary buttons are 48px tall with `{rounded.sm}` corners and bold Roboto at 16px with 0.5px letter spacing for a chunky, confident feel.
**`button-secondary`** — An outlined variant with a 2px solid #221155 border on a white background. Used for "View Details" or "Cancel" actions alongside primary buttons. Hover fills the background with `{colors.surface-soft}`.
**`button-stock-green`** — A compact 36px-tall button using #28a300 for "Add to Cart" on in-stock items or "Notify Me" for out-of-stock variants. Its smaller size and green fill signal a secondary but positive action.

### Cards
**`product-card`** — A white card with a 1px soft hairline border and `{rounded.sm}` corners. Contains a square aspect-ratio image with `{rounded.xs}`, the product name in 15px medium Roboto, and the price in 22px bold Roboto. Sale prices render in #28a300 with the original price struck through in muted gray. On hover, the border darkens and a subtle box shadow appears.

### Navigation
**`nav-bar`** — A 64px-tall solid band of #221155 with white Roboto nav links at 14px/500 weight. The active link uses the brand red #e03e2d. The search bar embedded in the nav uses the same purple background with white text and a lighter purple placeholder.
**`breadcrumb`** — A simple row of 13px Roboto links in muted gray, with the current page in dark body text. No background, just inline text with `{spacing.sm}` vertical padding.

### Forms
**`text-input`** — A standard white input with a 1px hairline border and `{rounded.sm}`. On focus, the border becomes a 2px solid #e03e2d. Used for search, checkout fields, and newsletter signups.

### Badges
**`badge-sale`** — A small uppercase label in bold 11px Roboto on a red #e03e2d background with white text and `{rounded.xs}`. Applied to product cards to indicate discounts.
**`badge-in-stock`** — Same shape but filled with #28a300 green. Used on product detail pages and cards to indicate availability.
**`badge-out-of-stock`** — Uses muted gray #999999 for unavailable items.

### Footer
**`footer-section`** — A full-width band of #221155 with light purple #d0c0e0 text. Links are 14px Roboto at 400 weight, turning red on hover. The section has generous `{spacing.xxl}` vertical padding.

### Hero
**`hero-banner`** — A large promotional area with a #221155 background, white text, and a minimum height of 300px. The headline uses Press Start 2P at 22px, with a subheadline in 16px Roboto in a lighter purple. Used for seasonal sales or featured collections.

### Pagination
**`pagination-button`** — A small square button with a 1px hairline border and `{rounded.xs}`. The active page uses the brand red fill, while inactive pages remain white with dark text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards go single-column; hero banner reduces to 200px min-height; search bar moves below nav; footer links stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards display in 2-column grid; hero banner at 250px min-height; search bar remains in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero banner at 300px min-height; search bar prominent in nav |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4- or 5-column grid; hero banner expands to 350px min-height with larger headline |

### Touch Targets
- All buttons and links maintain a minimum 44px touch target height
- Nav links have 12px horizontal padding for easy tapping
- Quantity selector buttons are 36px tall with 8px padding
- Pagination buttons are at least 36px × 36px

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px
- Product card grid reduces columns: 4 → 2 → 1
- Footer link columns stack vertically on mobile
- Hero banner text reduces in size and padding on mobile
- Search bar moves from inline nav to a full-width row below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns, not extracted from the live site
- Error styling for form inputs (validation, error messages) was not observed
- The exact font sizes and weights for Press Start 2P usage are estimated — the site may use it at different scales
- Spacing values for product card grids and layout gutters are assumed based on common e-commerce patterns
- The site's color palette may include additional accent colors for categories or promotions not captured in the extraction
- Dark mode or high-contrast mode styles are not defined
- The exact border radius for product card images (`{rounded.xs}`) is an estimate
- Dropdown menus and mega-menu styles for the nav were not observed
- The site may use additional font weights for Roboto (e.g., 300 for light text) that were not captured
- Checkout flow styling (cart page, payment forms) was not extracted
- The brand may use a secondary purple shade beyond #221155 for hover states or gradients
