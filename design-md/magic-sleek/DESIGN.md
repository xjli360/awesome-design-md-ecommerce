---
version: alpha
name: "Magic Sleek"
source_url: "https://www.magicsleek.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Magic Sleek presents itself as a clinical yet approachable haircare brand, built on a foundation of clean whites and cool grays that communicate precision and safety. The palette is anchored by a deep charcoal ink (`#1f2124`) for body text, set against a bright canvas (`#fcfbfe`) that feels almost sterile — a deliberate choice for a brand selling a "formaldehyde-free" straightening system. Accents of teal (`#5eead4`) and deep green (`#108474`) appear sparingly, suggesting natural or botanical efficacy, while a single punch of magenta (`#cc3366`) provides the only real warmth, used sparingly for badges or highlights. The typographic voice leans on `Nunito Sans` and `Open Sans` — rounded, approachable sans-serifs that soften the clinical edge — with `{rounded.full}` pill-shaped buttons and `{rounded.sm}` card corners that keep the interface feeling human rather than cold. Muted grays like `#69727d` and `#515151` handle secondary text and hairlines, while `{rounded.lg}` is reserved for hero images and product photography, creating a consistent visual rhythm of soft containment. The overall effect is trustworthy, modern, and slightly spa-like — a brand that wants you to feel both informed and pampered.

colors:
  primary: "#cc3366"
  primary-active: "#a62952"
  primary-disabled: "#e9a3b9"
  ink: "#1f2124"
  body: "#333333"
  muted: "#69727d"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#e9e6ed"
  canvas: "#fcfbfe"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#5eead4"
  accent-green: "#108474"
  accent-purple: "#720eec"
  badge-magenta: "#cc3366"
  badge-new: "#5eead4"
  star-rating: "#958e09"
  error: "#c13515"
  success: "#108474"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px

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
    rounded: "{rounded.full}"
    padding: 14px 32px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  button-pill-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
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
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-new-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
  badge-accent:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in the brand's signature magenta (`{colors.primary}`). On hover, it deepens to `{colors.primary-active}` for clear feedback. The disabled state uses `{colors.primary-disabled}` to visually communicate inactivity while maintaining brand consistency. Used for "Add to Cart", "Book Now", and primary form submissions.

**`button-secondary`** — An outlined variant with a white fill and magenta border, used for secondary actions like "Learn More" or "View Details". On active state, the border shifts to `{colors.primary-active}` and the background to `{colors.surface-soft}`. Maintains the same `{rounded.full}` pill shape for visual harmony.

**`button-tertiary`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Skip". Relies on `{typography.button-md}` weight for clarity and uses `{colors.ink}` for text color. Hover state adds a subtle underline.

**`button-pill-teal`** — A secondary accent button using the brand's teal (`{colors.accent-teal}`) for promotional or highlight actions. Typically used for "Shop Sale" or "New Arrivals" CTAs where the brand wants to draw attention without using the primary magenta.

### Cards
**`product-card`** — The standard product display card with a white background (`{colors.surface-card}`), soft rounded corners (`{rounded.md}`), and consistent padding (`{spacing.base}`). Product images sit within `{rounded.sm}` corners inside the card. Text uses `{typography.body-sm}` for descriptions and `{typography.title-sm}` for product names.

**`product-card-badge`** — A small pill-shaped badge overlaid on product cards, using the brand magenta (`{colors.badge-magenta}`) for sale or promotion indicators. Rendered in uppercase `{typography.badge}` for compact readability.

**`product-card-new-badge`** — A teal variant of the badge (`{colors.badge-new}`) specifically for "New" indicators, using dark text (`{colors.ink}`) for contrast against the bright teal background.

### Navigation
**`nav-bar`** — The primary site navigation, a clean white bar (`{colors.canvas}`) with a subtle bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` with `{colors.ink}` text. Active links switch to `{colors.primary}` with a 2px bottom border for clear active state indication.

**`nav-link-active`** — The active navigation state, distinguished by the brand's magenta color and a bottom border, providing clear wayfinding for the current page or section.

### Forms
**`text-input`** — Standard text input fields with a white background, `{rounded.sm}` corners, and a light gray border (`{colors.hairline}`). On focus, the border thickens to 2px and switches to `{colors.primary}` for clear interaction feedback. Error states use a 2px red border (`{colors.error}`) with accompanying error text in `{colors.error}`.

### Hero
**`hero-section`** — The primary hero banner area, using a soft gray background (`{colors.surface-soft}`) with `{rounded.lg}` corners at the bottom. Headlines use `{typography.display-xl}` for maximum impact, with generous padding (`{spacing.section}`) creating a spacious, editorial feel.

**`hero-cta`** — The hero's primary call-to-action button, larger than standard buttons with `16px 40px` padding for visual prominence. Uses the same `{rounded.full}` pill shape and `{colors.primary}` background as the standard primary button.

### Footer
**`footer`** — The site footer uses a dark background (`{colors.ink}`) with white text (`{colors.canvas}`) for strong contrast. Links are rendered in `{colors.muted-soft}` to reduce visual weight while maintaining readability. The footer contains site maps, legal links, and social media icons.

### Badges
**`badge-accent`** — A purple accent badge (`{colors.accent-purple}`) used for limited-time offers or exclusive content. Shares the same `{rounded.full}` pill shape and `{typography.badge}` typography as other badges, maintaining consistency across badge variants.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; product cards stack in single column; hero padding reduces to `{spacing.xl}`; buttons become full-width; search bar moves to top of page |
| Tablet | 744–1128px | Navigation shows condensed links; product cards display in 2-column grid; hero maintains `{rounded.lg}` but reduces padding; search bar remains in header |
| Desktop | 1128–1440px | Full navigation with all links; product cards in 3-column grid; hero at full `{spacing.section}` padding; search bar in header with expanded width |
| Wide | > 1440px | Maximum content width of 1440px; hero becomes full-width with `{rounded.lg}` at bottom only; product cards maintain 3-column grid with increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons and badge elements maintain minimum 32px touch target
- Navigation links have 48px minimum tap area on mobile
- Product card CTAs are at least 48px tall for easy tapping

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid collapses from 3 columns to 2 columns at tablet, then 1 column at mobile
- Footer link columns collapse to single column below 744px
- Hero section reduces vertical padding by 50% on mobile
- Search bar moves from header to prominent top position on mobile
- Secondary navigation (category strip) collapses to horizontal scroll on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for text-input fields beyond focus (e.g., hover border color change)
- Error state styling for select dropdowns and checkboxes
- Loading state animations and skeleton screen designs
- Dark mode color palette and component adjustments
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition)
- Detailed typography scale for mobile-specific font sizes
- Specific transition durations and easing curves for animations
- Shadow/elevation system for cards and modals
- Modal and overlay component specifications
- Tooltip and popover design details
- Form validation message styling (success, warning, info)
- Social media icon specifications and color variants
- Image aspect ratios and cropping behavior for product photos
- Video player component styling
- Accordion and tab component specifications
- Pagination and infinite scroll design details
- Cookie consent banner styling
- Accessibility focus ring specifications (color, width, offset)
