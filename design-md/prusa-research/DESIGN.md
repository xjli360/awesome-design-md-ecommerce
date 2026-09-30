---
version: alpha
name: "Prusa Research"
source_url: "https://www.prusa3d.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Orange #fa6831 operates at full saturation across an otherwise controlled dark-and-neutral spectrum — it lands on every primary CTA, every printer-status LED illustration, and every heat-gradient diagram explaining nozzle temperatures on exploded assembly views. The palette runs two distinct registers simultaneously. A light engineering canvas (#f5f6f7 with #e0e0e0 hairlines and #2a2a2a ink) handles product catalog, spec tables, and filament libraries. A near-black production zone (#121212, #2a2a3a) carries immersive hero sections where filament reels and print heads photograph against studio void — the darkness is not decorative; it mimics the enclosed build chamber environment Prusa's printers actually occupy. A second accent voltage, functional green #5ccc3d, operates exclusively in status and availability contexts: live build progress indicators, "In Stock" badges, and online printer health rings. #00c48d provides a teal variant for softer success states, and #00b67a arrives with the Trustpilot review widget — a third-party green that rhymes close enough with Prusa's own success state that no one notices the seam.

  Atlas Grotesk carries all type at weights 400–700, a grounded geometric grotesque that reads clearly at 12px spec callouts inside assembly diagrams and scales to 48px section heroes without requiring a separate display face. Line heights run tight — 1.1 to 1.25 for headings — matching the brand's precision-instrument sensibility. Letter-spacing compresses at large sizes, reinforcing technical density rather than airy consumer polish.

  Corners are nearly flat: {rounded.xs} on inputs and product cards, {rounded.sm} on buttons and badges. There are no pill shapes; the geometry echoes aluminum extrusion profiles. Focus rings collapse to a 2px #fa6831 outline — the only place primary orange appears outside a button. Navigation sits in a 72px utility bar at #2a2a3a with mega-menus for Printers, Filaments, Accessories, and Software, condensed Atlas Grotesk at 14px weight 500. The footer mirrors that dark register with a full ecosystem directory map — information density that Prusa's deeply technical customer base depends on. Error red #ff253a handles destructive states and critical print-failure alerts, completing a three-voltage system: orange for action, green for success, red for failure — the same three states any 3D printer display would show.

colors:
  primary: "#fa6831"
  primary-active: "#e05d2d"
  primary-disabled: "#f5c4ad"
  error: "#ff253a"
  ink: "#2a2a2a"
  body: "#3e3e3e"
  muted: "#808080"
  muted-soft: "#8c8c8c"
  muted-light: "#b3b3b3"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#f5f6f7"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-canvas: "#121212"
  dark-surface: "#2a2a3a"
  dark-surface-alt: "#2c2c2c"
  dark-ink: "#ffffff"
  accent-green: "#5ccc3d"
  accent-teal: "#00c48d"
  accent-green-dark: "#2a8b5f"
  trustpilot: "#00b67a"
  orange-alt: "#ff6600"

typography:
  display-xl:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  spec-label:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  status-label:
    fontFamily: "'Atlas Grotesk', 'AtlasGrotesk', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.dark-ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.dark-ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
    logoHeight: 32px
    megaMenuBackground: "{colors.dark-canvas}"
    megaMenuTextColor: "{colors.dark-ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.dark-ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaButton: "button-primary"
    imagePosition: right
    overlayOpacity: 0
  printer-status-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.dark-ink}"
    typography: "{typography.status-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  printer-status-badge-warning:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.status-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  printer-status-badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.status-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  availability-badge:
    inStockBackgroundColor: "{colors.accent-green}"
    inStockTextColor: "{colors.dark-ink}"
    outOfStockBackgroundColor: "{colors.hairline}"
    outOfStockTextColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 10px"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerTextColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rowStripedBackground: "{colors.canvas}"
    rounded: "{rounded.xs}"
  filament-chip:
    height: 32px
    width: 32px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    tooltip: "{typography.caption}"
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  alert-banner:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.dark-ink}"
    typography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
    padding: "{spacing.md} {spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted-light}"
  pagination:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
    border: "1px solid {colors.hairline}"
  trustpilot-widget:
    starColor: "{colors.trustpilot}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.dark-ink}"
    linkColor: "{colors.muted-light}"
    linkHoverColor: "{colors.dark-ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    headingColor: "{colors.muted}"
    borderTop: "1px solid {colors.dark-surface-alt}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Solid #fa6831 fill, white Atlas Grotesk 600 at 15px, 8px radius, 44px height. Active state shifts to #e05d2d; disabled washes to #f5c4ad. This button appears exclusively for primary purchase and download actions — "Order Now," "Download PrusaSlicer," "Add to Cart."

**`button-secondary`** — Transparent background with a 2px #fa6831 outline and #fa6831 text. On hover/active, the fill floods orange and text inverts to white — same color vocabulary, revealed rather than introduced. Used for secondary CTA pairs alongside a primary button.

**`button-ghost`** — Transparent with a 1px #e0e0e0 hairline border and #2a2a2a text. Used for non-purchase actions: "Compare," "Share," "View Details." Lowest visual weight in the hierarchy.

**`button-dark`** — #2a2a3a background with white text, appearing on light-canvas sections where a dark anchor is needed without orange emphasis. Used in navigation dropdowns and footer actions.

### Navigation

