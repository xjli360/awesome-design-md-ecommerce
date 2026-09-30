---
version: alpha
name: "Tocris Bioscience"
source_url: "https://www.tocris.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Each compound page at Tocris arrives pre-loaded as a condensed scientific briefing — target class badge, biological activity summary, molecular weight, solubility window, and peer-reviewed citations all appear before any add-to-cart button. This data-first hierarchy is the dominant visual fact of the design: product identity is established through pharmacological precision, not lifestyle photography. The primary color is an estimated corporate-science blue (approximately #005A9C, documented here with low confidence — see Known Gaps), applied to headers, primary CTAs, and navigation anchors against a near-white canvas. Gray hairlines at roughly #DDDDDD divide compound data tables and filter sidebars with the same measured regularity as ruled laboratory notebook pages. Rounded values are minimal throughout — buttons and cards carry tight radii near `{rounded.xs}` to `{rounded.sm}`, consistent with institutional software that prioritizes information density over consumer warmth. Typography leans on system sans-serif stacks at moderate weights; display headings stay restrained (font-weight 600 at most) while body copy drops to 14px in data tables to accommodate the volume of technical annotation per compound. The catalog browsing experience features a deep filter sidebar — target, pathway, research area, product type — that behaves more like a database query interface than a typical e-commerce facet panel. Product cards in grid view carry compound name, catalog number, target class, and biological activity summary as four mandatory fields before price, communicating that this audience reads assay data before checking cost. Structural signals reinforce the scientific register: monospace digits for catalog numbers, tabular-nums alignment in pricing columns, and tightly leaded captions for citation metadata. The footer organizes resources (literature, protocols, FAQs) with the same categorical discipline as the catalog itself, treating documentation as a first-class destination rather than legal boilerplate.

colors:
  primary: "#005A9C"
  primary-active: "#004070"
  primary-disabled: "#99BBDD"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#6B6B6B"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F0F4F8"
  surface-subtle: "#F7F9FC"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  success: "#2E7D32"
  success-bg: "#EDF7ED"
  warning: "#B05000"
  warning-bg: "#FFF3E0"
  error: "#C62828"
  data-highlight: "#E8F0FA"
  catalog-num: "#333333"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, 'Nimbus Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.36
    letterSpacing: 0.4px
    textTransform: uppercase
  data-cell:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  catalog-num:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase
  citation-meta:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
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
    padding: 9px 19px
    height: 40px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
    height: 30px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 52px
    topBand:
      backgroundColor: "{colors.primary-active}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      height: 32px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
    sectionHeaderTypography: "{typography.title-sm}"
    itemTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 48px 10px 16px
    height: 44px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 44px
  filter-sidebar:
    backgroundColor: "{colors.surface-subtle}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    width: 240px
    sectionHeaderTypography: "{typography.title-sm}"
    sectionHeaderColor: "{colors.ink}"
    itemTypography: "{typography.body-sm}"
    itemColor: "{colors.body}"
    checkboxAccent: "{colors.primary}"
    divider: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    shadow: "none"
    shadowHover: "0 2px 8px rgba(0,0,0,0.10)"
    padding: "{spacing.base}"
    compoundNameTypography: "{typography.title-md}"
    compoundNameColor: "{colors.primary}"
    catalogNumTypography: "{typography.catalog-num}"
    catalogNumColor: "{colors.catalog-num}"
    activityTypography: "{typography.body-sm}"
    activityColor: "{colors.body}"
    targetBadge: "{components.target-class-badge}"
    priceTypography: "{typography.title-sm}"
    priceColor: "{colors.ink}"
  target-class-badge:
    backgroundColor: "{colors.data-highlight}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  availability-badge-instock:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  availability-badge-limited:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  compound-data-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    rowTypography: "{typography.data-cell}"
    rowColor: "{colors.body}"
    rowAltBackgroundColor: "{colors.surface-subtle}"
    rowHoverBackgroundColor: "{colors.data-highlight}"
    catalogNumTypography: "{typography.catalog-num}"
  product-detail-tabs:
    backgroundColor: "{colors.canvas}"
    activeTabColor: "{colors.primary}"
    activeTabBorder: "2px solid {colors.primary}"
    inactiveTabColor: "{colors.muted}"
    inactiveTabBorder: "none"
    typography: "{typography.title-sm}"
    tabBarBorder: "1px solid {colors.hairline}"
  citation-item:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    authorTypography: "{typography.citation-meta}"
    authorColor: "{colors.muted}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.primary}"
    journalTypography: "{typography.caption}"
    journalColor: "{colors.muted}"
  solubility-panel:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
  pathway-diagram-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  quick-order-widget:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    sizeSelectTypography: "{typography.body-sm}"
    sizeSelectColor: "{colors.ink}"
    quantityInputWidth: 64px
  hero-catalog:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-md}"
    subTypography: "{typography.body-md}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.xxl} {spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "2px solid {colors.primary}"
    textColor: "{colors.body}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    copyrightTypography: "{typography.caption}"
    copyrightColor: "{colors.muted}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid `{colors.primary}` fill (#005A9C estimated) with white text at `{typography.button-md}` weight 600, tight `{rounded.xs}` radius (4px), 40px tall. Hover and focus darken to `{colors.primary-active}`; disabled state uses `{colors.primary-disabled}` with reduced opacity. Used for primary catalog actions: Add to Cart, Request Quote, Download SDS.

