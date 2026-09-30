---
version: alpha
name: "Season of Mist"
source_url: "https://shop.season-of-mist.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black canvas (#222222) and a single sharp orange accent (#f89406) define this online metal shop — a storefront that trusts high-contrast product photography and brutalist simplicity over decorative chrome. The palette is almost entirely monochrome: near-black ink on near-white canvas (#f5f5f5), with the orange reserved exclusively for primary actions, price highlights, and the rare badge that needs to cut through the noise. Red (#ee5f5b) appears as a secondary accent for sale indicators or limited-stock warnings, while a cool blue (#0088cc) surfaces in informational links and secondary navigation — a triadic system that feels more like a gig poster than a retail interface. Type runs Arial and Helvetica Neue at modest weights; there is no custom display face, no variable font, no decorative lettering — the brand lets album art and band logos do the typographic heavy lifting. Buttons are sharp-cornered (`{rounded.sm}` ~8px), product cards use a slightly softer radius (`{rounded.md}` ~12px), and the search bar sits as a full-width input rather than a pill, reinforcing the utilitarian, no-frills browsing experience. The footer collapses into a dense stack of monochrome links, and the nav bar stays fixed at 60px with a simple logo-left, links-right layout. This is a store designed for speed and clarity — find the record, add to cart, get out.

colors:
  primary: "#f89406"
  primary-active: "#e08500"
  primary-disabled: "#fce0b0"
  ink: "#222222"
  body: "#333333"
  muted: "#555555"
  muted-soft: "#a7a7a7"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ee5f5b"
  accent-red-active: "#c43c35"
  accent-blue: "#0088cc"
  accent-blue-active: "#0055cc"
  accent-green: "#62c462"
  accent-green-active: "#51a351"
  badge-sale: "#f13d34"
  badge-new: "#f89406"
  star-rating: "#fbb450"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-danger:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-danger-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 5px 15px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    margin: "{spacing.sm} 0 0 0"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.accent-red}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  pagination-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 10px"
  pagination-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-link-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-total:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.on-primary}"
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, rendered in the brand's orange (#f89406) on white. Used for "Add to Cart", "Buy Now", and primary form submissions. On hover, darkens to `{colors.primary-active}` (#e08500). Disabled state fades to a pale orange (#fce0b0) with no pointer events.

**`button-secondary`** — An outlined variant on a white background with a 1px hairline border. Used for "View Details", "Continue Shopping", and secondary actions. Active state swaps the background to `{colors.surface-soft}` and border to `{colors.muted}`.

