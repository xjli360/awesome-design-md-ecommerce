---
version: alpha
name: "Jenni Kayne"
source_url: "https://jennikayne.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #FCFCF9 canvas — an off-white warm enough to suggest linen, restrained enough to read as architecture — defines Jenni Kayne's digital surface before a single product image loads. That color is not an accident: it appears as the meta theme-color, meaning the browser chrome itself adopts the brand's temperature on mobile. Domaine-Redesign, a high-contrast editorial serif with crisp bracketed serifs and finely drawn strokes, handles every display moment: homepage collection titles, story-page pull quotes, and seasonal campaign headers. GT America Web manages the entire utility layer — navigation labels, product names, filter chips, form fields — in a restraint that lets the serif dominate without friction. DomaineText-RegularItalic operates as a third voice: editorial captions, collection subtitles, and the occasional hover-swap from roman to italic that signals interactivity without weight change or color shift.

  The palette is near-monochrome by design. Deep carbon #141414 anchors all primary CTAs and maximum-contrast text. #545454 handles secondary body copy. #e2e2e2 and #dedede carry the hairline and border work. The amber pair — #f59e0b and #fbbf24 — is the single chromatic break: warm, confident, deployed for sale-price callouts and promotional badges where a muted accent would disappear against the pale ground and an alarming red would feel off-brand. Rounded corners are used with restraint throughout: product imagery and cards sit square or at 2px, filter pills reach for {rounded.full}, and almost nothing lands in between, which keeps the aesthetic grown-up and architectural.

  Spacing is generous and intentional. Section gutters open to 80px on desktop, reflecting the brand's conviction that negative space is part of the merchandise. The sticky navigation dissolves into the off-white surface and relies on opacity and weight shifts rather than asserting a solid bar. Vertical rhythm is unhurried — the page breathes, imagery fills wide breakpoints unclipped, and editorial text blocks run single-column to enforce reading pace. California-light photography does the heavy lifting; the design system exists to stay out of its way.

colors:
  primary: "#141414"
  primary-active: "#1f1f1f"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#e2e2e2"
  hairline-soft: "#dedede"
  canvas: "#fcfcf9"
  surface-soft: "#f6f6f6"
  surface-card: "#fcfcf9"
  on-primary: "#fcfcf9"
  accent-amber: "#f59e0b"
  accent-amber-light: "#fbbf24"

