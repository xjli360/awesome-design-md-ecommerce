---
version: alpha
name: "Thermo Fisher Scientific"
source_url: "https://www.thermofisher.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Six distinct near-white surface values (#fafafa, #f9f9f9, #f8f8f8, #f7f7f7, #f4f4f4, #f3f3f3) tile the page before any brand color appears — the design system's first priority is unambiguous data legibility on a clinical white ground, not visual expression. When color arrives, it arrives with precision: #0071d0 carries every primary action while a deeper #005daa handles hover and pressed states, keeping the blue range narrow and systematic rather than expressive. What surprises is the presence of #262262, a dark indigo-navy that anchors the global utility strip and section headers, adding institutional gravity without warmth — and #802eff, a sharp electronic purple that surfaces in newer digital touchpoints and product-line overlays, signaling a quiet evolution from pure enterprise utility. The red family (#e71316, #d01013, #ee3134) is alert-red rather than brand-red: it appears only in error states, mandatory indicators, and critical-action confirmations, never on catalog browse pages. Typography runs Helvetica Neue throughout — no custom display typeface, no branded wordmark font — at weights 400 and 500 for reading efficiency across long product catalogues and multi-column specification tables. Corners are square to minimal-radius; `{rounded.full}` appears only on the search bar and filter pills, marking discovery as distinct from transactional forms. The `{colors.surface-blue-tint}` (#ebf2fa) creates quiet panel differentiation on feature sections without committing to full primary saturation — a pattern common in scientific platforms where calm visual hierarchy matters more than marketing voltage. Grid density is high by consumer-web standards; {spacing.sm} and {spacing.md} dominate product listings because the primary customer arrives to compare specifications and place a precise order, not to browse for inspiration. Product SKU identifiers render in monospace, the one typographic exception that enforces functional meaning over visual consistency.

colors:
  primary: "#0071d0"
  primary-active: "#005daa"
  primary-hover: "#1e8ae7"
  primary-disabled: "#a2a2a2"
  accent-red: "#e71316"
  accent-red-dark: "#d01013"
  accent-red-alt: "#ee3134"
  accent-navy: "#262262"
  accent-purple: "#802eff"
  ink: "#222222"
  ink-deep: "#1b1b1d"
  body: "#555759"
  muted: "#70707a"
  muted-soft: "#a2a2a2"
  hairline: "#dcdcdc"
  hairline-mid: "#d8d8d8"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f4f4f4"
  surface-mid: "#eeeeee"
  surface-blue-tint: "#ebf2fa"
  surface-error: "#fff5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0
  label:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Neue', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  product-sku:
    fontFamily: "monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px

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
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  button-destructive:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 8px 12px
    height: 40px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 8px 16px
    height: 44px
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    width: 44px
    height: 44px
  nav-bar-top:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
    borderColor: "{colors.hairline}"
  product-sku-tag:
    textColor: "{colors.muted}"
    typography: "{typography.product-sku}"
  product-price:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-badge-promo:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hero-banner:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  hero-banner-blue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  surface-panel:
    backgroundColor: "{colors.surface-blue-tint}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    rounded: "{rounded.sm}"
  promo-strip:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
  category-card-hover:
    backgroundColor: "{colors.surface-blue-tint}"
    borderColor: "{colors.primary}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  table-header:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "2px solid {colors.hairline}"
  table-row-even:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  table-row-odd:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  breadcrumb:
    textColor: "{colors.primary}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  alert-error:
    backgroundColor: "{colors.surface-error}"
    textColor: "{colors.accent-red-dark}"
    borderLeft: "4px solid {colors.accent-red}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.xs}"
  alert-info:
    backgroundColor: "{colors.surface-blue-tint}"
    textColor: "{colors.primary-active}"
    borderLeft: "4px solid {colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-hover}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Solid #0071d0 fill with white text at `{typography.button-md}` (16px, weight 500), `{rounded.xs}` corner (2px), 40px height. Hover shifts to `{colors.primary-active}` (#005daa) without animation flourish, reinforcing precision over playfulness. Disabled uses `{colors.primary-disabled}` (#a2a2a2), preserving form while removing affordance.

