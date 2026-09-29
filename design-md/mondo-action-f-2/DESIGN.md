---
version: alpha
name: "Mondo"
source_url: "https://mondoshop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  #d63021 — a red pulled from cinema lobby lighting rather than a hazard sign — runs every primary action on mondoshop.com: the add-to-cart button, the sold-out stamp that collectors dread, the sale badge that triggers the instant refresh. Against a near-black ink (#121212) and subdued mid-tone body text (#4d4d4d), this red reads as urgency without aggression — the visual equivalent of a drop-timer at 00:01. Poppins does all the type work, its geometric terminals giving product names a poster-credit sharpness at weight 700 in compressed tracking, while body copy settles at 400 for clinical specificity about scale, edition size, and materials. The hairline system uses two near-identical light grays (#dedede, #dadada) to separate card surfaces from page canvas with almost imperceptible depth — the browser chrome is meant to disappear so the product photography dominates. A supporting cobalt (#0073ce) handles hyperlinks and informational callouts, cool enough in temperature to avoid competing with the warm red primary. The overall surface language is flat and grid-rigid: product cards sit in dense two-to-four column layouts with no elevation or drop-shadow, relying on contained imagery borders in {rounded.sm} to keep listings legible without theatrical depth. Edition badges — 'Limited Edition', 'Exclusive', '1/6 Scale' — render in tight uppercase at {typography.badge} with the red primary as background, functioning less as decorations than as inventory-state signals. The sold-out overlay is a semi-opaque dark scrim stamped with white uppercase type, a deliberate design choice that keeps unavailable product visible as catalogue evidence while discouraging clicks. Navigation is a flat dark bar with the Mondo wordmark anchored left and utility icons right — search, cart count — with no mega-menu sprawl. The footer reverses to {colors.canvas-dark} with white Poppins links organized by collection category, a structural mirror of the collector's mental model: by property, by format, by artist.

