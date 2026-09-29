---
version: alpha
name: "Lian Li"
source_url: "https://lian-li.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The #17bbef cyan that indexes every hover underline, active nav indicator, and product-badge accent reads less like a brand color and more like a strip of addressable RGB caught mid-animation — precision-lit, technically deliberate. Lian Li's web presence mirrors its hardware philosophy: a neutral shell of surface-soft (#ecf0f5) panels and body-gray (#444444) copy gives product imagery — brushed aluminum extrusions, tempered glass side panels, dense cable-management ecosystems — the visual real estate to do the work. Montserrat carries every headline at weight 700, the same geometric confidence you find in a machined I/O shield; Roboto handles body copy at 400 weight, never competing. Outside that primary cyan, the palette is restrained: deep navy #003388 anchors secondary CTAs and structural nav links, while a graduated gray stack (#bfc3c8, #98a2b3, #667085) manages borders, metadata text, and dividers — the digital analogue of an anodized aluminum grille. Error states pull from #b94a48; utility badge states borrow orange (#ff6900) and amber (#f0ad4e) signals drawn from the PC-enthusiast vocabulary where every indicator color codes a function. The site is a light-mode system rather than a dark gaming theme, positioning Lian Li above the RGB-maximalist tier and into the architectural, premium-builder segment — a signal reinforced by `{rounded.xs}` (4px) button corners and `{rounded.sm}` (8px) card radii that echo the right-angle chassis geometry of the O11 Dynamic series. Specification tables, checkbox-tree filter sidebars, and dense multi-level category navigation are first-class UI patterns here because Lian Li's buyers cross-reference TDP clearances and PSU shroud dimensions before committing — the design system must support that homework, not fight it.

colors:
  primary: "#17bbef"
  primary-active: "#0ea5d4"
  primary-disabled: "#a8e4f7"
  secondary: "#003388"
  secondary-active: "#002266"
  ink: "#32373c"
  body: "#444444"
  muted: "#667085"
  muted-soft: "#98a2b3"
  hairline: "#dcdee2"
  hairline-soft: "#eaecf0"
  canvas: "#ffffff"
  surface-soft: "#ecf0f5"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#b94a48"
  error-dark: "#cf2e2e"
  warning: "#f0ad4e"
  accent-orange: "#ff6900"
  accent-amber: "#fcb900"
  dark-panel: "#353535"
  dark-ink: "#3f4b5b"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', 'Roboto', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Roboto', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAccentColor: "{colors.primary}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
    megaMenuBackground: "{colors.canvas}"
    megaMenuBorderTop: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    imageBackground: "{colors.surface-soft}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    badgeOffset: "{spacing.sm}"
    padding: "{spacing.base}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 4px 16px rgba(23,187,239,0.15)"
  hero-banner:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlayGradient: "linear-gradient(90deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 100%)"
    accentColor: "{colors.primary}"
    minHeight: 540px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.body}"
    borderColor: "{colors.hairline-soft}"
    alternateRowBackground: "{colors.surface-soft}"
    labelWidth: 200px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-featured:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-rgb:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    iconColor: "{colors.muted}"
    height: 40px
    focusBorderColor: "{colors.primary}"
    padding: 8px 16px 8px 40px
  category-pill-default:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkHoverColor: "{colors.primary}"
  price-tag-regular:
    typography: "{typography.price-display}"
    color: "{colors.ink}"
  price-tag-sale:
    typography: "{typography.price-display}"
    color: "{colors.error}"
  price-tag-original:
    typography: "{typography.price-sm}"
    color: "{colors.muted}"
    textDecoration: line-through
  footer:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
  pagination:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    defaultBackground: "{colors.canvas}"
    defaultTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px

## Components

### Buttons

