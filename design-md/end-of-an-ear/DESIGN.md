---
version: alpha
name: "End of an Ear"
source_url: "https://www.endofanear.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store that reads like a punk zine designed by a librarian — #3453a3, a deep cobalt blue, is the primary voltage, used for the site's header background, navigation links, and key interactive elements, standing out against a canvas of #e9e9e9. The typography stack is a monospace-heavy affair, with `Consolas`, `Menlo`, and `SF Mono` forming the core reading experience, giving every product title and price the weight of a typewriter. Buttons and badges use `{rounded.sm}` corners, but the real character comes from the color palette: a traffic-light system of green (#008a00) for "In Stock" badges and red (#ee0000) for "Sold Out," with a sharp yellow (#ffff2f) for sale pricing. The layout is dense and utilitarian — a single-column product grid on mobile, expanding to three columns on desktop — with `{spacing.sm}` gaps between cards and `{spacing.base}` padding inside each. There is no hero image, no lifestyle photography; the brand trusts its inventory photography and raw typographic hierarchy. The footer is a dark slab of #393939 with white links, and the search bar sits in the header as a full-width input with a `{rounded.sm}` border. It feels like a physical store's inventory system made public — honest, unpolished, and deeply functional.

colors:
  primary: "#3453a3"
  primary-active: "#213569"
  primary-disabled: "#a9a9a9"
  ink: "#121212"
  body: "#393939"
  muted: "#696969"
  muted-soft: "#a9a9a9"
  hairline: "#dcdcdc"
  hairline-soft: "#e0e3e4"
  canvas: "#e9e9e9"
  surface-soft: "#f3f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  stock-green: "#008a00"
  stock-green-active: "#00a500"
  sold-red: "#ee0000"
  sold-red-active: "#ff0000"
  sale-yellow: "#ffff2f"
  sale-yellow-active: "#ffbd00"
  footer-bg: "#393939"
  footer-text: "#e9e9e9"

typography:
  display-xl:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Consolas', 'Menlo', 'Monaco', 'SF Mono', 'Liberation Mono', 'Lucida Console', monospace"
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
    padding: 8px 16px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 7px 15px
    height: 36px
  button-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  button-sold:
    backgroundColor: "{colors.sold-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
    padding: "0 {spacing.base}"
  nav-link:
    color: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  nav-link-active:
    color: "{colors.on-primary}"
    textDecoration: underline
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.sale-yellow}"
    backgroundColor: "{colors.ink}"
    padding: "2px 4px"
  badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sold:
    backgroundColor: "{colors.sold-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.sale-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 36px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
    textDecoration: underline

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and checkout flows. Background is {colors.primary} with white text, set in monospace {typography.button-md}. On hover, shifts to {colors.primary-active}. Disabled state uses {colors.primary-disabled} with reduced opacity. Height is 36px with {rounded.sm} corners.

**`button-secondary`** — Used for secondary actions like "View Details" or "Clear Cart." Background is {colors.canvas} with {colors.ink} text, a 1px {colors.hairline} border, and the same 36px height and {rounded.sm} corners as the primary button.

**`button-stock`** — A compact, green badge-button indicating in-stock items. Uses {colors.stock-green} background with white text, set in {typography.button-sm}. Height is 24px with {rounded.sm} corners and 4px 8px padding.

**`button-sold`** — The inverse of the stock button, using {colors.sold-red} to clearly mark sold-out items. Same dimensions and typography as `button-stock`.

### Cards
**`product-card`** — The core inventory display unit. A white card ({colors.surface-card}) with {rounded.sm} corners and {spacing.sm} padding. Contains a product image with {rounded.sm} corners and `object-fit: cover`, a title in {typography.title-md}, and a price in {typography.body-md}. Sale-priced items overlay the price with {colors.sale-yellow} text on a {colors.ink} background. Badges for stock, sold, and sale status sit in the top-left corner of the image.

### Navigation
**`nav-bar`** — A fixed-height 48px bar using {colors.primary} background. Navigation links are white, set in {typography.nav-link}, with the active page underlined. The bar contains the store name/logo on the left and navigation links on the right, with {spacing.base} horizontal padding.

### Forms
**`text-input`** — Standard input fields for search and checkout forms. Background is {colors.canvas} with {colors.ink} text, a 1px {colors.hairline} border, and {rounded.sm} corners. On focus, the border switches to {colors.primary}. Height is 36px with 8px 12px padding.

**`search-bar`** — A full-width input in the header for searching the inventory. Same styling as `text-input` but with {spacing.sm} {spacing.md} padding and a slightly larger visual presence.

### Footer
**`footer`** — A dark slab ({colors.footer-bg}) with light text ({colors.footer-text}). Contains links, contact info, and store policies. Links are underlined and set in {typography.link}. Padding is {spacing.xl} vertical and {spacing.base} horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav-bar collapses to hamburger menu. Search bar moves below nav. Footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid. Nav-bar shows all links. Search bar in header. Footer in two columns. |
| Desktop | 1128–1440px | Three-column product grid. Full nav-bar with search. Footer in three columns. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px. |

### Touch Targets
- All buttons and links have a minimum touch target of 44px height.
- Nav-bar links have 48px touch height.
- Product card images are tappable with a minimum 120px height.
- Search bar has 36px height but is full-width, making it easy to tap.

### Collapsing Strategy
- On mobile, the nav-bar collapses to a hamburger icon that opens a full-screen overlay menu.
- The product grid collapses from 3 columns to 1 on mobile, with 2 columns on tablet.
- Footer links stack vertically on mobile, expanding to 2 columns on tablet and 3 on desktop.
- The search bar moves from the header to below the nav on mobile, becoming a full-width element.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components (only primary button active state is confirmed).
- Error styling for form inputs (validation, error messages).
- Sub-brand or category-specific color palettes (e.g., used for genre or format filtering).
- Dark mode or high-contrast mode support.
- Exact font weights and sizes for all typography (extracted only monospace stack; weights and sizes are inferred from common record store patterns).
- Spacing values are inferred from common e-commerce patterns; exact padding/margins may vary.
- The extracted hex list includes many social icon colors (#3b5998, #1da1f2, #bd081c, #d83776, #fd355a, #1ab7ea) and checkout widget colors (#008a00, #00aa00, #00a500, #ffbd00) which are not part of the brand's core palette. The true brand colors are likely #3453a3 (primary), #e9e9e9 (canvas), #393939 (body), and #121212 (ink).
- No extracted font-family for headings or body text beyond monospace; the brand may use a secondary font for display text that wasn't captured.
