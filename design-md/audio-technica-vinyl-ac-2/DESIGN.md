---
version: alpha
name: "Audio-Technica"
source_url: "https://www.audio-technica.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Audio-Technica's site runs Univers — the Swiss grotesque engineered for tabular specification data — in condensed and regular cuts that compress cartridge output impedance, frequency response ranges, and connector pinouts into scannable columns without sacrificing editorial authority. The palette centers on a deep engineering blue (#00558d) that carries primary CTAs and navigational rails, flanked by alert red (#e02b27) that fires on promotional badges and sale callouts, against an off-white canvas (#f4f3f1) textured enough to read as paper rather than screen. Dark navy (#002d5e) grounds footer blocks and section separators; the step from body text (#515153) down through muted (#6c6c6c) to hairline (#bdbdbd) describes a deliberate desaturation gradient that keeps catalog pages legible under high product-image density. A secondary red (#b50606) appears in hover states and error validation — darker and more serious than the promotional orange-red — and the brand operates two distinct reds without confusion because their semantic roles never overlap. The rounding vocabulary is deliberately conservative: buttons and form fields use a 4px radius rather than pill or large-radius shapes, communicating engineering neutrality over consumer friendliness. Product cards sit on white separated by thin #bdbdbd hairlines that echo the ruled tables of a technical datasheet. Spacing is generous in the vertical axis — 64px section whitespace keeps dense spec information from feeling cramped — while horizontal grid discipline aligns to a 12-column structure at 1440px desktop. Univers Condensed steps in for compact badges, model codes, and table headers where horizontal space is at a premium; Univers Medium handles body copy and spec labels. Helvetica Neue serves as the system fallback, preserving the same grotesque grammar. Audio-Technica does not use photography-as-hero in the typical DTC sense; instead, isolated product renders on neutral canvas backgrounds let the industrial form of a cartridge stylus or headphone driver speak without lifestyle staging.

colors:
  primary: "#00558d"
  primary-active: "#002d5e"
  primary-disabled: "#a6a6a6"
  accent-red: "#e02b27"
  accent-red-deep: "#b50606"
  accent-red-dark: "#6b0404"
  accent-pink: "#fc4c5e"
  navy-mid: "#1a334a"
  ink: "#0a0a0a"
  body: "#515153"
  muted: "#6c6c6c"
  muted-light: "#a6a6a6"
  hairline: "#bdbdbd"
  hairline-soft: "#efefef"
  canvas: "#f4f3f1"
  surface-soft: "#f1f1f1"
  surface-card: "#f5f5f5"
  surface-rule: "#d7dbd9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  warm-gray: "#dad6d2"
  cool-gray: "#ced7dd"

typography:
  display-xl:
    fontFamily: "'Univers Condensed', 'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Univers Medium', 'Univers Condensed', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Univers Regular', 'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Univers Regular', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Univers Condensed', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Univers Condensed', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  model-code:
    fontFamily: "'Univers Condensed', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Univers Condensed', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Univers Medium', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
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
    padding: 12px 24px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-red-active:
    backgroundColor: "{colors.accent-red-deep}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  nav-bar-utility:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-model:
    typography: "{typography.model-code}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    displayTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  hero-product-render:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-md}"
    padding: "{spacing.section}"
  search-bar:
    backgroundColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
  category-tab:
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
  category-tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  promo-banner:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  compare-checkbox:
    accentColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — Solid #00558d fill with white uppercase Univers Medium text at 15px and 0.3px letter spacing, 44px tall with a conservative 4px radius (`{rounded.xs}`). Active state drops to #002d5e navy; disabled grays out to #a6a6a6 with identical geometry. Audio-Technica does not use pill-shaped CTAs — the engineering neutrality of a near-square-cornered rectangle carries authority that a pill would undercut.

**`button-secondary`** — Transparent background with a 2px solid #00558d border and matching blue text in the same uppercase Univers Medium treatment. On hover the border fills solid, inverting to white text on blue. Height and radius match `button-primary` for consistent row alignment in comparison and configurator layouts.

**`button-red`** — Promotional variant in #e02b27 with the same geometry as primary. Used for sale event banners, limited-edition launch CTAs, and checkout flow entry points. Active deepens to #b50606 — the two reds are semantically distinct (promotion vs. error) and their contexts never ambiguate.

### Navigation
**`nav-bar`** — Two-tier bar: a thin 36px dark-navy utility strip (`nav-bar-utility`) above the 64px white main nav with a 1px #bdbdbd border-bottom. The main nav holds the AT logo at left, megamenu category links in Univers Medium 14px at center, and search/cart/account icon buttons at right. Category labels use `{typography.nav-link}` with no text-transform — the menu spans headphones, microphones, turntables, cartridges, and accessories without typographic overemphasis.

**`category-tab`** — Underline-style row below the main nav on catalog and sub-category pages. Inactive tabs render in #515153 body color; the active tab gains a 2px solid #00558d bottom border with blue text — a convention borrowed from data-table libraries that suits AT's spreadsheet-like browsing patterns.

