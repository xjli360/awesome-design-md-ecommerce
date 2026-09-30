---
version: alpha
name: "Lofree"
source_url: "https://www.lofree.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A teal #108474 pulse runs through every Lofree surface — the brand's signature voltage that turns mechanical keyboards into desk jewelry rather than utility tools. The site reads like a design studio portfolio: generous white canvas (#ffffff), product photography that floats against soft #edf5f5 backdrops, and a single gold accent (#ffd700) reserved for limited-edition badges and "NEW" flags. Typography splits between Lato for clean product specs and Lora for editorial storytelling — a serif/sans-serif dialogue that signals "we take design seriously but not ourselves." Buttons carry {rounded.sm} corners, while product cards use {rounded.md} to soften the hard geometry of keyboard grids. The nav bar stays transparent until scroll, then snaps to a white surface with a subtle {colors.hairline} bottom border — a quiet acknowledgment of hierarchy without shouting. Every product page leads with a hero image that bleeds edge-to-edge, the keyboard angled just so to catch light on keycaps, the brand name set in a condensed sans at 48px. This is a brand that sells objects of desire, not peripherals.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5cc"
  ink: "#050505"
  body: "#1a1a1a"
  muted: "#7b7b7b"
  muted-soft: "#dadada"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  surface-teal: "#edf5f5"
  on-primary: "#ffffff"
  gold: "#ffd700"
  gold-active: "#fbcd0a"
  star-rating: "#121212"

typography:
  display-xl:
    fontFamily: "'Lora', 'Roboto Condensed', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto Condensed', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  product-name:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    padding: 12px 28px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-gold-active:
    backgroundColor: "{colors.gold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-outline-gold:
    backgroundColor: transparent
    textColor: "{colors.gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.gold}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(16, 132, 116, 0.15)"
  text-input-error:
    border: "1px solid #e74c3c"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.04)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    transform: "translateY(-2px)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1/1"
  product-card-badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  product-card-original-price:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  hero-section:
    backgroundColor: "{colors.surface-teal}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  hero-image:
    rounded: "{rounded.md}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(16, 132, 116, 0.15)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
  divider-light:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  section-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  feature-grid:
    gap: "{spacing.lg}"
  feature-item:
    textAlign: "center"
    padding: "{spacing.lg}"
  feature-icon:
    width: "48px"
    height: "48px"
    marginBottom: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the brand's signature teal #108474. Used for "Add to Cart", "Pre-order", and primary checkout flows. On hover, shifts to `{colors.primary-active}` with a subtle scale transform. Disabled state uses `{colors.primary-disabled}` with reduced opacity. Secondary buttons invert to a white fill with a 2px teal border, used for "Learn More" and secondary product actions. Gold buttons (`{colors.gold}`) are reserved for limited-edition launches and special collections, with `{colors.gold-active}` on hover. Ghost buttons provide a text-only option for tertiary actions like "Cancel" or "View Details".

### Cards
**`product-card`** — The primary product display unit, a white card with soft `{rounded.md}` corners and a subtle drop shadow. The image occupies the top half with matching top-radius rounding. A gold badge overlays the top-left corner for limited editions, while a teal badge marks new arrivals. On hover, the card lifts 2px with an enhanced shadow. Price is set in `{typography.price}` with sale prices in teal and original prices struck through in muted gray. Star ratings use `{colors.star-rating}` at 16px.

### Navigation
**`nav-bar`** — A 72px transparent bar that becomes white with a subtle bottom border on scroll. Navigation links are uppercase Lato at 14px weight 600, with the active page underlined in teal. The logo sits left-aligned, typically as an SVG that inherits `{colors.ink}`. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard input fields with a 1px hairline border and `{rounded.sm}` corners. On focus, the border shifts to teal with a 3px teal shadow ring. Error states use a red border (#e74c3c). The search bar is pill-shaped (`{rounded.full}`) with a magnifying glass icon, used in the header and on collection pages.

### Footer
**`footer`** — A dark inversion on `{colors.ink}` with white text. Links are `{colors.muted-soft}` and lighten to full white on hover. The footer is divided into columns for product categories, support, and social links. A thin `{colors.hairline}` divider separates the newsletter signup from the link columns.

### Hero
**`hero-section`** — Full-width section on `{colors.surface-teal}` with a large serif headline (`{typography.display-xl}`) and a muted subtitle. The hero image floats with `{rounded.md}` corners, often featuring a keyboard angled diagonally to catch light. Used on the homepage and collection landing pages.

### Accordion
**`accordion`** — Expandable sections with a `{colors.title-sm}` header and a bottom border separator. Used for product descriptions, specifications, and FAQ. The chevron icon rotates on open. Content padding is `{spacing.base}` on all sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 28px; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 36px headline; side-by-side footer columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 48px; max-width container at 1128px |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns; hero image scales up |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Product card tap targets are the full card surface
- Accordion headers are 48px minimum height
- Quantity selector buttons are 40x40px minimum

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile
- Hero section reduces padding and font size on mobile
- Accordion content is collapsed by default on all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges and footer links are inferred from common patterns, not extracted from live CSS
- Error styling for forms (red border) is a standard assumption, not extracted from the site
- Dark mode is not implemented on the live site
- Sub-brand or collection-specific color variants (e.g., Flow, FL980) could not be extracted
- Typography scale for display sizes is estimated from page structure; exact font sizes for every heading level were not extractable
- Button padding and height values are approximated from common e-commerce patterns
- Animation durations and easing curves were not extractable from the live site
- The "JudgemeStar" font family suggests a review widget integration, but its exact styling is not captured
