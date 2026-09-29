---
version: alpha
name: "PLC Direct"
source_url: "https://www.plcdirect.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Part numbers outnumber brand moments on every page — PLC Direct leads with catalog density, not storytelling, and that choice is itself the brand statement. Sixteen-digit part numbers rendered in monospace beside thumbnail photographs of DIN-rail modules tell you the audience: controls engineers who arrive with a BOM and leave with an order confirmation. The palette is anchored in a deep industrial navy (approximately #0057A4) drawn from the aerospace-adjacent visual vocabulary shared by Rockwell, Siemens, and AutomationDirect — the parent company that powers plcdirect.com — where blue signals reliability and certification rather than aspiration. Canvas stays a clinical #FFFFFF with table rows alternating onto a faint #F5F7FA, so part grids scan like datasheets. Text hierarchy compresses unusually flat: display and body sit one or two steps apart because engineers trust precision over drama. Buttons are moderate-radius rectangles (approximately `{rounded.xs}`–`{rounded.sm}`) — nothing pill-shaped, nothing hard-cornered — inheriting the industrial middle ground. Search is the dominant interaction surface, surfaced prominently in the header with a full-width input that accepts part numbers, keywords, or cross-reference codes. Navigation is tab-and-mega-menu driven, organized around product families (PLCs, HMIs, Drives, I/O, Sensors), not lifestyle categories. Product cards render as dense table rows on desktop — image, part number, short description, price, stock indicator, and add-to-cart in one horizontal band — because the buyer already knows what they want. The overall register is a technical reference manual made clickable: authoritative, legible, and deliberately free of anything that would slow down a procurement workflow.

colors:
  primary: "#0057A4"
  primary-active: "#004080"
  primary-disabled: "#99BFD9"
  primary-light: "#E6F0F9"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F5F7FA"
  surface-card: "#FFFFFF"
  surface-alt-row: "#F9FAFB"
  on-primary: "#FFFFFF"
  danger: "#CC0000"
  success: "#2D7D46"
  warning: "#B35C00"
  stock-in: "#2D7D46"
  stock-low: "#B35C00"
  stock-out: "#CC0000"
  part-number: "#0057A4"
  price-highlight: "#1A1A1A"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
  part-number-lg:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.4px
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  breadcrumb:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  price-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px

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
    padding: 8px 20px
    height: 36px
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
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.primary}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
    iconLeft: cart-icon
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 5px 12px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 7px 10px
    height: 34px
    focus-border: "1px solid {colors.primary}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 44px 8px 12px
    height: 38px
    placeholderColor: "{colors.muted-soft}"
    focus-border: "2px solid {colors.primary}"
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "0 {rounded.xs} {rounded.xs} 0"
    padding: 0 16px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "none"
  top-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  logo-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
    padding: "{spacing.lg}"
  product-card-list:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "none"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"
    imageSize: 80px
  product-card-grid:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageSize: 140px
    hover-border: "1px solid {colors.primary}"
  part-number-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.part-number}"
    typography: "{typography.part-number}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-in:
    backgroundColor: "{colors.stock-in}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-low:
    backgroundColor: "{colors.stock-low}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-out:
    backgroundColor: "{colors.stock-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  breadcrumb-trail:
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    separator: "›"
    activeColor: "{colors.ink}"
    linkColor: "{colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    altRowBackground: "{colors.surface-alt-row}"
    headerBackground: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    cellPadding: "6px 12px"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    hover-backgroundColor: "{colors.primary-light}"
    imageSize: 64px
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    padding: "4px 10px"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    width: 60px
    height: 34px
    textAlign: center
  alert-banner:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.primary-disabled}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "#222222"
    textColor: "#CCCCCC"
    typography: "{typography.body-sm}"
    linkColor: "#AAAAAA"
    headingTypography: "{typography.title-md}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A compact, flat-rectangular navy button (`{colors.primary}`, `{rounded.xs}`) at 36px tall, font-weight 700. The restrained height versus standard 44–48px consumer buttons signals a density-first interface where screen real estate belongs to part listings. Active state drops to `{colors.primary-active}` (#004080); disabled washes to `{colors.primary-disabled}` with no cursor change.

