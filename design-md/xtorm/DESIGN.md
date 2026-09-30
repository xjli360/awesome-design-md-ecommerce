---
version: alpha
name: "Xtorm"
source_url: "https://www.xtorm.eu"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep teal (#108474) pulses through Xtorm's interface like a charged battery indicator — every primary button, active link, and category badge carries this single saturated hue against acres of neutral gray canvas. The palette is deliberately industrial: a near-black ink (#191d21), mid-weight body text in #555555, and a cool #eeeeee surface system that reads like brushed aluminum casing. Orange (#f28c00) fires only at urgency moments — sale badges, low-stock warnings, solar-output indicators — creating a two-signal vocabulary where teal means "go" and amber means "notice." Typography pairs Maven Pro for headlines (geometric, rounded terminals that echo USB-C port silhouettes) with Nunito Sans at 400/600 weights for body and UI chrome; both are sans-serifs tuned for small mobile screens where wattage specs and mAh figures must scan instantly. Cards sit on #ffffff surfaces lifted from a #f9fafb canvas with subtle #e2e2e2 hairlines — no heavy shadows, no glassmorphism, just clean separation. Corner radii stay tight: product cards at `{rounded.sm}`, buttons at `{rounded.xs}`, chips and badges nudged to `{rounded.full}` pill shapes for capacity tags like "20000 mAh" or "45W PD." The nav bar is a slim 64px strip with a dark #2b2f3d mega-menu dropdown housing product category icons. Grid gutters tighten aggressively on mobile where three-across product tiles pack maximum information density — image, wattage badge, price, and stock indicator in under 200px width. A secondary lavender (#a89cc8) appears exclusively on the Fuel Series product line, while light teal (#c1e6e6) backgrounds feature-comparison tables, giving each product family a chromatic identity without fragmenting the core teal+neutral system.

colors:
  primary: "#108474"
  primary-active: "#0c6a5d"
  primary-disabled: "#c1e6e6"
  accent: "#f28c00"
  accent-active: "#d87a00"
  accent-soft: "#fbcd0a"
  series-lavender: "#a89cc8"
  surface-teal: "#c1e6e6"
  ink: "#191d21"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  border-strong: "#bbbbbb"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-strong: "#efefef"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#ef0000"
  error-soft: "#ffdede"
  nav-dark: "#2b2f3d"
  dark-muted: "#686363"
  scrim: "#191d21"

typography:
  display-xl:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  mega-menu-heading:
    fontFamily: "'Maven Pro', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
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
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  mega-menu:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mega-menu-heading}"
    padding: "{spacing.xl} {spacing.xxl}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.primary}
    imageRatio: 1:1
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  wattage-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  capacity-chip:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
    ctaStyle: button-primary
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headerTypography: "{typography.caption}"
    valueTypography: "{typography.spec-value}"
    rounded: "{rounded.sm}"
    cellPadding: "{spacing.md} {spacing.base}"
    rowBorder: 1px solid {colors.hairline-soft}
  comparison-table:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-icon-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    iconSize: 40px
    hoverBackground: "{colors.surface-teal}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  stock-indicator:
    inStockColor: "{colors.primary}"
    lowStockColor: "{colors.accent}"
    outOfStockColor: "{colors.error}"
    typography: "{typography.caption}"

---

## Components

### Buttons

