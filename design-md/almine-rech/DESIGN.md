---
version: alpha
name: "Almine Rech"
source_url: "https://www.alminerech.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep royal blue (#003399) takes every primary link and CTA — a deliberate assertion against the all-black neutrality that dominates institutional gallery sites. The canvas holds at pure white, the meta theme-color #ffffff enforced so exhibition photography arrives without interference, applying to the screen the same logic a white-cube room applies to hung work. Text runs in #08191b, a near-black with a faint oceanic undertone that separates it from true black and from the charcoal grays (#323232, #595959, #7d7d7d) managing secondary and tertiary hierarchy. Cool gray #cccdd5 handles divider and surface-muted duty, while the light blue tint #ddeeff surfaces as a hover-state wash behind interactive elements — focus feedback that adds no new hue to the visual field.

  The typographic system pairs Akkurat, a geometric grotesque carrying navigation labels and metadata, with Cambon, a contemporary serif commanding editorial display heads and artist names. The sans handles structural chrome at 12–14px; the serif commands at 24–48px, institutional precision and editorial ambition resolved in one stack. Spacing follows gallery-hang logic: sections breathe at {spacing.section}, image grids take generous margins, and columns collapse early to preserve image scale over text density. Rounded corners are essentially absent — {rounded.none} on exhibition cards and artist tiles enforces the white-cube hard-edge sensibility; only inputs and micro-labels use {rounded.xs}.

  Navigation carries a multi-city architecture — Paris, Brussels, London, New York — so the top bar operates as a location-aware selector as much as a site map. Footer type drops to Akkurat caption scale against an #08191b ground, the chrome receding so the work holds center. Accent orange (#ff7d00) and green (#007d00) surface exclusively as status indicators — sold, on-view, available — never as structural brand color. The system is editorial-institutional at every scale: sparse, image-first, where blue means act here and everything else steps aside.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#cccdd5"
  ink: "#08191b"
  body: "#323232"
  muted: "#595959"
  muted-soft: "#7d7d7d"
  hairline: "#e1e1e1"
  hairline-soft: "#f1f1f1"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-muted: "#cccdd5"
  on-primary: "#ffffff"
  accent-hover: "#ddeeff"
  status-orange: "#ff7d00"
  status-green: "#007d00"
  gallery-dark: "#343957"

