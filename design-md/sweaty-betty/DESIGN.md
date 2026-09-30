---
version: alpha
name: "Sweaty Betty"
source_url: "https://sweatybetty.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two chromatically charged decisions define every Sweaty Betty surface — a pool-water teal (#06afa9) operating as the brand's north star, and a saturated hot pink (#d6006d) that fires across campaign imagery, sale flags, and promotional CTAs with the urgency of a sprint finish. The two voltages do not compete: teal anchors the identity while pink signals action, and a supporting bright mint (#02d0bc) plus fuchsia (#f35db5) extend the range into gradient territory for hero modules and seasonal banners. That chromatic confidence sits against a near-black ground (#1c1f21, #181818) in editorial contexts, then lifts to white canvas for product browsing — a deliberate oscillation that gives both teal and pink maximum luminosity against each environment.

  London origin is encoded not in geographic signifiers but in editorial restraint. Product names run in clean grotesque uppercase; body copy sets at modest sizes with generous leading; the typographic texture actively avoids the oversized-display maximalism that American activewear brands favour. Type holds tension with colour here — letterforms stay measured so the neon teal and candy pink carry the energy without tipping into chaos.

  Rounded radii skew modest: buttons and cards take `{rounded.sm}` rather than the pill-and-blob aesthetic common in lifestyle-adjacent brands. `{rounded.full}` appears on category badge chips — Run, Yoga, Train, Ski, Swim — which act as a colour-coded wayfinding system across collections, rendered in `{colors.primary}` teal on dark backgrounds or `{colors.ink}` on white. Product photography crops tight to engineered-seam and fabric-texture detail, often against gradient-teal or near-black backdrops that reinforce the chromatic identity without additional art direction.

  The spacing system leans generous at section level — 64px between content blocks, 48px between grid rows — to give photography room to breathe, while component gaps stay tight. Medium-gray (#4e555a) handles secondary body copy and form labels; a softer graphite (#222a30) carries primary body text; the lightest tonal gray (#d9d9d9) draws hairlines and input borders. No hard right angles are visible to the shopper — every interactive surface carries at least `{rounded.xs}` to maintain the brand's athletic-but-approachable character.

colors:
  primary: "#06afa9"
  primary-active: "#059a95"
  primary-disabled: "#a3d8d6"
  accent-pink: "#d6006d"
  accent-pink-active: "#b5005c"
  accent-fuchsia: "#f35db5"
  accent-mint: "#02d0bc"
  ink: "#1c1f21"
  body: "#222a30"
  muted: "#4e555a"
  hairline: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#181818"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent-pink: "#ffffff"
  sale-flag: "#cc0000"
  navy: "#000066"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  category-badge:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-accent-pink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-pink-active:
    backgroundColor: "{colors.accent-pink-active}"
    textColor: "{colors.on-accent-pink}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    borderColor: "{colors.on-dark}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  hero-module:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 600px
    overlayOpacity: 0.35
  hero-module-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 480px
  promo-banner:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-accent-pink}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.category-badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  category-badge-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.category-badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  sale-badge:
    backgroundColor: "{colors.sale-flag}"
    textColor: "{colors.on-dark}"
    typography: "{typography.category-badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  new-badge:
    backgroundColor: "{colors.accent-fuchsia}"
    textColor: "{colors.on-dark}"
    typography: "{typography.category-badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    unavailableTextColor: "{colors.muted}"
    unavailableDecoration: line-through
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    minWidth: 44px
    height: 44px
  color-swatch:
    size: 28px
    selectedBorderColor: "{colors.ink}"
    selectedBorderWidth: 2px
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA renders in Sweaty Betty's signature pool-water teal (`{colors.primary}`, #06afa9) with white uppercase text in `{typography.button-md}` at 0.8px letter-spacing. At 48px height with 8px corners (`{rounded.sm}`), it reads as athletic without feeling stiff; hover darkens to `{colors.primary-active}` (#059a95), and the disabled state bleaches to `{colors.primary-disabled}`. Appears on product pages for "Add to Bag" and all checkout flow primary actions.

