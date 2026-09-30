---
version: alpha
name: "Milkweed Editions"
source_url: "https://milkweed.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A literary publisher whose visual system is built on the tension between warm, earthy tones and a clean, airy canvas. The extracted palette reveals a surprising range: a deep, almost charcoal ink (#353434) grounds the body text, while a muted sage-gray (#7993a5) and a soft, dusty blue (#5b6f80) create a quiet, contemplative atmosphere. The most distinctive accent is a burnt orange (#e87746), used sparingly for primary CTAs and navigation highlights, providing a warm, human pulse against the cool grays. The brand leans heavily on serif typography—Goudy Old Style, Palatino, and Warnock Pro for display and body text—evoking a sense of literary tradition and authority. This is paired with a clean, geometric sans-serif (GothamSSm, SentinelSSm) for UI elements like buttons and navigation, creating a subtle but deliberate hierarchy: the serif speaks, the sans-serif acts. The overall mood is one of refined simplicity; generous whitespace and soft, rounded corners (`{rounded.sm}` on cards, `{rounded.md}` on buttons) prevent the system from feeling cold or academic. The primary canvas is a near-white (#f0f0f0), with a slightly warmer surface-soft (#edecec) for cards, giving the site a tactile, paper-like quality that mirrors the physical books it publishes.

colors:
  primary: "#e87746"
  primary-active: "#d46633"
  primary-disabled: "#f4b89a"
  ink: "#353434"
  body: "#454545"
  muted: "#5b6f80"
  muted-soft: "#7993a5"
  hairline: "#c7d7e0"
  hairline-soft: "#e4e4e4"
  canvas: "#f0f0f0"
  surface-soft: "#edecec"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-sage: "#7993a5"
  accent-dusty-blue: "#5b6f80"
  accent-warm-gray: "#c7c1ba"
  badge-green: "#198754"
  badge-blue: "#0d6efd"

typography:
  display-xl:
    fontFamily: "'Goudy Old Style', 'Warnock Pro', Palatino, 'Book Antiqua', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Goudy Old Style', 'Warnock Pro', Palatino, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Goudy Old Style', 'Warnock Pro', Palatino, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  title-sm:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  body-md:
    fontFamily: "'Goudy Old Style', 'Warnock Pro', Palatino, 'Book Antiqua', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Goudy Old Style', 'Warnock Pro', Palatino, 'Book Antiqua', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.75px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.75px
    textTransform: uppercase
  link:
    fontFamily: "'Goudy Old Style', 'Warnock Pro', Palatino, 'Book Antiqua', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'GothamSSm', 'SentinelSSm', Helvetica, Arial, sans-serif"
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
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
    border: "2px solid {colors.badge-blue}"
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
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "2/3"
  badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-award:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "16px 32px"
    height: 56px
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    border-bottom: "2px solid {colors.primary}"
    padding-bottom: "{spacing.sm}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the burnt orange `{colors.primary}` on a clean white `{colors.on-primary}` label. The button is set in uppercase `{typography.button-md}` with generous letter-spacing, giving it a confident, editorial weight. On hover, it shifts to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}`. The `{rounded.md}` corners keep it approachable without sacrificing formality.

**`button-secondary`** — An outlined variant for secondary actions, using a 2px solid `{colors.ink}` border on a `{colors.canvas}` background. The text remains in uppercase `{typography.button-md}`, maintaining the same typographic rhythm as the primary. On hover, the background fills with `{colors.surface-soft}` for a subtle tactile response.

**`button-tertiary-text`** — A text-only link styled as a button, used for inline actions like "Read More" or "View All." The text color is `{colors.primary}`, and it uses the same uppercase `{typography.button-md}` to maintain visual consistency across the button family. No background or border — it relies on the brand's accent color for emphasis.

