---
version: alpha
name: "BigBadToyStore"
source_url: "https://www.bigbadtoystore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  BigBadToyStore runs its catalog on density — tens of thousands of SKUs packed into a grid where every card competes for attention with pre-order badges, sale ribbons, and arrival-date callouts. The brand's primary red (approximately #cc0000) does double duty as logo voltage and the sole CTA accent color against a near-black navigation bar (#1a1a1a), a contrast stack that reads more like a specialty-electronics storefront than a traditional toy shop. Type stays functional, no custom typefaces or editorial lettering, because the real surface is the product photography: box art and prototype photos carry all the visual weight the grid's tight gutters allow. The signature "Pile of Loot" feature, which lets collectors park purchases until a single consolidated shipment makes financial sense, speaks to a customer tracking dozens of pre-orders simultaneously who values logistical control over packaging theater. Badge layering is the dominant UI idiom: a single product tile might wear four simultaneous overlays — NEW, SALE, PRE-ORDER, and an EXCLUSIVE ribbon — without the card feeling broken, because the grid's relentless rhythm normalizes the visual load. Buttons are blunt rectangles with no meaningful radius ({rounded.xs}), reinforcing a catalogue-store register that prioritizes throughput over luxury. The footer sprawls wide into deep-link columns covering every sub-niche in the hobby. The dark header with red logo sits fixed atop every page, grounding navigation in the brand's one visual constant regardless of how far into a subcategory a user dives. Color-coded badge variants — blue for pre-order (#0066cc), green for new (#339900), purple for exclusive (#663399), red for sale (#cc0000) — create a four-state status language that experienced collectors read at a glance across the dense grid without hovering or reading copy.

colors:
  primary: "#cc0000"
  primary-active: "#aa0000"
  primary-disabled: "#e88888"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-preorder: "#0066cc"
  badge-new: "#339900"
  badge-exclusive: "#663399"
  badge-sale: "#cc0000"
  star-rating: "#ffaa00"
  price-sale: "#cc0000"
  pile-of-loot: "#ff6600"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
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
    padding: 9px 19px
    border: "1px solid {colors.primary}"
    height: 40px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    width: "100%"
  button-pile-of-loot:
    backgroundColor: "{colors.pile-of-loot}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 36px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
    imageAspect: "1/1"
    gap: "{spacing.xs}"
  product-title:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    lineClamp: 2
  product-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  product-badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  product-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  product-badge-exclusive:
    backgroundColor: "{colors.badge-exclusive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-tag-sale:
    textColor: "{colors.price-sale}"
    typography: "{typography.price-display}"
  price-tag-msrp:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  star-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  pre-order-indicator:
    textColor: "{colors.badge-preorder}"
    typography: "{typography.caption}"
    fontStyle: italic
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separator: ">"
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
  pile-of-loot-banner:
    backgroundColor: "{colors.pile-of-loot}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"

## Components

### Buttons

**`button-primary`** — A flat-cornered red rectangle ({rounded.xs}) at full #cc0000 saturation, used for primary catalog actions. On hover it transitions to `primary-active` (#aa0000) with no animation delay, a blunt response curve matching the utilitarian register. The disabled state washes to #e88888 and removes pointer events.

**`button-add-to-cart`** — Full-width variant of the primary button, stretching to fill the product card's footer at 40px height. Every card in the grid shares this footprint, so rows of red buttons become a predictable rhythmic baseline rather than competing CTA targets.

