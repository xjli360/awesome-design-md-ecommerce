---
version: alpha
name: "Entertainment Earth"
source_url: "https://www.entertainmentearth.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The #313131 near-black anchoring Entertainment Earth's navigation sets the visual temperature for a collector marketplace where badge density — EXCLUSIVE, PRE-ORDER, NEW, SALE — carries more communicative weight than lifestyle photography ever could. Every product card is a micro-billboard: licensed character art, a product name in tight 13px body type, a price block, a badge strip, and an Add to Cart or Pre-Order CTA crammed into roughly 220×320px. The system font stack (system-ui, -apple-system, Arial) is a deliberate non-statement: the Marvel, Star Wars, DC, and Transformers IP on display is the typographic event, not the retailer's typeface.

  The primary red fires on every add-to-cart action and promotional flag, punching hard against both the dark nav and the white product-card canvas. A secondary promo-accent yellow marks markdown pricing and clearance runs — the collector's signal for a bargain hunt. Pre-order badges carry a distinct blue treatment, separating months-ahead reservation inventory from in-stock product at a glance, a UX affordance born from the reality that a large share of collector purchases are pre-decided franchise commitments rather than impulse browses.

  Spacing is tight by consumer-retail standards: {spacing.xs}–{spacing.sm} gutters between cards, dense category sidebars on desktop collapsing to horizontal scroll chips on mobile. Buttons use {rounded.xs} corners — the near-rectangular stance reads as direct and transactional, a deliberate contrast to the soft pill shapes popular on lifestyle DTC sites. The footer is encyclopedic: franchise sub-navigation, license-partner logos, and help links coexist at caption-scale type, serving as infrastructure for obsessive product discovery. A 3px primary-red top border on the footer is the only decorative flourish in an otherwise utility-first design system.

colors:
  primary: "#cc0000"
  primary-active: "#aa0000"
  primary-disabled: "#e88888"
  promo-accent: "#ffcc00"
  promo-accent-dark: "#cc9900"
  preorder-blue: "#1565c0"
  preorder-blue-active: "#0d47a1"
  ink: "#313131"
  body: "#444444"
  muted: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  nav-bg: "#313131"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-promo: "#000000"
  badge-exclusive-bg: "#cc0000"
  badge-exclusive-text: "#ffffff"
  badge-preorder-bg: "#1565c0"
  badge-preorder-text: "#ffffff"
  badge-new-bg: "#2e7d32"
  badge-new-text: "#ffffff"
  badge-sale-bg: "#ffcc00"
  badge-sale-text: "#000000"
  star-rating: "#ffcc00"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  product-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-preorder:
    backgroundColor: "{colors.preorder-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-preorder-active:
    backgroundColor: "{colors.preorder-blue-active}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 8px 18px
    height: 40px
  button-wishlist:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    focusBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    logoHeight: 40px
  nav-top-promo-bar:
    backgroundColor: "{colors.promo-accent}"
    textColor: "{colors.on-promo}"
    typography: "{typography.caption-bold}"
    height: 36px
  nav-category-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.product-title}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1:1"
    badgePosition: "top-left"
    hoverBorder: "1px solid {colors.primary}"
  badge-exclusive:
    backgroundColor: "{colors.badge-exclusive-bg}"
    textColor: "{colors.badge-exclusive-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder-bg}"
    textColor: "{colors.badge-preorder-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale-bg}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  hero-banner:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    minHeight: 320px
    imageOverlap: "right-bleed"
  price-block:
    currentPriceTypography: "{typography.price-display}"
    currentPriceColor: "{colors.primary}"
    originalPriceTypography: "{typography.price-original}"
    originalPriceColor: "{colors.muted}"
    savingsBadgeBg: "{colors.badge-sale-bg}"
    savingsBadgeText: "{colors.on-promo}"
    savingsBadgeTypography: "{typography.badge}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
    activeBg: "{colors.primary}"
    activeText: "{colors.on-primary}"
  star-rating:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    starSize: 14px
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeBg: "{colors.primary}"
    activeText: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.base}"

## Components

