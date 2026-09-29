---
version: alpha
name: "Uline"
source_url: "https://www.uline.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The red stripe anchoring Uline's masthead — #cc0000 cut flush against a deep #003366 navy — is not decoration but doctrine. This is a catalog company, and the website enforces the same density contract as the printed book it mails by the tens of millions each year to warehouses, labs, and dock offices across North America. Every element is held to the same standard the physical catalog demands: SKU visibility, price-break clarity, and a fast path to cart over any ambient brand expression. The palette is built from exactly two brand signals. Cardinal #cc0000 appears on every primary action — the search submit button, Add to Cart CTAs, promotional callout banners, the nav's bottom rule — while #003366 navy carries the global navigation rail, category hierarchy headers, and footer ground. Between them, a disciplined gray staircase — #808080 down through #aaaaaa, #c0c0c0, #d3d3d3, and #e4e4e4 — tiles table borders, surface backgrounds, and form fields without visual competition. Link blues #0064c7 and #0098f8 handle secondary link states inside a coherent blue family that never introduces a third competing signal; mid-range #336699 surfaces in hover states and horizontal separators. The single accent outlier is #ffff00 yellow, appearing as a high-contrast alert chip for promotional urgency — a warehouse signage convention carried directly into the interface. Typography runs entirely on Arial, AvantGardeGothic, and Helvetica: system and near-system faces that load instantly across the business buyers accessing the site from workstation PCs and purchasing-department desktops. Display sizes are modest at 22–28px, while body copy lands tight at 12–13px with minimal leading, reflecting the catalog imperative to surface ten product specifications where a consumer site might show three. Corners are sharp throughout — {rounded.none} is the dominant choice and {rounded.xs} the outer limit in most contexts, echoing the physical world of corrugated cartons and steel shelving. The product card shows the design at its most compressed: item number in small muted type, title as a tight link, price in {typography.price-display} at 16px bold, and a price-break quantity table immediately below. The overall effect is a B2B interface that trusts buyers to know what they need and optimizes relentlessly for transaction speed.

colors:
  primary: "#cc0000"
  primary-active: "#ee0000"
  primary-disabled: "#f5cccc"
  navy: "#003366"
  navy-mid: "#336699"
  link: "#0064c7"
  link-hover: "#0098f8"
  ink: "#000000"
  body: "#555555"
  muted: "#808080"
  muted-soft: "#aaaaaa"
  silver: "#c0c0c0"
  hairline: "#d3d3d3"
  hairline-soft: "#e4e4e4"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f2f2f2"
  surface-mid: "#efefef"
  on-primary: "#ffffff"
  on-navy: "#ffffff"
  alert-yellow: "#ffff00"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  item-number:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  table-header:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 6px 18px
    height: 30px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 6px 18px
    height: 30px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy}"
    border: "1px solid {colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 5px 17px
    height: 30px
    hoverBackgroundColor: "{colors.surface-card}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 6px 18px
    height: 30px
    hoverBackgroundColor: "{colors.navy-mid}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    height: 28px
    focusBorder: "1px solid {colors.navy}"
  utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 30px
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.nav-link}"
    height: 42px
    padding: "0 {spacing.base}"
    borderBottom: "3px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    inputTypography: "{typography.body-md}"
    inputColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 36px
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    submitWidth: 88px
    submitRounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    imageBackground: "{colors.surface-soft}"
    itemNumberTypography: "{typography.item-number}"
    itemNumberColor: "{colors.muted}"
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.link}"
    titleHoverColor: "{colors.primary}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    hoverBorderColor: "{colors.silver}"
  price-break-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    headerBackground: "{colors.surface-card}"
    headerTypography: "{typography.table-header}"
    headerColor: "{colors.ink}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    cellPadding: "4px 8px"
    activeTierBackground: "#fffde7"
    activeTierBorder: "1px solid {colors.primary}"
  add-to-cart-row:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.none}"
    ctaPadding: "8px 24px"
    ctaHoverBackgroundColor: "{colors.primary-active}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 28px
    width: 56px
    focusBorder: "1px solid {colors.navy}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.lg}"
    rounded: "{rounded.none}"
  alert-badge:
    backgroundColor: "{colors.alert-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  category-header:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.title-lg}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "3px solid {colors.primary}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.navy}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    hoverBorderColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.link}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.section}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — A compact, fully square-cornered red button at #cc0000, 30px tall, with white `button-md` text (13px/700). This height is deliberately lower than consumer-site norms, matching the dense catalog cadence where multiple actions share a row. Hover shifts to `primary-active` (#ee0000); disabled state renders `primary-disabled` (#f5cccc) fill with white text. It appears on every Add to Cart row, catalog order form, and primary CTA across the site.

