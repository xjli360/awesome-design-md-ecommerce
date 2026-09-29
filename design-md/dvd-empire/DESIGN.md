---
version: alpha
name: "DVD Empire"
source_url: "https://www.dvdempire.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-catalog movie marketplace that wears its e-commerce heritage openly — #428bca is the primary voltage, a saturated cerulean that appears in every primary button, navigation link, and category header, set against a near-black ink (#080808) and a scaffold of warm grays (#eeeeee, #f5f5f5, #e7e7e7) that give the page a well-worn, utilitarian feel. The brand's accent palette is unusually vivid for a media retailer: a marigold #f2ea2c and its deeper sibling #e7c603 power sale badges and price highlights, while a traffic-light trio of green (#468847), amber (#c09853), and red (#b94a48) signals stock status and messaging — a system borrowed from admin dashboards rather than consumer design. The typography stack is resolutely system-native (Arial, Helvetica, sans-serif), with no custom typeface investment; the brand trusts dense information architecture over typographic personality. Buttons use sharp {rounded.sm} corners, product thumbnails sit in tight grids with {rounded.xs} borders, and the header carries a full-width utility bar in #080808 with white links — a classic two-tier nav that prioritizes categories (DVD, Blu-ray, 4K, New Releases) over brand storytelling. The checkout flow introduces a secondary blue (#076aab) and a purple (#491a79) that suggest third-party payment integrations rather than intentional brand extension. DVD Empire feels like a store that has been running since the early 2000s and never saw a reason to redesign — its charm is in its directness, its dense data density, and the honest way it shows you every price, format, and stock badge without apology.

colors:
  primary: "#428bca"
  primary-active: "#2a6496"
  primary-disabled: "#bce8f1"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#757575"
  hairline: "#dadada"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#f2ea2c"
  accent-sale-dark: "#e7c603"
  accent-success: "#468847"
  accent-warning: "#c09853"
  accent-error: "#b94a48"
  accent-info: "#dff0d8"
  accent-info-border: "#d6e9c6"
  accent-warning-bg: "#fbeed5"
  accent-error-bg: "#eed3d7"
  accent-warning-border: "#fbba73"
  accent-orange: "#f48618"
  accent-blue-dark: "#076aab"
  accent-purple: "#491a79"
  surface-dark: "#303030"
  surface-gray: "#505050"
  surface-light: "#f1f1f1"
  surface-medium: "#6a6a6a"
  surface-border: "#c8c8c8"
  surface-strong: "#eeeeee"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
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
    padding: 6px 12px
    height: 34px
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
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 5px 12px
    height: 34px
  button-success:
    backgroundColor: "{colors.accent-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-danger:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-warning:
    backgroundColor: "{colors.accent-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  button-sale:
    backgroundColor: "{colors.accent-sale-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  text-input-focus:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 40px
  sub-nav:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 36px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.accent-error}"
    typography: "{typography.price}"
  product-card-sale-price:
    backgroundColor: transparent
    textColor: "{colors.accent-sale-dark}"
    typography: "{typography.price}"
  product-card-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-card-stock-badge:
    backgroundColor: "{colors.accent-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-card-out-of-stock:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 34px
  category-strip:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  alert-success:
    backgroundColor: "{colors.accent-info}"
    textColor: "{colors.accent-success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  alert-error:
    backgroundColor: "{colors.accent-error-bg}"
    textColor: "{colors.accent-error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  alert-warning:
    backgroundColor: "{colors.accent-warning-bg}"
    textColor: "{colors.accent-warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  pagination-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in #428bca with white text and {rounded.sm} corners. Used for "Add to Cart", "Search", and primary navigation actions. On hover, shifts to #2a6496 (`{colors.primary-active}`). Disabled state uses a pale blue #bce8f1 with muted text. **`button-secondary`** — A white button with #555555 text and a 1px #dadada border, used for secondary actions like "View Details" or "Clear Filters". **`button-success`** — Green background (#468847) for positive actions like "In Stock" confirmations or checkout progression. **`button-danger`** — Red background (#b94a48) for destructive actions like "Remove from Cart". **`button-warning`** — Amber background (#c09853) for cautionary actions. **`button-sale`** — Deep gold background (#e7c603) with black text, used exclusively for sale-related CTAs and price-drop alerts.

### Cards
**`product-card`** — A minimal white card with {rounded.xs} corners and a 1px #dadada border. Contains a product thumbnail, title in `{typography.title-sm}` with #080808 text, and pricing information. The card uses no shadow — the brand relies on grid density and border separation rather than elevation. **`product-card-badge`** — A bright yellow (#f2ea2c) pill badge with black text, positioned at the top-left of the product image to indicate "Sale" or "Deal". **`product-card-stock-badge`** — Green (#468847) badge indicating "In Stock". **`product-card-out-of-stock`** — Red (#b94a48) badge for "Out of Stock" items. Price display uses `{typography.price}` in red (#b94a48) for standard pricing, or `{typography.price}` in gold (#e7c603) for sale prices.

