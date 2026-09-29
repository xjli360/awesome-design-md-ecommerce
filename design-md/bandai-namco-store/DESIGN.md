---
version: alpha
name: "Bandai Namco Store"
source_url: "https://store.bandainamcoent.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-contrast, franchise-driven marketplace where #f6b700 — a sharp, almost citrus yellow — acts as the primary voltage against a predominantly dark canvas of #222222 and #1f1f1f. This is not a gentle storefront; it is a collector's bazaar built on dense product grids, aggressive discount badges in #e4002b, and tiered navigation that surfaces dozens of IPs (Dragon Ball, One Piece, Elden Ring, Gundam) without collapsing into hamburger menus. The brand's typography runs on Obvia, a geometric sans-serif with distinct condensed and expanded variants, giving the store a slightly arcade-era, action-label feel — especially in the condensed cuts used for product titles and badge copy. Buttons and cards use moderate rounding ({rounded.sm} ~8px), never pill-shaped, preserving a utilitarian, no-nonsense edge. The secondary palette is a study in industrial restraint: #333c3e, #778385, #869791, and #969696 form a muted greige-green axis that supports the yellow and red without competing. The checkout and promotional surfaces introduce #00b0b9 (a teal) and #00b959 (a green) for success states and limited-time offers, but these are tactical, not tonal. The overall effect is a store that feels less like a lifestyle brand and more like a convention hall — loud, dense, organized by franchise, and built for the fan who knows exactly what they want.

colors:
  primary: "#f6b700"
  primary-active: "#d49a00"
  primary-disabled: "#fce899"
  ink: "#222222"
  body: "#333c3e"
  muted: "#778385"
  muted-soft: "#969696"
  hairline: "#d6d6d6"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#222222"
  accent-red: "#e4002b"
  accent-red-active: "#c40024"
  accent-blue: "#0069b1"
  accent-teal: "#00b0b9"
  accent-green: "#00b959"
  dark-canvas: "#1f1f1f"
  dark-surface: "#232323"
  dark-muted: "#434343"
  badge-new: "#f6b700"
  badge-sale: "#e4002b"
  badge-preorder: "#0069b1"

