---
version: alpha
name: "Novo Guitars"
source_url: "https://www.novoguitars.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Novo Guitars lands on a canvas the color of aged bone — #e8e8e1, a warm off-white that registers less as a website background and more as the cream binding on a 1950s archtop. Against this understated ground, Open Sans carries all text at practical weights, a deliberate voice for a maker whose instruments do the speaking. The single voltage color is #ffde16, a chrome-yellow that reads as headstock-bright — not playful, not corporate, but metallically specific, the hue of a vintage Kluson tuner button or a well-lit selector switch cap. Primary CTAs fire in this yellow against near-black #231f20 ink, a lacquer-meets-binding contrast pair that sidesteps tech-brand convention entirely.

  The palette is essentially monochromatic with that one yellow accent. Near-blacks (#231f20, #1c1d1d, #121212) build depth gradations — navigation sits darker, card surfaces lighter. Medium grays (#444444, #dedede) anchor body copy and hairlines without introducing color distraction. The warm off-white canvas (#e8e8e1) carries tonal heat that straight white cannot, linking the digital surface to the warmth of nitrocellulose lacquer and aged maple binding.

  Corner radii are sparse — a {rounded.sm} 4px for inputs and cards, nothing pill-shaped. The spatial grammar is guitar-workshop: deliberate, wide-breathing, each model given enough room to read as an artifact rather than a catalog entry. Section padding is generous ({spacing.section}: 64px) and photography — typically shot against neutrals that echo {colors.canvas} — anchors every page section. Specification data runs at {typography.body-sm} inside structured grids that recall a printed hang-tag, not a dashboard widget.

  What separates Novo from mass-market guitar storefronts is the refusal to aestheticize through busyness. The #ffde16 accent appears at most once per viewport. There are no mega-menus, no icon-heavy chrome, no badge storms — just model names, series categories, and clean photography as navigation anchors. The brand assumes visitors arrive knowing what they want; the site's work is to present instruments with the same care the maker brings to shaping a neck heel. A boutique register, executed in Open Sans and bone-white.

colors:
  primary: "#ffde16"
  primary-active: "#e6c800"
  primary-disabled: "#fff8a0"
  ink: "#231f20"
  ink-deep: "#121212"
  body: "#444444"
  muted: "#767676"
  hairline: "#dedede"
  canvas: "#e8e8e1"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#231f20"
  on-dark: "#e8e8e1"

typography:
  display-xl:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  model-label:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "none"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 4px rgba(35,31,32,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 12px rgba(35,31,32,0.12)"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-series:
    typography: "{typography.model-label}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  series-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.model-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.model-label}"
    padding: "{spacing.section} {spacing.xl}"
    dividerColor: "{colors.hairline}"
  footer-link:
    textColor: "{colors.hairline}"
    hoverColor: "{colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  dealer-locator-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"

## Components

### Buttons

**`button-primary`** — The primary CTA fills with #ffde16 yellow and renders label text in #231f20 near-black at {typography.button-md} (Open Sans 15px/600, 0.5px tracking). Height is 44px with a tight {rounded.sm} 4px radius that avoids the pill softness of consumer apps. On `:hover` the surface shifts to {colors.primary-active} (#e6c800); on `:disabled` it falls back to the washed {colors.primary-disabled} with {colors.muted} text, preserving the yellow family without suggesting interactivity.

**`button-secondary`** — An outlined variant at the same 44px height — transparent fill, 1px solid #231f20 border, dark ink label at {typography.button-md}. Used for secondary catalog actions like "Find a Dealer" or "Compare" where the yellow CTA would compete with a nearby primary action.

**`button-ghost`** — Text-only, no border or fill. {typography.button-sm} in {colors.body} gray. Used in nav utility rows and inline callouts where spatial budget is tight.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} warm off-white background with a 1px {colors.hairline} bottom border. Model-category links run at {typography.nav-link} (14px/600). On scroll, a subtle box-shadow replaces the static border to maintain visual separation. The logo anchors left; model series names (Serus, Oranger, Dandy, Contino) fill the center or right zone; a cart icon sits at the far right with no visible text label.

### Product Cards

**`product-card`** — White surface-card fill, {rounded.sm} 4px radius, 4:3 image aspect ratio, {spacing.base} internal padding. The series badge ({series-badge}: yellow fill, {typography.model-label} uppercase type) sits as a tight chip above the model name. Price renders at {typography.title-md} weight-600. Hover state elevates the card with a soft shadow (0 4px 12px rgba(35,31,32,0.12)) without color change, preserving the neutral calm of the grid.

### Hero

**`hero`** — Full-bleed {colors.ink-deep} (#121212) background, minimum 560px height, with high-quality guitar photography layered above or beside the text column. Title at {typography.display-xl} (36px/700) in {colors.on-dark}; subtitle at {typography.body-md} at 0.75 opacity. A single `hero-cta` button in #ffde16 sits below the headline with wider 14px 32px padding — taller than the standard button to match the graphic weight of display type.

### Series Badge

**`series-badge`** — A compact rectangular chip in {colors.primary} fill with {colors.on-primary} dark text. {typography.model-label}: 11px uppercase, 1px letter-spacing, weight 700. {rounded.xs} 2px radius keeps it crisp. Used on product cards, guitar detail page headers, and collection section dividers to identify the model family (e.g. "Serus T Roasted", "Oranger HB").

### Spec Table

**`spec-table`** — Two-column key-value layout on a {colors.surface-soft} tint. Labels at {typography.spec-label} (12px uppercase/600, {colors.muted}); values at {typography.body-sm} in {colors.ink}. Each row separated by a 1px {colors.hairline} line. Padding is {spacing.md} vertical by {spacing.base} horizontal. The table mirrors the structure of a printed spec sheet, not a dynamic filter panel — static and read-only.

### Image Gallery

**`image-gallery`** — Main viewport with a horizontal thumbnail strip below. Inactive thumbnails carry a transparent 2px border; the active selection receives a 2px {colors.primary} (#ffde16) border highlight as the sole interactive color cue. Background is {colors.surface-soft}. {rounded.sm} on thumbnail corners. Swipe-enabled on touch; keyboard-navigable on desktop.

### Footer

**`footer`** — Full-width {colors.ink} (#231f20) dark background with {colors.on-dark} text. Column headings at {typography.model-label} (uppercase 11px/700) anchor link groups: Models, Dealers, About, Contact. Link rows at {typography.body-sm}; hover shifts text to {colors.primary} yellow. Padding is {spacing.section} vertical by {spacing.xl} horizontal. A {colors.hairline} rule separates the main link columns from the legal/copyright bar beneath.

### Dealer Locator Card

**`dealer-locator-card`** — White surface-card, 1px {colors.hairline} border, {rounded.sm} 4px radius, {spacing.base} padding. Dealer name at {typography.title-sm}; address and phone at {typography.body-sm} in {colors.body}. A text link ("Visit Website" or "Get Directions") at {typography.body-sm} gains a {colors.primary} yellow underline on hover — the only interactive color cue on the card.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero min-height drops to 360px with text stacked below image; spec-table goes single-column stacked; gallery enters fullscreen swipe mode |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero splits image/text 50/50; spec-table stays two-column |
| Desktop | 1128–1440px | Three-column product grid; full nav with all model series links; hero at full 560px+ with generous horizontal padding; footer in four columns |
| Wide | > 1440px | Content max-width ~1400px centered; hero photography bleeds edge-to-edge with content constrained inside; product grid stays three columns with larger gutters |

### Touch Targets

- All buttons minimum 44px height
- Nav hamburger and cart icon: 44×44px tap area
- Thumbnail strip items: 48×48px minimum with 4px gaps
- Footer links: 40px minimum line-height for comfortable tapping
- Dealer locator cards: full-card tap target on mobile

### Collapsing Strategy

- Primary nav collapses at 744px into a slide-in drawer from left, opened by hamburger icon at top-right
- Product filters (if present) render as a bottom sheet on mobile rather than a sidebar panel
- Spec table collapses to single-column stacked layout below 600px with label above value
- Image gallery thumbnail strip scrolls horizontally on mobile; wraps to a 2-row grid below the main image on desktop
- Hero text moves below the image on mobile (stacked block layout) rather than overlapping the photograph

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font stack shows Open Sans only — no custom display or heading typeface detected; brand may use a stylized wordmark font loaded as SVG or image asset that extraction cannot capture
- Many near-duplicate orange hex values (#f48120, #f58720, #f89f20, #f68d20, #f79a20, etc.) likely originate from payment-processor badge icons (PayPal, Shop Pay gradient) rather than the brand palette — only #ffde16 and the near-black/off-white range are treated as brand colors
- #006fcf and #3086c8 blues appear to be American Express and payment-gateway assets, not Novo Guitars brand colors — excluded from the palette
- Google icon colors (#4285f4, #34a853, #fbbc04, #ea4335, #5f6368) detected in extraction — sourced from Google Pay or font-service assets, not brand
- No hover/focus state color values observed; primary-active (#e6c800) and primary-disabled (#fff8a0) are inferred from yellow-hue logic, not directly extracted
- No explicit border-radius values captured; all rounded values inferred from boutique-guitar brand conventions
- Dark mode support unknown — no prefers-color-scheme tokens detected in extraction
- Cart, checkout, and account page component styling not available; Shopify default theme likely applies with minimal brand override beyond color and typography
