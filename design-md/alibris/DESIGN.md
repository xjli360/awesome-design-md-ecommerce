---
version: alpha
name: "Alibris"
source_url: "https://www.alibris.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A near-monochrome book marketplace where #313131 ink does all the heavy lifting — the single extracted color from the live site, a deep charcoal that reads as library-stack seriousness rather than e-commerce cheer. The brand trusts its inventory photography (dust jackets, rare-edition spines, reader hands) to supply all the warmth, keeping its own interface to a disciplined gray scale. Type runs the system font stack — -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif — at modest weights, never competing with the book covers. The search bar, the primary action on every page, sits in a generous {spacing.lg} padded container with {rounded.sm} corners, a soft invitation to browse rather than a hard sell. Category navigation runs as a horizontal strip of text links in {colors.muted}, each book cover thumbnail framed at {rounded.xs} — just enough corner to feel intentional without softening the academic tone. The footer, dense with links to seller resources, genre lists, and company information, reads like a library card catalog translated to web: utilitarian, information-dense, and quietly authoritative. There is no brand color voltage — no pink, no marigold, no teal — just the confidence that the books themselves are the only decoration needed.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#8a8a8a"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6e6e6e"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#0056b3"
  link-visited: "#4a0072"
  badge-sale: "#c62828"
  badge-new: "#2e7d32"
  star-rating: "#f5a623"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    lineClamp: 2
  product-card-author:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    textDecoration: underline
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  filter-panel:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
  filter-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  filter-checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Checkout," and "Sign Up." Uses the brand's deep charcoal {colors.primary} fill with white text in {typography.button-md}. On hover and active, shifts to {colors.primary-active} for a subtle darkening. Disabled state uses {colors.primary-disabled} with full opacity reduction. All states maintain {rounded.sm} corners and a consistent 44px height for touch accessibility.

**`button-secondary`** — A bordered alternative for "Save for Later," "Wishlist," and secondary actions. White background with {colors.primary} text and a 1px {colors.hairline} border. Active state darkens the border to {colors.primary} and adds a {colors.surface-soft} background. Height matches primary at 44px for alignment in form layouts.

**`button-tertiary-text`** — Text-only link-style button for "Cancel," "See All," and inline actions. Uses {colors.link} blue to distinguish from body text. No background or border — relies on the link color and underline on hover for affordance.

**`button-pill`** — A compact, fully rounded button for filter tags, category pills, and "Clear All" actions. Uses {colors.primary} fill with {typography.button-sm} at 36px height. The {rounded.full} shape signals a dismissible or toggleable element.

### Cards
**`product-card`** — The core inventory unit for book listings. A white card with a subtle box shadow and {rounded.xs} corners — just enough rounding to feel intentional without softening the academic tone. On hover, the shadow deepens to indicate interactivity. The card contains a 2:3 aspect ratio image slot, a two-line title in {typography.title-sm}, author name in {typography.caption}, and price in {typography.body-md} at {colors.primary}. Badges for sale or new items sit in the top-left corner.

**`product-card-badge`** — Sale badges use {colors.badge-sale} (deep red) for urgency. New arrival badges use {colors.badge-new} (forest green). Both use {typography.badge} at 11px uppercase with tight tracking, set on {rounded.xs} corners. Positioned absolutely over the card image.

### Navigation
**`nav-bar`** — A 60px fixed header with white background and a subtle bottom border. Contains the brand logo on the left, primary nav links in {typography.nav-link}, and a search icon on the right. Active links get a 2px bottom border in {colors.primary}. The bar collapses to a hamburger menu on mobile.

**`category-strip`** — A horizontal scrollable strip below the nav bar on a {colors.surface-soft} background. Contains genre categories (Fiction, History, Science, etc.) as text links in {colors.muted}. Active categories render as {rounded.full} pills in {colors.primary} with white text.

**`breadcrumb`** — Simple text-based navigation path in {typography.caption} at {colors.muted}. Active (current) page in {colors.ink}. Separators are simple angle brackets in {colors.muted-soft}. No background or border.

### Forms
**`text-input`** — Standard text entry for search, email, and address fields. White background with 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border thickens to 2px {colors.primary}. Error state uses {colors.badge-sale} border. Height is 44px for touch targets.

**`search-bar`** — The primary search input, larger than standard text inputs at 48px height. Same visual treatment as text-input but with a search icon inset on the left. On focus, the border thickens to 2px {colors.primary}. Used on the homepage hero and in the nav bar.

**`filter-checkbox`** — Small square checkbox with {rounded.xs} corners and a 1px {colors.hairline} border. Checked state fills with {colors.primary}. Used in the filter panel for genre, condition, and price range selections.

### Footer
**`footer`** — A dense, information-rich footer on {colors.primary} background with white text. Contains columns for Company Info, Customer Service, Genre Lists, and Seller Resources. Headings use {typography.title-sm}, links use {typography.link} with underline on hover. Padding is generous at {spacing.xxl} top/bottom and {spacing.section} sides.

### Pagination
**`pagination`** — Page number links in {typography.body-sm} at {colors.muted}. Active page gets a {colors.primary} background with white text in a {rounded.sm} pill. Hover state adds a {colors.surface-soft} background. Previous/Next arrows sit outside the numbered list.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger; product cards stack vertically; search bar reduces to icon; category strip becomes a dropdown; footer stacks columns; pagination shows "Prev/Next" only |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows text links for top 4 items; category strip scrolls horizontally; filter panel collapses to a drawer; footer shows 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; category strip fully visible; filter panel sits as a left sidebar; footer shows 4-column grid; pagination shows full page list |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; all elements at full size; additional whitespace on sides; footer columns expand to 5 |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Product cards have 48px minimum tap area for "Add to Cart" and "Wishlist" actions
- Category pills in the strip have 36px height with 8px internal padding
- Pagination page numbers have 36px minimum tap target
- Filter checkboxes have 44px tap area (includes label padding)
- Hamburger menu icon has 48px tap target

### Collapsing Strategy
- Primary nav links collapse to a hamburger drawer below 744px
- Category strip collapses to a single dropdown selector below 744px
- Filter panel collapses to a slide-out drawer below 1128px
- Product grid reduces from 4 columns to 1 column as viewport shrinks
- Footer columns stack from 5 to 1 as viewport shrinks
- Pagination collapses to "Prev/Next" only below 744px
- Search bar collapses to a search icon with expandable input below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one brand color (#313131) was extractable from the live site — the palette above is an inferred grayscale system. The true brand may have a secondary accent color (e.g., a muted gold, burgundy, or navy) that could not be extracted due to the site's reliance on book cover imagery for color.
- Font-family declarations resolved to the system font stack — no custom typeface was detected. The brand may license a bookish serif or display face that only appears in imagery or PDF assets.
- Hover and active states for most components are inferred from common patterns rather than extracted from live CSS.
- Error styling for forms (validation messages, error icons) could not be extracted.
- Dark mode or high-contrast mode styles are unknown.
- The site's "Just a moment..." page title suggests a Cloudflare challenge page — the extracted colors may reflect a fallback or loading state rather than the full brand experience.
- Sub-brand or seasonal color palettes (holiday, clearance, rare editions) are unknown.
- Button loading states, success states, and animation timings could not be extracted.
- The star rating color (#f5a623) is a common yellow and may not be the brand's chosen rating color.
- Link colors (#0056b3, #4a0072) are standard web defaults and may not reflect intentional brand choices.
