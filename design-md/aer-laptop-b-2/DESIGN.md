---
version: alpha
name: "Aer"
source_url: "https://www.aersf.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every primary call-to-action on aersf.com arrives as a rectangle of #000000 — not charcoal, not off-black, but a hard matte black that reads more like a stamped product spec than an invitation. The color story runs in compressed grayscale from white canvas through #f7f7f7, #f2f2f2, #e3e3e3, #d9d9d9, #959595, #707070, #575757, #404040, and #212121 before terminating at pure black — nine stops of extraction that strip the site of any warmth or decorative hue. Into that monochrome field arrives a single chromatic note: #d20000, a signal red reserved for sale pricing, urgency rails, and clearance badges, operating less as brand color and more as a binary flag for markdown. The font stack reaches for Helvetica Now Display — the 2019 optical overhaul of the Neue canon, wider and more optically consistent at large sizes — before falling back through the layered Helvetica Neue variants (Bold, Medium, LT Std 93) for body hierarchies. Weights are functional rather than expressive: display type at 700 carries the restraint of a specification label; body copy at 400 reads like a materials brief. Geometry follows the same logic: corners sit at {rounded.xs} and {rounded.sm} on inputs and cards, but the dominant shapes are near-zero-radius rectangles, as though curvature were a material cost the brand chose not to pay. Product photography occupies full-bleed modules shot against controlled white or neutral gray grounds, pack geometry treated with the same flat orthographic clarity as industrial product photography. The overall register is deliberate compression — every decorative variable removed until only function shows through, then rendered in black.

colors:
  primary: "#000000"
  primary-active: "#212121"
  primary-disabled: "#707070"
  accent: "#d20000"
  accent-active: "#651818"
  accent-surface: "#fff8f8"
  ink: "#212121"
  body: "#404040"
  muted: "#707070"
  muted-soft: "#959595"
  hairline: "#d9d9d9"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f2f2f2"
  surface-mid: "#f4f4f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#1f873d"
  success-surface: "#d3efcd"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-caps:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 16px 24px
    height: 52px
    width: 100%
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 15px 24px
    height: 52px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 15px 24px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-soldout:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
    touchSize: 28px
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-sale:
    saleColor: "{colors.accent}"
    originalColor: "{colors.muted-soft}"
    saleTypography: "{typography.price-sale}"
    originalDecoration: line-through
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    imageRatio: "16/9"
    mobileRatio: "4/5"
  feature-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 4px 8px
  sticky-atc:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    height: 80px
    typography: "{typography.title-sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 48px
    buttonWidth: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.title-sm}"
    rowBorder: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"

## Components

### Buttons

