---
version: alpha
name: "GT Omega"
source_url: "https://www.gtomega.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A racing-red #c62a32 pulse drives GT Omega's entire interface — the same voltage that fires through every "Add to Cart" button, category badge, and checkout CTA, set against a near-black #222222 ink and a cool silver #dadce0 hairline that reads like automotive trim. The brand lives in the gap between sim-racing hardware and gaming furniture, and the design mirrors that: Rubik at 400/500 weight keeps the interface legible at 14px body copy while 20px display headings carry the weight of product names and category headers. Product photography — carbon-fiber textures, stitched PU leather, aluminum wheel-rim details — does the heavy lifting, with the UI stepping back into a clean #f7f7f7 surface-soft canvas. Badges and price tags sit in #d92017 or #ffaa47 for sale flags, while the secondary #279a4b green signals "In Stock" with the same confidence as a pit-lane light. Every corner is softly radiused at 8px for buttons and 12px for cards — no sharp edges, but no pill-shaped excess either; the system reads as precision-engineered rather than playful. The top nav carries a full-width #222222 bar with white text and a sticky search, while the footer collapses into a dense #2c2d2e grid of legal links, payment icons, and newsletter forms. The overall impression is a storefront that trusts its product imagery and uses color as a binary signal — red for action, green for confirmation, orange for attention, gray for structure.

colors:
  primary: "#c62a32"
  primary-active: "#b91b14"
  primary-disabled: "#dedede"
  ink: "#222222"
  body: "#454545"
  muted: "#aaaeb6"
  muted-soft: "#dadce0"
  hairline: "#dadce0"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ffaa47"
  accent-green: "#279a4b"
  accent-red: "#d92017"
  dark-surface: "#2c2d2e"
  dark-ink: "#121212"

typography:
  display-xl:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 9px 13px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 500
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    height: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  newsletter-input:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.muted}"
  newsletter-input-focus:
    border: "2px solid {colors.primary}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: "{spacing.md} 0"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 0 0"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  pagination-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  rating-stars:
    color: "{colors.accent-orange}"
    fontSize: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-card-author:
    typography: "{typography.title-sm}"
    fontWeight: 500
  review-card-date:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the entire site, rendered in the brand's racing red #c62a32 with white text. On hover, it shifts to the deeper #b91b14 active state. When disabled, it fades to #dedede with muted text, signaling the action is unavailable. Padding is 12px top/bottom and 24px left/right, giving it a solid, confident footprint at 44px tall.

**`button-secondary`** — An outlined variant with a white background, dark ink text, and a 1px hairline border. Used for "View Details" and secondary product actions. On active state, the border thickens to match the ink color and the background shifts to surface-soft.

**`button-accent-orange`** and **`button-accent-green`** — Smaller, purpose-built buttons for sale flags (#ffaa47) and stock confirmations (#279a4b). These sit at 36px tall with tighter padding, used inside product cards and cart line items where real estate is limited.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounded corners and no internal padding (images bleed to the edges). The image area uses top-rounded corners only, while the title and price stack below with base-16px padding. Badges overlay the image area in the top-left corner, using the primary red for general labels, accent-red for sale tags, and accent-green for "In Stock" indicators.

**`review-card`** — A bordered card for customer reviews, with 12px rounded corners and base-16px internal padding. The author name sits in title-sm weight 500, the date in caption muted, and the review body in body-sm. Star ratings render in accent-orange.

### Navigation
**`nav-bar`** — A full-width dark bar at #222222 with white navigation links at 14px weight 500. The bar is 64px tall and sticks to the top on scroll. Active nav links switch to the primary red, while inactive links render in the muted-soft #dadce0. The logo sits left-aligned, with the search bar and cart icon right-aligned.

**`category-strip`** — A horizontal scrollable strip below the hero, on a surface-soft background. Category tabs toggle between an active state (filled primary red) and an inactive state (white with a hairline border). Each tab is 36px tall with 8px horizontal padding.

### Forms
**`text-input`** — A standard 44px-tall input with a white background, 1px hairline border, and 8px rounded corners. On focus, the border doubles to 2px and switches to primary red. Used for search, newsletter signup, and checkout fields.

**`select-input`** — Matches the text-input dimensions and styling, used for product variant selection (size, color, etc.).

**`newsletter-input`** — A dark variant of the text input, set on the #121212 footer background with a muted border and white text. The companion newsletter-button sits directly adjacent in primary red.

### Footer
**`footer`** — A dense, dark section at #2c2d2e with muted-soft link text and white headings. Links are 14px weight 400 and shift to white on hover. The layout uses a multi-column grid with newsletter signup, legal links, and payment icons. Padding is 48px top/bottom with base-16px horizontal.

### Badges
**`product-card-badge`** — Small uppercase labels at 11px weight 600, used for "NEW", "BESTSELLER", or "LIMITED EDITION" tags. The primary red variant is the default, with accent-red for sale and accent-green for stock status. Padding is 2px top/bottom and 8px left/right, with 4px rounded corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces full nav-bar, category strip becomes horizontal scroll, hero banner reduces to 250px height, footer collapses to single column, search bar moves to overlay |
| Tablet | 744–1128px | Two-column product grid, nav-bar shows limited links (logo + search + cart + hamburger), hero banner at 320px height, footer uses 2-column grid, category strip shows 4-5 visible tabs |
| Desktop | 1128–1440px | Three-column product grid, full nav-bar with all links visible, hero banner at 400px height, footer uses 4-column grid, category strip shows all tabs |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero banner at 480px height with parallax effect, footer uses 4-column grid with wider spacing |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav-bar links have a 48px touch area (padding + height).
- Product card CTAs ("Add to Cart", "Quick View") are at least 44px tall.
- Quantity selector buttons are 44px x 44px.
- Category tabs are 36px tall with 16px horizontal padding, meeting the 44px touch target when combined.

### Collapsing Strategy
- The full nav-bar collapses to a hamburger menu at tablet widths and below.
- The multi-column footer collapses to a single column on mobile, with accordion-style sections for link groups.
- The hero banner collapses to a single image with text overlay on mobile (no dual-column layout).
- Product filters move from a sidebar to a bottom sheet on mobile.
- The category strip becomes a horizontal scrollable row on mobile, with arrow indicators for overflow.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components were not fully extractable from the live site; only primary and secondary button hover states are confirmed.
- Error styling for form inputs (red border, error message typography) was not observed and is inferred from common patterns.
- Dark mode styling is not present on the live site; all observed pages use a light theme.
- Sub-brand or collection-specific color palettes (e.g., "GT Omega Racing" vs "GT Omega Office") were not extractable.
- Animation durations and easing curves (button press, card hover lift, nav scroll) were not measurable.
- Modal and overlay styling (cart drawer, quick-view popup) was not observed in the extraction.
- The exact font-weight for Rubik at different sizes is inferred from common usage; the live site may use additional weights.
- Checkout flow styling (Shopify Checkout) is not included as it uses Shopify's default theme.
- The extracted color list includes #e97f32 and #279a4b which may be Klarna/Afterpay widget colors rather than brand colors; they are retained as accent-orange and accent-green respectively based on observed usage.
