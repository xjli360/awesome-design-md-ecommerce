---
version: alpha
name: "Lumas"
source_url: "https://www.lumas.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cobalt blue (#003399) arrives uninvited in a room of light grays — Lumas runs every primary call-to-action, navigation active state, and interactive underline through that single loaded frequency while surfaces sit at #f2f2f2 and #f3f3f3, approximating the flat-lit neutrality of a physical gallery wall. The signal is gallery authority: most e-commerce sites reach for warmth to convert; Lumas reaches for institutional cool. Type is set entirely in Archivo, a narrow grotesque that performs across the full weight range the brand demands — Archivo Black for the oversized hero headlines that announce curated collections and seasonal editions, regular weight for dimension and medium labels that need to recede behind the artwork. Corners are held close to zero throughout the interface: product cards, buttons, and filter chips carry no rounding or at most 2px, enforcing the rectilinear logic of a framed print mounted flush against a wall. The palette extends in two directions from the cobalt core: downward into a warm umber (#8b6f47) that surfaces on framing selectors, material swatches, and edition-provenance strips — the color of a wooden frame — and sideward into a violet spectrum (#582c83 deep, #9678d3 medium) reserved for editorial badges, "LUMAS ORIGINAL" provenance labels, and promotional banners that need to register as culturally distinct from the primary blue. This two-axis chromatic logic lets Lumas signal price tier, edition type, and medium category through color alone without cluttering product thumbnails with text overlays. Spacing is generous — the gallery grid breathes at 24–32px column and row gaps, giving each artwork thumbnail room to read as a framed object rather than a catalog tile. Hover states are quiet: a card border lifts from transparent to hairline gray rather than adding shadow, keeping the ambient gallery hush intact. The footer inverts to near-black (#1a1a1a) canvas, a hard cut that signals the transition from commercial browsing to institutional information — shipping, certificates of authenticity, corporate provenance — and reinforces that Lumas is selling art, not just prints.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aacc"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#808080"
  muted-soft: "#aaaaaa"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  earth: "#8b6f47"
  editorial-deep: "#582c83"
  editorial-mid: "#9678d3"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Archivo Black', 'Archivo', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 900
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo Black', 'Archivo', Arial, sans-serif"
    fontSize: 38px
    fontWeight: 900
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  edition-label:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 14px 28px
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    underlineOnHover: true
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    activeIndicator:
      color: "{colors.primary}"
      thickness: 2px
      position: bottom
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    border: "1px solid transparent"
    borderHover: "1px solid {colors.hairline}"
    shadow: none
    imagePadding: "{spacing.sm}"
    metaPadding: "{spacing.sm} 0"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-artist:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  artwork-badge-editorial:
    backgroundColor: "{colors.editorial-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  artwork-badge-edition:
    backgroundColor: "{colors.earth}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  artwork-badge-original:
    backgroundColor: "{colors.editorial-mid}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    minHeight: 560px
    layout: left-aligned-over-full-bleed-image
    overlayScrim: "linear-gradient(to right, rgba(0,0,0,0.45) 0%, transparent 60%)"
  editorial-banner:
    backgroundColor: "{colors.editorial-deep}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  gallery-grid:
    columns: "4 (desktop) / 3 (tablet) / 2 (mobile)"
    columnGap: "{spacing.lg}"
    rowGap: "{spacing.xl}"
    backgroundColor: "{colors.canvas}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 48px
    gap: "{spacing.lg}"
  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  tag-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  size-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    padding: 10px 16px
  provenance-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderLeft: "3px solid {colors.earth}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Flat cobalt (#003399) rectangle with zero border radius; height 48px, padding 14px 28px. Archivo SemiBold at 15px with 0.3px tracking. Active state darkens to #002277 with no transition delay. Disabled state bleaches to #99aacc. No shadow at any state — depth is communicated through color shift alone, consistent with the gallery's avoidance of skeuomorphic elevation.

**`button-secondary`** — White fill with a 1px cobalt border and cobalt label. On hover the fill shifts to #f2f2f2 and border steps to #002277, keeping the hierarchy clear without introducing a new color. Same geometry and type scale as `button-primary`.

**`button-ghost`** — Transparent background, ink-colored label, underline appears on hover. Used for tertiary actions like "See all works" inline within editorial modules where a bordered button would compete with artwork.

### Navigation

**`nav-bar`** — 64px tall, white canvas, 1px hairline-soft bottom border. Category links in Archivo Medium 14px; the active category receives a 2px cobalt underline flush to the bottom edge rather than a background highlight — the line functions like a gallery label card below a mounted work. Logo rendered in Archivo Black at display scale, left-aligned; account/cart icons sit right.

### Product Card

**`product-card`** — Zero border radius, no drop shadow. Image area sits on #f2f2f2 to ensure white-edged prints float rather than bleed. On hover the outer border lifts from transparent to 1px #dddddd — the quietest possible acknowledgement that the tile is interactive. Artist name is muted gray caption below title; price renders in `{typography.price-display}` (Archivo Bold 20px) flush left. Edition and category badges overlay the top-left corner of the image using the three `artwork-badge-*` variants.

### Artwork Badges