### Cards
**`product-card`** — A book cover card with a soft `{rounded.sm}` corner and a `{colors.surface-card}` background. The card uses a 2:3 aspect ratio for the cover image, mimicking the proportions of a physical book. On hover, a subtle box-shadow lifts the card from the page, creating a gentle depth effect. The body text uses `{typography.body-sm}` for the book title and author, with the title in `{colors.ink}` and the author in `{colors.muted}`.

**`badge-new`** — A small, green (`{colors.badge-green}`) badge for new releases, set in `{typography.badge}` uppercase. The `{rounded.xs}` corners keep it compact and unobtrusive, sitting in the top-right corner of the product card image.

**`badge-sale`** — A burnt orange (`{colors.primary}`) badge for sale items, using the same compact `{typography.badge}` styling. It visually echoes the primary button color, creating a subtle connection between the badge and the call-to-action.

**`badge-award`** — A sage-green (`{colors.accent-sage}`) badge for award-winning titles, using the brand's secondary accent color to denote prestige without competing with the primary action.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, using a clean `{colors.canvas}` background with a thin `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` in uppercase with `{colors.ink}` text. The active state is indicated by a 2px `{colors.primary}` bottom border and a color shift to `{colors.primary}`.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a `{colors.canvas}` background and a `{colors.hairline}` border. On focus, the border thickens to 2px and shifts to `{colors.primary}`, providing a clear visual cue. The input uses `{typography.body-md}` for a comfortable reading size.

### Forms
**`text-input`** — A standard text input with `{rounded.sm}` corners and a `{colors.canvas}` background. The default state has a 1px `{colors.hairline}` border; on focus, it gains a 2px `{colors.primary}` border. Error states use a 2px `{colors.badge-blue}` border, providing a clear but non-alarming visual signal.

### Footer
**`footer-section`** — A dark footer using `{colors.ink}` as the background, creating a strong visual anchor at the bottom of the page. Text is set in `{colors.canvas}` using `{typography.body-sm}`. Links use `{colors.muted-soft}` and shift to `{colors.primary}` on hover, maintaining the brand's accent color as the interactive signal.

### Hero
**`hero-section`** — A full-width hero area using `{colors.surface-soft}` as the background, with `{colors.display-xl}` for the headline. The primary CTA (`{colors.primary}`) sits prominently, with generous padding (`{spacing.section}`) creating a spacious, editorial feel. The hero is designed to feature a single book or collection, with the cover image as the visual anchor.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; display-xl scales down to 32px |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar remains visible but reduces link spacing; hero section uses 36px display-lg |
| Desktop | 1128–1440px | Three-column grid for product cards; full nav-bar with all links visible; hero section uses 48px display-xl |
| Wide | > 1440px | Max-width container at 1440px; additional whitespace on sides; four-column grid for product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum height of 48px and a minimum width of 48px for touch accessibility.
- Icon buttons are 40px x 40px with a `{rounded.full}` shape, providing a generous tap target.
- Navigation links have a minimum padding of 12px on all sides.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu, with the full menu appearing as a slide-in overlay from the left.
- The search bar collapses from a full-width input to an icon button that expands on tap.
- Product cards stack vertically in a single column, with the cover image scaling to full width.
- The footer collapses from a multi-column layout to a single column, with links stacked vertically.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors include several generic web framework defaults (e.g., `#0d6efd`, `#198754`, `#0dcaf0`) that are likely from Bootstrap or similar libraries used in the admin or checkout flow, not the brand's design system. The true brand palette was inferred from the most distinctive and frequently occurring colors (`#e87746`, `#7993a5`, `#5b6f80`, `#353434`).
- Hover and focus states for all components were inferred from common design patterns; actual live site behavior may differ.
- Error, success, and warning states for forms and inputs were not extracted and are based on standard conventions.
- Dark mode styling was not observed and is not included.
- The specific font weights and sizes for each typography token were inferred from the extracted font families and common publishing industry standards; actual CSS values may vary.
- Sub-brand or seasonal palette variations (e.g., for specific book collections or awards) were not extracted.
- Animation and transition durations/easings were not captured.
- The `meta theme-color` was not present, so the browser chrome color is unknown.
