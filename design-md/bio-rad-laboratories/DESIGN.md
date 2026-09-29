---
version: alpha
name: "Bio-Rad Laboratories"
source_url: "https://www.bio-rad.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bio-Rad's navigation arrives as a multi-column mega-menu spanning product families from Droplet Digital PCR to Western Blotting reagents before the homepage hero has resolved — the site's information architecture treats its catalog depth as the primary interface, relegating photography and brand atmosphere to secondary roles. The dominant primary is a deep institutional blue, approximately #0054a6, that carries every navigation header, hyperlink, and call-to-action. It reads as authority without spectacle: a color that has spent decades on instrument panels and laboratory procurement portals, where trust is earned through specification accuracy rather than visual warmth. Body text runs in system-stack Arial at 14–16px with permissive line-height, choosing legibility for protocol-reading researchers over editorial personality. White (#ffffff) canvas with a faint surface-soft (#f2f6fb) lift on alternating sections creates low-noise zones for technical specification tables and instrument comparison grids — areas where the eye must scan horizontally across many data points without losing its row.

  The product card carries a dual-action footer: "Add to Cart" for consumables and reagent kits, "Request a Quote" for capital instruments — a fork that acknowledges two entirely different commercial paths without forcing the user to self-identify upfront. A persistent search bar with catalog-number autocomplete anchors every page; the search box is the primary wayfinding instrument, not secondary utility. A utility ribbon at the top carries region-selector, sign-in, and cart compressed into a 36px band above the 60px primary nav — the two-bar nav pattern is characteristic of B2B scientific portals where field sales reps and bench researchers share a domain but follow divergent paths.

  Corner radii stay minimal: {rounded.xs} on badges and filter pills, {rounded.sm} on input fields and larger cards. No decorative gradients or hero glows exist anywhere in the layout. Functional outline iconography at 18–24px aligns with instrument-panel conventions. The footer is an information architecture exercise — link columns organized by product line, applications, support, and regional compliance, capped with ISO and CE certification marks that communicate directly to procurement teams. Color temperature runs cooler than consumer DTC: the blue leans toward a suppressed-cyan navy rather than the warmer cobalt common in B2C contexts.

colors:
  primary: "#0054a6"
  primary-active: "#003d7a"
  primary-disabled: "#99bfe0"
  primary-light: "#e8f1fb"
  accent-red: "#c8102e"
  accent-red-light: "#fceef0"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#5f6368"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f2f6fb"
  surface-card: "#ffffff"
  surface-alt: "#f5f5f5"
  on-primary: "#ffffff"
  success: "#2e7d32"
  warning: "#e65100"
  link: "#0054a6"
  link-visited: "#5c00a3"

typography:
  display-xl:
    fontFamily: "Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.2px
  nav-primary:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-secondary:
    fontFamily: "Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  sku:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  spec-value:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  button-cta-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-quote:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  utility-bar:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-secondary}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-primary}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-secondary}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 12px rgba(0,0,0,0.10)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    focusBorder: "2px solid {colors.primary}"
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 40px
    width: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px rgba(0,0,0,0.06)"
    imageBackground: "{colors.canvas}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-sku:
    typography: "{typography.sku}"
    textColor: "{colors.muted}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    shadow: "0 2px 8px rgba(0,84,166,0.15)"
  product-category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    shadow: "0 2px 6px rgba(0,0,0,0.06)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 38px
    padding: "{spacing.sm} {spacing.base}"
    focusBorder: "1px solid {colors.primary}"
    focusShadow: "0 0 0 3px rgba(0,84,166,0.15)"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 38px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-promo:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  application-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  application-tile-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 400px
    padding: "{spacing.section} 0"
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    minHeight: 280px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    headerTypography: "{typography.title-sm}"
    headerBackground: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    borderColor: "{colors.hairline}"
    rowAlternate: "{colors.surface-soft}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  pagination:
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  section-header:
    textColor: "{colors.primary}"
    typography: "{typography.display-sm}"
    borderBottom: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
  alert-info:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  compare-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: "6px 12px"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    linkColor: "#a8c8f0"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
  footer-bottom:
    backgroundColor: "#002a5a"
    textColor: "#8ab0d0"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — Solid #0054a6 fill, white text at `{typography.button-md}` (14px/700), 4px radius, 40px tall. The sharp corner at `{rounded.xs}` signals a professional B2B environment rather than consumer softness; these buttons appear on every Add to Cart, Download Protocol, and Submit action across the site. Hover darkens to `{colors.primary-active}` (#003d7a). Disabled state desaturates to `{colors.primary-disabled}` with white label text retained.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching primary blue text. Used for "Request a Quote" and comparison initiators — the outline treatment distinguishes capital equipment inquiry paths from immediate consumable purchases. Hover shifts background to `{colors.primary-light}` and border to `{colors.primary-active}`.

