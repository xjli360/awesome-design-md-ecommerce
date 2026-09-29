---
version: alpha
name: "RS (RS Group)"
source_url: "https://us.rs-online.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Forty thousand components in a search box — that is RS Group's opening gambit. Where most distributors bury stock status in footnotes, RS surfaces unit price, packaging quantity, and real-time inventory count in the same card row, a density choice that signals the site is built for engineers at midnight chasing a specific MOSFET, not for casual shoppers. The brand's single chromatic anchor is RS red, approximately #da0011, a mid-warm signal red with enough orange in it to read as urgent without tipping into alarm-state territory; it drives every primary CTA, the masthead logo bar, and promo callout ribbons against an otherwise white-and-gray utilitarian shell. Navigation is structurally ambitious — a mega-menu taxonomy spanning 28 top-level product families means the nav bar carries more cognitive load than most consumer sites put in their entire homepage. Type scales stay compact and functional, leaning on 13–15px body text that serves part-number tables without requiring horizontal scroll on standard desktop widths. Cards are rectangular with squared corners or minimal radius, reinforcing the industrial register rather than the consumer-friendly pill-and-softness grammar. The search bar is the dominant UI element above the fold — wide, prominent, with autocomplete depth that surfaces product families, part numbers, and manufacturer names simultaneously. Surface colors cycle through white canvas, a light gray for alternating table rows, and a near-white card background; RS does not use strong elevation shadows, preferring a 1px hairline border to separate cards from canvas. The footer is a dense resource grid linking to technical references, regulatory compliance documents, and supplier partnership pages — content that has no equivalent in consumer DTC design and marks this as a professional-grade procurement tool.

