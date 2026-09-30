---
version: alpha
name: "The Last Line"
source_url: "https://www.thelastline.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pavé stones — sapphire-blue, canary-yellow, tourmaline-pink — stacked in intentionally mismatched ear cuffs and tennis bracelets are the visual vocabulary The Last Line leads with: fine materials worn as though they cost nothing, mixed together freely. The canvas is near-clinical white (#ffffff) and a deep editorial black (#0d0d0d) that frames photography-first grids, letting gemstone color do the brand-building rather than graphic flourish. Primary calls-to-action carry no gold shimmer or ornamental fuss; they sit as sharp black rectangles or clean inversions, communicating that the brand's confidence lives entirely in the product. Letter-spacing opens wide at the display level — a hallmark of contemporary jewelry editorial that signals restraint without receding — while body copy sits tight and direct, closer to a magazine's commerce page than a traditional jeweler's verbose description. Buttons strip themselves of the typical luxury softness: no pill shapes, edges land at {rounded.none}, a deliberate signal that The Last Line is not in dialogue with heritage houses. The nav is minimal — wordmark flush left, a compact row of tracked uppercase category links, and a bag count — keeping header footprint small so the first viewport is almost entirely product. The brand's signature move is the "stacked ear party" imagery rendered at near-square crop, always against neutral backgrounds, allowing the density of color in the jewelry itself to supply all visual energy the page needs. Gold tones (#c9a84c) surface only in badge and callout accents — a footnote, not a foundation — resisting the instinct to lean on metallic warmth as shorthand for luxury.

colors:
  primary: "#0d0d0d"
  primary-active: "#333333"
  primary-disabled: "#999999"
  ink: "#0d0d0d"
  body: "#333333"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-accent: "#c9a84c"
  gold-soft: "#e8d5a3"
  jewelry-highlight: "#f5f0ea"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.08em
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.06em
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05em
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.15em
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
    height: 44px
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "1px solid {colors.ink}"
    paddingBottom: 2px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 0px
    height: 40px
    focusBorderColor: "{colors.ink}"
    labelTypography: "{typography.label-uppercase}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
  hero-fullbleed:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 80vh
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    imagePosition: center
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  jewelry-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  gold-badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 40px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  pdp-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  pdp-price:
    typography: "{typography.price}"
    textColor: "{colors.muted}"
  search-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    suggestionTypography: "{typography.body-md}"
    overlay: "rgba(0,0,0,0.4)"
    padding: "{spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    headlineTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    borderLeft: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 36px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.nav-link}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A full-black flat rectangle with zero border radius and uppercase tracked text at `{typography.button-md}`. Hover darkens the fill to `{colors.primary-active}`. Disabled drops to `{colors.primary-disabled}` while retaining the flat geometry. The hard edge is a deliberate design statement — warmth is earned through product photography, not rounded UI chrome.

**`button-secondary`** — Identical dimensions to `button-primary` but inverted: white fill with a `1px solid {colors.primary}` border. Used for secondary CTAs such as "View Collection" or "Learn More." On hover, the border may intensify or the fill may shift to `{colors.surface-soft}`; the flat rectangle geometry matches the primary sibling so both read as a unified system.

**`button-text-link`** — Inline text with a `1px` bottom border in `{colors.ink}`, no background, no padding box. Used for editorial navigation moments — "Shop the Look," "View All," "See Details." Hover may briefly remove the underline to signal interaction without disrupting reading flow.

### Forms

**`text-input`** — Bottom-border-only input (no enclosing box) aligned with luxury editorial convention. A single underline reads as form without furniture. The `focusBorderColor` strengthens to `{colors.ink}` on focus. Labels render above in `{typography.label-uppercase}` — small, tracked, uppercase — so the entire field reads as editorial rather than utilitarian.

### Navigation

**`nav-bar`** — 64px tall, white background, soft `1px hairline` bottom border. Wordmark sits left; category links in `{typography.nav-link}` (all-caps, 12px, widely tracked) run across the center on desktop. Bag icon and account icon right-aligned as minimal 24px touch targets. The nav has almost no visual weight — its job is to disappear so the hero image takes full ownership of the first viewport.

**`announcement-bar`** — A 36px strip sitting above the nav in `{colors.primary}`. Carries promotional text, free-shipping thresholds, or limited-edition callouts in `{typography.label-uppercase}`. Full-width, non-dismissable on first load.

### Product Grid

**`product-card`** — Square 1:1 crop, no border radius, no drop shadow. Product name in `{typography.title-sm}` (tracked uppercase), price below in `{typography.price}` and `{colors.muted}`. On hover a second editorial angle may replace the primary image. No inline add-to-cart button — the entire card is a link to the PDP, matching fine jewelry's high-consideration purchase model.

**`jewelry-badge`** — Flat black tag for collection callouts ("New," "Best Seller," "Limited"). Zero radius, white `{typography.label-uppercase}` text. Anchors to the top-left corner of the product image at absolute position, never overlapping the product itself.

