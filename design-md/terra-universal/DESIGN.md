---
version: alpha
name: "Terra Universal"
source_url: "https://www.terrauniversal.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Contamination begins with a fingerprint; every surface in a Terra Universal modular cleanroom is engineered to reject it. That same logic — nothing accumulates without purpose — shapes the site's design posture: a stark #313131 charcoal anchors navigation and body text with the authority of printed technical documentation, while a generous white canvas enforces the visual hygiene the brand sells in physical form. Terra Universal manufactures for semiconductor fabs, biotech suites, and pharmaceutical environments where ISO classifications govern every material choice, so the UI must perform as a specification tool first and a marketing surface second: product tables run dense with filtration ratings, pressure differentials, and fan filter unit configurations; CTA buttons are functional declarations, not emotional prompts.

  Typography relies on the system UI stack — no proprietary typeface was recovered from extraction — which reads as deliberate restraint for a brand selling precision-engineered infrastructure: Arial and Helvetica Neue at controlled weights carry a laboratory-report cadence that a display font would undercut. Component structure skews toward data-dense layouts: category grids with dimensional callouts, downloadable CAD drawing links, request-a-quote forms, and compliance certificate callouts. The navigation architecture reflects a catalog mentality — cleanrooms, environmental monitoring, flooring, furniture, and HVAC components organized by functional category rather than brand narrative.

  Corner radii are minimal throughout; near-square or lightly-softened corners carry the engineering-precision association that generously rounded consumer edges would contradict. Badge treatments for ISO classification, UL listings, and compliance certifications function as purchase-authority primitives — they carry more decision weight on this site than any headline copy. Quote-request pathways are the primary conversion mechanic; product cards are optimized for comparison shopping across compatible modular components rather than single-item impulse decisions. Spacing is generous in section breaks to let dense specification copy breathe, while component padding keeps information architecture scannable for procurement engineers and facilities managers who are buying on specification, not aspiration.

colors:
  primary: "#1d5fa8"
  primary-active: "#154a87"
  primary-disabled: "#8cb3d4"
  ink: "#313131"
  body: "#444444"
  muted: "#717171"
  muted-soft: "#9b9b9b"
  hairline: "#d1d5db"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f6f8"
  surface-card: "#ffffff"
  surface-table-alt: "#f8f9fa"
  table-header-bg: "#eef1f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  safety-orange: "#e05c00"
  compliance-teal: "#0d7a60"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  data-label:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  tab-label:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  badge-label:
    fontFamily: "Arial, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    padding: 12px 22px
    height: 42px
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
    padding: 11px 21px
    height: 42px
  button-quote-request:
    backgroundColor: "{colors.safety-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 28px
    height: 46px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 10px 14px
    height: 40px
    focus-borderColor: "{colors.primary}"
    placeholder-color: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logo-height: 36px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    title-typography: "{typography.title-md}"
    padding: "{spacing.lg}"
    borderTop: "2px solid {colors.primary}"
    boxShadow: "0 6px 20px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    title-typography: "{typography.title-md}"
    caption-typography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    hover-boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    hover-borderColor: "{colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.table-header-bg}"
    altRowBackgroundColor: "{colors.surface-table-alt}"
    textColor: "{colors.body}"
    label-typography: "{typography.data-label}"
    value-typography: "{typography.spec-value}"
    borderColor: "{colors.hairline}"
    cellPadding: "10px 14px"
    rounded: "{rounded.none}"
  compliance-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    iconSize: 16px
  iso-tag:
    backgroundColor: "{colors.compliance-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    padding: "0 44px 0 14px"
    icon-color: "{colors.muted}"
    focus-borderColor: "{colors.primary}"
  category-grid-item:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    title-typography: "{typography.title-md}"
    imageAspectRatio: "1/1"
    hover-borderColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    display-typography: "{typography.display-xl}"
    subtitle-typography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.55
  quote-form:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    title-typography: "{typography.title-lg}"
    input-typography: "{typography.body-md}"
    label-typography: "{typography.data-label}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderRight: "1px solid {colors.hairline}"
    title-typography: "{typography.title-md}"
    option-typography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    width: 240px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    headingColor: "{colors.on-dark}"
    heading-typography: "{typography.title-md}"
    link-typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0 {spacing.xl}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — Steel-blue fill (`{colors.primary}`) with white label in `{typography.button-md}`, 42px tall with 22px horizontal padding and `{rounded.xs}` 2px corners that read as functional declarations rather than consumer-friendly rounded pills. Active state deepens to `{colors.primary-active}`; disabled washes to `{colors.primary-disabled}`. These appear on product listing pages and category headers where the action is navigational rather than transactional.

