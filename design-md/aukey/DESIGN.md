---
version: alpha
name: "Aukey"
source_url: "https://www.aukey.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-navy (#0f1822) electronics brand whose signature voltage comes from a vivid teal-green (#00bda2) — a color that reads as cool, conductive, and engineered, not warm or organic. The teal appears on primary CTAs, sale badges, and the "Shop Now" orb, while the dark navy forms the persistent header bar and footer, creating a high-contrast, technical feel. The extracted palette is unusually broad (25+ colors), suggesting a Shopify store with many widget layers, but the core brand axis is clear: navy canvas, teal action, and a secondary orange (#f15a24) used sparingly for urgency badges and price drops. Type runs Montserrat across multiple weights — SemiBold for headings, Medium for body, Regular for captions — with Epilogue appearing as a secondary display face. Product cards use soft corners (`{rounded.sm}` ~8px) and generous white space (`{spacing.base}` ~16px) to let the tech photography breathe, while the persistent top nav stays fixed at `{spacing.xl}` height with a white background and navy text. The checkout flow introduces a separate accent (#007aff) for Apple Pay integration, and the review stars use a dedicated JudgemeStar font. This is a brand that trusts its product imagery over decorative flourishes — the design system is a clean, dark-light frame for the hardware.

colors:
  primary: "#00bda2"
  primary-active: "#00a68e"
  primary-disabled: "#b3e6dd"
  ink: "#0f1822"
  body: "#383838"
  muted: "#676767"
  muted-soft: "#9e9e9f"
  hairline: "#d1d3d3"
  hairline-soft: "#e4e4e4"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f15a24"
  accent-red: "#ff2948"
  badge-sale: "#00bda2"
  badge-new: "#108474"
  star-rating: "#00b097"
  apple-pay: "#007aff"
  footer-bg: "#111921"
  footer-text: "#dadada"

typography:
  display-xl:
    fontFamily: "'Montserrat-Bold', 'Epilogue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat-SemiBold', 'Epilogue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Montserrat-SemiBold', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat-Medium', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat-Medium', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat-SemiBold', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat-Medium', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Montserrat-Medium', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Montserrat-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  badge:
    fontFamily: "'Montserrat-SemiBold', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat-SemiBold', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Montserrat-SemiBold', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-orange}"

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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 4px rgba(15, 24, 34, 0.08)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.primary}"
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
    padding: "14px 32px"
  star-rating:
    fontFamily: "JudgemeStar, sans-serif"
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's distinctive teal (#00bda2) with white text. Uses Montserrat SemiBold at 14px with 0.5px letter spacing for a precise, technical feel. On hover, shifts to `{colors.primary-active}` (#00a68e). Disabled state uses a muted teal (`{colors.primary-disabled}`) that still reads as active but unreachable. The `{rounded.sm}` (8px) corners keep the button feeling modern but not overly friendly — it's an electronics brand, not a toy store.

**`button-secondary`** — White background with a `{colors.hairline}` border and navy text. Used for "Learn More" links, secondary cart actions, and filter resets. Active state gains a full navy border (`{colors.ink}`) and a `{colors.surface-soft}` background. Height matches the primary button at 44px for consistent alignment in forms and product grids.

