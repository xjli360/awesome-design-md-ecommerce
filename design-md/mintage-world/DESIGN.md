---
version: alpha
name: "Mintage World"
source_url: "https://www.mintageworld.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pressed gold commands the first design decision at Mintage World: #ffc720 — an amber just warm enough to evoke struck metal rather than generic warning yellow — anchors every primary CTA and headline accent across a site that functions simultaneously as e-commerce storefront and educational archive. The platform's scope is unusual for the category: coins, stamps, and paper currency share equal catalog space, pushing the layout toward a reference-database aesthetic rather than a collectibles shop. A warm parchment surface (#e6dbb9) appears in editorial content bands, recalling the archival paper of numismatic reference books, while charcoal ink (#373b3e) grounds body copy and Bootstrap's semantic greens (#198754, #146c43) and cyans (#0dcaf0, #25cff2) handle status and informational states with the clinical precision of museum labeling. Cards surface with gentle {rounded.sm} radii against near-white canvas; category filters and denomination tags use pill shapes ({rounded.full}) that echo the round silhouette of a coin face. No custom display font was detectable — the site relies on inherited system sans-serifs and Font Awesome icon sets, giving the typography a practical, catalog-first character: legibility and information density over brand expressiveness. The search bar runs prominently in the nav, prioritizing discovery; the footer loads dense reference links organized by collection type (country, era, denomination) — information architecture closer to a library catalog than a retail experience. Color-coded alert ribbons (#d1e7dd for collection highlights, #cff4fc for featured issues, #fff3cd for rare items, #f8d7da for limited editions) provide at-a-glance editorial curation without requiring custom component work, leaning on Bootstrap's semantic palette as shorthand for curatorial hierarchy.

colors:
  primary: "#ffc720"
  primary-active: "#d4a800"
  primary-disabled: "#ffe088"
  accent-blue: "#0d6efd"
  accent-blue-active: "#0a58ca"
  accent-blue-light: "#6ea8fe"
  accent-blue-focus: "#86b7fe"
  accent-green: "#198754"
  accent-green-dark: "#146c43"
  accent-green-muted: "#75b798"
  accent-cyan: "#0dcaf0"
  accent-cyan-bright: "#25cff2"
  accent-pink: "#d63384"
  accent-red-muted: "#ea868f"
  ink: "#373b3e"
  body: "#565e64"
  muted: "#cbccce"
  hairline: "#dfe0e1"
  hairline-soft: "#e2e3e5"
  canvas: "#ffffff"
  surface-parchment: "#e6dbb9"
  surface-soft: "#e2e3e5"
  surface-card: "#ffffff"
  on-primary: "#373b3e"
  on-dark: "#ffffff"
  alert-info-bg: "#cff4fc"
  alert-success-bg: "#d1e7dd"
  alert-warning-bg: "#fff3cd"
  alert-danger-bg: "#f8d7da"
  alert-primary-bg: "#cfe2ff"
  badge-red: "#b02a37"
  badge-blue-soft: "#bacbe6"
  focus-ring: "#86b7fe"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-xs:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  footer-heading:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue}"
    border: "1px solid {colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 44px
  button-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 44px
  button-blue-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.accent-blue}"
    boxShadowFocus: "0 0 0 4px {colors.focus-ring}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    logoAccent: "{colors.primary}"
    height: 64px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.accent-blue}"
    boxShadowFocus: "0 0 0 4px {colors.focus-ring}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    submitButtonBg: "{colors.accent-blue}"
    submitButtonColor: "{colors.on-dark}"
    padding: 8px 12px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspect: "1 / 1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
    boxShadowHover: "0 4px 12px rgba(0,0,0,0.10)"
  collection-card:
    backgroundColor: "{colors.surface-parchment}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 400px
    padding: "{spacing.section}"
  denomination-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  period-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue}"
    border: "1px solid {colors.accent-blue}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-filter-pill-active:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.accent-blue}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  country-tag:
    backgroundColor: "{colors.alert-primary-bg}"
    textColor: "{colors.accent-blue-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 3px 8px
  alert-ribbon-info:
    backgroundColor: "{colors.alert-info-bg}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.accent-cyan}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    typography: "{typography.body-sm}"
  alert-ribbon-success:
    backgroundColor: "{colors.alert-success-bg}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.accent-green}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    typography: "{typography.body-sm}"
  alert-ribbon-warning:
    backgroundColor: "{colors.alert-warning-bg}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    typography: "{typography.body-sm}"
  alert-ribbon-danger:
    backgroundColor: "{colors.alert-danger-bg}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.badge-red}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.footer-heading}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — The brand's gold (#ffc720) CTA button carries dark charcoal text (#373b3e) for legibility against the warm amber field, sitting at 44px height with {rounded.sm} corners. On hover/press it deepens to `primary-active` (#d4a800), reinforcing the coin-metal metaphor; on disabled state it fades to #ffe088 with muted text. This button is reserved for top-tier actions: "Add to Cart", "Buy Now", and primary catalog navigation prompts.

