---
version: alpha
name: "Pioneer DJ"
source_url: "https://www.pioneerdj.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, precision-oriented instrument brand where #313131 ink meets a single blue voltage of #0076bf — the color of a cue light on a CDJ-3000 jog wheel, the exact shade that says "locked" and "ready." The palette is almost entirely achromatic: #fdfdfd canvas, #444444 body text, #808080 muted, #d7d7d7 hairline, with #e40010 reserved for record-red recording indicators and #006f00 for sync-lock confirmation. The brand trusts its hardware photography to carry emotion; the UI stays out of the way. Type runs system-native — -apple-system, Arial, Helvetica Neue, Segoe UI — at modest weights (400 body, 600 headings), never decorative. Buttons are flat rectangles with {rounded.xs} corners, the same 4px radius as the chamfer on a mixer chassis. The top nav is a dark strip (#2b2a38) with white text, a deliberate inversion of the white-canvas norm, mirroring the dimmed booth of a nightclub. Product cards use {rounded.sm} and a single hairline border, letting the gear's own industrial design — silver faceplates, black knobs, blue displays — provide all the visual interest. The search bar is a dark pill (#313131 on #fdfdfd), and the primary CTA is a solid #0076bf rectangle that never changes shape: no gradient, no shadow, no hover lift. This is a brand that edits by subtraction — every pixel that remains has a job.

colors:
  primary: "#0076bf"
  primary-active: "#00609e"
  primary-disabled: "#b3d4f0"
  ink: "#313131"
  body: "#444444"
  muted: "#808080"
  muted-soft: "#a7a9ac"
  hairline: "#d7d7d7"
  hairline-soft: "#e6e7e8"
  canvas: "#fdfdfd"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-bg: "#2b2a38"
  record-red: "#e40010"
  sync-green: "#006f00"
  cue-blue: "#0076bf"
  accent-teal: "#20dfc3"
  accent-blue-bright: "#24f6d6"
  accent-blue-mid: "#395ee2"
  accent-blue-soft: "#d2eaff"
  rating-star: "#bbbbbb"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-record:
    backgroundColor: "{colors.record-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  top-nav:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-item:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 64px
  top-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "0 {spacing.lg}"
    height: 40px
  search-bar-input:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    placeholderColor: "{colors.muted-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link-item:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.footer-link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    borderBottom: "1px solid {colors.hairline}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
    padding: "12px 16px"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "12px 16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
  rating-stars-active:
    color: "{colors.primary}"
    size: 16px
  notification-badge:
    backgroundColor: "{colors.record-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"

## Components

### Buttons
**`button-primary`** — The primary call to action across the site. A solid #0076bf rectangle with {rounded.xs} corners, white text in 15px/600 weight, and 44px height. On hover it darkens to #00609e (`{colors.primary-active}`); disabled state uses a pale blue #b3d4f0 (`{colors.primary-disabled}`). No shadow, no gradient — the flatness is intentional, matching the matte finish of DJ hardware.

**`button-secondary`** — An outlined variant for less prominent actions. White background, #313131 text, 1px solid #d7d7d7 border. Same 44px height and {rounded.xs} as the primary. Hover state adds a heavier border (2px) or shifts to a filled state depending on context.

**`button-tertiary`** — Text-only link styled as a button. Transparent background, #0076bf text, no border. Used for "Learn More" and "View Details" links within product cards. Hover adds underline.

**`button-dark`** — Used on light backgrounds in the hero or feature sections. Solid #313131 fill with white text. Same dimensions and radius as `button-primary`. Provides contrast inversion when placed on the white canvas.

**`button-record`** — A compact, high-alert button for recording or live-streaming actions. Solid #e40010 fill, white text in 13px/600 weight, 32px height. The red is the same shade as the REC indicator on Pioneer DJ hardware.

### Navigation
**`top-nav`** — The persistent global navigation bar. A dark strip at #2b2a38 (`{colors.nav-bg}`), 64px tall, with white uppercase nav links in 14px/600 weight and 0.5px letter spacing. The active page is indicated by a 2px #0076bf bottom border on the nav item. The brand logo sits left-aligned in white.

**`top-nav-item`** — Individual navigation links within the top bar. Padding of 16px on each side, full 64px height for clickable area. Hover state shows a subtle lightening of the text or a thin underline.

**`search-bar`** — A pill-shaped search input with #313131 fill and white text, 40px tall, placed in the top nav or hero area. The placeholder text is #a7a9ac (`{colors.muted-soft}`). The search icon is white. On focus, the border glows with a 1px #0076bf outline.

### Cards
**`product-card`** — The primary content container for DJ gear listings. White background, 1px solid #d7d7d7 border, {rounded.sm} corners, 16px padding. The product image sits at a 4:3 ratio with {rounded.sm} top corners. Below it: the product name in 16px/600 weight, the price in 16px/400 weight, and optional badges.

**`product-card-badge`** — A small label overlaid on the product image. Solid #0076bf fill, white uppercase text in 11px/700 weight, {rounded.xs} corners, 2px vertical padding and 8px horizontal. Used for "NEW," "BEST SELLER," or "LIMITED EDITION."

