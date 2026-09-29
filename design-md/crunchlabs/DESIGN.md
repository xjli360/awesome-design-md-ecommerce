---
version: alpha
name: "CrunchLabs"
source_url: "https://www.crunchlabs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bright, high-contrast engineering playground where #e52718 (a hot, slightly orange red) and #fed103 (a sharp marigold yellow) act as the primary voltage pair — a design choice that reads more like a construction-site warning than a toy brand, which is exactly the point. The brand’s deep navy #00416c provides a serious, technical counterweight, while #3c392c (a warm, almost leathery brown) and #f4f4f6 (a cool off-white) form the neutral backbone. Typography is a deliberate collision: the display head uses Audiowide, a geometric, almost digital-clock sans-serif that screams “circuit board,” while body copy runs Gotham Rounded — a friendly, approachable humanist sans that keeps the brand from feeling cold. The result is a system that feels like a well-organized workshop: bright yellow tape lines, red danger buttons, and navy blue toolboxes. Buttons are pill-shaped ({rounded.full}), product cards use soft corners ({rounded.md}), and the overall mood is one of enthusiastic, hands-on problem-solving — not sterile tech, but the joyful chaos of a garage full of prototypes. The extracted palette includes a surprising number of blues and grays, but the red and yellow are the unmistakable brand signatures, appearing consistently across CTAs, badges, and the logo lockup.

colors:
  primary: "#e52718"
  primary-active: "#c42211"
  primary-disabled: "#f6bbb6"
  ink: "#221f20"
  body: "#3c392c"
  muted: "#757575"
  muted-soft: "#9a9db1"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#faf8f4"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fed103"
  accent-navy: "#00416c"
  accent-blue: "#006ead"
  accent-blue-light: "#a6cce2"
  accent-brown: "#3c392c"
  badge-red: "#e52718"
  badge-yellow: "#fed103"
  star-rating: "#fed103"
  success: "#198754"
  scrim: "#282828"

typography:
  display-xl:
    fontFamily: "'Audiowide', 'Gotham Rounded', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Audiowide', 'Gotham Rounded', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Audiowide', 'Gotham Rounded', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-lg:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Gotham Rounded', 'GothamHTF', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  display-code:
    fontFamily: "'Martian Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-accent-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
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
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-content:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-subscription:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
    height: 60px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.accent-blue-light}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 40px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s signature red (#e52718) with white text. Uses a pill shape ({rounded.full}) and bold Gotham Rounded at 16px/700 weight. On hover, the background shifts to a deeper red (#c42211). The disabled state uses a soft pink (#f6bbb6) to indicate inactivity while maintaining brand color family.

**`button-secondary`** — An outlined variant with a dark ink (#221f20) border on a white (#faf8f4) canvas. The hover state inverts the colors, filling the button with ink and switching text to the warm off-white canvas. Used for less prominent actions like “Learn More” or “View Details.”

**`button-accent-yellow`** — The high-energy alternative, using the brand’s marigold yellow (#fed103) with dark ink text. This appears on dark navy hero sections and promotional banners where the red would feel too aggressive. The yellow provides maximum contrast against the deep blue backgrounds.

**`button-accent-navy`** — A dark blue variant (#00416c) with white text, used in contexts where the red or yellow would compete with surrounding elements. Often appears in the footer or on light gray surfaces.

### Cards
**`product-card`** — A white card with soft 12px corners ({rounded.md}) containing a full-width image and a content area below. The image uses rounded top corners only, creating a clear visual break. The title uses the bold 18px title style, while the price sits below in the standard 16px body weight. Cards are used for subscription boxes, individual kits, and merchandise.

**`product-card-image`** — The image container within a product card. Top corners are rounded to match the card, while bottom corners are square, allowing the image to sit flush against the content area below.

### Badges
**`badge-new`** — A small, pill-shaped badge in the brand’s yellow (#fed103) with dark ink text. Used to flag new product launches or recently added kits. The uppercase 11px bold type ensures readability at small sizes.

**`badge-sale`** — A red (#e52718) badge with white text, used for promotional pricing or limited-time offers. Matches the primary button color for visual consistency across sale touchpoints.

**`badge-subscription`** — A navy (#00416c) badge with white text, used to denote subscription-exclusive items or bundle deals. The dark blue provides a more premium, “members-only” feel compared to the urgency-driven red badge.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on the warm white canvas (#faf8f4). Navigation links use Gotham Rounded Bold at 16px with 0.3px letter spacing. Active links shift to the brand red, while inactive links sit in a muted gray (#757575). The logo typically appears on the left, with the cart icon and account link on the right.

**`nav-link-active`** — The active state for top-level navigation items. The text color changes to the brand red (#e52718) with no background change, creating a subtle underline effect without a physical line.

### Hero
**`hero-section`** — A full-width section using the deep navy (#00416c) as background, with white text. The headline uses Audiowide at 48px for maximum impact. The hero typically features a large product image or lifestyle photo overlaid with the yellow CTA button.

**`hero-cta`** — The hero’s primary action button, using the yellow (#fed103) on navy background for maximum contrast. At 60px tall with 18px bold type, it’s larger than standard buttons to anchor the hero composition.

### Forms
**`text-input`** — A standard input field with a 1px hairline border (#dedede) on the warm white canvas. On focus, the border thickens to 2px and shifts to the brand red (#e52718), providing clear visual feedback. The 48px height and 16px padding create comfortable touch targets.

**`search-bar`** — A pill-shaped search input with a full 9999px border radius, matching the button shapes for consistency. The 1px hairline border keeps it subtle, while the rounded form feels approachable and toy-like.

### Footer
**`footer-section`** — A dark section using the ink color (#221f20) as background, with white body text. Links use the light blue (#a6cce2) for legibility against the dark background. The footer typically contains navigation links, social icons, and legal text.

**`footer-link`** — Footer links in the light blue (#a6cce2) at 16px weight 500. The lighter blue provides sufficient contrast against the dark footer background without the harshness of pure white links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 28px; buttons become full-width; search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid; nav shows 3-4 links; hero uses 36px display; buttons remain inline but smaller padding |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at 48px; standard button sizes |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero may include additional content panels |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets are the entire card surface, not just text links
- Nav links have 48px minimum tap area even on desktop
- Quantity selectors and cart controls use 40px minimum touch targets

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid reduces columns progressively: 4 → 3 → 2 → 1
- Hero section reduces headline size and may hide secondary text below 744px
- Footer links stack vertically on mobile, with accordion-style section headers
- Search bar transforms from inline to a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors include several Shopify checkout-widget colors (#4285f4, #198754) and social-icon tones that are not part of the brand palette — these have been excluded from the primary palette
- The font list includes several decorative/display fonts (Bosque, Creative, CycloneLayers, SourGummy) that appear in marketing imagery but are not part of the core system — only Audiowide, Gotham Rounded, GothamHTF, and Martian Mono are confirmed as system fonts
- Hover and focus states for secondary components (badges, cards, footer links) could not be reliably extracted
- Error states for form inputs (red border, error message styling) are inferred from the primary red but not confirmed
- Dark mode is not supported on the live site; no dark palette exists
- Sub-brand or seasonal color variations (e.g., holiday themes, limited-edition kits) are not captured
- The exact border-radius values for cards and buttons are estimated from visual inspection; the live site may use slightly different values
- Typography line-height and letter-spacing values are estimated from common web patterns and may differ from the brand’s actual CSS
- The “Gotham Rounded” font may be a licensed font that requires separate purchase; fallback to system fonts is recommended for development
- Animation and transition timing values (ease-in-out durations, hover transitions) are not included