**`button-secondary`** — White background with a 1px #003366 navy border and navy `button-md` text, same 30px height as the primary. Used for "Get a Quote," "Save List," and print/share controls where the red CTA would compete with surrounding promotional elements. Hover adds a `surface-card` (#f2f2f2) background tint. The hard rectangular silhouette is identical to the primary button.

**`button-navy`** — Solid #003366 fill with white text, same geometry as the primary. Used for account actions, "Order History," and navigation-adjacent CTAs. Hover shifts to `navy-mid` (#336699). This button prevents the red primary from becoming visually overloaded on pages that already carry promo banners and category headers in red.

### Search Bar

**`search-bar`** — A 36px-tall input assembly with a 2px #cc0000 border on all four sides, making the entire search container a brand signal before any interaction. The right 88px is a full-height solid red submit block in white `button-md` type. No rounding anywhere. This red-bordered, red-submit pattern is the most prominent interactive element across every page type, reinforcing that locating a SKU is the site's primary job.

### Navigation

**`utility-bar`** — A 30px strip above the main nav in `surface-soft` (#f6f6f6) carrying account links, store locator, order status, and catalog request in `body-sm` (12px/400/#555555). Link text uses `link` (#0064c7). A bottom `hairline` (#d3d3d3) separates it from the navy nav bar below.

**`nav-bar`** — A 42px-tall #003366 navy bar housing the primary category megamenu in white `nav-link` type (13px/700). A 3px bottom rule in `primary` (#cc0000) closes the nav assembly and visually anchors the red+navy brand header. Megamenu dropdowns open on hover with a white background and red-accented left borders on active items.

**`category-header`** — Full-width section-heading bars in `navy` (#003366) with white `title-lg` (18px/700) and a 3px bottom border in `primary` (#cc0000). Used at the top of every category landing and sub-category list, repeating the nav's visual grammar one level deeper into the hierarchy.

### Product Card

**`product-card`** — A tight 1px `hairline` (#d3d3d3) bordered card with no rounding. The image sits over a `surface-soft` (#f6f6f6) field; below it, the item number appears in `item-number` style (11px/700/muted gray), the title as a `link`-colored (#0064c7) `body-md` anchor, and the unit price in `price-display` (16px/700/ink). Hover shifts the border to `silver` (#c0c0c0). Cards tile in dense 4–6 column grids on desktop with adjacent borders shared, creating a continuous catalog-grid appearance.

**`price-break-table`** — A compact table below or alongside the main price showing quantity tiers and per-unit cost. The `surface-card` (#f2f2f2) header row uses `table-header` (12px/700); data cells use `body-sm` (12px/400) with 4px 8px padding. All borders are 1px `hairline`. The active quantity tier highlights with a pale #fffde7 background and a 1px primary red border, visually locking in the buyer's selected price point.

**`add-to-cart-row`** — A `surface-soft` strip with a top `hairline` border holding the `quantity-selector`, the large `button-primary` ("Add to Cart"), and secondary action links in a horizontal row at the bottom of any product detail panel. The CTA receives wider 8px 24px padding on this specific context for conversion emphasis.

### Promotional Elements

**`promo-banner`** — Full-width #cc0000 bars carrying promotional headlines in white `title-md` (15px/700) at 8px 24px padding. Used across the homepage and category tops for shipping promotions, catalog offers, and inventory events. No rounding; the red bleeds edge-to-edge.

**`alert-badge`** — A small rectangular chip in `alert-yellow` (#ffff00) with black `caption` text (11px/400), zero rounding, and 2px 6px padding. Applied to "SALE," "CLOSEOUT," and "LIMITED STOCK" states on product cards and search results. The yellow-on-white combination reads as a physical warehouse label shorthand.

### Structural

**`breadcrumb`** — A horizontal list of `link`-colored (#0064c7) anchors in `body-sm` (12px) separated by a `muted` (#808080) "/" character. The final active segment renders in plain `ink` (#000000) without an anchor. No background or border — purely typographic, sitting flush above category content.

**`category-tile`** — A `surface-card` (#f2f2f2) panel with 1px `hairline-soft` border and `navy` (#003366) `body-sm` label text. Used in department landing grids and the homepage category navigation matrix. Hover shifts the border to `primary` (#cc0000), the only animation on the otherwise static tile.

**`footer`** — A #003366 navy ground anchoring every page with a 3px top rule in `primary` (#cc0000) that mirrors the nav's bottom rule, closing the red+navy frame. Link columns render in `body-sm` white; hover shifts to full `canvas` (#ffffff). The quick-order and catalog-request links are promoted in the first footer column, preserving the transactional priority even at page bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer in navy; search bar becomes full-width with full-height red submit; price-break table scrolls horizontally; utility-bar collapses to icon row |
| Tablet | 744–1128px | 2–3 column product grid; nav shows top-level items with tap-to-expand dropdowns; breadcrumb truncates middle segments; promo banners maintain full-width bleed |
| Desktop | 1128–1440px | 4–5 column product grid; full megamenu on hover; utility-bar fully expanded; category-header breadcrumbs visible at all hierarchy levels |
| Wide | > 1440px | 6 column product grid; max-width container centered at ~1400px; promo banners bleed to viewport edge with centered inner content |

### Touch Targets

- All buttons override to minimum 44px touch height on mobile; desktop 30px height is a desktop-only constraint
- Quantity selector expands to 44px height with larger flanking +/– tap zones on mobile
- Nav drawer list items are 48px tall for comfortable thumb reach
- Product card tap area covers full card face including image field
- Breadcrumb segments receive 8px additional vertical padding on mobile for reliable tapping
- Alert badges maintain minimum 32px tap height on mobile even at small visual size

### Collapsing Strategy

- Megamenu → accordion-style drawer on mobile, tap-to-expand per top-level category
- Utility bar → "Account" and "Cart" icon buttons only on mobile; full text labels on tablet+
- Price-break table → horizontal scroll container with the leftmost "Qty" column position-sticky
- Footer columns → vertical stack with accordion expand/collapse per column section on mobile
- Category filter sidebar → slide-in panel from left, triggered by a "Filter" button in `button-navy` style
- Product grid → falls from 6 → 4 → 2 → 1 columns across breakpoints; no layout engine shift

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom AvantGardeGothic weight variants and exact per-component size usage not confirmed; Arial equivalents substituted from page-level font-family stacks
- Exact font-size and weight values for megamenu dropdown items not extracted — estimated from nav-link scale
- Hover and focus ring colors for text inputs not extractable from static scan; navy inferred from brand pattern
- Megamenu column count and internal gap values not confirmed from extraction
- Mobile breakpoint pixel values are estimates; Uline's exact grid breakpoints not confirmed
- Whether the search bar 2px red border is always present or only on focus-within not determinable from static extraction
- Price-break table highlighted tier background (#fffde7) is derived from common B2B convention, not extracted from the live palette
- `primary-disabled` (#f5cccc) is derived by lightening primary red, not extracted from the live palette
- Exact padding and height values for the add-to-cart row on product detail pages not confirmed
- Whether `slick` in the font stack refers to a slider library or a custom typeface is unresolved; no visual evidence of a non-Arial display face was found
