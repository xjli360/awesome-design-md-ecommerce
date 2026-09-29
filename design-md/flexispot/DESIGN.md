---
version: alpha
name: "FlexiSpot"
source_url: "https://www.flexispot.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the proposition that a desk should move as much as you do, FlexiSpot’s digital presence is a study in high-contrast urgency — #df3409, a sharp orange-red, punches as the primary CTA voltage against a cool #f5f5f5 canvas, while #017acb and #004df2 provide a secondary technical authority that feels engineered rather than playful. The extracted palette is unusually wide, with a cluster of blues (#34adfe, #2396d9, #1890ff, #1677ff) that suggest a deep product-configuration UI and a multi-tier pricing system, alongside warning-grade accents like #eb5b2f and #b81f00 that flag sale badges and inventory alerts. The typography stack leans on Moderat-Bold and Moderat-Medium — a geometric sans-serif with a slight industrial cut — for headlines and navigation, while Inter handles body copy with its characteristic legibility at small sizes. The design language is fundamentally rectangular: product cards use {rounded.sm} corners, buttons are {rounded.xs} pills or sharp rectangles, and the hero section stacks a full-bleed image behind a left-aligned headline with a single {colors.df3409} CTA. There is no decorative flourish — every visual element serves conversion: the sticky top bar, the persistent cart badge, the “Shop Now” button that repeats at three scroll depths. The brand’s voice is direct, slightly urgent, and framed around ergonomic benefit statements (“Sit less, move more”) rather than lifestyle aspiration. The extracted hex #34b37e appears in sustainability badges and eco-certification callouts, a secondary green that signals trust without competing with the primary orange-red conversion engine.

colors:
  primary: "#df3409"
  primary-active: "#b81f00"
  primary-disabled: "#f1eeeb"
  ink: "#232324"
  body: "#26333a"
  muted: "#67696a"
  muted-soft: "#8b8c8b"
  hairline: "#d9d9d9"
  hairline-soft: "#ede9e4"
  canvas: "#f5f5f5"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#017acb"
  accent-blue-active: "#005ea6"
  accent-warning: "#eb5b2f"
  accent-sale: "#b41b19"
  accent-gold: "#feab00"
  accent-green: "#34b37e"
  link-blue: "#1890ff"
  link-blue-active: "#1677ff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Moderat-Bold', Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Moderat-Bold', Inter, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Moderat-Bold', Inter, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Moderat-Bold', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Moderat-Bold', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price-md:
    fontFamily: "'Moderat-Bold', Inter, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Moderat-Medium', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 48px
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-cart:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-cart-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "2px solid {colors.accent-warning}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
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
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price-sm}"
    padding: "{spacing.xs} {spacing.base} {spacing.sm}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    typography: "{typography.caption-sm}"
    color: "{colors.accent-gold}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "480px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: "16px 36px"
    height: 56px
  hero-subtitle:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "2px solid {colors.accent-blue}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.surface-card}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  category-tile-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary conversion engine, rendered in {colors.df3409} with white text and a tight {rounded.xs} corner. On hover it deepens to {colors.b81f00}; the disabled state drops to {colors.f1eeeb} with {colors.muted} text, signaling unavailability without visual noise. Used for “Add to Cart,” “Shop Now,” and primary checkout actions. **`button-secondary`** — A white button with a 2px {colors.hairline} border and {colors.ink} text, used for “Learn More” and “Compare” actions. Active state swaps the border to {colors.ink} for emphasis. **`button-ghost`** — Transparent background with {colors.primary} text, used for “View Details” links within product cards where a full button would compete with the CTA. **`button-sale`** — A compact, high-urgency button in {colors.b41b19} with white text and smaller padding, used exclusively for flash-sale timers and limited-stock badges. **`button-cart`** — The secondary CTA in {colors.017acb}, used for “Pre-Order” and “Notify Me” states where the primary orange-red would imply immediate purchase rather than waitlisting.

### Cards
**`product-card`** — A white card with a 1px {colors.hairline-soft} border and {rounded.sm} corners. The image occupies the full top half with a square aspect ratio; below it, the title uses {typography.title-sm}, the price uses {typography.price-sm}, and a gold star rating ({colors.feab00}) sits at the bottom. On hover, the border thickens to {colors.hairline} and a subtle shadow lifts the card. **`category-tile`** — A soft-gray tile ({colors.f0f0f0}) with centered text, used on the homepage to link to desk categories (Standing, Gaming, Office). Hover shifts the background to {colors.ede9e4} and tints the text {colors.primary}.

