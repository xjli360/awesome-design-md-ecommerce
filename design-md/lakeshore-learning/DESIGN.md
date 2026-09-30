---
version: alpha
name: "Lakeshore Learning"
source_url: "https://www.lakeshorelearning.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every category landing page signals its subject before a word is read — a manipulative math tile in warm red (#e8392a), a language-arts badge in cobalt blue (#1a6fb8), a science kit ringed in leaf green (#3a9e4d). Lakeshore Learning operates five distinct accent hues as a semantic taxonomy: age-group, subject area, and grade-level are encoded in color rather than left to text labels alone. The primary red carries logo, primary CTA, and sale-badge simultaneously and never appears as decoration. Canvas is hard white with minimal surface tinting; product photography supplies all warmth and visual density, so the grid can run short padding stacks and still read as generous.

  Type is set in a clean geometric sans — widely documented as Proxima Nova or a comparable humanist — at relatively modest weights. Display headings sit around 28–32px in weight 600; product-card titles run 15–16px weight 600 to hold legibility over busy photography thumbnails. Buttons are medium weight (500) at 15px to project authority without aggression. Letter-spacing runs near-zero throughout; the brand doesn't compress tracking to manufacture sophistication. Line-height in body copy is a roomy 1.55, deliberate for a reading audience of time-pressed classroom teachers scanning product specs.

  Corners are gently rounded everywhere — 8px on input fields, 6px on buttons, 12px on product cards, `{rounded.full}` on age-range and grade-level badges. The softness signals child-appropriate goods without sacrificing the grid discipline a professional educator expects. The top navigation holds a mega-menu organized by subject area, each column headed in one of the brand accent colors, functioning as a color-coded curriculum map. Product cards layer a "New" badge in primary red, a subject-area badge in the relevant accent, and a star-rating line — three information layers that stack cleanly because the type scale keeps each element in its lane.

colors:
  primary: "#e8392a"
  primary-active: "#c42e20"
  primary-disabled: "#f5b0aa"
  accent-blue: "#1a6fb8"
  accent-blue-soft: "#d6e9f7"
  accent-green: "#3a9e4d"
  accent-green-soft: "#d3eeda"
  accent-yellow: "#f5c518"
  accent-yellow-soft: "#fef6d0"
  accent-orange: "#f07d2a"
  accent-orange-soft: "#fde8d0"
  accent-purple: "#8b4fc8"
  accent-purple-soft: "#e8d8f7"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-blue: "#ffffff"
  on-accent-green: "#ffffff"
  on-accent-yellow: "#1a1a1a"
  sale-badge: "#e8392a"
  new-badge: "#e8392a"
  star-fill: "#f5c518"
  star-empty: "#dddddd"

typography:
  display-xl:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  mega-menu-heading:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    padding: 12px 24px
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
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.accent-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.mega-menu-heading}"
    borderTop: "2px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  mega-menu-column-heading:
    textColor: "{colors.primary}"
    typography: "{typography.mega-menu-heading}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md}"
    imageRounded: "{rounded.lg}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  subject-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  subject-badge-math:
    backgroundColor: "{colors.accent-orange-soft}"
    textColor: "{colors.accent-orange}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  subject-badge-literacy:
    backgroundColor: "{colors.accent-blue-soft}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  subject-badge-science:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  subject-badge-art:
    backgroundColor: "{colors.accent-purple-soft}"
    textColor: "{colors.accent-purple}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  subject-badge-early-childhood:
    backgroundColor: "{colors.accent-yellow-soft}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  new-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  star-rating:
    starFill: "{colors.star-fill}"
    starEmpty: "{colors.star-empty}"
    typography: "{typography.caption-bold}"
    gap: "{spacing.xs}"
  age-grade-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  search-submit-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 44px
    width: 44px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    minHeight: 400px
  category-grid-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    hoverBackgroundColor: "{colors.surface-card}"
    hoverBorder: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 36px
  pagination:
    activePageBackground: "{colors.primary}"
    activePageColor: "{colors.on-primary}"
    inactivePageColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "#1a1a1a"
    textColor: "#cccccc"
    headingTypography: "{typography.mega-menu-heading}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
  promo-strip:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.caption-bold}"
    height: 36px

