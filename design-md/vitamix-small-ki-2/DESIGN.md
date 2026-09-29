---
version: alpha
name: "Vitamix"
source_url: "https://www.vitamix.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The same deep red anchoring every Vitamix blender base for decades shows up as the sole chromatic voltage in the digital system — no secondary accent, no tertiary highlight, just {colors.primary} carrying every primary CTA, add-to-cart trigger, and promotional label against a near-white canvas. The typographic split reveals how seriously the brand stakes its performance legitimacy: Sentinel, a slightly bracketed oldstyle serif from Hoefler & Co., handles hero-scale display at sizes approaching 56px, lending editorial authority to peak-horsepower claims and cooking-outcome headlines; Gotham Narrow absorbs everything transactional — navigation labels, button copy, specification tables, ingredient callouts — in its condensed, engineered letterforms that pack four data points into the space where three would otherwise sit. When a spec row labels "Container Capacity: 64 oz." in {typography.spec-label} — all-caps Gotham Narrow at 11px with 1px letterSpacing — the density signals professional-kitchen calibration rather than home-appliance convenience. Product cards maintain hard corners ({rounded.xs}) against a {colors.surface-card} white field; no rounded-corner flourishes soften the brand's positioning toward the mass-consumer end of the kitchen category. The compare table is a signature UI moment: full-width, alternating {colors.surface-soft} rows, Gotham Narrow column headers naming blender series, each row resolving a specification that justifies a $200 price step between tiers. Navigation unfolds into a structured mega-menu organized by blender form factor — Full Size, Personal, Immersion — rather than lifestyle marketing language. Spacing leans generous between content sections but tight within spec blocks, leaving product photography of motor-housing geometry and blade assembly room to make the functional argument that copy alone cannot. No pill-shaped controls appear anywhere in the system; every interactive element sits at {rounded.xs} or {rounded.sm}, keeping the visual register closer to laboratory instrument than consumer lifestyle accessory.

colors:
  primary: "#CC1417"
  primary-active: "#A50F12"
  primary-disabled: "#DFA0A1"
  ink: "#1B1B1B"
  body: "#333333"
  muted: "#6B6B6B"
  muted-soft: "#999999"
  hairline: "#E0E0E0"
  hairline-soft: "#F0F0F0"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#1B1B1B"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  promo-bg: "#F8F3F0"
  check-green: "#2E7D32"

typography:
  display-xl:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  editorial-serif:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  price-strikethrough:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
    textDecoration: line-through

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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: 0 16px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
    columnGap: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-md}"
    subtitleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    strikePriceTypography: "{typography.price-strikethrough}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.editorial-serif}"
    rounded: "{rounded.none}"
    minHeight: 560px
    layout: split-image-right
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
  spec-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.title-md}"
    padding: "{spacing.lg} 0"
    dividerColor: "{colors.hairline}"
    columns: 4
  compare-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.title-sm}"
    rowLabelTypography: "{typography.spec-label}"
    rowValueTypography: "{typography.body-sm}"
    altRowBg: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
  model-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    activeBg: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  series-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    typography: "{typography.nav-label}"
    rounded: "{rounded.none}"
    tabHeight: 48px
    inactiveBorder: "1px solid {colors.hairline}"
  promo-banner:
    backgroundColor: "{colors.promo-bg}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  feature-checklist:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    checkColor: "{colors.check-green}"
    iconSize: 16px
    rowGap: "{spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: none
    padding: "{spacing.xxl} 0"

---

## Components

### Buttons

**`button-primary`** — Fully uppercase Gotham Narrow at 14px with 1.5px letter-spacing on a {colors.primary} red ground, 48px height, and a near-sharp {rounded.xs} corner that keeps the control visually closer to a precision instrument than a soft consumer CTA. Hover shifts to {colors.primary-active}, a slightly deeper crimson; disabled state washes the ground to {colors.primary-disabled} with white text retained. Reserved exclusively for add-to-cart, shop-now, and primary hero actions — never used decoratively.

**`button-secondary`** — Identical uppercase Gotham Narrow label, {colors.canvas} white ground with a 1px {colors.ink} border and the same 48px height. Appears alongside `button-primary` in product card footers and comparison-table CTAs, providing hierarchy without diluting the red primary. Ghost variant (`button-ghost`) renders {colors.primary} text on a transparent ground for inline editorial links and secondary in-content navigation.

