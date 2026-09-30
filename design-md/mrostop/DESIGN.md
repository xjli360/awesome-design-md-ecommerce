---
version: alpha
name: "MROStop"
source_url: "https://www.mrostop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dense part numbers, six-digit SKUs, and specification tables are the everyday medium of industrial procurement — MROStop's catalog interface is built for the buyer scanning rows of fasteners, bearings, and electrical conduit under warehouse fluorescents rather than the consumer browsing lifestyle photography. The palette leans into industrial-orange convention — a direct-signal hue that carries every primary CTA, add-to-cart action, and account button, set against a clean white canvas (#ffffff) and a dark-navy anchor (#1e3a5f) that holds the header and structural chrome. Search dominates the top viewport: a wide, high-contrast input with an orange submit trigger sits above fold before any category grid appears, because the typical MROStop session begins with a part number, not a category browse. Product cards are functional rectangles — minimal rounding ({rounded.sm}), tight spacing, and a compact type scale that fits SKU, brand, unit-of-measure, and price into a scannable 200px column without overflow. Safety-yellow accent (#ffc107) appears contextually on promotional callouts and bulk-order banners, borrowing from the physical-world language of caution tape and high-visibility gear. In-stock/out-of-stock states use saturated green (#16a34a) and red (#dc2626) respectively — procurement buyers need immediate availability signals, so these are never muted. Typography defaults to a neutral system sans at modest weights; there is no display headline ambition here, since the information hierarchy bottoms out at specification rows and compatibility notes, not brand storytelling. Footer and sidebar navigation carry heavy link density, reflecting a B2B audience comfortable with text-rich layouts. The overall register is practical, legible, and density-tolerant — a UI that competes with PDF spec sheets rather than consumer fashion retail.

colors:
  primary: "#e8540a"
  primary-active: "#c24008"
  primary-disabled: "#f5b89a"
  primary-hover: "#d44a06"
  secondary: "#1e3a5f"
  secondary-active: "#152b47"
  accent-yellow: "#ffc107"
  accent-yellow-active: "#e0a800"
  stock-green: "#16a34a"
  stock-red: "#dc2626"
  stock-amber: "#d97706"
  ink: "#1a1a1a"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-navy: "#1e3a5f"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-dark: "#ffffff"
  link: "#1d4ed8"
  link-visited: "#6d28d9"
  promo-bg: "#fff7ed"
  promo-border: "#fed7aa"

typography:
  display-xl:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  sku-label:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.4px
    textTransform: uppercase
  badge:
    fontFamily: "Inter, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase

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
    height: 40px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
    activeBackgroundColor: "{colors.secondary-active}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"

  button-outline-navy:
    backgroundColor: "transparent"
    textColor: "{colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.secondary}"

  button-sm-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 7px 14px
    height: 32px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 9px 12px
    height: 40px

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 10px 48px 10px 40px
    height: 44px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      width: 48px
      rounded: "0 {rounded.sm} {rounded.sm} 0"

  nav-bar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "none"
    linkHoverColor: "{colors.accent-yellow}"

  top-utility-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
    linkColor: "{colors.accent-yellow}"

  mega-nav-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.secondary}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.none}"
    shadow: "0 4px 12px rgba(0,0,0,0.15)"
    padding: "{spacing.xl}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    skuTypography: "{typography.sku-label}"
    skuColor: "{colors.muted}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"

  product-hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    skuTypography: "{typography.sku-label}"
    skuColor: "{colors.muted}"
    imageAreaBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"

  availability-badge-in-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px

  availability-badge-limited:
    backgroundColor: "{colors.stock-amber}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px

  availability-badge-out-of-stock:
    backgroundColor: "{colors.stock-red}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px

  promo-banner:
    backgroundColor: "{colors.promo-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.promo-border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    accentColor: "{colors.primary}"
    iconColor: "{colors.primary}"

  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.secondary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBackgroundColor: "{colors.surface-card}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.base}"
    imageSize: 64px

  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.secondary}"
    headerTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    bodyTextColor: "{colors.body}"
    rowBorder: "1px solid {colors.hairline-soft}"
    alternateRowBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"

  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 80px
    buttonColor: "{colors.secondary}"
    buttonTextColor: "{colors.on-secondary}"

  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    linkColor: "{colors.link}"
    padding: "{spacing.sm} 0"

  sidebar-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.secondary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    checkboxAccent: "{colors.primary}"
    activeBg: "{colors.promo-bg}"

  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    linkColor: "#a3b4cc"
    linkHoverColor: "{colors.accent-yellow}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0 {spacing.xl}"


## Components

