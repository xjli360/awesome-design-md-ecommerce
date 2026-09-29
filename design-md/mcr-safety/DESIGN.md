---
version: alpha
name: "MCR Safety"
source_url: "https://www.mcrsafety.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Crimson (#c91036) lands with the authority of a hard-hat warning label — MCR Safety's single brand voltage saturating every primary CTA, in-stock badge, and promotional callout against a near-black (#181818) field. The site makes no apology for its utilitarian posture: the entire type system runs on OS-native stacks (Liberation Sans, Segoe UI, -apple-system) at weights that favor legibility under warehouse fluorescence over typographic distinction. Icon libraries (Font Awesome, icomoon) carry heavy navigation duty across gloves, glasses, cut-resistant sleeves, and hearing protection — each subcategory tagged with ANSI/OSHA compliance ratings that demand dense, tabular layouts rather than the editorial grids of consumer retail. Light grays form a stacked surface system, from the near-white #f8f8f8 field to #e5e3df, a warm putty tone that grounds callout blocks without introducing color competition. A secondary accent blue (#5eb0ef) marks filter chips and informational links, desaturated enough to read as functional rather than promotional. Corner radii stay minimal — `{rounded.xs}` on inputs and standard cards signals that specification accuracy matters more than friendliness of form. Safety compliance documentation, bulk ordering, and product comparison tables sit at the center of the UX, pushing high-contrast body text (`{colors.ink}` on `{colors.canvas}`) and generous section breathing (`{spacing.section}`) to the front of every layout decision. Bright blue (#0091ff) surfaces in interactive states and hyperlinks as a system-browser anchor rather than a brand color. The tagline "We Protect People" is unusually direct for a B2B distributor — it encodes both the brand's mission and its design contract: warnings surface before checkout, compliance badges appear on card thumbnails, and the red primary carries urgency without tipping into alarm.

colors:
  primary: "#c91036"
  primary-active: "#a50d2d"
  primary-disabled: "#ebb8c4"
  ink: "#181818"
  body: "#374151"
  muted: "#bbbbbb"
  hairline: "#dbdbdb"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  surface-warm: "#e5e3df"
  surface-mid: "#ededed"
  on-primary: "#ffffff"
  accent-blue: "#5eb0ef"
  accent-blue-strong: "#0091ff"
  border-mid: "#d0d0d0"
  border-light: "#e0e0e0"
  bg-cool: "#ebeff2"
  bg-slate: "#e2e8f0"

typography:
  display-xl:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  compliance-tag:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Liberation Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 44px
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
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 7px 15px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.accent-blue-strong}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-top-utility:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBg: "{colors.surface-soft}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  compliance-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  ansi-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  in-stock-badge:
    backgroundColor: "#22c55e"
    textColor: "{colors.canvas}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  price-line:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  sale-price:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"
    typography: "{typography.display-xl}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 36px
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "2px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 48px
    submitBg: "{colors.primary}"
    submitColor: "{colors.on-primary}"
  filter-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    headingTypography: "{typography.title-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.body}"
    typography: "{typography.caption}"
    separator: "/"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    accentBorder: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.border-mid}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"

## Components

### Buttons

