---
version: alpha
name: "Tappan Collective"
source_url: "https://www.tappancollective.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every purchase action on Tappan Collective registers in #ff3300 — a warm tomato-red that lands against the near-white canvas like a gallery director's marker circling the work that's ready to ship. Against the warm linen surfaces (#e1ddc9, #fff2d8) that appear in editorial banners and featured-collection modules, that orange-red reads as curatorial authority rather than commercial urgency. goldenbook serifed headlines carry the editorial voice at display sizes, establishing an art-catalogue register that a sans-serif grid alone could not achieve, while neuzeit-grotesk and Instrument Sans handle all functional UI — pricing, artist names set in small-cap uppercase, filter labels — in deliberately quiet roman spacing that keeps the eye on the art rather than the chrome. The product grid runs dense but airy: each card surfaces only the artwork image, artist name in {typography.label-upper} small-caps, title, and price, with no borders or elevation shadows — flat surfaces all the way. Original works wear a flat dark badge at {rounded.xs}; limited editions carry print-count notation in the same uppercase label register. What makes the color system unusual for a gallery is the breadth of its taxonomy palette: emerald #00a47c, periwinkle #8da1e9, amber #ffb510, deep teal #19bcad, gold-brown #836300, purple #8500d3, and eight or nine further vivid tones appear on category and medium filter chips, giving each genre and material its own color stamp for scannable browsing. Filter chips use {rounded.full} pill geometry — the one place the design loosens its flat rectilinear posture — while all other components maintain {rounded.sm} or flat corners, holding a discipline closer to a printed catalogue than a consumer app.

colors:
  primary: "#ff3300"
  primary-active: "#cc2900"
  primary-disabled: "#fb8077"
  ink: "#111111"
  body: "#3d4246"
  muted: "#595959"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#f6f6f8"
  surface-warm: "#e1ddc9"
  warm-tint: "#fff2d8"
  on-primary: "#ffffff"
  dark-slate: "#222222"
  silver: "#c7c7c7"
  tag-emerald: "#00a47c"
  tag-teal: "#19bcad"
  tag-deep-teal: "#088f87"
  tag-blue: "#24a7ff"
  tag-periwinkle: "#8da1e9"
  tag-amber: "#ffb510"
  tag-gold: "#836300"
  tag-orange: "#f29100"
  tag-green: "#00bf48"
  tag-pink: "#ffc0cc"
  tag-purple: "#8500d3"
  tag-chartreuse: "#fcff80"

typography:
  display-xl:
    fontFamily: "'goldenbook', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.06
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'goldenbook', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'goldenbook', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'neuzeit-grotesk', 'Instrument Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  title-sm:
    fontFamily: "'neuzeit-grotesk', 'Instrument Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', 'neuzeit-grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', 'neuzeit-grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'neuzeit-grotesk', 'Instrument Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.15px
  label-upper:
    fontFamily: "'neuzeit-grotesk', 'Instrument Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "'neuzeit-grotesk', 'Instrument Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Instrument Sans', 'neuzeit-grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Instrument Sans', 'neuzeit-grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    artistTypography: "{typography.label-upper}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    artistColor: "{colors.muted}"
    gap: "{spacing.sm}"
  artist-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    nameTypography: "{typography.title-sm}"
    bioTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    padding: "{spacing.base}"
  badge-original:
    backgroundColor: "{colors.dark-slate}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-edition:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-filter-chip:
    backgroundColor-default: "{colors.canvas}"
    backgroundColor-active: "{colors.ink}"
    textColor-default: "{colors.muted}"
    textColor-active: "{colors.canvas}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
  medium-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.silver}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: none
    height: 42px
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    descriptionColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.lg}"
  artwork-detail-header:
    titleTypography: "{typography.display-sm}"
    artistTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    artistColor: "{colors.body}"
    metaColor: "{colors.muted}"
    gap: "{spacing.sm}"
  promo-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.xl} {spacing.section}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  sale-price:
    textColor: "{colors.primary}"
    typography: "{typography.price}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-upper}"
    height: 36px
  footer:
    backgroundColor: "{colors.dark-slate}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    linkColor: "{colors.silver}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The sole commerce-action button, rendered in #ff3300 with white uppercase label in {typography.button-md} and {rounded.sm} corners. Appears as "Add to Cart", "Buy Now", "Reserve", and "Notify When Available" — every state where Tappan is asking for a transaction. Hover transitions to {colors.primary-active} (#cc2900), a deeper red that reinforces decisiveness rather than softening the action. The disabled state uses {colors.primary-disabled} (#fb8077), a coral wash that signals unavailability without disappearing entirely. Letter-spacing at 0.06em gives the uppercase label breathing room at 13px.

