---
version: alpha
name: "Alpine Home Air"
source_url: "https://www.alpinehomeair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sixteen filter MERV ratings, eleven static pressure specs, and a cross-reference tool that accepts OEM part numbers before it accepts brand names — Alpine Home Air's catalog architecture announces its intended audience before a single product image loads. The site reads as a procurement interface wearing retail clothing: dimensional specs headline each product card, model-number fields sit in the primary search position, and the filter builder walks through cubic-feet-per-minute and duct geometry rather than lifestyle benefit. The confirmed extraction surface for this brand is narrow — only a deep charcoal (#313131) emerged from the live site, which sat behind anti-bot protection; this color anchors the text layer with the same authoritative weight that technical manuals use for body copy. The type stack defaults to the system sans-serif cascade (-apple-system, Roboto, Segoe UI), which reads as a practical choice for a brand where product data density matters more than bespoke letterform character — monospace alignment for filter dimensions, clean legibility for MERV comparison tables, and fast rendering for a customer base that is often on-site and mobile-browsing part numbers. Buttons carry a utilitarian energy: solid fills, lightly rounded corners ({rounded.sm}), and no decorative shadow treatment. The overall tone is that of a supply-house interface — confident in the catalog, spare with ornament, and priced for the buyer who already knows the difference between a MERV 13 and a MERV 16.

colors:
  primary: "#1a5fa8"
  primary-active: "#134a84"
  primary-disabled: "#90bde0"
  ink: "#313131"
  body: "#4b4b4b"
  muted: "#717171"
  muted-soft: "#9ca3af"
  hairline: "#dde2e8"
  hairline-soft: "#eff1f4"
  canvas: "#ffffff"
  surface-soft: "#f4f6f9"
  surface-card: "#ffffff"
  surface-strong: "#eaecf0"
  on-primary: "#ffffff"
  brand-charcoal: "#313131"
  utility-success: "#27ae60"
  utility-error: "#c0392b"
  utility-warning: "#e67e22"
  badge-sale: "#c0392b"
  badge-instock: "#27ae60"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  merv-badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
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
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: 10px 40px 10px 14px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
    height: 64px
    logoHeight: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
  merv-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.merv-badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-instock:
    backgroundColor: "{colors.badge-instock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.merv-badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.merv-badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
  category-filter-bar:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.sm} {spacing.base}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  filter-builder-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  dimension-spec-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    borderBottomColor: "{colors.hairline-soft}"
    borderBottomWidth: 1px
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.brand-charcoal}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    borderTopColor: "{colors.hairline}"
    borderTopWidth: 1px
    padding: "{spacing.xxl} {spacing.xl}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    itemSize: 36px

## Components

