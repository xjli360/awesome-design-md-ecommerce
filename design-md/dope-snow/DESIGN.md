---
version: alpha
name: "Dope Snow"
source_url: "https://www.dopesnow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A raw, high-contrast winter-sports brand that uses #121212 as its primary ink and #e9e9e8 as its canvas — a reversal of the typical white-background retail site, creating a nocturnal, neon-lit slope atmosphere. The brand's signature voltage comes from a triad of reds (#ad1519, #de0000, #cf2734) and a sharp yellow (#fabd00) that together read as warning beacons, speed markers, and après-ski glow. Manrope runs at medium weights with tight letter-spacing, giving headlines a compressed, athletic density that matches the brand's snowboard-and-hoodie silhouette. Buttons are pill-shaped ({rounded.full}), often rendered in full-bleed red or outlined in white against the dark canvas, while product cards float on #f0f2f3 surfaces with soft {rounded.md} corners — the only concession to softness in an otherwise angular, aggressive system. The nav bar sits at 64px with a sticky dark backdrop, and the search bar is a rounded pill with a subtle #d0cecb border. Badges use the yellow (#fabd00) for sale markers and red (#ad1519) for "new" flags, both set in condensed uppercase Manrope. The overall effect is a mountain-town billboard translated into a direct-to-consumer storefront — loud, fast, and unapologetically street.

colors:
  primary: "#ad1519"
  primary-active: "#de0000"
  primary-disabled: "#d0cecb"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6e7075"
  muted-soft: "#d0cecb"
  hairline: "#e0e0e0"
  hairline-soft: "#e9e9e8"
  canvas: "#e9e9e8"
  surface-soft: "#f0f2f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fabd00"
  accent-yellow-active: "#fddb21"
  accent-red-bright: "#de0000"
  accent-red-dark: "#ad1519"
  accent-red-mid: "#cf2734"
  accent-blue: "#3172da"
  accent-green: "#25d366"
  accent-dark-surface: "#191919"
  accent-navy: "#192f8e"
  accent-deep-navy: "#0f2e6b"
  accent-burgundy: "#bc002d"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.75px
  display-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Manrope', 'Manrope Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-secondary-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-outline-dark:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-circle-dark:
    backgroundColor: "{colors.accent-dark-surface}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-yellow}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-pill-dark:
    backgroundColor: "{colors.accent-dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-photo:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-dark:
    backgroundColor: "{colors.accent-dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  checkbox:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  radio:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  toggle-switch:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
  rating-stars:
    color: "{colors.accent-yellow}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  snackbar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  snackbar-error:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  snackbar-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in full-bleed #ad1519 with white Manrope 600 at 16px. Pill-shaped ({rounded.full}) with 14px/28px padding and a fixed 48px height. On hover, shifts to #de0000 for a brighter, more urgent red. Disabled state drops to #d0cecb with #6e7075 text, signaling the action is unavailable. Used for "Add to Cart", "Checkout", and "Shop Now" CTAs across the site.

**`button-secondary`** — A light variant on the dark canvas, using #e9e9e8 background with #121212 text. Same pill shape, 48px height, and Manrope 600 at 16px. Hover state darkens the background slightly. Used for "View Details", "Learn More", and secondary actions in hero sections.

**`button-secondary-dark`** — The inverse of secondary, using #121212 background with white text. Used on light backgrounds or as a contrasting CTA in product cards. Same dimensions and typography as button-secondary.

**`button-outline`** — A transparent background with #121212 text and a 1px solid #121212 border. Pill-shaped, 48px height. Hover fills with #121212 and inverts text to white. Used for tertiary actions like "Save for Later" or "Compare".

**`button-outline-dark`** — Transparent background with white text and a 1px solid white border. Used on dark backgrounds or hero overlays. Hover fills with white and inverts text to #121212.

**`button-pill-accent`** — A smaller, high-visibility pill using #fabd00 background with #121212 text. Manrope 600 at 14px, 10px/20px padding. Used for "Sale", "Limited Edition", or promotional badges that are clickable.

### Navigation
**`top-nav`** — A 64px sticky nav bar with #121212 background and white uppercase Manrope 700 at 14px. Logo sits left-aligned, nav links center or right, with a search icon and cart icon on the right edge. Active link uses #fabd00 text color. The nav bar is fixed to the top and remains visible on scroll.

**`nav-link-active`** — The active state for top-nav links, using #fabd00 text color. Indicates the current page or section.

**`nav-link-inactive`** — The default state for top-nav links, using white text. Hover state may add a subtle underline or shift to #d0cecb.

**`category-strip`** — A horizontal scrollable strip of category tabs, using #e9e9e8 background. Each tab is a pill-shaped button with Manrope 600 at 14px. Active tab uses #121212 background with white text; inactive tabs use #f0f2f3 background with #3a3a3a text.

**`category-tab-active`** — The active category tab, a pill with #121212 background and white text. Used to filter products by category (e.g., "Men's", "Women's", "Accessories").

**`category-tab-inactive`** — The inactive category tab, a pill with #f0f2f3 background and #3a3a3a text. Hover state may shift to #e0e0e0 background.

