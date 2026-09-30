---
version: alpha
name: "Fisher Scientific"
source_url: "https://www.fishersci.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forty thousand SKUs at any given moment, and the primary visual question Fisher Scientific resolves is how to make a laboratory procurement catalog feel navigable rather than overwhelming. The answer is a strict two-register system — institutional blue (#005daa) holds wayfinding and authority, while a warm gray canvas (#efeced) absorbs the page's density without reading as sterile. Promotional voltage — yellow (#f5c51f), orange (#ed7700), brick red (#ee3134) — arrives only on sale chips and urgency banners, punching through the clinical backdrop in precisely the way a specials board punches through a hospital supply room. FisherSciengliffic, the proprietary display typeface, carries brand headings and logotype; Arial and Helvetica Neue handle the catalog at body scale, a deliberate split that keeps instrumentation-grade clarity while allowing the wordmark distinct identity. Rounded corners are nearly absent: {rounded.xs} on form fields and status chips, {rounded.sm} on action buttons — a geometry that reads instrumental rather than aspirational, consistent with the stainless-steel culture of its end users. A deep family of blues spans the interface, from the hover depth of #004985 to the hyperlink utility of #1b7dce and the soft wash of #dfedf9 in informational callout tiles — six distinct stops without requiring a second hue family. The green spectrum (#01891e through #3bad2f) functions as a legibility layer for availability ribbons, which scientists and procurement buyers read instinctively as "in stock, act now." Six-column mega-nav menus, a persistent search input anchored at every scroll position, and a sticky cart indicator define the interaction frame: this is procurement software with a brand layer, not a discovery-first shopping experience.

colors:
  primary: "#005daa"
  primary-active: "#004985"
  primary-hover: "#0071d0"
  primary-disabled: "#a4c5e3"
  primary-light: "#dfedf9"
  primary-lighter: "#c8ddef"
  ink: "#1b1b1d"
  body: "#2b2b2b"
  muted: "#565656"
  muted-soft: "#888888"
  hairline: "#d7d6d6"
  hairline-soft: "#e5e4e4"
  canvas: "#ffffff"
  surface-soft: "#efeced"
  surface-mid: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#1b7dce"
  link-hover: "#005daa"
  promo-yellow: "#f5c51f"
  promo-orange: "#ed7700"
  promo-red: "#ee3134"
  promo-red-alt: "#e71316"
  success: "#01891e"
  success-mid: "#179732"
  success-light: "#3bad2f"
  accent-purple: "#643fa7"
  charcoal: "#54545c"

typography:
  display-xl:
    fontFamily: "'FisherSciengliffic', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FisherSciengliffic', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'FisherSciengliffic', Arial, Helvetica, sans-serif"
    fontSize: 20px
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
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  price-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-category:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.2px
    textTransform: uppercase
  breadcrumb:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  catalog-number:
    fontFamily: "Arial, monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
    hoverBackgroundColor: "{colors.primary-light}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 12px
    hoverBackgroundColor: "{colors.primary-light}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
    height: 36px
    padding: 8px 10px
  nav-utility-strip:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    height: 40px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 48px
  mega-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-category}"
    border: "1px solid {colors.hairline}"
    headerColor: "{colors.primary}"
    columns: 6
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.primary}"
    imageBackground: "{colors.canvas}"
    priceTypography: "{typography.price-sm}"
    titleTypography: "{typography.body-md}"
    catalogTypography: "{typography.catalog-number}"
    catalogColor: "{colors.muted}"
  promo-badge:
    backgroundColor: "{colors.promo-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  sale-badge:
    backgroundColor: "{colors.promo-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  new-badge:
    backgroundColor: "{colors.promo-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  availability-chip:
    inStockColor: "{colors.success}"
    lowStockColor: "{colors.success-mid}"
    outOfStockColor: "{colors.promo-red}"
    typography: "{typography.caption}"
    iconSize: 12px
  promo-strip:
    backgroundColor: "{colors.promo-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    textAlign: center
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 320px
    padding: "{spacing.xxl} {spacing.section}"
    overlay: "rgba(0,73,133,0.7)"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    hoverBackgroundColor: "{colors.primary-light}"
    padding: "{spacing.base}"
  info-callout:
    backgroundColor: "{colors.primary-lighter}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.link}"
    activeColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  data-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.body}"
    headerTypography: "{typography.body-sm}"
    rowTextColor: "{colors.ink}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    altRowBackgroundColor: "{colors.surface-mid}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.link}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    itemSize: 32px
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.primary-lighter}"
    borderTop: "3px solid {colors.primary-hover}"

