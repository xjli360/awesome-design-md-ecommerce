---
version: alpha
name: "Realisation Par"
source_url: "https://realisationpar.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Réalisation Par loads its product grid as a series of full-bleed editorial photographs before a price renders — an architecture that declares desire precedes information. The interface is a controlled void: near-black (#111111) fills every primary action, Arial at weight 300–400 handles every label, and hairline borders at #e5e5e5 trace container geometry so faintly that the garment photography feels unframed. The effect is closer to a lookbook than a storefront, and every UI decision reinforces it.

  The extracted palette resolves around a tension between near-neutral architecture and pockets of deliberate warmth. Six gray values — from #111111 through #555555 and #757575 to #e5e5e5 and #f5f5f5 — carry every text and border decision without variation in hue. Secondary swatches open temperature pockets: parchment cream at #fffdea for editorial callout zones, blush at #ffdddd for feminine overlay states, an amber-gold at #f1a500 marking sale and promotional contexts, and a deep indigo at #221155 anchoring the footer and announcement-bar surfaces. Interactive states migrate across a family of blues — periwinkle #476bef for hover links, electric #002fe1 for focus rings, muted slate #4496f6 for secondary interactive — a UI infrastructure layer invisible during browsing but surfacing correctly at checkout. Multiple extracted blues suggest some originate from embedded third-party widgets rather than core brand UI.

  Typography runs on system faces: Arial and Helvetica at sizes that consistently defer to imagery. Display headings sit at 30–32px weight 300, deliberately thin so the typeface neither competes with nor frames the photography. Navigation labels open letter-spacing to a magazine-spread cadence. Product names run at weight 400; prices at a smaller caption size — so the garment image always holds the primary read hierarchy.

  The orthogonal geometry is the brand's clearest structural signal. Buttons are hard-cornered rectangles ({rounded.none}), product cards have zero rounding, modals have square edges. The interface is a taut rectilinear container for the organic, curved photographic content within it. Softness appears only in filter chips and color swatches ({rounded.full}), a deliberate secondary tier that never dilutes the dominant flat geometry. Section spacing breathes at 64px while component padding stays compact — keeping grid density high enough to feel like an edited magazine spread rather than a catalog.

colors:
  primary: "#111111"
  primary-active: "#2d2d2d"
  primary-disabled: "#757575"
  ink: "#111111"
  body: "#444444"
  muted: "#757575"
  muted-soft: "#555555"
  hairline: "#e5e5e5"
  hairline-soft: "#dfdfdf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-cream: "#fffdea"
  surface-blush: "#ffdddd"
  surface-mint: "#d5ffd8"
  on-primary: "#ffffff"
  accent-indigo: "#221155"
  accent-blue: "#476bef"
  link: "#002fe1"
  link-muted: "#4496f6"
  link-teal: "#007dc6"
  sale-amber: "#f1a500"
  error: "#d14343"
  error-alt: "#cc4749"
  success: "#008a06"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.1em
  badge-text:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  price-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  announcement-text:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em

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
    padding: 16px 32px
    height: 48px
    border: none
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
    padding: 15px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.accent-indigo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement-text}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-label}"
    priceColor: "{colors.body}"
    salePriceColor: "{colors.error}"
    badgeBackgroundColor: "{colors.sale-amber}"
    badgeTextColor: "{colors.ink}"
    badgeTypography: "{typography.badge-text}"
    badgeRounded: "{rounded.none}"
    hoverOverlay: "rgba(0,0,0,0.04)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    overlayScrim: "linear-gradient(to bottom, transparent 40%, rgba(17,17,17,0.55) 100%)"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-primary}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    ctaComponent: "button-primary"
  editorial-tile:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  editorial-blush:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.ink}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    soldOutTextDecoration: line-through
    soldOutTextColor: "{colors.muted}"
    size: 40px
  badge-sale:
    backgroundColor: "{colors.sale-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.accent-indigo}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.hairline}"
    headlineTypography: "{typography.title-sm}"
    bodyTypography: "{typography.caption}"
    borderTop: none
    padding: "{spacing.xxl} {spacing.section}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    inputBorderBottom: "1px solid {colors.ink}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    backdropColor: "rgba(255,255,255,0.96)"
    padding: "{spacing.xl}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderDefault: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  wishlist-icon:
    strokeColor: "{colors.ink}"
    fillColor: transparent
    fillActive: "{colors.error}"
    strokeActive: "{colors.error}"
    size: 20px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    ctaComponent: "button-primary"

