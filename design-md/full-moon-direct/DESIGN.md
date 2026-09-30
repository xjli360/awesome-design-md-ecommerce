---
version: alpha
name: "Full Moon Direct"
source_url: "https://www.fullmoondirect.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-dark e-commerce bazaar for cult genre cinema, where #080808 ink fights #f5f5f5 canvas and the only consistent brand voltage is a muted #337ab7 blue that appears on every link, every CTA, every clickable word — a relic of the Bootstrap era that Full Moon Direct never bothered to override, and somehow that indifference is the brand. The page title announces "Adult. Sexy. Rare." in all-caps, and the design follows suit: a dense, text-heavy layout where #777777 body text on #ffffff canvas does the heavy lifting, punctuated by #5cb85c green success badges, #d9534f red error signals, and #f0ad4e amber warnings that feel borrowed from an admin dashboard rather than a storefront. Navigation is a horizontal strip of #e7e7e7 pills with #555555 text, each category a clickable slab — no drop shadows, no rounded corners beyond `{rounded.xs}`, no hero imagery, no product cards with padding. The brand's visual language is aggressively flat: #eeeeee section dividers, #e5e5e5 table borders, #fcf8e3 alert backgrounds. Every component reads like it was built in 2012 and left untouched, which is exactly the point — Full Moon Direct doesn't need to be beautiful, it needs to be browsable, and the #337ab7 link blue is the only wayfinding the user gets.

colors:
  primary: "#337ab7"
  primary-active: "#286090"
  primary-disabled: "#9d9d9d"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#5cb85c"
  success-bg: "#dff0d8"
  success-border: "#3c763d"
  info: "#5bc0de"
  info-bg: "#d9edf7"
  warning: "#f0ad4e"
  warning-bg: "#fcf8e3"
  warning-border: "#8a6d3b"
  danger: "#d9534f"
  danger-bg: "#f2dede"
  danger-border: "#a94442"
  link-hover: "#23527c"
  link-visited: "#2b542c"
  nav-bg: "#f8f8f8"
  nav-border: "#e7e7e7"
  nav-text: "#555555"
  nav-active-bg: "#e7e7e7"
  nav-active-text: "#555555"
  footer-bg: "#080808"
  footer-text: "#9d9d9d"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.danger}"
  meta:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    color: "{colors.muted}"

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
  button-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 8px rgba(51, 122, 183, 0.6)"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 50px
    borderBottom: "1px solid {colors.nav-border}"
  nav-item:
    backgroundColor: transparent
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    padding: "15px 15px"
  nav-item-active:
    backgroundColor: "{colors.nav-active-bg}"
    textColor: "{colors.nav-active-text}"
    typography: "{typography.nav-link}"
    padding: "15px 15px"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.none}"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    color: "{colors.danger}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.success-bg}"
    color: "{colors.success-border}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-danger:
    typography: "{typography.badge}"
    backgroundColor: "{colors.danger-bg}"
    color: "{colors.danger-border}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-warning:
    typography: "{typography.badge}"
    backgroundColor: "{colors.warning-bg}"
    color: "{colors.warning-border}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 34px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 34px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.footer-text}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "15px"
    border: "1px solid {colors.success}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "15px"
    border: "1px solid {colors.info}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "15px"
    border: "1px solid {colors.warning}"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "15px"
    border: "1px solid {colors.danger}"
  table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: "8px"
    borderBottom: "2px solid {colors.hairline}"
  table-cell:
    padding: "8px"
    borderTop: "1px solid {colors.hairline-soft}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  pagination-disabled:
    color: "{colors.muted-soft}"
    cursor: not-allowed

## Components

### Buttons
**`button-primary`** — The default CTA across the site, a #337ab7 blue slab with white text and `{rounded.xs}` corners. On hover it shifts to #286090. Disabled state fades to #9d9d9d. Height is a compact 34px with 6px 12px padding — no pill shapes, no gradients, no shadows. The same base style is reused for success (green), danger (red), and warning (amber) variants, each mapping to a semantic state: add-to-cart, delete, or flag. A `button-link` variant strips all background and border, rendering as plain #337ab7 text — used for "View Details" and "Read More" anchors within product listings.

### Navigation
**`nav-bar`** — A 50px fixed-height strip with #f8f8f8 background and a #e7e7e7 bottom border. Items are inline blocks with 15px horizontal padding, #555555 text, and no background until active — then they flip to #e7e7e7. Dropdown menus use a white canvas with `{rounded.xs}` and a `{colors.hairline}` border. The nav is the primary wayfinding mechanism; there is no sticky header, no mega-menu, no search bar in the nav itself.

