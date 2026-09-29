---
version: alpha
name: "Jade Yoga"
source_url: "https://jadeyoga.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, grounded brand built on a forest-floor palette where #108474 (a saturated pine-teal) acts as the primary voltage — appearing on every add-to-cart button, membership CTA, and footer background — while #1b4515 (a near-black forest green) anchors headers and the top navigation bar. The brand’s secondary accent #eb593c (a warm, dried-coral) appears sparingly on sale badges and promotional banners, creating a tension that reads as energetic rather than urgent. The canvas is #f9fafb, a cool off-white that keeps the site from feeling sterile, while #eeeeee and #f2f2f2 form the hairline and surface-soft layers. Typography runs Poppins at 400/500/600 weights — the display sizes use 600 weight at 28px, while body copy sits at 16px/400 with 1.5 line-height, creating a clean, readable hierarchy that lets product photography (mats, blocks, apparel shot on natural textures) carry the emotional weight. Buttons are softly squared at {rounded.sm} (8px), product cards use {rounded.md} (12px), and the search bar employs {rounded.full} pills. The brand avoids hard corners entirely except on the body grid. A secondary accent #a89cc8 (a muted lavender) appears in the footer and on membership badges, hinting at a meditation/wellness sub-brand without overwhelming the core green system. The overall feel is of a well-worn studio mat — clean but not sterile, serious but not severe.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d5cc"
  ink: "#1b4515"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#868686"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#eb593c"
  accent-lavender: "#a89cc8"
  accent-gold: "#fbcd0a"
  badge-sale: "#d02e2e"
  badge-new: "#56ad6a"
  badge-new-bg: "#ecfef0"
  star-rating: "#fbcd0a"
  scrim: "#191919"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-coral}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.accent-coral}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  badge-membership:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in {colors.primary} pine-teal with white text and {rounded.sm} corners. Used for "Add to Cart", "Join Membership", and "Shop Now" actions. On hover, the background shifts to {colors.primary-active} (#0d6b5e). The disabled state uses {colors.primary-disabled} (#a3d5cc) with the same white text. All primary buttons use uppercase Poppins 600 at 14px with 0.5px letter-spacing.

**`button-secondary`** — An outlined variant with a transparent background, {colors.ink} text, and a 2px solid {colors.ink} border. Used for "Learn More" and secondary actions alongside primary buttons. Hover state fills the background with {colors.ink} and inverts text to white.

**`button-tertiary-text`** — A text-only button with no background or border, using {colors.primary} text. Used for "View All" links in category strips and "Cancel" actions in modals. Hover state adds underline.

**`button-accent-coral`** — A promotional variant using {colors.accent-coral} (#eb593c) as background. Used exclusively for sale banners, limited-time offers, and clearance CTAs. Follows the same sizing and typography as `button-primary`.

**`button-pill-primary`** — A fully rounded pill variant at {rounded.full}, using {colors.primary} background and {colors.on-primary} text. Used for filter tags, category pills, and mobile navigation chips. Uses smaller typography ({typography.button-sm}) with 8px vertical padding.

**`button-pill-outline`** — An outlined pill variant with transparent background, {colors.ink} text, and a 1px {colors.hairline} border. Used for inactive filter tags and secondary chip actions.

### Cards
**`product-card`** — A white card with {rounded.md} corners containing a product image (4:5 aspect ratio), title, price, and optional badges. The card has no internal padding — the image fills the top, and text sits below with {spacing.sm} padding. On hover, the card lifts with a subtle box-shadow. Price uses {colors.body} at 14px; sale price uses {colors.accent-coral} at 600 weight.

**`product-card-badge`** — A small {rounded.xs} badge pinned to the top-left of product images. Sale badges use {colors.badge-sale} (#d02e2e) background with white text. New-arrival badges use {colors.badge-new-bg} (#ecfef0) background with {colors.badge-new} (#56ad6a) text. All badges use uppercase 11px Poppins 600.

### Navigation
**`nav-bar`** — A 64px white bar with a 1px {colors.hairline-soft} bottom border. The logo sits left-aligned, with nav links in uppercase Poppins 500 at 14px. Active links use {colors.primary} text; inactive links use {colors.muted}. The right side contains a search icon, account icon, and cart icon with badge count.

**`nav-link-active`** — Active navigation link styled with {colors.primary} text color. No underline or background — the brand trusts color alone to indicate current section.

**`nav-link-inactive`** — Inactive navigation link using {colors.muted} (#7b7b7b) text. On hover, text shifts to {colors.ink}.

### Forms
**`text-input`** — A standard text input with {colors.canvas} background, {colors.body} text, and a 1px {colors.hairline} border. On focus, the border becomes 2px {colors.primary}. Error state uses 2px {colors.accent-coral}. All inputs use {rounded.sm} corners and 48px height.

**`select-input`** — A dropdown selector matching the text-input styling with a custom chevron icon in {colors.muted}. Used for product sorting, size selection, and country/region pickers.

**`search-bar`** — A full-height pill input at {rounded.full} with 48px height, used in the mobile header and search overlay. Contains a magnifying glass icon in {colors.muted} on the left side.

### Footer
**`footer`** — A dark section with {colors.ink} (#1b4515) background and white text. Contains four columns: "Shop", "About", "Support", and "Connect" with newsletter signup. Links use {colors.muted-soft} (#868686) and shift to white on hover. The footer includes social icons, payment method icons, and a copyright line.

**`badge-membership`** — A pill-shaped badge using {colors.accent-lavender} (#a89cc8) background, used to denote "JadeYoga Member" pricing and exclusive content. The lavender is the only non-green accent in the membership system.

### Other Components
**`star-rating`** — A 5-star display using {colors.star-rating} (#fbcd0a) gold for filled stars and {colors.hairline} for empty stars. Each star is 16px. Used on product cards and review sections.

**`quantity-selector`** — A compact input with minus/plus buttons flanking a numeric display. Uses {rounded.sm} corners and a 1px {colors.hairline} border. Buttons are 40px tall with {colors.ink} text.

**`accordion-header`** — A clickable row with {colors.ink} title text and a chevron icon that rotates on open. Has a 1px {colors.hairline-soft} bottom border. Used for product descriptions, shipping info, and FAQ sections.

**`accordion-content`** — The expandable content area below accordion headers, using {colors.body} text at 14px. Padded with {spacing.sm} top and {spacing.base} bottom.

**`tab-active`** — An active tab with {colors.primary} text and a 2px {colors.primary} bottom border. Used in product detail tabs (Description, Reviews, Shipping) and account navigation.

**`tab-inactive`** — An inactive tab with {colors.muted} text and transparent bottom border. On hover, text shifts to {colors.ink}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically at full width; search bar becomes a fixed bottom element; footer columns stack; hero section reduces padding to {spacing.lg}; buttons become full-width |
| Tablet | 744–1024px | Two-column product grid; nav links remain visible but condensed; footer shows two-column layout; hero uses {spacing.xl} padding; search bar appears in header as icon |
| Desktop | 1024–1440px | Three-column product grid; full nav with all links; footer shows four-column layout; hero uses {spacing.section} padding; search bar is a full pill in the header |
| Wide | > 1440px | Max-width container at 1440px centered; product grid can show four columns; hero image scales with container; all spacing scales proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px touch area (padding + height)
- Quantity selector buttons are 40px × 40px minimum
- Accordion headers have 48px touch height
- Product card images are tappable with no minimum size constraint (image fills card width)

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer columns collapse from four to two at tablet, then to single column on mobile
- Product detail tabs collapse to accordion-style sections on mobile
- Hero section reduces vertical padding by half on mobile
- Search bar collapses from full pill to icon-only on mobile, expanding to full-screen overlay on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; exact transition durations and box-shadow values were not extractable from the live site
- Error states for forms (validation messages, error icon placement) were not observed
- Dark mode is not supported and no dark-mode color tokens were found
- Sub-brand palettes (JadeYoga Pro, JadeYoga Harmony) may exist but were not detected
- The exact font stack order for Poppins vs Nunito Sans could not be confirmed from CSS extraction — both appear in font-family declarations
- Modal/dialog styling (overlay opacity, close button placement, animation) was not observed
- Loading states (spinners, skeleton screens) were not extractable
- The brand's illustration style and icon set were not analyzed
- Checkout flow styling (Shopify checkout override colors) was not captured
- The extracted color list includes several grays (#bbbbbb, #c3c3c3, #d3d3d3) that may be Shopify default widget colors rather than intentional brand tokens — these were omitted from the palette
