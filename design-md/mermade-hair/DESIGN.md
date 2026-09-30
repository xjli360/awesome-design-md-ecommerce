---
version: alpha
name: "Mermade Hair"
source_url: "https://www.mermadehair.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dreamy, mermaid-core haircare brand that lives in a soft-focus world of blush pinks and muted mauves. The palette is anchored by {colors.primary} (#fdd4eb), a whisper-light bubblegum that appears on CTAs, badges, and hover states, and {colors.primary-active} (#ffbae0), a slightly warmer rose that signals interaction. Against a {colors.canvas} (#f7f7f8) background, the brand uses {colors.ink} (#1c1b1b) for body copy and {colors.body} (#363636) for headings, creating a gentle but legible contrast. Accent colors like {colors.accent-sage} (#b2f9e9) and {colors.accent-lavender} (#676986) appear in product badges and ingredient callouts, while {colors.hairline} (#dddddd) and {colors.hairline-soft} (#e5e5e5) define card borders and dividers. The typography pairs Playfair Display for editorial headlines with Work Sans for body text, giving the brand a modern-yet-romantic feel. Buttons use {rounded.full} pill shapes, product cards have {rounded.lg} corners, and the overall spacing is generous — {spacing.section} (64px) between major blocks — creating a spa-like, unhurried browsing experience. The brand's signature move is the "mermaid wave" motif: soft, undulating lines in illustrations and the liberal use of {colors.primary} (#fdd4eb) as a wash behind product imagery.

colors:
  primary: "#fdd4eb"
  primary-active: "#ffbae0"
  primary-disabled: "#f0c8cb"
  ink: "#1c1b1b"
  body: "#363636"
  muted: "#676986"
  muted-soft: "#84525c"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#363636"
  accent-sage: "#b2f9e9"
  accent-lavender: "#676986"
  accent-rose: "#ffadc9"
  accent-mauve: "#84525c"
  badge-new: "#ffbae1"
  badge-sale: "#fdd4eb"
  star-rating: "#272d45"
  scrim: "#121212"
  error: "#c13515"
  success: "#1990c6"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Work Sans', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 20px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.accent-mauve}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.md} 0"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. Rendered as a pill shape with {colors.primary} (#fdd4eb) background and {colors.on-primary} (#363636) text. On hover, shifts to {colors.primary-active} (#ffbae0). Disabled state uses {colors.primary-disabled} (#f0c8cb) with {colors.muted} (#676986) text. **`button-secondary`** — An outlined variant with a white background and 2px {colors.hairline} (#dddddd) border. Used for "Learn More" and secondary actions. Active state gains a {colors.primary} border. **`button-tertiary`** — A text-only button with no background or border, used for "Cancel" or "View Details" links. Active state changes text to {colors.primary-active}. **`button-pill`** — A smaller, compact pill used for filter tags, "Quick Add", and micro-actions. Uses {colors.primary} background with {typography.button-sm} sizing.

### Cards
**`product-card`** — The core product display component, featuring a white background with {rounded.lg} corners and {spacing.base} padding. The product image sits in a {rounded.md} container. The title uses {typography.title-sm} and the price uses {typography.body-md} in {colors.body}. On hover, a subtle box-shadow elevates the card. Used in grid layouts on collection pages and "You May Also Like" sections.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background. Links use {typography.nav-link} (14px uppercase Work Sans) in {colors.body}. Active links get a 2px bottom border in {colors.primary}. The nav includes a centered logo, left-aligned category links, and right-aligned icons for search, account, and cart.

### Forms
**`text-input`** — Standard text input with a white background, {rounded.md} corners, and a 1px {colors.hairline} border. On focus, the border thickens to 2px and turns {colors.primary}. Error state uses a 2px {colors.error} (#c13515) border. Used for email signup, search, and checkout fields.

### Footer
**`footer`** — A full-width footer with {colors.surface-soft} (#f4f4f6) background. Contains columns for customer service, about, and social links. Links use {typography.link} in {colors.muted} (#676986) and hover to {colors.primary}. Includes newsletter signup with a {rounded.full} email input and submit button.

### Badges
**`badge-new`** — A small pill badge with {colors.badge-new} (#ffbae1) background, used to flag new arrivals. **`badge-sale`** — Uses {colors.badge-sale} (#fdd4eb) with {colors.accent-mauve} (#84525c) text for sale items. Both use {typography.badge} (11px uppercase, bold).

### Accordion
**`accordion`** — Used for product descriptions, FAQs, and shipping details. Each item has a {typography.title-sm} header with a 1px {colors.hairline-soft} bottom border. Content area uses {typography.body-sm} in {colors.body} with {spacing.md} vertical padding.

### Star Rating
**`star-rating`** — A 14px star icon set in {colors.star-rating} (#272d45). Used on product cards and review sections. Empty stars render in {colors.hairline-soft}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, reduced hero height (300px), stacked footer columns, smaller display-xl (32px) |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, hero at 400px, footer in two rows |
| Desktop | 1128–1440px | Three-column product grid, full nav with dropdowns, hero at 400px, footer in four columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero at 480px |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44x44px touch target on mobile
- Product card tap targets (Add to Cart, Quick View) are at least 48px tall
- Nav icons (search, cart, account) are 44x44px with 8px padding
- Accordion headers are 48px tall for easy tapping

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer
- Product filters collapse into a bottom sheet or modal
- Footer columns stack vertically on mobile
- Hero content stacks (text above CTA) below 744px
- Product image galleries collapse to single-image carousels
- Multi-column product descriptions collapse to accordion sections

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom effect, secondary image reveal) — not reliably extracted from CSS
- Error state styling for form validation (specific border colors, error message typography)
- Success/confirmation state styling (checkout, email signup)
- Dark mode palette — not present on the live site
- Sub-brand palettes (if any exist for limited editions or collaborations)
- Animation timing and easing curves (transitions, hover effects, page loads)
- Specific icon set and sizes (social media, payment methods, shipping)
- Dropdown menu styling for navigation (mega menu vs. simple dropdown)
- Modal/overlay styling (quick view, size guide, cart drawer)
- Loading state skeletons and spinners
- Focus ring styles for keyboard navigation
- Print stylesheet specifications
