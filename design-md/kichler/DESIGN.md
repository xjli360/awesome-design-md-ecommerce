---
version: alpha
name: "Kichler"
source_url: "https://www.kichler.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Warm brass against a field of near-white grays — Kichler's signature gold (#c9a861) doesn't merely accent the interface; it mirrors the physical finishes on their outdoor wall lanterns, pendant housings, and landscape spotlights. The extraction surface confirms what the product catalog implies: every canvas is a neutral stage (#f6f6f6, #f2f2f2) designed to make photographed fixtures read as they would on a job-site sample board. Color enters the system in two temperature registers. On the cool axis, a steel-blue mist (#96aeb7) and a faint sky wash (#eff9ff) carry informational callouts and collection-family headers; on the warm axis, the gold (#c9a861) drives active states, badge accents, and footer border-top strokes that tie the page closed. A high-saturation utility blue (#34a0e4) handles links and secondary CTAs — kept distinct from the gold so neither color cannibalizes the other. Flat dark near-black (#2d2d2d) grounds headings and the utility nav bar, echoing the matte-black and olde-bronze finishes in the product line.

  Public Sans — a U.S. government-commissioned grotesque with wide apertures and neutral counters — does all the type work. It carries institutional authority without stiffness, which suits a brand that simultaneously sells a $45 pathway light and a $4,000 chandelier collection. Display headings run at 700 weight; body copy settles at 400 with a 1.6 line-height, trusting the font's generous letterspacing over artificially forced tracking. Button labels use 600 weight at 15px with a trace of positive letter-spacing (0.25px) to survive small viewport rendering.

  Corner radii stay deliberately restrained: {rounded.xs} at 4px for buttons, inputs, and product cards; {rounded.sm} at 8px for overlapping drawer panels and dropdown menus; {rounded.full} only for finish swatches and icon-button avatars. No pill-shaped CTAs appear anywhere — the geometry reads as precise and specification-grade, appropriate for a brand that publishes IES photometric files alongside lifestyle photography. Spacing scales generously: {spacing.section} (64px) separates product families on category pages; product cards use {spacing.base} internal padding so thumbnail imagery breathes without crowding wattage and lumens spec labels. Error states deploy #e40303 sparingly — out-of-stock SKU indicators and required configurator fields — never as decoration.

