---
version: alpha
name: "University of Chicago Press"
source_url: "https://press.uchicago.edu"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A scholarly marketplace where a deep teal (#007396) and a muted aubergine (#59315f) bracket the intellectual seriousness of the institution — the teal appears on primary CTAs, search bars, and category headers, while the aubergine surfaces in footer blocks and secondary navigation, creating a quiet tension between the empirical and the humanistic. The canvas is a warm off-white (#f4f4f4) rather than pure white, lending the reading experience the weight of paper stock rather than screen glare. Type is set in HCo Gotham for display and body, with Attleboro Gothic WTF Regular reserved for academic series titles and chapter headings — a deliberate shift from the sans-serif default that signals scholarly lineage. Buttons are softly rectangular ({rounded.sm}), never pill-shaped, and the search bar sits in a persistent top bar with a teal outline that recalls the spine of a cloth-bound book. The color palette is unusually broad for a university press — the extracted list includes a cyan accent (#4ad5ff), a warm gold (#d39e00), and a muted rose (#e83e8c) — but these are likely used sparingly for callouts, price tags, and series badges rather than as primary brand voltages. The overall effect is that of a library reading room translated into a web interface: restrained, authoritative, but with small moments of unexpected color that reward close attention.

colors:
  primary: "#007396"
  primary-active: "#004c63"
  primary-disabled: "#a6cedb"
  ink: "#3a3a3a"
  body: "#3a3a3a"
  muted: "#979797"
  muted-soft: "#c9c8cd"
  hairline: "#d8d8d8"
  hairline-soft: "#dae0e5"
  canvas: "#f4f4f4"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-aubergine: "#59315f"
  accent-aubergine-light: "#c6b7c7"
  accent-cyan: "#4ad5ff"
  accent-cyan-active: "#17c9ff"
  accent-gold: "#d39e00"
  accent-rose: "#e83e8c"
  accent-green: "#1e7e34"
  accent-red: "#bd2130"
  footer-bg: "#39203d"
  footer-text: "#d1c5d2"

typography:
  display-xl:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  series-title:
    fontFamily: "'Attleboro Gothic WTF Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'HCo Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: 1px solid "{colors.accent-red}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
    height: 42px
    border: 1px solid "{colors.primary}"
  search-bar-icon:
    color: "{colors.primary}"
    size: 18px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: 1px solid "{colors.hairline-soft}"
  product-card-hover:
    border: 1px solid "{colors.primary}"
    boxShadow: "0 2px 8px rgba(0,115,150,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3:4"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
    fontWeight: 500
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-series:
    backgroundColor: "{colors.accent-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
    hoverColor: "{colors.on-primary}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  category-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    border: 1px solid "{colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: 1px solid "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Search" actions. Rendered in the brand teal (#007396) with white text and a subtle 4px corner radius. On hover, the background deepens to the active state (#004c63). When disabled, the button fades to a muted teal (#a6cedb) with white text, signaling unavailability without visual noise.

**`button-secondary`** — An outlined variant used for secondary actions like "Preview" or "Learn More". Features a white background with a 1px teal border and teal text. On hover, the background fills with teal and text inverts to white, providing clear visual feedback.

**`button-tertiary`** — A text-only button used for inline actions such as "View All" or "Clear Filters". No background or border; relies on teal text color and the button's typography weight for affordance. Hover state adds an underline.

### Cards
**`product-card`** — The primary content container for book listings. A white card with a soft 1px border, 4px corner radius, and 16px internal padding. The card contains a 3:4 aspect ratio image, the book title in title-sm, the author name in caption, and the price in body-sm with 500 weight. On hover, the border shifts to teal and a subtle box shadow appears, creating a gentle lift effect that signals interactivity without overwhelming the scholarly tone.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height with a white background and a single 1px bottom border in hairline gray. Navigation links use nav-link typography with 12px horizontal padding. The active link is indicated by a 2px teal bottom border and teal text color, while inactive links remain in ink (#3a3a3a). The bar collapses to a hamburger menu on mobile.

**`search-bar`** — A persistent search input in the top navigation, rendered as a 42px tall input with a 1px teal border and 4px corner radius. The search icon is rendered in teal at 18px. On focus, the border thickens to 2px teal, providing clear keyboard focus indication.

### Forms
**`text-input`** — Standard text input for forms, including checkout and account creation. A 42px tall input with 1px hairline border, 4px corner radius, and 14px horizontal padding. On focus, the border becomes 2px teal. Error state uses a 1px red border (#bd2130) for accessibility.

### Badges
**`badge-new`** — A small, uppercase badge used to indicate new releases. Cyan background (#4ad5ff) with white text, 2px corner radius, and tight 2px/6px padding. The bright cyan provides a deliberate pop of color against the restrained palette.

**`badge-sale`** — A gold badge (#d39e00) with dark text for sale or discount indicators. Same dimensions as badge-new but uses warm gold to signal value without resorting to aggressive red.

**`badge-series`** — An aubergine badge (#59315f) with white text for academic series designations. This badge ties directly to the brand's secondary color and is used on book cards to indicate membership in a scholarly series.

### Footer
**`footer`** — A full-width footer with a deep aubergine background (#39203d) and light text (#d1c5d2). Contains column headings in title-sm with white text, and links in body-sm that lighten to white on hover. Padding is generous at 48px vertical and 24px horizontal, creating a substantial base for the page.

### Tabs
**`tab-active`** — Active tab in a tabbed interface (e.g., "Books", "Journals", "Authors"). Teal background with white text, 4px corner radius, and 8px/16px padding. Inactive tabs use a soft surface background (#ececf6) with muted text (#979797), providing clear visual hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger; product cards stack vertically; search bar moves below nav; footer columns stack; category header reduces to title-sm |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (Books, Journals, About); search bar remains in nav; footer shows 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; search bar in top nav; footer shows 4-column grid; breadcrumbs visible |
| Wide | > 1440px | Max-width container at 1440px; three-column grid with wider gutters; additional whitespace around content; footer expands to 5 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product cards have a minimum 48px tap area for the entire card
- Tab elements are at least 40px tall with 16px padding
- Pagination buttons are 36px tall with 12px padding (minimum 44px tap area via padding)
- Hamburger menu icon is 44px x 44px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at mobile widths (< 744px), hiding all nav links behind a slide-out drawer
- Product grid collapses from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Footer columns collapse from 5 (wide) to 4 (desktop) to 2 (tablet) to 1 (mobile)
- Breadcrumbs are hidden on mobile; replaced by a "Back" button
- Category headers reduce font size on mobile (display-md to title-md)
- Search bar moves from the top nav to below the nav on mobile, becoming a full-width element
- Accordion components are used for filter panels on mobile; on desktop they remain expanded

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary buttons (underline vs. color change) could not be confirmed from extracted data
- Error state styling for forms beyond border color (error message typography, icon placement) is not reliably extracted
- Focus ring styling (color, offset, thickness) for keyboard navigation was not found in extracted CSS
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand palettes for specific imprints (e.g., Phoenix Fiction, Chicago Guides) could not be identified
- The exact usage frequency and context of accent colors (cyan, gold, rose) is inferred from common academic press patterns rather than extracted data
- Animation and transition durations (hover effects, page transitions) are not available
- The specific font weights available for Attleboro Gothic WTF Regular beyond the single extracted weight are unknown
- Dropdown menu styling (mega-menu, sub-navigation) was not captured in the extraction
- Loading states (spinners, skeleton screens) are not documented
- Print stylesheet behavior is not captured
- The extracted color list includes several colors that appear to be Bootstrap defaults (#1e7e34, #117a8b, #d39e00, #bd2130, #dae0e5, #1d2124) — these may not be actively used in the brand's design system but were present in the page's CSS. The true brand palette is likely more restrained, centered on the teal (#007396), aubergine (#59315f), and off-white (#f4f4f4) identified as primary.
