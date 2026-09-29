---
version: alpha
name: "Jones Snowboards"
source_url: "https://www.jonessnowboards.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A mountain-crafted brand that runs on a deep charcoal ink (#2b2b2b) and a singular teal voltage (#108474) — the exact green of alpine lake water at altitude, used for every primary CTA, the "Shop Now" button, the cart badge, and the active-state underline on navigation links. The canvas is a near-white (#fbfbfb) that reads as snow-light rather than sterile white, while secondary surfaces shift to a warm off-white (#f9fafb) and a faint silver (#eeeeee) for product-card backgrounds. The brand's typography is set in Lato, a geometric sans-serif with humanist warmth, running at moderate weights (400–700) and never exceeding 28px for display — the product photography and snowscapes do the heavy lifting. The site uses a persistent top nav with a centered logo, a full-width hero that bleeds into the viewport, and product cards with a subtle shadow and a 4px rounded corner. The checkout flow introduces a secondary orange accent (#f48120) for "Add to Cart" in certain contexts, and a muted gray (#7b7b7b) for secondary text and disabled states. The overall feel is utilitarian but intentional — every corner is either sharp (0px) or barely softened (4px), never pill-shaped, reflecting the brand's no-nonsense backcountry ethos.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5cc"
  ink: "#2b2b2b"
  body: "#4a4a4a"
  muted: "#7b7b7b"
  muted-soft: "#949494"
  hairline: "#c2c2c2"
  hairline-soft: "#dedede"
  canvas: "#fbfbfb"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-secondary: "#eeeeee"
  on-primary: "#ffffff"
  accent-orange: "#f48120"
  accent-orange-active: "#d96a0e"
  star-rating: "#fbcd0a"
  error: "#eb001b"
  success: "#108474"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 1px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.sm} 0 {spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
    minHeight: "400px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand teal (#108474) and set in uppercase Lato 700 at 14px. Used for "Shop Now", "Add to Cart" (on product pages), and "Subscribe". On hover, shifts to a darker teal (#0d6b5d). Disabled state uses a muted teal (#a3d5cc) with white text. No border radius — sharp corners reinforce the utilitarian mountain aesthetic.

**`button-secondary`** — An outlined variant with a 2px solid ink (#2b2b2b) border on a white background. Used for "Learn More", "View Details", and secondary checkout actions. On hover, the fill and text swap — the button becomes solid ink with white text.

**`button-accent-orange`** — A warm orange (#f48120) variant used specifically for "Add to Cart" in collection pages and promotional banners. On hover, darkens to #d96a0e. This orange is a secondary brand accent that appears in limited, high-conversion contexts.

**`button-text`** — A text-only link styled as a button, using the teal primary color. Used for "Read More" on blog cards and "View All" in category strips. No padding, no border — just the link text with a hover underline.

### Cards
**`product-card`** — A clean, borderless card with a white background and no rounded corners. The product image fills the top at a 1:1 aspect ratio. The title uses 14px Lato 600, the price uses 14px Lato 400 in body gray (#4a4a4a). A small teal badge can appear in the top-left corner for "New" or "Sale" indicators. Cards sit on a faint silver (#eeeeee) surface background when in a grid.

**`product-card-badge`** — A small, sharp-cornered teal label with uppercase 11px Lato 700. Used for "NEW", "SALE", "BEST SELLER". Positioned absolutely over the product image at top-left.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, white background with a soft hairline bottom border (#dedede). The brand logo is centered. Navigation links are uppercase 13px Lato 700 with 1px letter-spacing. The active page link gets a 2px teal bottom border. The cart icon sits on the right with a teal circular badge showing item count.

**`nav-link-active`** — The currently active navigation link, distinguished by a 2px solid teal underline and teal text color. All other links remain ink (#2b2b2b).

### Forms
**`text-input`** — A standard input field with a 1px hairline border (#c2c2c2), no border radius, 44px height, and 16px Lato 400 text. On focus, the border switches to teal (#108474). Error state uses a red border (#eb001b). Used for email signup, search, and checkout forms.

**`search-bar`** — A compact 40px input with a 1px hairline border, used in the mobile menu and collection page filters. On focus, the border turns teal.

### Footer
**`footer`** — A full-width dark footer with ink (#2b2b2b) background and muted gray (#949494) text. Links are 14px Lato 400 and turn white on hover. The footer contains brand info, navigation links, social icons, and legal text. Padding is 48px top/bottom with 16px sides.

### Accordion
**`accordion-header`** — Used on product detail pages for "Description", "Specifications", and "Shipping" sections. A soft gray (#f9fafb) background with a 14px Lato 600 title and a bottom hairline border. On click, the content panel slides open.

**`accordion-content`** — The expanded panel below the header, white background with 16px padding and 14px Lato 400 body text.

### Hero
**`hero-section`** — A full-width section with a dark ink background and white text, typically featuring a large background image. The headline uses 28px Lato 700. A single teal CTA button sits below the headline. Minimum height is 400px, with 64px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in 2 columns; hero text reduces to 20px; footer links stack vertically; search bar moves to mobile menu drawer |
| Tablet | 744–1128px | Nav links remain visible but reduced font size (12px); product cards in 3 columns; hero maintains full-width image with centered text; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 4 columns; hero has larger typography (28px); footer uses 4-column layout with newsletter signup |
| Wide | > 1440px | Max-width container at 1440px; content centered; product cards in 4 columns with increased padding; hero may feature split layout with text and image side by side |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Mobile nav hamburger icon is 48px x 48px
- Product card tap targets (title, price, image) are at least 44px tall
- Accordion headers are 44px+ tall for easy tapping
- Cart icon badge is 18px but the icon container is 44px x 44px

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px)
- Product grid collapses from 4 columns (desktop) to 3 (tablet) to 2 (mobile)
- Footer collapses from 4 columns (desktop) to 2 (tablet) to single column (mobile)
- Hero text and CTA stack vertically on mobile; image may become full-width background
- Search bar moves from inline (desktop) to a slide-out drawer (mobile)
- Accordion sections remain collapsed by default on all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, image zoom) could not be reliably extracted from the live site
- Error styling for form validation (beyond red border) is not confirmed — error messages, iconography, and animation timing are unknown
- Sub-brand or collection-specific color palettes (e.g., "Mountain", "Splitboard", "Outerwear" lines) may exist but were not detected
- Dark mode is not implemented on the live site; no dark theme tokens exist
- The exact font weight for Lato in headings (700 vs 900) could not be verified — 700 is assumed based on common usage
- Button hover animation (e.g., background color transition duration) is not specified
- The star-rating color (#fbcd0a) was extracted but its exact usage context (reviews, product ratings) is inferred
- Social media icon colors (e.g., #334fb4, #142688) were extracted but are likely from embedded platform icons, not brand design tokens
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) were filtered but may appear in the extracted list — these are not brand colors
- The extracted font list includes "JudgemeStar" which is a review widget icon font, not a brand typeface
- Spacing values for specific components (e.g., product card padding, hero section margins) are inferred from common e-commerce patterns and may differ from the actual site
