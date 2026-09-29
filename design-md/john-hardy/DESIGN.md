---
version: alpha
name: "John Hardy"
source_url: "https://www.johnhardy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The forge-orange of #ff5c1d — John Hardy's single digital voltage — earns its intensity from what happens upstream of any product page: each piece exits a Bali workshop by hand, a fact the brand repeats in editorial copy, navigation callouts, and footer copy without apology. Against a near-white (#fcfcfc) canvas and deep-charcoal ink (#33383c), the orange reads less like a standard e-commerce CTA and more like an ember held from the metalworking floor — warm, deliberate, and structurally anchoring. Type runs in General Sans, a geometric sans-serif that gives the brand's heritage story a clean container without imposing editorial personality of its own; display sizes sit at weight 600 rather than punishing 700+, trusting product photography — silver chain coiled against dark stone, gold against warm skin — to carry visual weight that heavy type would crowd out. Surface hierarchy descends in shallow steps: #fcfcfc canvas to #f9f9f9 section backgrounds to #ffffff product cards, leaving no surface competing with imagery. Hairlines at #dedede and #e6e6e6 divide content zones without adding weight; the charcoal (#33383c) used for structural elements and ink echoes oxidized silver, connecting a craft finish to a system token. Buttons adopt {rounded.sm} (4px) rather than pills — the {rounded.full} radius is reserved exclusively for search inputs and filter pills, keeping a strict rectangular geometry elsewhere. Error states reach for #cb3b3b, a red closer in temperature to garnet than to tomato; success uses a botanical #63d977. Both appear as functional utilities the brand chose not to over-style. The material-tag component carries metal and gemstone callouts — Sterling Silver, 18K Gold Vermeil, Black Sapphire — in uppercase General Sans at 11px, a typographic nod to hallmark stamps more than to product labeling convention.

colors:
  primary: "#ff5c1d"
  primary-active: "#e04a10"
  primary-disabled: "#ffc4a8"
  error: "#cb3b3b"
  error-light: "#f7c7c7"
  success: "#63d977"
  success-light: "#c2f0c9"
  ink: "#33383c"
  body: "#646464"
  muted: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#fcfcfc"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-muted: "#ededed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  near-black: "#121212"

typography:
  display-xl:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  material-label:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  nav-link:
    fontFamily: "'General Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.01em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  announcement-bar:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.05em
    textTransform: uppercase
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "1/1"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  hero-banner:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlayOpacity: 0.4
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
  collection-badge:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.ink}"
    typography: "{typography.material-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  material-tag:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.material-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    border: "1px solid {colors.hairline}"
  material-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.material-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: 0 16px
  craft-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    accentBorderColor: "{colors.primary}"
    accentBorderWidth: 3px
    accentBorderPosition: top
    padding: "{spacing.section}"
  filter-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-muted}"
    bodyTypography: "{typography.body-sm}"
    headlineTypography: "{typography.title-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — A 48px tall, 4px-rounded rectangle in #ff5c1d with uppercase General Sans at 14px/weight 600 and 0.06em letter-spacing. The all-caps setting reads as a stamp rather than a label, consistent with the brand's hallmark vocabulary. Active state deepens to #e04a10; disabled state fades to the pale #ffc4a8 tint without altering shape. Never pill-shaped — the flat corner on primary CTAs is a deliberate luxury signal that distinguishes John Hardy from consumer-friendly pill-button brands.

**`button-secondary`** — Identical 48px height and 4px radius, transparent fill, 1.5px solid #33383c border and charcoal text. Pairing secondary beside primary on a product page produces an orange/outlined contrast that separates hierarchy without background color variance on the canvas.

**`button-ghost`** — Textual CTA in #ff5c1d, no border, no fill, zero radius. Used for inline editorial links in craft story sections and collection editorials where a framed button would add visual noise. Uppercase tracking preserved from the full button weight.

### Text Input
**`text-input`** — 48px tall, 4px rounded, 1px #dedede border sharpening to #33383c on focus. Placeholder in #888888. Height matches button height so inline search-and-submit layouts align without reflow.

### Navigation
**`nav-bar`** — 64px white bar with a 1px #e6e6e6 bottom border. Nav links in 14px General Sans weight 500 with tight 0.01em tracking. The `announcement-bar` sitting above it (36px, #121212 background, white caption text in uppercase) carries rotating shipping and craft-heritage messaging. On scroll the announcement bar collapses; the nav bar becomes sticky.

### Product Card
**`product-card`** — Sharp 0px radius, 1px soft hairline border, square 1:1 image. Title uses `{typography.title-sm}` (16px/500), price in `{typography.price-display}` (18px/500). Hover elevates via box-shadow rather than background color shift, keeping the surface system clean. The `material-tag` stacks beneath the product name in uppercase 11px General Sans to identify metal or gemstone type before the user opens the PDP.

