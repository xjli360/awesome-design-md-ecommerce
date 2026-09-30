---
version: alpha
name: "Billy Reid"
source_url: "https://billyreid.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The site's near-absolute darkness is the first signal — charcoal (#252525), near-black (#010002), and dark slate (#252a2e) account for four of the top five extracted colors, a palette that mirrors the brand's indigo-dyed fabrics and aged brass hardware rather than the aspirational bright-white of premium American menswear. Against this dark field, a dusty rose-red (#d94d5e) operates as the sole CTA voltage — not a vivid red but a worn, specific hue, closer to a faded mill label than a stop sign; it appears sparsely, which makes every instance carry weight. Faktum, a contemporary geometric sans extracted from the live site stack, carries all UI text at light-to-regular weights; its clean geometry holds legibility in the near-dark palette while Andale Mono surfaces in editorial callouts as a nod to in-house print culture. Spacing is editorial and unhurried — sections breathe at {spacing.section} or wider, with product imagery afforded full-bleed real estate on mobile. Corner radii trend toward {rounded.none} on virtually every component, reading as architectural and material rather than soft; the rare exceptions are swatch selectors at {rounded.full} and form inputs at {rounded.xs}. A honey amber (#f59e0b) surfaces in promotional strips and editorial callouts, warming the cold dark palette the way candlelight behaves against deep denim. The nav sits thin, typeset in tracked uppercase Faktum, nearly dissolving into the dark canvas so photography carries commercial weight. Product cards are wide and minimal; hover states surface alternative colorways rather than overlaid text, trusting the garment to close the sale. Florence, Alabama origin is not a theme bolted on top — it is a material constraint the digital system mirrors directly: dark, durable, free of ornament.

colors:
  primary: "#d94d5e"
  primary-active: "#990000"
  primary-disabled: "#a8a8a8"
  amber: "#f59e0b"
  amber-bright: "#fbbf24"
  ink: "#010002"
  body: "#252525"
  body-mid: "#1f1f1f"
  muted: "#6a6a6a"
  muted-light: "#8a8a8a"
  subtle: "#545454"
  hairline: "#e2e2e2"
  hairline-soft: "#efefef"
  canvas: "#f9f9f9"
  surface-soft: "#f6f6f6"
  surface-card: "#fcfcfc"
  surface-dark: "#141414"
  surface-deeper: "#1f1f1f"
  on-primary: "#f9f9f9"
  on-dark: "#f9f9f9"
  nav-bg: "#252525"
  footer-bg: "#141414"
  error: "#ff3451"
  navy: "#20436d"
  slate: "#252a2e"

typography:
  display-xl:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  product-name:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  editorial-mono:
    fontFamily: "'Andale Mono', 'Andale Mono WT', 'Courier New', 'DejaVu Sans Mono', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.1px
  overline:
    fontFamily: "'Faktum', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.5px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.body}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted-light}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 56px
    borderBottom: "none"
    logoColor: "{colors.on-dark}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRadius: "{rounded.none}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    hoverBehavior: "crossfade to alternate colorway image"
    paddingBottom: "{spacing.md}"
  sale-badge:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-deeper}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.muted-light}"
    overlayColor: "rgba(1,0,2,0.3)"
    layout: "full-bleed image, text anchored bottom-left"
    padding: "{spacing.xxl} {spacing.xxl} {spacing.section}"
  editorial-feature:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.amber}"
    layout: "50/50 image-text split, text on right"
    padding: "{spacing.section}"
  editorial-callout:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.editorial-mono}"
    padding: "{spacing.lg} {spacing.xl}"
    layout: "full-width strip"
  promo-banner:
    backgroundColor: "{colors.body-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    layout: "marquee or centered single-line"
  search-drawer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    inputBorder: "1px solid {colors.muted}"
    typography: "{typography.body-md}"
    layout: "full-width overlay slide-down from nav"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted-light}"
    typography: "{typography.caption}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.surface-dark}"
    columnGap: "{spacing.xxl}"
    padding: "{spacing.section} 0"
  price-display:
    regularColor: "{colors.body}"
    saleColor: "{colors.primary}"
    strikeColor: "{colors.muted-light}"
    typography: "{typography.price}"
    salePriceTypography: "{typography.price-sale}"
  swatch-selector:
    size: 20px
    gap: "{spacing.xs}"
    borderRadius: "{rounded.full}"
    selectedBorder: "1.5px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.subtle}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.sm}"
---

## Components

### Buttons

