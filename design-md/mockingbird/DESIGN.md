---
version: alpha
name: "Mockingbird"
source_url: "https://hellomockingbird.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy (#223746) frames Mockingbird's entire experience — not as a background, but as the primary brand voltage that colors every button, badge, and interactive element, creating a sense of quiet confidence that's rare in the stroller category. Against this dark anchor, a warm marigold (#f6d381) appears sparingly as the accent that signals action: sale markers, star ratings, and highlight badges glow in this honeyed yellow, while a soft coral (#ea817f) and its paler sibling (#f1afa9) handle secondary accents like limited-edition labels and playful micro-interactions. The canvas stays clean at #ffffff with subtle surfaces at #f2f4f7 and #f7f7f7, letting product photography — strollers in lifestyle settings, detail shots of harness clips and fold mechanisms — carry the emotional weight. Typography runs on Jost for display and Freight Sans Pro for body, a pairing that mixes geometric modernity with warm humanist readability. Buttons use `{rounded.sm}` corners rather than pills, and cards use `{rounded.md}`, a slightly more structured feel that matches the product category's need for safety and precision. The nav bar sits at 80px with a sticky white background, and product cards stack three across on desktop with generous `{spacing.lg}` gutters. A distinctive purple (#805ad5) appears in the extracted palette — likely used for the "Single-to-Double" expandability feature badge and the brand's "Compare" tool — adding a surprising third accent that signals innovation and modularity. The overall mood is trustworthy and warm, a nursery-lit storefront rather than a sterile gear shop.