**`button-quote-request`** — The site's highest-priority conversion action uses `{colors.safety-orange}` fill at 46px height with 28px horizontal padding, distinguishing quote requests from all other interactive elements on the page. Safety orange has a dual logic here: industrial visual language and hard contrast against the white canvas. It sits alongside spec tables and drawing downloads on product detail pages.

**`button-secondary`** — White canvas with `{colors.primary}` text and a 1px `{colors.primary}` border. Identical height and padding to `button-primary`, used for secondary actions such as "Download Spec Sheet" or "View Accessories" where a quote-request CTA already occupies the primary slot.

### Navigation
**`nav-bar`** — 64px white bar with `{typography.nav-link}` weight-600 labels and a 1px `{colors.hairline}` bottom border providing separation without shadow theatrics. Logo sits at 36px height on the left. Top-level items map to product categories (Cleanrooms, Fan Filter Units, Flooring, Furniture, Environmental Monitoring, HVAC), not brand-story pillars.

**`mega-menu`** — Opens on hover with a `{colors.canvas}` full-width panel carrying a 2px `{colors.primary}` top accent line and `{spacing.lg}` internal padding. Sub-category links use `{typography.body-sm}` with section headers in `{typography.title-md}`. The 12%-opacity box shadow depth-separates the panel from page content without occluding it. Structure mirrors a printed catalog's table of contents.

