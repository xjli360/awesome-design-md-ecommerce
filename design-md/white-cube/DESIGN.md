---
version: alpha
name: "White Cube"
source_url: "https://whitecube.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three cuts of Beausite — display for headings, text for navigation and prose, detail for caption and annotation — structure White Cube's site the way a curatorial wall label structures a gallery: the artist's name at scale, the work title one tier below, the medium and date in the smallest layer. The hierarchy is not decorative; it is the design. Against a near-white canvas (#fafafa), cobalt (#003399) arrives as institutional declaration rather than brand color — closer in register to a European museum department plaque than to a commercial gallery eager to be noticed. It appears on primary CTAs, active link states, and selected navigation elements; it does not decorate. The Shopify-powered editions shop introduces a quiet commerce layer that shares identical typographic restraint with every editorial page — no color shift, no marketing register, just product titles and prices in beausite-text at body scale.

  The palette carries unexpected warmth in its secondary register. An orange-sienna (#da532c) surfaces as an event or exhibition alert — the temperature of a 1970s art-world broadsheet, useful because it breaks the cool institutional field without decorating it. Blush (#ffbbbb) and pale straw (#f7eea6) read as seasonal or exhibition-specific color stories, likely originating in catalog or printed matter rather than permanent UI tokens; they soften the system when present without committing to lifestyle brand warmth.

  Full-bleed photography — installation views, artist portraits, surface details — carries the experiential weight that copy cannot. Type sits in a column grid above or below, never competing. Hairlines divide where boxes would crowd; corners are universally sharp ({rounded.none}). The white cube, by definition, has no curves. At mobile, the grid collapses to a single track and generous vertical rhythm preserves the pacing that makes editorial content legible at reading distance. The Shopify scaffold is nearly invisible behind the editorial voice.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aedd"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sienna: "#da532c"
  accent-blush: "#ffbbbb"
  accent-straw: "#f7eea6"
  footer-bg: "#111111"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'beausite-display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "'beausite-display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'beausite-display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'beausite-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'beausite-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'beausite-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'beausite-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'beausite-detail', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  caption-label:
    fontFamily: "'beausite-detail', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'beausite-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'beausite-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  artist-display:
    fontFamily: "'beausite-display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 12px
    height: 44px
    focus:
      borderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
  hero-full-bleed:
    imageObjectFit: cover
    overlayColor: "rgba(0,0,0,0.25)"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.on-primary}"
    captionTypography: "{typography.caption-label}"
    captionColor: "{colors.on-primary}"
  exhibition-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    metaTypography: "{typography.caption}"
    imageAspectRatio: "4/3"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  artist-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.artist-display}"
    detailTypography: "{typography.caption}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
  editions-product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
  event-badge:
    backgroundColor: "{colors.accent-sienna}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  gallery-location-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.ink}"
    height: 44px
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    linkColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption-label}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid cobalt (#003399) rectangle, 44px tall, sharp corners ({rounded.none}), white beausite-text at 14px with 0.04em tracking. Hover darkens to `primary-active` (#002277); disabled bleaches to #99aedd. Used for "Add to Cart" on editions pages and newsletter enrollment — the only surface where the brand's institutional blue becomes an explicit prompt.

**`button-secondary`** — Same geometry and type spec as `button-primary`, white fill with a 1px black border. Hover introduces `surface-soft` (#fafafa) fill. Used for secondary navigation actions, modal dismissal, and any context where cobalt would read as too assertive against an already dark background element.

**`button-text-link`** — No background, no border, primary blue with underline. Used inline within editorial body copy, press links, and catalogue entries. Not used in the nav or footer, where plain unhighlighted text carries links.

### Inputs

**`text-input`** — Hairline border (#dddddd), no radius, 44px height matching button geometry for vertical rhythm consistency. Focus upgrades the border to ink (#000000). Placeholder runs in muted (#666666). Appears in the search field, newsletter signup, and Shopify checkout fields; all share the same spec so the form layer reads as a single consistent system.

### Navigation

**`nav-bar`** — 60px white bar with a hairline bottom border, White Cube logotype typeset in beausite-display at 28px weight 300 on the left, secondary links (Artists, Exhibitions, Gallery, Editions, Press) in beausite-text nav-link at 14px on the right. Active states render the link in cobalt; no hover underline, no mega-menu, no imagery in the navigation layer. At mobile, all secondary links collapse behind a hamburger trigger; the logotype remains visible.

### Cards

**`exhibition-card`** — 4:3 image above a text block, no radius anywhere. Title in beausite-display at display-sm (28px weight 300), exhibition dates and location in caption (12px, beausite-detail). An `event-badge` chip in accent-sienna (#da532c) can overlay the image corner to mark current shows. Full-width at mobile; 2-up at tablet; 3-up at desktop.

**`artist-card`** — 3:4 portrait-orientation image, artist name in beausite-display at 18px (artist-display), gallery affiliation note in caption-label. Grid: 1-up mobile, 2-up tablet, 3-up or 4-up desktop. No hover overlay; the card is a directory entry, not a sales surface.

**`editions-product-card`** — Square 1:1 image above text. Title in title-sm (beausite-text, 16px), price in body-sm, edition size and medium in caption. The same hairline grid rules that structure editorial pages govern the shop index; there is no visual mode-switch between the gallery and commerce experience.

### Layout Blocks

**`hero-full-bleed`** — Full-viewport-width image with a 25% black scrim (rgba(0,0,0,0.25)). Headline in beausite-display at display-xl (64px, weight 300), white; attribution or exhibition subtitle in caption-label, white. Used on the homepage and major exhibition launch pages. At mobile the headline steps down to display-md (40px) and the scrim lightens to ensure legibility without a hard override.

**`event-badge`** — Sharp rectangular chip in accent-sienna (#da532c), white caption-label text (11px uppercase, 0.08em tracked), 3px top/bottom 8px left/right padding. Overlaid on exhibition cards and hero images to indicate current or forthcoming shows. The sienna is the only warm interruption of the cobalt-and-white field.

**`gallery-location-tag`** — Small surface-soft chip in caption-label, muted text, no radius. Appears alongside exhibition cards and artist detail pages to identify which gallery space (Bermondsey, Mason's Yard, Hong Kong, New York, Paris, Seoul). Not a navigation element — purely informational.

**`section-divider`** — 1px hairline rule at 64px ({spacing.section}) vertical margin. The primary structural separator between editorial modules, used in lieu of background color changes or card borders. The entire page rhythm is built on hairlines and vertical space.

**`footer`** — Dark background (#111111) with white body-sm text and white links. Organized in columns: gallery locations list, navigation links repeated from nav, newsletter signup using `text-input` (border-color updated to surface-soft for dark context), and social links in caption-label. Cobalt is not used in the footer; there is no color accent against the dark field.

**`search-input`** — Hairline-bordered field with a small ink-colored search icon, 44px, no radius. Appears inline within the nav at desktop; at mobile it expands to a full-width overlay row beneath the collapsed nav bar, dismissible via an ×.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to logotype + hamburger; hero headline steps from display-xl (64px) to display-md (40px); exhibition and artist cards go full-width; search becomes full-width overlay row |
| Tablet | 744–1128px | Two-column grids for exhibition and artist cards; nav links remain visible but may truncate to icons; hero headline remains at display-xl |
| Desktop | 1128–1440px | Three-column exhibition grid; four-column artist grid; nav fully expanded; section padding widens to maintain white space proportions |
| Wide | > 1440px | Max-width container (~1400px) centered; column gutters widen; hero image height caps at 90vh to prevent excessive bleed on ultra-wide screens |

### Touch Targets

- All interactive elements (buttons, inputs, nav links, card taps) are minimum 44px in height
- `nav-link` items at mobile receive 48px tap targets via vertical padding expansion in the hamburger menu
- `event-badge` and `gallery-location-tag` chips are informational only at mobile; no tap target required unless linked

### Collapsing Strategy

- Navigation: logotype stays; all secondary links move into a full-screen slide-in drawer at mobile, using the same nav-link typography at 20px for legibility
- Exhibition card grid: 3-up → 2-up → 1-up as viewport narrows; card aspect ratio and corner sharpness are preserved at all breakpoints
- Hero type: display-xl (64px) steps to display-md (40px) at mobile; letter-spacing tightens proportionally; the scrim opacity increases slightly to maintain contrast on smaller images
- Footer columns: 4-column grid collapses to 2-column at tablet, single-column stacked at mobile with the newsletter input promoted above the link lists

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font weights for each Beausite cut are not confirmed from extraction; weight 300 (display) and 400 (text/detail) are inferred from the gallery's known institutional aesthetic — actual weights may differ
- The exact role split between beausite-display, beausite-text, and beausite-detail is inferred from naming convention; no CSS variable declarations were captured confirming which cut maps to which use
- Accent colors (#ffbbbb blush, #f7eea6 pale straw) origin is unclear — may be exhibition-specific imagery bleeding into the extracted palette rather than permanent system tokens; treat as contextual only
- No confirmed spacing scale extracted; values follow an 8px base grid consistent with Shopify defaults
- No confirmed dark-mode tokens; the footer's #111111 dark field is the only dark surface in the extracted data
- Interactive state colors (hover, focus rings) beyond the primary button are not confirmed; values are extrapolated from the cobalt primary with standard darkening conventions
- Logo lockup size and positioning on the nav bar were not directly measured; 28px display-sm is estimated from visual proportion
