---
version: alpha
name: "HHKB"
source_url: "https://hhkeyboard.us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A monochrome engineering canvas (#404040, #ebebeb, #dedede) where the only color allowed is the one you choose — a single accent from a palette of six saturated signals: alert red (#bd2426), confirmation green (#9bca3e), link blue (#62a1d8), warning orange (#f68b1f), deep navy (#163959), and a secondary red (#de5052) that reads as a softer sibling of the primary alert. The brand is the keyboard itself: every design decision defers to the object. Product cards float on white with hairline-thin borders (`{rounded.sm}` ~8px), and the typography stack — system-native sans-serif with a fallback to Courier and Monaco — mirrors the terminal environment the HHKB was born for. Buttons are compact and rectangular (`{rounded.xs}` ~4px), never pill-shaped; the primary action uses a deep charcoal (`#404040`) with white text, while secondary and ghost variants use the same charcoal as outline or text-only. The checkout flow introduces a sudden blue (#0051c3) and a bright orange (#ee730a) — likely Shopify Pay and Klarna widgets — that violate the monochrome rule but are tolerated as third-party guests. There is no hero imagery, no lifestyle photography; the page is a grid of product thumbnails, spec tables, and add-to-cart bars. The brand trusts the keyboard's reputation, not visual storytelling. The result is a site that feels like a tool catalog — precise, unadorned, and completely confident that the product is the only thing worth looking at.

