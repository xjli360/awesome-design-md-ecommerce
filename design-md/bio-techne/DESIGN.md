---
version: alpha
name: "Bio-Techne"
source_url: "https://www.bio-techne.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Twelve subsidiary brands — R&D Systems, Novus Biologicals, Tocris, ProteinSimple, Shapes Sciences, and seven others — live as peer catalog entries under a single navigation umbrella rather than behind a brand-switcher; Bio-Techne trusts search and category taxonomy to route researchers who arrive with an antibody catalog number or a gene target in mind, not a parent-company preference. The design language is instrument-panel minimal — a white canvas (`{colors.canvas}`) carrying a corporate mid-blue primary (estimated #005BAC from observed site usage; extraction yielded no tokens, see Known Gaps) on nav fills, primary CTAs, and active tab underlines, never decoratively applied. Typography runs a clean sans-serif stack at restrained weights: body copy at 16px/400 on 1.5 leading, display at 24–32px without the heavy 700-weight maximalism common in consumer DTC — the brand communicates precision over persuasion, mirroring how a technical datasheet reads. Product cards carry dense metadata in a 12px caption tier — catalog number, host species, reactivity species, validated application icons (WB, IHC, IF, ELISA) — alongside a discreet 14px price and an "Add to Cart" button, because the purchase decision criterion is a specificity value, not a lifestyle image. The search experience functions as the true homepage regardless of page context: a prominent, full-width search bar with catalog-number and gene-name autocomplete sits above the fold on every template, acknowledging that scientists arrive with a molecular target rather than browsing intent. Corner radii are nearly absent — inputs and cards use `{rounded.xs}` at most, reinforcing the clinical, scientific-catalog register. A strict 12-column grid and 1px hairlines keep pages scannable at high information density without decorative fills. The B2B posture surfaces in CTA duality: "Add to Cart" and "Request a Quote" appear as sibling buttons on many product pages, and "Download Protocol" / "View Datasheet" links occupy their own CTA tier, reflecting institution-pricing workflows layered on top of a direct-purchase channel.

colors:
  primary: "#005BAC"
  primary-active: "#004A8C"
  primary-disabled: "#99BFE0"
  primary-light: "#E8F1FB"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F7FA"
  surface-card: "#FFFFFF"
  surface-nav: "#003D73"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#2E7D32"
  warning: "#E65100"
  error: "#C62828"
  tag-wb: "#4A90D9"
  tag-ihc: "#7B4FA6"
  tag-elisa: "#2E8B57"
  tag-if: "#D4870A"
  catalog-num: "#005BAC"
  quote-accent: "#F0F4FF"

typography:
  display-xl:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  catalog-num:
    fontFamily: "'Courier New', Courier, 'Lucida Console', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  nav-top-link:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  section-label:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  app-tag:
    fontFamily: "'Source Sans Pro', 'Open Sans', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-quote:
    backgroundColor: "{colors.quote-accent}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    focusBorderColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 48px 10px 16px
    height: 48px
    iconColor: "{colors.primary}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.none}"
      width: 48px
  nav-bar:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 48px
    topBarHeight: 36px
    topBarBackground: "{colors.primary}"
    topBarTypography: "{typography.nav-top-link}"
    dropdownBackground: "{colors.canvas}"
    dropdownTextColor: "{colors.ink}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.primary}"
    catalogNumTypography: "{typography.catalog-num}"
    catalogNumColor: "{colors.catalog-num}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    priceTypography: "{typography.title-sm}"
    priceColor: "{colors.ink}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 2px 8px rgba(0,91,172,0.12)"
  application-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.app-tag}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    activeBackground: "{colors.tag-wb}"
    activeTextColor: "{colors.on-primary}"
  catalog-number-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.catalog-num}"
    typography: "{typography.catalog-num}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  species-reactivity-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
    overlayOpacity: 0.55
    searchBarVariant: "search-bar"
  section-label-heading:
    textColor: "{colors.muted}"
    typography: "{typography.section-label}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.xs}"
    marginBottom: "{spacing.base}"
  data-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.caption}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rowHoverBackground: "{colors.primary-light}"
    rounded: "{rounded.none}"
  protocol-download-link:
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    iconSize: 16px
    hoverTextDecoration: underline
    paddingLeft: "{spacing.lg}"
  brand-subsidiary-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "3px 8px"
  citation-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    fontStyle: italic
  footer:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark}"
    linkColor: "#A8C8F0"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} 0"
    borderTop: "3px solid {colors.primary-active}"

