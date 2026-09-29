---
version: alpha
name: "Anita Dongre"
source_url: "https://www.anitadongre.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  On a warm ivory field (#faf8f0) that reads more like unbleached muslin than a web-default white, Anita Dongre positions every garment and jewel as an artifact of place — Rajasthani handloom, Goan coastline, the specific green of forest preserved through the brand's land conservation work. That forest green (#1e381e) is the site's most load-bearing visual decision: it surfaces in primary CTAs, nav hover states, and editorial text treatments, binding the sustainability narrative directly to the shopping interface rather than siloing it in a dedicated section. Gold (#b18e35) plays second voice — reserved for ornamental hover states, editorial link treatments, and jewellery detail callouts — conjuring the zari thread and jadau stone-setting the bridal collections are built around.

  Display headlines run in Cormorant Infant, a high-contrast waisted roman used above 40px for collection names, hero banners, and feature quotes. Montserrat handles every utility layer: navigation links, button labels, filter accordions, and size-selector grids that span both Indian and Western sizing conventions. The opposition between these two typefaces mirrors the brand's own tension — couture atelier finishing delivered at multi-city retail and e-commerce scale. Lora fills long-form editorial text on Sustainability and Story pages, lending warmth without the vertical stroke stress of a full display cut.

  The warm blush surface (#f3e2cb) underlies product carousels and lookbook modules as an alternative to flat white, reading naturally beside ochre, dusty rose, and ivory fabrics. Corner radii stay intentionally small: product cards carry {rounded.sm} corners and primary buttons use {rounded.xs} — the discipline comes from craft proportional principles rather than the rounded-corner vocabulary of consumer tech. Full-bleed hero panels carry minimal typographic overlay: a single collection name in Cormorant Infant at 60–80px, left-aligned, leaving embroidered lehengas and layered necklaces room to read as objects before they read as products.

  Navigation architecture — Clothing, Jewellery, Accessories, Bridal, Gifting, Sustainability — routes each category to an editorial landing page rather than a flat filter grid, signaling a storytelling-first model. Urgency mechanics are nearly absent: no countdown timers, no low-stock alerts, only an occasional 'New' callout at 11px Montserrat uppercase on category chips. Price positioning relies on object photography and craft context rather than promotional pressure.

colors:
  primary: "#1e381e"
  primary-active: "#155e33"
  primary-disabled: "#908c88"
  gold: "#b18e35"
  ink: "#231f20"
  body: "#1e1e1e"
  muted: "#908c88"
  hairline: "#dcdddd"
  hairline-soft: "#d8d8d8"
  canvas: "#faf8f0"
  surface-soft: "#f2efe5"
  surface-card: "#f3e2cb"
  surface-warm: "#fff0f1"
  on-primary: "#ffffff"
  error: "#e60000"
  blush: "#ff787d"
  link: "#4d96e7"

typography:
  display-xl:
    fontFamily: "'Cormorant Infant', Lora, 'Times New Roman', serif"
    fontSize: 72px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cormorant Infant', Lora, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Cormorant Infant', Lora, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.4px
  body-md:
    fontFamily: "'Lora', 'Crimson Pro', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lora', 'Crimson Pro', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  overline:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px

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
    padding: 14px 32px
    height: 48px
    border: none
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    hoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    nameColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    gap: "{spacing.sm}"
    padding: "{spacing.base}"
    imageBorderRadius: "{rounded.sm}"
    hoverImageScale: 1.04
    transition: "transform 0.35s ease"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-primary}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.gold}"
    ctaComponent: button-primary
    layout: full-bleed
    overlayMaxWidth: 560px
    textAlign: left
    padding: "0 {spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.surface-card}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.gold}"
    padding: "{spacing.xxl} {spacing.xxl}"
    textAlign: center
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.title-md}"
    labelColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    aspectRatio: "3 / 4"
    hoverScale: 1.02
    overlayColor: "rgba(30, 56, 30, 0.2)"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  editorial-strip:
    backgroundColor: "{colors.surface-card}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xxl}"
    layout: two-column
    imageRounded: "{rounded.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.blush}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  gold-accent-rule:
    color: "{colors.gold}"
    height: 1px
    width: 48px
    margin: "{spacing.md} auto"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    backdropColor: "rgba(35, 31, 32, 0.5)"
  jewellery-detail-panel:
    backgroundColor: "{colors.surface-soft}"
    nameTypography: "{typography.display-sm}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.primary}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    ctaComponent: button-primary
    padding: "{spacing.xl} {spacing.xxl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption}"
    linkColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.gold}"
    padding: "{spacing.xxl} {spacing.section}"
    newsletterInputBg: "rgba(255, 255, 255, 0.1)"

## Components