## Components

### Buttons

**`button-primary`** — Solid primary-red (#e8392a) fill at 44px height with 6px radius; this is the universal add-to-cart and checkout CTA. Active state darkens to `{colors.primary-active}` (#c42e20); disabled washes to `{colors.primary-disabled}`. The medium font weight (500) at 15px reads as decisive without aggression — appropriate for a parent purchasing on a school-supply deadline with a specific grade-level target.

**`button-secondary`** — White canvas with a 1.5px primary-red border and primary-red text, identical radius and height to the primary. Used for "Save to List," "Compare," and secondary page actions. Active state tints the canvas to `{colors.surface-soft}` to signal press without losing legibility.

**`button-text-link`** — Transparent background, accent-blue text, no border or height constraint. Used for ancillary actions such as "See all reviews," "View curriculum guide," and breadcrumb secondary calls-to-action. Inherits line context; no padding.

### Search

**`search-bar`** — Full-pill radius (`{rounded.full}`) with a 1.5px hairline border that sharpens to primary-red on focus. The submit button (`search-submit-button`) is a circular red orb anchored to the right end of the field at 44×44px. At mobile width, the search bar collapses to an icon trigger in the nav-bar; tapping opens a full-width input panel overlaid above the page.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline border-bottom. A `nav-bar-top-strip` in primary red (or `{colors.accent-blue}` during promotional periods) sits above it at 36px, carrying centered caption-bold copy for free-shipping thresholds and discount codes. The bar holds the logo left, search center, and cart/account icons right. Below: a horizontal subject-category row where each label links to a subject mega-menu.

**`mega-menu`** — Full-width dropdown with a 2px primary-red top border and a deep box-shadow (0 8px 24px). Columns are headed in `{typography.mega-menu-heading}` with text colored per subject: math in `{colors.accent-orange}`, literacy in `{colors.accent-blue}`, science in `{colors.accent-green}`. Each column lists sub-category links in `{typography.body-sm}`. The mega-menu is the primary wayfinding surface for teacher-shoppers who arrive knowing their subject area.

### Product Cards

**`product-card`** — White surface card with 12px radius, a 1px hairline-soft border, and a hover box-shadow lift. The image occupies roughly 65% of card height at matching 12px radius. Below: a row of subject and age/grade tags, then the product title in `{typography.title-sm}` weight 600, a star-rating row, and a price in `{typography.price}`. "New" and "Sale" badges overlay the image top-left and top-right respectively at full-pill radius. Grid is 4 columns on desktop, 2 on mobile.

**`subject-badge`** — Full-pill badges encoding subject category using a five-color semantic system: math uses `{colors.accent-orange-soft}` / `{colors.accent-orange}`, literacy uses `{colors.accent-blue-soft}` / `{colors.accent-blue}`, science uses `{colors.accent-green-soft}` / `{colors.accent-green}`, art uses `{colors.accent-purple-soft}` / `{colors.accent-purple}`, early-childhood uses `{colors.accent-yellow-soft}` / `{colors.on-accent-yellow}`. These badges do the subject-taxonomy work that a filter panel would otherwise obscure behind a click.

**`age-grade-tag`** — Muted surface-soft chip at xs radius (4px) in caption typography. Carries "Ages 3–5" or "Grades K–2" strings beneath the subject badge row. Provides the developmental-stage filtering axis without competing with the color-coded subject badge for visual priority.

### Badges

**`new-badge`** — 11px bold uppercase in primary-red fill, full-pill, overlays top-left corner of the product image. Indicates items added within the current catalog season.

**`sale-badge`** — Identical geometry and fill to `new-badge`, positioned at top-right. Carries a percentage-off string. Using the same primary-red for both badges keeps the badge vocabulary minimal; positional convention disambiguates the two at a glance.

### Hero Banner

**`hero-banner`** — Full-width panel, minimum 400px tall, with `{colors.surface-soft}` background and a headline in `{typography.display-lg}`. A button-primary CTA sits below the headline copy. Product photography is right-anchored on desktop, stacked above copy on mobile. Seasonal heroes for back-to-school or holiday campaigns swap the background to a solid `{colors.accent-blue}` or `{colors.accent-green}` band, keeping the photography dominant while signaling campaign context.

### Category Grid

**`category-grid-tile`** — Near-square tiles on `{colors.surface-soft}` at 12px radius, carrying an icon or cropped product photo plus a short title in `{typography.title-sm}`. Used on the homepage to surface the top-level subject taxonomy in a single scan. Hover brightens the background to canvas and adds a `{colors.hairline}` border. Grid is 5–6 tiles wide on desktop, 2 tiles wide on mobile.

### Filters

**`filter-chip`** — Full-pill chips in a horizontal scroll row above the product grid. Default: white canvas with `{colors.hairline}` border. Active: primary-red fill with `{colors.on-primary}` text. Tapping a chip filters the grid in-page; on mobile the chip row scrolls horizontally at 36px height to maintain a 44px touch affordance with surrounding padding.

### Footer

**`footer`** — Near-black (#1a1a1a) background with a 3px primary-red top border and muted link text (#cccccc). Column headers in `{typography.mega-menu-heading}` replicate the mega-menu subject taxonomy, making the footer a persistent secondary nav for returning shoppers. The final column carries social icons and the Lakeshore guarantee mark. On mobile, columns collapse to a single-column accordion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; search becomes icon trigger; product grid is 2 columns; hero image stacks above copy; filter chips scroll horizontally; mega-menu becomes full-screen slide-in drawer |
| Tablet | 744–1128px | Nav shows logo + search + cart/account but collapses subject row into a "Shop" dropdown; product grid is 3 columns; hero uses 50/50 split layout |
| Desktop | 1128–1440px | Full nav with subject-category row and mega-menu; 4-column product grid; hero right-anchors photography beside headline |
| Wide | > 1440px | Content max-width caps at ~1400px centered; hero gains lateral whitespace flanking the photography; grid gutters widen |

### Touch Targets

- All buttons and interactive badges maintain minimum 44px height and 44px width
- Filter chips are padded to 44px tap height despite 36px visual height
- Star-rating interactive zones pad to 44px touch area despite 20px star visual height
- Nav icons (cart, account, search trigger) are 44×44px tap areas in the collapsed mobile bar
- Age-grade tags and subject badges used as filter triggers pad to minimum 36px height on mobile

### Collapsing Strategy

- Subject-category nav row collapses first (around 1024px) into a single "Shop by Subject" dropdown before the full hamburger transition
- Mega-menu becomes a full-screen slide-in drawer on mobile, preserving the five-color column-heading taxonomy
- Product card secondary details (age/grade tags) truncate to one tag on the smallest breakpoint and expand on tap
- Hero CTA button runs full width (100%) on mobile; max 280px on tablet and up
- Footer columns stack to 2-column layout on tablet and a single-column accordion (expand/collapse per subject group) on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site (likely JS-loaded design tokens or anti-bot protection); all `colors.*` values in this spec are approximations derived from widely observable brand assets including the logo, catalog imagery, and print materials — treat every hex as provisional and verify against a live DOM inspector or official brand guidelines PDF before shipping
- Font family could not be confirmed via network extraction; Proxima Nova is cited as the most widely documented match for Lakeshore's web typography but has not been verified from an actual font request — could be a licensed equivalent or a clean sans-serif system stack
- No `meta theme-color` was found, so mobile browser chrome tinting color is unknown
- Exact corner radii on buttons, cards, and inputs are estimated from visual inspection; CSS extraction would be needed to confirm
- The five subject-area accent hues and their soft-tint variants are approximations; actual saturation and lightness values used in real tokens could differ meaningfully
- Dark-mode or high-contrast accessibility variant, if one exists, is entirely uncharted
- Animation and transition timings for mega-menu open/close, card hover lift, and filter-chip state transitions were not extractable
- Exact nav-bar height and top-strip height are estimated; the nav structure may include an additional promotional banner row not accounted for here
