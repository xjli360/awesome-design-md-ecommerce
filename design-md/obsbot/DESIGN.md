---
version: alpha
name: "OBSBOT"
source_url: "https://www.obsbot.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage hardware brand that wraps its AI-powered webcams in a #e60033 primary — a confident, almost urgent red that appears on every product badge, add-to-cart button, and promotional banner, signaling motion and attention rather than the muted grays typical of pro AV gear. The site runs on a dense system of Element UI components (the extracted palette reveals #409eff blues, #67c23a greens, #e6a23c ambers, and #f56c6c reds from the framework), but OBSBOT’s own voice cuts through in that specific crimson, the #303133 ink for body text, and a heavy reliance on #c0c4cc and #dcdfe6 hairlines that give product spec tables and comparison grids a crisp, technical feel. Typography leans on Montserrat for headings and Open Sans for body, both served at modest weights (400–600) with generous line spacing — the brand trusts its product photography and spec callouts over decorative type. Product cards use {rounded.sm} corners and thin #e4e7ed borders, while the primary CTA button sits at 40px height with {rounded.sm} and #e60033 fill, turning to #dd6161 on hover. The overall mood is precision-tool meets consumer electronics: clean enough for B2B buyers comparing 4K sensors, but with enough red voltage to feel alive in a shopping feed.

colors:
  primary: "#e60033"
  primary-active: "#dd6161"
  primary-disabled: "#fde6eb"
  ink: "#303133"
  body: "#606266"
  muted: "#909399"
  muted-soft: "#c0c4cc"
  hairline: "#dcdfe6"
  hairline-soft: "#e4e7ed"
  canvas: "#ffffff"
  surface-soft: "#f5f7fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#67c23a"
  warning: "#e6a23c"
  danger: "#f56c6c"
  info: "#909399"
  link-blue: "#409eff"
  link-blue-hover: "#3a8ee6"
  link-blue-soft: "#ecf5ff"
  badge-red: "#e60033"
  badge-green: "#5daf34"
  badge-amber: "#cf9236"
  badge-red-soft: "#fde6eb"
  star-rating: "#f56c6c"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.571
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.538
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.4px
  link:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.571
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.3px

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
  button-primary-hover:
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
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
  text-input-focus:
    borderColor: "{colors.link-blue}"
    boxShadow: "0 0 0 2px {colors.link-blue-soft}"
  text-input-error:
    borderColor: "{colors.danger}"
    boxShadow: "0 0 0 2px {colors.badge-red-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-sticky:
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-body:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    fontWeight: 600
  product-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-soft:
    backgroundColor: "{colors.badge-red-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  search-bar-focus:
    borderColor: "{colors.link-blue}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-link-hover:
    color: "{colors.link-blue}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    fontWeight: 600
  spec-table-row:
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-label:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  spec-table-value:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
  rating-star:
    color: "{colors.star-rating}"
    fontSize: 16px
  rating-star-empty:
    color: "{colors.hairline}"
    fontSize: 16px
  tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  tag-active:
    backgroundColor: "{colors.link-blue-soft}"
    textColor: "{colors.link-blue}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 32px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 32px
  pagination-button-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 32px
  breadcrumb-link:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with #e60033 and set in Montserrat 14px/600 with 0.5px letter spacing. On hover it shifts to #dd6161, and in its disabled state it fades to #fde6eb with muted text. Height is 40px with {rounded.sm} corners, giving it a compact, technical feel appropriate for add-to-cart and pre-order actions. **`button-secondary`** — An outlined variant with white fill and #303133 text, using a 1px #dcdfe6 border. Hover fills the background with #f5f7fa. **`button-text`** — A borderless link-style button in #409eff, used for "Learn More" and "View Specs" actions within product cards. **`button-danger`** — Uses #f56c6c for destructive actions like removing items from a comparison list.

### Text Inputs & Selects
**`text-input`** — Standard form input with white background, #303133 text, and a 1px #dcdfe6 border. On focus, the border turns #409eff with a 2px #ecf5ff box-shadow ring. Error state uses #f56c6c border and #fde6eb ring. Height is 40px with {rounded.xs} corners. **`select-input`** — Matches text-input styling with a custom dropdown arrow in #c0c4cc.