**`button-secondary`** — White fill with a `{colors.primary}` 1px border and matching text, same sizing and radius as primary. Represents lower-commitment actions: Save to List, Compare, View Related Products.

**`button-sm`** — Compact 30px-tall variant for inline table actions and filter chips. Same `{colors.primary}` fill, `{rounded.xs}` radius, `{typography.button-sm}` at 13px weight 600.

**`button-ghost`** — Transparent background with `{colors.primary}` text, no border. Used inside citation items and compound cards for secondary links like "View all literature" or "See related targets."

### Navigation

**`nav-bar`** — Two-band structure: a slim 32px utility band in `{colors.primary-active}` carrying account links, currency selector, and basket count at `{typography.caption}`; below it a 52px primary band in `{colors.primary}` with the Tocris logo left and a horizontal product-category nav at `{typography.nav-link}` weight 600 in white. The catalog's depth necessitates a `{components.nav-mega-menu}` flyout on hover for each major category.

**`nav-mega-menu`** — Full-width white panel anchored below the primary nav band, 1px hairline border on sides and bottom, 12px drop shadow. Internally organized into columns with `{typography.title-sm}` section headers and `{typography.body-sm}` item links. Tocris's catalog is deep (1000+ targets), so mega menus can carry three to four columns with a "Browse All" CTA at the bottom.

### Search

**`search-bar`** — 44px tall, `{rounded.xs}` left side, squared right side where a `{colors.primary}` submit button is flush-attached. Placeholder text at `{typography.body-md}` in `{colors.muted}`. On focus, border upgrades to 2px `{colors.primary}`. An autocomplete dropdown suggests compound names and catalog numbers with `{typography.catalog-num}` rendering for the catalog-number tokens. Positioned prominently in the nav or as a full-width section on the catalog homepage.

### Product Card

**`product-card`** — White card with `{colors.hairline}` border, no shadow at rest, subtle shadow on hover. Compound name at `{typography.title-md}` in `{colors.primary}` (acts as a link), catalog number beneath in `{typography.catalog-num}` monospace. A `{components.target-class-badge}` appears inline with the name. Biological activity is shown in 2 lines of `{typography.body-sm}` before truncation. Price sits at bottom-right at `{typography.title-sm}`. Add-to-cart and size-select elements compact into the card footer.

### Compound Data Table

**`compound-data-table`** — Dense tabular layout for size/concentration variants. Alternating row backgrounds (`{colors.canvas}` / `{colors.surface-subtle}`) with `{colors.data-highlight}` on hover. Header row on `{colors.surface-soft}` at `{typography.title-sm}` weight 600. Data cells at `{typography.data-cell}` 13px; catalog numbers always rendered in `{typography.catalog-num}` monospace for scanability. No border-radius — the table's visual weight signals authoritative data, not consumer-facing softness.

### Badges and Tags

**`target-class-badge`** — Light-blue `{colors.data-highlight}` fill with `{colors.primary}` text at `{typography.badge-label}` (11px, uppercase, weight 700). `{rounded.xs}` radius. Appears on product cards and the product detail page header to communicate pharmacological target category (e.g., GPCR, Ion Channel, Enzyme).

**`availability-badge-instock`** / **`availability-badge-limited`** — Green-tinted or amber-tinted pill badges at `{typography.badge-label}`. Appear in the table and quick-order widget to communicate real-time inventory status without disrupting the data grid.

### Product Detail Tabs

**`product-detail-tabs`** — Horizontal tab bar, bottom-border style. Active tab carries a `{colors.primary}` 2px underline and matching text color. Inactive tabs in `{colors.muted}`. The full tab bar sits on a `{colors.hairline}` bottom border. Typical tab set: Overview, References, Technical Data, Related Products. This is a high-traffic component on Tocris — researchers navigate directly to References to pull citation context.

### Citations

