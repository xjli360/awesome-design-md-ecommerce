---
version: alpha
name: "Grand Seiko"
source_url: "https://www.grand-seiko.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Grand Seiko's digital canvas opens on photography that behaves more like landscape painting than product documentation — a dial magnified until its texture reads as terrain: a frozen lake, a birch forest, snowflakes caught mid-fall above the Shinshu highlands. The dominant navigation color is `#000040`, a midnight navy so deep it borders on space-black, and it carries none of the urgency of a conventional luxury brand's gold-or-red hierarchy. It is still, precise, and as deliberately placed as a hand-polished bevel on a Zaratsu-finished case. As the page opens into product territory, the canvas lightens through `#f6f6f6` and `#eeeeee`, a seamless shift from brand gravity toward the clarity needed to evaluate a dial gradient or a movement specification.

  Typography leans on Georgia paired with Hiragino Mincho ProN — the rare dual-serif combination of a classical Western roman face with the Japanese Mincho form, the print-style kanji face most analogous to a serif in Western type tradition. This pairing reflects Grand Seiko's insistence on dual cultural identity: calibrated and cased entirely in highland Japan, presented to an international collector audience without translation or apology for either origin. Body copy runs in Noto Sans at conservative weights — a neutral carrier that yields the editorial stage to photography and movement specification language.

  The warm dark gray `#605b58` — a tone that reads like aged nickel or charcoal brushed with amber — appears in secondary text and navigation filters, functioning as the brand's quiet alternative to pure black, softening hierarchy without sacrificing legibility. Gold `#e6ae06` surfaces sparingly as an accent for collection tags and limited-edition markers, always compressed to small typographic sizes rather than deployed as background fill; on a brand that sells movement precision over surface ornament, gold is earned through restraint rather than volume.

  Corners run sharp to near-sharp — `{rounded.none}` on buttons, `{rounded.xs}` at most on cards — because softened edges introduce the approachability of consumer goods, and Grand Seiko declines that register entirely. Every interactive element defers to the dial photography; the UI is infrastructure, not decoration.

colors:
  primary: "#000040"
  primary-active: "#00003a"
  primary-disabled: "#b3b3c6"
  on-primary: "#f6f6f6"
  ink: "#212121"
  body: "#424242"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#dbdbdb"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f2f2f2"
  warm-charcoal: "#605b58"
  warm-charcoal-dark: "#534e4c"
  gold-accent: "#e6ae06"
  deep-navy-alt: "#000027"
  mid-gray: "#616161"
  light-gray: "#c5c5c5"
  error: "#dc3c31"

typography:
  display-xl:
    fontFamily: "Georgia, 'Hiragino Mincho ProN', 'Noto Serif', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "Georgia, 'Hiragino Mincho ProN', 'Noto Serif', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.015em
  display-md:
    fontFamily: "Georgia, 'Hiragino Mincho ProN', 'Noto Serif', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  title-lg:
    fontFamily: "Georgia, 'Hiragino Mincho ProN', 'Noto Serif', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "Georgia, 'Hiragino Mincho ProN', 'Noto Serif', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-uppercase:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.06em
  spec-label:
    fontFamily: "'Noto Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
    textTransform: uppercase
  price:
    fontFamily: "Georgia, 'Hiragino Mincho ProN', 'Noto Serif', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
    borderFocusColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    paddingX: "{spacing.xl}"
    borderBottom: none
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    paddingY: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    padding: 0
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.caption}"
    subtitleColor: "{colors.warm-charcoal}"
    hoverEffect: "image-zoom 0.4s ease"
  hero-fullbleed:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 100vh
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaVariant: button-ghost
    overlayOpacity: 0.35
    imageFit: cover
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xxl}"
    layout: image-left-text-right
  season-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    paddingX: "{spacing.sm}"
    paddingY: "{spacing.xs}"
  limited-badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    paddingX: "{spacing.sm}"
    paddingY: "{spacing.xs}"
  dial-detail-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.warm-charcoal}"
    valueTypography: "{typography.body-md}"
    borderTop: "1px solid {colors.hairline}"
    paddingY: "{spacing.base}"
    gap: "{spacing.md}"
  movement-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.warm-charcoal-dark}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    paddingCell: "{spacing.md} {spacing.base}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputBorderColor: "{colors.primary}"
    overlayScrim: "rgba(0,0,64,0.5)"
    resultTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    paddingY: "{spacing.sm}"
    gap: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.light-gray}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.hairline}"
    paddingY: "{spacing.section}"
    borderTop: none

