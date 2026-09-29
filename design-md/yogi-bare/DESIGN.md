---
version: alpha
name: "Yogi Bare"
source_url: "https://www.yogi-bare.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, earth-bound palette anchored on #5b1d10 — a burnt umber that reads like sun-baked clay — and lifted by #ab8c52, a muted brass that catches light like a brass singing bowl. The brand’s canvas is #f5f2ec, a warm off-white that avoids the clinical chill of pure white, while #212121 provides the ink weight for body text and #2e2e2e for secondary copy. Typography pairs the clean, geometric Figtree (for UI and body) with the carved-wood serifs of PPWoodland (for display and hero headings) and the condensed MiletusGrotesk (for badges and small labels), creating a layered voice that moves between modern clarity and handcrafted warmth. Product cards use soft {rounded.md} corners on a #fcfbf9 surface, with price tags and “Eco” badges set in #ab8c52 on #f5f2ec backgrounds. The checkout flow introduces #00164d — a deep navy — as an accent for trust signals (Klarna, PayPal badges) and footer links, while #c65d52 (a dried-rose red) marks sale prices and limited-stock warnings. Buttons are pill-shaped ({rounded.full}) in the primary #5b1d10 with white text, and secondary buttons invert to a #f5f2ec fill with #5b1d10 text and a #ab8c52 border. The overall mood is grounded, warm, and materially honest — like a studio that smells of cork and cedar.

colors:
  primary: "#5b1d10"
  primary-active: "#a73210"
  primary-disabled: "#e8d4ae"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#636262"
  muted-soft: "#a09e99"
  hairline: "#d9d9d9"
  hairline-soft: "#ece7db"
  canvas: "#f5f2ec"
  surface-soft: "#f7f4ef"
  surface-card: "#fcfbf9"
  surface-warm: "#f0ebe2"
  accent-gold: "#ab8c52"
  accent-gold-light: "#e8d4ae"
  accent-brass: "#806430"
  accent-sand: "#b0a38b"
  accent-terracotta: "#c65d52"
  accent-navy: "#00164d"
  on-primary: "#ffffff"
  on-gold: "#f5f2ec"
  star-rating: "#ab8c52"
  badge-eco: "#9a7e4a"
  badge-sale: "#c65d52"

typography:
  display-xl:
    fontFamily: "'PPWoodland-Regular', 'PPWoodland-Light', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'PPWoodland-Regular', 'PPWoodland-Light', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'PPWoodland-Regular', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'MiletusGrotesk-Regular', 'MiletusGrotesk-Light', 'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'MiletusGrotesk-Regular', 'Figtree', sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.accent-gold}"
  button-secondary-active:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-gold}"
  text-input-error:
    border: "2px solid {colors.accent-terracotta}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.04)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.accent-gold}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.accent-gold-light}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.accent-gold-light}"
    rounded: "{rounded.full}"
    height: 32px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  badge-eco:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s burnt umber {colors.primary} with white text and a full pill shape. On hover, it deepens to {colors.primary-active} (#a73210) for a subtle but clear state change. The disabled state uses {colors.primary-disabled} (#e8d4ae) with {colors.muted} text, signaling unavailability without visual noise.

**`button-secondary`** — An outlined variant on the warm canvas background, using {colors.primary} text with a 2px {colors.accent-gold} border. On hover, the background shifts to {colors.surface-warm} and the border becomes {colors.primary}, creating a layered interaction. Used for “Add to Cart” alternatives and secondary navigation actions.

**`button-tertiary-text`** — A text-only button with no background or border, used for links like “View Details” or “Read More.” Color is {colors.primary} and the typography matches {typography.button-md} for consistency, but the padding is zero to allow inline placement.

**`button-pill-gold`** — A smaller, accent-driven pill button in {colors.accent-gold} with {colors.on-gold} text. Used for “Shop Now” prompts on collection pages and promotional banners. Typography is {typography.button-sm} to fit tighter spaces.

### Cards
**`product-card`** — The primary product display unit, a white card on {colors.surface-card} with a subtle box shadow (0 2px 8px rgba(0,0,0,0.04)). The image area has rounded top corners ({rounded.md}) and the content area (title, price, badges) sits below with {spacing.sm} padding. On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.08) for a gentle lift effect.

