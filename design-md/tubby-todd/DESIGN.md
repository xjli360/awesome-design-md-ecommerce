---
version: alpha
name: "Tubby Todd"
source_url: "https://tubbytodd.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bath-water amber — #f59e0b held at the saturated edge of honey — does almost all the emotional work on Tubby Todd's site. It is the announcement bar, the primary CTA, the star fill, the skin-concern selector's active state; the near-black ink stack (#141414 anchoring to #1f1f1f) and a cool near-white canvas recede entirely so that single warm frequency can register as safe warmth rather than commercial urgency. The secondary amber #fbbf24 appears in decorative fills and hover states, letting the palette breathe without introducing a second hue. Every typographic decision runs through Inter — no custom letterforms, no secondary face, no display serif to signal premium heritage — which is a deliberate wager: legibility at body scale matters more to a new parent speed-reading an ingredient list at 2 AM than typographic personality does. Inter at 700 weight in display sizes reads sturdy without hardness; at 400 weight in body copy it disappears, letting clinical ingredient claims and benefit callouts land without friction. {rounded.full} pill shapes govern primary CTAs and skin-concern filter tags, borrowing the same formal vocabulary as the product shapes — squeeze-tube nozzles, dropper bottles — while {rounded.md} product cards and ingredient callouts feel grounded and grid-stable. The overall spatial logic is generous: {spacing.section} vertical padding between content blocks keeps the page from reading dense or clinical even when ingredient lists and benefit badges stack. Sensitive-skin concern filtering appears as a row of amber-active / soft-surface-inactive pills — the only interface element using the primary color as a selection indicator rather than a purchase prompt, which trains the user to read {colors.primary} as "selected and safe" rather than "buy now." The footer inverts to the near-black #141414 field, a hard reset from the warm ambient temperature above the fold, anchoring navigation and legal copy without competing with product photography.

colors:
  primary: "#f59e0b"
  primary-active: "#d97706"
  primary-hover: "#e68a00"
  primary-disabled: "#fde68a"
  amber-soft: "#fbbf24"
  ink: "#141414"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-muted: "#e2e2e2"
  on-primary: "#141414"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Inter, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-xs:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.badge}"
    badgeRounded: "{rounded.full}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
    ctaSpacing: "{spacing.lg}"
  benefit-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  concern-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "8px 14px"
  concern-tag-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "8px 14px"
    border: "1px solid {colors.hairline}"
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    labelTypography: "{typography.label-xs}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.title-sm}"
  bundle-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    border: "1.5px solid {colors.hairline}"
    padding: "{spacing.xl}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    savingsBadgeBackgroundColor: "{colors.primary}"
    savingsBadgeTextColor: "{colors.on-primary}"
    savingsBadgeTypography: "{typography.badge}"
    savingsBadgeRounded: "{rounded.full}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    starColor: "{colors.primary}"
    starEmptyColor: "{colors.hairline}"
  divider:
    color: "{colors.hairline}"
    height: 1px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.section}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons

