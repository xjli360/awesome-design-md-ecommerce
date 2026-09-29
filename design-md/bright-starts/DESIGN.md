---
version: alpha
name: "Bright Starts"
source_url: "https://www.brightstarts.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A navy-and-crimson world for the earliest years, where #0f193f (a deep, almost ink-blue) anchors the entire experience — from the meta theme-color to the primary navigation and footer — while #ec2c3e (a sharp, primary red) provides the voltage for CTAs, sale badges, and playful accent elements. The palette reads like a classic children’s board book: #f2f2f2 and #f7f7f7 create a soft, warm canvas, while #314439 and #3c5345 introduce earthy greens that echo the brand’s natural, developmental focus. Bright Starts uses generous whitespace and {rounded.sm} corners to keep the interface approachable for new parents navigating sleep-deprived shopping sessions. Product photography is the hero — toys, bouncers, and activity centers float on clean white or light gray backgrounds, with the occasional splash of #ffdf00 (a warm marigold) or #76dca1 (a minty green) in badges and promotional banners. The typography runs Karla and Lato, both humanist sans-serifs that feel friendly without being cartoonish. Buttons are pill-shaped ({rounded.full}) for the primary call-to-action, while secondary actions use {rounded.sm} to differentiate hierarchy. The overall mood is one of gentle confidence: the navy says “trust us,” the red says “this is fun,” and the greens whisper “we understand development.” There are no hard edges in the UI — even the search bar and input fields carry a soft radius — and the checkout flow inherits the same navy-and-crimson DNA, ensuring a cohesive experience from browse to buy.

colors:
  primary: "#ec2c3e"
  primary-active: "#e91529"
  primary-disabled: "#f7b0b8"
  ink: "#0d0d0d"
  body: "#212121"
  muted: "#607380"
  muted-soft: "#d1d1db"
  hairline: "#d9d9d9"
  hairline-soft: "#f1f1f1"
  canvas: "#f2f2f2"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#0f193f"
  navy-light: "#142154"
  green-deep: "#314439"
  green-mid: "#3c5345"
  green-bright: "#76dca1"
  green-soft: "#62d793"
  yellow: "#ffdf00"
  yellow-warm: "#fdb515"
  gold: "#f0d200"
  beige: "#f7f6f0"
  beige-warm: "#f5f2ec"
  sage: "#d4cead"
  purple: "#4c4b63"
  blue-bright: "#153bd2"

typography:
  display-xl:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 24px
    height: 48px
    border: "2px solid {colors.navy}"
  button-secondary-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
  button-pill-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-green:
    backgroundColor: "{colors.green-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.navy}"
  text-input-error:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 52px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.green-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
  category-tile-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "{spacing.sm} {spacing.lg} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature red (#ec2c3e) with white text and a pill shape ({rounded.full}). On hover, it deepens to #e91529. The disabled state uses a lighter pink (#f7b0b8) to indicate inactivity. Used for “Add to Cart,” “Shop Now,” and primary checkout actions.

