---
version: alpha
name: "Absolut Art"
source_url: "https://www.absolutart.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every piece in the Absolut Art inventory loads against an unbroken `{colors.canvas}` white, with the artwork occupying a full-width square cell and pricing surfaced only on hover — a product grid that borrows gallery-wall logic rather than retail-shelf logic. The brand's typographic hierarchy runs almost entirely on weight and size contrast: a light serif at generous tracking for editorial display moments, a clean neutral sans-serif for all transactional UI. There is no accent color racing for attention because the collection itself provides all the colour. Near-black `{colors.ink}` at `#1a1a1a` handles every heading, label, and CTA, while `{colors.muted}` carries supporting metadata such as artist nationality and medium. Hairlines at `{colors.hairline}` divide content zones with the subtlety of a paper fold rather than a wall — the whole surface reads as one continuous white room. Primary CTAs keep this logic: flat black rectangles at `{rounded.none}`, no shadow, no gradient, the button shape receding so the artwork beside it advances. The filter and browse experience sits in a collapsible left rail on desktop, where category chips carry `{rounded.full}` pill shape as the sole signal of interactivity against an otherwise-flat UI. Editorial sections — artist spotlights, curated collections — break the browse grid with asymmetric full-bleed image panels that pair a single large photograph with a sparse headline in a light display-serif weight, signalling that Absolut Art is as much a discovery platform as a transaction surface. Spacing is generous throughout: `{spacing.xl}` between cards, `{spacing.section}` between page sections, so each piece is afforded breathing room appropriate to its status as art rather than merchandise.

colors:
  primary: "#1a1a1a"
  primary-active: "#000000"
  primary-disabled: "#c0c0c0"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#767676"
  muted-soft: "#9e9e9e"
  hairline: "#e8e8e8"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f4f2"
  surface-card: "#ffffff"
  artwork-bg: "#f9f8f6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  tag-new: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  artwork-title:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  overline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em

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
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    padding: 0 32px
  artwork-card:
    backgroundColor: "{colors.artwork-bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.artwork-title}"
    artistTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.ink}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    padding: 6px 14px
    height: 32px
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    imagePosition: right
    padding: "{spacing.section}"
  media-type-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.tag-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  artist-byline:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "none"
    focusBorder: "1px solid {colors.hairline}"
    height: 44px
    padding: 0 16px
  price-range-display:
    textColor: "{colors.muted}"
    typography: "{typography.price}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Flat black rectangle at `{rounded.none}`, 44px tall, used for all primary transactional calls to action: "Add to Cart", "Make an Offer", "Enquire". Active state sharpens to pure `{colors.primary-active}` black; disabled state desaturates to `{colors.primary-disabled}` grey. Typography runs `{typography.button-md}` at 14px/500 with a trace of letter-spacing, giving the label an open quality that matches the surrounding white space rather than fighting it.

**`button-secondary`** — `{colors.canvas}` white fill with a 1px `{colors.ink}` border, sharing identical height and corner geometry with the primary button so the two sit on the same optical baseline in two-action zones such as offer confirmation modals or enquiry flows. The flat corner distinguishes it from the `{rounded.full}` filter chips elsewhere in the UI.

**`button-text`** — Underlined `{colors.ink}` text on a transparent background, reserved for low-priority tertiary actions: "See All Works", "Read More", "View Artist Profile". No background change on hover — only a subtle opacity shift.

### Text Input
**`text-input`** — Sharp-cornered field (`{rounded.none}`) with a resting `{colors.hairline}` border that firms to full `{colors.ink}` on focus. Canvas-white background throughout; error state appends a thin red underline accent rather than a flood fill, keeping the white-room aesthetic intact. Matches the 44px height used across all interactive controls for vertical rhythm consistency.

### Navigation
**`nav-bar`** — 64px horizontal bar on `{colors.canvas}` separated from page content below by a single `{colors.hairline}` hairline. The wordmark or logomark sits flush left; primary category links (Artists, Artworks, Prints, Editorial) run in `{typography.nav-link}` at 14px/400; search, account, and cart icons cluster at the far right. On scroll the bar acquires a subtle backdrop blur rather than a box shadow, preserving the clean surface without losing separation from content.

### Artwork Card
**`artwork-card`** — The primary browse unit. A 1:1 square image cell sits against `{colors.artwork-bg}` warm white; below it, `{typography.artwork-title}` renders the piece title in a light-weight serif, followed by the artist name in `{typography.body-sm}` `{colors.muted}` and price in `{typography.price}`. On hover a short slide-up overlay surfaces the "Add to Cart" and wishlist affordances, leaving the resting card free of action clutter. All corners are sharp at `{rounded.none}`, consistent with gallery-wall logic.

