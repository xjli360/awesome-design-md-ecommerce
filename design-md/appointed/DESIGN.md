---
version: alpha
name: "Appointed"
source_url: "https://appointed.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Trade Gothic LH Extended running letter-spaced and uppercase above Cormorant Garamond italics — that typographic pairing opens every Appointed page and encodes the brand's animating tension: industrial precision placed entirely in the service of intimate, paper-based daily practice. The canvas is a near-warm off-white (#f8f8f8) anchored by near-black ink (#1a1919), with the real palette living in the surface layer — stone (#c4bdb7), driftwood (#dcd7d4), linen (#c8beb6) — pigments that read less as invented brand colors and more as physical swatches lifted from the actual cloth and board covers of the products themselves. Deep navy (#1c274c) appears selectively as the primary action color, carrying enough visual weight to direct the eye without competing with product photography or the warm neutral field. Rounded corners are nearly absent — buttons, inputs, and product cards all sit at {rounded.none}, and the layout breathes through generous {spacing.section} vertical gaps rather than decorative border treatments. That architectural flatness is not a cost-cutting shorthand; it mirrors the physical objects, which are defined by right angles, parallel spines, and precise corner tabs rather than curves. The hero runs full-bleed editorial photography with an Austin News Headline lockup in the lower third, borrowing the visual authority of mid-century American magazine design and making the implicit argument that a daily planner is a cultural object rather than a supply. The site's most distinctive UI component is the inline cover-color swatch row beneath each product name: 24px circles at {rounded.full} rendered in actual product pigments — dark red (#8b0000), hunter green (#006400), amber (#ee9441), stone (#c4bdb7) among them — that turn the breadth of available colorways into browsing pleasure without requiring additional photography per SKU. Navigation holds Trade Gothic LH Extended tracked wide in a slender 64px bar that collapses to a hamburger drawer on mobile, preserving the same caps-and-tracking typographic register throughout every viewport.

colors:
  primary: "#1c274c"
  primary-active: "#111111"
  primary-disabled: "#9ba8c0"
  ink: "#1a1919"
  body: "#595859"
  muted: "#bebebe"
  hairline: "#d4d4d4"
  hairline-soft: "#eeeeee"
  canvas: "#f8f8f8"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#f8f8f8"
  stone: "#c4bdb7"
  driftwood: "#dcd7d4"
  linen: "#c8beb6"
  cover-maroon: "#8b0000"
  cover-hunter: "#006400"
  cover-amber: "#ee9441"

typography:
  display-xl:
    fontFamily: "'Austin News Headline', 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Austin News Headline', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  body-md:
    fontFamily: "'Bricolage Grotesque', Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bricolage Grotesque', Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.06em
  label-caps:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.14em
    textTransform: uppercase
  button-md:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  price:
    fontFamily: "'Bricolage Grotesque', Inter, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Trade Gothic LH Extended', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
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
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    padding: "{spacing.md}"
  hero:
    minHeight: 80vh
    overlayAlignment: bottom-left
    titleTypography: "{typography.display-xl}"
    eyebrowTypography: "{typography.title-md}"
    scrimColor: "{colors.ink}"
    scrimOpacity: 0.35
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    labelTypography: "{typography.label-caps}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    activeRingColor: "{colors.ink}"
    activeRingGap: 2px
    activeRingWidth: 2px
    inactiveRingColor: "{colors.canvas}"
  product-badge:
    backgroundColor: "{colors.stone}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
    thumbnailSize: 80px
    lineItemTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.stone}"
    columnHeaderTypography: "{typography.label-caps}"
    bodyTypography: "{typography.caption}"
    newsletterInputTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons

**`button-primary`** — A flat rectangle in deep navy ({colors.primary}) with no border radius, set in Trade Gothic LH Extended uppercase at 0.12em letter-spacing. The button reads as a printed label rather than a conventional interactive affordance, which reinforces the brand's editorial register. On hover the background shifts to {colors.primary-active} (near-black); disabled state renders in {colors.primary-disabled} at 0.6 opacity, retaining legibility without signaling interactivity.

