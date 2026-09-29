---
version: alpha
name: "Gladstone Gallery"
source_url: "https://www.gladstonegallery.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every surface on Gladstone Gallery's site reads as a prepared wall — the near-white canvas (#f8fafa) and hairline grays (#eaeaea, #dae2e2) replicate the white-box gallery interior with such fidelity that the interface itself becomes exhibition space. The single chromatic departure is a muted teal-slate (#647b7d), a color that reads neither green nor gray but occupies the precise frequency of mineral pigment — linen pressed against stone. It appears in navigation links and interactive states without ever asserting itself as a brand voltage; the gallery withholds that kind of declaration. Frame Head carries display text: an editorial face whose letterforms carry the slight authority of a museum label, spaced generously and set at low weight so the white field around each headline is as active as the type itself. Basel Grotesk runs body copy and UI chrome — a contemporary grotesque with enough optical neutrality to disappear into caption text and emerge again in navigation without tonal inconsistency. Buttons have no radius; every interactive element sits flush to a rectangular boundary, echoing the orthogonal hang of framed work. The spacing system opens wide at section level, using {spacing.section} and above to create the breath between content blocks that a gallery visitor would read as contemplation distance. Color roles compress to near-monochrome: lighter teal (#b2c4c5) marks hover and selection states, #dae2e2 defines soft surface boundaries, and deep teal-slate serves as the sole accent. There are no gradients, no shadows with color, no decorative motifs — only type, image, and the deliberate emptiness between them.

colors:
  primary: "#647b7d"
  primary-active: "#4f6163"
  primary-disabled: "#b2c4c5"
  ink: "#1a1a1a"
  body: "#2e2e2e"
  muted: "#647b7d"
  muted-soft: "#b2c4c5"
  hairline: "#eaeaea"
  hairline-soft: "#dae2e2"
  canvas: "#f8fafa"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  surface-teal: "#dae2e2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  selection: "#b2c4c5"

