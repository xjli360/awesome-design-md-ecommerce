---
version: alpha
name: "Sijo"
source_url: "https://sijohome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sijo is a performance bedding and bath brand that speaks in a quiet, confident palette of deep navy and soft stone. The primary voltage is a rich midnight blue (`#0b173a`) that appears on CTAs, headlines, and the brand's signature woven labels — a color that reads as both premium and restful, like a well-made bed in a dim room. Supporting this is a warm off-white canvas (`#f1efec`) that softens the digital experience, paired with a cooler surface tone (`#f4f4f6`) for cards and panels. The brand's accent palette introduces unexpected energy: a lime green (`#c7e400`) used sparingly for badges and highlights, a deeper forest green (`#468038`) for sustainability messaging, and a mustard yellow (`#ffcf2a`) for sale indicators and trust signals. Typography centers on `basis-grotesque-bold-pro` for display headings — a geometric sans-serif with sharp, confident letterforms — while body copy runs in a clean system stack (`-apple-system`, `Helvetica Neue`, `Roboto`). Buttons use `{rounded.sm}` (8px) corners, while product cards and modals adopt `{rounded.md}` (12px) for a soft but not pill-like feel. The overall mood is one of considered calm: generous whitespace, muted borders (`#dbdde4`), and a deliberate avoidance of visual noise. Signature design moves include a persistent top nav with a centered logo, product cards that float on `{surface-card}` with subtle shadow, and a footer that stacks utility links in a dense, readable grid. The brand trusts its textile photography — close-ups of percale weaves, bamboo fibers, and brushed cotton — to carry emotional weight, letting the UI step back into a supporting role. Every interaction feels deliberate, from the `{spacing.lg}` padding on CTAs to the `{spacing.section}` breathing room between product rows.

colors:
  primary: "#0b173a"
  primary-active: "#0a1433"
  primary-disabled: "#9da2b0"
  ink: "#0b173a"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#878787"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f1efec"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#468038"
  accent-lime: "#c7e400"
  accent-yellow: "#ffcf2a"
  accent-green-soft: "#4a883a"
  sale-badge: "#ffcf2a"
  eco-badge: "#468038"
  star-rating: "#ffcf2a"
  error: "#c13515"
  success: "#468038"
  scrim: "#0b173a"

typography:
  display-xl:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'basis-grotesque-bold-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.sm}"
    padding: 14px 32px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
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
  text-input-error:
    border: "1px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
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
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: 500px
  hero-banner-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 400px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-link-hover:
    textColor: "{colors.accent-lime}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "16px 20px"
  accordion-body:
    padding: "0 20px 16px 20px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  badge-eco:
    backgroundColor: "{colors.eco-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and checkout flows. Renders as a solid midnight blue (`{colors.primary}`) rectangle with 8px rounded corners and white text in `basis-grotesque-bold-pro` at 15px. On hover, shifts to a slightly deeper navy (`{colors.primary-active}`). Disabled state uses a muted gray-blue (`{colors.primary-disabled}`). Padding of 14px top/bottom and 32px left/right creates a substantial, confident feel.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses the same typography and height as primary but with a transparent fill, navy text, and a 2px solid navy border. On hover, fills solid with the primary color and inverts text to white.

**`button-tertiary`** — A text-only button for subtle actions like "Cancel" or "Clear Filters". No background or border, just navy text with standard link-style padding. Used in forms and filter panels where visual weight should be minimal.

**`button-pill`** — A fully rounded variant (9999px radius) used for filter chips, category tags, and mobile navigation items. Smaller at 40px height with 10px/24px padding. Also available as an outline variant (`button-pill-outline`) with a single hairline border.

### Cards
**`product-card`** — The primary product display unit on collection pages and search results. A white card with 12px rounded corners containing a square aspect-ratio image, product title in 16px semibold, price in 16px bold, and optional badges. Cards sit on `{surface-card}` with no border, relying on the contrast against `{surface-soft}` backgrounds. Badges use `{rounded.xs}` (4px) for a crisp, intentional look.

**`hero-banner`** — Full-width promotional banners at the top of key pages. The primary variant uses a navy background with white text and 500px height. An alternate variant uses the soft surface tone with navy text at 400px height for editorial content. Both center content vertically with generous padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on a warm off-white canvas. Contains the centered logo, left-aligned category links in uppercase 14px bold, and right-aligned utility icons (search, account, cart). Active links use the primary navy color; inactive links use muted gray. On mobile, collapses to a hamburger menu with a full-screen overlay.

