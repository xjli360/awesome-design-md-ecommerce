---
version: alpha
name: "Passenger"
source_url: "https://passenger-clothing.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Passenger's palette reads like a tidal range at dusk: deep ocean (`#204d67`) grounds all primary actions and header fills, while warm cream (`#f8f4ed`) replaces the clinical white canvas found on every other outdoor site — the difference registers as texture before it registers as color. Then a mint burst (`#b2f9e9`) arrives on sustainability callouts, certification badges, and sale ribbon accents, a bioluminescent pop that signals eco-credential without reaching for the mossy greens that outdoor brands have overworked. Burnt terracotta (`#df6439`) warms seasonal collection promos and campaign photography overlays; periwinkle (`#899df1`) floats across secondary UI states and hover treatments. None of these hues are borrowed from trail-gear graphics or alpine photography — they read coastal and tonal, closer to a mid-century nature print than a performance-sports catalog.

  GT Pressura drives all display and headline work: a compressed geometric grotesque that holds upright and utilitarian at weight 600, gaining forward momentum from tight letter-spacing rather than mass. Lato carries body copy with zero friction — 16px at 1.6 line-height for long product-description reads and brand storytelling alike. Poynter surfaces in longer editorial passages — impact reports, brand stories, sustainability deep-dives — giving those pages a journalistic register that separates them from the product grid and slows the reader into genuine attention.

  Rounded corners are moderate throughout: `{rounded.sm}` (8px) on buttons and inputs, `{rounded.md}` (12px) on product cards, `{rounded.full}` on pill-shaped filters and certification badges. No hard corners exist outside footer data grids. The spatial rhythm is deliberately unhurried — `{spacing.lg}` (24px) gutters inside cards, `{spacing.section}` (64px) vertical breathing between content bands — a cadence that invites reading over scanning. Sustainability proof-points appear inline as `{rounded.full}` mint badges marking GOTS and Fair Wear certifications directly on product cards, not tucked into footer links. The nav carries a persistent "Impact" entry alongside the standard collection tree, treating environmental accountability as a first-class destination rather than a footnote.

colors:
  primary: "#204d67"
  primary-active: "#19191e"
  primary-disabled: "#dbdde4"
  ink: "#19191e"
  body: "#525252"
  muted: "#707070"
  hairline: "#e5e5e5"
  hairline-soft: "#e4e4e5"
  canvas: "#f8f4ed"
  canvas-cool: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#fbf6ed"
  surface-warm: "#f7ead5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-mint: "#b2f9e9"
  accent-terracotta: "#df6439"
  accent-periwinkle: "#899df1"
  teal-dark: "#296160"
  deep-navy: "#272d45"
  slate: "#676986"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.1px
  editorial:
    fontFamily: "'Poynter', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  price:
    fontFamily: "'GT Pressura', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 700
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
    padding: "14px 28px"
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 28px"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 27px"
    height: 48px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 27px"
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    focusBorder: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    activeTextColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    imageAspectRatio: "4:5"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    badgeBackgroundColor: "{colors.accent-mint}"
    badgeTextColor: "{colors.primary-active}"
    badgeTypography: "{typography.label-uppercase}"
    badgeRounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.editorial}"
    minHeight: 600px
    overlayScrim: "rgba(25,25,30,0.35)"
    ctaVariant: button-primary
  sustainability-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    iconSize: 14px
  category-pill-filter:
    defaultBackgroundColor: "{colors.surface-soft}"
    defaultTextColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    gap: "{spacing.sm}"
    height: 36px
  impact-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 40px
    accentColor: "{colors.accent-mint}"
  collection-heading:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  size-selector:
    defaultBackgroundColor: "{colors.canvas}"
    defaultBorder: "1px solid {colors.hairline}"
    defaultTextColor: "{colors.body}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    unavailableTextColor: "{colors.primary-disabled}"
    rounded: "{rounded.xs}"
    size: 40px
    typography: "{typography.body-sm}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    buttonSize: 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.accent-mint}"
    accentColor: "{colors.accent-mint}"
    editorialTypography: "{typography.editorial}"

## Components

### Buttons

**`button-primary`** — Deep ocean fill (`#204d67`) with white uppercase GT Pressura labels at 14px/600 weight and 0.5px tracking, 48px height, 8px radius. Hover shifts the fill to near-black (`#19191e`); disabled state renders in washed blue-gray (`#dbdde4`) with muted text. This button carries all primary add-to-bag and checkout CTAs.

**`button-secondary`** — Warm cream canvas fill with a 1.5px ocean-teal border and matching teal label text; hover nudges the surface to `{colors.surface-soft}`. Used on PDPs alongside `button-primary` for secondary actions like "add to wishlist" or "find in store."

**`button-ghost`** — Transparent with a `{colors.hairline}` border and ink text. Reserved for low-priority actions: "back to collection," sort toggles, and modal dismiss buttons. Never competes with the primary CTA.

**`button-pill`** — Full `{rounded.full}` radius at 36px height in ocean-teal fill. Used for inline CTAs in newsletter sign-up strips and loyalty prompts. A mint-background variant (`{colors.accent-mint}` fill, `{colors.primary-active}` text) marks sustainability-specific CTAs like "read our impact report."

### Inputs

**`text-input`** — Warm cream background matching the canvas, 48px height, 8px radius, and a hairline border that thickens to ocean-teal on focus. Placeholder text sits at `{colors.muted}`. Applied uniformly to search, newsletter email fields, and checkout form inputs to maintain a consistent tactile surface across contexts.

### Navigation

