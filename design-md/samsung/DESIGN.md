---
version: alpha
name: "Samsung"
source_url: "https://www.samsung.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Samsung's refrigerator pages strip the product to center-frame isolation — each unit photographed on a near-white gradient, lit to expose the door-panel seam and handle geometry before a single specification appears. The single extracted brand voltage, #0c4da2, is a deep-navy sapphire that anchors every primary CTA, site-header link, and filter-chip highlight without competing with the stainless and matte-black appliance finishes that define the premium lineup. SamsungSharpSans carries all display-scale headings — a proprietary grotesque with compressed horizontal rhythm that reads as architectural at 48px while remaining composed at 18px; SamsungSSBody handles running copy and specification tables, and SamsungOne covers navigation micro-labels and badge text. Corner radii are deliberate but minimal: product cards use a near-square {rounded.sm} that reads as technical precision, while CTA buttons sit at {rounded.xs} — barely softened, enough to distinguish the interface from a CAD diagram without signaling friendliness. The refrigerator lineup includes the Bespoke modular-panel system (24 color combinations) and the Family Hub touchscreen line, requiring a color-picker component with circular swatch grids and a feature-comparison module spanning 4–6 columns. Spacing is generous at section breaks — the page breathes between hero, features, and spec rows — but compact inside specification tables to pack 12–18 attributes without scroll fatigue. The canvas holds pure white; {colors.surface-soft} (#f5f5f5) surfaces alternating table rows and filter-panel backgrounds; product photography carries all the color saturation the page requires.

colors:
  primary: "#0c4da2"
  primary-active: "#0a3d85"
  primary-disabled: "#8eb3d9"
  ink: "#1b1b1b"
  body: "#3c3c3c"
  muted: "#717171"
  hairline: "#e6e6e6"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1b1b1b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  filter-active-bg: "#e8f0fb"
  filter-active-border: "#0c4da2"
  energy-green: "#4caf50"
  bespoke-picker-border: "#c0c0c0"
  promo-badge-bg: "#e30019"
  promo-badge-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "SamsungSharpSans, SamsungOne, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "SamsungSharpSans, SamsungOne, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: -0.3px
  display-md:
    fontFamily: "SamsungSharpSans, SamsungOne, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "SamsungSharpSans, SamsungOne, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "SamsungOne, SamsungSSHead, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "SamsungOne, SamsungSSHead, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "SamsungSSBody, SamsungOne, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "SamsungSSBody, SamsungOne, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.571
    letterSpacing: 0
  caption:
    fontFamily: "SamsungSSBody, SamsungOne, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  spec-label:
    fontFamily: "SamsungSSHead, SamsungOne, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "SamsungSharpSans, SamsungOne, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: -0.2px
  button-md:
    fontFamily: "SamsungOne, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "SamsungOne, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "SamsungOne, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "SamsungOne, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 12px 28px
    height: 48px
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
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 48px
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
  nav-bar-mega:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    columnCount: 5
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "0 {spacing.xxl}"
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  feature-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    iconSize: 48px
    padding: "{spacing.section} {spacing.xxl}"
    columnCount: 3
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    altRowBg: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    cellPadding: "10px {spacing.base}"
  compare-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    columnMinWidth: 200px
    maxColumns: 6
  compare-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    height: 64px
    position: fixed
    bottom: 0
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.filter-active-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.filter-active-border}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  bespoke-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    outline: "2px solid {colors.bespoke-picker-border}"
    gridColumns: 8
  energy-badge:
    backgroundColor: "{colors.energy-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-badge:
    backgroundColor: "{colors.promo-badge-bg}"
    textColor: "{colors.promo-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackground: "{colors.primary}"
    activeText: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    size: 36px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"

---

## Components

### Buttons

**`button-primary`** — Fills #0c4da2 with white lettering at {typography.button-md} (16px/600), 48px height, and {rounded.xs} corners. Hover darkens to `primary-active` (#0a3d85); disabled falls to a muted periwinkle at {colors.primary-disabled} while keeping the button shape legible. Appears on "Add to Cart", "Buy Now", and filter-apply actions.

**`button-secondary`** — White background, #0c4da2 border and text at 2px stroke, matching the height and radius of `button-primary`. Applied to "Compare", "Learn More", and secondary navigation CTAs. The `button-secondary-dark` variant uses a transparent background with white border and text for placement over dark hero backgrounds.

