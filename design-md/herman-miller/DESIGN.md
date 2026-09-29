---
version: alpha
name: "Herman Miller"
source_url: "https://www.hermanmiller.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The red at the center of every Herman Miller call-to-action — #e22d00 — reads like powdercoated industrial steel rather than brand-book scarlet: hot enough to stop a page scan cold, grounded enough to sit beside Aeron mesh and walnut-veneer photography without competing. FF Meta Headline W05 carries the display work, Erik Spiekermann's humanist sans-serif engineered to function under newsprint compression; its slightly open apertures and ink-trap geometry give product-catalog headlines a workmanlike warmth that Swiss grotesks would flatten. The canvas settles at #fafafa — not pure white but a near-white that extends reading endurance across specification-heavy product pages — with ink at #252525, a near-black that delivers strong contrast without the harsh cold snap of true black on true white.

  The interaction grammar is strikingly restrained. Primary buttons hold #e22d00 with white text and a near-zero corner radius ({rounded.xs}), leaning geometric rather than friendly — the form recalls machined product components more than soft consumer apps. A secondary blue (#0073ce) steps in for navigation links and anchor text, creating a two-voltage system where red means "transact" and blue means "navigate." Warm taupe (#ceb4a9) surfaces in material-swatch thumbnails and lifestyle washes, quietly anchoring the brand in natural materials without over-decorating. The near-black gray family — #252525, #464646, #4c4c4c, #616161 — runs body copy and structural chrome, producing a catalog that reads measured and professional at every zoom level.

  Corners are architectural: buttons and cards use {rounded.xs}-to-{rounded.sm} radii (2–4px), rejecting the pill shapes common in consumer brands. The grid breathes with {spacing.section} vertical rhythm between product sections and {spacing.xl} internal card padding, signaling confidence that the products can hold attention without being compressed together. Material Icons supplement the type system for interactive affordances — filters, configurators, share actions — maintaining single-supplier icon coherence across the shopping and research experience. Herman Miller's digital presence reads less like a retail storefront and more like a design firm's catalog: disciplined, unsentimental about decoration, and organized around the premise that the product's geometry is persuasion enough.

colors:
  primary: "#e22d00"
  primary-active: "#a81910"
  primary-disabled: "#f2dede"
  primary-dark: "#601b15"
  ink: "#252525"
  body: "#464646"
  muted: "#616161"
  muted-soft: "#b3b3b3"
  hairline: "#ebebeb"
  hairline-soft: "#e1e1e1"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  charcoal: "#323131"
  neutral-mid: "#4c4c4c"
  accent-blue: "#0073ce"
  accent-blue-active: "#0069bc"
  warm-taupe: "#ceb4a9"
  error-fill: "#f2dede"
  error-border: "#ebccd1"

typography:
  display-xl:
    fontFamily: "'FF Meta Headline W05', 'Meta', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'FF Meta Headline W05', 'Meta', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'FF Meta Headline W05', 'Meta', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'FF Meta Headline W05', 'Meta', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Meta', 'FF Meta Headline W05', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Meta', 'FF Meta Headline W05', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Meta', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Meta', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Meta', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Meta', 'FF Meta Headline W05', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Meta', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Meta', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'FF Meta Headline W05', 'Meta', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Meta', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  breadcrumb:
    fontFamily: "'Meta', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.error-fill}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 12px
    height: 44px
    placeholderColor: "{colors.muted}"
  text-input-error:
    border: "1px solid {colors.primary}"
    backgroundColor: "{colors.error-fill}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 40px 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
    padding: "0 {spacing.xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    hoverTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: 4/3
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
  product-card-hover:
    border: "1px solid {colors.charcoal}"
    boxShadow: "0 2px 8px rgba(37,37,37,0.12)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  category-badge:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
    linkColor: "{colors.accent-blue}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
  material-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
    accentColor: "{colors.warm-taupe}"
  specification-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    borderColor: "{colors.hairline}"
    rowPadding: 10px 16px
    rounded: "{rounded.none}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.title-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Herman Miller's primary button fills #e22d00 on a 2px corner radius, set in uppercase FF Meta at weight 600 with 0.5px tracking. The near-zero radius reads as a machined component rather than a friendly consumer affordance. Hover darkens the fill to #a81910; disabled renders a pale pink fill (#f2dede) with muted text, preserving the uppercase geometry.

**`button-secondary`** — White canvas with a 1px solid #252525 ink border and identical uppercase tracking to the primary. Hover shifts the background to #fafafa. Used for secondary actions in configurator panels and modal dialogs where the red CTA would compete with product photography.

**`button-ghost`** — Transparent background with #e22d00 text and an underline; no border, no radius. Used for tertiary actions within description blocks, specification sheets, and inline editorial links.

### Text Inputs

**`text-input`** — 44px tall, 1px #ebebeb border at rest that steps to 1px #252525 ink on focus — no color-wash ring, maintaining catalog formality. Error state draws a 1px #e22d00 border with a #f2dede fill behind the text. Placeholder text runs in #616161 muted.

**`search-bar`** — Identical to text-input in form, with right-side icon gutter (40px padding-right) for a Material Icons search glyph in #616161. The bar sits prominently in the top nav on desktop; on mobile it expands full-width below the logo strip.

### Navigation

