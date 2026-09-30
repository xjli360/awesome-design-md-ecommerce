---
version: alpha
name: "Varmilo"
source_url: "https://www.varmilo.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Varmilo's site treats every keyboard as a collectible art print before it treats it as an input device — keycap legends read like calligraphy strokes, and the product page leads with a full-bleed photograph before any switch spec. The brand voltage is #fb637e, a warm coral-rose that appears on CTA buttons, price highlights, and sale badge fills; it reads as joyful rather than urgent, more flower-market than clearance rack. A secondary warm gold (#c79b68) surfaces on premium listings and limited-edition badge fills, drawing a collector's tier line without requiring a separate sub-brand. The canvas is a layered neutral-gray system — #f5f5f5 as page ground, #eeeeee and #e8e9eb for card surfaces, fine hairlines at #dedede — that keeps photographed keyboards visually dominant rather than the surrounding chrome. Dark ink sits at #222222 and #11151c, dense enough to read cleanly against those light-gray grounds without needing maximum contrast. Type runs in Dosis, a geometric sans-serif with slightly rounded terminals that echoes the soft keycap corners visible in every product shot; button labels and section headers carry fontWeight 600 at subdued tracking, while display sizes stay modest (28–32px) so the keyboard photograph always dominates the composition. Interaction radii lean gently rounded: buttons use {rounded.sm} (8px), cards use {rounded.md} (12px), and pill badges on limited editions push to {rounded.full}. Spacing is generous at the product-card level — {spacing.lg} internal padding lets keycap photography breathe. Navigation is restrained: a slim bar in {colors.body} or a near-black dark variant (#11151c for collection hero pages), Dosis at 14px/600, category tabs with an active coral underline, and a magnifier for the search overlay. The footer deepens to near-black (#121212) and drops font weight to 400, a quiet base beneath the color-active product grid. The overall effect is a keyboard museum with a gift-shop counter — methodical grid, deliberate coral accent, gold tier-marking, and a typeface whose rounded strokes nod to the physical object it is selling.