**`button-blue`** — Bootstrap's #0d6efd fills the secondary CTA role for discovery-oriented actions — "Browse Collection", "View All", "Explore Museum". The 44px height and {rounded.sm} rounding mirror `button-primary` exactly; active state shifts to #0a58ca. On gold or parchment backgrounds, the blue provides unambiguous differentiation from brand-gold interactions.

**`button-secondary`** — Ghost variant with white background, 1px #0d6efd border, and blue text. Used for lower-priority actions like "Save", "Compare", "Share Item". Maintains identical dimensions to `button-blue` via padding compensation on the 1px border.

### Navigation
**`nav-bar`** — White canvas bar at 64px height with a bottom hairline border (#dfe0e1). The logo carries a gold accent; Font Awesome icons handle cart, wishlist, and account affordances in the right cluster. The `search-bar` sits centrally or right-aligned for catalog-first discovery. Navigation labels use `nav-link` at 14px/500 — compact enough for a wide link set spanning coins, stamps, notes, and educational sections.

**`search-bar`** — Full-width on mobile, constrained to a central column on desktop. The input uses `text-input` styling with a blue focus ring ({colors.focus-ring}); the submit button cap is Bootstrap blue with a white magnifying-glass icon from Font Awesome, forming a clear affordance pair. {rounded.xs} corners match the utilitarian catalog aesthetic throughout.

### Product Cards
**`product-card`** — White card with 1px hairline border, {rounded.sm} rounding, and a box-shadow on hover that lifts the item from the grid. The image zone occupies a square 1:1 aspect ratio; below sit the item name in `title-sm`, origin country/era metadata in `caption` with a `country-tag` and `period-tag`, and price in `title-md`. A `denomination-badge` overlays the bottom-left of the image for face-value or grade labeling.

**`collection-card`** — Warm parchment (#e6dbb9) background distinguishes editorial collection features — "Ancient Rome Coins", "First Republic Indian Stamps" — from product listings. The warmer ground signals curation rather than commerce. Title at `title-md`, body at `body-sm`, generous {spacing.lg} padding, and {rounded.sm} corners matching the grid.

### Badges & Tags
**`denomination-badge`** — Compact gold (#ffc720) rectangular badge with dark uppercase text at 11px, applied directly over product images to label face value, catalog grade, or series number. {rounded.xs} keeps it sharp and precise against the coin imagery.

**`period-tag`** — A soft-gray pill ({rounded.full}) for era labeling: "Medieval", "Colonial", "British India", "Modern". Light surface with body-gray text ({colors.body}) keeps visual weight low so coin photography stays dominant. Only becomes interactive in filter contexts; decorative instances within product descriptions remain purely typographic.

**`category-filter-pill`** — Blue-outlined {rounded.full} pill for browsable category filters (Coins, Stamps, Notes, Medals, Bullion). The round shape deliberately echoes the coin silhouette. Active state fills solid with #0d6efd and inverts text to white — a clear on/off toggle with no intermediate state.

**`country-tag`** — Light blue (#cfe2ff) pill with darker blue text (#0a58ca) for country-of-origin labeling across catalog items. The Bootstrap primary-subtle palette marks it as informational rather than interactive, distinguishing it visually from actionable `category-filter-pill` elements.

### Alert Ribbons
**`alert-ribbon-info / success / warning / danger`** — Four semantic ribbon variants map to Bootstrap's contextual system, each differentiated by a 4px left-border accent and background tint. Info (cyan) surfaces featured collection callouts; success (green) marks verified grades or completed transactions; warning (gold, using `colors.primary`) signals limited availability or rare items; danger (red) flags out-of-stock or discontinued issues. All share {rounded.xs} corners and `body-sm` typography for uniform density.

### Hero
**`hero-banner`** — Deep charcoal (#373b3e) full-width banner with white headline text and a gold (#ffc720) accent on display headings or key statistics. Minimum 400px tall with section-scale vertical padding. The `button-primary` gold CTA stands out against the dark field; a subheadline at `body-md` weight frames the collection promise. Photography of featured coins or stamps can bleed behind a constrained text column on wide viewports.

### Footer
**`footer`** — Deep charcoal background with a 3px gold top border as a brand-closure signal. Organized in a reference-style multi-column grid across collection dimensions: Coins by Country, Stamps by Era, Notes by Denomination, About & Education. Link hover transitions to gold (#ffc720). Column headings use `footer-heading` (13px/700/uppercase/tracked) for catalog clarity; links use `body-sm`. Dense link sets mirror library reference indexes rather than standard retail footer grids.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen drawer; search collapses to tap-to-expand icon; hero min-height reduces to 280px; filter pills scroll horizontally in a single row below search |
| Tablet | 744–1128px | Two-column product grid; nav items inline with icon affordances; search visible in nav; hero at 360px min-height; sidebar filter renders as a top horizontal strip |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with mega-dropdowns for category/country/era filtering; hero at 400px; filter sidebar panel visible left of catalog grid |
| Wide | > 1440px | Content constrained to ~1320px max-width centered; four-column grid standard; hero allows full-bleed photography behind a contained two-column text/CTA layout |

### Touch Targets
- All buttons and filter pills: minimum 44×44px
- Nav icon buttons (cart, wishlist, account): 44px square touch zone even when visual icon is smaller
- Period tags and country tags: minimum 36px height when used as interactive filters; decorative inline instances may be smaller
- Search submit button: minimum 44px tall to pair symmetrically with the input field height
- Product card image zone: full-width tap target links to product detail; no nested tap regions inside image area

### Collapsing Strategy
- Nav mega-dropdowns collapse to accordion panels inside a hamburger drawer on mobile; top-level category links remain visible as bold section headers
- Desktop filter sidebar collapses to a horizontally scrolling {rounded.full} pill strip pinned below the search bar on mobile/tablet
- Footer multi-column reference grid collapses to single-column accordions on mobile; headings act as disclosure toggles
- Product card metadata (country-tag, period-tag, caption) de-prioritizes on very small viewports — item name and price remain always visible above the fold
- Hero sub-headline copy truncates or hides below 480px to keep the gold CTA button above the fold without excessive scroll distance

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected — all extracted font-family stacks are Font Awesome icon fonts and `inherit`; the site almost certainly uses Bootstrap 5's default system sans-serif stack. Any custom typeface would be loaded via Google Fonts or JS-injected at runtime, not visible in static extraction.
- No `meta theme-color` set — the brand color used for OS-level chrome (mobile browser bar, PWA manifest) is unspecified.
- Not on Shopify — platform and checkout stack unknown; no Polaris or platform-specific component tokens apply.
- The extracted palette is overwhelmingly Bootstrap 5 semantic tokens. Only #ffc720 (gold) and #e6dbb9 (parchment) appear non-standard enough to treat as brand-owned; all other hex values are Bootstrap utility defaults and may not represent intentional brand choices.
- Exact interactive color for the primary CTA is ambiguous: the site's Bootstrap setup may use #0d6efd as the actual button default with #ffc720 as a secondary accent rather than the primary — the gold-as-primary assignment is a design interpretation based on brand fitness, not confirmed extraction.
- Dark-mode tokens not observed or confirmed.
- Product image treatment for numismatic photography (obverse/reverse flip, high-res zoom, lightbox) could not be confirmed from static extraction; coin detail views likely require specialized image interaction patterns.
- Pricing display format (currency symbol placement, multi-currency handling for international coin sales) unconfirmed.
- No hover/transition timing values detectable from static extraction.
