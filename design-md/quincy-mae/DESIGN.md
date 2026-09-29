---
version: alpha
name: "Quincy Mae"
source_url: "https://quincymae.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A baby-clothing brand that uses a single warm charcoal (#313131) as its entire color story — no pastel pinks, no mint greens, no nursery-soft blues. The extracted palette is a monochrome reduction: one dark neutral applied to every headline, button, link, and product title against a pure white canvas. This is a deliberate editorial choice — the clothes are the color, not the interface. Product photography of swaddles, rompers, and sleep sacks in muted earth tones (oatmeal, sage, clay) does all the emotional work; the UI steps back into near-invisibility. Type runs the system stack at modest sizes — body copy at 14px, display at 24px — with no custom font declaration found, suggesting the brand trusts legibility over personality. Buttons are compact at 40px height with {rounded.sm} corners, never pill-shaped, never oversized. The overall effect is a quiet, restrained storefront that feels more like a minimalist Japanese boutique than a typical baby brand. There are no badges, no sale banners, no urgency patterns — just product, description, and the single charcoal thread holding it together.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
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
    padding: 10px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary-active}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 0
    height: auto
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.price}"
    textColor: "{colors.error}"
  product-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-detail-price:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
  product-detail-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  loading-spinner:
    border: "2px solid {colors.hairline-soft}"
    borderTop: "2px solid {colors.primary}"
    size: 24px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The single call-to-action style across the site. A compact 40px button filled with {colors.primary} (#313131) and white text, using {typography.button-md} at 14px with 0.5px letter-spacing. Corners are a subtle {rounded.sm} (4px). On hover/active, the background deepens to {colors.primary-active} (#1a1a1a). Disabled state uses {colors.primary-disabled} (#a0a0a0) with no border change. Used for "Add to Cart," "Checkout," and newsletter submission.

**`button-secondary`** — An outlined variant with a 1px solid {colors.primary} border on a white background. Same 40px height and {rounded.sm} corners. Active state darkens the border to {colors.primary-active} and adds a {colors.surface-soft} background. Used for "View Details" and secondary checkout actions.

**`button-text`** — A borderless, backgroundless text button using {colors.primary} and {typography.button-md}. No padding on sides, height auto. Used for "Read More" links and cancel actions within forms.

### Navigation
**`nav-bar`** — A 60px white bar with uppercase nav links in {typography.nav-link} (13px, 500 weight, 0.5px letter-spacing). Active links use {colors.primary}, inactive links use {colors.muted}. The bar is fixed or sticky at the top with a 1px {colors.hairline-soft} bottom border. The logo sits left-aligned, navigation links center or right-aligned, with a cart icon on the far right.

**`nav-link-active`** and **`nav-link-inactive`** — Define the two states for top-level navigation items. No background, no rounding — purely text-based differentiation.

### Product Cards
**`product-card`** — A minimal product display with no rounding, no shadow, no border. The image fills the card width, the title uses {typography.title-sm} (14px, 500 weight) in {colors.ink}, and the price uses {typography.price} (14px, 400 weight) in {colors.body}. Sale prices render in {colors.error}. On hover, the image may scale subtly (1.02x) but no card-level interaction.

**`product-card-title`** and **`product-card-price`** — Token references for the text elements within a product card. No background, no rounding.

### Forms
**`text-input`** — A 40px input with {rounded.sm} corners, a 1px {colors.hairline} border, and {typography.body-sm} (14px). Focus state swaps the border to {colors.primary}. Error state uses {colors.error} border. Padding is 10px vertical, 12px horizontal.

**`select-input`** — Same dimensions and styling as `text-input`, used for dropdown selectors (size, quantity, country).

**`quantity-selector`** — A compact input for product quantities, 40px height with a 1px {colors.hairline} border and {rounded.sm} corners. Used alongside the "Add to Cart" button.

### Footer
**`footer-section`** — A full-width section with {colors.surface-soft} background, 48px vertical padding. Contains column headings in {typography.title-sm} and links in {typography.link} at {colors.muted}. A newsletter signup sits in one column with `newsletter-input` and `newsletter-submit` components.

**`footer-heading`** and **`footer-link`** — Token references for footer typography. Headings are 14px/500 weight in {colors.ink}; links are 14px/400 weight in {colors.muted}.

### Product Detail
**`product-detail-title`** — The product name on the detail page, using {typography.display-md} (20px, 400 weight) in {colors.ink}. No background, no rounding.

**`product-detail-price`** — The price on the detail page, using {typography.title-md} (16px, 500 weight) in {colors.body}.

**`product-detail-description`** — The product description block, using {typography.body-sm} (14px, 400 weight) in {colors.body} with 1.6 line-height.

### Accordion
**`accordion-item`** — A clickable row with a 1px {colors.hairline-soft} bottom border, 16px vertical padding, and {typography.title-sm}. Used for "Details," "Care Instructions," and "Shipping" sections on product detail pages.

**`accordion-content`** — The expandable content area below an accordion item, using {typography.body-sm} in {colors.body} with 16px bottom padding.

### Utility
**`breadcrumb-link`** and **`breadcrumb-current`** — Breadcrumb navigation using {typography.caption} (12px, 400 weight). Links are {colors.muted}, current page is {colors.ink}.

**`loading-spinner`** — A 24px circular spinner with a 2px {colors.hairline-soft} border and a 2px {colors.primary} top border. Used during product loading and cart updates.

**`divider`** — A 1px horizontal rule in {colors.hairline-soft}. Used between sections and product details.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), nav-bar collapses to hamburger menu, product images stack vertically on detail page, footer columns stack, padding reduces to 16px on sides |
| Tablet | 744–1128px | Two-column product grid, nav-bar shows limited links (4-5), product detail page shows image left and details right, footer shows 2-3 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav-bar with all links visible, product detail page has large hero image with thumbnails below, footer shows 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, product detail page has expanded image area, footer shows 4 columns with newsletter |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 40px height
- Nav-bar links have 44px minimum tap area on mobile
- Product card images are tappable with no minimum size requirement (image fills card width)
- Quantity selector buttons are 40px × 40px minimum
- Accordion items have 44px minimum tap area

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer
- Product filters (if present) collapse into a "Filter" button that opens a modal or drawer
- Footer columns collapse into a single column with accordion-style section toggles
- Product description accordions remain collapsed by default on all breakpoints
- Secondary navigation (utility links like "Search," "Account") collapses into the hamburger menu on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site — the full palette (secondary, accent, error, success, etc.) is inferred from common e-commerce patterns and may not match the actual brand
- No custom font-family was found — the system font stack is used throughout; the brand may use a custom font that wasn't loaded in the extracted sample
- Hover and active states for buttons and links are inferred from common darkening patterns (primary-active: #1a1a1a) and may not reflect actual brand values
- Error and success colors (#d32f2f, #2e7d32) are Material Design defaults and likely not brand-specific
- No border-radius values were extracted — all rounding tokens are estimated based on typical e-commerce patterns
- No spacing values were extracted — all spacing tokens are standard 4px/8px increments
- No shadow or elevation values were found — product cards and modals may use shadows that weren't captured
- No typography scale beyond the system stack was found — font sizes are estimated based on common e-commerce ranges
- No data on mobile navigation patterns (hamburger menu behavior, drawer width, animation)
- No data on form validation styling (error messages, success states, tooltips)
- No data on modal or overlay styling (backdrop color, animation, close button)
- No data on image aspect ratios for product cards or detail pages
- No data on sale badge or "sold out" overlay styling
- No data on color swatch or size selector styling
- No data on cart drawer or mini-cart styling
- No data on search overlay or search results styling
- No data on announcement bar or promotional banner styling
- No data on loading states beyond the spinner (skeleton screens, shimmer effects)
- No data on dark mode or high-contrast mode support
- No data on print stylesheet behavior
