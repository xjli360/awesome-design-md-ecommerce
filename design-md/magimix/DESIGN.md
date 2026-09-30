---
version: alpha
name: "Magimix"
source_url: "https://www.magimix.us"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  That deep burgundy-red (#af303b) hits before any headline does — it pulses from the "Shop Now" buttons, the navigation hover states, and the silhouette badges that call out motor wattage on every product card. Magimix leans on Futura PT for headlines and navigation, its geometric letterforms echoing the cylindrical bowls and clean engineering lines of the machines themselves; body copy drops to Open Sans at regular weight, readable and unassuming, never competing with product photography that dominates the visual hierarchy. The palette is deliberately restrained: a near-black ink (#3a3a3a), a slate-gray body tone (#5e6a71), and an expanse of white canvas punctuated by cool surface grays (#f5f5f5, #eeeeee) that separate content bands without introducing borders. Cards float on `{colors.surface-card}` with a single `{colors.hairline}` separator, corners barely softened to `{rounded.xs}` — this is European industrial design translated to layout, where sharp geometry dominates and decorative radius is reserved only for pill badges and the search input (`{rounded.full}`). Blue (#0274be) appears strictly as a utility link color, never as brand expression. Section rhythm runs at `{spacing.section}` (64px) between content blocks, compressing to `{spacing.lg}` on mobile. The overall effect is a culinary catalog that trusts its product imagery and engineering claims, framing chrome-and-white appliances against generous negative space rather than burying them in lifestyle noise.

colors:
  primary: "#af303b"
  primary-active: "#8e2630"
  primary-disabled: "#d9969b"
  ink: "#3a3a3a"
  body: "#5e6a71"
  muted: "#808285"
  muted-soft: "#abb8c3"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  border-strong: "#555d66"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#0274be"
  link-hover: "#003388"
  accent-blue: "#1e73be"
  dark-overlay: "#424242"

typography:
  display-xl:
    fontFamily: "'futura-pt', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'futura-pt', 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'futura-pt', 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'futura-pt', 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-bold:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-lg:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link-active:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-value:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  spec-label:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  price:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'futura-pt', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.primary}
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px 12px 44px
    height: 44px
    border: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    transition: box-shadow 0.2s ease
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: 1 / 1
    objectFit: contain
    padding: "{spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 520px
    display: flex
    alignItems: center
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 52px
  spec-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 9px
    border: 1px solid {colors.primary}
  spec-stat:
    textColor: "{colors.ink}"
    typography: "{typography.spec-value}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    padding: "{spacing.base}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"
    minHeight: 200px
  category-tile-hover:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"
  comparison-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: 2px solid {colors.hairline}
  comparison-table-cell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
    borderBottom: 1px solid {colors.hairline-soft}
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.on-dark}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
  toast-notification:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.lg}"
    boxShadow: 0 4px 12px rgba(0,0,0,0.15)

---

## Components

### Buttons

