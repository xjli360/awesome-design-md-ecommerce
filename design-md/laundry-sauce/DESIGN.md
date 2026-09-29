---
version: alpha
name: "Laundry Sauce"
source_url: "https://laundrysauce.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every fragrance in the lineup gets its own color territory — lavender holds deep purple (#805ad5, #322659), eucalyptus claims near-black forest green (#1f3521), citrus warms into burnt sienna (#cc6328), and a bright fresh-clean green (#2ea818) anchors the lightest scent — while the base brand identity runs on a resolute dark charcoal (#303030) that refuses to soften into the white-canvas wellness vocabulary the laundry category typically defaults to. This is a brand that named itself after hot sauce and means it: CondensedBold display type crashes down at compressed widths with a tight 0.95 line-height and uppercase lock, referencing stadium signage and label typography more than bathroom-shelf minimalism. "The Signature" script cuts against that industrial force as a deliberate sparring partner — a fluid handwritten element that surfaces at section breaks and brand moments, reminding you there is a person behind the posture. The warm sand tone (#dfd5c4) is the one color that belongs to no single scent: it recurs on label grounds, section dividers, and the highlight band that carries punchy single-line claims in charcoal CondensedBold, functioning as a parchment-like neutral that unifies the fragrance palette without being owned by any of them. Buttons are full-width on mobile and dark-fielded everywhere — the brand projects conviction rather than invitation. The {rounded.sm} radius on cards and inputs is a studied restraint, just enough to read as premium consumer product without drifting into the soft-rounded vocabulary of skincare. Inter handles all body text and UI chrome with the measured neutrality of a secondary voice, keeping emphasis on the condensed display headlines and the photography. Color itself is the wayfinding system: when a user enters lavender territory, badges, active tab underlines, and swatch borders all pull toward #805ad5, making scent navigation a spatial, chromatic experience rather than a dropdown exercise.

colors:
  primary: "#303030"
  primary-active: "#121212"
  primary-disabled: "#707070"
  accent-sand: "#dfd5c4"
  variant-lavender: "#805ad5"
  variant-lavender-deep: "#322659"
  variant-forest: "#1f3521"
  variant-green: "#2ea818"
  variant-citrus: "#cc6328"
  error: "#d12121"
  error-deep: "#c70000"
  ink: "#171923"
  body: "#303030"
  muted: "#637381"
  muted-soft: "#aaaaaa"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-warm: "#f2f2f3"
  on-primary: "#f9fafb"
  on-dark: "#f9fafb"

typography:
  display-xl:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  script-accent:
    fontFamily: "'The Signature', cursive"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  script-sm:
    fontFamily: "'The Signature', cursive"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.02em
  price:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.05em
    textTransform: uppercase
  button-sm:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.04em
    textTransform: uppercase
  badge:
    fontFamily: "'CondensedBold', 'din_condensedbold', Impact, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px

  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 30px
    height: 52px

  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 30px
    height: 52px

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px

  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    paddingX: "{spacing.base}"
    textAlign: center

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    paddingX: "{spacing.xl}"

  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 600px
    paddingX: "{spacing.xl}"
    paddingY: "{spacing.xxl}"

  hero-sand-band:
    backgroundColor: "{colors.accent-sand}"
    textColor: "{colors.ink}"
    typography: "{typography.script-accent}"
    paddingY: "{spacing.lg}"
    textAlign: center

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
    imageAspect: "1/1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    padding: "{spacing.md}"

  scent-badge:
    rounded: "{rounded.full}"
    typography: "{typography.badge}"
    padding: "4px 12px"
    textColor: "{colors.on-dark}"
    colorByScent:
      lavender: "{colors.variant-lavender}"
      forest: "{colors.variant-forest}"
      citrus: "{colors.variant-citrus}"
      fresh: "{colors.variant-green}"

  scent-selector-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderActive: "3px solid {colors.primary}"
    borderInactive: "2px solid {colors.hairline}"
    gap: "{spacing.xs}"

  product-highlight-band:
    backgroundColor: "{colors.accent-sand}"
    textColor: "{colors.primary}"
    typography: "{typography.display-md}"
    paddingY: "{spacing.xl}"
    paddingX: "{spacing.base}"
    textAlign: center

  sticky-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    height: 64px
    paddingX: "{spacing.base}"
    position: fixed
    bottom: 0

  review-stars:
    starColor: "{colors.variant-citrus}"
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    gap: "{spacing.xxs}"

  review-count-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"

  scent-feature-card:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.accent-sand}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"

  ingredient-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"

  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-sand}"
    typography: "{typography.body-sm}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xl}"
    paddingX: "{spacing.xl}"

  footer-heading:
    typography: "{typography.button-md}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"

## Components

### Buttons