### Filter Chip
**`filter-chip`** — Pill-shaped `{rounded.full}` toggle in the browse rail, used for medium, style, artist, and price-range filters. Resting state: `{colors.canvas}` background, `{colors.hairline}` border, `{colors.ink}` text at `{typography.button-sm}`. Active state inverts fully to `{colors.ink}` background with `{colors.on-primary}` text. Height 32px keeps the filter strip compact; the pill shape is the only rounded element in the primary UI, making it the interaction landmark.

### Editorial Hero
**`hero-editorial`** — Full-viewport asymmetric two-column split: a single artwork or curated lifestyle photograph fills the right 55% of the canvas, while the left column carries a `{typography.display-xl}` headline at 40px/300-weight serif, a `{typography.body-md}` curatorial subline in `{colors.body}`, and a `button-primary`. The very light serif display weight signals editorial authority without competing with the image beside it. Outer padding `{spacing.section}` keeps all text well clear of viewport edges.

### Badges and Labels
**`media-type-badge`** — Small flat label on `{colors.surface-soft}` background with `{typography.overline}` uppercase 11px text in `{colors.muted}`, used to categorise artworks (Print, Original, Drawing, Photography) without visual interruption. **`new-badge`** — Same padding and corner geometry but `{colors.tag-new}` black background with `{colors.on-primary}` overline text, applied to newly listed works in curated feeds and artist pages.

### Search
**`search-bar`** — Borderless rectangle on a `{colors.surface-soft}` backing at rest; a `{colors.hairline}` outline appears on focus. No rounded corners, matching the flat geometry of text inputs. A search icon occupies the leading interior edge; a clear icon appears in the trailing position once text is entered. Heights match the 44px standard.

### Collection Header
**`collection-header`** — Rendered above browse grids on artist pages and curated collections. A `{typography.display-md}` heading in a light-weight serif sits above a `{typography.body-md}` curatorial note; the block closes with a `{colors.hairline}` rule and `{spacing.xl}` vertical padding before the grid begins. Keeps editorial framing visible without consuming excessive viewport height.

### Footer
**`footer`** — Full-width `{colors.ink}` dark bar carrying `{colors.on-dark}` white type in `{typography.body-sm}`. Four link columns (About, Artists, Support, Social) run side by side; a newsletter subscription module on the right contains a white-bordered `text-input` variant and an inverted-white button. `{spacing.xxl}` vertical padding gives the footer substantial visual weight as a closing element.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger + logo + cart icon; filter rail becomes a bottom sheet activated by a "Filter" pill button; hero-editorial stacks vertically with image above text |
| Tablet | 744–1128px | Two-column artwork grid; nav shows primary links, hides secondary utilities; filter rail becomes a collapsible horizontal chip strip above the grid |
| Desktop | 1128–1440px | Three-column artwork grid; left filter rail pinned alongside grid; full nav bar visible; hero-editorial runs side-by-side |
| Wide | > 1440px | Four-column grid; max-width container at 1440px with `{spacing.xxl}` outer margins; hero image stretches edge-to-edge within the container |

### Touch Targets
- All button and input controls minimum 44px tall (`button-primary`, `text-input`, `search-bar`)
- `filter-chip` at 32px height is paired with `{spacing.sm}` vertical margin to achieve a 48px effective tap zone on mobile
- Artwork cards are fully tappable; the hover-overlay add-to-cart becomes a persistent bottom action bar on mobile
- Nav icons in the mobile header padded to a minimum 44×44px tap target

### Collapsing Strategy
- Filter rail transitions from pinned left column (desktop) to horizontal chip strip (tablet) to bottom sheet (mobile)
- `hero-editorial` drops to full-width image banner above text column on mobile; headline scale reduces from `display-xl` to `display-sm`
- Collection header retains serif headline but reduces from `display-md` to `display-sm` at mobile breakpoint
- Footer columns stack vertically on mobile with `{spacing.lg}` between each section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site likely loads design tokens via JavaScript or was behind anti-bot at extraction time; all palette values above (`#1a1a1a`, `#e8e8e8`, `#f9f8f6`, etc.) are estimated from premium gallery-tier design conventions and should be replaced with values measured from the live site
- **No font families extracted** — the actual typefaces Absolut Art uses could not be confirmed; display-serif and sans-serif stacks above are placeholder fallbacks; the live site may use a custom foundry typeface or a licensed grotesque
- **No meta theme-color** — whether the brand uses any signature accent color beyond near-black and white for promotional modules, sale states, or hero overlays is unknown
- **Border-radius strategy unconfirmed** — `{rounded.none}` is assumed throughout based on gallery-aesthetic precedent; actual corner radii should be verified from the live site's computed styles
- **Sale and discount badge colors** — treatment of reduced-price or promotional labelling (color, placement, typography) could not be determined
- **Icon system style** — the weight, stroke width, and fill/outline approach of the action and category icon set is unknown
- **Artwork card hover mechanics** — exact animation duration, overlay opacity, and add-to-cart button positioning on hover were inferred from comparable platforms; should be verified against the live experience