typography:
  display-xl:
    fontFamily: "'Domaine-Redesign', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Domaine-Redesign', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Domaine-Redesign', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.1px
  display-italic:
    fontFamily: "'DomaineText-RegularItalic', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-italic:
    fontFamily: "'DomaineText-RegularItalic', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  price-original:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'GT America Web', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    position: sticky
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline-soft}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    height: 36px
    alignment: center
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: 0
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price-original}"
    textColor: "{colors.muted}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-amber}"
  sale-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-italic}"
    imageLayout: full-bleed
    overlayOpacity: 0
    ctaStyle: button-secondary
    textAlignment: center
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-italic}"
    padding: "{spacing.section} 0"
    alignment: center
  editorial-caption:
    typography: "{typography.body-italic}"
    textColor: "{colors.muted}"
    padding: "{spacing.md} 0"
  size-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 44px
    minWidth: 44px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  size-selector-unavailable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.hairline}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — A full-bleed dark rectangle (#141414) with no radius and tracked uppercase GT America at 12px. On hover the background deepens to #1f1f1f; disabled state washes to #dedede with muted text. On mobile, primary buttons typically expand to full container width for easy thumb reach.

**`button-secondary`** — A 1px ink border on a transparent field, same uppercase typographic treatment as primary. Hover inverts to filled ink background and off-white text, so the two states share identical spatial footprint with a clean swap. This is the preferred surface CTA — used on hero overlays, collection headers, and editorial modules where the dark filled button would feel too heavy against the pale canvas.

**`filter-pill` / `filter-pill-active`** — The only fully-rounded element in the main commerce UI. Inactive pills are outlined in hairline gray with muted text; active pills fill to ink with off-white text. Used in product grid filtering where the pill shape distinguishes toggleable facets from the rectangular product and nav forms.

### Navigation
**`nav-bar`** — Sticky at 64px height, background matching the #FCFCF9 canvas so it reads as a continuation of the page rather than a chrome band. Links are GT America at 13px, lightly tracked, normal weight — no uppercase in the nav to avoid visual competition with the uppercase CTA buttons lower on the page. Hover state swaps to italic (DomaineText) rather than changing color.

**`announcement-bar`** — A 36px band sitting above the nav in deep carbon #141414 with off-white uppercase type at 11px. Carries shipping thresholds, promotional copy, or limited-time messages. The inversion to black over the off-white canvas creates a clean bracket at the top of every page.

**`nav-dropdown`** — Mega-menu panel that opens below the sticky nav with a top hairline border. Uses body-sm GT America for category links and generous {spacing.xl} padding so the panel breathes rather than packing content. No shadow or lifted treatment — it sits flush with the page plane.

### Product Cards
**`product-card`** — Square-cornered, 3:4 aspect-ratio image with a {colors.surface-soft} field underneath. Title in body-sm at muted body ink; price in price-original at {colors.muted}. Sale price replaces the original line in accent-amber (#f59e0b), which is the only warm color touch in an otherwise neutral card. Hover state typically reveals a secondary image via crossfade, not a UI element, keeping the chrome invisible.

**`sale-badge`** — A flat amber rectangle (no radius) pinned to the image top-left, carrying uppercase 11px type in {colors.canvas}. The amber (#f59e0b) is the brand's sole non-neutral color and appears exclusively in promotional contexts so it retains signal value.

### Hero & Editorial
**`hero`** — Full-bleed photography with overlaid centered text: display-xl Domaine for the headline, display-italic DomaineText for a sub-headline or season descriptor. No color overlay — images are selected to have sufficient negative space for white or black text reads. CTA uses button-secondary (outlined) so it doesn't block the image with a filled rectangle.

**`collection-header`** — Centered section introduction, display-md Domaine headline over body-italic subtitle, with {spacing.section} vertical breathing room above and below. Used to transition between navigation and product grid, establishing editorial voice before commerce begins.

**`editorial-caption`** — A body-italic line in {colors.muted} sitting beneath editorial imagery or alongside pull quotes. The italic DomaineText voice distinguishes brand copy from product information without introducing a third typeface.

### Forms
**`text-input`** — Sharp-cornered field, 1px hairline border at rest, 1px ink border on focus. 48px height matches button-primary for vertical rhythm in side-by-side layouts. No shadow or floating label — the field is deliberately unadorned.

### Size Selection
**`size-selector-button`** — Square-cornered 44×44px tiles arranged in a horizontal or wrapped grid. Default state is hairline-bordered canvas; active fills ink; unavailable grays out with a strikethrough on the label. No radius keeps the selector vocabulary consistent with the rest of the form system.

### Footer
**`footer`** — Inverted to ink (#141414) background with off-white text, creating a strong bookend to the off-white body. Column headings in title-sm (uppercase 11px), links in caption. The inversion mirrors the announcement bar, framing the content zone between two dark bands on long pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text shifts to display-sm; nav collapses to hamburger; buttons expand to full width; announcement bar wraps to 2 lines if needed |
| Tablet | 744–1128px | Two-column product grid; hero maintains centered layout; nav shows top-level links, mega-menu opens as drawer; side padding 24px |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-menu dropdown; hero fills viewport width; section padding 80px |
| Wide | > 1440px | Content maxes at ~1440px centered; product grid may expand to five columns; hero imagery scales with viewport, text block stays capped |

### Touch Targets
- All interactive elements (buttons, size tiles, nav links) maintain a minimum 44×44px tap target
- Filter pills use 6px vertical padding to reach comfortable touch height at small screen widths
- Nav hamburger trigger is 44px square even when the visible icon is smaller

### Collapsing Strategy
- Product grid collapses 4 → 3 → 2 → 1 columns as width decreases
- Mega-menu transitions to a full-screen slide-in drawer on tablet and mobile, preserving the same link hierarchy
- Footer columns stack vertically on mobile with section headings acting as accordion triggers
- Hero editorial text reduces from display-xl (56px) to display-sm (24px) on mobile to prevent overflow against portrait images
- Filter bar converts from inline pills to a bottom-sheet modal on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights and optical sizes for Domaine-Redesign are not publicly documented; weight 300 and 400 are inferred from visual inspection of rendered headlines — confirm with foundry specimen
- #5bbad5 and #da532c appear in the extracted palette but match Windows tile and Apple touch-icon metadata colors respectively, not brand UI colors; excluded from the design system
- Hover and focus animation timing curves (easing, duration) could not be extracted — 200–300ms ease-in-out assumed
- Exact line-height and letter-spacing values for Domaine-Redesign at display sizes require live measurement; values here are approximations from visual reference
- No data on loyalty, account, or checkout UI color treatment — footer and announcement bar inversion is inferred from category norms
- Whether GT America Web or Inter takes precedence in body copy on slower connections (font fallback ordering) could not be confirmed from static extraction
