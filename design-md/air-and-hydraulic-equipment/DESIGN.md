---
version: alpha
name: "Air & Hydraulic Equipment"
source_url: "https://www.aheinfo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two colors carry the entire load-bearing authority of Air & Hydraulic Equipment's catalog: a compressed-denim navy (#003366) and a warning-signal crimson (#a90f14), a pairing borrowed directly from industrial safety signage that signals a supplier built around functional precision rather than visual appeal. The site operates less like a retail storefront and more like an engineered parts library — navigation runs several layers deep, categories nest by fitting type and pressure rating, and part numbers are the primary identifiers on every product card. Open Sans and Open Sans Condensed handle all typographic work, a deliberate pairing that trades expressiveness for extreme legibility across dense specification tables and faceted filter panels. The condensed cut appears at small sizes for metadata labels and stock-status badges, letting the grid pack more information per row without crowding. Every primary action — Add to Cart, Get a Quote, Request Pricing — arrives in the same navy-on-white or white-on-navy contrast, so engineers scanning for a purchase path can locate it instantly against walls of technical copy. The crimson (#a90f14, #cc2b2b) is reserved for urgency: sale tags, out-of-stock warnings, and promotional callout ribbons, which means the eye immediately distinguishes commercial signal from informational content. Corners are kept at {rounded.xs} — square to near-square — reflecting the industrial context where softened radii suggest consumer comfort, and nothing here is selling comfort. The dark canvas states (#2f2f2f, #313131) appear in footers and section dividers, creating a band structure common to MRO catalog sites that helps professional repeat visitors orient themselves in long, category-dense pages. Gray hairlines (#eeeeee) and a subtle surface step (#f5f7f9) carry the grid structure inside product listings. The overall system is high-density, high-contrast, and optimized for professional buyers who arrive with a part number already in mind.

colors:
  primary: "#003366"
  primary-active: "#002244"
  primary-disabled: "#99aabb"
  accent: "#a90f14"
  accent-active: "#7a0a0f"
  accent-soft: "#cc2b2b"
  link-blue: "#0066b4"
  ink: "#111111"
  body: "#2f2f2f"
  muted: "#444444"
  muted-soft: "#888888"
  hairline: "#eeeeee"
  hairline-mid: "#dddddd"
  canvas: "#ffffff"
  surface-soft: "#f5f7f9"
  surface-card: "#ffffff"
  surface-dark: "#313131"
  footer-bg: "#2f2f2f"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"
  badge-sale: "#a90f14"
  badge-new: "#0066b4"
  in-stock: "#2d7a3a"
  out-of-stock: "#cc2b2b"

typography:
  display-xl:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans Condensed', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-condensed:
    fontFamily: "'Open Sans Condensed', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  part-number:
    fontFamily: "'Roboto Mono', 'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-primary:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
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
    height: 40px
    border: "2px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    border: "1px solid {colors.hairline-mid}"
    height: 40px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
    height: 44px
    padding: 0 12px
  search-button:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 44px
    padding: 0 20px
  nav-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
    padding: 0 24px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-primary}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    padding: 0 24px
  nav-mega-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 1px 4px rgba(0,0,0,0.07)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-sku:
    typography: "{typography.part-number}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-stock-available:
    backgroundColor: "{colors.in-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-stock-unavailable:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 320px
    padding: "{spacing.xxl} {spacing.xl}"
  hero-banner-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-banner-sub:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline-mid}"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  filter-group-title:
    typography: "{typography.label-condensed}"
    textColor: "{colors.muted}"
    paddingBottom: "{spacing.xs}"
    borderBottom: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    stripeColor: "{colors.surface-soft}"
  spec-table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
  promo-ribbon:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-condensed}"
    padding: "{spacing.xs} {spacing.base}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    fontWeight: 700
    marginBottom: "{spacing.sm}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "#bbbbbb"

## Components

### Buttons

