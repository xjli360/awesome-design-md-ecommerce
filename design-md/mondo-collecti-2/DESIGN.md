---
version: alpha
name: "Mondo"
source_url: "https://mondoshop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A poster-obsessed, pop-culture shrine where #d63021 — a hot, theatrical red — acts as the brand's curtain-raiser, appearing on every primary button, badge, and accent, while #121212 ink grounds the typography and product shots against a #dedede canvas that reads more like a gallery wall than a retail page. The red is the same voltage as a movie-poster logo, and it never apologizes. Poppins, a geometric sans-serif with a slight humanist warmth, runs at moderate weights — display sits at 24–32px in weight 600 rather than the heavy 700+ that action brands use; the system trusts the art to do the shouting. Product cards use a tight {rounded.sm} corner, while hero sections and modals go to {rounded.lg}, creating a hierarchy of softness that mirrors the difference between a framed print and a gallery opening. The nav bar is a thin, dark strip — #121212 with white text — that feels like a cinema marquee, and the search bar is a {rounded.full} pill in the same red as the primary, making the act of searching feel like an event. There are no hard corners on interactive elements; every CTA, badge, and filter chip uses {rounded.sm} or {rounded.full}, so the interface reads as approachable even when the subject matter is cultish. The footer collapses into a single column of links on mobile, and the product grid shifts from 4 columns to 2 to 1, but the red button and the black nav never change — they are the constants.

colors:
  primary: "#d63021"
  primary-active: "#b0261a"
  primary-disabled: "#f0a098"
  ink: "#121212"
  body: "#4d4d4d"
  muted: "#8a8a8a"
  muted-soft: "#b0b0b0"
  hairline: "#dadada"
  hairline-soft: "#e5e5e5"
  canvas: "#dedede"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#0073ce"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
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
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  search-bar-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The brand's main call-to-action, a #d63021 red rectangle with {rounded.sm} corners and white Poppins uppercase text at 14px weight 600. On hover, it shifts to `primary-active` (#b0261a); on disabled, it fades to `primary-disabled` (#f0a098). Used for "Add to Cart", "Shop Now", and "View All" actions.
**`button-secondary`** — An outlined variant with a 2px #121212 border on the `canvas` background. Text is uppercase Poppins weight 600. Active state fills the background with `surface-soft`. Used for "Learn More" or secondary CTAs in product sections.
**`button-tertiary-text`** — A text-only link styled as a button, using `primary` red text with no background or border. Used for "See Details" links within product cards.
**`button-pill-red`** — A fully rounded pill button in the brand red, used for filter resets, quick-add actions, and mobile CTAs. Smaller padding (8px 20px) and smaller typography (`button-sm`).

### Cards
**`product-card`** — A white card on the `canvas` background with {rounded.sm} corners and no padding at the card level. The image uses top-rounded corners (`{rounded.sm} {rounded.sm} 0 0`), and the title and price sit below with `{spacing.sm}` top padding and `{spacing.base}` horizontal padding. The title uses `title-sm` (14px weight 600), the price uses `body-sm` in `body` gray. No shadow — the card relies on the contrast between white and `canvas` for separation.

### Navigation
**`nav-bar`** — A 56px-tall dark strip (#121212) with white uppercase Poppins nav links at 13px weight 600. The active link uses `primary` red text. The bar is fixed to the top on desktop, collapsing to a hamburger on mobile. The logo (typically "MONDO" in white) sits on the left, and the cart icon (a red badge on a white icon) sits on the right.

### Forms
**`text-input`** — A 48px-tall input on the `canvas` background with a 1px `hairline` border and {rounded.sm} corners. On focus, the border thickens to 2px and turns `primary` red. Typography is `body-md` (16px weight 400). Used in search, newsletter signup, and checkout forms.

### Badges
**`badge-new`** — A small red rectangle with {rounded.xs} corners, uppercase Poppins at 11px weight 600, and white text. Used to flag new arrivals.
**`badge-sold-out`** — Same shape and typography but with a #121212 background and white text. Used for sold-out items.

### Filters
**`filter-chip`** — A pill-shaped chip on the `canvas` background with a 1px `hairline` border, `caption` typography (12px weight 500), and {rounded.full} corners. Active state fills the chip with #121212 and white text. Used in category and size filter strips.

### Hero
**`hero-section`** — A full-width dark section (#121212) with white text, using `display-xl` for the title and `body-md` for the subtitle. Padding is `section` (64px) top and bottom, `lg` (24px) left and right. Used for collection headers and promotional banners.

### Footer
**`footer-link`** — Standard `link` typography (14px weight 400) in `body` gray. Used in the footer column lists.
**`footer-heading`** — `title-sm` (14px weight 600) in `ink` black. Used for column headers in the footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 32px; footer columns stack vertically; filter chips wrap to 2-per-row |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 48px padding; footer uses 2-column layout |
| Desktop | 1128–1440px | Four-column product grid; full nav bar; hero uses 64px padding; footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product grid may expand to 5 columns; hero uses 80px padding |

### Touch Targets
- All buttons and interactive elements have a minimum height of 44px (Apple HIG compliant)
- Filter chips are at least 32px tall with 16px horizontal padding
- Nav links have a minimum tap area of 44x44px
- Cart icon button is 44x44px with a 20px red badge

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px; the cart icon remains visible
- Product grid collapses from 4 columns to 2 at tablet, to 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile
- Filter strip collapses to a horizontal scrollable row on mobile, with a "Filters" button that opens a modal
- Hero section reduces padding and font sizes on mobile (display-xl becomes 24px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from the primary-active color; actual extracted hover values are not available
- Error styling for form inputs (red border, error message typography) is not extracted
- The accent-blue (#0073ce) appears in the extracted colors but its usage is unclear — it may be a link color, a secondary brand color, or a Shopify widget artifact
- Dark mode is not present on the live site; no dark-mode palette is available
- Sub-brand or collection-specific color variations are not extracted
- The exact font weights used for display vs. body text are inferred from common Poppins usage; the live site may use additional weights
- Animation durations, easing curves, and transition properties are not extracted
- The `surface-card` color is assumed to be white (#ffffff) based on common e-commerce patterns, but the extracted palette does not confirm this
- Spacing values are inferred from common grid patterns; the actual spacing system may differ
- The `button-secondary` border width and color are inferred from the ink color; the actual border may be different
- The `search-bar-pill` component is inferred from the brand's visual identity; the live site may use a different search pattern
