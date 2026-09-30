---
version: alpha
name: "Carbon & Hyde"
source_url: "https://www.carbonandhyde.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Carbon & Hyde wears its dark canvas (#191919) as a deliberate provocation — periwinkle (#899df1) glows against near-black the way a diamond catches stage light, turning the typically cream-and-gold language of fine jewelry into something electric. The brand's Los Angeles origin shows in a confident lightness: where heritage jewelers reach for antiquated serif hierarchies, Carbon & Hyde pairs Spectral (a screen-optimized editorial serif) against Untitled Sans Web in a system that reads equally well on phone glass and in a gallery caption. Borders and surfaces build in charcoal strata (#313131, #252525) rather than collapsing to white, so every product image floats as a lit specimen rather than a catalog scan. The periwinkle primary sits close enough to cornflower blue to feel gemstone-adjacent without feeling safe; it carries CTAs, hover states, and form focus rings, while steel blue (#8ba8c8) handles informational tags and link highlights. Red (#ff0000) is reserved for sale or urgency flags only — a pure signal with no decorative ambition. {rounded.none} to {rounded.sm} govern the hard geometry of buttons and inputs, echoing the faceted planes of cut stone; {rounded.full} appears only on badge pills, never on cards or CTAs. Spacing is generous at the product level — full-bleed hero imagery and wide column gutters — then collapses on mobile, where a single-column scroll treats each product card as a full-viewport moment. The overall register is Los Angeles studio-gallery: dark, lit, unhurried, with one charged color that holds all the energy.

colors:
  primary: "#899df1"
  primary-active: "#6b82e0"
  primary-disabled: "#4a5480"
  ink: "#ffffff"
  body: "#d4d4d4"
  muted: "#888888"
  muted-dark: "#6a6a6a"
  hairline: "#313131"
  canvas: "#191919"
  surface-soft: "#252525"
  surface-card: "#2d2d2d"
  charcoal: "#313131"
  on-primary: "#191919"
  accent-steel: "#8ba8c8"
  alert: "#ff0000"

typography:
  display-xl:
    fontFamily: "'Spectral', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Spectral', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Spectral', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Untitled Sans Web', 'Montserrat', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Untitled Sans Web', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  badge-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
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
  announcement-bar:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    kickerTypography: "{typography.title-md}"
    minHeight: 100vh
    layout: "full-bleed"
  product-detail-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    metaTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    salePriceColor: "{colors.alert}"
    originalPriceColor: "{colors.muted}"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  collection-grid:
    backgroundColor: "{colors.canvas}"
    columns: 3
    columnsMobile: 1
    gap: "{spacing.xl}"
    paddingInline: "{spacing.section}"
  filter-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  price-tag:
    regularColor: "{colors.ink}"
    saleColor: "{colors.alert}"
    originalColor: "{colors.muted}"
    typography: "{typography.price-display}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingBlock: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — A zero-radius rectangle filled with periwinkle (#899df1) carrying tight uppercase tracked lettering in Untitled Sans Web at 13px, ls 0.1em. Hard-cornered geometry echoes the faceted planes of cut stone — no pill softness anywhere in the CTA system. On hover the fill deepens to `{colors.primary-active}` (#6b82e0); disabled state collapses to a flat `{colors.primary-disabled}` charcoal-blue with muted text, signaling inertia rather than absence. Fixed at 48px height for consistent alignment across PDP, cart drawer, and newsletter inline.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and white text, same uppercase Untitled Sans Web tracking as primary. Acts as the ghost foil on dark surfaces — used for "Add to Wishlist" and secondary nav CTAs where periwinkle would compete with product imagery. Hover inverts to white fill, dark text.

**`button-ghost`** — No border, no fill; muted gray text in `{typography.button-sm}`. Reserved for tertiary links like "View Details" beneath product cards and inline editorial CTAs where strong visual weight would disrupt flow.

### Badges
**`badge-pill`** — Periwinkle pill with `{colors.on-primary}` text, tight caption scale. Marks collection labels, material callouts ("18K Gold", "Lab Diamond"), and editorial tags on lookbook cards. The `{rounded.full}` is the sole exception to the brand's hard-corner rule, intentionally reserved for floating metadata rather than interactive controls.

**`badge-sale`** — Identical pill geometry with pure #ff0000 fill and white text. Appears as a corner overlay on product card images during sale events. Its rawness is deliberate — the red alarm flag reads immediately in a dark, restrained system without any softening.