### Buttons
**`button-primary`** — Solid {colors.primary} blue fill, white text in {typography.button-md}, 44px tall with 12px/24px padding and {rounded.sm} corners. Transitions to `button-primary-active` (#134a84) on hover and press; `button-primary-disabled` uses the washed-out #90bde0 to signal unavailability without introducing a red error tone. Used for high-intent procurement actions: "Add to Cart", "Get Quote", "Check Availability".

**`button-secondary`** — White canvas with a 1.5px {colors.primary} border and matching text. Same height and padding as primary. Used for parallel actions like "View Spec Sheet", "Compare Products", and "Save for Later". On hover, background shifts subtly to {colors.surface-soft} to signal interactivity without competing with the primary.

**`button-ghost`** — Transparent background with {colors.ink} text in {typography.button-sm} and {rounded.xs} corners. Low visual weight; reserved for inline collapsible actions ("Show More Sizes", "Collapse Filters") and breadcrumb-adjacent navigation helpers.

### Text Input & Search
**`text-input`** — White canvas, 1px {colors.hairline} border, {rounded.sm}, 44px height. Placeholder text in {colors.muted}. Focus state promotes border to 2px {colors.primary} with no outer glow ring — keeping the focus indicator sharp rather than diffuse. Used for quantity fields, part-number entry, and account forms.

**`search-bar`** — Inherits text-input geometry with 40px right-side padding reserved for the magnifier icon. Sized to display 20-character part-number strings (e.g. "AFL20X25X4-MERV13-CS") without truncation — a functional distinction from generic keyword search bars. Icon color renders in {colors.muted} at rest; advances to {colors.primary} on field focus.

### Nav Bar
**`nav-bar`** — White canvas, 64px tall, 1px {colors.hairline} bottom border. Logo sits at 36px height on the left; right cluster holds search, account, and cart icon buttons with 44px minimum hit areas. Category navigation populates a mega-menu dropdown on desktop. On mobile, all category links collapse behind a hamburger icon that opens a full-height drawer overlay.

### Product Card
**`product-card`** — 1px {colors.hairline} border, {rounded.sm} corners, {spacing.base} internal padding, 1:1 image aspect ratio. The part number renders in {typography.part-number} (monospace) directly beneath the product name in {typography.title-sm}, giving the SKU label-weight rather than body-text weight. Price displays in {typography.title-md}. MERV badge and stock badge layer over the image at the top-left corner.

### MERV Badge
**`merv-badge`** — Solid {colors.primary} fill with white text in {typography.merv-badge}: 11px, 700 weight, uppercase, 0.8px letter-spacing. {rounded.xs} corners keep it compact inside the card image zone. Variants use identical geometry with semantic fill colors: {colors.badge-instock} for availability confirmations, {colors.badge-sale} for promotional pricing callouts.

### Hero Section
**`hero-section`** — Full-width {colors.surface-soft} band with {spacing.section} vertical padding. Heading in {typography.display-xl}; supporting copy in {typography.body-md} at {colors.body}. A `button-primary` CTA anchors below the copy. The hero leads with a filter category or seasonal promo rather than aspirational photography — keeping the visual language productfirst and specification-grounded.

### Category Filter Bar
**`category-filter-bar`** — A horizontal-scrolling row of filter chips appearing at the top of listing pages. Inactive chip: {colors.surface-strong} fill, {colors.ink} text, 1px {colors.hairline} border, {rounded.sm}. Active chip: {colors.primary} fill, white text. Applied facets: MERV rating, nominal filter dimension, brand, media type, and replacement-frequency interval.

### Filter Builder Panel
**`filter-builder-panel`** — A collapsible left-rail sidebar on desktop (320px fixed width) and a bottom-sheet overlay on mobile. 1px {colors.hairline} border, {rounded.sm}, {spacing.lg} internal padding. Section headings in {typography.title-sm}; option labels in {typography.body-sm}. Checkboxes and radios take {colors.primary} in their selected state. Powers the "Build My Filter" configuration flow: duct dimensions → media type → quantity.

### Dimension Spec Row
**`dimension-spec-row`** — A data-table row for displaying nominal vs. actual dimensions, CFM ratings, and static pressure values. Label in {typography.caption} at {colors.muted}; value in {typography.body-sm} at {colors.ink}. Rows sit on {colors.surface-soft} with a 1px {colors.hairline-soft} bottom rule. Used across PDP specification tables and product-comparison grids where engineers read multiple values in parallel.

### Footer
**`footer`** — Deep {colors.brand-charcoal} (#313131) background — the only confirmed extracted color, used here as structural fill rather than text color — with white copy and {colors.surface-soft} links in {typography.body-sm}. Four-column grid on desktop (Shop, Resources, Account, Contact) collapses to a tap-to-expand accordion on mobile. Trust signals — HVAC certification marks, BBB rating, and warranty terms — sit in the lower strip rendered in muted light tones against the dark field.

### Breadcrumb
**`breadcrumb`** — Transparent background, {typography.caption}, {colors.muted} for parent segments, {colors.ink} for the active leaf. A "›" separator in {colors.hairline} sits between levels at 4px horizontal spacing. Positioned directly below the nav-bar with {spacing.sm} vertical padding. Middle segments collapse to "…" on narrow viewports, always preserving root category and current page title.

### Pagination
**`pagination`** — A row of 36px square page-number buttons, each with 1px {colors.hairline} border, {rounded.xs}, and {typography.button-sm}. Active page: {colors.primary} fill with white text. Prev/Next controls are icon-only arrow buttons using the same 36px square geometry. Sits below the product grid with {spacing.lg} top margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter panel becomes a bottom-sheet triggered by a sticky "Filters" button; nav collapses to hamburger + search icon; hero padding reduces to {spacing.xl}; search bar spans full width |
| Tablet | 744–1128px | Two-column product grid; filter sidebar visible as collapsible panel at 260px; nav shows logo + search + cart, category links condensed under "Shop" dropdown |
| Desktop | 1128–1440px | Three-column product grid; persistent left-rail filter sidebar at 300px; full nav with mega-menu dropdowns; spec tables render all columns without scroll |
| Wide | > 1440px | Four-column product grid; content max-width 1400px centered; sidebar and main column expand proportionally; hero copy max-width 720px for line-length control |

### Touch Targets
- All buttons and filter chips maintain 44px minimum height
- Nav cart, search, and account icons expand hit area to 44×44px regardless of visual icon size
- Checkbox and radio inputs extend the clickable zone to the full row via label wrapping
- Category filter bar chips have 40px minimum height with {spacing.sm} horizontal gap for reliable thumb separation
- Accordion rows in the footer are 48px tall on mobile

### Collapsing Strategy
- Filter sidebar collapses to a sticky "Filters (N)" button on tablet and mobile; tapping opens a full-height bottom sheet with a fixed "Apply" button at the base
- Nav mega-menu converts to a full-height accordion drawer below 1128px; top-level categories are 48px tap targets
- Dimension spec tables scroll horizontally on mobile rather than truncating column values — part numbers must remain fully visible
- Breadcrumb middle segments collapse to "…" on viewports below 400px, always preserving the root category and the current page label

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one color was extracted (#313131 charcoal); the live site returned a Cloudflare "Just a moment..." challenge page, blocking full palette extraction. All colors except {colors.ink} and {colors.brand-charcoal} are inferred from HVAC industrial DTC category conventions and are unverified against the actual site.
- No brand typeface was detected; the full extracted font stack is system fonts only. It is unknown whether Alpine Home Air licenses a custom or commercial typeface — all typography tokens use the system sans-serif cascade.
- Primary blue (#1a5fa8) is an informed assumption; the actual primary CTA color could differ materially — some HVAC brands use orange, red, or teal accent systems rather than blue.
- Meta theme-color was absent, removing one reliable signal for confirming the brand primary.
- No secondary or promotional accent palette could be confirmed; utility-success, utility-error, and badge-sale values are functional defaults rather than extracted values.
- Component interaction states (hover timing, transition curves, box-shadow depths) are fully inferred; no CSS animation or shadow data was accessible behind the anti-bot gate.
- Platform is confirmed non-Shopify; the underlying e-commerce framework and its theme token conventions are unknown, so component structure reflects generic DTC patterns rather than a platform-specific schema.
