---
version: alpha
name: "Well Go USA"
source_url: "https://www.wellgousa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003399 anchors Well Go USA’s digital storefront — not a friendly sky blue but a serious, cinematic navy that carries the full weight of the brand’s action and martial-arts catalog. Against a black #090808 canvas, this primary blue reads as the voltage of a movie poster’s title treatment, commanding attention without shouting. Two accents cut through the darkness: a marigold #ffc60b that appears on hover states and secondary badges, and a burnt orange #da532c (the theme-color) that flares on CTAs and promotional banners like a stunt explosion. The typography system is absent from extraction — no font-family declarations were found — suggesting a system-ui fallback stack that lets the film stills, poster art, and trailer thumbnails do the expressive work. Cards and navigation panels sit on #5d5d65 muted surfaces, creating a layered hierarchy where the hero image or video player dominates the viewport. The brand trusts its visual assets over typographic ornament: a film’s one-sheet poster is the real headline, and the UI gets out of the way with compact spacing, thin hairlines, and a restrained use of `{rounded.sm}` on buttons and `{rounded.md}` on media cards. The result is a utilitarian, high-contrast interface that feels like browsing a festival catalog — functional, genre-aware, and built to let the movies sell themselves.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#8099cc"
  ink: "#090808"
  body: "#5d5d65"
  muted: "#5d5d65"
  muted-soft: "#8a8a90"
  hairline: "#5d5d65"
  hairline-soft: "#8a8a90"
  canvas: "#090808"
  surface-soft: "#5d5d65"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffc60b"
  accent-orange: "#da532c"
  accent-orange-hover: "#c44a27"
  star-rating: "#ffc60b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
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
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.on-primary}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: "transparent"
    textColor: "{colors.accent-marigold}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-year:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-genre:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    height: "60vh"
    minHeight: "400px"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: "0.8"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-icon:
    textColor: "{colors.muted}"
    size: "20px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.accent-marigold}"
  star-rating:
    textColor: "{colors.star-rating}"
    size: "16px"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  pagination-button:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  video-player-container:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.md}"
    aspectRatio: "16/9"
  trailer-play-button:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 64px
    width: 64px
  cart-button:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Buy Now", "Add to Cart", and "Subscribe" actions. Rendered as a solid navy rectangle with white uppercase text, it sits on the dark canvas with a subtle `{rounded.sm}` corner. On hover, it deepens to `{colors.primary-active}` (#002266); when disabled, it fades to a muted blue-gray `{colors.primary-disabled}` (#8099cc) with no pointer events.

**`button-secondary`** — An outlined variant for secondary actions like "Watch Trailer" or "View Details". Uses a transparent background with a 2px white border, matching the `{colors.on-primary}` text color. On hover, the background fills with a semi-transparent white overlay (not defined as a token, but visually present).

