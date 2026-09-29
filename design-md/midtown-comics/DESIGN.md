---
version: alpha
name: "Midtown Comics"
source_url: "https://www.midtowncomics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy anchor at #00365a sets the frame for a comic-book marketplace that runs on a high-contrast blue primary system — #0257a6, #1058a8, #026cd0, #0057a8 — where every CTA, badge, and link reads as urgent and collectible. The brand's voltage comes from two accent punches: a stop-sign red at #e31c3d for sale tags and clearance badges, and a marigold #f9c642 for star ratings, limited-edition flags, and pre-order callouts. Body type runs Open Sans at 400 weight on a near-white canvas (#f4f4f4), with Roboto reserved for product titles and pricing tables where mechanical clarity matters. Navigation sits as a persistent dark band at full width, the primary search bar rendered in white with a {rounded.full} pill shape against the navy header, while product cards use a soft {rounded.sm} corner and a clean white surface (#ffffff) with a #e1e1e1 hairline. The grid is dense — 4-5 columns on desktop — reflecting a catalog mentality where cover art is the hero and text is subordinate. Badges are sharp: red rectangle for "SALE", yellow pill for "NEW THIS WEEK", blue outline for "PRE-ORDER". The footer collapses into a three-column accordion on mobile, each section headed by a 14px Open Sans semibold label. This is a store that trusts its inventory photography over layout flourishes, using color as a wayfinding system: blue means actionable, red means discounted, yellow means noteworthy.

colors:
  primary: "#0257a6"
  primary-active: "#003cba"
  primary-disabled: "#8ab4e0"
  ink: "#00365a"
  body: "#353535"
  muted: "#545454"
  muted-soft: "#939393"
  hairline: "#bdbdbd"
  hairline-soft: "#e1e1e1"
  canvas: "#f4f4f4"
  surface-soft: "#eaeaea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e31c3d"
  accent-yellow: "#f9c642"
  accent-blue-light: "#0d79f2"
  accent-blue-bright: "#0080ff"
  star-rating: "#f9c642"
  sale-badge-bg: "#e31c3d"
  sale-badge-text: "#ffffff"
  preorder-badge-border: "#0257a6"
  preorder-badge-text: "#0257a6"
  new-badge-bg: "#f9c642"
  new-badge-text: "#00365a"
  footer-bg: "#00365a"
  footer-text: "#ffffff"
  nav-bg: "#00365a"
  nav-text: "#ffffff"
  search-bg: "#ffffff"
  search-text: "#353535"
  search-placeholder: "#939393"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Roboto', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  price-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  product-title:
    fontFamily: "'Roboto', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    border: "2px solid {colors.primary}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.new-badge-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-pill-search:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.search-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  button-pill-search-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.search-text}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "rgba(255, 255, 255, 0.7)"
    typography: "{typography.nav-link}"
    padding: "4px 12px"
  search-bar-nav:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.search-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    placeholderColor: "{colors.search-placeholder}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.product-title}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "2:3"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.accent-red}"
  badge-sale:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.new-badge-bg}"
    textColor: "{colors.new-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-preorder:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.preorder-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
    border: "1px solid {colors.preorder-badge-border}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.nav-link}"
    textColor: "{colors.footer-text}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.link}"
    textColor: "rgba(255, 255, 255, 0.7)"
  footer-link-hover:
    textColor: "{colors.footer-text}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 300px
  hero-banner-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.new-badge-text}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
    height: 48px
  category-grid:
    gap: "{spacing.sm}"
    columns: 4
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 600
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "none"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in {colors.primary} with white text and a {rounded.sm} corner. Used for "Add to Cart", "Checkout", and "Subscribe" actions. On hover, shifts to {colors.primary-active}. Disabled state uses {colors.primary-disabled} with reduced opacity.
**`button-secondary`** — An outlined variant with a white fill, {colors.primary} text, and a 2px solid border. Used for "View Details", "Compare", and secondary checkout flows. Maintains the same {rounded.sm} radius and 40px height as the primary button.
**`button-accent-red`** — A high-urgency button using {colors.accent-red} background. Reserved for clearance sales, limited-time offers, and final markdowns. Same dimensions as `button-primary`.
**`button-accent-yellow`** — A promotional button using {colors.accent-yellow} background with dark text. Used for "Pre-Order Now", "Claim Reward", and loyalty program CTAs.
**`button-pill-search`** — The search bar button rendered as a {rounded.full} pill with white background. Appears in the top navigation area. On focus, the background shifts to {colors.surface-soft}.

### Cards
**`product-card`** — A white card with a {rounded.sm} corner and a 1px {colors.hairline-soft} border. Contains a 2:3 aspect ratio cover image, product title in {typography.product-title}, and pricing in {typography.price-sm}. On hover, the border switches to {colors.primary} and a subtle box shadow appears. Sale prices render in {colors.accent-red}.
**`category-card`** — A larger card used for department navigation. White background with {rounded.sm} corners, 1px hairline border, and centered category name in {typography.title-md}. Hover state elevates with a {colors.primary} border and stronger shadow.

