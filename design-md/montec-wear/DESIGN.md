---
version: alpha
name: "Montec Wear"
source_url: "https://www.montecwear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-contrast alpine brand that uses a deep #121212 ink against a #e9e9e8 canvas, punctuated by a sharp #ad1519 red that appears on every product badge, sale marker, and primary CTA. The system runs Manrope at clean weights — display sits at 28px weight 600 rather than the heavy 700+ that outdoor brands typically use, letting the product photography and snow-spray action shots carry the drama. Three distinct reds (#ad1519, #de0000, #cf2734) create a layered urgency system: the deepest red for primary actions, the brightest for sale badges, and the mid-tone for hover states. The palette is anchored by a surprising #fabd00 marigold accent that appears on "NEW" tags and seasonal callouts — a warm voltage against the cool grays (#d0cecb, #6e7075) that form the structural grid. Button shapes use {rounded.sm} (8px) for a purposeful, not precious, feel — this is gear for motion, not a lifestyle feed. The nav bar runs full-bleed at 80px with the logo left-aligned and a cart icon that pulses the primary red when items are added. Product cards stack on a white surface with a {rounded.md} (12px) corner and a 1px hairline in #d0cecb, keeping the focus on the athlete in motion. The footer collapses to a single column on mobile, with the brand's Japanese market presence (the site title reads in katakana) reflected in a bilingual legal line.

colors:
  primary: "#ad1519"
  primary-active: "#c11123"
  primary-disabled: "#e0e0e0"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6e7075"
  muted-soft: "#9a9a9a"
  hairline: "#d0cecb"
  hairline-soft: "#e0e0e0"
  canvas: "#e9e9e8"
  surface-soft: "#f0f2f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fabd00"
  accent-marigold-bright: "#fddb21"
  badge-red: "#de0000"
  badge-red-alt: "#cf2734"
  sale-red: "#de0c39"
  sale-red-alt: "#ef303f"
  sale-red-dark: "#d80f1e"
  navy: "#192f8e"
  navy-dark: "#0f2e6b"
  navy-deep: "#00437a"
  green: "#009343"
  green-whatsapp: "#25d366"
  blue-link: "#3172da"
  blue-link-hover: "#2b76ca"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Manrope', 'Manrope Fallback', inherit, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-circle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    padding: "0 {spacing.xl}"
  top-nav-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.base}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px {spacing.md}"
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "8px {spacing.md}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  product-badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  product-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  product-badge-best-seller:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  price-display-sale:
    typography: "{typography.title-md}"
    textColor: "{colors.sale-red}"
  price-display-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px {spacing.md}"
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: "8px {spacing.md}"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.surface-card}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.surface-card}"
    textTransform: uppercase
    letterSpacing: 1px
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px {spacing.md}"
    height: 44px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-icon-active:
    textColor: "{colors.primary}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.md} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  social-icon:
    textColor: "{colors.muted-soft}"
    height: 20px
  social-icon-hover:
    textColor: "{colors.surface-card}"
    height: 20px
  payment-icon:
    textColor: "{colors.muted-soft}"
    height: 24px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site, using the deepest #ad1519 red on a white canvas. On hover, shifts to #c11123 for a subtle darkening that signals interactivity without animation. Disabled state drops to #e0e0e0 background with #6e7075 text, used only when size/color selections are incomplete. All primary buttons use {rounded.sm} (8px) — purposeful corners that reference outdoor gear hardware rather than pill shapes.

**`button-secondary`** — An outlined alternative with a 2px #121212 border on white background. Used for "Add to Wishlist" and "Size Guide" actions that sit alongside the primary CTA. Active state fills the background with #f0f2f3. The border weight keeps it visually balanced against the solid primary button at the same 44px height.

**`button-sale`** — A high-urgency variant using #de0c39 for clearance and flash-sale CTAs. Shares the same dimensions as `button-primary` but uses a brighter, more saturated red to create visual hierarchy on sale pages. Never used alongside the primary red to avoid confusion.

**`button-marigold`** — A warm accent button using #fabd00 with dark #121212 text. Reserved for seasonal campaigns, "Shop New Arrivals" CTAs, and the newsletter signup. The high contrast ratio (yellow on dark text) meets accessibility requirements while providing a tonal break from the red system.

### Navigation
**`top-nav`** — Full-bleed 80px bar on #e9e9e8 canvas. Logo sits left-aligned with a 32px xl spacing from the edge. Navigation links use uppercase Manrope at 14px weight 500 with 0.5px letter spacing — a technical, gear-catalog feel. The cart icon sits right-aligned with a `cart-badge` overlay that appears on item add. On mobile, the nav collapses to 64px with a hamburger menu and the logo centered.

**`nav-link-active`** — Uses the primary #ad1519 red for the current page or section. No underline or background change — the color shift alone signals state, keeping the nav clean.