### Buttons
**`button-primary`** — Deep forest green (#1e381e) fill with white text at 13px Montserrat uppercase, 1.5px letter-spacing, 4px corner radius, and 48px height. The uppercase tracking gives CTA labels formal weight expected in luxury fashion without relying on oversized type. Hover and active states deepen to `{colors.primary-active}` (#155e33); disabled state uses `{colors.primary-disabled}` at 60% opacity.

**`button-secondary`** — Transparent fill with a 1.5px forest-green border and matching button-md typography. On hover the button inverts to solid green with white text, creating a confident toggle rather than a hesitant outline state. Used for secondary CTAs like "Explore Collection" placed alongside a primary "Add to Bag."

**`button-text-link`** — Underlined body-sm at `{colors.ink}`, no background or padding, used inline in editorial passages and "Discover More" callouts within lookbook modules.

### Navigation
**`nav-bar`** — 72px tall on a warm ivory ground (`{colors.canvas}`) with a 1px hairline bottom border. The wordmark sits in a serifed light-weight treatment left of center. Category links run in 13px Montserrat weight 500 with 0.5px tracking; hover state transitions each link to `{colors.primary}`. Mega-menu panels open as full-width overlays pairing editorial imagery at left with nested category sub-links at right, preserving the storytelling-first architecture at every drill-down level.

### Product Card
**`product-card`** — Minimal card with a soft ivory image field (`{colors.surface-soft}`) and 8px corner radius on both the image and card container. Product name renders in 14px Montserrat semibold; price appears below in 15px Montserrat medium. On hover the card image scales at 1.04× with a 0.35s ease transition — deliberate enough to feel intentional, not sluggish. No star ratings or review counts appear on the card, keeping the visual register editorial rather than transactional.

### Hero Banner
**`hero-banner`** — Full-bleed photographic panel, typically 90–100vh on collection landing pages, with left-aligned editorial overlay constrained to 560px. Headline in Cormorant Infant at 72px weight 300 above a gold overline in 11px Montserrat uppercase that names the season or collection theme. CTA renders as `button-primary` below the headline. Overlay type sits directly on photography without a scrim, relying on image art direction to supply contrast — a choice that breaks down in strong edge cases and should be monitored.

### Category Tiles
**`category-tile`** — Portrait-ratio (3:4) tiles arranged in horizontal scroll rows on mobile or 4-column grids on desktop. On hover a semi-transparent forest-green overlay (20% opacity) washes the image, while the category label in 16px Montserrat semibold white anchors the lower third. Corner radius matches `{rounded.sm}`.

### Category Chips
**`category-chip`** — Fully pill-shaped (`{rounded.full}`) filter chips used on collection index pages to refine by metal, stone, or occasion. Default state is soft ivory with a hairline border; active state fills with `{colors.primary}` and white text. The pill shape is the one place the site's otherwise hard-corner language relaxes into softness.

### Editorial Strip
**`editorial-strip`** — Two-column layout alternating full-bleed photography against editorial copy on a warm blush field (`{colors.surface-card}`). Headline runs in Cormorant Infant at 32px forest green with a thin gold accent rule (48px wide, 1px height) above it. Body copy in Lora at 16px. Used for Sustainability stories, artisan origin narratives, and designer notes pages.

### Jewellery Detail Panel
**`jewellery-detail-panel`** — Right-side product panel on the PDP desktop layout, soft ivory background, no border radius. Product name in Cormorant Infant at 32px; price in 15px Montserrat medium forest green. Metal type, stone variety, and weight appear as 12px Montserrat caption in `{colors.muted}`. A 48px gold horizontal rule (`gold-accent-rule`) acts as a decorative section divider above the CTA block, echoing the jewellery's own ornamental logic.

### Badges
**`badge-new`** — Zero-radius rectangle in `{colors.primary}`, uppercase overline typography in white, anchored top-left over product card images. Used sparingly for truly new arrivals. **`badge-sale`** — Identical geometry in soft blush (#ff787d), appearing rarely given the brand's non-promotional commercial posture.

### Search Overlay
**`search-overlay`** — Full-width panel that drops beneath the nav bar on search icon tap, warm ivory background, no border radius. Input field carries a 1px hairline border and body-md Lora type for the query. A semi-transparent dark scrim covers the rest of the page. Results render as a two-column mini-grid of product cards within the overlay container.

### Footer
**`footer`** — Deep forest green field (`{colors.primary}`) with white link text and gold (`{colors.gold}`) section headings, inverting the page's light palette for visual closure. Four-column desktop grid covers collections, about, sustainability, and contact links. A semi-transparent newsletter input field sits against the green ground. The footer is the only full-width context where the forest green reads as a background rather than an accent.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer nav; hero reduced to 60vh with text below image; editorial strips stack vertically image-above-copy; footer collapses to accordion; category chips horizontal-scroll |
| Tablet | 744–1128px | Two-column product grid; nav retains full link row but collapses secondary sub-categories; hero at 75vh; editorial strips retain two-column with reduced padding |
| Desktop | 1128–1440px | Three- to four-column product grid; mega-menu overlays active; hero at full-bleed 90vh; PDP splits into two-column image/detail layout |
| Wide | > 1440px | Content caps near 1440px with canvas padding expanding symmetrically; hero photography extends edge-to-edge; type scales up slightly for display-xl contexts |

### Touch Targets
- All interactive elements meet 44×44px minimum; size-selector buttons are 44px square
- Nav hamburger tap zone is 48px
- Product card full surface is tappable, not only the image or CTA
- Filter chips carry 40px height with minimum 8px horizontal padding
- Mega-menu accordion items carry 48px row height on mobile drawer

### Collapsing Strategy
- Mega-menu collapses to full-screen drawer with accordion sub-categories on mobile
- Six-column footer grid stacks to single-column accordions
- Two-column editorial strips reflow to image above, copy below, full width
- Horizontal category chip rows become touch-scrollable with a hidden scrollbar
- PDP two-column layout stacks: image gallery above, detail panel below with sticky CTA bar

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact optical size axes and weight variants for Cormorant Infant — the site may use a variable font with specific axis settings not captured in font-family extraction
- Precise button border-radius not confirmed from computed styles; 4px inferred from visual inspection
- Mega-menu animation duration and easing not extracted
- Whether disabled button state uses a dedicated color token or CSS opacity reduction was not confirmed
- Cart drawer, wishlist panel, and size-guide modal visual specs not captured
- Exact letter-spacing values for Cormorant Infant at display sizes not confirmed — values here are approximated
- Mobile nav-bar height may differ from desktop 72px
- Sale price strikethrough color and original price treatment not specified
- Whether the site uses a custom web font served via Typekit or a system stack fallback for Cormorant Infant was not confirmed
