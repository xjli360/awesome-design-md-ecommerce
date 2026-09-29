---
version: alpha
name: "Promega"
source_url: "https://www.promega.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The life-science supply sector defaults to cold institutional blue, but Promega's interface opens on #fdb813 — a warm amber that runs from the navigation masthead through every primary CTA, communicating laboratory-grade optimism rather than corporate restraint. The color is genuinely anomalous: competing catalog sites reach for their respective shades of #0059b3 and regulatory gray; Promega brands itself with the color of reagent-vial labels warming under a biosafety cabinet. Below that amber anchor, the palette intentionally fragments into a product-line taxonomy legible at a glance. Blues (#0371bd, #2275d3, #048fef) shade molecular biology and cloning reagents; biology greens (#028845, #0eb58a, #4bc076) track genomics and cell-viability assay kits; teal (#317d8b) marks detection and instrument categories; mauve (#713a61) and violet (#660099) signal specialty or premium research lines; periwinkle-lavender (#7e8be4) appears in informational callouts and data-visualization strips. This is not aesthetic variety — it is a color-coded wayfinding system for researchers navigating a catalog numbering in the thousands of SKUs, each seeking the exact buffer or enzyme in under three clicks. Type runs Roboto across the full stack with Arial and Helvetica Neue as system fallbacks — no proprietary typeface, no variable-weight showmanship. Display hierarchy is built on size and weight contrast alone: 36px/700 at the hero level steps cleanly to 14px/400 body copy. Spare uppercase tracking at 11px/700 labels filter pills and section anchors, borrowing the fixed-abbreviation convention of laboratory signage — brief, unambiguous, scannable. Catalog numbers render in monospace to signal machine-copyability, a subtle but functional nod to scientists who paste SKUs into LIMS systems. Buttons sit on {rounded.sm} corners (4px), preserving the utilitarian geometry expected in professional procurement contexts; cards adopt {rounded.md} (6px); the canvas stays white (#ffffff) with #f1f1f1 surface-card fills and #ececec mid-tones for alternating table rows, importing the visual logic of a printed catalog into the screen. A 6px amber stripe anchors both the top nav and the footer top edge, framing every page in the brand's single voltage.

colors:
  primary: "#fdb813"
  primary-active: "#d99a00"
  primary-disabled: "#fce79a"
  on-primary: "#1c1c1c"
  accent-blue: "#0371bd"
  accent-blue-hover: "#0059b3"
  accent-blue-vivid: "#2275d3"
  accent-blue-bright: "#048fef"
  accent-green: "#028845"
  accent-green-mid: "#117744"
  accent-green-teal: "#0eb58a"
  accent-green-vivid: "#4bc076"
  accent-green-light: "#45c173"
  accent-teal: "#317d8b"
  accent-red: "#e20225"
  accent-mauve: "#713a61"
  accent-periwinkle: "#695e74"
  accent-lavender: "#7e8be4"
  accent-violet: "#660099"
  accent-amber-mid: "#f2cf5b"
  accent-amber-light: "#fdc746"
  ink: "#4d4d4d"
  body: "#515151"
  muted: "#a0a0a0"
  muted-soft: "#b0b0b0"
  hairline: "#c6c6c6"
  hairline-soft: "#d5d5d5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f1f1f1"
  surface-mid: "#ececec"
  surface-strong: "#e5e5e5"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-upper:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.08em
    textTransform: uppercase
  catalog-number:
    fontFamily: "'Roboto Mono', 'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "Roboto, Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
  xl: 24px
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
    padding: "10px 20px"
    height: 40px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "9px 19px"
    height: 40px
    border: "1px solid {colors.accent-blue}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-blue-hover}"
    border: "1px solid {colors.accent-blue-hover}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.accent-blue}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 48px 10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonIconColor: "{colors.on-primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
    topStripeBackgroundColor: "{colors.primary}"
    topStripeHeight: 6px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    headerTypography: "{typography.title-sm}"
    headerTextColor: "{colors.ink}"
    shadowColor: "rgba(0,0,0,0.10)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    catalogTypography: "{typography.catalog-number}"
    catalogTextColor: "{colors.muted}"
    priceTypography: "{typography.title-sm}"
    hoverBorderColor: "{colors.accent-blue}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.10)"
  product-line-chip:
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
    height: 22px
    textColor: "{colors.canvas}"
  application-badge:
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    minHeight: 380px
    ctaBackgroundColor: "{colors.canvas}"
    ctaTextColor: "{colors.primary-active}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    accentBarHeight: 4px
    hoverShadow: "0 4px 12px rgba(0,0,0,0.08)"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline}"
  catalog-number-tag:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
    typography: "{typography.catalog-number}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  data-table:
    headerBackgroundColor: "{colors.surface-card}"
    headerTypography: "{typography.label-upper}"
    headerTextColor: "{colors.ink}"
    rowBackgroundColor: "{colors.canvas}"
    rowAltBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "5px 14px"
    border: "1px solid {colors.accent-blue}"
    selectedBackgroundColor: "{colors.accent-blue}"
    selectedTextColor: "{colors.canvas}"
  alert-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.canvas}"
  alert-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkTextColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingTextColor: "{colors.canvas}"
    borderTopColor: "{colors.primary}"
    borderTopHeight: 4px