### Text Input & Search

**`text-input`** — Zero border-radius ({rounded.none}), 1px {colors.hairline} border at 48px height. Focuses to a 1px {colors.ink} border with no glow or shadow. Placeholder renders in {colors.muted}. The flat, squared treatment keeps form fields visually consistent with the product card and compare-table aesthetic — nothing curves unnecessarily.

**`search-bar`** — A 44px-tall input in {colors.surface-soft} with a {rounded.sm} corner and a {colors.muted} magnifier icon at left. Sits in the collapsed nav utility row at desktop widths and expands to full-width overlay on mobile. Placeholder text in {colors.muted-soft} Gotham Narrow.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} white ground, Vitamix logo at left, utility row (search, account, cart) at right. Primary product category labels render in {typography.nav-label} — 13px Gotham Narrow medium — and trigger the `mega-menu` on hover. A slim 1px {colors.hairline} bottom border separates the bar from page content.

**`mega-menu`** — Full-viewport-width panel, white ground, {spacing.xxl} column gaps. Column headers in {typography.title-sm} all-caps Gotham Narrow; link rows drop to {typography.body-sm}. Columns organize by product family (Full-Size Blenders, Personal Blenders, Immersion Blenders) with auxiliary columns for Recipes, Commercial, and Support. No imagery or icons inside the panel — information density does the work.

### Product Card

**`product-card`** — {colors.surface-card} white with a whisper-thin {colors.hairline-soft} border and {rounded.xs} corner. Product name in {typography.title-md}; a short positioning line in {typography.body-sm} {colors.muted} beneath it ("Professional-grade power for the home kitchen"). Price in {typography.price-display}; sale pricing shows the original in {typography.price-strikethrough} alongside the reduced amount. Square 1:1 image with centered product photography. CTA anchors at card bottom, full card width.

### Hero Banner

**`hero-banner`** — Dark {colors.surface-dark} ground, split-image-right layout at desktop: headline in {typography.display-xl} Sentinel on the left half, product photography bleeding to the viewport edge on the right. Subline in {typography.editorial-serif} at 20px softens the technical intro copy. A single {colors.primary} CTA button sits below the subline. Minimum height 560px ensures the full blender machine is visible before any scroll. On mobile, image moves above and headline scales down to {typography.display-md} Sentinel.

### Spec Strip

**`spec-strip`** — A {colors.surface-soft} horizontal band appearing immediately after the hero on product-detail pages. Four equally-spaced columns show Motor Peak HP, Container Capacity, Speed Settings, and Warranty. Each column renders a {typography.spec-label} category header above a {typography.title-md} value, separated by thin {colors.hairline} vertical rules. This component resolves the primary performance question within five seconds of landing — before the user commits to scrolling into the body.

### Compare Table

**`compare-table`** — Full-width, {rounded.none}, no outer border. Column headers sit on {colors.surface-dark} ground in {colors.on-dark} text, set in {typography.title-sm} uppercase. Row labels in {typography.spec-label} left-aligned; values in {typography.body-sm}. Alternating rows use {colors.surface-soft} and {colors.canvas}. A `model-badge` ("Best Value", "Most Popular") pins above the column header for editorially designated tiers. This table is the primary decision surface for users resolving a $200–$400 spread between blender lines through specification rather than marketing language.

### Model Badge & Series Selector

**`model-badge`** — A tight rectangular chip in {typography.spec-label} uppercase. Inactive: {colors.surface-soft} ground, {colors.muted} text. Active: {colors.primary} ground, {colors.on-primary} text. Applied to blender line labels ("Ascent Series", "Explorian Series") on PLPs, compare contexts, and PDP breadcrumbs.

**`series-selector`** — A horizontal tab strip at 48px height below the hero on category pages. Inactive tabs sit on {colors.canvas} with a 1px {colors.hairline} bottom border. The active tab shows a 2px {colors.primary} bottom indicator with no border. Typography is {typography.nav-label}. Scrolls horizontally on mobile rather than collapsing.

### Feature Checklist

**`feature-checklist`** — Vertical list of selling-point lines, each prefixed by a {colors.check-green} check icon at 16px. Body text in {typography.body-sm} {colors.body}. {spacing.sm} row gap. Appears in PDP "Why Vitamix" sections and comparison summaries, itemizing performance and warranty claims without requiring a full spec table.