**`category-strip`** — A horizontal scrollable strip below the hero, used for product category filters (Jackets, Pants, Accessories). Active tab gets a 2px bottom border in primary red. Inactive tabs sit in #6e7075 muted. On mobile, the strip scrolls horizontally with hidden scrollbars.

### Cards
**`product-card`** — White surface with 1px #d0cecb border and {rounded.md} (12px) corners. The product image fills the top 60% of the card with no padding — the athlete or product is cropped edge-to-edge. Below the image, the product name, a color swatch strip, and the price stack with {spacing.sm} gaps. On hover, the border shifts to primary red and a subtle box shadow lifts the card 4px.

**`product-badge-*`** — A set of four badge variants that overlay the top-left corner of product images. Each uses {rounded.xs} (4px) and uppercase 11px weight 700 type. The marigold badge signals "NEW", the red badge signals "SALE", the gray badge signals "SOLD OUT", and the navy badge signals "BEST SELLER". Badges sit 8px from the card edge with 2px horizontal padding.

### Forms
**`text-input`** — Standard input with 1px #d0cecb border and {rounded.sm} (8px). On focus, the border thickens to 2px and shifts to primary red. The placeholder text uses #6e7075 at 14px weight 400. Error state (not fully extracted) likely uses a red border with error text below.

**`size-selector`** — A grid of pill-shaped buttons for size selection (S, M, L, XL). Inactive state uses white background with gray border. Active state fills the button with #121212 ink and white text. The grid uses 4-column layout on desktop, 3-column on mobile.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking the quantity number. Uses #f0f2f3 background with {rounded.sm} (8px). The buttons are 40px square with centered icons.

### Footer
**`footer-section`** — A full-bleed #121212 ink section with white text. Columns stack in a 4-column grid on desktop, collapsing to 2-column on tablet and single-column on mobile. Each column has a uppercase heading with 1px letter spacing. Links use #9a9a9a muted-soft and shift to white on hover. The newsletter input sits in the first column with a red submit button.

**`social-icon`** — Social media icons (Instagram, YouTube, TikTok) in #9a9a9a at 20px height. On hover, shift to white. The icons sit in a row at the bottom of the footer, above the legal line.

### Hero
**`hero-section`** — A full-width section with a background image that bleeds edge-to-edge. The overlay uses a 30% black scrim for text readability. The headline uses `display-xl` (28px weight 600) centered on desktop, left-aligned on mobile. A single `hero-cta` button sits below the headline with 48px height and 32px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to 64px with hamburger menu; product cards go single-column; hero headline drops to 22px; footer collapses to single column; size selector goes 3-column; category strip becomes horizontally scrollable |
| Tablet | 744–1128px | Top nav stays at 80px; product cards in 2-column grid; footer in 2-column layout; hero headline at 24px; category strip shows 4-5 visible tabs |
| Desktop | 1128–1440px | Full 4-column product grid; 4-column footer; hero headline at 28px; category strip shows all tabs; side-by-side product detail layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid expands to 5-column for certain categories; hero image scales with viewport |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Icon buttons use 40px x 40px touch targets
- Size selector pills are minimum 40px x 40px
- Quantity selector buttons are 40px square
- Cart icon has 44px x 44px invisible touch area

### Collapsing Strategy
- Top nav: hamburger menu replaces full link set below 744px
- Product grid: 4-column → 2-column → 1-column
- Footer: 4-column → 2-column → single-column stack
- Hero: centered text → left-aligned text; CTA button becomes full-width
- Category strip: horizontal scroll with hidden scrollbar on mobile
- Product detail: side-by-side (image + info) → stacked (image above info)
- Accordion: all sections expanded on desktop, collapsed on mobile with tap-to-expand

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text links were inferred from common patterns; exact color transitions not extracted
- Error styling for form inputs (red border, error message typography) not present in extracted data
- Focus ring styles (outline color, offset, width) not captured
- Dark mode palette not implemented on the live site; no extraction available
- Sub-brand or collection-specific palettes (e.g., "Montec Pro" or "Montec Women") not distinguished
- Loading states (spinner colors, skeleton screen colors) not extracted
- Modal/dialog overlay opacity and animation timing not captured
- Dropdown menu styling (background, shadow, item hover) not present in extraction
- The extracted color list is heavily weighted toward grays and reds with several blues (#3172da, #2b76ca, #192f8e, #0f2e6b, #00437a) that may represent link colors, social icons, or sub-brand accents rather than core palette — the true primary is the most distinctive red (#ad1519) which appears consistently across badges and CTAs
- The green (#009343) and WhatsApp green (#25d366) likely represent checkout/social integrations rather than brand colors
- Animation durations and easing curves not extracted
- Typography hierarchy beyond the extracted Manrope family is inferred from common outdoor brand patterns; exact sizes and weights may vary
- The site title includes Japanese text suggesting a bilingual or international market presence, but the design system does not include a secondary font for CJK characters