**`button-secondary`** — White background, `{colors.primary}` text, 1px primary-color border. Hover shifts background to `{colors.surface-soft}` (#f7f7f7) and border to `{colors.primary-active}`. Used alongside `button-primary` in add-to-cart / request-quote side-by-side decisions, the most common dual-CTA pattern in the catalog.

**`button-ghost`** — Text-only in `{colors.primary}`, transparent background, no border. Appears heavily in data-dense contexts: specification comparison tables, filter resets, pagination links. Never used as a primary page action.

**`button-destructive`** — `{colors.accent-red}` (#e71316) background, reserved strictly for irreversible confirmation dialogs (delete saved list, cancel order). Never placed on catalog browse pages; its red matches the alert system, not the brand identity.

### Search

**`search-bar`** / **`search-submit`** — The search bar is one of only two `{rounded.full}` (pill-shaped) elements in the system, the other being filter pills. The contrast against otherwise-square form controls signals this as the primary discovery entry point. The solid blue `search-submit` orb (44×44px) sits flush at the right end of the pill, matching `{colors.primary}` exactly. Border shifts from `{colors.hairline}` to `{colors.primary}` on focus with no delay.

### Navigation

**`nav-bar-top`** — A 36px utility strip in `{colors.accent-navy}` (#262262) carrying locale selectors, account links, and institutional pricing notices at `{typography.caption}` size. The deep indigo creates an unmistakable separation between the corporate utility layer and the product-browsing layer below; it is the strongest brand-authority signal on the page.

**`nav-bar`** — White main header at 60px with a 1px bottom hairline. Navigation links at `{typography.nav-link}` (14px, weight 500). Mega-menu dropdowns (`nav-dropdown`) use white fills, `{rounded.xs}` corners, and a soft 16px-spread box-shadow — no rounded mega-menus, consistent with enterprise catalog convention where information density outranks visual softness.

### Product Cards

**`product-card`** — Low-relief cards with 1px `{colors.hairline-soft}` border, `{rounded.sm}` corners (4px), and a near-invisible 4px box-shadow. On hover, shadow deepens to 12px spread and border strengthens to `{colors.hairline}`. Product SKU renders in `{typography.product-sku}` (monospace, 12px), immediately distinguishing catalog identifiers from prose. Price renders in `{typography.price}` (20px bold) without currency decoration beyond the symbol.

**`product-badge-new`** / **`product-badge-promo`** — Compact inline labels using `{rounded.xs}` and tight 2px 6px padding. New products take `{colors.primary}` blue; promotional items take `{colors.accent-red}`. Both use `{typography.label}` at 12px weight 500 — no uppercase treatment, consistent with the system's rejection of decorative type conventions.

### Data Tables

**`table-header`** — `{colors.surface-mid}` (#eeeeee) fill with a 2px bottom border at `{colors.hairline}`. **`table-row-even`** alternates to `{colors.surface-soft}` (#f7f7f7); odd rows stay on canvas white. Product specification comparison tables use this alternating pattern across up to twelve columns — legibility over visual interest.

### Content Panels

**`hero-banner`** — Full-width flat-color panels in either `{colors.accent-navy}` (#262262) or `{colors.primary}` (#0071d0). Display type at `{typography.display-xl}` (36px bold) in white, body at `{typography.body-md}`. No gradient, no overlay photography treatment — flat color only, consistent with a brand that treats photography as supplemental rather than atmospheric.

**`surface-panel`** — `{colors.surface-blue-tint}` (#ebf2fa) background with `{rounded.sm}` corners. Used for feature callouts, promotional highlights, and secondary content zones alongside the main white canvas. Adds visual separation without introducing the full primary blue at 100% saturation.

### Alerts

**`alert-error`** — Left-bordered panel in `{colors.accent-red}` with a `{colors.surface-error}` near-white tinted background. **`alert-info`** mirrors the structure using `{colors.surface-blue-tint}` and a `{colors.primary}` left border. Both employ `{typography.body-sm}` and `{rounded.xs}` — functional and compact, never decorative.

### Filter Pills

**`filter-pill`** / **`filter-pill-active`** — The second `{rounded.full}` element class in the system, contrasting with square form inputs to signal filterability vs. data entry. Inactive state: `{colors.surface-soft}` fill, `{colors.hairline}` border. Active: solid `{colors.primary}` fill with white text. No intermediate hover color — state is binary by design.

### Footer

**`footer`** — Full-width `{colors.ink-deep}` (#1b1b1d) ground with white text and `{colors.primary-hover}` (#1e8ae7) links. Dense five-column link grid covering product category hierarchies, regulatory notices, institutional resources, and regional site selectors — the structural complexity of the footer mirrors the breadth of the catalogue above it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer replaces mega-menu; search bar full-width; hero text drops to `display-sm`; utility strip collapses to icon row or hides; filter panel becomes bottom-sheet modal |
| Tablet | 744–1128px | Two-column product grid; condensed horizontal nav with overflow scroll; search bar at 60% width; surface panels stack vertically; side-rail filters collapse to top-of-results filter bar |
| Desktop | 1128–1440px | Three-to-four column product grid; full mega-menu with two-row nav (utility strip + main nav); hero banners at full height; left-rail filter panel visible |
| Wide | > 1440px | Content capped at ~1400px centered; four-to-five column grid on category pages; full-width product comparison tables with all specification columns visible |

### Touch Targets

- All buttons 40px minimum height (matches desktop; no upscaling required)
- Search submit orb minimum 44×44px tap area
- Nav drawer items minimum 44px vertical hit area
- Product card full-card tap area, not title link only
- Filter pills minimum 36px height on mobile
- Table row tap area extends full row width for row-level actions

### Collapsing Strategy

- Mega-menu collapses to slide-in drawer with accordion category sections on mobile
- Utility strip (`nav-bar-top`) reduces to icon-only row at narrowest breakpoint, disappears below 480px
- Product specification tables collapse to horizontal scroll, not vertical stacking — column alignment must be preserved for comparison legibility
- Breadcrumb truncates middle segments with ellipsis, preserving root and current page nodes
- Footer link grid: five-column on desktop, two-column accordion on mobile
- Left-rail filter panel: visible sidebar on desktop, bottom-sheet modal with overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display or wordmark font confirmed — all extracted stacks are system fonts (Helvetica Neue, Arial, Roboto); a web-licensed font may load asynchronously post-JS or from a CDN not captured in static extraction
- White (#ffffff) assumed as primary canvas; only near-white variants (#fafafa–#f3f3f3) were captured; confirmed by inference from card and form backgrounds
- Exact button corner radius not confirmed from extraction — 2px (xs) assigned based on enterprise-conservative convention observed in scientific platform category; may be 0px (fully square)
- Icon font confirmed as `icomoon` in extraction but individual glyph set, sizing, grid, and color-per-context mapping are undocumented
- #802eff (purple) present in extraction but specific use context unknown — likely scoped to a product sub-brand (Ion Torrent, eBioscience, or a digital campaign overlay); not promoted to a general system color in this spec
- Hover and focus transition timing not extractable from static analysis — 150ms ease assumed throughout
- Mega-menu column widths, product comparison table column widths, and filter rail fixed width require direct design QA to specify
- Dark mode not observed and likely absent given enterprise catalog context and B2B purchasing workflow
