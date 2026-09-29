---
version: alpha
name: "Princeton Record Exchange"
source_url: "https://www.prex.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dense, joyful clutter of used vinyl, CDs, and ephemera organized on a near-white canvas (#fefefe) with a sharp yellow (#ffdd00) that acts as the store’s visual shout — sale tags, price stickers, and the occasional header badge all borrow this same high-frequency accent, while a secondary orange (#f58220) and a cautionary red (#d94a00) handle urgency and markdown tiers. The site reads like a well-loved physical bin: dark ink (#1f1f1f) for headings, a softer body (#555555) for descriptions, and a full gray spectrum from hairline (#e4e4e4) through muted (#aaaaaa) to deep charcoal (#222222) for the footer and structural bones. Navigation is utilitarian — a single row of genre links (Rock, Jazz, Classical, etc.) in a sans-serif stack that defaults to system fonts, with no decorative flourishes beyond the occasional `{rounded.sm}` button. The search bar sits prominently at the top, a wide white field with a blue accent (#0089ec) for the submit action, hinting at a database-driven inventory rather than a curated editorial shop. Product cards are simple: a thumbnail, a title in bold black, a price in yellow or orange, and a condition badge. There is no hero carousel, no lifestyle photography — just rows of records, priced and labeled, waiting to be flipped through.

colors:
  primary: "#ffdd00"
  primary-active: "#e6c700"
  primary-disabled: "#fff4b3"
  ink: "#1f1f1f"
  body: "#555555"
  muted: "#aaaaaa"
  muted-soft: "#bbbbbb"
  hairline: "#e4e4e4"
  hairline-soft: "#eeeeee"
  canvas: "#fefefe"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#1f1f1f"
  accent-orange: "#f58220"
  accent-red: "#d94a00"
  accent-blue: "#0089ec"
  accent-blue-soft: "#b1dcfb"
  badge-sale: "#ee2200"
  badge-new: "#0059bc"
  footer-bg: "#222222"
  footer-text: "#777777"

typography:
  display-xl:
    fontFamily: "site-headings, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "site-headings, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "site-headings, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "site-text, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-lg:
    fontFamily: "site-headings, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-thumbnail:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-condition:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
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
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  genre-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  genre-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature yellow (#ffdd00) with dark ink text. Used for "Add to Cart," "Checkout," and primary form submissions. On hover, shifts to `{colors.primary-active}` (#e6c700). Disabled state fades to a pale yellow with muted text. Height is 40px with `{rounded.sm}` corners.

**`button-secondary`** — A white button with a thin hairline border, used for less prominent actions like "View Details" or "Cancel." Text is dark ink, background is canvas white. Hover adds a subtle shadow or border darkening (not extracted). Disabled state uses muted text and lighter border.

**`button-accent-orange`** — Orange (#f58220) button for medium-urgency actions like "Add to Wishlist" or "Notify Me." White text, same sizing as primary. Hover state darkens the orange (exact hex not extracted).

**`button-accent-red`** — Red (#d94a00) button for high-urgency or destructive actions like "Remove" or "Clear Cart." White text. Hover state darkens to a deeper red.

### Navigation
**`nav-bar`** — A single-row, 48px-tall navigation bar with a white background and a bottom hairline border. Contains genre links (Rock, Pop, Jazz, Classical, etc.) in `{typography.nav-link}`. Active link has a 2px yellow underline (`{colors.primary}`). Inactive links are muted gray. No logo is present in the nav — the store name appears in the page title only.

**`genre-filter`** — Pill-shaped filter buttons for browsing by music genre. Default state is a soft gray background (`{colors.surface-soft}`) with dark ink text. Active state flips to yellow background (`{colors.primary}`) with dark ink text. Used in the sidebar or above the product grid.

### Forms
**`text-input`** — Standard text input with a white background, dark ink text, and a 1px hairline border. Focus state gains a 2px blue border (`{colors.accent-blue}`). Height is 40px with `{rounded.sm}`. Used for search, email signup, and checkout forms.

**`search-bar`** — A wider, 44px-tall text input specifically for the site search. Same styling as `text-input` but paired with a blue submit button (`{colors.accent-blue}`). The search bar is the most prominent interactive element on the page, sitting at the top of the layout.

### Cards
**`product-card`** — A simple card for displaying a record, CD, or other inventory item. Contains a square thumbnail with `{rounded.xs}`, a title in `{typography.title-sm}`, a price in `{typography.price-lg}` colored yellow (`{colors.primary}`), and a condition label in muted gray. Padding is 16px (`{spacing.base}`) with `{rounded.sm}` corners. No shadow or border — relies on the white card against the soft canvas background.

### Badges
**`badge-sale`** — A small, uppercase red badge (#ee2200) with white text, used to flag sale items. `{rounded.xs}` corners with 2px/6px padding. Appears on the top-left corner of product card thumbnails.

**`badge-new`** — A small, uppercase blue badge (#0059bc) with white text, used to flag new arrivals. Same sizing and placement as the sale badge.

### Footer
**`footer`** — A dark footer section (`{colors.footer-bg}` #222222) with muted gray text (`{colors.footer-text}` #777777). Contains links for About, Contact, Shipping, and Returns in `{typography.link}` with a lighter gray hover color (`{colors.muted-soft}`). Padding is 32px horizontal and 48px vertical.

### Pagination
**`pagination-button`** — White button with a 1px hairline border for navigating between pages of search results or inventory. Active page uses the yellow primary background. Inactive pages are white with dark ink text. `{rounded.sm}` with 6px/12px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row). Nav bar collapses to a hamburger menu. Genre filter becomes a horizontal scrollable strip. Search bar moves below the nav. Footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid. Nav bar shows genre links as a scrollable row. Search bar remains at top. Sidebar genre filter becomes optional. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all genre links visible. Search bar at top with full width. Sidebar genre filter visible. Footer in a multi-column layout. |
| Wide | > 1440px | Four-column product grid. Maximum content width of 1440px with centered layout. All elements at their largest comfortable size. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Search bar is 44px tall to meet touch target guidelines.
- Genre filter pills are 32px+ tall with adequate spacing between them.
- Nav links have 48px touch targets (full nav-bar height).

### Collapsing Strategy
- On mobile, the genre navigation strip collapses into a horizontal scrollable row with a "Genres" label.
- The sidebar (if present) collapses into a dropdown or overlay on mobile.
- Product grid columns reduce from 4 to 1 as viewport narrows.
- Footer links stack vertically on mobile, with each section becoming an accordion.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons (beyond primary-active) were not reliably extracted from the live site. The secondary button hover, accent button hovers, and link hovers are inferred from common patterns.
- Error styling for form inputs (red borders, error messages) was not found in the extracted data.
- The exact font family "site-headings" and "site-text" are placeholders — the actual font names could not be resolved from the extracted CSS. The fallback stack is accurate.
- Dark mode is not supported — the site uses a fixed light palette.
- The product card hover state (shadow, border, or scale) was not extracted.
- The checkout flow and cart components were not analyzed — only the browse/inventory pages were visible.
- Sub-brand or seasonal color variations (if any) are unknown.
- The exact spacing values for the product grid (gap between cards) were not extracted — `{spacing.base}` (16px) is an educated guess.
- The yellow (#ffdd00) and orange (#f58220) may have specific semantic meanings (sale vs. new vs. clearance) that could not be confirmed from the extracted data alone.
