---
version: alpha
name: "Radwell International"
source_url: "https://www.radwell.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Search boxes outnumber decorative images across Radwell's catalog — the entire interface functions as an industrial inventory lookup engine where part numbers, condition grades (New, Recertified, Repaired), and lead times are the primary content hierarchy. The single confirmed extracted color, charcoal #313131, anchors navigation rails, table headers, and inline labels as the workhorse ink for a high-density B2B catalog; all other palette values were unextractable because Cloudflare bot protection blocked the live site during analysis (see Known Gaps). The broader palette likely pairs that charcoal with a deep industrial blue for CTA buttons and search-submit actions, and an amber-orange for condition badges — the two-signal system standard across industrial automation e-commerce where procurement speed outranks visual novelty. Type is drawn entirely from the system stack, Arial and Roboto first, a declaration that utility supersedes aesthetics and that pages must render crisply on factory-floor workstations and field-service laptops where custom font loading is a liability. Corner geometry is blunt throughout: part cards carry {rounded.xs} at most, CTA buttons land at {rounded.xs}, and only the search input earns a slightly softer {rounded.sm} — square edges communicate engineering precision rather than consumer friendliness. The component hierarchy places a mega-search bar at the absolute top of every page, followed by manufacturer and condition facets that filter across millions of SKUs. Product cards carry dense spec rows — manufacturer, part number in monospace, condition badge, in-stock count, price — with thumbnail images subordinate to the data grid. Trust signals appear as inline callouts: ISO certifications, warranty durations, repair turnaround promises. Every layout decision compresses maximum information into minimum viewport height, optimized for procurement professionals returning daily to look up one specific part number.

colors:
  primary: "#1a5196"
  primary-active: "#14407a"
  primary-disabled: "#a8c4e5"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#dddddd"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#e07820"
  condition-new: "#2e7d32"
  condition-new-bg: "#e8f5e9"
  condition-recertified: "#1565c0"
  condition-recertified-bg: "#e3f2fd"
  condition-repaired: "#e07820"
  condition-repaired-bg: "#fff3e0"
  table-header-bg: "#f0f0f0"
  table-stripe: "#fafafa"
  error: "#c62828"
  success: "#2e7d32"
  border-input: "#cccccc"
  link: "#1a5196"

typography:
  display-xl:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  table-header:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "Arial, Roboto, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 11px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    border: "1px solid {colors.primary}"
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-input}"
    padding: 8px 12px
    height: 38px
    focusBorder: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 16px
    height: 46px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.none}"
      width: 80px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
    subNavBackgroundColor: "{colors.canvas}"
    subNavTextColor: "{colors.ink}"
    subNavBorder: "1px solid {colors.hairline}"
  top-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    thumbnailSize: 80px
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.link}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    conditionBadgeInline: true
  condition-badge-new:
    backgroundColor: "{colors.condition-new-bg}"
    textColor: "{colors.condition-new}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  condition-badge-recertified:
    backgroundColor: "{colors.condition-recertified-bg}"
    textColor: "{colors.condition-recertified}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  condition-badge-repaired:
    backgroundColor: "{colors.condition-repaired-bg}"
    textColor: "{colors.condition-repaired}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  part-number-display:
    typography: "{typography.part-number}"
    textColor: "{colors.link}"
    copyable: true
  data-table:
    headerBackgroundColor: "{colors.table-header-bg}"
    headerTypography: "{typography.table-header}"
    headerTextColor: "{colors.ink}"
    rowTypography: "{typography.body-sm}"
    stripeBackgroundColor: "{colors.table-stripe}"
    borderColor: "{colors.hairline}"
    cellPadding: "8px 12px"
  facet-filter:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headingTypography: "{typography.title-sm}"
    headingTextColor: "{colors.ink}"
    itemTypography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    checkboxAccentColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
    searchBarInline: true
    searchBarMaxWidth: 640px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    iconColor: "{colors.accent-orange}"
    padding: "{spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "#a8c4e5"
    headingTypography: "{typography.title-sm}"
    headingTextColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — Flat {rounded.xs} rectangle in {colors.primary} blue, uppercase {typography.button-md}, 40px tall. Hover darkens to {colors.primary-active}; disabled desaturates to {colors.primary-disabled}. Used for highest-priority CTAs: "Add to Cart", "Search", "Submit RFQ". Never pill-shaped; the square geometry is intentional.

