---
version: alpha
name: "Skagen"
source_url: "https://www.skagen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Skagen compresses its entire visual argument into a single contrast decision — charcoal #313131 pressed against an unbroken white field, every gram of interface chrome removed so the watch face fills the frame unopposed. The edit is thorough: no accent colors, no decorative gradients, no shadow lifting a card above its ground — the UI surface is negative space that makes product photography the only event on screen. Display type runs at weight 300 on hero headings, genuinely lightweight rather than marketing-lightweight, so the letterforms don't compete with the product; captions and labels retreat further still, tracking wider to hold legibility at low weights across a monochromatic field. The brand's only chromatic voltage comes from photography — warm brass cases against pale wrists, mesh bracelets catching studio light — which makes the interface deliberately recessive, never competing with the object it presents. Buttons use full charcoal fill rather than a distinctive brand color, making every CTA read as a stamped decision rather than a glowing affordance. Corners are sharp to near-sharp ({rounded.none} to {rounded.xs}), reinforcing the same formal vocabulary as the watch case edges themselves — no soft rounding anywhere, just the clean geometry of a manufactured object. Navigation is a single horizontal bar with no visual weight: white ground, fine hairline bottom rule, text-only links — it collapses into a hamburger at mobile without ceremony. Product cards show a square-cropped image, watch name in tracked uppercase, price in regular weight, with no border or shadow; the white canvas is the container. Spacing is generous and even: content bands breathe at {spacing.section}, card siblings at {spacing.xl}, so the catalog reads like a curated lookbook. The entire system is a study in suppression — trust the object, disappear the wrapper.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9e9e9e"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  caption-uppercase:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 1.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.3px
  price:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  label-tag:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.6px
    textTransform: uppercase

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    nameLine: "{typography.title-sm}"
    priceLine: "{typography.price}"
    gap: "{spacing.sm}"
  product-card-hover:
    imageSwap: "alternate product angle"
    quickAddButton: "button-primary at card bottom, full-width"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    layout: "full-bleed image with left-aligned or centered text overlay"
    minHeight: 560px
  hero-split:
    layout: "50/50 image-left text-right"
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-tag}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.ink}"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  price-display-sale:
    saleTypography: "{typography.price-sale}"
    saleColor: "{colors.ink}"
    originalDecoration: line-through
    originalColor: "{colors.muted}"
  strap-selector:
    swatchSize: 24px
    swatchRounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  watch-size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    padding: "{spacing.sm} {spacing.base}"
    minHeight: 36px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.caption-uppercase}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"
  newsletter-input:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    border: "none"
    borderBottom: "1px solid {colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
    placeholderColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — Full charcoal (#313131) fill with white tracked-uppercase type at 13px weight 500. Skagen avoids all border radius ({rounded.none}), so the button reads as a flat rectangular stamp — the same formal decision as the watch case geometry. Active state deepens to #1a1a1a; disabled mutes fill to #9e9e9e without changing shape. Padding extends to 32px horizontally to create a wide, unhurried CTA footprint that suits a premium positioning.

**`button-secondary`** — White canvas with a 1px charcoal stroke and identical tracked-uppercase label. It mirrors button-primary's flat geometry and type treatment exactly; the only distinction is fill versus stroke. Active state adds {colors.surface-soft} tint on the interior without breaking the monochromatic logic. Used for secondary CTAs on split heroes and detail pages where the full-black button would dominate.

**`button-ghost`** — Transparent background with underlined ink text in button-md tracking. Reserved for tertiary actions — "View All," "Learn More" — where a bordered button shape would distract from surrounding imagery. No border, no background shift on hover beyond cursor change.

### Navigation

**`nav-bar`** — A 60px white bar with a single 1px {colors.hairline} bottom rule providing the only structural line on the page. Wordmark sits left; top-level category links span the center in 13px nav-link type; search, bag, and account icons align right. No background color shifts on hover — just a subtle underline or weight change on the active item.

**`nav-dropdown`** — A full-width mega-panel that drops below the hairline on white ground. Subcategory links render in {typography.body-sm} in a multi-column grid; an editorial campaign image often occupies the right column. Padding is {spacing.lg} vertical, {spacing.xl} horizontal. The panel lifts into view without animation lag — immediacy over choreography.

### Product Card

**`product-card`** — Square-cropped 1:1 image on white ground with no border, shadow, or container shell. Watch name renders below in {typography.title-sm} (13px tracked uppercase), price in {typography.price} (16px regular). On hover, the primary image swaps to an alternate angle and a full-width `button-primary` Quick Add emerges at the card bottom. Padding is minimal ({spacing.sm}) — the white canvas is the container, not a card shape.

### Hero

**`hero`** — Full-bleed photography at minimum 560px height with headline overlaid in {typography.display-xl} weight 300. Text overlay is left-aligned or centered in white against dark photography; for studio-lit imagery with pale backgrounds, charcoal ink is used instead. The single CTA is always `button-primary`. No decorative overlays, gradient scrims, or typographic embellishment — image and label only.

**`hero-split`** — A 50/50 split at desktop: product photography left, editorial copy and CTA right on {colors.surface-soft} ground. Headline at {typography.display-md} weight 300; used for new collection introductions and seasonal drops. Collapses to stacked image-above-text at tablet and below.

### Filters and Selectors

**`collection-filter`** — Flat rectangular chips in {typography.caption-uppercase} (11px, 1.4px tracking). Inactive: white fill with 1px {colors.hairline} border and charcoal label. Active: charcoal fill with white label. No radius ({rounded.none}), consistent with the button vocabulary. Chips lay in a horizontal scroll row at mobile; wrap to a multi-row grid at desktop.

**`strap-selector`** — 24px circular color swatches indicating interchangeable strap options. Unselected: 1px {colors.hairline} border; selected: 2px {colors.ink} border. Swatches are spaced at {spacing.sm} and render inline on the product detail page beneath the size selector row.

**`watch-size-selector`** — Flat rectangular chips ({rounded.none}) in {typography.body-sm}. Inactive: white fill, 1px hairline border. Selected: {colors.ink} fill, {colors.on-primary} text. Minimum chip height 36px with {spacing.sm} gap between options; touch target padding ensures 44px tappable area.

### Badges

**`badge-new`** — Charcoal fill, white {typography.label-tag} uppercase text (10px, 1.6px tracking), zero radius. Sits absolutely positioned at the top-left corner of the product card image area. Discrete enough not to compete with the product image while legible at catalog scale.

**`badge-sale`** — White fill with 1px charcoal border and charcoal {typography.label-tag} text. Visually distinct from `badge-new` (outline vs. fill) without introducing a secondary color. Used on cards when a discount price is active alongside the struck-through original.

### Search

**`search-overlay`** — A full-width panel descending from the nav bar with a bottom-border-only text input in {typography.body-md}. No rounded corners, no box shadow — the panel extends the white canvas downward. Real-time results populate a product grid below the input line. Closes on outside click or Escape with no exit animation.

### Footer

**`footer`** — Full charcoal (#313131) fill, inverting the canvas cleanly. Column headings in {typography.caption-uppercase} (white); link lists in {typography.body-sm} at reduced opacity. Newsletter sign-up uses a bottom-border-only input on charcoal ground — avoiding an enclosed form shape that would read as a foreign element. Social icons are white SVG at 20px. The footer functions as the single large dark band on the page, bookending the white editorial experience.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark + bag icon; hero headline drops to {typography.display-sm}; collection filters become horizontal scroll row; hero text moves below image crop |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level text links only, no mega-dropdown; hero at {typography.display-md}; split-hero stacks image above text |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-nav dropdown with editorial column; hero at {typography.display-xl}; split-hero 50/50 activates |
| Wide | > 1440px | Grid caps at ~1440px centered; side gutters expand with white space; hero photography extends full-bleed behind centered content column |

### Touch Targets
- All interactive controls minimum 44×44px on mobile
- Watch size selector chips minimum 44×36px with 8px gaps between
- Strap swatches 24px visual diameter wrapped in a 44px tap target
- Nav icons 44×44px regardless of SVG visual size
- Filter chips minimum 36px tall with 8px horizontal gaps

### Collapsing Strategy
- Mega-nav collapses to left-sliding drawer at < 744px with accordion category expansion on tap
- Hero CTA moves below image on mobile; overlay text removed to avoid legibility issues on small crops
- Footer accordion at mobile — column headings are tappable toggles; links hidden until expanded
- Product card Quick Add hidden at mobile; tap navigates directly to PDP
- Split-hero stacks image-above-copy at tablet and below, with copy block padding reduced to {spacing.lg}

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color extracted (#313131); full palette including any accent colors for seasonal campaigns, hover states, or promotional elements could not be confirmed from live extraction — site was behind a Cloudflare anti-bot challenge at scrape time
- No brand font names captured; extraction returned only system font stacks (-apple-system, Roboto, Helvetica Neue, etc.). Skagen likely uses a licensed geometric or humanist sans-serif on live pages; the Helvetica Neue stack used here is an inference from the brand's established aesthetic
- Exact button border-radius value unconfirmed; {rounded.none} is inferred from brand formal vocabulary but may be {rounded.xs} (2px) in implementation
- Meta theme-color is absent — no mobile status-bar color preference confirmed
- Dark-mode palette completely unknown
- Navigation height (60px), dropdown timing curves, and animation easing values not confirmed
- Sale or promotional accent color (if any exists) not captured — palette may include a red or warm tone for discounts that did not appear in extraction
