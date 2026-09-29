---
version: alpha
name: "StringWorks"
source_url: "https://www.stringworks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep forest green (#335522) anchors StringWorks — not the expected mahogany or rosin-brown of orchestral tradition, but a cool, botanical hue that reads as precision and growth rather than nostalgia. The brand pairs this primary with a warm gold accent (#a16a00) that catches the eye like a brass tuning peg catching stage light, used sparingly on price highlights and select CTAs. The canvas is a soft off-white (#f8f8f8) rather than pure white, giving the page the feel of aged manuscript paper rather than a sterile catalog. Typography runs Montserrat for display and Lato for body — a clean sans-serif stack that avoids the script or serif flourishes one might expect from a violin shop, signaling instead that StringWorks is a modern instrument maker, not a dusty atelier. Product cards use generous whitespace and a tight 2px hairline (#2c2c2c at reduced opacity) to frame instruments with the clarity of a museum vitrine. The navigation bar sits at 80px with a sticky backdrop, the logo centered, and category links in uppercase Montserrat at 12px — a quiet, confident layout that lets the instruments breathe. Buttons are pill-shaped (`{rounded.full}`) in the forest green with white text, and secondary actions appear as outlined pills with the green as stroke. The overall mood is serious but not severe: the green is alive, the gold is warm, and the off-white canvas keeps the experience from feeling cold. StringWorks trusts its product photography — high-resolution, full-bleed hero shots of violin scrolls and cello bouts — to do the emotional work, while the UI stays out of the way.

colors:
  primary: "#335522"
  primary-active: "#264418"
  primary-disabled: "#a3b89a"
  ink: "#2c2c2c"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#2c2c2c"
  hairline-soft: "#cccccc"
  canvas: "#f8f8f8"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  accent-gold: "#a16a00"
  accent-gold-active: "#7a5200"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  star-rating: "#a16a00"
  badge-new: "#335522"
  badge-sale: "#a16a00"
  error: "#c13515"
  success: "#335522"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Lato', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Lato', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-accent:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price}"
    color: "{colors.accent-gold}"
  product-card-compare-at:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    textDecoration: line-through
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 500px
  hero-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.3)"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.accent-gold}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill in forest green (#335522) with white uppercase Montserrat text. On hover, it deepens to `{colors.primary-active}` (#264418). The disabled state uses `{colors.primary-disabled}` (#a3b89a), a muted sage that signals the action is unavailable without causing confusion. Used for "Add to Cart", "Checkout", and primary form submissions.

**`button-secondary`** — An outlined pill with a 2px solid `{colors.primary}` border and transparent fill. On hover, it fills with the forest green and inverts the text to white. Used for "Learn More", "View Details", and secondary actions that should not compete with the primary CTA.

