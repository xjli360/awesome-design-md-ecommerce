---
version: alpha
name: "Perrotin"
source_url: "https://www.perrotin.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric cobalt #003399 — a blue pitched at the frequency of neon signage rather than institutional trustworthiness — is the single interactive voltage in an otherwise achromatic field. The rest of the Perrotin palette is a graduated sequence of whites and neutral grays moving from near-white surfaces (#f6f6f6, #fafafa) through hairline separators (#e5e5e5) and mid-tone muted text (#8c8c8c, #777777) down to a near-black ink (#181818); the cobalt appears precisely at hyperlinks, active states, and primary CTAs, then withdraws entirely, leaving reproduced artwork uncontested on a white-cube canvas. Akzidenz-Grotesk and its Extended sibling carry every word: a Swiss grotesque whose century of commercial use has accumulated the kind of anonymous authority that purely geometric sans-serifs lack. The Extended cut governs display headings in uppercase with open tracking — artist names announced as typographic statements at scale — while regular-width Akzidenz handles navigation, body copy, and metadata at economy weights without competing with the image plane. Fira Code and JetBrains Mono appear in catalog, edition number, and provenance metadata contexts, framing precise numerical data as technical record. Corners are strictly rectilinear ({rounded.none}) throughout interactive elements and cards, echoing white-cube exhibition geometry; only notification indicators soften to {rounded.full}. An amber accent (#f59e0b) surfaces in narrow contexts — notification badges, status indicators — providing warm punctuation against the institutional cool of the cobalt-and-gray system. Section separators operate at {spacing.section} or wider; grid gutters are as intentional as the frames around the work itself. The overall effect is a digital space engineered to recede behind what it presents.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aacc"
  accent-amber: "#f59e0b"
  accent-amber-dark: "#c57f08"
  ink: "#181818"
  body: "#444444"
  muted: "#8c8c8c"
  muted-soft: "#777777"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f2f2f2"
  surface-strong: "#e0e0e0"
  on-primary: "#ffffff"
  error: "#dc2626"