### Badges
**`badge-sale`** — A solid red rectangle ({colors.accent-red}) with white uppercase text. Placed at the top-left corner of product images. Uses {typography.badge} at 11px bold.
**`badge-new`** — A yellow pill shape ({colors.accent-yellow}) with dark text. Used for "NEW THIS WEEK" and "JUST ARRIVED" flags. Full rounded corners.
**`badge-preorder`** — An outlined badge with a white fill, {colors.primary} text, and a 1px {colors.primary} border. Used for upcoming releases and pre-order items.

### Navigation
**`nav-bar`** — A full-width dark navy bar at {colors.nav-bg} with white uppercase navigation links. Height is 56px with {spacing.lg} horizontal padding. Active links have a semi-transparent white background pill.
**`search-bar-nav`** — A white pill-shaped search input embedded in the navigation bar. Uses {colors.search-placeholder} for placeholder text and {colors.search-text} for entered text. 40px height with 8px 16px padding.

### Forms
**`text-input`** — Standard form input with white background, {colors.body} text, and a 1px {colors.hairline} border. On focus, the border thickens to 2px {colors.primary}. Error state uses a 2px {colors.accent-red} border.
**`newsletter-input`** — A full-rounded pill input used in the footer for email collection. No border, white background, 44px height.
**`newsletter-submit`** — A matching pill button adjacent to the newsletter input. Uses {colors.primary} background with white text.

### Footer
**`footer-section`** — A dark navy ({colors.footer-bg}) section with white text. Contains 3-4 columns of links on desktop, each headed by an uppercase {typography.nav-link} label. Links render at 70% white opacity, shifting to full white on hover. Padding is {spacing.xxl} vertically.

### Hero
**`hero-banner`** — A full-width promotional banner with {colors.ink} background and white text. Uses {typography.display-lg} for headline copy. Minimum height of 300px. The CTA button uses {colors.accent-yellow} with dark text for maximum contrast against the dark background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; navigation collapses to hamburger; footer becomes accordion; hero banner reduces to 200px min-height; search bar moves to expandable overlay; filter chips stack vertically |
| Tablet | 744–1128px | 2-3 column product grid; navigation shows top-level links only; footer shows 2 columns; hero banner at 250px min-height; filter chips wrap to 2 rows |
| Desktop | 1128–1440px | 4-5 column product grid; full navigation visible; footer shows 3-4 columns; hero banner at 300px min-height; filter chips in single horizontal row |
| Wide | > 1440px | 5-6 column product grid; max-width container at 1440px; navigation remains full; footer shows 4 columns; hero banner at 350px min-height with wider typography |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Product card tap targets (image, title, price) are independently tappable with 48px minimum touch area
- Filter chips are 32px height — acceptable for touch but recommended minimum is 44px
- Navigation hamburger icon has 48x48px touch area
- Quantity selector buttons have 44x44px touch targets
- Pagination buttons are 36px height — below recommended 44px for touch; consider increasing to 44px on mobile

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Footer columns collapse to accordion panels below 744px, with each section togglable
- Filter sidebar collapses to a horizontal scrollable chip strip on mobile, with a "Filters" button that opens a bottom sheet
- Product grid reduces from 5 columns on wide to 1 column on mobile
- Search bar collapses from inline pill to a full-screen overlay on mobile
- Breadcrumb trail truncates to show only current page and parent category on mobile
- Hero banner text stack collapses from side-by-side to stacked on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; actual hover transitions (duration, easing) not extracted
- Error states for forms (validation messages, error icon placement) not observed on live site
- Dark mode — no evidence of implementation; not extracted
- Loading states (skeleton screens, spinner designs) not captured
- Focus ring styles (color, offset, thickness) not extracted from live CSS
- Dropdown menu styles (mega menu, sub-navigation panels) not observed
- Modal/overlay design (cart drawer, quick-view popup) not captured
- Toast/notification component design not observed
- Typography scale for mobile (responsive font sizes) not extracted — current values are desktop-first
- Color contrast ratios not verified against WCAG AA/AAA standards
- Animation durations and easing curves not extracted
- Icon set beyond Font Awesome not identified — brand may use custom comic-themed icons
- Checkout flow design (Shopify Pay, Klarna, Afterpay widgets) not extracted — colors may include these
- Print stylesheet not observed
- The extracted color list is heavily weighted toward blues and grays with only two accent colors (#e31c3d red, #f9c642 yellow). This may reflect a generic e-commerce palette rather than a distinctive brand identity. The true brand primary may include a more distinctive hue not captured in the extraction.
