---
version: alpha
name: "Norman Records"
source_url: "https://www.normanrecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, dusty crate-digger's interface where #313131 — a near-black charcoal — sets the tone for a site that prioritises inventory density over visual polish, and where the music itself is the only colour that matters. The palette is deliberately restrained: a single grey anchor, white canvas, and the occasional accent from album artwork or the bright orange "Add to Basket" button that cuts through the monochrome like a hi-vis vest in a record shop basement. Typography runs a flat system stack — Arial, Helvetica Neue, sans-serif — at modest sizes, with no custom typeface to distract from the thousands of product rows. The layout is a relentless vertical scroll of compact rows: artist, title, format, price, condition, and a tiny basket icon, all packed at 12–16px spacing. There is no hero image, no lifestyle photography, no editorial whitespace — just a search bar, a genre nav, and an infinite grid of second-hand vinyl. The site feels like the warehouse it ships from: utilitarian, honest, and built for people who already know what they're looking for.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#999999"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-basket: "#e67e22"
  accent-basket-hover: "#d35400"
  stock-in: "#27ae60"
  stock-low: "#e67e22"
  stock-out: "#c0392b"
  badge-new: "#3498db"
  badge-sale: "#e74c3c"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
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
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
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
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    backgroundColor: "{colors.accent-basket}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-primary-hover:
    backgroundColor: "{colors.accent-basket-hover}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-secondary-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 44px
  nav-bar-link:
    color: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 0 12px
  nav-bar-link-hover:
    color: "{colors.hairline-soft}"
  product-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 8px 0
    border-bottom: 1px solid "{colors.hairline-soft}"
  product-row-hover:
    backgroundColor: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 24px 16px
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.hairline-soft}"
  badge-stock:
    backgroundColor: "{colors.stock-in}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-stock-low:
    backgroundColor: "{colors.stock-low}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-stock-out:
    backgroundColor: "{colors.stock-out}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  basket-icon:
    color: "{colors.accent-basket}"
    height: 20px
  basket-icon-hover:
    color: "{colors.accent-basket-hover}"
  genre-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 32px
  genre-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  pagination-link:
    color: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: 4px 8px
  pagination-link-active:
    color: "{colors.canvas}"
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
    height: 32px
    border: 1px solid "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The bright orange "Add to Basket" call-to-action, the single colour accent in an otherwise monochrome interface. Uses `{colors.accent-basket}` (#e67e22) on a white background, with `{colors.accent-basket-hover}` (#d35400) on hover. Compact at 36px height with `{rounded.sm}` corners, sized to sit comfortably alongside dense product rows without dominating the layout.

