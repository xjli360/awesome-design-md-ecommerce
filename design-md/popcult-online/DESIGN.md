---
version: alpha
name: "PopCult Online"
source_url: "https://popcult.online"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The deepest near-black (#040404) stretched across the canvas signals immediately that PopCult Online is a destination for dedicated collectors rather than a casual retail browse — this is the visual register of a specialty floor where a chase variant Funko commands the same weight as a headline. Against that ground, a collector-grade red (#cc3b3b) fires through CTAs, sale badges, and price highlights with an intensity that reads as limited-edition urgency rather than generic retail alarm. Its darker sibling (#bd0000) handles hover and active states, tightening the chromatic voltage without breaking internal logic — the two reds form a narrow range that rewards closer inspection. Poppins and Rubik share the typographic stage: Rubik's slightly rounded geometry at heavier weights anchors display headings with a confidence that suits shelves lined with licensed character figures, while Poppins handles body copy and UI labels with approachable geometric legibility that pop culture fans — who range from teenage newcomers to thirty-year completionists — can scan at a glance. Neither font reaches for editorial formality; both lean toward the bold-but-friendly register that Funko's own visual identity occupies. The near-blacks are varied and layered: #111111 anchors the main canvas, #1e1e1e lifts card surfaces one tier, and #272727 provides a third stop for hover states and interactive wells. This three-stop dark stack creates spatial depth without introducing hue — product cards appear to float above the page rather than sit flush. The muted rose (#e99292) handles disabled and secondary accent states, and #aaaaaa carries metadata like SKU labels and availability text. Rounded corners read as restrained — `{rounded.sm}` to `{rounded.md}` is the operative range; the brand doesn't reach for pill shapes except in filter chips and the search input, keeping the layout feeling structured and catalogue-like over a grid that may display dozens of items per row.

colors:
  primary: "#cc3b3b"
  primary-active: "#bd0000"
  primary-disabled: "#e99292"
  ink: "#fafafa"
  body: "#eeeeee"
  muted: "#aaaaaa"
  hairline: "#272727"
  canvas: "#111111"
  canvas-deep: "#040404"
  surface-soft: "#1e1e1e"
  surface-card: "#272727"
  surface-input: "#1e1e1e"
  border-input: "#272727"
  on-primary: "#fafafa"
  strike-price: "#aaaaaa"

typography:
  display-xl:
    fontFamily: "'Rubik', 'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Rubik', 'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Rubik', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Rubik', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.border-input}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    shadow: "0 2px 8px rgba(0,0,0,0.4)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    shadow: "0 4px 16px rgba(0,0,0,0.6)"
    transform: translateY(-2px)
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-exclusive:
    backgroundColor: "{colors.canvas-deep}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.canvas-deep}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentColor: "{colors.primary}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
  price-regular:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-sale-display:
    saleColor: "{colors.primary}"
    typography: "{typography.price-sale}"
    strikethroughColor: "{colors.strike-price}"
  footer:
    backgroundColor: "{colors.canvas-deep}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary action button renders in collector red (#cc3b3b) with white Poppins semi-bold type at 14px and 0.3px tracking. On hover it deepens to #bd0000, communicating add-to-cart and checkout urgency without animation overhead. Disabled state uses the muted rose (#e99292) at half opacity, preserving chromatic identity even when the action is unavailable.

**`button-secondary`** — A hairline-bordered ghost button with dark surface and white type, used for wishlisting, sharing, and filter-adjacent actions. The 1px border in #272727 is subtle on the dark canvas, making it read as a secondary affordance without visual competition against the primary red.

**`button-ghost`** — Transparent background with primary-red text, used for inline "View All" tails on category rows and see-more expansions where a full button would over-weight the UI.

### Search

**`search-input`** — A slightly elevated surface (#1e1e1e) container with `{rounded.md}` corners and a leading icon in muted gray (#aaaaaa). No floating label animation — placeholder disappears on focus immediately. Used both in the nav bar (icon-triggered expansion on mobile) and as a visible inline field on desktop.

### Navigation

**`nav-bar`** — Fixed to the deepest canvas (#040404) to create a hard visual anchor at the top of the viewport, perceptually darker than the page body beneath it. Nav links render in Poppins 500 at 14px in near-white (#fafafa). A 1px hairline in #272727 provides a floor separation from the content layer. Cart icon and logo occupy the rightmost and leftmost positions respectively.

### Product Cards

**`product-card`** — The core grid unit. Cards sit on a mid-dark surface (#272727) with an image zone backed by the slightly softer #1e1e1e, creating a recessed box that frames product photography. Product name renders in Poppins 600 at 14px; price renders in Rubik 700 at 18px — the numerical weight carries collection-value signal at a glance. A subtle shadow (0 2px 8px rgba(0,0,0,0.4)) lifts cards off the canvas. On hover, the shadow deepens and the card translates 2px upward — a light float that signals selection intent without full-scale animation.

### Badges

**`badge-sale`** — Red (#cc3b3b) fill anchored to the top-left corner of the product image, uppercase Poppins 700 at 11px with 0.5px tracking. Reads as sale urgency at thumbnail scale. **`badge-exclusive`** — Inverted treatment: deep canvas-black (#040404) fill with primary-red text and a 1px red border, marking chase variants and site-exclusives — the outlined style reads as special-edition rather than on-sale. **`badge-new`** — Neutral dark surface (#1e1e1e) with white type for recently listed items that carry no pricing urgency.

### Category Filters

**`category-pill`** — Soft dark surface pill with light body text (#eeeeee), rendered in a horizontal scroll row above product grids for IP filtering (Marvel, Disney, DC, etc.). Active state fills to primary red with white type — a binary toggle that's scannable at speed. Minimum height 36px ensures touch accessibility in the horizontal strip.

### Hero Banner

**`hero-banner`** — Full-width section on the deepest canvas (#040404) with a display headline in Rubik 700 at 40px. The accent red appears in headline highlights or keyword spans rather than as a background fill, preventing the hero from reading as an alert state. Body copy in Poppins 400 at 15px and a primary button below form a clean three-layer structure: headline → context → action.

### Price Display

**`price-regular`** — Rubik 700 at 18px in near-white (#fafafa), carrying list-price weight on product cards and PDPs. **`price-sale-display`** — Same typeface and size but rendered in primary red (#cc3b3b) for the markdown price, with the original struck through in muted gray (#aaaaaa). The red/gray contrast makes the discount immediately legible against the dark card surface without requiring a separate badge.

### Footer

**`footer`** — Deep-black canvas (#040404) with a top hairline in #272727 separating it from the product grid above. Column navigation links render in Poppins 400 at 13px in light body color (#eeeeee); legal and policy links step down to muted gray (#aaaaaa). Vertical padding uses `{spacing.xxl}` above and below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; category pills convert to horizontal scroll strip; search field hides behind icon tap; hero headline scales to `display-md` |
| Tablet | 744–1128px | Two- to three-column product grid; main nav links revealed inline alongside logo; search input visible inline rather than icon-only |
| Desktop | 1128–1440px | Four-column product grid; full nav with all category labels and potential dropdown menus; breadcrumb visible; hero at full `display-xl` |
| Wide | > 1440px | Grid stays at four columns; container max-width constrains layout with expanding side gutters to preserve readability |

### Touch Targets
- All product cards are full-tap zones; no inner link disambiguation needed on mobile
- Primary and secondary buttons maintain 44px height at all breakpoints
- Category pills maintain 36px minimum height in horizontal scroll row
- Cart, hamburger, and search icons each hold a minimum 44×44px hit area

### Collapsing Strategy
- Navigation collapses to a left-slide drawer on < 744px, overlaying a dark scrim over the canvas
- Category filter row converts to a horizontally scrollable chip strip on mobile with hidden scrollbar
- Search transitions from inline nav field to full-width bar below the nav bar on mobile tap
- Footer column grid (4-up on desktop) collapses to single-column accordion-style stack on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Logo mark shape, dimensions, and exact treatment not extractable from color/font data
- Top-level navigation category count and dropdown depth unknown
- Whether product images use white, transparent, or dark backgrounds could not be confirmed — `{colors.surface-soft}` used as a safe card image background assumption
- Exact gutter widths and column counts at each breakpoint are estimates based on typical Funko-store grid conventions
- Wishlist, quick-view, and variant-selector interaction patterns not observable from extraction
- Animation easing and transition timing values not captured
- Whether the site uses a sticky/fixed nav or scrolls away with the page is unknown
- Dark/light mode toggle presence or absence not confirmed
