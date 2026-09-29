---
version: alpha
name: "Hyperdub"
source_url: "https://www.hyperdub.net"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four near-identical near-blacks — #121212, #141414, #151515 — layer the site the way sub-bass frequencies layer in a Burial record: barely perceptible separation, total tonal unity. Hyperdub's shop arrives stripped of decorative color; the extracted palette yields only grays (#787878, #dedede) and those near-blacks, a chromatic vocabulary so restrained that record sleeve art becomes the sole pigment event on any given page. Arial and Helvetica handle all type with zero affectation — no custom wordmarks, no expressive display cuts, no weight modulation for drama. The result mirrors the label's sound philosophy: Steve Goodman founded Hyperdub in 2004 around music that privileges negative space and low-end pressure over surface flourish. Navigation sits flat and unadorned; product cards hold release artwork in strict square format against the dark surface-card (#151515), with artist name and catalogue number in muted mid-gray (#787878) below, price in body-off-white (#dedede). Buttons invert the canvas logic — white fill on near-black, rendered at `{rounded.none}` — hard corners signal the industrial rather than the friendly. Text inputs follow the same flat geometry, borderlined in hairline-gray against the dark field. The spacing system breathes conservatively; section breaks happen through whitespace alone, not rules or dividers, echoing how dub production treats silence as structural material rather than gap. Release dates, catalogue numbers, and FLAC/MP3 format tags carry in caption-weight type at 10–11px — the metadata layer that the collector demographic reads first. Every component is subordinate to the record artwork: no rounded pill crops, no gradient overlays, full-bleed square at the top of the card, uninterrupted.

colors:
  primary: "#ffffff"
  primary-active: "#dedede"
  primary-disabled: "#3c3c3c"
  ink: "#ffffff"
  body: "#dedede"
  muted: "#787878"
  hairline: "#797979"
  canvas: "#121212"
  surface-soft: "#141414"
  surface-card: "#151515"
  on-primary: "#121212"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  catalogue-num:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2px
  format-tag:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 42px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.surface-soft}"
    padding: "0 {spacing.xl}"
  nav-link-active:
    textColor: "{colors.primary}"
    textDecoration: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1/1"
  product-card-image:
    width: "100%"
    aspectRatio: "1/1"
    objectFit: cover
    rounded: "{rounded.none}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  catalogue-badge:
    typography: "{typography.catalogue-num}"
    textColor: "{colors.muted}"
    backgroundColor: transparent
  format-tag:
    typography: "{typography.format-tag}"
    textColor: "{colors.ink}"
    backgroundColor: "{colors.muted}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.xs}"
  release-hero:
    backgroundColor: "{colors.canvas}"
    imageMaxWidth: 480px
    imageAspectRatio: "1/1"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    artistTypography: "{typography.body-sm}"
    artistColor: "{colors.muted}"
    metaTypography: "{typography.catalogue-num}"
    metaColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xl}"
  tracklist:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.surface-card}"
    trackTypography: "{typography.body-sm}"
    trackColor: "{colors.body}"
    trackNumberColor: "{colors.muted}"
    durationColor: "{colors.muted}"
    rowPadding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  artist-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.body}"
    padding: "{spacing.sm}"
  genre-tag:
    typography: "{typography.format-tag}"
    textColor: "{colors.muted}"
    backgroundColor: transparent
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.body}"
    borderTop: "1px solid {colors.surface-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.body}"
    activeBorder: "1px solid {colors.body}"
    rounded: "{rounded.none}"
    itemSize: 32px

## Components

### Buttons

