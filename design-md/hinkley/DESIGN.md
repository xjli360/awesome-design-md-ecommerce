---
version: alpha
name: "Hinkley"
source_url: "https://www.hinkley.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The palette describes a thermal arc — gray-cool architectural metal (#aaabac, #c2c2c2) warming through antique brass (#a48b5f) toward the amber pulse of a live filament (#ff9635) — and in a catalog whose subject is the transition between dark and lit, this chromatic sequence serves as both brand vocabulary and product demonstration. Surfaces lean warm rather than clinical: plaster-cream (#f2f1f0), aged linen (#eae2d8), and parchment (#fdf0d5) make product photographs read as if the fixtures are already switched on. The deepest neutral is not pure black but an oiled-bronze near-dark (#2c251c), a color that appears in product-line finish names and in the footer stripe, making the structural chrome feel continuous with the merchandise itself.

  Type pairs Chronicle — H&FJ's editorial serif that carries the cadence of an architectural monograph — with the Chalet family's mid-century American cut (ChaletNewYork1960), a House Industries geometric sans that holds faint postwar optimism. Chronicle handles collection titles, landing-page editorial headings, and price display; Chalet carries navigation, spec tables, filter labels, and all button chrome. The register shifts from formal in large headers to functional in interface copy without ever breaking composure.

  Components hold to a decisively rectangular vocabulary: `{rounded.xs}` on buttons and product cards, `{rounded.none}` on form inputs, with no pill shapes anywhere in the primary UI. The brass primary (#a48b5f) occupies CTAs and finish-swatch active states; amber (#ff9635) is reserved for "New" badges and promotional callouts that need warmth without the weight of the main action color. Safety-rating labels (UL Wet Rated, Damp Rated) sit as distinct spec-badge elements on `{colors.surface-linen}` rather than inline with product copy, acknowledging that a meaningful fraction of buyers are specifiers and contractors who need technical detail scannable at a glance.

  The gray range is unusually granular — seven distinct mid-grays from #aaabac through #353535 — appropriate for a brand whose finishes include Polished Nickel, Brushed Bronze, and Aged Zinc, where the catalog itself must distinguish metals that differ by only a few Kelvin of surface warmth.

colors:
  primary: "#a48b5f"
  primary-active: "#8a7349"
  primary-disabled: "#d4c4a0"
  ink: "#222222"
  ink-deep: "#2c251c"
  body: "#353535"
  muted: "#606060"
  muted-light: "#8f8f8f"
  hairline: "#d7d7d7"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-warm: "#f2f1f0"
  surface-linen: "#eae2d8"
  surface-card: "#ffffff"
  warm-glow: "#fdf0d5"
  on-primary: "#ffffff"
  accent-amber: "#ff9635"
  error: "#e02b27"
  error-deep: "#660000"
  link: "#1979c3"

typography:
  display-xl:
    fontFamily: "'Chronicle Display', Baskerville, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Chronicle Display', Baskerville, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Chronicle Display', Baskerville, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  spec-label:
    fontFamily: "'Chalet-NewYork1960', ChaletNewYork, Chalet, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price:
    fontFamily: "'Chronicle Display', Baskerville, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: "12px 28px"
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 27px"
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: "12px 0"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    height: 44px
    padding: "10px 14px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "10px 14px 10px 40px"
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.ink-deep}"
    dropdownBackground: "{colors.canvas}"
    dropdownBorder: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-warm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    hoverBorder: "1px solid {colors.hairline}"
    hoverShadow: "0 2px 12px rgba(44,37,28,0.10)"
  finish-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderInactive: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    outlineOffset: 2px
    gap: "{spacing.xs}"
    tooltip: "{typography.caption}"
  collection-hero:
    backgroundColor: "{colors.surface-warm}"
    overlayColor: "{colors.ink-deep}"
    overlayOpacity: 0.36
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    headingColor: "{colors.canvas}"
    subheadColor: "{colors.surface-linen}"
    padding: "64px 32px"
    minHeight: 480px
  promo-strip:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.surface-linen}"
    typography: "{typography.label-uppercase}"
    height: 36px
    linkColor: "{colors.primary}"
  spec-badge:
    backgroundColor: "{colors.surface-linen}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  room-filter-chip:
    backgroundInactive: "{colors.canvas}"
    backgroundActive: "{colors.ink}"
    textInactive: "{colors.body}"
    textActive: "{colors.canvas}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.surface-warm}"
    linkColor: "{colors.surface-linen}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-uppercase}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "48px 0"

