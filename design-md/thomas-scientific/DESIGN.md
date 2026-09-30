---
version: alpha
name: "Thomas Scientific"
source_url: "https://www.thomassci.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The scarlet alert-red Thomas Scientific uses for every primary CTA — #de1f27, close enough to ANSI safety red that it would not look out of place on a biohazard label — is the clearest signal this catalog was designed for procurement officers working under fluorescent lighting, not lifestyle browsers on OLED phones. Five extracted colors carry the entire functional vocabulary: #de1f27 for action and urgency; #222222 for the dense SKU-and-spec text hierarchy; #6d6e71 for secondary metadata like pack counts and catalog references; #b3d4fc, a washed periwinkle that surfaces in featured category tiles and callout backgrounds, providing the only visual softness in an otherwise utility-first interface; and #116600, a high-contrast institutional green reserved for in-stock confirmations and certified-product badges. Sans-serif is the only declared typeface — no custom brand font was resolved — which fits: typography here primarily serves readability of alphanumeric part numbers, specification tables, and CAS registry codes rather than brand storytelling.

  Buttons are rectangular, minimally rounded ({rounded.xs}), sized for decisive reorder clicks rather than exploratory browsing — the form follows the procurement workflow. The search bar dominates above the fold, flanked by a {colors.primary} submit button, because this catalog spans tens of thousands of SKUs and navigation by browse alone is impractical. Product cards lead with an image on a {colors.surface-soft} field, followed immediately by a monospace catalog number ({typography.part-number}), then title, pack size, and price in {colors.primary} — the hierarchy mirrors how a lab manager scans a requisition form. Category tiles draw on {colors.accent-blue} to visually separate browse-mode navigation from the transaction-mode product list. A top utility bar in {colors.primary} carries account links, order history, and quick-order entry — features only a returning professional purchaser needs at a glance.

colors:
  primary: "#de1f27"
  primary-active: "#b5181f"
  primary-disabled: "#f0a0a3"
  ink: "#222222"
  body: "#3d3d3d"
  muted: "#6d6e71"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#b3d4fc"
  status-success: "#116600"
  status-error: "#de1f27"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-lg:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-tertiary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 7px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 38px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  nav-bar-utility:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-mega-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  search-bar-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 44px
    width: 52px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-part-number:
    textColor: "{colors.muted}"
    typography: "{typography.part-number}"
  product-card-price:
    textColor: "{colors.primary}"
    typography: "{typography.price-lg}"
  category-tile:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-in-stock:
    backgroundColor: transparent
    textColor: "{colors.status-success}"
    typography: "{typography.caption-bold}"
  badge-out-of-stock:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
    width: 100px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  data-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    borderBottom: "2px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  data-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  data-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 32px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"

## Components

### Buttons
**`button-primary`** — A rectangular #de1f27 button with minimal rounding ({rounded.xs}), 40px tall, used exclusively for add-to-cart, request-a-quote, and checkout CTAs. Hover darkens to {colors.primary-active}; disabled washes out to {colors.primary-disabled}. The tight corner radius and strong color echo the decisive, utilitarian vocabulary of lab equipment instrumentation panels.

**`button-secondary`** — White canvas background with a 1px {colors.primary} border and red text, creating a clear visual pairing with the primary without competing for attention. Used for secondary purchase actions like "Add to Quote" or "Save to List" alongside the primary add-to-cart button.

**`button-tertiary`** — A low-contrast {colors.surface-soft} background button used for filter actions, comparison toggles, and non-purchase interactions. Keeps the page from becoming visually saturated with red across high-SKU category pages.

### Search Bar
**`search-bar`** + **`search-bar-button`** — The search input spans most of the header width with a right-anchored {colors.primary} submit icon-button flush to the input's edge (no rounding gap between them). This is the primary navigation instrument for a catalog of this depth; the red submit button reinforces that search is the primary action of every page, not browsing category tiles.

### Navigation
**`nav-bar-utility`** — A 36px-tall top strip in {colors.primary} carries account links, order tracking, and quick-order entry in {typography.caption-bold} white. This strip signals account-holder priority: guest visitors barely see it, but returning procurement users treat it as their primary control surface.

**`nav-bar`** — A white 60px main bar below the utility strip holds the logo and primary category megamenu triggers in {typography.nav-link}. Megamenu panels ({nav-bar-mega-panel}) drop on hover with a full-width border-framed panel, listing subcategories in {typography.body-sm} dense columns.

### Product Card
**`product-card`** — A bordered {rounded.sm} card with a square {colors.surface-soft} image field at top, catalog number below in monospace {typography.part-number} and {colors.muted}, title in {typography.title-sm}, and price in {colors.primary} via {typography.price-lg}. The part-number in monospace is a deliberate hierarchy signal: the catalog ID is how professionals actually search and reorder, so it leads the text block. In-stock status ({badge-in-stock} or {badge-out-of-stock}) sits between part number and price.

