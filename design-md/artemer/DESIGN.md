---
version: alpha
name: "Artemer"
source_url: "https://www.artemerstudio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first signal that Artemer is not a conventional bridal jeweler is the teal (#00555a) — not the safe navy that heritage houses use, and not the pale sage that contemporary DTC brands have over-adopted, but a specific deep-water green that appears on every interactive surface from CTAs to focus rings to nav underlines. Set against near-white grounds (#ecf0f1, #eeeeee), this single chromatic statement carries the entire brand voltage without needing a secondary hue to complete it. The warm gold tones (#ae9a64, #a99a71) are not decorative interface flourishes but direct visual quotations of the 14k and 18k metals the studio works in — they surface on material callouts and category labels rather than dominating the UI, so the palette reads as extracted from the objects rather than imposed over them. Typography is Lato throughout, set conspicuously light: headlines run at weight 300 rather than the 700 that competitors reach for, so every line shares the fine-drawn quality of Artemer's prong-set solitaires and thin-band pavés. The word "alternative" in the site title is load-bearing — it signals non-traditional stones, organic forms, and a customer who is not shopping for what her mother wore. Buttons answer that positioning with architectural bluntness: flat teal blocks at {rounded.none}, or ghost outlines with a 1px teal border. No pill shapes, no shadows, nothing that competes with the photography. Product cards are edited to the minimum: a single jewel on an #eeeeee ground, a price, and a one-line material note. No urgency badges, no "only 2 left" mechanics. Scarcity communicates through curation. The result reads less like a shop and more like a studio showing a seasonal body of work — each piece in its own field of near-silence, the teal there only when you reach for something.

colors:
  primary: "#00555a"
  primary-active: "#003d42"
  primary-disabled: "#99c4c7"
  gold: "#ae9a64"
  gold-muted: "#a99a71"
  ink: "#222222"
  ink-strong: "#121212"
  body: "#4c4c4c"
  muted: "#4c4c4c"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#ecf0f1"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  error: "#bc0000"
  near-black: "#202020"

