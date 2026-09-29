---
version: alpha
name: "NECA"
source_url: "https://necaonline.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A collector-grade action-figure marketplace that wears its fandom on its sleeve through a high-contrast palette anchored on a deep, almost-black ink (#111111) and a primary red (#e83630) that reads like a comic-book cover's signature color — bold enough to punch through a shelf of product photography, restrained enough to let the figures themselves be the spectacle. The brand's secondary palette is a toy-box explosion of purple (#600040, #600060), blue (#4054b2, #003388), and orange (#ff6900), used sparingly for category badges and limited-edition callouts, while the canvas stays a clean white (#eeeeee) with soft surface cards at (#ffffff) and hairline borders at (#bbbbbb). Typography runs a pragmatic sans-serif stack — Open Sans, Roboto, and system fonts — at modest sizes (body at 14–16px, display at 20–24px) with no decorative weights; the brand trusts the raw energy of its licensed IP photography over typographic flourish. Buttons are sharp-cornered rectangles (`{rounded.sm}` ~8px) in the primary red, while product cards use a softer `{rounded.md}` ~12px to frame the figures without competing. The nav bar is a dark band (`{colors.ink}`) with white text, a deliberate inversion that signals "this is the storefront, not the shelf." Search is a full-width bar with a red submit button, and the footer collapses into a dense grid of links in muted gray (#808080). The overall feel is that of a convention-exclusive booth translated into a web store — loud when it needs to be, functional when it doesn't.

colors:
  primary: "#e83630"
  primary-active: "#c92a24"
  primary-disabled: "#f5a09c"
  ink: "#111111"
  body: "#313131"
  muted: "#808080"
  muted-soft: "#bbbbbb"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-purple: "#600040"
  accent-blue: "#4054b2"
  accent-orange: "#ff6900"
  badge-red: "#cf2e2e"
  badge-green: "#00d084"
  star-rating: "#fcb900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-lg:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-exclusive:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 44px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Buy Now", and checkout flows. Rendered in the brand's signature red (`{colors.primary}`) with white text and an 8px rounded corner (`{rounded.sm}`). On hover, shifts to `{colors.primary-active}` (#c92a24). Disabled state uses `{colors.primary-disabled}` (#f5a09c) with no border change. Height is 44px with 12px vertical padding and 24px horizontal padding.

**`button-secondary`** — Used for secondary actions like "View Details" or "Wishlist". White background with ink text, same 44px height and 8px rounding. Outline variant (`button-secondary-outline`) adds a 1px hairline border for visual separation from the canvas.

**`button-pill-primary`** — A smaller, fully rounded variant (`{rounded.full}`) used for filter chips, category tags, and quick-add actions. 8px vertical padding, 16px horizontal, with `{typography.button-sm}`.

### Navigation
**`nav-bar`** — The primary site navigation, rendered as a 60px dark band (`{colors.ink}`) with white text. Links use `{typography.nav-link}` at 14px weight 600. Active link text shifts to `{colors.primary}` red. The bar is fixed at the top on desktop, collapsing to a hamburger menu on mobile.

**`category-strip`** — A horizontal scrollable strip below the nav bar, with pill-shaped category tabs. Active tab uses `{colors.primary}` background with white text; inactive tabs are white with a hairline border. Each pill is 6px vertical padding, 16px horizontal, with `{rounded.full}`.

### Cards
**`product-card`** — The core product display unit, a white card with 12px padding and `{rounded.md}` (12px) corners. Product images are cropped square or 4:3 with the same corner rounding. Title uses `{typography.title-sm}` in ink, price uses `{typography.body-md}` in primary red. Badges overlay the top-left corner of the image.

**`badge-new`**, **`badge-sale`**, **`badge-exclusive`** — Small, tightly padded badges (2px vertical, 8px horizontal) with 4px rounding (`{rounded.xs}`). "New" uses primary red, "Sale" uses accent orange (#ff6900), "Exclusive" uses accent purple (#600040). All use `{typography.badge}` at 11px weight 700.

### Forms
**`text-input`** — Standard text input for search and checkout forms. White background, 44px height, 12px padding, 8px rounding, with a 1px hairline border. On focus, the border thickens to 2px and shifts to `{colors.primary}` red.

**`search-bar`** — A full-width input field paired with a red submit button (`search-submit`). The input is 44px tall with 12px padding; the submit button is the same height with 20px horizontal padding. Both use `{rounded.sm}`.

### Footer
**`footer`** — A dense, dark footer (`{colors.ink}`) with 48px vertical padding. Links are in `{colors.muted-soft}` (#bbbbbb) at 14px weight 400. Section headings use `{typography.title-sm}` in white. The footer is organized in a 4-column grid on desktop, collapsing to a single column on mobile.

### Hero
**`hero-banner`** — Used for homepage and collection landing pages. Dark background (`{colors.ink}`) with white text, 64px vertical padding. The hero CTA (`hero-cta`) is a large primary button with 32px horizontal padding for emphasis.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in 1–2 columns; footer collapses to single column; hero padding reduces to 32px; category strip becomes horizontally scrollable |
| Tablet | 744–1128px | Nav bar shows top-level links; product cards in 3 columns; footer in 2 columns; hero padding at 48px |
| Desktop | 1128–1440px | Full nav bar visible; product cards in 4 columns; footer in 4 columns; hero at full 64px padding |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5 columns; all elements centered with generous margins |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav bar hamburger icon is 48px × 48px.
- Category strip pills are at least 32px tall.
- Product card CTAs are 44px tall with 24px horizontal padding.

### Collapsing Strategy
- Nav bar links collapse into a hamburger menu below 744px; the logo and cart icon remain visible.
- Product grid collapses from 5 columns (wide) to 4 (desktop) to 3 (tablet) to 2 (mobile).
- Footer grid collapses from 4 columns to 2 at tablet, to 1 at mobile.
- Category strip becomes a horizontally scrollable row on mobile, with no wrapping.
- Hero banner reduces vertical padding and stacks CTA below headline on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs, links, and secondary buttons were not reliably extracted from the live site; the values provided for `button-primary-active` and `text-input-focus` are inferred from common patterns and should be verified against the brand's actual CSS.
- Error styling (form validation, error messages, empty states) was not observed in the extraction.
- Dark mode is not supported; the site uses a light canvas exclusively.
- Sub-brand or collection-specific color palettes (e.g., for specific licensed IP lines) were not extracted; the accent colors provided (#600040, #4054b2, #ff6900) are the most distinctive non-primary colors found but may not represent all sub-brand variations.
- The extracted font list is a generic sans-serif stack (Open Sans, Roboto, system fonts); the brand may use a custom or licensed font for display headings that was not captured in the extraction.
- The extracted hex list includes many colors from checkout widgets (Shopify Pay, Klarna, Afterpay) and social media icons; the true brand palette is likely more limited than the full list suggests. The primary red (#e83630) and near-black ink (#111111) are the most confident picks.
- Spacing values (padding, margin, gap) for specific components were inferred from common e-commerce patterns and should be validated against the live site's computed styles.
- Animation and transition durations were not extracted; the brand may use subtle hover transitions (e.g., 0.2s ease-in-out) that are not documented here.
