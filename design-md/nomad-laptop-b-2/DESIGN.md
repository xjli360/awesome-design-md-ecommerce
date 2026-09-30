---
version: alpha
name: "Nomad"
source_url: "https://nomadgoods.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product photograph at nomadgoods.com opens on the same material vocabulary — ballistic nylon at near-black (#0e0e0e), bridle leather at warm taupe (#837e74), and olive webbing at military green (#4d5245) — and the UI takes its cues from that same field-kit logic rather than from the conventions of consumer electronics retail. Type is set in Gotham, the geometric sans that highway signage and mil-spec stenciling share, run at Bold weights for compressed headings and Book for body copy; Inconsolata surfaces at 13px for product specification callouts, where monospace grid alignment reads as a bill of materials rather than ad copy. The primary CTA is an electric cobalt (#0048ff) — a single voltage color that detonates against the near-black product-detail canvas and against the barely-off-white listing backgrounds alike; it appears nowhere decoratively, only on purchase actions. Warm taupe (#837e74) functions as the brand material token: it is the approximate hue of their full-grain leather and doubles as a secondary surface accent on spec callouts and material hang-tag badges. Olive (#4d5245) anchors colorway labeling for military-origin SKUs; cream (#cecdc0) surfaces on heritage-goods callouts; yellow (#efcf07) and orange (#ff5a00) serve as limited-edition accent signals, appearing seasonally in badge and swatch form. Corner radii are near-zero — {rounded.none} on primary buttons and product cards keeps geometry aligned with the straight-stitched edges of the physical goods, while {rounded.xs} rounds inputs and filter tags just enough for mobile tap comfort. Spacing is generous between grid items but compressed within them, channeling gear-catalog density. The overall system is a spec sheet that someone decided should feel premium: monochrome scaffolding, one voltage CTA, and material palette tokens that tie digital swatches directly to leather and nylon SKUs.

colors:
  primary: "#0048ff"
  primary-active: "#0036cc"
  primary-disabled: "#96b4ff"
  ink: "#0e0e0e"
  body: "#2f2f2f"
  muted: "#676767"
  muted-soft: "#b2b2b2"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#f3f3f3"
  surface-soft: "#f1f1f1"
  surface-card: "#ececec"
  on-primary: "#f3f3f3"
  on-dark: "#f3f3f3"
  brand-tan: "#837e74"
  brand-olive: "#4d5245"
  brand-cream: "#cecdc0"
  brand-yellow: "#efcf07"
  brand-orange: "#ff5a00"
  error: "#e3163b"

typography:
  display-xl:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
    textTransform: uppercase
  title-md:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham Book', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham Book', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham Book', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham Book', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  mono-spec:
    fontFamily: "'Inconsolata', 'Roboto Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  label-upper:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham Bold', 'Gotham', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    height: 44px
    focusBorderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.xl}"
    borderBottom: none
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(14,14,14,0.4)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspect: "1/1"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    productNameTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: "button-primary"
  badge-material:
    backgroundColor: "{colors.brand-tan}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-colorway-olive:
    backgroundColor: "{colors.brand-olive}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
    iconColor: "{colors.muted}"
  filter-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline}"
  filter-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.ink}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.label-upper}"
    valueTypography: "{typography.mono-spec}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    borderLeft: "3px solid {colors.brand-tan}"
  sticky-atc:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
    priceTypography: "{typography.title-md}"
    ctaVariant: "button-primary"
  collection-section-header:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} {spacing.xl}"
  swatch-selector:
    size: 24px
    gap: "{spacing.sm}"
    activeBorderColor: "{colors.ink}"
    activeBorderWidth: 2px
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.label-upper}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "1px solid {colors.body}"

## Components

### Buttons