typography:
  display-xl:
    fontFamily: "Cambon, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Cambon, Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Cambon, Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  artist-name:
    fontFamily: "Cambon, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "Akkurat, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.primary}"
    activeLinkColor: "{colors.primary}"
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.artist-name}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    statusTypography: "{typography.label-upper}"
    gap: "{spacing.sm}"
  artist-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    nameTypography: "{typography.display-sm}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    imageAspectRatio: "1/1"
  hero-full:
    backgroundColor: "{colors.gallery-dark}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.hairline}"
    minHeight: 560px
    overlayOpacity: 0.3
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  location-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.canvas}"
  press-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  status-badge-available:
    backgroundColor: "{colors.status-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  status-badge-sold:
    backgroundColor: "{colors.status-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  status-badge-on-view:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  artwork-detail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    artistTypography: "{typography.display-sm}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted-soft}"
    dividerColor: "{colors.hairline}"
    imageMaxWidth: "60%"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    padding: 10px 16px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Royal blue (#003399) fill, white text, zero border-radius, Akkurat 14px/500 weight at 44px tall. Active state deepens to `{colors.primary-active}` (#002277). Disabled collapses to `{colors.primary-disabled}` cool gray with muted text, preserving layout weight. Used on enquiry forms, newsletter sign-up, and exhibition CTAs.

**`button-secondary`** — Ink-bordered outline on white canvas, matching primary dimensions at 44px. Paired alongside primary on artwork detail pages (e.g. "Add to Wishlist" beside "Enquire"). Border steps to `{colors.ink}` on hover with no fill change.

**`button-ghost`** — Transparent ground, `{colors.primary}` text, underline decoration. Used for inline contextual links in editorial copy and press entries — keeps the action visible without the weight of a full button chrome.

### Text Input

**`text-input`** — Sharp-cornered, `{colors.hairline}` border at rest, stepping to `{colors.ink}` border on focus. No rounded radius — consistent with the card and tile geometry of the rest of the system. Placeholder in `{colors.muted-soft}`, 48px height, Akkurat body-md.

### Navigation Bar

**`nav-bar`** — White canvas, 64px tall, ruled at the bottom with a single `{colors.hairline}` line. City/location links — Paris, Brussels, London, New York — sit in Akkurat 14px alongside section anchors: Exhibitions, Artists, Art Fairs, Press. Links shift to `{colors.primary}` on hover and active. The wordmark anchors left; a hamburger handles overflow at tablet and below.

### Exhibition Card

**`exhibition-card`** — Flush-edge, sharp-cornered portrait tile at 4:5 ratio. Artist name in Cambon `{typography.artist-name}`, date range and location in Akkurat `{typography.caption}` at `{colors.muted}`. No shadow, no border, no hover lift — only a `{colors.primary}` underline on the title link at hover. Status badges render at top-left of the image frame.

### Artist Tile

**`artist-tile`** — Square crop, name in Cambon `{typography.display-sm}`, bio extract or birth year in `{typography.caption}` at `{colors.muted}`. On image hover, a `{colors.gallery-dark}` strip emerges at the bottom with a `{typography.label-upper}` "View Works" label in `{colors.on-primary}`. Zero radius throughout.

### Full-Bleed Hero

**`hero-full`** — Full-viewport exhibition hero. When photography is absent the ground is `{colors.gallery-dark}` (#343957); image-backed heroes carry a 0.3-opacity dark overlay. Headline in Cambon `{typography.display-xl}` in `{colors.canvas}`, subhead in Akkurat `{typography.body-md}` at `{colors.hairline}`, minimum 560px tall. The CTA button renders `{colors.primary}` fill.

### Location Pill

**`location-pill`** — Uppercase Akkurat 11px on `{colors.surface-soft}`, `{rounded.xs}` corners, for filtering exhibitions or artworks by city. Active state inverts to `{colors.ink}` background / `{colors.canvas}` text. Appears above exhibition grids and on art fair pages.

### Press Tag

**`press-tag`** — Uppercase Akkurat 11px label on `{colors.surface-soft}`, zero radius, categorizing press entries by type (Interview, Review, Preview, Feature). Sits above the article headline inline with the publication date.

### Status Badges

**`status-badge-available`** / **`status-badge-sold`** / **`status-badge-on-view`** — Three micro-label variants in `{colors.status-green}`, `{colors.status-orange}`, and `{colors.primary}` respectively. Uppercase Akkurat 11px, no radius, 2×8px padding. These are the only contexts where orange and green enter the UI; they render on artwork listings and exhibition card frames.

### Artwork Detail

**`artwork-detail`** — Two-column layout: image at 60% of container left, metadata right. Artist name in Cambon `{typography.display-sm}`, work title in `{typography.display-md}`, dimensions/medium/year in Akkurat `{typography.body-sm}` at `{colors.muted}`. Dividers use `{colors.hairline}`. Enquiry CTA (`button-primary`) anchors below metadata. Provenance and caption lines run `{typography.caption}` at `{colors.muted-soft}`.

### Search Bar

**`search-bar`** — Flush-cornered on `{colors.surface-soft}`, border steps from `{colors.hairline}` to `{colors.primary}` on focus. Akkurat body-md, 44px height. Used in the global header search overlay and the artists/exhibitions index filter bar.

### Footer

**`footer`** — `{colors.ink}` (#08191b) ground, `{colors.hairline}` body text, `{colors.hairline-soft}` links stepping to `{colors.canvas}` on hover. Four-column grid (Gallery, Artists, Exhibitions, Legal) over a mid-rule, social icons row beneath. Akkurat caption scale throughout, `{spacing.xxl}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; hero height 360px; exhibition cards use 3:4 ratio; artwork detail stacks (image full-width above metadata) |
| Tablet | 744–1128px | Two-column exhibition grid; nav shows primary sections, city links move to a dropdown; hero 460px; artwork detail remains stacked |
| Desktop | 1128–1440px | Three-column exhibition grid; full nav with all city links visible; two-column artwork detail; hero 560px |
| Wide | > 1440px | Container capped ~1320px centered; four-column exhibition grid; hero scales to 680px; extra whitespace in side margins |

### Touch Targets

- All nav links and icon buttons minimum 44×44px tap area
- Exhibition card tap target covers full card footprint (image + text block)
- Location pills padded to 36px minimum height on mobile
- Status badges padded to 32px minimum vertical touch zone in mobile list views

### Collapsing Strategy

- Four city links in desktop nav merge into a "Locations" dropdown at tablet and below
- Exhibition grid falls from three columns to two at 744px, then one column at 480px
- Artwork detail two-column layout stacks at 744px; image goes full-width first, metadata below
- Press archive switches from three-column card grid to single-column list at 480px
- Footer four-column grid collapses to two columns at 744px, then one column at 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav height and wordmark dimensions not extractable; 64px inferred from visual density
- `primary-active` (#002277) and `primary-disabled` (#cccdd5 repurposed) are derived — extracted palette does not include explicit interaction-state values for the primary blue
- Hover/focus animation timing and easing curves not captured from static extraction
- Dark-mode support unconfirmed; meta theme-color is #ffffff only
- Grid gutter widths and exact breakpoint pixel values are estimated from common gallery-site patterns, not extracted from source
- `Akkurat` is a licensed Lineto grotesque; fallback chain Arial/Helvetica applies when webfont is unavailable
- `Cambon` weight variants (italic, bold availability) and licensing tier not confirmed from extraction
- Newsletter modal design and cookie consent overlay styling not captured
