---
version: alpha
name: "Lemi Shine"
source_url: "https://lemishine.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cleaning brand that builds its visual language around a citrus-yellow voltage (#ffc52e) and a deep, almost-black ink (#121212), creating a system that feels both energetic and trustworthy. The yellow appears not as a timid accent but as the dominant force — it fills primary buttons, badge backgrounds, and promotional banners, while the dark ink anchors body text and navigation for readability. A secondary green (#3ed660) and orange (#ee9441) suggest the brand's citrus-derived formulations without needing literal fruit photography. The palette is rounded out by a warm gray family (#d1d1d1, #dedede, #c8c8c8, #d9d9d9) that keeps surfaces soft and approachable — product cards, input fields, and footer backgrounds use these muted tones rather than stark white or harsh black. Typography runs Inter at moderate weights (400 for body, 600 for buttons, 700 for display), with generous line heights (1.5 for body) that make ingredient lists and usage instructions feel scannable. Buttons are softly rounded at {rounded.sm}, while badges and promotional tags use {rounded.full} pill shapes that echo the brand's citrus-sphere identity. The overall mood is bright, clean, and confident — a household cleaner that doesn't whisper about its efficacy but announces it through saturated color blocks and clear, direct typography.

colors:
  primary: "#ffc52e"
  primary-active: "#f0b500"
  primary-disabled: "#ffe899"
  ink: "#121212"
  body: "#2c2d2c"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#d1d1d1"
  hairline-soft: "#dedede"
  canvas: "#f5f5f5"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  accent-green: "#3ed660"
  accent-orange: "#ee9441"
  badge-red: "#8b0000"
  badge-green: "#006400"
  star-rating: "#ffc52e"

typography:
  display-xl:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Sofia Pro', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    padding: 11px 23px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
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
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
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
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "48px 24px"
  hero-banner-alt:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "48px 24px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "48px 24px"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 32px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "16px 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 16px 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's signature yellow (#ffc52e) and dark ink text. Used for "Add to Cart", "Shop Now", and primary checkout actions. On hover, shifts to a slightly deeper yellow (#f0b500). Disabled state uses a pale yellow (#ffe899) to indicate inactivity while maintaining brand recognition. Height is 48px with 12px vertical padding for comfortable touch targets.

**`button-secondary`** — A ghost button with the canvas background and ink text, outlined by a 1px hairline border. Used for secondary actions like "Learn More" or "View Details". Maintains the same 48px height as the primary button for alignment in button groups. On hover, the border darkens to the hairline color.

**`button-tertiary-text`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Skip". Uses the same button-md typography but with transparent background, relying on the ink color for visibility.

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for promotional badges, category filters, and subscription CTAs. Smaller padding (8px vertical) makes it suitable for inline use within product cards or banner overlays.

**`button-pill-outline`** — The outline counterpart to the pill primary, used for secondary filter options or "Compare" actions. Maintains the same pill shape and sizing for visual consistency in filter strips.

