---
version: alpha
name: "CASETiFY"
source_url: "https://www.casetify.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A playground of personal expression where the phone case becomes a canvas, anchored on a stark white background that lets every color pop with maximum saturation. The brand's primary voltage is a deep, confident blue (#003399) that appears in the logo, primary CTAs, and navigation — a deliberate anchor against the riot of accent colors (#f4477b, #5dd7d7, #f47245, #edcf43, #b8e356, #da2eda, #ffbb44) that appear in product collections and limited-edition drops. CASETiFY's design language is fundamentally about contrast: the white canvas ({colors.canvas}) against saturated product photography, the heavy blue header against playful typography that mixes AvenirNext for body with decorative fonts like Bougenville and Comic Neue Angular for special collections. Buttons carry a soft {rounded.sm} radius — friendly but not childish — while product cards use {rounded.md} to frame the phone case as an object worth displaying. The brand trusts its product photography to do the heavy lifting; UI chrome stays minimal, with thin {colors.hairline} borders and generous {spacing.lg} padding that gives each product room to breathe. The result feels like walking through a gallery where every phone case is an artwork, with the brand's role being simply to frame it beautifully.

colors:
  primary: "#003399"
  primary-active: "#002a7a"
  primary-disabled: "#b3c6e6"
  ink: "#222222"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#d9d9d9"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#f4477b"
  accent-teal: "#5dd7d7"
  accent-orange: "#f47245"
  accent-yellow: "#edcf43"
  accent-green: "#b8e356"
  accent-purple: "#da2eda"
  accent-red: "#ce0000"
  accent-gold: "#ffbb44"
  star-rating: "#ffbb44"
  badge-new: "#f4477b"
  badge-sale: "#ce0000"
  badge-limited: "#da2eda"

typography:
  display-xl:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'AvenirNext', 'Avenir-Roman', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  decorative:
    fontFamily: "'Bougenville', 'Comic Neue Angular', cursive"
    fontSize: 24px
    fontWeight: 400
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
    border: "2px solid {colors.ink}"
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-colors:
    display: "flex"
    gap: "{spacing.xs}"
    marginTop: "{spacing.sm}"
  badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  color-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    textAlign: "center"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    textAlign: "center"
    maxWidth: 600px
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
    overflowX: "auto"
  category-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
    whiteSpace: "nowrap"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
    whiteSpace: "nowrap"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. Rendered in the brand's deep blue (#003399) with white text and a soft 8px radius. On hover, shifts to a darker shade ({colors.primary-active}); disabled state uses a muted blue ({colors.primary-disabled}) with reduced opacity. Text is set in AvenirNext 600 weight with 0.3px letter spacing for clarity.

**`button-secondary`** — An outlined alternative for secondary actions like "Learn More" or "View Details". White background with a 2px solid ink border. On hover, fills with ink background and inverts text to white. Maintains the same 48px height and 8px radius as the primary button for visual consistency.

**`button-accent-pink`** — Used for limited-edition drops, collaborations, and promotional CTAs. Uses the brand's signature pink (#f4477b) to create urgency and excitement. Same structural properties as `button-primary` but with a more playful, attention-grabbing color.

