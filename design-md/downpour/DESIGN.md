---
version: alpha
name: "Downpour"
source_url: "https://www.downpour.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A rain-drenched audiobook marketplace where #282828 — the meta theme-color and the brand's true ink — sets a moody, intimate stage against which a single accent, #b81d48 (a dried-crimson red), fires for every primary CTA, sale badge, and price highlight. The palette is deliberately compressed: #444444 and #3d4246 for body text, #b2b2b2 and #747474 for muted labels, and a warm off-white canvas of #f8f8f8 that avoids the sterile hospital white of typical ecommerce. Inter runs at modest weights — display titles at 600, body at 400 — and the brand trusts generous whitespace and the occasional #2e9e7b (a deep teal-green) for secondary accents or sale badges to create hierarchy without visual noise. Product cards use softly rounded corners (`{rounded.md}` ~12px), while the search bar and primary buttons take a tighter `{rounded.sm}` (8px) — a subtle signal that this is a utility-first tool, not a lifestyle playground. The nav bar sits at a compact 64px, and the footer uses a dense, link-heavy layout on #282828 with white text, reinforcing the brand's no-nonsense, value-driven positioning. The overall effect is that of a well-lit bookstore on a gray afternoon — warm, focused, and serious about the product.

colors:
  primary: "#b81d48"
  primary-active: "#9a173a"
  primary-disabled: "#e8a0b4"
  ink: "#282828"
  body: "#444444"
  muted: "#747474"
  muted-soft: "#b2b2b2"
  hairline: "#ebebeb"
  hairline-soft: "#e8e9eb"
  canvas: "#f8f8f8"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#2e9e7b"
  accent-blue: "#3b9cb7"
  error-red: "#d70101"
  sale-badge-bg: "#ef432d"
  sale-badge-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.error-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
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
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.sm}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-bestseller:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginTop: "{spacing.md}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    marginTop: "{spacing.lg}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and "Subscribe". Uses the brand's dried-crimson `{colors.primary}` on a white background with 8px rounded corners (`{rounded.sm}`). On hover, it shifts to `{colors.primary-active}` (#9a173a), and in disabled state it fades to `{colors.primary-disabled}` (#e8a0b4). Text is white, set in `{typography.button-md}` (15px/500). Height is 44px with 12px/24px padding.

**`button-secondary`** — Outlined variant for less prominent actions like "View Details" or "Save for Later". Uses a white background with a `{colors.hairline}` border. On hover, the background shifts to `{colors.surface-soft}` and the border to `{colors.muted}`. Text is `{colors.ink}`.

**`button-tertiary-text`** — Text-only link-style button for inline actions like "Clear Filters" or "Cancel". Uses `{colors.primary}` text on a transparent background. On hover, it shifts to `{colors.primary-active}`.

**`button-pill-accent`** — A fully rounded pill button (`{rounded.full}`) using the accent teal-green `{colors.accent-green}` for secondary promotional actions or "Shop Now" badges in category strips. Smaller padding (8px/16px) and `{typography.button-sm}`.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with a 1px `{colors.hairline-soft}` border and 12px rounded corners (`{rounded.md}`). Contains a square image with `{rounded.sm}`, the title in `{typography.title-sm}` (16px/500, `{colors.ink}`), the author in `{typography.caption}` (13px/400, `{colors.muted}`), and the price in `{typography.body-md}` (16px/400, `{colors.primary}`). On hover, the border thickens to `{colors.hairline}` and a subtle shadow appears. Sale badges sit in the top-left corner of the image.

### Navigation
**`nav-bar`** — A compact 64px header with a white background and a 1px `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` (14px/500). Active links have a 2px `{colors.primary}` bottom border; inactive links are `{colors.muted}`. The bar contains the brand logo on the left, primary nav links in the center, and utility icons (search, cart, account) on the right.

### Forms
**`text-input`** — Standard text input for search, login, and checkout forms. White background with a 1px `{colors.hairline}` border and 8px rounded corners (`{rounded.sm}`). On focus, the border switches to `{colors.primary}`. Error state uses a `{colors.error-red}` border. Height is 44px with 12px/16px padding.

**`search-bar`** — The primary search input, visually identical to `text-input` but with a search icon on the left. On focus, the border switches to `{colors.primary}`. Used in both the nav bar and the hero banner.