### Promo Banner

**`promo-banner`** — Single-row announcement bar at the top of the viewport in {colors.promo-bg}, centered text in {typography.body-sm}. Promotional amounts ("Save $100 through June") render in {colors.primary} inline. Dismissible via a close icon at right edge. Stacks above the nav-bar and does not scroll away with sticky nav.

### Footer

**`footer`** — {colors.surface-dark} ground, {colors.on-dark} text throughout. Four-column grid: {typography.title-sm} uppercase column headers (Products, Support, About, Connect) with {typography.body-sm} link rows beneath. Social icon row at base. No decorative imagery — purely architectural. Padding {spacing.xxl} top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; mega-menu becomes fullscreen drawer with back-per-column navigation. Hero switches to stacked layout — image above, Sentinel headline below at display-sm scale. Spec strip collapses to 2×2 grid. Compare table horizontally scrolls with sticky left column. Product grid goes single column. |
| Tablet | 744–1128px | Nav stays horizontal with abbreviated labels; mega-menu fires on tap. Hero maintains split layout but headline scales to display-md. Product grid 2 columns. Spec strip 4-column with tighter padding. |
| Desktop | 1128–1440px | Full mega-menu on hover, 3-column product grid, hero at full 560px height. Spec strip 4-column at standard spacing. Compare table renders all columns simultaneously. |
| Wide | > 1440px | Content max-width ~1400px centered with auto side margins. Hero image scales proportionally; headline remains at display-xl cap. Footer grid adds breathing room via auto column widths. |

### Touch Targets

- All buttons minimum 48×48px; icon-only utility controls padded to 44px tap area
- Compare table row height minimum 44px for comfortable row-label tapping on horizontal-scroll mobile layout
- Nav hamburger button padded to 48×48px regardless of visible icon size
- Product cards are fully tappable across the entire card surface — the CTA button is not the sole touch target
- Series-selector tabs minimum 44px height with full-tab touch area

### Collapsing Strategy

- Mega-menu collapses to a fullscreen overlay drawer with accordion-style column reveals and a top-level back button at mobile
- Spec strip transitions from 4-column to 2×2 grid at < 744px; stacks fully single-column at < 480px
- Compare table: sticky first column (model name + image), horizontal scroll for remaining columns at < 744px
- Footer 4-column grid collapses to collapsible accordion sections at < 744px; headers remain tappable at 48px height
- Series-selector overflows with horizontal scroll (no wrapping) at narrow widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site loads color tokens via JavaScript or has anti-bot protection that blocked extraction. All hex values above are informed by Vitamix's widely documented brand identity; the brand red is a consistent signature across decades of physical products and marketing. All values require verification against a live site audit or official brand kit.
- **Exact primary red unconfirmed** — `#CC1417` is a calibrated estimate; the true value may be closer to Pantone 485 C (≈ #DA291C) or Pantone 186 C (≈ #C8102E). Capture via browser dev tools on a live page for precision.
- **Secondary and promotional palette unknown** — whether Vitamix uses a warm gray, cream, or seasonal accent for sale events, refurbished-product badging, or commercial product lines could not be confirmed without live extraction.
- **Gotham Narrow weight variants loaded** — the site almost certainly loads a subset of Gotham Narrow (Light, Book, Medium, Bold); which specific weights are available at each breakpoint is unconfirmed.
- **Sentinel weight and style variants** — whether the site loads Sentinel italic (common for editorial pullquotes) or only roman weights is unknown.
- **Spacing scale not measured** — the base-8 system above is standard convention; actual grid gutters, section-break padding, and column margins require visual measurement against the live site.
- **Motion and transition tokens** — hover-state transition durations, menu reveal easing, and carousel animation parameters were not captured.
- **Icon system** — whether Vitamix uses a proprietary SVG icon library or a third-party set (Phosphor, Material, custom) is unknown; icon sizing and stroke-weight conventions are inferred.
- **Reconditioned / Commercial product badge system** — Vitamix sells certified-reconditioned machines and has a commercial line (Vita-Mix); whether these carry distinct badge colors or typographic treatments beyond `model-badge` is unconfirmed.