**`button-accent-teal`** — A secondary accent button for eco-friendly collections or sustainability messaging. Uses teal (#5dd7d7) with dark text for a fresh, approachable feel. Often paired with leaf icons or environmental badges.

**`button-ghost`** — A text-only button with no background, used for "View All" links, "See Details", and tertiary navigation. On hover, gains a subtle background tint of the primary color at 10% opacity. Maintains the same typography and height as other buttons for alignment in button groups.

### Cards
**`product-card`** — The core product display unit, a white card with 12px radius and subtle shadow. Contains a square product image with 8px radius, product title in 16px/500 weight, price in 16px/600 weight, and a row of color swatches. On hover, the shadow deepens and a subtle scale transform (1.02) signals interactivity. The card is designed to let the product photography dominate — UI elements are minimal and pushed to the bottom.

**`product-card-colors`** — A flex row of 24px circular color swatches showing available case colors. Each swatch has a 2px hairline border; the selected swatch gets a 2px ink border. Swatches are spaced 4px apart and can overflow into a "+N more" label when there are more than 6 colors.

### Navigation
**`nav-bar`** — A fixed 64px header with white background and thin bottom border. Contains the CASETiFY logo (left), navigation links (center, uppercase with 0.5px letter spacing), and utility icons for search, cart, and account (right). On scroll, gains a subtle box-shadow. Navigation links are 14px/600 weight with 16px horizontal padding; the active link gets a 2px primary-color bottom border.

**`nav-link`** — Individual navigation items styled as uppercase text with generous letter spacing. Inactive links use ink color; active links switch to primary blue with an underline indicator. Hover state adds a subtle background tint.

### Forms
**`text-input`** — Standard input field with white background, 8px radius, and 1px hairline border. On focus, the border thickens to 2px and switches to primary blue. Error state uses a 2px red border. Height is 48px to match button heights for aligned form layouts. Padding is 12px vertical / 16px horizontal.

### Search
**`search-bar`** — A pill-shaped search field (full radius) with light gray background and thin border. On focus, the border switches to primary blue. Used in the header for product search and on the search results page. Height is 44px to sit comfortably in the nav bar without overwhelming the layout.

### Badges
**`badge`** — Small, uppercase labels used to flag product attributes. Default badge uses the brand's pink (#f4477b) for "NEW" tags. Variants include red for "SALE", purple for "LIMITED EDITION", and teal for "ECO-FRIENDLY". All badges share the same 10px/700 weight typography with 0.5px letter spacing, 4px radius, and 2px/8px padding.

### Footer
**`footer`** — A dark footer section with ink background and white text. Contains columns for support, about, legal, and social links. Links are 14px/400 weight in muted gray, switching to white on hover. Padding is generous at 48px vertical and 64px horizontal on desktop.

### Hero
**`hero-section`** — Full-width white section with centered content. Contains a large headline (36px/700 weight), a subtitle in body text, and optional CTAs. No background color — relies on product photography or lifestyle imagery for visual impact. Padding is 64px vertical.

### Category Strip
**`category-strip`** — A horizontally scrollable strip of pill-shaped category tabs. Each tab is a pill with light gray background and body text. The active tab switches to primary blue with white text. Tabs are 14px/600 weight with 8px/20px padding. The strip has no visible scrollbar on desktop; on mobile, it scrolls with momentum.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), nav collapses to hamburger menu, hero text reduces to 28px, category strip becomes full-width scrollable, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (3 columns), nav links visible but condensed, search bar shrinks to icon-only, category strip shows 6-8 visible tabs |
| Desktop | 1128–1440px | Three-column product grid (4 columns), full nav with all links, expanded search bar, category strip shows 10+ tabs, footer has 4-column layout |
| Wide | > 1440px | Four-column product grid (5 columns), max-width container at 1440px, extra whitespace on sides, category strip centered with max-width |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Color swatches minimum 32px diameter on mobile
- Nav links minimum 44px tap area (padding extends beyond text)
- Search bar minimum 44px height
- Category tabs minimum 44px height

### Collapsing Strategy
- Primary nav links collapse into hamburger menu below 744px
- Search bar collapses to icon-only below 744px, expands to full bar on tap
- Product grid reduces columns: 5 → 4 → 3 → 2 as viewport shrinks
- Footer columns collapse from 4 to 2 to 1
- Category strip shows fewer tabs with overflow scroll on mobile
- Hero section reduces font sizes and padding on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary button and product card have extracted hover data)
- Error states for forms beyond text-input (select dropdowns, checkboxes, radio buttons)
- Loading states and skeleton screens for product grids and search results
- Dark mode or high-contrast mode specifications
- Animation durations and easing curves (transitions, hover effects, page loads)
- Modal and overlay styling (quick-view, cart drawer, size guide)
- Dropdown menu styling (country selector, sort options, account menu)
- Sub-brand palettes for collaborations (Disney, NBA, etc. — each has unique accent colors)
- Print stylesheet specifications
- Focus-visible styles for keyboard navigation
- Custom checkbox and radio button styling
- Tooltip and popover styling
- Accordion and disclosure widget styling
- Pagination component styling
- Breadcrumb component styling
- Rating star component exact sizing and spacing
- Quantity selector component (increment/decrement buttons)
- Image zoom and lightbox styling for product detail pages
