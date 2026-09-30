---
version: alpha
name: "The Poster Club"
source_url: "https://theposterclub.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Chronicle Display serifs at 60px, set against a white ground with near-zero decoration, make clear that the artwork — not the interface — is what The Poster Club sells. Every product page opens with the print spanning the full viewport width before navigation or metadata appear in scroll. The brand divides typographic labor between exactly two families: Chronicle Display (A and B variants) carries artist names, collection titles, and editorial headlines in a high-contrast oldstyle serif, while Visuelt Regular handles all functional text — prices, filter labels, navigation links — in a spare geometric sans-serif that never competes with the work on display. The primary accent is a deep royal navy `#003388`, reserved almost entirely for the "Add to Cart" CTA and active link states; it reads as institutional and deliberate rather than punchy, matching the brand's gallery-adjacent positioning. Corners are uniformly sharp — `{rounded.none}` on product cards, filter chips, image frames, and input fields — giving every layout the feel of a well-matted mounted print rather than a rounded-corner e-commerce template. The palette retreats to studied neutrals: `#f0f0f0` surface backgrounds, `#808080` mid-tone muted text, `#949494` hairlines, `#1e1f26` near-black ink. Product cards run tall at 4:5 aspect ratio, the image occupying roughly 80% of card height, with a minimal two-line footer strip showing artist name in Chronicle Display italic and price in Visuelt. Size selectors appear as inline text-button rows rather than dropdowns, and frame options use an underline indicator rather than a styled toggle — keeping the purchase flow as legible and uncluttered as the prints themselves.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8faad4"
  ink: "#1e1f26"
  body: "#32373c"
  muted: "#808080"
  hairline: "#949494"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#efefef"
  on-primary: "#ffffff"
  sale-accent: "#444444"

typography:
  display-xl:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  artist-name:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  button-md:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  collection-label:
    fontFamily: "'visuelt-regular', 'Gotham A', 'Gotham B', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoTypography: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    imageFit: cover
    footerPadding: "{spacing.sm} 0"
    artistTypography: "{typography.artist-name}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    hoverOverlay: "rgba(255,255,255,0.5)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    layout: fullbleed-image-left-text-right
    maxHeight: 680px
    textColumnPadding: "{spacing.section} {spacing.xl}"
  artist-feature:
    backgroundColor: "{colors.surface-soft}"
    nameTypography: "{typography.display-sm}"
    nameColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xl}"
  collection-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.collection-label}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  collection-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"
    height: 36px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  frame-selector:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.ink}"
    activeUnderline: "2px solid {colors.ink}"
    layout: inline-button-group
    gap: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: none
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    height: 44px
    iconColor: "{colors.muted}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    width: 420px
    borderLeft: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
  sale-badge:
    backgroundColor: "{colors.sale-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.collection-label}"
    padding: "{spacing.section} {spacing.xl}"
    columns: 4

## Components

### Buttons
**`button-primary`** — A sharp-cornered (`{rounded.none}`) navy `#003388` block, 48px tall, uppercase 13px Visuelt at 0.08em tracking. Used exclusively for "Add to Cart" and checkout progression; its institutional weight signals transaction, not exploration. Active state deepens to `{colors.primary-active}` `#002266`; disabled renders in `{colors.primary-disabled}`, a desaturated periwinkle that reads muted without disappearing.

**`button-secondary`** — Identical proportions with white fill and a 1px `{colors.ink}` border. Carries "View in Room", wishlist actions, and editorial CTAs. Hover inverts to `{colors.ink}` fill and `{colors.on-primary}` text — a stark, clean state change with no intermediate color.

**`button-text`** — Underlined `{typography.body-sm}` link for low-priority actions: "See all works by this artist", newsletter fine print, editorial navigation. No background, no border.

### Text Inputs
**`text-input`** — Flat sharp-cornered field on `{colors.canvas}` with a 1px `{colors.hairline}` border at rest. Focus state replaces the hairline with a full-weight `{colors.ink}` border — no glow, no color shift, no animation flourish. Placeholder text sits in `{colors.muted}` Visuelt.

### Navigation
**`nav-bar`** — 64px white bar with a whisper-thin `{colors.hairline-soft}` bottom rule. The wordmark sits left in Chronicle Display at display-sm scale; nav links — "Shop", "Artists", "Collections", "New Arrivals", "Sale" — run as 13px uppercase Visuelt with 0.04em tracking. Cart count and currency selector anchor the right. On scroll past the hero, a soft box-shadow appears without changing the bar's color.

### Product Cards
**`product-card`** — The primary commerce unit: a tall 4:5 image (no border, shadow, or radius) above a two-line footer. Artist name renders in Chronicle Display italic 14px; print title and right-aligned price appear below in 13px Visuelt. On hover, a white translucent scrim fades in over the image with a centered "Quick add" button in `button-secondary` style. The card never introduces a background color — the artwork sits directly on the page `{colors.canvas}`.

