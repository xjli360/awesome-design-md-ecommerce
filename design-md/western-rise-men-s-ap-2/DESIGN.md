---
version: alpha
name: "Western Rise"
source_url: "https://westernrise.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Before the product images load, Western Rise names the fabric — stretch percentage, moisture-wicking rating, and fabric weight in ounces per square yard — arranged in a monospaced spec block that treats technical data as a design element rather than fine print. The full site palette compresses into a disciplined range: near-black (#222222, #121212) for all primary actions, warm off-white surfaces (#f1f0ed, #fafafb) that keep the experience from going clinical or military, and a vivid mint (#b2f9e9) that appears on performance-attribute highlights and limited badge states — a single chromatic flare inside an otherwise earth-and-charcoal system. Muted olive (#707761), warm sage (#babfa7), and a deep midnight navy (#272d45) supply the secondary range, grounding the brand in outdoors and terrain without evoking recreation. Corners sit near-flat (`{rounded.xs}`, `{rounded.none}`) on every interactive element — buttons, size selectors, badges, and cards alike — the design language of working tools, not lifestyle objects. The type stack is led by Geist, a low-contrast geometric sans-serif, running at tight letter spacing in display positions and loosening into comfortable measure for fit guides and fabric descriptions; Geist-Mono handles spec data inline. A teal accent (#0e7a82) surfaces in sale states and secondary CTAs, narrow enough in usage that it retains impact. Navigation carries unusual information density: category, fit guide, fabric technology, and activity filters coexist at the top level, honoring an audience that arrives already knowing what they need. Product cards forgo editorial abstraction — no lifestyle taglines, just the product name, fabric descriptor, and price — in the same pattern of direct communication the brand uses in its technical specs and warranty documentation.

colors:
  primary: "#222222"
  primary-active: "#121212"
  primary-disabled: "#848587"
  ink: "#121212"
  body: "#2c2c2c"
  muted: "#848587"
  muted-soft: "#898a8d"
  hairline: "#e5e5e5"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#fafafb"
  surface-warm: "#f1f0ed"
  surface-warm-alt: "#f2f0ee"
  on-primary: "#ffffff"
  navy: "#272d45"
  midnight: "#2c3e50"
  slate: "#384b57"
  teal: "#0e7a82"
  purple-gray: "#676986"
  purple-gray-light: "#d3d4dd"
  olive: "#707761"
  sage: "#babfa7"
  sage-warm: "#bab7a7"
  mint: "#b2f9e9"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-strong:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  label-sm:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px
  price:
    fontFamily: "Geist, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  mono-spec:
    fontFamily: "Geist-Mono, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
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
    padding: 14px 24px
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
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  announcement-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-warm}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.md}"
    imageAspectRatio: "3/4"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlayOpacity: 0.4
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-mint:
    accentColor: "{colors.mint}"
    highlightBackground: "{colors.mint}"
    highlightTextColor: "{colors.ink}"
  fabric-spec-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  performance-badge:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    selectedBackground: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    soldOutBackground: "{colors.surface-soft}"
    soldOutTextColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    size: 44px
    typography: "{typography.body-sm}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
    border: "1px solid {colors.hairline}"
  product-detail-tabs:
    backgroundColor: "{colors.canvas}"
    activeTabColor: "{colors.ink}"
    inactiveTabColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    activeBorderBottom: "2px solid {colors.ink}"
    inactiveBorderBottom: "1px solid {colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    selectedBackground: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    height: 40px
    padding: "0 {spacing.md}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Flat-cornered (`{rounded.xs}`) dark charcoal (#222222) block at 48px height, 14px uppercase-tracked semi-bold text in white. Active state deepens to near-black (#121212); disabled desaturates to medium gray (#848587) with no opacity trick, keeping the element visible in layout.

**`button-secondary`** — White fill with a 1px charcoal border at the same 48px height and weight as primary, used for secondary actions like "Save to Wishlist" or "View Full Fit Guide." Equal visual mass to primary without competing in hierarchy.

