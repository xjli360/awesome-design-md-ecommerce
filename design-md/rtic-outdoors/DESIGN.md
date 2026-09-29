---
version: alpha
name: "RTIC Outdoors"
source_url: "https://rticoutdoors.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the tension between extreme durability and approachable value, where the primary voltage is a burnt-orange #ef8114 — the color of a well-used camp stove or a desert sunset — that punches through a landscape of cool grays (#f5f6f6, #c6c4ba, #555555) and near-blacks (#1f1f1f, #222222). The palette reads as industrial but not cold: the warm accent appears on CTAs, price tags, and badge elements, while the body grid stays in a neutral zone of #f2f2f2 canvases and #ededed surfaces. Typography runs Brut Grotesque at display sizes — a geometric sans with squared-off terminals that echoes the hard corners of a rotomolded cooler — paired with Francisco for body copy. Buttons use {rounded.sm} corners, while product cards and modals take {rounded.md} to soften the industrial edge just enough for e-commerce comfort. The brand's secondary accent palette is unusually broad for outdoor gear: a safety-orange #db6300, a deep red #bb3a1e, a muted olive #737a4e, and a surprising maroon #471c36 that appears in footer and sub-brand treatments. This is not a minimalist system — it's a working brand with multiple voices, from the loud "SALE" badge in #ef8114 to the quiet #79776f of secondary metadata.

colors:
  primary: "#ef8114"
  primary-active: "#db6300"
  primary-disabled: "#d3d3d3"
  ink: "#1f1f1f"
  body: "#393939"
  muted: "#555555"
  muted-soft: "#79776f"
  hairline: "#c6c4ba"
  hairline-soft: "#d3d3d3"
  canvas: "#f5f6f6"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#db6300"
  accent-red: "#bb3a1e"
  accent-red-deep: "#cb3f00"
  accent-olive: "#737a4e"
  accent-maroon: "#471c36"
  accent-gold: "#ffb800"
  accent-sage: "#a4c781"
  accent-sand: "#d2a97a"
  accent-blue: "#97c7ff"
  accent-navy: "#1c3c6b"
  badge-sale: "#ef8114"
  badge-new: "#737a4e"
  star-rating: "#ffb800"
  footer-bg: "#222222"
  footer-text: "#bbbbbb"

typography:
  display-xl:
    fontFamily: "'Brut Grotesque', 'FKScreamer', 'Francisco', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brut Grotesque', 'FKScreamer', 'Francisco', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Brut Grotesque', 'FKScreamer', 'Francisco', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Brut Grotesque', 'FKScreamer', 'Francisco', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brut Grotesque', 'FKScreamer', 'Francisco', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Francisco', 'Brut Grotesque', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Francisco', 'Brut Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Francisco', 'Brut Grotesque', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Francisco', 'Brut Grotesque', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Brut Grotesque', 'FKScreamer', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Brut Grotesque', 'FKScreamer', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Brut Grotesque', 'FKScreamer', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Francisco', 'Brut Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brut Grotesque', 'FKScreamer', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Brut Grotesque', 'FKScreamer', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Brut Grotesque', 'FKScreamer', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.accent-red}"

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-outline-orange:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-outline-orange-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(31, 31, 31, 0.4)"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-tile-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.surface-card}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  newsletter-input:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.muted}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    height: 40px
    width: 40px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, filled with the brand's signature burnt-orange #ef8114. Used for "Add to Cart", "Shop Now", and primary purchase actions. On hover, shifts to the deeper #db6300 (`primary-active`). Disabled state drops to #d3d3d3 with muted text, signaling unavailability without confusion. All primary buttons use {rounded.sm} (4px) — a slight softening of the brand's otherwise squared-off industrial language.

**`button-secondary`** — An outlined button with a 2px #1f1f1f border on a white canvas. Used for "Learn More", "View Details", and secondary actions that need equal visual weight without the orange voltage. Active state fills the background with #f2f2f2. The border weight ensures legibility against product photography.

**`button-outline-orange`** — A transparent button with a 2px orange border, used for "Customize" and "Build Your Own" flows where the orange needs to signal interactivity without overwhelming the product image. Active state fills solid orange, inverting the relationship.

**`button-pill`** — Fully rounded pill shape used for filter chips, category toggles, and mobile navigation items. Smaller padding and font size (13px) allow dense horizontal layouts. The pill shape is a deliberate departure from the system's mostly squared corners — it signals "filter/toggle" as a distinct interaction mode.

### Cards
**`product-card`** — The primary content container for the product grid. White background with 8px rounded corners and 16px padding. Each card contains an image (4px rounded), title, price, and optional badge. Cards sit on the #f5f6f6 canvas, creating a subtle elevation effect. The badge system uses two variants: `product-card-badge` (orange for sale) and `product-card-badge-new` (olive #737a4e for new arrivals), both with uppercase 11px type and tight 2px padding.