### Hero Banner
**`hero-banner`** — Full-bleed image left, editorial column right. The headline runs at `{typography.display-xl}` Chronicle Display (often a single artist name or collection title), a `{typography.body-md}` subtitle line below, then a `button-secondary` CTA. The image bleeds to the browser edge; the right column carries no background, reading straight off the white page. Maximum height 680px on desktop.

### Artist Feature
**`artist-feature`** — Section-level component on artist pages and curated landing pages. Pale `{colors.surface-soft}` field, artist name at `{typography.display-sm}` Chronicle Display, two-to-three sentence Visuelt `{typography.body-md}` bio below, then a grid of four to six product cards. No colored accents or decorative rules.

### Collection Tags & Badges
**`collection-tag`** — An 11px uppercase Visuelt label inside a 1px `{colors.ink}` border box, used as both a filter chip and editorial categorization tag. No fill at rest; `collection-tag-active` inverts to `{colors.ink}` fill. The border alone carries the weight.

**`sale-badge`** / **`new-badge`** — Flat rectangular patches with no radius, placed as absolute overlays at the top-left corner of product card images. Sale uses dark `{colors.sale-accent}` to avoid the promotional loudness of red; New uses `{colors.ink}`.

### Size & Frame Selectors
**`size-selector`** — A horizontal row of equal-width text buttons ("30×40", "50×70", "70×100", etc.) separated by 1px `{colors.hairline}` borders. Selected size inverts to `{colors.ink}` fill. All options display simultaneously — no dropdown, no modal.

**`frame-selector`** — Adjacent text labels ("No Frame", "Natural Wood", "Black") with an `{colors.ink}` 2px underline indicator on the active choice. Background stays `{colors.canvas}` throughout; the underline carries all selection state without adding visual weight.

### Search
**`search-bar`** — Activates as a full-width `{colors.surface-soft}` bar spanning the header zone, with a magnifier icon in `{colors.muted}` at left and a dismiss cross at right. No visible border. As the user types, an instant-result dropdown surfaces artist names and print titles before a full results page renders.

### Cart Drawer
**`cart-drawer`** — A 420px right-side overlay on `{colors.canvas}` separated from the page by a single `{colors.hairline-soft}` left border. Title in `{typography.title-md}`; item rows show a square thumbnail, artist name, size and frame selection summary, and price in `{typography.price-display}`. A full-width `button-primary` "Checkout" anchors the bottom above the fold.

### Footer
**`footer`** — The negative-space inversion of the site: `{colors.ink}` field with `{colors.canvas}` text. Four columns (Shop, Artists, About/Press, Newsletter) with column headings in `{typography.collection-label}` uppercase and links in `{typography.body-sm}`. No colored accent elements — monochrome throughout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; hero stacks image above text; size-selector scrolls horizontally on overflow; cart drawer becomes full-screen overlay |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only, sub-categories hidden; hero maintains split but text column widens to 50% |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero at full 680px height with full-bleed image left |
| Wide | > 1440px | Four-column product grid; all content sections max-width 1440px centered with equal side margins |

### Touch Targets
- All button heights minimum 44px on mobile
- Size-selector buttons expand to 44px tap height on mobile via padding
- Cart icon and hamburger menu hit areas padded to 48×48px
- Product card tap target extends across full card including footer text strip
- Frame-selector labels spaced minimum 44px apart vertically on mobile stacked layout

### Collapsing Strategy
- Navigation links collapse into a full-screen slide-in drawer on mobile, not a dropdown
- Artist feature section switches from side-by-side to stacked at tablet breakpoint and below
- Cart drawer becomes a full-screen bottom sheet at < 744px
- Footer collapses from 4-column to 2-column at tablet, single accordion at mobile
- Hero image aspect ratio shifts from 16:9 landscape to 4:5 portrait crop on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The majority of extracted hex colors appear to be WordPress Gutenberg block editor palette presets (`#00d084`, `#0693e3`, `#ff9900`, `#0757fe`, `#1ea0c3`, etc.) and social media brand colors (`#5865f2` Discord, `#0866ff` Facebook, `#ea4434` Google); only `#003388`, `#808080`, `#949494`, `#f0f0f0`, `#32373c`, `#1e1f26`, and `#efefef` are treated as brand-native
- Whether `#003388` is confirmed brand primary or also an editor preset could not be determined from static extraction alone — it is the most distinctive non-generic color in the list and fits the brand's Nordic editorial register
- Exact font weights for Chronicle Display variants not confirmed; weight 400 assumed throughout as consistent with high-end editorial minimal aesthetics
- Frame material color swatches (natural wood, walnut, white, black frame hex values) are absent from the extracted palette
- Epicene Text Bold appears in the font stack but its usage context — whether for pull quotes, editorial long-form, or specific page types — could not be confirmed
- Animation and transition timing values (hover fade duration, drawer open easing) not captured in static extraction
- Grid gutter width and exact column proportions not confirmed from extraction
