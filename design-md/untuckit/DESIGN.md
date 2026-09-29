---
version: alpha
name: "Untuckit"
source_url: "https://untuckit.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Alternate Gothic Condensed — all-caps, compressed horizontally, carrying an authority that fills whatever container it occupies — handles the brand's loudest register: promo headers slam across the full viewport, campaign callouts crowd their letters to the edge, and seasonal sale banners arrive like placards rather than whispers. Beneath that display energy, Proxima Nova carries body copy, product names, and navigation labels in a clean geometric sans that reads frank and functional rather than decorative. The palette is built in three layers: a deep navy (#142d51) drives every primary CTA, navigation background, and hover state; a concentrated burgundy (#4d0b35) and vivid crimson (#dc143c) surface in campaign moments and limited colorway badges, lending the brand a clubby confidence that flat navy alone would not carry. Everyday surfaces cool the palette — #eaeaea and #dedede grays hold product grids in an airy register while near-black #121212 handles price text and body prose at full ink density. Corner geometry throughout stays close to square: product cards clip at {rounded.xs} (4px), buttons are nearly rectangular, and the search bar inherits the same tight radius — there are no pill shapes anywhere in the layout. This right-angle discipline reinforces the brand's core claim that fit is a precise, engineered outcome, not a soft approximation. A promotional purple (#a45cec) surfaces on sale badge overlays, deliberately dissonant against the navy-and-crimson base, flagging a discount event as a distinct object rather than a tonal variation. The light accent blue (#accef7) appears in informational callouts and loyalty-program highlight strips. Navigation runs two tiers: a slim utility rail on {colors.surface-soft} for the country selector, size guide, and free-shipping threshold, then a full-width white primary bar with the wordmark centered and category links spread across — Shirts, Pants, Shorts, Sweaters, Outerwear — each opening a full-width mega-dropdown panel. Hero sections run full-bleed photography on desktop with white Alternate Gothic Condensed headlines reversed directly into the scene; on mobile the image compresses and the headline drops below in dark ink on canvas.

colors:
  primary: "#142d51"
  primary-active: "#0e1e38"
  primary-disabled: "#7a9dcc"
  ink: "#121212"
  body: "#4a4a4a"
  muted: "#7c7c7c"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#fefefe"
  surface-soft: "#eaeaea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-crimson: "#dc143c"
  accent-burgundy: "#4d0b35"
  accent-maroon: "#8e2231"
  accent-purple: "#a45cec"
  accent-blue-light: "#accef7"
  navy-mid: "#1e4174"
  navy-light: "#255090"

typography:
  display-xl:
    fontFamily: "'alternate-gothic-condensed-a', Impact, 'Arial Narrow', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'alternate-gothic-condensed-a', Impact, 'Arial Narrow', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'alternate-gothic-condensed-a', Impact, 'Arial Narrow', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "'alternate-gothic-condensed-a', Impact, 'Arial Narrow', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  button-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.02em
  price:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'alternate-gothic-condensed-a', Impact, 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.05em
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    border: "1.5px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    imageAspect: "3 / 4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted}"
    comparePriceDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    scrimColor: "rgba(0,0,0,0.25)"
    minHeight: 80vh
  badge-sale:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-promo:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  size-selector-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    minWidth: 40px
    height: 40px
  size-selector-chip-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  size-selector-chip-unavailable:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
  fit-quiz-cta:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "3px solid {colors.primary}"
    typography: "{typography.title-sm}"
    padding: 16px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 64px 0 32px

## Components

### Buttons