**`button-primary`** — Solid burgundy (#af303b) background with white uppercase Futura PT lettering at weight 600. Corners are barely rounded (`{rounded.xs}`, 4px), giving buttons the precision of a machined control panel rather than a soft consumer feel. On hover the fill darkens to `{colors.primary-active}` (#8e2630); disabled state drops to a muted rose (`{colors.primary-disabled}`) at reduced opacity.

**`button-secondary`** — White fill with a 2px solid ink-colored border. Text matches `{colors.ink}` in the same uppercase Futura PT treatment. On hover the button inverts entirely — ink background, white text — creating a definitive toggle effect that eliminates ambiguity about interactive state.

**`button-small`** — Compact 36px-height variant used inside product cards and comparison tables where full-size CTAs would overwhelm content. Same burgundy fill, smaller font scale (`{typography.button-sm}`).

### Navigation

**`nav-bar`** — Fixed-top white bar at 72px height, anchored by the Magimix wordmark at left and uppercase navigation links (`{typography.nav-link}`) spaced at `{spacing.xl}`. A single-pixel hairline border separates it from page content. On scroll, height compresses to 64px with a subtle drop-shadow appearing (`nav-bar-scrolled`).

**`nav-dropdown`** — Mega-menu panels that open on hover beneath category links. White background, light box-shadow, and internal grid layout organizing product families with thumbnail images. Typography drops to body-md weight for item labels.

### Search

**`search-input`** — Full-width pill-shaped field (`{rounded.full}`) sitting in a soft gray background (`{colors.surface-soft}`). A magnifying-glass icon is inset at 16px from the left edge. No visible border; focus state adds a 2px primary ring.

### Product Cards

**`product-card`** — Rectangular card on `{colors.surface-card}` with a faint border (`{colors.hairline-soft}`). Product image occupies the top portion on a neutral gray background with `object-fit: contain` to show the appliance silhouette cleanly. Below, the title uses `{typography.title-sm}` and price uses `{typography.price}` — bold Futura PT at 20px. Hover lifts the card with a soft shadow and strengthens the border.

**`product-card-image`** — Square aspect ratio container with generous internal padding so the appliance never bleeds to the card edge. Background matches `{colors.surface-soft}` to differentiate from the card body.

### Hero

**`hero-banner`** — Full-width section with a minimum height of 520px, typically split 50/50 between a lifestyle or product image and a text block. Background defaults to `{colors.surface-soft}` when no image fills the frame. The CTA button (`hero-cta`) is slightly larger than standard at 52px height with extra horizontal padding.

**`hero-headline`** — `{typography.display-xl}` at 42px bold, creating immediate visual hierarchy. Letter-spacing pulls tight (-0.5px) to keep long product names compact.

### Specification Badges

**`spec-badge`** — Small burgundy pills used to call out motor wattage, bowl capacity, or warranty years on product pages. Uppercase text at 11px (`{typography.badge}`) keeps them legible at small sizes without dominating the layout.

**`spec-badge-outline`** — Variant with transparent background and a 1px burgundy border, used for secondary attributes or filter tags.

**`spec-stat`** — Large numeral (`{typography.spec-value}`, 28px bold) above a small descriptive label (`{typography.spec-label}`). Used in product feature grids to communicate performance figures at a glance.

### Category Tiles

**`category-tile`** — Rectangular tiles with `{colors.surface-soft}` background linking to product families (Food Processors, Blenders, Juicers). Minimum height of 200px accommodates a category illustration or icon above the title. Hover darkens the background slightly to `{colors.surface-strong}`.

### Comparison Table

**`comparison-table-header`** — Sticky header row with a soft gray background and a 2px bottom border creating clear column delineation. Product names in `{typography.title-sm}`.

**`comparison-table-cell`** — Standard cell with body-sm text and a single-pixel soft border below. Alternating row backgrounds are not used; separation comes from borders alone.

### Footer

**`footer`** — Dark ink-colored background (#3a3a3a) spanning full width. Internal columns organize links under section headings (`{typography.title-sm}` in white). Link text uses `{colors.muted-soft}` and brightens to white on hover. Generous vertical padding (`{spacing.section}`) gives the footer visual weight.

### Utility Components

**`breadcrumb`** — Slash-separated path in caption-size text. Current page renders in `{colors.ink}`, parent levels in `{colors.muted}` with hover underlines.

**`toast-notification`** — Slide-up notification bar with dark background and white text, used for cart-add confirmations and form success messages. Rounded corners at `{rounded.xs}` and a medium shadow keep it distinct from page content.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger menu. Hero stacks vertically (image above text). Product cards fill full width in a single column. Display-xl drops to 28px. Section spacing reduces to `{spacing.xl}`. Comparison table scrolls horizontally. |
| Tablet | 744–1128px | Two-column product grid. Nav remains collapsed or shows abbreviated top-level links. Hero image/text split shifts to 40/60. Category tiles arrange in 2×2 grid. |
| Desktop | 1128–1440px | Full horizontal nav with dropdowns. Three-column product grid. Hero at full 50/50 split. Comparison table shows all columns. Max content width capped at 1200px centered. |
| Wide | > 1440px | Content remains at 1440px max-width centered. Additional whitespace on flanks. Product grid may expand to four columns for category pages. Hero image can bleed past content bounds for cinematic effect. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Navigation hamburger icon has 48px tap zone with 12px padding beyond visible icon
- Product card entire surface is tappable, not just the title link
- Spacing between adjacent tap targets is at minimum `{spacing.sm}` (8px)
- Footer links have `{spacing.md}` (12px) vertical spacing to prevent mis-taps

### Collapsing Strategy

- Top navigation: full horizontal links → hamburger slide-out drawer at tablet breakpoint
- Product comparison tables: fixed first column with horizontal scroll for remaining columns
- Specification grids: three-column → two-column → single stacked column
- Footer columns: four-column → two-column → single accordion on mobile
- Hero banner: side-by-side → stacked with image above, reduced min-height to 360px
- Category tiles: reduce from 3-across to 2-across to single column, maintaining minimum height

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Futura PT weights in use could not be confirmed from extraction — assumed 600/700 for headings based on geometric sans conventions; actual site may use 500/800
- No CSS custom properties or design-token layer was detected; the site likely applies styles via WordPress theme PHP/CSS rather than a token system
- Animation/transition durations and easing curves were not extractable
- Exact max-width container values and breakpoints are inferred from common WordPress theme patterns (Astra theme detected in font stacks), not measured
- Icon library not identified — product pages likely use inline SVGs or an icon font not captured in extraction
- Several extracted blues (#1e73be, #0274be, #0170b9, #003388, #21759b) appear to be WordPress/Astra defaults and WooCommerce link styles rather than intentional brand choices; they are mapped to utility `link` tokens but may not reflect deliberate brand expression
- Cart/checkout flow styling not captured
- Mobile navigation drawer animation and overlay scrim opacity not determinable from static extraction
