---
version: alpha
name: "Classic Game Source"
source_url: "https://classicgamesource.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A retro game marketplace that wears its eBay heritage like a well-loved cartridge — the primary voltage is #3665f3, eBay's signature blue, which appears on every CTA, search button, and listing link, while a secondary accent of #e0103a (a punchy red) signals price drops, sold-out items, and urgency badges. The canvas is #f7f7f7, a warm off-white that softens the utilitarian grid of product cards and listing rows, with #ffffff reserved for card surfaces and modals. Typography runs Market Sans for headings and body text — a clean, neutral sans-serif that prioritizes readability over personality — with Arial and Helvetica as fallbacks. The brand's design language is fundamentally transactional: dense information density, tight spacing at {spacing.sm} between listing elements, and a heavy reliance on colored badges (#92c821 for "Buy It Now", #ffbd14 for "Best Offer", #e0103a for "Sold") to create visual hierarchy without decorative flourishes. Search is the primary navigation gesture, rendered as a full-width bar with {rounded.full} ends and a #3665f3 submit button. Product cards use {rounded.sm} corners and a 1px #e5e5e5 hairline, with price tags in bold #111820 and shipping info in #8f8f8f muted text. The overall feel is that of a well-organized flea market catalog — functional, color-coded, and built for scanning.

colors:
  primary: "#3665f3"
  primary-active: "#0968f6"
  primary-disabled: "#8f8f8f"
  ink: "#111820"
  body: "#191919"
  muted: "#8f8f8f"
  muted-soft: "#e5e5e5"
  hairline: "#e5e5e5"
  hairline-soft: "#f1f1f1"
  canvas: "#f7f7f7"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e0103a"
  accent-green: "#92c821"
  accent-yellow: "#ffbd14"
  accent-orange: "#562f01"
  accent-teal: "#07465a"
  accent-purple: "#3b1fc6"
  accent-brown: "#553b06"
  accent-dark-green: "#345110"
  accent-dark-red: "#d70f38"
  accent-bright-red: "#f02d2d"
  accent-lime: "#4ce160"
  accent-dark-ink: "#01193d"
  accent-dark-teal: "#002b20"
  accent-dark-brown: "#562501"
  accent-maroon: "#360606"
  accent-olive: "#4e4e0c"
  accent-gold: "#524500"
  accent-light-blue: "#0064d2"
  accent-light-purple: "#f6f5fe"
  accent-charcoal: "#2f0e04"
  accent-dark-green-alt: "#0c310d"

typography:
  display-xl:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
  badge:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Market Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-danger:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 48px
  search-bar-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-image:
    rounded: "{rounded.xs}"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    margin: 8px 0 4px 0
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-shipping:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-condition:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sold:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-buy-it-now:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-best-offer:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-auction:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-free-shipping:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: 24px 16px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: 32px 16px
    rounded: "{rounded.sm}"
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  listing-detail-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    padding: 16px
    rounded: "{rounded.sm}"
  listing-detail-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.accent-red}"
  listing-detail-description:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 16px
    rounded: "{rounded.sm}"
  seller-info:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 12px
    rounded: "{rounded.sm}"
  pagination:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  filter-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 16px
    rounded: "{rounded.sm}"
  filter-checkbox:
    rounded: "{rounded.xs}"
    height: 18px
  filter-label:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  sort-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  rating-stars:
    color: "{colors.accent-yellow}"
    fontSize: 16px
  review-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
    height: 40px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  buy-it-now:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  watchlist-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 32px
  share-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  error-message:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  success-message:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  info-message:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  modal-overlay:
    backgroundColor: "{colors.ink}"
    opacity: 0.5
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, filled with #3665f3 (eBay blue) and white text. Uses Market Sans at 14px/600 weight. Rounded at 8px with 10px vertical padding and 20px horizontal. On hover, shifts to #0968f6. Disabled state uses #8f8f8f fill. Used for "Add to Cart", "Buy It Now", and "Search" actions.

**`button-secondary`** — An outlined variant with white background and #3665f3 text. Same typography and rounded corners as primary. Active state shifts text to #0968f6. Used for "Watchlist" and "Cancel" actions.

**`button-danger`** — A red variant using #e0103a fill with white text. Used for destructive actions like "Remove from Cart" or "Report Item". Same dimensions as primary.

**`button-pill`** — A compact, fully rounded pill button using #3665f3 fill. Uses 12px/600 weight Market Sans. 6px vertical padding, 16px horizontal. Used for category filters and quick actions.

### Cards
**`product-card`** — The core listing card, white background with 8px rounded corners and 12px padding. Contains an image area (200px height, 4px rounded), a title in 14px/600 weight, price in 16px/700 weight, and shipping info in 12px gray. Hover state shows a subtle shadow (not extracted, assumed). Badges overlay the image or sit below the title.

