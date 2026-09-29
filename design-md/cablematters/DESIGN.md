---
version: alpha
name: "CableMatters"
source_url: "https://www.cablematters.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A technical-accessories marketplace that signals reliability through a persistent orange voltage — #f17506 appears on every primary CTA, category badge, and price-highlight, while a secondary #0263c1 blue anchors informational links and secondary actions. The palette is unusually wide for a DTC brand: extracted hexes include #a72d2c (deep burgundy for sale badges), #d20000 (alert red for error states), and #004b91 (dark navy for footer backgrounds), suggesting a system built for information density rather than minimalism. Typography defaults to system sans-serif (Arial/Helvetica stack) at modest sizes — the brand trusts clarity over personality, letting orange and blue do the emotional work. Cards use soft 12px rounding (`{rounded.md}`) while buttons go fully pill-shaped (`{rounded.full}`), creating a hybrid language: rectangular product grids with friendly CTA endpoints. The canvas is off-white #f5f4ef rather than pure white, giving the page a warm paper-like substrate that makes the orange pop harder. Hairlines at #dedede and #d4d4d4 create layered depth in category navigation and product tables, while muted text at #595959 keeps body copy readable without competing with the orange callouts. This is a brand that sells cables and adapters — it doesn't need to be beautiful, it needs to be findable, and the color system prioritizes wayfinding over atmosphere.

colors:
  primary: "#f17506"
  primary-active: "#ec7d04"
  primary-disabled: "#f5c48d"
  ink: "#222222"
  body: "#484848"
  muted: "#595959"
  muted-soft: "#757575"
  hairline: "#dedede"
  hairline-soft: "#e4e4e4"
  canvas: "#f5f4ef"
  surface-soft: "#eaeaea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0263c1"
  accent-blue-dark: "#004b91"
  alert-red: "#d20000"
  sale-burgundy: "#a72d2c"
  badge-orange: "#f38727"
  border-strong: "#a2a2a2"
  border-light: "#d4d4d4"
  footer-bg: "#004b91"
  star-rating: "#f17506"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  link-blue:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    color: "{colors.accent-blue}"
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.sale-burgundy}"

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
  button-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-blue-hover:
    backgroundColor: "{colors.accent-blue-dark}"
    textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  price-display:
    typography: "{typography.price}"
    color: "{colors.ink}"
  price-sale-display:
    typography: "{typography.price-sale}"
    color: "{colors.sale-burgundy}"
  badge-sale:
    backgroundColor: "{colors.sale-burgundy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-category-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.accent-blue}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
  category-strip-item:
    padding: 8px 16px
    color: "{colors.muted}"
  category-strip-item-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.accent-blue}"
    typography: "{typography.caption}"
  breadcrumb-current:
    color: "{colors.ink}"
    typography: "{typography.caption-bold}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    padding: 4px 12px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 36px
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
  add-to-cart-bar-hover:
    backgroundColor: "{colors.primary-active}"
  checkout-button:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  checkout-button-hover:
    backgroundColor: "{colors.accent-blue-dark}"
  alert-banner:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  alert-banner-warning:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  alert-banner-success:
    backgroundColor: "#2e7d32"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  filter-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  filter-checkbox:
    color: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
  filter-checkbox-checked:
    color: "{colors.accent-blue}"
  filter-price-range:
    color: "{colors.primary}"
    typography: "{typography.price}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    padding: 8px 12px
    borderBottom: "2px solid {colors.hairline}"
  table-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 12px
    borderBottom: "1px solid {colors.hairline-soft}"
  table-row-hover:
    backgroundColor: "{colors.canvas}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in CableMatters orange (#f17506) with white text and full pill rounding. Used for "Add to Cart", "Buy Now", and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#ec7d04). Disabled state uses `{colors.primary-disabled}` (#f5c48d) with reduced opacity.

**`button-secondary`** — Outlined variant for secondary actions like "Compare" or "Save for Later". Uses white background with ink text and a 1px hairline border. On hover, background shifts to `{colors.surface-soft}` and border strengthens to `{colors.border-strong}`.

