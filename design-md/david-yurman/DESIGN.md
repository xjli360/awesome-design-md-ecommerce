---
version: alpha
name: "David Yurman"
source_url: "https://www.davidyurman.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The cable-twist silhouette — coiled sterling wire borrowed from sculptor's studio and nautical rope — has been David Yurman's identifying motif since 1980, and the digital surface carries that restraint into a near-monochromatic neutral register where almost nothing competes with the jewelry. Nearly the entire extracted palette runs from near-black (#212121) through stacked grays to a soft off-white canvas (#fbfbfb): a deliberate progression that functions as gallery light, letting platinum catch and gemstone color read true without interference from a competing background hue. Proxima Nova drives all type with geometric openness at light-to-regular weights — display headers open with wide tracking at weight 300 rather than asserting at heavy bold, trusting white space over typographic muscle. Two functional accents cut through the gray field: #d82325 anchors sale pricing and promotional callouts, while the green pair #208402 and #114501 flags sustainability certifications and ethical-sourcing marks — neither color appears decoratively anywhere in the system. Primary CTAs present as flat near-black rectangles (`{rounded.none}`), echoing the hard-edge geometry of David Yurman's packaging, box clasps, and brand mark; pill forms and heavy radii are absent throughout. Product cards use tight grid gutters and soft-white surfaces (#f9f9f9), presenting each piece as though laid flat with nothing to distract from stone and metal. Hover and active states drift within the gray spectrum — #383838 on a near-black button, a deepened tone on links — rather than jumping to accent colors, signaling permanence over urgency and a brand that expects to be trusted rather than persuaded.

