---
version: alpha
name: "Rejuvenation"
source_url: "https://www.rejuvenation.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A warm, tactile home furnishings brand that marries industrial heritage with soft, lived-in comfort. The palette is anchored in deep charcoals (#2b3033) and near-black ink (#1a1818), offset by a warm brass accent (#896b27) that appears in hardware, lighting fixtures, and decorative details — a nod to the brand's roots in salvaged and vintage-inspired design. The primary action color is a restrained vermilion (#d04727), used sparingly on buttons and key CTAs to create deliberate moments of energy against the otherwise muted backdrop. Typography runs Gotham and Arial at modest weights, with display sizes rarely exceeding 28px; the brand trusts generous whitespace and tactile product photography over typographic muscle. Surfaces are soft — cards and buttons use `{rounded.sm}` (8px) and `{rounded.md}` (12px) radii that read as approachable but not overly friendly, while the search bar and hero elements adopt `{rounded.full}` pill shapes for a refined, curated feel. The overall mood is that of a well-edited workshop: structured, honest, and quietly confident, with every design decision deferring to the materiality of the products themselves.

colors:
  primary: "#d04727"
  primary-active: "#b33d22"
  primary-disabled: "#e8a18f"
  ink: "#1a1818"
  body: "#2b3033"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#b9babb"
  hairline-soft: "#d4d5d6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#e8e9e9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-brass: "#896b27"
  accent-brass-light: "#a88b4a"
  badge-new: "#d04727"
  badge-sale: "#896b27"
  star-rating: "#2b3033"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02px
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  button-pill-brass:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.body}"
  text-input-error:
    border: "2px solid {colors.primary}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-pill-focus:
    border: "1px solid {colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.on-dark}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border-bottom: "2px solid {colors.ink}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: 4px

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, rendered in the brand's signature vermilion (`{colors.primary}`) with white text. Uses uppercase Gotham at 14px/600 weight for a confident, editorial feel. Hover state darkens to `{colors.primary-active}`. Disabled state fades to a soft salmon (`{colors.primary-disabled}`). All variants maintain `{rounded.sm}` (8px) corners and a consistent 48px height.

**`button-secondary`** — A ghost-style button with a subtle hairline border (`{colors.hairline}`) on a white background. Hover state darkens the border to `{colors.ink}` and adds a light fill (`{colors.surface-soft}`). Used for secondary actions like "Add to Wishlist" or "View Details."

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Learn More." Inherits `{colors.body}` and uses the same uppercase button typography for consistency.

**`button-pill-brass`** — A special-purpose pill-shaped button in the brass accent (`{colors.accent-brass}`), used sparingly for premium actions like "Schedule Consultation" or "Request a Swatch." The `{rounded.full}` shape and smaller padding give it a refined, jewelry-like presence.

### Cards
**`product-card`** — The primary product display card, featuring a square image with `{rounded.sm}` corners, a title in `{typography.title-sm}`, and a muted price line. The card itself has no background fill (white canvas) and relies on the product photography and generous whitespace for visual hierarchy. Hover state typically adds a subtle shadow or border.

**`hero-banner`** — A full-width promotional banner with a soft gray background (`{colors.surface-soft}`), large display typography, and a single primary CTA button. The banner has no rounded corners, creating a clean, editorial break between sections. Padding is generous at `{spacing.section}` vertical and `{spacing.xl}` horizontal.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). Navigation links use uppercase Gotham at 14px/500 weight. Active links are indicated by a 2px bottom border in `{colors.ink}`. The bar contains the brand logo, category links, and utility icons (search, account, cart).

**`category-strip`** — A horizontal scrollable strip of category tabs below the main nav. Inactive tabs are muted (`{colors.muted}`), active tabs are dark (`{colors.ink}`) with a 2px underline. Used for filtering product categories on collection pages.

### Forms
**`text-input`** — Standard text input with a white background, 1px hairline border, and 8px rounded corners. Focus state gains a 2px dark border (`{colors.body}`). Error state uses a 2px primary-red border. Disabled inputs fade to a soft gray background with muted text. Height is consistent at 48px to match buttons.

**`quantity-selector`** — A compact input for adjusting product quantities, with a hairline border and two small buttons for increment/decrement. The buttons use muted text and minimal padding to keep the component compact.

### Badges
**`badge-new`** — A small uppercase badge in the primary vermilion, used to flag new arrivals. Uses 11px/600 weight Gotham with 0.5px letter spacing for readability at small sizes.

**`badge-sale`** — A badge in the brass accent color, used for sale or promotional items. Same typography and sizing as `badge-new` for visual consistency.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` background and white text. Links are rendered in a muted gray (`{colors.muted-soft}`) and lighten on hover. The footer uses generous vertical padding (`{spacing.xxl}`) and contains multiple columns for navigation, support, and brand information.

### Accordion
**`accordion-header`** — A clickable header with a bottom border, used for product details, shipping information, and FAQ sections. Content panels slide open below with body typography and standard spacing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger nav replaces full category strip, hero banner reduces to 2/3 height, search bar collapses to icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, category strip remains scrollable, nav links show abbreviated labels, hero banner maintains full width with reduced padding |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, category strip shows all tabs, hero banner at full height with generous padding |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero banner may include parallax or full-bleed imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile
- Quantity selector buttons are 40x40px minimum
- Icon buttons (search, cart, account) are 48x48px on mobile, 40x40px on desktop
- Accordion headers have 48px minimum tap height

### Collapsing Strategy
- Main navigation collapses to a hamburger menu below 744px
- Category strip becomes horizontally scrollable (no wrapping) below 744px
- Footer columns stack vertically below 744px
- Product grid reduces columns progressively (4 → 3 → 2 → 1)
- Hero banner text and CTA stack vertically below 744px
- Search bar collapses to an icon that expands to full-width overlay on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors
- Error styling for forms (error messages, validation icons) is inferred from common patterns rather than extracted
- Dark mode or high-contrast mode tokens are not present in the extracted data
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured
- Specific shadow values (box-shadow, drop-shadow) were not extractable from the live site
- Transition/animation durations and easing curves are not defined
- Icon set details (stroke width, sizes, color inheritance) are not specified
- Print stylesheet or email-specific tokens are not included
- The `rejuvenation-icons` font family was detected but individual icon glyphs and their usage patterns could not be mapped
