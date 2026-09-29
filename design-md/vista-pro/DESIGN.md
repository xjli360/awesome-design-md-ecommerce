---
version: alpha
name: "Vista Pro"
source_url: "https://www.vistapro.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Steel weathered to a specific shade of slate — #415d6f, a desaturated teal-gray that sits between maritime metal and industrial primer — is Vista Pro's entire opening argument for the commercial specifier market. The brand's palette refuses warmth at every structural level: the deep teal-navy (#283c48) anchors footers and hero sections while near-white surfaces (#ebf0f1, #edeff0) carry just enough cool cast to read as poured concrete rather than retail cream. Hairlines and borders draw from #b5c2c7, a muted steel tone that mirrors the extruded aluminum housings the fixtures ship in. Raleway handles display headings in uppercase weight-700 with generous letter-spacing — a stamp, not a shout — while Poppins carries specification copy at comfortable reading sizes. Baskerville appears selectively for editorial pull-quotes or certification statements, lending serif-anchored authority to compliance language without ceding the system's industrial register. Product corners are barely softened ({rounded.xs}, 4px), communicating precision machining rather than consumer-product approachability. Primary CTAs darken from the steel-slate primary to #283c48 on hover, moving down the same cool axis rather than warming or brightening. The site's load-bearing content is specification-first: wattage tables, IES file downloads, DLC listing confirmations, and CCT selectors occupy more screen real estate than photography or lifestyle copy. Contractors and lighting designers arrive with specs already in mind; the UI honors that by foregrounding filter panels and downloadable photometric data over marketing narrative. The entire system reads as a technical document that happens to be styled — and that register is precisely correct for specifying architectural-grade exterior luminaires.

colors:
  primary: "#415d6f"
  primary-active: "#283c48"
  primary-disabled: "#b5c2c7"
  secondary-navy: "#003388"
  ink: "#313131"
  body: "#444444"
  muted: "#676767"
  muted-soft: "#9a9a9a"
  hairline: "#b5c2c7"
  hairline-soft: "#edeff0"
  canvas: "#fafafa"
  surface-soft: "#ebf0f1"
  surface-card: "#eeeeee"
  surface-dark: "#283c48"
  charcoal: "#393939"
  steel-mid: "#a5acb5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  editorial:
    fontFamily: "Baskerville, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  button-md:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Raleway', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  breadcrumb:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
    logoColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    logoColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    imageBg: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlay: "rgba(40,60,72,0.65)"
    padding: "{spacing.section} {spacing.xl}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    headerTextColor: "{colors.primary}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowAltBg: "{colors.surface-card}"
    rounded: "{rounded.none}"
  spec-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  product-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  download-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.primary}"
    padding: "{spacing.base}"
  editorial-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.charcoal}"
    typography: "{typography.editorial}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    linkColor: "{colors.steel-mid}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Vista Pro's primary CTA stamps its steel-slate (#415d6f) with white Raleway 700 uppercase copy at 1.5px tracking, producing a label that reads like a product certification mark. On hover the background shifts to the deeper teal-navy ({colors.primary-active}, #283c48) — the same palette axis, cooler and more resolved, with no animation delay. Disabled state uses {colors.primary-disabled} (#b5c2c7), the muted steel hairline tone, so even inactive controls stay on-brand. The 4px corner radius ({rounded.xs}) is the minimum softening — barely distinguishable from a hard corner at small sizes, preserving the rectilinear housing aesthetic.

**`button-secondary`** — A 2px outlined variant in {colors.primary} on a transparent ground, matching the uppercase Raleway type of the primary. Hover fills with {colors.surface-soft} for low-key acknowledgment. Used for secondary download actions ("View Spec Sheet," "Add to Compare") placed alongside primary CTAs on product detail pages. The outline variant keeps prominence hierarchy clear without introducing a third color.

### Text Input

