---
version: alpha
name: "Bigjigs Toys"
source_url: "https://www.bigjigstoys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A primary blue of #2ea3f2 — the color of a child's first clear sky drawing — anchors a playroom brand that refuses to shout. The palette is a wooden-toy rainbow: sage green (#7cc68d), lavender (#c37cc6), marigold (#edb059), and a single red alert (#e02b20) for sale badges and clearance markers. But the real design move is the canvas: #f7f7f7, not pure white, giving the site the soft warmth of unvarnished beechwood. Product photography floats on this off-white field with {rounded.md} corners, while category navigation runs in Montserrat at 400 weight — a sans-serif that reads as sturdy but not stern, like a well-sanded block. The brand's voice is "Creating perfect playrooms" — not "buy toys" but "build a space." CTAs use the blue primary on white text, with {rounded.sm} corners and 14px padding that feels substantial enough for a child's finger but not cartoonishly large. The footer collapses into a dense column of safety certifications, delivery promises, and small-print policies — the legal architecture of a brand that sells to cautious parents. Every badge (NEW, SALE, ECO) uses a distinct accent from the rainbow: #7cc68d for eco, #c37cc6 for new, #e02b20 for sale. The typography stack is Montserrat for headings and Open Sans for body — a pairing that balances geometric clarity with humanist readability, like a classroom blackboard next to a storybook.

colors:
  primary: "#2ea3f2"
  primary-active: "#0693e3"
  primary-disabled: "#8ed1fc"
  ink: "#313131"
  body: "#3e3e3e"
  muted: "#747d88"
  muted-soft: "#abb8c3"
  hairline: "#d9d9d9"
  hairline-soft: "#e2e2e2"
  canvas: "#f7f7f7"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#7cc68d"
  accent-lavender: "#c37cc6"
  accent-marigold: "#edb059"
  accent-red: "#e02b20"
  accent-red-dark: "#c41f18"
  accent-yellow: "#fcd21d"
  accent-orange: "#ff6900"
  accent-pink: "#f78da7"
  accent-teal: "#00d084"
  accent-blue-deep: "#003388"
  accent-gray: "#bcc8c9"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', 'Poppins', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    rounded: "{rounded.sm}"
    padding: 14px 28px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-accent-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
  button-accent-eco:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 3px {colors.primary-disabled}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.sm}"
  badge-new:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.surface-card}"
    fontWeight: 600
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    margin: "{spacing.lg} 0 0 0"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  category-tile-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "2px solid {colors.primary}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Basket", "Shop Now", and checkout entry points. Rendered in Montserrat 600 at 14px on a #2ea3f2 blue background with white text and {rounded.sm} corners. On hover, the background shifts to #0693e3 with a subtle scale(1.02) transform. Disabled state uses #8ed1fc with reduced opacity. Padding of 14px 28px gives the button a substantial, child-safe feel — large enough for small fingers but not cartoonishly oversized.

**`button-secondary`** — Outline variant for "Learn More", "View Details", and secondary actions. White background with a {colors.hairline} border and {colors.ink} text. Active state thickens the border to 2px solid {colors.ink} and shifts background to {colors.surface-soft}. Used alongside primary buttons to create visual hierarchy without competing for attention.

