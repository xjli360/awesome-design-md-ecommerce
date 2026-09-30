---
version: alpha
name: "Chesky Records"
source_url: "https://www.chesky.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-blue #006fcf primary anchors a site that treats high-resolution audio as a visual as well as sonic experience — the same cobalt that drives every “Add to Cart” button and genre-exploration link also appears in album-art accents and the site’s theme-color meta tag (#557b97), creating a consistent voltage from browser chrome to checkout. The palette is deliberately restrained: near-black #231f20 for headlines, #444444 for body text, and a warm mid-gray #6c7176 for secondary copy, all set against a pristine #ffffff canvas. Product cards use a soft #dedede hairline and #f7f7f7 surface-soft backgrounds, letting album covers — often high-contrast jazz and classical photography — do the emotional work. Buttons are pill-shaped ({rounded.full}) with generous 16px horizontal padding, echoing the rounded corners of CD jewel cases and vinyl sleeves. The nav bar sits at 72px with a subtle bottom border, and the search field is a full-width pill with a magnifying-glass icon in the primary blue, suggesting discovery as the site’s core interaction. There are no hard corners anywhere except the product-grid gutter; every interactive element — buttons, badges, search, category pills — uses {rounded.full} or {rounded.lg}, reinforcing the warmth of a listening room rather than the sterility of a spec sheet.

colors:
  primary: "#006fcf"
  primary-active: "#0059a6"
  primary-disabled: "#b3d4f0"
  ink: "#231f20"
  body: "#444444"
  muted: "#6c7176"
  muted-soft: "#8a8f94"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  theme-meta: "#557b97"
  accent-gray: "#54575b"
  accent-dark: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

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
    padding: 12px 24px
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
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-icon:
    color: "{colors.primary}"
    size: 20px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for “Add to Cart,” “Checkout,” and “Subscribe.” A full-pill shape in the brand’s signature cobalt (#006fcf) with white text and 16px horizontal padding. On hover, darkens to `{colors.primary-active}` (#0059a6); disabled state uses a pale blue `{colors.primary-disabled}` (#b3d4f0) with white text. **`button-secondary`** — An outlined variant with a 2px solid primary border on a white background, used for “View Details” and “Learn More” actions. Active state shifts border and text to the darker primary-active. **`button-tertiary-text`** — A text-only link styled as a button, used for “Clear Filters” or “Cancel” in modals; inherits primary color and uses no background or border. **`button-pill-primary`** — A compact 36px pill for category filters, genre tags, and “New Releases” badges. **`button-pill-outline`** — The inverse pill, used for “All Genres” or “Reset” in filter strips; has a 1px hairline border.

### Cards
**`product-card`** — Album display card with a 1px soft hairline border and `{rounded.md}` corners. The card body is white; the album art fills the top portion, with title and price below in `{typography.title-sm}` and `{typography.body-sm}`. On hover, a subtle box-shadow lifts the card and the border strengthens to `{colors.hairline}`. **`product-card-badge`** — A small primary-blue badge pinned to the top-left of the card for “New,” “Exclusive,” or “Hi-Res” labels; uses `{typography.badge}` (11px uppercase) with `{rounded.sm}`.

### Navigation
**`nav-bar`** — A 72px white bar with a 1px soft hairline bottom border. Links use `{typography.nav-link}` at 15px weight 500. The active link gets a 2px primary underline; inactive links render in `{colors.muted}`. The nav contains the Chesky Records logotype on the left, genre dropdowns in the center, and a search icon + cart icon on the right.

### Forms
**`text-input`** — Full-pill input field with a 1px hairline border and 12px vertical padding. On focus, the border becomes a 2px primary stroke. Used for email signups, search queries, and checkout forms. **`search-bar`** — A dedicated search input with a light gray `{colors.surface-soft}` background and a 20px primary-blue magnifying-glass icon on the left. The placeholder text reads “Search artists, albums, genres…” in `{colors.body}`.

### Footer
**`footer-section`** — A light gray (`{colors.surface-soft}`) full-width band with `{spacing.section}` vertical padding. Links are `{colors.muted}` and turn primary on hover. The footer includes columns for “About,” “Support,” “Artists,” and “Connect,” plus a copyright line in `{colors.muted-soft}`.

### Hero
**`hero-section`** — A full-width white canvas with `{spacing.section}` padding on top and bottom. Contains a `{typography.display-xl}` headline (e.g., “Experience Music in Pure High Resolution”) and a `{typography.body-md}` subtitle in `{colors.muted}`. Typically paired with a large album-art collage or a featured release image.

### Dividers
**`divider`** — A 1px horizontal rule in `{colors.hairline-soft}`, used between sections and within product lists.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; search bar becomes full-width below nav; category pills wrap to 2 rows; footer columns stack vertically |
| Tablet | 744–1128px | Nav shows all links but genre dropdowns become tap-to-expand; product cards in 2-column grid; hero padding at 48px; search bar remains in nav but shrinks to 60% width |
| Desktop | 1128–1440px | Full nav with hover dropdowns; product cards in 3-column grid; hero at full padding; search bar centered in nav at 400px max-width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with 800px max-width; all elements scale proportionally |

### Touch Targets
- All interactive elements (buttons, pills, links, icons) have a minimum touch target of 44x44px.
- Nav links on mobile use 48px tap areas.
- Search bar and text inputs maintain 48px height for comfortable tapping.
- Category pills are 36px tall with 16px horizontal padding, exceeding the 44px width minimum.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu that slides in from the left; the search icon moves into the hamburger panel.
- Product cards collapse from 3-column to 2-column (tablet) to single-column (mobile).
- Footer columns collapse from 4-column to 2-column (tablet) to single-column (mobile).
- Hero sections reduce vertical padding by 50% on mobile and stack text above imagery instead of side-by-side.
- Category pill strips become horizontally scrollable on mobile rather than wrapping.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the typography block uses Inter as a reasonable sans-serif default for a modern audio brand, but the actual brand typeface (possibly a custom or licensed face) is unknown.
- Hover and focus states for most components (beyond button-primary and product-card) are inferred from common patterns, not extracted.
- Error styling for form inputs (red borders, error messages) was not observed.
- The extracted color list is dominated by blues and grays — the primary #006fcf is the most distinctive accent, but the palette may include additional brand-specific tones (e.g., a gold or warm tone for “audiophile” badges) that were not captured.
- Dark mode styling is not present on the live site and is not defined.
- Sub-brand or collection-specific palettes (e.g., “Jazz Series,” “Classical Masters”) may exist but were not extracted.
- Spacing values for section padding and component padding are estimated from common e-commerce patterns; exact values may differ on the live site.
- The search-bar icon size and color are inferred from the primary color usage; the actual SVG may have different dimensions.
- No animation or transition durations were extracted (e.g., button hover fade, card lift).