**`footer-section`** — A dense, information-rich footer on a navy background with white text. Contains columns for customer service, company info, and social links. Links use 14px medium weight and shift to lime green (`{colors.accent-lime}`) on hover. Includes newsletter signup, payment icons, and legal text.

### Forms
**`text-input`** — Standard text input fields used in checkout, account forms, and newsletter signup. 48px height with 12px/16px padding, 8px rounded corners, and a single hairline border. On focus, the border thickens to 2px and turns navy. Error state uses a red border (`{colors.error}`). Background matches the canvas tone for a cohesive look.

**`select-dropdown`** — Custom-styled select elements matching the text input dimensions and styling. Used for size selection, quantity, and filter options. The dropdown arrow is a custom SVG in the muted gray color.

**`quantity-selector`** — A compact 40px input for adjusting product quantities, with minus/plus buttons flanking the numeric value. Uses a hairline border and 8px rounded corners.

### Badges & Indicators
**`badge-sale`** — A yellow (`{colors.sale-badge}`) badge with navy text, used to flag discounted items. 4px rounded corners with 2px/8px padding. Text is uppercase 11px bold.

**`badge-eco`** — A green (`{colors.eco-badge}`) badge with white text, used for sustainability claims like "Organic" or "Eco-Friendly". Same dimensions as sale badge but with inverted colors.

**`rating-stars`** — A 5-star rating display using yellow stars (`{colors.star-rating}`) at 16px. Used on product cards and review sections. Empty stars render in the hairline color.

### Layout Elements
**`divider`** — A 1px horizontal line in the hairline color, used to separate sections within cards, accordions, and footer columns. Full-width within its container.

**`section-header`** — A typographic section heading with 64px top padding and 24px bottom padding. Uses `display-md` (26px bold) in navy. Used for collection titles, category headings, and editorial section breaks.

**`accordion`** — Collapsible content panels used for product descriptions, shipping info, and FAQs. Each accordion has a clickable header (18px semibold) and a body that expands with a smooth animation. Uses 8px rounded corners and a single hairline border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger nav replaces full nav, hero banners reduce to 300px height, accordion layout for footer, search bar collapses to icon-only, product cards stack vertically with full-width images |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero banners at 400px height, footer splits into 2-column grid, search bar shows as icon with expandable input |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links visible, hero banners at 500px height, footer in 4-column grid, persistent search bar with placeholder text |
| Wide | > 1440px | Four-column product grid on collection pages, max-width containers (1440px) with centered content, hero banners maintain 500px height with wider typography, additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons in nav bar are 40px × 40px with 8px padding around icons
- Product card CTAs ("Quick Add", "Select Options") are 48px tall with generous tap targets
- Accordion headers have 56px minimum touch height (16px padding top/bottom on 18px text)
- Quantity selector buttons are 40px × 40px with centered +/- icons
- Mobile nav links are 48px tall with full-width tap targets
- Filter chips and badges are 40px tall with 24px+ padding for easy tapping
- Star rating stars are 16px with 4px gap, but the entire rating area is a 44px+ tap target

### Collapsing Strategy
- Top navigation collapses from full link set to hamburger menu at < 744px
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer collapses from 4-column grid → 2-column → single-column accordion layout
- Hero banners reduce height proportionally (500px → 400px → 300px)
- Search bar collapses from full input with placeholder → icon-only with expandable overlay
- Category filter strip collapses from horizontal scroll → dropdown selector
- Product card badges stack vertically on mobile instead of horizontal layout
- Secondary product images (hover state) disabled on touch devices
- "Quick Add" button on product cards becomes "Select Options" link on mobile to avoid accidental taps

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (secondary image reveal, shadow elevation) could not be reliably extracted from static CSS
- Error states for form validation (inline error messages, field-level error icons) were not visible in the extracted styles
- Dark mode or high-contrast mode variants are not present in the current design system
- Sub-brand or collection-specific color palettes (e.g., "Bamboo Collection", "Percale Collection") may exist but were not detectable
- Animation timing and easing curves (transition durations, spring animations, scroll behavior) are not captured
- Focus ring styles for keyboard navigation (outline color, offset, width) are not explicitly defined
- Loading states (skeleton screens, spinner designs, progress indicators) are not represented
- Modal and overlay designs (lightbox, cart drawer, size guide) lack specific styling details
- Print stylesheet behavior is unknown
- RTL (right-to-left) language support is not confirmed
- Custom checkbox and radio button styles (used in filters and product options) were not fully extractable
- Tiered pricing or sale price formatting (strikethrough, percentage off) needs visual confirmation
- Mobile swipe gestures (product carousels, image galleries) are not documented in the design tokens
