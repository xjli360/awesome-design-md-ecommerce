---
version: alpha
name: "BoltsandNuts.com"
source_url: "https://www.boltsandnuts.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Blood-red at #9f0000 is not decorative — it reads like oxide primer on hot-rolled steel, marking every "Add to Cart" trigger and primary CTA with the authority of a brand whose audience has measured twice. The site name is functional to the point of bluntness, and the design follows suit: Montserrat capitals anchor category headers and price points while Barlow runs body copy and form labels at weights that keep dense part-number grids legible without cramping. The palette is disciplined. Three shades of red (#9f0000, #b13030, #c56666) operate as a tint-and-shade ladder for hierarchy within branded elements, while an unexpected utility blue (#30abd8, #66c1e2, #99d5ec) surfaces in shipping callouts, info badges, and section accents — the kind of blue that appears on industrial signage precisely because it reads as neutral-informational rather than alarming. The majority of the canvas lives in a stepped neutral column: near-black #1a1a1a for ink, graduated grays (#5b5b5b body, #898989 muted, #cfcfcf hairlines) descending to #f5f5f5 surface-soft and implied white canvas. A secondary navy-slate register (#444e72, #747c97, #a3a8b9) appears in supporting UI — account navigation, category chips, blueprint-adjacent accents — without competing with the primary red. Corner radii are minimal: `{rounded.xs}` on inputs and product cards, `{rounded.sm}` on primary buttons, keeping the interface functional and direct. Spacing is generous at the section level (`{spacing.section}` between category rows) but tight at the component level — bulk pricing tables and specification grids favor density over breathing room because professional buyers are scanning part numbers, not browsing editorials.

colors:
  primary: "#9f0000"
  primary-active: "#7a0000"
  primary-disabled: "#d99999"
  primary-tint-mid: "#b13030"
  primary-tint-light: "#c56666"
  primary-tint-softest: "#c6b7b7"
  accent-blue: "#30abd8"
  accent-blue-mid: "#66c1e2"
  accent-blue-light: "#99d5ec"
  navy: "#444e72"
  navy-mid: "#747c97"
  navy-light: "#a3a8b9"
  navy-softest: "#b1b6cf"
  ink: "#1a1a1a"
  body: "#5b5b5b"
  muted: "#898989"
  muted-soft: "#b9b9b9"
  hairline: "#e0e0e0"
  hairline-soft: "#cfcfcf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#c2c2c2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  body-md:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-dense:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-label:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  sku-mono:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "2px solid {colors.hairline-soft}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 44px 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
    iconColorFocus: "{colors.primary}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    width: 80px
    height: 40px
    buttonBackground: "{colors.surface-soft}"
    buttonBorder: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    topBarBackground: "{colors.primary}"
    topBarTextColor: "{colors.on-primary}"
    topBarTypography: "{typography.caption-label}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headerColor: "{colors.primary}"
    headerTypography: "{typography.title-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    imageAspect: "1 / 1"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    skuTypography: "{typography.sku-mono}"
    skuColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    hoverBorder: "1px solid {colors.primary-tint-mid}"
    hoverShadow: "0 2px 8px rgba(159,0,0,0.10)"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-card-badge-info:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-image-viewer:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    thumbnailBorder: "2px solid {colors.hairline}"
    thumbnailBorderActive: "2px solid {colors.primary}"
  bulk-pricing-table:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    rowTypography: "{typography.body-sm}"
    rowColor: "{colors.body}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    rowAlternateBackground: "{colors.surface-soft}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.body-dense}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-dense}"
    valueColor: "{colors.ink}"
    rowAlternateBackground: "{colors.surface-soft}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 360px
  info-callout:
    backgroundColor: "{colors.accent-blue-light}"
    textColor: "{colors.navy}"
    border: "1px solid {colors.accent-blue-mid}"
    iconColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  shipping-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 36px
    minWidth: 36px

## Components

### Buttons

