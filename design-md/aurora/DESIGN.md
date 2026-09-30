---
version: alpha
name: "Aurora"
source_url: "https://auroragift.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A plush toy brand that uses #0052b4 as its primary blue — a saturated, almost electric cobalt — to signal softness through confidence rather than pastel. The palette is built on a high-contrast structure: #232323 ink for headlines, #f8f8f8 canvas for backgrounds, and #d80027 as a sharp accent red that appears on sale badges and promotional banners. Product photography is the real texture layer; the design system stays out of its way with generous whitespace, {rounded.md} card corners, and Poppins at 400/500 weight — a geometric sans that reads clean at small sizes on mobile product grids. The brand's signature move is the "squish" badge: a small {rounded.sm} pill in #ff8b21 orange with white text that calls out specific plush qualities ("Super Soft", "Huggable"), placed at the top-left corner of product cards. Navigation is minimal — a sticky top bar with a centered logo, search icon, cart icon, and account link, all in {colors.ink} on {colors.canvas}. The footer is dense with utility links in {colors.muted} (#969696) and a newsletter signup bar that uses {rounded.full} input fields. There is no hero carousel; the homepage leads with a full-width banner image and a single CTA button in {colors.primary} with white text, {rounded.sm} corners, and 48px height. The brand trusts its product imagery to carry emotion — the system provides a neutral, legible container.

colors:
  primary: "#0052b4"
  primary-active: "#003d8a"
  primary-disabled: "#b3cff5"
  ink: "#232323"
  body: "#323232"
  muted: "#969696"
  muted-soft: "#cbcbcb"
  hairline: "#e6e6e6"
  hairline-soft: "#f0f0f0"
  canvas: "#f8f8f8"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d80027"
  accent-orange: "#ff8b21"
  accent-yellow: "#ffc617"
  badge-sale: "#e4002b"
  badge-new: "#2f70ee"
  rating-star: "#e0b252"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px

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
  button-primary-hover:
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
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
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
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 24px
    padding: 8px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-squish:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  rating-stars:
    color: "{colors.rating-star}"
    fontSize: 14px
  product-grid:
    gap: "{spacing.base}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand's cobalt blue {colors.primary} background with white text in Poppins medium at 16px. Corners are softly squared at {rounded.sm} (8px). On hover, the background deepens to {colors.primary-active} (#003d8a). The disabled state uses {colors.primary-disabled} (#b3cff5) — a pale, desaturated blue that reads as inactive without visual noise. Height is fixed at 48px with 14px top/bottom padding and 28px left/right for comfortable tap targets.

**`button-secondary`** — An outlined alternative for less prominent actions. White background with {colors.ink} text and a 1px {colors.hairline} border. On hover, the background shifts to {colors.surface-soft} and the border to {colors.muted}. Same 48px height and {rounded.sm} corners as the primary button, maintaining visual consistency across the button family.

