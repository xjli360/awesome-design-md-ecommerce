---
version: alpha
name: "Aurora Corp"
source_url: "https://www.auroracorp.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pure red (#ff0000) and unmodified blue (#0000ff) pressed against nine tones of gray — Aurora Corp's interface arrives looking less like a designed brand system and more like a product instruction sheet that has always existed, legible and unambiguous. The company manufactures paper shredders and desktop calculators for the American office market, and the visual grammar reflects that provenance exactly. Franklin Gothic Medium, the condensed grotesque face that ran in newspaper headlines and government printing throughout the twentieth century, handles every type element from section titles to model-number callouts. It was not selected for personality — it was selected because it works at any size, in any gray-on-gray context, without requiring a custom font license. The chromatic palette is organized around industrial neutrals: near-white #f9fbfb for the canvas, layered machine grays #e1e1e1 through #c0c0c0 and #848484 for surfaces and dividers, near-black #2a2a2a as primary ink. These are the colors of ABS plastic housings, metal chassis panels, and photocopied product catalogs. Red (#ff0000) enters only where urgency is warranted — the primary CTA button, alert states, and warning-label elements that parallel the physical safety graphics on shredder feed slots. Blue (#0000ff) persists as the unmodified browser-default hyperlink color, a deliberate institutional holdover that prioritizes zero-confusion navigation over brand cohesion. Button corners sit at `{rounded.xs}` (4px) — enough to soften production artifacts, not enough to signal approachability. Specification tables and data grids run `{rounded.none}` flat borders throughout, reinforcing the sense that this interface was built to display accurate data and move procurement officers to a checkout page. No pill shapes, no gradient fills, no ambient hover animations anywhere in the system.

colors:
  primary: "#ff0000"
  primary-active: "#cc0000"
  primary-disabled: "#ffaaaa"
  accent-blue: "#0000ff"
  ink: "#2a2a2a"
  body: "#5f5f5f"
  muted: "#767676"
  muted-soft: "#848484"
  silver: "#a4a4a4"
  hairline: "#c1c1c1"
  surface-mid: "#c0c0c0"
  hairline-soft: "#d4d4d4"
  surface-soft: "#e1e1e1"
  canvas: "#f9fbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  model-number:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    border: "1px solid {colors.hairline}"
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 10px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    focusBorderColor: "{colors.ink}"
    height: 38px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
    linkActiveColor: "{colors.primary}"
    height: 54px
    padding: "0 {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    modelTypography: "{typography.model-number}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-md}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    borderBottom: "4px solid {colors.primary}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    rowBorderColor: "{colors.hairline-soft}"
    cellPadding: "{spacing.sm} {spacing.base}"
    altRowBackground: "{colors.canvas}"
  model-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.model-number}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  capacity-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  warning-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-sm}"
    height: 40px
    placeholderColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.accent-blue}"
    separatorColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  manual-download:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    hoverBackgroundColor: "{colors.surface-mid}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.accent-blue}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.section}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.surface-soft}"
    inactiveTextColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 32px
    minWidth: 32px

## Components

### Buttons

