---
version: alpha
name: "Abcam"
source_url: "https://www.abcam.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Teal at the hue of copper sulfate in solution — approximately #00b5c8 — anchors every primary CTA, navigation highlight, and active filter chip across Abcam's catalog, providing wayfinding inside a product database spanning hundreds of thousands of antibody and assay SKUs. The design problem is not branding but information architecture: a researcher arriving from a PubMed citation needs a product detail page that simultaneously surfaces reactivity species, host organism, conjugation state, application validation icons, and peer-citation count without the cognitive collapse typical of industrial lab-supply sites. Abcam resolves this with a white canvas and a hairline grid that compartmentalizes specification tables, product imagery, and social-proof panels into distinct reading zones. Type runs a clean system sans-serif stack — weight 400 for body copy, 600 for section labels — keeping the voice neutral and referential rather than editorial. The teal primary falls between pharmaceutical blue and consumer-tech cyan, occupying a hue register that connotes precision instruments, reagent vials, and PCR visualization dashboards rather than either clinical software or SaaS startups. Interactive elements carry modest {rounded.sm} corners — professional enough for purchasing decisions that affect experimental reproducibility, accessible enough to signal that Abcam is a direct-to-researcher platform rather than a wholesale distributor catalog. Secondary surfaces at {colors.surface-soft} delineate content zones without adding color noise. The overall palette is deliberately three-tone — teal, white, and near-black — because the real visual content on any Abcam page is fluorescence microscopy imagery, Western blot validation panels, and immunohistochemistry tissue sections embedded as product evidence. Navigation carries a sticky white bar with the teal logo mark and a prominent search input, reflecting how discovery on a research supply site is almost always search-first rather than browse-first. Filter chips in the left facet rail use {rounded.full} pill shapes for tactile contrast against the {rounded.sm} card edges, and active selections pull the primary teal to mark navigational state across a facet tree that can span dozens of specification categories. Footer architecture reflects the institutional customer base: regulatory documentation, distributor contacts, and compliance certificates anchor the bottom band on a near-black background with the teal top border as the only brand signal at that depth.

colors:
  primary: "#00b5c8"
  primary-hover: "#009db5"
  primary-active: "#008fa0"
  primary-disabled: "#b3e8ee"
  science-teal-light: "#e0f7fa"
  surface-teal: "#f0fbfd"
  ink: "#1c2431"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#16a34a"
  success-soft: "#dcfce7"
  warning: "#d97706"
  warning-soft: "#fef3c7"
  error: "#dc2626"
  error-soft: "#fef2f2"

