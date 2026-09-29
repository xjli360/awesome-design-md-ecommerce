---
version: alpha
name: "Primary"
source_url: "https://primary.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A children's clothing brand that uses near-neutral gray (#dedede) and near-black (#121212) as its primary palette — a deliberately muted choice for a category that usually screams with primary-bright rainbows. The brand trusts its product photography and clean white canvas (#ffffff) to provide all the color, keeping the UI itself as a quiet, functional frame. Every button, card, and input uses the same soft gray (#dedede) as its resting state, creating a uniform, almost architectural feel across the interface. The near-black (#121212) appears only on text, icons, and the brand's wordmark — never as a background or decorative element. This restraint suggests a brand that wants parents to focus on the clothes, not the shopping experience. The Shopify platform gives it standard e-commerce patterns (cart drawer, product grid, size selector), but the color discipline makes Primary feel more like a design studio than a baby store. There are no hard corners anywhere — inputs and buttons use {rounded.sm}, cards use {rounded.md}, and the search field uses {rounded.full} — but the radii are subtle enough to avoid feeling playful. The brand's voice is direct and informational: size charts, fabric details, and care instructions take priority over marketing copy. The result is a shopping experience that feels calm, trustworthy, and surprisingly adult for a kids' clothing brand.

colors:
  primary: "#dedede"
  primary-active: "#c8c8c8"
  primary-disabled: "#f0f0f0"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-dark: "#ffffff"
  error: "#c13515"
  success: "#2e7d32"
  sale: "#c13515"
  star-rating: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
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
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
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
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-active:
    border: 1px solid "{colors.ink}"
  text-input-error:
    border: 1px solid "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    border: 1px solid "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    color: "{colors.sale}"
  size-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: 1px solid "{colors.hairline}"
  size-selector-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: 1px solid "{colors.ink}"
  size-selector-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: 1px solid "{colors.hairline-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
    border: 1px solid "{colors.hairline}"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.ink}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: 400px
  cart-item:
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  cart-item-title:
    typography: "{typography.title-sm}"
  cart-item-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  cart-item-quantity:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Subscribe". Uses the brand's signature near-gray (#dedede) background with near-black (#121212) text. On hover, the background darkens to #c8c8c8 (`{colors.primary-active}`). In disabled state, the button fades to #f0f0f0 (`{colors.primary-disabled}`) with muted text, signaling the action is unavailable. The 4px radius (`{rounded.sm}`) keeps the button feeling precise rather than playful.

**`button-secondary`** — An outlined alternative for secondary actions like "Save for Later" or "View Size Chart". Uses a white background with a 1px hairline border. On hover, the border darkens to ink. Maintains the same 44px height and 4px radius as the primary button for visual consistency in forms.

**`button-tertiary-text`** — A text-only button for the least prominent actions (e.g., "Clear Filters", "Cancel"). No background or border — just the ink text color. Used primarily in filter bars and modal footers where visual weight should be minimal.

**`button-pill`** — A fully rounded variant used for filter chips, category tags, and promotional badges. Smaller padding and font size than the primary button, with a 9999px radius that creates a pill shape. Active state uses ink background with white text.