colors:
  primary: "#d63021"
  primary-active: "#b52419"
  primary-disabled: "#e8907d"
  accent-blue: "#0073ce"
  accent-blue-active: "#005fac"
  ink: "#121212"
  body: "#4d4d4d"
  muted: "#6e6e6e"
  hairline: "#dedede"
  hairline-soft: "#dadada"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-raised: "#dadada"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sold-out-scrim: "rgba(18,18,18,0.72)"
  error: "#d63021"
  link: "#0073ce"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  countdown:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 1px

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
    padding: 14px 24px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    padding: 12px 22px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
    padding: 10px 18px
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "none"
    logoColor: "{colors.on-dark}"
  nav-link-item:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    hoverColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    iconColor: "{colors.muted}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-sold-out:
    overlayBackground: "{colors.sold-out-scrim}"
    overlayTextColor: "{colors.on-dark}"
    overlayTypography: "{typography.badge}"
    overlayLabel: "SOLD OUT"
  edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  exclusive-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaButton: "button-primary"
    minHeight: 520px
    paddingY: "{spacing.xxl}"
  drop-countdown:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    digitTypography: "{typography.countdown}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: "{spacing.lg}"
  product-detail-gallery:
    thumbnailBorder: "2px solid {colors.hairline}"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
  collection-filter-tag:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  price-display-block:
    regularPriceTypography: "{typography.price-display}"
    regularPriceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    height: 36px
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.body}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Square-cornered ({rounded.none}), full uppercase Poppins at weight 600 with 0.5px letter-spacing, 48px tall, 24px horizontal padding. Background is Mondo red (#d63021); hover darkens to #b52419. Disabled state washes out to #e8907d with `cursor: not-allowed`.

**`button-secondary`** — Transparent background with a 2px solid ink border and ink-colored text, same uppercase type scale as primary. Hover state swaps border and text to the primary red, signaling collectibility without committing the full brand saturaiton.

**`button-ghost`** — Hollow with a 2px primary-red border and red text, used on dark-background hero sections where the secondary's ink border would disappear.

### Navigation

**`nav-bar`** — 60px dark bar (#121212 background) sitting flush against the page top. Mondo wordmark anchors left in white; utility icons (search, account, cart with item count badge) cluster right. No horizontal dividers, no dropdown mega-menu — category navigation lives in a secondary row or hamburger panel. Link items use 13px/500-weight Poppins with red hover state.

**`announcement-bar`** — 36px red bar above the nav, white uppercase badge-scale type centered. Used for drop announcements, shipping cutoffs, exclusive access windows.

### Product Cards

**`product-card`** — Zero-radius image container with a 1px hairline border, 12px padding, and a subtle shadow on hover. Title runs {typography.title-sm} (15px/600); price uses {typography.price-sm} (15px/600). No border-radius on imagery preserves the poster-art, frame-it-yourself aesthetic.

**`product-card-sold-out`** — A 72%-opacity near-black scrim (#121212) overlays the full card image with "SOLD OUT" in white uppercase {typography.badge} centered. The card remains in the grid at full opacity as catalogue evidence; the scrim communicates state without visual demotion.

**`edition-badge`** / **`exclusive-badge`** / **`sale-badge`** / **`new-badge`** — Flat rectangular chips (no radius) positioned top-left over card images. Edition badges use primary red; Exclusive uses ink-black; New uses accent cobalt (#0073ce). All render in 10px/700/0.8px-spaced uppercase — legible at grid density without competing with product photography.

### Hero Banner

**`hero-banner`** — Full-width, dark-canvas (#121212) strip with a minimum height of 520px. Heading in {typography.display-xl} (48px/700), subhead in {typography.display-sm} (24px/600), both in white. CTA uses `button-primary`. Image panels sit right or bleed behind a left-anchored copy column. No gradient overlays — hard crops against the dark background keep the cinematic register.

### Drop Countdown

**`drop-countdown`** — A dark-field component framed by a 1px primary-red border. Digit blocks use {typography.countdown} (28px/700, 1px letter-spacing) in white; unit labels ("DAYS", "HRS", "MIN", "SEC") in 12px caption beneath. Used on upcoming-release landing pages and in announcement bars to convert browsing into anticipation.

### Collection Filters

**`collection-filter-tag`** — Pill-shaped ({rounded.full}) soft-gray chips for category/format/property filtering. Active state fills with primary red and white text. Font is 12px/600 uppercase Poppins. These are the only rounded elements in the layout, providing tactile contrast against the otherwise hard-edged grid.

### Price Display

**`price-display-block`** — Current price in {typography.price-display} (20px/700) in ink; if on sale, sale price renders in primary red and original price appears to its right in muted gray with line-through. No parenthetical formatting — the visual color-coding does the differentiation work.

### Footer

**`footer`** — Dark reverse (#121212 background) with white Poppins column headings ({typography.title-sm}) and #dadada-toned link text ({typography.body-sm}). Hover links turn primary red. Organized by collection category (Figures, Prints, Music, Apparel) and utility links. Top border is 1px body-tone to separate from page content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero copy stacks above image; countdown digits scale to 22px; announcement bar wraps to two lines if needed |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories, hamburger for overflow; hero runs split 50/50 layout |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with all category links visible; hero copy left-anchored at 40% column width |
| Wide | > 1440px | Grid maxes at 1440px centered with auto side margins; hero image bleeds to viewport edge while copy column stays in max-width container |

### Touch Targets

- All buttons minimum 48px tall; icon buttons (cart, search, account) minimum 44×44px
- Filter tags on mobile expand to 40px minimum height with increased horizontal padding
- Product card touch areas include the full card surface, not just the image or title

### Collapsing Strategy

- Nav: all category links visible at ≥1128px; secondary categories move to hamburger panel at 744–1127px; full hamburger at <744px
- Product grid: 4-col → 3-col → 2-col → 1-col at respective breakpoints
- Hero: side-by-side layout at ≥744px; stacked (image below copy) at <744px
- Countdown: four-unit row at ≥744px; wraps to 2×2 grid at <480px
- Filter bar: horizontal scrollable row on mobile with no line wrap; overflow fades to gradient hint

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed dark-mode token split — whether the site uses #121212 as a universal canvas or only for nav/footer/hero is unverified; design assumes hybrid (white cards, dark nav/hero)
- Exact nav height and secondary navigation structure not confirmed from extraction; 60px is an estimate
- Font-weight distribution across Poppins variants not extracted beyond family name; weights 400/500/600/700 inferred from collector-brand conventions
- Animation/transition timing (hover states, sold-out overlay fade, countdown tick) not captured
- Grid gutter widths not extracted; standard Shopify defaults (20–24px) assumed
- Accent cobalt (#0073ce) usage scope (links only vs. broader UI) not confirmed beyond extraction presence
- Mobile breakpoint values are Shopify theme defaults; actual theme overrides not confirmed
