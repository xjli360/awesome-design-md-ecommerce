---
version: alpha
name: "WWAKE"
source_url: "https://www.wwake.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lavender where there should be champagne — WWAKE deploys #9681ff as the primary CTA voltage, a choice that would read as wrong on almost any other fine jewelry site and reads completely right here. Wing Yau's NYC studio makes pieces that are more structural than sentimental (segmented opal drops, mismatched stacking rings, bezel-set arrangements that prioritize geometry over flash), and the digital system follows: a near-black canvas (#17171c) several stops deeper than the soft charcoals competitors prefer, Unica as the house grotesque, and zero border-radius on buttons and input fields. The purple family spans five values — pale #cbc0ff and #bbaeff for disabled and ambient states, the brand-true #9681ff, the active hover #7e65ff, and the deep anchor #5c5092 — meaning the entire interactive hierarchy can be built within a single hue family using tint and saturation rather than importing a contrasting accent. Coral (#ff6464) enters as punctuation: sale badges, error borders, the occasional editorial hover that snaps attention. The monospace stack in the extraction suggests a secondary type register for SKUs, price formatting, or cart line items, creating a deliberate tension between the refined display grotesque and something more mechanical and utilitarian. Unica at low weight (300) for display headlines stays architectural without reading formal, and the uppercase tracking on button and badge labels — 0.08–0.10em — gives small text the spatial confidence to hold against product photography. Components use {rounded.full} strictly for pills and swatches, {rounded.none} everywhere structural, which enforces a clear vocabulary: organic only at the smallest scale, hard-edged everywhere else. The dark footer mirrors the dark hero, wrapping product grids in a continuous near-black ground so that each collection page reads as a lit vitrine rather than a retail shelf.

colors:
  primary: "#9681ff"
  primary-active: "#7e65ff"
  primary-deep: "#5c5092"
  primary-disabled: "#cbc0ff"
  primary-soft: "#bbaeff"
  accent: "#ff6464"
  ink: "#17171c"
  body: "#2d2d2d"
  dim: "#27252d"
  muted: "#777576"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-dark: "#121212"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.1px
  title-md:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  caption-mono:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.06em
  button-md:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  button-sm:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  badge-label:
    fontFamily: "Unica77, Unica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    border: "1px solid {colors.ink}"
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  text-input-error:
    borderColor: "{colors.accent}"
    textColor: "{colors.accent}"
    rounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1 / 1"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price}"
    textColor: "{colors.accent}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 80vh
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
    maxWidth: 640px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} 0 {spacing.xl} 0"
  filter-pill:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.md}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  product-detail-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4 / 5"
  swatch-circle:
    width: 20px
    height: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
  swatch-circle-selected:
    border: "2px solid {colors.ink}"
    rounded: "{rounded.full}"
  sku-label:
    typography: "{typography.caption-mono}"
    textColor: "{colors.muted}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — Sharp-cornered (`{rounded.none}`) lavender-violet block in `{colors.primary}` (#9681ff) with uppercase Unica at 12px and 0.10em tracking. Hover deepens to `{colors.primary-active}` (#7e65ff); disabled washes to `{colors.primary-disabled}` (#cbc0ff) without reducing opacity. The hard corner is load-bearing to the brand feel — it marks the button as a studio seal rather than a consumer pill.

**`button-secondary`** — Transparent fill, 1px `{colors.ink}` border, same uppercase Unica type. On hover the border fills solid ink with canvas text, creating an inversion that reads as a clean press state. Both button variants sit at 44px height to match the text-input baseline.

**`button-ghost`** — No border, no fill, muted text label in `{typography.button-sm}`. Reserved for soft actions (continue browsing, close overlay) where any border weight would compete with adjacent product imagery.