**`button-primary`** — Solid crimson (#c91036) fill, white text, 4px radius, 44px tall: the same visual register as a warning label repurposed as a CTA. Active state deepens to #a50d2d; disabled washes to #ebb8c4 with white text preserved. Used for "Add to Cart," "Request a Quote," and all primary form submissions throughout catalog and checkout flows.

**`button-secondary`** — White fill with a 1px crimson border and crimson text, sitting alongside primary buttons for secondary actions such as "Add to Wishlist" or "Compare Products." The outlined treatment withholds the urgency signal of a filled button without disappearing into the page.

**`button-ghost`** — Transparent background with a hairline border and body-gray text at `button-sm` scale. Handles tertiary actions — "View More," filter resets, pagination controls — where applying red would overload the urgency hierarchy that the crimson primary depends on.

### Navigation

**`nav-bar`** — Full-width near-black (#181818) bar carrying white nav-link type and a crimson search-submit element. Mega-menus expand on hover, prefixed by Font Awesome / icomoon glyphs for each PPE subcategory. On desktop the `search-bar` component is embedded directly inside the nav row, keeping the search affordance persistently visible.

**`nav-bar-top-utility`** — A 36px crimson bar stacked above the main nav, carrying phone numbers, account links, and promotional messaging in caption-bold white. It reads as an alert band because the crimson ground is identical to the primary CTA color — intentional, as it trains users to treat red fields as high-priority information.

### Product Card

**`product-card`** — White card with a 1px hairline border and 4px radius. The product image sits on a #f8f8f8 swatch; below it: product name in `title-sm`, SKU in `caption`, then a horizontal strip of compliance badges (`ansi-badge`, `compliance-badge`) before the price line. Sale pricing uses `sale-price` (crimson) directly beneath the standard `price-line`. A quantity input and "Add to Cart" button occupy the card footer, visible persistently on mobile and on hover on desktop.

### Search

**`search-bar`** — Full-width input with a 2px hairline border that thickens to solid crimson on focus, reinforcing the primary color as the brand's interactive signal. The submit button is a crimson-filled block flush to the right edge of the field. Autocomplete suggestions surface against `surface-soft` in `body-sm`, keeping the dropdown palette neutral relative to the branded input chrome.

### Compliance Badges

**`compliance-badge`** — Near-black (#181818) chip with white uppercase `compliance-tag` type; carries standards designations like "ANSI A4," "EN 388," or "OSHA Compliant." **`ansi-badge`** — Crimson variant for primary safety ratings, the highest urgency tier in the badge hierarchy. Both use 2px radius and 10px uppercase letterform for maximum density on crowded product cards where three or four ratings may stack. **`in-stock-badge`** — Green (#22c55e) variant signals inventory availability using the same compact chip format.

### Hero Banner

**`hero-banner`** — Near-black canvas with a full-bleed worker photography background, darkened by a scrim. The headline runs at `display-xl` in white; a crimson CTA button sits below it, reproducing `button-primary` against a dark ground for maximum contrast. Padding of `{spacing.xxl}` top and bottom keeps copy above the fold on desktop without crowding navigation.

### Promotional Bar

**`promo-bar`** — Full-width crimson bar, 36px tall, centered `caption-bold` white text. Carries flash sale countdowns, free-shipping thresholds, and seasonal offers. Stacks above `nav-bar-top-utility` during active campaigns, creating a two-tier red header that front-loads urgency before the user reaches category navigation.

### Filter Panel

**`filter-panel`** — Left-column sidebar on desktop, slide-in drawer on mobile. The #f8f8f8 surface with hairline borders keeps the panel visually recessive relative to the product grid. Section headings use `title-sm`; options present as checkboxes with `body-sm` labels. Active filter selections float above the product grid as `category-chip` pills with a crimson-text "Clear All" reset link.

### Section Heading

**`section-heading`** — Ink headline at `display-md` with a 3px crimson bottom border as an accent rule, extending the brand's red-as-signal vocabulary into editorial page structure. Used for category landing headers, homepage promotional modules, and content page dividers.

### Footer

**`footer`** — Near-black (#181818) ground, white `title-sm` column headings, muted gray (#d0d0d0) link text. Four-column layout on desktop: Products, Industries Served, Resources, Company. The tagline "We Protect People" and the logo anchor the bottom row. Social icons from the icomoon set appear in muted gray, matching the low-urgency link treatment.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter panel converts to a bottom drawer triggered by a "Filter" button above the grid; nav collapses to hamburger; search bar moves to a full-width row below the logo; promo bar wraps to two lines if text is long |
| Tablet | 744–1128px | 2-column product grid; filter panel shows as a collapsible left sidebar; nav displays top-level categories only with no mega-menu hover; hero text scales to `display-md` |
| Desktop | 1128–1440px | 3–4 column product grid; mega-menu drops on hover; `search-bar` embedded inline in `nav-bar`; filter panel always visible at ~240px fixed width |
| Wide | > 1440px | Max content width ~1440px centered with edge-to-edge hero photography; product grid expands to 4–5 columns; nav content constrained inside max-width wrapper |

### Touch Targets

- All buttons minimum 44px tall
- Checkbox and radio filter options minimum 44px tap zone with padded label regions
- Mobile nav links minimum 48px tall with hairline separators between items
- "Add to Cart" CTA pinned to bottom of viewport on mobile product detail pages
- Badge and chip elements are display-only; interactive equivalents (filter chips) maintain 36px minimum height

### Collapsing Strategy

- Primary nav condenses to: logo left, search icon center, hamburger right on mobile
- Mega-menu becomes an accordion within the hamburger drawer, preserving category hierarchy
- Filter panel converts from persistent sidebar to a full-height slide-in drawer
- Compliance badge rows wrap to a 2-column grid on narrow product cards rather than overflowing
- Footer collapses from 4 columns to a single accordion-style stack with expand/collapse per section
- `nav-bar-top-utility` and `promo-bar` stack vertically on mobile; one may be hidden if both are active

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed brand typeface — the site relies entirely on OS system fonts (Liberation Sans, Segoe UI, -apple-system); no web font loaded during extraction
- Exact border-radius values unconfirmed; xs (2px) and sm (4px) are inferred from the industrial utility aesthetic rather than measured
- Hover and focus state colors not captured in extraction; accent blues (#5eb0ef, #0091ff) are inferred as focus ring and link colors from the extracted palette but not confirmed in component context
- Precise nav bar height (56px estimated) and mega-menu column layout not directly measured
- Animation and transition timing values completely absent from extraction
- Mobile drawer open/close behavior and overlay scrim color not confirmed
- Product card hover micro-interactions (shadow lift, quick-add button reveal) not captured
- Exact footer column structure and full social icon set not confirmed
- Form validation error and success color tokens not extracted beyond the primary crimson; green in-stock badge color (#22c55e) is inferred from common e-commerce convention, not extracted
