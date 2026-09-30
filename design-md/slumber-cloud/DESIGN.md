---
version: alpha
name: "Slumber Cloud"
source_url: "https://www.slumbercloud.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Slumber Cloud is a sleep-focused DTC bedding brand that wraps its promise of cooler, more restful nights in a palette of calm, clinical precision and warm, approachable comfort. The brand's visual identity is anchored on a near-white canvas (#fafafa) and a soft, almost ethereal surface (#fcfaf1), against which a restrained set of accent colors — a deep navy (#191c2f, #1b1d36), a muted crimson (#d72c0d), a cooler red (#e8144b), and a fresh mint (#13a165) — create moments of deliberate contrast. The primary ink (#191919) is a near-black, used for body copy and headlines, while secondary text (#5e5e5e) and muted tones (#9ea2a2, #cbcbcb) keep the hierarchy calm and legible. Typography relies on Roboto, a clean, geometric sans-serif that feels both modern and trustworthy, with display sizes using modest weights (500–600) rather than heavy 700+ — the brand trusts its product photography and generous whitespace over typographic muscle. Signature design moves include softly rounded cards (`{rounded.md}` ~12px) and pill-shaped CTAs (`{rounded.full}`) that read as friendly and human, while the persistent use of a deep navy (#191c2f) for navigation and footer backgrounds grounds the page and creates a sense of stability. The brand's voice is reassuring and scientific — it speaks of "cooling technology" and "temperature regulation" without feeling clinical, using a warm red (#d72c0d) sparingly for urgency (sale badges, limited-time offers) and a soft green (#13a165) for positive signals (in-stock, free shipping). The overall effect is a brand that feels like a well-made bed: clean, inviting, and designed for deep, uninterrupted rest.

colors:
  primary: "#d72c0d"
  primary-active: "#c30000"
  primary-disabled: "#e0b5b2"
  ink: "#191919"
  body: "#333333"
  muted: "#5e5e5e"
  muted-soft: "#9ea2a2"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#191c2f"
  navy-light: "#1b1d36"
  accent-red: "#e8144b"
  accent-green: "#13a165"
  accent-green-soft: "#e0faef"
  accent-pink: "#fff4fa"
  accent-mint: "#aaccaa"
  accent-teal: "#b8e3e7"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  badge-sale: "#d72c0d"
  badge-sale-text: "#ffffff"
  badge-new: "#13a165"
  badge-new-text: "#ffffff"
  star-rating: "#191919"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
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
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.hairline}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
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
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 500
  product-card-sale-price:
    textColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-instock:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.accent-green}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-section-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "{spacing.base} {spacing.lg}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  review-card-name:
    typography: "{typography.title-sm}"
    fontWeight: 600
  review-card-text:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-navy:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. It uses the brand's signature red (#d72c0d) on a white background, with a soft 8px radius. On hover, it deepens to a richer red (#c30000). When disabled, it fades to a muted pink (#e0b5b2) to signal inactivity.

**`button-secondary`** — A secondary action button with a white background and a subtle hairline border (#dedede). Used for "Learn More" or "View Details" links that should not compete with the primary CTA. On hover, the border darkens slightly.

**`button-tertiary`** — A text-only link styled as a button, with an underline. Used for "See All" or "Read Reviews" actions within content sections. No background or border.

**`button-pill`** — A fully rounded pill button used for promotional badges, "Subscribe & Save" CTAs, or quick-add actions. Shares the primary red background but uses a smaller font size and generous horizontal padding for a compact, friendly appearance.

**`button-pill-outline`** — An outlined version of the pill button, used for secondary promotional actions like "Learn More" on hero banners. White background with a hairline border.

**`button-navy`** — A dark navy (#191c2f) button used on light backgrounds for a more subdued but still prominent CTA. Often appears in footer or secondary hero sections.

### Cards
**`product-card`** — The primary product display card, with a white background, soft 12px radius, and a subtle drop shadow. On hover, the shadow deepens to create a lifted effect. Contains the product image, title, price (with sale price in red), and optional badges.

**`review-card`** — A customer review card with a white background, soft radius, and a light border. Displays star rating, reviewer name, and review text. Used in product detail pages and homepage social proof sections.

### Navigation
**`nav-bar`** — The top navigation bar, fixed to the top of the page with a dark navy background (#191c2f). Contains the logo, navigation links, search icon, and cart icon with a badge. On scroll, it transitions to a white background with a subtle shadow.

**`nav-link`** — Navigation links in the top bar, set in uppercase Roboto with 0.25px letter spacing. Active links use the primary red for emphasis.

**`footer`** — The site footer, using the same dark navy background as the nav bar. Links are set in a muted gray (#9ea2a2) to reduce visual weight while maintaining readability.

### Forms
**`text-input`** — Standard text input fields with a white background, soft 8px radius, and a hairline border. On focus, the border becomes a 2px primary red line. Error states use a 2px red (#e8144b) border.

**`select-input`** — Dropdown select fields styled consistently with text inputs, using the same dimensions and border treatment.

**`search-bar`** — A fully rounded search bar used in the header and on search pages. White background with a hairline border and generous padding for a comfortable typing experience.

### Badges
**`badge-sale`** — A small, uppercase badge with a red background (#d72c0d) and white text. Used to highlight discounted products or limited-time offers.

**`badge-new`** — A green (#13a165) badge on a soft green background (#e0faef) for new arrivals or recently added products.

**`badge-instock`** — A subtle in-stock indicator using the same green palette, styled as a caption-sized label.

### Hero
**`hero-section`** — Full-width hero banners with a dark navy background and white text. Used for major campaigns and seasonal promotions. The `hero-section-alt` variant uses a light gray background (#f1f1f1) with dark text for a softer introduction.

### Accordion
**`accordion`** — Collapsible content sections used for product details, FAQ, and shipping information. White background with a hairline border and soft radius. Headers use the title typography with 16px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger menu, product cards stack vertically, hero text reduces to 24px, buttons become full-width, search bar moves to mobile menu |
| Tablet | 744–1128px | Two-column product grids, nav links remain visible but reduced spacing, hero maintains two-column layout with smaller text, side-by-side product details |
| Desktop | 1128–1440px | Full three- or four-column product grids, expanded nav with all links visible, hero uses full display-xl typography, multi-column footer |
| Wide | > 1440px | Max-width container (1440px) centered, additional whitespace on sides, product grids can expand to five columns, hero content centered with wider margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 44px touch areas
- Product card CTAs are 48px tall for easy tapping
- Nav links have 16px horizontal padding for comfortable touch targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), with the logo centered and cart icon visible
- Product filters collapse into a slide-out drawer on mobile and tablet
- Footer link columns stack vertically on mobile, with accordion-style expandable sections
- Product image galleries collapse to single-image carousels on mobile
- Multi-column content sections (reviews, features) collapse to single-column stacks

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be reliably extracted (assumed border darkening or underline changes)
- Focus ring styles for keyboard navigation are not specified (assume 2px primary color outline offset)
- Error message styling for form validation (color, placement, iconography) is not documented
- Dark mode color overrides are not available from the extracted data
- Sub-brand or collection-specific palette variations (e.g., "Cooling Comforter" vs "Pillow" lines) may exist but are not captured
- Loading states (skeleton screens, spinner colors) are not defined
- Modal and overlay styling (backdrop color, close button placement) is not documented
- Tooltip and popover styling (background, arrow, shadow) is not available
- Print stylesheet overrides are not specified
- Animation and transition timing values (duration, easing) are not extracted
- The exact font-weight for Roboto variants (300, 400, 500, 700) is assumed based on common usage; actual weights may vary by component
