---
version: alpha
name: "VWR (Avantor)"
source_url: "https://www.vwr.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Six hundred thousand catalog numbers deep, VWR lands with a search bar before it shows you a hero — the procurement-first hierarchy of a platform where lab managers navigate by SKU, CAS number, and pack size rather than by scrolling lifestyle photography. The interface is engineered for institutional buyers: order history, punchout integration, quantity breaks, and a request-a-quote flow sit at the same visual level as add-to-cart, because a $40,000 spectrophotometer and a box of nitrile gloves travel through the same checkout logic. The primary type color is the only confirmed extraction at `#313131`, a near-black charcoal that runs on a white canvas across system-ui stacks — Arial, Helvetica Neue, and their OS-native fallbacks — a deliberate refusal of brand fonts signaling compatibility with slow institutional machines and enterprise procurement terminals where custom font loading is a liability. The nav runs three layers deep: a utility bar carrying account and location context, a logo bar anchoring the primary search field, and a dark-blue category rail below that triggers mega-menus two or three levels wide. Corner radii stay tight across most surfaces — form inputs, data tables, and filter chips are nearly square at `{rounded.xs}`, communicating the precision register expected in a domain where tolerances are measured to the microgram. Only buttons and status badges carry any softness, creating a clear visual grammar between data surfaces and action affordances. The brand's primary blue (approximate — see Known Gaps) carries navigation, interactive links, and quote-related CTAs; an accent orange surfaces for add-to-cart actions and promotional sale pricing, a deliberate separation of transactional completion from navigational blue that prevents the two from competing in dense product-grid views. Product cards carry catalog number, pack size, unit price, and stock status without requiring hover or expansion — the behavior of a printed catalog translated to a screen-native grid, not a lifestyle marketplace adapted for procurement.

colors:
  primary: "#0057B8"
  primary-active: "#00408A"
  primary-disabled: "#9EC3E8"
  accent-orange: "#E8600D"
  accent-orange-active: "#C45209"
  ink: "#313131"
  body: "#444444"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F5F7FA"
  surface-card: "#FFFFFF"
  surface-nav: "#003E80"
  table-row-alt: "#F5F7FA"
  on-primary: "#FFFFFF"
  on-accent: "#FFFFFF"
  success: "#2E7D32"
  error: "#C62828"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  data-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.3px
    textTransform: uppercase
  catalog-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  nav-link-sub:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: "10px 20px"
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
    padding: "9px 19px"
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-add-to-cart:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "10px 20px"
    height: 40px
  button-add-to-cart-hover:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 48px 10px 16px"
    height: 44px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
    utilityBar:
      backgroundColor: "{colors.ink}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      height: 36px
    logoBar:
      backgroundColor: "{colors.canvas}"
      height: 64px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.nav-link-sub}"
    shadow: "0 4px 12px rgba(0,0,0,0.15)"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    skuTypography: "{typography.catalog-number}"
    priceTypography: "{typography.price-display}"
    hoverBorderColor: "{colors.primary}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    unitTypography: "{typography.caption}"
    unitColor: "{colors.muted}"
    saleColor: "{colors.accent-orange}"
    strikethroughColor: "{colors.muted-soft}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.data-label}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    rowAltBackgroundColor: "{colors.table-row-alt}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-sm}"
    optionTypography: "{typography.body-sm}"
    checkboxAccentColor: "{colors.primary}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-in-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-out-of-stock:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  breadcrumb:
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.muted-soft}"
  pagination:
    activeBg: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  cart-summary:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    headingTypography: "{typography.title-md}"
    totalTypography: "{typography.price-display}"

## Components

### Buttons

**`button-primary`** — A compact 40px blue rectangle (`{colors.primary}`, `{rounded.xs}`) used for secondary catalog actions such as "Add to Quote," "View Details," and account-area confirmations. Hover state darkens to `{colors.primary-active}`; disabled state washes out to `{colors.primary-disabled}` with no cursor interaction. Typography is Arial bold at 14px (`{typography.button-md}`) with no letter-spacing, matching the utilitarian register of procurement interfaces where label clarity outranks visual expressiveness.