## Components

### Buttons

**`button-primary`** — Solid `{colors.primary}` (#005BAC) fill, white text, 4px radius, 40px height at 10px/20px padding. Used for primary transactional actions: "Add to Cart", "Find Products", main search submission. Active state drops to `{colors.primary-active}` (#004A8C); disabled state uses `{colors.primary-disabled}` (light blue wash) with unchanged white text.

**`button-secondary`** — White background with a 1.5px `{colors.primary}` border and primary-blue text. Used as a sibling CTA to `button-primary` — appears alongside it on product pages for "Request a Quote" or "Compare Products." Same 40px height maintains visual alignment in button rows.

**`button-quote`** — Identical border and text to `button-secondary` but with a `{colors.quote-accent}` (#F0F4FF) fill to visually distinguish the consultative path from the transactional one. Signals "institution/bulk inquiry" without competing with the primary Add to Cart action.

**`button-text-link`** — Transparent background, primary-blue underlined text at body-sm scale. Used for datasheet links, protocol downloads, and "View All Results" navigation — secondary-information pathways that must not compete visually with CTAs.

### Search

**`search-bar`** — Full-width input with a 2px `{colors.primary}` border and an attached 48px-wide blue submit button with no radius on its inner edges (flush join). Autocomplete dropdown surfaces catalog numbers, gene names, protein targets, and brand-subsidiary matches in separate result groups. This component appears persistently in the top nav after the hero on interior pages, collapsing to an icon trigger on mobile below 744px.

### Navigation

**`nav-bar`** — Two-tier structure: a 36px utility bar at `{colors.primary}` (#005BAC) carrying account, cart, institution-login links at `{typography.nav-top-link}` scale; below it a 48px primary nav at `{colors.surface-nav}` (#003D73) carrying product category menus in `{typography.nav-link}`. Mega-dropdown panels open on hover with white (`{colors.canvas}`) backgrounds and full-bleed column layouts organizing brand subsidiaries and sub-category links. No hamburger animation — mobile shifts to a slide-in drawer.

### Product Cards

**`product-card`** — 1px hairline-bordered card on a white surface, 4px radius. Thumbnail image sits in a `{colors.surface-soft}` panel at top. Below: catalog number in monospace `{typography.catalog-num}` on `{colors.primary-light}` badge, product title as a primary-blue link in `{typography.title-sm}`, then a compact metadata row (host species, clonality, reactivity) in `{typography.caption}` gray. Application tags (`application-tag`) render as a wrapping row of small chips — highlighted in color when that application is validated (WB blue, IHC purple, ELISA green, IF amber). Price at `{typography.title-sm}` weight with "Add to Cart" and "Request a Quote" buttons stacked below. Hover state adds a 2px primary-blue border and a soft shadow.

### Data & Scientific Components

**`application-tag`** — Small 10px uppercase chip. Default state: `{colors.surface-soft}` background with `{colors.muted}` text — indicates the application is listed but not the primary validated use. Active state: colored background matching the application type (WB `{colors.tag-wb}`, IHC `{colors.tag-ihc}`, ELISA `{colors.tag-elisa}`, IF `{colors.tag-if}`) with white text, signaling peer-reviewed validation data exists for that application.

**`catalog-number-badge`** — Monospace 13px text on a `{colors.primary-light}` tint background. The catalog number is the primary lookup key for scientific researchers and must be visually distinct from prose text — monospace rendering and background tint accomplish this without requiring a large badge component.

**`data-table`** — Zero-radius table with 1px `{colors.hairline}` grid lines. Header row at `{colors.surface-soft}` fill with `{typography.caption}` muted labels. Cells at `{typography.body-sm}` ink. Row hover triggers a `{colors.primary-light}` wash for scannability across dense specification rows (molecular weight, purity, formulation, storage conditions). Used extensively on product detail pages and cross-reactivity comparison views.

**`citation-block`** — Indented italic block in `{colors.surface-soft}` with hairline border, housing PubMed-style reference strings. Appears below validated datasheet sections to establish peer-reviewed credibility of application data. Typography at `{typography.caption}` scale keeps citations readable but visually subordinate to the product data.

**`protocol-download-link`** — An icon-preceded text link (PDF icon, 16px) in primary blue. Appears in a dedicated "Resources" subsection on product pages alongside SDS sheets, certificates of analysis, and technical FAQs. Not a button — its text-link register distinguishes document downloads from transactional CTAs.

### Brand & Category Navigation

**`brand-subsidiary-badge`** — Small pill identifying which subsidiary brand (R&D Systems, Novus, Tocris, etc.) owns a given product. Appears on search result cards and the product detail header. Neutral `{colors.surface-soft}` fill — deliberately understated so product metadata, not brand attribution, holds visual priority.

**`section-label-heading`** — 11px all-caps label with a 2px primary-blue bottom border and `{spacing.xs}` padding below. Used as a section divider within product detail pages ("Specifications", "Publications", "Related Products") and in mega-dropdown nav columns. The underline is the only typographic decoration in the system.

### Hero & Footer

**`hero`** — Full-width `{colors.primary}` blue panel (or photographic overlay at 55% dark scrim) with white display text and a centered `search-bar` instance. Used on the homepage and major category landing pages. The dominant CTA is search — no lifestyle-copy subheads, just a category descriptor and the search input.

**`footer`** — Dark `{colors.surface-nav}` (#003D73) panel with `{colors.on-dark}` column headings at `{typography.title-sm}` and link lists at `{typography.body-sm}` in a light-blue link color (#A8C8F0) for legibility on dark. A 3px `{colors.primary-active}` top border separates the footer from page content. Subsidiary brand logos appear as a separate logo strip above the link columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar collapses to icon in top nav (tap to expand full-width input overlay); two-tier nav collapses to hamburger drawer; application-tag row wraps to two lines; data-table scrolls horizontally with sticky first column; hero search bar full-width |
| Tablet | 744–1128px | Two-column product card grid; nav mega-dropdowns collapse to accordion drawers in side panel; search bar visible inline in top nav at reduced width; hero text at `{typography.display-md}` |
| Desktop | 1128–1440px | Three-column product grid; full two-tier nav with mega-dropdown hover panels; hero at full `{typography.display-xl}`; data-table full visible without scroll |
| Wide | > 1440px | Max-width container at 1440px centered on `{colors.surface-soft}` side panels; four-column product grid on search results; footer four-column link layout |

### Touch Targets

- All buttons minimum 40px height; "Add to Cart" on mobile expands to full-width 48px target
- Application-tag chips minimum 32px touch height on mobile despite 20px visual height (via vertical padding extension)
- Nav drawer links minimum 44px row height
- Catalog number badges non-interactive — no tap target required
- Protocol download links padded to 40px tap height on mobile

### Collapsing Strategy

- Mega-dropdown nav → accordion inside slide-in drawer at < 744px
- Two-column spec + image layout on product detail → single-column stacked (image top, specs below) at < 744px
- Four-tab application filter bar → horizontally scrolling chip row at < 744px
- Citation blocks collapse to "Show references (N)" toggle on mobile to reduce scroll depth
- Search autocomplete dropdown reduces to 5 results (from 10) on mobile to avoid keyboard overlap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors unextracted**: bio-techne.com returned no CSS custom properties or inline color tokens during extraction (likely JS-loaded design tokens or anti-bot blocking). All color values in this file are estimated from observed site usage and documented brand materials — treat as approximate until verified against live computed styles.
- **Font families unconfirmed**: No `font-family` declarations were captured. Typography stack uses Source Sans Pro / Open Sans as a reasonable scientific-publishing default; actual font may differ (could be a licensed typeface served via Adobe Fonts or Typekit).
- **Subsidiary brand color tokens**: Each of Bio-Techne's twelve subsidiary brands (R&D Systems, Tocris, etc.) likely has its own accent color within the unified system — these were not extractable and are not represented here.
- **Dark-mode support unknown**: Cannot confirm whether the site implements a dark theme; `surface-nav` colors are used as a dark-surface stand-in for footer/nav but a full dark-mode palette is absent.
- **Icon system not documented**: Application validation icons (WB, IHC, IF, ELISA glyphs), download icons, and nav icons appear to be a custom SVG set — specific glyphs and naming conventions not captured.
- **Pricing tier logic**: Institution pricing, bulk discount tiers, and "Request a Quote" eligibility thresholds affect CTA rendering logic but cannot be documented without authenticated session access.
