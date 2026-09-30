---
version: alpha
name: "Collectors Anime"
source_url: "https://www.collectorsanime.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's marketplace that wears its blue-collar anime fandom on its sleeve, anchored on a warm gray canvas (#f7f7f7) and a primary blue (#003399) that reads more like a vintage import-shop awning than a tech startup's CTA. The palette is a study in contrast: the deep navy ink (#414141) of product descriptions sits against soft silver surfaces (#f0f0f0, #e5e5e5), while a single accent of safety green (#116600) and a rare flash of caution yellow (#ffff00) appear on price tags and limited-stock badges — colors borrowed from industrial labeling rather than brand guidelines. Typography runs Open Sans at modest weights (400–600), with display sizes staying below 24px; the brand trusts its product photography and dense information architecture over typographic drama. Navigation is a straightforward horizontal bar with a search field that uses a soft corner ({rounded.sm}) and a subtle border (#e5e5e5), while product cards stack in a clean grid with generous padding ({spacing.base}) and a faint shadow that lifts them off the canvas. The overall feel is that of a well-organized warehouse — utilitarian, trustworthy, and built for the collector who knows exactly what they're looking for.

colors:
  primary: "#003399"
  primary-active: "#2a6496"
  primary-disabled: "#969696"
  ink: "#414141"
  body: "#474747"
  muted: "#777777"
  muted-soft: "#969696"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f7f7f7"
  surface-soft: "#f0f0f0"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  accent-green: "#116600"
  accent-yellow: "#ffff00"
  accent-blue-light: "#54afe9"
  accent-gray-dark: "#3d3d3d"
  accent-gray-mid: "#505050"
  accent-gray-light: "#c0c0c0"
  link-blue: "#428bca"
  link-blue-hover: "#2a6496"
  error-red: "#c13515"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.53
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.42
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  price-tag:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0

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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-tag}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-stock-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.on-primary}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    linkColor: "{colors.link-blue}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xl} {spacing.section}"
    minHeight: 200px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Sign In". Uses the brand's deep blue (#003399) with white text and a subtle 4px corner. On hover, shifts to a lighter blue (#2a6496). Disabled state drops to a muted gray (#969696) with reduced opacity.

**`button-secondary`** — An outlined alternative for "View Details" and "Cancel" actions. Uses a white background with the ink text color and a 1px hairline border. Hover adds a subtle shadow. Disabled state uses muted-soft text and a lighter border.

**`button-accent-green`** — A compact, high-urgency button reserved for "In Stock" notifications and "Buy Now" quick actions. Uses the safety green (#116600) with white text and a smaller 32px height.

### Cards
**`product-card`** — The primary content container for the product grid. A white card with a soft 4px corner, 16px padding, and a faint drop shadow. Contains an image, title, price, and optional badges. On hover, the shadow deepens slightly and a subtle scale transform is applied.

**`product-card-badge`** — A small yellow (#ffff00) label pinned to the top-left of a product card, used for "Sale", "Clearance", or "Limited Edition" flags. Uses bold 11px type with tight tracking.

**`product-card-stock-badge`** — A green (#116600) badge indicating "In Stock" or "Low Stock" status. Positioned opposite the sale badge, typically top-right.

### Navigation
**`nav-bar`** — A fixed-height 56px bar with a white background and a 1px bottom border. Contains the brand logo on the left, category links in the center, and user actions (search, cart, account) on the right. Active links are underlined with a 2px primary-blue border.

**`search-bar`** — A text input styled as a search field with a magnifying glass icon on the left. Uses a white background, 4px corners, and a hairline border. On focus, the border thickens to 2px primary blue.

### Filters
**`category-filter`** — A pill-shaped filter chip used in the sidebar or above the product grid. Inactive chips use a soft gray background (#f0f0f0) with ink text. Active chips flip to primary blue with white text. Multiple chips can be selected simultaneously.

### Footer
**`footer`** — A dark bar (#414141) at the bottom of every page containing links, copyright, and social icons. Text is a muted gray (#969696) that brightens to white on hover. Links are spaced generously with 24px gaps.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, collapsed nav into hamburger menu, search bar moves to top, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, sidebar filters become a horizontal scroll strip |
| Desktop | 1128–1440px | Three-column product grid, full nav with dropdowns, persistent sidebar filters, hero banner at full height |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner expands to fill width with max-height constraint |

### Touch Targets
- All interactive elements (buttons, links, filter chips) maintain a minimum 44px touch target height
- Product card images are tappable and link to product detail pages
- Nav bar items have 48px touch height on mobile
- Filter chips are 32px tall but padded to 44px touch area

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer
- The sidebar category filter collapses into a horizontal scrollable strip at the top of the product grid
- The hero banner reduces to a single line of text with a background color, removing any illustration or secondary copy
- The footer's multi-column layout stacks into a single column with accordion-style expandable sections

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale) are inferred from common patterns; exact values not extracted
- Error styling for form inputs (border color, icon placement) not observed on live site
- The extracted color list is dominated by grays and blues; the brand's true accent palette may include additional colors not captured in the extraction
- Font stack is inferred from extracted declarations; the brand may use a custom font not present in the extraction
- Dark mode is not implemented on the live site
- Sub-brand or seasonal color palettes (e.g., holiday themes, exclusive drops) are not documented
- Animation durations and easing curves are not extracted
- The brand's logo and icon set are not captured in this design system
- Checkout flow styling (Shopify Pay, Klarna, Afterpay widgets) is excluded as it uses third-party defaults
