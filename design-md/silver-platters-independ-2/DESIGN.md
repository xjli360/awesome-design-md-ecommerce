---
version: alpha
name: "Silver Platters"
source_url: "https://www.silverplatters.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that wears its concrete floor and fluorescent lights as a badge of honor, Silver Platters builds its digital presence on a nearly bare canvas of #eeeeee — a warm, worn gray that reads less like a design choice and more like the patina of a thousand thumbed-through LP jackets. The brand makes no attempt to prettify itself: product cards sit on that same light gray surface with {rounded.sm} corners, type runs in system-adjacent stacks (Font Awesome 5 for icons, a custom spruce-icon-pack for vinyl-specific glyphs), and the entire experience feels like the store’s physical bins translated directly into a grid. There is no hero splash, no lifestyle photography — just rows of album covers, price tags, and condition notes. The primary color, whatever it is, remains invisible in the extracted palette; the site’s true visual language is one of absence — white space, gray space, and the saturated color of the album art itself. Buttons use {rounded.sm} rather than pills, navigation is a flat text strip, and the search bar is a simple input with no ornament. This is a store that trusts its inventory to do the talking.

colors:
  primary: "#eeeeee"
  primary-active: "#cccccc"
  primary-disabled: "#f5f5f5"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#111111"
  accent-sale: "#cc0000"
  accent-new: "#006600"
  badge-used: "#ff8800"
  badge-collectible: "#9900cc"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-accent-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-condition:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  badge-condition:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-used:
    backgroundColor: "{colors.badge-used}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-collectible:
    backgroundColor: "{colors.badge-collectible}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-icon:
    textColor: "{colors.muted}"
    fontSize: 14px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline}"
  category-tab:
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.xs} {spacing.md}"
    rounded: "{rounded.sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    padding: "{spacing.xs} {spacing.md}"
    rounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.section}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    marginTop: "{spacing.md}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The workhorse action button, rendered in the site's signature light gray `{colors.primary}` with dark text `{colors.on-primary}`. Uses `{typography.button-md}` at 14px weight 600 with 0.5px letter spacing for a slightly authoritative read. Corners are softly squared at `{rounded.sm}` (4px). On hover, the background shifts to `{colors.primary-active}` (#cccccc); disabled state drops to `{colors.primary-disabled}` (#f5f5f5) with muted text. Height is a compact 40px — no oversized CTAs here.

**`button-secondary`** — A white button with a 1px `{colors.hairline}` border, same dimensions and typography as primary. Used for "Add to Cart" alongside primary "Buy Now" actions, or for filter resets and secondary form submissions. Hover state adds a 2px `{colors.ink}` border.

**`button-accent-sale`** — A small, high-contrast button in `{colors.accent-sale}` (#cc0000) with white text, used exclusively for sale-price callouts and clearance banners. Uses `{typography.button-sm}` at 12px and a compact 28px height.

### Cards
**`product-card`** — The core inventory unit: a white card on the `{colors.surface-soft}` canvas with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. Contains a square album-art image (`{rounded.xs}`), the title in `{typography.title-sm}`, the price in bold `{typography.price}`, and a condition label in `{typography.caption-sm}`. On hover, the border darkens to `{colors.hairline}` and a subtle box-shadow lifts the card. No fancy overlays or quick-add buttons — just the record, its price, and its grade.

**`badge-condition`** — A small, unobtrusive label on `{colors.surface-soft}` background with `{colors.muted}` text, used for condition descriptors like "VG+" or "Mint". Uses `{typography.badge}` at 11px uppercase with `{rounded.xs}` corners. Variants include `badge-used` (orange #ff8800) for used copies and `badge-collectible` (purple #9900cc) for rare pressings.

### Navigation
**`nav-bar`** — A flat 48px white bar with a 1px `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` at 14px weight 600 with 0.5px letter spacing. Active links get a 2px `{colors.ink}` bottom border. No dropdowns, no mega-menus — just a horizontal strip of categories (Vinyl, CDs, Turntables, etc.) and a search icon.

**`category-strip`** — A secondary navigation row below the main nav, listing subcategories (Rock, Jazz, Classical, etc.) as inline tabs. Inactive tabs are `{colors.muted}` text on white; active tabs fill with `{colors.primary}` (#eeeeee) and dark text. Uses `{typography.button-sm}` with `{rounded.sm}` padding.

### Forms
**`text-input`** — A simple white input field with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border thickens to 2px `{colors.ink}`. Used for search queries, email signup, and contact forms. Height is 40px with 8px/12px padding.

**`search-bar`** — Nearly identical to `text-input` but with a magnifying-glass icon (Font Awesome 5) in `{colors.muted}` positioned at the left. No pill shape, no rounded-full treatment — just a straightforward input that says "Search vinyl, CDs, turntables..." in `{typography.body-md}`.

### Footer
**`footer`** — A light gray section on `{colors.surface-soft}` with a 1px `{colors.hairline}` top border. Links are `{colors.muted}` in `{typography.link}` at 14px, darkening to `{colors.ink}` on hover. Organized in columns (Shop, Info, Help, Follow Us) with generous `{spacing.xxl}` padding. Social icons use Font Awesome 5 Brands.

### Hero
**`hero-banner`** — An optional full-width banner on `{colors.primary}` (#eeeeee) with dark text, used sparingly for sales events or new-arrival announcements. The headline uses `{typography.display-lg}` at 24px weight 600; a subtitle sits below in `{typography.body-md}`. No background image, no gradient — just text on gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 cards), nav collapses to hamburger, category strip scrolls horizontally, hero banner reduces to 16px type |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but compact, category strip shows 6-8 tabs with overflow scroll |
| Desktop | 1128–1440px | Three-column product grid, full nav with all categories, category strip shows 10+ tabs, hero banner at full width |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, category strip expands to fill space |

### Touch Targets
- All buttons and links maintain minimum 44px touch target height
- Product cards have full-card tap targets (no separate "view" button)
- Category tabs are 40px+ tall for easy tapping
- Search bar input is 44px tall on mobile
- Nav hamburger icon is 44x44px

### Collapsing Strategy
- Main navigation collapses to a hamburger menu below 744px
- Category strip becomes a horizontal scrollable row on mobile (no wrapping)
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack vertically on mobile (single column)
- Hero banner text reduces in size but does not collapse entirely
- Search bar remains visible at all breakpoints (moves to nav bar on mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Primary brand color could not be confidently extracted. The extracted palette returned only #eeeeee (a light gray) and no distinctive accent color. This gray may be the intentional brand color (a "concrete floor" aesthetic), or the true brand color may be embedded in images or JavaScript that could not be parsed. If a brand color exists (e.g., a signature blue, red, or yellow), it should be added as `primary` and the current `primary` moved to a `surface-soft` or `hairline` token.
- Font family declarations were limited to Font Awesome 5 and a custom "spruce-icon-pack" — no body or heading fonts were extracted. The typography block uses Helvetica Neue as a reasonable system-adjacent fallback; the actual brand font may differ.
- Hover and focus states for all components are inferred from common patterns, not extracted from the live site.
- Error states (form validation, empty search results, 404 pages) are not documented.
- Dark mode is not supported and no dark-mode tokens exist.
- No extracted data for button border-radius, spacing, or component dimensions — these are estimated based on the site's utilitarian aesthetic and common record-store patterns.
- The extracted color list may include checkout-widget colors (Shopify Pay, Klarna, Afterpay) or social-icon colors that were not fully filtered. The true brand palette may include additional accent colors not captured.
