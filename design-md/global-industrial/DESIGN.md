---
version: alpha
name: "Global Industrial"
source_url: "https://www.globalindustrial.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The search bar carries more brand identity weight at Global Industrial than any hero image could — a catalog stretching past a million SKUs demands immediate wayfinding over visual seduction, and the site's orange CTA vocabulary reads as practical emphasis rather than lifestyle signal. The experience is engineered for procurement managers and facilities buyers who arrive with a part number or a spec sheet: product cards front-load SKU codes, model numbers, unit-of-measure designations, and next-day shipping eligibility; photography is secondary to the data table beneath it. Orange — approximated here at #F47B20 from documented brand materials, exact extraction blocked by anti-bot protection; see Known Gaps — punches against white (#FFFFFF) and light-gray (#F5F5F5) surfaces as the single action hue: add-to-cart wells, request-a-quote rails, and call-out pricing banners all draw from this one signal. A navy header (#1C3A6E approximated) anchors the top chrome with account tools, cart summary, and a prominently surfaced phone number — that last detail sets the register: phone support is a first-class wayfinding element, not a legal-footer afterthought, because B2B buyers close large orders by phone. Navigation runs five and six levels deep, so breadcrumbs are implemented as a persistent landmark rather than supplemental chrome, and mega-menu columns organize hundreds of subcategories under bold navy headers. Type runs system sans-serif, an Arial-forward stack chosen for cross-OS rendering consistency in enterprise procurement environments where custom font delivery is unreliable and print-to-PDF spec sheets must degrade gracefully. Spacing is noticeably denser than consumer-web norms: filter rails at 220–240px, product grids at three to four columns with narrow gutters, and spec-detail tables packing twelve to sixteen attribute rows into a single above-the-fold viewport. Red clearance badges (#CC0000) and bold savings-dollar callouts run as a secondary urgency layer across the grid — industrial buyers scan horizontally across product rows for value signals, so badge placement at top-left of the card image is load-bearing information design rather than decoration.

colors:
  primary: "#F47B20"
  primary-active: "#D96010"
  primary-disabled: "#FBCCA0"
  navy: "#1C3A6E"
  navy-dark: "#132850"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  on-navy: "#FFFFFF"
  sale-red: "#CC0000"
  sale-red-bg: "#FFF0F0"
  success: "#2E7D32"
  sku-label: "#555555"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  sku-mono:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  price-display:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-lg:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  nav-sub:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
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
    textColor: "{colors.navy}"
    border: "1px solid {colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    buttonBackground: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.nav-link}"
    height: 48px
    topBarBackground: "{colors.navy-dark}"
    topBarHeight: 36px
    topBarTypography: "{typography.caption}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerColor: "{colors.navy}"
    typography: "{typography.nav-sub}"
    headerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspect: "1:1"
    skuTypography: "{typography.sku-mono}"
    skuColor: "{colors.sku-label}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    padding: "{spacing.sm}"
    badgePosition: top-left
  product-card-hover:
    border: "1px solid {colors.primary}"
    shadow: "0 2px 8px rgba(0,0,0,0.12)"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    hoverColor: "{colors.primary}"
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  savings-callout:
    backgroundColor: "{colors.sale-red-bg}"
    textColor: "{colors.sale-red}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.sale-red}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackground: "{colors.navy}"
    headerTextColor: "{colors.on-navy}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    stripeBackground: "{colors.canvas}"
    rowHeight: 36px
    rounded: "{rounded.xs}"
  bulk-pricing-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.navy}"
    headerTextColor: "{colors.on-navy}"
    headerTypography: "{typography.caption}"
    priceTypography: "{typography.price-sm}"
    borderColor: "{colors.hairline}"
    highlightBackground: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  add-to-cart-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    qtyInputBackground: "{colors.canvas}"
    qtyInputBorder: "1px solid {colors.hairline}"
    qtyTypography: "{typography.title-md}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-lg}"
    quoteBackground: "{colors.canvas}"
    quoteTextColor: "{colors.navy}"
    quoteBorder: "1px solid {colors.navy}"
    padding: "{spacing.md} {spacing.base}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.navy}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    imageAspect: "4:3"
    hoverBorder: "1px solid {colors.primary}"
    hoverTextColor: "{colors.primary}"
  promo-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    accentColor: "{colors.primary}"
    typography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  filter-rail:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-sm}"
    headerTextColor: "{colors.ink}"
    optionTypography: "{typography.body-sm}"
    optionTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    checkboxAccent: "{colors.primary}"
    width: 240px
  sku-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.sku-label}"
    typography: "{typography.sku-mono}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.on-navy}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    borderColor: "{colors.navy}"
    padding: "{spacing.xl} 0"