typography:
  display-xl:
    fontFamily: "'Obvia Expanded', 'Obvia', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Obvia Expanded', 'Obvia', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Obvia', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Obvia Condensed', 'Obvia', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Obvia', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Obvia', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', 'Obvia', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Obvia', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Obvia', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Source Sans Pro', 'Obvia', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Obvia Condensed', 'Obvia', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Obvia Condensed', 'Obvia', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Obvia', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Obvia', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "'Source Sans Pro', 'Obvia', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Obvia', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  nav-link-condensed:
    fontFamily: "'Obvia Condensed', 'Obvia', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
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
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-dark-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-condensed}"
    padding: 24px 32px
    rounded: "{rounded.none}"
  nav-mega-menu-category:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-condensed}"
    padding: 8px 0
  nav-mega-menu-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 6px 0
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 12px 16px 4px
  product-card-price:
    typography: "{typography.body-md}"
    padding: 0 16px 12px
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "rgba(0,0,0,0.4)"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 32px 32px
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.primary}"
  footer-section-title:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link-condensed}"
    padding: 0 0 12px
  badge-count:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: 0 6px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  skeleton-loader:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The store's primary call-to-action, rendered in the brand's signature yellow (#f6b700) with dark text (#222222). Used for "Add to Cart", "Pre-order Now", and primary checkout flows. On hover, shifts to a deeper gold (#d49a00); disabled state fades to a pale yellow (#fce899) with muted text. Height is 44px with 12px/24px padding and {rounded.sm} corners — intentionally not pill-shaped to maintain a utilitarian, action-oriented feel.

**`button-secondary`** — An outlined variant with a 2px solid ink border on a white background. Used for secondary actions like "View Details" or "Continue Shopping". Active state fills the background with {colors.surface-soft}. The border maintains visual weight parity with the primary button.

**`button-accent-red`** — A high-urgency variant using the brand's alert red (#e4002b) with white text. Reserved for "Clearance", "Flash Sale", or "Limited Stock" CTAs. Active state darkens to #c40024. Never used for primary purchase flows to avoid confusion with error states.

**`button-dark`** — An inverted variant on the dark canvas (#1f1f1f) with white text. Used in hero banners, dark-themed promotional sections, and the footer. Active state shifts to the dark surface (#232323).

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft hairline border and {rounded.sm} corners. The image area occupies the top half with a soft gray background (#f6f6f6) for fallback. Below, the title uses {typography.title-sm} with 12px/16px padding, and the price uses {typography.body-md} with 0/16px padding. Badges overlay the image area at the top-left corner.

**`product-card-badge`** — A small uppercase label in {typography.badge} with {rounded.xs} corners. Three variants exist: yellow for "New", red for "Sale", and blue for "Pre-order". The badge sits flush against the card edge with 2px/8px padding, designed to be legible at small sizes without dominating the product image.

### Navigation
**`nav-bar`** — A fixed 64px white bar with a 1px soft hairline bottom border. Contains the store logo on the left, a mega-menu trigger (or franchise list) in the center, and utility icons (search, cart, account) on the right. On scroll, gains a subtle box shadow. The sticky variant maintains the same height to prevent layout shift.

**`nav-mega-menu`** — A full-width dropdown panel triggered by hovering over a top-level franchise link. Uses {typography.nav-link-condensed} for category headers (uppercase, 13px, weight 700) and {typography.body-sm} for individual product links. Categories are arranged in a multi-column grid with generous 24px/32px padding.

### Forms
**`text-input`** — Standard 44px input with {rounded.sm} corners, a 1px hairline border, and 10px/16px padding. On focus, the border thickens to 2px and turns yellow (#f6b700). Error state uses a 2px red border (#e4002b). The select input variant shares the same dimensions and border treatment.

**`search-bar`** — A compact 40px input with a soft gray background (#f6f6f6) and a 1px hairline border. The search icon sits at 20px in muted gray. On focus, the border becomes 2px yellow. This is distinct from the hero search — it's a utility bar, not a discovery tool.

### Footer
**`footer`** — A dark section (#1f1f1f) with white text, padded at 48px/32px/32px. Section titles use the condensed uppercase nav-link style. Links are white with a yellow hover state. The footer typically spans 4-5 columns: Shop by Franchise, Support, About, Legal, and Social.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; mega-menu becomes accordion; product cards go single-column; hero banner height reduces to 320px; footer stacks to single column |
| Tablet | 744–1128px | Nav shows top franchises only (no mega-menu preview); product cards in 2-3 column grid; hero banner at 400px; footer in 2 columns |
| Desktop | 1128–1440px | Full mega-menu navigation; product cards in 3-4 column grid; hero banner at 480px; footer in 4 columns |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-5 column grid; hero banner at 520px with wider margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px tap target height
- Filter chips are 32px tall with 16px horizontal padding — below the 44px ideal but acceptable for non-primary actions
- Cart icon and account icon in the nav bar are wrapped in 44x44px touch areas even if the icon itself is smaller
- Pagination buttons are 36px tall — consider increasing to 44px for mobile

### Collapsing Strategy
- Mega-menu collapses to a single-column accordion on mobile and tablet
- Product grid collapses from 4-5 columns to 2 columns on tablet, then 1 column on mobile
- Footer collapses from 4 columns to 2 columns on tablet, then 1 column on mobile
- Secondary nav links (support, about) collapse under a "More" dropdown on tablet
- Search bar collapses to an icon-only trigger on mobile, expanding to full width on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from the primary color shift — actual extracted hover colors were not available
- Error state styling (form validation, 404 pages) is assumed from the accent-red — no error-specific hexes were extracted
- Dark mode is not present on the live site; all dark sections use #1f1f1f as a design choice, not a system preference
- The extracted color list includes several checkout-widget colors (#d4edda, #c3e6cb, #00b959) that may belong to Shopify Pay or Afterpay — these have been noted but not used in the core palette
- Font weights for Obvia variants (condensed, expanded, narrow, wide) are assumed based on common usage — actual extracted font-weight values were not available
- Spacing values are inferred from common e-commerce patterns — the live site's exact padding/margin tokens were not extracted
- Animation durations, easing curves, and transition properties were not extracted
- The "bnea" font-family declaration could not be resolved — it may be a custom font or a misspelling; it has been excluded in favor of Obvia and Source Sans Pro which appear more consistently
- Product card hover states (scale, shadow) are not documented as they were not extractable from static CSS
