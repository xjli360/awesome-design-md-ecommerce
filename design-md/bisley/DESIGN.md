---
version: alpha
name: "Bisley"
source_url: "https://www.bisley.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Petrol-green filing cabinets finished in over 50,000 powder-coat colors ship from British factories, and the Bisley digital shell carries that color library into its UI through a warm parchment canvas (#eeece9 — the site's own meta theme-color) that flatters painted-steel photography without competing with it. Near-black ink (#1d1d1b) on parchment rather than pure white gives product tables and specification sheets a press-printed solidity, befitting a brand whose roots lie in post-war British civil service procurement. The deep petrol (#2e5b66) anchors primary actions and hover states — a color close enough to the product palette to feel material rather than UI-generic. A blue-teal family (#5b819f, #7ababb, #bce0da, #dee6ec) forms the cool-neutral layer for informational components and selected states, referencing the metalwork finishes Bisley polishes before shipping. FS Elliot sits at the top of the font stack: a humanist sans developed for UK public-sector legibility, a telling choice for a supplier whose cabinets fill NHS storage rooms and council archive halls. The typeface carries government-register clarity into long product configurators and multi-column specification tables without straining at small sizes. Warm surface neutrals (#f4f2f1, #edebe8, #e8e4e2) graduate the card and filter panel layers. Sage (#bccfa1, #465741) and blush (#f6e5de) surface as product colorway swatches rather than system chrome — the interface doubles as a physical finish browser. Error states spike to #d70f0f, visible on off-white without colliding with catalog reds. Corner radii stay at {rounded.xs} through {rounded.sm} across all functional elements, a precision restraint appropriate for a manufacturer whose tolerances are measured in millimeters.

colors:
  primary: "#2e5b66"
  primary-active: "#1c3b44"
  primary-disabled: "#8bb0c2"
  ink: "#1d1d1b"
  body: "#444444"
  muted: "#7c7d7f"
  muted-soft: "#aaaaaa"
  hairline: "#c3c2c2"
  hairline-soft: "#e8e4e2"
  canvas: "#ffffff"
  surface-warm: "#eeece9"
  surface-soft: "#f4f2f1"
  surface-card: "#f1eeec"
  on-primary: "#ffffff"
  accent-steel: "#5b819f"
  accent-teal: "#7ababb"
  accent-mint: "#bce0da"
  accent-sage: "#bccfa1"
  accent-forest: "#465741"
  accent-blush: "#f6e5de"
  error: "#d70f0f"
  error-deep: "#b10606"
  blue-gray: "#9697ab"

typography:
  display-xl:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-caps:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-label:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'FS Elliot', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    hover:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 48px
    hover:
      backgroundColor: "{colors.surface-soft}"

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
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focus:
      borderColor: "{colors.primary}"
      outline: "2px solid {colors.accent-mint}"
    error:
      borderColor: "{colors.error}"

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    focus:
      backgroundColor: "{colors.canvas}"
      borderColor: "{colors.primary}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 40px
    subNav:
      backgroundColor: "{colors.surface-warm}"
      textColor: "{colors.body}"
      typography: "{typography.body-sm}"

  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    imageBackground: "{colors.surface-warm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
    hover:
      border: "1px solid {colors.hairline}"
      boxShadow: "0 4px 12px rgba(29,29,27,0.08)"

  color-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selected:
      border: "2px solid {colors.ink}"
      outline: "2px solid {colors.canvas}"
    lowContrast:
      insetRing: "1px solid {colors.hairline}"
    tooltip:
      backgroundColor: "{colors.ink}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      rounded: "{rounded.xs}"

  color-swatch-grid:
    gap: "{spacing.sm}"
    maxColumns: 10
    overflowLabel:
      typography: "{typography.body-sm}"
      textColor: "{colors.muted}"

  product-badge:
    typography: "{typography.label-caps}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    variants:
      new:
        backgroundColor: "{colors.primary}"
      sale:
        backgroundColor: "{colors.error}"
      made-in-uk:
        backgroundColor: "{colors.ink}"

  filter-sidebar:
    backgroundColor: "{colors.surface-warm}"
    borderRight: "1px solid {colors.hairline}"
    width: 280px
    sectionHeaderTypography: "{typography.spec-label}"
    sectionHeaderColor: "{colors.ink}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.body}"
    padding: "{spacing.lg}"
    checkboxActiveColor: "{colors.primary}"

  spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    headerBackgroundColor: "{colors.surface-warm}"
    headerTypography: "{typography.spec-label}"
    headerTextColor: "{colors.ink}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    cellPadding: "10px {spacing.base}"
    stripeBackgroundColor: "{colors.surface-soft}"

  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 520px
    overlayOpacity: 0.45
    contentMaxWidth: 600px
    padding: "{spacing.xxl} {spacing.section}"

  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
    hover:
      textColor: "{colors.primary}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.accent-mint}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Deep petrol (#2e5b66) block at 48px tall with 2px corners and white FS Elliot Semibold label. On hover it darkens to #1c3b44; the disabled state washes to steel-light #8bb0c2, maintaining legibility without implying interactivity. The sharp corner radius is deliberate — it mirrors the precision-machined drawer edges in Bisley's physical product line rather than reaching for consumer softness.