**`button-primary`** — A 52px-tall charcoal (#303030) field carrying CondensedBold uppercase text at 18px with 0.05em letter-spacing, giving the compressed typeface just enough air to read cleanly at small sizes. Active state deepens to near-black (#121212); disabled drains to mid-gray (#707070) while keeping on-primary cream text so the inactive state reads as unavailable rather than broken. Padding is 14px/32px — wide enough to feel substantial, tight enough that the all-caps label dominates.

**`button-secondary`** — Transparent background with a 2px charcoal border and matching charcoal text, same CondensedBold uppercase treatment and 52px height as primary. The border gives it presence on light surfaces without competing with the product photography. On dark hero sections this role is fulfilled by `button-ghost-light`, which swaps both text and border to {colors.on-dark} cream.

### Navigation

**`nav-bar`** — 64px tall on a {colors.canvas} white background, separated from page content by a 1px {colors.hairline} bottom border. Logo sits left on desktop; nav links in Inter 14px/500 spread across the right half with cart and account icons terminal. The `announcement-bar` sits above it in primary charcoal (#303030) with reversed cream text and {typography.caption} uppercase — used for promotions, scent launches, or free-shipping thresholds.

### Product Card

**`product-card`** — 1:1 image aspect ratio in a {rounded.sm} container with a subtle 8px shadow that lifts the card off the {colors.surface-soft} page grid. Title in Inter 18px/600; price in Inter 20px/700 below. `scent-selector-swatch` circles (32px, {rounded.full}) appear beneath the title — active swatch outlined in 3px charcoal, inactive in 2px {colors.hairline} gray. The swatch row doubles as a color wayfinding signal for the fragrance lineup.

### Hero

**`hero`** — Full-bleed dark charcoal canvas with a `display-xl` CondensedBold headline (72px, uppercase, 0.95 line-height) that dominates the vertical space. A `hero-sand-band` can interrupt the hero as a contrasting warm strip carrying "The Signature" script font at 48px — the juxtaposition of industrial compressed type and handwritten script is the brand's visual signature. Min-height 600px on desktop; on mobile the headline drops to `display-lg` (52px) and the layout stacks.

### Scent System

**`scent-badge`** — Pill-shaped ({rounded.full}) color-coded labels driven by `colorByScent` mapping: lavender #805ad5, forest #1f3521, citrus #cc6328, fresh #2ea818. CondensedBold 11px all-caps at 0.08em tracking on {colors.on-dark} cream text. The active scent badge color bleeds into surrounding UI — PDP section headers, active swatch borders, and the `sticky-add-to-cart` bar all echo whichever variant territory the user has entered.

### Product Highlight Band

**`product-highlight-band`** — Full-width warm sand (#dfd5c4) band using `display-md` CondensedBold (36px, uppercase) in primary charcoal. Carries punchy single-line copy ("No fillers. No filler smells."). Acts as a pacing break between product grid sections and the hero; the warm sand tone is the only element that appears in every scent context without belonging to any one of them.

### Scent Feature Card

**`scent-feature-card`** — A charcoal-background tile used in editorial sections to spotlight a single scent, with a warm sand accent line or badge above the headline. `display-sm` CondensedBold headline with Inter body copy below. Typically laid out in a 2-up or 3-up grid on desktop, full-width stacked on mobile.

### Reviews

**`review-stars`** — Star icons in {colors.variant-citrus} (#cc6328), the warmest color in the palette that works against both light and dark backgrounds. Adjacent review count in Inter 14px/400 at {colors.muted} slate. `review-count-badge` wraps aggregate star counts in a {colors.surface-soft} pill with {rounded.xs} corners — understated so it supports rather than competes with the product headline.

### Footer

**`footer`** — Inverted dark charcoal (#303030) canvas with {colors.on-dark} body text and {colors.accent-sand} links that recall the warm sand brand thread. Column headings in CondensedBold uppercase via `footer-heading`. Three columns on desktop (Shop, About, Legal); stacks to accordion panels on mobile with one panel open at a time.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, full-width primary buttons, hamburger nav with slide-over drawer, hero headline at display-lg (52px), sticky-add-to-cart pinned to bottom |
| Tablet | 744–1128px | Two-column product grid, nav links visible, hero at full display-xl, announcement-bar retained, scent swatches inline |
| Desktop | 1128–1440px | Three-column product grid, nav expanded with hover states, hero split-layout (headline left, product image right), product-highlight-band at full width |
| Wide | > 1440px | Max-width container at 1440px centered, side margins grow proportionally, four-column product grid, hero image scales up |

### Touch Targets
- All buttons and inputs minimum 48–52px tall
- Scent swatches 32px diameter with 8px surrounding margin to reach 48px touch area
- Mobile nav items expand to full-width rows at 56px height
- Announcement bar links padded to ≥ 44px tappable height
- Footer accordion trigger rows minimum 48px tall

### Collapsing Strategy
- Nav collapses to hamburger at < 744px; all links stack full-width in a slide-over drawer at 100vw
- Footer columns collapse to accordion panels on mobile, one panel open at a time
- Hero switches from split-layout to stacked at < 744px; image above, headline below, or headline overlaid with a dark scrim
- Scent swatch row converts to horizontal scroll strip on mobile if more than five variants are present
- Product highlight band headline scales from display-md (36px) to display-sm (24px) on mobile to prevent text wrap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary CTA color** — The extraction contains reds (#d12121, #c70000) that may serve as an alternate CTA or sale-price accent; it is unclear from the hex harvest alone whether these are error states or brand-level action colors; #303030 charcoal is assigned as primary from the dominant non-gray extraction tone
- **Exact display font sizing** — CondensedBold and din_condensedbold pixel sizes are inferred from DTC category norms; live computed CSS measurements were not captured from the DOM
- **Shadow tokens** — Drop-shadow blur, spread, and color values are estimated; no shadow data was extractable from the color harvest
- **Animation and motion** — Transition durations, easing curves, and scroll-triggered animation details are not available
- **Logo geometry** — Whether the lockup is wordmark-only, icon + wordmark, or a combination, and the exact sizing ratios, were not captured
- **"The Signature" font scale** — The relative sizing of the script font against CondensedBold in live context was not measured; 48px is an estimate
- **Dark-mode toggle** — It is unclear whether the site operates a formal dark-mode toggle or uses dark sections contextually; the two-surface treatment is inferred from color distribution
- **Scent variant exhaustiveness** — The four scent color territories mapped here (lavender, forest, citrus, fresh) may not represent the complete current product lineup
