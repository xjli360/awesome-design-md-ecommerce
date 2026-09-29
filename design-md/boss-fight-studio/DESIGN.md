---
version: alpha
name: "Boss Fight Studio"
source_url: "https://bossfightstudio.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Seven extracted shades of near-total black and a single light gray — that is the complete static palette of bossfightstudio.com. The canvas floors at #121212, barely distinguishable from an unlit monitor; surfaces step up through #171717, #191919, and #1f1f1f in a depth hierarchy legible only under deliberate scrutiny. This tonal compression is structural: the hyper-articulated, paint-detailed figures the brand sells are meant to ignite against a surrounding field of engineered darkness, with zero chromatic interference from UI chrome or decorative color. Inter handles all type across the stack, running at weight 700–800 for display headings and 400 for body copy, accompanied by a monospace family for SKU strings and part-number callouts — a nod to the collector-community convention where exact part codes carry genuine secondary-market meaning. The single extracted light value, #dedede, does double duty as the primary ink tone on dark surfaces and the closest the palette offers to a CTA highlight; #777777 steps in for metadata hierarchy — series labels, stock indicators, filter counts — while #555555 absorbs disabled states and subdued secondary marks. Rounding is almost certainly kept near zero: hard corners read as precision-manufacturing discipline and suit a brand that counts articulation points per figure as a core selling argument. The Shopify backbone implies a conventional grid scaffold (4-column desktop collapsing to 1-column mobile) beneath the dark shell, with metafields likely carrying figure-specific structured data: scale, character faction, wave number, and accessories count. A brand-voltage accent color — whatever activates the primary "Add to Cart" state and hover feedback — did not appear in the static DOM extraction and is the single most consequential missing token in this system.

colors:
  primary: "#dedede"
  primary-active: "#ffffff"
  primary-disabled: "#555555"
  ink: "#dedede"
  body: "#aaaaaa"
  muted: "#777777"
  muted-deep: "#555555"
  hairline: "#2c2c2c"
  hairline-soft: "#1e1e1e"
  canvas: "#121212"
  surface-soft: "#171717"
  surface-card: "#191919"
  surface-raised: "#1f1f1f"
  on-primary: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.04em
  badge:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  sku:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
  label-mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em

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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  text-input-search:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: none
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxWidth: 120px
    padding: "0 {spacing.xl}"
  nav-bar-link-active:
    textColor: "{colors.primary-active}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    imageAspectRatio: "1/1"
    figureTitleTypography: "{typography.title-sm}"
    seriesTypography: "{typography.caption}"
    seriesColor: "{colors.muted}"
    priceTypography: "{typography.title-sm}"
    skuTypography: "{typography.sku}"
    skuColor: "{colors.muted-deep}"
    border: "1px solid {colors.hairline-soft}"
    hoverBorder: "1px solid {colors.hairline}"
    shadow: none
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    overlayGradient: "linear-gradient(to right, {colors.canvas} 40%, transparent)"
  series-badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sku-label:
    textColor: "{colors.muted-deep}"
    typography: "{typography.sku}"
    display: inline
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xl} {spacing.lg}"
  filter-pill:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: none
  product-detail-header:
    backgroundColor: "{colors.canvas}"
    figureNameTypography: "{typography.display-md}"
    seriesTypography: "{typography.title-sm}"
    seriesColor: "{colors.muted}"
    priceTypography: "{typography.display-sm}"
    skuTypography: "{typography.sku}"
    skuColor: "{colors.muted-deep}"
    layout: two-column
    imageColumnWidth: "55%"
  articulation-stat:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xl} {spacing.xl}"
    columns: 4

## Components

### Buttons

**`button-primary`** — A compact slab reversing #121212 text onto a #dedede fill, relying on extreme luminance contrast rather than hue to signal action — the only way to make a CTA readable when the entire canvas is near-black. The all-caps Inter 700 label with 0.08em tracking reads as command-line terse, consistent with a collector audience that values precision over warmth. Active state lifts the fill to pure white; disabled state sinks to #555555 at 0.5 opacity, effectively receding into the surrounding dark surface.

**`button-secondary`** — A ghost button with a 1px #2c2c2c border on a transparent field, pairing beside the primary without competing for attention. On hover the border lifts to #dedede and the background picks up the #1f1f1f raised tone. Shares the uppercase Inter 700 label spec for visual parity within any button group.

**`button-ghost`** — Text-only, no background or border, rendered in #777777. Reserved for tertiary actions like "Clear Filters" or "View All" where visual weight must drop to near-invisible without disappearing entirely.

### Navigation

**`nav-bar`** — A 64px bar on #171717 with a hairline bottom border in #1e1e1e, logo anchored left, navigation links in 13px Inter 500 at slight uppercase tracking. No mega-menu complexity is implied by the brand's catalog scale; a flat horizontal list with cart icon and hamburger collapse at mobile. The active link state draws a 2px #dedede underline rather than a background highlight, keeping the bar visually lean.