### Cards
**`product-card`** — A white card with 12px rounded corners and 16px internal padding, used to display individual products in grid layouts. The card contains a product image (with matching 12px rounded corners), title, price, rating stars, and optional badges. On hover, a subtle shadow elevation is applied (not captured in extracted data). The card background is white (#ffffff) while the surrounding grid uses the canvas color (#f5f5f5) for visual separation.

**`product-card-badge`** — A small pill-shaped badge overlaid on product card images, using the primary yellow with dark text. Used for "Best Seller", "Limited Edition", or promotional flags. The uppercase badge typography at 11px keeps the badge compact and readable at small sizes.

### Navigation
**`nav-bar`** — A 72px tall navigation bar with canvas background, containing the brand logo, navigation links, and a search icon. Navigation links use uppercase 14px font-weight 600 typography. Active links display in ink (#121212) while inactive links appear in muted gray (#6a6a6a). The bar is fixed at the top of the viewport on desktop.

**`nav-link-active`** — Active navigation link state with ink color and no background. The uppercase treatment gives the nav a clean, professional feel appropriate for a cleaning brand.

**`nav-link-inactive`** — Inactive navigation link state using muted gray, maintaining the same uppercase typography for visual consistency.

### Forms
**`text-input`** — A standard text input field with canvas background, 8px rounded corners, and a 1px hairline border. Used for search queries, email signups, and form fields. On focus, the border expands to 2px and shifts to the primary yellow for clear visual feedback. Height is 48px with 12px vertical padding for comfortable typing.

**`search-bar`** — A fully rounded pill-shaped search input with canvas background and hairline border. Used in the navigation bar and hero sections. The pill shape echoes the brand's citrus-sphere identity while providing a generous 48px height for touch targets.

### Hero
**`hero-banner`** — A full-width banner filled with the primary yellow, using large display typography (28px) and dark ink text. Used for promotional campaigns, seasonal sales, and new product launches. Contains a headline, subheading, and a primary CTA button. Padding is generous at 48px vertical.

**`hero-banner-alt`** — An alternative hero banner using the accent green (#3ed660) instead of yellow, used for eco-friendly messaging, sustainability campaigns, or "plant-based" product lines. Maintains the same layout and typography for visual consistency across hero variants.

### Badges
**`badge-sale`** — A red (#8b0000) pill badge with white text, used for sale and discount indicators. The dark red provides strong contrast against product card backgrounds and signals urgency effectively.

**`badge-new`** — A green (#3ed660) pill badge with dark ink text, used for "New Arrival" and "Just Launched" indicators. The green aligns with the brand's citrus-derived, plant-based messaging.

### Footer
**`footer-section`** — A dark footer using the ink color (#121212) as background with white text. Contains navigation links, social media icons, newsletter signup, and legal text. Padding is 48px vertical with 24px horizontal. The dark footer provides a strong visual anchor at the bottom of every page.

**`footer-link`** — Footer navigation links in white with 14px font-weight 500 typography. Links are spaced with 8px vertical gaps for scannability.

**`social-icon`** — Circular social media icons (32px) with transparent background and white icon color. Used in the footer for Instagram, Facebook, TikTok, and Pinterest links.

### Accordion
**`accordion-header`** — Expandable accordion section headers used for product descriptions, ingredient lists, and FAQ sections. Uses title-sm typography with a bottom border for visual separation. On click, the header expands to reveal the accordion content below.

**`accordion-content`** — The expandable content area beneath accordion headers, using body-sm typography for readable product details and ingredient information.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked hero layout, reduced padding (24px section), smaller display typography (28px → 24px), full-width buttons |
| Tablet | 744–1128px | Two-column product grid, visible navigation links, side-by-side hero content, 32px section padding, medium display typography |
| Desktop | 1128–1440px | Three-column product grid, full navigation bar, wide hero banners, 48px section padding, full display typography |
| Wide | > 1440px | Four-column product grid, max-width container (1440px), centered layout, maintained typography scale |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 48px height for touch accessibility
- Product card tap targets are the full card area, not just text links
- Accordion headers have 48px minimum touch height
- Social icons are 32px with 8px padding for 48px effective touch target
- Navigation links have 72px tap area within the nav bar

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero banners stack vertically (image below text) on mobile
- Footer columns collapse from 4 to 2 on tablet, 1 on mobile
- Accordion content collapses by default on all breakpoints
- Search bar collapses to icon-only on mobile, expanding on tap
- Category filter strip collapses to horizontal scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links beyond primary button (secondary, tertiary, pill variants) could not be reliably extracted
- Focus and error states for form inputs (red border, error message styling) are not confirmed
- Shadow/elevation values for cards, modals, and dropdowns are not captured
- Dark mode color overrides are not present in the extracted data
- Sub-brand or product-line-specific color palettes (e.g., "Lemi Shine Dishwasher Cleaner" vs "Lemi Shine Laundry") are not confirmed
- Animation durations, easing curves, and transition properties are missing
- Modal, tooltip, and dropdown component styling is not captured
- The extracted font list includes "inherit" and "sans-serif" as generic fallbacks — the primary brand font is assumed to be Inter based on the first declaration found, but "Sofia Pro" appears as an alternative and may be used for display headings in some contexts
- The extracted color list includes several grays (#d1d1d1, #dedede, #c8c8c8, #d9d9d9) that may represent different system roles (borders, backgrounds, disabled states) — the assignment above is an educated interpretation
- Red (#8b0000) and green (#006400) may be checkout-widget or stock-image colors rather than intentional brand colors — they are included as badge variants but should be verified against actual site usage
- The accent green (#3ed660) and orange (#ee9441) are distinctive and likely intentional, but their exact usage contexts (backgrounds, icons, text) need confirmation
- Star rating color is assumed to match the primary yellow based on common e-commerce patterns, but this is not confirmed from extraction
- Typography scale for mobile breakpoints (reduced font sizes) is not confirmed from extracted data
