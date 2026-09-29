---
version: alpha
name: "En Route"
source_url: "https://www.enroutejewelry.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Burnt paprika (#ef4f29) runs the entire visual argument — every add-to-cart button, every promotional badge, every hover state erupts from the same compressed flame against an ink-black (#1a1a1a) ground, while the rest of the canvas retreats into a family of near-white neutrals (#fafafa through #f4f4f4) that let gold, silver, and gemstone product photography read without competition. Simvoni, a display font exclusive to the brand's type stack, handles the editorial voice at large sizes — its distinct letterforms mark collection headers and hero lockups — while Poppins carries all navigation, body copy, and UI labels at weights that stay trim and contemporary. The palette is deliberately minimal: two warm near-blacks (#231815, #1a1a1a), a ladder of mid-grays for muted text and hairlines, and two accent outliers — a soft peach (#f9bda4) that softens promo surfaces and a muted sage green (#2d8a4e, surface tint #f0faf0) reserved for availability tags and success confirmations. Nothing in the gray ladder ventures to cool blue-gray; the entire spectrum tilts warm, keeping the terracotta primary emotionally coherent from hero to footer. Rounded values are restrained — `{rounded.xs}` on buttons and inputs, `{rounded.sm}` on cards — suggesting a brand that wants clean edges over the softness of a lifestyle marketplace. Product cards carry a tight grid, price typography sits at `{typography.price-display}` in near-black, and the struck-through compare-at price uses `{colors.muted}` so the discount reads clearly without the shouting red that fast-fashion brands rely on. The hero typically runs a full-bleed photograph with an overlay text column, and navigation defaults to a transparent-to-solid scroll behavior common on Shopify storefronts of this weight class.

colors:
  primary: "#ef4f29"
  primary-hover: "#e8431e"
  primary-active: "#d32f2f"
  primary-disabled: "#f9bda4"
  ink: "#1a1a1a"
  ink-deep: "#0d0c0c"
  body: "#222222"
  muted: "#737373"
  muted-mid: "#888888"
  muted-soft: "#8c8c8c"
  hairline: "#e5e5e5"
  hairline-soft: "#ebebeb"
  hairline-strong: "#d0d0d0"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#f8f8f8"
  surface-neutral: "#f4f4f4"
  on-primary: "#ffffff"
  accent-peach: "#f9bda4"
  accent-green: "#2d8a4e"
  accent-green-surface: "#f0faf0"
  sale-red: "#ff4d4f"

typography:
  display-xl:
    fontFamily: "'Simvoni', 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Simvoni', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Simvoni', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-compare:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  collection-label:
    fontFamily: "'Poppins', Inter, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1px
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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline-strong}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    padding: "{spacing.sm}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    compareAtTypography: "{typography.price-compare}"
    compareAtColor: "{colors.muted-mid}"
    gap: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 560px
    overlayOpacity: 0.35
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  stock-badge:
    backgroundColor: "{colors.accent-green-surface}"
    textColor: "{colors.accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  collection-header:
    backgroundColor: "{colors.surface-neutral}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.collection-label}"
    labelColor: "{colors.muted}"
    headlineTypography: "{typography.display-md}"
    padding: "{spacing.xl} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline-strong}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
  price-row:
    priceColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    compareAtColor: "{colors.muted-mid}"
    compareAtTypography: "{typography.price-compare}"
    saleHighlightColor: "{colors.primary}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "#bbbbbb"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.title-sm}"
    headlineColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"
  search-input:
    backgroundColor: "{colors.surface-neutral}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: 6px 16px

## Components

### Buttons
**`button-primary`** — The add-to-cart and checkout CTA uses the brand's paprika orange (#ef4f29) fill with all-caps Poppins at 14px/600 weight and 0.5px tracking on a 4px radius. Hover transitions to `primary-hover` (#e8431e) and active to `primary-active` (#d32f2f); the disabled state bleaches to the complementary peach (#f9bda4), maintaining palette coherence rather than reaching for a generic gray.

**`button-secondary`** — Transparent fill with a 1.5px ink border that inverts to a full ink fill on hover, producing a clean reversal. Used for secondary actions such as "View Collection" or "Save to Wishlist" where a filled button would compete with the primary CTA.