**`button-text-link`** — Transparent, primary-blue text at {typography.button-sm}. Used for "See All →" inline links within feature blocks and spec callouts. Color shifts to `primary-active` on hover; no underline at rest.

### Text Input

**`text-input`** — 48px tall, {rounded.xs}, 1px {colors.hairline} border at rest. On focus the border shifts to 1px {colors.primary}. Typography at {typography.body-md} (16px) prevents iOS auto-zoom. Deployed in site search, product registration forms, and retailer locator fields.

### Navigation

**`nav-bar`** — 56px white bar with 1px {colors.hairline} bottom border. Samsung logo left at 28px height; search, account, and cart icons cluster right. On scroll, the mega-panel collapses and the bar tightens. **`nav-bar-mega`** deploys on hover as a full-width white panel with up to 5 product-category columns, section headers in {typography.spec-label} uppercase, and product-thumbnail links at {typography.body-sm}. A thin 1px {colors.hairline} top border anchors the panel to the nav bar.

### Product Card

**`product-card`** — White card, 1px {colors.hairline-soft} border, {rounded.sm} radius, {spacing.base} padding. The product image occupies the upper ~60% of the card on a {colors.surface-soft} field. Model name in {typography.title-sm}; price in {typography.price-display} at 24px/700. A badge row below the image accommodates `promo-badge` and `energy-badge` chips. On hover the card lifts with a `box-shadow` increment; border color does not change, preserving the quiet grid rhythm.

### Hero

**`hero-full-bleed`** — Full-viewport-width dark hero, product silhouette right-aligned on a {colors.surface-dark} or dark-gradient field, copy left-aligned. Title at {typography.display-xl} (52px/700/−0.5px tracking), subhead at {typography.body-md} white. Two CTAs — `button-primary` and `button-secondary-dark` — sit beneath at {spacing.base} gap. Minimum 560px height; on wide viewports the image scales to fill the right half without cropping.

**`hero-split`** — Lighter alternative for mid-page Bespoke customization and seasonal promotional blocks. {colors.surface-soft} background, {colors.ink} text, product image right, copy left. Title at {typography.display-lg} (40px/700). Used when the brand needs warmth rather than drama.

### Feature Block

**`feature-block`** — White section, 3-column grid on desktop, 48px icon above a {typography.display-sm} heading and {typography.body-md} body. Used for repeated capability callouts — Twin Cooling Plus, AI Energy Mode, SpaceMax Technology. Section padding {spacing.section} top and bottom creates breathing room between content clusters.

### Spec Table

**`spec-table`** — Two-column key/value table. Column-one headers in {typography.spec-label} (12px/600/uppercase); values in {typography.body-sm}. Alternating rows use {colors.surface-soft}; all four edges carry 1px {colors.hairline}. Cell padding 10px {spacing.base}. On mobile the table gains a horizontal-scroll wrapper rather than collapsing columns, preventing label truncation across 12–18 attribute rows.

### Compare Table

**`compare-table`** — Multi-column grid for side-by-side model comparison (max 6 units). Header row in {colors.surface-soft} with model names at {typography.title-sm}; attribute rows use {typography.spec-label} for labels and {typography.body-sm} for values. Each column has a 200px minimum width with horizontal scroll on overflow. A sticky first column holds the attribute labels on all viewport sizes.

### Compare Bar

**`compare-bar`** — Fixed 64px bar pinned to the viewport bottom, visible once the user selects 2+ products via checkbox. {colors.surface-dark} background, {colors.on-dark} text, and a `button-primary` "Compare Now" CTA at the right edge. Selected product thumbnails appear as 40px squares with remove-X icons. The bar disappears when the comparison count drops below 2.

### Filters

**`filter-chip`** and **`filter-chip-active`** — Pill-shaped toggles at {rounded.full} using {typography.body-sm}. Default state: white fill, 1px {colors.hairline} border, {colors.ink} text. Active state: {colors.filter-active-bg} fill, 1px {colors.filter-active-border} border, {colors.primary} text. Chips wrap to two rows on mobile before a "Show More" expander reveals the remainder.

### Bespoke Color Picker