**`button-accent-orange`** — Reserved for urgency: limited-time offers, flash sale banners, and price-drop notifications. Uses `{colors.accent-orange}` (#f15a24) — a warm, high-energy contrast to the cool teal-navy system. Same dimensions and typography as the primary button, ensuring it can sit alongside without looking broken.

**`button-pill`** — A smaller, fully rounded (`{rounded.full}`) variant used for filter chips, category tags, and "Add to Compare" toggles. Uses `{typography.button-sm}` (12px Medium) and tighter padding (8px 20px) to fit in crowded UI zones like the product listing toolbar.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.sm}` corners and `{spacing.sm}` internal padding. The product image fills the top with a matching `{rounded.sm}` and a 1:1 aspect ratio. Below, the title uses `{typography.title-md}` (18px Medium) and the price uses `{typography.price}` (16px SemiBold). Sale items swap the price token to `{typography.price-sale}` which renders in `{colors.accent-orange}`. Badges (sale, new, discount) overlay the top-left of the image using `{spacing.sm}` offset.

### Navigation
**`nav-bar`** — A fixed 56px white bar spanning the full viewport width. Navigation links use `{typography.nav-link}` (14px Medium) with `{spacing.lg}` horizontal padding between items. The logo sits left-aligned, the search icon and cart icon sit right-aligned. On scroll, a subtle `boxShadow` appears to separate the bar from content. The mobile variant collapses the link list into a hamburger menu.

**`search-bar`** — A pill-shaped (`{rounded.full}`) input field on a `{colors.surface-soft}` background with a `{colors.hairline}` border. At 40px height, it's compact enough for the nav bar but expands to full width on the search results page. Focus state swaps the border to `{colors.primary}` teal.

### Footer
**`footer`** — A dark navy (`{colors.footer-bg}`) section with `{colors.footer-text}` (#dadada) body copy. Links use `{typography.link}` and turn teal on hover. The footer is divided into columns for product categories, support, and company info, with `{spacing.xxl}` padding top and bottom. A thin `{colors.hairline-soft}` separator divides the newsletter signup from the link columns.

### Hero
**`hero-section`** — Full-width promotional banners using a dark navy (`{colors.ink}`) background with white text. The headline uses `{typography.display-xl}` (32px Bold) and the CTA uses `{typography.button-md}` with `{colors.primary}` teal. The hero may include product photography or lifestyle imagery that bleeds to the edges, with text overlaid at `{spacing.section}` padding.

### Badges
**`badge-sale`**, **`badge-new`**, **`badge-orange`** — Small uppercase labels (11px SemiBold) with `{rounded.xs}` (4px) corners and tight 2px 8px padding. Sale badges use the primary teal, new-product badges use a deeper teal (`{colors.badge-new}`), and urgency badges use the accent orange. These overlay product images at a consistent top-left position.

### Star Ratings
**`star-rating`** — Uses the JudgemeStar font family at 16px with `{colors.star-rating}` (#00b097) — a slightly deeper teal than the primary, reserved for review elements. Stars render as filled, half-filled, or empty glyphs from the JudgemeStar typeface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in 2-column grid. Hero text reduces to `{typography.display-md}`. Footer columns stack vertically. Search bar moves to full-width below nav. |
| Tablet | 744–1128px | Nav bar shows 4-5 links. Product cards in 3-column grid. Hero maintains `{typography.display-xl}` but reduces padding. Footer shows 2-column layout. |
| Desktop | 1128–1440px | Full nav bar with all links. Product cards in 4-column grid. Hero at full padding. Footer shows 4-column layout. |
| Wide | > 1440px | Max-width container at 1440px with auto margins. Product cards may expand to 5-column grid. Hero content centered with max-width 1200px. |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility.
- Nav bar hamburger icon targets 48x48px tap area.
- Product card tap targets (title, price, add-to-cart) are at least 44px tall.
- Search bar input field is 40px tall with 44px tap area via padding.
- Footer links have 44px minimum tap height.

### Collapsing Strategy
- Nav bar link list collapses to hamburger menu below 744px.
- Product grid reduces columns: 4 → 3 → 2 as viewport shrinks.
- Hero section reduces vertical padding by 50% on mobile.
- Footer columns collapse from 4 to 2 to 1.
- Search bar moves from inline nav position to full-width below nav on mobile.
- Product card badges reduce font size to 10px on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color list is unusually large (25+ colors), likely including Shopify widget colors (Klarna, Afterpay, Apple Pay), social icon colors, and stock image dominant tones. The true brand palette may be smaller — the 6-8 core colors listed above are the most confident picks.
- Font stack includes "Mont-SerratSemiBold" with a typo (hyphen and missing "t") — likely a CSS error or custom font name. Mapped to Montserrat-SemiBold for consistency.
- "JudgemeStar" is a review widget font, not a brand typeface — included only for star rating component.
- "swiper-icons" font suggests a slider/carousel library — not included in typography.
- Hover states for buttons are inferred from common patterns; exact transition durations and shadow depths not extracted.
- Error states for form inputs (red border, error message styling) not observed on live site.
- Dark mode not present; no dark theme tokens available.
- Sub-brand or product-line-specific palettes (e.g., for Aukey's audio vs. charging products) not distinguishable.
- Checkout flow colors (#007aff for Apple Pay) may not be brand-controlled.
- Loading states, skeleton screens, and empty states not observed.
- Focus ring styles (outline, offset, color) not extracted.
