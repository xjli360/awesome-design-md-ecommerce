---
version: alpha
name: "Qiagen"
source_url: "https://www.qiagen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Futura W01 — three weights loading as separate webfont faces rather than a variable axis — handles every scale from the 11px uppercase catalog label to the 40px campaign headline, a typographic choice that signals geometric precision over the humanist warmth that most scientific instrumentation brands reach for. The primary voltage is #004d9f, a deep institutional navy that appears on primary CTAs, active navigation text, and anchor links; it stratifies downward through #1043aa for inline interactive text and #1b3067 for high-contrast display moments against dark fills. Below that, blue-gray #65708b and #677084 carry metadata and secondary annotations — the shades a researcher's eye scans past while hunting kit lot numbers. The surface palette is clinical without being sterile: #faf9fd as the primary background carries a barely-perceptible violet warmth against pure white (#ffffff) card fills, with #e5eff9 and #eef0f4 as departmental section tints communicating application area without introducing new hue families. Hairlines at #d0d6df and #e0e2ec separate catalog rows and table cells at low visual cost. Three descending error reds (#ba1a1a → #9e002a → #93000a) reveal a Material 3–influenced token architecture beneath the surface — an unusually granular error-state spec for a B2B catalog, suggesting a design-system refresh that adopted semantic token conventions while preserving Futura as the immovable brand constant. Buttons carry `{rounded.sm}` at 4px — not zero, but close enough that the UI reads as rectilinear rather than friendly. Icon fonts (Three_Size_Icons, glyphicons) embedded alongside the webfonts reveal a component architecture that predates the current design system, with legacy glyph layers living inside the modern token shell. The global search bar is the site's real primary interaction surface, positioned to serve researchers who navigate by product name, gene target, or catalog number rather than by visual browsing.

colors:
  primary: "#004d9f"
  primary-active: "#1b3067"
  primary-disabled: "#87a6d5"
  primary-light: "#e5eff9"
  interactive: "#1043aa"
  ink: "#1a1b1f"
  body: "#2f3033"
  muted: "#44474e"
  muted-soft: "#65708b"
  muted-subtle: "#677084"
  hairline: "#d0d6df"
  hairline-soft: "#e0e2ec"
  border: "#bcbcbb"
  canvas: "#faf9fd"
  surface-soft: "#f4f6fa"
  surface-card: "#ffffff"
  surface-tint: "#eef0f4"
  surface-neutral: "#f4f3f7"
  surface-pale: "#f9f9f9"
  on-primary: "#ffffff"
  error: "#ba1a1a"
  error-dark: "#9e002a"
  error-deep: "#93000a"
  error-surface: "#ffeaea"
  mid-blue: "#87a6d5"
  blue-tint: "#eef0f4"

typography:
  display-xl:
    fontFamily: "'Futura W01 Bold', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Futura W01 Bold', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Futura W01 Book', 'futura-book', 'futura-book-std', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Futura W01 Book', 'futura-book', 'futura-book-std', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Futura W01 Book', 'futura-book', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  catalog-id:
    fontFamily: "'Futura W01 Book', 'futura-book', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px
  label-uppercase:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.88px
    textTransform: uppercase
  button-md:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Futura W01 Medium', 'Futura W01', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 10px 24px
    height: 40px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 9px 23px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.interactive}"
    typography: "{typography.body-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 8px 12px
    height: 40px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMarkColor: "{colors.primary}"
    activeTextColor: "{colors.primary}"
    dropdownIndicatorColor: "{colors.muted-soft}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    padding: "{spacing.lg}"
    linkHoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.primary}"
    idTypography: "{typography.catalog-id}"
    idColor: "{colors.muted-soft}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    padding: "{spacing.lg}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    subheadColor: "{colors.primary-light}"
    minHeight: 400px
    padding: "{spacing.xxl} {spacing.section}"
    ctaBackgroundColor: "{colors.on-primary}"
    ctaTextColor: "{colors.primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.primary}"
    subheadTypography: "{typography.display-sm}"
    subheadColor: "{colors.muted}"
    minHeight: 360px
    padding: "{spacing.xxl} {spacing.section}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    height: 44px
    placeholderColor: "{colors.muted-soft}"
    searchButtonBackgroundColor: "{colors.primary}"
    searchButtonTextColor: "{colors.on-primary}"
    searchButtonTypography: "{typography.button-sm}"
    searchButtonRounded: "{rounded.xs}"
    searchButtonPadding: 0 16px
  application-tag:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    border: none
    padding: 6px 14px
  resource-card:
    backgroundColor: "{colors.surface-pale}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.interactive}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted-soft}"
    typeTagTypography: "{typography.label-uppercase}"
    typeTagColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    accentBorderLeft: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
    hoverBorderColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
    linkTextColor: "{colors.interactive}"
    separatorColor: "{colors.muted-soft}"
  alert-error:
    backgroundColor: "{colors.error-surface}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.error}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.error-dark}"
    padding: "{spacing.md} {spacing.base}"
  alert-info:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.primary-disabled}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  section-tint:
    backgroundColor: "{colors.surface-tint}"
    padding: "{spacing.section} 0"
  data-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.label-uppercase}"
    cellTextColor: "{colors.body}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowHoverBackgroundColor: "{colors.primary-light}"
    idCellTypography: "{typography.catalog-id}"
    idCellColor: "{colors.muted-soft}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    iconColor: "{colors.primary}"
    expandedBackgroundColor: "{colors.canvas}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.mid-blue}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.on-primary}"
    borderTopColor: "{colors.primary}"
    borderTopWidth: 3px
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — Deep navy #004d9f fill with white Futura W01 Medium text in 14px uppercase with 0.5px tracking, 4px border radius (`{rounded.sm}`), 40px height, 24px horizontal padding. Hover shifts to #1b3067 (`button-primary-hover`); disabled state lightens the fill to #87a6d5 (`primary-disabled`) without changing text color. Used exclusively for primary catalog and lead-gen actions: "Order Now", "Request Quote", "Download Protocol".