## Components

### Buttons
**`button-primary`** — Flat midnight navy (`{colors.primary}`) rectangle with `{rounded.none}` and uppercase spaced lettering at `{typography.button-md}`. On hover the fill deepens to `{colors.primary-active}` with no easing delay — the abruptness is intentional, soft transitions read as hesitation. Disabled state replaces the navy with `{colors.primary-disabled}`, a muted blue-gray that signals unavailability without overlays or strikethroughs.

**`button-secondary`** — White canvas fill (`{colors.canvas}`) with a single-pixel primary navy border and navy text, matching the height of `button-primary` at 48px exactly. Used for secondary CTAs such as "add to wish list" or "view calibre details" where the primary button already claims the page hierarchy.

**`button-ghost`** — Transparent fill with a 1px `{colors.on-primary}` border and white text, deployed exclusively over dark or photographic hero backgrounds. The border makes it legible without a contrasting fill that would fragment the full-bleed image beneath.

### Navigation
**`nav-bar`** — A 64px midnight navy bar spanning full width with the Grand Seiko wordmark anchoring left in `{colors.on-primary}`. Category links (Timepieces, Collections, Heritage, Boutique) run in `{typography.nav-link}` with 0.06em letter-spacing that recalls Japanese typographic spacing convention carried into Latin characters. A search icon and locale toggle occupy the right rail; both receive 48×48px touch targets.

**`nav-dropdown`** — A white canvas panel that drops below the fixed navy bar, separated by a 1px `{colors.hairline}` top rule. Sub-category columns layout horizontally; a featured seasonal collection image occupies a right-panel slot. The dropdown exits on cursor departure with no animation transition — deliberate.

### Product Card
**`product-card`** — A pure rectangle with no shadow, no radius, and a 4:5 image container that fills entirely with dial photography. Below the image: the reference number in `{typography.caption}` at `{colors.warm-charcoal}`, the collection name in `{typography.title-md}`, and the price in `{typography.price}` set in Georgia serif to echo the editorial register of the dial close-up above it. On hover the image scales to 102% over 400ms; the card frame does not move. No quick-add button, no color swatches — the dial sells itself.

### Hero
**`hero-fullbleed`** — Full-viewport-height imagery of a dial in extreme close-up or of Japanese highland landscapes: Lake Suwa, Shiga Kogen in winter, Shinshu birch forest. A 35% dark overlay keeps `{colors.on-primary}` legible; the collection headline sits in `{typography.display-xl}` at the lower-left third of the frame. A single `button-ghost` CTA sits beneath it. On mobile the headline drops to `{typography.display-md}` and re-anchors to center-bottom.

### Badges
**`season-badge`** — A flat midnight navy tag in `{typography.label-uppercase}` pinned to the top-left corner of product imagery. Used for thematic releases: "SHIZUKUISHI", "SHINSHU", "SUMMER GRADATION". Zero radius; the label reads like a classification code, not a marketing callout.

**`limited-badge`** — Gold fill (`{colors.gold-accent}`) with dark ink text (`{colors.ink}`), identical construction to `season-badge`. Reserved strictly for numbered limited editions; appears on imagery only, never in body copy, to preserve the signal weight.

### Dial Detail Panel
**`dial-detail-panel`** — A horizontal specification row repeated for each dial attribute: case material, crystal, water resistance, movement calibre, power reserve. Label in `{typography.spec-label}` at `{colors.warm-charcoal}` sits above the value in `{typography.body-md}`. A 1px `{colors.hairline}` rule separates each row. The panel sits directly on `{colors.canvas}` as part of the product detail page editorial flow — no card wrapper, no background fill.

### Movement Spec Table
**`movement-spec-table`** — A structured table on `{colors.surface-soft}` listing calibre-level technical data: movement type (Spring Drive / Hi-Beat 36000 / Quartz), oscillation frequency, jewel count, accuracy specification. Column headers in `{typography.spec-label}` at `{colors.warm-charcoal-dark}`; values in `{typography.body-sm}`. Cell borders in `{colors.hairline}`. Appears in an expandable section below the fold — rewarding the collector who wants the full specification, invisible to the casual visitor.

