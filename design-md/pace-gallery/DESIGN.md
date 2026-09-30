---
version: alpha
name: "Pace Gallery"
source_url: "https://www.pacegallery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The entire Pace Gallery digital presence resolves to a two-value argument — #101010 ink pressed against a #ffffff ground, with negative space functioning as the only decorative element. No secondary hue interrupts the field; no gradient softens the transition. The interface behaves precisely as a white cube gallery behaves: the artwork image carries all sensory responsibility, and every typographic and structural decision exists to get out of its way. Navigation presents as a minimal bar with near-zero visual mass, text at 14px in regular weight, a hairline border the only indication of zone change. Buttons arrive without radius — `{rounded.none}` throughout, corners as hard as a gallery wall edge. The discipline is institutional rather than aesthetic: a gallery that has represented Rothko, Rauschenberg, and Agnes Martin does not need a friendly pill-shaped CTA to establish authority. Typography runs in a clean neo-grotesque at light-to-regular weights; display headings sit at weight 300 and large point sizes, trusting the combination of scale and restraint over heavy typographic muscle. Section labels appear in tracked uppercase at 11px — `{typography.label-uppercase}` — the same register used by exhibition wall text for medium attribution. Artist listing pages resolve to a single column of names separated by `{colors.hairline}` rules, each row lifting to `{colors.surface-soft}` on hover: a phonebook of cultural consequence. Exhibition cards give image the dominant proportion and reduce date and location to `{typography.caption}` in `{colors.muted}`, below the title. The footer inverts to `{colors.surface-dark}` — the one moment the brand's black takes on a background role rather than a text role. Overall register: the confidence of an institution that has operated for sixty-five years and learned that the less the container says, the more the art speaks.

colors:
  primary: "#101010"
  primary-active: "#000000"
  primary-disabled: "#aaaaaa"
  ink: "#101010"
  body: "#2c2c2c"
  muted: "#767676"
  muted-soft: "#aaaaaa"
  hairline: "#e5e5e5"
  hairline-strong: "#cccccc"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#101010"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1.04
    letterSpacing: -1px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
  footer-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    border: none
    textTransform: uppercase
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    border: "1px solid {colors.ink}"
    textTransform: uppercase
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.ink}"
    padding: "0 0 2px 0"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: "10px {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.title-md}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline-strong}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    gap: "{spacing.sm}"
    hoverImageScale: 1.02
  artwork-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    artistTypography: "{typography.body-sm}"
    artistColor: "{colors.ink}"
    titleTypography: "{typography.caption}"
    titleColor: "{colors.muted}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: "0 0 {spacing.xl} 0"
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "16/10"
    locationTypography: "{typography.label-uppercase}"
    locationColor: "{colors.muted}"
    titleTypography: "{typography.title-lg}"
    titleColor: "{colors.ink}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    gap: "{spacing.md}"
    padding: "{spacing.lg} 0 {spacing.xxl}"
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    imageObjectFit: cover
    minHeight: 100vh
    titleTypography: "{typography.display-xl}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.on-dark}"
    captionPosition: bottom-left
    captionPadding: "{spacing.xl}"
    overlayOpacity: 0.15
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    imageAspectRatio: "16/9"
    padding: "{spacing.section} 0"
  filter-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.ink}"
    typography: "{typography.label-uppercase}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
    gap: "{spacing.xl}"
  artist-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    hoverBackgroundColor: "{colors.surface-soft}"
    secondaryTypography: "{typography.body-sm}"
    secondaryColor: "{colors.muted}"
  section-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.xl}"
  artwork-detail-meta:
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowGap: "{spacing.sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.md}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    borderBottom: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "6px {spacing.md}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.footer-link}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} 0"
    borderTop: none
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "6px 10px"

## Components

### Buttons

**`button-primary`** — A rectangular black block with no border radius, white text set in 13px medium weight with tracked uppercase lettering. On hover the background deepens to pure `{colors.primary-active}` #000000; the transition is instant rather than animated, maintaining the institutional register. Disabled state uses `{colors.primary-disabled}` to signal unavailability without softening.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, identical padding and uppercase typography. On hover the fill inverts to black and text turns white — a toggle rather than a gradient, consistent with the binary palette. Used for secondary actions on light surfaces.

**`button-ghost`** — No background, no border box; relies solely on a 1px bottom border on the text itself. Used inline within body copy and exhibition descriptions for "Read more" or "Inquire" calls that must not interrupt reading flow.

### Text Input

**`text-input`** — No border radius, 1px `{colors.hairline}` border on all sides in rest state, transitioning to 1px `{colors.ink}` on focus. Placeholder text in `{colors.muted}`. No floating label; the placeholder disappears on input, relying on proximity to a static label above.

### Navigation

**`nav-bar`** — 56px tall, white background, 1px `{colors.hairline}` bottom border. Logo mark at left in `{typography.title-md}` weight, primary navigation links at center in `{typography.nav-link}` 14px regular — no bold weight applied. Utility icons (search, account) at right as icon-only touch targets. On scroll, the border-bottom transitions to `{colors.hairline-strong}` for a slightly more defined separation without adding drop shadow.

### Content Cards

**`artwork-card`** — Portrait-ratio image (`3/4`) with zero rounding, artist name below in `{typography.body-sm}`, artwork title and medium in `{typography.caption}` `{colors.muted}`. No overlay, no hover CTA button; the card links as a whole unit. Images scale to 1.02× on hover via CSS transform, the only kinetic gesture in the system.