**`button-secondary`** — A hairline-bordered transparent rectangle (1px solid {colors.ink}) using identical Trade Gothic LH Extended caps typography as the primary button, creating a typographic equivalence rather than a weight hierarchy. On hover the field fills to {colors.ink} and text inverts to {colors.on-primary}, making the two buttons momentarily visually indistinguishable — an intentional effect that frames both actions as equally serious. Appears most often as "Add to Wishlist" or as a secondary CTA adjacent to a checkout primary.

### Navigation

**`nav-bar`** — A 64px horizontal band in {colors.canvas} with a single {colors.hairline} bottom border and no drop shadow. All links render in {typography.nav-link}: Trade Gothic LH Extended 12px, uppercase, tracked at 0.12em — the same type as every other UI label in the system, making the nav feel continuous with the page rather than architecturally distinct. The logo sits center-aligned on mobile and shifts left on desktop as category links (Notebooks, Planners, Journals, Accessories, Sale) expand inline. Cart icon sits at the far right with a small count indicator; search triggers an overlay rather than persisting as an always-visible field.

### Product Card

**`product-card`** — A square 1:1 product photograph at {rounded.none} occupies the full card width with no image padding. Below the image: product name in {typography.title-md} Trade Gothic LH Extended caps, price in {typography.price}, and a horizontal row of color-swatch circles indicating available cover colorways. No drop shadow, no border, no card surface elevation — the grid gap between cards handles separation. On hover, the primary image swaps to a lifestyle or detail photograph.

### Color Swatch

**`color-swatch`** — 24px circles at {rounded.full} rendered in the actual product cover pigment. Active selection shows a 2px {colors.ink} ring separated from the circle fill by 2px of {colors.canvas} negative space, creating a halo effect that reads clearly on any background. Inactive swatches carry no ring. Cover colorways available across the catalog include stone ({colors.stone}), driftwood ({colors.driftwood}), maroon ({colors.cover-maroon}), hunter ({colors.cover-hunter}), and amber ({colors.cover-amber}). The swatch row is the primary SKU differentiator in the grid without requiring separate photography per colorway.

### Hero

**`hero`** — Full-bleed editorial photography at minimum 80vh with a {colors.ink} scrim at 35% opacity for text legibility. The typographic lockup sits in the lower-left quadrant following magazine convention: a {typography.title-md} eyebrow label (e.g., "American Made Since 2013") sits above a {typography.display-xl} headline in Austin News Headline. The serif face at 52px borrows weight from mid-century broadsheet design, framing the stationery category as deliberate craft rather than commodity. A button-primary anchors below the headline with consistent Trade Gothic LH Extended caps tracking.

### Collection Header

**`collection-header`** — A full-width block in {colors.surface-soft} with {spacing.xxl} vertical padding. A {typography.label-caps} descriptor appears above the collection title in {typography.display-md} Cormorant Garamond, the only place on the page where the serif shifts from headline-weight Austin News Headline to Garamond's old-style roman forms. Filter and sort controls appear below the title as a horizontal row of filter-chip tokens. The warm off-white background distinguishes the header zone from the product grid below without introducing color contrast.

### Product Badge

**`product-badge`** — A flat stone-colored rectangle ({colors.stone}) at {rounded.none} with {typography.label-caps} text in {colors.ink}. Positioned as an absolute overlay in the upper-left corner of product card images. Common values: "Bestseller", "New", "Limited Edition". The muted stone pigment ensures the badge reads as a system label rather than a promotional interruption competing with the product image.

### Cart Drawer

**`cart-drawer`** — A 420px panel sliding from the right edge in {colors.canvas}, separated from page content by a {colors.hairline} left border with no shadow. Each line item shows an 80px square product thumbnail, name in {typography.body-sm} Trade Gothic caps, and a quantity stepper. A subtotal row in {typography.price} sits above a full-width button-primary ("Proceed to Checkout"). If a free-shipping threshold progress bar is shown, it uses {colors.primary} fill on a {colors.hairline-soft} track.

