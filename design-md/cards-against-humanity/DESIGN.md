---
version: alpha
name: "Cards Against Humanity"
source_url: "https://www.cardsagainsthumanity.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deliberately ugly, confrontational card game brand that weaponizes a garish, high-saturation palette — #fe2f2f (a screaming stop-sign red), #7333f1 (a bruise-purple), #d7b73b (a sickly mustard), and #fffe5b (a retina-searing yellow) — against the polite, pastel conventions of tabletop gaming. The brand's visual system is an anti-design manifesto: system fonts (-apple-system, BlinkMacSystemFont, Helvetica) set in all-caps at modest weights, hard 0px corners everywhere, and a layout that feels like a mid-2000s GeoCities page that got hit by a truck. The primary red `{colors.primary}` appears on the main CTA button, the "BUY NOW" banner, and the site's header bar — always set in white all-caps Helvetica Neue at 14px. There is no rounded corner softer than `{rounded.xs}` (4px) anywhere; cards, buttons, and input fields all terminate in sharp 90-degree angles. The secondary purple `{colors.secondary}` appears on hover states, the "EXPANSIONS" section headers, and the "ABOUT" page link. The mustard `{colors.accent-mustard}` and yellow `{colors.accent-yellow}` are used for sale badges, price tags, and the "FREE SHIPPING" callout — colors that feel like they were chosen to be ugly on purpose. The site's canvas is `{colors.canvas}` (#ffffff), but the brand's true background is the off-white `{colors.surface-soft}` (#ede5ff) that appears on product cards and the "HOW TO PLAY" section — a lavender-tinged gray that suggests a dirty whiteboard. The overall effect is a brand that screams "we don't care about design" with the precision of a professional designer — every ugly choice is intentional, from the 16px body text set in system sans-serif to the 48px section spacing that creates a cluttered, dense feel. The brand's voice is nihilistic, profane, and self-deprecating; the design system mirrors that by rejecting every rule of "good" design.

