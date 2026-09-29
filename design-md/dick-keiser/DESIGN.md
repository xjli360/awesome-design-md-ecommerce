---
version: alpha
name: "Dick Keiser"
source_url: "https://www.dickkeiser.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pure browser-blue (#0000cc) meets a philatelist's catalog logic — Dick Keiser's stamp shop wears its heritage in the palette itself, leaning into the unmodulated web-primaries that serious collectors recognize from decades of online dealing: electric blue links, forest-green availability indicators (#116600), and red (#cc0000) callouts for lot status. The site's visual grammar is that of a working reference catalog rather than a retail storefront: dense listings, tabular lot organization, and a light blue-gray wash (#d1dfed) that echoes the glassine stock cards philatelists use to sleeve stamps. Navigation is a flat horizontal bar in dark navy (#000033) — the same ink that anchors the lot-number labels and condition grades throughout the catalog. Typography runs entirely in system sans-serif, which keeps pages lightweight and legible at the dense information densities stamp collectors expect when scanning hundred-lot runs of revenues or airmail covers. The green family (#116600 base, #75be55 mid, #32a35e teal accent) carries availability and category signals, replacing the retail convention of using green only for price or checkout cues. Condition badges — the philatelic shorthand of VF, XF, F-VH — sit in small #eeeeee chips against the card surface, keeping grading information present without visual competition with the stamp scan. The hairline blue (#d1dfed) divides rows and panels without imposing weight, consistent with the collector-catalog tradition of guiding the eye across dense tabular data. No rounded corners beyond minimal field radii, no gradients, no hero imagery — the stamp photograph is the hero, and the interface exists to get out of its way.

colors:
  primary: "#0000cc"
  primary-active: "#0000ff"
  primary-disabled: "#6699cc"
  primary-hover: "#0000aa"
  ink: "#000033"
  body: "#000033"
  muted: "#6699cc"
  hairline: "#d1dfed"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  green-base: "#116600"
  green-mid: "#32a35e"
  green-light: "#75be55"
  red-accent: "#cc0000"
  blue-light: "#d1dfed"
  blue-muted: "#6699cc"

typography:
  display-xl:
    fontFamily: "sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  lot-number:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  price-display:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  category-label:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    padding: 6px 14px
    height: 32px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 5px 13px
    height: 32px
    border: "1px solid {colors.hairline}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    height: 28px
    border: "1px solid {colors.muted}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 36px
    padding: "0 {spacing.base}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.blue-light}"
    linkActiveColor: "{colors.green-light}"
  sub-nav:
    backgroundColor: "{colors.blue-light}"
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    height: 28px
    padding: "4px {spacing.base}"
    linkColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1/1"
    imageBorder: "1px solid {colors.surface-soft}"
  lot-number-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.lot-number}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  condition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "1px 5px"
    border: "1px solid {colors.hairline}"
  availability-indicator:
    availableColor: "{colors.green-base}"
    soldColor: "{colors.red-accent}"
    pendingColor: "{colors.blue-muted}"
    typography: "{typography.caption-bold}"
  price-tag:
    textColor: "{colors.red-accent}"
    typography: "{typography.price-display}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: "4px {spacing.sm}"
    height: 30px
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    activeLinkColor: "{colors.green-base}"
    activeLinkWeight: 700
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
  lot-table-row:
    backgroundColor: "{colors.canvas}"
    alternateBackgroundColor: "{colors.blue-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "4px {spacing.sm}"
  section-header:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "6px {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.caption}"
    separator: "›"
    padding: "{spacing.xs} 0"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "3px 7px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.blue-light}"
    linkColor: "{colors.blue-muted}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.base}"

## Components

### Buttons