colors:
  primary: "#c9a861"
  primary-active: "#b8923d"
  primary-disabled: "#e8d4a8"
  secondary: "#34a0e4"
  secondary-active: "#1d88cc"
  error: "#e40303"
  ink: "#2d2d2d"
  body: "#424242"
  muted: "#68696d"
  muted-soft: "#979797"
  hairline: "#d8d8d8"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-mid: "#f2f2f2"
  surface-card: "#ffffff"
  steel-blue: "#96aeb7"
  sky-tint: "#eff9ff"
  on-primary: "#2d2d2d"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Public Sans', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  label-sm:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Public Sans', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
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
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.secondary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.secondary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
    activeLinkIndicator: "2px solid {colors.primary}"
  utility-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    linkHoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    hoverElevation: "0 4px 16px rgba(0,0,0,0.10)"
    hoverBorderColor: "{colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlayColor: "rgba(45,45,45,0.55)"
    ctaStyle: "button-primary"
    paddingVertical: "{spacing.section}"
    minHeight: 560px
    rounded: "{rounded.none}"
  category-nav-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  finish-swatch:
    size: 36px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
    activeOffset: "2px solid {colors.canvas}"
    tooltipTypography: "{typography.caption}"
  product-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-dark}"
  product-badge-exclusive:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.secondary}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.muted}"
    dropdownBg: "{colors.canvas}"
    dropdownBorder: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rowAltBackgroundColor: "{colors.surface-soft}"
  info-callout:
    backgroundColor: "{colors.sky-tint}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    hoverColor: "{colors.secondary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
    copyrightTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Gold (#c9a861) fill with dark ink text ({colors.on-primary}: #2d2d2d), 48px tall, 4px radius ({rounded.xs}), 600-weight Public Sans at 15px. The dark-on-gold combination reads as a premium hardware finish rather than a standard CTA. Active state darkens to #b8923d; disabled state washes to #e8d4a8 with muted-soft text. Use for primary catalog actions: "Add to Cart," "Find a Dealer," "Download Spec Sheet."

**`button-secondary`** — Transparent fill, ink border (1.5px solid #2d2d2d), same 48px height as primary so paired CTAs align optically. Active state picks up a surface-soft (#f6f6f6) background fill. Use for secondary actions adjacent to a primary gold button: "Save to Project," "Compare," "View All."

**`button-ghost`** — No border, no background. Secondary-blue (#34a0e4) text, 15px/600 weight. Reserved for in-content text links and "Learn More" nudges inside collection banners where a full button border would feel heavy.

### Inputs & Search

**`text-input`** — White canvas, 1px hairline border (#d8d8d8), 4px radius, 48px height. Focus ring shifts to a 1.5px secondary-blue (#34a0e4) outline, making focused state unambiguous without using gold (which belongs to primary CTAs). Placeholder runs muted-soft (#979797).

**`search-bar`** — Slightly shorter at 44px to sit comfortably inside the nav header row. Same border and focus treatment as text-input. Trailing search icon runs in {colors.muted} (#68696d). Dropdown suggestion panel uses canvas background with a hairline border, no rounded corners, so it reads as a flat tray extending from the input.

### Navigation

**`nav-bar`** — Canvas background, 72px tall, 1px hairline bottom border. Public Sans 15px/500 weight nav-links. Active category indicated by a 2px solid gold bottom-border on the link item rather than a background chip — keeps the bar airy. Logo area reserves 36px height.

**`utility-nav`** — Ink (#2d2d2d) background bar sitting above the main nav, 36px tall. Caption-scale Public Sans in on-dark white. Carries "Find a Showroom," account, and regional selectors. Link hover shifts to {colors.primary} gold. Contrast against dark background lets it read as a separate tier from the shopping nav.

**`breadcrumb`** — Caption-scale (13px/400), muted gray (#68696d) links with hairline-colored separators. Active (current page) steps up to ink. Link hover shifts to secondary blue. Keeps hierarchy legible without occupying visual weight from the product headline above.

### Product Cards

**`product-card`** — White card on surface-soft page ground, 1px hairline-soft border ({colors.hairline-soft}: #e5e5e5), 4px radius. Product image renders on a surface-soft (#f6f6f6) swatch background so chrome, black, and nickel finishes read cleanly. Title in title-sm (16px/600), price in price-display (22px/700). On hover, border darkens to hairline (#d8d8d8) and a soft shadow drops in (0 4px 16px rgba(0,0,0,0.10)). Badges overlay the image top-left corner.

**`finish-swatch`** — 36px circle, full radius, 2px solid hairline border at rest. Selected state gains a 2px solid gold border with a 2px canvas offset ring between swatch and border, giving a halo effect that reads clearly across dark and light finishes. Tooltip on hover uses caption typography.

**`product-badge-new`** — Gold fill, on-primary dark text, 11px uppercase badge typography, 4px radius, 3px 8px padding. Stacks at top-left of product card image.

**`product-badge-sale`** — Error red (#e40303) fill, white text. Same size spec as badge-new.

**`product-badge-exclusive`** — Ink fill (#2d2d2d), white text. Used for "Kichler Exclusive" SKUs.

### Hero & Banners

**`hero-banner`** — Full-bleed dark panel. Photography sits behind a 55% ink scrim so display-xl white headlines remain legible across bright exterior photography. Primary CTA uses button-primary (gold). Vertical padding is {spacing.section} (64px) top and bottom; minimum height 560px on desktop. No border radius — bleeds to viewport edges.

**`collection-banner`** — Surface-soft (#f6f6f6) background, left-rail 4px gold border accent, display-sm heading, body-md copy. Used for seasonal collections and style-family features (e.g., "Transitional," "Farmhouse"). No radius; grid-contained rather than full-bleed.

**`category-nav-chip`** — Filter chips in a horizontally scrolling row below the main nav on category pages. Rest state: surface-soft background, body-colored label-sm text, hairline border. Active state: gold fill with on-primary dark text, matching gold border. Switching chips triggers the product grid filter.

### Utility & Data

**`spec-table`** — Two-column definition layout for lumens, wattage, bulb type, IP rating, and certifications. Header row uses surface-soft background with label-sm uppercase keys in muted (#68696d). Value rows alternate between canvas and surface-soft. Text in body-sm. Border rows use hairline color.

**`info-callout`** — Sky-tint (#eff9ff) background with a 4px secondary-blue left border. Body-sm Public Sans. Used for "This product requires a neutral wire" notices, code-compliance notes, and installation advisories. Subtle and readable without the alarm of the error red.

**`footer`** — Ink (#2d2d2d) background, 3px solid gold top border that ties back to the primary brand color. Column headings in title-sm white. Links in body-sm at hairline (#d8d8d8) lightness, brightening to primary gold on hover. Copyright row in caption. The gold top stroke is the strongest brand-recall element at page close.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Utility nav collapses to icon-only row; main nav replaced by hamburger drawer; hero min-height drops to 320px; product grid goes 2-col; spec-table stacks key-value vertically; category-nav-chips scroll horizontally with fade mask; footer columns stack single-column |
| Tablet | 744–1128px | Utility nav shows abbreviated labels; main nav shows top-level categories only, sub-menus in flyout; product grid is 3-col; hero display-xl steps down to display-md (32px); collection-banner switches to side-by-side text + image |
| Desktop | 1128–1440px | Full utility nav + main nav; product grid 4-col; hero at full display-xl 48px; spec-table two-column definition list; footer 4-column layout |
| Wide | > 1440px | Max-width container caps at 1440px centered; hero photography expands to fill but text column stays constrained to 680px; product grid stays 4-col with increased card padding |

### Touch Targets

- All buttons minimum 48px tall; icon-only buttons minimum 44×44px tap area
- Finish swatches (36px visual) padded to 44px hit area via invisible margin
- Nav-bar links minimum 44px height even at 15px font size
- Category-nav-chips minimum 40px tall on mobile

### Collapsing Strategy

- Main nav mega-menu collapses to a full-screen drawer at < 744px; drawer enters from the left with an ink overlay on content
- Utility nav compresses to account icon + phone icon only below 744px
- Search bar moves from nav-bar inline position to full-width row below nav on mobile
- Horizontal chip rails (category-nav, finish swatches) scroll natively with overflow-x: auto; right-edge fade mask (canvas-to-transparent gradient) signals continued content
- Hero CTA pair (primary + secondary) stacks vertically on mobile, full-width buttons

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; browser chrome color on mobile is unknown — defaulted to canvas white assumption
- Custom icon system (product-family glyphs, finish icons, certifications) not extracted; iconography style and stroke weight unconfirmed
- Exact nav mega-menu structure and depth (2-level vs. 3-level) not determined from extraction
- Hover and transition timing/easing curves not captured; defaults used throughout
- Dark-mode support not confirmed; palette assumes light-only
- Exact product-card image aspect ratio (appears to be 4:3 or 1:1) not confirmed
- Whether #34a0e4 is a brand-defined blue or a framework default could not be confirmed; treated as intentional given its distinctiveness relative to the gray neutrals
- Elevation/shadow tokens beyond the product-card hover state not observed; shadow system may be more elaborate in the live filtering and modal layers