## Components

### Buttons

**`button-primary`** — Brass-filled (#a48b5f) with white uppercase Chalet text at 0.08em tracking, 44px tall, 4px radius. The active state darkens to #8a7349; disabled state washes to #d4c4a0 and locks the cursor. Used exclusively for primary purchase actions (Add to Cart, Find a Dealer) and never for secondary wayfinding.

**`button-secondary`** — White fill with a 1px solid ink (#222222) border, matching height and typography to `button-primary`. Active state shifts the fill to `{colors.surface-warm}` rather than inverting, preserving the ink border. Used for secondary CTAs like Download Spec Sheet or View Collection.

**`button-ghost`** — Zero background, zero border, brass text (#a48b5f). Padding only on top/bottom; left edge aligns flush with surrounding copy. Used for inline text actions like "See all finishes" or breadcrumb-style navigation within product detail pages.

### Form Inputs

**`text-input`** — Full-square corners (`{rounded.none}`), 1px #d7d7d7 border at rest, upgrading to 1px #222222 on focus with no glow or shadow. Placeholder in #8f8f8f. Height 44px. Used in search, dealer locator, and checkout fields. The hard corner is consistent with the overall rectangular vocabulary and distinguishes inputs visually from the softly bordered product cards.

**`search-bar`** — Shares the square-corner treatment but sits on `{colors.surface-soft}` rather than white, making it read as a recessed input rather than a form field. Left-inset magnifier icon in `{colors.muted}`. Padding compensates for icon overlap at left. On mobile, expands full-width and replaces the nav utility row.

### Navigation

**`nav-bar`** — 72px tall, white canvas, bottom border in `{colors.hairline-soft}`. Logo sits left; navigation categories in uppercase Chalet (13px, 0.06em tracking) run center-right; utility icons (search, account, cart) anchor the far right. Dropdowns render on `{colors.canvas}` with a 1px `{colors.hairline}` border and no shadow, deferring to the content inside. The nav has no brass accent until hover, where category labels shift to `{colors.primary}`.

### Product Card & Finishes

**`product-card`** — 4:3 image well on `{colors.surface-warm}` (the warm off-white makes chrome fixtures read warmer than on pure white). Product name in `{typography.title-md}`, price in Chronicle (`{typography.price}`), and a one-line descriptor in `{typography.body-sm}`. Border at rest is `{colors.hairline-soft}`; hover adds a 10px spread shadow in oiled-bronze tint and tightens the border slightly. Finish swatch row lives inside card padding below the descriptor.

**`finish-swatch`** — 24px circles at `{rounded.full}`, spaced 4px apart. Inactive state: no border. Active state: 2px `{colors.ink}` ring with 2px transparent gap between ring and swatch (CSS outline pattern). A tooltip in `{typography.caption}` surfaces the finish name on hover. The active ring being ink-dark rather than brass-primary keeps the selected state neutral and legible against any finish color including brass itself.

### Collection Hero

**`collection-hero`** — Full-bleed image with a 36% dark-bronze overlay (`{colors.ink-deep}` at 0.36 opacity), ensuring Chronicle display type reads in white on any photography. Heading at `{typography.display-xl}` (300 weight, −0.5px tracking), subhead at `{typography.body-md}` in `{colors.surface-linen}`. Minimum height 480px; padding 64px vertical, 32px horizontal. On mobile, heading drops to `display-md` scale and the overlay tightens to 44% to compensate for smaller safe text area.

### Filters & Wayfinding

**`room-filter-chip`** — Rectangular chips in uppercase Chalet (`{typography.label-uppercase}`), 4px radius, 1px `{colors.hairline}` border at rest. Active state: fills solid `{colors.ink}` with white text — a stark inversion that makes the active filter unmissable in a horizontal scroll row. Used for room-type filtering (Outdoor, Foyer, Kitchen, Bath) and collection filtering. On mobile, the row scrolls horizontally without wrapping.

**`promo-strip`** — A 36px-tall announcement bar in `{colors.ink-deep}` that lives above the nav-bar. Text in `{typography.label-uppercase}` at `{colors.surface-linen}`; inline links shift to `{colors.primary}`. Typically used for finish promotions, seasonal collections, or dealer events. Dismisses via an x icon at the far right; the nav-bar position shifts up to fill the vacated space.

### Labels & Badges

**`spec-badge`** — Small linen-background pill (`{colors.surface-linen}`, 1px `{colors.hairline}` border) containing safety and certification text in `{typography.spec-label}`. Groups of badges appear below the price on product detail pages: "UL Wet Rated," "UL Listed," "Title 24." The linen background links visually to the warm surface palette and avoids the alarm register of colored labels.

**`badge-new`** — Amber-filled (`{colors.accent-amber}`) label in uppercase Chalet, 3px top-left corner on product card image well. Uses `{colors.ink-deep}` text rather than white so the amber warmth reads against the near-black without flattening. `badge-bestseller` uses `{colors.primary}` fill with white text for clear hierarchy between the two states.

### Footer

**`footer`** — `{colors.ink-deep}` background anchored by a 3px brass top border (`{colors.primary}`) that serves as the single strongest brand-color moment in the page structure outside of CTAs. Column headings in `{typography.label-uppercase}` at `{colors.surface-warm}`; body links in `{colors.surface-linen}`, shifting to `{colors.primary}` on hover. Social icons render at 20px in `{colors.muted-light}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; filter chips scroll horizontally; collection hero heading drops to `display-md`; promo-strip stacks to two lines if needed; finish swatches reduce to 20px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only, no mega-menu; hero heading at `display-md`; room filter chips wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with dropdowns; hero at `display-xl`; filter chips single row with overflow hidden behind fade gradient |
| Wide | > 1440px | Four-column product grid; content max-width 1440px centered; hero image extends edge-to-edge while text container stays within max-width; footer columns expand to five |

### Touch Targets

- All filter chips minimum 44px tall via vertical padding expansion on mobile
- Finish swatches increase to 32px diameter on touch viewports with 8px gap
- Nav hamburger target 44×44px
- Cart and account icons padded to 44×44px tap targets even when icon renders smaller

### Collapsing Strategy

- Mega-nav dropdowns collapse to accordion drawers inside the mobile hamburger panel; category order matches desktop left-to-right
- Spec-badge groups wrap below price on mobile rather than truncating
- Product card price and spec badges collapse into a single line on narrow cards using flex-wrap
- Promo-strip hides on viewports below 375px if content exceeds one line; a minimal version with only the CTA link remains

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Chalet variant used as the primary UI weight is ambiguous — the font stack includes London1960, London1980, NewYork1960, NewYork1980, Paris1960, and Paris1980 variants; ChaletNewYork1960 is assumed based on mid-century American positioning but has not been confirmed from live CSS
- Chronicle variant (Display vs. Text grade) at body-adjacent sizes is unconfirmed; Chronicle Display is assumed for all heading use cases
- Hover and focus animation durations and easing curves could not be extracted
- Exact finish-swatch hex values for specific finishes (Polished Nickel, Oil Rubbed Bronze, Aged Brass, etc.) are not in the extracted palette and would require product-page inspection
- Mobile nav flyout color treatment (whether it uses `{colors.ink-deep}` or `{colors.canvas}`) is unconfirmed
- Whether the blue values (#1979c3, #006bb4) are Hinkley brand colors or Magento/platform defaults for links is ambiguous; they are mapped to `{colors.link}` only and kept out of the primary palette
- Icon system (SVG set, stroke weight, size grid) not extractable from static analysis
- Cart and wishlist empty/filled state color logic not confirmed
