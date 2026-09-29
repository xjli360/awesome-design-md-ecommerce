---
version: alpha
name: "Fastener SuperStore"
source_url: "https://www.fastenersuperstore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fastener SuperStore runs a Bootstrap 3 skeleton stripped to its industrial minimum — the full Bootstrap alert spectrum (success green anchored on #dff0d8, warning amber on #fcf8e3, danger on #f2dede, info on #d9edf7) functions as a live inventory and order-status language, so a purchasing agent scanning a 500-line quote can parse availability at a glance without reading a word. The brand primary is a mid-register workman's blue (#0871b9) occupying the space between navy authority and consumer-app lightness — it covers every Add-to-Cart button, navigation rail, and active link, with a near-twin (#076eb9) for hover states. A dedicated action-red (#bc2026) handles flash-sale banners and urgent stock notices, distinguishable from Bootstrap's stock danger red (#d9534f) enough to read as intentional brand voltage rather than framework default.

  Type leads with Numans, a geometric Google Font whose squared terminals give catalog headings a slightly stencil-like precision — useful in a product universe measured in thread pitch, tensile class, and head-drive geometry. Body copy falls to Roboto, then Arial, a practical fallback for Windows-heavy industrial desktop environments where custom font loading is unreliable. The scale stays compact: display at 24–28px, body at 14–16px, with monospaced part-number captions that echo caliper-spec precision.

  Surfaces tile in low-contrast pale neutrals — #f6f6f6 page canvas, #f5f5f5 card fills, #eeeeee hairlines — so photography of zinc-coated hex bolts and stainless fasteners reads as the highest-contrast element on any product page. Rounded corners hold at Bootstrap's 4px default ({rounded.xs}) throughout; every button, input, and product tile shares the same minimal corner. Navigation and footer run near-black (#080808), bookending catalog pages with industrial weight that signals supply-chain credibility over lifestyle warmth.

colors:
  primary: "#0871b9"
  primary-hover: "#076eb9"
  primary-active: "#065fa0"
  primary-disabled: "#e9edf7"
  brand-red: "#bc2026"
  brand-red-active: "#9e1b1f"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#8a8b8c"
  hairline: "#eeeeee"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f5f5f5"
  surface-row-alt: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#0871b9"
  success-text: "#3c763d"
  success-bg: "#dff0d8"
  warning-text: "#8a6d3b"
  warning-bg: "#fcf8e3"
  danger-text: "#a94442"
  danger-bg: "#f2dede"
  info-text: "#31708f"
  info-bg: "#d9edf7"