**`category-tile`** — Larger, more visual tiles used for department navigation (Coolers, Drinkware, Totes, etc.). Soft gray background (#f2f2f2) that inverts to orange when active/selected. These tiles carry the brand's category taxonomy and often include an icon or small product image above the title.

### Navigation
**`top-nav`** — A 64px fixed bar on the #f5f6f6 canvas with a single hairline bottom border (#c6c4ba). Navigation links are uppercase 14px Brut Grotesque with 0.5px letter-spacing — a deliberate choice that reads as technical and precise rather than friendly. The active link state drops a 2px orange underline. The nav includes the RTIC logo (left), category links (center), and utility icons (search, account, cart — right).

**`nav-link`** — Uppercase, 14px, weight 600, with 8px vertical padding for comfortable tap targets. The uppercase treatment is a signature move — it appears throughout the system on buttons, badges, and navigation, creating a consistent voice of directness.

### Forms
**`text-input`** — Standard form input with 1px hairline border, 4px rounded corners, and 44px height for comfortable touch interaction. Focus state swaps to a 2px orange border — the only place in the system where orange appears on a form element. Error state uses the deep red #bb3a1e border.

**`search-bar`** — Slightly wider rounded corners (8px) than standard inputs, distinguishing the search affordance from form fields. 44px height matches the button system for visual alignment in search+button combinations. Focus state mirrors the text-input pattern with 2px orange border.

**`newsletter-input`** — A dark variant for the footer, using #1f1f1f background with #bbbbbb text and a #555555 border. The submit button sits immediately adjacent in full orange, creating a high-contrast call-to-action pair against the dark footer.

### Footer
**`footer`** — A dark section (#222222 background) with light text (#bbbbbb) and white headings. Uses the brand's full section spacing (64px) for generous breathing room. Links are standard body weight, not uppercase — a deliberate relaxation of the system's nav-link voice. The newsletter component lives here as the primary conversion point below the fold.

### Accordion
**`accordion-header`** — Used for product specifications, FAQ sections, and mobile category menus. Soft gray background (#f2f2f2) with 12px/16px padding and a hairline bottom border. The accordion pattern is the brand's solution for information-dense pages without overwhelming the user — common on product detail pages with multiple spec categories.

### Filters
**`filter-chip`** — Pill-shaped toggle elements for product listing filters (size, color, capacity). White background with hairline border in inactive state, inverting to orange fill when active. The pill shape distinguishes filters from navigation links and buttons, creating a clear mental model for "temporary selection."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), hamburger nav replaces top-nav links, search collapses to icon-only, category tiles stack vertically, footer collapses to single column, accordion replaces multi-column layouts |
| Tablet | 744–1128px | Two-column product grid (2-up), top-nav shows 4-5 category links with overflow menu, search bar shortens but remains visible, category tiles show in 3-column grid, footer shows 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (3-up), full top-nav with all category links visible, search bar at full width, category tiles in 4-column grid, footer shows 4-column layout |
| Wide | > 1440px | Four-column product grid (4-up) with max-width container, same nav as desktop, hero banners expand to full viewport width, category tiles show in 5-column grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Icon buttons use 40px × 40px touch targets
- Filter chips use 32px minimum height with 14px horizontal padding
- Product card tap targets extend to full card area
- Mobile nav hamburger uses 48px × 48px target

### Collapsing Strategy
- Top-nav category links collapse into a hamburger menu below 744px
- Multi-column footer collapses to single column below 744px
- Product grid reduces columns progressively (4→3→2→1)
- Category tiles reduce columns (5→4→3→stacked)
- Search bar collapses to icon-only on mobile, expanding on tap
- Accordion replaces tabbed interfaces below 744px
- Hero banner text overlay reduces font size and padding on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components could not be reliably extracted — the above uses pattern inference from the primary-active color and standard accessibility practices
- Error states for forms (validation messages, error icons) were not observed in extracted data
- Dark mode preferences or alternate color schemes were not detected
- Sub-brand or collection-specific color variations (e.g., "RTIC Camo" or "RTIC Pro" lines) may have their own palettes not captured in the top-level extraction
- Animation and transition timing values (hover transitions, page load animations) were not extractable
- Modal/dialog styling (overlay opacity, close button placement) not observed
- Tooltip and popover styling not present in extracted data
- The font-family list includes "FKScreamer" and "Francisco" which appear to be custom or licensed typefaces — fallback stacks are provided but exact weights and styles may vary
- Star rating component uses #ffb800 gold but exact sizing and spacing between stars could not be determined
- The extracted color list is unusually large (30+ colors), suggesting multiple third-party widgets (reviews, payments, social) are polluting the palette — the brand's true system likely uses 8-12 core colors with the rest being widget-specific
- Checkout flow styling (Shopify Pay buttons, cart drawer) was not extractable from the provided data
- Accessibility contrast ratios between some color pairs (e.g., #79776f on #f5f6f6) should be verified against WCAG 2.1 AA standards