**`button-primary`** — The primary action surface runs `{colors.primary}` (#9f0000) with white uppercase Barlow at 15px/0.5px tracking on `{rounded.sm}` corners at 44px height. Hover state deepens to `{colors.primary-active}` (#7a0000); disabled washes out to `{colors.primary-disabled}` (#d99999). Appears on category-level CTAs, "View Details," and any action requiring a clear commitment.

**`button-secondary`** — A 2px `{colors.primary}` outline on white ground with matching red type, maintaining brand color without flooding the viewport in red. Used for "Request Quote," "Download Spec Sheet," and secondary filter confirmations. Hover shifts background to `{colors.surface-soft}` and border to `{colors.primary-active}`.

**`button-add-to-cart`** — Full-width variant of `button-primary` at 48px height with 32px horizontal padding, dominating the PDP sidebar. Stacks directly beneath the `quantity-input` in a tight column, the two components functioning as a procurement unit.

**`button-ghost`** — Transparent background with `{colors.body}` text and `{typography.button-sm}`. Reserved for tertiary actions: "Compare," "Save to List," pagination edge arrows, and modal close triggers.

### Search

**`search-bar`** — Full-width bar anchored in the nav zone with a magnifier icon that shifts from `{colors.muted}` to `{colors.primary}` on focus. The 2px border transitions from `{colors.hairline-soft}` to `{colors.primary}`, creating an unmistakable focus ring for keyboard users navigating by part number or thread spec. Placeholder copy should suggest search-by-spec patterns ("Search by part number, thread size, material…").

### Navigation

**`nav-bar`** — Two-tier structure: a `{colors.primary}` top bar at ~32px carrying shipping-threshold copy and trust signals in `{typography.caption-label}` uppercase white, then a `{colors.ink}` main nav bar at 56px with category links in `{typography.nav-link}`. Dropdowns (`nav-dropdown`) surface on white with `{colors.primary}` section headers — procurement managers can scan product families fast without reading every item.

**`breadcrumb`** — Renders parent categories in `{colors.muted}` and current page in `{colors.ink}`, separated by `{colors.muted-soft}` chevrons. Essential at catalog depth; fastener sub-categories nest three or four levels deep.

### Product Card

**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. Square product image sits on `{colors.surface-soft}`. Beneath: part number in `{typography.sku-mono}` muted gray (scannable at a glance), product title in `{typography.title-md}` ink, price in `{typography.price-display}` `{colors.primary}`. Hover promotes the border to `{colors.primary-tint-mid}` and adds a faint red box shadow. Badges (`product-card-badge`) pin absolute to the image corner.

**`product-card-badge`** / **`product-card-badge-info`** — Red for "New," "Sale," or "Low Stock"; blue (`{colors.accent-blue}`) for "In Stock" or "Ships Today." Uppercase Barlow at 11px, `{rounded.xs}`, 3px×8px padding — compact but legible at grid density.

### Product Detail

**`bulk-pricing-table`** — A tiered quantity-break table (1–9 / 10–49 / 50–99 / 100+) is the key conversion surface for B2B buyers. Header row uses `{colors.surface-soft}` background with `{typography.title-sm}` labels; rows alternate `{colors.surface-soft}` for scannability. Price cells render in `{colors.primary}` `{typography.price-sm}` so savings are immediately visible without mental arithmetic.

**`spec-table`** — Two-column key-value grid for thread pitch, material grade, finish, head type, and drive style. Runs `{typography.body-dense}` throughout for maximum density: label column in `{colors.muted}`, value column in `{colors.ink}`, alternating row backgrounds from `{colors.canvas}` to `{colors.surface-soft}`.

**`product-image-viewer`** — Main image on `{colors.surface-soft}` with thumbnail strip beneath. Active thumbnail receives a 2px `{colors.primary}` ring; inactive thumbnails hold `{colors.hairline}` borders.

**`quantity-input`** — Compact 80px-wide spinner with flanking +/− buttons, all bordered in `{colors.hairline-soft}`. Designed for procurement volumes — supports typed entry, not just incremental tapping.

### Badges and Callouts

**`info-callout`** — Light blue wash (`{colors.accent-blue-light}` background, `{colors.accent-blue-mid}` border) for shipping timelines, minimum order notices, hazmat disclaimers, and spec caveats. The blue accent family reads as informational — attention without alarm, consistent with industrial signage convention.

**`shipping-badge`** — Solid `{colors.accent-blue}` rectangle on product cards and checkout rows, rendering lead time or stock status in `{typography.caption-label}`. Blue marks "proceed" against the red "attention" primary.

### Layout

**`hero-banner`** — Dark `{colors.ink}` field with `{colors.primary}` accent elements: headline underline rule, CTA button, decorative horizontal stripe. Minimum 360px height. Headline at `{typography.display-xl}`, subline at `{typography.body-md}` in `{colors.on-dark}`. Typically carries a promotional angle (free shipping threshold, new product line) rather than lifestyle imagery.

**`section-header`** — Category and page dividers use `{typography.display-md}` `{colors.ink}` with a 3px `{colors.primary}` bottom border rule — a standard catalog-page convention that visually nails the hierarchy without decorative weight.

**`category-chip`** / **`category-chip-active`** — Filter chips for material type (Stainless, Grade 5, Zinc), drive style (Phillips, Hex), and finish (Black Oxide, Galvanized). Inactive: gray ground with `{colors.hairline-soft}` border; active: solid `{colors.primary}` fill.

### Footer

**`footer`** — `{colors.ink}` background with a 4px `{colors.primary}` top border stripe anchoring it to the brand color. Section headings in `{colors.primary}` `{typography.title-sm}`; link text in `{colors.muted-soft}` stepping to `{colors.on-dark}` on hover. Column groups: Products, Account, Support, Resources. Newsletter input at bottom uses `text-input` styling against the dark field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar full width below nav logo row; bulk pricing table scrolls horizontally with sticky quantity column; nav collapses to hamburger with slide-in dark drawer; hero min-height 240px; spec table stacks label as gray row header above value |
| Tablet | 744–1128px | 2–3 column product grid; nav shows top-level categories, overflow to hamburger; hero 300px; bulk pricing table fully visible; PDP stacks image above detail column |
| Desktop | 1128–1440px | 4-column product grid; full two-tier nav with mega-dropdown panels; PDP sidebar layout — image viewer left, pricing and specs right; sticky add-to-cart bar visible without scroll |
| Wide | > 1440px | Container max-width 1440px centered; hero image bleeds edge to edge with constrained content zone at 1200px; product grid holds at 4 columns with increased gutter |

### Touch Targets

- All buttons minimum 44px height for thumb reach on mobile procurement workflows
- Quantity +/− buttons expand to 36×44px on mobile
- Category chips minimum 40px height on touch viewports
- Nav dropdown items minimum 48px tap target
- Pagination controls minimum 44×44px on mobile

### Collapsing Strategy

- Product grid: 4 → 3 → 2 → 1 column across breakpoints
- Spec table collapses label into a gray row header above each value on mobile
- Bulk pricing table scrolls horizontally on mobile with sticky first column (quantity range)
- PDP: image viewer moves above details panel on mobile; sticky "Add to Cart" bar pins to bottom viewport edge
- Footer columns stack vertically to single column below tablet; newsletter input moves to top of footer on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed body background hex extracted — white (#ffffff) assumed as standard Shopify canvas default
- `primary-active` (#7a0000) is derived by darkening `{colors.primary}` — not directly extracted from computed styles
- Font weights for Montserrat and Barlow not confirmed beyond browser rendering assumptions — 600 semi-bold and 700 bold assigned by convention
- Exact nav tier heights not extracted — 56px main nav and ~32px top bar estimated from standard Shopify theme patterns
- No icon set identified — SVG icon family unknown; likely a standard library (Feather, Material Icons, or theme-bundled set)
- Rounded corner values not extracted from computed styles — `{rounded.xs}` (4px) and `{rounded.sm}` (8px) assigned based on the no-frills industrial aesthetic implied by palette and category
- Dark mode support not confirmed; palette reads as light-mode-only
- Animation and transition durations not extracted
- Navy-slate register (#444e72, #747c97, #a3a8b9) placement is inferred — exact UI surfaces using these colors not confirmed