**`button-primary`** — A compact, flat blue rectangle (#0000cc) with white text and 2px radius corners, sized at 32px height to fit neatly beside lot listings and search controls. Hover shifts to a slightly deeper blue (#0000aa); active state flares to pure #0000ff. No shadow or animation — the button reads as a catalog control, not a retail CTA.

**`button-secondary`** — Light gray (#eeeeee) fill with an ink border, same compact height as primary. Used for secondary catalog actions like "View Details" or "Add to Watch List." Matches the utilitarian register of philatelic reference pages.

**`button-link`** — Inline underlined text in #0000cc, the classic hyperlink convention that stamp collectors navigating deep catalog hierarchies expect. No border or background.

### Navigation

**`nav-bar`** — Dark navy (#000033) horizontal bar carrying the top-level category links in bold 14px white sans-serif. Links span U.S. stamps, Worldwide, Collections, Covers, Revenues, and Postcards — the same taxonomy as the page title. Hover lightens link text to the blue-gray (#d1dfed); active category renders in green (#75be55) to distinguish current section.

**`sub-nav`** — A lighter blue-gray (#d1dfed) strip immediately below the main nav carrying sub-category links in uppercase 13px bold, with blue (#0000cc) link color. Provides the second layer of catalog drill-down without adding height to the page header.

### Product Card & Lot Table

**`product-card`** — Square stamp scan with a thin hairline (#d1dfed) border, followed by lot number badge, one-line description in 13px sans-serif, condition badge, and red (#cc0000) price. Cards sit edge-to-edge in a grid with no gap shadow — the image is the sole hierarchy signal.

**`lot-table-row`** — Alternating white and pale blue (#d1dfed) rows display lot number, Scott catalog number, description, condition, and price in columnar format. The alternating tint is the primary readability device on dense listing pages.

**`lot-number-badge`** — Small gray pill (#eeeeee) with 12px bold tracking, showing the sale lot number or catalog reference. Positioned top-left over the stamp image or at the start of the table row.

**`condition-badge`** — Tight gray chip with hairline border displaying philatelic grade abbreviations (VF, XF, F-VH, NH, OG). 12px bold, no color fill — condition grades are neutral data, not marketing signals.

### Catalog Structure

**`category-sidebar`** — A soft-gray (#eeeeee) left panel listing category and sub-category links in 13px sans-serif blue. Active category renders in green (#116600) bold to orient the collector within the taxonomy. A right hairline (#d1dfed) divides it from the listing column.

**`section-header`** — Navy (#000033) band with white bold title text, used to head each catalog section (U.S. Definitives, Air Mail, Special Delivery, etc.). Provides the visual chapter break in a long scrolling catalog.

**`availability-indicator`** — Inline colored text label: green (#116600) for available, red (#cc0000) for sold, muted blue (#6699cc) for pending or reserved. 12px bold, placed immediately after the price.

### Search & Utility

**`search-bar`** — Rectangular input with a thin blue border (#0000cc) and an inline submit button in #0000cc with white text. Compact 30px height sits within the nav zone or above catalog listings. No pill shape — straight corners throughout.

**`breadcrumb`** — Small 12px muted-blue chain with "›" separators, linking back through the catalog hierarchy. Hyperlinks render in #0000cc underlined; the current page renders in plain muted (#6699cc).

**`pagination`** — Flat page-number buttons with hairline borders and blue text. Active page fills solid navy (#000033) with white text. Sized at 26px height, arranged horizontally at the bottom of listing pages.

### Footer

**`footer`** — Dark navy (#000033) band with blue-gray (#d1dfed) body text and muted-blue (#6699cc) links. Contains contact information, philatelic society memberships, and category links. White on hover. Dense and informational — a second navigation layer for collectors who reach the page bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Category sidebar collapses to a dropdown selector; lot table converts to stacked cards; nav bar wraps to two rows; stamp images expand to full column width |
| Tablet | 744–1128px | Sidebar narrows to 160px; lot grid shifts from 4-up to 2-up; sub-nav compresses to horizontal scroll |
| Desktop | 1128–1440px | Standard two-column layout with 200px sidebar and lot grid or table at full width; nav bar fully expanded |
| Wide | > 1440px | Max content width ~1200px centered; side margins fill with canvas white; no decorative expansion |

### Touch Targets

- All nav links minimum 36px tap height on mobile
- Lot cards expand tap zone to full card surface (not just image or title)
- Pagination buttons minimum 36×36px on mobile
- Search submit button minimum 44px wide on touch

### Collapsing Strategy

- Category sidebar converts to a `<select>` dropdown on mobile to preserve vertical space
- Lot table collapses each row into a stacked card: lot number + image top, description + condition + price below
- Sub-nav scrolls horizontally on tablet and mobile with no wrapping
- Footer category columns stack vertically on mobile, two-up on tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface detected — only generic `sans-serif` stack; exact rendering depends on OS default (Arial on Windows, Helvetica Neue on macOS)
- No meta theme-color set; mobile browser chrome color cannot be confirmed
- Button border-radius values estimated from catalog convention; site may use fully square corners (0px) throughout
- Exact hover/focus states for form inputs not extractable from static hints
- Specific Scott catalog number formatting and lot image overlay conventions unconfirmed without full page inspection
- Green family usage split (#116600 vs #32a35e vs #75be55) is inferred from contrast hierarchy; precise role assignments per green shade not confirmed
- Cart, checkout, and account page styling not represented in extracted colors — may introduce additional tokens
- Whether condition badges use border or background fill only could not be confirmed from extraction