### Badges
**`badge-new`** — A small, uppercase badge using `{colors.accent-blue}` (#3b9cb7) for "New Release" labels. Set in `{typography.badge}` (11px/600, uppercase) with 2px/8px padding and 4px rounded corners (`{rounded.xs}`).

**`badge-sale`** — A sale badge using `{colors.sale-badge-bg}` (#ef432d) for discount indicators. Same typography and sizing as `badge-new`.

**`badge-bestseller`** — A bestseller badge using `{colors.accent-green}` (#2e9e7b) for top-performing titles. Same typography and sizing.

### Hero
**`hero-banner`** — A full-width banner with a `{colors.ink}` (#282828) background and white text. Uses `{typography.display-lg}` (28px/600) for the headline and `{typography.body-md}` for the subtitle in `{colors.muted-soft}`. Contains a `{colors.primary}` CTA button. Padding is `{spacing.section}` (64px) vertically and `{spacing.lg}` (24px) horizontally.

### Footer
**`footer`** — A dense, link-heavy footer on a `{colors.ink}` background with white text. Links use `{typography.link}` (14px/400) in `{colors.muted-soft}` (#b2b2b2), shifting to white on hover. Section headings use `{typography.title-sm}` (16px/500) with a `{spacing.md}` bottom margin. The footer is divided into columns for company info, customer service, and social links.

### Category Chips
**`category-chip`** — Pill-shaped filter chips (`{rounded.full}`) for browsing by genre or category. Default state uses `{colors.surface-soft}` background with a `{colors.hairline}` border. Active state uses `{colors.primary}` background with white text. Set in `{typography.button-sm}` (13px/500).

### Pagination
**`pagination-button`** — Square buttons for page navigation. Default state uses a white background with a `{colors.hairline}` border. Active state uses `{colors.primary}` background with white text. Disabled state uses `{colors.surface-soft}` background with `{colors.muted-soft}` text. All have 8px rounded corners (`{rounded.sm}`).

### Quantity Selector
**`quantity-selector`** — A compact input group for adjusting item quantities in the cart. Consists of a central text input with `{typography.body-md}` and two square buttons on either side. The buttons use `{colors.surface-soft}` background and are 32px × 32px with 4px rounded corners (`{rounded.xs}`). The entire group has a `{colors.hairline}` border and 8px rounded corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner reduces padding to 32px; footer stacks vertically; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero banner uses 48px padding; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero banner at full 64px padding; footer uses four-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner may include background imagery; footer remains four-column |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Category chips are at least 36px tall with 16px horizontal padding
- Quantity selector buttons are 32px × 32px — slightly below the 44px ideal but acceptable for non-primary interactions
- Search bar and text inputs are 44px tall
- Nav links have a minimum 40px touch area

### Collapsing Strategy
- On mobile (< 744px), the primary navigation collapses into a hamburger menu with a slide-out drawer
- The product grid collapses from 3 columns to 1 column
- The footer's multi-column layout collapses to a single column with accordion-style expandable sections
- Category chips wrap to multiple rows instead of a single horizontal scroll
- The hero banner's padding reduces by 50%
- Search bar moves from the nav bar to a full-width element below the nav

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (text-input, search-bar, product-card) are inferred from common patterns rather than extracted from the live site
- Error and validation styling for forms (error messages, success states) could not be reliably extracted
- The exact font weights and sizes for typography are inferred from common Inter usage patterns; the live site may use different values
- Dark mode styling is not present on the live site and is not defined
- Sub-brand or promotional palettes (e.g., holiday sales, genre-specific themes) are not captured
- The extracted hex list includes several colors that may be Shopify widget defaults (#5b21b6, #16a34a) or stock image tones; the brand's true palette is likely more focused on the #282828, #b81d48, #444444, #f8f8f8 core
- Animation and transition durations are not specified
- The exact border radius for product cards (12px) is an estimate based on common ecommerce patterns
- Iconography style and sizing (beyond search icon) is not defined
- Loading states and skeleton screens are not documented
- The hero banner's background treatment (solid color vs. gradient vs. image) is not confirmed from the live site
- Checkout flow components (cart, address form, payment) are not documented as they likely use Shopify's default checkout