**`text-input`** — Clean canvas-white ({colors.canvas}) with a 1px {colors.hairline} border and {rounded.xs} corners. Focus upgrades to a 2px solid {colors.primary} border, the only state change. Placeholder text draws from {colors.muted-soft} (#9a9a9a). Applied uniformly across search bars, contact and quote-request forms, and product filter inputs throughout the catalog.

### Navigation

**`nav-bar`** — A 72px white bar with Raleway 600 links at 14px/0.5px tracking, separated from page content by a 1px {colors.hairline} bottom border. The logo renders in {colors.primary} on white. A dark-variant `nav-bar-dark` (background: {colors.surface-dark}, #283c48) appears over full-bleed hero sections and category landing pages, with the logo reversed to white. On mobile the primary links collapse behind a hamburger control.

### Product Card

**`product-card`** — Cards sit on {colors.surface-card} (#eeeeee) with a 1px {colors.hairline-soft} border and {rounded.xs} corners, keeping the specification-document character intact. Product images render on a white ({colors.canvas}) inset so fixture finishes and photometric distributions read accurately against a neutral ground. The product name uses {typography.title-sm} (Poppins 600, 16px); wattage, series, and mounting-type metadata use {typography.body-sm}. Cards expand to full width on mobile.

### Hero

**`hero`** — Full-bleed sections in {colors.primary} or over photography with a dark overlay (rgba(40,60,72,0.65)) drawn from {colors.surface-dark}. Headline in {typography.display-xl} (Raleway 700 uppercase, 48px), supporting copy in {typography.body-md}. The overlay holds the cool teal-navy hue rather than going to a generic black scrim, so the brand color persists through imagery. The `hero-dark` variant uses {colors.surface-dark} directly as a solid background for section breaks between catalog categories, typically paired with a white or {colors.steel-mid} subhead.

### Spec Table

**`spec-table`** — The most prominent component on product detail pages. Column headers use {typography.spec-label} (Raleway 700 uppercase, 11px, 1px tracking) in {colors.primary} over {colors.surface-soft}. Data cells use {typography.body-sm} in {colors.body}. Alternating rows pull from {colors.surface-card} for legibility across dense wattage, lumen, CCT, and CRI grids. No corner radius anywhere — the table reads as a data document, not a UI card. On mobile the table gains horizontal scroll with the leftmost column (spec name) remaining sticky.

### Spec Chip

**`spec-chip`** — Pill-shaped ({rounded.full}) tokens on {colors.surface-soft} with {colors.primary} text in {typography.spec-label}. Applied inline with the product title to surface certifications (UL Listed, DLC Qualified, IP65, IP66), CCT options (3000K, 4000K, 5000K), and mounting configurations. They cluster below the product name in a wrapping flex row rather than appearing as filter controls.

### Category Badge

**`category-badge`** — Hard-cornered ({rounded.none}) rectangular labels in {colors.primary} with white {typography.spec-label} copy. Placed over the top-left corner of product grid images to identify fixture type ("Flood," "Wall Pack," "Area," "Bollard"). The sharp corner signals classification rigor and distinguishes badges from the rounded chips used for certifications.

### Search Bar

**`search-bar`** — 44px tall with a 1px {colors.hairline} border, {rounded.xs} corners, and a {colors.muted} magnifying-glass icon at the left edge. Sits in the top-right of the desktop nav bar and expands to full width at the top of catalog and category pages. On focus, border upgrades to {colors.primary} in the same pattern as `text-input-focus`.

### Product Filter

**`product-filter`** — A persistent left sidebar on {colors.surface-soft} with a 1px {colors.hairline} right border. Filter group headings use {typography.spec-label} in {colors.primary}; individual filter options use {typography.body-sm} in {colors.body}. Filters cover wattage, delivered lumens, CCT, CRI, mounting type, series, and listings. On mobile the sidebar converts to a full-screen sheet overlay triggered by a "Filter" button above the product grid.

### Download Card

**`download-card`** — A compact card on {colors.surface-card} with a 1px {colors.hairline} border and {rounded.xs} corners. A {colors.primary}-colored file-type icon (PDF, DWG, LDT) anchors the top-left; the document name follows in {typography.title-sm}, with file size and revision date in {typography.body-sm}. Cards appear in a responsive grid on the Resources tab of product detail pages, covering spec sheets, IES/LDT photometric files, installation guides, and CAD drawings.

### Editorial Callout

**`editorial-callout`** — A left-bordered callout block (4px solid {colors.primary}) on {colors.surface-soft} using {typography.editorial} (Baskerville, 20px, 400 weight). Applied to warranty statements, certifications summaries, and brand-position paragraphs where serif authority reinforces compliance credibility. Padding is generous ({spacing.lg} vertical, {spacing.xl} horizontal) to give the serif type room to breathe inside the otherwise geometric system.

### Footer

**`footer`** — Deep teal-navy ({colors.surface-dark}, #283c48) with a 2px solid {colors.primary} top border as the section divider. Column headings use {typography.title-sm} (Poppins 600) in white; body links use {typography.body-sm} in {colors.steel-mid} (#a5acb5). Legal copy and copyright sit in {typography.caption} at reduced opacity. The logo reverses to white on the dark ground. Footer columns cover Products, Resources, Support, and Company.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, filter panel becomes full-screen sheet overlay, hero headline scales to display-sm, spec tables gain horizontal scroll with first column sticky |
| Tablet | 744–1128px | Two-column product grid, filter sidebar collapses to a horizontal filter chip strip above the grid, nav links remain visible |
| Desktop | 1128–1440px | Three-column product grid with persistent left filter sidebar (~240px), full spec table visible without scroll, hero at full bleed height |
| Wide | > 1440px | Max content width 1440px centered with expanding side margins, hero background extends edge-to-edge behind constrained copy column |

### Touch Targets
- All buttons minimum 44px height
- Filter checkboxes padded to 44×44px touch area
- Nav menu items minimum 44px height on mobile sheet
- Download card full card surface is the tap target, not just the icon
- Spec chips minimum 36px height with horizontal padding ensuring 44px effective target on mobile

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; mega-menu drops become a full-height slide-in panel
- Left product filter sidebar converts to bottom sheet overlay on mobile, triggered by a sticky "Filter & Sort" bar above the grid
- Spec table scrolls horizontally on mobile with the spec-name column fixed (position: sticky, left: 0)
- Category badge pills in the hero become a horizontally scrollable strip on mobile rather than wrapping
- Footer four-column grid stacks to two columns at tablet and single column at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific icon set confirmed; `revicons` detected in font stacks (a WordPress plugin glyph font), so actual product UI icons are unknown and likely a separate SVG set
- Exact Raleway and Poppins weight usage not confirmed beyond font-family detection; weights above are inferred from commercial lighting catalog conventions
- Baskerville placement is confirmed by font-stack detection but exact DOM context (pull quotes, legal, brand statement) is not confirmed
- Role of #003388 is ambiguous — may be an interactive hyperlink color or secondary CTA accent; excluded from load-bearing component tokens pending confirmation
- Several extracted colors (#7a00df, #4721fb, #ab1dfe, #faaca8, #dad0ec, #fafae1, #00d084, #0693e3, #34e2e4) match WordPress Gutenberg editor default palette entries and were excluded as non-brand artifacts
- No confirmed shadow or elevation tokens for modals, dropdowns, or floating panels
- No confirmed motion/animation values (duration, easing curve) — none specified in extraction
- Product image treatment (background removal, drop shadow, neutral-swatch render) not confirmed from extraction
- Mobile navigation pattern (hamburger vs. tab bar) assumed from industry norm, not confirmed from DOM analysis