---

## Components

### Buttons
**`button-primary`** — Solid Fisher blue (#005daa) at 40px height with {rounded.sm} corners; the minimal 4px radius signals function over style. Hover lightens to #0071d0; active state deepens to #004985; disabled falls back to the extracted light blue (#a4c5e3), maintaining brand reference while indicating inactivity. Bold Arial at 14px ensures legibility against catalog-dense page backgrounds. Used for primary CTAs: "Add to Cart," "Request a Quote," "View Results."

**`button-secondary`** — White canvas with a 1px primary blue border and matching blue label. Hover fills with the soft blue tint #dfedf9 — enough contrast to register without abandoning the page's clinical restraint. Appears in paired CTA rows alongside `button-primary` for secondary actions like "Save to List" or "Compare."

**`button-ghost`** — Transparent background, primary blue label text, {rounded.sm}. Used for inline actions within product cards and data table rows where a bordered button would crowd dense information. Hover applies the same #dfedf9 tint as the secondary button.

**`button-sm`** — Compact 32px height at {rounded.xs}, bold 13px label. Appears inside product cards, search-result rows, and comparison tables where the full 40px button would overwhelm data density.

### Search Bar
**`search-bar`** — The most prominent interactive element on every page: a full-width input at 40px height with a flush blue submit button welded to the right edge ({rounded.none} so no gap appears between field and trigger). The input area carries {rounded.xs} on its left edge only. Placeholder text in #888888 ("Search by product name, catalog number, or keyword") signals procurement-trained users. A category scope selector sits left of the field as a bordered select element. Focus state promotes the border to 2px primary blue with no box-shadow, keeping the interaction tight and precise.

### Navigation
**`nav-utility-strip`** — A 32px dark-blue (#004985) full-bleed bar above the primary nav carrying account links, order status, and regional/lab preferences in 12px Arial caption. Scrolls away on desktop.

**`nav-bar`** — Primary blue (#005daa) full-width bar at 44px, hosting the FisherSciengliffic wordmark at left, the main category links, and account/cart icons at right. Sticky on scroll after the utility strip disappears. The stark blue-on-blue contrast between strip and bar creates a layered institutional authority without additional color.

**`mega-nav`** — Six-column dropdown panels on hover over top-level categories (Chemicals, Life Science, Lab Equipment, Safety, etc.). Column headings in 13px bold Arial in primary blue; sub-links in 13px regular {colors.body}. White background, 1px {colors.hairline} border, {spacing.lg} internal padding. The column count alone communicates catalog depth before users scroll a single pixel.

### Product Card
**`product-card`** — 1px {colors.hairline} border at {rounded.xs}; hover promotes the border to primary blue, confirming selection intent. Three lines of product title in body-md, catalog number in `{typography.catalog-number}` (12px with 0.3px letter-spacing, {colors.muted}) to visually separate descriptive copy from instrument-grade identifiers, then price in `{typography.price-sm}` bold. Availability chip and promo badge stack in the top-right corner of the image well. An `Add to Cart` button-sm renders below the price at full card width on hover or always on mobile.

### Badges
**`promo-badge`** — Red (#ee3134) rectangular chip at {rounded.xs}, uppercase 11px bold white label ("SALE", "LIMITED TIME"). **`sale-badge`** — Yellow (#f5c51f) fill with dark ink text, used for percentage-off promotions where the brightness alone draws the eye. **`new-badge`** — Orange (#ed7700) fill, white text, for recently listed products. These three states follow a traffic-light-adjacent logic — red for urgency, yellow for value, orange for novelty — that procurement buyers scan in sub-second recognition without reading the label. The accent purple (#643fa7) is reserved for Fisher Brand premium designation chips where catalog origin matters.

### Availability Chip
**`availability-chip`** — An inline status indicator: a small filled circle icon followed by plain text. In-stock renders in success green (#01891e) with "In Stock"; limited availability uses #179732 with a count suffix ("Only 4 Left"); out-of-stock uses #ee3134 with "Temporarily Unavailable." No background fill — the colored text-plus-icon alone carries the signal, keeping product rows uncluttered in dense catalog views.

### Hero Banner
**`hero-banner`** — Full-bleed image panel at 320px minimum height with a 0.7-opacity primary blue overlay preserving text legibility while lab photography shows through. FisherSciengliffic display-xl heading in white, body-md subtitle, and a button-primary CTA. Promotional hero variants swap the overlay for promo-red or a promo-yellow gradient; yellow variants switch to ink-colored headings for contrast compliance.

### Info Callout
**`info-callout`** — Light blue (#c8ddef) background tile with a 4px primary blue left-border accent, evoking a lab-notebook margin annotation. Used for regulatory notices, cold-chain shipping restrictions, and hazardous material handling alerts. Body-sm Arial at normal weight; {rounded.xs} corners. The left-border pattern is recognizable as "attention, but not error" — distinct from the promo-red strip used for urgency.

### Data Table
**`data-table`** — Surface-soft (#efeced) header row with bold body-sm labels; alternating {colors.surface-mid} (#e5e5e5) body rows at body-sm scale. Horizontal 1px {colors.hairline} cell dividers only — no vertical borders — maintaining a calm grid. Used for chemical property listings, instrument specification comparisons, and order history. Sortable column headers add a caret icon in primary blue.

### Footer
**`footer`** — Dark blue (#004985) full-width panel with white body-sm links organized in five or six labeled columns. Column headings in title-sm bold white. A 3px #0071d0 top border separates the footer from the last content row. Link hover color lightens to #c8ddef to remain visible on dark blue without going full white. Bottom bar carries legal/copyright in caption-scale muted text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Utility strip hidden; nav-bar collapses to hamburger + wordmark + cart icon; search bar drops below nav-bar at full width; product grid becomes single-column; mega-nav converts to full-screen accordion drawer; hero-banner height reduces to 220px; data tables get horizontal scroll overflow |
| Tablet | 744–1128px | Two-column product grid; mega-nav retains but compresses to three columns; utility strip visible but truncated to essential links; search bar stays in nav-bar row at reduced width |
| Desktop | 1128–1440px | Full six-column mega-nav; three or four-column product grid; utility strip fully expanded; sidebar filter panel appears in catalog views; hero-banner at full 320px |
| Wide | > 1440px | Content max-width caps at 1440px with symmetric canvas margins; product grid may expand to five columns on broad catalog views; hero-banner grows to 400px minimum height |

### Touch Targets
- All buttons minimum 40px height on mobile; icon-only controls (cart, account, search trigger) padded to 44×44px tap area
- Mega-nav replaced by full-screen drawer with 48px row height per top-level category
- Pagination items expand to 40px height on mobile with wider horizontal spacing
- Availability chips and promo badges maintain 32px minimum tap zone via invisible padding on mobile product rows

### Collapsing Strategy
- Utility strip is first to collapse (hidden below 744px)
- Mega-nav compresses to three columns at tablet, converts to full-screen accordion drawer below 744px
- Sidebar filters collapse into a modal "Filter & Sort" bottom sheet on mobile, triggered by a sticky pill button above the product grid
- Data tables gain `overflow-x: auto` horizontal scroll on mobile rather than reflowing columns; column count is preserved for spec integrity
- Six-column footer collapses to single-column accordion at mobile; column headings become tap-to-expand triggers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values not extractable from live site; {rounded.xs} (2px) and {rounded.sm} (4px) are inferred from the clinical B2B aesthetic of the extracted palette and category
- Canvas white (#ffffff) was not present in the extracted color list; assumed as the standard page background behind surface-soft (#efeced) content zones
- FisherSciengliffic font metrics (x-height, weight axes, optical sizing) are unknown; fontSize and lineHeight values for display-xl/md/sm are estimated from typical scientific catalog header patterns
- Exact nav-bar height (44px) and utility strip height (32px) are approximations not confirmed from extraction
- Product card image aspect ratio not extractable; likely 1:1 or 4:3 for chemistry and equipment imagery
- Search autocomplete dropdown styling (shadow depth, border treatment, result row height) not confirmed
- Hover transition durations not extracted; 150ms ease assumed as consistent with utility-first B2B UI norms
- Accent purple (#643fa7) use case is inferred as a Fisher Brand premium tier designator but not confirmed from the live site
- Whether promo-orange (#ed7700) appears at component level or only in marketing imagery is not confirmed
- Sticky behavior specifics (which elements remain fixed at which breakpoints) not confirmed from extraction
