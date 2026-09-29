---
version: alpha
name: "Eyestorm"
source_url: "https://www.eyestorm.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fire-engine red (#ff0000) sitting against a field of bone-warm neutrals is not a gallery design choice — it is a commercial argument made in the visual register of the art it sells. Eyestorm trades in limited-edition prints by Damien Hirst, Marc Quinn, and Yoko Ono, and its interface encodes that collision between collecting and purchasing directly: the softest imaginable neutral tones (#eceaeb, #e7e5e2, #d7d4ce) layer from card surface to background to hairline in increments barely perceptible to the eye, while every primary action fires in a red that brooks no hesitation. Proxima Nova carries all type — ProximaNovaLtSemibold pulls artist names and editorial headings into a humanist register that lands between the gallery world's traditional serif gravity and the directness of an e-commerce interface. Sharp corners rule the entire layout: {rounded.none} applies to artwork thumbnails, product cards, form inputs, and buttons without exception, letting photography carry whatever visual softness the page needs rather than any softening in the chrome. Edition numbers and certificate-of-authenticity language appear at {typography.edition-number} scale directly beneath each price, foregrounding scarcity in the same visual breath as the artwork image. The accent green (#116633) is strictly reserved for in-stock indicators and confirmation states; accent blue (#224488) surfaces only in hyperlinks and informational callouts — both held so tightly to functional roles that they never read as decoration. The primary red — pure and unmodulated at #ff0000 — is the single voltage running through every add-to-cart button, active filter underline, and hover state, making a commercial claim in the same unflinching tone as the contemporary art it frames.

