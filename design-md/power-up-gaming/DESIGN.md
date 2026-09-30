---
version: alpha
name: "Power Up Gaming"
source_url: "https://powerupgaming.ca"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A retro game retailer that wears its primary red (#cc0000) like a neon sign above a brick-and-mortar arcade — the same red that fills the browser tab bar, powers every primary CTA, and marks sold-out badges on product cards. The palette is a deliberate clash of gaming-era accents: a deep teal (#108474) for secondary buttons and navigation bars, a royal blue (#000d8d) for footer backgrounds and informational banners, and a marigold (#ffbd00) that flashes on sale tags and limited-stock indicators. The canvas is a warm off-white (#f9fafb) rather than pure white, giving the storefront the patina of a well-loved game shop rather than a sterile e-commerce template. Figtree, a geometric sans-serif with a friendly, slightly condensed character, runs at 400 weight for body copy and jumps to 600 for headings and buttons — never heavy, never aggressive, matching the approachable tone of a store that wants to help you find that missing cartridge. Corners are soft but not pill-shaped: buttons use {rounded.sm} (8px), product cards use {rounded.md} (12px), and the search bar uses {rounded.lg} (20px), creating a consistent radius hierarchy that feels playful without tipping into toy-like. The layout is a dense grid of product thumbnails, each with a bold price tag and stock badge, mimicking the visual density of a physical display case. The overall effect is a digital storefront that feels like a physical destination — warm, cluttered in a curated way, and unmistakably red.

colors:
  primary: "#cc0000"
  primary-active: "#a30000"
  primary-disabled: "#f0b3b3"
  ink: "#222021"
  body: "#4a4a4a"
  muted: "#7b7b7b"
  muted-soft: "#a9a9a9"
  hairline: "#dbdbdb"
  hairline-soft: "#e8e8e8"
  canvas: "#f9fafb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-blue: "#000d8d"
  accent-gold: "#ffbd00"
  accent-gold-light: "#fbcd0a"
  accent-purple: "#8533fc"
  badge-sold-out: "#800000"
  badge-in-stock: "#1c7b36"
  star-rating: "#ffce33"
  footer-bg: "#000d8d"
  nav-bg: "#108474"

typography:
  display-xl:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  price-md:
    fontFamily: "'Figtree', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 700
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
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "#0a6b5c"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.accent-teal}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.15)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-md}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-in-stock:
    backgroundColor: "{colors.badge-in-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  hero-banner:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.base} 0"
  category-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  category-tab-active:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 14px"
    height: 40px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 14px"
    height: 40px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  cart-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The store's main call-to-action, filled with primary red (#cc0000) and white text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, darkens to `{colors.primary-active}` (#a30000). When disabled, fades to a pale pink `{colors.primary-disabled}` (#f0b3b3) with white text, signaling the action is unavailable. The 8px radius (`{rounded.sm}`) keeps the button feeling approachable without being overly rounded.

**`button-secondary`** — A teal-filled alternative (`{colors.accent-teal}`) used for secondary actions like "View Details", "Browse More", and navigation prompts. Shares the same dimensions and radius as the primary button, maintaining visual consistency across the action hierarchy. Active state darkens to #0a6b5c.

**`button-outline`** — A ghost button with a 2px hairline border and transparent fill, used for less prominent actions like "Cancel", "Clear Filters", or "Learn More". On hover, the border darkens to `{colors.muted}` and the background takes a subtle `{colors.surface-soft}` fill.

**`button-gold`** — A high-visibility accent button filled with marigold (`{colors.accent-gold}`) and dark ink text, reserved for sale promotions, limited-time offers, and premium callouts. The gold against the red/teal palette creates a distinct promotional voltage.

**`button-sm`** — A compact version of the primary button at 36px height, used for inline actions like "Apply" on filter bars, "Subscribe" in newsletter forms, and quick-add buttons on product cards.

### Navigation
**`nav-bar`** — A fixed-height teal bar (`{colors.nav-bg}`) spanning the full viewport width. Logo sits left-aligned, navigation links are center-aligned, and the cart icon with badge sits right-aligned. When scrolled, a subtle box shadow drops in to separate the nav from the page content. The teal provides a calm, trustworthy anchor against the energetic red of the primary actions below.

**`nav-link`** — Navigation items in white with 15px Figtree at 600 weight. Each link has 8px horizontal padding and an 8px radius hover state that adds a semi-transparent white overlay, creating a subtle backlit effect. Active links (current page) get a stronger 15% white overlay.