**`button-cta-red`** — `{colors.accent-red}` (#c8102e) fill for high-urgency or promotional CTAs such as conference registration or limited-time offers. Appears sparingly — the red reads as an elevated-urgency signal against the predominantly blue site, and overuse would dilute its attention value.

**`button-quote`** — Structurally identical to `button-secondary`; semantically reserved for the "Request a Quote" action on capital instrument product pages. Kept as a distinct component to allow styling changes to the quote flow independently of other secondary buttons.

**`button-text-link`** — No background, `{colors.link}` underlined text at `{typography.body-sm}`. Used for in-prose document links, "Learn more" expansions, and cross-referenced application pages throughout the product catalog.

### Navigation
**`utility-bar`** — A 36px dark-blue (#003d7a) strip at the very top carrying region/language selector, sign-in, and order management in white `{typography.nav-secondary}`. Keeps logistics and account paths out of the primary nav real estate while keeping them persistently accessible.

**`nav-bar`** — White 60px bar containing the Bio-Rad wordmark left-anchored, main category links in `{typography.nav-primary}`, and a search field spanning approximately 40% of the bar width right of center. The search-first layout reflects that returning users arrive with catalog numbers or protocol names rather than browsing intent.

**`mega-menu`** — Drops full viewport width on hover over category labels (PCR, Western Blotting, Flow Cytometry, Genomics, etc.). Organized in four to six columns with `{colors.primary}` section headers at `{typography.title-sm}`. No photography — the mega-menu is a dense link library organized by product family and application. Closes on mouse-out with a brief delay to prevent accidental dismissal during cursor travel.

### Search
**`search-bar`** — Embedded in the nav bar at 40px height with `{rounded.xs}` radius and attached `{colors.primary}` icon button at the right edge. Autocomplete returns matches across product names, catalog numbers, gene targets, and application keywords in a dropdown panel with `{colors.surface-soft}` row highlighting. On focused input, border transitions to a solid 2px primary blue.

### Product Cards
**`product-card`** — White `{colors.surface-card}` surface, 1px `{colors.hairline}` border, `{rounded.xs}` radius, `{spacing.base}` internal padding. Product image occupies the upper portion of the card on a white background for visual consistency across instrument and reagent photography. Title renders in `{typography.title-sm}` primary blue as a clickable link; catalog number below in `{typography.sku}` muted gray. A hairline divider separates the image zone from the text zone. Two action buttons — Add to Cart and Request a Quote — appear in the card footer, representing the dual commercial path. Hover state adds a primary blue 1px border and a faint blue box shadow.

**`product-category-card`** — Used on the homepage and category landing pages to orient users into segment families. Larger tile with 4:3 image ratio, `{rounded.sm}` radius, and a light shadow. Title at `{typography.title-md}` sitting below the image on a white background strip. On hover the image scales 1.03× within the contained radius.

### Badges and Labels
**`badge-new`** — `{colors.accent-red}` fill with white uppercase `{typography.label}` text, `{rounded.xs}` radius, 2px × 6px padding. Applied as an overlay to recently launched instruments and kits. Because red appears nowhere else in the default product UI, it reads immediately as a freshness signal without requiring a legend.

**`filter-pill`** — Used in faceted search sidebars for filtering by application, format, species, and instrument compatibility. Default: `{colors.surface-soft}` fill with hairline border. Active state: solid `{colors.primary}` fill with white text — a binary that avoids ambiguous intermediate selection states. Pill shape at `{rounded.full}` softens the otherwise angular component vocabulary.

### Data and Specifications
**`spec-table`** — Header row in `{colors.primary}` with white `{typography.title-sm}` text. Body rows alternate between `{colors.canvas}` and `{colors.surface-soft}` for horizontal scan legibility across throughput, resolution, and compatibility data. Used on all instrument product pages. Cells receive 1px `{colors.hairline}` borders; no border-collapse to avoid artifacts.

**`application-tile`** — Square or near-square tile on application landing pages (Gene Expression, Genomics, Cell Biology). `{colors.surface-soft}` background with `{colors.hairline-soft}` border at `{rounded.sm}`. On hover shifts to `{colors.primary-light}` fill and full `{colors.primary}` border — provides a strong accessible focus indicator that works equally for keyboard and mouse navigation.

### Alerts and Feedback
**`alert-info`** — `{colors.primary-light}` background with `{colors.primary-active}` text and a 1px `{colors.primary}` border at `{rounded.xs}`. Used for shipping notices, regional regulatory notes, and product lifecycle status messages. The color family connects the alert visually to primary actions rather than treating it as system noise.

### Hero
**`hero-section`** — Deep `{colors.primary-active}` fill at 400px minimum height. Display heading in `{typography.display-xl}` white; body copy in `{typography.body-md}` white with reduced opacity. One primary and one secondary CTA in the bottom-left quadrant. Instrument photography or scientist-at-bench imagery positioned right-of-text at desktop widths, collapsing below text on mobile.

**`hero-light`** — `{colors.surface-soft}` variant used for sub-category landing pages. Heading in `{typography.display-md}` `{colors.ink}`, 280px minimum height. Less visual weight than the full dark hero — appropriate for pages where the content grid directly below carries the primary value.

### Section Framing
**`section-header`** — `{colors.primary}` heading text at `{typography.display-sm}` with a 3px solid primary bottom border as a visual rule. Used to delineate major homepage content sections (Featured Products, Applications, Resources). The border provides emphasis without adding background color blocks.

### Footer
**`footer`** — Full-width `{colors.primary-active}` dark blue with white section headings in `{typography.title-sm}` and light blue (#a8c8f0) link text in `{typography.body-sm}`. Organized in five to seven columns covering Products, Applications, Support, Company, and Regional links. ISO, CE, and other certification mark images appear above the bottom strip, targeting procurement and compliance reviewers.

**`footer-bottom`** — Darker #002a5a strip with muted #8ab0d0 text at `{typography.caption}` carrying copyright, privacy policy, cookie preferences, and legal links. Social icons rendered as white outline glyphs at 32px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Utility bar collapses to icon-only (cart, account); primary nav becomes a hamburger drawer; search bar moves below logo at full width; product grid switches to single column; mega-menu replaced by full-screen accordion drawer |
| Tablet | 744–1128px | Two-column product grid; nav bar retains wordmark and search field; category links condensed to a "Products" dropdown; hero image repositioned below text block |
| Desktop | 1128–1440px | Full two-row nav (utility bar + primary nav); three- to four-column product grid; mega-menu on hover; hero with side-by-side text and image layout |
| Wide | > 1440px | Content max-width capped at approximately 1400px; surplus whitespace distributed as symmetric horizontal margin; no additional product grid column added |

### Touch Targets
- All interactive elements (buttons, nav links, filter pills, accordion headers) minimum 44 × 44px on mobile viewports
- Product card entire surface is tappable on mobile, not only the title link
- Mega-menu replaced by full-height accordion drawer on touch devices to avoid hover-only navigation traps
- Search submit button maintains a 48px tap zone via padding extension beyond its 40px visual height
- Pagination numbers padded to at least 44px wide for one-handed thumb reach

### Collapsing Strategy
- Utility bar on mobile: region selector and language picker moved to footer; account icon and cart icon persist in the header right cluster
- Primary navigation: two-level accordion in mobile drawer — top-level category labels expand to reveal sub-category links sourced from the mega-menu columns, preserving the same IA without requiring hover capability
- Specification tables: horizontal scroll container on mobile with a pinned first column for the parameter name; row height increases by 4px for touch scan comfort
- Footer columns: stack vertically on mobile with accordion collapse; each section heading is a 44px touch target with a caret indicator; all columns collapsed by default to reduce initial scroll depth
- Filter sidebar: collapses into a modal sheet triggered by a "Filters" button above the product grid on mobile; applied filter count shown on the button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — bio-rad.com likely loads design tokens via JavaScript or serves a bot-protected response to automated requests; all color values in this file are estimates derived from widely visible brand materials and must be validated against Bio-Rad's internal design system or Figma source before production use
- The exact primary blue cannot be confirmed without direct extraction (#0054a6 is a reasonable public estimate; official brand guidelines may specify a slightly different value such as #004b9c, #0057b8, or a Pantone-derived equivalent)
- Accent red precise value is unconfirmed (#c8102e is estimated from visible brand assets; some Bio-Rad materials show a slightly brighter or more saturated red)
- No custom or licensed font was detected — the site uses Arial/system sans-serif throughout; a proprietary display or marketing font may exist in offline brand materials but was not found in any page font stack
- Secondary product-line accent colors (if any teal, green, or gold exists for sub-brands such as Bio-Rad Life Science vs. Clinical Diagnostics divisions) were not derivable from available extraction data
- Icon set vendor and exact glyph library are unknown; outline-style icons at 18–24px are inferred from visual convention for B2B scientific portals
- Animation and transition timing (mega-menu open/close duration, card hover timing, autocomplete fade) are not derivable from available data and require direct inspection
- Exact nav height values (36px utility bar, 60px primary nav) are estimates based on visual conventions for this site category and should be measured from the live DOM