**`button-add-to-cart`** — The highest-priority CTA on every product and cart surface, rendered in accent orange (`{colors.accent-orange}`) to visually separate the transactional completion action from the navigation and link blue that saturates the rest of the interface. Same 40px height and `{rounded.xs}` corner radius as `button-primary` so paired button rows align flush. Hover darkens to `{colors.accent-orange-active}`; the color carries no "warning" connotation here — orange is commerce completion, not caution.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching text, used for "Request Quote," "Download SDS," and filter-reset actions. Maintains identical outer dimensions to `button-primary` to avoid height mismatches when buttons sit in adjacent columns on product listing rows.

**`button-ghost`** — Transparent background with `{colors.primary}` text only, no border. Appears on "Show More" toggles, comparison selectors, and pagination-adjacent actions where a bordered button would create visual noise in an already data-dense layout.

### Search Bar

**`search-bar`** — A 44px-tall input with a 2px `{colors.primary}` border and an integrated blue submit button flush to the right edge, positioned at the center of the logo bar on every page. Placeholder text prompts entry by catalog number, keyword, or CAS number — the three search entry modes science procurement staff use most. On desktop the bar spans 600–800px; on tablet and mobile it stretches to full available width.

### Navigation

**`nav-bar`** — Three horizontal layers stacked vertically: a 36px `{colors.ink}` utility bar carrying account status, order history, and site-region selector; a 64px white logo bar housing the search field and cart icon; and a 48px `{colors.surface-nav}` category rail below holding all primary department links in white `{typography.nav-link}`. The layering allows utility context and transactional navigation to occupy distinct visual registers without competing.

**`mega-menu`** — Opens on hover of any category item in the nav rail, dropping a full-width panel with a 3px `{colors.primary}` top border over content. Interior columns use `{typography.title-sm}` section headings and `{typography.nav-link-sub}` link rows organized by discipline (e.g., Cell Biology, Chromatography, Filtration). The rightmost column typically carries featured product tiles or category photography. Shadow `0 4px 12px rgba(0,0,0,0.15)` separates the panel from underlying content without a hard border.

### Product Card

**`product-card`** — A bordered rectangle (`{rounded.xs}`, `1px {colors.hairline}`) carrying a square product image, catalog number in `{typography.catalog-number}` monospace, product title in `{typography.title-sm}`, pack-size selector dropdown, price in `{typography.price-display}`, and a row of action buttons. Hover upgrades the border to `{colors.primary}` to signal interactivity without animation. In list view the card expands to a horizontal row with specifications inline; in grid view it compresses to a tile with deferred spec detail.

### Price Block

**`price-block`** — Tiered pricing is the norm for lab procurement and the price block supports it: the unit price renders large in `{typography.price-display}`, with per-unit denomination and pack breakdown in `{typography.caption}` below. Sale prices display in `{colors.accent-orange}` with a strikethrough list price in `{colors.muted-soft}`. Tax-exclusion and currency notices use `{typography.caption}` in `{colors.muted}` beneath the price figure.

### Spec Table

**`spec-table`** — The specification table anchors every product detail page and is built for scanning, not reading. Column headers use `{typography.data-label}` (uppercase, letter-spaced) over `{colors.surface-soft}`; value rows alternate between white and `{colors.table-row-alt}` in `{typography.body-sm}`. No corner radius (`{rounded.none}`) — the table reads as structured instrument data, not a UI card. Typical columns include Catalog No., Description, Size/Quantity, Pack Type, Unit Price, and Availability status.

### Filter Sidebar

**`filter-sidebar`** — A 240px left rail of faceted filters with collapse/expand chevrons per section. Section headings in `{typography.title-sm}`; option rows in `{typography.body-sm}` with `{colors.primary}` checkbox accent. Result counts render in `{typography.caption}` `{colors.muted}` inline with each option label. Applied filters mirror as dismissible tag chips above the product grid so users can remove individual constraints without resetting the full filter state.

### Badges