**`button-secondary`** — Transparent background with a 2px petrol border and matching petrol label at identical height and padding to the primary. On hover a surface-soft (#f4f2f1) fill appears, confirming hover state without importing additional color. Used alongside primary for download-spec, enquire-now, or secondary configurator actions.

**`button-ghost`** — No border, no fill; ink label at button-sm scale. Appears inside filter panels, nav dropdowns, and data-dense rows where a third action needs to exist without competing visually with the two structured button types above.

### Search Bar

**`search-bar`** — A surface-soft trough sitting in the nav header and again above product grids. Ink text on #f4f2f1 background with a muted icon; on focus, background lifts to canvas white and a thin petrol border appears. No animation — the transition is purely color. At mobile widths the field expands to full viewport width below the logo row.

### Product Card

**`product-card`** — White card at 4px corner radius with a 1px hairline-soft border. The image well uses surface-warm (#eeece9) as a neutral photo ground that flatters painted steel in any finish. Title in title-sm, price in title-md; a caption line below carries the product code and available color count ("Available in 28 colors"). On hover the border tightens to hairline and a subtle 8px shadow lifts the card. A color swatch strip sits between the title and price row, capped at 10 chips with an overflow count beyond that.

### Color Swatch System

**`color-swatch`** — 32px circular chips ({rounded.full}) with a normally transparent 2px border. On selection the border fills ink and an inner 2px canvas gap creates the classic double-ring selected state. On hover, a tooltip in caption scale on an ink background shows the finish name. Low-contrast swatches (near-white finishes) automatically receive a 1px inset hairline ring for definition. This is the most brand-critical component in the system: Bisley's commercial differentiator is its finish range, and the swatch grid is how buyers make purchase decisions.

**`color-swatch-grid`** — A wrapping grid at 8px gap, maximum 10 columns before an overflow label in muted body-sm ("+ 14 more") triggers an expanded modal or accordion. Used in product cards, the dedicated Explore Colors landing section, and the inline configurator panel on product detail pages.

### Product Badge

**`product-badge`** — 11px uppercase label-caps text in a tight 4px/8px padded chip with 2px corners. "NEW" and standard variants use primary petrol; "SALE" uses error red (#d70f0f); "Made in UK" uses near-black (#1d1d1b). Badges pin to the top-left corner of the product card image well and do not stack — a hierarchy of one badge per card is enforced.

### Filter Sidebar

**`filter-sidebar`** — 280px persistent panel on surface-warm with a 1px hairline right border. Section headers in spec-label scale (uppercase, 0.8px tracking, 600 weight). Filter options in body-sm with checkbox controls that fill petrol on selection. All padding at 24px. On tablet the sidebar collapses to a horizontal scrolling chip strip pinned above the product grid; on mobile it becomes a bottom-sheet modal.

### Specification Table

**`spec-table`** — Full-width bordered table at 4px corner radius. The header row sits on surface-warm with spec-label typography; data rows alternate between canvas and surface-soft stripes at 10px/16px cell padding. Used on every product detail page for dimensions, weight, load capacity, fire resistance rating, and material specs. Facilities managers and procurement officers read these values before ordering, so the table is never collapsed or hidden behind an accordion on desktop.

### Hero Banner

**`hero-banner`** — Full-width image hero with an ink overlay at 45% opacity. Title renders in display-xl white; subtitle in body-md white at a 600px content max-width. The CTA button uses the primary button style. Minimum height 520px desktop, padding at 48px vertical / 64px horizontal; on mobile padding drops to lg (24px) and title scales to display-md. Content is always left-aligned — centered copy is not used anywhere in the system.

### Navigation Bar

**`nav-bar`** — 72px white header with a 1px hairline bottom border. The logo sits left; primary nav links in nav-link scale sit right. A sub-navigation drop panel on hover uses surface-warm (#eeece9) as its background, creating a visual continuation from header to page canvas. A search icon in the right cluster expands the search-bar component inline rather than navigating to a search page.

### Breadcrumb

**`breadcrumb`** — Caption-scale muted text with "/" separators in hairline color. The current page segment renders in ink weight; ancestor nodes are linked and turn petrol on hover. Always present on product and category pages — buyers arriving from search engines need orientation in the product hierarchy immediately.

### Footer

**`footer`** — Near-black (#1d1d1b) footer with a 4px petrol top border that echoes the product drawer-rail detail. Column headings in title-sm white; links in body-sm at #f4f2f1; active/hovered links in accent-mint (#bce0da). Four-column layout on desktop, two columns on tablet, single column on mobile. Includes a "Made in the UK" mark and third-party certification logos at 60% white opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes bottom-sheet modal; hero title scales to display-md; nav collapses to hamburger drawer; color swatch grid max 6 columns; search bar full width below logo |
| Tablet | 744–1128px | Two-column product grid; filter sidebar becomes horizontal scrolling chip strip above grid; hero min-height 400px; nav shows top-level links, secondary categories in hamburger overflow |
| Desktop | 1128–1440px | Three-column product grid; 280px filter sidebar persistent left; full nav with drop-panel sub-nav; hero 520px with left-aligned content |
| Wide | > 1440px | Four-column product grid; content constrained to 1440px centered with section padding; hero image edge-to-edge behind contained content column |

### Touch Targets

- All interactive controls minimum 44×44px on touch viewports
- Color swatches expand from 32px desktop to 40px on mobile
- Filter checkboxes use 44px tap area padded around a 20px visual box
- Nav hamburger icon minimum 44×44px centered hit area
- Breadcrumb links minimum 32px height with extended tap zones above and below

### Collapsing Strategy

- Filter sidebar → horizontal scrolling chip strip at tablet, bottom-sheet modal at mobile
- Mega-nav dropdowns → accordion list inside off-canvas drawer at tablet and below
- Spec table → horizontally scrollable with first column (label) sticky at mobile widths
- Color swatch grid → max-columns reduces to 6 at mobile with overflow count appearing earlier
- Hero content → image crops to 16:9 at mobile; title and subtitle stack vertically with reduced padding

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit button border-radius value extracted from live CSS; `{rounded.xs}` (2px) inferred from the brand's industrial product character
- FS Elliot weight variants (Light, Pro, Heavy) not confirmed by extraction; 400 and 600 assumed as the working pair
- Exact nav bar height (72px) estimated; live measurement was not available
- Product card hover shadow values inferred from convention; no extracted box-shadow tokens
- Sale price strikethrough treatment and currency symbol weight not confirmed
- `swiper-icons` detected in the font-family stack confirming a carousel component exists; its configuration, pagination style, and autoplay behavior are unknown
- Dark-mode or high-contrast theme tokens not detected; warm-parchment appears to be the single theme
- Custom icon set not identified; generic SVG icon system assumed throughout
- Mobile nav drawer animation timing and easing values not extractable from static hints
- Product configurator UI (drawer-count selector, lock-type toggle, color picker integration) may have additional bespoke components not represented here
