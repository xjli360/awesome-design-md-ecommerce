---
version: alpha
name: "Nonesuch Records"
source_url: "https://www.nonesuch.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label and shop where the page itself feels like a listening room — dark, quiet, and entirely in service of the music. The canvas is a deep, ink-black (#000000) that pushes every album cover, track title, and concert date forward with the clarity of a gallery wall. There are no decorative flourishes, no gradients, no brand pattern — just a single white (#ffffff) body text on black, with a muted gray (#808080) for secondary metadata like release dates and catalog numbers. The primary action color is a restrained blue (#0066cc) used sparingly for links and the single "Shop" CTA, never competing with the album art. Typography runs a clean sans-serif stack — likely a system font or a neutral workhorse like Helvetica — at modest weights (400 for body, 600 for headings), with the album title itself acting as the hero display at 24px. Cards are sharp-cornered (`{rounded.none}`) rectangles, letting the square album cover dictate the geometry; the only softness comes from the 8px radius (`{rounded.sm}`) on the search bar and the 4px radius (`{rounded.xs}`) on small badge elements. The nav is a thin, fixed black strip with white text and a subtle 1px bottom border (`{colors.hairline}`) that barely separates it from the content. This is a brand that trusts its product — the music — to do the talking, and the design gets out of the way.

colors:
  primary: "#0066cc"
  primary-active: "#0052a3"
  primary-disabled: "#4d94cc"
  ink: "#000000"
  body: "#ffffff"
  muted: "#808080"
  muted-soft: "#a0a0a0"
  hairline: "#333333"
  hairline-soft: "#262626"
  canvas: "#000000"
  surface-soft: "#1a1a1a"
  surface-card: "#111111"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#0066cc"
  link-hover: "#3399ff"
  badge-new: "#ff6600"
  badge-sale: "#cc0000"
  star-rating: "#ffcc00"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.body}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.primary}"
  text-input-placeholder:
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.body}"
    borderBottom: "2px solid {colors.body}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.md}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  footer-link-hover:
    textColor: "{colors.body}"
  social-icon:
    textColor: "{colors.muted}"
    height: 20px
  social-icon-hover:
    textColor: "{colors.body}"
  track-list-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  track-list-item-hover:
    backgroundColor: "{colors.surface-soft}"
  track-list-number:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    width: 24px
  track-list-title:
    typography: "{typography.body-md}"
  track-list-duration:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Buy Now", and "Subscribe". A solid blue (`{colors.primary}`) rectangle with zero rounding (`{rounded.none}`), white text, and a 40px height. On hover and active states, the background deepens to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}` to signal unavailability without introducing a new color.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Pre-Order". Uses a transparent background with a 1px `{colors.hairline}` border. On hover, the border becomes white and the background shifts to `{colors.surface-soft}`. Height and padding match the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button for inline actions like "Learn More" or "See All". No background, no border. Uses `{typography.button-md}` and inherits the parent text color. Hover state adds an underline.

### Navigation
**`nav-bar`** — A fixed top bar, 56px tall, with a black (`{colors.canvas}`) background and a subtle 1px bottom border (`{colors.hairline}`). Navigation links are uppercase (`{typography.nav-link}`) with 0.5px letter spacing. The active link has a 2px white bottom border; inactive links are `{colors.muted}`. The bar contains the Nonesuch logo (left), nav links (center), and a search icon (right).

### Cards
**`product-card`** — A minimal, square card for displaying album releases. The card has no background fill (inherits `{colors.canvas}`) and no rounding (`{rounded.none}`). The album cover image fills a 1:1 aspect ratio. Below the image, the title uses `{typography.title-sm}`, the artist name uses `{typography.body-sm}` in `{colors.muted}`, and the price uses `{typography.body-md}` with a 600 weight. No shadows, no borders — the album art is the card.

### Forms
**`text-input`** — A standard input field for search, newsletter signup, and checkout forms. Uses a `{colors.surface-card}` background with a 1px `{colors.hairline}` border and zero rounding (`{rounded.none}`). On focus, the border switches to `{colors.primary}`. Placeholder text is `{colors.muted}`. Height is 44px with 12px/16px padding.

