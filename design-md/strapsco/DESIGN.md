---
version: alpha
name: "StrapsCo"
source_url: "https://www.strapsco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  At 22mm, 20mm, and 18mm, the lug-width filter dominates StrapsCo's navigation hierarchy before a brand name is ever read — a catalog-first stance that positions the site as a precision parts shop rather than a lifestyle boutique. The palette enforces this reading: deep royal blue (#003399) anchors every primary CTA and category header, evoking instrument panels and technical schematics, while orange (#f58220) fires as a high-contrast accent the way a luminous index sits on a dive bezel. Dark slate (#353c4e) frames the navigation bar like a brushed-steel case back — functional and dense. Typography draws entirely from system fonts — Inter and Helvetica Neue — with no bespoke typeface investment; dimensional accuracy (lug width, strap thickness, material composition) is the brand's primary language, not editorial warmth. Surfaces stay neutral: off-white canvases (#f2f2f2, #fafafa) with hairlines in muted gray (#ccc9c9, #d9d9d9) keep photography and strap color swatches as the dominant visual signal. Button geometry favors modest rounding ({rounded.sm}) over the pill shapes lifestyle brands prefer — corners here are working edges, not friendly gestures. Filter sidebars and compatibility selectors are structurally the most prominent UI surfaces, organized around variables a collector actually uses: lug width, case brand, material, buckle type. Error states and discount flags appear in red (#e53e3e), cleanly separated from both blue and orange so no state signal reads ambiguously. The overall interface reads like a well-indexed technical reference — structured, dense with specification, and built for a customer who arrives already knowing the exact millimeter measurement of their watch case.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aacc"
  ink: "#222222"
  body: "#32373c"
  muted: "#7d7a7a"
  hairline: "#ccc9c9"
  hairline-soft: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#f2f2f2"
  surface-mid: "#ececec"
  on-primary: "#ffffff"
  accent: "#f58220"
  accent-active: "#d46a10"
  nav-bg: "#353c4e"
  nav-text: "#ffffff"
  error: "#e53e3e"
  error-dark: "#cf2e2e"
  muted-blue: "#abb8c3"
  dark-gray: "#4f4d4d"
  near-black: "#111111"