**`button-pile-of-loot`** — Orange (#ff6600) at the same sharp-cornered shape, placed immediately below the add-to-cart button on product pages. The distinct color creates an unambiguous two-path decision — buy now versus hold for later — without requiring copy-reading on a dense page.

**`button-secondary`** — White fill, red border, red text. Appears for secondary actions like "Notify Me When In Stock," "Add to Wishlist," and filter confirmations where the primary CTA slot is occupied. The shared red border color keeps secondary actions visually tied to the brand without competing for hierarchy.

### Product Card

**`product-card`** — Hard-edged ({rounded.none}), hairline-bordered tiles built for six-across grid density. The card leads with a square 1:1 product image, followed by a two-line clamped title via `product-title` and a price row. Badge overlays stack in the top-left image corner using color-coded badge variants; up to four simultaneous badges are a common occurrence in BBTS's catalog without triggering a layout break. The no-radius treatment aligns every card flush to a pixel grid, enabling the dense mosaic.

**`price-tag` / `price-tag-sale` / `price-tag-msrp`** — Price row uses bold 18px ink for standard price, switches to #cc0000 for the sale price, and renders the original MSRP in muted gray with a strikethrough beside it. The red sale price intentionally matches the primary button, reinforcing the red-means-action signal established across the UI.

### Navigation

**`nav-bar`** — A near-black (#1a1a1a) primary bar at 48px height carrying the red BBTS logo on the left and a wide search input to its right. The dark ground makes the logo's red pop without any additional framing treatment.

**`nav-bar-secondary`** — A red (#cc0000) secondary bar directly below the primary, containing the full category taxonomy in 13px bold white nav-link labels. The two-bar system separates brand identity (top, dark) from product taxonomy (bottom, red) — a catalog-store convention that makes subcategory switching fast.

**`search-bar`** — A left-anchored input spanning most of the top nav width, signaling search as the primary browsing mode. A red icon button anchors the right end; the input uses `body-md` at 14px with minimal padding to keep it compact in the fixed-height nav.

### Badges

**`product-badge`** (SALE) — Red (#cc0000) fill, white uppercase text at 10px with 0.5px tracking, no border radius. Sits flush in the product image corner.

**`product-badge-preorder`** — Blue (#0066cc) on the same sharp rectangle. Pre-order is BBTS's dominant inventory state, with items listing 12–24 months before ship; blue separates availability status from promotional status in the color-code language.

**`product-badge-new`** — Green (#339900), applied to items within 30 days of listing. Gives active browsers a freshness signal scannable at grid distance.

**`product-badge-exclusive`** — Purple (#663399), reserved for BBTS exclusives. Functions as a scarcity differentiator that justifies collector attention on items unavailable elsewhere.

### Pile of Loot

**`pile-of-loot-banner`** — An orange (#ff6600) informational banner surfaced on cart and pre-order confirmation pages explaining the warehouse-hold shipping option. Orange is the only warm non-red accent in the palette, giving this feature a visual identity distinct from the primary purchase flow. The `button-pile-of-loot` on product pages shares this color to build recognition of the feature across contexts.

### Footer

**`footer`** — Near-black (#1a1a1a) matching the top nav, creating a dark bookend that frames the white product canvas. Contains four to six deep-link columns across categories — Action Figures, Statues, Model Kits, Pre-Orders, New Arrivals, Sale — in `body-sm` white text with red hover states matching the primary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Two-column product grid; category nav collapses into hamburger drawer; search bar moves below logo row; dual nav bars merge to single dark bar; pile-of-loot button stacks below add-to-cart |
| Tablet | 744–1128px | Three- to four-column grid; category nav shows as horizontal scroll row; left-rail filters hidden behind toggle button |
| Desktop | 1128–1440px | Five- to six-column grid; left-rail category tree visible; dual nav bars fully rendered; filter sidebar persistent |
| Wide | > 1440px | Six-column grid within max-width container, centered with symmetrical gutters at page edges |

### Touch Targets

- Add-to-cart and Pile of Loot buttons are full-width at 40px height — sufficient tap area on narrow viewports
- Badge overlays are purely decorative; they carry no tap targets or tooltips
- Category nav items in the mobile hamburger drawer render at a minimum 44px row height
- Search input spans full width on mobile for easy single-thumb activation

### Collapsing Strategy

- Left-rail filter panel becomes a full-screen modal overlay triggered by a "Filter / Sort" button on mobile and tablet
- Product grid collapses: 6 columns → 4 (tablet) → 2 (mobile)
- Secondary red category bar folds into the hamburger menu on mobile; it becomes the primary navigation surface inside the drawer
- Product detail page switches from two-column (image left, info right) to stacked single-column below 744px
- Breadcrumbs truncate to the last two path segments on mobile to preserve horizontal space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site (likely JS-loaded design tokens or anti-bot protection); all palette values are estimated from widely visible brand assets — logo, screenshots, and historical UI references
- No font-family stacks were captured; `Arial, Helvetica, sans-serif` is a best-guess system fallback — BBTS may use a licensed or web-loaded typeface not visible to the extractor
- Exact border-radius values could not be confirmed; {rounded.xs} (4px) is inferred from the flat catalog-store aesthetic visible in brand screenshots
- Star-rating amber (#ffaa00) is approximated; the precise shade was not extractable
- Pile of Loot orange (#ff6600) is approximate; the exact brand value for this accent was not confirmed from a live source
- Badge color set (blue, green, purple) is inferred from common BBTS UI patterns; exact hex values not confirmed
- No spacing or grid-gap measurements were extracted; all spacing tokens use conventional catalog-store defaults
- Animation and transition timing data is entirely absent
- Pre-order date display format and countdown component styling could not be confirmed