**`button-blue`** — Blue variant for informational actions like "Learn More" or "View Specs". Uses `{colors.accent-blue}` (#0263c1) background. On hover, deepens to `{colors.accent-blue-dark}` (#004b91). Used in footer and informational contexts where orange would compete with primary CTAs.

### Cards
**`product-card`** — White card with 12px rounding and a soft hairline border. Contains product image, title, rating stars, price, and action buttons. On hover, the border switches to `{colors.primary}` orange, providing clear visual feedback. Image area uses `{rounded.sm}` and a soft gray background for loading states.

**`product-card-image`** — Image container within the product card, using `{rounded.sm}` and `{colors.surface-soft}` as placeholder background. Maintains a 1:1 aspect ratio for product photography.

### Navigation
**`nav-bar`** — Fixed top navigation at 56px height with white background and bottom hairline border. Contains logo, category links, search bar, and account/cart icons. Links use `{typography.nav-link}` at 14px weight 600.

**`nav-dropdown`** — Flyout menu for category navigation, white background with 8px padding and 8px rounding. Items use `{typography.body-md}` and show hover state with `{colors.surface-soft}` background.

**`category-strip`** — Secondary navigation below the main nav, 44px height with category pills. Active category shows orange underline and orange text. Inactive items use muted gray. Scrollable horizontally on mobile.

### Forms & Inputs
**`text-input`** — Standard form input with white background, 8px rounding, and hairline border. On focus, border doubles to 2px and switches to `{colors.accent-blue}`. Used for search, quantity, and address fields.

**`search-bar`** — Full pill-shaped search input with 40px height and hairline border. On focus, border switches to 2px `{colors.accent-blue}`. Includes a magnifying glass icon in `{colors.muted}`.

**`quantity-selector`** — Compact input for product quantity, 36px height with 8px rounding and hairline border. Includes minus/plus buttons on either side.

### Badges
**`badge-sale`** — Burgundy (#a72d2c) badge with white uppercase text, 4px rounding, and 2px vertical padding. Used to highlight discounted products. Text uses `{typography.badge}` at 11px weight 700.

**`badge-new`** — Orange (#f17506) badge matching the primary brand color, used for new arrivals or featured products. Same sizing and typography as sale badge.

**`badge-category`** — Pill-shaped category filter badges with soft gray background and muted text. Active state switches to orange background with white text. Used in product listing filters and category navigation.

### Footer
**`footer-section`** — Dark navy (#004b91) footer background with white text at 85% opacity for links. Contains multiple columns of category links, support links, and company information. Padding at 32px vertical, 16px horizontal.

**`footer-link`** — White text at 85% opacity, using `{typography.link}` at 14px. On hover, opacity increases to 100%. Underline appears on hover for accessibility.

### Alerts & Status
**`alert-banner`** — Full-width red (#d20000) banner for error messages and critical alerts. White text at `{typography.body-sm}`. Includes dismiss button.

**`alert-banner-warning`** — Orange (#f17506) banner for warnings and informational alerts. Same structure as error banner but using brand orange.

**`alert-banner-success`** — Green (#2e7d32) banner for success messages like "Added to Cart" confirmations. Same structure as other alert banners.

### Tables
**`table-header`** — Gray background (#eaeaea) header row with bold 12px text and 2px bottom border. Used in specification comparison tables and order history.

**`table-row`** — White row with 12px padding and soft bottom hairline. On hover, background shifts to `{colors.canvas}` (#f5f4ef). Alternating row backgrounds are not used — hover is the primary row differentiation.

### Pagination
**`pagination`** — Numbered page navigation using `{typography.body-sm}` in muted gray. Active page uses orange pill background with white text. Previous/next arrows use `{colors.muted}` with hover state in `{colors.ink}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, category strip collapses to scrollable row, footer stacks vertically, search bar becomes full-width below nav |
| Tablet | 744–1128px | 2-column product grid, top nav shows limited categories with "More" dropdown, category strip fully visible, footer in 2-column layout |
| Desktop | 1128–1440px | 3-4 column product grid, full top nav with all categories, category strip with all pills visible, footer in 4-column layout |
| Wide | > 1440px | 4-5 column product grid, max-width container at 1440px, additional whitespace on sides, larger product card images |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Product card CTAs are minimum 48px height
- Category strip items are minimum 44px height with 16px horizontal padding
- Filter checkboxes have 24px minimum touch area
- Quantity selector buttons are 36x36px minimum

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-out drawer for categories
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Product comparison tables become horizontally scrollable on mobile, or collapse to list view
- Footer link columns collapse to accordion sections on mobile, with expandable headers
- Category strip items collapse to a horizontal scroll container on mobile, hiding overflow
- Search bar collapses from inline to full-width below the nav on mobile
- Breadcrumbs truncate to show only current page and "Home" on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors are heavily weighted toward grays and blues, with #f17506 orange as the only distinctive brand accent — the true brand palette may include additional secondary colors not captured in the extraction
- Font-family extraction returned only system fonts (Arial/Helvetica) — the brand may use a custom web font that wasn't detected in the scan
- Hover and focus states for most components are inferred from common patterns rather than extracted from live CSS
- Error state styling (form validation, error messages) could not be extracted — alert colors are estimated
- Dark mode is not supported and no dark mode colors were extracted
- Sub-brand or product-line-specific color variations (e.g., Thunderbolt vs USB-C categories) were not detected
- Animation and transition durations/easings were not extracted
- Icon system (SVG vs icon font, stroke weights, sizes) was not captured
- Typography scale is estimated based on common e-commerce patterns — actual font sizes may vary
- Spacing scale is inferred from common grid systems — actual spacing tokens may differ
- The extracted color list includes many near-identical grays (#e4e4e4, #eaeaea, #e3e3e3, #dcdcdc) suggesting multiple surface and border variants that couldn't be precisely mapped
- Checkout flow components (payment forms, address validation, order summary) were not accessible for extraction
- Accessibility contrast ratios for text-on-background combinations were not verified
- Print stylesheet behavior is unknown
