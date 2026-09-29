---
version: alpha
name: "Galco Industrial Electronics"
source_url: "https://www.galco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Galco's search bar does the work that a hero image claims on a consumer site — the entire homepage vocabulary pivots on a part-number lookup field, because the buyer arriving at galco.com already knows the Allen-Bradley drive or Siemens PLC they need to source, and they need it confirmed fast. The extracted palette surfaces #313131, a near-charcoal that runs through navigation and structural chrome, asserting industrial authority before the first product thumbnail loads. Typography falls entirely on system stacks — Arial, Roboto, Helvetica Neue — with no proprietary typeface, consistent with a supplier whose credibility derives from 165,000+ SKUs and same-day ship rates rather than brand aesthetics. Information density is high by deliberate choice: part numbers, manufacturer cross-references, datasheet PDFs, and real-time stock counts share a compressed viewport in multi-column tables that would overwhelm a consumer shopper but reads as fluency to a maintenance engineer sourcing a replacement servo drive under production-downtime pressure.

  The component grammar trades ornament for utility — minimal {rounded.xs} corners throughout, tight table rows, high-contrast three-state stock badges, and faceted filters tuned for someone who already knows their specification. Navigation runs several layers deep into product family trees — drives, motors, sensors, PLCs, power supplies — with category breadth favored over hero imagery. Calls to action are declarative: "Add to Cart," "Request a Quote," "Check Availability." An accent orange distinct from the primary blue preserves CTA hierarchy between commercial actions and navigation actions, so quote requests never compete visually with browse links.

  Because the site was behind Cloudflare anti-bot protection during extraction (returning "Just a moment…"), only #313131 was confirmed. The primary blue and accent orange below are inferred from the Galco brand's widely visible industrial-blue and orange-highlight conventions and should be verified against live assets before committing to production components.

colors:
  primary: "#0066cc"
  primary-active: "#004fa3"
  primary-disabled: "#b3d1f5"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#e85000"
  accent-orange-active: "#c44400"
  success: "#2e7d32"
  warning: "#b45309"
  error: "#c62828"
  in-stock: "#2e7d32"
  out-of-stock: "#c62828"
  tag-bg: "#e8f0fb"
  tag-text: "#0066cc"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase
  table-header:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  label:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 8px 20px
    height: 36px
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 7px 20px
    height: 36px
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 20px
    height: 36px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 7px 10px
    height: 34px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 42px
    padding: 0 12px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.none}"
      width: 80px
  nav-bar-utility-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 28px
    paddingX: "{spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 44px
    paddingX: "{spacing.base}"
  category-megamenu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    columnGap: "{spacing.xl}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    imageAspect: "1 / 1"
    partNumberTypography: "{typography.part-number}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
  stock-badge-in-stock:
    backgroundColor: "{colors.in-stock}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  stock-badge-out-of-stock:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  stock-badge-call:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  part-number-tag:
    backgroundColor: "{colors.tag-bg}"
    textColor: "{colors.tag-text}"
    typography: "{typography.part-number}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowHeight: 36px
    alternateRowBackground: "{colors.surface-soft}"
  facet-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    checkboxAccentColor: "{colors.primary}"
    padding: "{spacing.md}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  rfq-form:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.label}"
    inputTypography: "{typography.body-md}"
    submitButton: "button-accent"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption-bold}"
    padding: "{spacing.xxl} {spacing.base}"

## Components

### Buttons

**`button-primary`** — A compact 36px-tall button at {rounded.xs} (2px) radius in {colors.primary} blue with {colors.on-primary} white label in {typography.button-md} bold Arial. The near-flush corners signal transactional utility over lifestyle friendliness. Hover darkens to {colors.primary-active}; disabled fades to {colors.primary-disabled}. Primary role: "Add to Cart" and checkout form submissions.

**`button-secondary`** — White fill with a {colors.primary} border and matching label text; same height and radius as `button-primary` so action rows stay vertically aligned. Used for secondary commercial actions alongside a primary — "Save to List," "Compare," "Download Datasheet."

**`button-accent`** — {colors.accent-orange} fill for the highest-priority commercial CTA: "Request a Quote," "Get Pricing," promotional banner calls. Hover shifts to {colors.accent-orange-active}. The distinct orange prevents hierarchy collapse when both blue and orange buttons appear on the same page.

**`button-ghost`** — Transparent background with {colors.primary} text label; minimal padding for use inside content areas ("View All Specifications," "See Related Products") without consuming visual weight.

### Search

**`search-bar`** — The dominant UI element: a full-width or header-pinned input with a 2px {colors.primary} border and a flush-right blue submit button ({rounded.none} on the join edge, creating a compound shape). Placeholder reads "Search by Part Number, Brand or Keyword" — foregrounding that the expected input is a technical identifier, not a browsing phrase. Covers the primary user job: confirm stock and pricing for a known part.

### Navigation

