---
version: alpha
name: "DCBS"
source_url: "https://www.dcbservice.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-green #114400 anchor — the color of a comic shop's back-issue wall, of longboxes stacked floor to ceiling — grounds a system otherwise built on cool grays (#f0f4f7, #c9cedb, #242c31) and the quiet authority of sans-serif system fonts. Discount Comic Book Service operates as a utilitarian marketplace where product density and price visibility trump visual flourish: every page is a grid of cover art thumbnails, each one a portal to a variant, a trade, a pre-order. The primary green appears sparingly — in the top nav bar, in the "Add to Cart" button, in the footer — but it carries the entire brand's voltage, a single chromatic promise that this is a place for collectors, not casual browsers. The canvas is a pale blue-gray #f0f4f7, not pure white; cards and surfaces lift into view with #ffffff on #e9eff4, creating a subtle depth that prevents the dense product grids from feeling flat. Borders are drawn in #d4dae0 and #c9cedb, soft enough to recede, present enough to define the thousands of tiny rectangles that organize covers, prices, and stock statuses. Typography runs the system stack at modest sizes — body copy at 14px, prices at 16px, titles at 18px — because the covers themselves do the heavy lifting. There is no hero image, no lifestyle photography, no brand story: just a green bar, a search field, and an infinite scroll of four-color art.

colors:
  primary: "#114400"
  primary-active: "#0c3300"
  primary-disabled: "#8ba67a"
  ink: "#161a1c"
  body: "#242c31"
  muted: "#5e6266"
  muted-soft: "#98a7b6"
  hairline: "#c9cedb"
  hairline-soft: "#d4dae0"
  canvas: "#f0f4f7"
  surface-soft: "#e9eff4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green-dark: "#0c0e0f"
  accent-green-mid: "#222a30"
  accent-gray-dark: "#2c2f31"
  accent-gray-mid: "#353d43"
  accent-gray-light: "#525f6b"
  stock-badge: "#667481"
  preorder-badge: "#114400"
  price-text: "#161a1c"
  savings-text: "#114400"
  sold-out: "#aebbc5"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
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
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-quantity:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-bar-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.price-text}"
    marginTop: "{spacing.xs}"
  product-card-savings:
    typography: "{typography.price-sm}"
    color: "{colors.savings-text}"
    marginTop: "{spacing.xxs}"
  product-card-stock-badge:
    backgroundColor: "{colors.stock-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-preorder-badge:
    backgroundColor: "{colors.preorder-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-sold-out-badge:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  filter-checkbox:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 18px
    width: 18px
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 600
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The single call-to-action in the system, rendered in deep green #114400 with white text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#0c3300). Disabled state uses a muted green-gray `{colors.primary-disabled}` (#8ba67a) with white text. Height is 40px with 10px 20px padding and `{rounded.sm}` corners.

**`button-secondary`** — An outlined variant on white background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Used for "View Details", "Cancel", and secondary actions. Height matches primary at 40px, padding is 9px 19px to account for the border.

**`button-tertiary`** — A text-only button with transparent background and `{colors.primary}` green text. Used for "Clear Filters", "See All", and inline actions where a full button would be too heavy. No border, no background — just the green text on hover underline.

