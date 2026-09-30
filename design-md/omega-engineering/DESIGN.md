---
version: alpha
name: "Omega Engineering"
source_url: "https://www.omega.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sixty-plus years of selling thermocouples and data-acquisition hardware to engineers has left a clear visual fingerprint — dense part-number grids, parametric filter columns, and a signature red that reads like a warning indicator on the instruments Omega actually makes. The brand's primary hue sits in the high-energy red zone (estimated #cc0000 family based on widely documented logo usage), wielded with the same confidence that safety-critical hardware demands: it marks every primary CTA, every category header, and the iconic Ω wordmark itself. Everything else steps back to make room for specifications: a near-white canvas ({colors.canvas}), cool mid-gray type ({colors.body}), and a navy structural tone ({colors.navy}) borrowed from ISO technical documentation. There is no decorative radius or soft-pill aesthetic here — buttons are close to square ({rounded.xs}), cards sit on hairline-bordered rectangles, and tables collapse to as many columns as the viewport can hold before the user manually scrolls. Typography is a utilitarian sans — Arial or Helvetica fallback is plausible given the site's anti-bot blocking — with condensed caption variants to squeeze model numbers into narrow cells. The product catalog is the UI; the brand's entire hierarchy exists to get an engineer from product category to PDF datasheet to part-number checkout in the fewest possible clicks. Badge systems carry heavy semantic weight: RoHS compliance markers, ISO-9001 seals, and expedited-shipping flags each have persistent positions on product cards. Spacing is tight by consumer standards — {spacing.sm} internal card padding, {spacing.base} column gutters — reflecting a catalog that must show 40-plus attributes per product without pagination. Color temperature skews cold and neutral outside the primary red, reinforcing the instrument-lab aesthetic rather than aspirational lifestyle.

colors:
  primary: "#cc0000"
  primary-active: "#a30000"
  primary-disabled: "#e8a0a0"
  primary-hover: "#b30000"
  navy: "#1a2b4a"
  navy-light: "#2e4470"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-table-alt: "#f9f9f9"
  on-primary: "#ffffff"
  on-navy: "#ffffff"
  warning: "#e67e00"
  success: "#2e7d32"
  compliance-green: "#4caf50"
  link: "#0057a8"
  link-hover: "#003d7a"
  part-number-bg: "#f0f4f8"
  alert-red: "#cc0000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  spec-value:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.2px
  category-label:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, 'Liberation Sans', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
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
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 10px
    height: 36px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.nav-link}"
    height: 44px
    paddingHorizontal: "{spacing.lg}"
  nav-bar-top:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 36px
    borderBottom: "1px solid {colors.hairline}"
  nav-category-mega:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline-soft}"
    aspectRatio: "1 / 1"
    maxHeight: 180px
  product-card-part-number:
    textColor: "{colors.primary}"
    typography: "{typography.part-number}"
    backgroundColor: "{colors.part-number-bg}"
    padding: "2px {spacing.xs}"
    rounded: "{rounded.xs}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    headerBg: "{colors.navy}"
    headerText: "{colors.on-navy}"
    altRowBg: "{colors.surface-table-alt}"
    cellPadding: "6px 10px"
  spec-table-header:
    typography: "{typography.title-sm}"
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    padding: "8px 10px"
  parametric-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    width: 240px
    sectionHeaderBg: "{colors.navy}"
    sectionHeaderText: "{colors.on-navy}"
    sectionHeaderTypography: "{typography.category-label}"
  compliance-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.xs}"
    iconColor: "{colors.compliance-green}"
  shipping-badge:
    backgroundColor: "#fff8e1"
    textColor: "{colors.warning}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px {spacing.sm}"
    border: "1px solid {colors.warning}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    minHeight: 300px
    padding: "{spacing.xxl} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    hoverBorderColor: "{colors.primary}"
    iconColor: "{colors.primary}"
    padding: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.link}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    buttonBg: "{colors.primary}"
    buttonColor: "{colors.on-primary}"
    buttonWidth: 80px
  datasheet-cta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    iconColor: "{colors.primary}"
  part-number-tag:
    backgroundColor: "{colors.part-number-bg}"
    textColor: "{colors.navy}"
    typography: "{typography.part-number}"
    rounded: "{rounded.xs}"
    padding: "4px {spacing.sm}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.body-sm}"
    linkColor: "#a0b8d8"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xl}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    typography: "{typography.caption-bold}"
    activeBg: "{colors.primary}"
    activeColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    itemSize: 32px

## Components

### Buttons

**`button-primary`** — Solid red (`{colors.primary}`) with all-caps white label at 14px bold weight, 2px radius, 40px tall. Hover darkens to `{colors.primary-hover}`; disabled bleeds to `{colors.primary-disabled}`. This is the "Add to Cart" and "Get Quote" workhorse — always uppercase, never pill-shaped.

**`button-secondary`** — White fill with a 1px red border and red uppercase text. Used alongside primary for secondary actions like "Compare" or "Save to List." Hover fills with `{colors.surface-soft}` and deepens border to `{colors.primary-active}`.

**`button-navy`** — Navy-filled variant (`{colors.navy}`) used in hero banners and section headers where the red primary would clash with the dark background. Same height and uppercase type treatment as primary.

**`button-ghost`** — Transparent background with link-blue text, used inline within spec tables and download rows where a full button is too heavy. No border.

### Navigation

**`nav-bar`** — Two-tier structure: a slim `{colors.canvas}` utility bar across the top for account, cart, and phone-number display, then the primary navy bar (`{colors.navy}`) at 44px housing the Ω logo, mega-menu categories, and search. Category labels are bold 13px white. The mega-menu (`nav-category-mega`) drops below with a hairline border and subtle shadow, organizing hundreds of subcategories into labeled columns.