**`button-ghost`** — Text-only, no border, muted (#737373) color at `{typography.button-sm}` scale. Appears for dismissals, "Continue Shopping", and low-priority navigation flows where a full button would overcrowd the layout.

### Text Inputs
**`text-input`** — White background with a mid-gray (#d0d0d0) border that steps to near-black on focus, signaling engagement without a jarring blue-ring convention. The 4px radius and 48px height match the primary button for vertical consistency in side-by-side form rows.

### Navigation
**`nav-bar`** — 64px tall sticky bar on white with a 1px hairline (#e5e5e5) base border, gaining a subtle drop-shadow on scroll via `nav-bar-scrolled`. Logo anchors left or center on mobile; desktop nav links (Poppins 14px/500) fan left with cart and search icons anchored right. An announcement bar above the nav typically runs an ink (#1a1a1a) fill with white promotional text.

### Product Cards
**`product-card`** — Square 1:1 image crop on a near-white (#f8f8f8) tile with 8px radius. Product name renders in `{typography.body-sm}`, current price in `{typography.price-display}` ink-colored, compare-at struck through in muted-mid (#888888). The `sale-badge` anchors to the top-left corner of the image as an absolute overlay; `new-badge` stacks below it when both apply simultaneously.

### Hero Banner
**`hero-banner`** — Full-bleed photography over an ink-toned ground (#0d0c0c) with a 35% dark scrim, white Simvoni headline at `{typography.display-xl}`, Poppins subhead at `{typography.body-md}`, and the primary CTA. Desktop minimum height is 560px; mobile collapses to a taller 70vh crop to preserve the product focal point.

### Badges
**`sale-badge`** / **`new-badge`** / **`stock-badge`** — All three share the same 4px radius, 3px/8px padding, and all-caps 11px Poppins/700 label. Sale uses the primary paprika; New uses ink fill; In-Stock uses the sage-green tint system (`{colors.accent-green-surface}` background, `{colors.accent-green}` text) to signal availability positively without competing with CTAs.

### Collection Header
**`collection-header`** — A neutral-surface (#f4f4f4) editorial block at the top of collection pages: muted all-caps `{typography.collection-label}` above the Simvoni display-md heading with an optional short description paragraph below. Establishes brand voice before the product grid begins.

### Price Row
**`price-row`** — Inline pair of current price (ink, `{typography.price-display}`) and compare-at price (muted-mid, struck through). When a sale is active the current price may adopt `{colors.primary}` to draw attention, gated by a Shopify theme setting.

### Footer
**`footer`** — Near-black (#1a1a1a) fill with white headlines and #bbbbbb muted link text in Poppins body-sm, organized into 3–4 link columns. Social icons appear as 24px glyph buttons at #bbbbbb fill. Email signup input sits above the link columns with a primary CTA button alongside.

### Search
**`search-input`** — Pill-shaped (#f4f4f4 background, `{rounded.full}`) search bar in the mobile header drawer and desktop slide-out overlay. Muted placeholder at body-md scale; magnifier icon left-padded inside the field.

### Filter Chips
**`filter-chip`** / **`filter-chip-active`** — Pill-shaped attribute selectors for metal type, price range, and style category. Default state uses white with a gray border; the active state inverts to a full ink fill. The `{rounded.full}` shape echoes the search pill, creating a visually unified filter row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero becomes 70vh tall with centered text overlay; filter chips collapse to a horizontal scroll row |
| Tablet | 744–1128px | Two-column product grid; nav links may remain visible with condensed spacing; hero drops to 480px fixed height |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav bar; filter sidebar appears left of the product grid |
| Wide | > 1440px | Grid max-width clamps at 1440px with auto horizontal margins; hero typography scales to full display-xl width |

### Touch Targets
- All buttons minimum 44×44px; primary CTA is 48px tall
- Filter chips minimum 36px tall for thumb comfort in a horizontal scroll row
- Product card tap area covers the full card tile, not just the image
- Cart and search icon buttons in the nav bar maintain minimum 44×44px hit areas

### Collapsing Strategy
- Desktop nav links collapse to a hamburger menu at < 744px; cart count badge persists in the mobile header
- Collection filter sidebar moves to a bottom-sheet drawer on mobile
- Hero text overlay shifts from a left-aligned column to full-width centered on mobile
- Footer four-column link grid collapses to accordion-style dropdowns on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Simvoni is present in the font stack but no size or weight specimen was extractable from static extraction — display scale values are inferred from typical Shopify editorial patterns
- The green accent pair (#2d8a4e / #f0faf0) may be Shopify UI chrome (success toasts, in-cart confirmations) rather than an intentional brand palette choice
- Exact hero module configuration (video loop vs. static image, crossfade vs. cut) was not determinable from color and font extraction
- Announcement bar background color inferred as ink (#1a1a1a); actual bar color was not isolated in the extracted palette
- No custom icon set or glyph library observed; icon implementation (inline SVG, sprite, or icon font) is unknown
- Dark-mode or alternate theme variant status is unconfirmed
- Product card hover behavior (image swap, zoom, quick-add drawer overlay) could not be confirmed from static extraction
- Motion and transition timing tokens are unspecified; animation durations are not extractable from this method
