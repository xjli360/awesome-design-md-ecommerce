---
version: alpha
name: "Gruv"
source_url: "https://www.gruv.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep purple #6b45ff — the meta-theme color and the brand's most distinctive signature — anchors a movie-and-TV marketplace that feels like a midnight video-store crawl digitized. The extracted palette is a noisy mix of checkout-widget blues (#003087, #012169 from PayPal, #4285f4 from Google Pay), payment accents (#ff5f00 from Klarna, #eb001b from Mastercard), and a long tail of orange-gold gradients (#f48120 through #d05b2e) that likely power sale badges and price-drop indicators. Against this cacophony, the purple holds: it appears in the page's `<meta theme-color>` and as #6b45ff and #6b50ff in the extracted list, suggesting a primary that's neither a generic blue nor a gray. The brand runs Titling_Gothic_FB_Wide — a condensed, squared-off gothic that reads as industrial and shelf-ready, like titles on a Blu-ray spine. The canvas is likely white (#ffffff) with a near-black ink (#231f20) for body copy, and the hairline (#dedede) keeps the grid clean. The orange cluster (#f48120–#d05b2e) is almost certainly the secondary accent for deals, discounts, and "sale" flags — a warm, urgent counterpoint to the cool purple primary. The overall mood is high-contrast, direct, and promotional: a storefront that knows it's selling entertainment, not curating it.

colors:
  primary: "#6b45ff"
  primary-active: "#5a31f4"
  primary-disabled: "#b8a6ff"
  ink: "#231f20"
  body: "#231f20"
  muted: "#5f6368"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f48120"
  accent-orange-active: "#e16f27"
  accent-orange-light: "#f89f20"
  sale-badge-bg: "#f48120"
  sale-badge-text: "#ffffff"
  price-drop: "#f79a20"
  star-rating: "#fbbc04"
  meta-theme: "#6b45ff"

typography:
  display-xl:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  caption-strong:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Titling_Gothic_FB_Wide', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
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
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.sale-badge-text}"
    rounded: "{rounded.sm}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  price-drop-label:
    backgroundColor: "{colors.price-drop}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    height: 400px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand purple #6b45ff and set in Titling_Gothic_FB_Wide uppercase. On hover, it shifts to `{colors.primary-active}` (#5a31f4). The disabled state uses `{colors.primary-disabled}` (#b8a6ff). All primary buttons use `{rounded.sm}` (4px) for a slight, no-nonsense corner.