### Buttons
**`button-primary`** — The workhorse CTA: orange (#e8540a) fill, white text, 4px radius, 40px height. Used for add-to-cart, request-quote, and account sign-in across the catalog. Hover darkens to #d44a06; active state drops to #c24008; disabled washes out to a pale salmon (#f5b89a) that signals unavailability without the full destructive red register.

**`button-secondary`** — Navy (#1e3a5f) fill for actions one tier below primary, such as "View Quote", "Compare", or account-level actions in the utility bar. Pair with `button-primary` in split-action scenarios where both add-to-cart and request-a-quote appear on the same product card.

**`button-ghost`** / **`button-outline-navy`** — Transparent-fill variants with 1px bordered outlines for lower-priority actions like "View Details", "Save for Later", and filter-reset triggers. Ghost uses orange stroke; outline-navy uses the secondary navy stroke. Both sit at 40px height to align with their solid siblings in row-level product actions.

**`button-sm-add-to-cart`** — Compact 32px orange button that appears inline on grid-view product cards where vertical space is scarce. Drops to 13px/600 button-sm typography to fit without overflow.

### Search
**`search-bar`** — Full-width input with a flush-right orange submit button that snaps to the same border-radius as the input field, creating a connected pill-adjacent unit. The input gains a 2px orange focus ring on click. A magnifying-glass icon sits inset left; placeholder text reads something like "Search by part #, keyword, or brand". On mobile this expands to full viewport width with a sticky position.

### Navigation
**`nav-bar`** — 48px navy (#1e3a5f) horizontal strip carrying category mega-nav links and account/cart controls in white text. Links highlight to accent-yellow (#ffc107) on hover — a nod to industrial high-visibility conventions. Sits below a 32px black utility bar (`top-utility-bar`) that carries shipping threshold messaging, phone number, and account links in caption-scale yellow text.

**`mega-nav-panel`** — Full-width dropdown with a 3px orange top-border entry line, white background, and padded multi-column category link grid. Column headings use navy `title-sm`, sub-links use `body-sm`. Panel drops shadow at 0 4px 12px rgba(0,0,0,0.15) to lift it clearly above product content below.

### Product Cards
**`product-card`** — 1px hairline-bordered rectangle at `{rounded.sm}` (4px). Contains a square product image area, a 12px SKU in `sku-label` monospace above the product title, price in `price-sm` weight-600, and the `button-sm-add-to-cart` action. Border upgrades to orange on hover to signal interactivity. Availability badge stacks below the price.

**`product-hero`** — Full product detail layout: large image with `surface-soft` background left, title/SKU/specs/price/quantity/CTA stack right. Price renders in `price-display` (20px/700) colored orange to draw the eye after the title scan. Below the fold: `spec-table` and related accessories rail.

### Availability Badges
Three pill badges cover the inventory signal space: green (#16a34a) "In Stock", amber (#d97706) "Limited Availability", and red (#dc2626) "Out of Stock". All use 11px/700 uppercase `badge` typography at `{rounded.xs}` (2px) with 2px × 8px padding — tight enough to tuck beside pricing without crowding the layout.

### Spec Table
**`spec-table`** — Alternating-row table with a `surface-soft` (#f9fafb) header row carrying uppercase `spec-label` headings in navy. Body rows alternate between white and `surface-soft` for scanability across 10–30 row spec sheets. Outer border is 1px `hairline`; row separators use `hairline-soft`.

### Sidebar Filter
**`sidebar-filter`** — Left-rail filter panel used on category/search result pages. Section headings in `title-sm` navy, filter options in `body-sm`. Checkboxes use orange accent. Active filter pills show a `promo-bg` (#fff7ed) chip with a close × at `caption` scale.

### Promo Banner
**`promo-banner`** — Warm-orange-tinted strip (background #fff7ed, border #fed7aa) used for bulk-order incentive messaging, free-shipping thresholds, and time-sensitive promotions. `body-sm` text with an orange icon left-anchor. Sits between the search bar and the category grid on the homepage.

### Footer
**`footer`** — Full-width navy (#1e3a5f) with a 4px orange top-border brand stripe. Four-column link grid (Customer Service, Account, Resources, About) in `body-sm` with #a3b4cc link color that lifts to accent-yellow on hover. Bottom row carries copyright and payment-method icon strip separated by a `hairline` rule within the navy field.


## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar full-width sticky; mega-nav collapses to hamburger drawer; sidebar filter moves to modal sheet triggered by "Filter" button; utility bar hides phone number, shows icon only |
| Tablet | 744–1128px | Two-column product grid; nav shrinks top-level categories to icons+labels; sidebar filter visible as collapsible accordion left of 2-col grid; mega-nav panels switch to full-width overlay |
| Desktop | 1128–1440px | Three-column product grid; full mega-nav; persistent sidebar filter at 240px; utility bar fully visible with phone + account text |
| Wide | > 1440px | Four-column product grid; content max-width 1440px centered; sidebar filter expands to 280px; promo banners gain secondary CTA column |

### Touch Targets
- All interactive product card areas minimum 44px tap height
- Quantity increment/decrement buttons minimum 40px × 40px
- Filter checkboxes padded to 44px touch target vertically
- Mobile nav drawer links minimum 48px row height
- Add-to-cart button full-width on mobile product detail view

### Collapsing Strategy
- Mega-nav → hamburger slide-in drawer with accordion sub-categories
- Spec table → horizontally scrollable on mobile, sticky first column for attribute labels
- Sidebar filter → bottom sheet modal triggered by sticky "Filters (N)" button
- Utility bar → icon-only on mobile (cart, account, phone icon)
- Product card SKU label hides on mobile grid view, visible in list view only
- Breadcrumb truncates to "... > Current Category" on mobile


## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (JS-loaded tokens or anti-bot protection blocked extraction); all palette values above are inferred from industrial MRO supply category conventions and are unverified against the actual brand
- No font-family stacks were extracted; Inter and system-ui stack is a reasonable assumption for a functional B2B catalog but is unconfirmed
- Brand logo treatment, wordmark, and any custom icon set are undocumented
- Exact button border-radius values are unconfirmed; `{rounded.sm}` (4px) is assumed from industrial catalog norms
- Pricing display logic (UOM, tiered/quantity pricing, contract pricing) not modeled — MRO sites commonly have complex pricing surfaces that require additional component design
- Account/quote-cart distinction (standard retail cart vs. RFQ workflow) not fully specced; MROStop may use a hybrid model
- No information on whether the site uses Shopify, Magento, or a custom platform — component naming may need adjustment for platform-specific override patterns
- Promotional and seasonal campaign color overlays (if any) are undocumented
- Dark-mode support status unknown; this spec assumes light-only