## Components

### Buttons

**`button-primary`** — Amber (#fdb813) fill with dark ink (#1c1c1c) text, 4px corners ({rounded.sm}), and 40px height. The amber fill against a white canvas is the site's most distinctive CTA signal — anomalous for a science catalog, immediately recognizable. Hover deepens to #d99a00; disabled drains to {colors.primary-disabled} with {colors.muted} text.

**`button-secondary`** — White fill with a 1px {colors.accent-blue} border and matching text, 40px height, same corner radius. Used for secondary actions like "Save to List," "Request Quote," and filter resets. Hover shifts fill to {colors.surface-card} and border to {colors.accent-blue-hover}.

**`button-ghost`** — Transparent background, {colors.accent-blue} text, no border. Appears inline within body copy, table footnotes, and breadcrumb navigation where a filled button would be visually heavy relative to surrounding content density.

### Search

**`search-bar`** — A 44px input with 1px {colors.hairline} border and an amber submit orb ({colors.primary} fill with dark icon) flush to the right inner edge. On focus, the border upgrades to a 2px {colors.primary} stroke — the amber ring is the site's most consistent interactive brand signal. Scientists enter catalog numbers (e.g. "C9941"), product names, or application keywords; when rendering catalog-number hints, use {typography.catalog-number} monospace inside the input hint layer.

### Navigation

**`nav-bar`** — 56px white bar anchored by a 6px {colors.primary} amber stripe along the very top edge. The stripe is the most persistent brand element on the site, appearing on all page types including utility and support pages. Product category links render in {typography.nav-link} (14px/500). On hover over a category, the mega-menu opens: a white panel with {colors.hairline-soft} border, grouped links beneath {typography.title-sm} category headers, with a shallow drop shadow.

### Product Cards

**`product-card`** — White fill, 1px {colors.hairline-soft} border, {rounded.md} corners. The product image sits on a {colors.surface-soft} pad; below it, the product name in {typography.title-sm} ink, and the catalog number in {typography.catalog-number} monospace muted gray — the monospace treatment is a functional signal that catalog numbers are machine-copyable. Price or "Login for Price" sits right-aligned in {typography.title-sm}. On hover, the border shifts to {colors.accent-blue} with a shallow drop shadow.

**`product-line-chip`** — Pill-shaped badge ({rounded.full}) that color-codes product lines using the full brand palette: blue (#0371bd) for molecular biology, green (#028845) for genomics and cell assay, teal (#317d8b) for detection and instruments, mauve (#713a61) for specialty research lines, violet (#660099) for premium or niche offerings. Typography is {typography.label-upper} — 11px, uppercase, 0.08em tracking — directly borrowing the abbreviation density of a reagent label.

**`application-badge`** — Neutral soft-gray pill ({colors.surface-mid} background, {colors.body} text, {typography.caption}) listing assay applications such as "PCR," "Protein Expression," or "Cell Viability." Multiple badges stack horizontally beneath the product title. No bright color — these are informational wayfinding, not navigational taxonomy, so they stay neutral against the color-coded product-line chips above them.

### Hero Banner

**`hero-banner`** — Full-width amber (#fdb813) fill, {colors.on-primary} dark-ink text. Display title in {typography.display-xl} (36px/700). Body copy in {typography.body-md}. The CTA inverts the standard button: white fill ({colors.canvas}) with {colors.primary-active} dark-amber text — reversing the primary button so the amber reads as banner background rather than interactive element. Minimum 380px tall; padding {spacing.xxl} vertical and {spacing.section} horizontal.

### Category Cards

**`category-card`** — {colors.surface-card} fill with a 4px top accent bar in the corresponding product-line color (matched to the `product-line-chip` palette above). {rounded.md} corners, 1px {colors.hairline-soft} border, title in {typography.title-md}. Hover lifts with `0 4px 12px rgba(0,0,0,0.08)` shadow. These cards populate the main product-category grid on the homepage, making the color-coded taxonomy visible at the highest navigation level.

### Catalog Number Tag

**`catalog-number-tag`** — An inline chip ({colors.surface-mid} fill, {rounded.xs}) rendering the SKU in {typography.catalog-number} monospace. Appears in product listings, search results, order history, and cart lines. The chip padding makes catalog numbers visually distinct from prose and easy to select for clipboard copy.

### Data Tables

**`data-table`** — Used extensively on technical data sheets and specification pages. Header row in {colors.surface-card} with {typography.label-upper} column labels in {colors.ink}; alternating body rows alternate between {colors.canvas} and {colors.surface-soft}; borders in {colors.hairline-soft}; cell text in {typography.body-sm}. No colored headers — the table prioritizes printability and data density over decorative branding.

### Filter Pills

**`filter-pill`** — Pill-shaped faceted-search toggles ({rounded.full}), 1px {colors.accent-blue} border, {colors.accent-blue} text, white fill when inactive. Selected state fills with {colors.accent-blue} and flips to white text. Used in the product-search sidebar for filtering by application, format, pack size, and product line.

### Alerts

**`alert-success`** — {colors.accent-green} (#028845) fill with white text and {rounded.sm} corners. Appears as a cart-add confirmation toast and form-submit success inline message. **`alert-error`** — {colors.accent-red} (#e20225) fill, white text, same radius. Used for out-of-stock notices and form validation failures.

### Footer

**`footer`** — Dark {colors.ink} (#4d4d4d) background with a 4px {colors.primary} amber stripe along the very top edge, mirroring the nav-bar stripe to close the amber frame around every page. Column headings in {typography.title-sm} {colors.canvas} white; links in {typography.body-sm} {colors.hairline-soft}. The amber top border is the only color element in an otherwise achromatic footer, ensuring the brand signature appears at both ends of every scroll.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with full-height side drawer; amber stripe persists at full width; search bar full-width below logo row; product grid 1-column; category cards stacked vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows logo, search, and hamburger for categories; mega-menu replaced by accordion within slide-in drawer; hero banner height reduces to 280px |
| Desktop | 1128–1440px | Full horizontal nav with mega-menu on hover; three-column product grid; hero banner at full 380px; sidebar filters visible alongside product grid as persistent left panel |
| Wide | > 1440px | Content max-width 1440px centered with expanding side margins; hero banner fills viewport width with centered content block capped at 960px |

### Touch Targets
- All buttons minimum 40px height, expanded to 44px on mobile for thumb reachability
- Filter pills padded to minimum 36px height on mobile
- Drawer nav links minimum 48px height
- Catalog-number-tag padding expands on mobile to 10px vertical to support long-press text selection for clipboard copy

### Collapsing Strategy
- Primary navigation collapses to hamburger at < 1128px; product categories move to a full-height side drawer with accordion sub-navigation
- Mega-menu degrades to stacked accordion panels within the drawer on tablet and mobile
- Faceted filter sidebar collapses to a modal filter sheet on mobile, triggered by a sticky "Filter & Sort" pill bar floating above the product grid
- Data tables scroll horizontally on mobile with a frozen first column (product name or property label) to preserve row context during horizontal scroll
- Footer collapses from four-column to two-column at tablet and single-column stacked at mobile; amber top stripe and dark fill persist at all widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom or licensed brand typeface detected; the entire stack resolves to Roboto, Arial, and Helvetica Neue. A proprietary display face may load via JS-injected CSS not captured in extraction.
- Exact button heights, input heights, and padding values are inferred from B2B catalog conventions — not confirmed from live CSS inspection.
- Catalog-number monospace font assumed to be Roboto Mono as a family companion; actual implementation may use system monospace fallback only.
- Product-line color-to-category mapping (which exact Promega product family maps to each chip color) requires verification against the live taxonomy — the palette suggests approximately six to eight distinct lines.
- Icon set style (outline vs. filled, stroke weight, corner treatment) not captured; Promega likely uses a custom SVG icon set for application and product-category glyphs.
- Animation and transition values (hover durations, menu slide timing, toast fade) not extracted.
- Dark-mode or high-contrast variant presence is unknown; site appears light-only from extraction data.
- E-commerce checkout flow, quote-request form, and account-portal UI may use a subset of this palette with additional utility states not documented here.