**`button-secondary`** — White fill with 1.5px #004d9f border and matching navy text; mirrors primary dimensions. On hover, background tints to `{colors.primary-light}` (#e5eff9) and border/text darken to #1b3067 — a subtle state change appropriate for a site where multiple CTAs compete on a single product page.

**`button-tertiary`** — Transparent, no border; 14px body-sm Futura Book in #1043aa with underline. Used for secondary actions within dense spec tables and resource sections where a full button would break reading rhythm.

### Search

**`search-bar`** — The dominant interaction surface on the global nav. 44px height, 1px #d0d6df border sharpening to 1.5px primary on focus. The attached search button sits flush-right inside the bar with a `{rounded.xs}` (2px) right cap, #004d9f fill, and uppercase Futura W01 Medium 12px label. Autocomplete suggestions drop in a `{rounded.sm}` panel matching `nav-dropdown` shadow treatment. Placeholder text runs in `{colors.muted-soft}` (#65708b).

### Navigation

**`nav-bar`** — 64px white bar with 1px #d0d6df bottom border. Logo mark anchors left in primary navy. Top-level links use Futura W01 Medium 14px; active state text color shifts to #004d9f with a 2px primary underline. Mega-dropdown menus (`nav-dropdown`) open on hover, using `{typography.label-uppercase}` headings in #65708b to group product families (e.g., "SAMPLE TECHNOLOGIES", "PCR & RT-PCR") above 14px regular links. Dropdown closes on outside click or ESC; no animation delay longer than 150ms to serve power users navigating dense catalogs.

### Product Card

**`product-card`** — White card, 1px #d0d6df border that shifts to primary navy on hover, `{rounded.sm}`. Catalog ID renders in 12px `{typography.catalog-id}` at #65708b above the title. Product name uses `{typography.title-sm}` in #1043aa as a link. Description body in 14px Futura Book. Ordering/inquiry CTA renders as `{typography.button-sm}` uppercase text link in #004d9f with hover underline; full button variant available for featured card slots.

### Hero Banner

**`hero-banner`** — Full-width #004d9f fill with 40px Futura W01 Bold headline and 22px medium subhead in #e5eff9. CTA button inverts to white fill / navy text (`on-primary` / `primary`) to maintain contrast. Minimum 400px height accommodates photography overlays. A light variant (`hero-banner-light`) uses `{colors.surface-soft}` background with primary navy headline for editorial and resource-hub sections.

### Application Tags & Category Chips

**`application-tag`** — #e5eff9 pill with #004d9f 11px uppercase Futura Medium, 2px radius. Applied to product cards and search results to label application area (e.g., "GENOMICS", "DIAGNOSTICS"). Multiple tags stack horizontally.

**`category-chip`** / **`category-chip-active`** — Rounded full-radius (20px) toggle chips for filtering result sets. Inactive state: white fill, #d0d6df border, #44474e text. Active: solid #004d9f fill, white text. Used in filterable catalog grids and application browser sidebars.

### Resource Card