### Product Cards
**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.xs}` corners presenting a 4:3 product image, `{typography.title-md}` title, and a `{typography.body-sm}` specification snippet. Hover transitions border to `{colors.primary}` and lifts box shadow to 16px spread. No price is displayed by default — B2B pricing flows through the quote-request mechanism, not a public price table.

### Specification Table
**`spec-table`** — Dense two-column layout for technical parameters: row labels in `{typography.data-label}` (11px, 0.8px letter-spacing, uppercase), values in `{typography.spec-value}`. Alternating rows use `{colors.surface-table-alt}`; column headers sit on `{colors.table-header-bg}`. `{rounded.none}` — corners are hard. This is the highest-density, highest-authority component on the page; procurement engineers and facilities managers read it before they read any headline copy.

### Compliance Badges
**`compliance-badge`** — A neutral `{colors.surface-soft}` chip for third-party certifications (UL, CE, RoHS, NFPA), using `{typography.badge-label}` with a 16px inline icon. Sits adjacent to product title areas and communicates regulatory standing to specifiers who may have contractual compliance requirements to satisfy before purchase.

**`iso-tag`** — `{colors.compliance-teal}` fill badge for ISO cleanroom classification (ISO 3–ISO 8). The distinct teal separates ISO classification from other compliance markers, letting specifiers scan the page and immediately locate the particle-count rating — the single most common purchase qualifier in cleanroom procurement.

### Search
**`search-bar`** — 40px height, 1px `{colors.hairline}` border, `{rounded.xs}` corners. Placeholder in `{colors.muted}`; focus promotes border to `{colors.primary}`. A magnifier icon right-padded inside the field. Part-number and model-number queries are primary use cases alongside keyword browsing, so the input must support exact-string matches without auto-correction interference.

### Hero Banner
**`hero-banner`** — Full-width image overlay with a 55% opacity `{colors.scrim}` panel over a product or facility photograph. White headline in `{typography.display-xl}` with `{typography.body-md}` subtitle. Vertical padding at `{spacing.section}`, horizontal at `{spacing.xl}`. Used on category landing pages and the homepage feature row; never promotional lifestyle imagery — always cleanroom environments or product installations.

### Quote Form
**`quote-form`** — `{colors.surface-soft}` panel with `{rounded.sm}` corners, `{spacing.xl}` padding, and a `{typography.title-lg}` heading. Field labels render in `{typography.data-label}` (uppercase, tight tracking); input values in `{typography.body-md}`. Appears as a right-column side panel on product detail pages and as a standalone full-page form. This is the primary lead-capture mechanism; visual weight and padding are sized to communicate that completing it is the expected next action.

### Category Grid
**`category-grid-item`** — Cells with `{colors.surface-soft}` fill, 1px `{colors.hairline}` border, `{rounded.sm}` corners, and a 1:1 product-family icon or photo. `{typography.title-md}` label below the image. Hover shifts border to `{colors.primary}`. Used on the homepage and top-level category pages as the primary wayfinding structure. Five to six across on desktop.

### Filter Sidebar
**`filter-sidebar`** — 240px fixed-left panel on `{colors.canvas}` with a 1px `{colors.hairline}` right border. Section headings in `{typography.title-md}`; checkbox labels in `{typography.body-sm}`. Active filter selections highlight in `{colors.primary}`. Filter dimensions map to technical parameters: ISO class, CFM range, material (stainless, polypropylene, PVC), pressure rating. This is a specification-matching tool, not taste-based filtering.

### Footer
**`footer`** — Dark `{colors.ink}` footer with a 3px `{colors.primary}` top accent line. Column headings in `{typography.title-md}` white; links in `{typography.body-sm}` `{colors.muted-soft}`. Standard sections: Products, Resources (datasheets, CAD files, installation guides), Company, Contact. `{spacing.xxl}` top padding provides visual mass appropriate to an industrial B2B context where the footer is a functional resource directory.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; mega-menu collapses to full-screen drawer with accordion category sections; spec tables scroll horizontally with sticky first column; hero reduces to 40vw height; quote form goes full-width stacked; product card grid becomes 1-up; filter sidebar converts to top-mounted horizontal scrollable filter chips |
| Tablet | 744–1128px | 2-column product grid; nav condenses to logo + hamburger + search icon; mega-menu becomes full-height side drawer; spec table retains full layout; category grid is 3 across; filter sidebar remains accessible via slide-in panel triggered by a "Filter" button |
| Desktop | 1128–1440px | Full mega-menu nav active; 3–4 column product grid; filter sidebar fixed at 240px left; spec table and quote form sit side-by-side on product detail pages; hero banner at full height with text zone left-anchored |
| Wide | > 1440px | Max-width container at 1400px centered with increased section padding; hero image zone expands without text zone scaling; product grids cap at 4 columns to preserve card legibility |

### Touch Targets
- All primary buttons minimum 44px tall; `button-quote-request` extended to 46px for conversion emphasis
- Nav drawer items 48px tap target height on mobile
- Filter checkboxes 24×24px minimum touch area with 16px visual checkbox inside
- Product card links cover the full card surface via stretched pseudo-element overlay
- Breadcrumb items minimum 36px tap height with horizontal padding expanded on mobile

### Collapsing Strategy
- Navigation: horizontal mega-menu → hamburger drawer at < 1128px; drawer uses full-height overlay with 320px slide-in panel and accordion sub-navigation
- Filter sidebar: 240px fixed left panel on desktop collapses to horizontal scrollable filter chip row pinned below the nav on tablet/mobile
- Spec tables: horizontal scroll container with 100px sticky first column on mobile to preserve row-label context while values scroll
- Category grid: 5-col → 3-col → 2-col → 1-col across breakpoints
- Hero banner: background-image maintains center crop at all widths; headline type scale reduces approximately 20% at mobile via fluid clamp
- Quote form: two-column field layout on desktop collapses to single-column stacked on mobile with full-width submit button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary color unconfirmed**: The site returned a Cloudflare anti-bot challenge ("Just a moment...") blocking all live palette extraction. Only `#313131` was captured — likely from a loading-state stylesheet, not the rendered brand palette. All other colors (primary blue `#1d5fa8`, `{colors.safety-orange}`, `{colors.compliance-teal}`) are inferred from industrial B2B and cleanroom industry convention, not extracted values. The entire palette should be validated against the live site once accessible.
- **No custom typeface detected**: The font stack is entirely system defaults (Arial, Helvetica Neue, system-ui). It is unknown whether Terra Universal loads a licensed typeface via JavaScript-injected CSS or a late-loading web font after initial render. If a custom typeface is identified, all `fontFamily` values require updating.
- **Navigation structure**: Mega-menu category labels and depth were inferred from domain knowledge of cleanroom equipment taxonomy, not live DOM inspection. Actual nav architecture, link labels, and icon treatments may differ materially.
- **Commerce model**: Whether the site supports any e-commerce checkout flow or operates exclusively on quote-request could not be confirmed. Component design assumes quote-first B2B model.
- **Dark mode**: No dark-mode tokens or `prefers-color-scheme` behavior could be observed.
- **Accent and semantic colors**: Warning orange, compliance teal, and the primary blue are conventional choices for industrial/compliance UI — they have not been verified against brand guidelines or extracted from the live site.
- **Component states**: Hover, focus, error, and loading states for form inputs and interactive elements were inferred from standard accessibility patterns, not live observation.
- **Logo mark**: Exact dimensions, clearspace requirements, and treatment on dark backgrounds are unknown.
