---
version: alpha
name: "Edmund Optics"
source_url: "https://www.edmundoptics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Thirty-thousand SKUs organized by wavelength, coating type, and numerical aperture — Edmund Optics treats its catalog as a precision instrument, building a site where specification tables carry more visual weight than lifestyle photography ever could. The canvas is clinically white against an ink confirmed at #313131, every surface tuned to reduce cognitive load for the engineer who needs an N-BK7 plano-convex lens at 1064 nm by Thursday. The primary red — a saturated crimson deeply embedded in the brand's identity — fires on every add-to-cart and quote-request CTA, standing out sharply against the white grid without competing with the dense technical content surrounding it. Navigation spreads wide in a mega-menu organized by optical family: Lenses, Mirrors, Beamsplitters, Filters, Fiber Optics, Optomechanics — each family subdivided by substrate and coating until the taxonomy reads like a reference map of photonics itself.

  Typography runs entirely on the system stack — no custom typeface was detectable under extraction — which is quietly appropriate for a brand whose audience uses the same sans-serif on their CAD software and lab instrumentation GUIs. Type weight carries the hierarchy: part numbers appear in monospaced or tight-tracking styles at small sizes inside dense tables, while section headers hold just enough weight to orient the eye without claiming editorial prominence. Corners are modest and practical, not expressive: product cards use a 4px radius, buttons round to 6px, nothing approaches pill geometry. The whole system reads like a well-formatted IEC datasheet coaxed into a responsive layout — dense, purposeful, and uninterested in decoration for its own sake. Stock indicators, lead-time callouts, and quantity-pricing tiers are first-class UI elements rather than footnotes, because for a specifying engineer those constraints determine whether a design is even buildable. A dark near-black nav bar anchors the top of long specification pages, staying visible as users scroll through optical-system configurators that can extend several dense viewport-heights.

colors:
  primary: "#cc2029"
  primary-active: "#a51821"
  primary-disabled: "#e8a4a7"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  muted-soft: "#9e9e9e"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-nav: "#2a2a2a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#0057a8"
  link-hover: "#003d78"
  spec-row-alt: "#f9f9f9"
  stock-in: "#2e7d32"
  stock-low: "#e65100"
  stock-out: "#b71c1c"
  tag-new: "#0057a8"
  tag-sale: "#cc2029"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  table-header:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
    height: 40px
  button-primary-active:
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    border: "1px solid {colors.primary}"
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
  button-quote:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    border: "1px solid {colors.link}"
    height: 40px
  cad-download-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.link}"
    padding: 6px 12px
    icon: download
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 36px
    focusBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    searchButtonBackground: "{colors.primary}"
    searchButtonColor: "{colors.on-primary}"
    searchButtonRounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 52px
    padding: "0 {spacing.xl}"
  nav-top-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    categoryHeaderTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    columnGap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.canvas}"
    padding: "{spacing.base}"
    partNumberTypography: "{typography.part-number}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    hoverBorder: "1px solid {colors.ink}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    altRowBackground: "{colors.spec-row-alt}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.spec-value}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    cellPadding: "6px 12px"
  quantity-pricing-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    altRowBackground: "{colors.spec-row-alt}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  part-number-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.part-number}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.hairline}"
  stock-indicator-in:
    textColor: "{colors.stock-in}"
    typography: "{typography.caption}"
  stock-indicator-low:
    textColor: "{colors.stock-low}"
    typography: "{typography.caption}"
  stock-indicator-out:
    textColor: "{colors.stock-out}"
    typography: "{typography.caption}"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    optionTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    width: 240px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  tag-new:
    backgroundColor: "{colors.tag-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  tag-sale:
    backgroundColor: "{colors.tag-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    itemSize: 32px
  hero-banner:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary action button uses brand red ({colors.primary}) at 40px tall with {rounded.sm} corners and {typography.button-md} at weight 600. It drives add-to-cart and stock-order flows; the active state darkens to {colors.primary-active} on press, and the disabled state mutes to {colors.primary-disabled}. Corners stay geometric at 4px — the brand has no interest in pill softening.