**`gold-badge`** — Same flat geometry as `jewelry-badge`, filled `{colors.gold-accent}`. Used sparingly for "Exclusive," "Holiday," or event-specific callouts where a warm metallic signal is contextually appropriate.

**`filter-chip`** — Hairline-bordered flat chip for gemstone type, metal, price, and category filters. Active state inverts to `{colors.primary}` fill with white text, making selection state immediately scannable in a dense horizontal filter rail.

### Product Detail Page

**`pdp-title`** — `{typography.display-sm}` scale, weight 400, moderate letter-spacing. The jewelry name anchors the top of the right column; metal and stone variant selectors fall below in `{typography.body-sm}`. Stack is sparse and unhurried — fine jewelry copy earns attention by not demanding it.

**`pdp-price`** — 14px, weight 400, `{colors.muted}`, sitting below the title. Muted treatment communicates that desire precedes price consideration — a deliberate hierarchy inversion versus typical commerce defaults.

### Overlays

**`search-drawer`** — Full-width panel dropping from the nav rather than a centered modal. The search input renders at `{typography.display-sm}` scale so the user's typed query reads as headline-level, reinforcing the editorial register. Recent searches and product suggestions populate below in `{typography.body-md}` with small square product thumbnails.

**`cart-drawer`** — 400px right-panel with `{colors.canvas}` background and a `1px solid {colors.hairline}` left border. Items list in `{typography.body-sm}` for name and `{typography.price}` for cost. Subtotal and checkout CTA anchor the bottom of the panel with a `button-primary` filling the drawer width.

### Hero & Editorial

**`hero-fullbleed`** — Full-viewport or 80vh bleed image, typically a model shot or close-up product editorial. Headline in `{typography.display-xl}` (weight 300, 0.08em tracking) floats against the image with enough contrast to read without a scrim. CTA uses `button-primary` placed below the headline.

**`collection-header`** — A `{colors.surface-soft}` banner section between the nav and the product grid on collection pages. Centered display text in `{typography.display-md}`, generous vertical padding at `{spacing.section}`. May carry a one-line editorial subline in `{typography.body-md}` and `{colors.muted}`.

### Footer

**`footer`** — Inverted: `{colors.primary}` background, `{colors.on-primary}` text throughout. Four-column link grid on desktop (Shop, About, Help, Follow) in `{typography.nav-link}`. Newsletter input uses the same bottom-border-only style as `text-input`, adapted for the dark surface. Legal line in `{typography.caption}` at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + bag icon; hero switches to portrait or square crop; announcement bar truncates to single rotating message; filter bar scrolls horizontally beneath collection header |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark and bag with hamburger for category links; hero uses 16:9 landscape crop; collection-header padding reduces to `{spacing.xl}` |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all category links visible; hero is full-viewport bleed; filter bar horizontal with all chips visible simultaneously |
| Wide | > 1440px | Content capped at 1440px centered; side margins grow proportionally; four-column grid with wider column gutters; hero image reframes to ultra-wide crop |

### Touch Targets
- All nav icon buttons minimum 44×44px tap area regardless of visual icon size
- Filter chips minimum 40px height with 12px horizontal padding
- Product card entire tile is tappable; no separate CTA required on mobile
- Cart drawer quantity steppers and close button minimum 44px touch area
- Announcement bar links minimum 36px tap height

### Collapsing Strategy
- Category nav links collapse into a slide-from-left full-screen drawer on mobile and tablet; drawer background is `{colors.canvas}` with links in `{typography.title-sm}`
- Product filter bar collapses into a single "Filter & Sort" bottom-sheet trigger on mobile
- Footer four-column link grid collapses to single-column accordion sections on mobile; each section header uses `{typography.title-sm}` with a plus/minus toggle
- PDP two-column layout (image gallery left, details right) stacks vertically on mobile, full-width image carousel first

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable — the live URL returned a third-party "coming soon" page ("Ray Mosley - Manchester - Digital Strategy is coming soon"), not the actual brand site. All color values are inferred from The Last Line's known editorial aesthetic and standard fine jewelry conventions. The actual production palette may differ significantly.
- No font stacks were detected. Typography is inferred from The Last Line's editorial identity (clean grotesque, tracked uppercase for labels). Actual typefaces — including any licensed display serif or custom wordmark font — are unconfirmed.
- Meta theme-color was absent, providing no primary brand color signal.
- Signature gemstone accent colors (sapphire blues, tourmaline pinks, canary yellows visible in product photography) are not represented as UI tokens; it is unknown whether any of these bleed into backgrounds, hover states, or badge treatments in the live system.
- The "coming soon" redirect may indicate a domain migration, site rebuild, or regional geo-block; the canonical design system state of thelastline.com is entirely unverifiable from this extraction run.
- No information available on whether the brand uses a custom serif wordmark typeface distinct from body typography.