**`button-primary`** — Filled rose-red (#d94d5e) with zero border radius and tracked uppercase Faktum at 12px/1.5px letter-spacing. Height is 44px with generous 32px horizontal padding. Active state darkens to #990000; disabled state uses #a8a8a8 fill to signal unavailability without adding visual weight. Used exclusively for the highest-priority action per screen — add to cart, checkout, submit.

**`button-secondary`** — Ghost style: transparent fill, ink border (1px solid #010002), same 44px height and uppercase tracking as `button-primary`. Active state inverts to full ink fill with on-dark text. Sits beside `button-primary` for secondary options like "Save to Wishlist" or size guide triggers.

**`button-ghost-light`** — Same construction as `button-secondary` but reversed for dark-field contexts: transparent fill, on-dark (#f9f9f9) border and text. Used in `hero-banner` CTAs and any component sitting on a dark surface.

### Text Input

**`text-input`** — Completely square (`{rounded.none}`), thin hairline border that steps up to body charcoal (#252525) on focus — a subtle visual upgrade rather than a colored glow. Placeholder in muted-light (#8a8a8a). Height 44px matches button height for inline search-and-submit layouts. No shadow or elevation on any state.

### Navigation

**`nav-bar`** — 56px tall, #252525 fill, no bottom border. Logo and nav links in on-dark (#f9f9f9) via `{typography.nav-label}` — 12px, 500 weight, 1px letter-spacing, uppercase. The near-invisibility of the nav relative to the dark photography it floats above is intentional. On hover, nav items gain a thin underline rather than a color change.

**`nav-dropdown`** — Flips to the light canvas (#fcfcfc) with ink body text, maintaining strong contrast reversal from the dark nav bar. Typeset in `{typography.body-sm}` with generous `{spacing.xl}` padding per column. A hairline top border separates it from the nav bar.

### Product Card

**`product-card`** — Zero border radius on images, minimal metadata below: product name in `{typography.product-name}` (14px/400), price in `{typography.price}`. Color swatch dots appear on hover via the `swatch-selector` component. The hover state crossfades to an alternate product image rather than surfacing a text overlay — the garment leads. No card shadow or surface elevation; cards are set directly on the page canvas.

### Hero Banner

**`hero-banner`** — Full-bleed photography with a 30% black scrim (#010002 at 0.3 opacity) and text anchored to the bottom-left. Headline in `{typography.display-xl}` (52px/300 weight), preceded by an uppercase overline in `{typography.overline}` at muted-light. CTA uses `button-ghost-light`. The dark overlay is kept deliberately light so fabric texture and color read through.

### Editorial Components

**`editorial-feature`** — 50/50 split on desktop: full-bleed image left, dark surface (#141414) panel right with headline in `{typography.display-md}` (36px/300), body copy in `{typography.body-md}`, and an amber (#f59e0b) accent element (typically a thin rule or category label). Used for campaign storytelling and collection launches.

**`editorial-callout`** — Full-width amber (#f59e0b) strip using `{typography.editorial-mono}` in near-black ink. The monospace setting is the key detail: it reads as a printed aside, a reference number, a dye lot — functional rather than decorative. Used for shipping thresholds, sale callouts, or editorial quotes.

**`promo-banner`** — Single-line dark strip (#1f1f1f) at 36px height, on-dark caption text. Sits above the nav bar. Copy is either centered or marquee-scrolling on mobile.

### Supporting Components

**`sale-badge`** — Amber fill (#f59e0b), ink text, no radius, uppercase caption. Sits as an absolute overlay at the top-left of product images.

**`new-badge`** — Body charcoal (#252525) fill, on-dark text, same construction as `sale-badge`. Used for season arrivals.

**`price-display`** — Regular price in body charcoal (#252525); sale price in rose-red (#d94d5e) with strikethrough original in muted-light (#8a8a8a). The only place `{colors.primary}` appears in product listing contexts.

**`swatch-selector`** — 20px diameter circles, `{rounded.full}`, spaced at `{spacing.xs}`. Selected state gains a 1.5px ink border; unselected uses hairline border. Appears on product card hover and is always present on the product detail page.

**`footer`** — Near-black (#141414) fill, small tracked uppercase Faktum throughout. Links default to on-dark (#f9f9f9) and shift to rose-red (#d94d5e) on hover. Four columns on desktop: Shop, About, Customer Care, Newsletter. Newsletter input uses the standard `text-input` construction against the dark footer surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text increases line-height for legibility; product grid shifts to 2-column with reduced side padding ({spacing.base}); editorial features stack image over text full-width |
| Tablet | 744–1128px | Nav remains full but compresses to icon-only for secondary actions; product grid 3-column; editorial 50/50 splits maintained but at reduced internal padding |
| Desktop | 1128–1440px | Full nav with dropdowns; product grid 4-column; hero type at full 52px display-xl scale; section padding expands to {spacing.section} |
| Wide | > 1440px | Max content width capped (~1440px) with canvas fill bleeding edge-to-edge on dark-surface sections; product grid holds at 4-column, card gutters widen |

### Touch Targets

- All buttons minimum 44px height, matching text-input height for inline form layouts
- Swatch selectors expand hit area to 32×32px despite 20px visible circle
- Nav hamburger icon minimum 44×44px tap target
- Product card touch region includes the full card surface, not just image

### Collapsing Strategy

- Nav: desktop flyout dropdowns → tablet icon-compressed → mobile full-screen drawer overlay on hamburger tap
- Hero: desktop bottom-left text anchor → mobile text moves below image (stacked), overlay removed
- Editorial feature: desktop 50/50 split → mobile image full-width stacked above text panel
- Footer columns: 4-column desktop grid → 2-column on tablet → accordion-collapsed single column on mobile
- Product grid: 4 → 3 → 2 columns; card image ratio preserved at roughly 3:4 portrait across all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom heading typeface — `Faktum` is present in the extracted stack but weight range and whether a display cut is licensed could not be verified; a subset of Inter or Helvetica Neue may substitute on load failure
- Exact button border-radius on the live site could not be confirmed; `{rounded.none}` is inferred from the heritage/architectural brand direction but may be `{rounded.xs}` (2px) in production
- Hover and focus animation durations not extracted; 150–200ms ease-in-out assumed from heritage menswear conventions
- The amber (#f59e0b, #fbbf24) appears in the color extraction but its exact usage context (sale banners vs. editorial vs. both) could not be confirmed from static extraction alone
- Dark navy tones (#20436d, #252a2e, #1d2433) appear in the palette but their component assignments (collection landing pages, alternate nav states, seasonal themes) are ambiguous
- Product page layout specifics (sticky add-to-cart bar, size guide modal, fit recommendation module) not extractable from homepage-level hints
- Icon set style (stroke weight, whether custom or a licensed set like Phosphor or custom SVG) not determined