**`button-secondary`** — A {colors.primary}-bordered outlined variant on a white ground, preserving the red accent while signaling a secondary action. Appears alongside `button-primary` on product pages when both cart and quote paths are available. Padding mirrors the primary at 9px 19px (1px inset for the border).

**`button-ghost`** — A frameless label-only button in {colors.ink} for low-hierarchy interactions like "View All", "Clear Filters", or section-level navigation inside long pages. No border, no fill; weight-600 label provides enough scan-weight.

**`button-quote`** — Mirrors `button-secondary` in shape but uses {colors.link} blue to distinguish quote-request actions from direct-cart purchases. Engineers frequently need volume quotes before finalizing BOMs; the blue separates that workflow from the red purchase path visually without requiring explanatory text.

**`cad-download-button`** — A compact {colors.link}-bordered button at 6px 12px padding with a download icon, used inline in product datasheets to trigger CAD model, drawing, or test data downloads. Smaller than standard buttons to sit comfortably within dense specification panels without dominating.

### Search

**`search-bar`** — The global search field is calibrated for part-number lookup as the primary mode: placeholder text cues "Search by Part #, Keyword, or Item #." A {colors.primary} submit button with {rounded.sm} corners attaches to the right edge. At mobile breakpoints the bar stretches full-width and the submit button stacks below or overlaps as an icon-only orb.

### Navigation

**`nav-bar`** — A near-black ({colors.surface-nav}) bar at 52px sits below a thinner `nav-top-strip` in {colors.ink} carrying account links, phone number, and international selectors. White {typography.nav-link} labels at weight 600 and 14px. Hover triggers a bottom-border underline accent in {colors.primary} rather than a background fill, keeping the bar visually quiet.

**`mega-menu`** — Opens on hover over top-level optical families — Lenses, Mirrors, Imaging Systems, Laser Optics, Fiber Optics, Optomechanics, Life Sciences — as a full-width white panel on {colors.canvas}. Categories arrange in four to six columns, each headed by a {typography.title-sm} weight-600 label followed by {typography.body-sm} subcategory links. No imagery or editorial features appear in the menu: it is pure taxonomy, reflecting catalog depth over curation.

### Product Components

**`product-card`** — A 1px-hairline-bordered card with a white padded image region, part number in {typography.part-number} monospace above the descriptive title, and price in {typography.price-display} red at the bottom. Hover sharpens the border from {colors.hairline} to {colors.ink}. Images sit padded within a white square rather than full-bleed, because optical components photograph against white for accurate substrate and coating representation.

**`spec-table`** — The dominant visual pattern on product detail pages. Column headers use {typography.table-header} all-caps at 12px with 0.4px tracking; cell values use {typography.spec-value} at 13px. Alternating rows use {colors.spec-row-alt} against {colors.canvas}, with 1px {colors.hairline} row separators for dense grids covering dozens of parameters: focal length, surface quality, wavefront error, coating bandwidth, damage threshold. Zero border-radius — a hard-edged table reads as consistent with datasheet convention.

**`quantity-pricing-table`** — Appears below the main spec block showing per-unit price tiers at 1, 5, 10, 25, 50, and 100 units. Identical visual language to `spec-table`: {colors.surface-soft} header row, {colors.spec-row-alt} alternating rows, {typography.body-sm} cells. Engineers reference this during design-phase BOM costing before committing to a production run.

**`part-number-badge`** — An inline chip on {colors.surface-soft} with a hairline border carrying the part number in {typography.part-number} monospace, used in search results, comparison tables, cross-reference blocks, and accessory callouts. Makes scannable IDs visually distinct from descriptive prose at a glance.

