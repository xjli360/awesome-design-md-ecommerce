---
version: alpha
name: "Nest New York"
source_url: "https://www.nestnewyork.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sanctuary of understated luxury, Nest New York's digital presence mirrors the quiet sophistication of its candles and home fragrances. The palette is anchored in warm, tactile neutrals — {colors.canvas} (#f1eee7) and {colors.surface-soft} (#f9f7f2) — that feel like raw linen or aged parchment, creating a hushed, residential atmosphere. Against this soft backdrop, the brand's signature blue, {colors.primary} (#1990c6), appears sparingly but with purpose: on primary CTAs, navigation links, and product badges, it reads as a breath of fresh air rather than a hard sell. A secondary accent, {colors.accent-rose} (#e2c2bc), whispers warmth into sale tags and promotional banners, while the deep charcoal of {colors.ink} (#121212) grounds body text and product titles with quiet authority. Typography is set in Gotham, a geometric sans-serif that balances approachability with precision — display sizes at 26px feel generous but never shouty, and body copy at 14px with generous line-height keeps reading effortless. Corners are softly rounded ({rounded.sm} 8px on buttons, {rounded.md} 12px on cards), avoiding the harshness of sharp edges while maintaining a clean, modern silhouette. The overall effect is one of curated calm: a space that invites browsing, lingers on product photography, and trusts the scent — not the interface — to sell.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#b0d4e8"
  ink: "#121212"
  body: "#4b4a49"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#e3ded5"
  canvas: "#f1eee7"
  surface-soft: "#f9f7f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#e2c2bc"
  accent-rose-soft: "#f0e0dc"
  badge-sale: "#e2c2bc"
  badge-new: "#1990c6"
  star-rating: "#121212"
  scrim: "#000000"
  footer-bg: "#4b4a49"
  footer-text: "#f1eee7"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.hairline}"
  button-rose:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 3px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.2
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.footer-text}"
    marginBottom: "{spacing.sm}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "{spacing.sm} 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: 1px solid "{colors.hairline}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Subscribe". Rendered in the brand's signature blue {colors.primary} (#1990c6) with white text and soft 8px rounded corners. On hover, it deepens to {colors.primary-active} (#136f99). The disabled state uses a lighter blue {colors.primary-disabled} (#b0d4e8) to signal inactivity. All buttons use uppercase Gotham at 13px with 0.5px letter-spacing for a refined, editorial feel.

**`button-secondary`** — A ghost button for less prominent actions like "Continue Shopping" or "View Details". Uses the warm canvas background {colors.canvas} (#f1eee7) with dark ink text. The outline variant adds a 1px hairline border {colors.hairline} (#dedede) for visual separation. Hover state adds a subtle shadow.

**`button-rose`** — A promotional accent button used for sale items or limited-time offers. Uses the soft rose {colors.accent-rose} (#e2c2bc) background, creating a warm, inviting contrast against the primarily blue-and-neutral palette. Text remains dark for readability.

### Cards
**`product-card`** — The primary product display component, used on collection pages and search results. A white card with 12px rounded corners, housing a product image (rounded top corners only), a title in 14px Gotham medium, and a price in 14px body weight. The card sits on the warm canvas background {colors.canvas} (#f1eee7), creating a subtle floating effect. Hover state adds a gentle elevation shadow.

**`hero-banner`** — Full-width promotional banner at the top of the homepage and key landing pages. Uses the soft surface background {colors.surface-soft} (#f9f7f2) with a dark scrim overlay at 20% opacity to ensure text readability over background imagery. Display text uses 26px Gotham medium for a calm, confident headline.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, using the warm canvas background {colors.canvas} (#f1eee7). Navigation links are uppercase Gotham at 13px with 0.5px letter-spacing, matching the button typography for consistency. On scroll, a subtle 1px shadow appears at the bottom. The logo sits centered or left-aligned, with cart and search icons on the right.

**`search-bar`** — A pill-shaped search input with full border-radius, using a white card background and 1px hairline border. The placeholder text uses body-sm typography. On focus, the border transitions to the primary blue {colors.primary} (#1990c6).

### Forms
**`text-input`** — Standard text input for forms (email signup, address, etc.). Uses the warm canvas background with 1px hairline border and 8px rounded corners. On focus, the border switches to the primary blue. Height is 48px for comfortable touch interaction.

**`quantity-selector`** — A compact input for adjusting cart quantities, with a 44px height and 8px rounded corners. Uses a white background with hairline border, with plus/minus buttons on either side.

### Footer
**`footer`** — A dark footer section using {colors.footer-bg} (#4b4a49) with light text {colors.footer-text} (#f1eee7). Links use 12px Gotham regular with generous line-height. Section headings use 14px Gotham medium. The footer includes columns for customer service, about, and social links, with a newsletter signup form.

### Badges
**`badge-new`** — A small blue badge for new products, using the primary blue {colors.primary} (#1990c6) with white uppercase text at 10px. Padding is tight (2px 6px) with 4px rounded corners.

**`badge-sale`** — A rose-colored badge for sale items, using {colors.accent-rose} (#e2c2bc) with dark text. Same sizing and typography as the new badge, but the warm rose color signals promotion without the urgency of a traditional red.

### Accordion
**`accordion`** — Used for product descriptions, FAQ sections, and filter panels. A white container with 8px rounded corners and generous padding. The header uses title-sm typography (14px Gotham medium) with a chevron icon that rotates on expand. Content area uses body-md typography (15px) with comfortable line-height for reading.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero-banner height reduces to 250px; search-bar moves to full-width below nav; footer columns stack; accordion becomes default for all collapsible sections |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (Logo, Shop, About, Search, Cart); hero-banner height at 350px; footer shows 2-column layout; search-bar remains in nav |
| Desktop | 1128–1440px | Full three-column product grid; complete nav-bar with all links; hero-banner at full 400px height; footer shows 4-column layout; search-bar in nav with expanded width |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product grid can show 4 columns; hero-banner content centered with generous whitespace; all components scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Nav-bar links have 48px touch targets even when text is smaller
- Quantity selector buttons are 44x44px minimum
- Product card tap targets (image, title, price) are full card width
- Accordion headers are 48px minimum height for easy tapping

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer columns collapse to a single column with accordion-style headers on mobile
- Search bar transitions from inline to full-width overlay on mobile
- Product image galleries collapse from thumbnail strip to single-image swipe on mobile
- Cart sidebar becomes a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text links could not be reliably extracted (likely a subtle opacity or color shift)
- Error state styling for form inputs (border color, error message typography) was not visible in the extracted data
- Active/focus ring styles for keyboard navigation are not documented (likely a 2px primary-blue outline)
- Dark mode preferences are not supported — the brand uses only the warm light palette
- Sub-brand or seasonal palette variations (holiday, limited edition) are not captured
- Loading states and skeleton screen patterns were not observed
- Toast/notification component styling is undocumented
- Modal/dialog overlay specifications (width, animation, scrim opacity) are inferred from common patterns
- Dropdown menu styling (mega menu, country selector) was not fully extractable
- Animation timing and easing curves are not specified (likely 200-300ms ease-in-out)