**`citation-item`** — Compact card with 1px `{colors.hairline-soft}` border and `{rounded.xs}` radius. Title at `{typography.body-sm}` in `{colors.primary}` (linked to PubMed or DOI). Authors and year at `{typography.citation-meta}` in `{colors.muted}`. Journal abbreviation and volume at `{typography.caption}`. A ghost CTA links to the full reference. Citations are numbered and their compound application context (target, assay type) may appear as an additional line.

### Solubility Panel

**`solubility-panel`** — Compact information panel in `{colors.surface-soft}` showing solubility in aqueous and organic solvents. Labels in `{typography.caption-label}` (uppercase, 11px) at `{colors.muted}`; values in `{typography.body-sm}` at `{colors.ink}`. Separated from the main compound description by a `{colors.hairline}` divider. Key for researchers before assay preparation.

### Quick Order Widget

**`quick-order-widget`** — Right-column panel on the product detail page. Contains a size/format dropdown at `{typography.body-sm}`, a numeric quantity input (64px wide), and a `{components.button-primary}` CTA. Background in `{colors.surface-soft}` to visually separate from the information column. Price updates dynamically on size selection.

### Hero

**`hero-catalog`** — Full-width banner in `{colors.primary}` blue. Heading in `{typography.display-md}` white, subtext in `{typography.body-md}` white at reduced opacity. A single `{components.button-primary}` CTA in white-background override or a contrasting pale variant. Used on category landing pages (e.g., Ion Channels, Neurotransmitters) as the section entry point.

### Footer

**`footer`** — `{colors.surface-soft}` background with a `{colors.primary}` 2px top border as a structural closing signal. Column headers at `{typography.title-sm}` in `{colors.ink}`. Links at `{typography.body-sm}` in `{colors.primary}`. Bio-Techne parent branding appears in the lower footer row. Copyright and legal links at `{typography.caption}` in `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar collapses to a modal drawer triggered by a filter button; nav compresses to hamburger menu; search bar full-width below nav; compound data table scrolls horizontally; quick-order widget moves below product detail content |
| Tablet | 744–1128px | Two-column product grid; filter sidebar shows as collapsible left rail (240px); nav shows primary categories with overflow into hamburger; search bar remains full-width in nav band |
| Desktop | 1128–1440px | Three-column product grid; filter sidebar fixed at 240px left; full mega-menu navigation; search bar 480px max-width in nav; product detail in two-column layout (info left, quick-order widget right) |
| Wide | > 1440px | Max-width container (~1400px) centers the layout; four-column grid optional for broad catalog pages; nav mega-menu panels cap at content width |

### Touch Targets

- All filter checkboxes minimum 44×44px touch target with ample vertical spacing
- Add-to-cart and CTA buttons minimum 40px height; on mobile expand to 48px for primary actions
- Tab bar items minimum 44px tap height with generous horizontal padding
- Citation links padded to at least 36px tap height given their smaller typography

### Collapsing Strategy

- Filter sidebar collapses to bottom-sheet modal on mobile with an "Apply Filters" commit button; active filter count shown as a badge on the filter trigger button
- Compound data table switches from full grid to a stacked card-per-row presentation below 480px, promoting catalog number and pack size as primary visible fields
- Mega-menu nav fully replaced by an accordion drawer on mobile; each top-level category expands to show sub-category links
- Product detail tabs reduce to a scrollable horizontal strip with no wrapping; tabs that overflow are accessible via horizontal scroll
- Footer columns stack vertically, each section header becomes an accordion toggle to save vertical space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors estimated**: The live site returned zero hex values from automated extraction (likely JavaScript-loaded tokens or anti-bot protection). Colors above are cautious estimates based on Tocris's documented brand identity as a Bio-Techne company; the specific blue `#005A9C` may be off by a significant margin. Verify against the official Tocris brand guide or computed styles.
- **No fonts extracted**: Typography stacks above use generic sans-serif web defaults. Tocris may license a specific typeface (potentially inherited from the Bio-Techne parent brand system). Inspect `document.fonts` or network requests for actual webfont URLs.
- **Catalog number font unconfirmed**: Monospace treatment for catalog numbers (`{typography.catalog-num}`) is inferred from standard scientific catalog conventions; confirm whether the live site uses an actual monospace face or just numeric tabular-nums on a proportional font.
- **Specific red/orange accent unconfirmed**: No evidence of whether Tocris uses a secondary accent color (orange, red, or teal) for promotional banners or section highlights. The warning color `#B05000` is a placeholder.
- **Icon system unknown**: Navigation and UI icon family (whether custom, Material, or Font Awesome variant) was not extractable.
- **Dark-mode support unknown**: Whether Tocris implements a dark-mode variant for laboratory/low-light use cases was not determinable from extraction.
- **Meta theme-color absent**: No PWA or mobile theme-color metadata was returned; mobile browser chrome color unspecified.
