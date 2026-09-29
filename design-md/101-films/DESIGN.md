---
version: alpha
name: "101 Films"
source_url: "https://101-films.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A film distributor’s site that feels more like a collector’s shelf than a streaming grid, anchored on a slate-blue #52636b that reads as archival rather than corporate — the kind of color you’d find on a 35mm film canister. The primary action color is a stark #dd1d0b, a red that lands with the blunt force of a cinema exit sign, used sparingly for purchase buttons and price badges so it never competes with the poster art. The canvas is a cool #cccacc, a near-gray that avoids the sterile white of modern ecommerce and instead suggests a repurposed warehouse wall. Typography runs Cabin for display and body, a geometric sans with a humanist warmth that keeps the experience from feeling cold despite the muted palette. Product cards use soft corners ({rounded.sm}) and thin hairlines (#d6d8db) to frame DVD and Blu-ray covers without overwhelming them. The navigation is a horizontal strip of genre and collection links, each sitting in a low-contrast state until hovered, when the red #dd1d0b appears as an underline — a restrained gesture that lets the filmography do the selling. The overall mood is that of a specialty video store that has been carefully curated but not over-designed: the interface steps back so the movies can step forward.

colors:
  primary: "#dd1d0b"
  primary-active: "#bd2130"
  primary-disabled: "#f1b0b7"
  ink: "#1b1e21"
  body: "#383d41"
  muted: "#545b62"
  muted-soft: "#818182"
  hairline: "#d6d8db"
  hairline-soft: "#dae0e5"
  canvas: "#cccacc"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#004085"
  accent-green: "#155724"
  accent-teal: "#0c5460"
  accent-yellow: "#856404"
  accent-red: "#721c24"
  border-strong: "#b9bbbe"
  border-focus: "#80bdff"
  border-input: "#c8cbcf"

typography:
  display-xl:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Cabin', 'Montsemi', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 48px 24px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Basket" and checkout flows. Rendered in the brand red #dd1d0b with white text and 8px rounded corners. On hover, it shifts to #bd2130 for a darker, more urgent state. The disabled variant uses a pale pink #f1b0b7 to signal inactivity without introducing a new color. Height is 44px with 12px/24px padding — compact enough for product rows but substantial enough for cart actions.

**`button-secondary`** — Used for secondary actions like "View Details" or "Continue Shopping." It takes the canvas color #cccacc with ink text and a 1px hairline border (#d6d8db). The hover state darkens the background slightly to #dae0e5. This button sits visually behind the primary, letting the red button lead.

**`button-tertiary-text`** — A text-only button for links like "Cancel" or "Clear Filters." It uses the primary red for text on a transparent background, with no border or fill. Hover adds an underline to reinforce the link-like behavior.

### Cards
**`product-card`** — The core product display unit for DVD and Blu-ray titles. A white card (#ffffff) with 8px rounded corners and a thin 1px hairline border (#d6d8db). The card contains a poster image (full-width, top-aligned), the film title in body-md, the release year in body-sm (muted), and a price badge in the bottom-right corner. The card has no shadow — it relies on the contrast between the white surface and the cool gray canvas (#cccacc) to float. On hover, the border shifts to #b9bbbe for a subtle lift.

**`product-card-badge`** — A small red label affixed to product cards to indicate format (e.g., "Blu-ray", "Limited Edition") or sale status. Uses 4px rounded corners, 2px/8px padding, and the badge typography at 11px uppercase.

### Navigation
**`nav-bar`** — A 64px horizontal bar using the canvas color (#cccacc) as background. Navigation links use uppercase 14px Cabin at 500 weight with 0.5px letter spacing. The active page or hovered link gets a 2px bottom border in the primary red (#dd1d0b). The nav includes a logo lockup on the left (text-based, using display-md weight 700) and genre/collection links on the right. On mobile, the nav collapses into a hamburger menu.

**`category-pill`** — Used for filtering products by genre (Horror, Thriller, Cult, etc.). A pill-shaped button with 16px horizontal padding and 6px vertical padding, set in 13px uppercase Cabin. The inactive state uses a soft background (#ececf6) with body text (#383d41). The active state flips to the primary red with white text.

### Forms
**`text-input`** — Standard text input for search and newsletter signup. A white background with 8px rounded corners, 10px/14px padding, and a 1px border in #c8cbcf. On focus, the border shifts to #80bdff (a blue focus ring) with a 2px outline. The height is 44px to match button height for aligned form rows.

**`search-bar`** — A pill-shaped search field with full rounding (9999px) for the site search. It uses the same dimensions as text-input but with 20px horizontal padding to accommodate the rounded ends. A magnifying glass icon sits on the left in muted (#545b62).

### Footer
**`footer-link`** — Standard text links in the site footer, set in 14px Cabin at 400 weight with muted color (#545b62). Links are stacked vertically in columns (About, Collections, Customer Service, Social). On hover, they shift to the primary red. The footer background uses the canvas color (#cccacc) with a top hairline border (#d6d8db) to separate it from the main content.

### Hero
**`hero-section`** — A full-width banner used on the homepage and collection pages. It uses the accent blue (#004085) as background with white text, creating a strong contrast against the rest of the site's cool gray palette. The hero contains a headline in display-xl (32px, 700 weight) and a subtitle in body-md. Padding is 48px top/bottom and 24px left/right. On collection pages, the hero may feature a film still as a background image with a dark scrim overlay.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards; nav collapses to hamburger; hero padding reduces to 32px; category pills wrap to two rows; search bar moves below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but font size drops to 13px; hero uses 28px display text; category pills in a horizontal scrollable strip |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; hero at full width with 32px display text; search bar in nav bar |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with auto margins; hero content centered with 640px max-width |

### Touch Targets
- All tappable elements (buttons, links, pills) maintain a minimum 44px height for touch accessibility
- Product cards have a minimum 120px width on mobile to ensure tap targets are distinct
- Category pills are at least 32px tall with 16px horizontal padding for finger-friendly tapping
- Search bar height remains 44px across all breakpoints

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px; the hamburger button is 44x44px with a 32px icon
- Product grid collapses from 4 columns to 1 column as viewport shrinks
- Category pills change from a horizontal scrollable strip on tablet to a wrapped grid on mobile
- Hero section reduces vertical padding from 48px to 32px on mobile
- Footer columns stack from 4 columns to 2 columns on tablet, then to 1 column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex color list is dominated by Bootstrap alert colors (blues, greens, reds, yellows) and generic grays, making it difficult to isolate the brand's true secondary palette. The primary red (#dd1d0b) and slate blue (#52636b) are the most distinctive colors; all other extracted colors are treated as system defaults or edge cases.
- Font-family declarations included "Cabin" and "Montsemi" — the latter may be a misspelling of "Montserrat" or a custom font. Without a verified font file or CSS @font-face rule, "Montsemi" is included as-is in the typography stack but may not render.
- Hover and focus states for text inputs and buttons are inferred from Bootstrap defaults (#80bdff focus ring) rather than extracted from the live site.
- Error state styling for forms (red borders, error messages) is not present in the extracted data and uses Bootstrap-adjacent defaults (#721c24 for error text).
- Dark mode is not supported; the site uses a light canvas (#cccacc) throughout.
- The brand's logo font and exact sizing could not be extracted; the logo is assumed to be text-based using Cabin at display-md weight.
- No extracted data for loading states, skeleton screens, or empty states.