**`artwork-badge-editorial`** — Deep violet (#582c83) pill-free rectangle, white uppercase Archivo 11px/0.6px tracking. Marks thematic editorial groupings ("URBAN LANDSCAPES", "ABSTRACT"). **`artwork-badge-edition`** — Umber (#8b6f47) background signals limited-edition or numbered works; the earth tone reads as material, analogous to a wooden frame. **`artwork-badge-original`** — Medium violet (#9678d3) for "LUMAS ORIGINAL" designation, one step lighter than editorial to signal a different authority tier.

### Hero

**`hero`** — Full-bleed image at minimum 560px tall with a left-to-transparent gradient scrim (rgba 0,0,0,0.45 → transparent at 60%) that lifts white headline and body copy off dark photography. Headline in Archivo Black 52px / -0.5px tracking, subline in Archivo Regular 16px / 1.6 leading. Primary CTA button sits below at 48px height. On mobile the scrim extends further right and the headline drops to `{typography.display-lg}`.

### Editorial Banner

**`editorial-banner`** — Full-width deep violet (#582c83) block with white headline in `{typography.display-md}` and body in `{typography.body-md}`. Used for collection launches and seasonal campaigns. Generous vertical padding (48px top/bottom) signals a section break rather than an inline callout.

### Gallery Grid

**`gallery-grid`** — Masonry-adjacent fixed-ratio grid at 4 columns desktop, 3 tablet, 2 mobile. Column gap 24px, row gap 32px. Uniform aspect-ratio image containers prevent layout shift; portrait and landscape artworks share the same container height and are letterboxed against #f2f2f2.

### Filter Bar

**`filter-bar`** — Sticky 48px bar below the nav with horizontal scroll on mobile. Category and medium filters as text links (Archivo 13px / muted gray); active filter gets cobalt color and a 2px bottom rule mirroring the nav active state. Sort dropdown sits right-aligned. `{tag-chip}` variants are used when filters are rendered as removable pills in a search-results context.

### Size Selector

**`size-selector`** — Square-cornered tiles listing print dimensions (e.g. "40 × 50 cm"). Default state: #f2f2f2 fill, 1px hairline border. Selected: cobalt fill, white text, cobalt border. Hover: surface-card fill. Type is Archivo Regular 14px. Sold-out sizes render with a diagonal strikethrough and muted text.

### Provenance Strip

**`provenance-strip`** — Light #f3f3f3 background with a 3px umber (#8b6f47) left border. Contains certificate-of-authenticity information, edition number, and print process details in Archivo Regular 14px. The umber border ties provenance visually to the `artwork-badge-edition` color, creating a consistent material signal across card and detail views.

### Search Bar

**`search-bar`** — Square-cornered 44px input against #f2f2f2 fill. Muted gray search icon left-inset. Border focus shifts to cobalt 1px. Autocomplete suggestions drop in a white panel with 1px hairline border, no shadow, results in `{typography.body-sm}`.

### Footer

**`footer`** — Near-black (#1a1a1a) full-width block, a hard inversion from the gallery canvas. Column links in Archivo Regular 14px / surface-soft color (#f2f2f2), headings in Archivo SemiBold 15px / white. Newsletter input sits in an inset #333333 field with white text. Trust badges (certificate, secure payment) render in muted-soft gray at caption size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column gallery grid; hero headline drops to `display-lg` (38px); nav collapses to hamburger + logo + cart; filter-bar becomes horizontal scroll strip; size-selector tiles stack 3-per-row |
| Tablet | 744–1128px | 3-column gallery grid; hero retains full-bleed with reduced padding; nav shows primary categories, overflow in dropdown; filter-bar visible but compacted |
| Desktop | 1128–1440px | 4-column gallery grid; full nav with all category links; hero at full 52px display-xl; editorial banner at full 48px vertical padding |
| Wide | > 1440px | Max content width capped at 1440px, canvas bleeds; gallery grid holds 4 columns with larger row gaps (40px); hero image scales beyond container, anchored center |

### Touch Targets

- All interactive nav links minimum 44px tap height via vertical padding
- Size-selector tiles minimum 44 × 44px on mobile
- Filter-bar items padded to 44px height on touch breakpoints
- Product card entire surface is tappable; no sub-element tap zones on mobile

### Collapsing Strategy

- Primary nav collapses at < 1024px to hamburger drawer; drawer slides from left with cobalt accent on active item
- Filter-bar transitions from inline tabs to a "Filter & Sort" modal trigger button on mobile
- Footer column grid (4-up desktop) collapses to 2-up tablet then accordion on mobile
- Hero text overlay left-aligns and compresses to bottom-third strip on mobile with a stronger scrim

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from live extraction — zero/near-zero assumption based on gallery aesthetic; actual values may be 4–6px
- Font weight numeric mapping for "Black Fallback", "medium-fallback", "semibold-fallback" not confirmed; assumed 900 / 500 / 600 respectively as standard Archivo axis values
- Exact nav height not extracted; 64px is an estimate consistent with similar gallery platforms
- Hover and focus animation durations not captured — transition timing (likely 150–200ms ease) inferred from convention
- Mobile breakpoint pixel values not confirmed from source; 744px and 1128px are structural estimates
- Dark-mode variant unknown — no `prefers-color-scheme` tokens extracted
- Cart drawer and checkout flow design not captured; cobalt primary assumed to carry through but unverified
- Exact price formatting (currency symbol placement, sale/original price treatment) not extracted
