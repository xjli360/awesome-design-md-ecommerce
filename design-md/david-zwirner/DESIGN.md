---
version: alpha
name: "David Zwirner"
source_url: "https://www.davidzwirner.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Twelve nav links at AvenirNext weight against #f7f7f7 — no icons, no decorative chrome, the gallery window opened as an infinite white room where text placement IS the design. Every surface floats on a graduated near-white stack (#fafafa, #f7f7f7, #f5f5f5) that reads not as background but as exhibition wall, with #0a0a0a ink that refuses to soften into accessible gray. The most arresting decision in the extracted palette is #faff1f — an electric chartreuse that would be alarming on a lifestyle brand but here operates as a precisely timed voltage, dropped into campaign banners and digital platform features against acres of silence, making the yellow read as almost violent before the canvas reclaims it. Deep navy (#112054) earns its gravity in archival and collection contexts, the typographic register of auction records and institutional provenance. The spectrum of additional accent values — #dc2626 crimson, #0d9a0d institutional green, #c48a16 amber, #b51912 deep red — are not permanent brand tokens but chromatic identities lent to individual exhibitions, each show consuming a color field for its duration before the white resets. AvenirDemi handles the weight of artist names and exhibition titles at display scale; AvenirNext carries body and caption with geometric steadiness; a monospace stack (Consolas, Courier New, Menlo) surfaces in edition records and dimensions, the typewriter register indexing document authority alongside art-historical data. `{rounded.none}` governs every interactive surface — no pill buttons, no softened card corners, every rectangle a hard frame. Shopify commerce operates nearly invisibly beneath an editorial grid that privileges the work over the transaction, edition numbers appearing in `{typography.monospace-caption}` beneath titles as if transcribed from a physical inventory sheet.

colors:
  primary: "#faff1f"
  primary-active: "#d4e000"
  primary-disabled: "#f5f5a0"
  navy: "#112054"
  navy-mid: "#334155"
  ink: "#0a0a0a"
  body: "#1a1a1a"
  muted: "#757575"
  muted-soft: "#9ca3af"
  hairline: "#e8e8e8"
  hairline-soft: "#f5f5f5"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-mid: "#e5e7eb"
  on-primary: "#0a0a0a"
  on-dark: "#fafafa"
  exhibition-red: "#dc2626"
  exhibition-green: "#0d9a0d"
  exhibition-amber: "#fbbf24"
  exhibition-deep-red: "#b51912"

typography:
  display-xl:
    fontFamily: "'AvenirDemi', 'AvenirNext', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'AvenirDemi', 'AvenirNext', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'AvenirNext', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'AvenirDemi', 'AvenirNext', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirNext', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.05px
  body-md:
    fontFamily: "'AvenirNext', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'AvenirNext', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'AvenirNext', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  monospace-caption:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, 'Liberation Mono', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  monospace-body:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, 'Liberation Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  button-md:
    fontFamily: "'AvenirDemi', 'AvenirNext', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'AvenirDemi', 'AvenirNext', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'AvenirNext', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  label-caps:
    fontFamily: "'AvenirDemi', 'AvenirNext', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 1.0px
    textTransform: uppercase

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.monospace-caption}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    imageAspectRatio: "16/9"
  exhibition-hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-md}"
    rounded: "{rounded.none}"
    paddingVertical: "{spacing.section}"
  artist-name-display:
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.lg}"
  edition-detail:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.monospace-caption}"
    priceTypography: "{typography.title-md}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  edition-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
  campaign-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
  navy-section:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    height: 44px
  filter-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "6px {spacing.sm}"
  filter-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Solid #faff1f fill with #0a0a0a text, zero border radius, uppercase AvenirDemi at 14px with 0.5px letter-spacing, 44px height. The yellow is deployed sparingly — Add to Cart and primary commerce CTAs — preserving its voltage by scarcity rather than spending it as a UI convention. Active state shifts to #d4e000; disabled lightens the fill to #f5f5a0 and moves text to muted gray, signaling unavailability without relying on opacity.

**`button-secondary`** — Transparent fill with a 1px #0a0a0a border, dimensions and typography matching `button-primary`. The hard rectangle mirrors a physical exhibition label; on hover, the border weight optionally thickens to 2px. Used for Inquire, Learn More, Download, and any action that should register weight without commanding the same urgency as a commerce CTA.

**`button-ghost`** — No border, no fill, #757575 text in 12px uppercase AvenirDemi. Functions as a low-hierarchy tertiary action — Close, Reset Filters, View All — where adding visual weight would compete with artwork content.

### Navigation

**`nav-bar`** — 56px tall on a #fafafa background with a 1px #e8e8e8 bottom border. All links render in AvenirNext 14px at regular weight; no bold, no icons, no hover fill. Active items receive a 1px bottom border in #0a0a0a — the most minimal active treatment available. Gallery name in AvenirDemi anchors left; the full exhibition/artists/gallery hierarchy spans center on desktop; cart and language toggle sit right. The gallery's five physical locations (New York, Los Angeles, London, Paris, Hong Kong) appear as secondary nav under Gallery, rendered identically to other nav links.

### Product Card (Edition/Print)

**`product-card`** — A 4:5 artwork image on a #f7f7f7 surface with zero corner radius. Below the image: artist name in title-sm weight, edition title in body-sm regular italics, then a monospace-caption line encoding medium, dimensions, and edition number. This monospace line is the most distinctive UI convention on the site — it transcribes physical inventory data in a typewriter register that separates art-historical fact from marketing copy. Price renders at title-sm weight below, and the Add to Cart button occupies a discrete row at the card's bottom edge.