**`bespoke-swatch`** — 32px circular swatches at {rounded.full} filled with the panel color. Default state has a 2px transparent inner border and a 2px {colors.bespoke-picker-border} outer outline. Selected state switches to a 2px {colors.primary} inner border with a 3px gap between fill and border, creating a visible selection ring. Arranged in an 8-column grid with color-name tooltip on hover, narrowing to 6 columns on tablet and 5 on mobile while maintaining the 32px swatch size.

### Badges

**`energy-badge`** — #4caf50 green badge for EU/KR energy-efficiency ratings. {typography.badge} in uppercase, {rounded.xs}, 3px 8px padding. Stacks above the price on product cards and PDPs.

**`promo-badge`** — #e30019 red badge for "Sale", "New", and limited-offer labels. Identical shape and typography to `energy-badge`; the two may stack vertically on the card image corner with {spacing.xxs} gap.

### Breadcrumb

**`breadcrumb`** — {colors.muted} caption-scale links at {typography.caption}, separated by "/" glyphs in {colors.hairline}. Appears 12px below the nav bar on PDP and category pages.

### Pagination

**`pagination`** — Row of 36×36px square page-number buttons at {rounded.xs}. Active page fills {colors.primary} with {colors.on-primary} text. Inactive pages hold white with {colors.ink} text. Previous/Next chevron buttons share the same dimensions and radius.

### Footer

**`footer`** — Full-width {colors.surface-dark} footer with 4–5 link columns, each headed by a {typography.title-sm} label in white. Links at {typography.body-sm} white. A bottom strip carries legal copy at {typography.caption} and a regional/language selector.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero switches to full-bleed portrait crop with title scaled to `display-md`; filter chips collapse to horizontally scrolling row; spec and compare tables gain horizontal-scroll wrapper; compare bar stacks to two rows; nav collapses to hamburger drawer |
| Tablet | 744–1128px | 2-column product grid; hero retains split layout but title scales from `display-xl` to `display-lg`; filter sidebar becomes top-mounted sheet; mega nav reduces to 3 columns; bespoke swatch grid narrows to 6 columns |
| Desktop | 1128–1440px | 3–4 column product grid; full mega nav active; hero at full 560px height; feature blocks in 3-column grid; spec and compare tables at full column width |
| Wide | > 1440px | Content locks at 1440px max-width centered; hero image scales to fill right panel; feature blocks may expand to 4 columns; footer column widths increase with whitespace padding |

### Touch Targets

- All interactive elements minimum 44×44px effective tap target; filter chips and bespoke swatches use padding to reach 44px even when visually smaller
- Compare-bar buttons hold minimum 48px height for comfortable thumb reach at the viewport bottom
- Mobile nav items minimum 48px height with {spacing.base} left padding
- Pagination buttons render at 44px on mobile (expanded from 36px desktop)

### Collapsing Strategy

- Navigation: full mega nav on desktop → 2-level dropdown on tablet → hamburger with slide-in overlay drawer on mobile
- Filters: sticky left sidebar on desktop → top-mounted chip row on tablet → collapsible bottom sheet triggered by a "Filter" button on mobile
- Feature blocks: 3-column icon grid → 2-column → single-column with full-width feature images
- Spec table: horizontal scroll wrapper on all viewports narrower than the table's natural width; no column hiding or data suppression
- Bespoke swatch picker: 8-column → 6-column → 5-column, maintaining 32px swatch size throughout
- Compare table: horizontal scroll on tablet and mobile; first attribute column remains sticky

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#0c4da2) was extractable from the live site; the full Samsung design-token palette including dark-mode surfaces, gradient stop values, and interactive state shades could not be confirmed
- All neutral color values (body, muted, hairline, surface-soft, surface-dark) are inferred from Samsung's general brand language rather than extracted values
- Samsung's global brand standard may specify #1428A0 as the canonical brand blue; the extracted #0c4da2 comes from Samsung Japan's theme-color meta tag and may reflect a regional override
- Exact font metric data (precise line-height ratios and letter-spacing values) is inferred from Samsung's documented proprietary type system; optical sizing was not extractable from the live site
- Button and card border-radius values could not be confirmed from extraction; {rounded.xs} (4px) is inferred from visual analysis of samsung.com
- Bespoke panel color system (24 finish options with specific hex values per color name) was not extractable and is omitted from the palette
- Family Hub touchscreen interface component specifications (widget grid, app launcher, camera feed overlay) were not extractable and are not represented in components
- Hover animation timing, transition curves, and scroll-triggered entrance animations could not be extracted and are not specified