**`product-card-badge`** — A small uppercase label in {colors.accent-gold} on {colors.on-gold} background, using {typography.badge} (MiletusGrotesk at 11px). Used for “Eco,” “New,” or “Bestseller” tags. The sale variant uses {colors.accent-terracotta} on white for urgency.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on {colors.canvas} background, with a 1px bottom border in {colors.hairline-soft}. Navigation links use {typography.nav-link} (uppercase Figtree 14px) with {colors.muted} for inactive and {colors.ink} for active states. The active link has a 2px {colors.primary} bottom border.

**`nav-link-active`** — The selected navigation item, distinguished by {colors.primary} text and a 2px solid underline in the same color. The typography remains {typography.nav-link} for consistent alignment.

### Forms
**`text-input`** — A standard input field on {colors.canvas} with a 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border thickens to 2px and shifts to {colors.accent-gold}. Error state uses a 2px {colors.accent-terracotta} border. Height is 48px for comfortable touch targeting.

**`search-bar`** — A pill-shaped search field on {colors.surface-card} with a 1px {colors.hairline} border. On focus, the border becomes 2px {colors.accent-gold}. Used in the header and on collection pages for product discovery.

### Footer
**`footer-section`** — A full-width footer in {colors.primary} with white text. Links are set in {colors.accent-gold-light} (#e8d4ae) and shift to white on hover. Social icons are circular ({rounded.full}) at 32px with gold-light icons. The section padding is {spacing.xxl} top and bottom for generous breathing room.

### Badges
**`badge-eco`** — A small, uppercase badge in {colors.badge-eco} (#9a7e4a) with white text, used to highlight sustainable materials or certifications. Typography is {typography.badge} (MiletusGrotesk, 11px, uppercase) with {rounded.xs} corners and 2px 8px padding.

**`badge-sale`** — A sale or clearance badge in {colors.badge-sale} (#c65d52) with white text, same typography and sizing as the eco badge but with a higher-contrast, urgent color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards stack in single column; hero text reduces to {typography.display-lg}; buttons become full-width; footer links stack vertically |
| Tablet | 744–1128px | Nav-bar shows all links (no hamburger); product cards in 2-column grid; hero text at {typography.display-xl}; buttons remain inline |
| Desktop | 1128–1440px | Full layout: 3-column product grid, sticky nav-bar, hero with side-by-side image and text; search bar visible in header |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero section uses larger padding; footer columns spread horizontally |

### Touch Targets
- All buttons and interactive elements have a minimum height of 48px (buttons, inputs, nav links).
- Icon buttons (social icons, cart icon) are 32px minimum with 8px padding.
- Product card tap targets (title, price, badge) are at least 44px tall.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The footer’s multi-column layout collapses to a single vertical stack on mobile.
- Product filters (on collection pages) collapse into a “Filter” button that opens a modal overlay.
- The search bar collapses from a full input to a magnifying-glass icon that expands on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most components (buttons, cards, links) are inferred from common patterns; exact transition durations and easing curves were not extracted.
- **Error styling** for forms (validation messages, error icons) is not present in the extracted data; the error border color (#c65d52) is an assumption based on the brand’s accent palette.
- **Dark mode** is not supported on the live site; no dark-mode tokens are defined.
- **Sub-brand palettes** (e.g., “Yogi Bare Pro” or “Eco Essentials”) were not detected; all colors are from the main site.
- **Checkout-specific colors** (#00164d navy, #c65d52 red) may belong to third-party widgets (Shopify Pay, Klarna) rather than the brand itself; they are included as accents but should be verified.
- **Font weights** for PPWoodland and MiletusGrotesk are assumed based on available variants (Light, Regular); exact weight numbers (e.g., 300 vs 400) could not be confirmed.
- **Spacing values** for section padding and component margins are estimated from typical Shopify patterns; the extracted CSS did not include explicit spacing tokens.
- **Animation and transition** data (e.g., hover fade duration, card lift timing) is not available; a default 200ms ease-in-out is recommended for all interactive states.