typography:
  display-xl:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "none"
  nav-bar-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md}"
    imageAspect: "4/3"
  lug-width-badge:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  material-tag:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  accent-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    groupPadding: "{spacing.base} {spacing.lg}"
    width: 260px
  size-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 34px
  size-chip-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 34px
  swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 400px
  compatibility-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    inputTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
    size: 36px
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.muted-blue}"
    linkColor: "{colors.nav-text}"
    headingTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Royal blue (#003399) fill with white text and {rounded.sm} corners at 44px height. Hover deepens to #002277 with no shape change; disabled state washes the background to #99aacc while preserving white text. The definitive Add to Cart and checkout action button across all pages.

**`button-secondary`** — White background with a 1px royal blue border and blue text, same 44px height as primary for alignment parity on product pages. Used for secondary catalog actions like Add to Wishlist, Compare, or Save for Later.

**`button-accent`** — Orange (#f58220) fill with white text, reserved for promotional contexts — Sale events, limited-run collection CTAs, and bundle offers. The heat signal is deliberate: orange appears only where urgency or discount is present, never as a default navigation element.

**`button-ghost`** — Hairline-bordered neutral button (transparent fill, {colors.body} text) for low-weight actions like Reset Filters, Clear All, or View More in paginated lists. Visually recedes on white canvas.

### Navigation
**`nav-bar`** — Dark slate (#353c4e) header bar at 60px height; the contrast against white page body creates a strong instrument-panel reading. Links are 14px Inter weight 500 in white. On desktop a mega-menu surfaces category columns (by material, by lug width, by brand); on mobile the bar collapses to a hamburger drawer with accordion sub-navigation.

**`nav-bar-secondary`** — A 40px off-white strip below the primary nav carries category breadcrumbs or filter shortcuts. 13px body-sm in {colors.body} with a hairline bottom border. Acts as a wayfinding rail on deep catalog pages.

**`promo-bar`** — Full-width royal blue strip pinned above the primary nav at 36px, carrying site-wide messaging (free shipping threshold, discount codes) in 13px white body type. Includes a dismiss icon at the right edge on mobile.

### Product Card
**`product-card`** — White card with 1px hairline-soft border and {rounded.sm} corners. The image occupies a 4:3 aspect ratio slot. Below the image: a dark slate lug-width badge (e.g., "20MM"), product title in 16px semibold, material tag in 11px uppercase gray, and price in 18px bold. Sale items receive a red badge (#e53e3e) positioned absolute top-right on the image thumbnail. Cards sit in a 3-column grid on desktop, 2-column on tablet, 1-column on mobile.

### Filters & Specification
**`filter-sidebar`** — Left-rail panel at 260px on desktop, collapsing to a full-height bottom-sheet drawer on mobile. Group headers use `spec-label` type (11px, uppercase, 0.5px letter-spacing) in dark gray with hairline dividers between groups. Lug width is the primary group and renders as size chips; material, case brand, color, and buckle type follow as checkbox lists in 13px body-sm. The sidebar never uses rounded corners — edges are flush with the grid.

**`size-chip` / `size-chip-selected`** — Compact, 4px-radius chips for lug-width selection (16mm through 26mm in 2mm increments). Default state: light gray (#f2f2f2) fill, body-color text, hairline border. Selected state: royal blue fill, white text, blue border. 34px height; chips wrap into two rows when more than six options are shown.

**`compatibility-selector`** — A structured input panel on the PDP (and optionally as a site-wide finder widget) allowing the customer to choose their watch brand, model, and lug width to verify strap fit. Rendered in off-white (#fafafa) with hairline border, spec-label group headings, and dropdown inputs in 15px body-md.

### Badges
**`lug-width-badge`** — Small dark slate (#353c4e) chip with white uppercase 11px text. Appears on product cards and PDP thumbnails to surface lug width without requiring a dropdown interaction. This is the most visually prominent badge type — reinforcing the catalog's dimension-first logic.

**`material-tag`** — Light gray (#ececec) chip with uppercase body text denoting material category (Leather, Rubber, NATO, Metal, Canvas). Sits beneath the product title on cards and clusters horizontally on the PDP.

**`sale-badge`** — Red (#e53e3e) badge positioned absolute top-right on product card images. Short uppercase label: "SALE" or a percentage string. Clear chromatic separation from both blue and orange ensures no confusion with primary or accent signals.

### Hero & Collection Banner
**`hero-banner`** — Full-width dark slate (#353c4e) band at minimum 400px height desktop. Title renders in 36px bold Inter in white; supporting body copy at 15px regular. Button row places primary (blue) and accent (orange) CTAs inline — typically "Browse All Straps" alongside a sale or new-arrival action. Collection heroes swap the dark slate for photography with an overlay gradient; text treatments remain white.

### Footer
**`footer`** — Dark slate (#353c4e) background with muted blue-gray (#abb8c3) body text and white link text. Column headings use spec-label style (uppercase 11px, weight 600). Four columns on desktop: Shop (by material, by lug width, by brand), Help (sizing guide, FAQ, returns), Company (about, blog), and Social icons. Collapses to stacked accordion sections on mobile with chevron toggles.

### Pagination
**`pagination`** — Row of numbered page chips at 36px, {rounded.xs} corners. Active page: royal blue fill, white text. Inactive: transparent with hairline border and body-color text. Previous/Next arrows flank the number row. Sits below product grids and search results.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes full-height bottom-sheet drawer; nav collapses to hamburger accordion; hero min-height 260px; promo bar persists; size chips wrap to two rows |
| Tablet | 744–1128px | Two-column product grid; filter sidebar collapses to horizontal top-of-grid filter strip with dropdowns; nav shows primary category labels only |
| Desktop | 1128–1440px | Three-column product grid with 260px left-rail filter sidebar; full nav with mega-menu on hover; compatibility finder widget visible in sidebar |
| Wide | > 1440px | Four-column product grid; max-width 1400px container centered; nav and footer increase horizontal padding; hero padding scales up |

### Touch Targets
- All buttons minimum 44px height per spec; `size-chip` minimum 34px height padded to 44px tap area on mobile
- Swatch visual size 24px but touch target padded to 32×32px via transparent inset
- Filter checkbox rows minimum 44px full-row tap area regardless of visible element height
- Hamburger menu link rows minimum 44px height in mobile drawer
- Pagination chips minimum 44px touch area on mobile via padding expansion

### Collapsing Strategy
- Filter sidebar → full-height bottom-sheet drawer triggered by a sticky "Filters" bar above the product grid
- Mega-menu → hamburger drawer with first-level links and expandable accordion sub-groups
- Four-column footer → stacked accordion with chevron toggles; columns expand/collapse independently
- Compatibility selector → moves from sidebar to a collapsible inline banner above the product grid on tablet/mobile
- Promo bar remains pinned on all breakpoints with a right-edge dismiss icon; re-appears on page refresh unless cookie is set

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface found; entire type system resolves to system stack (Inter / Helvetica Neue / Arial) — any proprietary weights or optical sizing variants are unverified
- Many extracted hex values (#f78da7, #7bdcb5, #fcb900, #ff6900, #0693e3, #9b51e0, #00d084, #8ed1fc, #357b49, #007a33, #551144) match WordPress Gutenberg block editor palette defaults verbatim — these are excluded from the design system as framework artifacts, not brand tokens
- Meta theme-color is unset; no PWA or browser chrome color signal available
- Exact computed border-radius values and button padding cannot be confirmed without live CSS inspection — values above are inferred from visual category norms
- Hover/focus ring styles and transition durations (drawer easing, card hover lift) not extractable from static extraction hints
- Mega-menu structure and column organization inferred from category depth typical of high-SKU watch strap catalogs — actual nav schema unverified
- Accent orange (#f58220) usage split between promotional and informational contexts is assumed; exact trigger rules unconfirmed
- Whether #003399 or #003388 (both appear in extraction) is the canonical primary blue is ambiguous — #003399 used here as the more saturated signal
