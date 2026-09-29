---
version: alpha
name: "Amazfit"
source_url: "https://www.amazfit.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Amazfit runs its global storefront on a near-black #0f0f0f canvas — a deliberate inversion of the white-default DTC template that places the brand alongside premium consumer electronics rather than lifestyle accessories. The single most arresting accent is an amber-gold (#ffd75e), a warmth that cuts cleanly against the dark ground and carries every primary CTA; it deepens to #ea9f30 on press, avoiding the cool steel that would read too industrial. A deep crimson (#b20000) surfaces on sport and performance SKU badges, signaling a second product line with its own emotional key rather than leaning on the single-accent pattern most tech stores use. Health and fitness features get cyan (#1fade6) and teal (#02909c) treatments — sometimes against a pale #e4f3f7 wash — while mint (#69c69c) marks wellness metrics, building a spectral system where color encodes product category rather than decoration. Type falls to Arial throughout the extracted stack; no brand typeface was served, which the site compensates for by letting spec density and photography carry identity weight. Cards sit in #232323 — two stops above the #0f0f0f base — giving them just enough lift to read as objects without breaking the cinematic dark unity. Corners are tight: interactive elements use 4–8px radii, and category filter chips are the only pill-shaped elements ({rounded.full}), marking them as navigational rather than structural. The spacing contract favors product imagery over editorial breathing room, packing spec chips and rating rows close beneath product names in dense catalog contexts while opening to section-scale vertical rhythm in hero zones. This is a storefront built for users who read spec sheets first — the amber pulse says "buy" to engineers who otherwise distrust ornament.

colors:
  primary: "#ffd75e"
  primary-active: "#ea9f30"
  primary-disabled: "#5f5f5f"
  ink: "#f9f9f9"
  body: "#dedede"
  muted: "#9c9c9c"
  muted-soft: "#888888"
  hairline: "#34313a"
  hairline-soft: "#232323"
  canvas: "#0f0f0f"
  surface-soft: "#121212"
  surface-card: "#232323"
  on-primary: "#0f0f0f"
  on-dark: "#f9f9f9"
  accent-red: "#b20000"
  accent-red-mid: "#ca2f2f"
  accent-red-deep: "#770e0e"
  accent-cyan: "#1fade6"
  accent-cyan-soft: "#e4f3f7"
  accent-teal: "#02909c"
  accent-mint: "#69c69c"
  accent-amber: "#f79555"
  neutral-mid: "#5f5f5f"
  cool-gray: "#c8ccd4"

typography:
  display-xl:
    fontFamily: "Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-tag:
    fontFamily: "Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    priceTypography: "{typography.price-tag}"
    nameTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBackgroundColor: "{colors.surface-soft}"
    hoverTransform: translateY(-2px)
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaComponent: button-primary
    minHeight: 600px
    overlayGradient: "linear-gradient(90deg, rgba(15,15,15,0.85) 0%, rgba(15,15,15,0.0) 60%)"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-chip:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 16px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: none
    padding: 6px 16px
  feature-tag:
    backgroundColor: "{colors.accent-cyan-soft}"
    textColor: "{colors.accent-cyan}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sport-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-red}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-tag}"
    saleColor: "{colors.accent-red-mid}"
    originalColor: "{colors.muted}"
  rating-row:
    starColor: "{colors.primary}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    focusBorder: "1px solid {colors.primary}"
  product-series-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-sm}"
    subheadTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "48px 0"

## Components