**`button-primary`** — Cyan (#17bbef) fill with white uppercase Montserrat label at 14px/700, 4px corners, 44px tall. Hover and active states shift to `{colors.primary-active}` (#0ea5d4); disabled drains to the pale `{colors.primary-disabled}` wash while preserving the uppercase label for readability. Used for primary purchase CTAs ("Add to Cart", "Buy Now") and prominent section CTAs throughout the product catalog.

**`button-secondary`** — Deep navy (#003388) fill with white uppercase Montserrat label. Shares the same 4px corner and 44px height geometry as the primary. Appears as an alternative action (Compare, Find a Retailer, Register Product) where the primary cyan is already occupied. Hover darkens to `{colors.secondary-active}` (#002266).

**`button-ghost`** — Transparent body with a 1.5px cyan border and cyan label. On hover the fill converts to full primary cyan and the text flips to white — a two-state transition that reads as decisive without requiring a separate active surface. Common in hero banner secondary CTA slots and modal footers where a filled button already anchors the primary action.

### Text Inputs

**`text-input`** — White canvas with a 1px `{colors.hairline}` border and 4px corners at 40px height. Focus upgrades the border to primary cyan with no shadow, preserving the clean geometry. Placeholder text in `{colors.muted}`. Used for search fields, newsletter signup, and checkout forms throughout.

### Navigation

**`nav-bar`** — White canvas at 64px height with a 1px hairline bottom border. The Lian Li logo wordmark uses the primary cyan as its accent. Active category links render a 2px cyan underline indicator rather than a background fill, keeping a dense multi-level hierarchy (Cases, Cooling, Fans, Accessories, Software, Where to Buy) legible without visual noise. Mega-menus drop below the nav with a 2px primary cyan top border anchoring them to the trigger. Cart and account icons sit flush right.

### Product Cards

**`product-card`** — White canvas body with 1px hairline border and 8px corners. The image area is set against `{colors.surface-soft}` (#ecf0f5) so product shots with transparent backgrounds read cleanly. On hover, the border upgrades to primary cyan and a tinted drop shadow (`rgba(23,187,239,0.15)`) lifts the card — the product subtly illuminates as if backlit. Price renders in `{typography.price-sm}` Montserrat at `{colors.ink}`; badges pin to the top-left corner at `{spacing.sm}` offset from the edge.

### Hero Banner

**`hero-banner`** — Dark panel (#353535) base with a left-anchored gradient overlay fading from 70% black to transparent, letting product photography fill the right two-thirds of the frame. Heading uses `{typography.display-xl}` in white; body copy uses `{typography.body-md}`. A primary cyan accent — either a ruled line above the heading or the CTA button — marks the entry point. Minimum 540px height to give full tower-case photography room to read. The overlay gradient approach avoids cropping issues when hero imagery changes across product launches.

### Specification Table

**`spec-table`** — The specification table is a first-class content pattern for Lian Li, given equal visual weight to the product image carousel. Header cells use `{colors.surface-soft}` with `{typography.spec-label}` in `{colors.muted}`. Value rows alternate between white and surface-soft for scannability. The spec label column is fixed at 200px to align long technical strings (Maximum GPU Length, Radiator Support, Drive Bays). All borders use `{colors.hairline-soft}`. No border-radius — the table reads as a precise data instrument.

### Product Badges

**`product-badge-new`** — Cyan primary fill, signals new SKUs entering the catalog. **`product-badge-sale`** — Error red (#b94a48), used for discounted pricing. **`product-badge-featured`** — Navy secondary, used for editor-featured or award-winning products. **`product-badge-rgb`** — Accent orange (#ff6900), signals RGB/addressable lighting compatibility. All four variants share uppercase `{typography.badge}` at 11px/700, 4px corners, 3×8px padding. The four-color badge vocabulary maps directly to the signal language PC builders already use from motherboard manual LEDs — error red, status blue, amber warning, and activity cyan.

### Search Bar

**`search-bar`** — Surface-soft (#ecf0f5) background with a left-side search icon in `{colors.muted}`, 40px height, 4px corners. On focus the border activates to primary cyan. Appears both inline in the top nav and as a full-width element heading the catalog and search-results pages. Placeholder in `{colors.muted}`.

### Category Pills

**`category-pill-default`** / **`category-pill-active`** — Pill-shaped (`{rounded.full}`) filter controls for product-series filtering (O11 Dynamic, LANCOOL, GALAHAD AIO, UNI FAN). Inactive state: surface-soft background with 1px hairline border and body-gray label. Active state: solid primary cyan fill with white label. Uppercase Montserrat 12px/700. Arranged in a horizontal scrolling row on mobile, a wrapping row on desktop.

### Footer

**`footer`** — Dark `{colors.dark-ink}` (#3f4b5b) background anchored by a 2px primary cyan top border that mirrors the mega-menu connection motif. Column headings in white `{typography.title-sm}`; body links in `{colors.muted-soft}` that highlight to primary cyan on hover. A sub-footer strip holds region selector, social links, legal text in `{typography.caption}`, and compliance badges separated from the main columns by a `{colors.hairline}` divider. Padding `{spacing.xxl}` top and bottom.

### Pagination

**`pagination`** — Square-cornered (`{rounded.xs}`) cells at 36×36px. Active page: solid primary cyan fill with white label. Inactive pages: white canvas with hairline border and body-gray label. Previous/Next arrows match the inactive style. Uppercase Montserrat 12px/700 for numerals.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero collapses to 280px tall with stacked CTAs; spec table scrolls horizontally with sticky first column; filter sidebar becomes bottom sheet |
| Tablet | 744–1128px | Two-column product grid; top nav condenses with icon+label treatment; hero at 400px; mega-menu becomes multi-level accordion inside the drawer |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with mega-menu flyout; hero at full 540px; filter sidebar visible as fixed 240px left panel |
| Wide | > 1440px | Centered max-width container (1440px) with symmetric gutters; product grid can expand to five columns; hero image scale-locks to prevent excessive stretch on ultra-wide displays |

### Touch Targets
- All buttons minimum 44×44px; icon-only nav controls padded to 48×48px touch area
- Category pills minimum 36px tall with 8px horizontal gap between pills in scrolling row
- Product card entire surface is tappable on mobile; wishlist and compare actions revealed via a tap-to-reveal overlay icon in the top-right corner
- Pagination controls expand to 44×44px minimum on mobile

### Collapsing Strategy
- Top nav collapses to hamburger below 744px; category hierarchy becomes a multi-level accordion with chevron toggles inside the slide-in drawer
- Filter sidebar collapses to a sticky "Filter & Sort" bottom bar on mobile and tablet; drawer state persists across open/close cycles within the session
- Spec table does not reformat on mobile — horizontal scroll with the spec label column sticky at left is strongly preferred over reflowing to a single-column list, which destroys cross-row comparability
- Product image aspect ratio locks to 1:1 at all breakpoints to prevent layout shift when navigating between SKUs
- Footer four columns collapse to two on tablet, to single accordion-expandable columns on mobile with headings as toggle triggers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) inferred from convention; no explicit white extracted from the site's color list — likely a CSS reset default or framework base
- No dark-mode token variants confirmed; site appears light-mode system-wide, but dark panels (#353535, #3f4b5b) appear in the footer and hero — a full dark-mode surface palette may exist for campaign landing pages
- Exact mega-menu column count, icon illustration style, and hover animation timing not determinable from color/font extraction alone
- Product image carousel behavior (auto-advance interval, indicator pip style, swipe physics) not captured
- Hover/focus transition durations not extracted — 150ms ease-in-out assumed as a safe default
- Exact live border-radius on buttons and cards unconfirmed; 4px and 8px chosen to match the angular chassis geometry aesthetic
- Filter sidebar checkbox and range-slider component styling not captured beyond inferred base tokens
- Mobile breakpoint pixel values are estimated from standard conventions; Lian Li's actual CSS breakpoint declarations were not extracted