## Components

### Buttons
**`button-primary`** — A sharp-cornered black rectangle with no border radius, uppercase type at 13px/weight 500/0.12em tracking, 16px vertical padding yielding a 48px hit-height. Hover transitions to `#2d2d2d` ({colors.primary-active}); disabled drops to mid-gray #757575 ({colors.primary-disabled}) retaining white text. Used exclusively for add-to-cart, proceed-to-checkout, and primary editorial CTAs.

**`button-secondary`** — Identical geometry to the primary but inverted: white fill, 1px black border, black text. Used for secondary editorial actions, waitlist sign-up, and side-by-side CTA pairs where primary/secondary hierarchy must be maintained without introducing a new visual shape.

**`button-ghost`** — Transparent background, black underlined text at `{typography.button-md}` scale. Used for low-hierarchy actions such as "View all", "See more", and in-content text-link CTAs where a bordered rectangle would add too much visual weight.

### Text Input
**`text-input`** — No-radius input field with a 1px `#e5e5e5` border that sharpens to 1px `#111111` on focus. Placeholder in `{colors.muted}` (#757575). 48px tall, Arial 14px/400. Used for email newsletter signup, promo code entry, and address fields. The sharp corners mirror the button geometry exactly, creating a consistent orthogonal form vocabulary across interactive elements.

### Nav Bar
**`nav-bar`** — 56px fixed header on white canvas with a 1px `#e5e5e5` bottom border. Primary category links in `{typography.nav-label}` (13px/0.1em tracking) sit inline; the wordmark centers; search, wishlist, and cart icons sit right. On scroll past the hero the bar retains its border, anchoring the layout. No background blur or opacity shift — the nav stays opaque white throughout.

### Announcement Bar
**`announcement-bar`** — A 36px-tall deep-indigo (#221155) bar above the nav, white body copy in 12px/0.08em tracking. Carries shipping-threshold messages, promotion callouts, or region-selector prompts. The indigo is the only non-neutral brand surface in the entire header zone, making every announcement feel elevated rather than operational.

### Product Card
**`product-card`** — Zero-radius image container with no visible card boundary — the grid gap alone separates items. Product name in 13px/400/`{colors.ink}`, price in 14px/400/`{colors.body}` directly below. Sale price swaps to `{colors.error}` (#d14343) with the original struck through in `{colors.muted}`. A `badge-sale` chip in amber (#f1a500) can overlay the image top-left corner. On hover a faint `rgba(0,0,0,0.04)` scrim applies or a secondary editorial frame may swap in; the card itself never gains a shadow or lift effect.

### Hero Banner
**`hero-banner`** — Full-bleed photographic panel with a bottom-gradient scrim (`rgba(17,17,17,0.55)`) that lets white headline and sub-copy sit legibly over the image. Headline at `{typography.display-xl}` (32px/300), sub-copy at `{typography.body-md}`. A `button-primary` CTA sits within the content zone anchored near the lower third of the frame. No decorative borders, corner rounding, or text-shadow treatment.

### Editorial Tiles
**`editorial-tile`** and **`editorial-blush`** — Solid-background text panels that pair with full-bleed images in alternating 50/50 or 60/40 horizontal splits. Cream (#fffdea) and blush (#ffdddd) variants supply warmth contrast against the otherwise neutral page canvas. Headlines at `{typography.display-md}` (24px/300), body at `{typography.body-md}`, with `{spacing.xxl}` padding on all sides. The two variants alternate across editorial content rows, creating a soft temperature oscillation without introducing new structural shapes.

### Filter Chips
**`filter-chip`** — Pill-shaped chips for collection filtering by color, size, and category. Default: white fill, 1px `#e5e5e5` border. Active: black fill, white text, black border. The pill geometry here is the deliberate exception to the brand's flat-edge rule — it keeps filters visually distinct from the product card and button system, signaling "interactive toggle" rather than "primary CTA."

### Size Selector
**`size-selector`** — 40×40px square tiles with 1px `#e5e5e5` border, no radius, echoing the button geometry exactly. Active tile: black fill, white text. Sold-out tiles show struck-through labels in `{colors.muted}` (#757575). The square proportions maintain visual rhyme with the add-to-cart button sitting beneath them.

### Badges
**`badge-sale`** — Amber (#f1a500) hard-cornered rectangle with black uppercase 11px badge-text, absolute-positioned over the product image corner. **`badge-new`** — Same geometry in ink (#111111) with white text. Neither badge uses soft rounding — they read as clean geometric marks stamped on the photography rather than decorative overlays.

### Footer
**`footer`** — Deep-indigo (#221155) full-width panel carrying white column-link navigation, newsletter input, and policy links. Section headings in `{typography.title-sm}` (13px uppercase/0.1em tracking), links and body copy in `{typography.caption}`. The indigo footer is a deliberate counterweight to the editorial-white page body — it grounds the scroll experience and functions as the brand's sole large-surface color moment below the product content.

### Search Overlay
**`search-overlay`** — Full-width white overlay at 96% opacity, centered input with no box border — just a 1px black bottom border appearing on focus. Suggestion results render in `{typography.body-md}`. The overlay closes on outside-click or Escape. The underline-only input treatment keeps the search experience feeling editorial rather than utilitarian.

### Color Swatch
**`color-swatch`** — 20px circles at `{rounded.full}` with a 2px transparent border that switches to 2px `{colors.ink}` on active selection. The circular swatch is the only persistent use of full rounding in the product interaction zone, giving it instant identifiability alongside the square size tiles sitting beside it.

### Cart Drawer
**`cart-drawer`** — 400px right-anchored slide-in panel on white canvas with a 1px `{colors.hairline}` left border. Item names in `{typography.body-sm}`, section header in `{typography.title-md}`. Closes via an X icon or backdrop-click. Checkout CTA is a full-width `button-primary`, maintaining the flat black button as the single action shape across the entire purchase funnel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark + bag icon; announcement bar wraps to two lines if needed; hero text scales to display-md (24px/300); filter chips scroll horizontally in a single snapping row |
| Tablet | 744–1128px | Two-column product grid; nav shows 3–4 links with overflow in hamburger; hero remains full-bleed; editorial tiles stack if < 900px else remain 50/50 split |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav at 56px; editorial tiles at 50/50 or 60/40; cart drawer at 400px; search overlay spans full viewport width |
| Wide | > 1440px | Grid caps at four columns with increased gutter; max-width container (~1440px) centers content; hero image crops to a 16:5 or 16:4 aspect ratio |

### Touch Targets
- All buttons maintain 48px minimum height on mobile
- Size-selector tiles expand to 48×48px on touch viewports via padding increase
- Filter chips gain 44px touch height through additional vertical padding
- Nav icon targets (search, wishlist, cart) are padded to 44×44px minimum tap area
- Color swatches grow to 28px on mobile to remain comfortably tappable

### Collapsing Strategy
- Primary nav collapses to hamburger at < 1128px; category mega-menu becomes a full-screen slide-in drawer on mobile with accordion sub-categories
- Footer column links collapse to accordion-style expandable sections at < 744px
- Editorial 50/50 splits stack vertically (image above, text below) on mobile
- Product grid: 1 col (mobile) → 2 col (tablet) → 3–4 col (desktop)
- Announcement bar truncates to a single key message on mobile; if multiple messages, a carousel rotates them at 4s intervals

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom brand typeface not captured — the site almost certainly loads a proprietary or licensed serif/script font via JavaScript or CDN; Arial and Helvetica represent fallback stacks only and do not reflect the actual editorial typographic voice
- Canvas white (#ffffff) and on-primary white (#ffffff) are inferred as standard; neither appears in the extracted hex list
- Multiple blues extracted (#476bef, #002fe1, #4496f6, #007dc6) alongside the deep indigo (#221155) — it is unclear which are core brand UI colors versus colors from embedded third-party widgets (live chat, cookie consent banners, payment provider buttons); treat the blue family as interactive/infrastructure states rather than brand primaries
- Exact button hover transition timing and easing curves are not recoverable from static extraction
- Product card hover behavior (secondary image swap vs. zoom vs. scrim) could not be confirmed without live interaction observation
- Logo/wordmark exact rendering, custom lettering, and spacing rules are not captured
- Product image aspect ratios are not confirmed — likely 2:3 portrait for product tiles, 16:9 or 16:5 for hero panels
- Modal, drawer, and overlay animation specifics (slide direction, duration, easing) are not extractable statically
- Whether the announcement bar color is consistently #221155 or varies by promotion season could not be determined from a single extraction pass