**`button-accent`** — The burnt orange `{colors.accent-orange}` (#da532c) button reserved for promotional CTAs, limited-time offers, and "Pre-Order" actions. It carries the same uppercase `{typography.button-md}` as the primary button but uses the orange as its signal color. On hover, it shifts to `{colors.accent-orange-hover}` (#c44a27).

### Navigation
**`nav-bar`** — A fixed 64px header bar on the black `{colors.canvas}` background. Navigation links use uppercase `{typography.nav-link}` in white, with the active or hover state switching to the marigold `{colors.accent-marigold}` (#ffc60b). The bar contains the Well Go USA logo (typically a text or icon mark in white), a search icon, and a cart icon. On mobile, the nav links collapse into a hamburger menu.

**`nav-link-active`** — Active navigation items are distinguished by the marigold accent color, creating a clear wayfinding signal against the dark header.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` corners that displays a film's poster thumbnail, title, and release year. The poster image occupies a 2:3 aspect ratio with `{rounded.sm}` corners. The title uses `{typography.title-sm}` in `{colors.ink}`, and the year uses `{typography.caption}` in `{colors.muted}`. Cards are typically arranged in a responsive grid with `{spacing.base}` gaps.

**`badge-new`** — A small marigold `{colors.accent-marigold}` pill with dark text, used to flag newly added titles. Uses `{typography.badge}` with tight padding and `{rounded.xs}` corners.

**`badge-genre`** — A muted surface `{colors.surface-soft}` pill with white text, used for genre tags like "Action", "Martial Arts", or "Thriller". Uses `{rounded.full}` pill shape and `{typography.badge}`.

### Hero Section
**`hero-section`** — A full-viewport-height section on the black `{colors.canvas}` background, featuring a large film poster or video still as a background image. The hero title uses `{typography.display-xl}` in white, with a subtitle in `{typography.body-md}` at 80% opacity. A `{button-accent}` CTA sits below the text, typically reading "Watch Now" or "Pre-Order". The section has a minimum height of 400px and scales to 60vh on larger screens.

### Forms & Search
**`text-input`** — A standard input field with a white background, `{rounded.sm}` corners, and a `{colors.hairline}` border. On focus, the border thickens to 2px and switches to `{colors.primary}`. Uses `{typography.body-md}` for input text.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a white background and a search icon in `{colors.muted}`. Used for searching the film catalog by title, actor, or genre. The input text uses `{typography.body-md}`.

### Footer
**`footer`** — A black `{colors.canvas}` footer with muted gray `{colors.muted}` text. Contains links for "About", "Contact", "Privacy Policy", "Terms of Service", and social media icons. Link text uses `{typography.link}` and turns marigold `{colors.accent-marigold}` on hover. The footer has generous `{spacing.section}` padding top and bottom.

### Video & Media
**`video-player-container`** — A 16:9 aspect ratio container on the `{colors.ink}` background, used for embedding trailer videos. The container has `{rounded.md}` corners. A `{trailer-play-button}` — a large 64px orange circle with a white play icon — is centered over the container as the primary interaction.

### Filters & Pagination
**`filter-tag`** — A pill-shaped filter chip on the `{colors.surface-soft}` background with white uppercase text. Used in the "All Films" page to filter by genre, year, or format. The active state (`{filter-tag-active}`) fills with `{colors.primary}`.

**`pagination-button`** — A transparent square button with white text and `{rounded.sm}` corners, used for page navigation at the bottom of film listings. The active page uses `{colors.primary}` as the background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column (1 col); hero section reduces to 50vh; filter tags wrap to 2 rows; search bar moves below hero |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero section at 55vh; filter tags in a horizontal scrollable strip |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at 60vh; filter tags in a single row; pagination visible |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero at 60vh with max-height 600px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements have a minimum height of 44px to meet touch target guidelines.
- Filter tags and badge-genre pills have a minimum tap area of 36px height.
- Nav links have a minimum touch area of 44px height.
- Search bar has a 48px height for comfortable tapping.
- Trailer play button is 64px, well above the minimum.

### Collapsing Strategy
- On mobile (< 744px), the top navigation links collapse into a hamburger menu. The search bar moves from the nav into the hero section or below it.
- Product card grids collapse from 4 columns on wide screens to 3 on desktop, 2 on tablet, and 1 on mobile.
- Filter tags collapse from a single row on desktop to a horizontally scrollable strip on tablet, and to a 2-row wrap on mobile.
- The hero section's title and subtitle stack vertically on mobile, with the CTA button full-width below.
- Footer links stack vertically on mobile, arranged in a single column.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site; the typography block uses a system-ui fallback stack. The brand may use a custom font (e.g., a licensed typeface for posters) that is not applied via CSS on the HTML pages.
- Hover and focus states for text inputs, buttons, and links are inferred from common patterns; exact color values for `button-secondary` hover (semi-transparent overlay) and `text-input-focus` border are not confirmed from extraction.
- Error styling for form inputs (e.g., validation errors, error messages) was not extracted.
- The brand's logo mark (likely a text or icon-based logo) was not analyzed; its exact color, size, and placement in the nav bar are assumed.
- Dark mode is not applicable as the brand already uses a dark canvas (#090808) as its primary background.
- Sub-brand or category-specific color palettes (e.g., for "Action", "Martial Arts", "Drama" sections) were not extracted.
- The exact spacing between product cards in the grid (gap) is inferred as `{spacing.base}` (16px) from common patterns; the actual value may differ.
- The `hero-section` background image handling (overlay gradient, scrim opacity) was not extracted; a black scrim is assumed for text readability.
- The `video-player-container` may use a different aspect ratio (e.g., 21:9 for cinematic trailers) depending on the content.
- The `cart-button` and `search-icon` colors are inferred; the actual icon set (SVG, icon font) is unknown.
- The brand may use a sticky header on scroll; this behavior was not confirmed.
- The `pagination-button` active state may use a different shape (e.g., underlined text instead of a filled rectangle).
