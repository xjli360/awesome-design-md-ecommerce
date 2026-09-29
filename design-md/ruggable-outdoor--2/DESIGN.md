---
version: alpha
name: "Ruggable"
source_url: "https://ruggable.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Linen parchment (#f6f4ef) spreads across Ruggable's digital surface before a single product loads — the background itself is a material reference, warm enough to suggest woven goods without naming them. The custom aprisRuggable typeface carries all display and headline weight, its letterforms landing somewhere between a geometric serif and a print-foundry workhorse; Manrope handles navigation, body, and UI chrome with a clean geometric warmth that never competes with the product photography. Neither font family appears in typical Shopify templates — both are deliberate brand choices.
  The palette runs in two registers. The first is earthy-dark: a near-charcoal (#282521) anchors every primary CTA and the wordmark, warm enough to avoid the coldness of true black while reading as premium rather than harsh. The second is accent: sage (#657567), rust (#934b32), marigold (#f5ce4e), and mint (#9fe3ba) rotate as collection or seasonal framing — not permanent brand primaries but chromatic signals that let photography set the mood. Error and alert states reach for a saturated red (#f02828 / #b30000), the only moment of high chroma unconnected to product color.
  Surfaces layer in warm neutrals: parchment (#f6f4ef) as the outermost canvas, linen (#ebe8dd) for section alternation, near-whites (#f7f7f7, #f1f1f1) for card faces. Corners are honest rather than pill or sharp: {rounded.sm} on buttons and inputs, {rounded.md} on cards, with {rounded.full} reserved only for filter chips, color swatches, and washability badges.
  The washability proposition — the single most differentiated claim in the rug category — surfaces through a persistent badge system stamped on nearly every product tile. A room visualizer and a Build Your Own rug configurator push the interaction surface well beyond a standard product grid, demanding distinct UI states for swatch selection, pile-height filtering, and scene toggling. Spacing follows a generous base-16 rhythm with section breaks at {spacing.section}, suited to the large-format photography that sells pattern and color at scale. Mobile touch targets hold at 44px minimum, reflecting a shopping journey that often begins with a customer photographing their own floor before browsing.

colors:
  primary: "#282521"
  primary-active: "#1a1817"
  primary-disabled: "#b3b3b3"
  ink: "#282521"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#f6f4ef"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  linen: "#ebe8dd"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sage: "#657567"
  rust: "#934b32"
  marigold: "#f5ce4e"
  mint: "#9fe3ba"
  error: "#f02828"
  error-text: "#b30000"
  link: "#2563eb"

typography:
  display-xl:
    fontFamily: "'aprisRuggable', 'aprisRuggable Fallback', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'aprisRuggable', 'aprisRuggable Fallback', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'aprisRuggable', 'aprisRuggable Fallback', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  badge-label:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  filter-label:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  price-display:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 14px 28px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focus-border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    imageRadius: "{rounded.sm}"
    cardRadius: "{rounded.md}"
    gap: "{spacing.sm}"
  hero-full-bleed:
    backgroundColor: "{colors.linen}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaStyle: button-primary
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  washable-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  collection-badge:
    backgroundColor: "{colors.linen}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.filter-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.filter-label}"
    rounded: "{rounded.full}"
    border: none
    padding: 8px 16px
    height: 36px
  rug-swatch-selector:
    size: 32px
    rounded: "{rounded.full}"
    border-inactive: "2px solid transparent"
    border-active: "2px solid {colors.ink}"
    border-hover: "2px solid {colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
    focus-border: "1px solid {colors.ink}"
  promotional-banner:
    backgroundColor: "{colors.linen}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption-strong}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Warm charcoal (#282521) fill with white all-caps Manrope label at 15px/600 weight and 0.6px letter-spacing. Corners sit at {rounded.sm} — honest, not pill-shaped. On hover deepens to near-black (#1a1817); disabled collapses to a mid-gray (#b3b3b3) fill with the same white label. Fixed height of 48px keeps vertical rhythm consistent whether the button sits in a hero, a product drawer, or a sticky add-to-cart footer.

**`button-secondary`** — Transparent fill bounded by a 1.5px charcoal stroke, matching all-caps typography and 48px height of the primary. Used when a secondary action lives beside a primary CTA — "Save to List" next to "Add to Cart", or "Browse All" beside a featured collection hero. On hover, the stroke thickens to 2px.

**`button-text`** — No fill, no border, 13px all-caps Manrope with underline. Inline tertiary actions only: "View All", "See More Colors", "Read Full Description".

### Navigation

**`nav-bar`** — 64px tall parchment (#f6f4ef) bar with a faint hairline ({colors.hairline-soft}) rule below. The wordmark sits left in aprisRuggable; Manrope 14px/500 links span the center (Rugs, Decor, Sale, How It Works); a search icon, account icon, and cart badge cluster right. On scroll, a subtle drop shadow appears without any background color shift, keeping the warm canvas tone in place.

### Product Card

**`product-card`** — Portrait-ratio image fills the top flush with {rounded.sm} image clipping. Below: product name in {typography.title-sm}, colorway descriptor in {typography.caption} muted, price in {typography.price-display}. A `washable-badge` dark pill overlays the image top-left on all machine-washable SKUs. A row of up to six `rug-swatch-selector` dots lines the bottom image edge, with a "+N" muted caption when more colors exist. No card border — cards lift on hover via shadow only.

### Hero

**`hero-full-bleed`** — Full-viewport-width panel with a linen (#ebe8dd) base, typically layered with a large lifestyle photograph at 50–60% of the panel width. Headline in aprisRuggable {typography.display-xl} (56px); one or two lines of {typography.body-md} Manrope below; a single {components.button-primary} CTA beneath that. The aprisRuggable letterforms at this scale carry the brand-premium signal without needing color help.

### Badges

**`washable-badge`** — Charcoal pill on every eligible tile, the word WASHABLE in 11px/700 all-caps Manrope. This badge is the most persistent UI element in the entire catalog view — it appears on approximately 90% of product tiles, functioning as both a feature flag and a brand reminder.

**`collection-badge`** — Linen-colored pill for editorial labels (NEW, BEST SELLER, LIMITED). Uses the same {typography.badge-label} scale but a warm background rather than charcoal fill, keeping it secondary in visual weight to the washable stamp.

**`sale-badge`** — Rust (#934b32) rectangle with {rounded.xs} corners for clearance and promotional pricing. The warm rust reads as urgency without the harshness of a pure red, staying harmonious with the earthy overall palette.

### Filter Chips

**`filter-chip`** — Pill-shaped ({rounded.full}) facet selectors for Size, Color, Style, Pile Height, and Material. Inactive: light gray surface with 1px hairline border and {typography.filter-label} charcoal text. Active: full charcoal fill with white text, border removed. On mobile, chips arrange in a horizontally scrollable single row below the category header, avoiding the need for a drawer on quick single-attribute filtering.

### Rug Swatch Selector

**`rug-swatch-selector`** — 32px circular color fills with a 2px charcoal ring on active, transparent ring idle, muted-soft ring on hover. Selecting a swatch immediately updates the product card image and the visible colorway name. When the swatch count exceeds six, remaining options are accessible via a "+N more" text link that opens the full color drawer.

### Search Bar

**`search-bar`** — Pill-shaped ({rounded.full}) input, 44px height, 1px hairline border at rest, strengthening to 1px charcoal on focus. A magnifier icon sits inside the left edge. On mobile, tapping the search icon in the nav expands to a full-width overlay with recent searches and trending categories listed below.

### Promotional Banner

**`promotional-banner`** — A slim linen (#ebe8dd) strip pinned above the nav bar. {typography.body-sm} Manrope text centered, carrying free-shipping thresholds, sale end dates, or promo codes. No close button in the standard configuration; dismisses on scroll in some campaign variants.

### Footer

**`footer`** — Full charcoal (#282521) dark footer, white body-sm links, caption-strong section headings. Four-column layout on desktop (Shop, Help, Company, Email Signup). Email capture uses a light-bordered input field on the dark surface — the single instance of an input rendered against a dark background throughout the UI. Social icons row below the columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to {typography.display-sm}; filter chips scroll horizontally in a single row; nav collapses to hamburger + wordmark; footer sections become tap-to-expand accordion |
| Tablet | 744–1128px | Two-column product grid; hero retains side-by-side image and text; filter chips wrap to two rows before switching to a filter-drawer trigger; nav shows primary links, hides secondary utility links |
| Desktop | 1128–1440px | Three- or four-column product grid; hero goes full bleed with text overlay left-aligned; persistent left filter rail replaces chip bar; sticky add-to-cart bar appears in PDP |
| Wide | > 1440px | Max-width container centered at 1440px; horizontal gutters grow proportionally; hero padding expands to {spacing.section} each side; product grid stays at four columns |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch target, including nav icons, swatch dots, and filter chips
- Rug swatch circles are 32px visual size wrapped in a 44px tap zone via invisible padding
- Filter chip height is 36px visual but extended to 44px effective touch area via vertical padding on the scroll row
- Cart icon and hamburger icon in mobile nav are padded to 44px square

### Collapsing Strategy

- Nav: full horizontal link bar → hamburger drawer containing all links, account, search, and a persistent cart icon
- Filters: left persistent rail on desktop → "Filter & Sort" floating pill button opening a bottom sheet on mobile
- Footer: four-column link grid → individual accordion sections; email signup remains visible and expanded at all widths
- Hero: two-column image+text → stacked image above text, CTA button centered, headline scales from display-xl to display-sm
- Product grid: 4 columns → 3 → 2 → 1 column as viewport narrows through breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus color values for interactive elements not extracted; primary-active (#1a1817) inferred from the palette's darkest warm-charcoal entry
- aprisRuggable font metrics (specific weight variants, x-height ratio, cap-height) are unknown; display sizes estimated at 56/36/24px based on common custom-serif display usage patterns
- Confirmed nav bar pixel height not recoverable from extraction; 64px is estimated from common Shopify Plus header patterns
- Transition durations and easing curves for swatch image updates, filter chip state changes, and hero parallax effects not captured
- Shadow/elevation token values (drop-shadow on scrolled nav, card hover lift) not present in extracted data
- Exact breakpoint pixel values for Ruggable's Shopify theme may differ from the 744/1128/1440 estimates used above
- Color roles for 'NEW' and 'BEST SELLER' collection badges are inferred from palette; actual hex assignments unconfirmed
- Marigold (#f5ce4e) and mint (#9fe3ba) usage context unknown — may be limited to seasonal campaign modules or visualizer UI elements rather than core product chrome
- Dark-mode or high-contrast accessibility variant not found in extraction