### Buttons
**`button-primary`** — Red (#cc0000) fill with white uppercase 14px/700 text and near-flat {rounded.xs} corners at 40px height. This is the Add to Cart trigger and fires on every in-stock product card; the all-caps treatment signals a transactional rather than aspirational purchase moment. Active state deepens to #aa0000; disabled renders washed-out at {colors.primary-disabled}.

**`button-preorder`** — The collector-specific CTA: preorder blue (#1565c0) separates future-availability items from in-stock product at a glance, a critical affordance when a large share of the catalog consists of items months from shipping. Same rectangular geometry as `button-primary`. Active deepens to #0d47a1. Typically rendered alongside a release-window string in {typography.caption}.

**`button-secondary`** — White fill with a 2px red border and red text, used for secondary actions like View Details or Compare. Maintains height parity with `button-primary` so mixed-CTA rows stay vertically aligned.

**`button-wishlist`** — Circular ghost icon button (32×32px), transparent background, muted text. Overlays the product-card image on hover; uses {rounded.full} to stay visually distinct from the rectangular primary buttons.

### Product Cards
**`product-card`** — The foundational repeating unit across every listing page: square 1:1 image crop, product title in {typography.product-title} capped at two lines via `-webkit-line-clamp`, a `price-block`, and an add-to-cart or pre-order button. Badge strip stacks vertically in the top-left image corner — up to three badges can coexist without overlap. Idle state shows a 1px {colors.hairline} border; hover flips to a 1px {colors.primary} red border, providing clear keyboard-navigable focus feedback. The {rounded.xs} corner is deliberately minimal to keep the grid feeling like a dense catalog rather than a lifestyle storefront.

### Badges
**`badge-exclusive`** — Red fill (#cc0000), white uppercase 10px text, zero radius. Marks Entertainment Earth-exclusive products, a primary value proposition for collectors who cannot source the item elsewhere. Renders at the top of any badge stack.

**`badge-preorder`** — Blue fill (#1565c0), white text. Always ships alongside an estimated release quarter or date in {typography.caption} below the badge strip.

**`badge-new`** — Green fill (#2e7d32), white text. Applied to items added within the last 30 days of inventory.

**`badge-sale`** — Promo-accent yellow (#ffcc00) fill with black text — the highest-contrast badge in the set, intentionally louder than the others to drive clearance velocity. Can coexist with `badge-exclusive` on discounted exclusives.

### Navigation
**`nav-bar`** — #313131 background at 56px height. Logo anchored left, search bar centered (full-width on mobile), account/cart utilities right. No border-bottom is needed; the dark register creates its own edge against the white page canvas below.

**`nav-top-promo-bar`** — Promo-accent yellow (#ffcc00) announcement band above the main nav. Announces free shipping thresholds, site-wide sales, or exclusive launch events in 12px {typography.caption-bold} black text. Dismissible on mobile via a close icon.

**`nav-category-bar`** — Slightly darker #1a1a1a sub-nav strip with franchise and category links in {typography.caption-bold} white: MARVEL, STAR WARS, DC, ANIME, GAMING, and similar. Collapses to hamburger menu on mobile.

### Search
**`search-bar`** — Inline bar embedded in the dark nav, white fill, 40px height, {rounded.sm} on the left corners only. A red submit button flushes flush to the right edge of the field with {rounded.none} on its left side, creating a compound pill-meets-rectangle form. Autocomplete dropdown extends full nav width on mobile.

### Hero Banners
**`hero-banner`** — Full-bleed dark-background editorial placement with franchise key art bleeding off the right edge. Headline in {typography.display-xl} (32px/700), subhead in {typography.body-md}, CTA using the primary red button styles. Minimum 320px height; desktop banners expand to 400–480px. The dark background (#313131) creates visual continuity with the nav above, giving the entire above-fold region a unified dark register before the white product grid below.

### Price Block
**`price-block`** — Sale price in primary red at {typography.price-display} (18px/700), original price struck-through in {typography.price-original} at {colors.muted}, optional promo-yellow savings badge below. This three-element stack appears on every product card, PDP, and cart line item and is the most data-dense element in the system.

### Category Chips
**`category-chip`** — Soft gray {colors.surface-soft} chips with {rounded.sm} corners for franchise or product-type filtering. Active state flips to red fill with white text. On desktop, rendered as a vertical sidebar checkbox list; on mobile, reflows to a horizontal scroll strip.

### Footer
**`footer`** — #313131 background matching the nav, with a 3px {colors.primary} red top border as the only decorative element. Link columns use {typography.body-sm} in {colors.on-dark}; section headings use {typography.title-sm}. Houses franchise partner logos, social icons, a newsletter signup input, and a long tail of sub-category navigation links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; nav collapses to hamburger + search icon + cart; promo bar is dismissible; category bar becomes horizontal scroll chips; sidebar filters move to a bottom-sheet modal drawer |
| Tablet | 744–1128px | 3-column product grid; search bar visible in nav; condensed category bar retains top franchise links; hero banners center-crop |
| Desktop | 1128–1440px | 4-column product grid; full sidebar filter panel visible alongside grid; all category-bar links visible |
| Wide | > 1440px | Max-width container (~1400px) centered; grid stays at 4–5 columns; hero banner reaches full cinematic bleed width |

### Touch Targets
- Add to Cart and Pre-Order buttons: minimum 40px height, full card-width on mobile
- Wishlist icon button: 32×32px visible target with invisible padding extending tap area to 44×44px
- Nav icons (cart, account, hamburger): 44×44px tap area
- Category chips in horizontal scroll: 36px height minimum, 12px horizontal padding
- Badge strips: non-interactive, no touch target required

### Collapsing Strategy
- Sidebar filters collapse to a bottom-sheet modal triggered by a sticky "Filter & Sort" bar at the bottom of the viewport on mobile
- Multi-level category navigation collapses to a single-level accordion hamburger menu; franchise sub-categories nest one level deep
- Product badge strips remain visible at all breakpoints — clipping would suppress a primary purchase signal
- Price block always renders all three elements (current, original, savings badge) without truncation
- Promo bar dismisses after first downscroll on mobile to recover vertical space; re-appears on upscroll to page top

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was behind Cloudflare anti-bot protection at extraction time (page title: "Just a moment...") — only one hex value (#313131) was reliably captured
- Primary red, preorder blue, promo yellow, and badge greens are inferred from brand knowledge rather than confirmed DOM extraction — actual production hex values may differ
- No brand-custom typeface found; system font stack confirmed, but specific size/weight scales are inferred from collector e-commerce conventions, not measured from live DOM
- Meta theme-color was absent — dark nav color and mobile browser chrome treatment unconfirmed
- Logo lockup dimensions, exact SVG mark geometry, and clearspace rules unknown
- Hover and focus transition durations, easing curves, and animation timings not captured
- Mega-menu panel behavior (animation direction, overlay scrim opacity, close trigger) not confirmed
- Newsletter signup validation state styling (error, success) not extracted
- Product quick-view modal design and behavior not captured