**`nav-bar`** — 72px dark utility bar in #2a2a3a across full viewport width. Logo pins left at 32px height. Category links (Printers, Filaments, Accessories, Software, Community) run center in Atlas Grotesk 14px weight 500, white. Right zone: search icon, cart indicator with orange badge count, account icon. On scroll, bar gains a subtle bottom shadow but holds its dark background without transparency collapse. Mega-menus drop against #121212 with product thumbnails, sub-category grids, and featured product cards.

### Product Card

**`product-card`** — White (#ffffff) surface on the #f5f6f7 canvas, 1px #e0e0e0 border, 4px radius. Image fills the upper ~55% against a #f5f5f5 tinted zone. Below: printer name in `title-md`, short spec summary in `body-sm` / #808080, price in `price-display` (28px/700), and availability badge. Hover lifts with a 4px 16px rgba shadow. Card width normalizes to ~280px grid columns at desktop.

### Status Badges

**`printer-status-badge`** — Three-state system echoing actual printer LCD feedback. Green #5ccc3d for online/healthy, orange #fa6831 for warning/paused, red #ff253a for error/offline. All uppercase Atlas Grotesk 700 at 11px with 0.4px tracking, 4px radius pill, 3px × 8px padding.

**`availability-badge`** — "In Stock" renders #5ccc3d background with near-black text. "Out of Stock" uses #e0e0e0 background with #808080 text. Both uppercase badge typography. Sits below the price in product cards and at the top of product detail pages.

### Spec Table

**`spec-table`** — Data-dense grid used on every printer product page. Header row in #f5f5f5 with Atlas Grotesk 500 12px uppercase muted labels. Data cells in 14px weight 400. Alternating rows stripe between #ffffff and #f5f6f7. A 1px #e0e0e0 grid rule separates all cells. No rounded corners on internal cells; outer container gets 4px radius. Horizontal scroll activates on mobile without breaking column alignment.

### Filament Chip

**`filament-chip`** — 32px circle swatches rendered in the actual filament hex color. Inactive state: 2px #e0e0e0 ring. Active/selected state: 2px #fa6831 ring with 2px gap offset (box-shadow technique). Hovering reveals a tooltip in `caption` typography with the filament name and material type. Chips arrange in a wrapping flex row with 8px gaps.

### Hero Banner

**`hero-banner`** — Full-width section on #121212 dark canvas. Headline in `display-xl` white, sub-headline in `body-md` #808080, primary CTA button ({colors.primary}). Product photography positions right on desktop, stacks above text on mobile. No overlay gradients; photography is pre-masked against dark or transparent background. Section padding is `{spacing.section}` (64px) top and bottom.

### Alert Banner

**`alert-banner`** — Thin sticky strip at #2a2a3a, used for promotions, shipping notices, or firmware update notifications. Body text in white `body-sm`, inline CTA link in #fa6831 `button-sm`. 16px vertical padding, full width.

### Footer

**`footer`** — #121212 base with five-column link directory: Printers, Filaments & Materials, Software, Community, Company. Column headers in uppercase `spec-label` at #808080; links in `body-sm` at #b3b3b3, hover to white. Social icons at 20px, orange on hover. Bottom strip: copyright in `caption` muted, legal links row, and language/region selector.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + logo + cart; hero stacks image above headline; spec-table horizontally scrollable; filament chips wrap freely; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows logo and hamburger; mega-menus become full-sheet drawers; hero splits 50/50; spec-table visible without scroll at 600px+ |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav-bar with all category links; mega-menu drops as overlay panel; hero image fills right 55% |
| Wide | > 1440px | Content max-width caps at ~1400px, centered with symmetric gutters; hero imagery scales with viewport but headline container stays fixed-width; nav links gain increased spacing |

### Touch Targets

- All buttons minimum 44px height
- Filament chips 32px with 8px surrounding touch padding for an effective 48px target
- Nav icons (cart, account, search) minimum 44px × 44px tap area
- Pagination cells 36px with 4px margins for 44px effective target
- Mobile accordion rows in spec-table minimum 48px height

### Collapsing Strategy

- Nav mega-menus → full-screen drawer slide-in from left on mobile/tablet
- Spec table category sections → accordion collapse below 744px, tap header to expand
- Filament chip rows → scroll horizontally if they exceed container (no wrap truncation)
- Footer link columns → single scrollable column stacked vertically below 744px
- Hero image → moves from right-side panel to full-width image above text below 744px
- Product card grid: 4-up (wide) → 3-up (desktop) → 2-up (tablet) → 1-up (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit disabled-state orange extracted; `primary-disabled` (#f5c4ad) is a derived approximation — confirm against Prusa3D's actual component library
- `surface-card` (#ffffff) inferred from common e-commerce pattern; extraction returned no explicit pure-white token
- Exact nav-bar height (72px) estimated from visual proportion; not confirmed via computed CSS
- Dark-mode / light-mode toggle behavior unclear — site may serve a single theme with dark hero sections rather than a true system-preference toggle
- Button border-radius confirmed as small (xs/sm range) but exact px value not extracted from computed styles
- Typography scale sizes (display-xl at 48px, display-md at 32px) estimated from visual hierarchy; Atlas Grotesk's exact size ladder not published
- Atlas Grotesk license/CDN path not visible in extraction; fallback stack will render in system-ui if font fails to load
- Hover and transition durations (e.g., button fill animation speed) not captured
- `#2a8b5f` (dark green) appears in extraction but its specific use context — possibly a sale/promo badge or a deeper hover state for accent-teal — could not be confirmed