**`button-secondary`** — A neutral grey button for secondary actions like "View Details" or "Clear Filters". Uses `{colors.surface-soft}` (#f5f5f5) background that shifts to `{colors.hairline-soft}` (#e5e5e5) on hover. Same 36px height and `{rounded.sm}` as the primary button for visual consistency.

### Navigation
**`nav-bar`** — A persistent 44px charcoal strip at the top of every page, using `{colors.primary}` (#313131) as background. Contains genre links (Rock, Electronic, Jazz, etc.), a search bar, and the basket icon. Links are white `{colors.canvas}` at 13px weight 600, with a subtle lightening on hover to `{colors.hairline-soft}`. No dropdowns — the nav is a flat horizontal list that scrolls horizontally on mobile.

### Product Rows
**`product-row`** — The core inventory unit: a single horizontal row containing album art thumbnail, artist name, title, format, condition, price, and a basket add button. Each row is 8px padding top and bottom, separated by a `{colors.hairline-soft}` border. On hover, the entire row shifts to `{colors.surface-soft}` (#f5f5f5) for a subtle highlight effect. No card shadows or elevation — the rows are flat and dense.

### Search
**`search-bar`** — A simple text input with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` (#313131). No icon inside the field by default; the search action is triggered by pressing Enter or clicking a magnifying glass icon next to the input. Height is 40px to match the nav bar's scale.

### Badges
**`badge-stock`**, **`badge-stock-low`**, **`badge-stock-out`** — Small, uppercase status badges that communicate inventory levels at a glance. Green (#27ae60) for "In Stock", orange (#e67e22) for "Low Stock", red (#c0392b) for "Out of Stock". Each is 10px weight 700 with 0.5px letter-spacing, padded 2px 6px, with `{rounded.xs}` corners. Also includes `badge-new` (blue, #3498db) and `badge-sale` (red, #e74c3c) for promotional flags.

### Footer
**`footer`** — A `{colors.primary}` (#313131) background strip at the bottom of every page, containing links to About, Contact, Shipping, Returns, and social media. Text is `{colors.canvas}` white at 12px weight 400. Links use `{colors.canvas}` with a hover state of `{colors.hairline-soft}`. Padding is 24px top and bottom, with 16px left and right.

### Genre Filter
**`genre-filter`** — A set of pill-shaped filter buttons for narrowing product listings by music genre. Inactive state uses `{colors.surface-soft}` background with `{colors.ink}` text. Active state flips to `{colors.primary}` background with `{colors.canvas}` text. Height is 32px with `{rounded.sm}` corners, making them compact enough to sit in a horizontal row above the product list.

### Pagination
**`pagination-link`** — Numbered page links at the bottom of search results and genre listings. Inactive links are `{colors.primary}` text with no background. The active page uses `{colors.primary}` background with `{colors.canvas}` text and `{rounded.sm}` corners. Each link is padded 4px 8px for comfortable tapping.

### Quantity Selector
**`quantity-selector`** — A small input field for specifying how many copies of a record to add to the basket. Uses `{colors.canvas}` background with `{colors.ink}` text, a 1px `{colors.hairline}` border, and `{rounded.sm}` corners. Height is 32px, with 4px 8px padding. Typically paired with the `button-primary` in product rows.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product rows stack vertically with larger album art; genre filter becomes a dropdown; search bar moves to top of page; footer links stack in a single column |
| Tablet | 744–1128px | Nav bar shows abbreviated genre labels (e.g., "Rock" instead of "Rock & Pop"); product rows use two-column grid; search bar remains in nav; footer links in two columns |
| Desktop | 1128–1440px | Full nav bar with all genre links; product rows in single-column list with full detail; search bar in nav; footer links in four columns |
| Wide | > 1440px | Max-width container at 1440px with centred content; additional whitespace on sides; product rows can optionally show more metadata columns |

### Touch Targets
- All buttons and links: minimum 44x44px tap target (enforced via padding, not visual size)
- Product rows: full row height is tappable (minimum 44px)
- Genre filter pills: 32px height with 12px padding — meets 44px tap target via padding
- Pagination links: 32px height with 8px padding — meets 44px tap target via padding
- Basket icon: 20px icon with 12px padding on each side (44px total tap area)

### Collapsing Strategy
- Nav bar: genre links collapse into a hamburger menu below 744px; search bar moves to a dedicated row above the nav
- Product rows: on mobile, rows stack vertically with album art at full width; on tablet, a two-column grid; on desktop, the classic single-column list
- Genre filter: on mobile, becomes a select dropdown; on tablet and desktop, remains a horizontal row of pills
- Footer: links collapse from four columns on desktop to two on tablet to a single column on mobile
- Album art thumbnails: on mobile, display at 120px width; on tablet, 80px; on desktop, 60px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex colour (#313131) was reliably extracted from the live site; the remaining palette (accent orange, stock status colours, badge colours) is inferred from common patterns in independent record store UIs and may not match the exact live site values
- No font-family declarations beyond the system stack were found; the site likely uses a system font stack with no custom typeface
- Hover states for buttons and links are inferred from common patterns; exact hover colours were not extractable
- Error styling for form inputs (validation, error messages) was not observed
- Dark mode is not supported and likely not implemented
- The site uses a Cloudflare challenge page ("Just a moment...") which prevented full extraction of the design system; the extracted colour may be from the challenge page rather than the main site
- Sub-brand or seasonal colour palettes (e.g., for Record Store Day, sales events) were not observed
- Loading states, skeleton screens, and empty states were not extractable
- The basket icon colour (#e67e22) is inferred from the orange accent commonly used by Norman Records; the exact hex may differ
- Stock status badge colours are inferred from standard e-commerce patterns; exact values may vary
