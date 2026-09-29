---
version: alpha
name: "Fisher & Paykel"
source_url: "https://www.fisherpaykel.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Stainless steel rendered as negative space — Fisher & Paykel's digital presence mirrors the flush-mount panels and handle-free facades of its appliance hardware, where every pixel of whitespace is as deliberate as a 2mm panel gap. The brand's signature blue (#006ebe) appears only at decision moments — primary CTAs, active navigation states, configurator selections — functioning like the single illuminated control dial on an otherwise featureless appliance face. Typography runs through Clarity City, a geometric sans-serif with open counters and uniform stroke width that echoes engineering draftsmanship, paired with Gotham for display headings where architectural weight is needed. The near-black ink (#1e1e1c) sits against vast expanses of #f7f7f7 canvas, creating a gallery-like reading environment where full-bleed product photography dominates. Corners are kept deliberately sharp — `{rounded.none}` on inputs, `{rounded.xs}` on buttons — because this is a brand built on precision tolerances, not friendly curves. The spacing system breathes generously: `{spacing.section}` of 64px between content blocks creates the visual equivalent of the negative space inside a column refrigerator. A secondary red (#c20012) surfaces for alerts and promotional urgency, while #008827 marks energy efficiency ratings — both functional signals, never decorative. The navigation is a slim 72px bar that communicates product hierarchy through mega-menus rather than crowding the top rail, and product cards present themselves as architectural elevations: flat, shadowless rectangles with spec-sheet precision in their typography. The color palette deliberately avoids warmth — no amber, no cream, no earth tones — staying entirely in the blue-gray-white spectrum of professional kitchens and surgical-grade steel. `{spacing.base}` of 16px governs internal component rhythm while `{spacing.lg}` separates related content groups, maintaining the kind of systematic rigor you would expect from a brand whose physical products are measured in hundredths of a millimeter.