**`button-primary`** — Pill-shaped (#f59e0b fill, {rounded.full}, 48px tall) with dark ink text {colors.on-primary} rather than white, keeping WCAG contrast viable over the mid-luminance amber. Hover shifts to `{colors.primary-hover}` (#e68a00) to signal interactivity without a hue jump; active presses darken further to `{colors.primary-active}` (#d97706). Disabled state drains saturation to `{colors.primary-disabled}` (#fde68a) with muted text so unavailable actions read clearly without confusion.

**`button-secondary`** — White canvas fill with a 1.5px solid ink border and the same {rounded.full} pill geometry as primary, maintaining formal consistency across the CTA hierarchy. Hover fills the interior with `{colors.surface-soft}` (#f6f6f6), giving visible feedback without changing the border. Used for secondary actions like "Learn More" or "View All" where the amber primary would compete with product photography.

**`button-ghost`** — Transparent background, ink text, pill shape, smaller {typography.button-sm} scale. Used inside content blocks — testimonials, ingredient sections, editorial strips — where a bordered or filled button would feel heavy against already-dense content.

### Text Input

**`text-input`** — 48px tall, {rounded.sm} corners (8px), 1.5px hairline border at rest. Focus state upgrades the border to `{colors.ink}` so the active field is unmistakable even on a light {colors.surface-soft} background. Placeholder text runs in `{colors.muted}` (#545454) — light enough to be clearly secondary, dark enough to remain readable for users with low-contrast sensitivity.

### Navigation

**`nav-bar`** — White canvas, 64px tall, 1px bottom border in `{colors.hairline}` (#dedede) acting as a page-edge marker rather than a decorative element. Nav links use {typography.nav-link} at 14px weight 500 — notably smaller than typical DTC navbars — keeping the header spare and foregrounding the logo and search. A cart count bubble would carry `{colors.primary}` as its fill to extend the amber system into transactional UI.

**`announcement-bar`** — Sits above the navbar; full-bleed {colors.primary} (#f59e0b) fill with {typography.caption} centered text in `{colors.on-primary}`. Because amber occupies this premium screen-top position, it conditions users to read the color as "information from the brand" from first scroll.

### Product Card

**`product-card`** — {rounded.md} (12px) corners on both the card container and the product image, so the image shape rhymes with its wrapper rather than floating hard-edged inside a rounded frame. Title in {typography.title-sm} (15px/600), price in {typography.body-md} (16px/400) — price reads at the same scale as body copy, avoiding aggressive upsell signaling. Bestseller or "New" badges sit in the upper-left image corner using {rounded.full} pill geometry, {colors.primary} fill, {typography.badge} uppercase tracking.

### Hero Section

**`hero-section`** — {colors.surface-soft} (#f6f6f6) background rather than pure white, giving photography a lifted frame. Headline in {typography.display-xl} (44px/700), body copy in {typography.body-md} with generous 1.6 line-height for scan-reading. Vertical padding is {spacing.section} (64px) above and below, maintaining the open spatial tempo that separates Tubby Todd's editorial pace from discount DTC density.

### Skin Concern Tags

**`concern-tag-active`** / **`concern-tag-inactive`** — A horizontal pill-tag row lets users filter by skin concern (eczema-prone, dry skin, fragrance-free, etc.). Active selection fills with `{colors.primary}` amber; inactive tags sit on `{colors.surface-soft}` with a `{colors.hairline}` border and muted text. The amber fill here is the only place on the page where a non-CTA element uses the primary color, teaching users to read it as "this filter is on" — a subtle but useful UX convention.

### Benefit Badge

**`benefit-badge`** — Small pill ({rounded.full}) on `{colors.surface-soft}` with an uppercase {typography.badge} label (11px/700). Used to surface claims like "Pediatrician Tested", "EWG Verified", "Fragrance Free" beneath product titles or in a scarcity strip above the fold. The hairline border distinguishes these from the amber concern-tags so the two badge types don't compete visually.

### Ingredient Callout

**`ingredient-callout`** — A compact `{rounded.md}` tile on `{colors.surface-soft}` with a `{typography.label-xs}` uppercase category label (e.g., "KEY INGREDIENT") in `{colors.muted}` above a `{typography.title-sm}` ingredient name. Used in PDP ingredients sections and editorial landing pages to surface hero ingredients — colloidal oatmeal, sunflower oil — without building a full data table.

### Bundle Card

**`bundle-card`** — {rounded.lg} (20px) corners and a `{colors.hairline}` border frame the kit. A savings badge in `{colors.primary}` amber with {typography.badge} uppercase text and {rounded.full} sits in the upper corner. Title in {typography.display-sm} (22px/600), body copy in {typography.body-sm}. The amber accent recurs here as a commercial signal — one of the few places the brand allows the warm color to serve a purely transactional function.

### Testimonial Card

**`testimonial-card`** — {rounded.md} tile on `{colors.surface-soft}` with a 5-star row using `{colors.primary}` amber fill (empty stars default to `{colors.hairline}`). Quote text in {typography.body-md} with 1.6 line-height; author name and product name in {typography.caption} / `{colors.muted}`. The star color repeating the primary amber creates cohesion between review UI and the brand's core hue without requiring additional palette entries.

### Footer

**`footer`** — Hard inversion to `{colors.ink}` (#141414) background, a deliberate page-closing move that ends the warmth of the amber/soft-gray content zone. All text in `{colors.on-dark}` (#ffffff); section headings use {typography.title-sm}; links use {typography.body-sm} in `{colors.hairline-soft}` (#e2e2e2) to read as secondary without disappearing. {spacing.section} top and bottom padding maintains the generous spatial rhythm through to the page end.

### Search

**`search-input`** — Pill-shaped ({rounded.full}), 40px tall, `{colors.surface-soft}` fill with `{colors.hairline}` border. Sits inline in the nav or expands to a full-width overlay. Placeholder text in `{colors.muted}`; {typography.body-sm} keeps it compact within the 64px nav height.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to display-md (30px); nav collapses to hamburger icon + cart; announcement bar remains full-bleed; concern-tag row scrolls horizontally; benefit badges wrap to two lines |
| Tablet | 744–1128px | Two-column product grid; hero supports split image+text layout; nav expands to icon-row with abbreviated labels; bundle cards shift to 2-up grid |
| Desktop | 1128–1440px | Three-to-four column product grid; hero at full display-xl (44px) with large-format photography; nav fully expanded; concern-tag row fits single line without scroll |
| Wide | > 1440px | Max content width capped ~1400px, centered with canvas-color gutters; section padding increases proportionally; hero image zones grow without type scaling beyond 44px |

### Touch Targets

- All buttons minimum 48px height with {rounded.full} geometry — easy to tap anywhere along the pill width
- Concern-tag filters minimum 40px height with 14px horizontal padding to avoid mis-taps in scrolling rows
- Nav bar icons and links minimum 44×44px tap target even when visually smaller
- Cart and close icons in overlays padded to 48×48px tap zone

### Collapsing Strategy

- Navigation: desktop inline links → mobile hamburger drawer with full-height slide-in overlay on `{colors.canvas}` background
- Concern-tag row: desktop wraps freely → mobile becomes horizontally scrollable single-row strip with edge fade gradient
- Product grid: 4-col → 3-col → 2-col → 1-col at respective breakpoints; card padding reduces from {spacing.md} to {spacing.sm} on mobile
- Bundle cards: desktop 2-up → mobile full-width stacked with image above text
- Footer columns: desktop 4-column grid → mobile single-column accordion with `{colors.hairline}` dividers between sections
- Ingredient callout tiles: desktop 3-up row → mobile 2-up, truncating label to one line with ellipsis

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Inter is the default Shopify/system font stack; Tubby Todd may use a custom display face for hero headlines or wordmark that was not extractable from the computed styles
- No meta `theme-color` was set, so mobile browser chrome tinting preference is unknown
- Only nine hex values were extracted — brand likely uses additional tints (a soft peach or blush for baby girl SKU callouts, a sage or mint for natural/organic positioning) that did not surface in the top color extraction
- Illustration and icon style (whether the brand uses custom line-art icons or relies on generic Shopify icon sets) was not capturable
- Animation and transition preferences (easing curves, durations for hover states and drawer animations) are not derivable from static extraction
- Sale/discount badge color convention — whether a distinct red or secondary amber is used for sale pricing — was not confirmed
- Dark mode / high-contrast mode support status unknown
- Exact letter-spacing and weight variants used in the live announcement bar and product badge copy were not directly measured
