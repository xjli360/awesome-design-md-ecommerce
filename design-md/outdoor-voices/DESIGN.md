---
version: alpha
name: "Outdoor Voices"
source_url: "https://outdoorvoices.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  OV Gothic — a custom wide-set grotesque with slightly squared terminals — announces itself at every category landing page, choosing legibility over refinement; it is an activewear typeface for people who want to be read from across a park. The electric cobalt (#000f9f) drives every primary CTA and anchors the brand's energetic register, sitting alongside a secondary teal (#0e7a82) that marks collection wayfinding and editorial eyebrow labels — two blues inhabiting the same system without collision because they occupy distinct functional layers rather than competing for the same attention. A warm amber (#f59e0b, #fbbf24) surfaces as a tertiary accent on sale callouts and campaign highlights, the visual equivalent of a yellow highlighter stroke over recreational enthusiasm.

  The dark layer — #141414 for ink, #202020 for body text, a near-black scrim on campaign pages — gives the site enough gravity to prevent vivid product photography from floating unanchored. Surface tones draw from a cool gray-lavender register (#f4f4f6, #e5e5eb) rather than the warm beige that dominates most apparel direct-to-consumer sites, a quiet signal that OV's palette consciousness runs all the way down to its off-whites. Sharp corners appear on primary interactive elements — buttons, size tiles, text inputs — signaling that utility rather than softness is the underlying promise of the brand.

  Pill shapes ({rounded.full}) are reserved specifically for filter tags, activity badges, and color swatches — the "Running," "Cycling," "Yoga" use-case labels that encode OV's community-segmented identity. This creates a visual grammar where roundness signals selectability and sharp corners signal action. Section gaps at 64px create pauses that feel like rest intervals between effort, and product cards carry no border radius, flush-filling image to edge with no interior padding.

  Merlo, a secondary editorial face with humanist serif warmth, appears on campaign landing pages that OV Gothic, in its utilitarian breadth, cannot carry alone. TTCommonsPro handles body copy and all navigation UI, a neutral geometric sans that stays out of the way while the custom brand typefaces lead. The combined typographic system operates in three registers — declarative (OV Gothic), editorial (Merlo), and functional (TTCommonsPro/Inter) — that together support the brand's dual role as recreational community and e-commerce storefront.

colors:
  primary: "#000f9f"
  primary-active: "#272d45"
  primary-disabled: "#676986"
  on-primary: "#ffffff"
  ink: "#141414"
  body: "#202020"
  muted: "#545454"
  muted-soft: "#949494"
  hairline: "#e2e2e2"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#f4f4f6"
  surface-border: "#e5e5eb"
  teal: "#0e7a82"
  purple-gray: "#676986"
  amber: "#f59e0b"
  amber-bright: "#fbbf24"
  dark-navy: "#272d45"
  error: "#dd000d"
  error-dark: "#b72121"
  scrim: "#141414"

typography:
  display-xl:
    fontFamily: "'OV Gothic', 'NordiquePro', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'OV Gothic', 'NordiquePro', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'OV Gothic', 'NordiquePro', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-editorial:
    fontFamily: "'Merlo', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  eyebrow:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "Inter, 'TTCommonsPro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'TTCommonsPro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'TTCommonsPro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'TTCommonsPro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 14px 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    padding: "0 0 16px 0"
  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    paddingTop: 64px
    paddingBottom: 64px
  hero-dark:
    backgroundColor: "{colors.dark-navy}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-primary}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.surface-card}"
  activity-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.surface-border}"
    padding: 6px 12px
    height: 36px
  activity-badge-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 12px
    height: 36px
  sale-badge:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  eyebrow-label:
    textColor: "{colors.teal}"
    typography: "{typography.eyebrow}"
  color-swatch:
    shape: circle
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1.5px solid {colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 52px
  size-selector-unavailable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    textDecoration: line-through
    rounded: "{rounded.none}"
    height: 44px
    width: 52px
  collection-tile:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.display-md}"
    labelColor: "{colors.ink}"
    overlayGradient: "linear-gradient(to top, rgba(20,20,20,0.5), transparent)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: 48px

## Components

