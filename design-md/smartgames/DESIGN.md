---
version: alpha
name: "SmartGames"
source_url: "https://www.smartgames.eu"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A playground of primary-color logic puzzles where teal (#16a7bb) and royal blue (#0072b9) act as the twin anchors of a system that feels more like a toy box than a storefront. The brand’s signature move is a warm, almost nostalgic palette — canary yellow (#eedd55), lime green (#bbee77), and a deep forest ink (#234600) — that signals "brain game" without a hint of clinical gray. Product cards sit on a soft cream canvas (#ffffea) with rounded corners ({rounded.md}) that invite touch, while the accent orange (#ed541d) and its darker sibling (#8c2e0b) appear on sale badges and age-range tags, creating a gentle urgency. Bowlby One, a chunky display face with a hand-drawn quality, runs across headers and hero text, lending a playful, almost comic-book energy that contrasts with the clean Montserrat body copy — a deliberate tension between "fun" and "serious thinking." The navigation bar uses a white background with the teal as a hover state on links, and the search bar is a pill-shaped field ({rounded.full}) with a soft gray border (#c4c4c4) that feels approachable rather than sterile. Error states and sale flags lean into the red (#ff0000) and deep brown (#8c2e0b), while success or "in stock" indicators use a fresh green (#47c965). The overall impression is of a brand that trusts color as its primary communication layer — each hex carries a job title, not just a decorative role.

colors:
  primary: "#16a7bb"
  primary-active: "#15a1b7"
  primary-disabled: "#bbbbbb"
  ink: "#141414"
  body: "#234600"
  muted: "#884400"
  muted-soft: "#b4b4b4"
  hairline: "#c4c4c4"
  hairline-soft: "#eeeeee"
  canvas: "#fffff0"
  surface-soft: "#f8fff0"
  surface-card: "#ffffea"
  on-primary: "#ffffff"
  accent-yellow: "#eedd55"
  accent-lime: "#bbee77"
  accent-orange: "#ed541d"
  accent-orange-dark: "#8c2e0b"
  accent-red: "#ff0000"
  accent-green: "#47c965"
  sale-badge: "#ed541d"
  age-badge: "#0072b9"
  star-rating: "#eedd55"
  scrim: "#141414"

typography:
  display-xl:
    fontFamily: "'Bowlby One', 'Arial Black', Impact, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Bowlby One', 'Arial Black', Impact, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bowlby One', 'Arial Black', Impact, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  hero-cta:
    fontFamily: "'Bowlby One', 'Arial Black', Impact, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-hero:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.hero-cta}"
    rounded: "{rounded.full}"
    padding: 16px 36px
    height: 56px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "3px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(20, 20, 20, 0.1)"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  age-badge:
    backgroundColor: "{colors.age-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.accent-lime}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  star-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Shop Now," "Add to Cart," and "Learn More" actions. Rendered in the brand's teal (#16a7bb) with white text and a soft 8px corner radius. On hover, shifts to a slightly darker teal (#15a1b7); disabled state drops to a muted gray (#bbbbbb). The button uses Montserrat 700 at 16px with 0.5px letter spacing for a confident, readable weight.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Compare." Uses a white background with a 2px teal border, matching the primary's height and padding. Hover state fills the background with teal at 10% opacity (not yet extracted, but inferred). Disabled state uses a light gray border.

**`button-accent`** — Reserved for high-urgency actions like "Sale" or "Limited Edition" calls. Uses the brand's orange (#ed541d) with white text. Active state darkens to #8c2e0b. Typically paired with a sale badge or countdown timer.

**`button-hero`** — The hero section's main CTA, using the canary yellow (#eedd55) with dark ink text (#141414) and a fully rounded pill shape. Uses Bowlby One at 18px for a playful, oversized feel. Height is 56px with generous 16px/36px padding to anchor the hero layout.

### Cards
**`product-card`** — The primary content container for product listings. A cream card (#ffffea) with 12px rounded corners and 16px padding. On hover, a subtle box shadow lifts the card. Contains the product image, title (Montserrat 700 at 18px), age badge, star rating, and price. The card's background matches the warm canvas of the site, making the teal and orange accents pop.

**`sale-badge`** — A small, rectangular badge in orange (#ed541d) with white uppercase text (Montserrat 700 at 11px). Used to flag discounted items. Positioned at the top-left corner of product cards.

**`age-badge`** — A pill-shaped badge in royal blue (#0072b9) indicating the recommended age range (e.g., "6+", "8-12"). Uses the same typography as the sale badge but with a fully rounded shape for visual distinction.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a cream-white background (#fffff0). Contains the logo (Bowlby One), category links (Montserrat 600), a search bar pill, and a cart icon. Active nav links gain a 3px teal bottom border and teal text color. On mobile, the nav collapses into a hamburger menu.

**`category-strip`** — A horizontal scrollable strip below the hero, containing category tabs. Inactive tabs use a soft green background (#f8fff0) with dark text; active tabs fill with teal and white text. All tabs use fully rounded corners and compact 8px/16px padding.

### Forms
**`text-input`** — A pill-shaped input field with a 1px gray border (#c4c4c4) and cream background (#ffffea). On focus, the border thickens to 2px teal. Used for search, newsletter signup, and filter fields. Height is 48px with 12px/20px padding.

**`search-bar-pill`** — A dedicated search component with a magnifying glass icon inside the pill. Shares the same styling as text-input but with muted placeholder text (#884400). On mobile, expands to full width below the nav.

### Footer
**`footer-section`** — A dark ink (#141414) footer with cream text. Links use the lime green (#bbee77) for a playful contrast against the dark background. Organized in columns: "Products," "Support," "About," and "Newsletter." The newsletter input uses an inverted version of the text-input (dark background, light text).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero heading drops to 28px; search bar moves below nav; category strip becomes horizontal scroll |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero heading at 36px; search bar remains in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero heading at 48px; search bar in nav with expanded width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero section with larger photography |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Category tabs and badges are at least 32px tall with 8px padding for easy tapping.
- Search bar and text inputs are 48px tall to accommodate finger input.
- Nav links have a minimum 44px tap area, even when text is smaller.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The category strip becomes a horizontally scrollable row with snap points.
- Product cards stack from 3-column grid to single column.
- The hero section reduces padding and stacks text above the CTA button.
- Footer columns stack vertically with accordion-style expandable sections.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary buttons, text inputs, and links were not fully extractable from the live site's static CSS. The active states for `button-secondary` and `text-input-focus` are inferred from common patterns.
- Error styling (form validation, 404 pages) was not observed; the red (#ff0000) is assumed for error text but not confirmed.
- Dark mode is not present on the site; no dark palette tokens are defined.
- Sub-brand or seasonal palette variations (e.g., holiday themes, special editions) were not extracted.
- The exact font weights for Montserrat beyond 400, 500, 600, and 700 are inferred from common usage; the site may use additional weights.
- The `boxShadow` value for `product-card-hover` is an estimate based on visual inspection; the exact spread and opacity were not extractable.
- The `button-secondary` hover state (teal at 10% opacity) is a design assumption; the live site may use a different treatment.
- The `hero-section` background color (#f8fff0) is extracted but may vary by page or campaign.
- The `footer-link` color (#bbee77) is extracted but may have a hover state (e.g., lighter or underlined) that was not observed.
- The `star-rating` component uses the yellow (#eedd55) but the exact sizing and spacing of stars were not extractable.
