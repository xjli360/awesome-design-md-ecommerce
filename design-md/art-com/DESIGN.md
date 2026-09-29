---
version: alpha
name: "Art.com"
source_url: "https://www.art.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Millions of prints compete for the eye on the same white canvas, so the interface earns its keep by receding — neutral grays (#404040, #595959, #737373) carry body copy while catalog imagery does the personality work. The one moment the brand asserts itself is at the call-to-action: a flat crimson (#bd2426) fires on every "Add to Cart" and checkout button, drawing the eye without competing with a Klimt or a Warhol in the adjacent thumbnail. Deep navy (#163959) anchors the top utility bar, category headers, and editorial rail labels, giving hierarchy to a system that otherwise runs entirely on system typography — Arial and Helvetica Neue at modest weights, staying visibly out of the art's way. Radius work is conservative throughout: product cards and input fields use {rounded.xs} corners rather than the pill geometry of lifestyle brands, reinforcing the catalog-department-store sensibility over boutique warmth. The badge system is color-coded and compact — warm orange (#f68b1f) signals "Best Seller," fresh green (#9bca3e) marks new arrivals, and sale pricing inherits the primary crimson, all rendered at 11px uppercase type against white card faces. Link affordances use a standard web blue (#0051c3) with no branded deviation, a deliberate choice that keeps navigation legible without pulling focus from product thumbnails. The page grid is image-forward at every breakpoint: a responsive masonry of square thumbnails, a horizontal-scroll rail for editorial picks, and a dark (#272727) footer that collapses into accordions on mobile. The overall visual language is high-volume and image-forward, trusting the art to supply the personality that the brand interface deliberately withholds.

colors:
  primary: "#bd2426"
  primary-active: "#521010"
  primary-disabled: "#de5052"
  secondary: "#163959"
  secondary-hover: "#2f7bbf"
  accent-blue: "#62a1d8"
  accent-orange: "#f68b1f"
  accent-orange-warm: "#ee730a"
  accent-orange-dark: "#c16508"
  accent-green: "#9bca3e"
  accent-green-muted: "#bada7a"
  link: "#0051c3"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#ebebeb"
  hairline-strong: "#dedede"
  rule: "#bfbfbf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  category-label:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    padding: 8px 16px
    height: 40px
    focus-border: "2px solid {colors.secondary}"
  nav-bar-top:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    height: 32px
    padding: 0 24px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    border-bottom: "1px solid {colors.hairline}"
    padding: 0 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    padding: 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    height: 40px
    padding: 0 16px
    searchButtonBackgroundColor: "{colors.secondary}"
    searchButtonColor: "{colors.on-secondary}"
    focus-border: "2px solid {colors.secondary}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
    height: 28px
  badge-bestseller:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  price-display:
    textColor: "{colors.primary}"
    typography: "{typography.price}"
  price-original:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 360px
    padding: 48px 64px
  category-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    border-bottom: "2px solid {colors.hairline}"
    padding: 24px 0
    labelTypography: "{typography.category-label}"
    labelColor: "{colors.secondary}"
  editorial-rail:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.category-label}"
    labelColor: "{colors.secondary}"
    padding: 32px 0
  breadcrumb:
    textColor: "{colors.muted-soft}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
    separator: "/"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-secondary}"
    linkColor: "{colors.hairline}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — Flat crimson (#bd2426) with uppercase white type at 15px/700 weight and a conservative {rounded.xs} corner radius, used for every cart, checkout, and primary conversion action. Hover and active states step down to the dark maroon {colors.primary-active} (#521010); the disabled state uses the washed pink {colors.primary-disabled} (#de5052) with no opacity fade. Height holds at 44px to maintain a consistent CTA footprint across the catalog grid.

**`button-secondary`** — White fill with a 2px crimson border and matching crimson type, carrying the same {rounded.xs} and uppercase {typography.button-md}. Used for "Save to Collection," wishlist actions, and secondary CTAs where a ghost outline keeps the art-first canvas visible behind the interaction layer.

**`button-tertiary`** — Neutral canvas fill with a 1px {colors.hairline-strong} border and {colors.body} text at {typography.button-sm}. Appears on filter toggles, sort controls, and low-hierarchy shelf actions.

### Search

**`search-bar`** — A horizontal input at 40px height with a 1px {colors.hairline-strong} border and a flush right-side submit button block in {colors.secondary} navy. The search button carries a white icon; on input focus the border upgrades to 2px navy. Autocomplete suggestions drop below in a white panel with {rounded.xs} corners and {typography.body-sm} suggestion rows, artist and subject grouped into labeled sections.

### Product Card

**`product-card`** — A square 1:1 image container with a 1px {colors.hairline} border and no drop shadow at rest. Title renders in {typography.body-sm} at {colors.ink} below the image; price in {typography.price-sm} in {colors.primary} crimson. On hover, a subtle `box-shadow: 0 2px 8px rgba(0,0,0,0.12)` lifts the card without scaling the image. Badge overlays ({badge-bestseller}, {badge-sale}, {badge-new}) pin to the top-left corner of the image area.

### Navigation