**`button-primary`** — Electric cobalt (#0048ff) flat rectangle with zero corner radius, Gotham Bold 13px all-caps at 1.5px letter-spacing. On interaction it darkens to `primary-active` (#0036cc); the disabled state shifts to `primary-disabled` (#96b4ff) at 50% opacity. The all-caps uppercase label convention ("ADD TO CART", "SHOP NOW") is consistent across all CTAs and creates the visual cadence of a printed gear catalog.

**`button-secondary`** — Transparent with a 1px solid ink (#0e0e0e) border, matching text color, same Gotham Bold all-caps typography as primary. On hover, fill inverts to full ink with on-dark text — no radius change. Used for secondary actions ("VIEW DETAILS", "COMPARE") sitting adjacent to a primary CTA.

**`button-ghost`** — Zero-border, zero-background text link in Gotham Bold 11px uppercase with no padding. Reserved for tertiary in-page navigation ("SEE ALL REVIEWS", "MORE IN THIS COLLECTION") where a bordered button would add visual weight to an already-dense spec section.

### Navigation

**`nav-bar`** — Fixed 60px bar on a near-black (#0e0e0e) background with on-dark (#f3f3f3) nav links in Gotham Bold 14px uppercase. The always-dark nav ensures brand legibility against all hero image colors and eliminates the need for a scroll-triggered inversion. On scroll, a rgba(14,14,14,0.4) shadow at 8px blur adds depth while preserving the flat black tone.

### Product Card

**`product-card`** — Square 1:1 image on #ececec, zero border radius. Product name in Gotham Book 14px, price in Gotham Book 13px below. Material badges overlay the image's top-left corner. On hover a secondary colorway image crossfades, allowing shoppers to preview the leather-tan or olive variant without leaving the grid — the zero-radius crop keeps all transitions geometrically clean.

### Hero Banner

**`hero-banner`** — Full-bleed near-black (#0e0e0e) section with on-dark (#f3f3f3) text. Heading in Gotham Bold 40px uppercase, body copy in Gotham Book 15px at 1.6 line-height. 64px vertical padding gives the product photography room to breathe against the dark field. A single `button-primary` CTA sits below the subhead.

### Badges

**`badge-material`** — Warm taupe (#837e74) flat rectangle with Gotham Bold 10px uppercase label, zero radius, used on product cards and PDP headers to identify material type: "FULL-GRAIN LEATHER", "BALLISTIC NYLON", "WAXED CANVAS". The taupe-on-surface-card placement mirrors the physical hang-tag convention.

**`badge-new`** — Electric cobalt (#0048ff) variant of the material badge pattern for new SKU introductions.

**`badge-sale`** — Error red (#e3163b) variant for clearance and promotional pricing overlays.

**`badge-colorway-olive`** — Military olive (#4d5245) variant on product cards that carry olive colorway options, linking the digital grid swatch to the physical material colorway at a glance.

### Search

**`search-bar`** — Soft gray (#f1f1f1) input at 40px height, 4px radius, Gotham Book 15px placeholder in muted (#676767) with a magnifier icon at left. Expands to full-width on mobile; sits as a fixed-width overlay in the nav on desktop.

### Filters

**`filter-tag`** / **`filter-tag-active`** — Compact rounded-xs tags for collection filtering. Inactive: #ececec fill, 1px hairline border, Gotham Book 12px. Active: full ink fill with on-dark text — no icon or checkmark, the solid fill is the sole active signal. Tags scroll horizontally on mobile.

### Spec Callout

**`spec-callout`** — A #f1f1f1 inset block with a 3px left border in brand-tan (#837e74), used on product detail pages to present technical specifications (dimensions, weight, protection rating) in Inconsolata 13px. Labels in Gotham Bold 10px uppercase, values in monospace. The serif-monospace-plus-tan-bar treatment reads as a component data sheet from a gear manual.

### Sticky Add-to-Cart

**`sticky-atc`** — A canvas (#f3f3f3) bar with 1px hairline top border that appears after the user scrolls past the primary ATC zone on the PDP. Contains price in Gotham Bold 16px left-aligned and a full-width `button-primary` right-aligned on desktop, stacked vertically on mobile.

### Collection Section Header

**`collection-section-header`** — Full-width near-black (#0e0e0e) band separating product grid sections, carrying a Gotham Bold 24px uppercase section title. Acts as a hard typographic chapter break in the grid-scan flow: "LAPTOP PROTECTION", "BAGS & CASES", "ACCESSORIES".

### Swatch Selector

**`swatch-selector`** — 24px circular swatches at 8px gap, with a 2px ink (#0e0e0e) active border. No tooltip on hover; the selected colorway name appears in a Gotham Book 12px caption line above the swatch row after selection. Swatches expand to 32px on mobile touch targets.

### Footer

**`footer`** — Near-black (#0e0e0e) background matching the nav, column headings in Gotham Bold 10px uppercase, link text in Gotham Book 13px at muted-soft (#b2b2b2). A 1px body (#2f2f2f) top border separates the footer from the last content section, creating a visible but low-contrast seam.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; sticky ATC fills full width anchored to bottom; nav collapses to hamburger drawer; hero heading drops to display-md; filter tags scroll horizontally; swatch circles expand to 32px |
| Tablet | 744–1128px | Two-column product grid; nav retains icon links but drops flyout menus; hero splits 50/50 image and text; spec callouts stack vertically |
| Desktop | 1128–1440px | Three-column product grid; flyout nav menus active; sticky ATC moves to right-rail column; spec callouts display inline two-column |
| Wide | > 1440px | Four-column grid maximum; content max-width container at 1440px centers in viewport; hero gains proportional vertical height |

### Touch Targets
- All tappable elements minimum 44px height
- Filter tags minimum 36px height on mobile
- Swatch selectors expand from 24px to 32px on touch viewports
- Nav hamburger hit area minimum 44×44px
- Button-ghost text links gain 8px vertical padding on mobile to meet 36px minimum

### Collapsing Strategy
- Navigation: full link bar → icon bar with labels → hamburger drawer below 744px
- Product grid: 4col (wide) → 3col (desktop) → 2col (tablet) → 1col (mobile)
- Spec callout: two-column grid on desktop → single stacked column on mobile
- Collection section headers: full-width at all breakpoints; heading scale drops one step (display-xl → display-md) on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) was not present in extracted palette; `on-primary`, `surface-card`, and card backgrounds use near-white values (#f3f3f3, #ececec) — verify actual white usage in production
- Numeric font weights for Gotham Bold vs. Gotham Book not confirmed from extraction (fonts found as named strings, not weight integers); 700/400 mapping is inferred from standard Gotham family conventions
- Aleo serif was extracted but no component assignment was identifiable — likely confined to editorial blog posts, press pages, or testimonial pull-quotes; no Aleo components are specified here
- Exact letter-spacing values for nav and button labels are estimated from conventional Gotham all-caps norms, not directly measured from computed styles
- Hero video overlay gradient stop values and opacity ramps are not recoverable from a static color extraction pass
- Dark-mode variant unknown; all tokens assume default (light) theme
- #efcf07 yellow and #ff5a00 orange colorway assignments are inferred from product photography context; exact component usage (limited-edition badge vs. swatch only) not confirmed
- Icon set grid dimensions and stroke weights not extracted
