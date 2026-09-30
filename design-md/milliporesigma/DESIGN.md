---
version: alpha
name: "MilliporeSigma"
source_url: "https://www.sigmaaldrich.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Merck signature red (#E2001A) — same vermillion anchoring the parent company's global identity — arrives as a precision instrument in MilliporeSigma's otherwise austere, laboratory-grade interface. The site at sigmaaldrich.com runs at information densities calibrated for PhD researchers and procurement officers rather than casual browsers: product pages carry CAS numbers, MDL numbers, linear formula strings, and multi-column specification tables that telescope from brief descriptions to full analytical certificates in a single scroll. Navigation is organized around scientific discipline and application rather than lifestyle or aspiration — "Analytical," "Biochemistry," "Labware" replace the hero-image carousels that characterize consumer DTC brands, and the search bar is architecturally dominant because catalog-number lookup is the primary user gesture. The background runs near-white (#FFFFFF / #F5F5F5) against a deep navy (#003865) header band that creates an institutional authority register; the red surfaces only on primary CTAs and promotional banners, making each appearance load-bearing. Typography is utilitarian — a system sans stack running at body sizes as small as 12–13px to pack specification rows — with bold weight reserved for catalog identifiers and section headers rather than emotional display copy. Catalog numbers render in a monospace face, elevating the seven-digit identifier to first-class UI element; no other consumer brand treats a product code with this typographic seriousness. Radius values sit in the `{rounded.xs}`–`{rounded.sm}` range and never approach pill shapes; every corner stays functional. Spacing is compressed by consumer-web standards: the dense tabular layouts that scientists expect from print catalogs translate to tight `{spacing.sm}`–`{spacing.md}` cell padding throughout. A persistent mega-nav with discipline-level categories, a molecular structure drawing tool embedded in the search header, and horizontal-scroll pricing tables with add-to-cart per SKU row are the brand's signature functional signatures — design choices that serve bench scientists who know exactly what they need and want the fastest path to a COA download or a bulk pricing quote.

colors:
  primary: "#E2001A"
  primary-active: "#B30015"
  primary-disabled: "#F5A0A9"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  table-stripe: "#F9F9F9"
  on-primary: "#FFFFFF"
  navy: "#003865"
  navy-light: "#004F94"
  link: "#0066CC"
  link-hover: "#0052A3"
  footer-link: "#99BBDD"
  warning: "#FF9900"
  success: "#2E7D32"
  badge-new: "#004F94"

typography:
  display-xl:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  catalog-number:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  cas-number:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  nav-primary:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.2px
    textTransform: uppercase
  nav-secondary:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  table-header:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.1px
  table-cell:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  link:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
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
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
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
    padding: 7px 15px
    height: 36px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 20px
    height: 40px
    iconLeading: cart
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 6px 10px
    height: 34px
    focus: "border-color: {colors.link}; outline: 2px solid {colors.link}; outline-offset: 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 8px 12px
    height: 40px
    appendButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.none}"
      padding: 0 20px
  chemical-structure-search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    canvasBackground: "{colors.canvas}"
    toolbarBackground: "{colors.navy}"
    toolbarTextColor: "{colors.on-primary}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-primary}"
    height: 48px
    utilityBarBackground: "{colors.ink}"
    utilityBarHeight: 32px
    utilityBarTypography: "{typography.caption}"
  mega-nav:
    backgroundColor: "{colors.canvas}"
    borderTop: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
    categoryHeaderTypography: "{typography.title-sm}"
    linkTypography: "{typography.nav-secondary}"
    linkColor: "{colors.link}"
    padding: "{spacing.lg} {spacing.xl}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.link}"
    catalogTypography: "{typography.catalog-number}"
    catalogLabelColor: "{colors.muted}"
    casTypography: "{typography.cas-number}"
    priceTypography: "{typography.title-md}"
    hover:
      borderColor: "{colors.link}"
      shadow: "0 2px 8px rgba(0,0,0,0.10)"
  pricing-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.navy}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.table-cell}"
    borderColor: "{colors.hairline}"
    stripeBackground: "{colors.table-stripe}"
    rowHoverBackground: "{colors.surface-soft}"
    cellPadding: "{spacing.sm} {spacing.md}"
  specification-table:
    backgroundColor: "{colors.canvas}"
    labelBackground: "{colors.surface-soft}"
    labelTypography: "{typography.caption-bold}"
    labelColor: "{colors.body}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    cellPadding: "{spacing.sm} {spacing.md}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    hoverColor: "{colors.link}"
  badge-promotional:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sds:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link}"
    border: "1px solid {colors.link}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  document-download:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.link}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.md} {spacing.base}"
    hover:
      backgroundColor: "{colors.canvas}"
      borderColor: "{colors.link}"
  product-quantity-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    buttonBackground: "{colors.surface-soft}"
    buttonColor: "{colors.ink}"
    height: 34px
    width: 80px
  alert-banner:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.footer-link}"
    borderTop: "4px solid {colors.primary}"
    sectionHeaderTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"