### Exhibition Card

**`exhibition-card`** — Full-bleed 16:9 imagery with artist name overlaid at bottom-left in display-md on a gradient scrim, and exhibition dates below in monospace-caption. On hover the image dims to 80% opacity and gallery location surfaces as a text layer. No rounded corners, no card shadow — the image boundary IS the card frame. Exhibition-specific chromatic identities may replace the scrim color, making each card visually distinct while preserving structural consistency.

### Exhibition Hero

**`exhibition-hero`** — Full-width, defaulting to #0a0a0a background, with artist name in display-xl and exhibition title in display-md stacked below. Vertical padding at `{spacing.section}` on each side. This is the primary injection point for exhibition chromatic identities: an individual show may override backgroundColor with #dc2626, #faff1f, or any exhibition-accent color extracted from the DOM, then the canvas resets to default after the show closes. Text color flips to `{colors.on-dark}` against any dark override.

### Campaign Banner

**`campaign-banner`** — Solid #faff1f fill spanning full viewport width, #0a0a0a display-xl text, zero radius. Reserved for major digital campaigns or platform announcements. The electric yellow reads as a rupture in the near-white system precisely because it appears once per visit rather than as a recurrent UI convention.

### Edition Detail

**`edition-detail`** — Two-column layout on desktop: artwork image at 60% left, metadata at 40% right on #f7f7f7. The metadata block follows a strict label/value pattern — edition-label (label-caps in muted gray) over monospace-caption values for Artist, Title, Year, Medium, Dimensions, and Edition. Price appears in title-md weight below the metadata block, followed by the primary commerce CTA. The visual pattern reads as a museum object-label transcribed to screen rather than a retail product spec sheet.

### Search

**`search-bar`** — Full-width on mobile, 360px max-width on desktop. #f7f7f7 background, no rounding, 1px #e8e8e8 border that sharpens to 1px #0a0a0a on focus. AvenirNext body-md for placeholder text. Results appear in a borderless overlay panel with 1px #e8e8e8 row separators; hover state uses bold weight on the matched term only rather than a background fill.

### Filter Tags

**`filter-tag`** — Uppercase AvenirDemi at 11px, 1.0px letter-spacing, transparent fill, 1px #e8e8e8 border. Active state inverts to #0a0a0a fill with #fafafa text — a stark reversal that communicates selection without any color accent. Tags filter by medium, artist nationality, and exhibition year across the gallery's archive.

### Footer

**`footer`** — #0a0a0a background in four columns of link lists on desktop. Column headers in label-caps at muted-soft color; links in body-sm at muted-soft #9ca3af that lifts to #fafafa on hover. Gallery address blocks use monospace-body for location data. Social icons sit at bottom-right as minimal SVG glyphs. The footer is the densest information layer and the one consistent dark surface in an otherwise near-white system — it signals institutional completeness rather than decorative richness.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to text-label "Menu" link triggering a full-height slide-in drawer; edition-detail stacks to single column image-over-metadata; filter tags scroll horizontally in a no-wrap row; section padding compresses to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; primary nav links visible, secondary links in a hover dropdown; exhibition-detail moves to 50/50 split; location tabs render as a scrollable pill row |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav visible; edition-detail at 60/40 split; container max-width 1280px centered with symmetric gutters |
| Wide | > 1440px | Layout locks at 1280–1440px max-width; side gutters expand symmetrically; no structural changes beyond margin distribution |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target height, even when visual type is smaller
- Filter tags extend to 44px tap height via vertical padding rather than visual size
- Nav items in the mobile drawer have 48px tap height
- Monospace edition-number and dimension lines are display-only and carry no touch target

### Collapsing Strategy
- Primary nav collapses at < 1024px: "Artists", "Exhibitions", "Gallery" move into a slide-in drawer triggered by a text-label "Menu" link — no hamburger icon, preserving the text-only navigation philosophy on mobile
- Location sub-navigation (New York / Los Angeles / London / Paris / Hong Kong) compresses to a horizontally scrollable tab row on tablet and mobile, with no truncation or overflow indicator beyond scroll shadow
- Footer four-column layout stacks to a single accordion column on mobile, with label-caps headers acting as collapse toggles

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Display type sizes (display-xl at 48px, display-lg at 32px) are inferred from gallery editorial conventions rather than extracted directly from CSS; the extraction did not surface explicit font-size rules at heading scale
- The many exhibition-accent colors (#dc2626, #0d9a0d, #c5cc23, #c48a16, #b51912, #f0abfc, #4e9cf6, #0284c7) are confirmed as present in the DOM but their assignment to specific shows or persistent UI roles could not be determined — listed as reserved color tokens rather than permanent brand slots
- The precise deployment context of #faff1f is unconfirmed: it is present in the palette but whether it functions as a permanent campaign CTA, a seasonal platform feature, or a single exhibition identity could not be verified from extraction alone
- meta theme-color is absent, suggesting either no PWA manifest or a per-exhibition dynamic value
- Icon system is unidentifiable from extraction — unknown whether custom SVG, an icon font, or inline images are used for cart, social, and navigation glyphs
- Hover, focus, and active state details for exhibition-card and artist-name-display were not extractable; values above are inferred from gallery UI conventions
- AvenirNext/AvenirDemi are confirmed present as font-family stack entries but licensing model (self-hosted vs. Adobe Fonts vs. system fallback) was not determinable