**`button-secondary`** — Canvas background with a 1px {colors.ink} border and the same uppercase {typography.button-md} label. Matches primary in height (44px) so the two can sit side-by-side without visual imbalance. Used for secondary collector actions like "View Artist Profile", "See More Works", and "Add to Wishlist". Border darkens on hover or background lifts to {colors.surface-soft} to indicate interactivity.

**`button-ghost`** — Text-only, {colors.body} color, underlined, in {typography.body-sm}. No background, no border. Reserved for low-hierarchy navigation flows: "Back to Collection", "Clear All Filters", "Show Less". Keeps structural links visually subordinate to artwork content.

### Navigation

**`nav-bar`** — 60px tall white bar with a feather-light {colors.hairline-soft} bottom border. Logo anchors left; primary navigation links — Shop, Artists, Editorial, About — sit center or left-adjacent in {typography.nav-link}; cart and account icons anchor right. The bar uses no fill color heavier than white and no typographic weight heavier than 500, ensuring the commerce frame reads as minimal against the gallery content beneath it.

**`announcement-bar`** — A 36px strip above the nav in {colors.dark-slate} with {colors.canvas} text in {typography.label-upper}. Used for shipping promotions, new collection announcements, or limited-time offers. The near-black bar grounds the top of the page before the white nav opens the layout.

**`search-bar`** — Embedded in the nav or as a full-width bar on collection pages. Recessed into a {colors.surface-soft} trough with no visible border, placeholder in {colors.silver}. Compact 42px height. On collection pages it may expand to a full-width filter bar combining keyword search with medium and price dropdowns.

### Product & Artist Cards

**`product-card`** — The primary browsing unit across all collection grids. Artwork image fills the card top at 4:5 aspect ratio; below it: artist name in {typography.label-upper} small-caps at {colors.muted}, then artwork title in {typography.body-sm} at {colors.ink}, then price in {typography.price}. No card border, no box shadow, no hover elevation — the artwork generates all visual interest. On hover, the image may dim slightly or an "Add to Cart" button slides in as an overlay. Cards are 3–4 columns on desktop, tightly gapped at {spacing.base}.

**`artist-card`** — Used in "Browse by Artist" modules and featured-artist editorial sections. {colors.surface-soft} flat background, artist portrait image above, name in {typography.title-sm}, and a short specialty or location line in {typography.caption}. The card signals a person, not a product, so padding is generous and the name is set heavier than the artwork card's artist label.

**`badge-original`** — A small pill on {colors.dark-slate} fill with {colors.canvas} uppercase text at {rounded.xs}. Pinned to the image corner or placed below the title to signal one-of-a-kind authenticity. Kept tight — 3px top/bottom, 8px left/right — so it reads as a tag rather than a banner. Communicates scarcity without overwhelming the art.

**`badge-edition`** — Outlined and subdued: {colors.surface-card} fill, 1px {colors.hairline} border, {colors.muted} text. Used for print editions where the edition number (e.g. "Ed. 25") carries the information. Quieter than the original badge because editions are more plentiful and the count itself is the value signal.

### Taxonomy & Filtering

**`category-filter-chip`** — The only {rounded.full} pill element in the component set, signaling "toggleable tag" through its curvature alone against the otherwise rectilinear layout. Default state: {colors.canvas} background, {colors.hairline} border, {colors.muted} label in {typography.label-upper}. Active: {colors.ink} fill, {colors.canvas} text. Each visual art medium, price range, or genre corresponds to one chip. When rendered as colored dot-accented variants rather than filled chips, the taxonomy palette — tag-emerald, tag-teal, tag-blue, tag-periwinkle, tag-amber, tag-gold, tag-orange, tag-green, tag-pink, tag-purple — assigns a distinct hue to each medium category.

**`medium-tag`** — A non-interactive warm-surface pill ({colors.surface-warm}) used on artwork detail pages and artist profiles to surface medium and style metadata. Softer than the filter chip — it annotates rather than controls. Pairs visually with the linen promo-banner surface for editorial warmth.

### Editorial & Merchandising

**`hero`** — Full-bleed artwork image with an optional white-panel or overlay text block. Title in {typography.display-xl} goldenbook serif at 52px, weight 400 — the italic or regular cut of this typeface at that size creates an editorial-poster quality that separates the hero from any product grid. Subtitle or collection description in {typography.body-md} at {colors.muted}. The goldenbook/sans-serif split is sharpest here: art-world gravitas at the top, store mechanics below.