**`button-primary`** — A sharp-cornered black rectangle at 52px tall spanning the full container width on mobile and fitting content width on desktop. Typography is Helvetica Neue Bold at 14px, uppercase, with 0.5px letter-spacing — the label reads as specification, not call-to-action. Hover darkens to `{colors.primary-active}` (#212121); disabled state fills to `{colors.primary-disabled}` (#707070) with white text and pointer-events disabled. This button appears as the dominant "Add to Bag" CTA on every product detail page.

**`button-secondary`** — White fill with a 1px solid black border, matching primary in height and typography. Used for secondary product actions (gift wrapping, save for later) and in two-button stacks beneath primary CTAs. Hover may optionally shift background to `{colors.surface-soft}`.

**`button-ghost`** — Transparent fill with a 1px `{colors.hairline}` border and black text. Used in low-priority contexts — "View All", tertiary navigation actions — where visual weight must stay minimal against a white ground.

### Navigation

**`nav-bar`** — White ground with a light hairline bottom border at `{colors.hairline-soft}`. Logo sits left-anchored; primary category links (Bags, Accessories, Sale) are center or right-grouped at 14px/500 with no underlines. Cart icon and account link occupy the far right. Height is 64px. On scroll, bar becomes sticky and may add a subtle box-shadow. On mobile, collapses all links into a hamburger icon opening a full-height drawer.

### Product Elements

**`product-card`** — Zero-radius card on canvas white. Image sits in a `{colors.surface-soft}` square container at 1:1 ratio. Below, product name renders in `{typography.title-md}`, colorway label in `{typography.body-sm}` / `{colors.muted}`, and price in `{typography.price}`. Sale items show `{typography.price-sale}` in `{colors.accent}` (#d20000) with the original price struck through in `{colors.muted-soft}`. Badge stack (SALE, NEW, SOLD OUT) is pinned to the top-left corner of the image using `badge-sale` or `badge-new`.

**`badge-sale`** — A flat #d20000 no-radius rectangle, 3px × 6px padding, uppercase Helvetica Neue Bold at 11px/white. The only pure chromatic element on the grid — a hard interrupt that the brand deploys sparingly to signal markdown. No rounded corners, no shadow; legibility by contrast alone.

**`badge-new`** — Identical geometry to `badge-sale` but filled with `{colors.primary}` (#000000). Used for new arrivals and product launches. Because the card ground is also white, the black badge creates strong contrast without the urgency connotation of red.

**`badge-soldout`** — Same geometry filled with `{colors.muted}` (#707070). Communicates inventory state without the visual voltage of red or the priority of black. Often overlaid on a desaturated product image.

**`color-swatch`** — 20px circular dots in a horizontal row below product name. Active swatch carries a 2px solid black ring with 2px gap; inactive shows a 1px hairline ring. Swatch colors are the actual product colorway (black, slate, sand, etc.). Touch devices expand hit target to 28px. Used on cards (3–4 swatches max before truncation) and on the full product detail page.

**`price-display`** — Single price in `{typography.price}` at `{colors.ink}` for non-sale items. No label or context needed.

**`price-sale`** — Sale price in `{typography.price-sale}` at `{colors.accent}` (#d20000), followed by the original price at the same size with `text-decoration: line-through` and `{colors.muted-soft}` color. The red acts as a precise signal color here — the only place on a non-sale page where #d20000 appears.

**`hero-section`** — Full-bleed image module at 16:9 desktop, 4:5 mobile. Pack photography against controlled white or neutral gray grounds — no lifestyle blur, no atmosphere. Headline in `{typography.display-xl}` sits adjacent to or below the image rather than overlaid, preserving product clarity. No gradients or scrim overlays on product-focused heroes; editorial campaign images may use a light `{colors.scrim}` opacity mask.

**`feature-tag`** — Small near-square chip in `{colors.surface-card}` with a 1px `{colors.hairline}` border, 2px radius, `{typography.caption}` at `{colors.muted}`. Stacked or wrapped horizontally on product pages to call out weatherproofing, volume, carry weight, or material specs. Read more as data labels than marketing tags.

**`sticky-atc`** — Fixed viewport-bottom bar active on mobile product detail pages. White ground with 1px hairline top border. Left column shows condensed product name and selected options at `{typography.title-sm}`; right column holds a constrained "Add to Bag" button. 80px total height. Appears on downward scroll once the native ATC button exits the viewport, disappears on upward scroll.

**`quantity-selector`** — Three-part inline component: 48px-wide minus button (hairline border, `{rounded.none}`), center count display in `{typography.title-md}`, plus button. No border radius. Shares border language with `text-input`. Sits immediately above or beside `button-primary` on the product detail page.

**`spec-table`** — Two-column label/value grid for product dimensions, materials, and feature lists. Labels at `{typography.body-sm}` / `{colors.muted}` left; values at `{typography.title-sm}` / `{colors.ink}` right. Rows separated by a 1px `{colors.hairline-soft}` rule with `{spacing.md}` vertical padding. No outer border or background fill — the table sits directly on canvas white.

**`footer`** — Full-width black (`{colors.primary}`) footer with white text and `{colors.muted-soft}` links. Column headings in `{typography.label-caps}` (uppercase, tracked). Links in `{typography.body-sm}`. Legal text and social icons sit in a sub-footer row at the bottom of the black field. No card or border separation between sections — all text on flat black.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-height drawer; button-primary full-width; hero at 4:5 ratio; sticky-atc pinned to viewport bottom; spec-table full-width stacked |
| Tablet | 744–1128px | 2-column product grid; nav expands to show primary category links inline; hero at 16:10; sticky-atc persists on product detail |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with possible mega-menu dropdown; hero full-bleed 16:9; sticky-atc desktop-only if scroll depth warrants |
| Wide | > 1440px | Content max-width capped at ~1440px centered; hero bleeds edge-to-edge with text column constrained inside grid; footer columns evenly distributed at wider gutter |

### Touch Targets

- All interactive elements minimum 44×44px per platform guidelines
- Color swatches expand hit target to 28px on touch without changing visual size
- Nav links carry 48px touch height via vertical padding expansion
- Quantity selector minus/plus buttons 48px × 48px minimum
- Badge chips non-interactive; no touch target requirement

### Collapsing Strategy

- Navigation: full horizontal link row collapses to hamburger icon below 744px; mega-menu panels replaced by full-height side drawer with accordion category sections
- Product grid: 4-col → 3-col (1128px) → 2-col (744px) → 1-col (< 744px)
- Hero layout: side-by-side image + text collapses to stacked image-above, text-below below 744px
- Footer: multi-column link grid collapses to single-column accordion sections on mobile; social icons move to sub-footer row
- Spec tables: two-column label/value layout remains on all breakpoints; table width shrinks with container

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific custom typeface confirmed; Helvetica Now Display is a licensed font and may not load consistently; fallback to Helvetica Neue is highly likely for most visitors
- Border-radius values are inferred from brand aesthetic (near-zero) — no direct CSS extraction confirmed
- Exact navigation height (64px estimated) and sticky-scroll trigger threshold not confirmed
- Mega-menu structure and hover/focus states for category dropdowns not extracted
- Animation and transition durations not available (likely 150–200ms ease on interactive states given brand restraint)
- Product page tab design (Overview, Features, Specs, Carry Guide) active/inactive color states not confirmed
- Dark-background variant (black hero with white text) state handling not extracted
- Mobile menu drawer animation direction and overlay opacity not confirmed
- Exact image aspect ratios for product cards (estimated 1:1) not confirmed