### Text Input
**`text-input`** — `{colors.surface-soft}` (#252525) fill, no border radius, 1px hairline border (#313131) that steps up to periwinkle on focus. 48px height matches button height so form rows align cleanly. Placeholder text in `{colors.muted}`. Error state uses `{colors.alert}` border with caption-scale error message below.

### Navigation
**`nav-bar`** — 64px dark bar flush against the canvas, typeset in uppercase 13px Untitled Sans Web at ls 0.08em. Logo center or left; cart and search icons right-aligned. A 1px hairline border-bottom in `{colors.hairline}` separates the nav from hero content below. On scroll past 100px, the bar gains a subtle backdrop-blur with `{colors.surface-soft}` background without a color shift — dark stays dark.

**`announcement-bar`** — A 36px `{colors.charcoal}` strip above the nav, `{typography.caption}`-scale text in `{colors.body}` centered. Used for shipping thresholds, new collection launches, or limited-time notices. Kept deliberately muted so it registers as information, not promotion.

### Product Card
**`product-card`** — Zero-radius image container on the `{colors.canvas}` ground, square or portrait crop (1:1 or 3:4). Product name in `{typography.body-sm}`, price in `{typography.price-display}`. On hover a secondary image swaps in-place with a crossfade — no slide, no lift — preserving the stillness of the grid. Sale `badge-sale` overlays the top-right corner of the image at 8px inset. No card border; product floats on the continuous dark field.

### Hero
**`hero`** — Full-bleed, viewport-height dark imagery with a centered or left-anchored headline in Spectral at `{typography.display-xl}` (56px, weight 300). A `{typography.title-md}` uppercase kicker sits above the headline as a chapter label. One `button-primary` CTA anchors below. The near-zero font weight in Spectral light creates drama without mass — diamonds and controlled light carry the visual energy.

### Product Detail Header
**`product-detail-header`** — Product name in `{typography.display-md}` Spectral (36px, weight 300), material/category meta in `{typography.title-sm}` uppercase kicker above the title. Price in `{typography.price-display}` below, with original price in `{colors.muted}` strikethrough and sale price in `{colors.alert}`.

### Section Label
**`section-label`** — Uppercase `{typography.title-md}` in `{colors.muted}` with a 1px `{colors.hairline}` rule beneath. Acts as a chapter divider within editorial pages and collection intros: "New Arrivals", "The Edit", "By Material".

### Collection Grid
**`collection-grid`** — Three columns on desktop, two on tablet, one on mobile. `{spacing.xl}` gap between cards, `{spacing.section}` horizontal padding on wide viewports. No surface variation — all cards live on the same `{colors.canvas}`, creating a continuous field of lit objects.

### Filter Tags
**`filter-tag`** — `{colors.surface-card}` (#2d2d2d) zero-radius chips for collection filtering. Active state flips to `{colors.primary}` fill with `{colors.on-primary}` text. Inactive hover lightens background by ~8%. Chips overflow into a horizontal scroll on mobile.

### Price Tag
**`price-tag`** — Regular price in `{colors.ink}`, original (crossed out) in `{colors.muted}`, sale price in `{colors.alert}`. All use `{typography.price-display}` for consistent weight across grid and PDP contexts.

### Footer
**`footer`** — Slight surface lift to `{colors.surface-soft}` over canvas, 1px `{colors.hairline}` top border. Navigation links in `{typography.body-sm}` at `{colors.body}`. Legal and copyright text in `{colors.muted}`. Newsletter input uses the `text-input` spec inline with a `button-primary`, stacked vertically on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero headline drops to display-md (36px Spectral); horizontal padding reduces to {spacing.base}; announcement bar height increases to 44px |
| Tablet | 744–1128px | Two-column product grid; nav shows full logo, condensed links, search icon visible; hero layout shifts to left-anchored text with product imagery right; section padding at {spacing.xl} |
| Desktop | 1128–1440px | Three-column product grid; full nav bar at 64px height; hero at full 100vh with display-xl Spectral headlines; side-by-side PDP layout with imagery left and controls right |
| Wide | > 1440px | Content max-width caps at 1400px centered; hero text block capped at 680px; increased inter-section whitespace; grid columns remain at three |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Filter tag chips expand to full row tap area on mobile
- Nav icon buttons (cart, search, hamburger) padded to 48×48px tap area
- Swipe left/right on mobile PDP imagery triggers secondary image view

### Collapsing Strategy
- Hamburger menu reveals full-height dark drawer with stacked nav links in `{typography.title-md}` uppercase; periwinkle left border marks active section
- Facet filters move into a bottom drawer on mobile, triggered by a fixed "Filter" pill button
- Footer columns stack vertically; newsletter block floats to top of footer on mobile
- Announcement bar collapses to single-line scrolling marquee if content exceeds viewport width on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; dark canvas default assumed from #191919 and overall palette directionality
- Font weight range for Spectral not confirmed from extraction; light (300) assumed from fine jewelry editorial conventions and the "edge" positioning
- Montserrat listed in extracted font stack but may serve as a fallback rather than a primary display face; Untitled Sans Web treated as the primary UI sans
- "slick" in extracted font stack is the Slick.js carousel library, not a typeface — filtered as a framework artifact
- Exact button border treatment (0px vs 1px vs xs) not confirmed from static extraction; zero-radius assumed from brand name ("edge") and dark geometric aesthetic
- Hover transition durations and easing curves not extractable from static scan
- Exact product card aspect ratio (1:1 vs 3:4) not confirmed
- No icon system details available (custom drawn vs Feather/Heroicons/Phosphor)
- Animation behavior for hero section (parallax, fade-in) not confirmed
- Drawer and modal overlay background opacity not confirmed; standard 0.6–0.8 scrim over canvas assumed