**`listing-detail-header`** — The full listing view header, white card with 16px padding and 8px rounded corners. Contains the title in 18px/600 weight and the price in 20px/700 weight red (#e0103a).

**`listing-detail-description`** — The description section, white card with 16px padding and 8px rounded corners. Uses 16px body text.

**`seller-info`** — A soft gray (#f5f5f5) card with 12px padding and 8px rounded corners. Displays seller name, rating, and feedback count.

### Navigation
**`nav-bar`** — The top navigation bar, white background, 56px height. Contains logo, category links, and search bar. Links use Market Sans at 14px/600 weight. Active link uses #3665f3, inactive uses #8f8f8f.

**`category-strip`** — A horizontal scrollable strip of category pills. White background with 8px vertical padding. Active pill uses #3665f3 fill, inactive uses #f5f5f5 fill with dark text. Both use full rounded corners.

**`breadcrumb`** — A simple text breadcrumb trail using 12px gray text. Active (current) item uses dark text. No background.

### Forms
**`text-input`** — Standard text input, white background, 40px height, 8px rounded corners, 8px/12px padding. Uses 16px body text. Focus state adds a #3665f3 border (assumed, not extracted).

**`search-bar`** — The primary search input, white background, 48px height, fully rounded corners, 8px/16px padding. Uses 16px body text. Focus state maintains white background with blue border.

**`sort-dropdown`** — A dropdown selector, white background, 40px height, 8px rounded corners, 8px/12px padding. Uses 14px body text.

**`filter-checkbox`** — A small checkbox with 4px rounded corners, 18px height. Label uses 14px body text.

### Badges
**`badge-condition`** — Green (#92c821) badge for condition labels like "New" or "Used - Like New". Uses 11px/700 weight uppercase Market Sans. 2px/6px padding, 4px rounded corners.

**`badge-sold`** — Red (#e0103a) badge for sold items. Same dimensions as condition badge.

**`badge-buy-it-now`** — Green (#92c821) badge for "Buy It Now" listings. Same dimensions.

**`badge-best-offer`** — Yellow (#ffbd14) badge with dark text for "Best Offer" listings. Same dimensions.

**`badge-auction`** — Purple (#3b1fc6) badge for auction-style listings. Same dimensions.

**`badge-free-shipping`** — Teal (#07465a) badge for free shipping offers. Same dimensions.

### Footer
**`footer`** — The site footer, dark background (#111820) with white text. 24px/16px padding. Links use #e5e5e5 color with underline on hover. Contains store policies, contact info, and social links.

### Messaging
**`error-message`** — Red (#e0103a) banner with white text, 8px rounded corners, 12px padding. Used for form errors and transaction failures.

**`success-message`** — Green (#92c821) banner with white text, same dimensions. Used for successful actions.

**`info-message`** — Blue (#3665f3) banner with white text, same dimensions. Used for informational notices.

**`tooltip`** — Dark (#111820) tooltip with white text, 4px rounded corners, 4px/8px padding. Uses 12px text.

### Modal
**`modal`** — A white card with 12px rounded corners and 24px padding. Overlay uses #111820 at 50% opacity. Used for confirmations, image zoom, and detailed filters.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column layout, stacked product cards, hamburger menu, search bar collapses to icon, category strip becomes horizontal scroll, filter panel becomes full-screen modal, footer stacks vertically |
| Tablet | 744–1128px | Two column product grid, search bar remains full width, category strip visible with horizontal scroll, filter panel slides in from left, footer splits into two columns |
| Desktop | 1128–1440px | Three to four column product grid, full navigation visible, search bar centered, filter panel visible as sidebar, footer splits into four columns |
| Wide | > 1440px | Four to five column product grid, max-width container at 1440px, whitespace increases on sides, filter panel remains sidebar |

### Touch Targets
- All buttons and interactive elements minimum 40px height (primary, secondary, text inputs)
- Search bar 48px height for easy tapping
- Category pills 32px height with 16px horizontal padding
- Checkboxes 18px height (minimum recommended 44px tap area)
- Pagination buttons 40px height
- Sort dropdown 40px height

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Search bar collapses to icon-only trigger below 744px, expands to full bar on tap
- Filter panel collapses to button trigger below 1128px, opens as modal or slide-in
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer sections stack vertically below 744px
- Category strip becomes horizontal scrollable on all sizes, but pills shrink on mobile
- Breadcrumb truncates on mobile (shows only last 2 levels)
- Seller info section collapses to expandable accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, border color) not extracted — assumed standard elevation
- Focus states for text inputs and search bar not extracted — assumed blue border
- Error states for form fields (red border, error icon) not extracted
- Dark mode not present on live site
- Loading states (skeleton screens, spinners) not extracted — assumed standard blue spinner
- Animation durations and easing curves not extracted
- Specific font weights for Market Sans not confirmed — used standard weights
- TengwarTelcontar font appears in extracted list but likely a decorative/novelty font used sparingly (e.g., for logos or themed sections) — not included in primary typography
- The extracted color list is heavily weighted toward eBay's platform colors (#3665f3, #0968f6, #0064d2) and generic web colors — the brand's own accent palette (if any) could not be isolated from eBay's system colors
- Sub-brand or seasonal color variations not detected
- Print stylesheet not analyzed
- Accessibility contrast ratios not verified against WCAG
- Custom scrollbar styling not extracted
- Image aspect ratios for product cards not confirmed (assumed 1:1 or 4:3)
- Video player styling not extracted
- Mobile app-specific components (if any) not analyzed
