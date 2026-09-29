---
version: alpha
name: "Xavier Hufkens"
source_url: "https://www.xavierhufkens.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The warm parchment canvas — #f7f8f5 set against near-black #191919 — signals something other than clinical white-cube orthodoxy: Xavier Hufkens presents contemporary art on a ground with just enough warmth to recall catalogue stock rather than a sterile screen. BellBQ carries the display hierarchy, a serif with editorial authority suited to artist names and exhibition titles; Messina handles navigation and running text, its clean proportions sustaining long biographies and exhibition histories without fatigue. The palette is almost entirely neutral — a descending sequence from #191919 through #414141, #878787, #aeaeae, and #dcdcdc arriving at the warm #f7f8f5 ground — with no chromatic accent evident in the extracted tokens beyond #007aff, an iOS system default that surfaces in focus and link states rather than as intentional brand voltage. This restraint is deliberate: the gallery subordinates its graphic identity to the work it represents, letting a Luc Tuymans grey or a Francis Alÿs blue carry whatever chromatic charge a page holds rather than competing with it. Navigation runs in controlled tracking across the top against {colors.canvas}, collapsing to a minimal trigger on mobile without losing horizontal discipline. Artwork cards carry hard corners ({rounded.none}), maintaining the rectilinear discipline of the gallery hang. The wall-label component — artist name set in {typography.display-md} BellBQ, work title italicised in {typography.title-md} Messina, medium and dimensions in {typography.caption} — echoes the physical labels mounted at the Brussels spaces on Rue Van Eyck. Interactive states shift through opacity and {colors.hairline} border changes rather than colour swaps, keeping the interface chrome subordinate to the art on display. The presence of swiper-icons in the font stack points to a horizontal exhibition-browse rhythm that models the act of moving between rooms.

colors:
  primary: "#191919"
  primary-active: "#000000"
  primary-disabled: "#878787"
  ink: "#121212"
  body: "#414141"
  muted: "#878787"
  muted-soft: "#aeaeae"
  hairline: "#dcdcdc"
  hairline-soft: "#ececec"
  canvas: "#f7f8f5"
  surface-soft: "#f7f8f5"
  surface-card: "#ffffff"
  surface-mid: "#d9d9d9"
  on-primary: "#f7f8f5"
  scrim: "#191919"
  link: "#007aff"

