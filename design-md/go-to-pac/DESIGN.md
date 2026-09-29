---
version: alpha
name: "Go-To-PAC"
source_url: "https://www.gotopac.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cobalt-blue procurement infrastructure meets construction-orange urgency — the Go-To-PAC palette pairs #006bb4 with #f88431 using the same chromatic logic applied to cleanroom warning strips and HVAC actuator panels: one color anchors navigation and organizational trust, the other marks action and deadline. Production Automation Corporation is a deep-catalog industrial supplier serving engineers and facilities managers who arrive with a part number already in hand. The visual system exists to close that transaction in as few clicks as possible, not to tell a brand story.

  Type runs on Open Sans at 14px — compact enough for multi-column specification tables, legible enough for print-to-PDF purchase orders. Seven distinct gray values (#575757, #636363, #7d7d7d, #808080, #8f8f8f, #959595, #bbbbbb) provide the hierarchy needed to separate SKU identifiers from product names, pricing tiers from per-unit footnotes, and category breadcrumbs from page titles — without introducing color where functional distinction already exists. The near-black ink (#111111) anchors headings; body copy runs at #575757 to reduce visual density on data-heavy catalog pages. Part numbers and SKU strings render in Consolas, a monospace face that signals precision and allows character-by-character comparison across search result rows.

  A full semantic feedback palette covers the operational realities of industrial procurement: light-blue #cce6fb for informational callouts, warm-amber #fdf0d5 with #6f4400 text for minimum-order thresholds and lead-time notices, soft-red #fae5e5 for stock-out and validation errors, and pale-green #e5efe5 for order confirmations. The error-dark red (#bc1e2b) marks destructive actions and critical form failures. Link blue (#1979c3) is deliberately distinct from the primary brand blue so interactive inline text never blurs into branded UI chrome.

  Buttons sit at {rounded.xs} — 4px — the minimum radius that reads as interactive without softening the industrial register. The Add-to-Cart action breaks from the primary blue and fires in orange accent (#f88431), a deliberate contrast that makes the transaction path visible at a glance in a page dense with specification text and pricing data. Product cards are rectilinear data blocks: monospace part number at {typography.part-number} scale, product name at {typography.title-md}, price at {typography.price-display}, and the orange CTA anchoring the bottom edge. No decorative gradients, no lifestyle photography — the visual grammar is part specification, part procurement table, entirely in service of repeat industrial buyers.

colors:
  primary: "#006bb4"
  primary-active: "#00579e"
  primary-disabled: "#7db8dc"
  accent: "#f88431"
  accent-bright: "#ff9635"
  accent-active: "#c07600"
  error: "#e02b27"
  error-dark: "#bc1e2b"
  warning-text: "#6f4400"
  link: "#1979c3"
  ink: "#111111"
  body: "#575757"
  body-alt: "#636363"
  muted: "#7d7d7d"
  muted-soft: "#808080"
  muted-light: "#8f8f8f"
  muted-xlight: "#959595"
  hairline: "#bbbbbb"
  hairline-mid: "#c2c2c2"
  hairline-light: "#c6c6c6"
  hairline-xlight: "#cfcfcf"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-light: "#efefef"
  surface-mid: "#e8e8e8"
  surface-strong: "#ebebeb"
  surface-tinted: "#e6f0f3"
  surface-card: "#ffffff"
  surface-info: "#cce6fb"
  surface-warning: "#fdf0d5"
  surface-error: "#fae5e5"
  surface-success: "#e5efe5"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  part-number:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  table-header:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0

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
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    border: none
  button-add-to-cart-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-tinted}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-light}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline-light}"
    activeColor: "{colors.primary}"
    hoverColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    inputTypography: "{typography.body-md}"
    inputColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.xs}"
    height: 40px
    placeholderColor: "{colors.muted-light}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-light}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    ctaBackgroundColor: "{colors.accent}"
    ctaTextColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    linkColor: "{colors.link}"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
    border: "1px solid {colors.hairline-light}"
  alert-info:
    backgroundColor: "{colors.surface-info}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary}"
  alert-warning:
    backgroundColor: "{colors.surface-warning}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.accent-active}"
  alert-error:
    backgroundColor: "{colors.surface-error}"
    textColor: "{colors.error-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.error}"
  alert-success:
    backgroundColor: "{colors.surface-success}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  spec-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.table-header}"
    headerColor: "{colors.ink}"
    rowTypography: "{typography.body-sm}"
    rowColor: "{colors.body}"
    partNumberTypography: "{typography.part-number}"
    borderColor: "{colors.hairline-light}"
    alternateRowColor: "{colors.surface-light}"
    baseRowColor: "{colors.canvas}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    unitTypography: "{typography.body-sm}"
    unitColor: "{colors.muted}"
    saleColor: "{colors.error-dark}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.accent}"
    ctaTextColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.surface-tinted}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — The primary action button runs cobalt blue (#006bb4) on white text at a 4px radius (`{rounded.xs}`), maintaining the industrial precision register throughout. Hover and focus darken to `{colors.primary-active}` (#00579e) with no transition delay — procurement users expect immediate, unambiguous feedback. Disabled state softens to `{colors.primary-disabled}` while retaining shape and size; height is fixed at 40px with 10px vertical and 20px horizontal padding. Used for account actions, checkout progression, and secondary order operations.

**`button-add-to-cart`** — Deliberately distinct from the primary blue, this button fires in construction orange (#f88431) with white text. It is the highest-priority CTA on every product page and catalog row; the color break from the blue navigation system ensures it reads at a glance in dense SKU grids. Active/pressed state deepens to `{colors.accent-active}` (#c07600). On mobile product detail pages, it spans the full card width and pins to the viewport bottom. Same dimensions as `button-primary`.

**`button-secondary`** — White background with a 1px cobalt-blue border and primary blue text. Used for lower-priority purchase-path actions: "Request Quote," "Download Spec Sheet," "Add to Wishlist," "Compare." Active state fills the background with `{colors.surface-tinted}` (#e6f0f3) and darkens the border to `{colors.primary-active}`. Both primary and secondary buttons share the same `{rounded.xs}` 4px radius — there is no visual softening to distinguish hierarchy, only color.

### Search Bar

**`search-bar`** — Full-width input at 40px height with a 1px `{colors.hairline}` border terminating flush in a cobalt-blue submit button. Input text at `{typography.body-md}` with placeholder copy at `{colors.muted-light}`. On focus the border shifts to `{colors.primary}` with no animation. The submit button inherits `{colors.primary}` background and `{colors.on-primary}` icon; on hover it shifts to `{colors.primary-active}`. On mobile the search bar collapses to a magnifier icon in the top bar; tapping it expands to a full-width overlay input.

### Navigation

**`nav-bar`** — White canvas with a 1px `{colors.hairline-light}` bottom border and 48px height. Primary nav links at `{typography.nav-link}` (14px/600 weight); active and hover states render in `{colors.primary}` with a bottom indicator bar. A promotional strip above the main nav may carry a cobalt-blue field with white body text for shipping thresholds or order deadlines. Category mega-menus drop on hover, structured as two- or three-column grids of subcategory links on `{colors.surface-soft}`.

### Product Card

**`product-card`** — Rectilinear data block with a 1px `{colors.hairline-light}` border and `{rounded.xs}` corners. Stacked layout from top: monospace part number at `{typography.part-number}` in `{colors.muted}`, product name at `{typography.title-md}` in `{colors.ink}`, short description at `{typography.body-sm}` in `{colors.body}` truncated to two lines, price at `{typography.price-display}`, then the orange `button-add-to-cart` pinned to the card bottom. Most SKUs render with a white-background product photograph or a `{colors.surface-soft}` gray placeholder. No shadow — border provides containment.

### Specification Table

**`spec-table`** — Used on product detail pages for technical attributes: dimensions, materials, certifications, compatible models, operating ranges. Column headers at `{typography.table-header}` on `{colors.surface-soft}` background. Data rows alternate between `{colors.canvas}` and `{colors.surface-light}` for scan-ability across dense attribute lists. Part numbers and model codes within cells render in `{typography.part-number}` to preserve monospace alignment and allow visual comparison. Borders at `{colors.hairline-light}` separate columns and rows.

### Alerts and Feedback

**`alert-info`** — Light-blue surface (#cce6fb) with `{colors.primary-active}` text and a 1px `{colors.primary}` border. Used for warehouse source notices, certification disclosures, and bulk pricing tier explanations. **`alert-warning`** — Warm-amber surface (#fdf0d5) with `{colors.warning-text}` (#6f4400) for minimum-order quantities, lead-time disclosures, and hazmat shipping notices — the warm amber signals caution without the alarm of red. **`alert-error`** — Soft-red surface (#fae5e5) with `{colors.error-dark}` for stock-out, form validation failure, and payment errors. **`alert-success`** — Pale-green surface (#e5efe5) with `{colors.body}` text for order confirmation and cart success toasts. All four variants share `{rounded.xs}` and `{spacing.base}` internal padding.

### Breadcrumb

**`breadcrumb`** — Small `{typography.caption}` trail above product titles and category landing pages. Intermediate crumbs render in `{colors.link}` (#1979c3) as underlined links; the current page renders in `{colors.ink}` as non-linked text. Separator is a `›` glyph in `{colors.hairline}`. Breadcrumb rows on catalog pages frequently span four or five levels deep (Home › Cleanroom › HEPA Filters › 24×24 › ULPA-Rated).

### Price Block

**`price-block`** — Primary price at `{typography.price-display}` (20px, bold) in `{colors.ink}`. Per-unit callouts ("/ each", "/ box of 50", "/ case") appear in `{typography.body-sm}` at `{colors.muted}` immediately after the price value. Sale or promotional prices render in `{colors.error-dark}` (#bc1e2b) with the original price struck through at `{colors.muted}`. Login-gated pricing ("Sign in for contractor pricing") displays as a `{colors.link}` text link in place of the price value.

### Hero Banner

**`hero-banner`** — Full-width promotional banners on a `{colors.primary}` cobalt-blue field with white heading text at `{typography.display-xl}` and body copy at `{typography.body-md}`. The CTA inside banners uses the orange `button-add-to-cart` styling to maintain accent contrast against the blue field. Text areas are left-aligned with product or category imagery floating to the right. On mobile the image collapses and text spans full width.

### Category Badge

**`category-badge`** — Small label chips on product cards and search results indicating product classification ("Cleanroom," "HEPA," "Class 10," "ISO 5"). Renders `{typography.caption}` in `{colors.body}` on `{colors.surface-soft}` with a `{colors.hairline-light}` border. Used in multiples, inline below the product name. Background and text remain constant — no color-coding by category class.

### Footer

**`footer`** — Dark `{colors.ink}` (#111111) background with white heading columns at `{typography.title-sm}` and link rows at `{typography.body-sm}` in `{colors.surface-tinted}` (#e6f0f3) — a light blue-white that reads as accessible on dark without the full glare of pure white. Columns cover navigation, contact information, certification logos (ISO, cleanroom class badges, UL listings), and legal text. No imagery. Newsletter input uses `text-input` styling with a `button-primary` submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar collapses to icon, expands on tap to full-width overlay; nav becomes hamburger drawer; spec tables scroll horizontally; price block and Add-to-Cart button pin to viewport bottom on product detail pages |
| Tablet | 744–1128px | Two-column product grid; top nav secondary links collapse into "More" dropdown; search bar remains visible inline in header; category sidebar converts to horizontal filter chips above the grid |
| Desktop | 1128–1440px | Three- to four-column product grid; left sidebar for category tree navigation; full top nav visible with mega-menu dropdowns; search bar at full width in header |
| Wide | > 1440px | Content max-width capped at approximately 1440px with symmetric side whitespace; four-column product grid persists; no layout change beyond centering |

### Touch Targets

- Minimum 44×44px for all interactive elements on mobile
- Add-to-Cart button expands to full card width on mobile product cards
- Breadcrumb links maintain 32px minimum height with vertical padding added
- Nav drawer links at minimum 48px row height for reliable tapping
- Alert dismiss controls padded to 44px touch area regardless of icon size

### Collapsing Strategy

- Category sidebar collapses first (desktop → tablet), converting to horizontal filter chips above the grid
- Top nav secondary links fold into a "More" dropdown or hamburger drawer before the search bar collapses
- Spec tables become horizontally scrollable on mobile rather than reflowing — column alignment must be preserved for part number comparison
- Product card description text truncates to two lines in grid view; full text visible on product detail page
- Alert banners stack vertically on mobile and do not auto-dismiss; user must acknowledge each

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom brand font — Open Sans is the most prominent non-system font in the extraction, likely loaded via Magento theme or Google Fonts CDN; Arial/Helvetica Neue are listed as fallbacks and may be primary on some page segments
- Exact border-radius not confirmed from computed CSS — `{rounded.xs}` (4px) is inferred from industrial B2B visual conventions and Magento Luma theme defaults; fully square (0px) is possible in the deployed theme
- Button padding and height values are estimated from Magento catalog theme conventions, not extracted from computed styles
- Primary disabled color (#7db8dc) is an estimate — no exact disabled-state blue appears in the extracted hex list
- No meta theme-color declared, confirming no PWA color or native browser chrome tint configured
- Platform confirmed as Magento (inferred from `luma-icons` and `magento-icons` font families); exact Magento version and customization depth unknown — some token values may diverge from Luma defaults
- Success-state foreground green not extracted — alert-success text defaults to `{colors.body}` (#575757) in this spec; actual implementation may use a dedicated success green not captured
- Promotional or seasonal color overrides (sale events, clearance campaigns) not captured in extraction
- Logo SVG color treatment unconfirmed — primary blue assumed in the wordmark but a distinct logomark color cannot be ruled out
