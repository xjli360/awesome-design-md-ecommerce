---
version: alpha
name: "Cable Matters"
source_url: "https://www.cablematters.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Safety-vest orange (#f17506) is the load-bearing color of this catalog — not the friendlier tangerine consumer electronics brands favor, but a utility-grade signal hue that Cable Matters fires at every primary CTA, price callout, and promotional accent, set against a warm ecru canvas (#f5f4ef) that immediately separates the site from clinical-white competitors; the ecru choice is the quiet tell that this is a dense product database built for buyers who comparison-shop connector types and bandwidth ratings across hundreds of SKUs rather than browsing for brand experience. Text runs entirely in Arial — no custom typeface, no variable font — which reads as a trust signal in a category where purchase decisions rest on technical compatibility tables and accurate product photography rather than brand narrative.

  Red appears in two functional registers: a burnt crimson (#a72d2c) marks sale pricing and inventory warnings, while a hotter alert red (#d20000, escalating to #e12000) signals urgent low-stock or error states — a legible urgency ladder that works without iconography. Informational blue (#0263c1, deepening to #004b91 on hover) handles anchor links and callout badges, cleanly separated from the orange commercial register so a buyer scanning a spec page always knows which element is after their wallet and which is simply after their attention. The neutral stack runs warm — primary text at #484848, body copy at #595959, stepping through #757575 and #8c8c8c toward hairlines at #dedede — keeping the large SKU grid from reading as raw data.

  Buttons carry {rounded.xs} corners — workmanlike and unambiguous — and product cards sit on white ({colors.surface-card}) against the ecru page ground, lifted by a thin hairline border rather than drop shadows. Orange CTAs read at full saturation against both surfaces, ensuring add-to-cart actions stay unambiguous deep in a paginated category grid of hundreds of cable SKUs. Badge geometry shares the same low-radius discipline: no pill shapes, no theatrical hover states — a system that prizes scanability over decoration.

colors:
  primary: "#f17506"
  primary-active: "#ec7d04"
  primary-hover: "#f38727"
  accent-red: "#a72d2c"
  accent-red-dark: "#a50013"
  alert-red: "#d20000"
  alert-red-hot: "#e12000"
  accent-blue: "#0263c1"
  accent-blue-mid: "#2b70a9"
  accent-blue-dark: "#004b91"
  ink: "#484848"
  body: "#595959"
  muted: "#757575"
  muted-soft: "#9d9da1"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#f5f4ef"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

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
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  breadcrumb:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    height: 42px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 42px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    iconColor: "{colors.muted}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
    megaMenuBackground: "{colors.surface-card}"
    megaMenuBorder: "1px solid {colors.hairline}"
    megaMenuHeaderTypography: "{typography.title-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imagePadding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    ratingColor: "{colors.primary}"
    ctaButton: "button-primary"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-alert:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.sm}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: "{spacing.xs} {spacing.sm}"
  breadcrumb:
    textColor: "{colors.accent-blue}"
    typography: "{typography.breadcrumb}"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.body}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    alternateRowBackground: "{colors.canvas}"
  rating-row:
    starColor: "{colors.primary}"
    reviewCountColor: "{colors.accent-blue}"
    typography: "{typography.caption}"
  price-block:
    priceColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    salePriceColor: "{colors.alert-red}"
    strikethroughColor: "{colors.muted}"
    originalPriceTypography: "{typography.body-sm}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    itemTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    activeAccentColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid orange (#f17506) fill, white bold 15px Arial text, 4px radius ({rounded.xs}), 42px height. Hover lightens to `primary-hover` (#f38727); press deepens to `primary-active` (#ec7d04). Used for "Add to Cart", "Buy Now", and primary filter submissions — the only button that ever appears in orange fill.

**`button-secondary`** — White fill with a 1px orange border and orange text at the same size and radius as `button-primary`. Used for secondary commerce actions ("Compare", "Add to Wishlist") when the primary cart slot is already occupied. Hover shifts border and text to `primary-active`.