typography:
  display-xl:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-label:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  product-sku:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-hover}"
    active:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.primary}"
    hover:
      backgroundColor: "{colors.surface-teal}"
    active:
      backgroundColor: "{colors.science-teal-light}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    hover:
      textDecoration: underline
      backgroundColor: transparent

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    focus:
      borderColor: "{colors.primary}"
      outline: "2px solid {colors.science-teal-light}"
    error:
      borderColor: "{colors.error}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    activeColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    position: sticky
    top: 0
    zIndex: 100

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
    focus:
      borderColor: "{colors.primary}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.sm}"
      padding: 0 20px
      hover:
        backgroundColor: "{colors.primary-hover}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    skuTypography: "{typography.product-sku}"
    skuColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    hover:
      borderColor: "{colors.primary}"
      boxShadow: "0 2px 12px rgba(0, 181, 200, 0.12)"

  validation-badge:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    border: "1px solid {colors.primary-disabled}"

  application-icon-set:
    iconSize: 24px
    activeColor: "{colors.primary}"
    inactiveColor: "{colors.muted-soft}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    layout: row
    gap: "{spacing.md}"
    tooltipBackground: "{colors.ink}"
    tooltipTextColor: "{colors.canvas}"
    tooltipRounded: "{rounded.xs}"

  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerTextColor: "{colors.body}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rowHoverBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    keyColumnWidth: 220px

  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    sectionLabelTypography: "{typography.spec-label}"
    sectionLabelColor: "{colors.body}"
    activeChipBackground: "{colors.primary}"
    activeChipTextColor: "{colors.on-primary}"
    inactiveChipBackground: "{colors.surface-soft}"
    inactiveChipBorder: "1px solid {colors.hairline}"
    chipRounded: "{rounded.full}"
    chipTypography: "{typography.button-sm}"
    width: 256px
    borderRight: "1px solid {colors.hairline}"

  citation-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    countTypography: "{typography.display-sm}"
    countColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"

  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    hoverColor: "{colors.primary}"

  hero-catalog:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
    searchBarEmbedded: true
    borderBottom: "1px solid {colors.hairline}"

  section-divider-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    accentBorder: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"

  alert-banner:
    infoBackground: "{colors.science-teal-light}"
    infoTextColor: "{colors.primary-active}"
    infoBorder: "1px solid {colors.primary-disabled}"
    successBackground: "{colors.success-soft}"
    successTextColor: "{colors.success}"
    errorBackground: "{colors.error-soft}"
    errorTextColor: "{colors.error}"
    warningBackground: "{colors.warning-soft}"
    warningTextColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — The teal fill (#00b5c8) CTA used for Add to Cart, Request Quote, and primary search submission. Height is 44px with 24px horizontal padding and {rounded.sm} corners; weight 600 at 15px reads as assertive without overpowering the dense specification context around it. Hover darkens to #009db5, active to #008fa0, disabled fades to the pale teal #b3e8ee — all three states remain on-brand within the same hue family.

**`button-secondary`** — White fill with a 1.5px teal border and teal text, used for secondary actions like Download Datasheet or Compare. Paired with `button-primary` on product detail pages, the two-button pairing keeps action hierarchy clear against white card surfaces. Hover fills the background with `{colors.surface-teal}` rather than inverting colors, preserving legibility.

**`button-ghost`** — Transparent background with teal text, used inline for See All, View Protocol, and expandable section toggles. Underline on hover indicates the link register without adding a border to already-dense layout areas.

### Search Bar

**`search-bar`** — A full-width input with an attached teal submit button, positioned as the primary navigation mechanism in the sticky nav bar and repeated in the hero. The input border is `{colors.hairline}` at rest and transitions to `{colors.primary}` on focus with a soft outline ring from `{colors.science-teal-light}`. Autocomplete suggestions drop in a white surface card below with {rounded.sm} and a hairline border.

### Navigation

**`nav-bar`** — Sticky white bar at 64px height with a bottom hairline border. The teal logo anchors the left; primary product-category links run center-left with weight 500 at 14px; account, wishlist, and cart icons anchor the right. Active category items receive a 2px teal underline to ground the current section. On scroll past the hero, the nav collapses to a condensed height of 56px on mobile.

### Product Card

**`product-card`** — White card with a hairline border and {rounded.sm}. Title runs `{typography.title-sm}` in near-black; catalog SKU runs `{typography.product-sku}` in monospace at `{colors.muted}`, visually separating the identifier from the human-readable name. Application validation icons appear as a compact row at 24px with active icons in teal and inactive in `{colors.muted-soft}`. Hover state elevates with a teal-tinted box shadow without lifting off the grid.

### Spec Table

**`spec-table`** — The primary data delivery surface on product detail pages. Header row uses `{colors.surface-soft}` with `{typography.spec-label}` (12px, weight 600, slight letter-spacing) to distinguish column labels from cell content. Rows alternate on hover to `{colors.surface-soft}` for row tracking across wide tables. The key-column (property name) is fixed at 220px to keep label/value pairing stable on narrow viewports.

### Filter Sidebar

**`filter-sidebar`** — Left-rail facet navigator 256px wide. Section labels use `{typography.spec-label}` uppercase treatment. Facet values render as pill chips ({rounded.full}) — inactive chips show on `{colors.surface-soft}` with a hairline border, active selections fill with `{colors.primary}` and white text. Multiple active selections stack in the same row before wrapping, giving researchers a compact audit trail of their filter state.

### Validation Badge

**`validation-badge`** — Small pill rendered in `{colors.surface-teal}` with a teal border and uppercase `{typography.caption-label}` at 11px. Used to flag application-validated claims (WB, IHC, IF, Flow Cytometry) on catalog tiles and within product headers. The teal-on-teal-light combination reads as positive/confirmed rather than alert, appropriate to experimental evidence signals.

### Application Icon Set

**`application-icon-set`** — A horizontal row of 24px icons representing validated applications (Western Blot, Immunoprecipitation, ELISA, etc.). Active icons render in `{colors.primary}`, inactive in `{colors.muted-soft}`. Tooltip overlays on hover display the full application name on a dark `{colors.ink}` background with {rounded.xs} corners. Icon row appears on both product cards and the detail page header.

### Citation Panel

**`citation-panel`** — A soft-background panel ({colors.surface-soft}) displaying peer-citation count as a large `{typography.display-sm}` number in teal, followed by body-sm citation excerpts with teal links. Positioned on product detail pages as social-proof infrastructure, citing published research that used the specific lot or product. The count number in primary teal is the most visually prominent non-CTA element on the page.

### Alert Banner

**`alert-banner`** — Full-width contextual banners for stock status, regulatory notices, and promotional messaging. Info variant uses `{colors.science-teal-light}` background with `{colors.primary-active}` text — the teal-on-teal-light keeps the alert within brand register. Error and warning variants use their respective soft backgrounds while maintaining `{typography.body-sm}` sizing for inline density.

### Hero / Catalog Entry

**`hero-catalog`** — A `{colors.surface-soft}` band with `{typography.display-xl}` headline and embedded search bar. Avoids hero photography at the catalog level, instead relying on clear copy and the prominent search input to drive immediate task completion. Category landing pages may include a teal accent band or product family imagery as a secondary signal.

### Footer

**`footer`** — Near-black ({colors.ink}) background with a 3px teal top border as the sole brand signal at page bottom. Column headings in white `{typography.title-sm}`, links in `{colors.muted-soft}` with hover to canvas white. Contains regulatory, compliance, distributor, and product-family navigation — the heavier information architecture appropriate to institutional and procurement users.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar collapses to a bottom sheet triggered by a teal filter pill; nav bar reduces to logo + hamburger + search icon; spec tables scroll horizontally within their container; hero search bar stacks label above input |
| Tablet | 744–1128px | Two-column product grid; filter sidebar may remain as a slide-in drawer at 300px width; nav shows top-level categories, sub-nav hidden behind hover; citation panels stack below spec content |
| Desktop | 1128–1440px | Three-column product grid; filter sidebar fixed left at 256px; full sticky nav with category links visible; hero shows full headline + search bar side-by-side; spec table key column fixed |
| Wide | > 1440px | Content constrained to 1440px max-width with centered layout; four-column product grid possible; hero receives additional padding; footer columns spread to six-column layout |

### Touch Targets

- All interactive chips and filter pills minimum 44px tall on mobile
- Add to Cart and primary CTA buttons full-width on mobile viewports
- Icon buttons in application icon sets increase to 40px hit area on touch with {spacing.xs} gap minimum
- Spec table row height increases to 48px on mobile for tap comfort

### Collapsing Strategy

- Filter sidebar collapses first: transitions to bottom sheet modal on mobile, drawer on tablet
- Secondary nav items collapse into a hamburger menu; search expands to full-width overlay
- Spec tables gain horizontal scroll containers with a visual overflow fade indicator
- Citation panel stacks below the spec table on single-column layouts
- Breadcrumb truncates middle segments with ellipsis, always preserving first and last nodes

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — all palette values are sourced from brand memory; Abcam's teal primary (#00b5c8) is a well-known brand color but the exact hex may differ from the current design system
- No font families were extracted — typography assumes a modern system sans-serif (Inter/Helvetica Neue); Abcam may use a licensed typeface or proprietary font not identifiable from public extraction
- Exact border-radius values unconfirmed — {rounded.sm} (8px) is an informed estimate based on the brand's professional register
- Spacing scale and component heights are estimated from category norms for scientific B2B e-commerce, not measured from live layout
- Dark mode or alternate theme tokens unknown
- Promotional and sale state colors (discount badges, urgency signals) not captured
- Exact shadow values for elevated components (dropdowns, tooltips, modals) not extracted
- Product image aspect ratios and packaging photography guidelines not confirmed
