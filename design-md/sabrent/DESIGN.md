---
version: alpha
name: "Sabrent"
source_url: "https://www.sabrent.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-navy (#080341) e-commerce storefront for high-performance storage hardware, where technical credibility is signaled through a stark two-tone palette of midnight blue and clean white (#f3f4f6) rather than flashy gradients or lifestyle photography. The brand’s primary voltage is a confident corporate blue (#0057b8) that appears on every add-to-cart button, category header, and product badge — a color borrowed from industrial engineering rather than consumer tech. Product pages read like spec sheets: dense tables of read/write speeds, controller chips, and NAND types sit in a tight 12-column grid, with the only visual relief coming from product shots on pure white backgrounds and the occasional green (#3ed660) “in stock” indicator or orange (#ee9441) sale badge. The typography runs Inter at modest weights (400–600) across all headings and body text, with no display-size hero type — the brand trusts its product photography and technical copy to carry the page. Navigation is a fixed top bar with a left-aligned logo, a search icon, and a cart counter, all rendered in the same deep navy as the footer. Every interactive element — buttons, input fields, dropdowns — uses a crisp 4px radius (`{rounded.xs}`), a deliberate choice that reads as precise and utilitarian, matching the machined-aluminum enclosures of the SSDs themselves. The checkout flow is Shopify-hosted, introducing a secondary blue (#007aff) for payment actions that sits slightly warmer than the brand’s primary blue, a subtle but noticeable shift in the purchase funnel.

colors:
  primary: "#0057b8"
  primary-active: "#004494"
  primary-disabled: "#8ab4e0"
  ink: "#080341"
  body: "#121212"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#dedede"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  stock-green: "#3ed660"
  sale-orange: "#ee9441"
  error-red: "#8b0000"
  success-green: "#006400"
  link-blue: "#007aff"
  dark-bg: "#0a142f"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.15px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  price-sale:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
    color: "{colors.sale-orange}"

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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-link:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 40px
  cart-icon-button:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.xs}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    margin-top: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    margin-top: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.sale-orange}"
    margin-top: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.sale-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    margin-top: "{spacing.base}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "4px 0"
  footer-link-hover:
    textColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.lg} 0"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 18px
    width: 18px
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.base}"
    border-top: "1px solid {colors.hairline}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s corporate blue (#0057b8) with white text and a crisp 4px radius. On hover, it shifts to a darker active state (#004494). When disabled, it fades to a muted blue (#8ab4e0) with no shadow or border, signaling non-interactivity. Used for “Add to Cart”, “Buy Now”, and “Subscribe” actions.

**`button-secondary`** — An outlined variant with a white fill, dark navy text, and a 1px hairline border. The border darkens to the ink color on hover, and the background takes on a soft gray (#f3f4f6) tint. Used for “Compare”, “View Details”, and secondary form actions like “Cancel” or “Clear Filters”.

**`button-ghost`** — A text-only button with no background or border, using the primary blue for its label. Used for inline actions like “Learn More”, “Read Specs”, or “Remove” in cart line items. No hover background shift — only the text color may darken slightly.

### Cards
**`product-card`** — The primary product display unit, a white card with a 1px soft hairline border and 4px radius. Contains a product image on a light gray (#f3f4f6) background, a title in 16px medium weight, and a price in 20px semibold. Sale prices render in orange (#ee9441). Badges sit in the top-left corner of the image area, using the primary blue for “New” or “Best Seller”, orange for “Sale”, and green for “In Stock”. Cards are arranged in a responsive grid with 16px gaps.

**`product-card-badge`** — Small uppercase labels (11px, 600 weight) pinned to product images. Three color variants: blue for informational badges, orange for sale/discount, and green for stock status. All use white text and a 4px radius.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, filled with the deep navy (#080341). Contains the brand logo left-aligned, a search icon button, and a cart icon button right-aligned. Link text is white at 14px medium weight, with active links highlighted in the primary blue. No dropdown menus — the nav is intentionally sparse, directing focus to the product catalog.

**`breadcrumb`** — A secondary navigation element in 13px regular weight, using muted gray for static text and primary blue for clickable links. Separators are simple slashes in a lighter gray. Sits above the page title on category and product pages.

### Forms
**`text-input`** — Standard input fields with a white background, 1px hairline border, and 4px radius. On focus, the border thickens to 2px and turns primary blue with no outline. Height is 44px with 10px/12px padding. Used for search, email signup, and address forms.

**`select-dropdown`** — Matches the text-input styling but includes a custom chevron icon. Used for sorting (e.g., “Best Match”, “Price Low-High”) and filtering options.

**`quantity-selector`** — A compact input group for cart quantities, with a 44px height and two side buttons (minus/plus) on a soft gray background. The center value is editable text in 16px regular weight.

### Footer
**`footer`** — A full-width section in the deep navy (#080341) with white text at 14px regular weight. Links are in a lighter gray (#9ca3af) and shift to white on hover. Organized in a multi-column layout with section headers in 16px medium weight. Includes legal text, social links, and payment method icons in the bottom row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; filter panel becomes a slide-out drawer; quantity selector stacks vertically; footer columns stack to single column |
| Tablet | 744–1128px | Two-column product grid; nav bar shows limited links (Home, Products, Support); filter panel is a collapsible sidebar; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; filter panel is a persistent left sidebar; footer shows four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with centered content; nav bar and footer remain full-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height
- Icon buttons (search, cart, quantity controls) are at least 40px × 40px
- Filter checkboxes are 18px × 18px with 8px touch padding
- Product card links have a minimum 48px tap area

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile, revealing a full-screen overlay with links and search
- Product filters collapse to a bottom sheet or slide-out drawer on mobile and tablet
- Product image galleries switch from thumbnail strip to swipeable carousel on mobile
- Footer columns stack to single column on mobile, with section headers acting as accordion toggles
- Breadcrumbs hide on mobile, replaced by a single “Back” link

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by generic web blues, grays, and a few accent colors — the brand’s true primary (#0057b8) was chosen as the most distinctive blue, but it may not be the exact brand blue used in all contexts (e.g., hover states, disabled states are inferred)
- Font-family declarations only returned “Inter” and “swiper-icons” — no fallback stack or secondary typeface was found; the Inter family is assumed to include all weights (400, 500, 600) but exact weight usage for each heading level is inferred from common e-commerce patterns
- No meta theme-color was found, so the browser chrome color is unknown (likely the deep navy or white)
- Hover and focus states for most components are inferred from common patterns (darken primary, thicken border) rather than extracted from live CSS
- Error state styling (red borders, error messages) is not confirmed — the extracted #8b0000 is assumed for error text but may be used elsewhere
- Dark mode is not supported; no dark-theme tokens were found
- The Shopify checkout flow introduces a secondary blue (#007aff) that may not be part of the brand’s intentional palette — it’s noted as a gap
- Stock photography and product image dominant tones may have influenced the extracted color list; the true brand palette may be more limited (navy, white, blue, and one accent)
- No animation or transition timing values were extracted (hover transitions, page load animations, etc.)
- Sub-brand or product-line-specific color variants (e.g., Rocket series vs. standard) are not captured
