---
version: alpha
name: "LD Products"
source_url: "https://www.ldproducts.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Orange (#ff5501) interrupts institutional blue (#1979c3) at every conversion moment — add-to-cart buttons, deal callout strips, countdown banners — a color pairing that declares "trust us, act now" in one visual beat. The palette otherwise retreats into a long gray corridor: #d1d1d1 borders, #f2f2f2 surfaces, #7d7d7d secondary text — a deliberately un-branded shell that pushes products, yield figures, and compatibility tables to the foreground. Open Sans carries every scale from 28px hero headers down to 11px compatibility badges without weight variation; it is a functional choice matching the utilitarian register of a business-supplies catalog rather than a lifestyle store. Warm amber surfaces — #fdf0d5 fields with #6f4400 type — lift deal pricing out of the gray lattice with a receipt-stub warmth that signals savings without screaming clearance. Dark green (#006400) marks compatibility check marks and "You Save" tallies, anchoring the eye at the moment of purchase justification. {rounded.xs} corners on product cards and search inputs signal a no-frills Magento architecture; there are no pill shapes or soft radii except on promotional badge chips. Pricing display is the real hero content: OEM original struck through in muted gray beside the LD savings figure in bold — that contrast is the brand's core UI gesture, repeated on every product tile, every cart line, every confirmation email. No proprietary typeface, no illustrated mascot, no seasonal hero imagery — just ink pricing mathematics, surfaced clearly enough that the customer can verify the savings and proceed.