colors:
  primary: "#da0011"
  primary-active: "#a8000d"
  primary-disabled: "#f0a0a5"
  primary-light: "#fce8e9"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  border-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-alt-row: "#fafafa"
  on-primary: "#ffffff"
  success: "#2e7d32"
  success-soft: "#e8f5e9"
  warning: "#e65100"
  warning-soft: "#fff3e0"
  out-of-stock: "#999999"
  info: "#0057a8"
  info-soft: "#e3f0fb"
  promo-ribbon: "#da0011"
  nav-bar-bg: "#da0011"
  nav-bar-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  table-header:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-primary:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-secondary:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-lg:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-strong}"
    padding: 9px 19px
    height: 40px
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
  button-ghost-red:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  add-to-basket:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    iconLeft: cart
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-strong}"
    padding: 8px 12px
    height: 38px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
    focusBorderColor: "{colors.primary}"
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
    submitButtonWidth: 52px
  nav-bar:
    backgroundColor: "{colors.nav-bar-bg}"
    textColor: "{colors.nav-bar-text}"
    typography: "{typography.nav-primary}"
    height: 52px
    logoAreaWidth: 140px
    searchAreaFlex: 1
    utilityLinksColor: "{colors.on-primary}"
  nav-utility-strip:
    backgroundColor: "#1a1a1a"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 32px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-secondary}"
    borderTop: "3px solid {colors.primary}"
    columnCount: 4
    headerColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    partNumberTypography: "{typography.part-number}"
    priceTypography: "{typography.price-sm}"
    hoverBorderColor: "{colors.primary}"
    hoverBoxShadow: "0 2px 8px rgba(218,0,17,0.12)"
  product-card-list:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    layout: horizontal
    imageWidth: 120px
    partNumberTypography: "{typography.part-number}"
    priceTypography: "{typography.price-lg}"
  parametric-filter-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    width: 240px
    activeFilterColor: "{colors.primary}"
    checkboxAccentColor: "{colors.primary}"
  stock-badge-in-stock:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-low:
    backgroundColor: "{colors.warning-soft}"
    textColor: "{colors.warning}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-out:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.out-of-stock}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  promo-ribbon:
    backgroundColor: "{colors.promo-ribbon}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    padding: "3px 8px"
    rounded: "{rounded.none}"
  price-break-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.table-header}"
    border: "1px solid {colors.hairline}"
    alternateRowColor: "{colors.surface-alt-row}"
    rounded: "{rounded.none}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    hoverBorderColor: "{colors.primary}"
    hoverBackgroundColor: "{colors.primary-light}"
  datasheet-link:
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.info}"
    hoverTextColor: "{colors.primary}"
  footer:
    backgroundColor: "#1a1a1a"
    textColor: "#cccccc"
    linkColor: "#aaaaaa"
    linkHoverColor: "{colors.on-primary}"
    headingColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid RS red (#da0011) fill with white type, 40px tall, 2px radius — the minimal rounding signals utility over friendliness. Hover darkens to `{colors.primary-active}` (#a8000d); disabled state washes out to `{colors.primary-disabled}`. Used exclusively for "Add to Basket", checkout confirmation, and account creation actions.

**`button-secondary`** — White canvas with a 1px medium-gray border and dark ink text. On hover the border tints to `{colors.primary}` and text shifts to red, creating a hover state that echoes brand color without committing to fill. Used for "Compare", "Save to List", "Request Quote", and secondary navigation actions.

**`button-ghost-red`** — Transparent background, red text, underlined. Used for inline textual actions like "View all", "See more", and "Technical specifications" links within body copy and product description panels. No border, no padding container.

**`add-to-basket`** — Shares the `button-primary` visual treatment but includes a cart icon to the left of the label. The icon + label lockup sits at a consistent 40px height. Quantity stepper (–/+) sits adjacent at the same height, separated by `{spacing.sm}`.

### Search

**`search-bar`** — Full-width within the red masthead, white input field with a 2px hairline border that focuses to red. The submit button is a solid red block (52px wide) flush to the right edge of the input, containing a white magnifying-glass icon. Autocomplete dropdown appears below with 1px hairline border, white background, and 8–12 items grouped by product family, part number match, and manufacturer. This component is the visual center of the entire above-fold experience.

### Navigation

**`nav-bar`** — A solid RS red (#da0011) bar at 52px height spanning the full viewport width. Left zone holds the white RS logo lockup (~140px). Center zone holds the `search-bar` stretching to fill available space. Right zone contains utility icons (account, basket, wishlist) in white. No transparency or scroll effects — the bar stays red at all scroll positions.

**`nav-utility-strip`** — A 32px near-black (#1a1a1a) strip above the main nav bar containing country/currency selectors, "Sign In / Register" text links, and order-tracking link in small gray caption type. This strip collapses entirely on mobile.

**`mega-menu`** — Triggered on hover over top-level category labels (a secondary dark bar below the red masthead). Drops a full-width panel on a white canvas with a 3px red top border accent. Four-column layout: column 1 holds subcategory headings in bold, columns 2–4 hold tertiary links in 13px regular weight. The depth and column count distinguishes RS from consumer DTC mega-menus — 40–80 visible links in a single panel is common. Box shadow grounds the panel over page content.

### Product Cards

**`product-card`** — Square white card with 1px hairline border, no border radius (squared corners reinforce industrial catalog register). Contains a square product image at top (1:1 aspect), manufacturer name in muted caption, product title in 13px bold body, RS part number in monospace `{typography.part-number}`, stock badge, unit price, and "Add to Basket" button. Hover state shifts border to red and adds a faint red-tinted drop shadow.

**`product-card-list`** — Horizontal layout variant used in list-view search results. 120px image on the left, all text metadata in a vertical stack to the right, with larger `{typography.price-lg}` price display and a more expanded description excerpt (2–3 lines). Technical specifications appear as a compact key–value row below the description.

**`price-break-table`** — A compact HTML table component unique to RS's B2B pricing model. Columns: quantity break, unit price, and optionally contract/account price. Header row uses uppercase table-header type on a soft gray background; alternating rows use near-white `{colors.surface-alt-row}`. Red highlight on the currently selected quantity tier.

### Parametric Filters

**`parametric-filter-panel`** — Left-rail panel (240px) on category and search results pages. Section headers in bold 13px, filter values as checkboxes with red `{colors.primary}` accent color when checked, numeric range sliders with red track fill. Active filter pills appear above results in a "Your filters:" strip. This panel is the dominant UI pattern distinguishing RS from consumer DTC — filter trees can reach 6–8 levels deep for parameters like tolerance, power rating, and operating temperature.

### Badges and Status

**`stock-badge-in-stock`** — Green-on-green-soft pill, uppercase 11px bold, 2px radius. Typically shows exact stock quantity ("In stock: 4,821") rather than a binary flag — a transparency signal aimed at engineers who need confidence before specifying a part.

**`stock-badge-low`** — Amber-on-amber-soft pill, same size and weight as in-stock badge. Shown when quantity drops below a threshold (typically <100 units).

**`promo-ribbon`** — Solid red banner, no border radius, uppercase badge type in white. Overlays the top-left corner of product card images or sits at the top of a section header. Used for "New Product", "Sale", and "Featured Supplier" callouts.

### Product Detail

**`datasheet-link`** — Blue text link with a PDF icon glyph, 13px body-sm weight. Appears in the documents section of every product page. Color follows `{colors.info}` to visually separate technical document links from navigation links (which use red). Hover shifts to red to acknowledge the user's intent to act.

**`breadcrumb`** — Single-line navigation trail in 12px caption type, muted gray text with right-chevron separators. Active (current) page in ink. Full trail clickable; hover state shifts to red. On mobile the trail truncates to show only parent and current level.

**`category-tile`** — Used on category landing pages as a 2–4 column grid of navigational tiles. Light gray background with 1px hairline border, product-family icon centered above the category label, bold 13px title. Hover shifts border to red and background to the pale `{colors.primary-light}` tint — the only softly red-tinted surface in the system.

### Footer

**`footer`** — Near-black (#1a1a1a) background, four or five columns of resource links: Products, Solutions, Services, About RS, Help. Link text in #aaaaaa gray, column headers in white bold. A secondary strip below holds legal, privacy, and cookie links at caption size. The depth of the footer resource tree (30–50 links) matches the catalog complexity and serves engineers navigating regulatory, compliance, and technical reference content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav utility strip hidden; red masthead stacks logo above full-width search bar; hamburger menu replaces mega-menu taxonomy; product grid collapses to single column; parametric filters move to a slide-in drawer triggered by a "Filter" button above results |
| Tablet | 744–1128px | Two-column product grid; mega-menu remains but column count reduces to two; search bar narrows slightly; price-break table scrolls horizontally within card |
| Desktop | 1128–1440px | Full four-column mega-menu; three-column product grid with left filter rail; utility strip visible; all nav elements at full weight |
| Wide | > 1440px | Content container max-width caps at ~1440px with canvas side margins; product grid can expand to four or five columns; filter rail stays fixed at 240px; no full-bleed hero stretch |

### Touch Targets

- "Add to Basket" button minimum 44px tall on mobile to meet touch target floor
- Quantity stepper +/– buttons minimum 36px × 36px tap area regardless of visual size
- Filter checkboxes expand touch zone to 44px height rows on mobile
- Nav hamburger menu icon 44×44px tap target
- Product card entire surface is tappable on mobile (not just title/button)

### Collapsing Strategy

- Parametric filter panel collapses to full-screen drawer with "Apply Filters" CTA on mobile; filter count badge shows on trigger button
- Mega-menu collapses to accordion-style tree within the hamburger drawer; L1 → L2 → L3 progressive disclosure
- Price-break table scrolls horizontally within a fixed card width rather than reflowing columns
- Product comparison bar (sticky at bottom) collapses from 4 items to 2 items on mobile
- Nav utility strip (account, track order, country selector) moves into the hamburger drawer on mobile
- Breadcrumb trail truncates to immediate parent + "…" + current on screens under 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from us.rs-online.com — the site likely loads design tokens via JavaScript bundles not accessible to static extraction. The RS red (#da0011) is used as an approximation of the widely documented RS Group brand red; the exact production hex value may differ.
- No font-family stacks were extracted. Arial/Helvetica system fallbacks are used as placeholders; RS may use a licensed sans-serif (possibly a custom face or a licensed grotesque such as Akzidenz-Grotesk or Neue Haas Grotesk) not accessible without JS execution.
- Exact nav bar height, spacing grid, and icon sizing are inferred from standard industrial distributor patterns rather than measured values.
- Account-specific UI (quote management, order history, approval workflows, contract pricing panels) was not captured — RS has a substantial logged-in B2B experience that likely diverges significantly from the public-facing catalog design.
- Dark mode / high-contrast mode support could not be verified.
- Animation and transition timing values (hover transitions on cards and buttons, mega-menu open/close) were not captured.
- Mobile breakpoint exact pixel values and responsive grid column counts may differ from the inferred values above.