### Buttons
**`button-primary`** — Amber-gold (#ffd75e) fill with near-black (#0f0f0f) text at 16px/600; 4px radius and 48px height. Activates to #ea9f30 on press, preserving brand warmth without shifting hue family. Disabled state collapses to #5f5f5f fill with muted text. This is the single highest-contrast interactive element in an otherwise dark environment and should be reserved strictly for primary purchase and navigation actions.

**`button-secondary`** — Transparent background with 1px #34313a hairline border; ink (#f9f9f9) text. Hover fills to surface-card (#232323) and border brightens to muted (#9c9c9c). Used for "Compare," "Add to Wishlist," and secondary spec-page actions alongside a primary.

**`button-ghost`** — Text-only in primary (#ffd75e), no background or border, button-sm typography. Used for inline "Learn more" or "See all specs" links inside product cards and specification tables where a boxed button would overwhelm information density.

### Text Input
**`text-input`** — #232323 fill, 4px radius, 1px #34313a border with 48px height. Placeholder text and leading icons in muted (#9c9c9c). Focus ring swaps the border to primary (#ffd75e), maintaining brand coherence with no drop shadow or glow. Used in site-wide search and newsletter signup forms in the footer.

### Nav Bar
**`nav-bar`** — Sticky 64px bar on #0f0f0f canvas; a 1px #34313a bottom border separates it from page content without introducing a bright line. Navigation links at 14px/500 in ink (#f9f9f9). Utility icons (search, cart, region) sit right-aligned; cart icon carries a gold (#ffd75e) numeric badge dot on non-zero counts. Sub-category flyouts use surface-card (#232323) as the panel background.

### Product Card
**`product-card`** — #232323 lifts cleanly off the #0f0f0f base with no box shadow; image zone uses #121212 (surface-soft) as its inner background to frame product photography without a stark white swatch. Product name in title-sm (16px/600), price in price-tag (20px/700). Spec badges and feature/sport tags stack below the price row in a flex-wrap group. Hover applies a 2px upward translate. No outline or ring — depth comes solely from the surface-color step.

### Hero Section
**`hero-section`** — Full-bleed #0f0f0f canvas with product or lifestyle photography. A left-anchored gradient overlay (85% → 0% opacity) keeps headline and CTA legible over bright product imagery without boxing the image. Headline in display-xl (48px/700), subhead in body-md with body (#dedede) color, CTA as button-primary. Minimum height 600px. On mobile the gradient rotates to a bottom scrim and text stacks below the image.

### Spec Badge
**`spec-badge`** — Compact uppercase 11px/700 chips on surface-soft (#121212) fill, muted (#9c9c9c) text. Used for quantitative specs — battery life hours, GPS type, water resistance ATM, display size — in catalog listing cards and comparison tables. The tight 4px/8px padding and 4px radius keeps them scannable without inflating card height.

### Category Chip (Filter)
**`category-chip`** — Transparent background, 1px hairline border, full-pill radius ({rounded.full}), 12px caption type. Active state fills solid to primary (#ffd75e) with on-primary (#0f0f0f) text, border removed. These chips appear in a horizontally scrollable filter row above the product grid and are the only pill-shaped interactive element in the system.

### Feature Tag and Sport Tag
**`feature-tag`** — Pale cyan wash (#e4f3f7) background with cyan (#1fade6) text in spec-label style; marks health and biometric features such as heart rate, SpO2, stress index, and sleep tracking. **`sport-tag`** uses surface-soft (#121212) fill with crimson (#b20000) text for sport-mode counts, VO2 Max, and performance-focused SKUs. Both tags appear together on mixed-category watches, creating a quick visual shorthand for capability scope.

### Price Display
**`price-display`** — Current price in price-tag style (20px/700, ink #f9f9f9). On sale: original price rendered in muted (#9c9c9c) with line-through decoration; sale amount or percentage off appears in accent-red-mid (#ca2f2f) as a small label beside or below.

### Search Bar
**`search-bar`** — 40px height, #232323 fill, 4px radius; leading magnifier icon in muted (#9c9c9c). Compact relative to the 48px text-input; used in the nav bar overlay on desktop and as a full-width element on mobile. Focus border shifts to primary (#ffd75e).

### Product Series Banner
**`product-series-banner`** — Dark #121212 panel with 8px radius; display-sm headline (24px/600) in ink, body-sm subhead in muted. A primary (#ffd75e) accent — either an underline rule, a left border, or a CTA button — anchors the brand color in editorial content blocks separating product family sections.

### Footer
**`footer`** — #232323 background with 1px #34313a top border. Default text in muted (#9c9c9c), links in body (#dedede). Upper band holds regional selector, social icons, and newsletter signup (text-input + button-primary). Lower band drops to caption (12px) for legal links and copyright. Full-width at all breakpoints; columns collapse to single-column accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav collapses all categories into drawer; hero stacks with image above copy and bottom scrim; filter chips scroll horizontally |
| Tablet | 744–1128px | 2-column product grid; condensed nav retains wordmarks but hides secondary utility links; hero retains left-anchored layout at reduced text scale (display-md) |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with mega-menu flyouts on hover; hero at full 600px minimum height with left-half text zone |
| Wide | > 1440px | Max-width container (1440px) centered; hero expands to 720px minimum; grid holds 4 columns with wider card padding and increased section spacing |

### Touch Targets
- All tappable elements minimum 44×44px on mobile
- Nav icons and cart badge enforce 48px tap zones regardless of visual size
- Category filter chips minimum 36px tall on mobile
- Product card tap zone covers full card surface including image and text zones

### Collapsing Strategy
- Primary nav condenses to hamburger at < 744px; mega-menu becomes accordion drawer with chevron toggles
- Spec badge groups wrap to 2-line max, then truncate with "Show all specs" text link
- Footer columns collapse to single-column accordion on mobile; newsletter signup moves above legal block
- Hero headline scales: display-xl (48px desktop) → display-md (32px tablet) → display-sm (24px mobile)
- Product series banners reduce padding from xxl/xl to base/lg on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand typeface detected — Arial is the extracted system fallback; Amazfit likely serves a custom geometric sans-serif via JavaScript after initial render, values here are defaults
- Exact production border-radius values could not be confirmed; 4px and 8px used as reasonable minimums for a tech-forward brand
- Animation and transition timings (hover elevations, drawer openings, image carousels) not captured from static extraction
- Light-mode variant existence unconfirmed — all extracted tokens point to a dark-primary experience; a mode toggle may exist on select product-detail pages
- Icon system details beyond FontAwesome attribution not captured; Amazfit likely maintains a proprietary pictogram set for health metrics and sport modes
- Precise CSS grid column counts and gutter widths per breakpoint not confirmed
- Social proof components (Trustpilot widget, press logo strip) and their token usage not extracted
- #4285f4 (Google blue) and #1fade6 appear likely as OAuth and ecosystem integration colors respectively; their exact scoping to non-brand UI was not confirmed