### Text Inputs
**`text-input`** — Standard form input for email, password, and text fields. White background with a 1px hairline border and 4px radius. On focus, the border switches to ink (#121212) for clear active-state feedback. Error state uses a red border (#c13515). The 48px height provides a comfortable tap target on mobile.

**`select-input`** — Dropdown selector for size, quantity, and filter options. Matches the text-input styling exactly — same height, radius, border, and typography — so form rows feel cohesive. The dropdown arrow uses the ink color.

### Navigation
**`nav-bar`** — The primary site header, fixed at 64px height with a white background and a soft hairline bottom border. Contains the brand wordmark (ink color), navigation links, search icon, and cart icon. On scroll, a subtle shadow is added (not captured in tokens). The header is sticky on desktop but collapses on mobile.

**`nav-link-active`** — Active navigation link with a 2px ink underline. Used for the current page or section. Inactive links use muted gray (#666666) with no underline, creating clear visual hierarchy.

### Search
**`search-bar`** — A pill-shaped search input with a soft gray (#f5f5f5) background. On focus, the background switches to white and a 1px ink border appears. The 44px height is slightly shorter than form inputs, signaling this is a utility element rather than a form field. Used in the header and on the search results page.

### Product Cards
**`product-card`** — The primary product display unit on collection pages and search results. White background with 8px radius (`{rounded.md}`). The product image fills the top with a matching 8px radius. Below the image, the product title uses title-sm typography, followed by the price in muted gray. Sale prices render in red (#c13515). Cards have no border or shadow — they rely on the white-on-white contrast with the soft gray page background.

**`size-selector-button`** — Individual size buttons (XS, S, M, L, XL) in the product detail page. White background with a 1px hairline border and 4px radius. Active state fills the button with ink and white text. Disabled state (for out-of-stock sizes) uses soft gray background with muted text and a strikethrough effect.

### Badges
**`badge-sale`** — A small red badge with white uppercase text, used to flag discounted items on product cards and collection pages. 2px radius with tight 2px/6px padding keeps it compact. The red (#c13515) is the only saturated color in the entire UI, making it immediately noticeable.

**`badge-new`** — An ink-colored badge for new arrivals. Same typography and dimensions as the sale badge, but uses the brand's near-black instead of red. This creates a clear visual distinction between "new" and "sale" without introducing additional colors.

### Footer
**`footer`** — The site footer uses a soft gray (#f5f5f5) background with muted gray (#666666) text. Links are the same muted gray with an ink hover state. The footer contains accordion-style sections on mobile (shipping, returns, about, help) that expand on tap. On desktop, these sections display as a multi-column layout.

### Cart Drawer
**`cart-drawer`** — A slide-in panel from the right side of the screen, 400px wide on desktop. White background with ink text. Each cart item shows the product image, title (title-sm), price (body-sm in muted), and a quantity selector. Items are separated by soft hairline borders. The drawer includes a checkout button at the bottom using the primary button style.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product grid goes to 2 columns; cart drawer becomes full-width overlay; footer sections become accordions; size selector buttons stack vertically |
| Tablet | 744–1128px | Nav bar shows limited links (Shop, Sale, Account); product grid uses 3 columns; cart drawer remains 400px; footer shows 2-column layout |
| Desktop | 1128–1440px | Full nav bar with all links; product grid uses 4 columns; cart drawer at 400px; footer shows 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product grid uses 4 columns with wider gutters; all other layouts remain same as desktop |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (Apple HIG guideline)
- Size selector buttons are 36px height (minimum for tap targets on mobile)
- Nav bar links have 48px tap area (padding extends beyond text)
- Cart drawer close button is 44x44px
- Quantity selector +/- buttons are 44x44px

### Collapsing Strategy
- Primary nav links collapse into hamburger menu below 744px
- Secondary nav (account, cart icons) remains visible on all breakpoints
- Product filters collapse into a "Filter" button on mobile, opening a slide-in panel
- Footer accordion sections collapse on mobile, expand on tap
- Size guide and product details collapse into accordions on mobile
- Search bar collapses to icon-only on mobile, expands on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the Inter font family used in this document is an educated guess based on the brand's clean, geometric aesthetic. Actual font may differ.
- Only two hex colors were extracted (#dedede, #121212) plus the meta theme-color (#ffffff). The remaining colors (muted, surface-soft, error, success, sale) are inferred from common e-commerce patterns and may not match the live site exactly.
- Hover states for buttons and links beyond the primary button are inferred from standard interaction patterns — actual hover colors may differ.
- Error state styling (text-input-error, form validation messages) is inferred from common patterns — actual error colors and messaging may differ.
- The brand's Shopify platform may use default Shopify components (cart drawer, checkout, product form) that override some of these custom tokens.
- No data was available for: dark mode, high-contrast mode, focus ring styling, loading states, skeleton screens, toast notifications, modal dialogs, or tooltip styling.
- The brand may use additional accent colors for seasonal promotions, holiday campaigns, or limited-edition collections that are not captured here.
- Product swatch colors (for multi-color items) are not captured — these are typically dynamic and product-specific rather than part of the design system.
