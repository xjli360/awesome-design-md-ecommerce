---
version: alpha
name: "Shout! Factory"
source_url: "https://shoutfactory.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A catalog-driven entertainment brand that uses a deep navy anchor (#163959) as its structural spine and a sharp red accent (#bd2426) as its purchase trigger — the red appears on “Add to Cart,” sale badges, and pre-order banners, while the navy governs headers, footer blocks, and the primary nav background. The palette reads like a mid-century movie poster: warm grays (#404040, #595959) for body text, a cool off-white (#ebebeb) for page backgrounds, and a secondary blue (#62a1d8) for informational links and category tags. What distinguishes Shout! Factory from a generic e‑commerce template is its use of green (#9bca3e) for stock indicators and “In Stock” badges — a color more commonly associated with organic or outdoor brands, here signaling availability with an almost botanical freshness against the navy-and-red scheme. The typography stack defaults to system fonts (Arial, Helvetica Neue, Segoe UI) with no custom brand typeface, which gives the site a utilitarian, database‑like feel — the content (thousands of Blu‑ray, DVD, and vinyl titles) is the hero, not the typography. Product cards use a soft rounded corner ({rounded.sm} ~8px) with a white surface ({colors.surface-card}) and a subtle hairline border ({colors.hairline}), while the search bar sits in a full‑width navy band with white text, creating a clear entry point. The overall mood is that of a well‑organized specialty video store: functional, genre‑rich, and unpretentious, with color used sparingly to direct attention to what matters — the cover art and the price.

