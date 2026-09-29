---
version: alpha
name: "AmiAmi"
source_url: "https://www.amiami.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dense, information-rich import marketplace where the primary voltage is a cool, trustworthy blue (#2f7bbf) — not a warm brand color but a functional one, used for the search bar, the "Add to Cart" button, and the category navigation strip, signaling reliability rather than emotion. The canvas is a pale gray (#ebebeb) rather than pure white, giving the page a slightly aged, utilitarian feel like a well-thumbed catalog. Red accents (#bd2426) appear on sale badges and price reductions, creating a clear urgency signal against the gray field. The typography stack is system-native (-apple-system, Arial, BlinkMacSystemFont, Helvetica Neue, Oxygen, Roboto, Segoe UI, Ubuntu) — no custom typeface, which reinforces the no-frills, function-over-form ethos of a shop that prioritizes inventory breadth over brand polish. Product cards sit on a white surface (#ffffff) with a soft gray hairline (#dedede), and the footer collapses into a dense grid of links in muted gray (#737373). The overall mood is that of a busy, reliable warehouse — every pixel is justified by utility, not aesthetics.

colors:
  primary: "#2f7bbf"
  primary-active: "#1a5c99"
  primary-disabled: "#a3c4e0"
  ink: "#272727"
  body: "#404040"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ebebeb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-red: "#bd2426"
  sale-red-active: "#8a1b1c"
  stock-green: "#9bca3e"
  stock-green-active: "#7aa82e"
  preorder-orange: "#f68b1f"
  preorder-orange-active: "#c16508"
  badge-new: "#62a1d8"
  badge-limited: "#de5052"
  link-blue: "#0051c3"
  footer-bg: "#163959"
  footer-text: "#bada7a"

typography:
  display-xl:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, Arial, BlinkMacSystemFont, 'Helvetica Neue', Oxygen, Roboto, 'Segoe UI', Ubuntu, sans-serif"
    fontSize: 10px
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
    padding: 10px 20px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 36px
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
  button-sale-active:
    backgroundColor: "{colors.sale-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-preorder:
    backgroundColor: "{colors.preorder-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 40px
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    height: 40px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.sale-red}"
    fontWeight: 700
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-preorder:
    backgroundColor: "{colors.preorder-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  category-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 40px
  category-nav-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  pagination:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
    fontWeight: 600

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Search", and "Proceed to Checkout". Rendered in the brand blue ({colors.primary}) with white text and a subtle 4px radius. On hover, shifts to a darker shade ({colors.primary-active}). Disabled state uses a pale blue ({colors.primary-disabled}) to indicate non-interactivity. Height is compact at 36px, reflecting the dense, information-heavy layout.

**`button-secondary`** — Used for less prominent actions like "View Details" or "Cancel". White background with a 1px hairline border ({colors.hairline}) and dark text ({colors.ink}). Hover state adds a subtle shadow or border darkening. Same compact 36px height as primary.

**`button-sale`** — A red variant ({colors.sale-red}) used exclusively for sale-priced items or clearance promotions. Active state darkens to {colors.sale-red-active}. Shares the same dimensions and typography as `button-primary`.

**`button-preorder`** — An orange variant ({colors.preorder-orange}) for pre-order items. Active state uses {colors.preorder-orange-active}. Used sparingly to differentiate pre-order from in-stock inventory.

### Badges
**`badge-sale`** — A small, uppercase red badge ({colors.sale-red}) applied to product cards and list items to indicate a discounted price. Compact padding (2px 6px) and 10px bold type ensure it fits within the dense card layout without overwhelming the product image.

**`badge-new`** — Blue badge ({colors.badge-new}) for newly arrived items. Same dimensions and typography as `badge-sale`. Used to draw attention to fresh inventory.

**`badge-limited`** — Red badge ({colors.badge-limited}) for limited-edition or scarce items. Slightly more saturated than the sale red to differentiate urgency types.

**`badge-preorder`** — Orange badge ({colors.preorder-orange}) for items available for pre-order. Matches the preorder button color for visual consistency.

**`badge-stock`** — Green badge ({colors.stock-green}) for items with low stock warnings or "in stock" indicators. Uses the brand's green accent from the extracted palette.

### Cards
**`product-card`** — The core inventory display unit. A white card ({colors.surface-card}) with a soft 4px radius and a 1px hairline border ({colors.hairline}). Contains a product image (with matching 4px radius), a title in 14px semibold, and a price in 14px regular. Sale prices render in red ({colors.sale-red}) with bold weight. Cards stack in a responsive grid with 8px gaps. On hover, a subtle shadow or border highlight indicates interactivity.