**`exhibition-card`** — Landscape-ratio image (`16/10`) above a text block: gallery location in tracked uppercase `{typography.label-uppercase}` `{colors.muted}`, exhibition title in `{typography.title-lg}`, date range in `{typography.caption}`. No card border, no shadow — cards are defined entirely by image edge and typographic grouping.

### Hero

**`hero-full-bleed`** — Full-viewport bleed photograph with a thin dark overlay at 15% opacity. Exhibition or artist name appears at bottom-left in `{typography.display-xl}` 300 weight `{colors.on-dark}`, with a medium credit line in `{typography.body-sm}` directly below. The minimal overlay preserves color fidelity of artwork imagery. No button sits on the hero; the image itself is the CTA.

**`hero-editorial`** — White-background layout for text-forward moments: title in `{typography.display-md}` at weight 300, supporting paragraph in `{typography.body-md}`, with an adjacent or below-positioned image at 16/9 ratio. Used for press sections, about pages, and artist features.

### Navigation & Filtering

**`filter-strip`** — Horizontal strip of `{typography.label-uppercase}` category labels separated by spacing. Inactive labels in `{colors.muted}`, active label in `{colors.ink}` with a 2px bottom border as the sole selection indicator. No pill background, no chip shape — filtering is communicated purely through weight and underline.

**`artist-row`** — Full-width row with artist name in `{typography.title-md}`, dates or nationality in `{typography.body-sm}` `{colors.muted}` at right. Separated by 1px `{colors.hairline}` rules. Row background lifts to `{colors.surface-soft}` on hover. The list reads as an inventory rather than a marketing surface.

### Detail & Metadata

**`artwork-detail-meta`** — Two-column label/value grid below artwork imagery. Labels in `{typography.label-uppercase}` `{colors.muted}`, values in `{typography.body-sm}` `{colors.ink}`. Each row separated by `{spacing.sm}` vertical gap. A 1px `{colors.hairline}` top border marks the transition from image to metadata. Inquiry button appears after the metadata block as `button-primary`.

**`section-header`** — Short uppercase label in `{typography.label-uppercase}` with a 1px `{colors.hairline}` bottom border flush to the grid edge, followed by `{spacing.xl}` of breathing room before content. Functions as a divider rather than a title.

### Search

**`search-bar`** — Activates as an overlay or inline expansion. Text input uses `{typography.body-md}` with only a 1px `{colors.ink}` bottom border — no surrounding box. Search icon at left, close icon at right. Results appear in a dropdown list of artist names, exhibitions, and artworks separated by `{typography.label-uppercase}` category headers.

### Footer

**`footer`** — Inverted to `{colors.surface-dark}` background, providing the only large black field on most page templates. Column headers in `{typography.label-uppercase}` `{colors.muted-soft}`, links in `{typography.footer-link}` `{colors.on-dark}`. Social icons as minimal glyphs. Newsletter input uses the same borderless bottom-border style as `search-bar` adapted for dark field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger + logo + search icon; hero title drops to `{typography.display-sm}`; filter-strip scrolls horizontally; footer stacks columns vertically |
| Tablet | 744–1128px | Two-column artwork grid; exhibition cards stack image above text; nav shows partial links with overflow; hero text at `{typography.display-md}` |
| Desktop | 1128–1440px | Three- or four-column artwork grid; full horizontal nav; exhibition section uses asymmetric two-column layout; artist row gains secondary metadata column |
| Wide | > 1440px | Grid columns expand to five for artwork; max content width caps at ~1400px with auto margins; hero text scales to full `{typography.display-xl}` 64px |

### Touch Targets

- All nav-bar interactive elements minimum 44×44px regardless of visual text size
- Artist-row tap target spans full row width and 56px minimum height
- Filter-strip items padded to minimum 40px height
- Artwork cards link the entire card including image and text block

### Collapsing Strategy

- Hamburger drawer on mobile draws from left, black background matching `{colors.surface-dark}`, white links in `{typography.title-md}`
- Filter-strip becomes horizontally scrollable on mobile with scroll-snap alignment per category
- Hero full-bleed reduces to 70vh on mobile to allow content fold discovery
- Artwork-detail meta grid collapses to single-column label-above-value stacking below 744px
- Footer column grid collapses 4→2→1 columns at tablet→mobile breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Brand typeface unconfirmed**: no font families were extracted from the live site; the system likely loads fonts via JavaScript after initial parse or uses a custom web font not visible to the extractor. The `'Helvetica Neue', Helvetica, Arial, sans-serif` stack is a placeholder based on institutional gallery conventions — verify against actual CSS before shipping.
- **Color palette is monochromatic by extraction**: only `#101010` was confirmed from the live site; `#ffffff` inferred from meta theme-color. All mid-tone values (`{colors.muted}`, `{colors.hairline}`, `{colors.surface-soft}`) are logically derived, not measured.
- **No accent or interactive-state colors confirmed**: the gallery may use a subtle warm or cool tint for hover states, links, or active filters that was not captured. Check computed styles on links and form focus rings.
- **Logo mark treatment unknown**: whether Pace uses a wordmark, monogram, or icon lockup at small sizes could not be determined; nav-bar logo spec above is placeholder.
- **Animation/transition timing**: the gallery's micro-interaction signature (fade speed, transform easing on artwork hover) is undocumented — assume 200ms ease for transitions unless site inspection confirms otherwise.
- **Artwork inquiry flow**: the modal or page-based inquiry form pattern, including its field set and validation behavior, could not be assessed from extraction.
