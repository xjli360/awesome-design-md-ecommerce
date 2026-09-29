---
version: alpha
name: "Citizen"
source_url: "https://www.citizenwatch.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Five distinct product lines — Eco-Drive, Promaster, Satellite Wave, Calendrier, and Attesa — each carry a separate color chapter on citizenwatch.com, yet all route back to a single deep navy (#253a63) that inhabits the top navigation, primary CTAs, and collection-banner fills simultaneously. The brand's engineering argument is treated as a design asset rather than footnote: Eco-Drive's light-conversion technology earns dedicated iconography and a standalone explainer block on nearly every collection page, sitting in-grid alongside specifications rather than buried in a FAQ accordion. Against that navy anchor, three accent stories emerge from the extracted palette — a brick rust (#a13c2e and its deeper sibling #541f18) for Promaster land collections; a shadowed forest green (#364d3b paired with #1c281f) for dive and field references; and a warm gold-caramel (#c79f70) that lifts dress-watch listings above the sport grid without invoking the jeweler's register. Surface hierarchy descends from a warm near-off-white (#e0ded9, {colors.surface-soft}) through a deeper sand tone (#e8d8c5, {colors.surface-warm}) to the deep navy itself, keeping dial photography always reading forward against a receding ground. Typography resolves entirely to Helvetica Neue at light weights — 300 for display, 400 for body — with uppercase small-caps labels carrying 1–1.5px tracking, a convention borrowed from instrument-panel and spec-sheet labeling rather than retail warmth. Model numbers (e.g. "BM8550-14E") are set in Courier New, the one monospace face in the detected stack, a literal nod to the SKU-dense watchmaker catalog that distinguishes a 40mm dive bezel from its 44mm sibling at a glance. Buttons carry uppercase tracked type and a tight {rounded.xs} corner — no pill shapes, no hard 0px angles — landing at the precise midpoint between technical discipline and consumer approachability. The overall system reads closer to an engineer's portfolio than a jeweler's showcase, which aligns with Citizen's positioning as the brand whose premium justification is function demonstrated before finish admired.

colors:
  primary: "#253a63"
  primary-active: "#131e33"
  primary-disabled: "#73859f"
  accent-rust: "#a13c2e"
  accent-rust-dark: "#541f18"
  accent-green: "#364d3b"
  accent-green-dark: "#1c281f"
  accent-gold: "#c79f70"
  accent-warm-brown: "#67533a"
  accent-terracotta: "#ae7867"
  ink: "#1b1e21"
  body: "#2b333f"
  muted: "#53514d"
  muted-soft: "#818182"
  hairline: "#c2c8d3"
  hairline-soft: "#e0ded9"
  canvas: "#ffffff"
  surface-soft: "#e0ded9"
  surface-card: "#f5f5f2"
  surface-warm: "#e8d8c5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  blue-mid: "#73859f"
  blue-light: "#718fca"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  label-uppercase:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  model-number:
    fontFamily: "Courier New, Consolas, Liberation Mono, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
  price:
    fontFamily: "Helvetica Neue, Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.2
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
    padding: 12px 28px
    height: 44px
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
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-outline-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    logoColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBg: "{colors.canvas}"
    titleTypography: "{typography.title-md}"
    modelTypography: "{typography.model-number}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
  collection-banner:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    labelTypography: "{typography.label-uppercase}"
    accentColor: "{colors.accent-gold}"
    minHeight: 320px
    padding: "{spacing.xxl}"
  collection-card-promaster:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    accentColor: "{colors.accent-gold}"
    padding: "{spacing.xl}"
  collection-card-eco:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    accentColor: "{colors.accent-gold}"
    padding: "{spacing.xl}"
  eco-drive-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    accentColor: "{colors.accent-gold}"
  technology-block:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    iconColor: "{colors.primary}"
  collection-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 20px
    height: 40px
  collection-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 20px
    height: 40px
  series-filter:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
    typography: "{typography.title-sm}"
    height: 48px
  watch-spec-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.label-uppercase}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "12px 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    mutedTextColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons
