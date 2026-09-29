---
version: alpha
name: "Rough Trade UK"
source_url: "https://www.roughtrade.com/en-gb"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record shop that never stopped being a record shop — #404040 ink on #ffffff canvas, with #bd2426 as the sole voltage that says "buy this record" or "this is the price." That red, a dried-blood brick tone, appears on price tags, add-to-cart buttons, and the sale badge, and it never appears anywhere else: no decorative flourishes, no gradient hero sections, no brand-pattern backgrounds. The site reads like a shelf. Type is system sans-serif at modest sizes — body sits at 14–16px in weight 400, titles at 18–22px in weight 600 — because the content is the cover art and the tracklist, not the typography. Product cards use `{rounded.none}` corners and `{spacing.sm}` padding; there is no pill-shaped anything except the search input, which gets `{rounded.full}` as a quiet functional gesture. The nav bar is a single dark strip at `{colors.ink}` with white links, no mega-menu, no illustrations, no "NEW" badges. This is a site that trusts you know what you want. The secondary palette — #62a1d8 for pre-order badges, #9bca3e for in-stock indicators, #f68b1f for limited-edition flags — reads like warehouse bin tags, not a brand system. The footer is dense with shipping policies, store addresses, and label directories, all at `{typography.caption}` size in `{colors.muted}`. The design is not quiet luxury; it is loud utility, a digital version of flipping through bins in a basement on Talbot Road.