### Hero Banner
**`hero-banner`** — Full-bleed dark-tinted image (#121212 at 0.4 scrim) with a display-xl headline and an orange primary CTA. The near-black overlay and #ff5c1d button produce the brand's signature high-contrast editorial entry point used across collection launches and seasonal campaigns. Body copy in 16px/400/1.6 line-height sits between headline and CTA.

### Collection Badge & Material Tag
**`collection-badge`** — Small rectangle on #ededed in uppercase 11px General Sans with 2px radius, used to mark collection family (Classic Chain, Dot Dash, Bamboo) on product cards and within navigation mega-menus. Carries no interactive state — it is a label, not a filter.

**`material-tag`** / **`material-tag-active`** — Full-radius pill with transparent fill and hairline border in inactive state; inverts to #33383c fill and white text when active. Used on PDPs for metal finish selectors and on PLP filter rows for material refinement. The full-radius pill distinguishes these from the rectangular editorial buttons, preventing affordance confusion.

### Craft Callout
**`craft-callout`** — A full-width editorial band in #f9f9f9 with a 3px #ff5c1d top accent line — the only place in a non-CTA context where the primary orange appears structurally. Headline in display-sm (24px/600), body in body-md (16px/400/1.6). This component carries the Bali workshop origin story, recycled-metals commitment, and "handcrafted since 1975" messaging on the homepage, category pages, and sustainability editorial.

### Search Bar
**`search-bar`** — 40px full-radius pill in #f9f9f9 with a 1px #dedede border. The pill shape creates a distinct, immediately recognizable search silhouette against the otherwise rectangular component vocabulary. On desktop it sits inset in the nav bar; on mobile it expands to full-width below the nav row.

### Filter Pills
**`filter-pill`** / **`filter-pill-active`** — Paired pill components for PLP refinement. Inactive is white with a hairline border; active inverts to #33383c fill with white text. The full-radius distinguishes these filter affordances from the rectangular editorial CTAs elsewhere in the page, preventing mode confusion.

### Footer
**`footer`** — #121212 background with white body text and #ededed muted link color. Section headlines in title-sm (16px/500). Three-column layout on desktop collapses to accordion on mobile. The dark footer anchors the near-white page stack and mirrors the announcement-bar register at the top of the viewport, bracketing content in the brand's charcoal-to-near-black range.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger drawer replaces inline nav; product grid collapses to 2 columns; hero headline drops to display-md (32px); announcement-bar shows single rotating message; filter pills enter horizontal scroll tray |
| Tablet | 744–1128px | 3-column product grid; nav shows primary links only with overflow dropdown; craft-callout switches to two-column image+text split; footer two columns |
| Desktop | 1128–1440px | Full nav with mega-menu dropdowns; 4-column product grid; hero max-width 1440px; craft-callout content max-width 1200px centered; announcement-bar shows full message set |
| Wide | > 1440px | Content locked at 1440px max-width; side gutters grow symmetrically; hero image scales to fill; no layout structure changes |

### Touch Targets
- All interactive elements (buttons, nav links, filter pills) minimum 44px tall on mobile
- Product card full tap-zone spans image, title, and price — no separate "add to cart" target required on card
- Hamburger icon: 44×44px touch area regardless of visual glyph size
- Announcement-bar close button: 44×44px centered on the 36px bar height
- Material-tag pills: minimum 36px height on mobile, padded to meet 44px vertical tap zone with margin

### Collapsing Strategy
- Nav collapses to left-sliding hamburger drawer at < 744px; overlay scrim darkens content at 40% opacity
- Footer accordion on mobile: each section label is a full-width tap target, content sections collapsed by default
- Material tag rows on PDP: wrap to second line on mobile rather than truncating or scrolling
- Craft-callout image moves above text block on mobile; text loses side padding to allow near full-bleed
- PLP filters: hidden behind a "Filter" pill on mobile that opens a slide-up bottom sheet with full filter tree

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- General Sans identified in extraction but no weight specimen or size scale confirmed — typography values are design-system defaults calibrated for geometric sans-serif at luxury retail scale
- Muted text shade (#888888) is interpolated; extraction returned no mid-gray between #646464 (body) and #dedede (hairline)
- primary-active (#e04a10) and primary-disabled (#ffc4a8) are derived — no explicit hover, focus, or disabled color tokens were extracted
- Blues (#7896e2, #416bd6, #c6d3f3) and greens (#81e287, #63d977, #c2f0c9) appear to be Shopify framework defaults for system notification states; only the success green (#63d977) and error red (#cb3b3b) were carried into brand tokens
- No motion or transition tokens extracted (drawer slide duration, hover fade timing, scroll behavior)
- Mega-menu column structure and image-panel layout not confirmed; described from standard luxury-retail navigation conventions
- No confirmed logo lockup dimensions or clearspace rules extracted
