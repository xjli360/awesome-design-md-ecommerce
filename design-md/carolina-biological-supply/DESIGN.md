---
version: alpha
name: "Carolina Biological Supply"
source_url: "https://www.carolina.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ninety-seven years of printed catalogs leave a mark — Carolina Biological Supply's digital presence carries the DNA of a supply-house catalog that science teachers have trusted since 1927: dense product grids, SKU-forward navigation, and an institutional blue that reads as credential rather than brand emotion. The primary hue sits in the medium-to-dark royal-blue register (#0066a4, estimated), a shade that signals academic authority and aligns visually with the kind of laminated binder covers found in every school stockroom. Where consumer brands layer photography and lifestyle aspiration, Carolina leans on structured taxonomy — phylum-level category trees, grade-band filters, and NGSS-alignment labels that are themselves a form of brand communication, telling the buyer that the company understands the curriculum as well as the specimen jar. Corners are conservative — modest radii of around 4–8px on cards and inputs, no pill-shapes in primary navigation. Call-to-action buttons carry a gold-amber contrast accent (#e07b00, estimated) against the blue primary, a pairing borrowed from the science-fair ribbon tradition that feels earned rather than arbitrary. Utility is the organizing principle: the homepage prioritizes the search bar above the fold, category tiles use high-contrast label overlays on photographic backgrounds of petri dishes and microscopes, and the product card leads with the catalog number before the product name — a habit from print that signals this site was built for purchasing agents and biology teachers with requisition forms in hand, not casual browsers. Type is system-stack sans-serif throughout, sized for scan-reading across wide product tables and long specification lists. The footer expands into a dense resource grid — teacher guides, safety data sheets, live-specimen care instructions — reinforcing that the brand's value proposition is expert support, not just supply logistics.

colors:
  primary: "#0066a4"
  primary-dark: "#004d7a"
  primary-active: "#004d7a"
  primary-disabled: "#99c3e0"
  primary-light: "#e6f1f8"
  accent: "#e07b00"
  accent-active: "#b86200"
  accent-light: "#fdf2e3"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f7f9"
  surface-card: "#ffffff"
  surface-table-alt: "#f0f4f8"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  success: "#2e7d32"
  warning: "#e07b00"
  error: "#c62828"
  safety-badge: "#b71c1c"
  ngss-badge: "#1565c0"
  grade-band: "#37474f"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, 'Liberation Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  sku-label:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.4px
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.2px
  table-header:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.5px
    textTransform: uppercase
  badge-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  search-input:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 42px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 42px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 42px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  add-to-cart:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 42px
    icon: cart-plus
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 8px 12px
    height: 40px
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.search-input}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 16px
    height: 48px
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.none} {rounded.sm} {rounded.sm} {rounded.none}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 52px
    borderBottom: none
  nav-bar-top-utility:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.accent}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
    rounded: "{rounded.none}"
    columnCount: 4
  category-tile:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    overlayGradient: "linear-gradient(to bottom, transparent 40%, rgba(0,51,83,0.82) 100%)"
    labelPosition: bottom-left
    aspectRatio: 4/3
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    skuTypography: "{typography.sku-label}"
    skuColor: "{colors.muted}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary-dark}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.10)"
  product-card-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  safety-badge:
    backgroundColor: "{colors.safety-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  ngss-badge:
    backgroundColor: "{colors.ngss-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  grade-band-badge:
    backgroundColor: "{colors.grade-band}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.table-header}"
    rowAltBackgroundColor: "{colors.surface-table-alt}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  spec-accordion:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    checkboxAccentColor: "{colors.primary}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  alert-info:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.accent-light}"
    textColor: "{colors.accent-active}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.accent}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "#99c3e0"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    borderTop: "3px solid {colors.accent}"
    columns: 5

## Components