**`nav-category-mega`** — Full-width flyout on white canvas, subdivided by product family. Section headers use `{typography.category-label}` in uppercase to separate Temperature, Pressure, Flow, Data Acquisition, etc. Dense, 3–5 column layouts with no imagery — purely text links and icon glyphs.

### Search

**`search-bar`** — Rectangular input field with a right-anchored red submit button labeled "SEARCH." Keyword, part-number, and model-number search all funnel through the same control. On the catalog pages a separate `parametric-filter` sidebar refines results by measurement range, connector type, accuracy class, and material — rendered as stacked accordion sections with navy headers.

### Product Card

**`product-card`** — Hard-edged rectangle, hairline border, no border-radius. Stacked layout: square image in `{colors.surface-soft}`, product title in `{typography.title-sm}`, then a `part-number-tag` in monospace. Price sits below the part number in bold red. Compliance badges (`compliance-badge`) cluster at the card bottom. Hover lifts a 2px red left-border accent rather than a shadow, consistent with the brand's flat technical aesthetic.

**`product-card-part-number`** — Monospace type on light blue-gray tint (`{colors.part-number-bg}`), visually distinct from prose copy. Engineers scan for model numbers first; the contrast ensures immediate legibility.

### Spec Table

**`spec-table`** — Full-bleed table with a navy header row (`{colors.navy}` background, white `{typography.title-sm}` labels) and alternating white / `{colors.surface-table-alt}` data rows. Attribute names left-aligned in `{typography.body-sm}` bold; values right-aligned in `{typography.spec-value}` monospace. No padding generosity — 6px vertical, 10px horizontal — because 20+ row tables are standard.

### Parametric Filter

**`parametric-filter`** — Fixed 240px left column on catalog pages. Navy accordion headers with `{typography.category-label}` reveal checkbox or range-slider controls below. Active filters display as dismissible red chips above results. Filter apply is immediate (no separate button) on desktop; on mobile it becomes a full-screen modal triggered by a "Filter" button.

### Badges

**`compliance-badge`** — Small bordered pill for RoHS, CE, UL, and ISO marks. Hairline border, muted gray label, green checkmark icon. Multiple badges stack horizontally on product cards.

**`shipping-badge`** — Amber background, warning-orange text for "In Stock / Ships Same Day" messaging. Positioned top-right of product card image.

### Hero Banner

**`hero-banner`** — Dark navy fill, white display type, minimum 300px tall. Used on homepage and category landing pages to present product family messaging. CTA renders as `button-primary` (red on navy). No gradient, no photographic treatment by default — the navy is flat and authoritative, like an instrument panel legend.

### Datasheet CTA

**`datasheet-cta`** — Light gray button with a PDF icon in `{colors.primary}` and link-blue label text. Appears in product detail sidebars and spec table footers. Engineers expect datasheet access at every product touchpoint; this component appears consistently below the add-to-cart zone.

### Footer

**`footer`** — Navy background matching `{colors.navy}`, 5-column layout on desktop with category quick-links, technical support phone number, ISO certification mark, and newsletter signup. Link color is desaturated blue (`#a0b8d8`) rather than white, reducing visual noise against the dark background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column catalog, parametric filter moves to full-screen modal, spec tables scroll horizontally, nav collapses to hamburger with accordion category tree |
| Tablet | 744–1128px | Two-column product grid, filter sidebar collapses to a slim 180px panel or toggleable overlay, mega-menu becomes single-column dropdown |
| Desktop | 1128–1440px | Three-column product grid, full 240px parametric filter sidebar, two-tier nav bar at full width, spec tables fully visible |
| Wide | > 1440px | Four-column product grid, content container max-width at 1400px, side margins fill with canvas white, footer columns gain breathing room |

### Touch Targets

- All interactive controls minimum 44×44px on mobile, including filter checkboxes which gain padding to 32px height
- Part-number tags have no interactive state on mobile; tap navigates to product detail directly from card
- Accordion filter headers use full-width tap targets, not just the label
- Cart and account icons in mobile nav minimum 48px hit areas

### Collapsing Strategy

- Parametric filter sidebar converts to a floating modal triggered by a fixed "Filter (N)" button that shows active-filter count in red
- Spec tables that exceed 5 columns on mobile collapse to a key-specs summary (top 4 attributes) with an expandable "Full Specifications" toggle
- The mega-menu flattens into a hamburger drawer with single-level category list, sub-items indented rather than columned
- Hero banners reduce to 200px tall on mobile with title capped at `{typography.display-sm}`
- Breadcrumb truncates intermediate nodes with "…" keeping only root and current page on narrow screens

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex values are estimated from general brand knowledge** — the live site returned HTTP 403 (Access Denied) and no colors, fonts, or theme-color were extracted. The `{colors.primary}` red (#cc0000) is consistent with widely observed Omega logo usage but should be verified against the actual brand style guide.
- **Font stack unconfirmed** — Omega's actual web font could be a licensed sans-serif (Roboto, Open Sans, Source Sans) behind bot-detection. The Arial fallback stack is a safe default for an industrial B2B site but must be replaced once the live CSS is inspectable.
- **Exact nav bar height and spacing** — two-tier nav dimensions are estimated from comparable industrial catalog sites; actual pixel values require a live DOM inspection.
- **Product card layout variants** — Omega's catalog likely has list-view and grid-view toggles with different spec display densities; only the grid card is specified here.
- **Color scale depth** — no pressed, focus-ring, or skeleton-loading variants were extractable. The `primary-disabled` and surface tokens are interpolated estimates.
- **Dark mode / high-contrast mode** — unknown whether Omega's site supports either; omitted from this spec.
- **Iconography style** — icon set (outline vs. filled, stroke weight) is undocumented without live asset access.