colors:
  primary: "#404040"
  primary-active: "#272727"
  primary-disabled: "#bfbfbf"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  alert-red: "#bd2426"
  alert-red-soft: "#de5052"
  confirm-green: "#9bca3e"
  confirm-green-dark: "#516b1d"
  link-blue: "#62a1d8"
  link-blue-dark: "#2f7bbf"
  warning-orange: "#f68b1f"
  warning-orange-dark: "#c16508"
  deep-navy: "#163959"
  deep-navy-dark: "#521010"
  checkout-blue: "#0051c3"
  checkout-orange: "#ee730a"
  checkout-orange-soft: "#f9b169"
  checkout-orange-dark: "#904b06"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  monospace:
    fontFamily: "courier, monaco, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-add-to-cart-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-quantity:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 32px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.alert-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-detail-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  product-detail-spec-row:
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  product-detail-spec-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  product-detail-spec-value:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-section-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.hairline-soft}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-trigger-active:
    textColor: "{colors.primary}"
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  badge-new:
    backgroundColor: "{colors.confirm-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.warning-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    height: 28px
  quantity-selector-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: center
    padding: "4px"
    height: 28px
  checkout-button:
    backgroundColor: "{colors.checkout-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 44px
  checkout-button-active:
    backgroundColor: "{colors.link-blue-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  checkout-klarna-button:
    backgroundColor: "{colors.checkout-orange-soft}"
    textColor: "{colors.checkout-orange-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 36px
  checkout-paypal-button:
    backgroundColor: "{colors.checkout-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Buy Now," and primary form submissions. Rendered as a solid charcoal (`{colors.primary}`) rectangle with white text and a 4px corner radius (`{rounded.xs}`). On hover/active, the background deepens to `{colors.primary-active}` (#272727). The disabled state uses `{colors.primary-disabled}` (#bfbfbf) with white text, signaling the action is unavailable.

**`button-secondary`** — An outlined variant of the primary button, using a 2px solid `{colors.primary}` border on a white background. Used for secondary actions like "View Details" or "Cancel." On active state, the background shifts to `{colors.surface-soft}` and the border to `{colors.primary-active}`.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Learn More" or "Read Specs." Text color is `{colors.primary}`. On hover/active, a subtle `{colors.surface-soft}` background appears.

**`button-add-to-cart`** — A slightly taller variant of `button-primary` (44px vs 40px) with 24px horizontal padding, used specifically on product detail pages for the primary add-to-cart action. Active state uses `{colors.primary-active}`.

**`button-quantity`** — A compact 32px-tall button used inside quantity selectors. White background with a `{colors.hairline}` border and `{colors.ink}` text. Used for increment/decrement actions.

### Cards
**`product-card`** — The primary product display unit, used in grid layouts on collection pages and search results. A white card (`{colors.surface-card}`) with a 1px `{colors.hairline-soft}` border and 8px corner radius (`{rounded.sm}`). Contains a product image with `{rounded.xs}`, a title using `{typography.title-sm}`, and a price using `{typography.body-md}` in `{colors.primary}`. On hover, the border darkens to `{colors.hairline}` and a subtle box shadow appears.

**`product-card-badge`** — A small, uppercase label overlaid on product cards to indicate status. Uses `{colors.alert-red}` background with white text for "Sale" or "New" indicators. A `{colors.muted}` variant exists for "Sold Out" or "Discontinued" labels.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar, 60px tall, white background with a 1px `{colors.hairline-soft}` bottom border. Contains logo, product category links, and utility icons (search, cart, account). Active links use `{colors.primary}` text with a 2px `{colors.primary}` bottom border.

**`nav-link-active`** — The active state for navigation links, distinguished by `{colors.primary}` text color and a 2px solid bottom border in the same color.

### Forms
**`text-input`** — Standard text input field used for search, checkout forms, and account creation. White background, `{colors.ink}` text, 4px corner radius (`{rounded.xs}`), and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`. Error state uses `{colors.alert-red}` border.

**`select-input`** — Dropdown select element matching the `text-input` styling: white background, `{colors.ink}` text, 4px corner radius, and a 1px `{colors.hairline}` border.

### Product Detail
**`product-detail-section`** — A section divider on product detail pages, using white background with `{typography.body-md}` text and a `{colors.hairline-soft}` bottom border. Contains spec tables, descriptions, and accordion panels.

**`product-detail-spec-row`** — A single row in a product specification table. Uses `{typography.body-sm}` with a `{colors.hairline-soft}` bottom border. The label column uses `{colors.muted}` and `{typography.caption}`, while the value column uses `{colors.ink}` and `{typography.body-sm}`.

### Hero
**`hero-section`** — The full-width hero banner on the homepage or landing pages. White background with `{typography.display-xl}` for the headline and generous vertical padding (`{spacing.section}`). Contains a single `button-primary` CTA.

### Footer
**`footer-section`** — The site footer, using `{colors.primary}` as background with white text. Contains navigation links, legal information, and social icons. Links use `{typography.link}` and lighten to `{colors.hairline-soft}` on hover.

### Accordion
**`accordion-trigger`** — The clickable header of an accordion panel, used on product detail pages for "Specifications," "Shipping," and "Returns" sections. Uses `{typography.title-sm}` with `{colors.ink}` text and a `{colors.hairline-soft}` bottom border. Active state uses `{colors.primary}` text.

**`accordion-panel`** — The expandable content area below an accordion trigger. Uses `{typography.body-md}` with `{colors.ink}` text and `{spacing.base}` padding.

### Badges
**`badge-new`** — A green (`{colors.confirm-green}`) badge for "New" products.
**`badge-sale`** — A red (`{colors.alert-red}`) badge for sale items.
**`badge-limited`** — An orange (`{colors.warning-orange}`) badge for limited edition items.

### Quantity Selector
**`quantity-selector`** — A horizontal control for adjusting product quantity, composed of a decrement button, a text input, and an increment button. The container uses a 1px `{colors.hairline}` border and 4px corner radius. Buttons are 28px tall with `{colors.surface-soft}` background.

### Checkout
**`checkout-button`** — A blue (`{colors.checkout-blue}`) button used for the primary checkout action. Active state uses `{colors.link-blue-dark}`. This color is a third-party widget and does not match the brand's monochrome palette.

**`checkout-klarna-button`** — A soft orange (`{colors.checkout-orange-soft}`) button for Klarna payment option. Text is `{colors.checkout-orange-dark}`.

**`checkout-paypal-button`** — A bright orange (`{colors.checkout-orange}`) button for PayPal payment option.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked product detail sections, full-width hero |
| Tablet | 744–1128px | Two-column product grid, visible top nav with dropdowns, side-by-side product detail layout |
| Desktop | 1128–1440px | Three-column product grid, expanded top nav, multi-column footer, max-width container |
| Wide | > 1440px | Four-column product grid, max-width container centered, additional whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Quantity selector buttons are 28px tall — below the 44px recommendation — but are paired with a larger text input for the primary interaction.
- Product card links use the full card area as a touch target, not just the title text.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer for links.
- Product detail sections (specs, description, shipping) collapse into accordion panels below 744px.
- Footer links collapse into accordion-style sections below 744px, with the legal text remaining visible.
- Product grid reduces from 4 columns to 3, 2, and 1 column as viewport narrows.
- Hero section reduces font size and padding on mobile, with the CTA button becoming full-width.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is dominated by grays (#404040, #ebebeb, #dedede, #595959, #737373, #272727, #bfbfbf) and a set of six saturated accents (red, green, blue, orange, navy). The brand's true primary is likely the charcoal (#404040), but the accent colors' exact usage (badges, links, alerts, brand highlights) could not be confirmed from the extraction alone. The six accent colors are included as brand-specific tokens but their semantic roles (which is the "brand" color vs. utility colors) are inferred.
- The extracted font stack is entirely system-native sans-serif with Courier/Monaco as monospace fallbacks. No custom or brand-specific typeface was found. The monospace token is included based on the presence of "courier" and "monaco" in the extracted declarations, but its usage (code snippets, technical specs, or decorative) is unknown.
- Hover, focus, and active states for all components are inferred from common patterns and may not match the live site exactly. The `product-card-hover` shadow is a best-guess value.
- The checkout button colors (#0051c3, #ee730a, #f9b169, #904b06) are likely third-party payment widget colors (Shopify Pay, Klarna, PayPal) and not part of the HHKB brand palette. They are included as tokens for completeness but should be verified against the actual checkout integration.
- No dark mode, error page, or empty state styling could be extracted.
- The `meta theme-color` was absent, so the browser chrome color is unknown.
- The site is not on Shopify, so Shopify-specific design tokens (cart drawer, checkout overlay) are not applicable.
- The "Attention Required! | Cloudflare" page title suggests the extraction may have been blocked by a security challenge, so the extracted colors and fonts may represent a fallback or error page rather than the full brand experience. The design system above assumes the extracted data is representative of the main site, but this is a significant caveat.