**`button-secondary`** — White fill with a 1px {colors.primary} border and matching uppercase label. Used for secondary actions: "Save to List", "Compare Parts", "Print Page". On hover, background fills with a light primary-blue tint; border weight stays constant.

**`button-ghost`** — Transparent background with {colors.primary} text in {typography.button-sm}. Used for low-priority inline actions — "View All Results", "Load More", pagination controls — where adding border weight would clutter dense data layouts.

### Search Bar
**`search-bar`** — The dominant UI element on every page. Full-width input with a 2px {colors.primary} border (persistent — the strong border signals primary interaction, not just focus state) and a flush right-attached submit button in solid {colors.primary}. Placeholder text prompts part number, manufacturer, or keyword entry. The submit button carries an uppercase SEARCH label in {typography.button-md}. On mobile, the search bar spans full viewport width with the submit button always visible.

### Navigation
**`nav-bar`** — Two-tier structure: a thin {colors.primary} {top-utility-bar} above a {colors.ink} charcoal main nav. The utility bar (32px) carries phone numbers, a "Get a Quote" link, and account/cart icons in {typography.caption} white. The main nav holds mega-menus for product categories — PLC Brands, Drives & Motion Control, Safety, Sensors, Repair Services — in {typography.nav-link}. Mega-menu panels open on hover with a white sub-panel, {colors.hairline} border, and 3–4 columns of linked categories.

**`top-utility-bar`** — Always visible; never collapsed on desktop. Phone number for the direct sales line occupies the left side; account, order history, and cart icons sit right-aligned.

### Product Cards
**`product-card`** — Compact white card with {rounded.xs} corner and 1px {colors.hairline} border. Layout top-to-bottom: small square thumbnail (80px), manufacturer name in {typography.body-sm} muted, part number in {typography.part-number} monospace colored {colors.link} for click affordance, inline condition badge, availability count, price in {typography.price-display}. "Add to Cart" and "Request Quote" buttons stack at bottom. No padding-trick aspect ratios — images are fixed small cells in a data-forward layout where the part number is the hero element.

### Condition Badges
**`condition-badge-new`**, **`condition-badge-recertified`**, **`condition-badge-repaired`** — Compact chip badges that communicate inventory grade, the primary data-differentiation signal across the catalog. Each uses a lightly tinted background with a matching dark-text label in {typography.badge-label} uppercase: New maps to green ({colors.condition-new} on {colors.condition-new-bg}), Recertified to blue ({colors.condition-recertified} on {colors.condition-recertified-bg}), Repaired to orange ({colors.condition-repaired} on {colors.condition-repaired-bg}). These badges appear in search result rows, product cards, cart line items, and order history.

### Part Number Display
**`part-number-display`** — Monospace {typography.part-number} in {colors.link} blue with a copy-to-clipboard affordance. Appears on product detail pages, cross-reference tables, and order confirmations. The monospace rendering is functional: it visually aligns alphanumeric codes and prevents character confusion in part numbers like "0O1lI".

### Data Tables
**`data-table`** — Dense specification tables with a {colors.table-header-bg} header row in {typography.table-header} uppercase. Body rows alternate between white and {colors.table-stripe} for scan speed. Used on product detail pages for interchangeable part cross-references, specification attributes, and repair history. Cell padding is tight at 8px vertical, 12px horizontal to pack maximum rows above the fold.

### Facet Filters
**`facet-filter`** — Left-rail panels in {colors.surface-soft} with a 1px {colors.hairline} border. Each facet group has a {typography.title-sm} heading and a checkbox list in {typography.body-sm}. Active selections display in {colors.primary}. Manufacturer-brand facets may carry small manufacturer logos at 20px height alongside the brand name. A "Clear All" link in {colors.link} appears above the filter list when any filter is active.