typography:
  display-xl:
    fontFamily: "'BellBQ', Georgia, 'Times New Roman', Times, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'BellBQ', Georgia, 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'BellBQ', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    fontStyle: italic
  title-sm:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    fontStyle: italic
  body-md:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-label:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  overline:
    fontFamily: "'Messina', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 40px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 40px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    logoTypography: "{typography.display-sm}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  artwork-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageRounded: "{rounded.none}"
    artistTypography: "{typography.body-md}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    metaColor: "{colors.muted}"
    gap: "{spacing.sm}"
    imageHoverOpacity: 0.9
  hero-exhibition:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    metaTypography: "{typography.overline}"
    rounded: "{rounded.none}"
    imageAspectRatio: "16/9"
    overlayOpacity: 0.4
    padding: "0"
  wall-label:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    artistTypography: "{typography.display-md}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    mutedColor: "{colors.muted}"
    gap: "{spacing.xs}"
  artist-list-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  exhibition-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    dividerColor: "{colors.muted}"
    padding: "{spacing.xxl} 0"
  image-slideshow:
    backgroundColor: "{colors.scrim}"
    rounded: "{rounded.none}"
    controlColor: "{colors.on-primary}"
    paginationColor: "{colors.muted-soft}"
    paginationActiveColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — A flat near-black (#191919) rectangle with zero rounding ({rounded.none}) and uppercase {typography.button-md} lettering at 0.1em tracking. Hover deepens to #000000 with no transition delay — the response is immediate, consistent with the gallery's preference for direct rather than animated feedback. Disabled state uses {colors.primary-disabled} (#878787) fill with {colors.canvas} text.

**`button-secondary`** — Same height and typography as primary but rendered as an outlined ghost: transparent fill, 1px {colors.primary} border, {colors.primary} text. Used for secondary actions (e.g. "Request Information" paired with a primary "View Exhibition"). On hover, fill picks up a thin wash of {colors.surface-mid} without the border changing.

**`button-ghost`** — Transparent with a {colors.hairline} border and {colors.muted} text in {typography.button-md}. Serves filter interfaces and archive pagination where deselected states must recede without disappearing entirely.

### Text Input
**`text-input`** — Zero-radius field with a full 1px {colors.hairline} border on contact and newsletter forms; the search overlay variant strips three sides to a bottom-only border for a cleaner inline feel. Focus upgrades the border to {colors.primary}. No shadow, no background shift — the gallery's orthogonal grid holds everywhere.

### Nav Bar
**`nav-bar`** — 56px tall on a {colors.canvas} ground, logotype "Xavier Hufkens" in {typography.display-sm} BellBQ at left. Primary items (Artists, Exhibitions, News, Contact) sit at equal weight in {typography.nav-label} with a hover underline only — no bold active state, no coloured indicator. A 1px {colors.hairline} bottom border separates the bar from page content. On mobile, all items collapse behind a single text or icon trigger into a full-screen overlay.

### Artwork Card
**`artwork-card`** — Full-width, hard-cornered image followed by a compact typographic stack: artist name in {typography.body-md} {colors.ink}, work title in {typography.title-md} italic Messina, medium/year in {typography.caption} {colors.muted}. No hover overlay, no drop shadow. The image fades to 90% opacity on hover via a direct opacity change — the UI recedes, the art advances.

### Hero Exhibition
**`hero-exhibition`** — Full-bleed 16:9 image with a 40% {colors.scrim} overlay anchoring the exhibition title in {typography.display-xl} BellBQ and the date range in {typography.overline} uppercase. The artist name runs above the title in {typography.display-sm} at reduced opacity. On mobile the aspect ratio adjusts to 4:3, the title steps down to {typography.display-md}, and vertical padding compresses to keep the image readable.

### Wall Label
**`wall-label`** — A pure typographic component that mirrors the physical gallery convention: artist name in {typography.display-md} BellBQ, work title in {typography.title-md} italic Messina, then medium, dimensions, and year in {typography.caption} at {colors.muted}. No container, no border, no background fill — clean hierarchy against {colors.canvas}, with {spacing.xs} gap between each line of metadata.

### Artist List Item
**`artist-list-item`** — Single-row entry: artist name in {typography.body-md} {colors.ink} at full width, followed by a {colors.hairline} bottom rule. Padding is {spacing.base} top and bottom, flush to the grid horizontally. No thumbnail at list level — clicking opens the individual artist page with biography and full artwork grid.

### Exhibition Badge
**`exhibition-badge`** — A compact tag in {typography.overline} uppercase with a 1px {colors.hairline} border and no background fill, labelling "Current", "Past", or "Upcoming" status. The border carries the distinction without any colour coding, keeping the palette rigorously neutral even in state-signalling contexts.

### Search Bar
**`search-bar`** — Full-width input triggered from the nav, 48px tall, with {typography.body-md} text and a bottom-border-only {colors.hairline} line. Results appear below in {typography.body-sm} separated by {colors.hairline} dividers. No radius anywhere. Closing the search collapses the bar immediately without animation.

### Footer
**`footer`** — Near-black {colors.primary} background, {colors.on-primary} text in {typography.body-sm}. Gallery address, newsletter field (ghost input style against the dark ground with an {colors.on-primary} bottom border), and social links arranged in a columnar grid. A {colors.muted} divider separates address from nav columns. Padding is {spacing.xxl} top and bottom.

### Image Slideshow
**`image-slideshow`** — Swiper-driven full-bleed carousel for exhibition views and artist portfolios. No border-radius on images. Pagination dots in {colors.muted-soft}, active dot in {colors.on-primary}. Arrow controls are minimal glyph-only buttons in {colors.on-primary} against the dark image region. The component suggests a lateral browse rhythm modelling the act of moving between gallery rooms.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to logotype + icon trigger with full-screen overlay; hero shifts to 4:3 aspect ratio; wall-label steps down one type scale; footer stacks to single column |
| Tablet | 744–1128px | Two-column artwork grid; nav items visible but condensed at reduced tracking; hero holds 16:9; wall-label retains full label detail inline |
| Desktop | 1128–1440px | Three- or four-column artwork grid; full horizontal nav at 56px; exhibition detail renders in side-by-side image/text layout; section padding expands to {spacing.section} |
| Wide | > 1440px | Max content width ~1400px centred; four-column grid; section padding increases to 96px; hero image expands with typographic overlay anchored to fixed vertical position |

### Touch Targets
- All nav items carry minimum 44px tap height via vertical padding expansion
- Artwork cards are full-width tap targets on mobile with no fragmented inline zones
- Footer links maintain minimum {spacing.lg} vertical gap to prevent mis-taps on dense address blocks
- Search trigger in nav expands to 44×44px touch area with a transparent padding halo

### Collapsing Strategy
- Primary nav collapses behind a single text or icon trigger on mobile into a full-screen overlay with the same {typography.nav-label} items at increased line height
- Artwork grid reflows 4-col → 3-col → 2-col → 1-col across breakpoints without gutters changing proportionally
- Exhibition badge labels may abbreviate to single initials (C / P / U) below 400px viewport width
- Footer multi-column layout stacks to a single column with increased top padding at mobile breakpoint; newsletter input moves to the top of the stack

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- BellBQ weight variants and optical sizes are not confirmed from extraction; the gallery likely uses a single Regular 400 weight throughout display usage
- Messina variant is unresolved — only the family name was extracted; Messina Sans is assumed based on gallery UI convention, but Messina Modern (a mixed-axis face) is plausible for certain editorial uses
- No explicit hover, focus, or active colour tokens were extractable; all interactive states are inferred from neutral-palette logic and opacity shifts
- #007aff appears to be a browser or iOS system default and is almost certainly not a deliberate brand colour; it may surface only in default anchor focus rings
- Exact grid gutter widths and column counts are not confirmed; values are inferred from gallery-site convention
- Dark-mode or inverted-palette variants could not be confirmed despite the near-black primary; no separate token set was found in extraction
- No confirmed icon library or SVG sprite system beyond swiper-icons; navigation and UI icons are uncharacterised
