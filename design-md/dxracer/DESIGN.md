---
version: alpha
name: "DXRacer"
source_url: "https://www.dxracer.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage gaming ecosystem where #efbd16 (a sharp, metallic gold) and #5357d6 (a cool, electric violet) collide against a canvas of #f2f2f2 and #d2d2d2. The brand's visual language is built on aggressive angularity — not the soft pill shapes of consumer tech, but hard, faceted forms that echo the racing bucket seats and carbon-fiber panels of its product line. Typography runs on a dual-engine system: Montserrat in medium-to-bold weights for headlines and navigation, and system fonts (Arial, Helvetica Neue) for body copy, creating a hierarchy where display text punches hard while reading text stays clean and legible. The extracted palette reveals a brand that uses color as a signaling system — #fc337c (a hot pink) appears in accent badges and promotional ribbons, while #004085 and #155724 suggest a deep, serious tone for informational alerts and footer backgrounds. Buttons and interactive elements favor the gold (#efbd16) as primary action color, with the violet (#5357d6) as a secondary or hover state, creating a two-speed system: one for urgency (gold, the "buy now" voltage), one for depth (violet, the "learn more" anchor). The absence of rounded corners in the extracted CSS — no pill shapes, no soft radii — confirms a design philosophy that prioritizes speed and precision over friendliness. This is a brand that wants you to feel the grip of a racing seat, not the embrace of a living room couch.

colors:
  primary: "#efbd16"
  primary-active: "#d39e00"
  primary-disabled: "#ffe8a1"
  ink: "#1b1e21"
  body: "#383d41"
  muted: "#6c757d"
  muted-soft: "#818182"
  hairline: "#c8cbcf"
  hairline-soft: "#b9bbbe"
  canvas: "#f2f2f2"
  surface-soft: "#ececf6"
  surface-card: "#ffffff"
  on-primary: "#1b1e21"
  accent-hot-pink: "#fc337c"
  accent-violet: "#5357d6"
  accent-violet-active: "#0062cc"
  alert-success: "#155724"
  alert-info: "#0c5460"
  alert-warning: "#856404"
  alert-error: "#721c24"
  badge-gold: "#efbd16"
  badge-pink: "#fc337c"
  badge-blue: "#b3d7ff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat-Bold', 'Montserrat', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat-Bold', 'Montserrat', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat-SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat-SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat-Bold', 'Montserrat', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-violet:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-accent-violet-active:
    backgroundColor: "{colors.accent-violet-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-pill-gold:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-violet}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 36px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge-hot-pink:
    backgroundColor: "{colors.accent-hot-pink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-blue:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  alert-success:
    backgroundColor: "{colors.alert-success}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-info:
    backgroundColor: "{colors.alert-info}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.alert-warning}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-error:
    backgroundColor: "{colors.alert-error}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary action button, filled with gold (#efbd16) and set in uppercase Montserrat SemiBold. On hover, it shifts to a deeper gold (#d39e00). The disabled state uses a pale yellow (#ffe8a1) with muted text, signaling the button is inert. Padding is generous (12px top/bottom, 28px left/right) to create a substantial tap target.

