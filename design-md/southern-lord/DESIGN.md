---
version: alpha
name: "Southern Lord"
source_url: "https://www.southernlord.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated blue (#003388) anchors a label and shop that traffics in heavy, atmospheric, and extreme music — the color reads like a midnight sky just before a storm, not a corporate navy. That primary blue appears on the header bar, primary buttons, and footer backgrounds, set against a warm off-white canvas (#eeeeee) that softens the intensity. The palette is unusually broad for a music brand: alongside the core blue sit a vivid cyan (#00d084), a bright electric blue (#0693e3), a deep purple (#7a00df), and a hot pink (#f78da7) — these appear as accent badges, genre tags, and limited-edition vinyl variant swatches, giving the shop a collector's-edition energy. Typography runs a single sans-serif stack (the only extracted font-family is WPMenuCart, likely a fallback or widget font, so the system defaults to a clean web-safe sans) at moderate sizes — body text sits around 14–16px, headings at 20–24px, with no heavy display weights. Buttons use the primary blue with white text and soft corners ({rounded.sm}), while the navigation bar is a dark blue (#003388) bar with white links. Product cards are white ({surface-card}) with a thin hairline border (#969696) and a subtle shadow, the album art doing all the emotional work. The overall feel is utilitarian but intentional — a record store that knows its audience wants the music front and center, with the shop as a clean, reliable container.

