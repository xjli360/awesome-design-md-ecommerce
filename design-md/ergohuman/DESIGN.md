---
version: alpha
name: "Ergohuman"
source_url: "https://ergohuman.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every hero image on Ergohuman's site is a product photograph, never a lifestyle scene — a mesh back panel or an aluminum crossbar fills the viewport with the matter-of-factness of a technical manual, trusting the chair's joint geometry to do persuasion work that copywriting usually handles. The interface wraps this hardware confidence in Poppins, a geometric sans that occupies the precise midpoint between an engineer's data sheet and a consumer catalogue; its rounded apertures soften the precision of mechanical photography without deflecting it. The palette, as best can be determined from brand knowledge rather than live extraction (see Known Gaps), runs on near-black charcoal (#1a1a1a) for body text, a bright orange-red (#e05525) for every actionable surface — add-to-cart buttons, configurator selectors, promotional badges — and a white-to-light-grey field (#f7f7f7, #ffffff) that keeps photography from competing with the interface. Corners are controlled and confident: product cards sit at {rounded.sm}, primary buttons at {rounded.xs}, and the interface never reaches for pill shapes — the brand is too technically anchored to adopt the friendly-consumer softness {rounded.full} implies. Spacing is generous by category standards; the product configurator — a signature interaction for a brand that sells chairs across mesh-colour and base-finish variants — uses {spacing.xxl} gutters between option swatches and a persistent sticky summary panel rather than an accordion. The nav carries model-hierarchy complexity directly: sub-models (Ergohuman Plus, Pro, Fit) appear in a structured mega-menu grid rather than a flattened link list. The overall effect is a brand that prioritises specification legibility and purchase confidence over visual warmth: someone committing to a four-figure task chair wants to know exactly what they are buying before they want to feel good about it.

