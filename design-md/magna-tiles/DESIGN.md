---
version: alpha
name: "Magna-Tiles"
source_url: "https://www.magnatiles.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A primary-blue #2346da and crimson #e11d48 voltage runs through every CTA, badge, and interactive element on a near-black #171717 canvas — a system that reads as bold, primary-colored, and unapologetically child-directed. The brand trusts saturated accent colors (violet #9c00ff, orange #ff7e27) over photography to create hierarchy, with product tiles floating on a light gray #dedede surface that keeps the focus on the translucent, geometric tiles themselves. Inter at 400–700 weight handles all type, set at generous sizes for readability by small hands and adult shoppers alike. Buttons are pill-shaped (`{rounded.full}`) in the brand blue, while secondary actions use the crimson as a high-alert accent — a pattern that echoes the magnetic snap of the product. The nav bar sits at 64px with a clean white background and the logo centered, a restrained choice for a brand whose product is anything but restrained. There is no subtlety here: every color is at full saturation, every CTA is a pill, every edge is soft, and the overall effect is of a toy box organized by a very confident designer.

colors:
  primary: "#2346da"
  primary-active: "#1a35a8"
  primary-disabled: "#a0b0e8"
  ink: "#171717"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-crimson: "#e11d48"
  accent-violet: "#9c00ff"
  accent-orange: "#ff7e27"
  product-bg: "#dedede"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent-crimson:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-accent-crimson-active:
    backgroundColor: "#b01538"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image-wrapper:
    backgroundColor: "{colors.product-bg}"
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.on-primary}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full pill in brand blue `#2346da`. On hover, it shifts to `{colors.primary-active}` (`#1a35a8`). The disabled state uses `{colors.primary-disabled}` (`#a0b0e8`) with full opacity — no dimming. Text is white `{colors.on-primary}` set in `{typography.button-md}` at 600 weight.

**`button-secondary`** — An outlined pill variant with a white fill and a 2px `{colors.primary}` border. Text remains brand blue. Used for secondary actions like "Learn More" or "View Details" alongside primary buttons. Hover state fills the background with `{colors.primary}` and flips text to white.

**`button-accent-crimson`** — The high-energy accent button in `{colors.accent-crimson}` (`#e11d48`). Used for the most urgent CTAs — "Shop Now" in hero sections, "Add to Cart" on product pages. Hover darkens to `#b01538`. This is the brand's secondary voltage, visually louder than the primary blue.

**`button-pill-outline`** — A thin, subtle outline pill with a transparent background and a 1px `{colors.hairline}` border. Used for filter toggles, sort options, and tertiary actions. Hover fills with `{colors.surface-soft}`.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners and 16px padding. The image area sits on a `{colors.product-bg}` (`#dedede`) background at a 1:1 aspect ratio with `{rounded.sm}` (8px) corners — a soft container for the translucent tile photography. Below, the title uses `{typography.title-sm}` and the price uses `{typography.body-md}` at 600 weight. An optional `{colors.accent-crimson}` badge can overlay the top-left of the image area for promotions.

### Navigation
**`nav-bar`** — A 64px white bar with centered logo and left/right nav links. Links use `{typography.nav-link}` (14px, 500 weight) and turn `{colors.primary}` on active page. The bar is fixed on scroll with a subtle `{colors.hairline}` bottom border. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — A standard input with white background, 12px padding, `{rounded.sm}` (8px) corners, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Placeholder text uses `{colors.muted-soft}`. Error state uses a 2px `{colors.accent-crimson}` border.

### Hero
**`hero-section`** — A full-width section on a `{colors.ink}` (`#171717`) background with white text. The heading uses `{typography.display-xl}` (36px, 700 weight) and the subheading uses `{typography.body-md}` in `{colors.muted-soft}`. The CTA is a `{colors.accent-crimson}` pill using `{typography.button-lg}` (18px, 600 weight) with 14px vertical padding. This is the brand's most dramatic layout — dark canvas, bright accent, no photography competing.

### Search
**`search-bar`** — A full pill (`{rounded.full}`) with white background, 12px vertical padding, and a 1px `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`. Used on the product listing page and in the mobile nav overlay. Height is 48px.

### Footer
**`footer`** — A dark section on `{colors.ink}` with `{colors.muted-soft}` text. Links use `{typography.link}` (14px, 500 weight) and lighten to `{colors.on-primary}` on hover. Column headings use `{typography.title-sm}` in white. The footer is divided into 3–4 columns on desktop, collapsing to a single column on mobile.

### Badges
**`badge-new`** — A small pill in `{colors.accent-violet}` (`#9c00ff`) used to flag new products or collections. Text is white, set in `{typography.badge}` (11px, 700 weight, uppercase). Padding is 2px vertical and 8px horizontal.

**`badge-sale`** — A small pill in `{colors.accent-orange}` (`#ff7e27`) used for sale or clearance items. Same typography and sizing as `badge-new`. These badges are the brand's way of creating urgency without relying on photography or layout changes.

### Category Pills
**`category-pill`** — A 36px tall pill with `{colors.surface-soft}` background and `{colors.ink}` text. Used in a horizontal scrollable strip for filtering product categories. The active state fills with `{colors.primary}` and flips text to white. This is the primary navigation pattern on the product listing page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero padding reduces to 32px; category pills scroll horizontally with no wrap; footer stacks to single column; search bar moves to sticky top |
| Tablet | 744–1128px | Nav links remain visible but compact; product cards in 2-column grid; hero heading reduces to 28px; category pills show 4–5 visible items |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full padding; category pills show 6–8 visible items |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 800px |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons at 48px, category pills at 36px — note: pills are below recommended minimum and should be reviewed for accessibility)
- Icon buttons at 40x40px
- Nav links have minimum 44px tap area even if text is smaller
- Search bar at 48px height for easy tapping

### Collapsing Strategy
- Primary nav: hamburger menu at < 744px, full bar at ≥ 744px
- Product grid: 1 column mobile, 2 tablet, 3 desktop, 4 wide
- Footer: 1 column mobile, 2 tablet, 3–4 desktop
- Category pills: horizontal scroll on mobile, full visible row on tablet+
- Hero: reduced padding and smaller heading on mobile; full treatment on tablet+

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and outline buttons were not reliably extracted — the `button-secondary` hover behavior (fill with primary) is inferred from common patterns, not confirmed from the live site
- Error styling for forms (error text color, icon placement, border animation) could not be extracted
- The `scrim` color (`#121212`) is used for overlay backgrounds but the exact opacity value (likely 60–80%) was not extractable
- Dark mode is not supported by the live site — all pages use a white or near-black canvas with no media query toggle
- Sub-brand or collection-specific palettes (e.g., "Magna-Tiles Farm" or "Magna-Tiles Arctic") may exist but were not captured in the extraction
- The `font-family: inherit!important` declaration suggests some elements inherit from a parent — the exact cascade for headings vs. body could not be fully resolved
- Animation durations and easing curves (e.g., button hover transitions, card hover lifts) were not extractable
- The extracted color list includes `#121212` which is very close to `#171717` — the latter is used as the primary dark canvas based on frequency, but the distinction between the two may be intentional (e.g., `#121212` for scrims, `#171717` for backgrounds)