**`button-primary`** — Flat red (#ff0000) rectangle with 4px corners, uppercase Franklin Gothic Medium at 15px, 40px tall. On hover the background shifts to `{colors.primary-active}` (#cc0000) with no transition delay — the switch is instant, matching the mechanical feedback aesthetic of the product category. Disabled state washes out to `{colors.primary-disabled}` and sets `cursor: not-allowed`; no opacity hack.

**`button-secondary`** — Light gray (#e1e1e1) fill with 1px `{colors.hairline}` border, same uppercase typography as primary. Active state deepens fill to `{colors.surface-mid}` and tightens border to `{colors.muted}`. Used for secondary catalog actions: Compare, Add to Wishlist, Download Spec Sheet.

### Inputs and Search

**`text-input`** — White fill, 1px `{colors.hairline}` border, 4px radius. Focus ring replaces border color with `{colors.ink}` (no blue glow, no box-shadow). Placeholder in `{colors.muted}`. Used for model-number lookup fields and quote-request forms.

**`search-bar`** — Full-width bar combining a text input region with an attached red submit button carrying uppercase "SEARCH" in `{typography.button-sm}`. The two regions share a single 1px outer border at `{colors.hairline}`, dividing only at the button seam. Matches the catalog search pattern common across B2B equipment sites.

### Navigation

**`nav-bar`** — Off-white canvas (#f9fbfb) bar, 54px tall, underlined by a 3px red border that functions as the persistent brand identifier at the top of every page. Nav links in uppercase `{typography.nav-link}`, active link color shifts to `{colors.primary}`. No mega-menu animations; dropdowns appear/disappear immediately.

**`breadcrumb`** — Small `{typography.body-sm}` trail in `{colors.accent-blue}` (the browser-default blue, unmodified), with the current page rendered in `{colors.body}` and muted separators. Sits 8px below the nav-bar on product and category pages.

### Product Display

**`product-card`** — White card with 1px `{colors.hairline}` border and 4px radius. Image region fills with `{colors.surface-soft}` gray as background to neutralize white-product-on-white-background washout. Model number renders in `{typography.model-number}` (spaced caps) above the product title in `{typography.title-md}`. Hover state sharpens border to `{colors.primary}` red — the only place red appears without a button context. Price in `{typography.title-md}` weight, no badge or callout styling.

**`category-tile`** — Gray-fill tile with 1px border, used on the homepage and category landing pages to navigate between Shredders and Calculators product lines. Headline in `{typography.display-sm}`, caption line in `{typography.caption}`, hover border fires to `{colors.primary}`.

### Specification and Documentation

**`spec-table`** — Full-width flat table (`{rounded.none}` on all corners) with header row in `{colors.surface-soft}` and uppercase `{typography.spec-label}` column headers. Body rows alternate between white and `{colors.canvas}` for scan-ability. Used for sheet capacity, security level (DIN P-1 through P-7), run time, throat width, and bin volume.

**`model-badge`** — Ink-black rectangle with zero radius, white `{typography.model-number}` text. Appears in the upper-left corner of product images and at the top of product detail pages. The no-radius choice is intentional: it reads as a stamp or part number label rather than a UI chip.

**`capacity-badge`** — Red pill-adjacent tag in `{typography.caption}`, used to call out sheet capacity (e.g., "12 SHEETS") on product cards and category filters. Sits inline next to the product name.

**`warning-badge`** — Red background, uppercase `{typography.spec-label}`, used for safety-relevant callouts: jam protection, auto-stop, paper detection. Maps directly to the physical warning label vocabulary on the devices.

**`manual-download`** — Gray-fill row with a red document icon, `{typography.body-sm}` filename, and right-aligned download size. Used in the Support and Product Detail sections for PDF manuals, quick-start guides, and compliance documents. Hover fills to `{colors.surface-mid}`.

### Structure

**`hero-banner`** — Near-black (#2a2a2a) field with white `{typography.display-xl}` headline and `{typography.body-md}` subhead. A 4px red bottom border grounds the section before the product grid. Photography, when present, is product-forward (machine on white or gray seamless), not lifestyle.

**`footer`** — Ink-black footer with 3px red top border mirroring the nav-bar's bottom border. Link columns in `{typography.title-sm}` headers and `{typography.body-sm}` body links colored `{colors.accent-blue}`. Contains sitemap columns, legal links, and a manual-search input. No social icon cluster in the primary layout.

**`pagination`** — Row of 32px square buttons, active page in red fill, inactive in `{colors.surface-soft}` with `{colors.hairline}` border. Uppercase `{typography.button-sm}` numerals. Square-ish at 4px radius — consistent with the no-pill constraint.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + logo; hero headline drops to `{typography.display-md}`; spec-table scrolls horizontally; breadcrumb hidden |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories, drops sub-nav to drawer; hero retains two-column text+image split |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdown category menus; spec-table fully visible |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px, outer canvas exposed; hero banner fills full bleed with contained text column |

### Touch Targets

- All buttons minimum 40px height on mobile, matching the defined component height
- `manual-download` rows expand to 48px minimum on mobile for thumb clearance
- `pagination` buttons expand to 44×44px on mobile
- Search submit button minimum 44px wide on touch viewports

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; drawer slides from left with `{colors.ink}` background and white links
- Spec tables scroll horizontally inside a clipped container rather than reflowing to stacked key-value pairs, preserving the column-comparison use case
- `hero-banner` stacks text above product image on mobile rather than splitting side-by-side
- Footer link columns collapse to a single accordion-style column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color is unknown and left unspecified
- Only one font-family stack detected (Franklin Gothic Medium); no confirmed webfont URL or CDN source — the stack may fall through to Arial Narrow or Arial on systems without Franklin Gothic installed
- Blue (#0000ff) is pure browser-default; no evidence of a custom link-color token — treated here as `accent-blue` but may simply be an unset CSS property
- No confirmed hover or focus animation durations; transition timings are estimated as instant (0ms) based on the utilitarian pattern
- Surface-card (#ffffff) not directly extracted — inferred as white from typical page background behind product images; may be #f9fbfb in practice
- No evidence of icon system, illustration style, or brand iconography extracted from the site
- No pricing display format, badge hierarchy for sale/clearance states, or promotional callout patterns confirmed
- No confirmation of whether #0000ff blue is used for anything beyond legacy hyperlinks (e.g. info states, secondary CTAs)