**`button-accent-sale`** — High-urgency badge-button for clearance and sale items. Uses {colors.accent-red} (#e02b20) background with white text and compact padding (10px 20px). Always paired with the `badge-sale` component. The red is the most saturated color in the palette — used sparingly to preserve its alert value.

**`button-accent-eco`** — Sustainability callout button for eco-friendly product lines. Uses {colors.accent-sage} (#7cc68d) background. Same sizing as the sale button but communicates positive reinforcement rather than urgency.

### Cards
**`product-card`** — The primary product display unit, a white card on {colors.canvas} with {rounded.md} corners and a subtle 1px shadow. The image occupies the top half with rounded top corners only, creating a clear boundary between photography and text. Title uses {typography.title-sm} (Montserrat 500, 16px) and price uses {typography.body-md} with 600 weight. On hover, the shadow deepens to 4px/12px and a slight translateY(-2px) lifts the card. No border — the card relies on shadow depth against the off-white canvas.

**`category-tile`** — Grid tile for department navigation (Wooden Toys, Puzzles, Arts & Crafts). Same card anatomy as product cards but with centered text and a hover state that adds a 2px {colors.primary} border. Used in the homepage category grid and sidebar navigation.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height on {colors.canvas} background. Logo sits left-aligned with a max-height of 40px. Navigation links use {typography.nav-link} (Montserrat 500, 14px) with 8px 12px padding and {rounded.xs} hover states. The active link uses {colors.primary} text on a {colors.surface-soft} background. On scroll, the nav gains a subtle box-shadow and the background shifts to solid white for contrast against page content.

**`nav-link`** — Individual navigation items with transparent background and {colors.ink} text. Hover state adds a light gray background ({colors.surface-soft}) and optional underline. Active/current page state uses {colors.primary} text color. No uppercase — the brand avoids shouting in navigation.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. White background with 1px {colors.hairline} border and {rounded.sm} corners. Focus state thickens the border to 2px {colors.primary} with a 3px outer glow in {colors.primary-disabled}. Error state uses 2px {colors.accent-red} border with a red error message below. Height of 48px ensures touch-friendly targets.

**`search-bar`** — Pill-shaped search input ({rounded.full}) used in the header and mobile navigation. Same dimensions as text-input but with fully rounded ends. Focus state adds a blue glow ring. The placeholder text reads "Search toys..." in {colors.muted-soft}.

### Badges
**`badge-new`** — Lavender (#c37cc6) badge for newly added products. Uppercase Montserrat 700 at 11px with 0.5px letter spacing. Compact 4px 8px padding with {rounded.xs} corners. Positioned absolutely on the top-left of product card images.

**`badge-sale`** — Red (#e02b20) badge for discounted items. Same typography and sizing as badge-new but with the brand's highest-contrast accent color. Always includes a percentage or "SALE" text.

**`badge-eco`** — Sage green (#7cc68d) badge for sustainable or FSC-certified products. Communicates environmental values without greenwashing — the color is muted enough to feel sincere.

**`badge-out-of-stock`** — Gray (#abb8c3) badge for unavailable items. Uses {colors.ink} text on the muted background. Positioned centrally over the product image with a slight opacity overlay.

### Footer
**`footer`** — Dark section at the bottom of every page, using {colors.ink} (#313131) background with white text. Organized in a 4-column grid on desktop collapsing to single column on mobile. Links use {colors.muted-soft} with hover to white. Includes brand trust signals: delivery information, safety certifications, payment icons, and social links. Padding of {spacing.xxl} top and bottom with {spacing.lg} horizontal.

### Hero
**`hero-banner`** — Full-width promotional banner on the homepage and category landing pages. Uses {colors.surface-soft} (#f4f4f4) background — a warm gray that doesn't compete with product photography. Headline uses {typography.display-lg} (Montserrat 600, 28px) with a single CTA button below. No carousel or animation — the brand trusts a single strong message. Padding of {spacing.section} (64px) vertical creates generous breathing room.

### Accordion
**`accordion-header`** — Used for product details, FAQ sections, and filter panels. Light gray background ({colors.surface-soft}) with {colors.ink} text in {typography.title-sm}. Includes a chevron icon that rotates on open state. Padding of {spacing.md} vertical and {spacing.base} horizontal.

**`accordion-content`** — Expandable panel below the header. White background with {colors.body} text in {typography.body-sm}. Padding of {spacing.base} all sides. Content can include bullet lists, product dimensions, or safety information.

### Quantity Selector
**`quantity-selector`** — Horizontal stepper for product page quantity selection. White background with 1px {colors.hairline} border and {rounded.sm} corners. Contains two square buttons (32x32px) with minus/plus icons and a centered text display. Buttons use {colors.surface-soft} background with {colors.ink} icons. Height of 40px keeps it compact alongside the add-to-basket button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item), hamburger nav replaces full nav-bar, footer collapses to stacked layout, hero banner reduces to 40px padding, search bar moves to sticky header, category tiles stack vertically, accordion becomes default for all filter panels |
| Tablet | 744–1128px | 2-column product grid, nav-bar shows condensed links (no dropdowns), footer uses 2-column grid, hero banner at 48px padding, category tiles in 3-column grid, search bar remains in header but collapses to icon on scroll |
| Desktop | 1128–1440px | 3-column product grid, full nav-bar with dropdowns, 4-column footer, hero banner at 64px padding, category tiles in 4-column grid, search bar always visible in header |
| Wide | > 1440px | 4-column product grid, max-width container at 1440px centered, nav-bar links have increased letter-spacing, hero banner at 80px padding, category tiles in 5-column grid, additional whitespace around all sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target per WCAG 2.1
- Product card tap targets extend to full card area on mobile
- Quantity selector buttons are 32x32px with 4px internal padding — meets 44px target through surrounding container
- Accordion headers are 48px minimum height
- Nav links have 8px padding on all sides, ensuring 30px+ touch area
- Badge tap targets are small (28px) but are never the sole interactive element — always paired with a card or button

### Collapsing Strategy
- Top navigation collapses to hamburger menu at < 744px, with full-height overlay drawer
- Footer grid collapses from 4-column to 2-column at tablet, single-column at mobile
- Product filters collapse to accordion panels on mobile, with a "Filter" button that opens a bottom sheet
- Category sidebar collapses to a horizontal scroll strip on mobile
- Hero banner reduces vertical padding from 64px to 40px on mobile
- Product image galleries collapse from thumbnail grid to single-image swipe on mobile
- Search bar collapses to icon-only on tablet scroll, expands to full bar on tap
- Multi-column product descriptions collapse to single-column accordion on mobile
- Trust badges (free shipping, secure checkout) collapse from inline to stacked on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for footer links, accordion headers, and category tiles were inferred from common patterns — actual hover transitions (color, duration, easing) not extracted from live site
- Error state styling for forms (text-input-error border color confirmed, but error message typography and icon placement not extracted)
- Focus-visible ring styles not confirmed — assumed 3px outline based on common accessibility patterns
- Dropdown menu styling for navigation (mega-menu vs simple dropdown, animation, z-index) not extracted
- Mobile hamburger menu animation, overlay opacity, and close button styling not confirmed
- Product card price formatting (currency symbol, decimal places, strikethrough for sale prices) not extracted
- Accordion animation duration and easing not confirmed
- Quantity selector icon SVGs (minus/plus) not extracted — assumed simple line icons
- Checkout flow styling (progress bar, payment form, order summary) not extracted — site does not appear to use Shopify
- Dark mode or high-contrast mode not supported — no media query found
- Sub-brand or seasonal color palettes not identified
- Loading states (skeleton screens, spinners) not extracted
- Toast/notification styling (success, error, info) not confirmed
- Print stylesheet behavior not verified
- The extracted color list is unusually large (30+ hexes) and includes many generic web palette colors (#00d084, #0693e3, #cf2e2e, etc.) that may be WordPress block editor defaults rather than intentional brand colors. The primary (#2ea3f2) and accent colors (#7cc68d, #c37cc6, #edb059, #e02b20) were selected as the most distinctive and frequently used across the site. The remaining hexes are documented in the colors block for reference but may not all be actively used in the design system.
