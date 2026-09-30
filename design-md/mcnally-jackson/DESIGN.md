---
version: alpha
name: "McNally Jackson"
source_url: "https://www.mcnallyjackson.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue (#003399) as authoritative as a library card catalog anchors a system that otherwise reads as warm, papery, and unpretentious — the kind of place where the checkout counter is cluttered with staff picks and a stack of remaindered paperbacks. That blue, used for the primary navigation bar, the footer background, and every primary button, sits against a near-white canvas (#f6f6f6) that avoids the sterile hospital-white of many e-commerce sites; it's the color of unbleached paper stock. A secondary accent of marigold (#dad55e) and a softer butter (#fffa90) appear in sale badges, promotional banners, and hover states, injecting a cheerful, independent-bookstore energy. The typography relies on Adobe Caslon Pro for display and body text — a serif face that signals literary seriousness without academic stuffiness — paired with Helvetica Neue for UI elements like buttons and form labels. Buttons are softly rectangular with {rounded.sm} corners, never pill-shaped; the brand trusts the authority of its blue rectangle over the friendliness of a circle. Product cards use a clean white surface ({colors.surface-card}) with a subtle drop shadow, and the overall spacing is generous — {spacing.section} between major sections — giving each book room to breathe. The checkout flow, however, introduces a jarring note: a bright pink (#ff5e99) and a sky blue (#31a8f0) that belong to third-party payment widgets, not the bookstore itself. The overall impression is of a serious but warm literary institution that has chosen restraint over trend — no hero carousels, no full-bleed photography, just books arranged in a clean, browsable grid.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#b3c6e6"
  ink: "#222222"
  body: "#454545"
  muted: "#757575"
  muted-soft: "#aaaaaa"
  hairline: "#c5c5c5"
  hairline-soft: "#e9e9e9"
  canvas: "#f6f6f6"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#dad55e"
  accent-butter: "#fffa90"
  accent-marigold-dark: "#777620"
  sale-badge: "#f1d600"
  error: "#c13515"
  star-rating: "#f1a899"

typography:
  display-xl:
    fontFamily: "'adobe-caslon-pro', 'big-caslon-fb', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'adobe-caslon-pro', 'big-caslon-fb', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'adobe-caslon-pro', 'big-caslon-fb', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'adobe-caslon-pro', 'big-caslon-fb', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'adobe-caslon-pro', 'big-caslon-fb', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'adobe-caslon-pro', 'big-caslon-fb', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.accent-marigold-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-mobile:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 56px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.accent-butter}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.accent-marigold-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Submit." A deep blue rectangle ({colors.primary}) with white uppercase sans-serif text. On hover, the background deepens to {colors.primary-active}. Disabled state uses a washed-out blue ({colors.primary-disabled}) with muted text, signaling the action is unavailable. The 4px corner radius ({rounded.sm}) is subtle enough to feel professional, not playful.

**`button-secondary`** — An outlined variant for secondary actions like "Save for Later" or "View Details." Uses a white background with a 1px solid {colors.primary} border and blue text. Active state fills the background with {colors.surface-soft}. Height and typography match the primary button for visual alignment in forms.

**`button-tertiary-text`** — A text-only button for low-emphasis actions like "Cancel" or "Clear Filters." No background or border; relies on {colors.primary} text color. Hover adds a soft background ({colors.surface-soft}) for affordance.

**`button-sale`** — A compact, high-visibility button used on sale items and promotional banners. Uses the marigold accent ({colors.accent-marigold}) with dark text ({colors.accent-marigold-dark}) and smaller uppercase sans-serif type. Shorter height (36px) allows it to sit inline with product cards without overwhelming the layout.

### Cards
**`product-card`** — The primary content container for book listings. A white card with a subtle drop shadow (0 1px 3px rgba(0,0,0,0.08)) and 8px rounded corners. Contains a book cover image (2:3 aspect ratio), title in {typography.title-sm}, author name in muted body-sm, and price in bold body-md. Hover elevates the shadow to 0 4px 12px rgba(0,0,0,0.12), providing a gentle lift effect. Badges overlay the top-left corner of the image.