**`button-secondary`** — White fill with a 1px navy border and navy label, same radius and height as primary. Used for secondary actions like "Compare," "Save to List," or "Request Quote" where the primary slot is occupied by add-to-cart.

**`button-add-to-cart`** — Visually identical to `button-primary` but carries a cart glyph on the left. This is the highest-frequency action on product-listing and PDP pages; its placement is always rightmost in the product-row action cluster.

**`button-sm`** — 28px tall, 13px text, used inside table rows, pagination controls, and filter chips where the 36px primary would crowd the grid.

---

### Search

**`search-input`** + **`search-button`** — The search bar is the visual centerpiece of the `logo-bar`. The input is full-width between logo and cart icons, 38px tall with a flush right-attached navy `search-button`. Engineers type full part numbers (e.g., `D2-260`) or cross-reference codes; placeholder text reflects this: "Search by part number, keyword, or cross-reference." Focus state upgrades to a 2px `{colors.primary}` border. On mobile the bar collapses to a magnifier icon that expands to a full-width overlay.

---

### Navigation

**`top-bar`** — A 32px black utility strip (`{colors.ink}`) carrying phone number, account link, cart count, and regional/language selectors in 12px white text. Always rendered above everything else.

**`logo-bar`** — 72px white bar with the PLC Direct wordmark left-anchored, search center, and icon links (account, cart) right. Separated from nav by a `{colors.hairline}` 1px rule.

**`nav-bar`** — 44px solid `{colors.primary}` band with white-text category tabs: PLCs, HMIs, Drives, I/O Modules, Sensors, Power Supplies, Software. Hover state reveals the `mega-menu`; active tab carries an underline or light-tinted background.

**`mega-menu`** — Full-width panel dropping below the nav with white background, 1px border, and a 12px box shadow. Columns organize sub-categories as link lists; a featured product or promotional image may anchor the rightmost column. Typography is `{typography.body-md}` for links, `{typography.spec-label}` for column headings.

---

### Product Listings

**`product-card-list`** — The dominant display mode on category and search-results pages. A horizontal row: 80×80px product thumbnail left, then part number (`{typography.part-number-lg}` in `{colors.part-number}`), short description (`{typography.body-md}`), and a right-aligned cluster of price (`{typography.price-lg}`), stock badge, quantity input, and add-to-cart button. Rows separate by a `{colors.hairline-soft}` bottom border; alternate rows tint to `{colors.surface-alt-row}` for scan-readability across 20–50 results.

**`product-card-grid`** — Optional grid view (2–4 columns) with 140px images, the same part-number badge, and a stacked price + add-to-cart layout. Hover promotes the card border from `{colors.hairline}` to `{colors.primary}`.

**`part-number-badge`** — A small `{colors.primary-light}` pill with `{colors.part-number}` monospace text, attached to every product wherever the part number appears in non-primary type contexts (related products, order history, cross-reference tables).

---

### Stock Indicators

**`stock-badge-in`**, **`stock-badge-low`**, **`stock-badge-out`** — Three filled badge variants in green/amber/red corresponding to in-stock, low-stock, and out-of-stock states. Always 11px bold, `{rounded.xs}`. For procurement-critical buyers, stock status is load-bearing information — the badge sits immediately adjacent to the add-to-cart button.

---

### Product Detail

**`spec-table`** — A two-column key/value table consuming the full content width on PDP pages. Header row background in `{colors.surface-soft}`, alternate data rows in `{colors.surface-alt-row}`, labels in uppercase 12px `{typography.spec-label}`. This component carries the highest information density of any UI pattern on the site; it may render 40–80 rows for complex PLCs.

**`quantity-input`** — A narrow 60px center-aligned number input flanking the add-to-cart button. Supports keyboard increment/decrement; border darkens on focus.

---

### Utility

