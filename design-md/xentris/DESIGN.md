---
version: alpha
name: "Xentris"
source_url: "https://www.xentriswireless.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Steel-gray dominates the viewport like the brushed aluminum of the accessories it sells — #eeeeee washes across product grids and specification panels, creating a neutral theater where device photography does the heavy lifting. Xentris Wireless builds its visual language on utility rather than lifestyle aspiration: the interface reads closer to a technical catalog than a boutique storefront, with dense product matrices organized by device compatibility rather than editorial narrative. Typography relies on the operating system's native sans-serif stack (no custom webfont was detected in static markup), which keeps page weight lean and load times fast — a pragmatic choice for a brand whose buyers often comparison-shop across dozens of SKU pages in a single session. Navigation follows a megamenu pattern common to accessories distributors, categorizing by device family, product type, and brand partnership. Buttons appear in a saturated tech-blue (`{colors.primary}`) against the light-gray canvas, ensuring CTAs punch through the neutral backdrop without competing with product imagery. Card containers use `{rounded.sm}` corners — restrained, never playful — and spacing stays tight (`{spacing.md}` gutters between grid items) to maximize density and scanability. The overall aesthetic signals wholesale professionalism: no hero lifestyle banners, no influencer carousels, just structured data delivery with enough visual hierarchy to guide a procurement buyer or end consumer through thousands of compatible accessories efficiently.

colors:
  primary: "#0058a3"
  primary-active: "#004785"
  primary-disabled: "#99c2df"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-strong: "#f5f5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#2e7d32"
  warning: "#f57c00"
  error: "#c62828"
  accent-charcoal: "#2c2c2c"
  footer-bg: "#1a1a1a"
  footer-text: "#cccccc"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.53
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
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
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 2px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.error}
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px 10px 40px
    height: 44px
    border: 1px solid {colors.hairline}
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.lg}
  nav-bar-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    borderBottom: 1px solid {colors.hairline}
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.hairline}
    hoverShadow: 0 2px 8px rgba(0,0,0,0.06)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1/1
    objectFit: contain
    padding: "{spacing.md}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    maxLines: 2
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  compatibility-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: 1px solid {colors.hairline}
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    textAlign: center
    hoverBackgroundColor: "{colors.hairline-soft}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    padding: 0 12px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"

---

## Components

### Buttons

**`button-primary`** — Solid tech-blue rectangle with barely-rounded corners (`{rounded.xs}`). On hover, darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with `not-allowed` cursor. Used for "Add to Cart", form submissions, and search confirmation. Height stays at 44px across breakpoints.

**`button-secondary`** — White fill with a 2px blue border and blue text. On hover, background shifts to `{colors.surface-soft}` and border deepens. Used for "View Details", secondary filter actions, and comparison toggles.

**`button-add-to-cart`** — Full-width variant of primary that fills the product detail sidebar. Taller (48px) and wider padding signals the primary conversion action on product pages.

### Navigation

**`nav-bar`** — 64px-tall sticky header with white background and a single-pixel bottom border. Logo sits left, search input center-weighted, account/cart icons right. Collapses to hamburger + icon row on mobile.

**`nav-bar-mega-menu`** — Dropdown panel triggered by category hover. Organized into columns by device family (Apple, Samsung, Google) with product-type sub-links. Subtle box-shadow separates it from content below.

**`breadcrumb`** — Muted caption-size trail showing Device > Category > Product. Active (current) segment renders in `{colors.ink}` while ancestors stay `{colors.muted}`.

### Product Display

**`product-card`** — Vertical card with contained product image on a light-gray background pad, two-line title, and bold price. Border is nearly invisible at rest (`{colors.hairline-soft}`) but firms up on hover alongside a faint shadow. Grid lays 4-across on desktop, 2-across on mobile.

**`product-card-image`** — Square aspect-ratio container with `object-fit: contain` and internal padding so accessories (cables, cases) never bleed to the card edge. Background is `{colors.surface-soft}` to separate white-bodied products from the white card surface.