**`button-secondary`** — An outlined or ghost variant on a white canvas with ink text. Used for less prominent actions like "Cancel" or "View Details". The border is `{colors.hairline}` (#dedede) and the text remains `{colors.ink}`.
**`button-accent-orange`** — The promotional workhorse, filled with `{colors.accent-orange}` (#f48120). Used for "Shop Sale", "Add to Cart" on discounted items, or any price-driven CTA. Active state shifts to `{colors.accent-orange-active}` (#e16f27).
**`button-link`** — A text-only link styled as a button, using `{colors.primary}` for the text. No background, no border. Used for "Learn More" or "See All" links within cards or sections.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` (8px) corners. Contains a product image (also `{rounded.md}`), a title in `{typography.title-sm}`, a price, and optional badges. The card may have a subtle shadow or border from `{colors.hairline}`. On hover, a slight elevation or border color change is expected.
**`product-card-image`** — The image container within a product card. Uses `{rounded.md}` to match the card's corner radius. Aspect ratio is typically 3:4 or 16:9 depending on the media type (movie poster vs. TV show key art).

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 64px height, white background (`{colors.canvas}`). Navigation links use `{typography.nav-link}` — Titling_Gothic_FB_Wide at 13px, uppercase, with 0.5px letter-spacing. The active category tab has a 2px bottom border in `{colors.primary}`. The logo (likely "GRUV") is set in the same typeface at a larger size.
**`search-bar`** — A pill-shaped input (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`). Placeholder text is `{colors.muted}`. On focus, it may gain a border in `{colors.primary}`. The search icon is typically a magnifying glass in `{colors.muted}`.
**`category-tab`** / **`category-tab-active`** — Horizontal tabs for browsing by genre or category. Inactive tabs are `{colors.muted}`; the active tab is `{colors.ink}` with a 2px bottom border in `{colors.primary}`. All tabs use `{typography.nav-link}`.

### Forms
**`text-input`** — A standard input field with a white background, `{rounded.sm}` (4px) corners, and `{colors.hairline}` border. Padding is 12px 16px. On focus, the border changes to `{colors.primary}`. Used for email signups, search filters, and checkout forms.

### Badges & Labels
**`sale-badge`** — A small, uppercase badge with an orange background (`{colors.sale-badge-bg}`) and white text. Uses `{typography.badge}` (11px, 700 weight, 0.5px letter-spacing). Typically positioned on the top-left corner of a product image. Padding is 2px 8px, with `{rounded.xs}` (2px) for a sharp, tag-like look.
**`price-drop-label`** — Similar to the sale badge but uses `{colors.price-drop}` (#f79a20) as the background. Indicates a price reduction. Same typography and sizing as the sale badge.

### Footer
**`footer-section`** — A full-width footer with a soft gray background (`{colors.surface-soft}`). Links use `{typography.link}` in `{colors.muted}`. The footer typically includes columns for "Help", "About", "Terms", and social media links. The copyright text is in `{typography.caption}`.

### Hero
**`hero-banner`** — A full-width promotional banner with a purple background (`{colors.primary}`) and white text. Uses `{typography.display-lg}` for the headline. Height is 400px on desktop, collapsing on mobile. May include a `{button-primary}` or `{button-accent-orange}` CTA.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu. Product cards go to 2-column grid. Hero banner height reduces to 250px. Search bar moves to a toggle icon. Category tabs become a horizontal scroll strip. |
| Tablet | 744–1128px | Nav-bar remains full but may condense. Product cards in 3-column grid. Hero banner at 350px. Search bar is full-width in the nav. |
| Desktop | 1128–1440px | Full nav-bar with all links. Product cards in 4-column grid. Hero banner at 400px. Search bar is prominent in the nav. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product cards in 5-column grid. Additional whitespace on the sides. |

### Touch Targets
- All buttons and interactive elements have a minimum height of 44px.
- Nav-bar links have a minimum tap area of 44x44px.
- Search bar has a minimum height of 44px.
- Category tabs have a minimum height of 40px.
- Product card images are tappable with a minimum area of 120x180px.

### Collapsing Strategy
- On mobile, the nav-bar collapses to a hamburger menu. The primary navigation links are hidden behind a slide-out drawer.
- The search bar collapses to a search icon; tapping it expands a full-width search input.
- The category strip becomes a horizontally scrollable row with no wrapping.
- The footer columns stack vertically on mobile.
- The hero banner's text and CTA stack vertically, with the image (if any) moving below the text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is heavily polluted with third-party payment and social media brand colors (PayPal, Klarna, Google Pay, Mastercard, Visa, Afterpay). The true brand palette is likely much smaller — the purple #6b45ff and the orange #f48120 are the most distinctive signals, but their exact usage (primary vs. secondary, hover states, disabled states) is inferred.
- Font-family declarations were limited to `Titling_Gothic_FB_Wide`. It's unclear if this is used for all headings or only display text. A fallback body font (likely Helvetica or Arial) is assumed but not confirmed.
- No extracted data for hover states, focus states, error states, or disabled states beyond the primary button.
- No dark mode or high-contrast mode tokens were found.
- No spacing or rounded values were extracted from the live site; the values above are reasonable defaults for a retail/movie site.
- No data on the logo or its color (likely white on purple or black on white).
- No extracted data for the checkout flow, cart, or user account pages.
- The exact corner radius for product cards and buttons is unknown; the values assigned are common for this type of site.
- No data on typographic scale beyond the single font-family declaration. The sizes and weights are estimated based on the brand's promotional, high-impact tone.