typography:
  display-xl:
    fontFamily: "'Frame Head', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Frame Head', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Frame Head', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Frame Head', Georgia, serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-upper:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Basel Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  artist-name:
    fontFamily: "'Frame Head', Georgia, serif"
    fontSize: 16px
    fontWeight: 300
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
  section-lg: 96px
  section-xl: 128px

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 40px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    gap: "{spacing.md}"
    titleTypography: "{typography.artist-name}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    border: none
  hero-fullbleed:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    padding: "{spacing.section-xl} {spacing.xl}"
    imagePosition: cover
    overlayColor: "transparent"
  exhibition-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/2"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.label-upper}"
    metaColor: "{colors.muted}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    gap: "{spacing.base}"
  artist-label:
    textColor: "{colors.ink}"
    typography: "{typography.artist-name}"
    secondaryTypography: "{typography.caption}"
    secondaryColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  section-header:
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.md}"
  press-item:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    typography: "{typography.body-sm}"
    sourceLabelTypography: "{typography.label-upper}"
    sourceLabelColor: "{colors.muted}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  fair-badge:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  image-caption:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    marginTop: "{spacing.sm}"
    borderLeft: "2px solid {colors.hairline-soft}"
    paddingLeft: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — Rectangular with zero radius (`{rounded.none}`), background in teal-slate (#647b7d), text in white using uppercase Basel Grotesk at 12px with generous tracking. Hover darkens to #4f6163; disabled falls to the lighter teal (#b2c4c5), maintaining chromatic continuity rather than going to a generic gray. Height is fixed at 40px — smaller than marketplace conventions, reflecting gallery restraint over retail urgency.

**`button-secondary`** — Transparent field with a 1px ink border and identical uppercase type. On hover, the border and fill invert: background becomes ink (#1a1a1a) and text becomes white, a high-contrast flip that mirrors the black-frame conventions of gallery walls. No animation curve required — the state change reads as a hard cut.

**`button-ghost`** — No border, no fill; teal-slate text in uppercase caption weight. Used for inline "View all" and archival navigation links where adding a button silhouette would impose editorial weight the layout doesn't need.

### Navigation

**`nav-bar`** — 56px tall on a canvas (#f8fafa) ground, separated from content by a single 1px hairline (#eaeaea). Links run in Basel Grotesk at 12px with 0.04em tracking — restrained enough to read as metadata rather than wayfinding. Active states underline in teal-slate (#647b7d) using a 1px rule rather than a bold weight shift. Logo sits flush left; secondary links (artists, exhibitions, fairs, press) extend right without a search or cart element — this is not a transactional interface.

### Cards

**`exhibition-card`** — Full-bleed image at 3:2 ratio with no border, no shadow, no radius. Below: a label-upper tag (e.g., "Current Exhibition") in muted teal, the exhibition title in Frame Head display-sm, artist name(s) in caption weight, and date range. The gap between image and text is `{spacing.base}`. Cards tile in a 2-up grid on desktop with `{spacing.xl}` column gutters — the whitespace between cards is as load-bearing as the cards themselves.

**`product-card`** — Used for artist roster and publication listings. Image at 4:5 aspect ratio (portrait-oriented, matching artwork proportions). Below: artist name in `{typography.artist-name}` (Frame Head, weight 300), secondary line in `{typography.caption}` with muted color for medium or nationality. No visible border; hover state shifts the name color to teal-slate (#647b7d).

**`artist-label`** — A pairing of artist name (Frame Head) with a secondary descriptor (Basel Grotesk caption), separated from adjacent content by a 1px top hairline. Used in list contexts — press pages, fair participation records — where dense information must remain legible without resorting to card containers.

### Typography Elements

**`section-header`** — A display-md Frame Head title paired with a label-upper prefacing category, separated by a 1px bottom hairline at `{spacing.md}` padding. The label (e.g., "Artists", "On View") appears above the title in muted uppercase — the visual hierarchy mirrors a catalog entry rather than a marketing headline.

**`image-caption`** — Caption-weight Basel Grotesk in muted color, with a left border accent in `{colors.hairline-soft}` at 2px. Used beneath installation views and artwork documentation images. The left rule grounds the caption without boxing it.

### Utility

**`fair-badge`** — A rectangular chip in `{colors.surface-teal}` (#dae2e2) with ink text in label-upper. Marks gallery participation in art fairs (Art Basel, Frieze, etc.) on exhibition and news cards. No radius, no icon — purely typographic, the teal field is the only warm chromatic note in an otherwise gray-white system.

**`press-item`** — Soft-surface card with a 1px hairline border and source publication in label-upper above the quote or headline in body-sm. Used on press archive pages. Padding at `{spacing.lg}` gives each item breathing room without the generous whitespace of exhibition listings.

**`footer`** — Dark-field reversal: ink (#1a1a1a) background, white body text, muted-soft (#b2c4c5) links that brighten to full white on hover. Contains location addresses (New York, Brussels, Seoul), newsletter signup input, and legal links — all in body-sm with nav-link weight for the section headers. The ink footer grounds a page that otherwise floats on near-white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; nav collapses to hamburger with full-screen overlay; exhibition cards stack vertically; display-xl reduces to 32px; section padding compresses to `{spacing.xl}`; image captions shown below each image in-flow |
| Tablet | 744–1128px | 2-column exhibition grid retained; nav links visible but condensed; hero type scales to display-lg (36px); footer shifts to 2-column link grid |
| Desktop | 1128–1440px | 3-column artist grid; 2-column exhibition grid with generous gutters; full nav bar with all primary links; hero at display-xl (52px); section padding expands to `{spacing.section-lg}` |
| Wide | > 1440px | Content max-width capped (~1320px) and centered; gutters grow proportionally; hero maintains type size with increased padding to `{spacing.section-xl}` |

### Touch Targets

- All nav links padded to minimum 44px tap height via vertical padding even when type is 12px
- Exhibition card tap zone is the full card area, not just the title
- Footer links given `{spacing.lg}` vertical spacing to prevent mis-tap on dense address blocks
- Mobile hamburger target: 44×44px minimum

### Collapsing Strategy

- Primary nav: logo + hamburger icon only below 744px; overlay reveals full link list in display-sm Frame Head at large scale
- Exhibition grid: 3-up → 2-up → 1-up across breakpoints; gutter maintained proportionally
- Artist roster: 4-up grid → 2-up → 1-up; name/meta always visible, no truncation
- Hero text: display-xl (52px) → display-lg (36px) → display-md (24px) at mobile; line breaks managed manually per hero variant
- Footer columns: 4-up → 2-up → stacked single column; newsletter input always full-width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No theme-color meta tag found; canvas color (#f8fafa) assumed as background but not confirmed as the literal `<html>` background token
- "slick" in font stack is the Slick Carousel JS library, not a typeface — excluded from typography system
- Frame Head is likely a proprietary or licensed display face; fallback stack (Georgia, serif) may render differently and should be tested against live specimens
- No interactive state colors (focus rings, error states) could be confirmed from extraction; teal-slate (#647b7d) assumed for focus outlines
- Exact font weights available in the Frame Head and Basel Grotesk licenses are unconfirmed; weight 300 assumed from gallery aesthetic convention
- No explicit dark mode or high-contrast mode rules observed
- Animation/transition durations and easing curves not extractable from static analysis
- Mobile navigation pattern (hamburger vs. bottom bar) not confirmed; hamburger assumed from gallery site conventions
- Exact grid column counts and gutter widths not extracted; values above are derived from visual convention for this gallery category
