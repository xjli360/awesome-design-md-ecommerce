---
version: alpha
name: "Kinn Studio"
source_url: "https://kinnstudio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The most unusual decision in Kinn Studio's visual system is pairing a deep petrol-teal primary — #012e36, the near-black of a freshly struck hallmark stamp — against a warm parchment ground (#f9f5ec, #f0e6d9) that reads like unbleached cotton or the tissue paper inside a gift box. This is not the gold-on-white of conventional fine jewelry retail; it is closer to opening a green-velvet presentation tray under gallery lighting. Type divides into two distinct registers: Quarto Light and Cormorant carry all editorial display weight, their bracketed serifs giving every headline the gravity of a foundry document, while Neue Haas Grotesk handles the interface layer — navigation, pricing, form labels — in quiet uppercase tracking at modest weights. York Script ES materializes only as a calligraphic gesture, a signature flourish above a collection name or pull-quote, never at small sizes. The coral-red accent (#e93f2c) is used with economy: sale prices, countdown timers, occasional badges, appearing just enough to create voltage without competing with the warm golds and silvers of the jewelry photography itself. Corners are largely eliminated — primary CTAs, product cards, and grid tiles all sit at {rounded.none}, communicating quality print and editorial standards rather than consumer-app friendliness. The one notable exception is filter chips, which use {rounded.full} to differentiate them as interactive selectors within an otherwise flat visual field. Spacing across sections is wide and unhurried, with editorial breathing room at {spacing.section} and beyond, reflecting a curatorial pace that asks the visitor to linger. The deep-teal footer and navigation bar frame the warm interior like a bookbinding, closing the experience with the same #012e36 that anchors the brand mark — the tagline "Modern legacy — then, now, always" made structural.

colors:
  primary: "#012e36"
  primary-active: "#002026"
  primary-disabled: "#a8c0c4"
  ink: "#121212"
  body: "#393939"
  muted: "#7a7470"
  hairline: "#dedede"
  hairline-soft: "#eae6e3"
  canvas: "#f9f5ec"
  surface-soft: "#f6f4f0"
  surface-card: "#f1eee8"
  surface-warm: "#f0e6d9"
  on-primary: "#ffffff"
  accent-coral: "#e93f2c"
  accent-rust: "#623529"
  error: "#ec0000"
  success: "#1a8000"

