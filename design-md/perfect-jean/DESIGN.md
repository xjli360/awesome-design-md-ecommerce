---
version: alpha
name: "The Perfect Jean"
source_url: "https://theperfectjean.nyc"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Blinding electric yellow (#ffff00) is the first thing a visitor encounters at theperfectjean.nyc — a full-width promotional strip that makes no apologies for its urgency against the composed, denim-blue system beneath it. The structural palette is anchored to #1a6fa7, a medium-value blue that reads like the wash of a well-worn five-pocket, running through primary CTAs, nav link hovers, and interactive states, while a secondary teal (#108474) marks category labels, trust badges, and filter chips with a quieter, more editorial register. Canvas steps back to #f9f9f9 rather than optical white, giving product photography a faint warmth; cards float on this surface without hard borders, relying on color contrast and implied elevation instead. Type makes an unexpected move — display headlines reach for Baskerville, a classical book serif, in a space where most stretch-denim competitors stay strictly geometric sans. The choice communicates longevity and craft: The Perfect Jean is positioned not as a fast-fashion impulse but something worn for years. Body and UI copy falls to Helvetica/Arial, a workhorse stack that keeps mobile readability crisp. Button labels carry weight 600 with a touch of letter-spacing, giving CTAs legibility on small screens without resorting to all-caps aggression. Comfort cues appear as {rounded.full} pill badges in {colors.surface-subtle} with muted uppercase text — "All-day stretch," "Move freely" — placed near product imagery to reinforce the brand's core claim before the visitor reaches the description block. Sale pricing uses #da2e3a, deployed sparingly so it keeps alarm value. Star ratings from the Judgeme widget bring golden #fbcd0a fills against the light card surface, anchoring social proof directly adjacent to the add-to-cart zone. The teal secondary (#0f918b) reappears in trust icons — free shipping, returns, sustainability pledges — giving functional badges a distinct visual register, separated from the blue CTA hierarchy so neither competes for click priority.

colors:
  primary: "#1a6fa7"
  primary-active: "#036297"
  primary-disabled: "#c1e6e6"
  accent-teal: "#108474"
  accent-teal-dark: "#0f918b"
  promo: "#ffff00"
  error: "#da2e3a"
  error-dark: "#c52726"
  ink: "#111111"
  body: "#555555"
  muted: "#66747f"
  muted-soft: "#9ca3af"
  hairline: "#dedede"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#f3f4f6"
  surface-subtle: "#eeeeee"
  on-primary: "#ffffff"
  on-promo: "#111111"
  star: "#fbcd0a"
  lavender: "#a89cc8"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  promo-bar:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    linkActiveColor: "{colors.primary}"
  promo-banner:
    backgroundColor: "{colors.promo}"
    textColor: "{colors.on-promo}"
    typography: "{typography.promo-bar}"
    padding: 10px 16px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: none
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.error}"
    originalPriceColor: "{colors.muted}"
    imageRounded: "{rounded.xs}"
  product-badge:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.muted}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  star-rating:
    starFill: "{colors.star}"
    starEmpty: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    padding: 64px 32px
    textAlign: center
  size-swatch:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    selectedBorder: "2px solid {colors.primary}"
    selectedTextColor: "{colors.primary}"
    unavailableTextColor: "{colors.hairline}"
    unavailableDecoration: line-through
  color-swatch:
    rounded: "{rounded.full}"
    size: 24px
    selectedBorder: "2px solid {colors.ink}"
    borderOffset: 2px
  filter-chip:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    iconColor: "{colors.accent-teal}"
    typography: "{typography.caption}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.surface-subtle}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
  quantity-selector:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    buttonColor: "{colors.muted}"
    buttonHoverColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — The primary CTA carries `#1a6fa7` fill with white type set in weight-600 Helvetica at 15px with 0.5px letter-spacing, sitting in a 48px-tall container on 4px corners (`{rounded.xs}`). On hover the background deepens to `{colors.primary-active}` (#036297) with no transition delay, maintaining the denim-blue metaphor across states. Disabled state uses the pale `{colors.primary-disabled}` teal-wash (#c1e6e6), signaling unavailability without aggressive gray.

**`button-secondary`** — Outlined variant: white fill, `{colors.primary}` text and 1.5px border. Used for secondary actions like "View Details" or "Add to Wishlist" at the same 48px height, preserving click-target consistency alongside the primary button in paired layouts.

**`button-teal`** — An accent CTA in `{colors.accent-teal}` (#108474) deployed for contextually distinct actions such as "Find My Fit" or quiz-style entry points, separating them from the purchase funnel's blue hierarchy.

### Promo Banner

**`promo-banner`** — Site-wide, full-bleed strip in the unmistakable `{colors.promo}` (#ffff00) with near-black type and weight-700 tracking. Sits above the nav bar so it is the literal first rendered element. Dismiss behavior is site-session scoped; the bar re-appears on new visits. Text centers and truncates to a single line on mobile.

### Navigation

**`nav-bar`** — White canvas, 64px tall, hairline bottom border (`{colors.hairline}`). Links render in `{typography.nav-link}` at weight 500; the active or hovered link shifts to `{colors.primary}`. Logo anchors left; cart, search, and account icons anchor right. No mega-menu: category navigation typically falls to a horizontal scrollable strip directly beneath the bar on desktop.

### Product Card

**`product-card`** — Borderless cards float on `{colors.surface-soft}`, image block carries `{colors.surface-soft}` background to hold the space before load. Title renders in `{typography.title-sm}` (weight 600, 15px Helvetica); price in `{typography.body-md}`. Sale price appears in `{colors.error}` with the original price struck through in `{colors.muted}`. Badge chips (sale, new) overlay the image corner using `{rounded.full}` pill geometry.

### Size & Color Selectors

**`size-swatch`** — Rectangular chips with 1px `{colors.hairline}` border, selecting to a 2px `{colors.primary}` border and primary-blue label. Sold-out sizes show struck-through text in `{colors.hairline}` gray and are not removed — they remain visible to indicate range breadth.

**`color-swatch`** — Circular `{rounded.full}` dots at 24px, offset-bordered when selected (2px `{colors.ink}` ring with 2px gap). Hovering shows color name in a tooltip using `{typography.caption}`.

### Trust Badges

**`trust-badge`** — Three-up icon + label modules (free shipping, easy returns, stretch guarantee) with teal icon fills (`{colors.accent-teal}`) that visually separate this strip from the primary blue button zone. Label type is `{typography.caption}`; heading type is `{typography.title-sm}` in `{colors.ink}`.

### Filter Chips

**`filter-chip`** — `{rounded.full}` pills in `{colors.surface-subtle}` for unselected state; selected chips flip to `{colors.primary}` fill with white text. Used on the collection page for size, inseam, rise, and color filtering. Horizontal scroll on mobile with no wrap.

### Star Rating

**`star-rating`** — Judgeme widget delivers SVG stars filled in `{colors.star}` (#fbcd0a) against light card surfaces. Review count renders in `{typography.caption}` at `{colors.muted}`. The aggregate star display near the product title links directly to the reviews section below the fold.

### Footer

**`footer`** — Full-width `{colors.ink}` (#111111) background with `{colors.surface-soft}` body text and `{colors.surface-subtle}` links. Section headings use `{typography.title-sm}` in `{colors.canvas}`. Four-column grid on desktop collapses to single-column accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; promo banner single-line truncated; nav collapses to hamburger + cart icon; filter chips horizontally scroll; hero copy drops to `{typography.display-sm}`; size swatches wrap into two rows |
| Tablet | 744–1128px | Two-column product grid; nav shows full logo + icon row with hidden text links; hero layout splits 50/50 image-copy; trust badges collapse to icon-only with tooltip |
| Desktop | 1128–1440px | Three-column product grid; full nav with text links and hover states; trust badge strip shows icon + label + subtitle; hero at full `{typography.display-xl}` |
| Wide | > 1440px | Grid max-width caps at ~1400px, centered with symmetric margin; promo banner text remains single-centered line; hero image bleeds edge-to-edge behind constrained content column |

### Touch Targets

- All swatch buttons minimum 40×40px tap target regardless of visual size
- Filter chips minimum 36px tall on mobile
- Quantity selector increment/decrement buttons minimum 44×44px
- Nav icons minimum 44×44px on mobile

### Collapsing Strategy

- Hamburger menu replaces full nav below 744px; categories list in a slide-out drawer
- Promo banner persists across breakpoints but clips text to one line with ellipsis below 375px
- Trust badge strip switches from icon+label to icon-only at tablet, restoring labels at desktop
- Footer four-column grid collapses to stacked accordion sections on mobile
- Size guide link folds into an inline text-button beneath the size selector row on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected — only system fonts (Baskerville, Helvetica/Arial) and third-party review widget icon fonts (JudgemeStar, JudgemeIcons) were found in CSS; it is possible a display font is loaded via JavaScript or hosted externally and was not captured
- Multiple near-identical primary blues extracted (#1a6fa7, #006daa, #036297, #016497) — the true single brand-primary is ambiguous; #1a6fa7 is used here as it appeared first in the extraction, but #006daa or #036297 may be the canonical CTA value
- Meta theme-color not set, so no OS-level browser chrome color signal was available
- Lavender (#a89cc8) and light teal (#c1e6e6) appear in the extraction but their exact usage context (product swatch colors, UI accents, or background variants) could not be confirmed from CSS alone
- No motion/animation tokens could be extracted; transition timing and easing for hover/focus states are assumed standard (200ms ease)
- Exact grid gutter widths and column counts for collection pages are estimated from visual convention, not confirmed from source stylesheets