**`button-accent`** — A gold (#a16a00) pill used sparingly for high-value actions like "Shop Sale" or "Limited Edition". On hover, it darkens to `{colors.accent-gold-active}` (#7a5200). This button carries the emotional weight of a special offer or featured instrument.

**`button-ghost`** — A text-only button with no background or border, using `{typography.button-sm}` in uppercase. Used for tertiary actions like "Cancel", "Clear Filters", or "Remove" in cart line items. Hover state adds a subtle underline.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners, housing a product image, title, price, and optional badges. The image area uses `{rounded.md} {rounded.md} 0 0` to maintain the card's corner radius at the top while allowing the image to bleed to the bottom edges. The title uses `{typography.title-md}` (16px/600 weight) and sits 12px below the image. The price uses `{typography.price}` (20px/700 weight) in the ink color. Sale prices render in `{colors.accent-gold}` with the original price struck through in `{colors.muted}` using `{typography.caption}`.

**`product-card-hover`** — On hover, the card gains a subtle shadow (0 4px 12px rgba(0,0,0,0.08)) and the image scales up 2% with a smooth 300ms ease transform.

### Navigation
**`nav-bar`** — A sticky 80px bar on the off-white canvas, with the StringWorks logo centered and navigation links in uppercase Montserrat at 12px with 1px letter-spacing. Links are spaced generously (32px apart) and the active page link is underlined with a 2px `{colors.primary}` border. The bar includes a cart icon on the right and a search icon on the left, both in `{colors.ink}`. On scroll, the bar gains a 1px bottom border in `{colors.hairline-soft}`.

### Forms
**`text-input`** — A standard input field with white background, 1px `{colors.hairline-soft}` border, and `{rounded.sm}` (8px) corners. On focus, the border thickens to 2px `{colors.primary}`. Error state uses a 2px `{colors.error}` (#c13515) border. The input height is 48px to meet touch-target requirements, with 12px/16px padding for comfortable text entry.

**`select-input`** — Matches the text-input styling but includes a custom dropdown arrow in `{colors.primary}`. Used for instrument size selection (4/4, 3/4, 1/2, etc.) and product filtering.

### Badges
**`badge`** — A small forest green label with white uppercase text, 4px/8px padding, and `{rounded.xs}` (4px) corners. Used for "New", "Best Seller", and "Handcrafted" indicators. The `badge-sale` variant uses `{colors.accent-gold}` background for urgency.

### Hero
**`hero`** — A full-width section at 500px height on the off-white canvas, featuring a large display headline (`{typography.display-xl}` at 36px/700 weight) and a supporting subheadline in `{typography.body-md}`. The hero may include a full-bleed product photograph with a dark overlay (`rgba(0,0,0,0.3)`) for text legibility. The primary CTA sits centered below the headline.

### Footer
**`footer`** — A dark section (`{colors.ink}` background) with white text, organized into columns for customer service, about us, and policies. Links are white `{typography.link}` (14px Lato) and turn gold (`{colors.accent-gold}`) on hover. The footer includes a newsletter signup form with a `{rounded.full}` input and a `button-primary` submit. Padding is `{spacing.section}` (64px) top and bottom, with `{spacing.lg}` (24px) side padding.

### Accordion
**`accordion`** — A white card with `{rounded.sm}` (8px) corners and a 1px `{colors.hairline-soft}` border. The header uses `{typography.title-md}` (16px/600 weight) with 16px/24px padding. On click, the accordion expands to reveal content with 24px side padding and 24px bottom padding. Used for product descriptions, specifications, and shipping details.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger, product cards stack vertically, hero height reduces to 300px, font sizes scale down one step (display-xl → 28px), footer columns stack |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but logo shrinks, hero height at 400px, font sizes at 90% of desktop |
| Desktop | 1128–1440px | Three-column product grid, full nav with uppercase links, hero at 500px, standard font sizes |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero may extend full viewport width with content constrained to 1440px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets (title, image, price) are at least 48px tall
- Nav links on mobile have 48px tap areas
- Accordion headers have 48px minimum tap height
- Search bar and text inputs are 48px tall

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-in drawer from the left
- The product filter sidebar collapses into a bottom sheet or modal on mobile
- The footer's multi-column layout collapses into a single column with accordion-style section headers
- The hero's side-by-side content (text + image) stacks vertically on mobile
- Product cards in the grid collapse from 3-4 columns to 2 columns on tablet and 1 column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; actual extracted hover colors were not available from the static CSS analysis
- Error and success styling for forms (validation messages, input states) was not extractable; colors are best guesses based on web conventions
- The exact font weights for Montserrat and Lato in use could not be determined from the extracted font-family declarations alone; weights are inferred from typical usage in the orchestral instrument e-commerce space
- Dark mode is not present on the live site and has not been designed
- The specific border-radius values for cards and buttons were not extractable from the static analysis; values are based on visual inspection of the site's rounded-corner aesthetic
- The accent gold color (#a16a00) appears in price highlights and sale badges but its exact usage frequency and secondary applications (e.g., hover states, link underlines) could not be confirmed
- The hero overlay opacity (rgba(0,0,0,0.3)) is an estimate; the actual overlay may be lighter or darker depending on the hero image
- The product card shadow on hover (0 4px 12px rgba(0,0,0,0.08)) is a common pattern but the exact shadow values were not extractable
- The nav-bar scroll behavior (adding a bottom border) is inferred from common sticky navigation patterns
- The mobile hamburger menu animation and drawer width were not extractable
- The newsletter signup form in the footer is assumed based on common e-commerce patterns; its exact styling was not visible in the extracted data
- The accordion component's expand/collapse animation timing and easing were not extractable
- The product card's image scale-on-hover effect (2% scale, 300ms ease) is a common pattern but the exact values are estimates
- The font stack order (Montserrat before Lato) is inferred from the extracted declarations; the actual fallback order may differ
- The star-rating color (#a16a00) is assumed to match the accent gold, but the actual rating color could not be confirmed from the extracted data