typography:
  display-xl:
    fontFamily: "'Akzidenz-Grotesk-Extended', 'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: 0.04em
    textTransform: uppercase
  display-md:
    fontFamily: "'Akzidenz-Grotesk-Extended', 'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.03em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Akzidenz-Grotesk-Extended', 'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.03em
    textTransform: uppercase
  artist-display:
    fontFamily: "'Akzidenz-Grotesk-Extended', 'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  title-md:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  catalog-mono:
    fontFamily: "'Fira Code', 'JetBrains Mono', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Akzidenz-Grotesk', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em

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
    padding: 12px 24px
    height: 40px
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    borderBottomFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 0
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  artwork-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.artist-display}"
    metaTypography: "{typography.caption}"
    titleColor: "{colors.ink}"
    titleHoverColor: "{colors.primary}"
    metaColor: "{colors.muted}"
    editionTypography: "{typography.catalog-mono}"
    gap: "{spacing.sm}"
  artist-listing-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  exhibition-hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-sm}"
    subtitleColor: "{colors.surface-strong}"
    minHeight: 560px
    padding: "{spacing.section}"
  edition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.catalog-mono}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    textActiveColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "6px 14px"
    height: 32px
  notification-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 5px"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "none"
    borderBottom: "1px solid {colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
  location-switcher:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    textHoverColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.surface-strong}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A flat cobalt (#003399) rectangle with {rounded.none}, uppercase Akzidenz-Grotesk at 0.1em tracking, 40px height, and no shadow or elevation. Active state shifts to `{colors.primary-active}` (#002277); disabled state fades to `{colors.primary-disabled}`. The button reads as a graphic element — more poster than widget — because of the high-saturation blue against the gallery's neutral canvas.

**`button-secondary`** — Identical geometry to `button-primary` but white fill with a 1px `{colors.ink}` border. On hover, fill and stroke invert: the button becomes black with white text. Used wherever the primary action is already taken or the surface is not the main conversion surface.

**`button-ghost`** — No background, no border, cobalt text in `{typography.button-md}`. Used for inline editorial links that require a button affordance without adding visual mass to a content-dense page.

### Text Input

**`text-input`** — Three sides borderless, with a single bottom stroke in `{colors.hairline}` that transitions to `{colors.primary}` cobalt on focus. No enclosing rectangle, no border-radius. This underline convention is common in gallery and museum interfaces and signals editorial restraint: the form recedes until the user engages it.

### Navigation Bar

**`nav-bar`** — 56px fixed bar on `{colors.canvas}` with a 1px `{colors.hairline}` bottom border. The Perrotin wordmark anchors left in `{typography.artist-display}` Extended uppercase; primary nav items (Exhibitions, Artists, News, Fairs, Gallery) run in `{typography.nav-link}` with 0.04em tracking. Location and language switcher sit at right alongside a search icon. Dropdowns are borderless flat lists with no elevated surface — they appear as a continuation of the document, not a floating layer.

### Artwork Card

**`artwork-card`** — Vertical stack: image at a portrait 4:5 ratio with no border-radius, followed by artist name in `{typography.artist-display}` (Extended uppercase, wide tracking), artwork title in `{typography.caption}`, and edition or medium in `{typography.catalog-mono}`. No card border or shadow; the grid gutter separates cards. On hover, the artist name transitions from `{colors.ink}` to `{colors.primary}` — this is the only hover feedback, reinforcing the hierarchy that the work is primary and the navigation system secondary.

### Artist Listing Header

**`artist-listing-header`** — Full-width ruled block: a 1px `{colors.hairline}` top border, then the artist name filling the content column at `{typography.display-xl}` (Akzidenz-Grotesk-Extended, uppercase, 0.04em tracking). On the artists index page, these headers stack alphabetically with `{spacing.section}` vertical padding above and below. The combination of the hairline rule and Extended uppercase gives each entry the weight of a printed catalogue raisonné entry.

### Exhibition Hero

**`exhibition-hero`** — Full-bleed dark block in `{colors.ink}` (#181818), minimum 560px tall. Exhibition title in `{typography.display-xl}`, artist and date range in `{typography.title-sm}` with subdued `{colors.surface-strong}` color. When a photograph is present, it bleeds fully across the frame with a semi-transparent dark scrim preserving text legibility. This inversion of the standard white-canvas layout signals that exhibitions are the gallery's primary institutional statement.

### Edition Badge

**`edition-badge`** — A small rectangular chip in `{colors.surface-soft}` carrying edition numbers ("Ed. 5/30"), print dimensions, or technique notes in `{typography.catalog-mono}`. The monospace font makes the numerical precision of provenance data immediately legible and distinguishes it from marketing copy using regular Akzidenz.

### Filter Tags

**`filter-tag`** — Flat rectangular chips in `{typography.button-sm}` uppercase. Inactive: `{colors.hairline}` border, `{colors.muted}` text. Active: `{colors.ink}` border, `{colors.ink}` text — no fill change. The border-weight-only selection signal is deliberately minimal: it communicates state without introducing color into the filter UI.

### Notification Badge

**`notification-badge`** — A circular pill in `{colors.accent-amber}` (#f59e0b), the sole warm hue in the entire interface. Used over cart or alert icons. Because the cobalt-and-gray system is uniformly cool, the amber reads instantly as a status signal without requiring large size or heavy weight.

### Search Input

**`search-input`** — An overscaled inline field using `{typography.display-md}` so the typed query itself becomes a display element. Bottom-border only, no enclosing form chrome. Treating search as an editorial moment — rather than a utility widget tucked in a corner — reflects the gallery's stance that every interaction surface should have the compositional deliberateness of a page layout.

### Location Switcher

**`location-switcher`** — Small uppercase `{typography.button-sm}` text selector for gallery cities (Paris, New York, Hong Kong, Seoul, Tokyo, Dubai, Los Angeles). Inactive state in `{colors.muted}`; hover and active in `{colors.ink}`. No border, no background — pure typographic affordance.

### Footer

**`footer`** — Dark `{colors.ink}` background mirroring the exhibition hero, creating a deliberate bookend effect on every page. Canvas-white type for primary content, `{colors.surface-strong}` for secondary links. A newsletter signup uses the underline `text-input` variant against the dark field. Gallery addresses by city, social links, and legal copy all sit in `{typography.body-sm}`. The newsletter CTA uses `button-primary` — cobalt on dark ink — as the highest-contrast CTA pairing on the site.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger with full-screen ink-background drawer; exhibition hero reduces to 320px min-height; display-xl scales to ~26px; section spacing contracts to {spacing.xl}; filter tags scroll horizontally in a single row |
| Tablet | 744–1128px | 2-column artwork grid; nav items visible but language/location switcher moves to drawer; hero 420px min-height; search expands to overlay |
| Desktop | 1128–1440px | 3–4 column artwork grid; full nav bar with all items visible; exhibition hero 560px; display-xl at full 52px |
| Wide | > 1440px | Content column max-width ~1280px centered; hero expands to 70vh; artwork grid may reach 5 columns on artist pages |

### Touch Targets
- All nav links maintain minimum 44×44px tap target even when `{typography.nav-link}` renders at 13px
- Artwork cards: full image-plus-caption block is tappable, not just the text
- Filter tags maintain 44px height on mobile via increased vertical padding
- Edition badges are display-only and do not require tap targets

### Collapsing Strategy
- Nav items collapse right-to-left: Gallery → Fairs → News → Artists; Exhibitions always visible
- Location/language switcher is first to move into hamburger drawer at tablet
- Artist listing headers maintain Extended uppercase display type at all breakpoints, reducing font-size from 52px to 26px progressively
- Footer columns reflow from 4-column grid to 2-column at tablet, single-column at mobile while maintaining full dark-background treatment

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Official typographic scale not published; all font sizes inferred from art-gallery visual hierarchy conventions and Akzidenz-Grotesk's documented usage patterns
- Nav-bar height estimated at 56px; exact value not extractable from static analysis
- Pure white (#ffffff) canvas is almost certainly present as the base surface but was not captured in extraction — near-whites (#fafafa, #f8fafc) are present and likely framework defaults
- #007aff in extracted palette is an iOS system blue originating from a web component framework, not a Perrotin brand color — excluded from tokens
- #e7f3ff and #f0fff4 appear to be info/success state tints from a UI framework rather than brand choices — not promoted to design tokens
- Whether italic cuts of Akzidenz-Grotesk are used for artwork titles is unconfirmed; art-world convention of italic artwork titles assumed
- Animation easing curves and transition durations not extractable from static color/font analysis
- Exact grid column counts and gutter widths per breakpoint not confirmed; values above reflect gallery-context inference