**`button-pink`** — Fires on high-urgency promotional moments — sale launches, limited drops, newsletter sign-ups. The fill swaps to `{colors.accent-pink}` (#d6006d), matching the promo-banner and sale-badge system for a coherent top-to-bottom urgency signal on promotional days. Active state darkens to `{colors.accent-pink-active}`. Identical dimensions to `button-primary` so layout remains stable during CTA A/B tests.

**`button-secondary`** — 1.5px `{colors.ink}` outline, transparent fill, uppercase text in `{colors.ink}`. Handles secondary actions (View Details, See More, Explore Collection) where a primary button already owns the focal point. The `button-secondary-on-dark` variant flips all ink values to `{colors.on-dark}` for placement over hero and dark-canvas modules.

### Navigation

**`nav-bar`** — 64px-tall bar on white canvas with a 1px `{colors.hairline}` bottom border. Logo anchors left; primary nav links (`{typography.nav-link}`, 14px weight 500) sit in a centred horizontal row with category mega-dropdowns; search, account, and bag icons cluster right. The bar remains fixed on scroll with a subtle box-shadow upgrade. The `nav-bar-dark` variant — used on dark editorial landing pages and campaign hubs — flips canvas to `{colors.surface-dark}` (#181818) and reverses all text to `{colors.on-dark}`.

### Product Card

**`product-card`** — 3:4 portrait-ratio imagery fills the card top; below sit product name in `{typography.body-sm}` and price in `{typography.price}` (16px, weight 600), separated from the image by an 8px gap (`{spacing.sm}`). On hover, a row of `color-swatch` dots surfaces at the image bottom alongside a quick-add button overlay. Category badge chips stack over the image top-left corner. `{rounded.xs}` (4px) corners align the card with the brand's modest-radius system.

### Hero Module

**`hero-module`** — Full-bleed photography overlaid at 35% `{colors.surface-dark}` scrim, with headline in `{typography.display-xl}` (52px, uppercase, weight 700) and sub-headline in `{typography.display-sm}`. Minimum 600px height on desktop; a white or teal CTA button anchors the lower-left quadrant. The `hero-module-teal` variant replaces photography with a solid `{colors.primary}` (#06afa9) fill and white text — used for campaign launches and category hubs where colour is the lead element rather than an image backdrop.

### Promotional Banner

**`promo-banner`** — A 36px full-width strip in `{colors.accent-pink}` (#d6006d) pinned above the nav. Scrolling or static copy in `{typography.button-sm}` (12px, uppercase, 0.8px tracking) carries shipping thresholds and offer codes. The hot-pink tone deliberately echoes `sale-badge` and `button-pink`, creating a vertical urgency signal from page-top to product card on sale days.

### Category & Status Badges

**`category-badge`** — Pill chips (`{rounded.full}`) in `{colors.primary}` teal with white uppercase text (`{typography.category-badge}`, 11px, 0.6px tracking). Tags sport category (Run, Yoga, Train, Ski, Swim) on product cards and collection page filters. `category-badge-dark` uses `{colors.ink}` fill for white-canvas contexts. `sale-badge` fires in `{colors.sale-flag}` (#cc0000); `new-badge` fires in `{colors.accent-fuchsia}` (#f35db5) — the badge palette maps directly to the brand's signature voltage colours rather than introducing neutrals.

### Size Selector

**`size-selector`** — Square 44×44px tiles with 1px `{colors.hairline}` borders, white fill, `{colors.ink}` text in `{typography.body-sm}`. Selected state inverts to `{colors.ink}` fill with `{colors.on-dark}` text. Out-of-stock sizes render in `{colors.muted}` with a line-through decoration; tapping them may surface a notify-me email capture modal. `{rounded.xs}` corners match the card and input system.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) field in `{colors.surface-soft}` with `{colors.muted}` placeholder text. Expands from an icon tap in the nav to a full-screen overlay on mobile; on desktop it opens a type-ahead drawer populated with trending searches rendered as `category-badge` chips in `{colors.primary}` teal.

### Footer

**`footer`** — Dark canvas (`{colors.surface-dark}`, #181818) with white text in a four-column grid: Brand, Help, Sustainability, Social. Column headings use `{typography.title-sm}` (16px, weight 600); links use `{typography.body-sm}` (14px, weight 400). Teal and pink are absent from the footer — the dark ground anchors the page without chromatic competition. A newsletter sign-up at footer base pairs the standard `text-input` with a `button-primary` teal submit button, the one place the brand's primary colour re-enters the footer row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer + bottom icon bar; hero headline drops from 52px to 28px; promo-banner text truncates to single static offer; filters open as bottom-sheet drawer |
| Tablet | 744–1128px | Two-column product grid; nav retains horizontal links but drops secondary subcategory panels; hero module min-height 480px; category badge row scrolls horizontally |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-nav with category imagery panels; hero at 600px min-height with left-anchored text block over image |
| Wide | > 1440px | Max-width container centres at 1440px; outer gutters fill with canvas; product grid holds four columns with larger imagery; editorial hero sections can expand edge-to-edge |

### Touch Targets

- All buttons minimum 48px height; `size-selector` tiles minimum 44×44px
- `color-swatch` minimum 28px diameter with at least 4px gap between adjacent swatches
- Nav icons (search, account, bag) padded to minimum 44px hit area
- Promo banner tap zone spans full width; any dismiss chevron padded to 44px
- Badge chips on mobile padded vertically to reach 36px minimum tap height

### Collapsing Strategy

- **Nav**: Horizontal mega-nav with imagery panels → hamburger drawer with nested accordion category panels; search icon → full-screen overlay with autofocus
- **Hero**: Full-bleed split text/image layout → stacked image-above-text; headline scales 52px → 28px; CTA shifts from lower-left to below the text block
- **Product grid**: 4 col → 3 col → 2 col → 1 col at mobile breakpoint
- **Filter bar**: Horizontal pill-filter row → "Filter & Sort" bottom-sheet drawer on mobile
- **Footer**: 4-column grid → 2 columns → single-column accordion with collapsible headings on mobile; social icons remain visible at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extracted from the live site — the brand likely loads a custom or licensed grotesque typeface via JS or a CDN-hosted webfont. All typography above uses a `Helvetica Neue` system fallback; identify and replace with the actual webfont (possibly a proprietary variant or licensed grotesque such as Aktiv Grotesk) before production use.
- Exact button border-radius values were not confirmed from CSS inspection; `{rounded.sm}` (8px) is inferred from visual observation of comparable activewear brand conventions.
- Dark/light mode switching behaviour is unconfirmed — the dual dark-editorial/white-canvas pattern is inferred from the near-black (#1c1f21, #181818) and white usage distribution in the extracted palette.
- Animation and transition durations for hover states, mega-nav reveals, quick-add overlays, and swatch-row appearance on product cards were not captured.
- Deep navy (#000066) and muted reds (#bd3d44, #192f5d) appear in the extracted palette but their precise usage contexts — possibly country-flag imagery, error states, or promotional graphics — are unconfirmed; they are not wired to components above.
- The `sale-flag` value (#cc0000) is used for `sale-badge` but sale pricing display conventions (strikethrough colour, percentage-off label placement) were not confirmed from extraction.
- Product card quick-add overlay specifics (z-index behaviour, animation direction, button label) were not confirmed.