**`badge-sale`** — Orange (`{colors.accent-orange}`) label in `{typography.badge}` uppercase, positioned at the top-left corner of product card images for discounted items. **`badge-new`** — Blue (`{colors.primary}`) version indicating recent catalog additions. **`badge-in-stock`** / **`badge-out-of-stock`** — Green and red availability status chips that appear near the add-to-cart row; the presence or absence of the in-stock badge communicates more neutrally than a hard "OUT OF STOCK" block in a supply chain environment where availability fluctuates by region and account type.

### Cart Summary

**`cart-summary`** — Sticky right-column panel on cart and checkout pages. Light gray surface (`{colors.surface-soft}`) with `{colors.hairline}` border and `{rounded.sm}` corners carries line-item count, subtotal in `{typography.price-display}`, estimated shipping tier, and a full-width checkout button styled as `button-add-to-cart`. A secondary "Convert to Purchase Order" row handles the quote-to-order workflow common for institutional procurement accounts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Three-layer nav collapses to hamburger + search icon row; mega-menu becomes full-screen accordion drawer; product grid shifts to 1-column list; filter sidebar hidden behind sticky "Filter & Sort" bar that opens a bottom sheet; search bar spans full width; spec tables scroll horizontally with sticky first column |
| Tablet | 744–1128px | Utility bar hidden; logo and search combine into single 56px row; product grid 2 columns; filter sidebar collapses to horizontal chip strip above grid; mega-menu becomes 2-column dropdown |
| Desktop | 1128–1440px | Full three-layer nav visible; product grid 3–4 columns; filter sidebar 240px fixed left rail; search bar 640px centered in logo bar; mega-menu full-width panel |
| Wide | > 1440px | Max content width 1400px centered with margin; product grid 4–5 columns; mega-menu columns expand with additional featured-product tiles visible |

### Touch Targets

- All buttons minimum 40px height; add-to-cart button minimum 44px on mobile
- Filter checkboxes have 40px tap-target area regardless of 16px visual checkbox size
- Nav drawer links minimum 48px row height
- Quantity stepper ± buttons each 40px wide and 36px tall
- Pack-size dropdown minimum 44px height on touch viewports

### Collapsing Strategy

- Three-layer desktop nav compresses to a single hamburger-plus-search row at mobile breakpoint; layers are restored progressively at tablet and desktop
- Mega-menu navigation converts to accordion sections inside a full-screen left drawer on mobile and tablet
- Filter sidebar reflows to a bottom sheet triggered by a sticky "Filter & Sort" button pinned above the product grid
- Specification tables become horizontally scrollable with the row-label column sticky on the left
- Price block condenses pack-size selector and price into a vertical stack on mobile, removing the default side-by-side layout used on desktop product pages

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full color palette**: Only `#313131` was extracted — the site returned a Cloudflare challenge page ("Just a moment...") blocking the crawl. Primary blue (`#0057B8`), accent orange (`#E8600D`), and nav navy (`#003E80`) are approximate values derived from Avantor/VWR brand knowledge, not confirmed site extraction.
- **Custom typeface**: No proprietary brand font was detected; all stacks resolved to system-ui/Arial/Helvetica fallbacks. VWR may load a licensed typeface via deferred JavaScript — unverifiable under anti-bot interception.
- **Exact corner radii**: Button and input radii are set to near-zero (`{rounded.xs}` = 2px) based on B2B catalog conventions; actual rendered values on live components are unconfirmed.
- **Promotional and sale module colors**: Specific hex values for sale-banner backgrounds, homepage hero overlays, and loyalty/contract-pricing badge variants could not be extracted without an authenticated session.
- **Dark mode or high-contrast theme**: Institutional buyers may require accessibility-compliant contrast modes; no alternate-theme tokens were extractable.
- **Print stylesheet**: Lab supply procurement commonly involves printed order confirmations and Safety Data Sheets; print-specific typography, color substitutions, and layout rules are not captured.
- **Meta theme-color**: Not set, confirming no PWA or mobile app shell configuration.
- **Authenticated pricing UI**: Contract pricing, volume-break tables, and punchout-specific UI variants require a logged-in institutional account to observe.