### Footer

**`footer`** — A full-width {colors.ink} field with column headers in {typography.label-caps} and body links in {typography.caption} rendered in {colors.stone}. A newsletter subscription input using {typography.body-sm} with an inline submit runs along the top of the footer block. The bottom legal row (copyright, privacy, terms) renders in {typography.caption} at 60% opacity. The transition from the warm off-white page canvas to the near-black footer creates the primary tonal contrast in the vertical scroll experience.

### Search Bar

**`search-bar`** — Opens as a full-width overlay bar in {colors.surface-soft} at {rounded.none}. Typed characters render in {typography.body-md}; placeholder text uses {colors.muted}. Results appear as a borderless dropdown list, each row separated by a 1px {colors.hairline} line. Each row shows a 40px product thumbnail at left, product name in {typography.title-md}, and price in {typography.price}. No card surfaces — the list is purely typographic.

### Filter Chip

**`filter-chip`** — A {rounded.none} outlined selector in {colors.canvas} with {typography.label-caps} text in {colors.ink}. On active selection the background fills to {colors.ink} and text inverts to {colors.on-primary}. Used in collection pages for filtering by cover color, size, format, and binding style. On mobile, chips sit in a horizontally scrollable single row without wrapping.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav drawer replaces horizontal nav bar; hero drops to 60vh; color swatch row truncates to 5 visible with "+N" overflow indicator; filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; primary category links appear inline in nav bar; hero returns to 70vh; cart drawer narrows to 360px |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; collection-header filter row fully visible without scroll |
| Wide | > 1440px | Content max-width ~1440px centered on screen; four-column product grid maintained; hero image scales to fill without cropping product subject |

### Touch Targets

- All interactive controls minimum 44×44px on touch viewports
- Color swatches expand to 32px diameter on touch breakpoints to meet minimum tap target requirements
- Cart icon and hamburger trigger each hold a 44px hit area regardless of visual icon size
- Filter chips minimum 36px height on mobile with horizontal-scroll container

### Collapsing Strategy

- Navigation collapses to a full-height slide-over drawer at < 744px, preserving Trade Gothic LH Extended caps and 0.12em tracking throughout the drawer link list
- Collection filter row collapses below the collection header fold on mobile; a sticky "Filter & Sort" button at the bottom of the viewport reveals the full chip set as a bottom sheet
- Footer columns stack to a single accordion-style list on mobile; the newsletter field remains visible above the accordion stack
- Cart drawer becomes a full-screen modal (100vw) at viewports below 480px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) not present in color extraction — {colors.surface-card} inferred as white from Shopify convention; verify against live product-card backgrounds before using
- Font weight values for Trade Gothic LH Extended not extractable from static scan; weight 400 assumed throughout (the typeface has limited weight variants by design)
- Austin News Headline is a licensed editorial typeface — confirm whether the site serves it via a CDN license, type foundry embed, or a close substitute; fallback chain may need a substitute such as Georgia or a licensed alternative
- Exact hover/focus transition durations not extractable from color and font scan; 150ms ease-in-out assumed as Shopify default
- Grid column count at desktop (3 vs. 4 columns) not confirmed; four-column layout assumed from typical Shopify stationery store patterns
- #667eea and #764ba2 in extraction appear to be Shopify Pay gradient colors, not brand colors — excluded from palette
- #3ed660 appears to be a Shopify success or in-stock UI indicator, not a brand color — excluded
- #007aff appears to be an iOS system blue (link or Apple Pay button), not brand — excluded
- Whether Bricolage Grotesque or Inter is the primary body face could not be determined from extraction order alone; both are present in the font stack; {typography.body-md} uses Bricolage Grotesque as primary with Inter as first fallback
- Mobile nav treatment (hamburger drawer vs. bottom tab bar) unconfirmed from static extraction