typography:
  display-xl:
    fontFamily: "'Quarto Light', 'Cormorant', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Quarto Light', 'Cormorant', Georgia, serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant', 'Quarto Light', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  script-accent:
    fontFamily: "'York Script ES', cursive"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em
  badge:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  kr-accent:
    fontFamily: "'Noto Serif KR Medium', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    borderBottom: "1px solid {colors.ink}"
  icon-button-circle:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    size: 40px
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    typography: "{typography.body-md}"
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 52px
    borderBottom: none
  nav-announcement:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
    hoverReveal: "quick-add button overlaid at image bottom"
  product-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    position: "top-left"
  hero-editorial:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 560px
    paddingX: "{spacing.xxl}"
    ctaVariant: "button-secondary-on-dark"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    layout: "50/50 image-left text-right"
    imageObjectFit: cover
    ctaVariant: "button-ghost"
  script-headline:
    typography: "{typography.script-accent}"
    textColor: "{colors.primary}"
    display: block
    marginBottom: "{spacing.base}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    labelPaddingTop: "{spacing.sm}"
  filter-chip:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    saleColor: "{colors.accent-coral}"
    strikethroughColor: "{colors.muted}"
    layout: "sale-price then strikethrough inline"
  swatch:
    size: 20px
    gap: "{spacing.xs}"
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    selectedOffset: 2px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    columnCount: 4
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — sharp-cornered ({rounded.none}), deep teal (#012e36) fill, white uppercase Neue Haas Grotesk at 13px with 0.12em tracking. Hover darkens to #002026; disabled renders in the desaturated teal (#a8c0c4). Height is 48px across all breakpoints. The absence of radius is intentional — it reads like a quality label or embossed stamp rather than a digital button.

**`button-secondary`** — transparent fill with a 1px #012e36 border, same uppercase tracked type in {colors.primary}. Used alongside a primary CTA on warm canvas backgrounds. On dark teal hero backgrounds, the variant swaps to white text and white border (`button-secondary-on-dark`).

**`button-ghost`** — text only, no box, with a 1px bottom border underline in {colors.ink}. Appears as inline editorial CTAs ("Shop the collection", "See all") within prose sections and product grids. No padding box, no hover fill — only the underline reacts on hover.

### Navigation

**`nav-bar`** — 52px bar in {colors.primary} (#012e36), reversing all type and icons to white. Nav links at 13px uppercase Neue Haas Grotesk, 0.06em tracking. Cart, search, and account icons render at 24px with 44×44px minimum hit targets. On scroll, the bar remains fixed with no shadow or border change — the deep teal is opaque enough to read above all canvas backgrounds.

**`nav-announcement`** — 36px strip anchored above the main nav in the same {colors.primary}, white {typography.caption} type centered. Used for free-shipping thresholds, new-collection teasers, and limited-time promotions. Never uses the coral red for background; urgency is expressed through copy alone.

### Product Card

**`product-card`** — flat, shadowless, square-cropped image (1:1 ratio) on a warm off-white ground ({colors.surface-card}, #f1eee8). Product name in {typography.body-sm}, price in {typography.price-display} directly below. On hover, a quick-add CTA overlays the bottom quarter of the image as a teal button. `product-badge` (NEW, SALE, SOLD OUT) pins top-left in coral (#e93f2c) with no radius and all-caps badge type.

### Hero Modules

**`hero-editorial`** — full-width deep-teal block (#012e36), white display type in Quarto Light or Cormorant at {typography.display-xl}. Minimum 560px tall; the CTA renders as `button-secondary-on-dark` (white-outlined). Photography may bleed into the left or right half but the text area always sits on solid teal, never on a busy image.

**`hero-split`** — 50/50 grid on {colors.canvas}: left panel is full-bleed photography with cover fit, right panel carries a Cormorant headline at {typography.display-lg} and a ghost CTA. This layout appears for collection launches and editorial stories. The `script-headline` component often sits above the Cormorant title as a York Script ES accent line.

### Typography Components

**`script-headline`** — York Script ES at 28px in {colors.primary}, displayed as a block-level element above Cormorant display headings. Purely editorial: found on collection landing pages and homepage editorial modules. Never used in UI, PDPs, or navigation.

**`section-header`** — Cormorant 32px regular in {colors.ink}, used as the title for collection grids, editorial modules, and content blocks. Centered or left-aligned depending on the grid layout. Wide bottom margin ({spacing.lg}) before the content begins.

### Filtering & Swatches

**`filter-chip`** — hairline-bordered ({colors.hairline}) rounded-full pills on {colors.canvas}. Active state fills in {colors.primary} with white type — the teal chip against the warm ground creates clear selection contrast. Typography is {typography.caption}, 12px. Chips scroll horizontally on mobile.

**`swatch`** — 20px circles, {rounded.full}, separated by {spacing.xs}. Selected state draws a 2px {colors.ink} border offset by 2px, visible as a ring around the active color. No label unless the color name appears below the swatch group.

### Pricing

**`price-tag`** — regular price in {colors.ink} at {typography.price-display}. When discounted, the sale price appears first in {colors.accent-coral} (#e93f2c) and the original price follows as a strikethrough in {colors.muted}, both inline. No surrounding badge is needed if the color split is already visible.

### Footer

**`footer`** — full-width {colors.primary} block mirroring the nav header, completing the bookbinding frame. Four-column link grid in white {typography.body-sm}; legal and policy text at {typography.caption} with reduced opacity. Social icons are white at 20px. The warm interior of the page is thus literally enclosed top and bottom in the same deep teal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + full-screen teal overlay drawer; hero headline drops to {typography.display-md}; section padding reduces to {spacing.lg}; filter chips become a horizontal scroll strip; script-headline hidden to preserve legibility hierarchy |
| Tablet | 744–1128px | Two-column product grid; hero-split stacks vertically (image top, text below); nav shows primary links only with secondary links in overflow menu; hero-editorial maintains full height |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with mega-menu dropdown; hero-split renders 50/50 side by side; script-headline visible at full 28px |
| Wide | > 1440px | Max content width 1440px with auto outer margins; hero imagery expands edge-to-edge; grid remains at 4-col; typography sizes unchanged |

### Touch Targets
- All nav icons (cart, search, hamburger) maintain a 44×44px minimum touch target regardless of icon visual size
- Swatch circles are 28px tappable area on mobile, regardless of the 20px visual size
- Filter chips expand padding to 10px 20px on mobile for easier one-handed tapping
- Add-to-cart button expands to full-width on mobile PDP sticky bar
- Ghost button underline-only treatment gets a 44px minimum tap height on mobile

### Collapsing Strategy
- Navigation: full horizontal bar with links → hamburger icon with full-screen teal drawer; drawer uses the same #012e36 background as the desktop bar
- Hero: hero-editorial (dark-teal full-bleed) remains full-width at all breakpoints with no structural change; hero-split collapses to single column (image stacked above text) below 744px
- Product grid: 4-col → 3-col → 2-col → 1-col descending through breakpoints
- Footer: 4-col link grid → 2-col → vertically stacked accordion sections on mobile
- Script-headline decorative type hidden below 744px; the Cormorant heading stands alone without the York Script accent

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Noto Serif KR Medium appears in the font stack, suggesting Korean-language support or localization; its specific usage context (full Korean locale, CJK product names, editorial accent) was not determinable from extraction alone
- Hover micro-animation timing (transition durations, easing curves) for product-card reveal, button state changes, and nav dropdowns not extracted
- Mega-menu dropdown structure (column count, whether a featured editorial image panel is included) not confirmed from extraction
- Cart drawer / slide-out panel styling inferred from Shopify conventions; not directly verified
- PDP layout details — image carousel behavior, accordion sections for product details/sizing/materials, sticky add-to-cart bar behavior — not confirmed
- Exact weight distribution between Quarto Light and Cormorant (which headlines use which face) not fully resolved from extraction; both appear as display-register serifs
- `primary-disabled` (#a8c0c4) is a derived intermediate teal, not directly extracted from the palette
- `muted` (#7a7470) is a derived warm gray; no explicit mid-gray was present in the extracted color list
- Whether #623529 (accent-rust) appears as a text color, a material swatch color, or only in photography tone was not determinable
