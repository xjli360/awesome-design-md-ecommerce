---
version: alpha
name: "Beached"
source_url: "https://beached.shop"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Salt-lifted hair — the kind that dries into effortless texture after an afternoon in the surf — is what Beached sells, not a product category but a post-ocean feeling that most haircare brands only gesture at. The palette reads like a tidal strip at low tide: warm cream canvas #FDFAF5 where the dry sand begins, ocean teal #3D8F8F at the waterline where all primary brand energy lives, and deep driftwood ink #2C2416 carrying the reading work so the primary never feels overused. No harsh chrome, no clinical white — the system breathes at low contrast before the teal arrives on a CTA, a price callout, or an active nav state. Coral #E87B5A appears only on urgency markers: new-arrival badges, sale tags, the single warm accent in an otherwise cool-neutral field. Cards sit at {rounded.md} corners, reading like a sun-worn edge rather than an engineered corner; only the search pill and filter chips break into {rounded.full}, the one place the system allows a fully resolved curve. Type runs at unassuming weights — display headings at 600 rather than 800, body copy at a loose 1.6 line-height — because the copy does the mood-setting through ingredient origin stories and surf-report pacing rather than typographic muscle. Spacing is generous throughout: section breaks at {spacing.section} push content into breathing sequences that feel like walking from one tide pool to the next. The footer drops onto a warmer sand surface #EDE6DA rather than a stark dark band, keeping the register warm even in the bottom third. Collection headers use a sand wash #C4A882 as a background tone, while ingredient-focused callouts layer sea-foam #B8D9D4 behind the panel. The overall system sits at the intersection of beach-lifestyle ease and the precision that premium haircare demands: effortless without being careless.

colors:
  primary: "#3D8F8F"
  primary-active: "#2D7272"
  primary-disabled: "#A8CFCF"
  ink: "#2C2416"
  body: "#4A3E30"
  muted: "#8A7B6A"
  hairline: "#D4C8B8"
  canvas: "#FDFAF5"
  surface-soft: "#F5EFE4"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  sand: "#C4A882"
  coral: "#E87B5A"
  sea-foam: "#B8D9D4"
  footer-surface: "#EDE6DA"

