---
version: alpha
name: "Century Media"
source_url: "https://www.centurymedia.store"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label storefront that uses a deep violet #412a78 as its primary brand voltage — a color more often found on a 90s metal album cover than a Shopify checkout — against a near-black #111111 ink and a #121212 canvas that makes the violet glow like a stage light in a dark room. The palette is deliberately stark: #efeef1 and #ebebeb surfaces provide the only relief, while #10b484 teal and #ff0000 red appear as accent badges and sale markers, giving the store a fanzine-meets-ticket-booth energy. Montserrat runs the typography at moderate weights — display sits at 20–24px in weight 500/600, letting album art and band photography carry the emotional weight rather than heavy type. Product cards use soft {rounded.sm} corners on a near-black field, with the violet primary surfacing on add-to-cart buttons and genre tags. The nav bar is a thin strip of #111111 with white text, and the footer collapses into a dense block of links and social icons. The overall effect is a store that feels like a venue lobby: dark, focused, with the primary color hitting like a guitar riff.

colors:
  primary: "#412a78"
  primary-active: "#2e1d54"
  primary-disabled: "#8a7ab3"
  ink: "#111111"
  body: "#121212"
  muted: "#9ca3af"
  muted-soft: "#dedede"
  hairline: "#ebebeb"
  hairline-soft: "#efeef1"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#1f1f1f"
  on-primary: "#ffffff"
  accent-teal: "#10b484"
  accent-red: "#ff0000"
  accent-gray: "#9ca3af"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
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
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.on-primary}"
  social-icon:
    color: "{colors.muted}"
    size: 24px
  social-icon-hover:
    color: "{colors.primary}"
  genre-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  genre-tag-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.on-primary}"
    padding: "{spacing.lg} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The main call-to-action, using the brand's deep violet #412a78 on a near-black canvas. Hover state shifts to a darker #2e1d54, and disabled state lightens to #8a7ab3. Text is uppercase Montserrat at 14px weight 600 with 0.5px letter-spacing. Corners are softly squared at {rounded.sm}. **`button-secondary`** — An outlined variant with transparent background and a white hairline border, used for secondary actions like "View Details" or "Cancel". **`button-accent-teal`** and **`button-accent-red`** — Smaller, denser buttons for sale badges, pre-order flags, or genre-specific CTAs. Teal uses #10b484 with dark ink text; red uses #ff0000 with white text.

### Cards
**`product-card`** — A dark surface card (#1f1f1f) with a softly rounded image area and body text in white. The title uses {typography.title-sm} and the price uses {typography.body-sm} in muted gray. A red badge overlays the top-left corner for sale or new-release items. Cards stack in a responsive grid with {spacing.base} gutters.

### Navigation
**`nav-bar`** — A fixed 60px strip of #111111 with uppercase nav links in white. The active link switches to the primary violet. The bar contains the store logo on the left, genre/category links in the center, and a search icon + cart icon on the right. On mobile, the center links collapse into a hamburger menu.

### Forms
**`text-input`** — A dark input field (#1a1a1a) with a subtle hairline border and white text. On focus, the border switches to the primary violet. Used for search, newsletter signup, and checkout forms. Padding is 12px vertical, 16px horizontal.

### Footer
**`footer`** — A dense block of links, social icons, and legal text on the #111111 background. Links are muted gray by default and switch to white on hover. Social icons are 24px and switch to primary violet on hover. The footer includes columns for "Shop", "Support", "About", and "Connect".

### Badges & Tags
**`genre-tag`** — Pill-shaped tags using the primary violet for active genres and dark gray for inactive ones. Used in the category filter strip and on product cards. Text is 10px uppercase Montserrat weight 700.

### Hero
**`hero-section`** — A full-width banner on the near-black canvas with a large display title and a muted subtitle. Used for featured releases, tour announcements, or seasonal sales. The hero may include a background image or album art that bleeds to the edges.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav links collapse to hamburger; hero text shrinks to {typography.display-md}; footer stacks vertically; search bar becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains two-thirds width; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with genre tags; hero at full width with larger title; footer uses four-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero may include parallax or video background |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Nav bar hamburger icon is 48px × 48px
- Social icons are 24px with 12px padding (effective 48px touch area)
- Product card images are tappable with no minimum size constraint

### Collapsing Strategy
- Nav links collapse to hamburger menu below 744px
- Genre tag strip collapses to a horizontal scrollable row on mobile
- Footer columns stack vertically below 744px
- Product grid reduces columns from 4 to 1 as viewport shrinks
- Hero image may crop or reposition on mobile to maintain focal point

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links were inferred from common patterns; exact extracted hover colors are not available
- Error styling (form validation, error messages, empty states) could not be extracted from the live site
- Dark mode is not applicable as the site already uses a dark canvas (#121212); no light mode variant was observed
- Sub-brand or genre-specific color palettes (e.g., metal vs. punk vs. indie) may exist but were not extracted
- The extracted font list includes Montserrat and system fonts; the exact font stack order and fallbacks are inferred
- Checkout flow styling (Shopify default vs. custom) could not be determined
- Loading states, skeleton screens, and transition animations were not captured
- The extracted hex list includes #9ca3af (muted gray), #10b484 (teal accent), and #ff0000 (red accent); these are used as secondary accents but their exact usage context is inferred
- No meta theme-color was found, suggesting the site may not use a browser chrome color
