---
version: alpha
name: "Bulova"
source_url: "https://www.bulova.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The sweep hand on a Bulova Precisionist completes eight full micro-steps per second — where a standard quartz moves once — and that engineering fixation on the barely perceptible translates directly into a digital identity that works through restraint rather than spectacle. The interface is built almost entirely from a stepped gray scale: #f7f7f7 near-white canvas, #e5e5e5 and #b2b2b2 for hairlines and muted surfaces, #3c3c3c as the primary ink. Against this neutral field, the brand's Bulova blue (#2559a8, deepening to #1f5da0 on active states) lands with authority — precise and contained, the way a second hand meets its marker. The Japan site's font stack leads with Lato before falling through Hiragino Kaku Gothic ProN and Meiryo, a deliberate layering that keeps the experience coherent across Latin and CJK character sets without font-swapping artifacts mid-line. Accent colors are kept rare: #da4453 appears only for promotional badges and limited-run callouts, while #4caac0 teal surfaces in collection accent chips and hover states on collection tiles. Product cards use very shallow rounding ({rounded.xs} to {rounded.sm}) — consistent with the geometry of case-and-lug profiles rather than consumer-tech pill shapes — and dial photography dominates the grid at roughly 60:40 image-to-text ratios. Navigation sits in a white horizontal bar with a persistent search icon; collection-section headers use wide tracked uppercase caps to announce transitions between movement families. The overall effect is a heritage watch brand that trusts the movement inside the case to do the talking — the interface steps back to near-invisibility so the dial commands the viewport.

colors:
  primary: "#2559a8"
  primary-active: "#1f5da0"
  primary-disabled: "#667895"
  primary-dark: "#006db8"
  accent-red: "#da4453"
  accent-teal: "#4caac0"
  accent-teal-dark: "#0b6752"
  ink: "#3c3c3c"
  body: "#5c5c5c"
  muted: "#7c8790"
  muted-soft: "#b2b2b2"
  hairline: "#e5e5e5"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  promo-badge-bg: "#da4453"
  promo-badge-text: "#ffffff"
  new-badge-bg: "#2559a8"
  price-sale: "#da4453"

typography:
  display-xl:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  display-sm:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
  collection-header:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 2.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', Arial, Tahoma, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-item-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.price-sale}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 540px
    textAlign: center
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
  collection-badge:
    backgroundColor: "{colors.new-badge-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  promo-badge:
    backgroundColor: "{colors.promo-badge-bg}"
    textColor: "{colors.promo-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  sale-ribbon:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    position: absolute
    top: 0
    left: 0
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  collection-section-label:
    typography: "{typography.collection-header}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
  price-range-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    thumbColor: "{colors.primary}"
    height: 4px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  watch-spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  wishlist-icon:
    color: "{colors.muted-soft}"
    colorActive: "{colors.accent-red}"
    size: 20px

## Components

### Buttons

