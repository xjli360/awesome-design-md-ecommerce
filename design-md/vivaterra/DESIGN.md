---
version: alpha
name: "VivaTerra"
source_url: "https://www.vivaterra.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pressed-clay coral (#ff6f61) holds every primary CTA and hover state — an unusual choice for a garden brand that could have defaulted to green, and the tension is intentional: VivaTerra positions itself closer to design-forward homewares than to gardening supply, using terracotta as sensory shorthand for kiln-fired pots and sun-warmed earth rather than foliage. Jost, a geometric sans-serif with even stroke weights, runs the entire type system; it gives category labels and product names the same unhurried authority without the warmth of a humanist face or the coldness of a grotesque. Display sizes sit at 56px at weight 600, trusting wide lifestyle photography to carry visual energy rather than typographic mass. Olive tones (#899541, #95a054) surface as accent badges and collection markers — a yellowed, late-season lichen green quite different from the saturated emerald (#28bb74) used for in-stock indicators and environmental messaging. The rounding language stays deliberately moderate: {rounded.sm} on buttons and inputs, {rounded.md} on product cards, never the {rounded.full} pill-shape of beauty or fashion brands — handcrafted-adjacent without overdoing the craft signal. A warm blush (#ffe2df) underlies promotional banners and newsletter callouts, providing a softer field than white when overlay copy would otherwise feel clinical. The dark end of the palette extends from near-black #1f1f1f through a long neutral staircase (#2b2b2b, #3e3e3e, #525252, #767676) that allows the interface to stratify collection metadata, pagination, and secondary labels without borrowing blue or green for hierarchy. Deep navy #001f39 anchors the footer and occasional full-bleed dark sections, creating a nighttime-garden depth that contrasts with the warm coral of daytime CTAs. Amber (#ff9736) appears selectively for bestseller badges and urgency signals, completing a warm-earth triad with coral and olive that keeps even promotional moments feeling grounded in the natural world the brand references.

colors:
  primary: "#ff6f61"
  primary-active: "#cc594e"
  primary-disabled: "#ffa9a0"
  primary-pale: "#ffe2df"
  ink: "#1f1f1f"
  body: "#2b2b2b"
  muted: "#767676"
  muted-soft: "#a6a6a6"
  hairline: "#e5e5e5"
  hairline-soft: "#dcdcdc"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-blush: "#ffe2df"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#001f39"
  olive: "#899541"
  olive-light: "#95a054"
  emerald: "#28bb74"
  amber: "#ff9736"
  error: "#d74047"

typography:
  display-xl:
    fontFamily: "'Jost', sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Jost', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  label-uppercase:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Jost', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    padding: 12px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: 11px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderColor: "{colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    height: 44px
    iconColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.surface-soft}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.xl}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.olive}"
    hoverOverlay: "rgba(0,0,0,0.08)"
  badge-new:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-bestseller:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-banner:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 40px
    linkColor: "{colors.primary-active}"
    linkTypography: "{typography.button-sm}"
  newsletter-block:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted-soft}"
    padding: "{spacing.section} {spacing.xl}"
    inputBackgroundColor: "{colors.canvas}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "1px solid rgba(255,255,255,0.1)"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Coral terracotta (#ff6f61) fill with white text in Jost 600 at 15px with 0.5px tracking, 48px tall, {rounded.sm} corners. The shape reads confident without being pill-friendly — VivaTerra's CTAs never abandon their grounded geometry. On hover the background deepens to {colors.primary-active} (#cc594e); disabled bleaches to pale coral #ffa9a0, maintaining warmth without active affordance.

**`button-secondary`** — White canvas background with a 1.5px ink border and ink text, matching primary height and typography. Used throughout product listing pages where an Add-to-Cart primary needs a sibling Compare or Wishlist action. Hover shifts background to {colors.surface-soft}, signaling interactivity without adding color competition.

**`button-ghost`** — A compact 36px outline button in coral border and coral text ({colors.primary}), used for inline category CTAs and product page secondary actions like "View Full Collection." Keeps coral brand language present at smaller scale without demanding the same visual weight as the filled primary.

### Inputs

**`text-input`** — 48px height, 1px {colors.hairline} border, {rounded.sm}. Focus swaps border to full {colors.ink} without a colored ring, maintaining the palette's neutral restraint. Placeholder text renders in {colors.muted} (#767676). Used for search, address fields, account forms, and review submission throughout the site.

**`search-bar`** — Shares input geometry but uses {colors.surface-soft} fill rather than white canvas, sitting in the nav header at 44px height. The soft-gray fill distinguishes it from page-level form fields. On focus, a 1px {colors.hairline} border appears; background stays soft-gray. Search icon renders in {colors.muted}.

### Navigation