**`button-primary`** — White-fill block button at 44px height, zero border-radius, all-caps Arial 13px weight 700 with 0.8px letter-spacing. The `{colors.on-primary}` near-black text (#121212) creates a hard inversion of the dark canvas — the only moment of brightness on the page belongs to the call to action. Active/press steps fill back to `{colors.primary-active}` (#dedede), sustaining flat geometry throughout. Disabled state fills with `{colors.primary-disabled}` (#3c3c3c) — legible as inactive without introducing any new hue into the palette. No shadow, no transition glow; the button communicates exclusively through contrast and shape.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` white border and matching white text in the same `{typography.button-md}` all-caps treatment. On hover the background lifts to `{colors.surface-soft}` (#141414) — a shift barely perceptible to the eye, like a sub-frequency pulse. Hard corners preserved. Used for secondary purchase options, format toggles (LP vs. digital), and cancel actions in checkout flows.

### Text Input

**`text-input`** — Dark-filled at `{colors.surface-soft}` (#141414), 1px `{colors.hairline}` border, 42px height, zero radius. Placeholder renders in `{colors.muted}` (#787878), ghosting into the dark field until the input is touched. Focus shifts the border cleanly to `{colors.primary}` white without box-shadow or glow — consistent with the site's refusal of decorative states. Used in newsletter signup, search field, and Shopify checkout address inputs.

### Navigation

**`nav-bar`** — 56px bar in `{colors.canvas}` (#121212) with a 1px `{colors.surface-soft}` bottom-border providing the minimum visual separation from page content. Nav links in `{typography.nav-link}` at 13px/400 weight, `{colors.body}` (#dedede) at rest, stepping to `{colors.primary}` white on hover. Label wordmark holds left; cart count and optional search icon hold right. Primary link taxonomy: Releases, Artists, News, About, and Cart — five destinations for a label that releases deliberately rather than prolifically. No dropdown megamenu.

### Product Card

**`product-card`** — Zero-radius rectangle in `{colors.surface-card}` (#151515) with a single square release artwork at strict 1:1 aspect ratio, full-width and uncropped — the artwork is the card. Below the image: artist name in `{typography.body-sm}` at `{colors.muted}`, release title in `{typography.title-sm}` at `{colors.body}`, catalogue number via the `catalogue-badge` component in tracked uppercase gray. Price sits below in `{typography.title-sm}`. Available format chips (`format-tag`) — LP, CD, FLAC, MP3, WAV — run inline below price. On hover, no card lift or shadow; only the cursor changes. The card is a display node, not an interaction surface.

### Release Hero

**`release-hero`** — Full-width section with release artwork as focal element: square image up to 480px, left-column at desktop, full-width above metadata at mobile. Right column carries artist in `{typography.body-sm}` muted, title in `{typography.display-md}` white, catalogue number in `{typography.catalogue-num}`, tracklist via `tracklist`, and purchase buttons. No gradient scrim, no overlay treatment — the artwork sits clean and edge-to-edge within its container. Format options (LP, digital) render as `button-primary` and `button-secondary` stacked at 44px height, with price adjacent in `{typography.title-sm}`.

### Tracklist

**`tracklist`** — Stacked rows in `{colors.surface-soft}`, each padded `{spacing.sm}` vertical by `{spacing.base}` horizontal, separated by a 1px `{colors.surface-card}` top-border on each row — separation through the darkest gap in the palette rather than a visible rule. Track number left in `{colors.muted}`, track name in `{typography.body-sm}` `{colors.body}`, duration right-aligned in `{colors.muted}`. No play icon at rest; on hover, a minimal triangle glyph in muted gray appears if a preview stream is available. Side A / Side B section labels render in `{typography.catalogue-num}` above their respective track groups.

### Format Tag

**`format-tag`** — Compact format identifier (LP / CD / FLAC / MP3 / WAV) at `{typography.format-tag}`: 10px, weight 700, 1px letter-spacing, uppercase, `{colors.ink}` white text on `{colors.muted}` (#787878) fill, zero radius, 3px vertical padding. Used inline on product cards and in the release hero purchase area. The muted-gray fill reads as label, not button — no hover state, no affordance beyond identification. Multiple formats stack horizontally with `{spacing.xs}` gap.

### Artist Card

**`artist-card`** — Matches `product-card` geometry: zero-radius `{colors.surface-card}` rectangle with square or portrait artwork at top, artist name in `{typography.title-md}` at `{colors.body}` below. No bio excerpt on the card face — the card is a navigation node to the artist's full discography page. Grid on the Artists index renders 2-up on mobile, 3-up at tablet, 4-up at desktop, using the same gutter as the release grid to maintain a unified catalogue feel across pages.

### Catalogue Badge

**`catalogue-badge`** — Inline text in `{typography.catalogue-num}`: 11px, uppercase, 1px letter-spacing, `{colors.muted}` on transparent. Appears on product cards beneath the release title and in the release hero alongside label metadata. Catalogue numbers follow the HDB-prefixed pattern (HDB001, HDB002…) and function as the primary lookup identifier for the collector demographic — they are placed more prominently than price on the card hierarchy.

### Genre Tag

**`genre-tag`** — Outline chip for genre and style labels (Bass, Grime, Experimental, Electronic…) in `{typography.format-tag}` at `{colors.muted}`, 1px `{colors.hairline}` border, transparent fill, zero radius, 3px vertical padding. Used on artist pages and release filter interfaces. Unlike `format-tag`, these carry no fill — they read as categorisation labels, lighter in visual weight than the format identifiers which signal purchasable variants.

### Footer

**`footer`** — Full-width `{colors.canvas}` block with a 1px `{colors.surface-soft}` top-border. Column links in `{typography.body-sm}` at `{colors.muted}`, lifting to `{colors.body}` on hover. Column heads in `{typography.title-sm}` at `{colors.body}`. Columns: Label (About, Contact, Press), Shop (Releases, Merchandise, Gift Cards), Follow (Bandcamp, SoundCloud, Instagram links), and a newsletter row with inline `text-input` + `button-primary`. Copyright line at 11px in `{colors.muted}`. No oversized logo lockup; the label name prints in plain Arial matching body weight, refusing any promotional emphasis.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid (preserves browse density); nav collapses to hamburger overlay in `{colors.canvas}`; release-hero stacks artwork above metadata; tracklist goes full-width; footer single-column stacked |
| Tablet | 744–1128px | 3-column product grid; nav shows primary links, collapses secondary overflow; release-hero splits 50/50 artwork/metadata side-by-side |
| Desktop | 1128–1440px | 4-column product grid; full nav visible; release-hero uses wide split with artwork capped at 480px; section padding increases to `{spacing.section}` |
| Wide | > 1440px | Content constrained to ~1280px max-width, centered; no additional grid columns; flanking whitespace in `{colors.canvas}` fills the field |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- Nav links padded to full bar height (56px) for tap-area coverage across the entire bar height
- `format-tag` chips stacked vertically on mobile release hero to prevent mis-tap between adjacent small targets
- Pagination items maintain 32px base with additional 8px padding on mobile
- Cart icon and hamburger menu icon minimum 44×44px tap area regardless of glyph size

### Collapsing Strategy

- Navigation: hamburger at < 744px; sliding overlay drawer in `{colors.canvas}` with full link list in `{typography.title-md}` — same monochrome palette, no color injection at mobile breakpoint
- Product grid: 2-up on mobile minimum (never single-column — artwork browse density is core to the catalogue experience), 3-up at tablet, 4-up at desktop
- Release hero: artwork-first stacking at mobile with image above the fold, tracklist and purchase below scroll; 50/50 column split at tablet; wide asymmetric split (artwork ~45%, metadata ~55%) at desktop
- Tracklist track numbers: hidden on mobile viewports below 375px to recover horizontal space for track name

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — site appears to use system Arial/Helvetica/Calibri throughout; if Hyperdub employs a custom display cut for editorial headlines or hero text, it was not extractable from the live session
- Pure white (#ffffff) is not present in the extracted palette but is inferred as the highest-contrast text/button fill for this dark-theme context; if the site uses a slightly off-white instead, that value was not captured
- Accent or highlight color absent — the full extracted palette is monochrome; if a label-specific color (red for sale badges, an active filter state, a category highlight) exists, it did not surface in extraction
- Exact nav bar height and internal padding not measured from live DOM; 56px is a proportional estimate
- Audio preview player component (for digital download pages and stream embeds) not observed in extraction; component spec above is estimated from label-shop conventions
- Mobile-specific font-size scaling not confirmed from live DOM; responsive type sizes are design-system estimates based on the extracted desktop scale
- Shopify theme identifier not detected; component implementation details may diverge from Dawn or other standard Shopify theme defaults