**`button-ghost`** — Transparent background, `accent-blue` (#0263c1) text, no border. Used inline for "See All", "View Details", and text-link-style CTAs within product descriptions and editorial sections.

### Search

**`search-bar`** — Full-width bar anchored in the top navigation. White fill, 1px `hairline` border, 40px height, {rounded.xs} on outer corners. A muted-gray magnifier icon sits left. The submit trigger is a flush-joined orange block button with no inner border radius, inheriting the outer {rounded.xs} on its right edge only — the color break alone is enough signifier. Placeholder text renders in `muted` (#757575).

### Navigation

**`nav-bar`** — 60px tall, white background, 1px `hairline` bottom border. Logo left-aligned; primary navigation items in bold 14px Arial expand via mega-menu panels for the extensive category tree (USB-C, Thunderbolt, DisplayPort, HDMI, Ethernet, power, AV). Mega-menu panels are white with hairline borders and category columns using `title-sm` headers in ink, body items in `body-sm`. Cart and account icons anchor the right edge. A `promo-banner` stripe in primary orange typically sits immediately above the nav for site-wide messages.

### Product Cards

**`product-card`** — White card on the ecru `canvas`, 1px `hairline` border, {rounded.xs} corners, 16px internal padding. Product image in a neutral padded well at top. `title-sm` product name below (two-line clamp with ellipsis). `rating-row` renders orange stars and a blue-underlined review count. `price-block` follows: current price in bold, sale price in `alert-red` with struck-through original in muted. A full-width `button-primary` anchors the card bottom. `badge-sale` overlays the image corner at top-left.

### Badges

**`badge-sale`** — Crimson (#a72d2c) fill, white uppercase 11px bold text with 0.5px tracking, 4px radius. Renders as an image overlay or inline beside a list price. **`badge-new`** — identical geometry in `primary` orange for new arrivals. **`badge-alert`** — hot red (#d20000) fill for low-stock and time-sensitive notices. All three share `badge-label` typography; the only differentiation is fill color, making urgency legible at a glance across a dense grid.

### Category Chips / Filters

**`category-chip`** — `surface-soft` (#f5f5f5) fill, 1px `hairline` border, {rounded.xs} radius, 4px/8px padding. Active state flips to solid `primary` orange fill with white text (`category-chip-active`) and an orange border. Used in the filter sidebar and horizontal scroll bars on category pages to refine by connector type, cable speed, cable length, or compatibility certification.

### Spec Table

**`spec-table`** — The structural workhorse of the product detail page. Two-column (label/value) or multi-column (comparison) layout. Header row background is `surface-soft`, header text uses `spec-label` (bold 13px). Data rows alternate between white and ecru `canvas` backgrounds. Hairline borders on all sides. On mobile the table scrolls horizontally inside its container. This component carries more purchase-decision weight than any other on the site.

### Price Block

**`price-block`** — Current price in `price-display` (22px bold, `ink` #484848). When on sale, the promotional price renders in `alert-red` (#d20000) at full `price-display` weight immediately above the struck-through original price in `body-sm` `muted` — a hard urgency signal that needs no label.

### Hero

**`hero`** — Full-bleed orange section used for campaign promotions and product-family launches (Thunderbolt 5, USB4, etc.). White `display-xl` headline, white `body-md` copy, no border radius. A white-fill outline CTA or `button-primary` sits below the headline. Campaign heroes may swap flat orange for a product-photography background with an orange color overlay at ~60% opacity, maintaining the brand register while adding visual variety.

### Promo Banner

**`promo-banner`** — Thin orange stripe above or below the nav bar announcing free shipping thresholds, site-wide promotions, or new certifications. `title-md` typography, white text, no radius. Dismissible with a white X icon on the right edge.

### Filter Sidebar

**`filter-sidebar`** — Left-rail panel on category pages. `canvas` (#f5f4ef) background, 1px `hairline` right border. Section headings in `title-sm` ink. Filter options as checkboxes with `body-sm` labels; selected state accents the checkbox and label in `primary` orange. Collapses to a bottom-sheet drawer on mobile triggered by a "Filter" `button-secondary`.

### Footer

**`footer`** — Dark `ink` (#484848) background anchored by a 3px `primary` orange top border as a brand marker. Four-column layout: white section headings in `title-sm`, `muted-soft` (#9d9da1) body links in `body-sm`. Bottom strip holds copyright, payment icons, and trust badges on a slightly darker band. Link hover shifts to white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger overlay with nested accordion categories; search bar drops below logo row; filter sidebar becomes bottom-sheet drawer with Apply/Clear actions; spec table scrolls horizontally; promo banner wraps to two lines |
| Tablet | 744–1128px | Two-column product grid; nav retains horizontal primary categories with overflow hamburger for deep subcategories; filter sidebar becomes collapsible left panel; hero padding reduces |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu navigation; filter sidebar persistent left rail; hero at full bleed with max text width ~600px |
| Wide | > 1440px | Grid expands to four columns; content container max-width ~1400px centered; ecru `canvas` bleeds to viewport edges as gutter |

### Touch Targets

- All buttons minimum 44×44px tap area on mobile
- Category chips expand vertical padding to 10px on mobile
- Nav icons (cart, account, hamburger) minimum 44×44px hit area regardless of rendered icon size
- Spec table rows minimum 40px height on mobile for comfortable scanning
- Filter checkboxes minimum 24×24px touch target with generous label hit area

### Collapsing Strategy

- Mega-menu collapses to nested accordion inside a full-screen hamburger overlay; parent categories are tappable headers, subcategories indent below
- Filter sidebar collapses to a "Filter" button (bottom-fixed on mobile) opening a full-height bottom-sheet drawer with Apply and Clear All actions
- Footer columns collapse to labeled accordion sections; each section header is a full-width tap target
- Promo banner remains pinned and stacks to two lines on narrow viewports rather than truncating
- Breadcrumb collapses to show only the immediate parent category plus the current page on mobile, separated by a `muted` chevron

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact disabled state for `button-primary` not extractable — assume `primary-hover` (#f38727) at 50% opacity as a safe fallback; not confirmed from static extraction
- Footer background may be darker than #484848 (the darkest neutral in the extracted palette); actual footer could use a near-black not surfaced by the color sweep
- Hover and active states for `button-secondary` and `button-ghost` inferred from primary button pattern; not directly confirmed
- No custom web font detected — site uses system Arial/Helvetica throughout; if a web font loads via late JavaScript injection it was not captured in static extraction
- Icon set source unknown — likely inline SVG; glyph style (outlined vs. filled) and stroke weight not determinable from extraction
- Exact mega-menu animation timing and easing curves not available from static analysis
- The presence of multiple overlapping reds (#a72d2c, #a50013, #d20000, #e12000) suggests context-based or state-based red variation (sale vs. error vs. urgency) that may be more granular than the three-register model above
- Mobile breakpoints estimated from common custom-platform patterns; exact pixel values not confirmed (platform-shopify: False indicates a non-Shopify stack with potentially custom breakpoint choices)
- Rating star style (filled, outlined, half-star) and exact star color shade not confirmed — `primary` orange (#f17506) assumed based on brand palette