**`resource-card`** — #f9f9f9 surface, 1px soft hairline border, 3px left-edge #004d9f accent stripe that identifies it as a document rather than a product. Title in `{typography.title-sm}` #1043aa link; resource type (Application Note, Brochure, Webinar) renders in `{typography.label-uppercase}` #65708b above the title. Publication date and size metadata in 12px caption. Hover elevates border to primary navy.

### Data Table

**`data-table`** — Used extensively on product specification and ordering pages. Header row in `{colors.surface-soft}` with 11px uppercase Futura Medium labels. Catalog numbers in `{typography.catalog-id}` at #65708b; spec values in 14px Futura Book. Alternating hover highlight at #e5eff9. 1px #d0d6df horizontal borders only — no vertical grid lines. Critical for the ordering flow where researchers compare kit sizes, quantities, and pricing across rows.

### Accordion

**`accordion`** — Used for FAQs, protocol steps, and product description expansion. Title row in `{typography.title-sm}` with a right-aligned chevron in primary navy. Bottom border at `{colors.hairline}` separates items. Expanded state background shifts to `{colors.canvas}` (#faf9fd); body text in 14px Futura Book.

### Alerts

**`alert-error`** — #ffeaea background, 1px #ba1a1a border, error-red text with `{colors.error-dark}` icon. Used for form validation, ordering errors, and regulatory notices. **`alert-info`** mirrors structure in the `{colors.primary-light}` / `{colors.primary-active}` family for informational notices (e.g., product availability, shipping restrictions).

### Footer

**`footer`** — #1a1b1f near-black fill with 3px top border in #004d9f. Link columns use 11px uppercase Futura Medium headers in white; body links in 14px Futura Book at #87a6d5, shifting to white on hover. Legal copy sits in 12px Futura Book at #65708b in a subdued row below the main columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hamburger nav replaces mega-menu; search bar collapses to icon tap-target that expands full-width; product cards stack vertically; data tables scroll horizontally; hero min-height drops to 280px |
| Tablet | 744–1128px | Two-column product grid; nav retains top bar with flyout drawer replacing mega-dropdown; search bar full-width in drawer; hero at 340px min-height; resource cards in 2-up grid |
| Desktop | 1128–1440px | Full mega-menu navigation; three- or four-column product grid; search bar embedded in nav bar; data tables fully visible; hero at 400px+ with optional image panel |
| Wide | > 1440px | Content max-width 1280px centered; hero image bleeds edge-to-edge behind constrained text column; footer columns spread to five-up with logo block; section padding increases to `{spacing.section}` on each side |

### Touch Targets

- All nav top-level links minimum 44×44px tap area, expanded via padding
- Search icon tap target 44×44px before bar expands
- Product card titles link area extends full card width on mobile
- Accordion rows minimum 48px height on touch
- Buttons minimum 40px height; 44px on mobile breakpoint
- Category chips minimum 36px height on touch

### Collapsing Strategy

- Mega-menu nav collapses to hamburger drawer at < 1024px; drawer uses full-height slide-in from left
- Product filters move from sidebar to top-anchored horizontal chip scroll at < 744px
- Hero text column occupies 100% width below 744px; image stacks below or becomes background with scrim
- Data tables gain horizontal scroll container on mobile; sticky first column (catalog ID) for orientation
- Footer column grid collapses 5→3→1 column across breakpoints; headings become tap-to-expand accordion on mobile
- Secondary nav tabs (application sub-categories) convert to horizontal scroll strip below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button height and padding values not extracted from live CSS; 40px height and 10/24px padding are inferred from visual inspection typical of Futura-set B2B sites
- Font sizes for display scales not directly extracted; values above are inferred from viewport proportion and Qiagen's known marketing templates
- Icon system specifics: Three_Size_Icons and glyphicons font families are present but individual glyph mappings, sizes, and usage rules are not documented
- Error-surface token (#ffeaea) is derived from the three extracted error reds (#ba1a1a, #9e002a, #93000a) — no light error container was directly observed in the color extraction
- Animation and transition durations not extracted
- Exact box-shadow values for cards and dropdowns not extracted; 0 4px 16px rgba(0,0,0,0.10) is an approximation
- Navigation hover/active underline thickness and offset not confirmed from extraction
- Mobile breakpoint exact px values (744px, 1128px used above) are inferred; Qiagen may use different grid breakpoints (e.g., 768px, 1024px) in their framework
- Product image aspect ratios and lazy-load strategy not observed
- Dark-mode support status unclear; theme-color is #ffffff but no prefers-color-scheme rules confirmed
