---
version: alpha
name: "Lynskey"
source_url: "https://lynskeyperformance.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Seventeen-degree tube angles, CNC-machined dropouts, and a mill floor in Chattanooga — Lynskey Performance embeds manufacturing precision into every pixel of its digital presence. The primary CTA carries #116dff, a voltage blue that punches through the near-black (#080808) canvas like a headlamp on a mountain descent; it appears on every "Build Yours" button, active link, configurator progress accent, and geometry dimension line across the site. Where the primary blue asserts, the secondary accent retreats to #7fccf7, a pale sky blue that maps directly to the cold luster of raw Grade 9 titanium — it surfaces on material badges, highlight rows in the size guide, and selected-state indicators in the build configurator, giving warmth without weight. Body type runs Arial and Helvetica Neue as honest workhorses, with the Madefor font stepping in for headings and UI labels — a geometric sans that holds tight letter-spacing at large sizes (−1.5px at 56px display) and reads with the same tolerance stack you'd expect from a tube-mitering machine. Gray lands on #5f6360, a warm mechanical hue that keeps component callouts and spec table values from going clinical. The corner language is almost square — `{rounded.xs}` on buttons, cards, and input fields — an engineer's preference for dimensionally exact edges over consumer-brand softness. The one exception is the material badge, where `{rounded.full}` pills float above product photography to call out "USA Made Titanium" in titanium-sky text on an ink ground. Elevation is used sparingly: cards lift on hover via a subtle box shadow rather than a border-color change, trusting depth to do all the spatial work. Spacing follows a 16px base grid; sections breathe at `{spacing.section}` (64px) vertical rhythm, keeping the catalog from feeling like a component dump. The dark footer in #080808 inverts the surface, with `{colors.titanium-sky}` links providing contrast that doubles as a material signature. The overall effect is less a consumer storefront and more a precision instrument — every layout decision reads like a tolerance spec, nothing looser than it needs to be.

colors:
  primary: "#116dff"
  primary-active: "#0052cc"
  primary-disabled: "#a8c8ff"
  ink: "#080808"
  body: "#1c1c1c"
  muted: "#5f6360"
  hairline: "#d6d6d6"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#0d0d0d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  titanium-sky: "#7fccf7"
  secondary-blue: "#3899ec"