### Product Card

**`product-card`** — A grid cell on #191919 with a 1px #1e1e1e border and no shadow, keeping the elevation system entirely flat. A 1:1 image square occupies the top portion so figure photography dominates; below it, the series name renders in 12px Inter 500 #777777, the figure title in 15px Inter 600 #dedede, and the SKU string in 11px monospace #555555 — three distinct hierarchy tiers without any color other than grays. Border brightens one step on hover. No rounded corners larger than 2px.

### Hero Banner

**`hero-banner`** — Full-width composition on #121212 with a left-anchored text column and a right-positioned hero figure photograph. A canvas-to-transparent gradient scrim ensures the display-xl heading remains legible without a hard crop against the product image. Subheadline runs in #777777 at body-md weight 400, creating maximum hierarchy distance from the 800-weight heading above. Minimum height 560px guarantees the figure is visible at full scale before the grid begins.

### Badges and Labels

**`series-badge`** — A small all-caps label (Inter 700, 10px, 0.08em tracking) identifying the product line or wave, rendered in #1f1f1f fill with #2c2c2c border. The 2px radius keeps corners hard. Multiple badges may stack horizontally on a product card when a figure belongs to a sub-line within a series.

**`new-badge`** — Identical typographic spec to series-badge but inverted to #dedede fill with #121212 text — the closest to a highlight color the extracted palette allows.

**`sku-label`** — Inline monospace 11px #555555 beneath the price point; functions as a catalog cross-reference for collectors who track part numbers across secondary markets.

**`articulation-stat`** — A small data cell displaying a numeric spec (e.g., "32 points of articulation") with a caption-weight label and a title-md value. Sits in a #1f1f1f box with 1px border, used in a horizontal strip on the product detail page to summarize figure specifications.

### Filters

**`filter-pill`** — A pill-shaped (#9999px radius) toggle in #1f1f1f with 1px border; active state fills to #dedede with #121212 text. Used in a scrollable horizontal strip on collection pages to narrow by series, scale, or character faction.

### Footer

**`footer`** — Four-column link grid on #171717 with a single top border in #2c2c2c. Section headings in 15px Inter 600 #dedede; links in 14px Inter 400 #777777, rising to #dedede on hover. No background variation between columns — the footer reads as a single flat panel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero stacks image above text block; filter bar collapses to a "Filter" sheet trigger |
| Tablet | 744–1128px | Two-column product grid; condensed nav with fewer visible links; hero image scales to ~50% column width |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with all links visible; hero two-column split; filter pill bar visible above grid |
| Wide | > 1440px | Max-width container (~1400px) centered with auto side margins; grid may extend to five columns; section padding increases to accommodate white space |

### Touch Targets
- Minimum 44px tap height on all interactive elements at mobile breakpoint
- Product cards expose a full-bleed tap zone covering the entire cell, not limited to title text
- Filter pills expand to 18px horizontal padding on mobile for easier thumb access
- Cart and hamburger icons in the nav bar sit within a 48×48px invisible tap target
- Articulation-stat cells are display-only on mobile; no tap interaction expected

### Collapsing Strategy
- 4-column product grid → 2-column at 744px → 1-column at 480px
- Horizontal filter pill bar → "Filter" bottom-sheet drawer at < 744px
- Navigation links → hamburger drawer; cart and search icons remain pinned in the bar at all breakpoints
- Hero image may be hidden below 480px if the text column alone fills the viewport at acceptable hierarchy
- Footer 4-column grid → 2-column at 744px → 1-column accordion at < 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No chromatic accent color extracted — the brand almost certainly uses a non-gray CTA voltage (common in collector and gaming brands: electric blue, red, neon green) that loads via JavaScript or a late-loaded stylesheet; this is the highest-priority missing token before building any interactive state
- Entire extracted palette is achromatic (#121212 through #dedede); all seven values serve structural depth rather than brand-identity differentiation
- Inter may be a Shopify theme default rather than a deliberate brand choice; `inherit!important` in the font stack suggests at least some elements are overriding a theme base, and the true brand typeface may differ
- No hover, focus, or active-state colors were reachable from static DOM; all interaction tokens in this file are inferred from the achromatic available values
- Sale/markdown pricing accent color (typically red or struck-through gray) not extracted
- Star-rating and review-count colors undetermined — no review UI was present in the crawled static output
- Shadow and elevation values are entirely speculative; the flat all-dark palette makes it possible the brand uses no shadows at all
- Exact product grid gutter widths and column counts could not be confirmed; 4-column desktop is inferred from Shopify collection-page conventions
- Figure detail page layout (single vs. multi-image gallery, sticky add-to-cart bar behavior) not confirmed from extraction