**`product-card-sale-price`** — Overrides the standard price token when a discount is active. Uses red color and bold weight to emphasize savings.

### Navigation
**`nav-bar`** — The top-level navigation bar, 48px tall, white background ({colors.surface-card}), with dark text ({colors.ink}). Contains category links (Figures, Model Kits, etc.) in 13px semibold. Active or hovered categories may use an underline or a subtle background change. The bar is fixed or sticky on desktop, collapsing to a hamburger menu on mobile.

**`category-nav`** — A secondary navigation strip below the main nav, 40px tall, used for sub-categories (e.g., "Pre-Order", "Sale", "New Arrivals"). Active category uses the brand blue background ({colors.primary}) with white text, rendered as a pill or tab. Inactive categories are muted gray ({colors.muted}) on white.

**`nav-dropdown`** — A dropdown panel triggered by hovering over a nav item. White background with a subtle shadow, containing links in 13px regular. Items have 8px vertical padding for touch targets.

### Forms
**`text-input`** — Standard text input for search filters, login forms, and checkout. White background, 36px height, 8px horizontal padding, and a 1px hairline border. Focus state uses the brand blue border ({colors.primary}) for clear indication.

**`search-bar`** — The primary search input, slightly larger than standard inputs at 40px height with 16px horizontal padding. Has a 8px radius and sits within a white container. The search submit button is a blue square ({colors.primary}) with a magnifying glass icon, matching the 40px height and 8px radius.

### Footer
**`footer`** — A dark blue footer ({colors.footer-bg}) with light green text ({colors.footer-text}) for links. Contains multiple columns of links (About Us, Customer Service, etc.) with white headings ({colors.on-primary}). Links are 13px regular with hover underlines. The footer is dense and information-rich, mirroring the overall site density.

### Pagination
**`pagination`** — Page number buttons at the bottom of search results and category pages. White background with dark text, 4px radius. The active page uses the brand blue background ({colors.primary}) with white text. Compact sizing to fit within the dense layout.

**`breadcrumb`** — Navigation breadcrumbs in 11px regular gray ({colors.muted}). The current page is rendered in dark text ({colors.ink}) with semibold weight. Separators are simple ">" characters in muted gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar becomes full-width; badges stack vertically; footer columns collapse to single column |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but condensed; search bar is 60% width; footer in 2 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; search bar in top-right; footer in 4 columns |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements: minimum 36px height (meets WCAG touch target recommendations)
- Nav links: minimum 40px tap area (padding extends hit area)
- Product cards: entire card is tappable, linking to product detail page
- Search bar: 40px height with clear visual affordance
- Pagination buttons: 32px minimum tap target

### Collapsing Strategy
- Main navigation collapses to hamburger menu below 744px
- Category navigation strip collapses to a dropdown selector below 744px
- Product grid reduces columns as viewport shrinks (4 → 3 → 2 → 1)
- Footer columns collapse from 4 to 2 to 1 as viewport narrows
- Badges on product cards stack vertically on mobile to prevent text overflow
- Search bar expands to full width on mobile, pushing other elements below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While active and disabled states are defined for primary buttons, hover states for secondary buttons, text inputs, and navigation items could not be reliably extracted from the static HTML/CSS. Assumed standard patterns (border darkening, subtle shadow) are used.
- **Error states**: Form validation styling (error borders, error messages) was not present in the extracted data. Standard red (#bd2426) borders with error text in the same color are assumed.
- **Dark mode**: No dark mode tokens were found. The site appears to be light-mode only.
- **Sub-brand palettes**: AmiAmi may have seasonal or category-specific color schemes (e.g., holiday promotions, anime series-specific themes) that were not captured.
- **Typography weights**: The extracted font stack is system-native with no custom weights specified. The 400, 600, and 700 weights used are assumptions based on common system font availability.
- **Animation/transition**: No transition durations or easing curves were extractable. Standard 200-300ms ease-in-out transitions are assumed for hover and focus states.
- **Spacing scale**: The spacing tokens are inferred from common e-commerce patterns and may not exactly match the live site's grid. The extracted data did not include explicit spacing values.
- **Checkout flow**: Checkout-specific components (payment forms, address fields, order summary) were not extractable from the initial page load. These may use different styling.
- **The extracted color list includes many grays and blues, which is typical for a functional e-commerce site. The primary blue (#2f7bbf) was chosen as the most distinctive non-gray color that appears in navigation and CTAs. The red (#bd2426) and green (#9bca3e) accents are used for sale and stock indicators respectively. The orange (#f68b1f) is used for pre-order badges. These assignments are based on common e-commerce conventions rather than extracted usage data.