**`button-ghost`** — Transparent fill with a 1px hairline border (#e5e5e5), deployed for tertiary actions — filter resets, collapse triggers, "Load More" — where visual weight should recede behind the product content.

### Navigation
**`nav-bar`** — 64px white bar with a 1px hairline bottom border. Nav links at 14px weight-500 with 0.1px tracking, no all-caps. Logo anchors center or left depending on viewport; cart, wishlist, and account icons anchor right as icon-only targets with 44px tap areas. Collapses to sticky at 56px with a soft 4px box-shadow.

**`announcement-bar`** — 36px midnight navy (#272d45) strip pinned above the nav. Copy runs in 12px all-caps weight-600 white with 0.3px tracking — shipping thresholds and promotion codes, never lifestyle language.

### Product Cards
**`product-card`** — Portrait 3:4 image on a warm off-white (#f1f0ed) tile background; product name in 15px weight-600 `{typography.title-sm}`; price in 16px weight-600 below; fabric descriptor in `{typography.caption}` gray below the price. No taglines. Desktop hover reveals a quick-add size row at the card bottom edge without expanding the card.

**`product-card-badge`** — Flat-cornered black label positioned at image top-left for "New" and category callouts. **`product-card-badge-sale`** uses teal (#0e7a82) to flag discounted items with identical geometry.

### Product Detail
**`fabric-spec-tag`** — Monospaced 12px tiles (Geist-Mono) inside hairline-bordered rectangles on the PDP, displaying weight in oz/yd², stretch percentage, and moisture metrics as bare data. Warm soft-gray (#f4f4f6) background against the page's off-white canvas creates a subtle data-block separation.

**`performance-badge`** — Mint (#b2f9e9) flat pill in 11px all-caps weight-600, applied to specific functional attributes: "4-Way Stretch," "UPF 40+," "Quick-Dry." The high chroma against the neutral page draws the eye without adding hierarchy noise elsewhere.

**`size-selector`** — 44×44px square tiles with hairline borders in default, charcoal fill with white text when selected (`{colors.primary}` / `{colors.on-primary}`). Sold-out tiles receive a soft-gray fill (`{colors.surface-soft}`) with muted text and a diagonal line through the label — they remain visible and present to show availability context rather than collapsing out of the grid.

**`color-swatch`** — 28px full-radius circles with a 1px hairline border. Selected state: 2px charcoal ring with 2px offset so the ring floats around the swatch without clipping the swatch color.

**`product-detail-tabs`** — Flat-bottom tabs (Description, Fabric & Care, Fit Guide, Reviews) switching by 2px charcoal underline on active, hairline-weight on inactive. Tab labels at `{typography.title-sm}` weight-600, no pill or background fill.

### Filtering and Search
**`filter-chip`** — Full-radius pills (`{rounded.full}`) with hairline border in rest state, filling to charcoal on selection with white text — used across collection pages for activity type, fit, and fabric technology facets. Chips scroll horizontally on mobile.

**`search-bar`** — 40px surface-soft input tile (`{colors.surface-soft}`) with flat corners, 14px muted placeholder, expanding to a full-screen overlay with autocomplete suggestions on mobile. Desktop renders inline in nav-bar on focus.

### Hero
**`hero-banner`** — Full-bleed photography with a 40% dark scrim, midnight navy (#272d45) as fallback background, 40px weight-700 display headline in white with -0.5px tracking, and a single `button-primary` CTA anchored lower-left. The **`hero-banner-mint`** variant layers a mint (#b2f9e9) accent strip or headline highlight for performance collection launches, keeping ink (#121212) as the text color on that strip for legibility.

### Footer
**`footer`** — Charcoal (#222222) full-width footer with white body text and muted-gray links. Four columns: Shop by Category, Fabric Technologies, Support (with warranty and repair documentation links surfaced at the same level as return policy), and Company. Column headings at `{typography.label-sm}` 11px all-caps. The inclusion of repair documentation at footer level signals expected product longevity — a design decision that reinforces the warranty narrative without needing a hero placement.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero crops to 9:16 with text anchored bottom-left; size selector expands to full-width bottom drawer; filter chips scroll horizontally; announcement bar truncates to single key message; fabric spec tags stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with mega-menu on tap; hero switches to 16:9; fabric spec tags wrap to 2×N grid; PDP tabs remain visible, not accordion |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu on hover with fabric technology sub-nav; hero at native aspect ratio with text anchored left third; fabric spec tags in a horizontal row |
| Wide | > 1440px | Content max-width clamped at 1440px with increased horizontal padding; four-column grid maintained; hero fills full viewport width with text column constrained to ~480px |

### Touch Targets
- Minimum 44×44px for all interactive elements: size selector tiles, color swatches, nav icons, filter chips
- Cart and account icons padded to 44px via invisible hit area expansion, not visible padding
- Announcement bar links maintain 36px minimum tap height despite the bar being 36px tall

### Collapsing Strategy
- Mega-nav collapses to a full-screen slide-in drawer with accordion category groups on mobile; "Fabric Technologies" becomes a second-level accordion item
- Product detail tabs collapse to stacked collapsible accordion sections on mobile, defaulting to Description open
- Fabric spec tag row collapses to 2-column grid below 744px, then single-column below 480px
- Footer four-column grid collapses to single accordion column on mobile, all sections closed by default

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom brand typeface captured; Geist and system fonts appear across the stack — Western Rise may use a licensed custom face loaded client-side or via Shopify font hosting that was not captured in extraction
- Button border-radius confirmed near-flat but exact pixel value not extracted; `{rounded.xs}` (4px) is assumed from visual inspection norms for technical apparel brands
- Mint (#b2f9e9) usage context partially inferred from extraction — it could originate from a third-party review widget (Okendo, suggested by `oke-widget-icons` font found in stack) rather than core brand UI; confirm before using as a brand accent
- Teal (#0e7a82) placement context not confirmed — may be sale badge, may be a secondary CTA color; treat as provisional
- Hero overlay opacity and image aspect ratios are inferred, not extracted from computed styles
- No animation timing, transition duration, or easing values extracted
- Dark mode variant data absent; theme-color is #ffffff, suggesting no dark mode implementation or a light-only configuration