colors:
  primary: "#fb637e"
  primary-active: "#e04060"
  primary-disabled: "#fdc4cc"
  accent-gold: "#c79b68"
  accent-gold-active: "#a87d4e"
  ink: "#222222"
  ink-deep: "#11151c"
  body: "#3d4246"
  muted: "#7f8084"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  hairline-faint: "#e8e9eb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  surface-hover: "#e8e9eb"
  surface-dark: "#121212"
  nav-dark: "#3d4246"
  scrim: "#000000"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  price-display:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Dosis', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px

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
    padding: "12px 28px"
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
    height: 44px

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 27px"
    height: 44px
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.muted}"

  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
    height: 44px
    hoverBackgroundColor: "{colors.accent-gold-active}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 42px
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.ink-deep}"

  nav-bar-dark:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px

  category-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"

  category-tab-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    hoverTextColor: "{colors.body}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
    imageObjectFit: "contain"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
    hoverBackgroundColor: "{colors.surface-hover}"

  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"

  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"

  product-card-price-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"

  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 560px
    imageObjectFit: "contain"
    padding: "{spacing.xxl} {spacing.lg}"

  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink-deep}"

  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"

  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"

  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"

  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"

  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "2px solid transparent"
    gap: "{spacing.xs}"

  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    inputRounded: "{rounded.full}"
    backdropColor: "rgba(0,0,0,0.50)"
    shadow: "0 8px 32px rgba(0,0,0,0.12)"

  spec-row:
    backgroundColor: "{colors.surface-soft}"
    altBackgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"

  spec-row-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"

  switch-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    padding: "{spacing.sm} {spacing.md}"

  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    headingTypography: "{typography.caption}"
    headingTextColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — coral-rose (#fb637e) fill with white Dosis label at 600 weight, 0.5px letter-spacing. Rounded at {rounded.sm} (8px), matching the gentle corners on Varmilo's keycap photography. Hover darkens fill to {colors.primary-active}; disabled washes to {colors.primary-disabled} at the same geometry. Height is 44px to maintain generous touch targets.

**`button-secondary`** — white canvas with a 1px {colors.hairline} border and {colors.ink} Dosis label. Hover tightens the border to {colors.muted}. Used for add-to-wishlist, filter toggles, and secondary CTA pairings alongside the coral primary.

**`button-gold`** — {colors.accent-gold} (#c79b68) fill reserved for limited-edition and pre-order flows. It signals collector-tier purchasing intent without requiring a separate page template. Hover deepens to {colors.accent-gold-active}; shares padding and height with `button-primary`.

**`button-ghost`** — transparent background, {colors.body} Dosis label at 14px/600, used for "View all", "Load more", and inline text-level secondary actions. No border, minimal padding.

### Cards

**`product-card`** — {colors.surface-card} (#eeeeee) ground with {rounded.md} corners and {spacing.lg} internal padding. Image renders at a 4:3 aspect ratio with object-fit: contain so full-keyboard shots are never cropped at the edges. A subtle 6% opacity shadow lifts to 10% on hover. Title uses {typography.title-md}; regular price renders in {typography.price-display} at {colors.ink}; sale prices switch to {colors.primary}. Badge overlays (sale, new, limited) float top-left over the image.

### Navigation

**`nav-bar`** — white canvas at 60px height, {colors.hairline-soft} bottom border. Logo and category links use {typography.nav-link} (Dosis 600/14px) in {colors.body}. The dark variant (`nav-bar-dark`) uses {colors.ink-deep} for collection-specific hero pages where the keyboard photograph extends edge-to-edge behind the bar.

**`category-tab-active`** — transparent background, {colors.primary} label, 2px bottom-border accent in the same coral. Inactive tabs use {colors.muted} with no underline and soften to {colors.body} on hover. Spacing at {spacing.sm} vertical / {spacing.base} horizontal gives tabs room without swelling the bar.

### Hero

**`hero`** — {colors.surface-soft} ground at 560px minimum height on desktop. A keyboard photograph with object-fit: contain centers the product without cropping; padding at {spacing.xxl} vertical keeps the image from touching the nav or the below-fold grid. Title uses `hero-title` ({typography.display-xl}, {colors.ink-deep}); subtitle uses `hero-subtitle` ({typography.body-md}, {colors.muted}).

### Badges

**`badge-sale`** — coral (#fb637e) fill, white Dosis uppercase 11px/700, {rounded.xs} corners, 2px × 8px padding. Floats top-left over product-card image areas.

**`badge-limited`** — {colors.accent-gold} fill, same geometry as badge-sale. Marks limited-run colorways and collector editions; never appears alongside badge-sale on the same card.

**`badge-new`** — near-black (#222222) fill, same geometry. Signals recent catalog additions without the urgency of a sale flag.

### Product Detail

**`color-swatch`** — 20px circles at {rounded.full}, spaced at {spacing.xs}. The active swatch gains a 2px {colors.ink} outer ring; inactive swatches are borderless. The cluster sits below the product title, before the switch selector row.

**`switch-selector`** — a row of inline pill buttons: default state is {colors.surface-soft} with a hairline border; selected state fills to {colors.primary} with white text. Allows multiple switch types to be shown without a dropdown. Used for switch variant, layout, and connectivity selectors.

**`spec-row`** — zebra-striped table rows alternating {colors.surface-soft} and {colors.canvas}. Dosis 400/14px in {colors.body}, 8px × 16px padding, {colors.hairline-soft} bottom border. Label column uses {typography.caption} in {colors.muted}; value column uses {typography.body-sm} in {colors.ink}. Covers switch actuation force, travel distance, layout, dimensions, weight, and connectivity.

### Search

**`search-overlay`** — full-width modal over a 50% black scrim. Pill-shaped input at {rounded.full}, white canvas background, box-shadow at 12% opacity. Result rows render product-card titles in {typography.title-md} with 32px square thumbnails to the left.

### Footer

**`footer`** — near-black (#121212) background, white-text link columns in {typography.body-sm}/400. Column headers use {typography.caption}/600 in {colors.on-dark}. Bottom strip carries social icon row and a regional/language selector. Logo renders as white reversed mark.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero drops to 320px min-height; color swatches wrap at two rows; spec table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only; hero at 420px; category tabs scroll horizontally with fade mask |
| Desktop | 1128–1440px | Three-column product grid; full nav with subcategory flyouts; hero at 560px; spec table inline beside product image |
| Wide | > 1440px | Four-column product grid; hero expands to 640px; max-width container at 1440px centers all content |

### Touch Targets
- All buttons minimum 44px height on mobile
- Color swatches expand to 28px diameter on touch viewports
- Nav hamburger menu links minimum 44px tap height
- Product card tap area covers the full card surface including padding

### Collapsing Strategy
- Nav hamburger below 744px; drawer slides in from left over a 40% scrim
- Category tabs switch to horizontal scroll on tablet and below; active tab scrolls into view on load
- Product hero switches from side-by-side (image + text columns) to stacked layout at 744px, image above copy
- Switch selector pill row wraps to two lines below 480px; no horizontal scroll to avoid accidental swipe-dismiss
- Footer column grid collapses from 4-column to 2-column at 744px, then 1-column at 480px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) is almost certainly a Shopify framework default and was not present in extracted CSS tokens; all near-white values extracted were #f5f5f5 and #eeeeee
- No dark-mode color set detected — the `nav-bar-dark` variant is inferred from visual inspection of collection hero pages, not a confirmed separate token set
- Animation and transition durations (hover color fade, drawer slide, overlay appear) were not extractable from static extraction
- Exact nav height (estimated 60px) and breakpoint pixel values not confirmed from source; derived from visual proportion
- A secondary display typeface may exist for large hero lockups; only Dosis was detected in font-family stacks
- Exact button padding values estimated from visual proportion against known height; not extracted from CSS
- Switch selector interaction pattern (pill row vs. dropdown vs. radio) not confirmed; pill row is inferred from product photography
- Social icon set and footer regional selector design not confirmed beyond their presence in page structure