colors:
  primary: "#003388"
  primary-active: "#002a6e"
  primary-disabled: "#8099bb"
  ink: "#313131"
  body: "#444444"
  muted: "#969696"
  muted-soft: "#abb8c3"
  hairline: "#969696"
  hairline-soft: "#cccccc"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00d084"
  accent-blue: "#0693e3"
  accent-purple: "#7a00df"
  accent-pink: "#f78da7"
  accent-orange: "#ff6900"
  accent-red: "#cf2e2e"
  badge-new: "#00d084"
  badge-sale: "#cf2e2e"
  badge-limited: "#7a00df"
  vinyl-variant-1: "#34e2e4"
  vinyl-variant-2: "#4721fb"
  vinyl-variant-3: "#ab1dfe"
  vinyl-variant-4: "#faaca8"
  vinyl-variant-5: "#fdd79a"
  vinyl-variant-6: "#67a671"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "rgba(255,255,255,0.7)"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px rgba(0,0,0,0.1)"
  product-card-hover:
    shadow: "0 4px 12px rgba(0,0,0,0.15)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  genre-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  genre-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "rgba(255,255,255,0.7)"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  vinyl-variant-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "2px solid {colors.hairline}"
  vinyl-variant-swatch-selected:
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the shop. Uses the deep blue `{colors.primary}` background with white text and a subtle 4px corner radius (`{rounded.sm}`). On hover/active, shifts to `{colors.primary-active}` (#002a6e). Disabled state uses `{colors.primary-disabled}` (#8099bb) to indicate non-interactivity. Height is 44px with 12px/24px padding for comfortable tap targets.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Add to Wishlist". White background with a 2px solid `{colors.primary}` border and blue text. Active state darkens the border to `{colors.primary-active}`. Same 44px height as primary for visual consistency.

**`button-accent-cyan`** and **`button-accent-purple`** — Smaller accent buttons (36px tall) used for genre filters, pre-order actions, or limited-edition drops. Cyan uses `{colors.accent-cyan}` (#00d084) with dark text for high contrast; purple uses `{colors.accent-purple}` (#7a00df) with white text. These bring the brand's broader palette into interactive elements.

### Cards
**`product-card`** — The primary content container for the shop grid. White background (`{colors.surface-card}`) with a subtle drop shadow (`0 1px 3px rgba(0,0,0,0.1)`) and 8px corner radius (`{rounded.md}`). Contains a square album art image (`{rounded.sm}`), the release title in `{typography.title-sm}`, artist name, format, and price in `{typography.body-sm}` with `{colors.muted}` text. On hover, the shadow deepens to `0 4px 12px rgba(0,0,0,0.15)` to indicate interactivity.

### Navigation
**`nav-bar`** — A fixed or sticky 64px header bar in `{colors.primary}` (#003388). Navigation links use `{typography.nav-link}` — uppercase, 14px, weight 600 with 0.5px letter spacing. Active/current page links have a semi-transparent white background (`rgba(255,255,255,0.1)`) with 4px rounding; inactive links use 70% opacity white. The bar may include the label logo, a search icon, and a cart icon.

### Badges & Tags
**`badge-new`**, **`badge-sale`**, **`badge-limited`** — Small uppercase labels (11px, weight 700, 0.5px letter spacing) with 2px rounding. "New" uses `{colors.accent-cyan}` (#00d084) with dark text; "Sale" uses `{colors.accent-red}` (#cf2e2e) with white text; "Limited" uses `{colors.accent-purple}` (#7a00df) with white text. These appear overlaid on product card images or next to titles.

**`genre-tag`** and **`genre-tag-active`** — Pill-shaped filters (full rounding) for browsing by genre (e.g., "Doom", "Drone", "Black Metal", "Ambient"). Inactive tags use a soft gray background (`{colors.surface-soft}`) with muted text; active tags flip to `{colors.primary}` background with white text. 4px/12px padding, 13px caption typography.

### Forms
**`text-input`** — Standard text input for newsletter signups, search, or checkout fields. White background, 44px height, 10px/14px padding, 4px rounding, with a 1px `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.primary}` for clear focus indication.

### Search
**`search-bar`** — A full-rounded pill (44px tall) with white background, 1px hairline border, and 10px/20px padding. Uses `{typography.body-sm}` for placeholder and input text. The pill shape and generous padding make it feel approachable and distinct from the more utilitarian form inputs.

### Footer
**`footer-section`** — A full-width footer in `{colors.primary}` (#003388) with white text at 70% opacity for links, full opacity for headings. Contains navigation columns (Releases, Artists, Shop, Info), social media links, and a newsletter signup. Padding is `{spacing.xl}` vertical and `{spacing.base}` horizontal.

### Vinyl Variant Swatches
**`vinyl-variant-swatch`** — Small 24px circular color swatches representing different vinyl pressings. Each swatch has a 2px `{colors.hairline}` border. When selected, the border switches to `{colors.ink}` (#313131). The swatch colors draw from the extracted palette: `{colors.vinyl-variant-1}` (#34e2e4), `{colors.vinyl-variant-2}` (#4721fb), `{colors.vinyl-variant-3}` (#ab1dfe), `{colors.vinyl-variant-4}` (#faaca8), `{colors.vinyl-variant-5}` (#fdd79a), `{colors.vinyl-variant-6}` (#67a671).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row); nav bar collapses to hamburger menu; genre tags stack vertically; footer columns stack; search bar reduces to icon-only; product card padding reduces to 12px |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but may condense; genre tags wrap in a horizontal scrollable strip; footer shows 2-column layout; search bar shows full width |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; genre tags in a horizontal filter bar; footer shows 4-column layout; search bar in nav or hero area |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; additional whitespace around content; genre filter bar may expand with more visible tags |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product cards are fully tappable (image + title + price)
- Genre tags have 36px minimum height with generous padding
- Vinyl variant swatches are 24px — borderline for touch; consider 32px on mobile
- Search bar is 44px tall with full-width tap target on mobile

### Collapsing Strategy
- Navigation links collapse into a hamburger/drawer menu below 744px
- Genre filter strip becomes horizontally scrollable on mobile (no wrapping)
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer columns collapse from 4 → 2 → 1
- Secondary navigation (breadcrumbs, sub-links) hides on mobile, shown in drawer
- Search bar collapses to icon-only on mobile, expands on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The only extracted font-family was "WPMenuCart" — likely a widget or plugin font, not the brand's primary typeface. The actual body and heading fonts could not be determined; the system font stack used above is a best-guess fallback. If the brand uses a custom typeface (e.g., a heavy gothic or serif for headings), this should be updated.
- No hover, focus, or active states could be reliably extracted beyond the primary button. All interaction states in this document are inferred from common patterns.
- No error state styling (form validation, 404 pages, empty states) was available.
- The extracted color list is unusually large (30+ colors) and includes many that appear to be WordPress block editor defaults (e.g., #cf2e2e, #ff6900, #fcb900, #f78da7, #abb8c3). The true brand palette may be smaller; the primary blue (#003388) and canvas (#eeeeee) are the most confident picks. The accent colors and vinyl swatches are speculative but grounded in the extraction.
- No dark mode or high-contrast mode styling was detected.
- No animation or transition timing values (durations, easings) were available.
- No typography scale beyond the extracted font-family declaration — all font sizes, weights, and line heights are estimated based on common record-label shop patterns.
- No spacing scale could be extracted; the values above are standard increments.
- No border-radius values could be extracted; all rounding is inferred from the general aesthetic (utilitarian but not harsh, so 4px for buttons, 8px for cards).
- No shadow values were available; the product card shadow is a common default.
- No checkout or cart component styling was available (likely a third-party plugin).
- No mobile navigation drawer styling (overlay, animation, menu item spacing) was available.