colors:
  primary: "#223746"
  primary-active: "#1b1c30"
  primary-disabled: "#2b3844"
  ink: "#171923"
  body: "#273745"
  muted: "#1f2c39"
  muted-soft: "#2b3844"
  hairline: "#e2e8f0"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f2f4f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#f6d381"
  accent-marigold-active: "#fdd174"
  accent-coral: "#ea817f"
  accent-coral-soft: "#f1afa9"
  accent-purple: "#805ad5"
  accent-purple-active: "#514be9"
  accent-purple-dark: "#322659"
  star-rating: "#f6d381"
  badge-sale: "#ea8180"
  badge-new: "#805ad5"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Freight Sans Pro', cronos-pro, 'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Freight Sans Pro', cronos-pro, 'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Freight Sans Pro', cronos-pro, 'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Freight Sans Pro', cronos-pro, 'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Freight Sans Pro', cronos-pro, 'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  price:
    fontFamily: "'Jost', 'Freight Sans Pro', cronos-pro, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
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
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  text-input-error:
    borderColor: "{colors.accent-coral}"
    textColor: "{colors.accent-coral}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4:3"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
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
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  search-bar-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.accent-marigold}"
  badge-feature:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-rating:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 {spacing.lg} {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and "Subscribe". Rendered in deep navy (#223746) with white text and `{rounded.sm}` corners. On hover, shifts to `button-primary-active` (#1b1c30) for a slightly darker state. Disabled state uses `button-primary-disabled` (#2b3844) at 50% opacity, signaling the button is present but unavailable. **`button-secondary`** — An outlined variant with a white background and navy text, used for "Learn More" and "Compare" actions. Active state fills with `surface-soft` (#f2f4f7) for a subtle press effect. **`button-accent-marigold`** — The warm yellow (#f6d381) button reserved for promotional CTAs like "Shop Sale" and "Bundle & Save". Uses dark ink (#171923) text for contrast. **`button-accent-purple`** — The purple (#805ad5) button used for the "Single-to-Double" expandability feature and the "Build Your Stroller" configurator. **`button-text-link`** — A text-only link styled as a button, used for "View Details" and "Read Reviews" in product cards. **`button-pill`** — A fully rounded pill variant used for filter tags and category toggles, with `{rounded.full}` and compact padding.

### Cards
**`product-card`** — The primary product display unit, a white card with `{rounded.md}` corners and `{spacing.base}` padding. Each card contains a 4:3 image with `{rounded.sm}`, a title in `title-sm`, and a price in the `price` token. On hover, a subtle shadow (`0 4px 16px rgba(0,0,0,0.08)`) lifts the card. Badges appear in the top-left corner using `product-card-badge` (marigold for general badges), `product-card-badge-sale` (coral for sale items), or `product-card-badge-new` (purple for new arrivals). Cards stack three across on desktop, two on tablet, and single-column on mobile with `{spacing.lg}` gaps.

### Navigation
**`nav-bar`** — A sticky white header at 80px on desktop, collapsing to 64px on scroll. Contains the brand logo (left), nav links (center), and utility icons (right: search, account, cart). Active links use `nav-link-active` with the primary navy color; inactive links use `nav-link-inactive` with a muted tone. The sticky variant adds a subtle `boxShadow` for visual separation. On mobile, the nav collapses into a hamburger menu with a full-screen overlay drawer.

### Forms
**`text-input`** — Standard text input with white background, `{rounded.sm}` corners, and `body-md` typography. On focus, a 2px navy ring (`boxShadow: 0 0 0 2px #223746`) appears. Error state uses `text-input-error` with coral (#ea817f) border and text. **`select-input`** — Matches text input styling for dropdown selects, used in product filters and checkout forms.

### Hero
**`hero-section`** — The full-width hero banner on the homepage and campaign pages. Background uses `surface-soft` (#f2f4f7) with `display-xl` typography. The primary CTA uses `hero-cta` with larger padding and a 56px height for visual prominence. Hero images are full-bleed with no rounded corners, creating a clean break from the card grid below.

### Badges
**`badge-feature`** — Purple (#805ad5) pill badges used to highlight key product features like "Single-to-Double" and "Travel System Compatible". Uses `{rounded.full}` for a friendly, approachable look. **`badge-rating`** — Marigold (#f6d381) badges for star ratings and review summaries, with compact padding and `caption-sm` typography.

### Footer
**`footer-section`** — A deep navy (#223746) footer with white text and marigold (#f6d381) headings. Links use `footer-link` with white text and underline on hover. The footer contains four columns: Shop, Support, Company, and Social. A secondary footer bar sits below with copyright and legal links.

### Accordion
**`accordion-header`** — Used in product details, FAQ sections, and the "Compare" tool. White background with `title-md` typography and generous padding. **`accordion-content`** — Expands below the header with `body-md` text and bottom padding only, creating a clean reveal animation.

### Dividers
**`divider`** — A 1px line using `hairline` (#e2e8f0) for separating sections. **`divider-soft`** — A lighter variant using `hairline-soft` (#dedede) for within-card separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `display-lg`; buttons go full-width; footer stacks to single column; search bar moves to overlay |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains `display-xl`; footer splits to two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at full width; footer in four columns |
| Wide | > 1440px | Max-width container at 1440px; product grid may expand to four columns; hero content centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons in the nav bar use 48px touch targets
- Product card CTAs are at least 48px tall
- Accordion headers are 56px tall for easy tapping

### Collapsing Strategy
- Nav bar: On mobile (< 744px), the full nav menu collapses into a hamburger icon; a full-screen overlay drawer opens with all links, search, and account options
- Product grid: Collapses from 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer: Collapses from 4 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Hero section: On mobile, the hero image may crop or stack below the text; CTAs stack vertically
- Search bar: On mobile, the inline search bar collapses into a search icon that opens a full-screen search overlay

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (badges, accordions, footer links) could not be reliably extracted from the live site
- Error state styling for forms (validation messages, error icons) is inferred from common patterns rather than observed
- Dark mode is not present on the live site; no dark palette tokens are available
- The exact font weight and size for `display-xl` and `display-lg` are estimated from the Jost font family and typical brand usage; live site may vary
- Sub-brand or campaign-specific palettes (e.g., holiday, limited edition) are not captured
- Animation timing and easing curves (hover transitions, accordion expand/collapse) are not documented
- The extracted color list includes several very similar navy/charcoal tones (#223746, #273745, #1f2c39, #2b3844, #171923, #1b1c30, #121212) — the primary was chosen as the most distinctive and frequently occurring navy (#223746), but the exact mapping of each tone to specific UI elements is inferred
- The purple (#805ad5) and coral (#ea817f) accents appear in the extracted palette but their exact usage context (badges, buttons, links) is based on brand positioning rather than direct observation
- Font-family declarations were inconsistent across the live site (multiple `!important` overrides); the primary pairing of Jost for display and Freight Sans Pro for body is based on the most common declarations and typical brand usage
- Checkout-specific colors (Shopify Pay, Klarna, Afterpay widgets) may be present in the extracted palette but are not included in the design system tokens
