---
version: alpha
name: "Third Window Films"
source_url: "https://thirdwindowfilms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003388 anchors Third Window Films like a cinema screen before the projector starts — that same cobalt runs through the header, primary buttons, and footer, while a sharp green #22b339 cuts in as the accent for add-to-cart actions and sale badges, a pairing that feels more like a repertory cinema poster than a standard ecommerce palette. The site reads like a physical shelf of Japanese and Asian film releases: Georgia serves the body text with a bookish, slightly serifed warmth, while Open Sans handles navigation and buttons with clean utility. Product listings stack in a dense, text-forward grid — no hero carousels, no lifestyle photography — just covers, titles, and prices, trusting the film art to do the selling. The canvas is a soft off-white #f8f8f8, with cards lifted on #ffffff and hairline separators in #c4c4c4, creating a quiet, library-like hierarchy. Buttons use a modest {rounded.sm} radius — nothing pill-shaped, nothing playful — and the search bar sits as a simple text input with a blue border, not an orb. The overall effect is that of a specialist label's storefront: serious, browsable, built for people who already know what they're looking for.

colors:
  primary: "#003388"
  primary-active: "#003399"
  primary-disabled: "#3a70ad"
  ink: "#1e1e1e"
  body: "#323a45"
  muted: "#51575d"
  muted-soft: "#aaaaaa"
  hairline: "#c4c4c4"
  hairline-soft: "#e0e0e0"
  canvas: "#f8f8f8"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#22b339"
  accent-sale-hover: "#1a8f2e"
  footer-bg: "#23282d"
  footer-text: "#aaaaaa"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-accent-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    typography: "{typography.button-sm}"
    textColor: "{colors.primary}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

## Components

### Buttons
**`button-primary`** — The standard call-to-action, filled with the deep blue #003388 and white uppercase Open Sans text. Hover shifts to the slightly brighter #003399. Disabled state fades to #3a70ad. Used for "Add to Cart", "Checkout", and primary form submissions. The 4px radius and 40px height keep it compact and serious — no pill shapes, no gradients.

**`button-secondary`** — An outlined variant with a white background and blue text, matching the primary's dimensions and uppercase weight. Used for "View Details" and secondary actions alongside primary buttons. The 1px border uses `{colors.primary}`.

**`button-accent-sale`** — The green #22b339 button reserved for sale items and promotional CTAs. Same dimensions and uppercase styling as the primary, but the green signals urgency without resorting to red. Hover deepens to #1a8f2e.

### Text Inputs
**`text-input`** — A simple white input with a light gray #c4c4c4 border and Georgia body text inside. Focus state swaps the border to the brand blue #003388. Used for search, newsletter signup, and checkout forms. Height is 40px with 8px/12px padding — nothing oversized, nothing decorative.

### Navigation
**`nav-bar`** — A full-width blue #003388 bar at 48px height, carrying uppercase Open Sans links in white. Links have 16px horizontal padding and no background on hover — just a text color shift to a lighter blue. The bar is fixed to the top on desktop, collapsing to a hamburger on mobile.

**`breadcrumb`** — Small gray Open Sans text at 13px, with the current page in dark ink. No arrows or slashes between items — just spacing and color to separate levels.

### Product Cards
**`product-card`** — A white card with no border radius and no shadow, containing a film cover image, title in 18px Open Sans, and price in 16px Georgia. The card is essentially a container for the cover art — the typography is secondary. Sale items get a small green badge in the top-left corner.

**`product-card-sale-badge`** — A tiny green #22b339 pill with white uppercase text, 2px/6px padding, and a 2px radius. Positioned absolutely over the cover image.

### Search
**`search-bar`** — A simple text input with a white background, gray border, and Georgia placeholder text. No icon inside the field — the search icon sits to the left as a separate element. Focus highlights the border in blue. Height is 36px, narrower than the standard input.

### Footer
**`footer`** — A dark #23282d section with light gray #aaaaaa links and body text. Links are 14px Open Sans with no underline. The footer stacks in two columns on desktop (links left, copyright right) and collapses to a single column on mobile.

### Pagination
**`pagination`** — Blue Open Sans uppercase links at 12px, with the active page getting a blue background and white text in a 4px rounded box. Inactive pages are just text links with no underline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; footer stacks vertically; search bar moves below nav |
| Tablet | 744–1024px | Nav links remain visible but condensed; product grid shows 2 columns; footer remains two-column |
| Desktop | 1024–1440px | Full nav with all links; product grid at 3–4 columns; search bar in header |
| Wide | > 1440px | Max-width container at 1200px; product grid expands to 5 columns; no layout changes beyond centering |

### Touch Targets
- All buttons and links: minimum 40px height
- Nav links: 48px tap target (matches nav bar height)
- Search bar: 36px height (below recommended 40px — note in gaps)
- Pagination links: 32px minimum tap target

### Collapsing Strategy
- Top nav: links collapse to hamburger menu below 744px
- Product grid: 4 columns → 2 columns → 1 column
- Footer: two-column layout collapses to single column below 744px
- Search bar: moves from header to below nav on mobile
- Breadcrumbs: hidden on mobile, shown on tablet and above

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are dominated by blues and grays — the list may include Shopify defaults and social icon colors. The true brand primary (#003388) and accent (#22b339) were selected as the most distinctive colors from the extracted set, but the palette may be incomplete.
- Only two font families were extracted (Georgia, Open Sans) — heading weights and sizes are inferred from common patterns, not verified against the live site's CSS.
- No hover, focus, or active states were extractable from the static analysis — button-secondary hover, link underlines, and input focus borders are estimated.
- Error states for forms (validation colors, error messages) are not documented.
- Dark mode is not present on the live site.
- The search bar height of 36px may not meet WCAG touch target guidelines — this is an observation, not a confirmed design choice.
- Sub-brand or collection-specific color variations (e.g., "Third Window" vs. "Third Window Classics") are not captured.
- No animation or transition timings were extractable.
- The meta theme-color tag is absent — the browser chrome/taskbar color is unset.