### Cards
**`product-card`** — A white (#ffffff) card with {rounded.md} corners, containing a product image, title, price, and optional badge. Typography uses Manrope 400 at 14px for details, with the title in Manrope 600 at 16px. The card floats on the #e9e9e8 canvas with a subtle shadow or border (#e0e0e0). Hover state may lift the card with a stronger shadow.

**`product-card-photo`** — The image container within a product card, using {rounded.md} to match the card corners. Images are typically 1:1 or 3:4 aspect ratio, with object-fit: cover.

**`product-card-badge`** — A small badge overlaid on the product card, using #fabd00 background with #121212 text. Manrope 700 at 11px, uppercase, with {rounded.sm} corners and 4px/8px padding. Used for "Sale", "New", or "Best Seller" labels.

**`product-card-badge-new`** — A variant using #ad1519 background with white text. Used specifically for "New" arrivals.

**`product-card-badge-sale`** — A variant using #de0000 background with white text. Used specifically for sale or discount items.

### Forms
**`text-input`** — A standard text input with white background, #121212 text, Manrope 400 at 16px, {rounded.sm} corners, and 12px/16px padding. Height is 48px. Border is #e0e0e0, shifting to #ad1519 on focus. Used for search, email, name, and address fields.

**`text-input-dark`** — A dark variant using #191919 background with white text. Used on dark backgrounds or in the footer. Same dimensions and typography.

**`select-dropdown`** — A dropdown select with white background, #121212 text, Manrope 400 at 14px, {rounded.sm} corners, and 10px/16px padding. Height is 44px. Used for size, quantity, and filter selections.

**`checkbox`** — A small square checkbox with {rounded.xs} corners. Default state is white background with #e0e0e0 border. Checked state uses #ad1519 background with white checkmark.

**`radio`** — A circular radio button with {rounded.full}. Default state is white background with #e0e0e0 border. Selected state uses #ad1519 fill.

**`toggle-switch`** — A pill-shaped toggle with #d0cecb background. Active state shifts to #ad1519. The knob is white and circular.

**`quantity-selector`** — A compact control with #f0f2f3 background, Manrope 400 at 16px, {rounded.sm} corners, and 8px/12px padding. Height is 40px. Contains minus, value, and plus buttons.

**`size-selector`** — A pill-shaped size button with white background, #121212 text, Manrope 400 at 14px, {rounded.sm} corners, and 8px/12px padding. Height is 40px. Active state uses #121212 background with white text.

### Hero & Footer
**`hero-banner`** — A full-width hero section with #121212 background and white text. Uses display-xl typography (Manrope 700 at 42px). Often includes a background image or video with overlay. CTA buttons use button-primary or button-outline-dark.

**`hero-banner-accent`** — A variant using #ad1519 background with white text. Uses display-lg typography (Manrope 700 at 34px). Used for promotional or seasonal hero sections.

**`footer`** — A full-width footer with #121212 background and #d0cecb text. Manrope 400 at 14px. Contains columns for links, social icons, newsletter signup, and legal text. Links use #d0cecb color, hovering to white.

**`footer-link`** — Footer links using #d0cecb text and Manrope 500 at 14px. Hover state shifts to white.

**`footer-heading`** — Footer column headings using white text and Manrope 600 at 16px.

### Feedback & Overlays
**`tooltip`** — A small tooltip with #121212 background, white text, Manrope 500 at 13px, {rounded.sm} corners, and 6px/12px padding.

**`modal-overlay`** — A semi-transparent black overlay (#000000 at 50% opacity) behind modal dialogs.

**`modal-content`** — A white modal dialog with {rounded.md} corners and 24px padding. Contains title, body text, and action buttons.

**`snackbar`** — A notification bar with #121212 background, white text, Manrope 400 at 14px, {rounded.sm} corners, and 12px/16px padding. Used for success, error, or informational messages.

**`snackbar-error`** — Error variant using #ad1519 background.

**`snackbar-success`** — Success variant using #25d366 background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to display-md; category strip becomes horizontally scrollable; footer stacks columns |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains display-lg; category strip shows 4-5 visible tabs |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses display-xl; category strip shows all tabs; sidebar filters visible |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero full-bleed with max-width content; additional whitespace around cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Icon buttons are 40x40px minimum
- Quantity selector buttons are 40x40px
- Size selector pills are 40x40px
- Toggle switches are 44px wide minimum
- Category tabs are 40px tall minimum

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px; the hamburger icon is 40x40px with a {rounded.full} shape
- Category strip becomes horizontally scrollable on mobile, with snap points per category
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Sidebar filters collapse into a bottom sheet or modal on mobile
- Search bar collapses to an icon on mobile, expanding to full-width on tap
- Hero text reduces by one size step on each breakpoint (display-xl → display-lg → display-md)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns; exact color shifts and transition durations are not extracted
- Focus states (outline colors, ring offsets) are not captured; likely uses #ad1519 or #3172da for accessibility
- Error state styling for form inputs (border color, error message typography) is not extracted
- Active/pressed states for buttons beyond primary are inferred
- Dark mode is not present on the live site; all dark backgrounds are part of the brand's default light mode
- Sub-brand or collection-specific color palettes (e.g., "Dope Snow x Artist") are not captured
- The exact font weights available in Manrope on the live site are inferred; the site may use a subset (400, 500, 600, 700)
- Letter-spacing values for typography are estimated based on common Manrope usage; exact values may vary
- Shadow values (box-shadow, elevation) are not extracted; product cards likely use subtle shadows
- Animation durations and easing curves are not captured
- The extracted color list includes several blues (#3172da, #2b76ca, #192f8e, #0f2e6b) and greens (#25d366, #009343) that may be from third-party widgets (social icons, payment badges) rather than brand colors; the brand's true palette is dominated by reds, yellow, and dark neutrals
- The extracted color list includes many red variants (#ad1519, #de0000, #cf2734, #e01414, #c11123, #de0c39, #ef303f, #d80f1e, #bc002d) — the primary red (#ad1519) is chosen as the most distinctive and frequently used, but the brand may use multiple reds for different contexts
- The extracted color list includes #00437a, which may be a legacy or secondary brand color
- The site may use a Japanese-language specific typography stack for its Japanese storefront (Manrope may be supplemented with Japanese fonts)