**`product-card-badge-new`** — A variant for the "NEW" badge specifically, using #20dfc3 (`{colors.accent-teal}`) fill with #313131 text. The teal signals freshness without competing with the primary blue.

### Forms & Inputs
**`filter-chip`** — A pill-shaped filter toggle for product listing pages. White background, #444444 text, 1px solid #d7d7d7 border, {rounded.full} corners, 6px vertical and 16px horizontal padding. Active state inverts to #313131 fill with white text.

**`quantity-selector`** — A horizontal stepper for cart quantities. White background, 1px solid #d7d7d7 border, {rounded.xs} corners, 40px height. The minus and plus buttons are 40px squares with no border radius, sitting flush inside the container.

**`tab-bar`** — A horizontal tab strip for product detail pages (Overview, Specs, Reviews, Support). White background, 1px solid #d7d7d7 bottom border. Active tab has a 2px #0076bf bottom border and #313131 text; inactive tabs use #808080 text.

### Navigation & Wayfinding
**`breadcrumb`** — Secondary navigation path, typically "Home > Products > DJ Players > CDJ-3000." Uses 13px/400 weight text in #808080, with the final (active) crumb in #444444. Separator is a simple ">" in #d7d7d7.

**`pagination-button`** — Page number buttons for product listing grids. White background, #444444 text, 1px solid #d7d7d7 border, {rounded.xs} corners, 8px vertical and 12px horizontal padding. Active page uses #0076bf fill with white text.

### Feedback & Status
**`notification-badge`** — A small circular indicator for cart count or alerts. Solid #e40010 fill, white text in 12px/400 weight, {rounded.full} shape, 20px minimum size. Positioned absolutely at the top-right of the cart icon.

**`rating-stars`** — Five 16px star icons in #bbbbbb for empty, #0076bf for filled. Used on product cards and detail pages. Half-star rendering is supported for fractional ratings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards go single-column (1-up); hero section reduces padding to 32px; filter chips stack vertically; search bar moves below nav; footer links collapse to accordion. |
| Tablet | 744–1128px | Top nav shows abbreviated labels (icons + short text); product cards display 2-up grid; hero uses 48px padding; filter chips wrap in a horizontal strip; search bar remains in nav but shrinks to 32px height. |
| Desktop | 1128–1440px | Full top nav with all links; product cards display 3-up grid; hero uses 64px padding; filter chips in a horizontal scrollable strip; search bar at full 40px height. |
| Wide | > 1440px | Max-width container at 1440px, centered; product cards display 4-up grid; hero uses 80px padding; additional whitespace around content; footer expands to 4-column layout. |

### Touch Targets
- All interactive elements (buttons, links, filter chips) maintain a minimum 44x44px touch target on mobile.
- Top nav hamburger icon is 48x48px.
- Quantity selector buttons are 40x40px.
- Product card tap targets (image, title, price) are the full card width.
- Filter chips have 6px vertical padding ensuring a 32px+ touch height.

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px; the menu overlay is full-screen with a #2b2a38 background.
- Product card grids reduce columns: 4→3→2→1 as viewport shrinks.
- Footer link groups collapse to accordion panels below 744px, each with a chevron toggle.
- Hero section reduces vertical padding from 80px to 32px on mobile.
- Filter chip strip becomes a vertical list on mobile, with a "Filters" toggle button.
- Breadcrumbs truncate on mobile, showing only the current page and a "Back" link.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by grays (#808080, #313131, #444444, #fdfdfd, #d7d7d7, #a7a9ac, #bbbbbb, #b9b9b9, #e4e4e4, #eeeeee, #888888, #5e5e5e, #a9a9a9, #c1c1c1) and blues (#0076bf, #395ee2, #0073a8, #0087c6, #007db7, #d2eaff, #496ceb), with a few bright accents (#24f6d6, #20dfc3, #23cfd8, #e40010, #006f00). The primary #0076bf was selected as the most distinctive brand-aligned blue, but confirmation from Pioneer DJ's official brand guidelines would be ideal.
- Font-family declarations were limited to system fonts; Pioneer DJ may use a custom typeface (e.g., a modified version of Helvetica or a proprietary font) that wasn't detectable from CSS.
- Hover states for buttons and links are inferred from common patterns; exact color values (e.g., `button-primary` hover darkening) need verification.
- Error styling for forms (validation messages, input error borders) was not extracted.
- Dark mode support is unknown; the site appears to use a light canvas with dark nav as its primary scheme.
- Sub-brand palettes (e.g., Pioneer DJ Pro Audio, TORAIZ, rekordbox) may have distinct color systems not captured.
- Animation and transition timing (hover fades, page transitions, loading states) was not extracted.
- Iconography system (SVG library, stroke weights, icon sizes) was not available from the extraction.
- The extracted list includes potential social-icon colors (#395ee2, #496ceb) and checkout-widget tones; these should be validated against the live brand.