### Category Tiles
**`category-tile`** — Uses {colors.accent-blue} as background, the only place this periwinkle appears at block scale, giving category-browse a distinctly cooler temperature than the red-and-white transactional zone. Text and icon sit centered within the tile; hover typically shifts background opacity or border. These tiles appear in the homepage grid and top of major category pages to orient first-time visitors.

### Badges
**`badge-promo`** — Solid {colors.primary} pill in all-caps {typography.badge} for sale pricing, limited-time offers, and clearance items. Overlays the top-left corner of product card images.

**`badge-new`** — Uses {colors.accent-blue} with dark ink text, visually distinguished from the urgency-red promo badge. Applied to recently added catalog items.

**`badge-in-stock`** / **`badge-out-of-stock`** — Inline text-only status indicators in {colors.status-success} green or {colors.muted} gray respectively; no background fill, keeping the product card metadata row compact.

### Data Tables
**`data-table-header`** + **`data-table-row`** + **`data-table-row-alt`** — Specification comparison tables are a primary content format for lab equipment; the header row uses a {colors.surface-soft} background with {typography.caption-bold}, rows alternate between white and {colors.surface-soft} for scanability. Column widths are typically fixed to align specs across many products. Part numbers in table cells use {typography.part-number} monospace.

### Hero Banner
**`hero-banner`** — Full-width {colors.primary} red banner used for homepage promotions, seasonal sales, and category feature placements. White text and a white button variant keep contrast accessible. The approach trades visual variety for maximum urgency — every promotional message inherits the authority of the primary brand red.

### Quantity Stepper
**`quantity-stepper`** — A compact 36px-tall inline input with decrement/increment icon buttons flanking a numeric field, bordered in {colors.hairline}. Appears on product pages and within cart line items. Width is intentionally constrained (~100px) because lab orders often require precise quantity entry rather than approximate selection.

### Footer
**`footer`** — A {colors.ink} (#222222) dark footer carrying column-based link lists in {colors.muted} with {typography.footer-heading} white section titles. Common columns: About, Customer Service, Ordering Information, Regulatory Resources. The dark footer visually terminates the page and provides a place for legal, safety compliance, and ISO certification links that a scientific supplier must surface.

### Tooltip
**`tooltip`** — Small dark-ink tooltip used to surface SDS (Safety Data Sheet) links, hazard codes, and shipping restriction icons on product cards. Tight padding (6px 10px) and {rounded.xs} corners keep it compact enough to float near dense spec tables without obscuring adjacent content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav replaces megamenu; search bar moves below logo row and spans full width; product grid collapses to 1-2 columns; utility nav bar collapses to icon strip; quantity stepper and add-to-cart button stack vertically on PDP |
| Tablet | 744–1128px | 2–3 column product grid; megamenu replaced by accordion drawer; search bar in header at reduced width; data tables scroll horizontally with sticky first column |
| Desktop | 1128–1440px | Full megamenu active; 4-column product grid; persistent utility bar; data table at full width with all columns visible |
| Wide | > 1440px | Content max-width capped (~1400px) centered on canvas; hero banner image expands edge-to-edge behind centered text container |

### Touch Targets
- Minimum 44×44px for all interactive controls (add-to-cart, quantity stepper buttons, nav links)
- Quantity stepper input expands tap area to full stepper height on mobile
- Category tiles scale to full-bleed card height on mobile for easy thumb navigation
- Search submit button maintains minimum 48px width on touch viewports

### Collapsing Strategy
- Megamenu flattens to a full-screen drawer with accordion sections at tablet and below
- Utility bar condenses to icon-only strip (account, cart, orders) on mobile; text labels hidden
- Product card metadata (brand, pack-size, catalog number) truncates to one line on mobile with expand-on-tap
- Specification comparison tables remain full-width but scroll horizontally; left column (attribute name) is sticky
- Footer columns collapse to single accordion on mobile; all link lists hidden behind expand controls

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The site returned "Something went wrong" during extraction — only five hex values and a bare `sans-serif` declaration were recovered. All derived colors (primary-active, primary-disabled, hairline, surface-soft, canvas) are reasonable inference from the extracted palette, not confirmed values
- No custom typeface was identified; the actual site likely uses a licensed or web-hosted sans-serif (possibly Arial, Source Sans Pro, or a Fonts.com license) that was not resolvable during extraction — typography scale sizes and weights are estimated from B2B catalog norms
- Exact button border-radius values are unconfirmed; {rounded.xs} (2px) is inferred from the functional/utilitarian category rather than measured
- No icon system or illustration style was extracted; Thomas Scientific likely uses a combination of product photography and vector category icons
- Hover states, focus rings, and animation durations are fully inferred — no motion or interaction tokens were recoverable
- The role of {colors.accent-blue} (#b3d4fc) is inferred from its position in the extracted color list; it may serve a narrower function (e.g., selected-state highlight or a single promotional banner) rather than the category-tile use modeled here
- Pricing display format (login-gated vs. public list price) is unknown; many scientific supply catalogs hide pricing behind account login, which would significantly change product card layout