**`nav-bar`** — 64px tall on warm cream (`#f8f4ed`), separated from the body by a single hairline rule. Logo left in near-black ink; category links in GT Pressura at 14px/600 with 0.3px tracking. An "Impact" link receives subtle ocean-teal color treatment to visually distinguish it from product categories without relying on an icon. Mobile collapses to a hamburger triggering a full-height cream drawer.

**`announcement-bar`** — 36px ink-black strip sitting above the nav, white 12px Lato text rotating free-shipping thresholds and sustainability messages. Persistent across all pages.

### Product Cards

**`product-card`** — Warm card surface (`#fbf6ed`), 12px radius, 4:5 portrait image ratio. Product name in GT Pressura `{typography.title-sm}`, price in `{typography.price}`. Certification badges rendered as `{colors.accent-mint}` pill labels sit over the image top-left corner. On hover the card lifts with a subtle shadow and a quick-add button fades in at the bottom image edge, keeping the resting state clean.

### Hero

**`hero-banner`** — Full-bleed photography or solid ocean-teal fill with a 35% dark scrim. Headline in `{typography.display-xl}` — GT Pressura 48px/700, white. Subhead in `{typography.editorial}` — Poynter serif at 20px, easing the register from declaration to invitation. CTA renders as `button-primary`. On campaign pages with photography, the scrim preserves type legibility across all image content without requiring a separate color block.

### Sustainability Badges

**`sustainability-badge`** — Pill-shaped mint (`#b2f9e9`) labels with dark near-black text, uppercase 11px GT Pressura at 1.2px tracking. Used for GOTS, Fair Wear, and recycled-material markers directly on product cards and PDPs. The mint is distinctive enough to read as a brand signal rather than a borrowed "eco" visual shorthand.

### Category Filters

**`category-pill-filter`** — Horizontal scroll row of pill-shaped filters on collection pages. Default: `{colors.surface-soft}` fill with `{colors.body}` text. Active: ocean-teal fill with white text. Pills sit at 36px height with `{spacing.sm}` gaps; on mobile the row scrolls horizontally without wrapping, keeping one-thumb reachability.

### Impact Bar

**`impact-bar`** — A 40px ocean-teal band appearing beneath the nav on brand and impact-focused pages, running a rotating ticker of sustainability metrics (tonnes of CO₂ offset, items made from recycled materials) in `{typography.label-uppercase}` with mint accent dots as separators between entries.

### Collection Heading

**`collection-heading`** — `{typography.display-md}` GT Pressura headline on warm cream canvas with a `{typography.body-md}` subhead in `{colors.body}` below. A `{colors.hairline}` rule separates the heading band from the product grid. Breadcrumb in `{typography.caption}` Lato sits above the headline in `{colors.muted}`.

### Size Selector & Quantity Stepper

**`size-selector`** — 40px square tiles with a 4px radius, hairline border at rest, near-black fill when selected. Unavailable sizes render in `{colors.primary-disabled}` with a diagonal strikethrough. **`quantity-stepper`** — Pill-shaped `{rounded.full}` container with canvas fill and hairline border; plus/minus buttons are 32px circles sitting inside the pill ends.

### Footer

**`footer`** — Near-black ink background (`#19191e`) with white 14px Lato link columns and GT Pressura `{typography.title-sm}` section headings. A brief impact statement in `{typography.editorial}` Poynter type sits above the link grid, giving the footer an editorial close. Mint (`#b2f9e9`) activates on link hover and borders the newsletter CTA button. Four-column layout on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + full-height cream drawer; hero headline drops to `{typography.display-sm}` (24px); category pills scroll horizontally without wrap; PDP stacks image above details; footer collapses to accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with sub-menus in drawer; hero allows 50/50 text-image split; filter sidebar collapses to top pill-row |
| Desktop | 1128–1440px | Three-column product grid; full nav with megamenu dropdowns; hero at full 600px min-height; filter sidebar visible left at 240px wide |
| Wide | > 1440px | Content max-width 1440px centered; four-column product grid; hero typography holds at `{typography.display-xl}` 48px; extra horizontal padding added to content bands |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- Size selector tiles expand from 40px (desktop) to 44px (mobile) with increased tap margins
- Category pills hold 36px height but horizontal padding increases to 10px 20px for thumb reach
- Quantity stepper buttons expand from 32px to 44px tap target on mobile
- Nav hamburger renders as a 44×44px touch target

### Collapsing Strategy

- Filters move from persistent left sidebar (desktop) → top pill scroll row (tablet) → bottom-sheet modal (mobile)
- Product grid drops from three columns → two → one, maintaining 4:5 image ratio throughout
- Hero text shifts from bottom-overlay layout to a full-width stacked text panel beneath the image on mobile
- Footer transitions from four-column link grid to tap-to-expand accordion sections on mobile
- Announcement bar persists across all breakpoints; text truncates to one priority message on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav height on mobile not confirmed — 56px estimated from common Shopify theme patterns
- Button border-radius may vary between 4px and 8px across theme components; Shopify theme allows per-component override
- Precise display-xl mobile scale not extracted — desktop values applied throughout with responsive note added
- Poynter usage scope uncertain; may be limited to editorial blog and impact content rather than core product pages
- Shadow and elevation values for product card hover state not captured
- Megamenu column count and internal spacing not confirmed
- Transition durations for drawer open, card hover, and pill filter activation not extracted
- Whether `#899df1` periwinkle appears in live product UI or only in campaign imagery is unconfirmed — treated as secondary accent with estimated usage scope
- `#234e6b` is nearly identical to `#204d67`; one may be a hover/active state of the other rather than a distinct token — merged under `primary` pending visual confirmation