### Buttons
**`button-primary`** — The primary action button runs institution blue (#0066a4) with white type at 700 weight. Corners use `{rounded.sm}` (4px), maintaining the conservative geometry of a catalog-driven interface. Active state darkens to `{colors.primary-active}` (#004d7a); disabled washes to a light tint `{colors.primary-disabled}`. Padding is compact at 10px vertical to fit dense product listing contexts.

**`button-accent`** and **`add-to-cart`** — Gold-amber (#e07b00) carries the purchase-intent actions, including the main "Add to Cart" button which pairs the accent color with a cart-plus icon. This amber-on-blue accent pairing is the primary brand contrast signal, echoing the science-fair ribbon tradition. Active state deepens to `{colors.accent-active}` (#b86200).

**`button-secondary`** — White background with a 1.5px primary-blue border and blue type. Used for secondary actions like "Add to Quote" or "View SDS." Ghost variant (`button-ghost`) strips the border for inline tertiary links within content areas.

### Search Bar
**`search-bar`** — Dominates the header with a 48px tall input field carrying a 2px `{colors.primary}` border, attached flush to a blue search-submit button. The attached button eliminates any gap, creating a unified input-action unit. No border radius on the interior edge between input and button; `{rounded.sm}` closes the outer corners. Placeholder text in `{colors.muted-soft}` uses `{typography.search-input}` (16px) to remain legible across browsers without zoom triggers on mobile.

### Navigation
**`nav-bar-top-utility`** — A slim 32px dark-blue (#004d7a) strip above the main nav carries account links, cart, and phone number in `{typography.caption}` white type. This two-tier nav pattern is characteristic of institutional B2B/B2E commerce: utility functions separate from primary category navigation.

**`nav-bar`** — The main navigation bar is full primary blue (#0066a4) at 52px. White type in `{typography.nav-link}` (14px, 600 weight) labels top-level categories: Science Kits, Living Organisms, Lab Supplies, Chemicals, Microscopes, Safety. Hover triggers an underline or background-lightening without color shift.

**`nav-mega-menu`** — Drops from the primary nav as a white full-width panel marked at the top with a 3px amber accent stripe (`{colors.accent}`). Four columns of category links in `{typography.body-sm}` with section headers in `{typography.title-sm}` blue. A box shadow (0 4px 12px rgba(0,0,0,0.12)) lifts it off the page content.

### Category Tiles
**`category-tile`** — Photo-background tiles with a gradient overlay fading from transparent to dark blue at the bottom, where white title text sits in `{typography.title-md}`. Aspect ratio is 4/3. Hover lifts the tile with a subtle scale(1.02) transform. Used on the homepage in a grid of 6–8 tiles (two rows of three or four) for top-level departments.

### Product Card
**`product-card`** — Bordered (1px `{colors.hairline}`) card with 8px radius. Leads with a product image, then the catalog number in monospace `{typography.sku-label}` muted type — the SKU-first presentation signals B2E purchasing culture. Product name follows in `{typography.body-sm}` ink, price in `{typography.title-md}` primary-dark. Badges (`product-card-badge`, `safety-badge`, `ngss-badge`, `grade-band-badge`) stack in the upper-left corner of the image area. Hover adds shadow (0 2px 8px rgba(0,0,0,0.10)). An "Add to Cart" button appears at the card base.

### Product Table
**`product-table`** — Many Carolina products (live organisms, chemical sets, multi-unit kits) display variants in a structured table rather than a dropdown. The header row runs full primary blue with white all-caps 11px `{typography.table-header}` labels. Alternating rows use `{colors.surface-table-alt}` (#f0f4f8) for scan-reading across wide column sets (catalog number, grade level, quantity, price, availability). This is a brand-signature component with no consumer-marketplace equivalent.

### Specification Accordion
**`spec-accordion`** — Product detail pages expand specification sections (Safety Data, Living Organism Care, NGSS Alignment, Teacher Notes) via accordion panels. Title rows in `{typography.title-sm}` primary-blue with a chevron icon. Open panels render body content in `{typography.body-sm}` on `{colors.surface-soft}` background, bordered at `{colors.hairline}`. The Living Organism Care section often includes a temperature/humidity requirement table nested inside.

### Badges
**`ngss-badge`** — Institutional blue (#1565c0) pill tag reading "NGSS Aligned" in 11px bold uppercase, appearing on product cards and category filters. Signals curriculum standards compliance — a purchasing decision driver for school district buyers. **`safety-badge`** — Crimson (#b71c1c) tag for hazardous material classification. **`grade-band-badge`** — Slate (#37474f) tag for "Grades 6–8", "AP/College" etc.

### Filter Sidebar
**`filter-sidebar`** — Left-rail filter panel on category pages with checkboxes for Grade Level, Subject, NGSS Standard, Availability, Price Range, and Format. Checkbox accent uses primary blue. Collapsible sections with `{typography.title-sm}` section headers. On mobile collapses to a "Filter & Sort" drawer triggered by a sticky bottom button.

### Alerts
**`alert-info`** and **`alert-warning`** — Inline contextual messages used on product pages (e.g., "Live specimens ship Monday–Wednesday only" in amber-warning style; "Requires 2-week lead time" in blue-info style). Compact padding, 8px radius, border matches the color tone of the variant.

### Footer
**`footer`** — Dark primary-blue (#004d7a) spanning five columns: Shop by Category, Resources (teacher guides, SDS, care sheets), About Carolina, Customer Service, and Contact. A 3px amber border-top ties back to the accent system. Link color is a lightened blue (#99c3e0) for legibility on dark background. Heading labels in white `{typography.title-sm}`. A sub-footer strip carries copyright, accreditation logos, and regulatory compliance notes.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar spans full width below collapsed hamburger nav; filter sidebar becomes bottom-sheet drawer; product table scrolls horizontally with sticky first column (SKU); utility nav collapses to icon-only row |
| Tablet | 744–1128px | Two-column product grid; mega-menu replaced with slide-out drawer nav; filter sidebar toggleable panel overlay; category tiles shift to 2×3 grid |
| Desktop | 1128–1440px | Three-column product grid with left filter sidebar; full mega-menu; two-tier nav fully visible; homepage hero plus six category tiles in 3×2 |
| Wide | > 1440px | Four-column product grid; content max-width 1400px centered with wider gutters; hero expands but headline remains left-anchored |

### Touch Targets
- All interactive controls (buttons, checkboxes, accordion toggles, nav links) target minimum 44×44px hit area on mobile
- Product card "Add to Cart" button spans full card width on mobile for easy thumb access
- Accordion rows expand touch area to full row width, not just the chevron icon
- Quantity stepper inputs use large +/− buttons (44px min) to prevent mis-tap on dense order forms

### Collapsing Strategy
- Top utility bar collapses completely below 744px — phone number and account links move into hamburger menu
- Mega-menu navigation converts to a hierarchical drawer (root categories → subcategories) on tablet and below
- Filter sidebar hides off-canvas; "Filter (n)" sticky button at viewport bottom triggers full-height drawer
- Product specification tabs collapse to a stacked accordion list on mobile
- Data tables become horizontally scrollable containers with the SKU/name column sticky-left
- Homepage category tile grid reflows: 3×2 desktop → 2×3 tablet → 1×6 mobile with reduced image height (landscape→square crop)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are estimates** — the live site returned zero extracted colors (likely dynamic JS token injection or anti-bot protection). Primary blue (#0066a4), accent amber (#e07b00), and all derived tints are inferred from documented brand presence and institutional science education conventions; verify against actual CSS variables or brand guidelines before shipping.
- **Typography stack unverified** — no font-family stacks were extracted. The spec defaults to Helvetica Neue / Arial system sans-serif; the live site may use a licensed typeface (e.g., a web-licensed humanist sans). Inspect computed styles on carolina.com to confirm.
- **Exact button radii unknown** — 4px (`{rounded.sm}`) is estimated from the conservative, catalog-era aesthetic; actual values may be 0px (fully square) or up to 6px.
- **Primary brand color ambiguity** — some Carolina materials show a slightly greener teal-blue rather than royal blue. The exact primary should be sampled directly from the logo SVG or CSS.
- **Checkout and account flows** — no data on cart, checkout, order history, or account dashboard design patterns; these may differ significantly from the marketing/catalog surface.
- **Mobile nav pattern** — whether the mobile nav uses a hamburger drawer, bottom tab bar, or hybrid could not be determined without live rendering.
- **Price display format** — volume pricing tiers, unit-of-measure display, and "Request a Quote" flow styling are not captured here and are likely significant for the B2E purchase context.
- **Living specimen product page template** — care instruction layout, shipping calendar widget, and live-animal disclaimer styling are brand-signature elements that could not be modeled without live extraction.
