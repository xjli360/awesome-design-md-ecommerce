---
version: alpha
name: "Phanteks"
source_url: "https://www.phanteks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Phanteks runs its entire digital language off a single synthetic frequency: #00ffdd, a saturated cyan that appears at threshold-level brightness against the brand's near-black infrastructure (#212934) and its clean white product pages. This is not a color borrowed from gaming convention — it is pulled directly from the meta theme-color declaration, the earliest signal the browser receives when loading the site. Every CTA, every hover state, every RGB preview widget returns to this wavelength. The dark anchor (#212934, #32373c) reads less like a consumer lifestyle neutral and more like a system interface — the same family of near-black engineers use when they want data to feel authoritative rather than decorative.

  Type splits between Poppins, which handles display hierarchies and navigation, and PT Sans, which carries product descriptions and longer specification copy. Poppins at weight 600–700 gives product headers clean geometric confidence that stops short of aggressive; PT Sans provides slightly warmer contrast in body paragraphs. The monospace stack — Consolas, Menlo, Monaco — surfaces in spec tables and part-number callouts, a typographic signal that this brand is conversant with the people who actually build systems.

  Surfaces are almost entirely white or light gray (#f4f4f4, #fbfbfb), inverting the expectation that a PC hardware brand defaults to a dark canvas. Darkness concentrates in the navigation, footer, and hero overlays, framing products as luminous objects against a workshop surface rather than submerging them in ambient glow. Product cards use hairlines in #d2d2d2 to define geometry without shadow. The #65bc7b green reads as a secondary accent for availability and go states; #e0284f marks alerts, out-of-stock conditions, and sale pricing. Corner radii are minimal — `{rounded.sm}` at most for card borders, `{rounded.xs}` on inputs — signaling precision hardware rather than soft consumer goods. The only soft shape in the system is the badge pill (`{rounded.full}`), which carries stock labels and promotional flags.

colors:
  primary: "#00ffdd"
  primary-active: "#00ccbb"
  primary-disabled: "#555555"
  primary-dark: "#008888"
  primary-deepest: "#003333"
  accent-green: "#65bc7b"
  accent-red: "#e0284f"
  ink: "#212934"
  body: "#32373c"
  muted: "#747474"
  muted-soft: "#aaa9a9"
  hairline: "#d2d2d2"
  hairline-soft: "#eaeaea"
  canvas: "#fbfbfb"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-mid: "#e9eaee"
  surface-dark: "#32373c"
  surface-darkest: "#212934"
  on-primary: "#212934"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'PT Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'PT Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'PT Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  spec-label:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-value:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  part-number:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    border: "1px solid {colors.primary-active}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "2px solid {colors.primary}"
  nav-bar-top:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
    imageBackground: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    overlayOpacity: 0.6
    paddingY: "{spacing.section}"
    accentColor: "{colors.primary}"
    accentRule: "2px solid {colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowBorder: "1px solid {colors.hairline-soft}"
    alternateRowBackground: "{colors.surface-soft}"
    labelColumnWidth: "40%"
  rgb-badge:
    backgroundColor: "transparent"
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  stock-badge-available:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  stock-badge-unavailable:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  stock-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    height: 42px
    expandedWidth: 320px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    backgroundActive: "{colors.surface-darkest}"
    textColorActive: "{colors.primary}"
    borderActive: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  part-number-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.part-number}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  breadcrumb:
    textColor: "{colors.muted}"
    textColorActive: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkColorHover: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — Filled with `{colors.primary}` (#00ffdd) and `{colors.on-primary}` (#212934) text, rendered in uppercase Poppins 600 at 14px with 0.5px letter-spacing. The 2px `{rounded.xs}` radius signals precision hardware; hover transitions to `{colors.primary-active}` (#00ccbb). Disabled state mutes to `{colors.primary-disabled}` (#555555) with `{colors.muted-soft}` text — an "unlit" treatment analogous to an inactive LED channel.

**`button-secondary`** — Transparent background with a 1px `{colors.primary}` border and matching text, same uppercase Poppins typographic treatment as primary. Used for secondary CTAs such as "Add to Compare" or "Download Specs PDF". Hover tightens the border to `{colors.primary-active}`.

**`button-dark`** — `{colors.surface-darkest}` (#212934) fill with `{colors.on-dark}` text; deployed in hero sections and dark-panel contexts where the cyan primary would disappear against an already-light background.

**`button-ghost`** — Text-only, no border, `{colors.body}` color. Appears as tertiary actions within product card footers and filter drawer controls.

### Text Input
**`text-input`** — 42px height on `{colors.canvas}` with `{colors.hairline}` border and a sharp `{rounded.xs}` corner. Focus state transitions the border to `{colors.primary}`, mirroring the button hover system. PT Sans 400 (`{typography.body-md}`) keeps field labels legible without competing with adjacent spec data.

### Navigation
**`nav-bar`** — Two-tier structure: a 36px `{colors.ink}` utility strip (`nav-bar-top`) carrying regional selectors, dealer locator, and support links, above the primary `{colors.surface-darkest}` nav with a 2px `{colors.primary}` bottom border that anchors the cyan system at the page top. Navigation labels in Poppins 500 (`{typography.nav-link}`) in `{colors.on-dark}`; active category items expose dropdown panels with `{colors.surface-card}` backgrounds and `{colors.hairline}` borders.

### Product Card
**`product-card`** — White surface with `{colors.hairline}` border and `{rounded.sm}` corners. Hover promotes the border to `{colors.primary}`, giving interactive feedback without any shadow system. Product image sits in a 1:1 `{colors.canvas}` well. Below the image: model name in `{typography.title-sm}`, part number in `{typography.part-number}` (monospace, uppercase), then a horizontal row of `rgb-badge` and `stock-badge` pills. No drop shadows appear anywhere in the card — all geometry is defined by hairlines alone.

### Hero Banner
**`hero-banner`** — Full-width `{colors.surface-darkest}` with product photography behind a 60% opacity overlay. Display headline in `{typography.display-xl}` (Poppins 700) in `{colors.on-dark}`, sub-headline in `{typography.body-md}` (PT Sans 400). A horizontal 2px `{colors.primary}` rule punctuates the headline block, connecting the hero accent to the nav-bar border and the footer border — three cyan brackets around the page. Primary CTA uses `button-primary`; secondary uses `button-secondary` on a dark field. Vertical padding is `{spacing.section}` (64px).

### Spec Table
**`spec-table`** — Two-column layout with alternating rows between `{colors.canvas}` and `{colors.surface-soft}`, separated by `{colors.hairline-soft}` dividers. Labels in `{typography.spec-label}` (Consolas 12px, `{colors.muted}`); values in `{typography.spec-value}` (Consolas 13px, `{colors.ink}`). The monospace stack signals machine-readable figures rather than marketing copy. Label column is 40% width; value fills the remainder. On mobile the table scrolls horizontally rather than collapsing to stacked rows, preserving the side-by-side label/value relationship.

### Badges
**`rgb-badge`** — Outlined `{rounded.full}` pill in `{colors.primary}` (#00ffdd), 11px Poppins 600 uppercase, 3px/10px padding. Marks products with addressable ARGB/DRGB lighting headers. Distinguished from `stock-badge-new` by its transparent fill.

**`stock-badge-available`** — Solid `{colors.accent-green}` (#65bc7b) pill with `{colors.canvas}` text. Indicates in-stock status on both listing cards and the product detail page header.

**`stock-badge-unavailable`** — Solid `{colors.accent-red}` (#e0284f) pill with `{colors.canvas}` text. Marks out-of-stock or discontinued SKUs; the same red is used for sale price text in product listings.

**`stock-badge-new`** — Solid `{colors.primary}` (#00ffdd) fill with `{colors.on-primary}` text. Marks newly launched products and differentiates from the outlined `rgb-badge` by its filled background.

### Search Bar
**`search-bar`** — `{colors.surface-soft}` fill with a `{colors.muted}` magnifier icon at left. Focus transitions border to `{colors.primary}` and expands width to 320px. In the nav-bar it sits at 42px height inline with nav links. On mobile it collapses to a 44×44px icon touch target that opens a full-width overlay search panel.

### Filter Chip
**`filter-chip`** — Used in product listing sidebars for socket type, form factor, cooling type, and RGB compatibility filters. Default state: `{colors.surface-soft}` background, `{colors.hairline}` border, `{colors.body}` text. Active state inverts to `{colors.surface-darkest}` background with `{colors.primary}` text and border — a direct inversion that reads as a "selected channel" rather than a simple checked state.

### Category Tile
**`category-tile`** — Grid of product category entries (Cases, Coolers, Fans, Memory, Power Supplies). White `{colors.surface-card}` with `{colors.hairline}` border and `{rounded.sm}` corner. On hover the border transitions to `{colors.primary}`. Category name in `{typography.title-sm}`, icon or thumbnail above it. `{spacing.lg}` internal padding on all sides.

### Footer
**`footer`** — `{colors.ink}` (#212934) background with a 2px `{colors.primary}` top border, mirroring the nav-bar's bottom border and closing the page's cyan bracket system. Link labels in `{colors.muted-soft}` transition to `{colors.primary}` on hover. Four-column grid on desktop: Products, Support, Company, Social. Social icons drawn from Font Awesome 5 Free.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-in dark drawer; hero headline drops to `{typography.display-md}`; spec tables scroll horizontally; filter sidebar becomes bottom sheet; `nav-bar-top` utility strip hidden |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with overflow hamburger for subcategories; hero maintains two-column image/text split; filter chips wrap above grid |
| Desktop | 1128–1440px | Three-column product grid; full dual-tier nav with dropdown panels; spec table rendered inline in product detail body; hero full-bleed with overlay text |
| Wide | > 1440px | Max-width container at 1400px centered; four-column product grid on category pages; hero imagery scales to fill; footer grid gains fifth column for newsletter signup |

### Touch Targets
- All buttons and interactive filter chips minimum 44×44px tap area
- Nav links in mobile drawer minimum 48px height
- Badge pills are display-only and exempt from tap-target sizing; interactive filter variants use `{spacing.lg}` vertical padding
- Search icon in collapsed mobile nav: 44×44px hit area
- Part-number-tag is display-only; no tap-target required

### Collapsing Strategy
- Dual-tier nav collapses to single hamburger at < 744px; `nav-bar-top` utility strip hides entirely on mobile
- Product grid collapses 4 → 3 → 2 → 1 column across breakpoints
- Spec tables maintain two-column layout but enable horizontal scroll on mobile; rows do not stack
- Footer four-column grid collapses to two columns at tablet, single column on mobile
- Hero CTA buttons stack vertically on mobile; side-by-side on tablet and above
- Category tile grids collapse from 6-up to 3-up to 2-up

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- RGB lighting preview / ARGB color-picker widget not extractable from static HTML — likely rendered client-side via canvas or WebGL; component structure inferred from product page layout patterns
- Confirmed font weights for Poppins and PT Sans not verifiable at network level; 400/500/600/700 assumed from standard usage
- Price typography treatment (sale price vs. regular vs. MSRP stacked layout) not confirmed — `{colors.accent-red}` for sale price is an inference from the extracted palette
- No modal or overlay dialog component observed in extraction — drawer and bottom-sheet patterns inferred from category and filter structure
- Exact nav breakpoints not confirmed from live site; values above are industry-standard inferences
- Logo lockup dimensions, clearspace rules, and favicon asset format not extractable
- Dropdown mega-menu column count and image treatment within nav panels not confirmed
- Social icon set selection within Font Awesome 5 Free not verified (Twitter/X, YouTube, Instagram, Facebook are typical for this category)
- Pagination vs. infinite-scroll strategy on product listing pages not determinable from extraction