**`nav-bar-top`** — A 32px utility strip in {colors.secondary} navy (#163959) holding promotional copy, help links, and account/sign-in shortcuts in 12px white type. Sits above the main nav and is the first brand color a visitor sees.

**`nav-bar`** — White bar at 60px height with a 1px {colors.hairline} bottom border. Logo sits left; centered search bar occupies the middle column; cart count badge, account, and favorites icons anchor right. Category labels expand into full-width mega-menu panels on hover, presenting subcategory grids with thumbnail previews.

### Badges

**`badge-bestseller`** — Warm orange (#f68b1f) fill with white uppercase 11px type, {rounded.xs}, pinned to the image top-left. The orange reads warm and promotional without alarm.

**`badge-sale`** — Crimson (#bd2426) fill matching the primary action color, providing strong reinforcement that a price has been reduced. Paired with a {price-original} strikethrough on the card below.

**`badge-new`** — Fresh green (#9bca3e) fill with {colors.ink} dark text, differentiating new arrivals from promotions in the color-coded badge vocabulary.

### Hero Banner

**`hero-banner`** — Full-width navy (#163959) panel with large white headline at {typography.display-xl}. Campaign heroes layer a full-bleed photograph over the navy base with a semi-transparent overlay ensuring text legibility. A single {button-primary} CTA sits left-aligned or centered below body copy at {typography.body-md}.

### Editorial Rail

**`editorial-rail`** — A {colors.surface-soft} (#f5f5f5) section with a {typography.category-label} uppercase label in {colors.secondary} navy above a horizontally scrollable row of {product-card} tiles. Used for "Trending Now," "Editor's Picks," and artist spotlights. The navy label creates a visual anchor that separates editorial context from the open catalog grid above and below.

### Category Header

**`category-header`** — White background with a large {typography.display-md} heading and a 2px {colors.hairline} rule below. A {typography.category-label} uppercase subtitle in {colors.secondary} sits above the main heading for breadcrumb-style context. Used at the top of every browse and search results page.

### Breadcrumb

**`breadcrumb`** — {typography.caption} in {colors.muted-soft} gray, "/" separator, with the active (current page) segment in {colors.body}. Sits below the nav-bar and above the category-header on product detail and browse pages.

### Price Display

**`price-display`** — Current prices render in {colors.primary} crimson at {typography.price} weight 700, making the price a visual signal that rhymes with the add-to-cart button. Where a sale applies, the original price appears immediately to the right or below in {typography.price-sm} with `text-decoration: line-through` at {colors.muted}.

### Footer

**`footer`** — A full-width {colors.ink} (#272727) footer with four columns on desktop: About, Help, Browse, and Connect. Column headings in {typography.title-sm} in {colors.hairline} gray; links in {typography.body-sm} in slightly lighter {colors.hairline}. Legal copy and copyright sit on a separate bottom row in {typography.caption}. Link color uses {colors.hairline} for readability against the dark background without competing with the page content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar moves to a full-width row below the logo strip; top utility nav collapses into the hamburger drawer; hero banner reduces to 220px tall; footer columns become tap-to-expand accordions; editorial rails shift to horizontal scroll carousels |
| Tablet | 744–1128px | Two-to-three column product grid; mega-menu replaced by a left slide-in drawer; search bar retains inline position in the nav; category pills appear as a horizontally scrollable strip below the nav |
| Desktop | 1128–1440px | Four-column product grid; full mega-menu dropdowns on nav hover; hero at 360px min-height; footer renders all four columns inline |
| Wide | > 1440px | Container max-width centers at ~1440px; product grid stays at four columns with increased gutters; hero may use extended full-bleed image with centered content block |

### Touch Targets

- All primary and secondary buttons maintain 44px minimum tap height
- Nav icon buttons (cart, account, search toggle) use 44×44px hit areas regardless of visual icon size
- Category pills on mobile use minimum 36px height with sufficient horizontal padding
- Search input field renders at 44px tall on mobile to prevent iOS auto-zoom on focus
- Breadcrumb links pad to at least 32px touch height on mobile via increased vertical padding

### Collapsing Strategy

- Mega-menu navigation collapses to a hamburger icon on tablet and below; drawer slides from the left with a full category tree and back-navigation
- The top navy utility bar collapses into the hamburger drawer on mobile; a dismissible promo banner may surface its most important message at the top of the page
- Badge and price information on product cards remain visible at all breakpoints; artist name truncates to one line with ellipsis on narrow cards
- Editorial rails switch from a static multi-column grid to a horizontal scroll carousel on mobile, preserving card size rather than shrinking content
- Footer four-column grid reflows to stacked sections with disclosure accordions; legal links remain a single inline row at the very bottom

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was served behind Cloudflare bot protection at extraction time; page title returned "Attention Required! | Cloudflare" — no live DOM, rendered component markup, or computed CSS was captured
- Exact primary font is unknown; extraction yielded only system stacks (Arial, Helvetica Neue, -apple-system); Art.com may use a licensed typeface not visible in static assets
- No confirmed border-radius values from live components — {rounded.xs}/{rounded.sm} values are inferred from the utilitarian catalog style, not measured
- No spacing or grid measurements extracted; container widths, column gutters, and section padding are approximated from the scale and category of the site
- Button height, padding, and exact CTA color treatment could not be confirmed from live product detail or cart flow pages
- Several extracted colors (#bada7a, #516b1d, #9bca3e, #bada7a) may belong to a specific promotional campaign or seasonal theme rather than the evergreen brand palette
- Dark-mode or alternate-theme variants are unknown — no @media prefers-color-scheme rules were captured
- Mega-menu structure, column counts, and thumbnail dimensions in navigation panels could not be confirmed without live DOM access
- Cart and checkout flow component styling (order summary, address forms, payment inputs) entirely unconfirmed