**`stock-indicator-in`** / **`stock-indicator-low`** / **`stock-indicator-out`** — Three semantic availability states rendered as colored inline text next to quantity steppers: green {colors.stock-in} for in-stock, orange {colors.stock-low} for limited quantity, red {colors.stock-out} for backorder. All use {typography.caption} at 12px with no badge background — the color signal alone carries the message without adding visual noise to an already information-dense page.

**`filter-panel`** — A 240px left-column panel that bleeds into the page background with no card border. Facet group labels use {typography.spec-label} all-caps at 12px; checkbox options use {typography.body-sm}. Facets reflect actual engineering parameters: wavelength range, substrate material, coating type, diameter tolerance, numerical aperture, surface flatness — not marketing categories.

### Hero

**`hero-banner`** — Full-width campaign banners use the dark near-black {colors.surface-nav} as background with white reversed type, giving homepage features a subdued, institutional energy rather than a consumer-retail brightness. Heading at {typography.display-xl}, body at {typography.body-md}, single red CTA. Product imagery when used appears against white rather than styled lifestyle contexts.

### Footer

**`footer`** — Dark {colors.ink} background with {colors.on-dark} body text and {colors.hairline-soft} link color. Four to five columns cover Products, Resources, About Edmund Optics, International distributors, and contact information including regional phone numbers. The register of international offices — Americas, Europe, Asia — signals a global scientific and industrial customer base that the design does not try to obscure.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces mega-menu with side-drawer accordion; search bar full-width; spec tables horizontally scroll; filter panel collapses behind sticky "Filter & Sort" bar |
| Tablet | 744–1128px | Two-column product grid; mega-menu compresses to two columns or converts to overlay drawer; filter panel collapses to modal |
| Desktop | 1128–1440px | Three- or four-column grid; full six-column mega-menu; left-rail filter panel fixed at 240px alongside results |
| Wide | > 1440px | Max-width container (~1400px) centers content; additional whitespace flanks the grid; product columns stay at four |

### Touch Targets

- All primary and secondary buttons minimum 40px height
- Filter checkboxes padded to 40px touch area with visible 2px focus ring in {colors.primary}
- Part-number badges tappable at minimum 32px height in mobile list views
- Quantity steppers minimum 36px × 36px to avoid misfire on precision-quantity entry
- Pagination items minimum 32px × 32px with 4px gaps

### Collapsing Strategy

- Mega-menu converts to a side-drawer at < 1128px with accordion-expanded optical families; depth preserved, layout linearized
- Specification tables scroll horizontally rather than reflowing — column alignment is essential for multi-parameter comparison and must not be sacrificed for narrower viewports
- Left-rail filter panel transitions to a modal overlay at < 1128px triggered by a sticky "Filter & Sort" bar pinned above results
- Breadcrumbs truncate middle segments with ellipsis when hierarchy depth exceeds three levels on narrow viewports
- Quantity-pricing tiers collapse to a "View Volume Pricing" expandable row at < 744px to reduce page height on mobile product pages
- `nav-top-strip` collapses or hides at mobile, surfacing only phone number and account icon

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site — the page returned an anti-bot challenge ("Just a moment...") blocking full palette extraction; all colors except {colors.ink} are based on brand-knowledge approximation and may not match current production tokens
- Primary red (#cc2029) is an approximation; the exact Edmund Optics brand hex was not confirmed from live extraction and may differ from the crimson registered in their brand identity system
- No custom typeface was detected; the site appears to use the system sans-serif stack, but a licensed web font may be loaded via JavaScript or a webfont CDN not captured by the crawler
- Exact button radii, input heights, and spacing values are inferred from technical B2B conventions rather than measured from live DOM computed styles
- Dark mode or high-contrast accessibility variant (if any) not assessed
- International site variants (EU, Japan, China, India) may carry localized typography, currency formatting, or layout patterns not modeled here
- Configurator and optical-design-tool UI patterns — custom coating request flows, Zemax/OpticStudio integration pages, optical system builders — are not modeled and may introduce distinct component patterns
- CAD/drawing viewer component styling (used for downloadable product drawings) not assessed
