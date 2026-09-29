---
version: alpha
name: "Downtown Music Gallery"
source_url: "https://www.downtownmusicgallery.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Forty years of avant-garde inventory compressed into a catalog interface: Downtown Music Gallery builds its digital presence the way a serious record collector expects to browse — dense product rows, spare typographic hierarchy, and almost no decorative surface competing with artist names and imprint details. The store, a fixture of New York's experimental, jazz, and niche-genre music scene, carries collector-culture DNA into its web presence: product listings read like liner-note entries rather than retail hero cards, and navigation prioritizes genre depth over visual merchandising splash. Because no live hex values or font stacks were extractable from the site (see Known Gaps), the palette here is inferred from the brand archetype rather than confirmed tokens — a near-black ink register (#1a1a1a) against a white canvas (#ffffff), with a single warm-crimson accent (#c0151e) that echoes the matte-printed covers of underground LP releases. Square corners govern product thumbnails ({rounded.none}), reflecting the album-cover grid aesthetic that serious collectors recognize instantly; only interactive controls receive {rounded.xs} — just enough to signal clickability without softening the utilitarian register. Spacing is tighter than lifestyle retail: {spacing.base} gutters keep rows dense, and section dividers use {spacing.xl} rather than the generous editorial breathing room of fashion or home-goods stores. The footer doubles as a secondary genre and format index, listing categories, imprints, and media types — a structural choice that signals to the specialist buyer exactly what kind of inventory awaits. Typography leans on a neutral sans-serif system stack at modest weights; no bespoke display face announces the wordmark, which is itself a statement about where the brand's authority lives: in the depth and credibility of its catalog, not its visual identity.

colors:
  primary: "#c0151e"
  primary-active: "#96101a"
  primary-disabled: "#e8a0a4"
  ink: "#1a1a1a"
  body: "#2e2e2e"
  muted: "#6a6a6a"
  muted-soft: "#9a9a9a"
  hairline: "#d8d8d8"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#111111"
  on-primary: "#ffffff"
  on-dark: "#f0f0f0"
  price-sale: "#c0151e"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  catalog-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.9px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-category:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 10px 18px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 9px 17px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px 10px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 54px
    padding: 0 24px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-category}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline}"
    padding: 10px 0
    imageSize: 80px
    imageRounded: "{rounded.none}"
    gap: 12px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price}"
    textColor: "{colors.price-sale}"
  product-card-format-badge:
    typography: "{typography.catalog-label}"
    textColor: "{colors.muted}"
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  product-grid:
    columns: 4
    columnsMobile: 2
    columnsTablet: 3
    gutter: 16px
    rowGap: 16px
  product-list-row:
    borderBottom: "1px solid {colors.hairline}"
    padding: 10px 0
    minHeight: 68px
    display: flex
    gap: 12px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  genre-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.catalog-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  new-arrival-flag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.catalog-label}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  format-filter-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.catalog-label}"
    rounded: "{rounded.none}"
    borderBottom: "2px solid transparent"
    padding: 8px 0
  format-filter-tab-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.catalog-label}"
    borderBottom: "2px solid {colors.ink}"
    padding: 8px 0
  section-header:
    typography: "{typography.catalog-label}"
    textColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: 8px
    marginBottom: 16px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: 48px 24px
    minHeight: 240px
  imprint-tag:
    typography: "{typography.catalog-label}"
    textColor: "{colors.primary}"
    backgroundColor: transparent
    rounded: "{rounded.none}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 6px 10px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderTop: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-category}"
    padding: 32px 24px
    columnGap: 32px

## Components

### Buttons

**`button-primary`** — Flat square-cornered button ({rounded.none}) in warm crimson ({colors.primary}), 40px tall with 10px/18px padding. Used exclusively for high-commitment actions: Add to Cart, Checkout, and Subscribe. Active state deepens to {colors.primary-active}; disabled state washes out to {colors.primary-disabled} with no cursor change. No shadow, no gradient — the flatness is deliberate and consistent with the store's utilitarian register.

**`button-secondary`** — White canvas with a 1px ink border; same square corner and height as primary. Used for secondary actions like Save, Wishlist, and View Details. Active state fills with {colors.surface-soft} to confirm press without competing with primary CTAs.

**`button-text`** — Transparent background with {colors.primary} underlined text; functions as an inline link-style action for things like "See full tracklist" or "Read more." No padding or border.

### Form Inputs

**`text-input`** — Zero-radius input field with a 1px {colors.hairline} border that sharpens to {colors.ink} on focus. System sans-serif at 15px. No floating label animation; label sits above the field in {typography.catalog-label} uppercase.

**`search-bar`** — Housed in {colors.surface-soft}, same sharp corners as text-input. Used in the site header and at the top of catalog pages. Placeholder reads in {colors.muted}; icon is a simple 16px magnifying glass in {colors.muted}, shifting to {colors.ink} on focus.

### Navigation

