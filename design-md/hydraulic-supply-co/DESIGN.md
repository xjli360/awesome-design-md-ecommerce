---
version: alpha
name: "Hydraulic Supply Co"
source_url: "https://www.hydraulic-supply.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every interaction with Hydraulic Supply Co begins at a search bar — not a marketing hero, not a lifestyle image, but a direct query field for cylinder bores, fitting threads, and manifold assemblies. The confirmed palette anchors on `#313131`, a deep charcoal that runs through headings, data labels, and navigation text with the same no-ceremony weight you'd find printed on a parts-room shelf tag. System fonts carry all typographic work — no custom brand face was loaded, signaling a site built for procurement speed over brand expression. Product cards carry dense specification grids rather than aspirational copy: operating pressure in bar, bore diameter in millimeters, connection type in ISO standard codes. The component vocabulary reads closer to enterprise ERP than consumer e-commerce — sortable data tables, paginated catalog views, and request-for-quote flows rather than impulse add-to-cart paths. Corners stay angular throughout, with minimal radii (`{rounded.sm}` at most on cards and inputs) that match the industrial geometry of the products sold. The grid tightens at every breakpoint to preserve horizontal data density — a pneumatic cylinder datasheet needs eight columns to remain readable without column collapse. Badge treatments mark items as in-stock, on-lead-time, or end-of-life, and these status signals carry more visual weight than any promotional callout. Trust is communicated through legibility and completeness: the precision of a well-organized parts catalog is itself the brand promise.

colors:
  primary: "#1e4fa0"
  primary-active: "#163d80"
  primary-disabled: "#8faed4"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#767676"
  hairline: "#d4d4d4"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-alt: "#eef1f6"
  on-primary: "#ffffff"
  status-instock: "#27ae60"
  status-leadtime: "#e67e22"
  status-eol: "#c0392b"
  status-instock-bg: "#eafaf1"
  status-leadtime-bg: "#fef5e7"
  status-eol-bg: "#fdedec"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: -0.25px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  part-number:
    fontFamily: "'Courier New', Courier, 'Roboto Mono', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: 0.5px
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0

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
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.sm}"
  button-quote-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 44px
    iconColor: "{colors.muted}"
    submitButtonBg: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitRounded: "0px {rounded.sm} {rounded.sm} 0px"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 36px
    linkHoverColor: "{colors.primary}"
    utilityBarBg: "{colors.surface-soft}"
    utilityBarTextColor: "{colors.muted}"
    utilityBarTypography: "{typography.caption}"
    utilityBarHeight: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-sm}"
    partNumberTypography: "{typography.part-number}"
    priceTypography: "{typography.title-md}"
    specLabelTypography: "{typography.label-sm}"
    specValueTypography: "{typography.spec-value}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.08)"
  spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    headerBg: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.label-sm}"
    cellTypography: "{typography.body-sm}"
    cellBorderColor: "{colors.hairline-soft}"
    rowAltBg: "{colors.surface-alt}"
    valueColor: "{colors.body}"
    valueMonospace: "{typography.spec-value}"
    partStringTypography: "{typography.part-number}"
  part-number-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.part-number}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-instock:
    backgroundColor: "{colors.status-instock-bg}"
    textColor: "{colors.status-instock}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-leadtime:
    backgroundColor: "{colors.status-leadtime-bg}"
    textColor: "{colors.status-leadtime}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  stock-badge-eol:
    backgroundColor: "{colors.status-eol-bg}"
    textColor: "{colors.status-eol}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  category-breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
  category-nav-tree:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    activeFontWeight: 600
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    itemPadding: "{spacing.sm} {spacing.md}"
    groupLabelTypography: "{typography.label-sm}"
    groupLabelColor: "{colors.muted}"
  hero-catalog:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    searchEmbedded: true
    height: 220px
  pagination:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activePageBg: "{colors.primary}"
    activePageColor: "{colors.on-primary}"
    activePageRounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    itemPadding: "10px 14px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0 {spacing.xl}"
    copyrightTypography: "{typography.caption}"
    copyrightColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — Solid `{colors.primary}` (inferred industrial blue) fill, white text at 40px height with `{rounded.sm}` corners. Used for add-to-cart, filter apply, and primary catalog actions. Active state darkens to `{colors.primary-active}`; disabled state washes to `{colors.primary-disabled}` with a `not-allowed` cursor. Typography runs `{typography.button-md}` — 14px semibold with slight letter-spacing to hold legibility against dense catalog backgrounds.

**`button-secondary`** — White canvas fill with `{colors.hairline}` border at identical height and radius. Used for secondary filters, part comparison, and table-export actions. Hover shifts background to `{colors.surface-soft}` and border to `{colors.muted}`.

**`button-quote-cta`** — Charcoal `{colors.ink}` fill with white text, identical sizing to `button-primary`. Marks request-for-quote and inquiry flows, visually distinguishing procurement paths from immediate purchase. The contrast between blue (buy now) and charcoal (request quote) creates a clear two-tier CTA hierarchy essential for B2B catalogs.

### Search
**`search-bar`** — Left-aligned input (44px tall, `{rounded.sm}`) with a flush-right submit button carrying `{colors.primary}` background. Placeholder copy references part numbers explicitly ("Search by part number, keyword, or category"). The bar dominates the hero zone above the fold and repeats in the sticky nav on scroll. Focus state activates a `{colors.primary}` border ring on the input; the submit button remains filled at all states.