colors:
  primary: "#ff0000"
  primary-active: "#ed2e24"
  primary-disabled: "#ff9999"
  accent-green: "#116633"
  accent-blue: "#224488"
  ink: "#353535"
  body: "#4a4848"
  muted: "#767472"
  hairline: "#d7d4ce"
  canvas: "#ffffff"
  surface-soft: "#eceaeb"
  surface-warm: "#e7e5e2"
  surface-card: "#eceaeb"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Proxima Nova', 'ProximaNovaLtSemibold', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Proxima Nova', 'ProximaNovaLtSemibold', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  artist-label:
    fontFamily: "'ProximaNovaLtSemibold', 'Proxima Nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  edition-number:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.2px
  footer-heading:
    fontFamily: "'Proxima Nova', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.8px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    height: 60px
  filter-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    itemPaddingY: "{spacing.sm}"
    itemPaddingX: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    artistTypography: "{typography.artist-label}"
    artistColor: "{colors.ink}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    editionTypography: "{typography.edition-number}"
    editionColor: "{colors.muted}"
    padding: "{spacing.md}"
    gap: "{spacing.xs}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    overlayColor: "rgba(53,53,53,0.45)"
    minHeight: 480px
    paddingX: "{spacing.section}"
  artist-page-header:
    backgroundColor: "{colors.surface-soft}"
    nameTypography: "{typography.display-md}"
    nameColor: "{colors.ink}"
    bioTypography: "{typography.body-md}"
    bioColor: "{colors.body}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
  edition-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.edition-number}"
    rounded: "{rounded.none}"
    paddingY: "{spacing.xs}"
    paddingX: "{spacing.sm}"
  stock-indicator-available:
    textColor: "{colors.accent-green}"
    typography: "{typography.caption}"
  stock-indicator-soldout:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: none
  artwork-lightbox:
    backgroundColor: "{colors.ink}"
    overlayOpacity: 0.95
    imageMaxWidth: 800px
    captionTypography: "{typography.caption}"
    captionColor: "{colors.surface-warm}"
    closeButtonColor: "{colors.canvas}"
  certificate-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.edition-number}"
    borderTop: "1px solid {colors.hairline}"
    paddingY: "{spacing.md}"
    paddingX: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-warm}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.footer-heading}"
    headingColor: "{colors.canvas}"
    borderTop: "none"
    paddingY: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — A hard-cornered ({rounded.none}) rectangle in pure primary red (#ff0000), uppercase Proxima Nova at 13px/600 weight with 1px letter-spacing. Active state shades to #ed2e24 via `button-primary-active`; disabled washes to a light pink #ff9999. The all-caps uppercase treatment reads as commercial intent without hedging — this is the add-to-cart moment and the interface does not soften it with rounded corners or a gentle hover fade.

**`button-secondary`** — White canvas fill enclosed by a 1px solid ink (#353535) border, matching height and typography to `button-primary`. Used for wishlist saves, share actions, and secondary navigation flows where the primary red would compete visually with artwork imagery. Active state moves to `surface-soft` (#eceaeb) fill while retaining the ink border.

### Text Input

**`text-input`** — Square-cornered input on white, resting with a 1px hairline (#d7d4ce) border that sharpens to 1px ink on focus. No border-radius on any form element — the search bar, newsletter signup, and checkout fields all maintain the same rectilinear discipline as the artwork grid itself.

**`search-bar`** — Shares the flat-corner treatment of `text-input` but sits on `surface-soft` (#eceaeb) ground. Focus state swaps the border to 1px primary red rather than ink, the only interactive moment where the primary color appears in an outline rather than a fill.

### Navigation

**`nav-bar`** — 60px white bar with a 1px hairline bottom border. The Eyestorm logotype renders in primary red (#ff0000) — the only decorative deployment of the primary color outside CTA buttons. Navigation links use `typography.nav-link` at 13px/regular weight, deliberately understated to avoid visual competition with artwork titles in the hero zone below.

**`filter-nav`** — A horizontal category strip on browse and artist pages. Inactive labels sit in muted (#767472); the active category carries a 2px solid primary red bottom border — the same voltage as the CTA color but delivered as a hairline rule rather than a fill, preventing the filter row from dominating the artwork grid it governs.

### Product Card

**`product-card`** — A square-cropped 1:1 artwork image with no border-radius on `surface-card` (#eceaeb) ground. The artist name renders above the artwork title in `typography.artist-label` (uppercase, 0.8px tracking), followed by the title in `typography.body-md`, the price in `typography.price-display` (18px/600), and the edition line in `typography.edition-number` (11px, muted color). This vertical hierarchy puts the artist above the work above the commercial fact — a deliberate editorial ordering. Hover state adds a subtle box-shadow without altering corners or background.

### Hero

**`hero`** — Full-bleed artwork image behind a `rgba(53,53,53,0.45)` scrim that maintains photographic richness while keeping white headline copy readable at `typography.display-xl`. A single primary red CTA button sits below the headline copy. Minimum height 480px; generous `spacing.section` horizontal padding aligns the hero text column with the grid below.

### Artist Page Header

**`artist-page-header`** — A full-width `surface-soft` (#eceaeb) band that opens every artist landing page. Artist name in `typography.display-md` (24px/600, ink), followed by biography text in `typography.body-md`. The `spacing.xxl` vertical padding gives the artist identity room to breathe before the print grid begins below; this is the only layout zone where the warm neutral background carries significant visual weight rather than receding behind imagery.

### Edition Badge

**`edition-badge`** — A small flat chip in `surface-warm` (#e7e5e2) containing edition metadata ("Edition of 50", "Artist Proof", "Open Edition") in `typography.edition-number`. No border, no radius — the chip reads as a label woven into the card surface rather than a floating tag. Multiple badges can stack vertically beneath a price without creating visual clutter.

### Stock Indicators

**`stock-indicator-available`** — Caption-scale green (#116633) text, label "Available" or the remaining edition count. **`stock-indicator-soldout`** — Same scale in muted (#767472), "Sold Out". Neither uses a colored background or an icon glyph; the text color alone carries the functional signal, keeping the card's visual hierarchy anchored on the artwork rather than its availability state.

### Artwork Lightbox

**`artwork-lightbox`** — A near-opaque ink overlay (0.95 opacity) with the artwork image centered at up to 800px wide. Caption and edition details render in `typography.caption` at `surface-warm` (#e7e5e2) beneath the image. A white close control sits top-right. The near-total ink field strips away all environmental context and approximates the dark-room quality of physical print viewing — the deliberate choice of opacity 0.95 rather than pure black softens the frame without destroying its isolation.

### Certificate Strip

**`certificate-strip`** — A `surface-soft` band beneath the artwork detail text column, housing certificate-of-authenticity language, print specifications, and edition provenance in `typography.edition-number`. A single 1px hairline top border separates it from body copy above. The strip keeps legal and provenance copy present and accessible without elevating it to the same visual register as the artwork description.

### Footer

**`footer`** — Full-width ink (#353535) ground with `surface-warm` (#e7e5e2) body links, `canvas` (#ffffff) column headings in `typography.footer-heading` (uppercase, 0.8px tracking), and `body-sm` body link text. Four-column layout on desktop. The dark footer anchors the page and echoes the hero scrim treatment, creating a visual bracket — dark entrance, warm neutral middle, dark close — around the gallery's inventory.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to logo + hamburger drawer; hero reduces to 320px min-height; filter-nav becomes horizontally scrollable chip row; edition-badge wraps below price line |
| Tablet | 744–1128px | Two-column artwork grid; artist-page-header padding reduces to `spacing.xl`; filter-nav remains full horizontal strip; hero at 400px |
| Desktop | 1128–1440px | Three- or four-column artwork grid; full nav-bar link set visible; hero at full 480px+; certificate-strip expands to two-column detail layout |
| Wide | > 1440px | Content max-width constrained to ~1400px, centered; hero image fills edge-to-edge with extended scrim; grid gains outer gutter white space |

### Touch Targets

- All buttons maintain minimum 44px height on mobile
- Filter-nav items carry minimum 40px tap height within the horizontal scroll container; wrapping disabled
- Product card tap area covers the full card tile including padding, not just the image crop
- Artwork lightbox close control is minimum 44×44px with an expanded invisible tap region
- Stock indicator text is never the sole tap target for navigation — always paired with the parent card

### Collapsing Strategy

- Nav collapses to logo-left / hamburger-right at < 744px; all secondary links (About, Artists, Contact, FAQ) move into a full-height slide-in drawer on `surface-soft` background
- Artist-page-header biography truncates to 3 lines on mobile with a "Read more" inline toggle in `typography.body-sm`
- Footer four-column grid stacks to single column on mobile; column headings become accordion toggles, body links hidden until expanded
- Filter-nav becomes a no-wrap horizontal scroll row on mobile; active category is scrolled into center viewport on page load
- Hero text and CTA restack to bottom-aligned within the image frame on mobile, with reduced heading size stepping from display-xl to display-md

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was extracted; mobile browser chrome color and PWA manifest color are unspecified
- Nav bar height (60px) and logo dimensions are estimated; exact measurements were not captured
- Font weights beyond ProximaNovaLtSemibold (bold, extra-bold, thin variants) are inferred from the family name rather than confirmed from extracted CSS
- Body and muted color tokens (#4a4848, #767472) are derived by interpolation from the extracted #353535 ink — they do not appear directly in the extracted palette
- Hover transition durations and easing curves (for card lift, filter-nav active state, button color fade) were not extractable
- Exact artwork grid gutter widths and whether the layout uses strict equal-width columns vs. any masonry approach are unconfirmed
- Whether #224488 (accent blue) is a documented brand blue or present only in default hyperlink styling could not be confirmed
- Mobile hamburger drawer design and animation direction are unspecified