**`nav-bar`** — 54px-tall white bar with a single 1px {colors.hairline} bottom border. Left: wordmark in {typography.title-md} weight 700. Center or right: genre megamenu links in {typography.nav-link}. No sticky behavior on mobile; collapses to hamburger below 744px. Dropdowns open flush below with {rounded.none}, 1px border all sides.

**`format-filter-tab` / `format-filter-tab-active`** — Horizontal row of format filters (Vinyl, CD, Cassette, Digital, Books) displayed in {typography.catalog-label} uppercase. Inactive tabs show {colors.muted} text with no underline; active tab shifts to {colors.ink} with a 2px solid {colors.ink} bottom border — a classic catalog tab pattern.

### Product Display

**`product-card`** — Two layout modes: grid (4-up on desktop, 2-up on mobile) with square album-art thumbnail at top, and list row (dense horizontal strip, 80px square image, text columns). Both modes use {rounded.none} image corners. The grid card shows title in {typography.title-sm}, artist in {typography.body-sm} {colors.muted}, imprint in {typography.caption} {colors.muted-soft}, price in {typography.price}, and format badge bottom-right.

**`product-card-format-badge`** — A small pill in {colors.surface-soft} uppercase 11px tracking — "LP", "CD", "CASS", "BOOK". Renders inline with price on list rows, or anchored bottom-right on grid cards.

**`new-arrival-flag`** — Flat crimson tag ({colors.primary}) in {typography.catalog-label} reading "NEW". Overlays top-left corner of grid card artwork — no radius, no shadow.

**`imprint-tag`** — Inline text in {colors.primary} {typography.catalog-label}; clicking filters the catalog to that imprint. No background or border — just a colored label that acts as a faceted link.

### Catalog Structure

**`section-header`** — Full-width {typography.catalog-label} label in {colors.muted} uppercase with a 1px {colors.hairline} bottom rule. Used to divide page sections ("New Arrivals", "Staff Picks", "By Genre") without adding visual weight.

**`genre-badge`** — Small inline tag in {colors.surface-soft} with {typography.catalog-label} text. Used in product detail pages and search results to show genre classifications. Multiple badges stack horizontally and wrap.

**`hero-banner`** — Dark (#111111) full-width band used for featured artist spotlights or seasonal sale announcements. Title in {typography.display-xl} white, body copy in {typography.body-md} {colors.on-dark} at reduced opacity. Minimum 240px tall; no parallax or animation.

### Pagination & Footer

**`pagination`** — Square page-number buttons in {typography.body-sm}, 1px {colors.hairline} border; active page fills {colors.ink} with {colors.on-dark} text. Previous/Next arrows alongside numbers. Aligned center below catalog grid.

**`footer`** — Light {colors.surface-soft} background, 1px top border, three or four link columns covering Genres, Formats, Imprints, and About/Policy links. Column headers in {typography.catalog-label} {colors.muted}; links in {typography.nav-category} {colors.body}. The footer functions as a secondary site map that specialist shoppers use as a navigation shortcut.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product list (no grid); nav collapses to hamburger + search icon; hero banner reduces to 160px min-height; format filters scroll horizontally |
| Tablet | 744–1128px | 2-column grid; nav shows top-level links only, dropdowns on tap; section headers remain full-width |
| Desktop | 1128–1440px | 4-column product grid; full megamenu dropdowns on hover; hero banner at full height; sidebar genre filter visible alongside catalog |
| Wide | > 1440px | Max content width 1320px, centered with auto margins; grid stays 4-up; no additional columns added |

### Touch Targets

- All buttons and interactive controls minimum 40px tall (button-primary, button-secondary, text-input, search-bar)
- Format filter tabs padded to 40px touch target height on mobile via increased padding
- Product list rows minimum 68px height for thumb-friendly tap
- Pagination buttons minimum 36px square

### Collapsing Strategy

- Mega-menu collapses to full-screen drawer on mobile, triggered by hamburger icon
- Product grid switches from 4-column to 2-column at 744px, single-column below 480px
- Format filter tabs overflow-x: scroll with hidden scrollbar on mobile rather than wrapping
- Footer link columns stack vertically on mobile, accordion-collapsed by default
- Search bar moves from header inline to full-width top-of-page position on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors extracted from live site — palette (crimson #c0151e, near-black #1a1a1a, white #ffffff) is inferred from independent record store brand archetype, not confirmed site tokens; actual brand colors may differ significantly
- No font-family stacks extracted — system sans-serif stack assumed; site may load a custom or licensed typeface via JS or a font service
- No meta theme-color or Shopify theme data available to confirm platform-specific component behavior
- Exact nav-bar height, megamenu structure, and dropdown geometry not confirmed
- Badge color, sale price styling, and wishlist/save UI not extractable without live rendering
- Mobile drawer and hamburger menu exact behavior unconfirmed
- Footer column count and link taxonomy inferred from genre-store conventions, not confirmed from site HTML