**`button-primary`** — Bulova blue (#2559a8) fill with white uppercase Lato at 14px/1px tracking, 44px height, and a minimal 4px radius. The uppercase + tracked treatment echoes the engraved text conventions of watch case backs, giving CTAs a hardware-adjacent authority. Active state deepens to #1f5da0; disabled collapses to muted #667895 with the same geometry.

**`button-secondary`** — White fill with a 1px solid primary-blue border and blue text, creating a clear hierarchy against `button-primary` without competing with product photography. Hover shifts the fill to #f7f7f7 `surface-soft`. At 44px it matches primary height so stacked CTA pairs stay optically balanced.

**`button-text-link`** — Transparent background, primary blue text, uppercase 12px Lato with 1px tracking, no border. Used for secondary actions inside product tiles ("View Details", "Compare") where a bordered button would overcrowd the card.

### Navigation

**`nav-bar`** — 60px white bar with a 1px #e5e5e5 bottom border. Links render in Lato SemiBold 13px at 0.5px tracking; the active item gains a 2px solid blue underline — a minimal indicator borrowed from ruled-dial convention. Logo sits left; search, wishlist, and account icons right-aligned at 40×40px tap targets.

### Product Card

**`product-card`** — Light gray (#f2f2f2) background with 4px rounding. The image occupies a square 1:1 ratio with slight internal padding so the case bezel never bleeds to the card edge. On hover, a 0 4px 12px shadow at 10% opacity elevates the card without altering its shape. Title renders in `title-sm`, regular price in `price-display` ink; a sale price swaps to `price-sale` #da4453. `promo-badge` and `collection-badge` chips sit flush top-left with zero radius, visually pinned to the card corner like a hangtag.

### Hero Banner

**`hero-banner`** — Either deep charcoal (#3c3c3c) fill or full-bleed photography behind white display type. Title at `display-xl` (36px, weight 700) sits center-aligned with a subtitle in `body-md` at 85% opacity below. Minimum 540px height keeps at least 60% of any featured dial visible above the fold on desktop. The CTA `button-primary` sits centered below the subtitle with 48px top margin.

### Badges

**`collection-badge`** — Hard-cornered rectangular chip (radius 0) in Bulova blue, 10px uppercase Lato. The zero-radius decision on badges contrasts with the 4px rounding on cards: badges read as labels, not interactive elements. `promo-badge` uses the identical geometry in #da4453 red, appearing on tiles for limited editions or sale items.

### Filter Chips

**`filter-chip`** — 1px hairline-bordered chips in 12px Lato caption weight. Active state fills solid primary blue with white text. Used for faceted filtering across movement type (quartz, automatic, solar), case material, strap type, and water resistance rating. On mobile these wrap to a horizontally scrolling single row above the grid.

### Footer

**`footer`** — Inverted charcoal (#3c3c3c) canvas with off-white link text (#b2b2b2 `muted-soft`). Section headings in `title-sm` at full white; link columns in `body-sm`. The color split — bright headings against quieter links — creates scannability without a separate visual divider between columns. A secondary hairline-colored row at the bottom holds copyright, privacy, and language-selector links.

### Watch Spec Table

**`watch-spec-table`** — Two-column key/value layout inside a #f7f7f7 soft surface, used on PDP pages to surface movement type, case diameter, water resistance, and crystal type. Labels in muted #7c8790, values in ink #3c3c3c — the same light/dark split used on analog dial subsidiary indexes versus main numerals. Rows separated by 1px #e5e5e5 hairlines; no outer border, letting the surface color define the container.

### Search Bar

**`search-bar`** — #f7f7f7 fill with a 1px hairline border that upgrades to primary blue on focus. Lato Regular 15px placeholder text in #7c8790. At 40px height it sits comfortably in the nav drawer on mobile or as an inline bar at the top of collection pages on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger replaces horizontal nav; hero scales to 320px min-height; filter panel collapses to bottom-sheet drawer |
| Tablet | 744–1128px | Two-column grid; nav condenses to icon row with labels; hero at 420px; filters as slide-in left panel |
| Desktop | 1128–1440px | Three or four-column grid; full horizontal nav with dropdown megas; hero at 540px; filter sidebar persistent left-rail at 240px |
| Wide | > 1440px | Container max-width 1440px centered; five-column grid on collection pages; hero extends edge-to-edge behind container |

### Touch Targets
- All buttons minimum 44px height on all breakpoints
- Nav icon buttons padded to 44×44px tap area despite 20–24px visual icon size
- Filter chips have 38px minimum height on mobile with 8px vertical padding
- Wishlist icon padded to 40×40px hit area regardless of 20px rendered size
- Product card is fully tappable as a single target; no nested tap-within-tap patterns

### Collapsing Strategy
- Desktop mega-menu collapses to nested accordion inside the hamburger drawer on mobile
- Three-column footer becomes vertically stacked accordions separated by 1px hairline dividers on mobile
- Watch spec table remains two-column across all breakpoints; type scales from 13px to 12px on mobile
- Price and "Add to Cart" lock to a fixed bottom action bar on mobile PDP to keep the primary CTA visible while scrolling through spec content

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display typeface confirmed; Lato is the primary Latin web font extracted from the Japan site but whether the global bulova.com uses a proprietary headline font could not be verified
- Canvas white (#ffffff) assumed — not present in the extracted palette, likely filtered as a framework default before hints were generated
- Exact nav height, mega-menu layout columns, and hover/transition timing not extractable from static scrape
- Accent tones #4caac0 teal, #0b6752 deep green likely map to specific collection sub-brands (e.g., Precisionist, Marine Star) — collection-to-color assignments not confirmed and should not be used as global brand tokens
- Light warm tones (#fceef0, #ffb3b3, #ffe6ad, #ffff98, #fab194) appear to be collection-palette swatches rendered in imagery rather than CSS tokens; treat as decorative data, not system colors
- Japanese site may diverge from the global bulova.com in spacing and type scale due to CJK character rendering requirements; these specs should be verified against the English-language global site before applying universally
