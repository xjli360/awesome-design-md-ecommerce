---
version: alpha
name: "Fluke Corporation"
source_url: "https://www.fluke.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Caution-stripe logic runs through every surface — Fluke's #ffc20e, a saturated construction-site amber matching the molded housings on their handheld multimeters and clamp meters, delineates every CTA, active state, and category anchor against near-black (#212121) and deep navy (#003b78). The pairing is not aesthetic preference; it mirrors the display-contrast standards built into the instruments themselves, where a misread reading on a live electrical panel carries real consequence. Type runs on Arial and Noto Sans rather than a custom variable font, workhorse stacks chosen for maximum legibility at the small sizes professionals need when scanning part numbers and voltage-range specs on a warehouse screen. Navigation is category-dense and hierarchically deep, reflecting a catalog that spans handheld meters through industrial power analyzers; the top bar uses a dark mega-menu drawer (#242a37) that layers over the page rather than displacing it, preserving context for procurement buyers who cross-reference multiple product families in a single session. Button corners are nearly square ({rounded.xs}), and the amber primary is reserved exclusively for purchase and download CTAs, so there is zero ambiguity about what triggers a transaction. Status colors — amber (#ffc20e) for caution, green (#3fa21c) for OK, red (#e03d3d) for fault — mirror the indicator conventions on Fluke meter displays, giving UI feedback an instrument-panel literalism that makes the site feel continuous with the products it sells. A dark sidebar (#32394a) on product and category pages houses filter facets and technical parameters without competing with product imagery. The custom regulation-certification font renders compliance marks (CE, CAT III/IV, ATEX) inline with product listings, eliminating a separate document-lookup step for industrial buyers who need certification clearance before a purchase order can be raised.

colors:
  primary: "#ffc20e"
  primary-active: "#e4aa00"
  primary-disabled: "#fdca40"
  navy: "#003b78"
  navy-mid: "#336699"
  navy-light: "#477dca"
  navy-dark: "#264d73"
  ink: "#212121"
  body: "#555555"
  muted: "#727272"
  muted-light: "#a7a7a7"
  hairline: "#c4ccda"
  hairline-soft: "#d0d0d0"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-subtle: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#212121"
  on-dark: "#ffffff"
  dark-ui: "#242a37"
  dark-ui-raised: "#32394a"
  dark-ui-border: "#434b5c"
  sidebar: "#32394a"
  near-black: "#282828"
  error: "#e03d3d"
  success: "#3fa21c"
  warning: "#ffc20e"

typography:
  display-xl:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-primary:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  nav-secondary:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  cert-label:
    fontFamily: "regulation-certification, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Noto Sans', Arial, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  part-number:
    fontFamily: "Arial, monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  footer-link:
    fontFamily: "Arial, 'Noto Sans', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy}"
    border: "1px solid {colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 20px
    height: 40px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-dark:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    hover:
      backgroundColor: "{colors.sidebar}"
  button-ghost-amber:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 20px
    height: 40px
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    focus:
      border: "1px solid {colors.navy-mid}"
      outline: "2px solid {colors.navy-light}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-primary}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    utilityStrip:
      backgroundColor: "{colors.navy}"
      textColor: "{colors.on-dark}"
      height: 36px
      typography: "{typography.caption}"
  mega-menu:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-secondary}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.section}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"
    columnGap: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    partTypography: "{typography.part-number}"
    partColor: "{colors.muted}"
    priceTypography: "{typography.price}"
    ctaButton: "button-primary"
    shadow: "0 1px 4px rgba(0,0,0,0.08)"
    hover:
      border: "1px solid {colors.primary}"
      shadow: "0 2px 8px rgba(0,0,0,0.14)"
  category-tile:
    backgroundColor: "{colors.dark-ui-raised}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    accentLine: "3px solid {colors.primary}"
    hover:
      backgroundColor: "{colors.sidebar}"
      accentLine: "3px solid {colors.primary-active}"
  hero-banner:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    accentColor: "{colors.primary}"
    minHeight: 420px
    overlayGradient: "linear-gradient(90deg, {colors.dark-ui} 45%, transparent 100%)"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    linkColor: "{colors.navy}"
    linkFontWeight: 700
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.sm} {spacing.base}"
    alternateRowColor: "{colors.surface-subtle}"
  cert-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.cert-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    iconColor: "{colors.navy}"
  filter-sidebar:
    backgroundColor: "{colors.sidebar}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.dark-ui-border}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"
    width: 260px
    padding: "{spacing.base}"
  status-indicator:
    ok:
      color: "{colors.success}"
    caution:
      color: "{colors.warning}"
    fault:
      color: "{colors.error}"
    typography: "{typography.caption-bold}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 44px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 48px
    focus:
      border: "1px solid {colors.navy-mid}"
      outline: "2px solid {colors.navy-light}"
  alert-banner:
    info:
      backgroundColor: "{colors.navy}"
      textColor: "{colors.on-dark}"
    warning:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
    error:
      backgroundColor: "{colors.error}"
      textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    typography: "{typography.footer-link}"
    borderTop: "4px solid {colors.primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons
**`button-primary`** — The amber (#ffc20e) primary button uses all-caps Noto Sans/Arial at 14px weight 700 with 0.5px letter spacing, {rounded.xs} corners, and 40px height. This is the sole action color on the page; it appears only on "Add to cart," "Get a quote," and download CTAs, so nothing competes with it for purchase intent. Hover darkens to {colors.primary-active} (#e4aa00); the disabled state uses {colors.primary-disabled} with {colors.muted} text to preserve button geometry without suggesting interactivity. On-primary text is near-black (#212121) rather than white, exploiting the full contrast range of the amber hue.

**`button-secondary`** — Navy-bordered ghost button with {colors.navy} text on canvas, same all-caps typographic treatment. Used for "Compare," "Find distributor," and secondary navigation CTAs. Hover fills to {colors.surface-soft} without changing the border, keeping the ink-to-background ratio stable.

**`button-dark`** — Dark-field variant on {colors.dark-ui} background, white text, same {rounded.xs} radius. Used inside hero banners and the mega-menu panel where the canvas background is absent.

**`button-ghost-amber`** — Transparent background with a 2px {colors.primary} border and amber text, reserved for tertiary actions on dark-surface sections. On hover, the button floods amber and shifts text to {colors.on-primary}, inverting the border treatment into a filled primary button.

### Navigation
**`nav-bar`** — Two-tier structure: a 36px utility strip in {colors.navy} carrying account, cart, and distributor links in caption-scale white, stacked above a 64px white main bar with the Fluke wordmark, primary category links in {typography.nav-primary}, and a search input. This mirrors B2B portal conventions — utility tools are always visible without occupying primary real estate.

**`mega-menu`** — Full-width dark overlay panel ({colors.dark-ui}) with a 3px {colors.primary} accent stripe at the top edge. Category section headings render in {colors.primary} at {typography.title-sm} weight; sub-links are {colors.on-dark} at {typography.nav-secondary}. The abrupt dark-on-white contrast acts as a visual modal: users understand immediately they are inside navigation, not a product page. Column gap is {spacing.xxl} to maintain scan-line separation across a dense product taxonomy.

### Product Cards
**`product-card`** — Zero-radius cards with a 1px {colors.hairline-soft} border on white. Product image sits in a {colors.surface-soft} photo well at fixed aspect ratio; the part number renders in {typography.part-number} (monospace-adjacent, 0.3px tracking) below the product title in {colors.muted}, providing a scannable catalog reference. Price in {typography.price} weight 700 precedes the amber CTA. On hover, border color swaps to {colors.primary} and box shadow deepens, making the card behave like a physical selector on a shelf.

**`category-tile`** — Dark-surface tiles ({colors.dark-ui-raised}) with a 3px {colors.primary} left accent line used in category navigation grids. All-caps {typography.title-sm} in white. Amber is the only chromatic element in each tile; the rest is monochrome dark, so the accent line reads as a category identifier rather than decorative flourish.

### Search
**`search-bar`** — Full-width input field with a flush square-cornered amber submit button on the right. The amber trigger echoes the primary CTA hue, reinforcing that search is the primary product-discovery action. Focus state adds a {colors.navy-mid} border and {colors.navy-light} outline ring to meet WCAG 2.1 AA contrast requirements.

### Spec Table
**`spec-table`** — Two-column rows with a {colors.surface-soft} header band, alternating {colors.surface-subtle} stripes on data rows, and {colors.hairline} borders throughout. Label column uses {typography.spec-label} (bold, 13px); value column uses {typography.spec-value} (regular, 13px). No color is used to differentiate row types beyond the alternating background — legibility at scan speed is the sole criterion.

### Certification Badges
**`cert-badge`** — Compact {rounded.xs} chips using the custom `regulation-certification` font at 10px/uppercase. A {colors.navy} icon precedes the certification code. Badges appear inline in product headers and on product cards, letting procurement buyers verify compliance (CE, CAT III/IV, IEC 61010, ATEX) without leaving the listing view.

### Promotional Strip
**`promo-strip`** — 40px full-width amber bar above the nav-bar tier. Body-sm near-black text for offer copy; a bold {colors.navy} link for the CTA. The amber strip reads as a site-wide alert: the brand reuses its primary hue here to give promotions the same urgency as a status warning, which is entirely intentional given the professional audience.

### Filter Sidebar
**`filter-sidebar`** — 260px dark panel ({colors.sidebar}) on category and search-results pages. Section headings in {colors.primary} at {typography.title-sm} weight; filter option labels in {typography.body-sm} white. The dark sidebar reads as subordinate to the product grid without losing legibility. Section separators use {colors.dark-ui-border}; the heading amber color creates visual anchors that let users jump between filter categories at a glance.

### Status Indicators
**`status-indicator`** — Three-state system mirroring panel-meter display conventions: {colors.success} (#3fa21c) for available/compliant, {colors.warning} (#ffc20e) for low-stock/caution, {colors.error} (#e03d3d) for unavailable/fault. Rendered in {typography.caption-bold}. Using the same stop-light colors as physical instrument indicators makes inventory and compatibility status immediately recognizable to field technicians and procurement engineers alike.

### Alert Banner
**`alert-banner`** — Inline contextual banners in three variants: info (navy background, white text), warning (amber background, near-black text), error (red background, white text). Used for safety advisories, firmware notices, and out-of-stock alerts. All three share the same {typography.body-sm} and {rounded.xs} radius to maintain visual system cohesion.

### Footer
**`footer`** — Full-width dark footer ({colors.dark-ui}) with a 4px {colors.primary} top border that anchors it as a deliberate page-end landmark. Column headings in {colors.primary} at {typography.title-sm}; link lists in {typography.footer-link} white. The amber top border mirrors the mega-menu's accent stripe, wrapping the page in a consistent amber-on-dark framing device.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger collapses nav-bar; mega-menu becomes full-screen slide-in drawer with accordion category hierarchy; filter-sidebar becomes bottom-sheet modal triggered by a sticky "Filters" chip; hero-banner stacks headline above image; product-card grid shifts to single column; promo-strip truncates to one line |
| Tablet | 744–1128px | Two-column product grid; filter-sidebar collapses to horizontal chip-row above grid; nav retains utility strip but condenses main links to overflow menu; hero-banner retains landscape layout at reduced image crop; spec-table horizontal scrolls if column count exceeds viewport |
| Desktop | 1128–1440px | Three-column product grid; full 260px filter-sidebar visible alongside grid; mega-menu opens at full page width; hero-banner shows full landscape image with gradient overlay; spec-table renders fully without scroll |
| Wide | > 1440px | Content container caps at 1440px and centers; product grid may extend to four columns; hero-banner image scales to fill while gradient overlay preserves text legibility; footer columns redistribute to maintain ≤ 5 columns |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Filter chips minimum 36px height with {spacing.sm} gap between chips in horizontal chip-row
- Product card CTA button expands to full card width on mobile for easy tap
- Nav utility-strip links consolidate to account icon plus cart icon on mobile to preserve 44px targets
- Cert-badge chips stack vertically on mobile rather than wrapping inline

### Collapsing Strategy
- Mega-menu collapses to full-screen slide-in drawer; category hierarchy becomes tap-to-expand accordion with {colors.primary} chevron indicators
- Filter sidebar becomes a sticky "Filters" chip at top of product grid; tap opens bottom-sheet modal with full filter facets
- Spec-table maintains two columns at all breakpoints; row padding reduces to {spacing.xs} on mobile; horizontal scroll enabled only as last resort for tables with more than two value columns
- Promo-strip persists across all breakpoints as it carries time-sensitive messaging; text truncates at mobile with a "See offer" link
- Hero-banner overlay gradient rotates from horizontal (desktop) to vertical (mobile) so text remains readable above the image

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display or heading typeface confirmed; site relies on Arial, Noto Sans, and Verdana — no variable font file or weight axis data extracted; all weight values above are estimated from visual hierarchy conventions
- Exact button height, padding, and input height not extracted from computed styles; values are estimated from visible proportions consistent with a 40px industrial touch-friendly UI baseline
- Box-shadow and elevation token values not extractable from CSS snapshot; card and panel shadow values are approximated
- Exact nav-bar tier heights (utility strip vs. main bar) not confirmed from live extraction; 36px + 64px are visual estimates
- Animation timing functions and durations not extracted (hover transitions, drawer open, accordion expand)
- Mobile breakpoints not confirmed from Shopify theme CSS; Shopify default breakpoints (tablet ~768px, desktop ~1024px) assumed
- Dark-mode or high-contrast theme not confirmed; site appears single-theme light/dark hybrid with deliberate dark-surface sections
- Icon glyph set and sizing for `fluke-icon-font` not catalogued; referenced in extraction but no codepoint or size data available
- Exact `regulation-certification` font glyph set not inspectable; assumed to render standardized certification mark symbols only
- Product image aspect ratio and minimum resolution not confirmed from asset delivery rules
