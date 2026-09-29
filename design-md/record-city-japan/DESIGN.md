---
version: alpha
name: "Record City Japan"
source_url: "https://www.recordcity.jp"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dense, information-rich independent record store interface that prioritizes browsability over visual polish — #222222 ink on #ffffff canvas with #3097d1 as the single accent voltage, used sparingly on links, active states, and the checkout CTA. The palette reads like a well-worn price tag: #777777 muted for secondary metadata, #eeeeee surface-soft for table stripes and filter backgrounds, and a full suite of semantic alert colors (#3c763d success, #8a6d3b warning, #a94442 error) that signal inventory status and order conditions rather than brand personality. Typography runs Raleway at modest weights (400 for body, 700 for headings) with monospace fallbacks for tracklist details and catalog numbers — the site trusts dense text layouts and tabular data over hero imagery. Sharp corners dominate: product listings stack in tight grids with {rounded.none} cards separated by #d3e0e9 hairline borders, while the search bar and primary CTA use {rounded.sm} for subtle hierarchy. The overall feel is utilitarian and collector-focused — a digital crate-digger where every pixel serves the task of finding Japanese pressings and rare CDs.

colors:
  primary: "#3097d1"
  primary-active: "#2579a9"
  primary-disabled: "#8eb4cb"
  ink: "#222222"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#d3e0e9"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-strong: "#f5f5f5"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  success: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  error: "#a94442"
  error-bg: "#f2dede"
  error-border: "#ebccd1"
  info: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"
  footer-bg: "#f5f8fa"
  footer-text: "#636b6f"
  near-black: "#030202"
  near-black-alt: "#090909"

typography:
  display-xl:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  catalog-number:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
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
    padding: 8px 16px
    height: 36px
  button-primary-hover:
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
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 50px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-catalog-number:
    typography: "{typography.catalog-number}"
    textColor: "{colors.muted}"
  product-condition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-stock-badge-instock:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-stock-badge-low:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-stock-badge-out:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  filter-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  filter-checkbox:
    width: 16px
    height: 16px
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  pagination-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-link-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.success-border}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.warning-border}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.error-border}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.info-border}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "2px solid {colors.hairline}"
  table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  table-row-hover:
    backgroundColor: "{colors.surface-strong}"
  breadcrumb-link:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  breadcrumb-separator:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Search". Rendered in {colors.primary} (#3097d1) with white text on a {rounded.sm} background. On hover, shifts to {colors.primary-active} (#2579a9). Disabled state uses {colors.primary-disabled} (#8eb4cb) to signal unavailability. **`button-secondary`** — Outlined variant for "Cancel", "Reset Filters", and secondary actions. Uses white background with {colors.ink} text and a {colors.hairline} border. Hover fills background with {colors.surface-soft} and darkens border to {colors.muted}. **`button-success`** and **`button-danger`** — Semantic action buttons for order confirmation and destructive actions, using {colors.success} (#3c763d) and {colors.error} (#a94442) backgrounds respectively.

### Cards & Product Listings
**`product-card`** — The core inventory unit: a sharp-cornered container with a {colors.hairline} border and white background. On hover, the border switches to {colors.primary} to indicate selectability. Inside, the product title uses {typography.title-sm} in {colors.ink}, the price uses {typography.price} for emphasis, and the catalog number renders in monospace ({typography.catalog-number}) in {colors.muted}. Condition and stock status appear as small badges in the top-right corner. **`product-stock-badge-instock`**, **`product-stock-badge-low`**, and **`product-stock-badge-out`** — Semantic badges using the extracted alert color system: green for in-stock, amber for low stock, red for out-of-stock, each with a matching background tint.

### Navigation & Search
**`nav-bar`** — A compact 50px header with white background and a single {colors.hairline} bottom border. Navigation links use {typography.nav-link} (14px, 700 weight) — active links turn {colors.primary}, inactive stay {colors.ink}. **`search-bar`** — A standard text input with {rounded.sm} corners and {colors.hairline} border, paired with **`search-submit`** — a {colors.primary} button that triggers the lookup. The search form sits prominently above product listings.