colors:
  primary: "#212121"
  primary-active: "#383838"
  primary-disabled: "#b8b8b8"
  ink: "#212121"
  body: "#3f3f3f"
  muted: "#6b6b6b"
  muted-soft: "#ababab"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  border-strong: "#c9c9c9"
  canvas: "#fbfbfb"
  surface-soft: "#f9f9f9"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#d82325"
  sale-active: "#701213"
  sale-soft: "#ff7f7f"
  sustainability: "#208402"
  sustainability-dark: "#114501"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.08em
  display-lg:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.06em
  display-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  display-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.03em
  title-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.04em
  title-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  caption:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em
  price-display:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  price-sale:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  label-uppercase:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
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
    padding: 14px 32px
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    textDecoration: underline
    rounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "{spacing.base}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.sale}"
  product-card-price-original:
    typography: "{typography.price-display}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-sustainability:
    backgroundColor: "{colors.sustainability}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    height: 48px
    padding: "0 {spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.base}"
  hero:
    textColor: "{colors.on-dark}"
    imageOverlay: "rgba(0,0,0,0.18)"
    minHeight: 600px
    padding: "0 {spacing.section}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-cta-bar:
    display: flex
    gap: "{spacing.md}"
    marginTop: "{spacing.xl}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "6px {spacing.base}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "6px {spacing.base}"
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "1px solid {colors.hairline}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.md}"
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — Flat near-black (#212121) rectangle using uppercase Proxima Nova tracked at 0.1em; even short labels like "Add to Bag" carry a composed, deliberate weight. Hover deepens to #383838 with no scale or shadow — the state change registers intent without excitement. Disabled state fades to #b8b8b8, holding rectangular form throughout.

**`button-secondary`** — Transparent fill bounded by a 1px near-black stroke with the same uppercase tracking. Used for secondary paths like "View More" or "Save to Wishlist." Active state adds a #f9f9f9 background tint while preserving the border, keeping the visual footprint stable.

**`button-ghost`** — Underlined text link in muted gray (#6b6b6b) at 11px uppercase, used for tertiary actions in product detail pages and footer navigation where visual weight must be suppressed.

### Navigation
**`nav-bar`** — 60px tall canvas-white bar with a 1px #d9d9d9 bottom hairline. Nav links set in 13px Proxima Nova at 0.06em tracking — slightly wider than body text but short of the dramatic spread reserved for display headlines. A mega-menu overlay opens on hover with a matching white fill and bordered top edge, arranging collections by material type, collection name, and product category in a multi-column grid.

### Product Cards
**`product-card`** — Zero-radius cards on #fbfbfb canvas with square 1:1 photography and 16px internal padding. Product name renders in 14px semi-bold below the image; retail price in regular 15px follows. Sale items show the #d82325 new price alongside a struck-through original in muted-soft (#ababab). A zero-radius "SALE" badge in #d82325 overlays the top-left corner of the image when marked down.

### Badges
**`badge-sale`** — Flat #d82325 rectangle, 10px uppercase Proxima Nova at 0.12em tracking, zero radius. Used exclusively for markdown pricing events, never for editorial or marketing copy.

**`badge-new`** — Identical geometry to badge-sale but filled near-black, flagging recent collection additions with the same contained, label-register tone.

**`badge-sustainability`** — #208402 background indicating recycled metal, certified stone provenance, or responsible-sourcing credentials. Part of the brand's environmental communications layer, not decorative.

### Forms & Search
**`text-input`** — Zero-radius input with a 1px #d9d9d9 border that sharpens to 1px #212121 on focus. Placeholder text in #6b6b6b, entered text in #212121, 48px tall. No box-shadow on focus — the border transition alone marks the active state, consistent with the brand's low-signal-economy approach.

**`search-bar`** — Shares the zero-radius form of text-input at a reduced 44px height, appearing in the site header search drawer.

### Filters
**`filter-chip`** — Small zero-radius bordered chip in 12px caption type, used to filter by metal, stone, price range, and collection. Active state flips to solid near-black fill with white type — a clear binary rather than a tint.

### Product Detail Controls
**`swatch-selector`** — 24px circular dot (`{rounded.full}`) for color or metal variation selection. Active swatch gains a 2px #212121 ring; inactive swatches carry a 1px #d9d9d9 border.

**`size-selector`** — Zero-radius 44px button for ring sizes and chain lengths. Active state mirrors button-primary with solid near-black fill and white text, keeping size-picking visually aligned with add-to-cart intent.

**`accordion`** — Zero-background accordion for product details, shipping, and material specifications. A 1px #d9d9d9 bottom hairline divides each row; title in 14px semi-bold Proxima Nova at 0.04em tracking. No background color change on expand.

### Hero
**`hero`** — Full-bleed editorial photograph with a thin dark overlay (rgba(0,0,0,0.18)) preserving image richness while ensuring white type legibility. Display-xl Proxima Nova at 48px/weight 300 with 0.08em tracking renders the campaign headline. CTAs sit in a flex row 32px below the headline.

### Footer
**`footer`** — Near-black (#212121) fill inverts the canvas-primary hierarchy of the rest of the site, using the same color as the primary button to create visual bookend closure. Body copy and primary links render white; secondary items like legal copy drop to muted-soft (#ababab) for reduced visual emphasis.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces full menu bar; hero height reduces to ~400px; filter row converts to modal bottom sheet |
| Tablet | 744–1128px | 2-column product grid; condensed nav with abbreviated labels; hero at ~500px; mega-menu collapses to single-column panel |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with mega-menu; hero at 600px+; inline filter panel visible alongside grid |
| Wide | > 1440px | Content max-width ~1440px centered; grid gutter increases; hero image fills viewport while content column remains capped |

### Touch Targets
- All buttons minimum 48px tall per WCAG 2.5.5
- Swatch selectors: 24px visual size, recommend 44px touch area via padding or negative margin
- Nav links: 44px minimum tap area even when visual text height is shorter
- Size selector buttons: 44px height with adequate spacing between adjacent sizes

### Collapsing Strategy
- Primary nav collapses to hamburger icon + centered wordmark at < 744px
- Mega-menu converts to stacked accordion drawer inside a slide-in panel on mobile
- Product filter row converts to full-screen or modal bottom sheet on mobile, triggered by a "Filter & Sort" bar
- Hero CTAs stack vertically below 480px
- Product grid steps 1-col → 2-col → 3–4 col across mobile / tablet / desktop breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- True white (#ffffff) was not extracted; canvas and card surfaces are inferred as near-white (#fbfbfb, #fdfdfd) — confirm whether the page background is pure white or a warm off-white
- Gold or champagne accent color for 18k gold and special collections (e.g., Osetra, Stax) not captured in extraction — the site may use a warm gold tone for select editorial moments
- #ffffff for on-primary (white text on dark buttons) inferred, not extracted
- #000000 for modal/drawer scrim inferred, not extracted
- Exact nav height and sticky-scroll behavior not confirmed
- Animation timing and easing curves for hover transitions, mega-menu opens, and carousel slides not available
- Product image hover behavior (secondary image swap vs. zoom vs. none) not confirmed
- Mobile navigation drawer geometry (full-screen vs. side-panel, transition direction) not confirmed
- Whether a serif or script display typeface appears on special campaign or editorial pages beyond Proxima Nova — extraction returned no serif stack
- Exact grid gutter widths and column counts for product listing pages at each breakpoint not confirmed