### Navigation
**`top-nav`** — A full-width utility bar in #080808 with white text, 40px height, containing account links, cart status, and customer service links. Links use `{typography.nav-link}` at 13px bold. **`sub-nav`** — A secondary navigation bar in #eeeeee with #555555 text, 36px height, containing category links (DVD, Blu-ray, 4K, New Releases, Pre-orders). Active category tabs use `{category-tab-active}` with a #428bca background. **`category-strip`** — A horizontal scrollable strip of category links in #eeeeee, used on the homepage to surface genre categories.

### Forms
**`text-input`** — Standard form input with {rounded.sm} corners, 34px height, 6px 12px padding, and a 1px #dadada border. On focus, the border shifts to #428bca (`{colors.primary}`). **`search-bar`** — A dedicated search input matching the `text-input` dimensions, paired with a `search-button` in #428bca. The search form is prominently placed in the sub-nav area.

### Alerts
**`alert-success`** — Pale green background (#dff0d8) with green text (#468847) and a #d6e9c6 border, used for success messages like "Item added to cart". **`alert-error`** — Pale red background (#eed3d7) with red text (#b94a48), used for error states. **`alert-warning`** — Pale amber background (#fbeed5) with amber text (#c09853) and a #fbba73 border, used for warnings like "Limited stock".

### Pagination
**`pagination`** — A row of numbered page links in #428bca with {rounded.xs} corners. Active page uses `{pagination-active}` with a #428bca background and white text. Disabled links use `{pagination-disabled}` with #f5f5f5 background and #777777 text.

### Footer
**`footer`** — A full-width footer in #080808 with #777777 body text and #428bca links. Organized in columns for customer service, account info, and company details. Uses `{typography.body-sm}` for content and `{typography.link}` for navigation links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, stacked navigation, hamburger menu replaces top-nav and sub-nav, search bar collapses to icon, category strip becomes horizontal scroll, product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid, top-nav remains visible but condensed, sub-nav collapses to dropdown, search bar remains full-width, category strip shows 4-5 items |
| Desktop | 1128–1440px | Three-column product grid, full top-nav and sub-nav visible, search bar prominently displayed, category strip shows all items, product cards show full metadata |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, additional whitespace on sides, category strip expands to show sub-genres |

### Touch Targets
- All buttons and links maintain minimum 44x44px tap targets on mobile
- Product card thumbnails are tappable with minimum 80x80px area
- Category strip items have 48px minimum height for touch scrolling
- Search bar expands to full width on mobile with 48px height for easy tapping
- Pagination links maintain 44x44px tap targets
- Cart icon and account links in top-nav have 48x48px touch areas

### Collapsing Strategy
- Top-nav collapses to a hamburger menu on mobile, revealing account links, cart, and customer service in a slide-out panel
- Sub-nav collapses to a single "Categories" dropdown on mobile
- Product grid collapses from 4 columns to 1 column on mobile
- Category strip becomes a horizontally scrollable row on tablet and mobile
- Search bar collapses to a search icon that expands on tap on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Product card metadata (format, release date) hides on mobile, shown on hover/expand

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily weighted toward Bootstrap defaults and generic web grays — the true brand identity may include additional accent colors not captured in the extraction. The most distinctive extracted colors (#428bca, #f2ea2c, #491a79) are used as primary, sale, and secondary accent respectively.
- Font stack is entirely system-native (Arial, Helvetica, sans-serif) — no custom typeface was detected. The brand may use a web font that wasn't captured in the extraction.
- Hover and focus states beyond primary button and text input are inferred from common patterns; actual hover colors for secondary buttons, nav links, and badges could not be reliably extracted.
- Error state styling for form validation (border colors, helper text) is not present in the extracted data.
- Dark mode or high-contrast mode variants are not supported in the extracted data.
- The purple (#491a79) and dark blue (#076aab) colors appear in the extraction but their specific usage context (likely third-party payment widgets or checkout integrations) could not be confirmed.
- Spacing values are estimated from common e-commerce patterns; the actual grid and spacing system may differ.
- The product card shadow/elevation system could not be extracted — the site appears to use flat design with border separation rather than shadows.
- Animation and transition timing values (hover transitions, page load animations) are not available.
- The checkout flow design system (multi-step progress, payment forms, address forms) could not be extracted from the homepage data.