**`collection-header`** — A section header between the nav and the product grid, carrying the collection name in {typography.display-md} goldenbook and an optional curatorial description in {typography.body-md}. Separated from the grid by a {colors.hairline} bottom border rather than padding alone, giving the editorial context a clean handoff to the commercial grid.

**`artwork-detail-header`** — On individual artwork pages: artist name in {typography.title-md} at {colors.body}, artwork title in {typography.display-sm} goldenbook at {colors.ink}, then a row of metadata (medium, year, dimensions, edition info) in {typography.caption} at {colors.muted}. The hierarchy drops quickly from serif display to small-cap caption — the art's provenance reads like a wall label, not a product spec sheet.

**`promo-banner`** — A full-width editorial strip on {colors.surface-warm} linen (#e1ddc9). Carries messaging like "New Works Just Added" or "Free Shipping on Orders Over $X" in {typography.body-md}. The warm cream tone positions the announcement as editorial context rather than sale urgency. Generous horizontal padding ({spacing.section}) keeps it from reading as an alert bar.

**`price-display`** — Standard {typography.price} in {colors.ink} for all undiscounted works. When a piece is on promotion, the original price renders in {colors.muted} with strikethrough and the active price renders in {colors.primary} (#ff3300) — the only context outside CTAs where the brand red appears. This keeps the primary color semantically coherent: red means "act on this".

### Footer

**`footer`** — {colors.dark-slate} (#222222) background grounds the bottom of every page. Text in {colors.canvas}, links in {colors.silver}, column headings in {typography.label-upper} tracking. Body copy in {typography.body-sm}. Columns cover: Shop (mediums and price ranges), Artists, Collector Resources (shipping, returns, authentication), Company (about, press, careers), and newsletter signup. The newsletter input pairs a {text-input}-styled field with a {button-primary} "Subscribe" button in-line.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single- or 2-column product grid; nav collapses to hamburger + cart icon; announcement bar truncates to one line; filter chips scroll horizontally below nav bar; hero shifts to stacked image-over-text with reduced display-xl font size (~32px); promo-banner padding reduces to {spacing.base} |
| Tablet | 744–1128px | 2–3 column product grid; primary nav links visible, secondary links in drawer; filter chips in horizontal scroll row; artwork detail layout shifts from 2-column to stacked; artist cards 2-up |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav; filter chips in sticky horizontal bar above grid or left sidebar; artwork detail in 2-column split (image left, metadata + purchase right); hero at full bleed |
| Wide | > 1440px | Layout centers at max-width ~1440px with symmetric gutters; product grid stays at 4 columns; hero image fills viewport width, text block constrained to ~580px; footer columns expand spacing |

### Touch Targets

- All filter chips, nav links, cart/account icons minimum 44×44px tap area
- Product card entire surface is tappable, not just image or title
- button-primary and button-secondary fixed at 44px height across all breakpoints
- badge-original and badge-edition are display-only; no touch target required
- Search bar input expands to full keyboard-avoidance height on mobile focus

### Collapsing Strategy

- Navigation collapses to hamburger icon below 744px; cart icon and logo remain always visible
- Filter chips collapse to a horizontally scrollable single row on mobile with an active-count badge if overflow exists
- Artist cards in Browse Artists modules: 4-column → 2-column at tablet → 1-column at narrow mobile
- Promo-banner collapses to reduced padding and single-line copy at mobile; second line of text wraps or truncates
- Artwork detail page: 2-column image/purchase split collapses to stacked (image above, purchase block below) at tablet
- Footer: 4-column horizontal → 2×2 grid at tablet → stacked accordion at mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav height and logo lockup dimensions not confirmed from extraction; 60px height is estimated from Shopify gallery patterns
- goldenbook is a licensed typeface; the exact font-family declaration string and fallback behavior on non-licensed contexts was not confirmed — Georgia fallback will alter editorial character significantly
- Exact border-radius values in production not pixel-confirmed; {rounded.sm} (4px) estimated from screenshot visual patterns
- Hover and focus ring styles for filter chips, product cards, and nav links not extracted
- The full taxonomy color-to-category mapping (which tag color corresponds to which medium or genre) is inferred from the palette breadth — exact assignments not confirmed
- Dark mode or high-contrast mode not observed; may not exist
- Animation durations for cart drawer, filter panel transitions, and image hover effects not extracted
- Exact goldenbook font weights available (italic vs. roman, weight range) not confirmed — design assumes regular weight 400 only
- Mobile breakpoint for product grid (1-up vs. 2-up) not confirmed; both patterns are common on Shopify art storefronts