### Product Cards
**`product-card`** — A flat white rectangle with no rounding, a `{spacing.base}` padding, and a soft #eeeeee border. The image area is a fixed 200px height with no rounding. Below it, the title uses `{typography.title-sm}` in #080808, the price uses `{typography.price}` in #555555, and sale prices render in #d9534f. Badges appear as small colored pills: green for "In Stock", red for "Sold Out", amber for "Pre-Order". The card has no hover state, no shadow, no overlay — it's a functional container, not a visual object.

### Forms
**`text-input`** — A 34px tall input with `{rounded.xs}`, a `{colors.hairline}` border, and `{typography.body-md}`. On focus, the border turns #337ab7 and a blue box-shadow appears (rgba(51, 122, 183, 0.6)). Select inputs share the same dimensions and styling. The search bar is identical to a text input but paired with a `search-submit` button that uses `button-primary` styling. There are no floating labels, no animated placeholders, no custom select arrows.

### Alerts
**`alert-success`**, **`alert-info`**, **`alert-warning`**, **`alert-danger`** — Four semantic alert boxes, each with a light background, a colored border, and `{rounded.xs}`. Success uses #dff0d8 / #3c763d, info uses #d9edf7 / #5bc0de, warning uses #fcf8e3 / #8a6d3b, danger uses #f2dede / #a94442. All have 15px padding and `{typography.body-md}`. These appear above product listings for stock notifications, shipping updates, and error messages.

### Tables
**`table`** — A bordered table with `{colors.hairline}` outer border, `{colors.hairline-soft}` row dividers, and a #f5f5f5 header row. Header cells use `{typography.button-sm}` with a 2px bottom border; data cells use `{typography.body-sm}`. Used on product detail pages for specs, on checkout for order summaries, and on account pages for order history.

### Pagination
**`pagination`** — A horizontal list of page numbers, each a `{rounded.xs}` pill with a `{colors.hairline}` border and #337ab7 text. The active page inverts to #337ab7 background with white text. Disabled pages (first, last, or ellipsis) render in #9d9d9d with `cursor: not-allowed`. No arrow icons, no "Previous/Next" labels — just bare numbers.

### Footer
**`footer`** — A #080808 full-width strip with #9d9d9d text, `{typography.body-sm}`, and `{spacing.xl}` vertical padding. Links are the same muted gray with no underline. The footer contains copyright text, a link to the privacy policy, and a link to the terms of service. No newsletter signup, no social icons, no sitemap columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Nav collapses to hamburger; product cards stack single-column; tables scroll horizontally; search bar moves below nav; footer text stacks vertically |
| Tablet | 768–992px | Nav items shrink padding; product cards display 2-column grid; tables remain full-width; search bar stays in nav row |
| Desktop | 992–1200px | Nav items full padding; product cards display 3-column grid; tables normal; search bar in nav row |
| Wide | > 1200px | Max-width container (1170px) centered; product cards display 4-column grid; no other changes |

### Touch Targets
- All buttons and links maintain minimum 34px height (touch-compliant for 48px target on mobile).
- Nav items on mobile expand to full-width, 44px height tap targets.
- Pagination links remain 34px tall — no mobile-specific size increase.

### Collapsing Strategy
- Top nav collapses to a hamburger toggle on screens below 768px. The dropdown menu overlays the content area with a white background.
- Product card grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Tables collapse to a stacked card layout on mobile: each row becomes a bordered block with labels inline.
- Footer links stack vertically on mobile, centered.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by Bootstrap defaults (#337ab7, #5cb85c, #d9534f, #f0ad4e, #5bc0de) and generic grays — the brand's true primary may be one of these, but it's indistinguishable from framework scaffolding. No distinctive brand color (pink, orange, purple) was found.
- Font-family declarations are all system stacks (Arial, Helvetica, Courier New) — no custom or brand-specific typeface was detected. The brand likely uses no web font.
- No hover, focus, or active states were extractable beyond the Bootstrap defaults. The `button-primary-hover` and `text-input-focus` tokens are inferred from Bootstrap conventions.
- No dark mode, high-contrast, or reduced-motion media queries were found.
- No icon system or SVG sprite was detected — the site likely uses Unicode characters or no icons at all.
- No animation, transition, or micro-interaction tokens were extractable.
- No spacing or layout grid system was confirmed — the `spacing` tokens are generic estimates.
- No typography scale beyond the system stack was found — all font sizes are inferred from common Bootstrap defaults.
- The "Adult. Sexy. Rare." tagline appears in the page title but no corresponding visual treatment (badge, hero text, etc.) was found in the extracted data.
- No checkout flow, cart drawer, or payment form components were extractable — these may use Shopify's default UI if the site migrates to Shopify in the future.
