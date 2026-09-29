---
version: alpha
name: "Nucleus Films"
source_url: "https://www.nucleusfilms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A monochrome film marketplace built on a single extracted hex — #313131, a deep charcoal that reads as the color of exposed film stock before processing, and which serves as the sole structural anchor across the entire interface. The brand strips away all decorative color, trusting instead the raw contrast of white text on this near-black ground to create a cinema-screen tension. Typography relies on the system font stack — -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif — avoiding any custom typeface investment, which positions the brand as a utility-first platform rather than a premium streaming service. Buttons are hard-cornered rectangles (`{rounded.none}`) with 48px heights and generous 16px horizontal padding, a deliberate anti-pill choice that signals seriousness and editorial neutrality. The top navigation runs a full-bleed `{colors.ink}` bar with white nav links, and the search bar mirrors this inversion — white background, charcoal text, no rounding. Product cards use a white canvas with `{rounded.sm}` corners and a single `{colors.hairline}` border, letting poster art and metadata do all the emotional work. The overall effect is that of a film festival program translated into a database: severe, legible, and utterly dependent on the content it hosts for any warmth.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#8a8a8a"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6a6a6a"
  muted-soft: "#9a9a9a"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  rating-star: "#f5a623"
  badge-new: "#e74c3c"
  badge-sale: "#27ae60"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-new}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0 {spacing.base}"
  product-card-meta:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.rating-star}"
    fontSize: 14px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-ink}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
    marginTop: "{spacing.md}"
  filter-bar:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a hard-cornered rectangle (`{rounded.none}`) in the brand's deep charcoal `{colors.primary}` with white text. At rest, the button sits at 48px height with 12px top/bottom and 24px left/right padding. On hover, the background shifts to `{colors.primary-active}` (#1a1a1a) for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` (#8a8a8a) to signal unavailability without introducing a new color.

**`button-secondary`** — An outlined variant with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Dimensions match the primary button (48px height, 11px 23px padding accounting for the border). On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Disabled state uses `{colors.muted-soft}` text and `{colors.hairline-soft}` border.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` for the text. On hover, the color shifts to `{colors.primary-active}`. Used for "View all" links, "Cancel" actions, and secondary navigation prompts.

### Cards
**`product-card`** — A white card with `{rounded.sm}` (4px) corners and a 1px `{colors.hairline-soft}` border. The card contains a poster image with rounded top corners (`{rounded.sm} {rounded.sm} 0 0`), a title using `{typography.title-sm}`, and metadata using `{typography.caption}` in `{colors.muted}`. On hover, the card elevates with a subtle box-shadow and the border shifts to `{colors.hairline}`. Badges like "NEW" (`{colors.badge-new}`) or "SALE" (`{colors.badge-sale}`) appear as hard-cornered rectangles in the top-left of the image area.

### Navigation
**`nav-bar`** — A full-width, 64px tall bar using `{colors.ink}` background with white text. Navigation links use `{typography.nav-link}` — 14px, weight 500, 0.5px letter-spacing, uppercase — for a cinema-program feel. The active link is underlined with a 2px white border; inactive links use `{colors.muted-soft}`. The bar is fixed to the top of the viewport on desktop and collapses to a hamburger menu on mobile.

### Forms
**`text-input`** — A 48px tall, hard-cornered input with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. On focus, the border becomes a 2px `{colors.primary}` stroke. Error state uses a 2px `{colors.badge-new}` (#e74c3c) border. Padding is 12px vertical, 16px horizontal.

**`search-bar`** — Identical in structure to `text-input` but with a distinct semantic role. The search bar sits in the nav area on desktop and expands to full width on mobile. On focus, the border becomes 2px `{colors.primary}`.

### Footer
**`footer`** — A full-width section using `{colors.ink}` background with `{colors.muted-soft}` text. Links use `{typography.link}` (14px, weight 400) and shift to white on hover. The footer contains three columns on desktop (About, Support, Legal) that stack to a single column on mobile. Padding is 48px vertical, 16px horizontal.

### Hero
**`hero-section`** — A full-bleed section using `{colors.ink}` background with white text. The hero title uses `{typography.display-xl}` (32px, weight 700, -0.5px letter-spacing) and the subtitle uses `{typography.body-md}` in `{colors.muted-soft}`. The section has 64px vertical padding. Used for featured films, collections, and seasonal promotions.

### Filter Bar
**`filter-bar`** — A horizontal strip below the hero with a `{colors.surface-soft}` background and a 1px `{colors.hairline}` bottom border. Filter tags are hard-cornered rectangles (`{rounded.none}`) with white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Active tags invert to `{colors.primary}` background with white text. Tags have 6px vertical and 12px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in single column; search bar becomes full-width below nav; footer stacks to single column; hero padding reduces to 32px vertical; filter bar scrolls horizontally with overflow-x |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; search bar sits in nav row; footer in 2 columns; filter tags wrap to 2 rows |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; search bar in nav with 400px max-width; footer in 3 columns; filter tags in single row |
| Wide | > 1440px | Content max-width at 1440px with auto margins; product cards in 4-column grid; nav bar max-width at 1440px; hero content centered with 800px max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Filter tags are 32px tall — below the 44px recommendation — but are spaced with 8px gaps to reduce mis-taps
- Nav hamburger icon is 44x44px on mobile
- Product card tap targets (title, image, meta) are the full card width

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; the hamburger icon reveals a full-screen overlay with all nav links stacked vertically
- Footer columns collapse from 3 to 2 at tablet, then to single column at mobile
- Product card grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Filter bar switches from a single horizontal row to a horizontally scrollable strip on mobile, with a "Filters" button that opens a modal for advanced filtering
- Search bar moves from the nav row (desktop) to a full-width element below the nav (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one extracted hex color (#313131) was available from the live site; all other colors in this system are inferred from common web patterns and the brand's monochrome aesthetic. The true secondary palette (if any) could not be determined.
- No custom font family was detected; the site uses the system font stack. A custom typeface may be used in production but was not present in the extracted CSS.
- Hover and focus states for all components are speculative — the live site may use different transitions, box-shadows, or color shifts.
- Error styling for forms (text-input-error) is inferred from common patterns; the actual error color and border treatment may differ.
- Badge colors (#e74c3c for "NEW", #27ae60 for "SALE") are assumed from common e-commerce patterns; the brand may use different accent colors or no badges at all.
- Rating star color (#f5a623) is a standard gold; the brand may use a different accent or no rating system.
- Dark mode is not supported in this system; the brand may or may not offer it.
- Sub-brand or seasonal palette variations (e.g., for film festivals or curated collections) are not captured.
- The meta theme-color tag was absent from the extracted hints; the browser chrome color is unknown.
- Animation timing, easing curves, and transition durations are not specified.