### Buttons
**`button-primary`** — Full cobalt (#000f9f) fill with white uppercase TTCommonsPro at 14px, sharp right-angle corners throughout. Active state deepens to dark navy (#272d45); disabled falls to purple-gray (#676986) — a desaturated echo of the primary that reads as unavailable without introducing a semantic red. Full-width on mobile, auto-width on desktop.

**`button-secondary`** — White canvas with 1.5px ink border and the same uppercase button-md typography as primary, creating a clear CTA hierarchy without adding a new color to the frame. Used for "Add to Wishlist," "Learn More," and secondary checkout actions.

**`button-pill`** / **`button-pill-active`** — 36px-tall full-radius pills for filter chips, activity category selectors, and quick-add size rows. Default state renders in surface-card (#f4f4f6) with ink text; selected state inverts to full ink background with white text. The height step-down from 48px to 36px signals lower interaction weight than primary CTAs.

### Navigation
**`nav-bar`** — 64px bar with a 1px hairline bottom separator in light contexts; full ink (#141414) background on campaign and editorial pages (`nav-bar-dark`). Logo centers on mobile; on desktop it shifts left with nav links inline. Cart and account icons anchor the right edge, with a small cobalt dot indicating cart item count. On desktop, hovering main nav categories opens a mega-panel grid of collection tiles organized by activity type.

### Product Card
**`product-card`** — Zero border-radius cards in a CSS grid; 3:4 aspect-ratio image bleeds flush to all card edges with no interior padding. Title in TTCommonsPro 600/16px, price in 500/15px on a second line. A horizontal color swatch row beneath the name lets customers swap the displayed colorway image inline. Sale items receive an amber (#f59e0b) rectangular badge overlaid at the top-left corner of the product image.

### Hero
**`hero`** — Full-bleed photography with OV Gothic display-xl at 56px leading a declarative verb phrase. Subhead in Inter body-md at #202020, followed by a sharp-cornered primary CTA. Dark variant (`hero-dark`) uses the deep navy (#272d45) field with white headline — reserved for campaign launches, seasonal drops, and editorial editorial moments.

### Activity Badges
**`activity-badge`** — Pill-shaped filter tags that organize product grids by use case. Default state: cool gray-lavender surface (#f4f4f6) with a 1px border at #e5e5eb. Selected: full ink fill with white text. Badge typography — uppercase 11px/600/0.8px spacing — keeps labels dense and scannable in horizontally scrolling filter rows. These are OV's primary taxonomy signal, encoding community segments rather than generic lifestyle aspirations.

### Sale Badge
**`sale-badge`** — Amber (#f59e0b) rectangular tag with no border radius, overlaid on product imagery. Ink-colored uppercase badge text reads across varied photography backgrounds without requiring a contrasting outline.

### Color Swatch
**`color-swatch`** — 24px circular dots in a horizontal row on product cards and the product detail page. Selected swatch carries a 2px ink border ring; unselected shows 1px hairline. Hovering a swatch on desktop swaps the product image without a page load — a key pattern for OV's multi-colorway releases.

### Size Selector
**`size-selector`** — Square 44×52px tiles with sharp corners, 1px hairline border at rest, 1.5px ink border on selection. Unavailable sizes show a diagonal strike-through in muted (#545454) on a light surface (#f8f8f8) — same geometry as available tiles, no icon substitution or removal.

### Eyebrow Label
**`eyebrow-label`** — Uppercase 11px/700 TTCommonsPro in teal (#0e7a82) used above section headers and editorial callouts to signal activity category or editorial context. Teal distinguishes these from the cobalt primary system while remaining within the blue-green family.

### Collection Tile
**`collection-tile`** — Lightly rounded (8px) image tiles for category landing pages; OV Gothic display-md labels float over a gradient overlay that fades from semi-opaque ink at the bottom to transparent at top. Used in the mega-nav panel and homepage activity-category grid.

### Search
**`search-bar`** — Full-pill input on the near-white surface (#f8f8f8) with a magnifying-glass prefix icon in muted-soft (#949494). On desktop, opens as a full-width overlay panel; on mobile, replaces the nav bar entirely with a dismiss affordance at the right edge.

### Footer
**`footer`** — Full-width ink (#141414) field with white body-sm link copy in a four-column grid on desktop, single-column stacked on mobile. Section headings in TTCommonsPro 600; link rows in Inter 400 at surface-card (#f4f4f6). Social icons render as bare glyphs in the final column without enclosing circles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero stacks image above text block; filter badges scroll horizontally in a snap container; button-primary goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows logo and condensed text links without mega-panel; hero maintains split layout at reduced padding |
| Desktop | 1128–1440px | Three or four-column product grid; full mega-nav panel on hover; hero full-bleed with side text overlay; mega-panel opens on hover delay ~150ms |
| Wide | > 1440px | Content max-width capped at 1440px with auto side margins; product grid stays at four columns; section padding increases proportionally |

### Touch Targets
- Cart, account, and hamburger icons are minimum 44×44px tap targets on mobile
- Color swatches scale from 24px to 32px on mobile to reduce mis-tap rate
- Size selector tiles remain 44px tall on mobile, arranged in a 3-per-row grid
- Activity badge pills maintain 36px height minimum on touch viewports
- Swatch hover behavior replaced by tap-to-select on touch devices

### Collapsing Strategy
- Mega-nav collapses to a full-height slide-in drawer with activity category accordion sections expanding inline
- Product card color swatch rows collapse to "N colors" text link on viewport widths below 375px
- Footer four-column grid collapses to single-column accordion with TTCommonsPro 600 section headings as expand triggers
- Hero split layout stacks image above text below 744px; text block receives 24px horizontal padding
- Horizontal filter badge rows use CSS scroll-snap with partially visible trailing pill indicating scrollability

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- No meta theme-color extracted; dark-mode system theming behavior is inferred from the dark surface color values, not confirmed
- Button border-radius not confirmed from CSS extraction — sharp corners (0px) assumed from brand aesthetic; actual value may be xs (4px)
- OV Gothic and Merlo are proprietary typefaces; weight axis ranges and OpenType feature sets are not confirmed from extraction
- Amber (#f59e0b, #fbbf24) usage contexts are inferred — distinction between sale badge, editorial highlight, and campaign accent roles may differ from documented usage
- Purple-gray (#676986) is mapped to disabled and muted states; it may also appear as an active product colorway swatch in the UI
- Mega-nav animation timing, hover delay, and easing curves not extractable from static color/font extraction
- Grid gutter widths, column counts, and exact max-content-width breakpoints not confirmed from extraction
- #007aff appears to be an iOS system color surfacing through the Shopify/OkendoReviews widget stack, not an OV brand token — excluded from palette