### Forms & Filters
**`text-input`** and **`select-input`** — Standard form controls with {rounded.sm} corners, {colors.hairline} borders, and 36px height. On focus, the border switches to {colors.primary} with a subtle {colors.primary-disabled} box-shadow ring. **`filter-panel`** — A sidebar or top-bar filtering area on {colors.surface-soft} background. Contains **`filter-checkbox`** — small square checkboxes that fill with {colors.primary} when checked. Filter labels use {typography.title-sm} for clear hierarchy.

### Pagination
**`pagination-link`** — Individual page number buttons with white background, {colors.primary} text, and {colors.hairline} border. The active page uses **`pagination-link-active`** — filled with {colors.primary} and white text. Disabled links use **`pagination-link-disabled`** — grayed out with {colors.muted-soft} text and {colors.hairline-soft} border.

### Alerts & Status Messages
**`alert-success`**, **`alert-warning`**, **`alert-error`**, **`alert-info`** — Four semantic alert variants using the extracted color system. Each has a tinted background, matching text color, and a 1px border in the corresponding hue. Used for order confirmations, stock notifications, error messages, and informational banners.

### Footer
**`footer`** — A full-width footer on {colors.footer-bg} (#f5f8fa) with {colors.footer-text} (#636b6f) body text. Links use {typography.link} styling in the same muted tone. A {colors.hairline} top border separates it from the main content area.

### Tables
**`table-header`** — Table column headers on {colors.surface-soft} with a thicker bottom border. **`table-row`** — Standard rows with alternating white background and {colors.hairline-soft} bottom borders. Hover state uses **`table-row-hover`** with {colors.surface-strong} background for row highlighting.

### Breadcrumbs
**`breadcrumb-link`** — Navigation breadcrumbs with {colors.primary} links, separated by **`breadcrumb-separator`** (typically ">" or "/") in {colors.muted}. The current page uses **`breadcrumb-current`** in {colors.ink} with no link styling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, filter panel collapses to a toggleable drawer, nav-bar reduces to hamburger menu, search bar moves below header, pagination shows "Prev/Next" only |
| Tablet | 744–1128px | Two-column product grid, filter panel remains visible as a collapsible sidebar, nav-bar shows truncated link set, search bar stays in header |
| Desktop | 1128–1440px | Three-column product grid, full filter sidebar, complete nav-bar with all links, full pagination with page numbers |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target area
- Filter checkboxes use 44px tap zones despite 16px visual size
- Pagination links expand to 44px minimum on mobile
- Product cards have full-card tap targets on mobile

### Collapsing Strategy
- Filter panel collapses to a slide-out drawer on mobile, triggered by a "Filters" button
- Nav-bar collapses to hamburger menu on mobile, with full-height overlay drawer
- Product grid collapses from 4 columns (wide) to 1 column (mobile)
- Search bar moves from inline header position to full-width below header on mobile
- Pagination collapses from numbered pages to "Previous / Next" buttons on mobile
- Footer links collapse from multi-column layout to single-column stacked on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, cards, links) are inferred from common patterns — exact transition durations and box-shadow values not extractable
- Active/focus states for navigation and form elements are approximated — exact focus ring styles may differ
- Typography scale (font sizes, line heights, letter-spacing) is estimated from extracted Raleway usage and typical record-store layout patterns — exact values may vary
- Spacing scale is inferred from common Bootstrap/Laravel defaults — the site may use a different spacing system
- Border radius values are estimated — the site uses mostly sharp corners with subtle rounding on interactive elements
- Dark mode or high-contrast mode styles are not present in the extracted data
- Sub-brand or seasonal color palettes (if any) are not captured
- Animation and transition timing values are unknown
- Icon set and illustration style are not documented — the site likely uses Glyphicons Halflings based on extracted font declarations
- Checkout flow and cart-specific component styles are not fully extractable
- Mobile-specific navigation patterns (hamburger menu, filter drawer) are inferred from common responsive patterns
- The extracted color palette is heavily weighted toward Bootstrap/Laravel defaults (alert colors, table stripes) — the brand's true distinctive accent may be more subtle than the extracted data suggests
