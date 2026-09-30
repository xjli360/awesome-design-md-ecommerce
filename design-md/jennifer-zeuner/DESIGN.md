---
version: alpha
name: "Jennifer Zeuner"
source_url: "https://www.jenniferzeuner.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Neon pink bleeds through a white canvas like spilled nail lacquer — Jennifer Zeuner's signature #ea1298 magenta saturates every primary CTA, active badge, and hover state against the brand's crisp off-white scaffolding. The palette refuses simple femininity: hot pink sits alongside deep teal (#108474), a shade more associated with apothecary signage than costume jewelry, and acid gold (#fbcd0a) that reads closer to contemporary art than bridal. A softer lavender (#a89cc8) and muted mint (#c1e6e6) emerge in promotional sections and category tints, giving the color vocabulary range without the monoculture of most jewelry brands at this price point. The brightest variant, #ff0890, surfaces in hover moments and sale callouts — a single step hotter than the base primary, extending the pink register into something genuinely electric rather than just coral-adjacent.

  Typography runs a two-family system. Montserrat carries all navigational, display, and button text in uppercase — tracking opens to 0.08–0.1em on smaller labels, creating geometric-sans authority in compressed formats. Nunito Sans softens product descriptions and body copy into a conversational, rounded register, letting the uppercase display assertions breathe. Baskerville appears in select editorial placements, a serif note that nods toward the brand's 14K gold positioning even within the costume category.

  Geometry is predominantly flat — buttons are sharp rectangles with no border radius (`{rounded.none}`), product cards sit square without elevation or shadow, and image presentation relies on a subtle 1.03× scale hover rather than card lift or shadow casting. The deliberate exception is the filter chip system, which uses pill shapes (`{rounded.full}`) as a contrast to the otherwise hard-cornered UI — making browse interaction feel exploratory where purchase interaction feels decisive. Review stars break from convention by rendering in the brand magenta rather than conventional gold, folding social proof into the visual system rather than treating it as an unstyled widget import.

colors:
  primary: "#ea1298"
  primary-active: "#ac036c"
  primary-bright: "#ff0890"
  primary-disabled: "#ff96d7"
  accent-teal: "#108474"
  accent-gold: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-mint: "#c1e6e6"
  ink: "#212121"
  body: "#555555"
  muted: "#646464"
  muted-light: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  surface-light: "#f2f2f2"
  on-primary: "#ffffff"
  error-bg: "#f8d7da"
  error-text: "#721c24"