## Components

### Buttons

**`button-primary`** — Orange (#F47B20) fill on a nearly-square-cornered (`{rounded.xs}`, 2px) rectangle, 40px tall with bold 15px type. The CTA vocabulary across the entire site — add-to-cart, submit-quote, download-spec-sheet — runs through this single component at consistent sizing so procurement buyers don't have to re-identify the action target as they move through dense product pages. Active state darkens to #D96010; disabled washes to `{colors.primary-disabled}`.

**`button-secondary`** — White fill with a navy border (`{colors.navy}`) and navy text, matching `button-primary` in height and type weight so the two sit cleanly side-by-side in the `add-to-cart-bar`. Used primarily for "Request a Quote" and "Add to List" alongside the primary add-to-cart action. No hover fill-change — just border darkens.

**`button-ghost`** — Transparent background with `{colors.primary}` text, no border. Used for inline link-style actions in spec tables and filter rails where a bordered button would add too much visual weight to an already-dense layout.

### Search Bar

**`search-bar`** — The site's most prominent interactive element: full-width below the nav rail, with a 2px `{colors.primary}` border that signals the input's priority before the user focuses it. The submit button is a filled orange rectangle (`{colors.primary}`) flush to the right edge, sized to 44px height to match the input. Placeholder copy is muted gray (`{colors.muted}`). On mobile, the search bar collapses into the sticky header as an icon that expands to full-width overlay.

### Navigation

**`nav-bar`** — Two-tier structure: a narrow top bar in `{colors.navy-dark}` at 36px carrying phone number, account sign-in, and order tracking in `{typography.caption}`; below it a 48px primary rail in `{colors.navy}` with the logo left, category mega-menu triggers center, and cart/account icons right. The phone number's prominence in the top bar is a deliberate B2B signal — enterprise buyers need to escalate to a human for large-order questions.

**`mega-menu`** — White (`{colors.canvas}`) panel that drops full-width below the nav, organized into 3–5 columns of subcategory links. Column headers use `{typography.title-sm}` in `{colors.navy}`; item links use `{typography.nav-sub}` in `{colors.ink}`. No images or promotional tiles — this menu is entirely link-list, prioritizing depth of navigation over visual merchandising.

### Product Card

**`product-card`** — The workhorse of the catalog grid. A 1px `{colors.hairline}` border card with 2px radius, square product photography (1:1 aspect ratio), then below it: SKU in `{typography.sku-mono}` at `{colors.sku-label}`, product title in `{typography.body-md}`, price in `{typography.price-display}`, and an inline add-to-cart input with a compact orange button. Hover lifts to a `{colors.primary}` border with a subtle box-shadow. The sale-badge and new-badge position at top-left of the image well, since eye-tracking research on B2B catalog grids confirms buyers scan the upper-left corner for status signals.

### Spec and Pricing Tables

**`spec-table`** — Alternating white/gray rows (`{colors.canvas}` / `{colors.surface-soft}`) with a navy header row (`{colors.navy}` fill, `{colors.on-navy}` text). Attribute labels in the left column use `{typography.title-sm}`; values in the right column use `{typography.body-sm}`. Row height is 36px — compact but touch-accessible. The table is the product-detail page's primary above-the-fold content on desktop, positioned before the "you may also need" rail.

**`bulk-pricing-table`** — Navy header row labeling quantity tiers (1–9, 10–24, 25–49, 50+), with price-per-unit in `{typography.price-sm}` per cell. The active tier (matching the current qty-input value) highlights in `{colors.surface-soft}`. This component drives B2B purchasing decisions more directly than any hero element; it appears prominently on all stocked product pages.

### Badges

**`sale-badge`** — Red (#CC0000) fill, white uppercase text in `{typography.badge}`, 2px radius. Appears at top-left of product card image. Used for clearance, limited-time pricing, and percent-off promotions. Maximum one badge per card in this slot.

**`new-badge`** — Orange (`{colors.primary}`) fill, white uppercase text, same size and radius as `sale-badge`. Used for recently added catalog items. Shares the same top-left image position; `sale-badge` takes priority when both conditions apply.

### Add to Cart Bar

**`add-to-cart-bar`** — A sticky strip on product detail pages: quantity stepper input (white, 1px `{colors.hairline}` border, bold qty in `{typography.title-md}`), an orange add-to-cart button (`{colors.primary}` fill, `{colors.on-primary}` text, `{typography.button-lg}`), and a secondary "Request a Quote" button (white fill, navy border). The bar uses `{colors.surface-soft}` background to lift it slightly off the page content. On mobile it pins to the bottom of the viewport.

### Filter Rail

**`filter-rail`** — Left sidebar fixed at 240px on desktop. Each filter group opens as an accordion with bold headers in `{typography.title-sm}` and checkbox options in `{typography.body-sm}`. Active checkboxes and range sliders use `{colors.primary}` accent. No rounded pills — facets present as square checkboxes consistent with the site's minimal-radius aesthetic. Applied filters appear as small dismissible tags above the product grid.

### Category Tile

**`category-tile`** — White card with 1px `{colors.hairline}` border and 2px radius, containing a 4:3 aspect-ratio photograph above bold navy title text in `{typography.title-sm}`. Used on category landing pages in 3–4 column grids. Hover changes border to `{colors.primary}` and text to `{colors.primary}`. No overlay or scrim effect — the tile relies on border-color change alone to signal interactivity.

### Footer

**`footer`** — Dark navy (`{colors.navy-dark}`) background in four columns: Products, Services, Resources, Company. Column headers in `{typography.title-sm}` and `{colors.on-navy}`; links in `{typography.body-sm}` at a lighter blue (#A8C4E0) for readability against the dark field. A secondary strip below carries copyright, privacy links, and accepted payment icons. The footer is link-dense — it doubles as a site-map for procurement buyers who bookmark by URL pattern.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar moves into sticky header as icon-expand; filter rail becomes bottom-sheet drawer; nav mega-menu collapses to accordion; add-to-cart bar pins to viewport bottom |
| Tablet | 744–1128px | Two-column product grid; filter rail collapses to a horizontal filter bar above the grid; top nav drops to single-tier; breadcrumb truncates to last two segments |
| Desktop | 1128–1440px | Three-to-four-column product grid; filter rail at 240px sidebar; two-tier nav at full width; spec table and bulk-pricing table visible side-by-side on product detail |
| Wide | > 1440px | Grid max-width centered at 1440px; side gutters increase; product grid stays at four columns; no layout changes beyond horizontal centering |

### Touch Targets

- All primary buttons (add-to-cart, search submit) minimum 44px tall
- Quantity stepper inputs minimum 36px tall with ± tap targets at 44×44px
- Filter checkboxes wrapped in a 40px tall tap row including label
- Nav top-tier links minimum 48px tall on touch breakpoints
- Category tiles and product cards full-card tap target

### Collapsing Strategy

- Mega-menu collapses to a hamburger-triggered accordion stack at < 1024px; category hierarchy flattens to two visible levels with "See all" expansion
- Filter rail collapses to a "Filter & Sort" button that opens a full-screen bottom drawer on mobile; applied-filter count badge appears on the button
- Breadcrumb collapses beyond three segments to "… > Parent > Current" ellipsis form
- Bulk-pricing table scrolls horizontally on mobile rather than stacking — preserving the tier comparison layout that drives B2B decisions
- Spec table collapses to a single-column label/value list on mobile with accordion grouping by attribute category

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex values are approximations** — the site returned an anti-bot error during extraction; no colors, fonts, or theme tokens were captured from live CSS. Values here are derived from publicly documented brand materials and logo inspection only.
- **Exact primary orange** — #F47B20 is the closest match to Global Industrial's documented brand orange but has not been confirmed against current live CSS; could range from #F06C10 to #F58E30.
- **Navy header value** — #1C3A6E is approximated; the actual nav background may differ in saturation or lightness.
- **Typography stack** — no font-family declarations were extracted. Arial-forward system stack is assumed; Global Industrial may use a licensed web font not visible without JS execution.
- **Border-radius values** — the site's actual radius scale could not be measured; 0px/2px/4px values are inferred from the utilitarian B2B aesthetic.
- **Exact spacing scale** — density assumptions are based on comparable MRO catalog sites; actual padding tokens were not captured.
- **Component state colors** (hover, focus outlines, error states) — not verified from live inspection.
- **Icon set** — navigation and UI icons not identified or described; could be a licensed set (Font Awesome, custom SVGs) or inline SVGs.