**`search-bar`** — The only component with rounding (`{rounded.sm}`). A dedicated search input with a `{colors.surface-card}` background and a 1px `{colors.hairline}` border. On focus, the border becomes `{colors.primary}`. Includes a magnifying glass icon on the left.

### Track Lists
**`track-list-item`** — A row in an album's track listing. Each row contains a track number (24px wide, `{colors.muted}`), the track title (`{typography.body-md}`), and the duration (`{colors.muted}`, `{typography.caption}`). Rows are separated by a 1px `{colors.hairline-soft}` border. On hover, the entire row gets a `{colors.surface-soft}` background.

### Badges
**`badge-new`** — A small orange (`{colors.badge-new}`) badge for new releases. Uses `{typography.badge}` (10px, uppercase, 700 weight) with 2px/6px padding and `{rounded.xs}`.

**`badge-sale`** — A red (`{colors.badge-sale}`) badge for sale items. Same typography and sizing as `badge-new`.

### Footer
**`footer`** — A full-width footer with a black background and a 1px `{colors.hairline}` top border. Links are `{colors.muted}` and `{typography.caption}`; on hover they become `{colors.body}`. Social icons are 20px tall and also `{colors.muted}` with a white hover state. Padding is `{spacing.xxl}` top and bottom.

### Hero
**`hero-section`** — A full-width section at the top of the homepage or artist pages. Uses the black canvas with white text. The heading uses `{typography.display-xl}` (24px, 600 weight), and the subheading uses `{typography.body-md}` in `{colors.muted}`. A primary button sits below the subheading. No background image — the hero relies on typography and whitespace.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards (1 column). Nav links collapse into a hamburger menu. Track list items stack with full-width rows. Hero heading drops to 20px. Footer links stack vertically. |
| Tablet | 744–1128px | Two-column grid for product cards. Nav links remain visible but condensed. Track list items have a 24px left margin for track numbers. Hero heading at 24px. |
| Desktop | 1128–1440px | Three-column grid for product cards. Full nav with all links visible. Track list items have a 48px left margin. Hero section has 64px top padding. |
| Wide | > 1440px | Four-column grid for product cards. Max-width container at 1440px, centered. Hero section has 80px top padding. |

### Touch Targets
- All buttons and links: minimum 44px height for touch targets.
- Search bar: 44px height, 44px minimum width.
- Nav links: 44px tap area (even if text is smaller).
- Product cards: entire card is tappable, minimum 120px height.
- Track list items: 44px minimum height per row.

### Collapsing Strategy
- **Mobile nav**: Full nav links collapse into a hamburger icon. The search bar moves into the hamburger menu or becomes a persistent icon.
- **Product grid**: Collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- **Track list**: Track numbers are hidden on mobile to save horizontal space; only title and duration remain.
- **Footer**: Multi-column footer links collapse into a single vertical stack on mobile.
- **Hero**: On mobile, the hero subheading is hidden to reduce vertical space.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family**: No font-family declarations were extracted from the live site. The typography block uses a generic sans-serif stack (Helvetica Neue, Helvetica, Arial) as a placeholder. The actual brand font (likely a custom or licensed typeface) is unknown.
- **Color palette**: No hex colors were extracted from the live site (the page returned "Access Denied"). The colors in this file are inferred from the brand's visual identity (black, white, blue, gray) and common record-label design patterns. They should be verified against the actual site.
- **Hover states**: Hover colors for buttons, links, and cards are estimated. Actual hover transitions (ease, duration) are unknown.
- **Error states**: No form error styling (red borders, error messages) was extracted. A generic red (`#cc0000`) is assumed for error text.
- **Dark mode**: The site is already dark (black background), so no separate dark mode is defined. However, if the site has a light mode variant, it is not captured here.
- **Sub-brand palettes**: Nonesuch may have sub-brands or series (e.g., "Nonesuch Explorer Series") with distinct color treatments. These are not included.
- **Animation and transitions**: No CSS transition properties were extracted. The site likely uses subtle fades or instant state changes.
- **Checkout flow**: The shopping cart and checkout pages were not accessible. Their styling (form fields, payment buttons, order summary) is not captured.
- **Accessibility**: Contrast ratios, focus indicators, and screen-reader labels are not defined. The black-on-white and white-on-black combinations likely pass WCAG AA, but specific ratios are unverified.