**`nav-bar`** — 64px tall, white canvas, 1px {colors.hairline} bottom border. Logo in {colors.ink}. Nav links use {typography.nav-link} (Jost 500, 14px, 0.2px tracking). On lifestyle-image pages with scroll-past-hero triggers, `nav-bar-dark` applies: {colors.navy} background (#001f39) with {colors.on-dark} link text and logo, creating continuity with the footer's dark register.

### Product Card

**`product-card`** — {rounded.md} card on white {colors.surface-card}. Image occupies the top 4:3 ratio area; title in {typography.title-sm} (Jost 600, 16px), price in {typography.price-display} (Jost 500, 18px). Sale prices render in {colors.primary} coral; regular prices in {colors.ink}. Overlay badges (badge-new, badge-sale, badge-bestseller) position at image top-left. Subtle box-shadow on hover lifts the card without heavy animation.

### Hero

**`hero-banner`** — Full-width lifestyle image overlay, minimum 560px tall. Title in {typography.display-xl} (Jost 600, 56px) in {colors.on-dark}, body in {typography.body-md} in {colors.surface-soft}. The dark variant uses {colors.navy} as a solid background when no photography is available. `hero-banner-light` switches to {colors.surface-soft} with {colors.ink} text for seasonal editorial sections — spring lookbooks, gifting roundups — where warmth over drama is preferred.

### Collection Tile

**`collection-tile`** — {rounded.md} card on {colors.surface-soft} background, used in category browsing grids (typically 3-across desktop, 2-across tablet). A {typography.label-uppercase} label in {colors.olive} (#899541) sits above the image to mark the category register in a muted, editorial voice. Title in {typography.title-md}. On hover, rgba(0,0,0,0.08) dims the image gently — enough to register, not enough to feel modal.

### Badges

**`badge-new`** — Olive (#899541) background, white uppercase Jost 600 at 11px/1.2px tracking, {rounded.xs}. Reads as editorial and garden-native rather than commercial. **`badge-sale`** — {colors.primary} coral fill, same type spec for immediate promotional signal. **`badge-bestseller`** — {colors.amber} (#ff9736) fill, same type — the three badge tiers form a warm-earth hierarchy readable through color alone without additional iconography.

### Promotional Banner

**`promo-banner`** — 40px announcement bar in {colors.surface-blush} (#ffe2df), ink body text in {typography.body-sm}, inline link in {colors.primary-active} at {typography.button-sm} weight. The blush ground is warmer than a white bar and reinforces the earthy palette without introducing a hard promotional color. Sits above the nav-bar on campaign days.

### Newsletter Block

**`newsletter-block`** — Full-width {colors.navy} section with {colors.on-dark} title in {typography.title-lg} and {colors.muted-soft} body in {typography.body-sm}. White canvas email input beside a button-primary CTA; stacked vertically on mobile. Section padding is {spacing.section} top and bottom, giving the block the visual weight of a content section rather than a footer addendum.

### Breadcrumb

**`breadcrumb`** — {colors.muted} (#767676) in {typography.caption} (Jost 400, 12px) with {colors.hairline} separators. Current-page segment renders in {colors.ink}. Appears on all PDP and collection pages, positioned between the nav and the product hero or listing grid.

### Footer

**`footer`** — {colors.navy} (#001f39) background, column headings in {typography.title-sm} at {colors.on-dark}, link lists in {typography.body-sm} at {colors.muted-soft} (#a6a6a6). Links lighten to {colors.on-dark} on hover. A 1px rgba(255,255,255,0.1) border separates the main columns from the legal row. {spacing.section} vertical padding treats the footer as a destination rather than a footnote.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero title drops to {typography.display-sm} (28px); promo-banner truncates to a single centered line; newsletter-block stacks input above button; footer columns collapse to tap-to-expand accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links, secondary utilities collapse; hero at {typography.display-md} (40px); collection tiles 3-across |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all utility icons; hero at {typography.display-xl} (56px); newsletter-block renders two-column with editorial text left, form right |
| Wide | > 1440px | Layout constrained to 1440px max-width centered; four-column product grid; hero padding increases proportionally; no additional breakpoint typography changes |

### Touch Targets

- All primary and secondary buttons minimum 48px height on mobile
- Nav icons (cart, hamburger, wishlist) padded to 44×44px minimum tap zone
- Product card entire surface is tappable to PDP on touch devices
- Badge and breadcrumb links padded to 32px minimum height on touch viewports
- Footer accordion headers minimum 48px touch height

### Collapsing Strategy

- Primary nav category links collapse first at 744px, replaced by a hamburger sheet drawer with full link tree
- Footer four-column link grid collapses to single-column accordions below 744px
- Hero body copy line-clamped to 3 lines on mobile, full on tablet and above
- Product card material subtitle and secondary metadata hidden on mobile to reduce scanning load
- Promo-banner text collapses to centered single sentence; marquee scroll if campaign copy exceeds one line

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No logo geometry or wordmark details were extractable — capitalization style, icon lockup, or alternate marks are inferred from Jost as the sole extracted font
- Canvas white (#ffffff) not observed in extraction; assumed as browser default page background not captured by scanner
- Exact nav height and scroll-behavior (sticky, hide-on-scroll, transparent overlay) not confirmed from extraction
- Motion and animation timing curves not present in extraction; transitions assumed at 150–200ms ease-out as a reasonable default
- Whether #3b86ff, #475a96, #49b2e8, #0d76b4, and #1199ff are genuine brand colors or Shopify widget / third-party app colors is ambiguous — excluded from brand token set pending visual confirmation
- #d63384 excluded; strongly resembles Bootstrap 5 default pink, not a VivaTerra brand color
- Product image aspect ratio (square, 4:3, or portrait) not confirmed; 4:3 assumed from typical garden-decor merchandising conventions
- Exact Jost weight ladder and letter-spacing values not confirmed via live specimen measurement; values inferred from geometric sans-serif conventions appropriate for the stack