colors:
  primary: "#1979c3"
  primary-active: "#006bb4"
  primary-disabled: "#68a8e0"
  accent: "#ff5501"
  accent-warm: "#ff9635"
  savings: "#006400"
  deal-surface: "#fdf0d5"
  deal-text: "#6f4400"
  deal-text-light: "#c07600"
  error: "#e02b27"
  ink: "#111111"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#777777"
  strikethrough: "#8f8f8f"
  hairline: "#d1d1d1"
  hairline-soft: "#e4e4e4"
  border-mid: "#c2c2c2"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#f0f0f0"
  surface-mid: "#e8e8e8"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-strike:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.22px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  breadcrumb:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-deal:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-deal-hover:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
  text-input-focus:
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  nav-bar-top:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
  search-button:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    border: "1px solid {colors.primary}"
    shadow: "0 2px 8px rgba(25,121,195,0.15)"
  price-current:
    textColor: "{colors.accent}"
    typography: "{typography.price-display}"
  price-strike:
    textColor: "{colors.strikethrough}"
    typography: "{typography.price-strike}"
    textDecoration: line-through
  savings-badge:
    backgroundColor: "{colors.savings}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  deal-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  deal-callout:
    backgroundColor: "{colors.deal-surface}"
    textColor: "{colors.deal-text}"
    border: "1px solid {colors.deal-text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  compatibility-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  compatible-check:
    textColor: "{colors.savings}"
    typography: "{typography.body-sm}"
    fontWeight: 600
  breadcrumb-nav:
    textColor: "{colors.primary}"
    typography: "{typography.breadcrumb}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 32px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  promo-strip:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  hero-banner:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.section}"
  ink-type-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  ink-type-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — Blue (#1979c3) fill with white text and {rounded.xs} corners; the default action button for navigation links, account actions, and secondary page CTAs. Hover darkens to #006bb4; disabled renders at the lighter #68a8e0 to preserve the blue register without implying interactivity. Height is fixed at 40px across all contexts to maintain a consistent touch target.

**`button-deal`** — Orange (#ff5501) fill used at the highest-urgency conversion moments: Add to Cart on product pages, "Shop Now" on promotional banners, and bundle deal triggers. Orange is visually louder than the structural blue, creating a clear action hierarchy where purchase intent outranks browsing navigation. Hover warms to #ff9635.

**`button-secondary`** — White canvas with 1px primary-blue border and blue text; used for Compare, View Details, Add to Wishlist, and other secondary actions. Preserves brand color signal at low visual weight.

### Search Bar
**`search-bar`** + **`search-button`** — A wide white input field with no border-radius on its right edge, butting flush against the orange search-trigger button. This joined unit — white input against orange submit — is the most distinctive interface pattern on the site: the two elements read as one horizontal control bar. The orange button uses {typography.button-md} at 700 weight. At mobile the pair expands to full viewport width.

### Navigation
**`nav-bar-top`** + **`nav-bar`** — Two stacked horizontal bars form the header. The upper strip (32px, near-black #111111) holds account links, order tracking, and phone support in caption-scale white type. The lower bar (44px, primary blue #1979c3) holds category navigation in 14px 600-weight Open Sans. This two-tier header is common to high-SKU catalog stores and signals both a utilitarian catalog and a customer-service-first value proposition simultaneously.

### Product Card
**`product-card`** — White canvas with 1px #d1d1d1 border and {rounded.xs} corners; hover adds a primary-blue border and a soft blue drop shadow. The card interior stacks top-to-bottom: printer compatibility thumbnail → product name in {typography.title-sm} → yield figure and page count in {typography.caption} → price pair (struck OEM price above LD price) → Add to Cart button at full card width. Horizontal two-column layout at mobile collapses image to 80×80px thumbnail on the left with price and button on the right.

### Pricing Display
**`price-current`** — Orange (#ff5501) at 24px 700 weight; the visually loudest element on any product card, deliberately outweighing the product name to center the value proposition. **`price-strike`** — Muted gray (#8f8f8f) at 14px regular with `text-decoration: line-through`, rendering the OEM reference price as a visible discount anchor immediately above the LD price. This struck/live pairing is the brand's core UI gesture and appears on every tile, cart row, and order summary.

### Savings & Deal Badges
**`savings-badge`** — Dark green (#006400) rectangle with white uppercase type at 11px; appears in the product-card corner or beside the price pair to quantify "You Save $X.XX." Green is used nowhere else in the palette, making it an unambiguous savings signal. **`deal-badge`** — Orange accent with white uppercase type; flags "HOT DEAL," "BEST SELLER," or time-limited promotions. Both share {rounded.xs} — no pill shapes — to align with the flat catalog grid register.

### Deal Callout
**`deal-callout`** — Warm amber (#fdf0d5) surface with #6f4400 text and a 1px #c07600 border; appears as an inline callout below cart totals or on product pages to surface coupon codes, bulk tier discounts, or free-shipping thresholds. The amber warmth visually separates it from gray system notices and orange CTAs without adding a fourth brand signal.

### Compatibility Check
**`compatible-check`** — Dark green (#006400) text at {typography.body-sm} weight 600, typically preceded by a check glyph from the magento-icons font. Used on product pages and category filters to confirm "Compatible with [Printer Model]." Anchors the purchase decision at the precise moment of compatibility verification.

### Ink-Type Tabs
**`ink-type-tab-active`** + **`ink-type-tab-inactive`** — Toggle tabs used on category and product pages to switch between Compatible, Remanufactured, and Original OEM ink sets. Active tab fills with primary blue; inactive renders on soft gray with muted text. Both share {rounded.xs} corners. The tab row sits above the product grid and directly beneath the breadcrumb.

### Promo Strip
**`promo-strip`** — Full-width orange (#ff5501) band positioned just beneath the nav bar or above the footer, carrying a single promotional message in {typography.title-sm}. Used for sitewide free-shipping thresholds ("Free Shipping on Orders Over $50") or percentage-off announcements. The strip is the one layout element that bleeds edge-to-edge at all breakpoints.

### Footer
**`footer`** — Near-black (#111111) background with a four-column link grid; column headings in {typography.title-sm} white, links in {typography.body-sm} at #d1d1d1. The hard color break from the white product grid functions as a clear page terminus. Typical columns: Customer Service, My Account, About LD Products, and Popular Printer Brands.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar full-width with flush orange button; nav collapses to hamburger drawer; product cards switch to horizontal two-column (80px thumbnail left, text+price+CTA right); promo strip wraps to two lines; breadcrumb hidden |
| Tablet | 744–1128px | Two-column product grid; top-level nav categories visible; search bar fixed width in header center; left-rail filters shift to slide-up drawer; deal callouts inline at 50% width |
| Desktop | 1128–1440px | Three- or four-column product grid; full two-tier navigation bar; left-rail category filter panel on category pages; breadcrumb visible; hero banner at full height |
| Wide | > 1440px | Content max-width ~1440px centered; product pages shift to left-rail filter + product grid + right-rail upsell three-column layout; footer four-column grid full-width |

### Touch Targets
- All interactive buttons minimum 40px height (button-primary, button-deal, search-button)
- Pagination controls minimum 32px height with {spacing.sm} gap between page numbers
- Nav links in collapsed mobile hamburger drawer minimum 48px row height for thumb reach
- Add to Cart button full card width on mobile product cards
- Ink-type tab minimum 36px height with {spacing.md} horizontal padding

### Collapsing Strategy
- Two-tier nav (black top bar + blue category bar) merges into a single hamburger drawer below 744px; phone number and account link promoted to top of open drawer
- Left-rail category and brand filters shift to a slide-up sheet on mobile/tablet, triggered by a "Filter & Sort" button pinned above the product grid
- Horizontal product card at mobile collapses image to 80×80px thumbnail; price-current and Add to Cart retain full visual weight on the right column
- Breadcrumb hidden on mobile; category display heading at {typography.display-sm} serves as contextual wayfinding
- Footer four-column link grid collapses to single-column accordion on mobile, each section header tappable to expand
- Deal callout strips stack vertically at mobile rather than displaying inline beside price

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; browser chrome treatment inferred from dominant blue palette
- Custom icon fonts (magento-icons, boilerplate-theme-icons) not individually documented; only font-family names are known — individual glyph codepoints unavailable
- Exact box-shadow values not extractable from color extraction; values approximated from Magento storefront conventions
- Hover and focus transition timing (duration and easing curve) not extracted; 150–200ms ease assumed
- Whether Add to Cart buttons use orange (#ff5501) or blue (#1979c3) by default could not be confirmed without live interaction; both are present in the palette and may differ per page template
- Exact nav breakpoint pixel value not confirmed; 744px inferred from common Magento responsive grid
- Product photography treatment (white-background vs. packaging shot) not determinable from color extraction
- Font loading strategy (FOUT handling, font-display) not observed
- Mobile header height may vary depending on whether the search bar collapses into the nav bar or persists as a separate row