typography:
  display-xl:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  display-md:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.03em
    textTransform: uppercase
  title-md:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  editorial:
    fontFamily: "Baskerville, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  price:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "Montserrat, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
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
    height: 44px
    transition: background-color 0.2s ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-bright:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-ghost-pink:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-md}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: 1/1
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    hoverImageScale: 1.03
    hoverTransition: transform 0.3s ease
    badgeTypography: "{typography.button-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaComponent: button-primary
    minHeight: 520px
    imagePosition: right
  collection-banner:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"
    padding: 48px 64px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 8px 16px
    height: 36px
  price-display:
    regularPriceTypography: "{typography.price}"
    regularPriceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    comparePriceColor: "{colors.muted}"
    comparePriceDecoration: line-through
  review-stars:
    starFilledColor: "{colors.primary}"
    starEmptyColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.surface-light}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    accentColor: "{colors.primary}"
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — A flat magenta rectangle (#ea1298) with no border radius and uppercase Montserrat at 13px/700/0.1em tracking. On hover the background deepens to #ac036c; in sale or promotional contexts the brighter #ff0890 variant (`button-primary-bright`) takes over, amplifying urgency without introducing a new color family. Disabled state bleeds to washed #ff96d7 while keeping white text legible. Height is fixed at 44px across all size contexts to maintain a consistent vertical rhythm.

**`button-secondary`** — White fill with a 1px solid #212121 border, mirroring button-primary's letterform and dimensions exactly. Used for "Continue Shopping," cart confirmation dismissals, and any secondary CTA that must sit beside a primary without competing. No border radius maintains the hard-edge pairing.

**`button-ghost-pink`** — A transparent field with 1px solid #ea1298 border and magenta text, used in product overlay flows, wishlist actions, and anywhere the surface behind the button carries visual weight that a filled button would interrupt.

### Product Card

**`product-card`** — Square 1:1 imagery sits on a white field with zero border radius and no drop shadow, keeping the grid visually flat. Hover triggers a 1.03× CSS scale transform (0.3s ease) — a zoom-in that signals interactivity without the card popping off the page. Product title sets in Montserrat 600 at 16px; price in Montserrat 600 at 15px. Sale prices render in #ea1298, compare-at prices in #646464 with line-through, creating a three-level hierarchy that is readable at grid density. `badge-new` (magenta) and `badge-sale` (gold) sit top-left, pinned absolutely over the image.

### Badges

**`badge-new`** — A flat magenta (#ea1298) rectangle with white uppercase Montserrat at 11px and no border radius. Positioned over the top-left corner of the product image to capture attention without obscuring the main product area.

**`badge-sale`** — Identical geometry to `badge-new` but filled with acid gold (#fbcd0a) and dark #212121 text. The color distinction between sale and new states is immediate even at small sizes in a dense grid.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — Pill shapes (`{rounded.full}`) are the only rounded interactive elements in the vocabulary, deliberately contrasting the flat button and card geometry. Inactive chips use a white field with a #dedede hairline border; active chips flip to solid #ea1298 with white uppercase text. The pill-vs-rectangle distinction codes browsing as exploratory and purchasing as decisive at the UI grammar level.

### Hero Banner

**`hero-banner`** — A full-width split composition on a #f7f7f7 ground: copy anchored left, editorial product photography right. The headline uses display-xl — 36px Montserrat uppercase at 0.04em tracking — while the subhead drops to Nunito Sans body-md for contrast. A `button-primary` CTA sits below the subhead. Minimum 520px height preserves editorial weight above the fold on all desktop breakpoints.

### Collection Banner

**`collection-banner`** — A shallower band in #f2f2f2 used between product grid rows to introduce category or editorial context. The headline runs display-md (Montserrat uppercase 24px); body copy in body-sm (Nunito Sans 14px). A thin #ea1298 accent line or typographic color treatment marks the section as a brand voice moment rather than a Shopify boilerplate separator.

### Review Stars

**`review-stars`** — Filled stars render in #ea1298 rather than the conventional yellow-gold, integrating the review widget into the brand's color system. The count and average appear in Nunito Sans 12px/caption at #646464. This treatment makes ratings a brand touchpoint rather than an imported third-party component.

### Navigation

**`nav-bar`** — A white 64px bar with a #e9e9e9 hairline bottom border. All navigation links run in Montserrat uppercase 12px/600 at 0.08em tracking. The logo uses display-md (Montserrat uppercase 24px). The bar carries no mega-menu illustration or category imagery — all navigation is text-only, keeping the chrome minimal for a jewelry context where the product image carries full visual authority.

### Search Bar

**`search-bar`** — A flat, zero-radius input in #f7f7f7 with a #dedede border and a #646464 search icon. Height of 40px keeps it compact within the nav band or as a standalone page element. On focus, the border steps to #212121.

### Footer

**`footer`** — A dark #212121 ground with #f7f7f7 body text and section headings in Montserrat uppercase 12px/700. Body links in Nunito Sans 14px. The #ea1298 accent surfaces in hover states on links and in the logo lockup, maintaining brand presence without overwhelming the dark ground. Organized in a three-column grid on desktop (about us / shop / contact + social), collapsing to a stacked accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks to full-width image above copy; nav collapses to hamburger drawer; filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; hero retains split layout at reduced image proportion; nav shows top-level links only, no sub-categories visible |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all category text links; hero at full 520px height with generous side margins |
| Wide | > 1440px | Content max-width capped at ~1380px centered; generous side margins; product grid stays at four columns; hero image scales up within its container |

### Touch Targets
- All primary and secondary buttons minimum 44px height on mobile
- Filter chips minimum 36px height with 16px horizontal padding
- Nav links minimum 44px tap area via vertical padding extension on mobile drawer
- Product card "Quick Add" or "Add to Cart" overlays cover the full card width at mobile sizes
- Search bar minimum 44px height on mobile

### Collapsing Strategy
- Navigation: hamburger drawer (slides in from left) at < 744px; full inline link bar at ≥ 744px
- Product grid: 1 column → 2 columns → 3–4 columns across Mobile → Tablet → Desktop
- Hero: stacked image-above-copy on mobile; side-by-side split from tablet upward
- Filter chips: horizontal scroll row on mobile; wrapping pill grid on tablet and above
- Footer columns: single stacked accordion on mobile; 3-column grid on desktop; column order preserved

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom webfont hosting; Montserrat and Nunito Sans likely load via Google Fonts CDN — exact weight subset and optical size configuration not verified
- Baskerville usage is inferred from font-stack presence in extracted CSS; specific components or page sections using it could not be confirmed without full Liquid template access
- Accent colors #a89cc8 (lavender) and #c1e6e6 (mint) appear in the extracted palette but their exact component assignments are unclear — likely promotional section backgrounds or seasonal banner tints rather than permanent UI tokens
- No icon system identified; stroke weight, fill style, and glyph set for cart, search, and wishlist icons not confirmed
- Animation timing and easing curves for hover states, drawer transitions, and filter chip toggles are inferred Shopify/CSS defaults — no design tokens extracted
- Mobile navigation drawer design (background color, close gesture, stacking with announcement bar) not confirmed
- Announcement bar / promotional banner above the nav-bar: color and typography treatment not confirmed
- No confirmed quick-add or product overlay interaction pattern on the product grid card