colors:
  primary: "#e05525"
  primary-active: "#b83f16"
  primary-disabled: "#f0bb9f"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-promo: "#e05525"
  spec-alt-row: "#f7f7f7"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
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
    height: 50px
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
    height: 50px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 50px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.08)"
    columns: 4
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    imagePadding: "{spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  badge-promo:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    imageWeight: "55%"
    imageAspect: "16/9"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowPadding: "{spacing.md} {spacing.base}"
    altRowBackground: "{colors.spec-alt-row}"
    stripedRow: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  configurator-swatch:
    size: 36px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "2px solid {colors.hairline}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  sticky-summary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 -4px 16px rgba(0,0,0,0.06)"
    priceTypography: "{typography.price-display}"
  feature-icon-block:
    iconSize: 48px
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    gap: "{spacing.md}"
  model-comparison-table:
    headerBackground: "{colors.ink}"
    headerText: "{colors.canvas}"
    headerTypography: "{typography.title-sm}"
    bodyBackground: "{colors.canvas}"
    bodyText: "{colors.body}"
    bodyTypography: "{typography.body-sm}"
    altRowBackground: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — A flat orange-red (#e05525) block with 4px corners ({rounded.xs}), 50px tall, carrying Poppins SemiBold at 15px with 0.3px letter spacing. Active state drops to #b83f16; disabled washes to the pale coral #f0bb9f. No gradients, shadows, or icon adornments — the color alone carries CTA weight, consistent with the brand's undecorated technical voice.

**`button-secondary`** — Matching dimensions to primary but white canvas with a 1px solid #1a1a1a border. Used for "Learn More" and "Compare" actions on category and landing pages. Hover inverts to dark fill with white text.

**`button-ghost`** — White background with a 1px orange-red border and matching text, reserved for configurator and modal contexts where both a primary and a secondary action are visible simultaneously and neither should fully recede.

### Navigation
**`nav-bar`** — A 72px-tall white bar with a 1px bottom hairline. Wordmark anchors left; search, cart, and account icon-buttons cluster right; model-family text links occupy the centre in Poppins 500/14px. On hover, primary model links open a full-width mega-menu rather than a simple dropdown — the model range requires it.

**`nav-mega-menu`** — A full-width white panel dropping below the nav, padded at {spacing.xl}, with sub-model thumbnail cards in a 4-column grid. Each card carries a small product render, the model name in title-sm, and a one-line key differentiator in body-sm. A soft shadow (0 8px 24px rgba(0,0,0,0.08)) lifts it from the page without a hard border.

### Product Card
**`product-card`** — White card with 1px hairline border and {rounded.sm} corners. The image area sits on a #f7f7f7 swatch padded at {spacing.lg}; below it the model name in title-sm leads, followed by a variant descriptor in muted (#666666), then the price in the 28px bold price-display style. A full-width button-primary spans the card bottom. On hover the card lifts with a subtle box-shadow.

**`badge-promo`** — All-caps Poppins Bold/11px at 0.5px tracking, orange-red fill, white text, pinned to the top-left of the product image. Carries "NEW", "AWARD WINNER", and promotional callouts.

### Configurator
**`configurator-swatch`** — 36px circle swatches for mesh-colour and base-finish selection. The selected swatch carries a 2px orange-red ring; unselected swatches carry a 2px hairline ring. A tooltip on hover names the colour or finish in body-sm.

**`configurator-panel`** — White panel ({rounded.sm}, 1px hairline border) containing labelled swatch rows, option group titles in title-md, and descriptive copy in body-sm. Option groups are separated by hairline rules rather than spacing alone, maintaining the data-sheet legibility the brand requires.

**`sticky-summary`** — Fixed-bottom bar that appears after the user scrolls past the product title on the PDP. Carries model name in title-sm, price in price-display, and the primary CTA. A 6% opacity upward shadow lifts it cleanly from page content. On mobile it spans the full viewport width.

### Specification Table
**`spec-table`** — Striped table with alternating #f7f7f7 and white rows. Row labels use spec-label style (Poppins 600/11px, 0.8px tracking, uppercase) in muted; values use body-sm in body colour (#333333). This is the trust-building engine of every model page — weight capacity, seat-height range, armrest adjustment count, warranty duration, and material certifications all live here. The table has {rounded.sm} corners and a 1px hairline border wrapping the whole block.

### Hero
**`hero-section`** — Full-width white section with the chair photograph occupying roughly 55% of the horizontal frame at desktop. Display type (Poppins 700/48px) runs left with a body-md sub-headline and a button-primary/button-secondary CTA pair below. Section padding is {spacing.section} top and bottom. No gradient overlays or text scrims; photography is never degraded by colour washes.

### Feature Icons
**`feature-icon-block`** — Stacks a 48px line-style icon, a title-sm label, and body-sm copy with {spacing.md} gap. Used in 3–4 column grids on landing pages to communicate ergonomic certifications, material grades, and adjustability ranges. Icons render in ink or primary-colour depending on promotional context.

### Model Comparison
**`model-comparison-table`** — Side-by-side table with a dark ink header row carrying model names in title-sm white text. Feature rows alternate between white and surface-soft. Boolean features use a checkmark or dash; numeric values render in body-sm. The first column (feature names in spec-label style) sticks during horizontal scroll.

### Footer
**`footer`** — Dark ink (#1a1a1a) background with white headings in title-sm and hairline-grey link rows in body-sm. Four-column link grid at desktop, collapsing to stacked accordions on mobile. A newsletter email input (white field, {rounded.xs}) anchors the first column. Social icons appear as small line-style glyphs in hairline colour at the base.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; mega-menu becomes a full-screen slide-in drawer with accordion sub-sections; configurator swatches stack vertically below the product image; sticky summary spans full viewport width; product grid collapses to 1-up; hero image moves above headline |
| Tablet | 744–1128px | 2-column product grid; mega-menu renders as a 2-column panel; configurator panel shifts below the hero image in a 1-column stack; comparison table scrolls horizontally with 2 models visible |
| Desktop | 1128–1440px | 3–4 column product grid; full 4-column mega-menu; configurator splits 60/40 image-left panel-right; sticky summary shrinks to a slim bar at bottom |
| Wide | > 1440px | Max-width container (~1400px) centred with auto margins; hero image scales proportionally within the container; no new layout zones introduced |

### Touch Targets
- All interactive controls (buttons, swatches, nav links) meet a 44×44px minimum hit area on touch viewports
- Configurator swatches expand from 36px visual diameter to 44px touch target via padding
- Sticky summary CTA spans the full mobile viewport width for thumb reach
- Mega-menu replaced by a bottom-anchored full-screen drawer; list items sized to 48px row height minimum
- Cart and icon buttons in nav-bar padded to 44×44px touch targets regardless of visual icon size

### Collapsing Strategy
- Nav mega-menu → full-screen slide-in drawer with accordion-collapsed model sub-sections
- Spec table → horizontal scroll container with sticky first (feature-label) column preserved
- Comparison table → horizontally scrollable with two model columns visible at a time on mobile
- Feature icon blocks → 1×N vertical stack on mobile, 2×N on tablet, 4×1 on desktop
- Configurator panel → moves below product image on tablet/mobile; swatch rows become full-width
- Footer link columns → accordion collapsed by default on mobile with chevron expand toggle

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site (likely JS-injected design tokens or anti-bot protection); all palette values are inferred from brand knowledge and must be verified against Ergohuman's actual style tokens before production use
- Meta theme-color was absent, removing the most common single-color primary signal
- No border-radius values were extractable; all `rounded.*` values are calibrated estimates for a precision-hardware brand and should be measured from live UI
- Exact nav-bar height, mega-menu column count, and sticky-summary scroll trigger point require live measurement
- Icon set style (line vs filled, proprietary vs icon-font) is unconfirmed
- Poppins weight usage beyond Regular/SemiBold/Bold (400/600/700) is assumed but not confirmed — Medium (500) may or may not be in active use
- Dark-mode palette, if any, is entirely unknown
- Promotional or sale accent color (if distinct from primary orange-red) could not be confirmed
- Exact grid gutter widths and max-width container value were not extractable
