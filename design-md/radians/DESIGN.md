---
version: alpha
name: "Radians"
source_url: "https://www.radians.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Eurostile Extended does the heavy lifting at Radians — the wide, squared-off geometry of that typeface signals industrial authority before a single word registers, positioning safety equipment the way aerospace manufacturers label cockpit controls: functional, legible at a glance, no excess. The brand's primary color, #c8102e, walks the line between corporate red and OSHA danger-signal red, a deliberate ambiguity that makes product packaging and digital surfaces reinforce each other without redundancy. A secondary blue (#1e8ecd) handles informational UI — product filters, links, interactive indicators — while a safety-yellow-green (#d2de28) marks promotional callouts and compliance badges, echoing the high-visibility colorways of the PPE products themselves. The overall surface treatment is near-white (#fefefe) with light gray fills (#eeeeee, #f3f3f3) and a controlled range of neutral grays (#444444, #5e5e5e, #707070) that create clear hierarchy without resorting to black. Corners are sharp or nearly so — a 4px maximum radius on most interactive elements; the brand never softens into consumer-friendly pill shapes because the audience is a procurement manager or safety director specifying compliant gear for a workforce, not a shopper browsing aesthetics. Product cards foreground compliance certifications — ANSI/ISEA ratings, protection-level classifications — as prominently as price, rendered in small-caps badge weight at the card base. The search experience surfaces by product category first (Eye Protection, Hearing, Gloves, Hi-Vis, Head Protection), then by compliance standard, a navigation hierarchy that mirrors how safety professionals actually spec purchases rather than how general retailers organize assortments. A two-tier navigation — a dark charcoal (#393b44) utility bar above for account and dealer tools, a white category bar below — reinforces that Radians serves both end-users and B2B procurement channels simultaneously.