**`button-primary`** — Navy (#003366) fill with white uppercase Open Sans at 14px/700, 40px tall with near-square {rounded.xs} corners. This is the default add-to-cart and page-action button across the catalog. Active state drops to #002244; disabled state fades to the slate-blue wash (#99aabb) so inactive controls don't compete with live ones in dense filter panels.

**`button-secondary`** — White fill with a 2px navy border and navy text. Used for secondary purchase-path actions such as "Add to Wishlist," "Compare," and "Save Quote." Identical corner treatment and uppercase type as primary so the pair reads as a coherent family.

**`button-accent`** — Crimson (#a90f14) fill with white text. Reserved for high-commercial-urgency actions: "Get a Quote," "Request Pricing," "Call for Availability." The color distance from the primary navy creates an unmistakable visual priority tier — when both buttons appear on a page, the crimson one reads as the higher-stakes action.

**`button-ghost`** — Transparent with navy text and no border. Used for tertiary navigation like "View All," "See More Specs," and inline text-link actions within specification copy.

### Search

**`search-bar`** — Full-width input with a 2px navy border, no radius ({rounded.none}), and a flush crimson search button welded to the right edge. The zero-gap, zero-radius junction between input and button treats the whole unit as a single control — the dominant above-fold element because engineers arrive with a part number in mind. Placeholder text renders in {colors.muted-soft}.

### Navigation

**`nav-top-strip`** — A 32px navy band above the main nav carries account login, order status, dealer access, and a phone number in 11px condensed caps on white. This strip is the primary utility layer and disappears on mobile.

**`nav-bar`** — White background, 60px tall, main category labels in 14px semi-bold. A bottom hairline separates from page content. Hover reveals a mega-panel flyout rather than a simple dropdown.

**`nav-mega-panel`** — White surface with a 1px hairline border and a 16px drop shadow. Category links render as dense body-sm text columns organized by product type (e.g., Hydraulic Pumps → Gear Pumps / Piston Pumps / Vane Pumps). No illustrations or photography — the panel is a pure text directory matching the MRO catalog convention.

### Product Cards

**`product-card`** — White card with a 1px hairline border and a minimal 4px box shadow. Title links in primary navy at 15px/600. Part number displays directly below in monospace (`{typography.part-number}`) for at-a-glance identification. Price renders at 22px/700 in ink. A stock-status badge (green or red) sits alongside the price, and sale/new overlay badges anchor to the top-left corner. Add-to-cart button runs full width at the card bottom on hover.

### Badges

**`badge-sale`** — Crimson (#a90f14) background, white 11px condensed caps, 2px radius. Overlays the top-left corner of product card images. **`badge-new`** — Same geometry in link-blue (#0066b4). **`badge-stock-available`** and **`badge-stock-unavailable`** use contextual green (#2d7a3a) and red (#cc2b2b) respectively, appearing inline next to the price rather than as image overlays.

### Hero Banner

**`hero-banner`** — Full-width navy (#003366) band, minimum 320px tall. Headline in display-xl white; supporting copy in body-md at 85% opacity. A crimson accent button sits below the copy. Used on the homepage and category landing pages for seasonal promotions and featured product lines.

### Category Tiles

**`category-tile`** — Light surface (#f5f7f9) cards with 1px hairline border, square corners, and navy title text. On hover, the tile fills solid navy and text inverts to white — a hard binary state swap rather than a gradient fade. Icons or silhouette product images may accompany the label.

### Filter Sidebar

**`filter-sidebar`** — Left-column panel in surface-soft with filter group titles rendered in condensed all-caps ({typography.label-condensed}, {colors.muted}). Checkboxes, toggle groups, and range sliders appear inside each group. The panel is sticky on desktop; on mobile it collapses behind a "Filter & Sort" drawer trigger button.

### Specification Table

**`spec-table`** — Full-width table with a navy header row in white condensed caps and alternating surface-soft row stripes. Used on product detail pages to tabulate pressure ratings (PSI/bar), port configurations, flow rates (GPM), temperature ranges, and material specs. Horizontal scroll is enabled on narrow viewports with a right-fade gradient indicator.

### Promo Ribbon

**`promo-ribbon`** — A full-bleed crimson (#a90f14) strip used for sitewide announcements (free shipping thresholds, holiday hours, clearance events). Text in white condensed caps at 11px. Sits above the nav-top-strip and is the first element in DOM order.

### Footer

**`footer`** — Dark charcoal (#2f2f2f) band spanning full width. Section columns: Product Categories, Customer Service, About AHE, Contact Information. Heading labels in white 15px/700; links in #bbbbbb body-sm. A logo lockup and social icons row appear at the bottom of the column grid above a thin copyright line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger drawer replaces nav-top-strip and nav-bar; search bar goes full-width below condensed header; filter sidebar becomes slide-in drawer; product grid collapses to single column; spec tables enable horizontal scroll; sticky add-to-cart bar appears on product detail page bottom |
| Tablet | 744–1128px | Two-column product grid; mega-menu becomes full-width accordion; filter sidebar shown as collapsible panel above results grid; nav-top-strip visible |
| Desktop | 1128–1440px | Three- to four-column product grid; mega-menu flyout panel; filter sidebar sticky left column ~240px wide; full nav-top-strip |
| Wide | > 1440px | Content container capped ~1400px with equal gutters; hero banner stays full-bleed; filter sidebar widens to ~280px; product grid up to five columns |

### Touch Targets
- All buttons minimum 40px height; add-to-cart button 44px on mobile product detail pages
- Hamburger nav trigger 44×44px tap area
- Filter checkboxes padded to 28×28px touch target with generous label padding
- Part number copy links padded to at least 36px height for accurate tapping
- Quantity stepper buttons minimum 40×40px

### Collapsing Strategy
- Top utility strip (account, dealer login, phone) hides on mobile; phone number surfaces inside hamburger menu
- Mega-menu navigation converts to a full-screen accordion drawer on mobile and tablet
- Breadcrumb truncates to last two levels on mobile with an ellipsis ancestor link
- Spec table overflow scrolls horizontally with a right-edge fade gradient hinting at additional columns
- Footer column grid stacks vertically with accordion toggles per section on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface confirmed — Open Sans is a strong candidate from font-stack extraction but weight calibration and sizing scale are estimated from MRO catalog conventions, not measured from live screenshots
- Several extracted hex values (#00d084, #0693e3, #2271b1, #cd2653, #7a00df, #f0b849, #4ab866, #e4ff00, #cd2653) are recognizable WordPress Gutenberg editor palette colors and were excluded as CMS framework artifacts rather than brand tokens
- No meta theme-color set, so mobile browser chrome color is unconfirmed
- Pricing display model (login-gated pricing, quantity-break tiers, call-for-price states) could not be extracted — standard visible price is assumed
- Exact mega-menu category depth and subcategory count not captured; component described from MRO catalog conventions
- Animation and transition timing values not available from static extraction
- Logo dimensions, clearspace rules, and favicon treatment not confirmed
- Whether a monospace font (Roboto Mono) is actually loaded for part numbers is unconfirmed; fallback to Courier New will be used if not present