colors:
  primary: "#bd2426"
  primary-active: "#a01e20"
  primary-disabled: "#e8a0a1"
  ink: "#404040"
  body: "#595959"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-preorder: "#62a1d8"
  badge-instock: "#9bca3e"
  badge-limited: "#f68b1f"
  badge-sale: "#bd2426"
  badge-new: "#163959"
  star-rating: "#f68b1f"
  error: "#de5052"
  success: "#516b1d"
  link: "#2f7bbf"
  link-visited: "#521010"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
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
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.primary}"

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 32px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 48px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  badge:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-instock:
    backgroundColor: "{colors.badge-instock}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 12px"
    height: 40px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    color: "{colors.link}"
  breadcrumb-current:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    padding: "4px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  cart-total:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  cart-checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Checkout," and "Pre-order." Uses `{colors.primary}` (#bd2426) background with white text. On hover, shifts to `{colors.primary-active}` (#a01e20). Disabled state uses `{colors.primary-disabled}` (#e8a0a1). Height is 40px for standard buttons, 44px for add-to-cart, and 48px for checkout. All primary buttons use `{rounded.sm}` (4px).

**`button-secondary`** — Used for "Continue Shopping," "View Details," and secondary actions. White background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Hover adds a subtle shadow. Same height and padding as primary.

**`button-tertiary-text`** — Text-only button for "Clear filters," "Remove," and "Cancel." Transparent background, `{colors.ink}` text, no border. Hover underlines.

**`button-pill-search`** — The search submit button, a rare pill shape (`{rounded.full}`) at 32px height. Uses `{colors.primary}` background. Only pill in the system.

### Navigation
**`top-nav`** — A fixed 48px dark strip at `{colors.ink}` (#404040). Contains the Rough Trade logo (white text), nav links, search icon, and cart icon. Links are white `{typography.nav-link}` at 14px weight 500. Active link has a 2px `{colors.primary}` bottom border. No dropdowns, no mega-menu.

**`breadcrumb`** — Simple text-based navigation at the top of category and product pages. Uses `{typography.caption}` (13px) in `{colors.muted}`. Current page is `{colors.ink}`. Links are `{colors.link}` (#2f7bbf).

### Cards
**`product-card`** — A minimal card with no border, no shadow, no rounded corners (`{rounded.none}`). Contains a 1:1 square image, artist name in `{colors.muted}` caption, album title in `{title-sm}`, and price. Padding is `{spacing.sm}` (8px). On hover, the image gets a subtle dark overlay and a "Quick View" button appears.

**`product-card-price-sale`** — When a record is on sale, the price uses `{colors.primary}` (#bd2426) in weight 700. The original price is shown with a line-through in `{colors.muted-soft}`.

### Badges
**`badge`** — Small uppercase labels at 11px weight 700, `{rounded.xs}` (2px). Five variants: pre-order (blue `#62a1d8`), in-stock (green `#9bca3e`), limited edition (orange `#f68b1f`), sale (red `#bd2426`), and new release (dark blue `#163959`). All use white text. Padding is 2px 6px.

### Forms
**`search-input`** — The only pill-shaped element in the system (`{rounded.full}`). White background, 40px height, 8px 16px padding. Has a magnifying glass icon on the left and a `{colors.primary}` submit button on the right.

**`filter-dropdown`** — Standard select dropdown for sorting and filtering. White background, 1px `{colors.hairline}` border, `{rounded.sm}` (4px), 36px height. Uses system-native dropdown arrow.

**`newsletter-input`** — Email input in the footer. White background, 1px `{colors.hairline}` border, `{rounded.sm}`. Paired with a `{colors.primary}` submit button.

### Footer
**`footer`** — Dark section at `{colors.ink}` (#404040) with white headings and `{colors.muted-soft}` (#bfbfbf) body text. Organized in columns: Help, About, Stores, Newsletter. Links are `{typography.caption}` (13px). Padding is `{spacing.xxl}` (48px) top and bottom.

### Cart
**`cart-item`** — Row layout with product image, title, format, quantity selector, and price. White background, 1px `{colors.hairline}` bottom border. Padding `{spacing.base}` (16px) top and bottom.

**`quantity-selector`** — A compact input with minus/plus buttons and a numeric display. White background, 1px `{colors.hairline}` border, `{rounded.sm}`, 36px height.

### Pagination
**`pagination`** — Simple numbered pagination at the bottom of search and category results. Active page uses `{colors.primary}` background with white text. Inactive pages are text-only in `{colors.ink}`. Previous/Next arrows are text links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column product grid (2 columns). Top nav collapses to hamburger menu. Search bar moves to a toggleable overlay. Filter bar becomes a sticky bottom sheet. Footer stacks vertically. Product card images are 1:1 but smaller. |
| Tablet | 744–1128px | Two-column product grid. Top nav shows limited links (Logo, Search, Cart, Hamburger). Filter bar is a horizontal scroll. Footer shows 2-column layout. |
| Desktop | 1128–1440px | Three-column product grid. Full top nav with all links visible. Filter bar is a horizontal strip with dropdowns. Footer shows 4-column layout. Breadcrumb visible. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px. Top nav and footer are centered within max-width. Additional whitespace on sides. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px height.
- Icon buttons (search, cart, hamburger) are 32px with 44px padding on mobile.
- Filter dropdowns and quantity selectors are 36px minimum.
- Product card links have 44px tap area on mobile.

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px.
- Search bar becomes a full-screen overlay on mobile.
- Filter bar collapses to a sticky bottom sheet on mobile.
- Footer columns collapse to a single column on mobile.
- Product grid goes from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 2 (mobile).
- Breadcrumb hides on mobile.
- Sidebar (if present on category pages) collapses to a top section on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily weighted toward grays (#404040, #ebebeb, #dedede, #595959, #737373, #272727, #bfbfbf) and blues (#62a1d8, #2f7bbf, #163959, #0051c3), which may include Shopify checkout widget colors and social media icon colors. The brand's true primary (#bd2426) was identified as the most distinctive non-gray, non-blue color in the list.
- Font-family declarations were system-only (-apple-system, Arial, BlinkMacSystemFont, Helvetica Neue, Oxygen, Roboto, Segoe UI, Ubuntu, courier, monaco, monospace, sans-serif). No custom brand font was detected. The site may use a web font that wasn't captured in the extraction.
- Hover states for buttons, links, and cards are inferred from common patterns, not extracted from the live site.
- Error styling (form validation, 404 pages, error messages) was not extracted.
- Dark mode is not supported and was not detected.
- Sub-brand palettes (Rough Trade NYC, Rough Trade Nottingham, Rough Trade Bristol) may have distinct colors not captured.
- Animation and transition timings were not extracted.
- The extracted list includes #9bca3e, #bada7a, #516b1d (greens) and #f68b1f, #f9b169, #904b06, #c16508, #ee730a (oranges) — these may be badge colors, stock image dominant tones, or seasonal promotional colors rather than core brand tokens. They are included as badge variants but may not be permanent.
- The site was behind Cloudflare's "Attention Required" page during extraction, so some structural elements (hero sections, promotional banners, featured collections) may not have been captured.
- Checkout flow colors (Shopify Pay buttons, Klarna badges) may be mixed into the extracted palette.