### Navigation
**`nav-bar`** — A full-width, 64px-tall bar in {colors.primary} with white text. Contains the store logo (left), navigation links (center), and search + cart icons (right). Links use 14px sans-serif with 0.3px letter spacing. Active page links turn butter-yellow ({colors.accent-butter}). On mobile, the bar collapses to 56px and navigation links move to a hamburger menu.

**`nav-link`** — Individual navigation items with 8px vertical padding and 12px horizontal padding for comfortable tap targets. White text on the blue bar, with active state highlighted in {colors.accent-butter}.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. White background with a 1px {colors.hairline} border and 4px rounded corners. Focus state gains a 2px {colors.primary} border and removes the default outline. Error state swaps to a red border ({colors.error}). Height is 44px for comfortable typing.

**`search-bar`** — A compact search input (40px height) used in the navigation bar. White background with a subtle border. On focus, expands to a 2px {colors.primary} border. The search icon sits inside the input on the left.

### Badges
**`sale-badge`** — A bright yellow ({colors.sale-badge}) badge with bold uppercase 11px text. Used to flag discounted items, typically positioned at the top-left of product card images. Minimal 2px corner radius ({rounded.xs}) keeps it sharp and readable.

**`new-badge`** — A marigold ({colors.accent-marigold}) badge for new arrivals or restocked items. Dark text ({colors.accent-marigold-dark}) ensures readability. Same dimensions and placement as the sale badge.

### Footer
**`footer`** — A full-width footer in {colors.primary} with white text. Contains store information, links, newsletter signup, and social icons. Links are white with 85% opacity, increasing to full opacity on hover. Padding is generous ({spacing.xxl} vertical) to create a solid base for the page.

### Section Headings
**`section-heading`** — Used for category titles ("Fiction," "New Releases," "Staff Picks") and page headings. Set in Adobe Caslon Pro at 24px with 600 weight. The serif face provides literary authority, while the generous bottom margin ({spacing.lg}) creates clear separation from the content below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to 56px; navigation links hidden behind hamburger menu; product cards stack in single column; search bar moves below nav; footer links stack vertically |
| Tablet | 744–1128px | Nav bar at full height; product cards in 2-3 column grid; search bar in nav; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links visible; product cards in 3-4 column grid; search bar prominent in nav; footer in 3-4 column layout |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-5 column grid; increased whitespace around sections |

### Touch Targets
- All buttons and links maintain minimum 44px tap target height
- Navigation links have 8px vertical padding for comfortable tapping
- Quantity selector buttons are 36px × 36px minimum
- Product card tap targets (title, image, button) are at least 48px tall

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Product card grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer columns collapse from 4 → 2 → 1
- Search bar moves from inline nav to below the nav on mobile
- Breadcrumb text truncates on mobile (shows only current page)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components were inferred from common patterns, not extracted from the live site
- Error state styling (form validation, 404 pages, empty states) could not be reliably extracted
- The checkout flow likely uses a third-party payment system; its colors (#ff5e99, #31a8f0, #b2f7ff) appear unrelated to the bookstore brand
- Dark mode is not implemented on the live site
- The extracted color list is unusually large (30+ colors), suggesting framework defaults, social media icons, and stock image tones were not fully filtered. The true brand palette is likely smaller: the deep blue (#003399), the marigold (#dad55e), the butter (#fffa90), and a range of grays/whites
- Font weights beyond the standard 400/600/700 were not extractable; actual usage may include 300 or 500 weights
- Line heights and letter spacing values are estimated from typical serif/sans-serif pairings, not extracted from CSS
- The site may use a custom serif font beyond Adobe Caslon Pro; "big-caslon-fb" suggests a Big Caslon variant, but exact licensing is unknown
- Animation durations, easing curves, and transition properties were not extracted
- The shopping cart drawer or modal behavior was not observable from static HTML
- Accessibility contrast ratios have not been verified against WCAG standards