**`button-secondary`** — A white button with a 2px navy (#0f193f) border and navy text. On hover, the background fills with navy and text flips to white. Used for secondary actions like “View Details” or “Learn More.” The rounded corners are softer ({rounded.sm}) than the primary pill, creating visual hierarchy.

**`button-tertiary`** — A text-only button with no background or border, using navy text. On hover, a subtle underline appears. Used for less prominent actions like “Cancel” or “See All.”

**`button-pill-navy`** — A navy pill button used for promotional banners and age-group filters. The dark background makes white text pop, and the full radius matches the primary button’s friendliness.

**`button-pill-green`** — A bright green (#76dca1) pill button used for “New Arrivals” or “Eco-Friendly” badges and CTAs. The green signals freshness and sustainability, contrasting with the navy-and-red system.

### Cards
**`product-card`** — The standard product display card, white with a soft shadow and {rounded.sm} corners. The product image sits at the top with rounded top corners, while the title, price, and rating live below. Badges (sale, new, bestseller) overlay the image at the top-left.

**`product-card-badge`** — A small, uppercase label in the brand red with white text, used for “Sale” or “Limited Edition.” The badge is compact ({rounded.xs}) and sits directly on the product image.

**`product-card-badge-sale`** — A yellow (#ffdf00) badge with dark text, used specifically for percentage-off promotions. The warm yellow creates urgency without the aggression of red.

**`product-card-badge-new`** — A mint green (#76dca1) badge for new arrivals. The green feels fresh and developmental, aligning with the brand’s focus on early milestones.

**`category-tile`** — A large, clickable tile linking to a product category (e.g., “Bouncers,” “Play Gyms”). It uses a light gray background (#f7f7f7) with a centered icon and title. On hover, the background shifts to navy and text becomes white.

### Navigation
**`nav-bar`** — The top navigation bar, a full-width navy (#0f193f) strip with white uppercase links. The brand logo sits left-aligned, with category links centered and a search icon on the right. On scroll, the bar collapses to a white background with dark text for readability against page content.

**`footer`** — A navy footer with white text, divided into columns for “Shop,” “Support,” “About,” and “Social.” Links are body-sm weight with generous vertical spacing. The footer includes a newsletter signup field styled as a white input with a red submit button.

### Forms
**`text-input`** — A standard text input with a white background, 1px hairline border, and {rounded.sm} corners. On focus, the border thickens to 2px navy. On error, the border turns red (#ec2c3e). Used for search, newsletter signup, and checkout fields.

**`search-bar`** — A pill-shaped search bar with a white background and 1px hairline border. The full radius ({rounded.full}) makes it feel approachable. Placeholder text reads “Search products…” and a magnifying glass icon sits on the left.

### Accordion
**`accordion`** — Used for product descriptions, FAQs, and shipping details. Each accordion has a white background, 1px hairline border, and {rounded.sm} corners. The header is clickable with a chevron icon that rotates on open. Content padding is generous (12px left/right, 16px bottom) for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text shrinks to display-md; search bar moves to full-width below nav; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav shows 4-5 category links; hero banner uses display-lg; search bar is 60% width; footer columns in 2x2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; hero uses display-xl; search bar is 40% width; footer in 4 columns |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can show 4 columns; hero image scales up; whitespace increases |

### Touch Targets
- All buttons and links: minimum 44px height for tap targets
- Product card CTAs: 48px height
- Nav links: 44px tap area (even if text is smaller)
- Accordion headers: 48px tap area
- Search bar: 52px height for easy tapping
- Category tiles: minimum 80px height

### Collapsing Strategy
- Top nav: On mobile, full nav collapses to a hamburger menu; the logo and cart icon remain visible
- Product filters: On tablet and below, filters collapse into a “Filter” button that opens a slide-out panel
- Footer: On mobile, footer columns collapse into an accordion-style list
- Product image gallery: On mobile, thumbnails become a horizontal scroll strip below the main image
- Accordion content: On mobile, all accordions start collapsed to save vertical space

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be reliably extracted from the live site; the active states listed above are inferred from common patterns in the brand’s palette
- Error styling for forms (validation messages, error icons) is not documented; the text-input error border is assumed from the primary red
- Dark mode is not present on the live site; no dark-mode tokens are defined
- The exact font stack order between Karla and Lato is unclear; the extracted CSS shows both declared with `!important` on Arial, suggesting a fallback chain that may vary by page
- Sub-brand or seasonal palette variations (e.g., holiday, gender-neutral) are not captured
- The meta theme-color (#0f193f) is used as the nav and footer background, but its exact role in the browser chrome is unverified
- Checkout-specific components (payment forms, shipping selectors) are not documented; they may inherit Shopify default styling
- Animation durations and easing curves are not extracted; all transitions are assumed to be 200ms ease-in-out
- The extracted color list includes several low-frequency tones (#121127, #000001, #e6c900) that may be stock-image artifacts or unused CSS; they are omitted from the palette