### Product Card
**`product-card`** — White card with a 1px #efefef border and 4px radius sits on the #f4f3f1 page canvas. Product renders appear against the same canvas tone, making image edges seamless without a visible bounding box. Title uses `{typography.title-md}` in near-black; model code below steps to Univers Condensed 13px in muted gray, reflecting the catalog-database lineage of AT's alphanumeric product naming (AT-VM95E, AT-LP120XBT-USB). Price in `{typography.title-sm}`.

**`badge-sale`** and **`badge-new`** — Zero-radius rectangular chips pinned to the top-left of the card image. Sale uses #e02b27; New uses #00558d. Univers Condensed uppercase 11px with 0.4px tracking reads clearly at chip scale. No rounded corners — the hard edge matches the spec-table aesthetic.

### Spec Table
**`spec-table`** — The spiritual center of Audio-Technica product pages: a bordered table with #f1f1f1 header rows bearing Univers Condensed uppercase spec labels at 11px and 0.5px tracking over #f5f5f5 surface. Data cells use Univers Regular 14px in #515153. Thin #bdbdbd hairlines divide columns and rows; alternating rows stay white to preserve reading rhythm across 15–20 rows of cartridge frequency response, output impedance, or headphone driver specifications. Horizontal scroll activates at mobile breakpoints with the label column sticky-pinned left.

### Hero
**`hero-banner`** — Full-bleed section in #002d5e dark navy with white Univers Condensed headline at `{typography.display-xl}` and Univers Regular body at 16px. Padding of 64px vertical gives the headline room against the deep navy without requiring additional graphic decoration. Used for seasonal campaigns and product-line launches.

**`hero-product-render`** — Product-focused hero on #f4f3f1 canvas, centering an isolated product render with no lifestyle staging. Headline in `{typography.display-md}` ink color, `button-primary` CTA below. This is the dominant per-product-line hero pattern.

### Search
**`search-bar`** — White input field, 44px tall, 4px radius; unfocused border is #bdbdbd, focused border is 1px solid #00558d. Univers Regular 16px placeholder in #a6a6a6. A blue magnifying-glass icon button anchors the right edge. The border-color state change is the only animation — no shadow bloom, no background fill on focus.

### Promo Banner
**`promo-banner`** — A 36px strip anchored above `nav-bar-utility` in #e02b27 with centered Univers Condensed uppercase badge text announcing a sale threshold or free-shipping offer. When both promo and utility bars are active, the stacking order is promo → utility → nav-bar top-to-bottom.

### Footer
**`footer`** — Deep #0a0a0a near-black background with #ffffff body text and #bdbdbd link color. Univers Regular 14px for all copy. Four-column grid: product categories, support links, about/careers, and social icons. Copyright line and legal links render in `{typography.caption}` at 12px.

### Compare
**`compare-checkbox`** — A small checkbox and label below each product card on catalog pages, allowing up to four items for side-by-side spec comparison. Accent color #00558d; label in `{typography.caption}` Univers Condensed 12px. On mobile the control is hidden; comparison redirects to a dedicated compare page reached via product detail.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + hamburger + search icon; spec tables scroll horizontally with label column sticky; hero headline drops to display-sm (24px); promo banner text truncates to one line; compare control hidden |
| Tablet | 744–1128px | Two-column product grid; dual-tier nav retained but megamenu becomes full-width drawer overlay; spec table retains columns at reduced widths; category-tab row horizontally scrolls if overflow |
| Desktop | 1128–1440px | Three- or four-column product grid; full megamenu dropdown with column groupings; hero banner at full display-xl scale; compare feature active below cards |
| Wide | > 1440px | Max-width container ~1440px centered with flanking #f4f3f1 canvas gutters; no additional layout changes |

### Touch Targets
- All buttons maintain 44px minimum height
- Nav icons (cart, search, account) padded to 44×44px tap areas with 24px internal icon
- Category tabs on mobile use 48px height for reliable tap targeting
- Compare checkbox tap area padded to 44px height via surrounding label element

### Collapsing Strategy
- Category megamenu collapses to an accordion drawer on mobile with top-level items as expand triggers
- Product filter sidebar collapses to a slide-in bottom sheet on mobile and tablet
- Spec tables use horizontal scroll on mobile with first column (parameter label) sticky-pinned left
- Two-tier nav consolidates to single-height bar on mobile: AT logo left, hamburger + search right
- Section whitespace scales from 64px (desktop) to 40px (mobile) to preserve density without crowding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Univers numeric font weights (400/500/600/700) not confirmed from computed styles — weights here are estimated from the named cuts (Regular, Medium, Condensed)
- Precise button padding values not extracted from live computed styles; values are estimates consistent with 44px target height
- Megamenu column count, category groupings, and sub-nav structure not confirmed
- Product image aspect ratio (1:1 vs. 4:3 vs. custom) and hover overlay behavior not extracted
- Dark-mode support unknown — no prefers-color-scheme tokens extracted
- Animation easing curves and transition durations not captured
- Sticky header scroll behavior (shrink, shadow, hide-on-scroll-down) not confirmed
- Footer column count at tablet breakpoint not confirmed
- Cart drawer vs. dedicated cart page routing not extracted
- Exact breakpoint values used by AT's CSS grid not confirmed; values in this file are inferred from common AT grid patterns