typography:
  display-xl:
    fontFamily: "'Numans', 'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Numans', 'Roboto', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Numans', 'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Numans', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Numans', 'Roboto', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Numans', 'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "'Numans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  button-danger:
    backgroundColor: "{colors.brand-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-danger-hover:
    backgroundColor: "{colors.brand-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 5px 10px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 36px
    placeholderColor: "{colors.muted-soft}"
    focusBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 40px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
      width: 44px
  top-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 50px
    utilityBar:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      height: 36px
  breadcrumb:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.body}"
    separatorColor: "{colors.muted-soft}"
    padding: "{spacing.sm} {spacing.base}"
  category-nav-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.primary}"
    activeText: "{colors.on-primary}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
  status-badge-in-stock:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-badge-out-of-stock:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-badge-limited:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    border: "1px solid {colors.success-text}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    border: "1px solid {colors.warning-text}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    border: "1px solid {colors.danger-text}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info-text}"
    border: "1px solid {colors.info-text}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    altRowBackground: "{colors.surface-row-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    valueTypography: "{typography.part-number}"
    border: "1px solid {colors.hairline}"
  pagination:
    activeBackground: "{colors.primary}"
    activeText: "{colors.on-primary}"
    defaultBackground: "{colors.canvas}"
    defaultText: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
    minWidth: 36px
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    accentRule: "{colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The core add-to-cart and checkout CTA uses brand blue (#0871b9) with white text, 36px height, and a 4px radius (`{rounded.xs}`) matching Bootstrap 3's standard `.btn` geometry. Hover shifts to `{colors.primary-hover}` (#076eb9); active state compresses to `{colors.primary-active}` (#065fa0). Disabled state uses a pale blue `{colors.primary-disabled}` (#e9edf7) background with `{colors.muted}` gray text to signal unavailability without alarming the user.

**`button-secondary`** — White background with a 1px `{colors.hairline}` border and the same 36px height. Used for secondary catalog actions — "Add to Compare," "Request Quote," "Save for Later." Hover applies a light `{colors.surface-soft}` fill without border color change.

**`button-danger`** — Solid brand-red (#bc2026) button for clearance banners, urgent promotions, and destructive actions in account management. Maintains the same 36px height and `{rounded.xs}` corner as other buttons for visual consistency. Hover darkens to `{colors.brand-red-active}` (#9e1b1f).

**`button-sm`** — A compact 28px version of `button-primary` using `{typography.button-sm}` and 5px/10px padding. Deployed inside data tables, quantity-adjustment rows, and filter chips where vertical density is critical.

### Search

**`search-bar`** — Full-width input group with a 44px-wide `{colors.primary}` submit button flush to the right edge. The input uses `{rounded.xs}` on all four corners; Bootstrap's input-group CSS squares the input's right edge where it joins the button. The submit button icon is a magnifier glyph from Glyphicons Halflings. Placeholder text renders in `{colors.muted-soft}`; focus state shifts the full border to `{colors.primary}`. Appears prominently below the logo in both the utility header and the mobile collapsed nav.

### Navigation

**`nav-bar`** — Two-tier header structure: a `{colors.primary}` (#0871b9) utility bar at 36px height carrying phone number, account login, and cart count; below it a full-width `{colors.ink}` (#080808) main nav bar at 50px. The logo renders white against the dark main nav. Desktop nav items use `{typography.nav-link}` in white with hover underlines; category dropdowns open against `{colors.surface-card}` with standard `{colors.body}` text.

**`breadcrumb`** — Renders on a `{colors.surface-soft}` (#f6f6f6) strip immediately below the nav, using `{typography.body-sm}` in `{colors.muted}` gray. The current page label uses `{colors.body}` (#555555) without bolding; separators are "/" characters in `{colors.muted-soft}`.

**`category-nav-pill`** — Horizontal pill-strip selectors on category landing pages for navigating screw drive types, thread standards, and material grades. Each pill uses `{rounded.xs}` with a subtle `{colors.hairline}` border. The active selection fills with `{colors.primary}` and white text; inactive pills sit on `{colors.surface-soft}`. On mobile the strip becomes horizontally scrollable without wrapping.

### Product Card

**`product-card`** — A `{colors.surface-card}` (#f5f5f5) tile bordered by 1px `{colors.hairline}`. Product image renders on a pure white `{colors.canvas}` swatch to maintain visual neutrality for hardware photography — zinc, stainless, and black-oxide finishes all read accurately against white. Part number displays in `{typography.part-number}` (monospace) in `{colors.muted}` below the product title, echoing a catalog line-item entry. Price renders in `{typography.title-md}` at `{colors.primary}` blue. A `status-badge` pill sits below the price showing stock state.

### Alerts and Status Badges

**`alert-success / alert-warning / alert-danger / alert-info`** — Bootstrap's four-color alert system repurposed as an order-status and inventory-notification language. All four variants share `{rounded.xs}`, a 1px border using the text color, and `{typography.body-sm}` copy. They appear inline on product pages for stock notices, in checkout flows for shipping updates, and on account pages for order status.

**`status-badge-in-stock / status-badge-out-of-stock / status-badge-limited`** — Small inline badges inside product listings and search results. All use `{rounded.xs}` (not fully rounded) and `{typography.badge}` — 11px uppercase with 0.3px tracking. The three-tier color mapping (green/red/amber) allows a buyer to scan availability across a multi-row quote list without reading individual labels.

### Spec Table

**`spec-table`** — Two-column key-value grid for listing thread pitch, material, finish, tensile strength, head drive type, and dimensional standards. Header row uses `{colors.surface-soft}` fill; alternating data rows use `{colors.surface-row-alt}` (#f0f0f0) for zebra-striping. Value cells render in `{typography.part-number}` (monospace) to visually align numeric specifications and standardize at-a-glance comparison. Outer and inner borders use 1px `{colors.hairline}`.

### Footer

**`footer`** — Full-width `{colors.ink}` (#080808) block matching the top nav bar, creating a dark frame around the catalog. Section headings use `{typography.title-sm}` in white; body links render in `{colors.surface-soft}` (#f6f6f6) at `{typography.body-sm}`. A thin `{colors.primary}` (#0871b9) horizontal rule separates the link columns from the copyright strip at the base. Standard four-column layout (Customer Service, My Account, About, Connect) collapses to an accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; utility bar collapses to icon-only; nav becomes hamburger drawer; search bar goes full-width below logo; spec table gains horizontal scroll |
| Tablet | 744–1128px | Two-column product grid; category nav-pill strip becomes horizontally scrollable; breadcrumb truncates to last two segments |
| Desktop | 1128–1440px | Three-column product grid; full two-tier nav visible; category filter sidebar at 240px fixed width alongside results |
| Wide | > 1440px | Content max-width 1400px centered; four-column product grid; sidebar widens to 280px |

### Touch Targets

- All buttons maintain a minimum 36px height; `button-sm` (28px) is used only inside data tables where row-level tappability supplements the button target
- Search submit button: minimum 44×40px tap zone
- Pagination items: minimum 36×36px per number
- Mobile nav items in expanded hamburger drawer: minimum 48px row height
- Status badges are display-only; the tappable unit is the product card, not the badge

### Collapsing Strategy

- Two-tier nav merges to a single icon-strip header on mobile; utility-bar content (phone, account, cart) condenses to three icons aligned right
- Category filter sidebar converts to a slide-in drawer triggered by a "Refine Results" button above the product grid
- Spec tables receive `overflow-x: auto` wrapper on mobile; all columns remain visible via horizontal scroll rather than truncated
- Alert strips go full-width and stack vertically on mobile; on desktop they are constrained to the content column width
- Product card actions (quantity selector, Add to Cart button) stack vertically below the price on mobile and render as an inline row on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact logo typeface unconfirmed — Numans is inferred from the font-family stack but its use in the wordmark is not verified from CSS extraction alone
- No animation or transition timing values extracted; Bootstrap 3 defaults (0.15s ease-in-out) are assumed throughout
- Precise nav-bar height breakpoints not confirmed; 50px main nav height is inferred from Bootstrap 3 `.navbar` defaults
- No dark-mode palette detected; site appears light-only with no prefers-color-scheme media query evidence
- Custom checkout, account portal, or dealer-pricing portal may use a divergent design system from the public catalog
- No custom icon set beyond Glyphicons Halflings identified; product-category icons may use a separate sprite sheet not captured in CSS extraction
- Product image aspect ratio not confirmed; 1:1 square crop assumed from standard catalog conventions
- Exact spacing rhythm inside product-card and spec-table not measurable from CSS hints; Bootstrap 3 grid gutters (30px) assumed