### Navigation
**`nav-bar`** — Two-tier bar: a 32px utility strip above (`{colors.surface-soft}` background, account links, phone number, cart indicator in `{typography.caption}`) and a 64px primary nav below (white canvas, logo left, main category links center, search shortcut right). Category links use `{typography.nav-link}` at 14px/500 weight; hover shifts text to `{colors.primary}`. Category navigation lives in a sidebar tree on landing pages rather than a fly-out mega-menu, keeping the primary bar clean.

### Product Card
**`product-card`** — 1×1 image aspect ratio (product on white background), part number in `{typography.part-number}` (monospaced, bold) directly below the image, product title in `{typography.title-sm}`, price in `{typography.title-md}`. A 3–4 row micro spec grid below shows key parameters (pressure rating, bore, stroke, connection type). The stock badge sits in the top-right corner overlay. On hover, border lifts to `{colors.primary}` with a `0 2px 8px` shadow at 8% opacity.

### Spec Table
**`spec-table`** — The signature component: a full-width bordered table with alternating row fill (`{colors.surface-alt}` / `{colors.canvas}`). Column headers run `{typography.label-sm}` uppercase in a `{colors.surface-soft}` header row. Cell values use `{typography.spec-value}` (500 weight, 13px) for numeric parameters, with unit labels in `{colors.muted}`. Thread standards and ISO codes (G 1/4", BSP, JIC 37°) render in `{typography.part-number}` monospace for instant visual differentiation. The table scrolls horizontally on mobile — no column collapse. The first column (parameter name) is pinned.

### Badges
**`part-number-badge`** — Inline chip with `{colors.surface-soft}` background and `{colors.hairline}` border; text in `{typography.part-number}` for SKU strings in search results and comparison views. Appears inline alongside product titles and in cart line items.

**Stock badges** — Three variants keyed to inventory state: `stock-badge-instock` (green tint `{colors.status-instock-bg}`, text `{colors.status-instock}`), `stock-badge-leadtime` (amber tint), `stock-badge-eol` (red tint). Each carries `{typography.label-sm}` uppercase text. Placed at top-right of product card and prominently at top of product detail page. These three states are the most business-critical UI signals on the site.

### Category Navigation
**`category-nav-tree`** — Left-sidebar panel (`{colors.surface-soft}` background, `{colors.hairline}` border) listing product families as collapsible groups. Group headers use `{typography.label-sm}` uppercase in `{colors.muted}`; leaf items use `{typography.body-sm}`. Active item text shifts to `{colors.primary}` at 600 weight with no background highlight. On mobile, the entire tree becomes a full-screen drawer triggered by a "Browse Categories" button.

### Hero
**`hero-catalog`** — Dark `{colors.ink}` band (220px tall) with white `{typography.display-xl}` headline and embedded `search-bar`. No photography — the hero communicates category authority through catalog copy ("Industrial Hydraulic Cylinders — Over 40,000 Components in Stock"). Keeps above-the-fold real estate focused on search conversion rather than brand storytelling.

### Footer
**`footer`** — Dark `{colors.ink}` background with a 3px `{colors.primary}` top border that carries the primary accent into the lower chrome. Four-column link grid in `{typography.body-sm}`. Column headings in `{typography.title-sm}` at `{colors.canvas}`. Copyright and legal line in `{typography.caption}` at `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category tree collapses to full-screen drawer; spec-table scrolls horizontally with pinned first column; nav collapses to hamburger; search bar full-width below logo |
| Tablet | 744–1128px | Two-column product grid; sidebar tree shows at 200px condensed width; utility nav bar hides phone number; hero remains full-width but reduces to 180px height |
| Desktop | 1128–1440px | Three-column product grid; sidebar category tree fully expanded at 240px; dual-tier nav bar visible; hero at full 220px; spec table fully visible without scroll |
| Wide | > 1440px | Four-column product grid; content max-width 1400px centered; lateral whitespace increases; footer link grid expands to five columns |

### Touch Targets
- All buttons minimum 40px height (primary, secondary, quote-cta)
- Search submit button spans full 44px height of the search bar
- Category nav tree items padded to minimum 44px touch height on mobile
- Pagination page numbers padded to 40×40px minimum on mobile
- Stock badges are display-only and excluded from interactive tap-target requirements

### Collapsing Strategy
- Category sidebar tree → full-screen drawer on mobile, triggered by "Browse Categories" button
- Utility nav bar → hidden on mobile; phone number and account links promoted to footer
- Spec table → horizontal scroll with pinned parameter-name column; no column removal
- Product card spec preview → truncated to two rows on mobile; full spec accessed on product detail page
- Footer link groups → stacked single-column with accordion-collapsed sections on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex value (`#313131`) was extracted; the primary accent (`{colors.primary}` set to `#1e4fa0`) is inferred and must be validated against the live site
- All secondary palette colors (surface, status badges, primary hover/active states) are derived or inferred — none confirmed by extraction
- No custom brand typeface was detected; the system font stack is confirmed but whether a licensed web font loads via JavaScript is unknown
- Meta theme-color is absent; mobile browser chrome color is unconfirmed
- The live site was behind a Cloudflare bot-protection challenge ("Just a moment...") during extraction, making full color and component discovery impossible
- Product price formatting, B2B login-gated pricing behavior, and promotional pricing display styles could not be observed
- Exact grid gutter widths, breakpoint pixel values, and column counts are inferred from industrial e-commerce category norms rather than measured
- Icon set (SVG library, icon font, or custom set) could not be identified
- Whether the site uses request-for-quote as a primary checkout flow versus standard cart-and-checkout is unknown and would significantly alter the CTA hierarchy