**`button-primary`** — Navy (#142d51) fill with white type in Proxima Nova at 14px, 700 weight, uppercase, 0.08em letter-spacing. The corner radius is {rounded.xs} (4px), keeping the button almost architecturally rectangular — UNTUCKit does not soften its CTAs. Active state darkens the fill to #0e1e38; disabled state fades to a washed #7a9dcc with 0.6 opacity. The 44px height holds across all contexts including mobile.

**`button-secondary`** — Canvas white fill with a 1.5px navy border and navy text using the same {typography.button-md} spec. Used for secondary actions — "View All", "See Details" — and wherever a second action sits beside the primary CTA without competing for attention.

**`button-ghost-on-dark`** — Transparent fill, 1.5px white border, white text. Appears over hero photography where a filled button would obscure the scene. Hover fills with white at 10% opacity. Never appears on light backgrounds.

### Navigation

**`utility-bar`** — A slim {colors.surface-soft} strip (36px tall) pinned above the main nav carrying the country selector, store-locator link, and free-shipping threshold callout in {typography.caption}. On mobile it collapses to a scrolling marquee strip showing only the most time-sensitive message.

**`nav-bar`** — White background, 64px tall, wordmark center-aligned, primary category links spread symmetrically left and right in {typography.nav-link}. Hover triggers a full-width mega-dropdown panel with subcategory link columns and a lifestyle image tile. Cart, search, and account icons anchor the right slot; the search field expands inline on the right rail rather than opening an overlay.

### Product Card

**`product-card`** — White surface with a {rounded.xs} clip and no shadow. The image slot is 3:4 aspect-ratio with object-fit cover. Product name renders in {typography.title-sm}, sale price in {typography.price} at {colors.ink}, and the compare-at price in {typography.price-compare} at {colors.muted} with a line-through decoration. Color swatch dots (14px circles, 4px spacing) live below the price row rather than overlaying the image. Cards sit flush against the {colors.surface-soft} grid field with no visible seam.

### Hero Banner

**`hero-banner`** — Full-bleed photography at 100vw × 80vh on desktop with a 25% black scrim. The headline is set in {typography.display-xl} reversed white, left-aligned at a 72px inset. One {button-primary} CTA and an optional {button-ghost-on-dark} secondary CTA stack 24px below the headline. On mobile the image compresses to 16:9 and the headline drops below in {colors.ink} on {colors.canvas}, with the CTAs stacking vertically below that.

### Badges

**`badge-sale`** — Crimson (#dc143c) fill, white type in {typography.badge}, zero rounding ({rounded.none}). Positioned absolutely at the top-left corner of the product image tile. Multiple badges stack vertically with 2px gaps. The hard-edge rectangle keeps the badge reading as a label rather than a soft overlay.

**`badge-promo`** — Purple (#a45cec) fill with the same {typography.badge} spec. Used for "Gift with Purchase", "Bundle & Save", and promotional overlay moments. The purple is deliberately off-palette — it registers as an event, not an ambient design choice.

**`badge-new`** — {colors.primary} navy fill with {colors.on-primary} type in {typography.badge}. Marks new-arrival products in the grid without the urgency register of crimson.

### Size Selector

**`size-selector-chip`** — Rectangular chips with {rounded.none}: 40×40px for alpha sizes (S, M, L, XL), 52×40px for numeric and inseam sizes. Unselected: {colors.canvas} fill, {colors.hairline} border, {typography.body-sm} in {colors.ink}. Selected (`size-selector-chip-selected`): {colors.primary} fill, {colors.on-primary} text, {colors.primary} border. Unavailable (`size-selector-chip-unavailable`): {colors.muted} text, {colors.hairline-soft} border, a diagonal strikethrough line rendered at 45°.

### Fit Quiz CTA

**`fit-quiz-cta`** — A full-width strip on {colors.surface-soft} with a 3px left border in {colors.primary}. A short headline in {typography.title-sm} reads "Not sure about your size?" and a text link in {colors.primary} opens the size-quiz modal. Positioned between the color selector and the add-to-cart button on the product detail page, surfacing the brand's core conversion aid close to the purchase action.

### Search Bar

**`search-bar`** — {colors.surface-soft} fill, {rounded.xs} radius, 1px {colors.hairline} border, placeholder text in {typography.body-md} at {colors.muted}. A magnifier icon sits right-aligned inside the bar. On mobile the bar expands to full-width on focus, pushing content rather than showing a modal overlay.

### Footer

**`footer`** — Deep navy ({colors.primary}) background with {colors.on-primary} text throughout. A three-column link grid in {typography.body-sm} covers Help, Company, and Follow Us. The newsletter input carries {colors.canvas} background with a {button-primary} submit CTA inside the same row. The bottom bar holds the copyright line, social icons, and payment-method logos in {colors.on-primary} at 60% opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero compresses to 16:9 with headline dropped below image in dark ink; nav collapses to hamburger + centered wordmark; utility bar becomes single-line scrolling marquee; size chips expand to 48px touch height |
| Tablet | 744–1128px | Two-column product grid; hero full-bleed with {typography.display-md} headline; nav shows wordmark + hamburger; mega-dropdown becomes a full-height slide-in drawer from the left |
| Desktop | 1128–1440px | Three-column product grid; full two-tier nav with full-width mega-dropdown; hero at 80vh with {typography.display-xl} headline |
| Wide | > 1440px | Four-column product grid; layout centered in a 1440px container with full-bleed background extending to viewport edges |

### Touch Targets
- All buttons minimum 44px tall; add-to-cart button expands to 52px on mobile
- Size selector chips expand from 40px to 48px minimum touch height on mobile
- Nav hamburger and icon buttons are 44×44px tap areas
- Swatch dots expand from 14px visual to 24px touch target with transparent padding
- Product card is fully tappable; no sub-regions requiring precision tapping

### Collapsing Strategy
- Primary nav collapses to hamburger at < 1128px; mega-dropdown becomes a full-height left drawer
- Utility bar collapses to scrolling marquee at < 744px; country selector moves into the hamburger drawer footer
- Hero secondary CTA hides below 480px; primary CTA always remains visible
- Product grid: 4-col (wide) → 3-col (desktop) → 2-col (tablet) → 1-col (< 480px)
- Footer three-column link grid stacks to a single accordion column at < 744px
- Fit quiz CTA strip retains full width at all breakpoints; left border accent reduces to 2px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile status-bar and address-bar tinting behavior is unknown
- Color #a45cec (purple) appears in extraction but whether it is a persistent badge color or a campaign-season swap cannot be confirmed from static extraction alone
- Whether #4d0b35 (deep burgundy) is used as a UI accent or exclusively as a product colorway (shirt color swatch) is ambiguous from extraction
- Alternate Gothic Condensed and Proxima Nova load via Adobe Fonts / Typekit — exact weight axes available (variable vs. discrete) not confirmed; fallback stack (Impact / Arial Narrow) is a rough proxy for Alternate Gothic Condensed in condensed display contexts
- Exact nav bar and utility bar pixel heights are inferred from viewport proportion; not extracted from computed styles
- Button border-radius confirmed as minimal (0–4px range) but exact computed value not verified against live DOM
- Hover animation timing, focus ring specifications, and transition durations are not observable from static extraction
- Mega-dropdown column layout and image tile placement are inferred from common Shopify apparel patterns; not confirmed against live render