**`button-danger`** — Red (#ee5f5b) for destructive actions like "Remove from Cart" or "Cancel Order". Active state darkens to #c43c35. Always paired with a confirmation dialog.

**`button-ghost`** — A text-only button with no background or border. Used for inline actions within cards or tables. Active state adds a soft gray background (#f9f9f9).

**`button-pill-primary`** — A compact pill-shaped variant of the primary button, used for filter tags, category toggles, and small inline CTAs. Uses `{typography.button-sm}` and `{rounded.full}`.

**`button-pill-outline`** — The outlined counterpart to the pill primary, used for inactive filter tags and unselected category toggles. Border uses `{colors.hairline}` (#e5e5e5).

### Navigation
**`nav-bar`** — A fixed 60px bar on a near-black background (#222222) with white text. Logo sits left, primary navigation links right. No dropdowns — this is a flat, single-level nav. Active link and hover state both use the orange accent (#f89406).

**`nav-link`** — White text at 14px/600 weight. Active state switches to orange. No underline decoration — color alone signals state.

**`breadcrumb-link`** — Muted gray (#555555) links at 13px. Active (current page) uses the ink color (#222222). Separator is a simple ">" character in `{colors.muted-soft}`.

### Cards
**`product-card`** — A white card with 12px rounded corners (`{rounded.md}`). Contains a product image (top, radius clipped to match card top), title, price, and an optional badge. The "Add to Cart" button sits at the bottom of the card, using `{colors.primary}`.

**`product-card-badge`** — A small red (#f13d34) uppercase label pinned to the top-left of the card image. Used for "SALE" or "% OFF" indicators. New arrivals use the orange badge variant (`{colors.badge-new}`).

**`category-tag`** — A pill-shaped tag on a soft gray background (#f9f9f9) with muted text. Active state fills with orange and white text. Used in filter strips and category navigation.

### Forms
**`text-input`** — A standard 40px input with a white background and 1px hairline border. Focus state adds a 2px orange ring (`{colors.primary-disabled}` as the ring color). Error state swaps the border to red (#ee5f5b).

**`select-input`** — Same dimensions and styling as `text-input`, but rendered as a native `<select>` element. The dropdown arrow is styled in `{colors.muted}`.

**`search-bar`** — A full-width text input styled identically to `text-input`. No pill shape — the brand favors a clean rectangular search field. A magnifying glass icon sits inside the left padding.

**`quantity-selector`** — A compact 36px input with a hairline border, used in cart items. Contains a minus button, the quantity number, and a plus button. Buttons are `{colors.muted}` text on transparent background.

### Footer
**`footer`** — A dense, near-black (#222222) footer with white and muted-gray links. Organized in columns (Shop, Help, About, Social). Links use `{colors.muted-soft}` (#a7a7a7) and hover to orange. No newsletter signup — the footer is purely informational.

### Hero
**`hero-banner`** — A full-width section on a near-black background with white text. Used for featured releases, seasonal promotions, or band spotlights. The CTA button uses `{colors.primary}` with white text. Background may feature a full-bleed album art image with a dark scrim overlay.

### Cart & Checkout
**`cart-item`** — A white row with a bottom hairline border. Contains product thumbnail, title, price, quantity selector, and a remove button (ghost style, red on hover).

**`cart-total`** — Bold 16px text in `{colors.ink}`, right-aligned below the cart items. Includes subtotal, shipping (if applicable), and total.

**`checkout-button`** — A green (#62c462) full-width button at the bottom of the cart. Active state darkens to #51a351. This is the only green element in the system — reserved exclusively for the purchase confirmation action.

### Pagination
**`pagination-link`** — Numbered page links in muted gray. Active page fills with orange. Hover state adds a soft gray background. Previous/Next arrows use the same styling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu. Product cards stack in single column. Hero banner reduces padding to 32px. Footer columns stack vertically. Search bar remains full-width. |
| Tablet | 744–1128px | Nav links remain visible but may wrap. Product cards display in 2-column grid. Hero banner uses 48px padding. Footer columns display in 2x2 grid. |
| Desktop | 1128–1440px | Full nav bar. Product cards in 3-column grid. Hero banner at full padding (64px). Footer columns in 4-column layout. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product cards in 4-column grid. Additional whitespace on left and right of hero banner. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Quantity selector buttons are 44px wide to accommodate tap targets.
- Product card "Add to Cart" buttons are 48px tall on mobile.
- Nav hamburger icon is 44x44px with adequate padding.

### Collapsing Strategy
- On mobile, the primary nav collapses into a full-screen overlay menu triggered by a hamburger icon in the top-left of the nav bar.
- The category filter strip (pills) collapses into a horizontal scrollable row on mobile, with a "Show Filters" button that expands into a modal.
- Product card badges remain visible on all breakpoints but reduce font size to 10px on mobile.
- The footer collapses from 4 columns to 2 columns on tablet, and to a single stacked column on mobile.
- The hero banner reduces vertical padding from 64px to 32px on mobile, and the CTA button becomes full-width.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only from CSS pseudo-classes found in the live site. Some hover transitions (e.g., product card image zoom, link underlines) may exist but were not captured.
- **Error and validation styling**: Error states for forms (red border) are inferred from common patterns. Specific error message typography, iconography, and animation timing are unknown.
- **Loading states**: Skeleton screens, spinner animations, and disabled button loading states were not extracted. The brand may use a custom spinner or a simple text-based "Loading..." indicator.
- **Dark mode**: No dark mode variant was detected. The site appears to be light-mode only, with the near-black nav and footer serving as the only dark surfaces.
- **Sub-brand or seasonal palettes**: The brand may use limited-edition color schemes for specific album releases or seasonal promotions. These were not captured.
- **Font stack details**: The extracted font declarations include generic fallbacks (Arial, Helvetica Neue) but no custom web fonts. The brand may use a self-hosted or CDN-loaded font that was not detected in the CSS extraction.
- **Animation and transition timing**: No `transition` or `animation` properties were reliably extracted. The brand likely uses simple 0.2s–0.3s ease transitions for hover states, but exact values are unknown.
- **Accessibility focus styles**: The `:focus-visible` outline style was not extracted. The brand may use a custom focus ring (e.g., 2px solid orange) or rely on browser defaults.
- **Checkout flow**: The extracted colors include green (#62c462) and blue (#0088cc) that may correspond to third-party payment widgets (PayPal, Klarna, etc.). The exact checkout component styling is inferred from common patterns rather than extracted from the live site.
- **Social media icon colors**: The extracted palette includes multiple blues and grays that may correspond to social media brand colors (Facebook blue, Twitter blue, etc.). These are not part of the Season of Mist design system and should be treated as third-party assets.
