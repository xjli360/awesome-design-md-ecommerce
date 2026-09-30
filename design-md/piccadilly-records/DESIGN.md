---
version: alpha
name: "Piccadilly Records"
source_url: "https://www.piccadillyrecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, saturated blue (#003399) anchors Piccadilly Records — it appears as the primary brand colour across the site header, key navigation elements, and prominent call-to-action buttons, lending a sense of authority and musical heritage. This is paired with a vibrant orange (#f16e22) used as a secondary accent for sale tags, badges, and hover states, creating a high-contrast, energetic rhythm against the predominantly white canvas (#fefffe). The site feels dense and information-rich, a deliberate choice for a record store where browsing is the primary activity. Typography relies on a system stack (Arial, Helvetica Neue, sans-serif) for reliability, with the distinctive MochaMattari font reserved for display headings and the Piccadilly Records wordmark, adding a bespoke, hand-drawn quality. Layouts are grid-based and tightly packed, with product cards using minimal whitespace and a subtle hairline (#eeeeee) to separate items. The overall mood is utilitarian but warm, driven by the bold colour blocking and the tactile promise of vinyl discovery. Buttons are sharp-cornered rectangles (`{rounded.none}`) with solid fills, reinforcing a no-nonsense, direct approach. The footer expands into a dense information hub, using muted tones (#d1c7c7) for secondary links and a distinct gold (#e5d974) for sale or featured item highlights.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#b3c6e6"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#eeeeee"
  hairline-soft: "#f2f2f2"
  canvas: "#fefffe"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f16e22"
  accent-orange-hover: "#eb600f"
  accent-gold: "#e5d974"
  accent-gold-dark: "#c9a561"
  accent-green: "#29b473"
  accent-green-hover: "#1ebf74"
  border-light: "#d1c7c7"
  border-muted: "#c6b9b9"
  text-muted-light: "#adacac"

typography:
  display-xl:
    fontFamily: "'MochaMattari', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'MochaMattari', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'MochaMattari', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
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
    rounded: "{rounded.none}"
    padding: 10px 20px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 9px 19px
    height: 40px
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.text-muted-light}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-featured:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, used for actions like "Add to Cart" and "Checkout". It features a solid `{colors.primary}` fill with white text, set in uppercase bold sans-serif. The button has no border radius (`{rounded.none}`), reinforcing the direct, no-frills aesthetic. On hover, it transitions to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}` to indicate inactivity.

**`button-secondary`** — An outlined variant used for secondary actions such as "View Details" or "Cancel". It has a white background with `{colors.ink}` text and a 1px solid `{colors.ink}` border. The hover state fills the background with `{colors.ink}` and inverts the text to white. It shares the same `{rounded.none}` and uppercase typography as the primary button.

**`button-accent`** — A smaller, high-energy button used for sale or promotional actions. It uses `{colors.accent-orange}` as the background, drawing immediate attention. The typography is `{typography.button-sm}` and the padding is tighter, making it suitable for inline use within product cards or banners.

### Navigation
**`nav-bar`** — The primary site navigation bar, a solid band of `{colors.primary}` spanning the full viewport width. It contains the Piccadilly Records logo (set in `{typography.display-md}` using MochaMattari) and navigation links styled with `{typography.nav-link}` in white. The bar has a fixed height of 48px and no border radius. Links are padded horizontally at `{spacing.base}`.

**`category-strip`** — A horizontal scrollable strip of genre or department links, positioned below the main nav. It sits on the `{colors.canvas}` background. Active categories use `{colors.primary}` as a background with white text, while inactive categories use transparent background with `{colors.ink}` text. All categories have `{rounded.none}`.

### Cards
**`product-card`** — The standard product display card for album listings. It has a white background with no border radius. The card contains a product image (typically square), the artist name in `{typography.body-sm}` with `{colors.muted}`, the album title in `{typography.title-sm}` with `{colors.ink}`, and the price in `{typography.body-md}` with `{colors.ink}`. A `{colors.hairline}` border separates cards in a grid layout. On hover, a subtle shadow is applied.

**`product-card-badge`** — A small, rectangular badge overlaid on the product card image. It uses `{colors.accent-orange}` as the background with white uppercase text. The badge is positioned at the top-left corner of the image and has no border radius.

### Forms
**`text-input`** — A standard text input field used for search, newsletter signup, and checkout forms. It has a white background, `{colors.ink}` text, and a 1px solid `{colors.hairline}` border. The input has no border radius and a height of 40px. On focus, the border changes to `{colors.primary}`.

**`search-bar`** — A dedicated search input, identical in styling to `text-input` but often placed within a larger search module. It may include a search icon button on the right, which uses `{colors.primary}` as the background.

### Footer
**`footer-section`** — The site footer, a dense information area with a `{colors.ink}` background. It contains multiple columns of links, each with a heading in `{typography.title-sm}` and white text. Links are styled with `{typography.link}` and `{colors.text-muted-light}`. The footer includes sections for customer service, about us, social media links, and a newsletter signup. It uses `{spacing.section}` for top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; category strip becomes a horizontal scroll; footer links stack vertically; search bar moves to a toggleable overlay. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but may be truncated; category strip is fully visible; footer uses a 2-column layout. |
| Desktop | 1128–1440px | Three-column product grid; full navigation visible; category strip is a horizontal row; footer uses a 4-column layout. |
| Wide | > 1440px | Four-column product grid; maximum content width of 1440px with centered layout; additional whitespace on the sides. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card images are tappable and link to the product detail page.
- The hamburger menu icon has a 48x48px touch area.
- Category strip items have a minimum height of 40px.

### Collapsing Strategy
- The main navigation bar collapses into a hamburger menu on mobile.
- The category strip becomes a horizontally scrollable list on mobile.
- The footer sections collapse into accordion-style panels on mobile, with the first section expanded by default.
- The search bar is hidden behind a search icon on mobile and expands to a full-width overlay when activated.
- Product grids reduce from 3-4 columns on desktop to 1-2 columns on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all interactive elements could not be fully extracted from the live site; the provided active states are inferred from common patterns.
- Error styling for form inputs (e.g., invalid email, missing required fields) was not observed and is not defined.
- The exact font weight and letter-spacing for MochaMattari could not be verified; the values provided are based on typical usage for display serif fonts.
- Dark mode or high-contrast mode styles are not present in the extracted data.
- The specific border width for `button-secondary` (1px) is assumed based on common implementation; it was not explicitly extracted.
- The shadow applied to `product-card` on hover is not defined as it could not be reliably extracted.
- The spacing values for `footer-section` and `category-strip` are based on common layout patterns and may not exactly match the live site.