**`button-accent-red`** — Used for urgent or promotional actions like "Shop Sale" or "Limited Stock". Uses {colors.accent-red} (#d80027) background with white text. Slightly shorter at 40px height with 10px/20px padding, making it suitable for inline use within product cards or banners.

### Badges
**`badge-sale`** — A small, high-contrast pill in {colors.badge-sale} (#e4002b) with white uppercase text at 11px bold. Used to flag discounted items on product cards and collection pages. The {rounded.sm} corners and compact padding (4px 8px) let it sit neatly in the top-left corner of product images without obscuring too much of the photo.

**`badge-new`** — A blue variant in {colors.badge-new} (#2f70ee) for "New Arrival" flags. Same typography and sizing as the sale badge, maintaining a consistent badge system. The blue is slightly more saturated than the primary, creating visual distinction between badge types.

**`badge-squish`** — Aurora's signature badge in {colors.accent-orange} (#ff8b21). Used to call out specific plush qualities like "Super Soft", "Huggable", or "Squishy". The warm orange stands out against the blue primary palette and signals the tactile, playful nature of the product.

### Cards
**`product-card`** — The primary product display unit. A white card with {rounded.md} (12px) corners and no border — the card sits on the {colors.canvas} (#f8f8f8) background, using negative space for separation. The product image fills the top of the card with rounded top corners only ({rounded.md} {rounded.md} 0 0). Below the image, the product title appears in {typography.title-sm} (Poppins 500, 16px) with {spacing.sm} top padding and {spacing.base} side padding. The price follows in {typography.body-md} at {colors.body} with {spacing.sm} bottom padding. Badges overlay the top-left of the image area.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height with white background and a subtle bottom border in {colors.hairline-soft}. The logo is centered, with icon buttons for search, account, and cart on the right side. Navigation links use {typography.nav-link} (Poppins 500, 14px) in {colors.ink}. On mobile, the nav collapses to a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — Full-rounded input fields ({rounded.full}) with white background, 1px {colors.hairline} border, and 48px height. On focus, the border thickens to 2px and shifts to {colors.primary}. Used for search bars, newsletter signup, and checkout forms. The pill shape is a deliberate design choice to feel approachable and soft — no sharp corners anywhere in the form system.

**`footer-newsletter-input`** and **`footer-newsletter-button`** — A paired input and button for the email signup in the footer. Both use {rounded.full} corners and 44px height. The input has a 1px {colors.hairline} border, while the button uses {colors.primary} background. They sit side by side in a flex row, creating a seamless pill-shaped form.

### Hero
**`hero-banner`** — A full-width banner section at 400px height on desktop, scaling down proportionally on mobile. The background is {colors.canvas} with the hero image filling the container. Text overlays use {typography.display-xl} (Poppins 600, 32px) in {colors.ink}. A single {hero-cta} button sits below the headline, using the same {button-primary} styling but with wider padding (14px 32px) for visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid goes to 2 columns; nav-bar collapses to hamburger; hero-banner height reduces to 250px; footer stacks vertically; search bar becomes full-width below nav |
| Tablet | 744–1128px | Product grid uses 3 columns; nav-bar shows limited links (logo, search, cart); hero-banner at 320px; footer uses 2-column layout |
| Desktop | 1128–1440px | Product grid uses 4 columns; full nav-bar visible; hero-banner at 400px; footer uses 4-column layout with newsletter |
| Wide | > 1440px | Max-width container at 1440px; product grid can use 5 columns; hero-banner content centered with max-width |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (exceeds Apple's 44pt guideline)
- Icon buttons in nav-bar are 24px with 8px padding, creating a 40px effective touch area
- Product cards have full-surface tap targets (no dead zones)
- Search bar input is 48px tall for comfortable typing
- Footer links have 36px minimum tap height with generous spacing

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Product grid columns reduce from 4 to 2 on mobile
- Footer columns stack vertically on mobile (4-column → 2-column → 1-column)
- Hero banner text overlay reduces font size and padding on mobile
- Search bar moves from inline nav to full-width below nav on mobile
- Product card badges scale down font size on mobile (11px → 10px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site CSS; the hover colors provided for buttons are inferred from common patterns and should be verified against the actual implementation
- Error states for form inputs (validation colors, error messages) were not visible in the extracted data
- Dark mode styling is not present on the live site and was not extracted
- Sub-brand or seasonal palette variations (e.g., holiday collections, licensed characters) were not captured
- The exact font weight for Poppins across different text styles could not be confirmed from the extracted CSS; weights shown are based on typical usage patterns for the font
- Animation and transition durations/easings were not extracted
- Dropdown menu styling (e.g., account menu, country selector) was not visible in the extracted data
- The extracted color list includes several generic web colors (#3d4852, #606f7b, #dff0d8, #fff2dd) that are likely from Shopify's default theme or third-party widgets — these have been excluded from the palette
- The brand's true primary blue (#0052b4) was selected as the most distinctive color from the extracted list, but the live site may use additional brand-specific colors not captured in the extraction