### Text Input
**`text-input`** — Flat field with a 1px `{colors.hairline}` border at rest. Focus shifts the border to `{colors.primary}`, making the lavender visible in a form context without a fill change. No corner radius (`{rounded.none}`) holds the form grid consistent with buttons. Error state uses `{colors.accent}` (#ff6464) on border and label text simultaneously for immediate legibility.

### Navigation
**`nav-bar`** — 56px bar at `{colors.canvas}` with a 1px `{colors.hairline}` rule beneath. Category links at `{typography.nav-link}` (12px, 0.06em) sit compactly — fine jewelry navigation rarely needs more than five top-level items. The dark variant (`nav-bar-dark`) switches fill to `{colors.ink}` for editorial landing pages, matching the hero ground. The announcement bar above deploys `{colors.primary}` as background, making the lavender the first brand signal on every page load.

### Product Card
**`product-card`** — Square image (1:1 aspect), no rounding, title in `{typography.body-sm}`, price in `{typography.price}`. Sale pricing switches the value to `{colors.accent}`. Spacing between card elements uses `{spacing.sm}`; grid gaps are handled at the layout level so cards remain fully flush when tight-gridded. `new-badge` and `sale-badge` pills float over the image corner using `{rounded.full}`.

### Hero
**`hero`** — Dark-field section at `{colors.surface-dark}` (#121212) with display type in `{typography.display-xl}` at weight 300, capped at 640px to preserve a sense of restraint and white space on wide viewports. Subtitle drops to `{colors.muted}` against the dark ground, softening the transition before product grid.

### Collection & Filtering
**`collection-header`** — White canvas with display-md heading, generous top and bottom padding. `filter-pill` elements use a hairline border and muted label text at rest; active state inverts to a solid ink fill. Both states use `{rounded.full}` to signal that filters are interactive chips, not structural tabs.

### Badges
**`material-badge`** — Surface-soft pill in `{typography.badge-label}` uppercase for metal and material callouts (14k gold, sterling, opal). `{sale-badge}` arrives in `{colors.accent}` coral; `{new-badge}` in `{colors.primary}` lavender — the two badge colors map directly to the brand's two action voltages.

### Product Detail
**`product-detail-gallery`** — 4:5 portrait frame with `{colors.surface-soft}` background for consistent object photography presentation. `swatch-circle` elements are 20px discs with a `{rounded.full}` mask; the selected state adds a 2px `{colors.ink}` ring with a gap transparent-border that remains legible against both light and dark metal finishes.

**`sku-label`** — Monospace caption in `{colors.muted}` for SKU and material code display beneath the product title. The monospace stack creates a brief, intentional register shift — engineering code next to artisan description.

### Search Overlay
**`search-overlay`** — Full-width panel in `{colors.canvas}` dropping from the nav bar. Bordered at the bottom by a `{colors.hairline}` rule. Input uses the standard `text-input` style; results render as a compressed product-card grid below.

### Footer
**`footer`** — Near-black field (`{colors.surface-dark}`) closing the page on the same ground note as the hero, wrapping the user experience symmetrically. `{typography.title-sm}` uppercase headings in `{colors.muted}` label the columns; link text at `{typography.body-sm}` remains muted rather than bright, signaling utility without promotion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + hamburger + cart icon; hero title scales to `{typography.display-md}`; footer columns stack to single column |
| Tablet | 744–1128px | Two-column product grid; nav expands inline at full label set; hero padding tightens to `{spacing.xl}` |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav and announcement bar visible; hero at 80vh with 640px text cap |
| Wide | > 1440px | Container capped ~1400px and centered; grid stays four columns; hero image scales to fill with text block fixed-width |

### Touch Targets
- All buttons minimum 44px height
- Swatch circles expand to 32px touch target via invisible padding ring on mobile
- Nav links minimum 44px tap zone with vertical padding compensation
- Cart, search, and hamburger icons maintain 44×44px active area
- Filter pills minimum 36px height on mobile with 12px horizontal padding minimum

### Collapsing Strategy
- Navigation collapses to hamburger drawer at mobile; drawer background uses `{colors.canvas}` with full-height overlay
- Product filters collapse behind a bottom sheet "Filter / Sort" toggle on mobile; filter-pill grid renders inside the sheet
- Hero text block shifts from side-by-side with image to stacked, text below image, at mobile
- Footer grid collapses: four columns at desktop, two at tablet, one at mobile
- Announcement bar truncates to a single scrolling marquee line on narrow viewports if copy overflows

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Border-radius convention (`{rounded.none}` for structural elements) inferred from brand positioning; no explicit CSS radius values extracted
- Font weight range for Unica77 not confirmed — weights 300/400/500 assumed based on grotesque font conventions and jewelry-category norms
- Canvas color not directly extracted; #ffffff assumed from implicit page background
- No dark-mode palette variant detected in extraction
- Hover/focus transition durations not captured — CSS animation values unavailable
- Monospace font stack presence confirmed (`monospace` in extraction) but specific usage contexts (SKU, price, cart) are inferred
- Grid column counts, gutter widths, and breakpoint pixel values are inferred, not extracted from live CSS media queries
- No explicit letter-spacing or tracking values extracted for body text; values derived from grotesque conventions