**`button-primary`** — Solid teal (#108474) fill with white text, tight 4px radius, and 700-weight Nunito Sans at 15px. On hover the background deepens to `primary-active` (#0c6a5d) with no transition on border-radius. Disabled state flips to the pale teal `primary-disabled` (#c1e6e6) with muted gray text, signaling unavailability without losing brand hue.

**`button-secondary`** — White fill with a 2px solid ink border, matching the primary's 44px height and 4px radius. On hover/active the button inverts fully: ink background, white text. Used for "Add to Compare" and filter toggles where the action is secondary to the purchase flow.

**`button-accent`** — Orange (#f28c00) fill reserved exclusively for urgency CTAs: flash-sale "Shop Now," limited-edition launches, and solar-promotion banners. Same dimensions as primary but psychologically hotter.

### Navigation

**`nav-bar`** — A 64px white strip pinned to viewport top, separated from content by a single `hairline` border. Logo left-aligned, category links center-set in `nav-link` weight 600, cart/search icons right-aligned. Scrolling past 100px adds a subtle box-shadow (0 2px 8px rgba(0,0,0,0.06)).

**`mega-menu`** — Drops from the nav on category hover as a full-width panel in `nav-dark` (#2b2f3d). Product families are organized in columns with uppercase headings (`mega-menu-heading`) and thumbnail grids below. Transition: opacity 200ms ease, translateY(-4px → 0).

### Product Cards

**`product-card`** — Square image container (1:1 ratio) on a white surface with soft hairline border. On hover the border color transitions to `primary` teal over 150ms. Below the image: product title in `title-sm`, capacity chip (pill-shaped, teal tint background), price in bold `spec-value`, and a wattage badge floated top-right over the image.

**`wattage-badge`** — Pill-shaped indicator overlaid on product images showing output wattage (e.g., "100W"). Teal background, white uppercase text at 11px. Positioned 8px from top-right corner of the image container.

**`sale-badge`** — Identical shape to wattage badge but in accent orange. Shows percentage discount. Positioned top-left to avoid collision with wattage badge.

**`capacity-chip`** — Inline pill below product title showing battery capacity (e.g., "20000 mAh"). Light teal background (#c1e6e6), darker teal text, 12px font at 600 weight.

### Hero & Banners

**`hero-banner`** — Full-width dark (#191d21) panel with a product lifestyle image as background (50% opacity overlay). Headline in `display-xl` Maven Pro white, subhead in `body-md`, and a primary CTA button. Minimum height 480px, content vertically centered with max-width 600px for text block.

**`announcement-bar`** — 36px teal strip above the nav bar cycling through promotional messages (free shipping thresholds, new product launches). White text in `caption` style, auto-rotating every 5 seconds with a crossfade.

### Specifications & Comparison

**`spec-table`** — Alternating-row layout on `surface-soft` background. Header column in `caption` uppercase, value column in `spec-value` bold. Rows separated by `hairline-soft` borders. Used on PDP pages below the fold.

**`comparison-table`** — Light teal (#c1e6e6) background panel with 12px radius, housing side-by-side product columns. Column headers use `title-sm`, cell values use `spec-value`. Check/cross icons in primary/error colors for feature presence.

### Search

**`search-bar`** — Pill-shaped input (9999px radius) with `surface-soft` gray fill. Search icon left-inset in `muted` gray, placeholder text in `body-sm`. On focus the border appears in `primary` teal and background shifts to white.

### Footer

**`footer`** — Dark ink (#191d21) background spanning full width. Four-column grid of link lists (Products, Support, Company, Legal) in `body-sm` with `hairline-soft` colored links. Bottom row contains payment icons, social links, and copyright. Internal padding uses `section` vertical and `xxl` horizontal spacing.

### Utility

**`stock-indicator`** — Inline colored dot + text beside price: green-teal for in stock, orange for low stock ("Only 3 left"), red for out of stock. Dot is 8px circle, text in `caption` style.

**`category-icon-tile`** — Square tile with centered 40px category icon (line-art style) and caption text below. `surface-soft` background, `sm` radius. On hover background transitions to `surface-teal` over 150ms, giving a branded highlight effect.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up tiles), hamburger replaces nav links, mega-menu becomes full-screen slide-over, hero height drops to 320px, search bar moves into expandable icon, announcement bar text truncates to single message |
| Tablet | 744–1128px | Three-column product grid, nav links visible but condensed, mega-menu drops to 2-column layout, hero maintains 400px height, spec table scrolls horizontally if needed |
| Desktop | 1128–1440px | Four-column product grid, full mega-menu with thumbnails, hero at 480px, comparison table shows up to 4 products side-by-side, footer expands to 4-column link grid |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid holds 4 columns with increased gutter, hero image gains additional bleed, lateral padding increases to 80px |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile
- Product card tap zone covers the full card surface, not just the title link
- Mega-menu items have 48px row height on touch devices
- Close/dismiss buttons are 44px circles with generous hit-state padding
- Capacity chips and badges are non-interactive on mobile (no tap action)

### Collapsing Strategy

- Nav links collapse into a hamburger icon at < 744px; slide-out drawer opens from left with full category tree
- Spec tables switch to a stacked key-value list on mobile, removing the table layout
- Comparison table limits to 2 products on mobile with horizontal swipe pagination
- Footer columns stack vertically as accordions on mobile, each section header tappable to expand
- Hero text block shifts from centered overlay to below-image layout on mobile for readability
- Filter sidebar becomes a bottom-sheet modal on mobile triggered by a sticky "Filter" button

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact transition/animation durations and easing curves not extractable from static analysis
- Icon system details unclear — appears to use a mix of Line Awesome and custom SVG sprites; specific icon set and sizing rules could not be confirmed
- No custom web font loading strategy visible (Maven Pro and Nunito Sans likely loaded via Google Fonts but `font-display` strategy not confirmed)
- Product image hover behavior (zoom, swap, carousel) not determinable from color/font extraction alone
- Exact box-shadow values on cards and elevated elements not captured in hex extraction
- The lavender (#a89cc8) and light-blue (#4fc3f7) colors appear in limited contexts (possibly product-line-specific); their full usage rules are unclear
- Mobile menu animation direction and overlay treatment not confirmed
- Review/rating star styling (JudgemeStar font) integration details not extracted