### Collection Filter
**`collection-filter`** — A horizontal strip of uppercase filter labels in `{typography.label-uppercase}` for categories such as "ELEGANCE", "SPORT", "SPRING DRIVE", "HI-BEAT". The active filter gains a 2px bottom border in `{colors.primary}` and text shifts to `{colors.primary}`; inactive labels sit in `{colors.ink}`. No pill background, no chip shape — the underline is the only active indicator, referencing the restraint of Japanese design publication layouts.

### Search Overlay
**`search-overlay`** — A full-width panel descending from the nav bar on search-icon activation. Text input styled with `{colors.primary}` bottom border only, no box border, with placeholder in `{colors.muted}`. Results appear beneath as a plain list in `{typography.body-md}`. The area behind is covered by a navy-tinted scrim (`rgba(0,0,64,0.5)`) that contextualizes the modal state without harsh black contrast.

### Footer
**`footer`** — Full-width midnight navy (`{colors.primary}`) panel. Column headings in `{typography.label-uppercase}` at `{colors.light-gray}` introduce four link groups: Timepieces, Grand Seiko World, Customer Support, Legal. Links in `{typography.body-sm}` at `{colors.on-primary}`. The bottom row carries locale selectors, monochrome social icons, and the Seiko Holdings attribution in `{typography.caption}` at `{colors.light-gray}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `{typography.display-md}` centered at bottom; nav collapses to hamburger flyout in `{colors.primary}`; `dial-detail-panel` switches to vertical label-above-value stack; `collection-filter` becomes a horizontally scrollable strip with no wrapping |
| Tablet | 744–1128px | Two-column product grid; `collection-banner` stacks image above text; nav shows top categories only, sub-items behind "More" overflow; `movement-spec-table` collapses to single-column label:value pairs |
| Desktop | 1128–1440px | Three-column product grid; full `nav-dropdown` with feature image panel visible; `hero-fullbleed` at 100vh with text anchored to lower-left third |
| Wide | > 1440px | Four-column product grid; hero and nav content max-width capped at 1440px with generous lateral padding; `collection-banner` layout locks to image-left-text-right at fixed proportions |

### Touch Targets
- All nav-bar icons padded to minimum 44×44px hit area on mobile
- `collection-filter` labels receive 12px vertical padding on mobile to meet touch minimum
- `product-card` tap area covers the full card surface; no separate tap zone for title vs. image
- `season-badge` and `limited-badge` are display-only overlays with no independent tap target
- `button-primary` and `button-ghost` already satisfy 48px height on all breakpoints

### Collapsing Strategy
- Navigation collapses to hamburger at < 744px; the full-bleed navy flyout maintains primary brand color throughout
- `movement-spec-table` collapses to a single-column label:value accordion on mobile
- `collection-banner` stacks image above text on tablet; image above text with reduced padding on mobile
- `nav-dropdown` feature-image panel is hidden on tablet; sub-category columns reduce to a single scrollable column on mobile
- `dial-detail-panel` shifts from horizontal rows to vertical stacked blocks on mobile, each block separated by `{colors.hairline}`

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; Georgia and Hiragino Mincho ProN are system or bundled fonts, suggesting Grand Seiko may load a licensed serif via CSS not captured in static extraction
- Gold accent `#e6ae06` is present in the extracted palette but its precise semantic scope (limited-edition badge, hover state, price accent) could not be confirmed from static analysis alone
- Several extracted colors — `#d63384`, `#0dcaf0`, `#8bc34a`, `#fcc7c3`, `#b3e5fc` — appear to be Bootstrap utility or debug palette entries and have been excluded from brand tokens
- Exact nav bar height, dropdown panel animation duration, and hover transition timing values are not reliably extractable from static page capture
- Dark mode or high-contrast variant not confirmed; the site may serve region-specific palette variations for Japanese vs. international storefronts
- Grand Seiko wordmark may be an SVG lockup rather than live text; exact logotype weight and size could not be verified
- Price display format (with/without tax notation, currency behavior across locale toggles) was not observable from static extraction