**`product-card-price`** — Bold 18px numeral anchored bottom-left of the card body. No currency animation or strikethrough patterns detected.

**`compatibility-badge`** — Small inline pill listing compatible device models ("iPhone 15 Pro", "Galaxy S24"). Light-gray background with subtle border. Appears below product title on both card and detail views.

### Product Detail

**`spec-table-row`** — Alternating-implied rows (separated by `{colors.hairline-soft}` bottom borders) with a left-aligned uppercase label and right-aligned value. Used for weight, dimensions, material, certifications.

**`spec-table-label`** — Uppercase 13px header in muted gray. Provides scanning structure for spec-dense accessory listings.

### Category & Search

**`category-tile`** — Square tile with centered icon and label used on landing pages to route users by product type (Cases, Chargers, Screen Protectors, Mounts). Light gray fill darkens subtly on hover.

**`search-input`** — Slightly rounded input with magnifying-glass icon inset left. Gray fill at rest, white on focus with blue border. Positioned prominently in the nav bar.

### Footer

**`footer`** — Dark charcoal block (`{colors.footer-bg}`) with multi-column link layout. Column headings in white at `{typography.title-sm}`, link text in muted light gray. Contains contact information, warranty links, and partner logos.

### Pagination

**`pagination`** — Row of numbered page buttons below product grids. Active page gets solid `{colors.primary}` fill with white text; inactive pages are plain with body-color text. Compact 36px height to stay subordinate to product content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-across for cards), hamburger nav replaces megamenu, search moves behind icon tap, footer stacks to single column, add-to-cart button becomes sticky bottom bar |
| Tablet | 744–1128px | 3-column product grid, megamenu partially visible (top categories only), sidebar filters collapse to drawer, spec table remains full-width |
| Desktop | 1128–1440px | 4-column product grid, full megamenu on hover, sidebar filter panel visible, product detail uses 60/40 image-info split |
| Wide | > 1440px | Content max-width caps at 1440px and centers, grid gutters expand to `{spacing.lg}`, hero banner scales proportionally |

### Touch Targets

- All interactive elements maintain minimum 44×44px hit area on mobile
- Card tap zones cover the entire card surface, not just the title link
- Filter checkboxes use 44px row height with full-row tap activation
- Pagination buttons spaced with `{spacing.sm}` gaps to prevent mis-taps

### Collapsing Strategy

- Navigation: megamenu → hamburger drawer with accordion sections per device family
- Filters: left sidebar panel → slide-in drawer triggered by "Filter" button above grid
- Product images: horizontal thumbnail strip → swipeable carousel with dot indicators
- Spec tables: remain full-width but may truncate to "Show all specs" toggle on mobile
- Footer columns: 4-column → single stacked accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary brand color unconfirmed**: Only #eeeeee was extracted from static markup. The blue (`#0058a3`) used as primary is inferred from category norms for wireless/tech brands — actual brand blue may differ significantly. Verify against rendered site or brand guidelines.
- **No custom fonts detected**: Only Font Awesome icon fonts appeared in static CSS. The site likely loads body/display fonts via JavaScript, a CDN with deferred loading, or inlined critical CSS not captured in extraction. System font stack is used as placeholder.
- **No hero/banner component data**: Unable to determine if the site uses lifestyle hero banners, rotating carousels, or static product showcases on the homepage.
- **Interaction patterns unobserved**: Hover states, transitions, animation durations, and micro-interactions could not be extracted from static analysis.
- **Dark mode**: No evidence of dark-mode support or alternate color scheme detected.
- **Exact border-radius values unconfirmed**: The `{rounded.xs}` (4px) used throughout is inferred from the utilitarian visual style — actual values may be 2px or 6px.
- **Cart/checkout flow styling**: No data on cart drawer, checkout page typography, or form field styling beyond generic patterns.
- **Partner/certification badge styling**: Xentris likely displays MFi, Samsung-certified, or similar partner logos — placement and sizing unknown.