**`button-primary`** — Filled {colors.primary} navy (#253a63) with uppercase tracked type at {typography.button-md} (14px, weight 600, 1px letter-spacing) and a 4px {rounded.xs} radius that reads restrained rather than clinical. Hover deepens to {colors.primary-active} (#131e33) with no scale transform — the state change is a value shift, not motion. Disabled state applies {colors.primary-disabled} (#73859f), the mid blue-gray, preserving button shape without suggesting interactivity.

**`button-secondary`** — White canvas with a 1px {colors.primary} border and matching text, dimensionally identical to the primary. Sits adjacent to the primary CTA on PDPs for secondary actions (save, compare, find a retailer). Active state firms the border to {colors.primary-active}.

**`button-outline-dark`** — Transparent fill with white border and {colors.on-dark} text, deployed exclusively on navy or dark-green hero banners where canvas buttons would dissolve. Shares uppercase tracking and {rounded.xs} with the primary for family consistency.

### Navigation
**`nav-bar`** — 64px tall, white canvas, 1px {colors.hairline} bottom rule. Logo renders in {colors.primary}. Top-level links use {typography.nav-link} (13px, weight 500, 0.5px tracking) — subdued enough that the nav reads as a utility rail rather than a brand billboard. On collection landing pages the bar swaps to `nav-bar-dark`, filling with {colors.primary} so the navigation merges flush into the hero banner below it rather than floating as a separate layer.

### Product Card
**`product-card`** — Light {colors.surface-card} fill with the watch image centered on a pure white tile. Title in {typography.title-md}, model reference number in {typography.model-number} (Courier New, 12px) — the monospace choice signals catalog precision, differentiating a BM8550 from a BM8553 at scan speed. Price renders in {typography.price} at 20px weight 300. A 1px {colors.primary} border appears on hover without layout shift. The {rounded.xs} corner (4px) is consistent with every container in the system.

### Hero Banner
**`hero-banner`** — Full-width, 560px minimum height, {colors.primary} navy fill. Display type at {typography.display-xl} (52px, weight 300) — the light weight is deliberate; dial photography carries the visual mass and the headline describes rather than commands. `hero-banner-light` swaps in {colors.surface-soft} (#e0ded9) for campaign pages targeting dress or vintage-adjacent collections, reading close to ivory against browser chrome.

### Collection Banners
**`collection-banner`** — Deeper than nav navy, {colors.primary-active} (#131e33) fill, used for product-line landing section headers. Collection name at {typography.display-md} weight 300; an uppercase label at {typography.label-uppercase} sits above as a category identifier. A {colors.accent-gold} ruled line or icon fill distinguishes premium sub-lines within a collection.

**`collection-card-promaster`** and **`collection-card-eco`** — Full-bleed color tiles in the collection-split grid: forest {colors.accent-green} (#364d3b) for Promaster categories, {colors.primary} navy for Eco-Drive. Both carry {colors.accent-gold} as an accent pin marking the active sub-line. White type on both using {typography.title-md} for the collection name and {typography.label-uppercase} for the category descriptor.

### Technology Badge & Block
**`eco-drive-badge`** — A compact inline badge on product cards with {colors.primary} fill, {typography.label-uppercase} type, and a {colors.accent-gold} accent element (icon or ruled line). Surfaces the Eco-Drive power type at browse level so users can filter by technology without entering a PDP.

**`technology-block`** — Full-width or two-column section in warm sand ({colors.surface-warm}, #e8d8c5) explaining Eco-Drive, Super Titanium, or GPS Satellite Sync. Title at {typography.title-md}, body at {typography.body-sm}; icon fills in {colors.primary}. The sand background separates editorial content zones from the product grid without a hard border.

### Filters & Tabs
**`collection-tab-active`** / **`collection-tab-inactive`** — Paired tab buttons for product-line carousels. Active: solid {colors.primary} fill, white text. Inactive: transparent fill, 1px {colors.hairline} border, {colors.muted} text. Both at {typography.button-sm} (12px, uppercase, 1.2px tracking) and {rounded.xs}, 40px height.

**`series-filter`** — A sticky 48px strip below collection heroes, white canvas with a {colors.hairline} bottom rule. The active filter item renders a 2px {colors.primary} bottom indicator line. Labels use {typography.title-sm} (uppercase, 1px tracking) — the same register as button labels, keeping the filter strip visually unified with the tab system.

### Spec Row
**`watch-spec-row`** — Two-column layout in the technical specifications accordion on PDPs. Left column: {typography.label-uppercase} label (Water Resistance, Case Diameter, Movement, Lug Width). Right column: {typography.body-sm} value. Rows divided by {colors.hairline-soft}. The monospace model number from the product card reappears here in the Movement field for internal consistency.

### Search
**`search-bar`** — {colors.surface-card} fill, 1px {colors.hairline} border focusing to {colors.primary}. Search icon in {colors.muted}, placeholder text in {colors.muted-soft}. 44px height, {rounded.xs} corner matching all interactive inputs.

### Footer
**`footer`** — Near-black {colors.ink} (#1b1e21) fill creates a definitive page terminus. Section headings at {typography.label-uppercase} (uppercase, 1.5px tracking, weight 600), links at {typography.body-sm} in {colors.on-dark}, secondary links in {colors.muted-soft}. Country/language selector renders as a flag-icon row in {colors.muted-soft}. No border-top — the color transition from page to footer is the delimiter.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero drops to 400px, headline and CTA stack vertically; series-filter scrolls horizontally; collection tabs wrap to two rows |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level items without mega-menu hover panels; hero at 480px; technology blocks shift to side-by-side icon + text |
| Desktop | 1128–1440px | 3- to 4-column product grid; full mega-menu nav with collection imagery per panel; hero at 560px; nav-bar-dark merges with hero on collection pages |
| Wide | > 1440px | Max content width ~1400px centered; hero crops to wide cinematic ratio; 4-column grid with widened gutters; footer columns expand to 5-up layout |

### Touch Targets
- All buttons minimum 44px height
- Nav items padded to 48px tap zones on mobile via expanded hit area
- Product card image zone uses full-card tap area, not text-label-only
- Collection tabs minimum 40px height with 16px horizontal padding
- Spec rows minimum 44px touch height in PDP accordion

### Collapsing Strategy
- Mega-menu condenses to accordion drawer on mobile, organized by collection line (Eco-Drive, Promaster, Satellite Wave) rather than flattened links
- PDP specification accordion defaults to collapsed on mobile; Movement and Water Resistance rows pre-expanded as highest-priority specs
- Technology block stacks icon above copy vertically below 744px
- Collection banner label + title + CTA restack from horizontal-split to vertical center-aligned below 744px
- Footer columns collapse from 4-up to 2-up at tablet, then single stacked list at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface captured — the full font stack resolves to system fonts (Helvetica Neue, Arial, -apple-system). Citizen's live site likely loads a proprietary or licensed sans-serif via JavaScript after initial CSS parse; this was not captured in extraction.
- `#e83e8c` appears in the extracted palette but is Bootstrap's default `$pink` variable — a framework artifact, not a brand color; excluded from the token set above.
- `surface-card` (#f5f5f2) and `canvas` (#ffffff) are inferred near-whites; no explicit light-surface hex was captured in the extraction.
- No meta theme-color declared, blocking mobile browser chrome color inference.
- Dark-mode or high-contrast alternate-theme configurations not captured.
- Exact hover animation timing, easing curves, and image-zoom behavior on product cards require JS instrumentation to document accurately.
- Regional sub-site palette differences (Japan, UK, Europe) not analyzed — extraction reflects the global .com only.
- Logo SVG geometry and exact lockup proportions not confirmed from extraction.