colors:
  primary: "#bd2426"
  primary-active: "#a01e20"
  primary-disabled: "#e8a0a1"
  ink: "#163959"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  accent-blue: "#62a1d8"
  accent-blue-dark: "#2f7bbf"
  accent-green: "#9bca3e"
  accent-green-dark: "#516b1d"
  badge-sale: "#bd2426"
  badge-new: "#f68b1f"
  badge-preorder: "#ee730a"
  star-rating: "#f9b169"
  footer-bg: "#163959"
  nav-bg: "#163959"
  search-bg: "#163959"
  link-default: "#0051c3"
  link-visited: "#521010"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  price-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    opacity: 0.8
  search-bar:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.sm} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-stock-indicator:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.accent-blue}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.on-ink}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-blue-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-tag-active:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.link-default}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.xs}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for “Add to Cart,” “Checkout,” and “Subscribe.” Rendered in the brand red (#bd2426) with white text and a soft 8px corner. On hover, shifts to a darker red (#a01e20). Disabled state uses a pale pink (#e8a0a1) to indicate inactivity. Height is 44px with 12px vertical / 24px horizontal padding.

**`button-secondary`** — An outlined variant for secondary actions like “View Details” or “Wishlist.” Uses a white background with a 2px navy (#163959) border and navy text. Active state fills the background with a light gray (#f5f5f5). Same 44px height as primary for alignment in button groups.

**`button-ghost`** — A text-only button for tertiary actions such as “Cancel” or “Clear Filters.” Transparent background with navy text. On hover, gains a light gray background (#f5f5f5). Matches primary button height for consistent row layouts.

**`button-small`** — A compact variant for inline actions like “Apply” in filters or “Remove” in cart line items. Uses the primary red with white text, 32px height, and tighter 8px horizontal padding. Corners are 4px for a more utilitarian feel.

### Cards
**`product-card`** — The core content unit for displaying movies, TV shows, and music titles. A white card with an 8px rounded corner, no padding on the container (padding is applied to inner elements). The image area uses top-only rounding to match the card shape. Title appears in 16px/600 weight navy text, price in 14px/700 weight gray text below. Badges overlay the image area for sale, new, or pre-order status. Stock availability is indicated by a green (#9bca3e) pill badge.

**`product-card-badge`** — A small uppercase label pinned to the top-left of product card images. Sale badges use the primary red, new badges use orange (#f68b1f), and pre-order badges use a deeper orange (#ee730a). All badges are 4px rounded with 2px vertical / 8px horizontal padding.

### Navigation
**`nav-bar`** — The primary site navigation, a 56px navy (#163959) bar spanning the full viewport width. Navigation links are white, uppercase, 14px/600 weight with 0.2px letter spacing. The active page is indicated by a 3px red underline. Inactive links render at 80% opacity. The bar contains the brand logo (left), category links (center), and utility icons (right — search, account, cart).

**`search-bar`** — A full-width search component embedded in the navy nav area. The input field itself is white with a 1px gray border and 8px rounding. The surrounding container is navy, creating a distinct search zone. Placeholder text is in the muted gray (#595959).

### Forms
**`text-input`** — Standard form input for checkout fields, account forms, and search filters. White background, 44px height, 8px rounding, and a 1px light gray border (#dedede). On focus, the border becomes a 2px blue (#62a1d8) stroke. Error state uses a 2px red border (#bd2426).

**`select-input`** — Dropdown selector for sorting, filtering, and quantity choices. Shares the same dimensions and border styling as text inputs. Uses a custom dropdown arrow (not specified, but should be a down-chevron in the muted gray).

**`quantity-selector`** — A compact numeric input for cart quantities. 40px height with a 1px gray border and 4px rounding. Typically paired with increment/decrement buttons.

### Footer
**`footer`** — A full-width navy (#163959) section with white text. Contains columns for customer service, company info, and social links. Links are styled in the accent blue (#62a1d8) and shift to white on hover. Padding is 48px vertical / 32px horizontal.

### Tags & Filters
**`category-tag`** — A pill-shaped filter tag for browsing by genre, format, or collection. Light gray background (#f5f5f5) with dark blue text (#2f7bbf). Active state fills with the accent blue and white text. Padding is 4px vertical / 12px horizontal with full rounding.

### Pagination
**`pagination-button`** — A 36px square button for page navigation. White background with a 1px gray border and 4px rounding. The active page uses the primary red with white text. Used in product listing pages and search results.

### Accordion
**`accordion-header`** — Expandable section headers for product details, shipping info, and FAQ content. Light gray background (#f5f5f5) with navy text in 16px/600 weight. Content area is white with 14px body text. Both sections use 4px rounding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 items), hamburger nav replaces full nav bar, search bar collapses to icon-only, footer stacks vertically, hero banner reduces padding to 32px vertical |
| Tablet | 744–1128px | Two-column product grid, nav bar shows top-level categories only, search bar remains full-width but condensed, footer splits into two rows |
| Desktop | 1128–1440px | Three-to-four-column product grid, full nav bar with dropdowns, search bar at full width, footer in four columns |
| Wide | > 1440px | Four-to-five-column product grid, max-width container (1440px) centered, nav bar and footer expand to full viewport width with content constrained |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have 48px tap targets (padding extends beyond text)
- Product card CTAs are at least 44px tall
- Category tags are 32px tall (below 44px minimum, but acceptable for non-primary actions)
- Quantity selector buttons are 40px tall

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Secondary navigation (sub-categories, filters) collapses to a dropdown or slide-out panel below 744px
- Product filters move from sidebar to top-of-page accordion below 744px
- Footer columns collapse from four to two at 744px, then to a single column below 480px
- Hero banner text reduces from display-lg to display-md below 744px
- Product card badges hide on mobile to reduce visual clutter (stock indicator remains)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns; exact transition durations and easing curves were not extracted
- Focus-visible styles (keyboard navigation outlines) were not observed; a 2px blue (#62a1d8) outline is assumed but not confirmed
- Error state styling for forms (iconography, helper text placement) was not captured
- Dark mode is not supported by the current site
- Sub-brand palettes (Shout! Factory Kids, Shout! Select, etc.) may have distinct accent colors not present in the extracted palette
- Checkout-specific components (payment form, shipping selector, order summary) were not analyzed due to Cloudflare block
- The extracted font stack is entirely system fonts; no custom web fonts were detected, but the brand may license a typeface for specific marketing pages
- The green (#9bca3e) and orange (#f68b1f) accents appear in extracted colors but their exact usage context (beyond stock indicators and new badges) is inferred
- Star rating color (#f9b169) is assumed from extracted hex; exact implementation (SVG, CSS, or image) is unknown
- The `#521010` (dark maroon) hex may be a link-visited color or a secondary background; usage is speculative
- The `#c16508` and `#904b06` (brown/orange) hexes appear to be image-dominant tones rather than design system colors; excluded from palette