### Navigation
**`nav-bar`** — A 72px white bar with a single {colors.ede9e4} bottom border. Logo sits left, category links center, and utility icons (search, account, cart) right. The sticky variant shrinks to 56px and gains a subtle shadow on scroll. Active nav links render in {colors.primary}; inactive links in {colors.muted}. **`nav-link-active`** — No background, just a color shift to {colors.primary} and the same {typography.nav-link} weight, creating a clean underline-free active state that relies on color contrast alone.

### Forms
**`text-input`** — A white input with a 1px {colors.d9d9d9} border and {rounded.xs} corners. On focus, the border doubles to 2px and shifts to {colors.017acb}. Error state uses a 2px {colors.eb5b2f} border. **`select-dropdown`** — Matches the text-input styling but includes a custom chevron icon in {colors.muted}. **`quantity-selector`** — A compact 40px input with increment/decrement buttons on either side, used in the cart and product detail pages.

### Badges
**`badge-new`** — A green badge ({colors.34b37e}) with white uppercase text, used for newly launched products. **`badge-sale`** — A red badge ({colors.b41b19}) with white text, used for discounted items. **`badge-eco`** — A pill-shaped green badge with white text, used for sustainability certifications. **`cart-icon-badge`** — A 20px circle in {colors.df3409} with white text, positioned at the top-right of the cart icon to show item count.

### Hero
**`hero-section`** — A full-width section with a minimum height of 480px, left-aligned content, and a background image that bleeds edge-to-edge. The headline uses {typography.display-xl} in {colors.ink}, the subtitle uses {typography.body-md} in {colors.26333a}, and the single CTA uses {colors.df3409} with {typography.button-lg} at 56px height. No secondary button — the hero is designed for a single action.

### Footer
**`footer-section`** — A dark footer in {colors.232324} with white text. Links render in {colors.8b8c8b} and shift to white on hover. The layout is a multi-column grid with company info, support links, and social icons. No rounded corners — the footer is a hard rectangle that anchors the page bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero reduces to 320px min-height; buttons go full-width; font sizes drop one step (display-xl → 28px) |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only; hero maintains 400px min-height; search bar moves to sticky header |
| Desktop | 1128–1440px | Three-column product grid; full nav with all subcategories; hero at 480px; search bar in top nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px preferred)
- Nav links minimum 40px tap area
- Quantity selector buttons minimum 36px tap area
- Product card tap target is the entire card surface
- Cart icon badge minimum 20px diameter with 8px padding around it

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Secondary nav (subcategories) collapses to dropdown below 1128px
- Footer multi-column grid collapses to single column below 744px
- Product filters collapse to a “Filter” button with modal overlay below 744px
- Search bar collapses to icon-only trigger below 744px, expanding to full-width overlay on tap
- Hero image collapses to 50% viewport height on mobile, with text overlay instead of side-by-side

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex list is unusually large (30+ colors) and includes several blues that may be framework defaults (#1890ff, #1677ff are Ant Design primaries; #34adfe may be a social icon color). The true brand palette likely centers on #df3409 (orange-red), #017acb (blue), and #232324 (ink), but the exact secondary palette is uncertain without access to the design token file.
- No extracted meta-theme-color, so dark mode support is unknown.
- Hover and active states for most components are inferred from common patterns; actual transition durations, easing curves, and shadow values are not extracted.
- Error, success, and warning form states beyond the error border are not confirmed.
- The extracted font list includes both Moderat (likely the brand font) and Inter (likely the system fallback), but the exact weight assignments for body copy vs. headings are inferred from common usage.
- No extracted data for loading states, skeleton screens, or spinner animations.
- Sub-brand or regional palette variations (e.g., FlexiSpot EU vs. US) are not captured.
- The extracted palette includes #eb2f96 (pink) and #f5222d (red) which may be checkout-widget colors (Shopify Pay, Klarna) rather than brand colors — these are excluded from the primary palette.
- No extracted data for the product configurator UI (desktop height selector, color swatches, cable management options) which is a core brand interaction.
- The extracted #fdfcf5 and #e6f9ff may be background tints for specific sections (testimonials, warranty callouts) but their usage is unconfirmed.