## Components

### Buttons

**`button-primary`** — Red fill (#E2001A) at 36px height with 2px radius, carrying `{typography.button-md}` (14px bold Arial). Active state deepens to `{colors.primary-active}` (#B30015); disabled washes to `{colors.primary-disabled}` (#F5A0A9). Used exclusively for high-priority purchase and form submission actions; appears sparingly to preserve its urgency.

**`button-secondary`** — White background with a 1px red border and red label text, matching the primary's 36px height and 2px radius. Used for parallel CTAs on product pages — "Add to Favorites," "Get a Quote," "Request Sample" — sitting adjacent to the primary add-to-cart action without competing for attention.

**`button-navy`** — Same geometry as primary but filled with `{colors.navy}` (#003865). Appears in the utility bar and on institutional landing pages for actions like "Contact Sales," "Sign In," and "Access My Account."

**`button-ghost`** — Transparent with `{colors.link}` blue text; no border or background. Reserved for tertiary inline actions like "View All," "Compare Selected," or "Show More" within tables and filter panels, where adding visual weight would clutter the data-dense layout.

**`button-add-to-cart`** — Slightly taller (40px) red button with a leading cart icon. Anchored to the right column of product detail pages and repeated per row in pricing tables. The additional height and icon distinguish the e-commerce conversion action from informational primary buttons.

### Search Bar

**`search-bar`** — Full-width input at 40px height with a flush-attached red "Search" button (`{rounded.none}` join, zero gap). Accepts catalog number, product name, CAS number, MDL number, and chemical synonyms interchangeably. Below the main bar, a "Structure Search" toggle opens the `{chemical-structure-search}` drawer — a molecular editor canvas (JSDraw/MarvinJS) with a navy toolbar — making substructure and similarity searches available without leaving the page header.

### Navigation

**`nav-bar`** — Two-tiered header: a 32px near-black utility bar at top for account, region selector, and cart links in `{typography.caption}`, and a 48px navy primary band carrying discipline-level labels in uppercase `{typography.nav-primary}`. The navy band's institutional authority distinguishes MilliporeSigma from consumer brands that use white headers throughout.

**`mega-nav`** — Triggers on hover over any discipline tab, deploying a full-width multi-column link grid with a 2px `{colors.primary}` red accent at the top edge. Column headers use `{typography.title-sm}` bold; sub-links render in `{typography.nav-secondary}` 14px regular in `{colors.link}` blue. No imagery — the nav is a pure text grid prioritizing catalog coverage breadth. Closes on mouse-out with a 150ms fade.

### Product Card

**`product-card`** — 1px `{colors.hairline}` border, 2px radius, white fill. Product name in `{colors.link}` blue at `{typography.title-sm}` links to the detail page. The catalog number renders directly below in `{typography.catalog-number}` monospace bold — a deliberate typographic choice that marks the identifier as a distinct data class. CAS number appears in `{typography.cas-number}` at lighter weight. Pack size options and price follow, with the add-to-cart button appearing inline on search results grids. Hover state promotes the border to `{colors.link}`.

### Pricing Table

**`pricing-table`** — Full-width data table with a navy header row in `{typography.table-header}` white. Body rows alternate between `{colors.canvas}` and `{colors.table-stripe}` (#F9F9F9) at `{typography.table-cell}` 13px; row hover turns `{colors.surface-soft}`. Standard columns: Catalog Number, Description, Pack Size, Price, and a per-row Quantity + Add to Cart control. This table is the primary purchase interface for multi-SKU products and drives the majority of add-to-cart conversions.

### Specification Table

**`specification-table`** — Two-column label/value grid with `{colors.surface-soft}` gray label cells against white value cells. Labels use `{typography.caption-bold}` 12px; values use `{typography.body-sm}` 13px. Cell padding is `{spacing.sm} {spacing.md}`. Used throughout product detail pages for physicochemical properties, quality grades, regulatory data, and storage conditions. Borders use `{colors.hairline-soft}` for minimal visual noise.

### Document Downloads

**`document-download`** — Card-style row with a red document icon at left, blue-linked filename in `{typography.body-md}`, and metadata (file type, revision date) in `{typography.caption}` muted gray. Grouped in a Documents & Certificates section to surface SDS sheets, COAs, technical bulletins, and application notes. Hover shifts the outer border to `{colors.link}` blue and brightens the background to `{colors.canvas}`.

### Badges

**`badge-promotional`** — Small red chip at `{rounded.xs}` with `{typography.caption-bold}` 12px white text. Used on search result cards to flag promotional pricing or bundle deals. **`badge-new`** — Same geometry with navy fill (#004F94); applied to recently added catalog entries. **`badge-sds`** — Outlined chip in `{colors.link}` blue on transparent background; signals SDS document availability without the urgency weight of filled badges.

### Alert Banner

**`alert-banner`** — Full-width amber (#FF9900) strip at `{rounded.none}` pinned below the nav for site-wide announcements: shipping delays, regulatory compliance notices, system maintenance windows. Ink-colored text in `{typography.body-sm}` keeps readability high against the warm background.

### Footer

**`footer`** — Navy (#003865) background with a 4px `{colors.primary}` red top border as the single brand-color flourish at the bottom of the page. Section headers use `{typography.title-sm}` white bold; links use `{typography.body-sm}` in desaturated light-blue (#99BBDD) for legibility on dark. Standard sections: Products & Services, Support, Company, Legal, and a country/language selector.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Mega-nav collapses to hamburger drawer; search bar goes full-width below nav band; chemical structure search hidden; pricing tables scroll horizontally; product cards stack single-column; utility bar condenses to icon-only |
| Tablet | 744–1128px | Two-column product grid; mega-nav collapses to accordion drawers on tap; specification tables maintain two-column layout; left sidebar filters appear as collapsible panel |
| Desktop | 1128–1440px | Three-column product grid; mega-nav at full hover behavior; persistent left sidebar filters on search results; product detail pages render two-column (image + content) |
| Wide | > 1440px | Max-width container (~1400px) centered with auto margins; four-column product grid on category pages; persistent sidebar widens to 280px |

### Touch Targets

- All primary CTA buttons minimum 44px tall on mobile (overriding the 36px desktop default)
- Quantity selector increment/decrement buttons expand to 44×44px touch areas on mobile
- Hamburger and utility bar icons at minimum 44×44px touch areas
- Mega-nav accordion rows at minimum 48px row height for reliable tapping
- Document download rows gain 8px additional vertical padding on touch viewports

### Collapsing Strategy

- Mega-nav discipline tabs collapse to a full-screen side drawer on mobile, preserving the category hierarchy as expandable accordion sections with `{colors.primary}` active indicators
- Specification tables maintain label/value structure on mobile at 100% width with wrapping value cells — they do not collapse to single-column cards
- Pricing tables on mobile display horizontal scroll with sticky first column (Catalog Number) so users retain orientation while scrolling through pack sizes and prices
- Chemical structure search widget is hidden on viewports under 744px; a "Use Desktop for Structure Search" message appears in its trigger location
- Breadcrumbs truncate on mobile to show only the immediate parent category and current page title

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — all color values are derived from publicly documented Merck KGaA brand identity and general knowledge of the sigmaaldrich.com visual appearance; treat as approximate and verify against DevTools computed styles
- No font-family stacks were extractable; the Arial/Helvetica system stack is an inference from pharmaceutical/scientific brand conventions; the site may use a licensed typeface such as MyriadPro, FF DIN, or a proprietary Merck typeface
- Exact button heights, padding values, and border-radius measurements are estimated from visual knowledge rather than extracted computed styles; measure in DevTools before building
- The molecular structure drawing tool (JSDraw / MarvinJS) ships its own internal design system not documented here
- Sub-brand palette variants for BioReliance, SAFC, and Supelco product lines within the MilliporeSigma umbrella are not addressed
- Product image treatment, lightbox zoom behavior, and certificate-of-analysis viewer modal styling are not documented
- Tiered pricing display states (contract pricing, login-gated pricing, bulk quote flows) require separate business logic documentation beyond static design specs
- Dark-mode support, if any, is undocumented