**`button-quantity`** — Small 32x32 square buttons used in cart and product detail quantity selectors. Background is `{colors.surface-soft}` (#e9eff4) with `{colors.body}` text. Uses `{typography.button-sm}` at 12px.

### Cards
**`product-card`** — The fundamental unit of the DCBS interface. A white card on `{colors.surface-soft}` canvas with `{rounded.sm}` corners and 8px padding. Contains a cover image with `{rounded.xs}`, a title in `{typography.title-md}`, a price in bold `{typography.price}`, optional savings text in green, and a stock status badge. Cards are arranged in dense grids with minimal gap — the cover art is the hero, not the card itself.

**`product-card-stock-badge`** — A small uppercase label in `{colors.stock-badge}` (#667481) with white text, `{rounded.xs}` corners, and 2px 6px padding. Reads "IN STOCK" or similar. The muted gray keeps it from competing with the cover art.

**`product-card-preorder-badge`** — Identical shape to stock badge but in `{colors.preorder-badge}` (#114400) green, signaling a future release. The green badge is the only place the brand color appears on a card, making it instantly scannable.

**`product-card-sold-out-badge`** — Uses `{colors.sold-out}` (#aebbc5), a pale gray-blue, to indicate unavailability. The low contrast keeps sold-out items visually recessive.

### Navigation
**`nav-bar`** — A 48px fixed-height bar in `{colors.primary}` green spanning the full viewport width. Links are white, 14px, weight 600, with 16px horizontal padding. Active links get a 2px white bottom border. The bar is deliberately short — it's a utility header, not a brand showcase.

**`search-bar`** — A 44px white input with `{rounded.md}` (8px) corners and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` green. The search is the primary navigation tool — users find comics by title, publisher, or creator, not by browsing categories.

### Forms
**`text-input`** — Standard 40px input with white background, `{colors.body}` text, `{rounded.sm}` corners, and 8px 12px padding. Border is `{colors.hairline}` (#c9cedb). Focus state uses `{colors.primary}` green border. Used in checkout forms, account settings, and filter fields.

**`filter-panel`** — A sidebar or dropdown panel on `{colors.surface-soft}` (#e9eff4) background with `{rounded.sm}` corners and 16px padding. Contains checkboxes, dropdowns, and price range inputs. The soft gray background visually separates filters from the white product grid.

**`filter-checkbox`** — 18x18 white square with `{rounded.xs}` (2px) corners and `{colors.hairline}` border. Checked state fills with `{colors.primary}` green and green border. No custom checkmark — the green fill is the indicator.

### Footer
**`footer`** — A `{colors.primary}` green bar at the bottom of every page, matching the top nav bar. Contains links to policies, contact info, and social icons in white. Padding is 32px vertical, 16px horizontal. Links use `{typography.link}` at 14px weight 400.

### Pagination
**`pagination-button`** — 36px white buttons with `{colors.body}` text, `{rounded.sm}` corners, 6px 12px padding, and a 1px `{colors.hairline}` border. Active page uses `{colors.primary}` green background with white text. Used at the bottom of search results and category pages.

### Dividers
**`divider`** — A 1px line in `{colors.hairline}` (#c9cedb). Used between sections in the filter panel, between product rows, and in the footer. The cool gray is unobtrusive but present — it organizes without adding visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; filter panel becomes a slide-out drawer; search bar moves below nav; product cards stack vertically with full-width images; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav bar shows top-level links but collapses secondary items; filter panel remains sidebar but narrower; search bar stays in nav; product cards show 2-across with smaller images |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; filter panel is a persistent left sidebar; search bar is full-width in nav; product cards show 3-across with medium images; pagination is fully visible |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with centered layout; filter panel remains sidebar; product cards show 4-across; additional whitespace on sides; pagination centered with extra spacing |

### Touch Targets
- All buttons and interactive elements are minimum 40px height on mobile
- Filter checkboxes are 44x44px tap targets (18px visual checkbox with 13px padding)
- Nav bar hamburger icon is 48x48px tap target
- Quantity buttons are 44x44px on mobile (32px visual with 6px padding)
- Product card links have 44px minimum tap height
- Pagination buttons are 44px height on mobile (36px on desktop)

### Collapsing Strategy
- Nav bar: On mobile, all links collapse into a hamburger menu; the green bar shows only the logo/brand name and hamburger icon
- Filter panel: On mobile, filters collapse into a "Filter" button that opens a full-screen drawer; on tablet, filters collapse into a narrower sidebar with scroll
- Product grid: Columns collapse from 4 (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Search bar: On mobile, search collapses to an icon that expands to full-width input on tap
- Footer: On mobile, link columns stack vertically; on tablet, they arrange in 2 columns; on desktop, they spread across 4 columns
- Breadcrumbs: On mobile, breadcrumbs collapse to show only the current page and a "Back" link

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site CSS; only primary button hover and text-input focus are confirmed
- Error state styling (form validation, error messages, input error borders) was not visible in the extracted data
- Active/pressed states for buttons beyond primary are inferred from common patterns, not extracted
- Dark mode or high-contrast mode styles are not present in the extracted data
- Sub-brand or promotional palettes (seasonal sales, variant covers, publisher-specific themes) could not be identified
- Typography scale is inferred from common system font sizes; exact font sizes for every token (e.g., display-xl, caption) are estimated based on typical usage in dense product grids
- The extracted hex list is dominated by cool grays and one distinctive green (#114400); no secondary accent color (e.g., for sale tags, limited editions) was found beyond the green itself
- Animation and transition durations/easing functions were not extractable
- Spacing scale is inferred from common 4px/8px base systems; exact component padding values are estimated
- The extracted font-family list contains only system fallbacks; no custom web font was found on the live site
- Checkout flow components (payment forms, address inputs, order summary) were not extractable from the product browsing pages
- Mobile-specific component variants (e.g., bottom nav, sticky add-to-cart) could not be confirmed from the extracted data