colors:
  primary: "#fe2f2f"
  primary-active: "#ff6b6b"
  primary-disabled: "#fff1f1"
  secondary: "#7333f1"
  secondary-active: "#e2bbff"
  ink: "#1b5bff"
  body: "#000000"
  muted: "#7333f1"
  muted-soft: "#ede5ff"
  hairline: "#d7b73b"
  hairline-soft: "#fffd6d"
  canvas: "#ffffff"
  surface-soft: "#ede5ff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  accent-mustard: "#d7b73b"
  accent-yellow: "#fffe5b"
  accent-green: "#b1ffc5"
  accent-cyan: "#a0e9ff"
  accent-pink: "#ffa0f0"
  accent-lime: "#b4ff91"
  accent-orange: "#ff9559"
  accent-blue: "#1b5bff"
  accent-purple: "#7333f1"
  accent-red: "#fe2f2f"
  accent-magenta: "#ff6b6b"
  accent-violet: "#e2bbff"
  accent-cream: "#fff1f1"
  accent-gold: "#fffd6d"
  accent-mint: "#82ffa2"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -2px
    textTransform: uppercase
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    textTransform: uppercase
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
    textTransform: uppercase
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
    textTransform: uppercase
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.5px
  price-strikethrough:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-buy-now:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 56px
  button-buy-now-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
  button-add-to-cart:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-add-to-cart-hover:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  nav-link-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-subtitle:
    typography: "{typography.body-lg}"
    color: "{colors.on-primary}"
  hero-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 56px
  section-header:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.display-md}"
    padding: 24px 16px
  section-header-alt:
    backgroundColor: "{colors.accent-mustard}"
    textColor: "{colors.body}"
    typography: "{typography.display-md}"
    padding: 24px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  checkbox:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    height: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.none}"
    height: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
  footer-link-hover:
    typography: "{typography.link}"
    color: "{colors.accent-yellow}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-free-shipping:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-limited:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  price-display:
    typography: "{typography.price}"
    color: "{colors.ink}"
  price-strikethrough:
    typography: "{typography.price-strikethrough}"
    color: "{colors.muted}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    padding: 16px
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 8px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, rendered in `{colors.primary}` (#fe2f2f) with white all-caps text in `{typography.button-md}` (14px Helvetica Neue Bold). Has zero border-radius (`{rounded.none}`), creating a sharp, aggressive rectangle. On hover, shifts to `{colors.primary-active}` (#ff6b6b). Disabled state uses `{colors.primary-disabled}` (#fff1f1). Used for "BUY NOW", "ADD TO CART", and "SUBSCRIBE" actions.

**`button-secondary`** — Secondary action button in `{colors.secondary}` (#7333f1) with white text. Same zero-radius treatment as primary. Hover state shifts to `{colors.secondary-active}` (#e2bbff). Used for "LEARN MORE", "VIEW EXPANSIONS", and "SEE ALL" links.

**`button-outline`** — Outlined button with a transparent background and `{colors.ink}` (#1b5bff) text. Maintains the same zero-radius and all-caps typography. Used for secondary actions like "CANCEL" or "BACK".

**`button-buy-now`** — The hero purchase button, larger than standard at 56px height with `{typography.button-lg}` (18px). Uses `{colors.primary}` background. This is the most prominent button on the site, appearing in the hero section and on product detail pages.

### Navigation
**`top-nav`** — A 60px-high sticky header bar in `{colors.primary}` (#fe2f2f). Contains the brand logo (typically "CARDS AGAINST HUMANITY" in white all-caps) and navigation links in `{typography.nav-link}` (14px bold all-caps). Links are white on red, with hover state shifting to `{colors.primary-active}`. No border-radius, no shadows, no underlines.

**`nav-link`** — Navigation link styled in white all-caps Helvetica Neue Bold at 14px. No underline, no decoration. On hover, background shifts to `{colors.primary-active}`. Active state is indicated by a subtle underline or heavier weight.

### Cards
**`product-card`** — A zero-radius white card (`{colors.surface-card}`) with 16px padding. Contains a product image (also zero-radius), a title in `{typography.title-sm}` (16px bold all-caps), and a price in `{typography.price}` (22px heavy). Badges (sale, new, limited) appear as small zero-radius rectangles in the top-left corner. Cards stack in a grid with 16px gaps.

**`product-card-badge`** — Small zero-radius badge in `{colors.accent-yellow}` (#fffe5b) with black text. Used for "FREE SHIPPING" or "BEST SELLER" labels. Sale badges use `{colors.primary}` (#fe2f2f) with white text. New badges use `{colors.accent-green}` (#b1ffc5) with black text.

### Forms
**`text-input`** — A zero-radius input field with white background, 44px height, and 16px padding. Text is set in `{typography.body-md}` (16px Helvetica Neue). On focus, the border shifts to `{colors.primary}`. Error state uses `{colors.primary}` text color. No rounded corners, no shadows.

**`select`** — Same styling as text-input, used for dropdown menus. Zero-radius, white background, 44px height.

**`checkbox`** — A 20px square checkbox with zero border-radius. Checked state fills with `{colors.primary}` (#fe2f2f). No rounded corners.

### Hero
**`hero`** — Full-width hero section with `{colors.primary}` (#fe2f2f) background and white text. Contains a headline in `{typography.display-xl}` (48px heavy all-caps), a subtitle in `{typography.body-lg}` (18px), and a CTA button (`{colors.on-primary}` background, `{colors.primary}` text). Padding is 64px top/bottom, 24px left/right.

### Section Headers
**`section-header`** — Full-width section header in `{colors.secondary}` (#7333f1) with white text. Uses `{typography.display-md}` (28px bold all-caps). Padding is 24px top/bottom, 16px left/right. An alternate version uses `{colors.accent-mustard}` (#d7b73b) background with black text.

### Footer
**`footer`** — Full-width footer in `{colors.ink}` (#1b5bff) with white text. Links are white, shifting to `{colors.accent-yellow}` (#fffe5b) on hover. Uses `{typography.body-sm}` (14px) for body text and `{typography.link}` (14px bold all-caps) for links. Padding is 48px top/bottom, 24px left/right.

### Badges
**`badge-sale`** — Red badge (`{colors.primary}`) with white text. Zero-radius. Used for sale items.
**`badge-new`** — Green badge (`{colors.accent-green}`) with black text. Used for new products.
**`badge-free-shipping`** — Yellow badge (`{colors.accent-yellow}`) with black text. Used for free shipping promotions.
**`badge-limited`** — Orange badge (`{colors.accent-orange}`) with black text. Used for limited editions.

### Accordion
**`accordion-header`** — Section header in `{colors.surface-soft}` (#ede5ff) with black text. Uses `{typography.title-sm}` (16px bold all-caps). Zero-radius. Content area is white with `{typography.body-md}` (16px).

### Dividers
**`divider`** — A 1px line in `{colors.hairline}` (#d7b73b). Used between sections.
**`divider-soft`** — A 1px line in `{colors.hairline-soft}` (#fffd6d). Used within cards or content areas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards; hero text reduces to `{typography.display-md}` (28px); navigation collapses to hamburger menu; section headers stack vertically; buttons become full-width |
| Tablet | 744–1128px | Two-column grid for product cards; hero maintains `{typography.display-lg}` (36px); navigation remains horizontal but links may wrap; section headers maintain full-width layout |
| Desktop | 1128–1440px | Three-column grid for product cards; hero uses `{typography.display-xl}` (48px); full navigation visible; standard layout |
| Wide | > 1440px | Four-column grid for product cards; hero text scales up slightly; max-width container at 1440px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch targets
- Navigation links have minimum 44px tap area (padding extends clickable zone)
- Product card images are tappable with minimum 120px height
- Checkbox and radio inputs are 20px minimum, with 44px tap area via padding
- Accordion headers have 44px minimum tap height

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product card grid collapses from 4 columns to 1 column on mobile
- Hero section reduces font size and may stack CTA below text on mobile
- Section headers reduce padding on mobile (from 24px to 16px)
- Footer links stack vertically on mobile
- Accordion behavior is maintained across all breakpoints
- Badges may reduce in size on mobile (from 10px to 8px font)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary/secondary button hovers extracted)
- Active/focus states for text inputs, selects, and checkboxes
- Error states for form validation (text color only extracted)
- Disabled states for secondary, outline, and ghost buttons
- Dark mode or high-contrast mode variants
- Sub-brand or expansion-specific color palettes (e.g., "The Box", "The Voting Game")
- Animation and transition specifications (duration, easing)
- Shadow and elevation tokens (none detected on live site)
- Icon system details (social media icons, cart icon, hamburger menu)
- Typography scale for mobile (font sizes may scale down)
- Specific font weights for system fonts (Helvetica Neue weights may vary by OS)
- Meta theme-color for browser chrome (none detected)
- Shopify-specific checkout widget colors (may include Klarna, Afterpay, etc.)
- Stock image dominant tones that may have been filtered from extracted colors
- The brand's true primary may be #fe2f2f (red) based on frequency, but the extracted list includes many high-saturation colors that could be used in different contexts