typography:
  display-xl:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.04em
  display-md:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.03em
  display-sm:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.35
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  price:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-lg:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.14em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em
  label-gold:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  announcement:
    fontFamily: "'Lato', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em

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
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  announcement-bar:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.announcement}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "1px solid {colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspect: "1/1"
    gap: "{spacing.sm}"
    padding: 0
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  product-card-hover:
    outlineColor: "{colors.hairline}"
    outlineWidth: 1px
    backgroundColor: "{colors.surface-card}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    minHeight: 70vh
    padding: "{spacing.section} {spacing.xl}"
  collection-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  material-badge:
    backgroundColor: "transparent"
    textColor: "{colors.gold}"
    typography: "{typography.label-gold}"
    border: "1px solid {colors.gold-muted}"
    rounded: "{rounded.none}"
    padding: 4px 10px
    display: inline-block
  category-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    border: "none"
  category-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  ring-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.ink}"
    gap: "{spacing.lg}"
    borderLeft: "1px solid {colors.hairline}"
    padding: "0 0 0 {spacing.xxl}"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    width: 44px
    height: 44px
  metal-swatch:
    width: 28px
    height: 28px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "2px solid transparent"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.surface-card}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — A flat teal block (#00555a) with zero border radius and uppercase Lato at 12px/0.14em letter-spacing. The height is fixed at 48px; padding is 14px 32px so the button sits comfortably wide without dominating photography-led pages. The pressed/active state deepens to `{colors.primary-active}` (#003d42); the disabled state bleaches to a muted `{colors.primary-disabled}` while keeping white text. No shadow or elevation — the button reads as a controlled typographic element, not a call-to-action device shouting for attention.

**`button-secondary`** — Ghost variant: transparent fill, 1px `{colors.primary}` border, same uppercase Lato. On hover, the teal fills in and text flips to white — a clean inversion rather than a soft wash. Used for secondary actions on the product detail page ("Save to Wishlist", "Book Appointment") below the primary Add to Cart action.

**`button-text`** — Zero chrome: no background, no border, underlined `{colors.ink}` text in `{typography.button-sm}`. Appears inline in editorial copy for navigational nudges ("Explore the collection", "Read about our process"). Does not compete with the primary CTA.

### Announcement Bar

**`announcement-bar`** — 36px near-black (#121212) strip at the topmost edge of the page, carrying shipping thresholds and promotional copy in 12px Lato at modest letter-spacing. Light `{colors.surface-soft}` text keeps it readable without the harshness of pure white on black.

### Navigation

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom rule. Nav links render in 13px Lato at 0.06em letter-spacing — light enough to feel editorial. The wordmark is left-aligned on desktop, centered on mobile. A 1px teal underline marks the active section. Utility icons (search, account, cart) sit right-aligned; cart shows a numeric indicator in `{colors.primary}` when populated.

### Product Card

**`product-card`** — Square 1:1 crop on an `{colors.surface-card}` (#eeeeee) ground with zero padding — the photograph fills edge to edge. Below: the ring name in `{typography.title-md}` at `{colors.ink}`, price in `{typography.price}` at `{colors.body}`, and a material note in `{typography.caption}` at `{colors.muted}`. No hover overlays, no secondary image swap, no urgency badges. The grid communicates through density and restraint rather than interactivity mechanics. `{component.material-badge}` may appear beneath the price when the product has a featured metal story.

### Hero

**`hero`** — Full-width editorial module, typically a single large-format photograph with the ring centered against a neutral or dark ground. The overlay carries a `{typography.display-xl}` headline at weight 300 and a `{typography.body-md}` subhead in `{colors.body}`, followed by a single `{component.button-primary}`. Minimum height 70vh on desktop. The background is `{colors.surface-soft}` when no photography is present.

### Collection Banner

**`collection-banner`** — Centered text module at the top of category pages: a `{typography.display-md}` headline and a `{typography.caption}` descriptor sentence in `{colors.muted}`, separated from the grid below by a 1px `{colors.hairline}` rule. No imagery; the words alone introduce the category.

### Material Badge

**`material-badge`** — An inline tag in `{colors.gold}` (#ae9a64) with a 1px `{colors.gold-muted}` border. Displays metal type ("14k Yellow Gold", "Platinum 950", "Rose Gold") on product cards and within the detail panel's options section. Zero border radius — the squared corners echo machined precision. When multiple metal options exist, badges appear as a horizontal row.

### Category Filter

**`category-filter-pill`** / **`category-filter-pill-active`** — Flat rectangular tabs filtering collections by style (solitaire, pavé, cluster, eternity). Inactive: `{colors.surface-soft}` fill, `{colors.ink}` text. Active: `{colors.primary}` fill, white text. Both at {rounded.none} — no pill shaping. On mobile these scroll horizontally in a single row with hidden scrollbar.

### Ring Detail Panel

**`ring-detail-panel`** — The right column of the product detail layout. Price renders large in `{typography.price-lg}` (22px, weight 300) — present but never heavier than the photography. A 1px `{colors.hairline}` left border separates it from the image column on desktop; on mobile it stacks below. Metal swatches (`{component.metal-swatch}`) sit in a row directly below the price; selecting one updates imagery inline.

### Size Swatch

**`size-swatch`** — 44×44px squares in a uniform grid for ring size selection. Default state: `{colors.canvas}` fill, `{colors.hairline}` border. Selected state: border swaps to `{colors.primary}`, fill remains white — only the perimeter signals state, keeping the grid visually calm. A "Find my size" text link in `{typography.button-sm}` sits below the grid.

### Metal Swatch

**`metal-swatch`** — 28px circular swatches colored to represent the actual alloy (yellow gold, rose gold, white gold, platinum). A 2px `{colors.primary}` ring appears on the selected swatch; unselected swatches carry a transparent border so they read as floating circles rather than buttons.

### Breadcrumb

**`breadcrumb`** — Compact trail in `{typography.caption}` at `{colors.muted}`, with chevron separators in `{colors.hairline}`. The active (current) page name renders in `{colors.ink}` and is not linked. Appears on product detail and collection pages; omitted from the homepage.

### Footer

**`footer`** — Near-black (#202020) ground with `{colors.surface-soft}` body text and `{colors.hairline-soft}` link text. Section labels ("Shop", "About", "Help", "Follow") in `{typography.title-sm}` uppercase with `{colors.surface-card}` color. On hover, links brighten to `{colors.on-primary}`. An inline email field for newsletter signup uses a minimal teal-border `{component.text-input}` variant against the dark background. Social icons are right-aligned on desktop, centered on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer with teal accent on active item; hero becomes 80vh portrait; ring detail panel stacks below imagery; size swatch grid spans full width; filter pills scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; abbreviated nav shows four primary links; hero uses landscape crop at 55vh; detail panel appears in a 45/55 image/text split |
| Desktop | 1128–1440px | Three-column product grid; full nav visible with utility icons; ring detail panel beside image at 50/50 split; collection banner centered at max 800px |
| Wide | > 1440px | Content max-width ~1280px centered on canvas; four-column grid option on collection pages; hero photography fills viewport width with content constrained |

### Touch Targets

- All size swatches are minimum 44×44px per platform guidelines
- Nav links and footer links padded to 44px tap height on mobile even when visually smaller
- "Add to Cart" button spans full content width on mobile (100% minus {spacing.xl} margins)
- Metal swatches are 28px visually but receive a 44px invisible tap target via padding
- Filter pills padded to minimum 36px tap height

### Collapsing Strategy

- Nav hamburger slides a full-height left drawer; active section marked by 2px teal left border
- Product detail switches from horizontal two-column to vertical stack at 744px: image → breadcrumb → title → material badges → price → metal swatches → size swatches → CTA → description
- Category filter row becomes horizontally scrollable at < 744px; `overflow-x: scroll; scrollbar-width: none`
- Footer changes from four-column to accordion-collapsed sections on mobile; each section header toggles visibility
- Hero headline scales from 36px (desktop) to 24px (< 744px) via two fixed breakpoints rather than fluid type

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Lato confirmed as the only distinctive web font in the stack; exact weight distribution per component (300 vs 400 vs 700) not confirmed from extracted computed styles — weights above are inferred from brand positioning
- Primary teal (#00555a) is confirmed; hover/active variant (#003d42) estimated at approximately 15% luminance reduction — not directly extracted
- Gold token function (#ae9a64, #a99a71) unclear — may be limited to specific promo callouts or material labels rather than a system-wide accent; treat as conditional
- #0e5abf appears in the extracted palette and is likely a Shopify default link color (not an Artemer brand token); excluded from all component specs
- No motion or transition data extracted — hover durations, panel slide animations, and image lazy-load behavior are unconfirmed
- Footer background confirmed from #202020/#121212 in palette; exact Shopify section structure not verified
- Photography treatment (ground color, lighting style, whether lifestyle or product-only) inferred from #eeeeee surface-card — not directly observed
- Ring sizer / guide tool implementation unknown; may be a third-party embed (Whiteflash, Ring Advisor) or a custom Shopify section
- No iconography or illustration style data extracted — icon weight and style (line vs filled, stroke width) unconfirmed