**`mobile-menu-toggle`** — A transparent button with a hamburger icon in white, shown only below 744px. Tapping opens a full-screen overlay menu with the same teal background and stacked navigation links.

### Cards
**`product-card`** — The core product display unit: a white card with a 12px radius (`{rounded.md}`), a subtle box shadow, and 16px internal padding. The card contains a square aspect-ratio product image with 8px radius, the product title in 16px/600 weight, the price in 18px/700 weight in primary red, and a stock badge (sold-out or in-stock) overlaid on the image. On hover, the shadow deepens to create a subtle lift effect.

**`badge-sold-out`** — A small maroon (`{colors.badge-sold-out}`) pill with white uppercase text, overlaid on product images to indicate unavailability. Uses 4px radius (`{rounded.xs}`) for a tight, label-like appearance.

**`badge-in-stock`** — A green (`{colors.badge-in-stock}`) pill indicating available inventory, using the same dimensions and typography as the sold-out badge. The green provides immediate positive feedback against the red-heavy palette.

**`badge-sale`** — A gold (`{colors.accent-gold}`) pill with dark text, used to flag discounted items. The gold creates a promotional urgency distinct from the stock-status badges.

### Forms
**`text-input`** — Standard text fields with a white background, 1px hairline border, 8px radius, and 44px height. On focus, the border thickens to 2px and turns primary red, providing clear focus indication. Used for search filters, newsletter signup, and checkout forms.

**`search-bar`** — A wider, more prominent input with 20px radius (`{rounded.lg}`), giving it a friendly, exploratory feel. On focus, the border shifts to teal (`{colors.accent-teal}`) rather than red, creating a subtle distinction between search and form inputs.

### Footer
**`footer`** — A deep blue (`{colors.footer-bg}`) full-width section with white text, containing store information, link columns, and social icons. Links are set at 80% opacity by default, shifting to full opacity on hover. The blue provides a visual bookend opposite the teal navigation bar, framing the page content between two saturated color blocks.

### Hero
**`hero-banner`** — A full-width teal section with large display typography and a gold call-to-action button. Used on the homepage and category landing pages to announce sales, new arrivals, or featured collections. The teal background provides a calm, authoritative canvas for the gold CTA to pop against.

### Category Strip
**`category-tab`** — Pill-shaped filter tabs (full radius) in a horizontally scrollable strip below the hero. Inactive tabs have a soft gray background with body text; active tabs switch to teal fill with white text. The pill shape creates a tactile, tag-like browsing experience.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), hamburger menu replaces nav links, hero banner reduces to 48px padding, search bar collapses to icon-only, category strip becomes horizontally scrollable with snap points |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero banner at 32px padding, search bar full-width but shorter, category strip shows 4-5 visible tabs |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero banner at 64px padding, search bar with placeholder text, category strip shows 6+ visible tabs |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero banner with background pattern, additional whitespace around product cards |

### Touch Targets
- All buttons and interactive elements maintain minimum 44x44px touch target (exceeds WCAG 2.1 AA)
- Product cards have full-area tap targets (no dead zones within card bounds)
- Category strip tabs are minimum 40px tall with 8px gaps between them
- Mobile menu toggle is 44x44px minimum
- Cart icon button is 40x40px with 4px internal padding

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Secondary navigation (category strip) collapses to horizontal scroll below 744px
- Footer link columns collapse to single column below 744px, with accordion-style expand/collapse for each section
- Product filters collapse to a single "Filter" button that opens a slide-out panel below 744px
- Hero banner image collapses to a smaller aspect ratio on mobile (16:9 → 4:3)
- Search bar collapses to icon-only on mobile, expanding to full-width on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns rather than extracted from the live site — actual implementations may vary
- Error state styling for form inputs (validation colors, error messages) was not extractable from the provided data
- Dark mode is not present on the live site and was not designed for
- The exact font weight hierarchy for Figtree (400 vs 500 vs 600) was inferred from common usage — the live site may use different weight combinations
- Product card hover animations (scale, shadow depth) were not extractable — current values are best guesses
- The checkout flow uses Shopify's default styling, which may override some brand tokens (Shopify Pay button colors, form layouts)
- Star rating component color (#ffce33) was extracted but its exact usage context (reviews, product ratings) was inferred
- Mobile navigation animation timing and transition curves were not extractable
- The extracted color list includes many grays and neutrals that may be framework defaults rather than intentional brand choices — the primary accent colors (red, teal, blue, gold) are the most reliable brand signals
- No data was available for loading states, skeleton screens, or empty-state illustrations
- The exact spacing scale was inferred from common e-commerce patterns — the live site may use different increments