typography:
  display-xl:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Inter', 'DM Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
    priceTypography: "{typography.price}"
    nameTypography: "{typography.title-sm}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: button-primary
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    textBlockMaxWidth: 560px
  ingredient-badge:
    backgroundColor: "{colors.sea-foam}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  new-arrival-badge:
    backgroundColor: "{colors.coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  collection-header:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  rating-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 12px
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.footer-surface}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA renders in ocean teal (#3D8F8F) at 48px height on {rounded.md} corners, with 600-weight button type at 15px. Active state deepens to #2D7272 via a direct color swap with no shadow or lift effect; disabled state bleaches to the pale sea-foam #A8CFCF, keeping the same geometry so layouts never reflow. Use for Add to Cart, Checkout, and primary form submissions.

**`button-secondary`** — Same 48px height and {rounded.md} corner as primary, filled with {colors.canvas} and enclosed by a 1.5px {colors.hairline} border. Ink text (#2C2416) keeps the label legible without competing with the primary color. Use for Save, View Collection, or secondary modal actions where the primary button already owns the strongest CTA.

**`button-ghost`** — Transparent fill with {colors.primary} teal text, no border. Reserved for inline editorial contexts — "Read the full story", ingredient expand links — where a full button would impose too much visual weight on a content-heavy layout.

### Search

**`search-bar`** — Pill-shaped ({rounded.full}) at 44px height, filled with the warm {colors.surface-soft} cream. The pill is the brand's single signature curve, kept exclusive to search and filter chips so its shape carries unambiguous meaning. On focus the border shifts from {colors.hairline} to {colors.primary} teal. Placeholder text runs in {colors.muted} (#8A7B6A).

### Navigation

**`nav-bar`** — 64px tall on canvas (#FDFAF5) with a 1px {colors.hairline} bottom border. Logo anchors left at 32px height; primary nav links run centered in {typography.nav-link} (14px / 500 weight); cart icon and account link anchor right. After scrolling past 80px the bar receives a subtle box-shadow (0 2px 8px rgba(44,36,22,0.08)) to signal elevation above content without changing background color.

### Product Card

**`product-card`** — 4:5 image crop with a {rounded.md} clip, product name in {typography.title-sm} (15px / 600), price in {typography.price} (18px / 700), and an 8px gap between all text elements. Cards sit on white {colors.surface-card} with no drop shadow — grid gutters and image edges do the visual separation. A {colors.coral} new-arrival badge pins absolute top-left over the image when the product qualifies.

### Badges

**`ingredient-badge`** — Sea-foam (#B8D9D4) pill on {rounded.full} with uppercase 11px / 700 lettering in {colors.ink}, 6px top/bottom and 14px side padding. These tag ingredient callouts (e.g., "Sea Kelp", "Salt Minerals", "Coconut Oil") on product and editorial pages, functioning as scannable flavor notes rather than navigation or filter controls.

**`new-arrival-badge`** — Coral (#E87B5A) rectangle on {rounded.xs} with uppercase 11px / 700 white text. The only warm element in the system; its rarity is load-bearing — it signals genuinely new inventory without crying wolf across every card. Appears as an absolute-positioned overlay pinned to the image top-left corner.

### Collection Header

**`collection-header`** — Full-width band in {colors.sand} (#C4A882), headline in {typography.display-md} (32px / 600), body copy below in {typography.body-md}, padded at {spacing.xxl} vertical and {spacing.xl} horizontal. No rounded corners — the edge-to-edge band creates a deliberate horizon-line break between content zones, mimicking a shoreline transition rather than a boxed content module.

### Hero Banner

**`hero-banner`** — Built on {colors.surface-soft} (#F5EFE4) or a full-bleed product/lifestyle image with a translucent warm scrim overlay. Headline in {typography.display-xl} (48px / 600 / -0.5px tracking), body copy in {typography.body-md} beneath, followed by a button-primary CTA. Minimum height 560px on desktop so imagery has room to breathe rather than being heavily cropped. Text block aligns left with a 560px max-width cap to preserve comfortable line lengths.

### Promo Banner

**`promo-banner`** — A 40px teal strip ({colors.primary}) pinned at the very top of the viewport, above the nav. White caption-weight text is centered horizontally, carrying a free-shipping threshold or limited-time offer message. Sits fixed on scroll on desktop; on mobile it scrolls away with the page after the first viewport height to recover screen space.

### Rating Chip

**`rating-chip`** — Compact pill on {rounded.full} with {colors.surface-soft} fill, carrying a star glyph followed by a numeric average in {typography.caption} (12px / 500). Appears below the product name on cards and inline on the PDP near the price block. No border — the warm tint fill alone separates it from the white card background.

### Footer

**`footer`** — Warm sand surface (#EDE6DA) keeps the footer in the tan register rather than going dark. Section headings in {typography.title-sm} (15px / 600), body links in {typography.body-sm} (14px / 400) at {colors.ink}. Four-column grid on desktop collapses to two on tablet. Social icon row sits at the base using 24px stroke icons in {colors.muted} (#8A7B6A). No black background — the warm landing closes the page in the same sand family that runs through the collection-header banding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen drawer; hero min-height reduces to 420px; hero body copy hides below 375px if needed to prevent overflow; collection-header padding drops to {spacing.lg} vertical; promo banner scrolls with page |
| Tablet | 744–1128px | Two-column product grid; nav visible with condensed label spacing; hero text block max-width 420px; footer collapses to two columns; promo banner remains fixed |
| Desktop | 1128–1440px | Three- or four-column product grid depending on collection size; full nav bar with all links and icons visible; hero text block 560px max-width; four-column footer |
| Wide | > 1440px | All content constrained to 1320px max-width container centered on page; hero image uses a wider crop region but text block stays at 560px; grid gutters expand proportionally |

### Touch Targets

- All interactive elements minimum 44×44px on mobile; buttons at 48px height already satisfy this
- Product card tap target covers the full card surface, not just the image or title
- Nav hamburger icon padded to a minimum 44×44px tap area even if the visual glyph is smaller
- Ingredient and new-arrival badges are decorative at mobile breakpoint; no required tap action
- Rating chips are read-only display elements; no tap target requirement

### Collapsing Strategy

- Nav: hamburger drawer at < 744px; full horizontal link row at ≥ 744px
- Hero: headline drops from display-xl (48px) to display-md (32px) on mobile; body copy conditional hide below 375px viewport width
- Product grid: 1-column mobile → 2-column tablet → 3–4 column desktop
- Collection-header: headline stays at all breakpoints; body copy may truncate to two lines on mobile
- Footer: 4-column → 2-column → 1-column stacked; each column becomes an accordion section on mobile with chevron toggle
- Promo banner: fixed on desktop and tablet; scrolls away on mobile after initial viewport to recover vertical space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from beached.shop — the site appears to load design tokens via JavaScript or sits behind anti-bot protection. All palette values in this file are brand-knowledge estimates based on the brand name, slug, and haircare category conventions; treat as provisional until live-site extraction succeeds.
- No font families were detected. Typography assignments (Inter / DM Sans) are category-appropriate system defaults, not confirmed brand fonts. The actual brand may use a licensed or custom typeface not detectable via static extraction.
- No meta theme-color tag was found, which typically signals either a JS-driven token system or a non-PWA Shopify build with no native browser chrome coloring.
- Logo mark style — wordmark vs. icon, serif vs. sans, hand-drawn vs. geometric — is unconfirmed. The design system assumes a clean sans wordmark consistent with the brand name.
- Icon style (stroke vs. filled, weight) is unconfirmed; the system assumes a lightweight stroke icon set at 20–24px.
- Motion and animation specs (hover transition durations, scroll-triggered reveal easing, add-to-cart micro-animations) are entirely absent and must be confirmed from live site inspection or brand guidelines.
- Exact border-radius values are estimated at {rounded.md} (12px) for cards and inputs; the actual brand radius may differ.
- Product photography art direction (flat-lay vs. lifestyle, color grade temperature) is assumed warm and lifestyle-oriented based on the brand name, but is not confirmed.