**`nav-bar`** — 64px tall white bar with a 1px #ebebeb hairline bottom border. Logo aligns left at 28px height; primary categories render in 14px Meta weight 500. The active category receives a 2px #e22d00 bottom border. Cart and account icons use Material Icons at 24px. A utility row above the main nav carries shipping/support links in 12px caption.

**`nav-link`** — Hover state switches text to #e22d00; active underline is 2px solid primary. On desktop, hovering a primary category opens a mega-menu flyout anchored to the nav bottom edge.

### Product Card

**`product-card`** — Zero border radius, 1px #ebebeb border, 4:3 image ratio. Price displays in 24px FF Meta Headline weight 600; product title in 16px Meta semibold; series or collection label in 12px uppercase spec-label. On hover, the border steps to #323131 charcoal and a 2px shadow lifts the card off the grid. Sale badges (red) and category badges (charcoal) pin to the top-left of the image area.

### Hero

**`hero`** — Full-width band on #fafafa, minimum 560px tall on desktop. Headline at 48px display-xl, subtext at 16px body-md, left-aligned. Photography bleeds from the right half or occupies the full background behind a gradient scrim. A single primary button sits left-aligned below the subtext with {spacing.lg} top gap.

### Badges

**`category-badge`** — Zero-radius label in #323131 charcoal with white uppercase spec-label text (12px, 0.8px tracking). Applied to product-card corners to identify collection or product line. **`sale-badge`** — Same geometry and typography in #e22d00 primary; appears only during promotional events and adjacent to marked-down prices.

### Filter Chips

**`filter-chip`** — 4px-radius chip, 1px #ebebeb border, 14px body-sm text. Active state inverts to #252525 fill with white text and a matching border. Used in category browse sidebars and search refinement bars; on mobile they scroll horizontally in a single overflowing row.

### Material Swatches

**`material-swatch`** — 32px circle, 2px transparent border at rest; selection draws a 2px #252525 ink border. Swatches cluster in rows with 4px gaps. Warm taupe (#ceb4a9) appears frequently as a default finish for upholstered and woven options. The full swatch set scrolls horizontally on product detail pages when options exceed available width.

### Specification Table

**`specification-table`** — Borderless table on #fafafa with #ebebeb hairline row dividers, no corner radius. Row labels in 12px uppercase Meta with 0.8px tracking and weight 700; values in 14px body-sm weight 400. Used below the fold on every product detail page; on mobile, rows collapse into an accordion with one attribute group visible at a time.

### Configurator Panel

**`configurator-panel`** — White panel, 1px #ebebeb border, no radius, 32px internal padding. Hosts material swatches, fabric pickers, dimension inputs, and quantity selectors. Panel headline runs at 18px title-md (Meta semibold). On desktop the panel sits to the right of the product hero image in a fixed sticky container; on tablet and below it stacks beneath the image.

### Footer

**`footer`** — #252525 near-black fill with a 3px #e22d00 top border stripe — the one place the primary red functions as structural chrome rather than a CTA. Column headers in 16px title-sm semibold white; links in #b3b3b3 muted-soft, hover-transitioning to white. The bottom sub-row holds legal copy in 12px caption and social icons via Material Icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + hamburger + cart; filter panel becomes full-screen bottom sheet; hero drops to 360px min-height; display-xl scales to 28px |
| Tablet | 744–1128px | Two-column product grid; top nav shows primary categories only with no mega-menu; configurator panel moves below product image; hero at 420px min-height |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu flyouts; side-by-side configurator layout; hero at full 560px+ |
| Wide | > 1440px | Four-column grid option; content max-width 1440px centered; section padding scales to 80px; hero can extend to full viewport width |

### Touch Targets
- All buttons minimum 44×44px tap area on mobile
- Material swatches expand hit area to 40×40px even when visually rendered at 32px
- Nav links padded to 44px vertical touch target in mobile menu
- Filter chips minimum 36px height on touch viewports
- Breadcrumb links padded to 36px height

### Collapsing Strategy
- Specification tables collapse to accordion groups on mobile, one attribute section expanded at a time
- Configurator panel stacks below the product image on tablet and below; sticky behavior disabled at mobile
- Footer columns collapse to a single vertical stack on mobile with expand/collapse toggle per column heading
- Multi-image product gallery converts from grid to horizontal swipe carousel at mobile breakpoint
- Primary navigation reduces to logo + hamburger + cart icon on mobile; full category tree renders in a left-edge slide-in drawer
- Mega-menu flyouts on desktop become drill-down panels within the mobile drawer

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Border-radius values not confirmed from extraction — inferred from Herman Miller's documented geometric design language; actual values may differ by 1–2px
- Font weight variants for FF Meta Headline W05 (Light, Regular, Bold, Heavy) not individually confirmed; using weight 600/700 based on display-context conventions
- Exact button height and padding not directly extracted; values interpolated from visible grid proportions
- Animation and transition timing not captured; industry-standard 200–250ms ease likely applies to hover states
- Dark mode or high-contrast mode not evidenced anywhere in the extraction
- Mobile breakpoint pixel values not confirmed from CSS; using standard 744/1128/1440 splits
- The yellow (#ffff00) appears in extraction with unclear UI role — possibly a clearance highlight or accessibility focus indicator; withheld from components until confirmed
- Exact mega-menu structure, column count, and featured-image treatment not captured
- Configurator disabled-option rendering (unavailable finish or size) not characterized
- Product configurator pricing update animation not captured