colors:
  primary: "#006ebe"
  primary-active: "#005a9e"
  primary-disabled: "#99c7e5"
  ink: "#1e1e1c"
  body: "#4f4f49"
  muted: "#767676"
  muted-soft: "#7e7e7e"
  hairline: "#d8d8d8"
  hairline-soft: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c20012"
  error-soft: "#fde8ea"
  success: "#008827"
  success-soft: "#e6f4eb"
  info-soft: "#cce2f2"
  warning-soft: "#fcf8e3"
  badge-promo: "#c20012"
  badge-eco: "#008827"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Gotham A', 'Gotham B', 'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham A', 'Gotham B', 'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.22
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham A', 'Gotham B', 'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0
  title-lg:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Clarity City', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid "{colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.08)"
  mega-menu-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.sm} 0"
  mega-menu-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0 {spacing.xs}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-card-eco-badge:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xxl}"
  hero-banner-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0 {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  category-tile-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  comparison-tool:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: 1px solid "{colors.hairline-soft}"
    padding: "{spacing.lg}"
  comparison-tool-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.base}"
  energy-rating-badge:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline-soft}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  search-results-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
    padding: "{spacing.sm} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    padding: "0 0 {spacing.base}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid "{colors.hairline-soft}"
    padding: "{spacing.lg} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: 1px solid "{colors.hairline}"
  tab-active:
    textColor: "{colors.primary}"
    borderBottom: 2px solid "{colors.primary}"
  tab-inactive:
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — A solid rectangle in Fisher & Paykel blue (#006ebe) with barely-there 2px corner radius and white text set in Clarity City 14px medium weight. The minimal rounding preserves the brand's engineering precision while softening just enough to avoid severity. On hover, the background deepens to `{colors.primary-active}` (#005a9e). Disabled state washes out to `{colors.primary-disabled}` (#99c7e5), maintaining shape but draining conviction.

**`button-secondary`** — An outlined variant with a 1px border in `{colors.primary}`, white fill, and blue text matching the border color. Same dimensions and typography as the primary button but communicates lower-priority actions — "Compare Models", "View Specifications", "Download Manual". On hover, the background shifts to `{colors.surface-soft}` and the border darkens.

**`button-tertiary`** — A text-only button with no background or border, rendered in `{colors.primary}`. Used for inline actions within content blocks or as "Learn more" links within product descriptions. The lack of container makes it read as refined rather than weak.

**`button-dark`** — A solid near-black (#1e1e1c) rectangle with white text, used for high-contrast CTAs against light photography or on hero banners where the brand blue would compete with the imagery. Same geometry as the primary button.

### Text Inputs
**`text-input`** — A sharp-cornered rectangle with zero border radius, reflecting the brand's precision-machined aesthetic. The border is `{colors.hairline}` (#d8d8d8) by default, transitioning to `{colors.primary}` on focus. Text is set in `{typography.body-md}` (Clarity City 16px regular). Error states switch the border to `{colors.error}` (#c20012). The placeholder uses `{colors.muted-soft}` (#7e7e7e). All inputs are 48px tall with 12px vertical / 16px horizontal padding.

### Navigation
**`nav-bar`** — A 72px-tall white bar with a subtle bottom border in `{colors.hairline-soft}` (#e7e7e7). The left side holds the Fisher & Paykel wordmark, center contains primary category links (Cooling, Cooking, Laundry, Dishwashing) in `{typography.nav-link}` (Clarity City 14px medium), and right side has utility icons (search, account, compare). On scroll, the border is replaced by a soft box-shadow for depth indication. Active nav links receive a 2px bottom border in `{colors.primary}`.

**`mega-menu`** — A full-width dropdown that opens below the nav bar with a subtle shadow, containing product category columns. Each column has a heading in `{typography.title-sm}` followed by product links in `{typography.body-sm}`. The mega-menu includes product thumbnails for featured items and uses `{spacing.xl}` (32px) internal padding with `{spacing.xxl}` (48px) horizontal margins.

### Product Cards
**`product-card`** — A borderless, shadowless rectangle — no rounded corners, no elevation — presenting the product as a flat architectural rendering. The image area uses a `{colors.surface-soft}` background with a 4:3 aspect ratio, giving products a gallery-like float. Below, the product name appears in `{typography.title-sm}` (16px medium) followed by price in `{typography.body-sm}` at `{colors.body}`. Optional badges — promotional red or eco-rating green — sit in the top-left of the image area as compact uppercase labels.

### Hero Banner
**`hero-banner`** — A full-width section on a `{colors.surface-soft}` background showcasing a hero product image alongside or behind display text. Headlines use `{typography.display-xl}` (Gotham 48px light weight with -0.5px letter spacing), creating the architectural headline style — large but weightless. The subtitle runs in `{typography.body-lg}` (18px regular) at `{colors.body}`, followed by a CTA button slightly larger than standard (52px tall). Section padding is `{spacing.section}` (64px) vertically.

### Category Tiles
**`category-tile`** — Square or landscape rectangles with full-bleed product photography and a text overlay or adjacent label in `{typography.title-md}`. No borders, no shadows, no rounded corners — tiles sit flush in a grid, separated only by `{spacing.sm}` (8px) gutters. Used on the homepage and category landing pages to direct users into product verticals.

### Specification Table
**`spec-table`** — An alternating-row data display for product specifications (dimensions, capacity, energy rating, features). Labels use `{typography.spec-label}` (12px uppercase semibold in `{colors.muted}`), values use `{typography.body-sm}` in `{colors.ink}`. Rows are separated by `{colors.hairline-soft}` borders. No background alternation — the hierarchy comes purely from typography weight differences.

### Comparison Tool
**`comparison-tool`** — A side-by-side product comparison panel with a light border and `{spacing.lg}` internal padding. Column headers show product images and names in `{typography.title-md}`, with specification rows below using the same label/value pattern as the spec table. Differences between products are highlighted with `{colors.primary}` text weight. Used for the "Compare" feature central to appliance purchasing decisions.

### Energy Rating Badge
**`energy-rating-badge`** — A compact green (#008827) pill displaying the appliance's energy star rating in uppercase `{typography.badge}`. Positioned on product cards and detail pages near the price. This is a functional signal — not decorative — communicating regulatory compliance information.

### Search
**`search-bar`** — A subtle rectangle with a 4px radius and `{colors.surface-soft}` background, bordered by `{colors.hairline-soft}`. On focus, the border transitions to `{colors.primary}`. The input uses `{typography.body-md}` and includes a magnifying glass icon on the left. Results appear in a dropdown card with `{rounded.sm}` corners and a soft box-shadow, listing product suggestions with thumbnail images.

### Footer
**`footer`** — A dark footer using `{colors.ink}` (#1e1e1c) as background with white text, creating a grounding anchor at the page bottom. Section headings use `{typography.title-sm}` in white, with link lists below in `{typography.body-sm}` at `{colors.hairline}` (#d8d8d8) — slightly muted against the dark background but still legible. Links brighten to full white on hover. Content is organized into columns: Products, Support, About, and legal/locale information. Padding is `{spacing.section}` (64px) vertically.

### Accordion
**`accordion`** — Used on product detail pages for collapsible sections (Features, Specifications, Downloads, Reviews). Each section header is `{typography.title-sm}` with a chevron icon, separated by `{colors.hairline-soft}` bottom borders. Expanded content uses `{typography.body-sm}` in `{colors.body}` with `{spacing.base}` padding. The interaction communicates state through chevron rotation only — no background change, no color shift.

### Tab Bar
**`tab-bar`** — A horizontal set of tabs used on product detail pages to switch between Overview, Features, Specifications, and Reviews. Active tabs display `{colors.primary}` text with a 2px bottom border in the same color. Inactive tabs use `{colors.muted}`. The entire bar sits above a `{colors.hairline}` 1px border. Typography is `{typography.button-md}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger with slide-out drawer; hero banner stacks image above text; product grid becomes 1-2 columns; mega-menu becomes full-screen accordion; comparison tool stacks vertically or becomes swipeable; spec table remains full-width; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows condensed links with hamburger for overflow; hero banner maintains side-by-side at reduced proportions; mega-menu appears as a contained dropdown; comparison tool shows 2 products side-by-side; category tiles in 2x2 grid |
| Desktop | 1128–1440px | Three-to-four column product grid; full nav-bar with all category links and mega-menu on hover; hero banner at full width with generous asymmetric layout; comparison tool supports up to 3 products; footer displays 4-5 columns; spec table has label-value pairs in two-column rows |
| Wide | > 1440px | Content constrained to 1440px max-width centered on canvas; product grid may expand to 4 columns; hero imagery fills available width while text remains within the content container; all other components maintain desktop behavior within the centered frame |

### Touch Targets
- All buttons maintain 48px minimum height on all breakpoints
- Nav-bar utility icons (search, account, compare) are 44x44px tap targets with adequate padding
- Accordion headers are 56px tall for comfortable mobile interaction
- Product card tap targets extend to the full card area on mobile
- Tab bar items maintain 44px minimum height with 16px horizontal padding
- Footer links have 44px vertical tap area with 8px vertical spacing between items

### Collapsing Strategy
- Primary navigation collapses to hamburger at 744px, opening a full-height slide-out drawer
- Product grid reduces from 4 to 3 columns at 1128px, to 2 at 744px, to 1 at 480px
- Hero banner switches from side-by-side to stacked at 744px
- Mega-menu converts to an accordion-based drill-down navigation on mobile
- Comparison tool limits to 2 products on tablet, becomes a swipeable carousel on mobile
- Category tiles reduce from 4 columns to 2 at 744px, with increased vertical spacing
- Footer columns collapse from 4-5 to 2 at 744px, then to 1 at 480px
- Tab bar becomes horizontally scrollable on mobile with active indicator following scroll position
- Spec table remains full-width but switches to a stacked label-above-value layout on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Clarity City font weights and optical sizes could not be verified; the extracted font-family reference confirms its presence but specific weight files (300, 400, 500, 600) are inferred from common geometric sans usage
- Gotham A / Gotham B distinction (screen-optimized vs. print variants from Hoefler & Co) suggests cloud-hosted webfonts whose exact rendering parameters could not be captured
- Animation and transition timing (hover durations, mega-menu open/close easing, accordion expand speed) could not be extracted from static analysis
- The product configurator/builder component (used for custom panel selections, handle finishes) was not captured in color/layout tokens
- Dark mode or alternate theme states are not present in the extracted data
- Focus ring styles for keyboard navigation are not documented; recommend 2px solid `{colors.primary}` with 2px offset
- Loading states (skeleton screens for product imagery, spinner for comparison tool) are not defined
- Several Bootstrap utility colors (#e83e8c, #6610f2, #6f42c1, #fd7e14, #20c997) appeared in extraction but are framework defaults, not brand tokens — excluded from the palette
- Noto Sans SC (Chinese language support) sizing and line-height adjustments for CJK typography are not captured
- Video player controls (used for product demonstration content) are not documented
- The "Where to Buy" dealer locator component and its map/pin styling are not captured
- Promotional banner bar (above nav, used for sale events) color and typography could not be reliably separated from page-level tokens