### Hero Banner
**`hero-banner`** — Full-width {colors.primary} blue section on homepage and major category landings. White headline in {typography.display-xl}, a one-line subhead in {typography.body-md}, and a centered search bar (max 640px wide) inline below. Background may carry a low-opacity circuit-board or grid watermark in a slightly lighter blue. No photography in the hero — the search field is the only interactive element above the fold.

### Trust Badges
**`trust-badge`** — Small horizontal cards with an {colors.accent-orange} icon glyph, a short label in {typography.title-sm}, and a caption line in {typography.caption}. Displayed in a 3–4 column row above the footer or in the product-page sidebar. Content set: "5M+ Parts In Stock", "ISO 9001 Certified", "Same-Day Shipping", "1-Year Warranty on Repairs". The {colors.accent-orange} icon color provides the only warm accent against an otherwise blue-and-gray palette.

### Footer
**`footer`** — Full-width {colors.ink} charcoal footer with a 3px {colors.primary} top border as a visual anchor. White column headings in {typography.title-sm}, links in muted blue #a8c4e5 with white hover states. Four to five columns: Product Categories, Services (Repair, Calibration, Exchange), About Radwell, Contact Us, Social Media. A copyright row at bottom carries certification logos. Dense link density mirrors the catalog's data-first personality.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar full-width with stacked submit button; nav collapses to hamburger with slide-out drawer; facet filters move behind a sticky "Filter & Sort" bar that opens a bottom sheet; condition badges truncate to initials (N / RC / RP) in tight row layouts |
| Tablet | 744–1128px | Two-column product grid; facet sidebar visible at 200px; nav bar items truncate to icon+abbreviated label; utility bar collapses to phone icon and cart only |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu nav with hover panels; dual-bar header fully visible; facet sidebar at 240px; data tables show all columns without horizontal scroll |
| Wide | > 1440px | Four-column product grid; content max-width 1400px centered with auto side margins; hero search bar expands to 640px; part-count callout and certification badges gain visibility in hero subhead |

### Touch Targets
- All buttons minimum 44×44px on mobile viewports
- Condition badge chips padded to 36px tap-target height on touch devices
- Part number links padded to 44px minimum tap target via vertical padding
- "Add to Cart" and "Request Quote" always full-width stacked on mobile product cards
- Nav hamburger icon minimum 44×44px hit area

### Collapsing Strategy
- Mega-menu navigation collapses entirely to a categorized list inside a hamburger slide-out drawer
- Facet filter sidebar collapses to a sticky "Filter" bottom bar that opens a full-screen sheet modal
- Top utility bar hides non-critical links on mobile; only the direct phone number and cart icon persist
- Data tables on mobile switch to stacked label–value card rows rather than horizontal scroll; part numbers stay monospace
- Hero search bar reduces from two-line (headline + search) to single search bar only on mobile, headline hidden

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site blocked by Cloudflare at extraction time** — page title "Just a moment..." confirms the live site was not rendered. Cloudflare's challenge page itself generated the single extracted color; none of Radwell's actual stylesheet was captured.
- **#313131 may be Cloudflare's color, not Radwell's** — this charcoal appears in Cloudflare's standard challenge page and may not reflect any Radwell brand token. Verify against live site nav and body text.
- **Primary blue #1a5196 is brand-knowledge inference** — not extracted from the live site. All blue, orange, and green values in this file are estimated from industrial B2B conventions and publicly visible screenshots. Verify every hex value before implementation.
- **No custom typeface detected** — font stack is entirely system fonts. Either Radwell ships no custom web font, or font-loading JS was blocked along with everything else. Confirm whether a licensed typeface is used.
- **Accent orange #e07820 unconfirmed** — estimated from condition-badge and trust-badge conventions common to industrial parts e-commerce; verify against live badge rendering.
- **Condition badge exact hex values unconfirmed** — the New / Recertified / Repaired taxonomy is documented in Radwell's catalog, but the precise badge colors are estimated.
- **Mega-menu taxonomy estimated** — category labels (PLCs, Drives, Safety, Sensors, Repair Services) inferred from known Radwell product lines; verify exact nav structure and depth against live site.
- **No meta theme-color extracted** — cannot corroborate primary color from browser chrome hints.