**`breadcrumb-trail`** — "Home › PLCs › Modular PLCs › D2-260" in `{typography.breadcrumb}` with `›` separators. All but the last segment link in `{colors.primary}`; the final crumb renders in `{colors.ink}` non-linked. Always present on category and PDP pages.

**`alert-banner`** — Light-blue `{colors.primary-light}` banner with a 1px `{colors.primary-disabled}` border for site-wide announcements (shipping delays, promotional pricing windows). Rendered between `logo-bar` and `nav-bar`.

**`pagination`** — Numbered page buttons in 28px squares, bordered, with current page filled `{colors.primary}` / white text. Flanked by "Prev" and "Next" text buttons.

**`category-tile`** — Square tile used on the homepage and top-level category pages. Gray background, centered 64px category illustration or icon, and a 14px bold navy category name below. Hover shifts to `{colors.primary-light}` fill.

**`footer`** — Dark `#222222` footer with four link columns (Products, Support, Company, Resources), a logo lockup, contact info block, and a legal/copyright strip. Link text in `#AAAAAA`; column headings white and 700 weight.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | `logo-bar` collapses search to icon; `nav-bar` becomes a hamburger-menu drawer sliding from left; `product-card-list` drops to stacked card layout (image top, details below); `spec-table` scrolls horizontally; `mega-menu` replaced by nested accordion inside the drawer |
| Tablet | 744–1128px | Search bar retains full width in `logo-bar`; nav tabs visible but truncated to 5–6 items with "More ›" overflow; `product-card-list` shows 3-column grid option; `mega-menu` renders in narrower 2-column layout |
| Desktop | 1128–1440px | Full three-bar header (`top-bar` / `logo-bar` / `nav-bar`); `product-card-list` is default with grid toggle; full `mega-menu` with 4–5 columns; `spec-table` full-width |
| Wide | > 1440px | Content max-width ≈ 1380px centered; `category-tile` grid expands to 6 columns; search bar grows proportionally; extra padding added to `mega-menu` columns |

### Touch Targets

- Add-to-cart buttons maintain minimum 36px height; on mobile, width expands to full row width for easier tapping
- Quantity input stepper includes −/+ flanking tap targets each ≥ 40×40px on mobile
- Nav drawer links expand to 48px row height on touch devices
- Stock badges and part-number badges are display-only, not interactive, so no minimum tap size applies

### Collapsing Strategy

- The three-tier header (`top-bar` / `logo-bar` / `nav-bar`) collapses to a two-tier header (condensed brand bar + icon strip) below 744px
- Category taxonomy depth (typically 3 levels) collapses to a slide-in accordion at mobile; breadcrumb truncates to one parent + current page
- `product-card-list` row mode is unavailable below 744px; grid 2-column becomes the default
- `spec-table` wraps into a single-column definition list below 480px rather than horizontal scroll, to avoid tiny text

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: The crawler returned zero hex values from plcdirect.com. All palette values in this file are approximations derived from the AutomationDirect parent-brand visual vocabulary and industrial-automation category norms. The primary navy (#0057A4) is an approximation — actual brand primary may differ. Verify against live site or brand assets before implementation.
- **No font stacks extracted**: Zero font-family declarations were captured. Arial/Helvetica system stack is assumed from the functional, cost-conscious nature of industrial catalog sites. The site may load a licensed web font (e.g., Open Sans, Roboto) not captured at extraction time.
- **No theme-color meta tag**: Prevents browser-chrome and PWA color inference.
- **Icon library unknown**: Category icons, cart/account glyphs, and nav icons are referenced but their specific library (Font Awesome, custom SVG sprite, etc.) could not be determined.
- **Exact border-radius values unconfirmed**: `{rounded.xs}` (4px) assumed; actual UI may use 0px (fully square) or 2px consistent with industrial-catalog conventions.
- **Mega-menu structure**: Column count, featured-product placement, and promotional zone layout within the mega-menu are inferred from category conventions, not extracted.
- **Checkout and account flows**: Order management, quote request, and account portal styling are unobserved; components defined here cover catalog and PDP surfaces only.