### Navigation
**`nav-bar`** — A 60px white bar with Montserrat 14px/500 nav links in #303133. The bar uses a subtle `box-shadow: 0 2px 8px rgba(0,0,0,0.06)` when sticky. Links have 0.3px letter spacing and transition to #409eff on hover. The brand logo sits left-aligned with the product category dropdowns to its right.

### Product Cards
**`product-card`** — A white card with {rounded.sm} corners and a 1px #e4e7ed border. The image area uses `{rounded.sm} {rounded.sm} 0 0` to match the card's top corners. The body section uses {spacing.md} horizontal and {spacing.base} vertical padding. The title renders in Montserrat 18px/500 (#303133), and the price appears in #e60033 at 16px/600. **`product-badge`** — Small red (#e60033) tags with white text, 11px/600, {rounded.xs}, used for "Sale" and "Best Seller" labels. **`product-badge-new`** — Green (#67c23a) variant for "New Arrivals". **`product-badge-soft`** — A softer red (#fde6eb) with #e60033 text, used for "In Stock" or "Free Shipping" messaging.

### Spec Tables
**`spec-table-header`** — A #f5f7fa background row with Montserrat 18px/600 text in #303133, used as the category header in product comparison tables. **`spec-table-row`** — White rows with a 1px #dcdfe6 bottom border. Labels use #909399 at 14px/400, values use #303133 at 14px/400. Padding is {spacing.md} vertical and {spacing.base} horizontal.

### Search & Filtering
**`search-bar`** — A pill-shaped (#c0c4cc border, {rounded.full}) input with 36px height and 8px/16px padding. On focus the border turns #409eff. Used for site-wide product search. **`tag`** — Small filter tags in #f5f7fa with #606266 text, {rounded.xs}, 2px/8px padding. **`tag-active`** — Active filter state using #ecf5ff background and #409eff text.

### Pagination
**`pagination-button`** — 32px square buttons with white fill and #303133 text. Active state fills with #e60033 and white text. Disabled state uses #e4e4e4 text. All have {rounded.xs} corners.

### Breadcrumbs
**`breadcrumb-link`** — 13px/400 links in #909399, with the active (current page) link in #303133. Separators are #c0c4cc chevrons with 8px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero banner reduces to 32px padding; spec tables become stacked rows; search bar moves to overlay |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level links only; hero uses 48px padding; spec tables remain full-width but reduce font sizes |
| Desktop | 1128–1440px | 3-4 column product grid; full nav with dropdowns; hero at 64px padding; spec tables at full width with 18px headers |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 4 columns; hero uses 80px padding for breathing room |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height on mobile
- Product card tap targets (add-to-cart, quick-view) are at least 48px tall
- Nav hamburger icon is 44x44px with 12px padding
- Search bar height increases to 44px on mobile for better tap targeting

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-out drawer
- Product comparison tables collapse to stacked label-value pairs on mobile
- Footer link columns collapse to accordion sections below 744px
- Hero banner reduces from two-column (image + text) to single-column stack on mobile
- Filter sidebar collapses to a horizontal scrollable tag strip on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors are heavily dominated by Element UI framework defaults (#409eff, #67c23a, #e6a23c, #f56c6c, #909399, #c0c4cc, #dcdfe6, #e4e7ed, #f5f7fa, #f2f6fc, #ecf5ff, #f0f9eb, #fdf6ec, #fef0f0). The brand's true primary (#e60033) was identified as the most distinctive non-framework color, but its exact usage context (hover states, active states, disabled states) is inferred from common patterns rather than extracted.
- No meta theme-color was found — the brand may not use a browser chrome color.
- Font stack is inferred from CSS declarations found; exact font weights and sizes for each typography token are estimated based on common patterns for Montserrat/Open Sans pairings.
- Hover states for all components (beyond primary button) are estimated.
- Error, success, and warning form states beyond the extracted danger red (#f56c6c) and success green (#67c23a) are not confirmed.
- Dark mode is not present on the live site.
- Sub-brand or product-line-specific palettes (e.g., OBSBOT Tiny, OBSBOT Tail) are not extracted.
- Animation durations, easing curves, and transition properties are not extracted.
- The site uses Japanese page titles and may have locale-specific styling that was not captured.