colors:
  primary: "#c8102e"
  primary-active: "#990c23"
  primary-disabled: "#e88a96"
  safety-yellow: "#d2de28"
  safety-blue: "#1e8ecd"
  safety-blue-light: "#b3d4fc"
  ink: "#222222"
  body: "#444444"
  muted: "#5e5e5e"
  muted-soft: "#707070"
  hairline: "#cbcbcb"
  hairline-soft: "#dedede"
  canvas: "#fefefe"
  surface-soft: "#f3f3f3"
  surface-card: "#eeeeee"
  surface-strong: "#393b44"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.2px
    textTransform: uppercase
  display-sm:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0
  title-sm:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'eurostile-extended', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  compliance-tag:
    fontFamily: "'eurostile-extended', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'eurostile-extended', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'eurostile-extended', 'Trebuchet MS', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.safety-blue}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focusBorderColor: "{colors.safety-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    topBarHeight: 36px
    topBarBackground: "{colors.surface-strong}"
    topBarTextColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    accentColor: "{colors.safety-yellow}"
    minHeight: 480px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "3px solid {colors.primary}"
    itemPadding: "{spacing.base} {spacing.xl}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  compliance-badge:
    backgroundColor: "{colors.safety-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  ansi-rating-chip:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    buttonBackground: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    height: 48px
    placeholderColor: "{colors.muted}"
  product-finder:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    filterLabelTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    borderTop: "4px solid {colors.primary}"
  promo-alert:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  safety-alert:
    backgroundColor: "{colors.safety-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    borderLeft: "4px solid {colors.primary}"
  safety-category-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    borderBottom: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
    iconColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.safety-blue-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A flat #c8102e rectangle at 44px height with `{rounded.xs}` (4px) radius, uppercase eurostile-extended at 14px weight 700 with 0.5px letter-spacing. On hover the fill deepens immediately to `{colors.primary-active}` (#990c23) with no transition delay — the brand does not use soft fades. Disabled state fills `{colors.primary-disabled}` (#e88a96) at identical geometry. This is the canonical "Add to Cart," "Get a Quote," and "Find a Distributor" button throughout the site.

**`button-secondary`** — White (#fefefe) fill with a 2px solid #c8102e border and matching red label. On hover, a 10% red tint fills the interior. Used for secondary CTAs like "View Full Catalog" or "Download SDS Sheet" when paired alongside a primary action.

**`button-ghost`** — Transparent background, #1e8ecd (`{colors.safety-blue}`) text label, no border. Appears in product card footers and filter panels for low-priority actions like "Compare" or "Learn More."

### Navigation

**`nav-bar`** — Two-tier structure: a 36px `{colors.surface-strong}` (#393b44) dark utility bar at page top for account login, dealer locator, and distributors; a 56px white main nav below carrying eurostile-extended category links in uppercase 13px. Active category links receive a 3px bottom border in `{colors.primary}`. The logo sits left in the main tier; the search bar appears center at desktop widths. Mobile collapses both tiers into a single bar with a hamburger icon opening a full-height right drawer.

### Product Card

**`product-card`** — White canvas with 1px `{colors.hairline-soft}` border and `{rounded.xs}`. Image region sits on `{colors.surface-soft}` (#f3f3f3). `compliance-badge` chips stack at image top-left for ANSI ratings (e.g. "ANSI Z87.1+"). Product title in `{typography.title-sm}`, SKU and short spec in `{typography.caption}` `{colors.muted}`. `ansi-rating-chip` clusters (dark charcoal, white text) sit below the title before the price. Price renders in `{typography.price-display}`; "Add to Cart" is a full-width `button-primary` at card base.

### Hero Banner

**`hero-banner`** — Full-bleed panel on `{colors.surface-strong}` (#393b44), white headline in `{typography.display-xl}` uppercase eurostile-extended, subhead in `{typography.display-sm}`. A `{colors.safety-yellow}` (#d2de28) geometric stripe or badge anchors upper-left as accent. Primary CTA is `button-primary`; an outlined white button serves as secondary. Minimum 480px tall on desktop; product imagery bleeds the right half on wide viewports. Hero copy typically calls out a compliance standard or product category rather than a lifestyle statement.

### Category Strip

**`category-strip`** — Horizontally scrollable row of category tiles on `{colors.surface-soft}` pinned below the nav-bar. Each tile carries a category icon and `{typography.title-sm}` uppercase label; active tiles flip to `{colors.primary}` fill with `{colors.on-primary}` text. On desktop the strip triggers a mega-menu dropdown on hover; on mobile it scrolls freely and taps directly into the category PLP.

### Compliance & Safety Badges

**`compliance-badge`** — Flat `{colors.safety-yellow}` (#d2de28) rectangles with `{rounded.none}`, `{typography.compliance-tag}` uppercase in `{colors.ink}`. Applied to product cards and PDP headers to surface ANSI/ISEA standard labels (e.g. "ANSI Z89.1 Type I," "ANSI/ISEA 105-2016").

**`ansi-rating-chip`** — `{colors.surface-strong}` fill, `{colors.on-dark}` text, 0px radius. Clusters below the product title to display protection-level classifications ("Type II," "Class E," "ARC 2," "ANSI Level A6"). Multiple chips can appear in a horizontal flex row.

### Search

**`search-bar`** — 48px full-width input with `{rounded.xs}` throughout and a `{colors.primary}` red submit button flush to the right edge. Placeholder text in `{colors.muted}`. Appears as the dominant hero element above the category strip on the homepage, and as a collapsible icon-to-expanded element in the main nav at tablet widths.

### Product Finder

**`product-finder`** — A guided configurator module on `{colors.surface-soft}` with a 4px top border in `{colors.primary}` and `{rounded.sm}` overall radius. Dropdowns and radio filters carry `{typography.caption}` labels; selections progressively narrow the compliant product set. The primary entry point for procurement buyers who need to spec PPE against a specific ANSI, OSHA, or EN standard before browsing SKUs.

### Alert Banners

**`promo-alert`** — Full-width #c8102e band at page top, `{typography.caption}` centered white text. Used for sitewide sale events, new product launches, and shipping promotions.

**`safety-alert`** — `{colors.safety-yellow}` background with a 4px left border in `{colors.primary}`. Used strictly for compliance notices, product-recall information, or regulatory updates — never for promotional content, preserving its signal value.

### Footer

**`footer`** — `{colors.surface-strong}` (#393b44) field, column headings in `{typography.title-sm}` eurostile-extended uppercase white, body links in `{typography.body-sm}` `{colors.safety-blue-light}` (#b3d4fc). Standard columns: Products, Resources (SDS sheets, catalogs), Where to Buy, About, and a distributor-finder CTA button. Social icons render in muted white at 20px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav drawer; search lives in drawer header; hero stacks text above image; category strip becomes horizontal scroll; compliance badges show only the single most prominent rating on cards (full set on PDP); price and Add to Cart float as a sticky bottom bar on PDP |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + search icon + hamburger; category strip visible but condensed; hero retains side-by-side layout at reduced scale; product finder becomes a top-of-page filter bar |
| Desktop | 1128–1440px | Three-column product grid; full two-tier nav; category strip with hover mega-menu; product finder as left sidebar toggled by filter icon; hero image bleeds right half |
| Wide | > 1440px | Four-column product grid; hero image fills up to 50% viewport width; max-width container 1440px centered; footer expands to six columns |

### Touch Targets

- All buttons minimum 44px height and 44px tap width
- Category strip tiles minimum 48px height with `{spacing.base}` horizontal padding
- Filter checkboxes and radio inputs minimum 44×44px hit area
- Nav hamburger icon 44×44px touch target
- Product card entire surface tappable on mobile (not just CTA button)
- Compliance badge chips are display-only on mobile; no interactive tap target required

### Collapsing Strategy

- Top utility bar (account, dealer locator, distributor links) collapses into hamburger drawer on mobile
- Mega-menu category navigation converts to accordion within mobile drawer
- Product finder sidebar becomes a bottom-sheet modal on mobile (<744px), triggered by a "Filter" sticky button
- ANSI rating chip clusters truncate to the highest-priority single chip on mobile cards; full cluster visible on PDP and at tablet+
- Two-tier nav collapses to a single-height bar; utility bar content moves into drawer top section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `eurostile-extended` is served via Adobe Fonts (Typekit); a kit ID is required for web rendering — fallback stack (Trebuchet MS, Arial, Helvetica Neue) is specified but visual fidelity will differ significantly without the licensed font
- `primary-disabled` (#e88a96) is a derived mid-tint of #c8102e, not present in the extracted palette; actual disabled treatment may differ
- No motion or transition timing values were extractable from the static snapshot; animation durations default to ~150ms ease-in-out throughout
- Hover-state shadow depth and lift transform on product cards were not confirmed from extraction; values are inferred from industrial e-commerce conventions
- Exact nav-bar height values (56px main + 36px utility) are estimated from visual inspection, not confirmed via CSS extraction
- Mega-menu column count, image presence, and featured-product slots within the desktop nav were not captured in this extraction pass
- Actual CSS breakpoint declarations were not captured; mobile/tablet/desktop boundaries above are inferred from common Radians layout behavior
- No confirmed spacing values for the product-finder configurator's internal filter layout