typography:
  display-xl:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Madefor', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Madefor', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  button-md:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Madefor', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  hero-fullbleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(8,8,8,0.45)"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 600px
    viewportHeight: 80vh
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    hoverBoxShadow: "0 4px 20px rgba(0,0,0,0.10)"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-dark}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowAlternateColor: "{colors.canvas}"
    rowBorderColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  material-badge:
    backgroundColor: "{colors.titanium-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  geometry-diagram:
    backgroundColor: "{colors.surface-soft}"
    lineColor: "{colors.primary}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  size-guide:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-sm}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    highlightRowColor: "{colors.titanium-sky}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
  color-swatch:
    size: 32px
    rounded: "{rounded.full}"
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 2px
    unselectedBorderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    stepLabelTypography: "{typography.spec-label}"
    stepValueTypography: "{typography.title-sm}"
    activeStepBorderColor: "{colors.primary}"
    activeStepBorderWidth: 2px
    activeStepBorderSide: left
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.titanium-sky}"
    mutedTextColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    paddingVertical: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The primary action button carries `{colors.primary}` (#116dff) with white text at `{typography.button-md}` (weight 600, 0.3px tracking), cut to `{rounded.xs}` corners that read as precision-engineered rather than polished-consumer. At 48px tall with 28px horizontal padding it sits assertively on light and photography surfaces. Active state drops to `{colors.primary-active}` (#0052cc); disabled washes to `{colors.primary-disabled}` (#a8c8ff). This is the "Build Yours", "Shop Now", and configurator-submit button throughout the catalog.

**`button-secondary`** — Outlined with a 1.5px `{colors.ink}` border and `{colors.canvas}` fill, used for secondary decisions like "View Specs" or "Compare Models" paired alongside a primary CTA. Maintains the same 48px height so paired buttons sit flush on a shared baseline.

**`button-ghost`** — Transparent fill with a 1.5px white border and `{colors.on-dark}` label, used exclusively on dark-surface placements — hero overlays, full-bleed section breaks — where `{colors.primary}` would fight the photography. Identical sizing to primary for layout compatibility.

### Text Input

**`text-input`** — A minimal rectangular field at `{rounded.xs}`, 48px tall, `{colors.hairline}` border going to `{colors.primary}` on focus. Placeholder in `{colors.muted}`. Used across search, mailing-list capture, and configurator form fields. No visible label animation; labels sit above the field in `{typography.spec-label}` uppercase.

### Navigation

**`nav-bar`** — White canvas bar at 68px with a single `{colors.hairline}` bottom rule. Logo anchors left at 36px tall; category links (Bikes, Custom, Racing, About) run `{typography.nav-link}` weight 500 center; a "Build Yours" button in `{colors.primary}` closes the right end. Sticky on scroll with no blur or shadow — the hairline rule alone separates it from page content.

### Hero

**`hero-fullbleed`** — Full-viewport-width photography with a 45% near-black scrim ensuring legibility on action and landscape imagery. Headlines render at `{typography.display-xl}` (56px, −1.5px tracking); sub-copy at `{typography.body-md}`. Minimum 600px, 80vh on desktop. Primary CTA is `button-primary`; a `button-ghost` secondary action sits beside it for "View Gallery" or "Learn More" paths. Text and buttons align bottom-left on desktop, centered on mobile.

### Product Card

**`product-card`** — White card with a `{colors.hairline}` border and a 4/3 photography well that fills fully to the card edge, no internal padding. Model name in `{typography.title-md}`, starting price in `{typography.price-display}` (24px, weight 700). A `{colors.titanium-sky}` material badge ("Grade 9 Titanium", "USA Made") floats over the image at the lower-left corner using `material-badge`. On hover, the card lifts with a 20px diffuse shadow — no border-color change, depth alone signals interactivity.

### Spec Table

**`spec-table`** — Alternating `{colors.surface-soft}` / `{colors.canvas}` rows, with a solid `{colors.ink}` header band carrying white all-caps labels in `{typography.spec-label}` (11px, 700, 1.2px tracking). Values in `{typography.body-sm}`. Covers tube dimensions, weight, dropout width, bb shell standard, and component build specs. Embedded inline on every frame detail page and floated beside the geometry diagram on wide viewports.

### Material Badge

**`material-badge`** — Pill-shaped label at `{rounded.full}` in `{colors.titanium-sky}` (#7fccf7) with `{colors.ink}` text at `{typography.spec-label}` uppercase. Used to surface "USA Made Titanium", "Lifetime Warranty", and grade callouts ("3AL-2.5V", "CP1"). Titanium-sky is the brand's single most distinctive extracted accent; its use here ties the visual identity to the physical material in a way that no brand copy can.

### Geometry Diagram

**`geometry-diagram`** — A technical illustration panel with a `{colors.surface-soft}` field, dimension lines drawn in `{colors.primary}` (#116dff), and measurement labels in `{colors.muted}` at `{typography.caption}`. The frame silhouette runs as a neutral dark stroke. Embedded inline on geometry tabs, typically in a two-column layout beside a size-guide grid. Border is `{colors.hairline}`, corners `{rounded.sm}`.

### Size Guide

**`size-guide`** — A responsive grid table mapping rider height ranges to frame size recommendations. The active or recommended size row is highlighted with `{colors.titanium-sky}` background. Header row uses `{typography.spec-label}`; cell values use `{typography.body-sm}`. Collapses to a horizontal-scroll single row on mobile.

### Color / Finish Swatch

**`color-swatch`** — 32px circles at `{rounded.full}` with `{colors.hairline}` resting border and a 2px `{colors.primary}` ring on selection. Tooltip or inline label in `{typography.caption}` names each finish (Brushed, Polished, Raw, Anodized Blue). Groups of 4–6 swatches arrange inline below each configurator section heading.

### Build Configurator Panel

**`configurator-panel`** — A padded (`{spacing.xl}`) `{colors.surface-soft}` panel with `{colors.hairline}` border and `{rounded.sm}` corners. Each configuration step (Frame, Fork, Groupset, Wheels, Finishing Kit) renders a `{typography.spec-label}` uppercase step title and a `{typography.title-sm}` selected-value line below it. The active step gets a 2px `{colors.primary}` left border accent. A horizontal step-progress indicator lives above the panel at full width; the running price total updates in `{typography.price-display}` at panel bottom.

### Footer

**`footer`** — Near-black (#080808) slab inverting the page surface. Primary text in `{colors.on-dark}`, link text in `{colors.titanium-sky}` — the sky blue on dark reads clearly while doubling as the brand's material signature. Columns cover Shop, Custom, Racing, Support, and a mailing-list field. Fine print and legal links in `{colors.muted}`. Section padding `{spacing.section}` top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger drawer; hero 100vw × 70vh, text centered; spec table horizontal scroll; size guide single-column stacked; swatches wrap to two rows; configurator steps become accordion |
| Tablet | 744–1128px | Two-column product grid; nav links visible but "Build Yours" button hidden (moved to sticky top bar); hero headline drops to `{typography.display-md}`; geometry diagram stacks above spec table |
| Desktop | 1128–1440px | Three-column product grid; full nav with CTA pill; hero 80vh; geometry diagram and spec table side-by-side at 50/50; configurator panel floats as right-column sidebar |
| Wide | > 1440px | Content capped at ~1280px max-width, centered; outer gutters absorb extra space; hero image scales but typography stays at defined sizes |

### Touch Targets
- All interactive elements minimum 44 × 44px on mobile
- Swatches scale to 40px diameter on touch viewports
- Hamburger toggle and cart icon each occupy 44px hit areas with transparent padding
- Configurator step rows expand to 56px tap height on mobile accordion
- A sticky "Build Yours" bar (48px CTA, full width) appears pinned to the bottom of the viewport on mobile product detail pages

### Collapsing Strategy
- Navigation: full horizontal bar → hamburger with full-height slide-in drawer at < 744px
- Product grid: 3-column → 2-column at tablet → 1-column at mobile
- Hero: overlay text shifts from bottom-left to center-bottom on mobile; paired CTA buttons stack vertically
- Spec table: fixed-layout table → overflow-x scroll container on mobile
- Configurator panel: persistent right-column sidebar → bottom-anchored accordion at mobile
- Geometry diagram: inline float beside spec table → stacked above it at < 1128px
- Footer: 4-column grid → 2-column at tablet → stacked single-column at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only 5 hex values extracted; shadow tones, scrim opacity, and row-stripe alternates are inferred rather than measured from live CSS
- No custom icon set detected — stroke weight, grid size, and filled vs. outline style for nav and UI icons are unconfirmed
- Exact nav height (68px here) and sticky-scroll shadow/border behavior are inferred, not confirmed from extraction
- Madefor font stack detected but licensed weight variants (300/400/500/700) and whether a variable font is served are unverified
- No dark-mode variant detected — design assumes light-mode-only
- Animation and transition curves (configurator step changes, card hover timing, drawer slide) are not extractable from a static snapshot
- No promotional announcement bar or sale-banner color data extracted
- Border-radius on cards inferred as `{rounded.xs}` (4px) from brand character; actual computed CSS values not confirmed
- `{colors.secondary-blue}` (#3899ec) appears in extraction but its specific UI role (hover state, link underline, icon fill) could not be determined from available data