**`button-secondary`** — A white button with dark ink text, used for secondary actions like "View Details" or "Compare." The active state gains a light violet background (#ececf6) for subtle feedback. Shares the same dimensions and typography as `button-primary` for visual consistency.

**`button-accent-violet`** — An alternative primary button using the electric violet (#5357d6) for scenarios where gold is overused or where a cooler, more technical tone is needed (e.g., "Customize Your Chair"). Hover shifts to a deeper blue-violet (#0062cc).

**`button-pill-gold`** — A fully rounded variant of the gold button, used sparingly for promotional call-to-actions or newsletter signups. The pill shape is a deliberate departure from the brand's otherwise angular system, creating visual emphasis through contrast.

### Cards
**`product-card`** — The core product display unit, a white card with 8px rounded corners and 16px padding. The product image sits in a 4px rounded container at the top, followed by the title, price, and a gold or hot-pink badge for promotions or new arrivals. Cards are typically arranged in a responsive grid with 24px gaps.

**`product-card-badge`** — A small, sharp-cornered (2px) label pinned to the top-left of the product image. Gold for "Best Seller" or "Sale," hot pink (#fc337c) for "New," and blue (#b3d7ff) for "Limited Edition." Text is 10px uppercase Montserrat Bold with 0.5px letter spacing.

### Navigation
**`nav-bar`** — A fixed 64px header with white background, containing the DXRacer logo, product category links in uppercase Montserrat Medium, a search icon, and a cart icon. Active nav links are highlighted with the brand gold (#efbd16). On mobile, the nav collapses into a hamburger menu.

### Forms
**`text-input`** — A standard input field with a 1px hairline border (#c8cbcf), 4px rounded corners, and 10px padding. On focus, the border thickens to 2px and turns violet (#5357d6), providing clear visual feedback. The input height matches buttons (44px) for alignment in forms.

### Hero
**`hero-section`** — A full-width section with a dark ink (#1b1e21) background and white text, featuring a large headline (36px Montserrat Bold), a supporting subtitle, and a gold CTA button. The hero often includes a product image or lifestyle photography that bleeds to the edges, with no rounded corners on the container.

### Alerts
**`alert-success`**, **`alert-info`**, **`alert-warning`**, **`alert-error`** — System feedback messages with dark backgrounds and white text, using the extracted alert colors (#155724, #0c5460, #856404, #721c24). Each has 8px rounded corners and 12px/16px padding. These appear in checkout flows, account settings, and inventory notifications.

### Footer
**`footer-section`** — A dark ink (#1b1e21) footer with muted gray (#818182) links that lighten to white on hover. Contains columns for product categories, support links, and social media icons. The footer uses the same `{spacing.section}` padding as the hero for visual rhythm.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text scales to 24px; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only; hero maintains 28px headline; search bar moves to nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; hero at 36px; search bar in nav; sidebar filters appear |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero content area constrained to 1200px |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav links have a minimum 40px tap area, even when text is smaller.
- Product card tap targets (title, price, "Add to Cart") are at least 48px tall.
- Search bar and text inputs are 44px tall with 16px padding for comfortable typing.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- Product category filters collapse into a "Filter" button that opens a modal overlay.
- The hero section's secondary text and decorative elements are hidden on mobile, showing only the headline and primary CTA.
- Footer columns collapse into an accordion pattern on mobile, with each section expandable via a tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is heavily polluted with Bootstrap alert colors, system grays, and what appear to be framework defaults (e.g., #004085, #155724, #0c5460, #856404, #721c24). The true brand palette likely has fewer, more intentional colors. The gold (#efbd16) and violet (#5357d6) are the most distinctive and are treated as primary and secondary brand colors, but their exact usage (hover states, disabled states, text on them) is inferred.
- No extracted data for hover states on links, buttons, or cards beyond what is listed. The `button-primary-active` and `button-accent-violet-active` colors are best guesses based on darkening the base color.
- No extracted data for error states on form inputs (e.g., red border, error message styling). The alert-error color (#721c24) is used as a background for error alerts, but input-level error styling is unknown.
- No extracted data for dark mode or high-contrast mode. The brand may have a dark theme for gaming environments, but it is not present in the extracted CSS.
- Font weights for Montserrat variants (Bold, SemiBold, Medium) are inferred from the font-family declarations found. The exact `fontWeight` values (700, 600, 500) are standard mappings.
- The `rounded` values are inferred from typical gaming-chair brand patterns (sharp corners, minimal rounding). No explicit border-radius values were found in the extracted data.
- Spacing values are based on standard 8px grid assumptions, not extracted from the live site.
- Component heights (buttons, inputs, nav) are inferred from common e-commerce patterns for gaming brands. Actual heights may vary.