**`nav-bar`** — 44px, {colors.ink} (#313131) background carrying {colors.on-dark} white category links in {typography.nav-link} bold. The dark background separates global nav from the white product surface and reads as authoritative before any product thumbnail appears. The `nav-bar-utility-strip` above it — a {colors.primary} 28px strip — always shows phone number, account login, and order tracking, because B2B buyers frequently need to call a rep rather than complete an unassisted transaction.

**`category-megamenu`** — Full-width white panel triggered by hover on product family links. Zero border-radius, {colors.hairline} border on all edges. Column headers use {typography.title-sm} bold; item links use {typography.body-sm}. Columns map to top-level product families: Drives, PLCs, HMIs, Sensors, Safety, Power Supplies — category breadth favored over visual hierarchy.

### Product Cards

**`product-card`** — Compact card with a 1:1 white-background studio image, manufacturer name in {typography.caption} {colors.muted}, part number in {typography.part-number} monospace bold with `part-number-tag` pill, short title in {typography.body-sm}, and unit price in {typography.price-display}. Stock badge sits directly below price; it is the primary decision signal. Border is {colors.hairline} at rest; hover shifts to {colors.primary}. No lifestyle photography.

### Stock Badges

**`stock-badge-in-stock`** / **`stock-badge-out-of-stock`** / **`stock-badge-call`** — Three-state availability pills in {typography.badge} all-caps: green {colors.in-stock} for available inventory, red {colors.out-of-stock} for no stock, amber {colors.warning} for "Call for Availability." These are primary decision data — they appear identically on search results, product cards, and PDP pages so buyers never have to relearn the vocabulary.

### Spec Table

**`spec-table`** — Multi-column table with {colors.surface-soft} header rows in {typography.table-header} (12px bold all-caps), alternating row backgrounds for readability at high row counts, and {colors.hairline} borders on all edges. Row height is 36px — compact enough to surface 15–20 electrical parameters without scrolling on a 1280px viewport. Used for operating voltage, current ratings, certifications, and dimensional specs.

### RFQ Form

**`rfq-form`** — "Request a Quote" is a primary conversion path for non-stock, high-volume, or contract orders. Rendered as a contained panel on {colors.surface-soft} with {typography.label} bold field labels and standard inputs. The submit button uses `button-accent` orange to maintain the orange-for-commercial-intent hierarchy distinct from the blue navigation and add-to-cart actions.

### Category Tiles

**`category-tile`** — Square or landscape tiles on homepage and category landing pages. {colors.surface-soft} background, {colors.hairline} border at rest, {colors.primary} border on hover. Typography is {typography.title-sm} bold centered below a product-family icon or thumbnail. Surfaces Drives, PLCs, HMIs, Sensors, Safety in a scannable grid for buyers who know the product family but not the exact part.

### Footer

**`footer`** — {colors.surface-dark} (#1a1a1a) background with {colors.on-dark} white text. Multi-column layout: {typography.caption-bold} uppercase section headers, {typography.body-sm} link lists. Contains company contact info, phone numbers, certifications, and compliance marks. The dark footer anchors the page and reinforces the professional-supplier register distinct from the white product surface above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces megamenu; search bar full-width below nav strip; spec tables horizontally scrollable with right-edge gradient hint; RFQ form fields stack vertically |
| Tablet | 744–1128px | Two-column product grid; megamenu condenses to two columns; facet filters collapse to slide-over drawer triggered by "Filter" button; hero banner body text truncated to two lines |
| Desktop | 1128–1440px | Three- to four-column product grid; full megamenu on hover; facet filters in 240px left sidebar; search bar fixed in header at defined width |
| Wide | > 1440px | Layout constrained to ~1400px max-width, centered; side margins widen; column count unchanged; no additional breakpoint content |

### Touch Targets

- All buttons expand to 44px minimum height on touch viewports (`button-primary`, `button-accent`, `button-secondary` grow from 36px desktop)
- Stock badges are display-only; the adjacent "Add to Cart" button carries the tap target
- Facet filter checkboxes expand to a 24×24px touch area on mobile
- Category tiles minimum 44px tall in mobile list-view
- Pagination buttons maintain minimum 32×44px touch target via vertical padding extension

### Collapsing Strategy

- Megamenu collapses to a full-height slide-in drawer with accordion-style category expansion on mobile
- Left-rail facet filter becomes a bottom-sheet or full-screen overlay modal triggered by a sticky "Filter & Sort" bar
- Spec tables scroll horizontally within a fixed container; right-edge gradient indicates overflow content
- Top utility strip (phone, account, order tracking) folds into the hamburger drawer on mobile
- Product card images scale to 80×80px in mobile list-view; grid-view maintains square aspect at ~47% viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette severely under-extracted**: Cloudflare challenge page blocked live extraction; only #313131 (charcoal ink/nav) was confirmed. All other colors — primary blue, accent orange, surface tones, border values — are inferred from broadly visible Galco brand assets and industrial B2B conventions. Verify every non-ink color against live galco.com DevTools before production use.
- **No custom typeface detected**: all stacks are system fonts (Arial, Roboto, Helvetica Neue). Galco may serve a licensed typeface via CDN that was not accessible during blocked extraction. Check whether a custom font loads in an authenticated or unblocked session.
- **No meta theme-color tag**: the HTML head could not be inspected; primary brand color cannot be inferred from this signal.
- **Component-level spacing unverified**: padding, gap, and grid-column counts are estimated from industrial B2B conventions; require DevTools inspection on a live session.
- **Logo treatment unknown**: SVG vs. PNG, dimensions, and dark/light logo variants were not captured.
- **Dark mode support**: unknown; assumed light-only based on industrial-supplier precedent.
- **Motion and animation**: no transition timing, skeleton loaders, or hover animation data was extracted.
- **Promotional overlay and alert-banner patterns**: flash-sale banners, back-order alert banners, and cookie-consent styling were not visible during extraction.
