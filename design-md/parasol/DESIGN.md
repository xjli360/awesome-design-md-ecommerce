---
version: alpha
name: "Parasol"
source_url: "https://parasolco.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baby-care brand that wraps its products in a botanical green (#2b361b) and a blush pink (#f2bdb6) — a pairing that reads less like a nursery pastel and more like a forest floor at dawn. The green anchors the primary button and the top navigation bar, while the pink surfaces in secondary accents, hover states, and the soft glow of the subscription-callout badge. The canvas is a warm off-white (#f3efe9) rather than a clinical white, and the body text runs at #4f4f4f — a charcoal that avoids the harshness of pure black on a baby brand. Rubik, a geometric sans-serif with a friendly circular 'o' and open apertures, carries all text at modest weights (400 for body, 500 for buttons, 600 for titles), never exceeding 700. The system uses rounded corners sparingly — buttons get {rounded.sm} (8px), cards get {rounded.md} (12px), and only the subscription badge and search input reach {rounded.full} (pill shape). There is no hard corner on any interactive element, but the brand avoids the over-softness of a toy brand; the 8px radius on buttons feels intentional, not accidental. The product grid uses a 2-column layout on mobile and 3-column on desktop, with each card showing a single hero image, the product name in {typography.title-md}, a price line, and a "Subscribe & Save" toggle that switches the CTA from "Add to Cart" to "Subscribe Now" — the primary green button (#2b361b) with white text (#ffffff). The footer is a dense column of links in {typography.body-sm} at #4f4f4f, with a newsletter signup that mirrors the pill-shaped search bar. The brand's voice is direct and reassuring — "Gentle on skin. Strong on protection." — and the design system follows suit: clean, warm, and uncluttered, with the green-pink duo doing all the emotional work.

colors:
  primary: "#2b361b"
  primary-active: "#01150f"
  primary-disabled: "#8ec18f"
  ink: "#121212"
  body: "#4f4f4f"
  muted: "#aaaaaa"
  muted-soft: "#b8b8b8"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f3efe9"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#f2bdb6"
  accent-green-light: "#b1e4b7"
  accent-green-soft: "#b1e3b7"
  accent-green-medium: "#66c872"
  accent-green-strong: "#3c9342"
  accent-red: "#d02f2e"
  accent-blue: "#005fcc"
  badge-save: "#478947"
  error: "#d50000"
  error-soft: "#db4827"

typography:
  display-xl:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-pill-subscribe:
    backgroundColor: "{colors.accent-green-strong}"
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
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-save:
    backgroundColor: "{colors.badge-save}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "4px 4px"
    height: 32px
  subscription-toggle-active:
    backgroundColor: "{colors.accent-green-light}"
    textColor: "{colors.primary}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.sm}"
  footer-newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 40px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe Now", and "Shop All" links. Rendered in the brand green (#2b361b) with white text, an 8px rounded corner, and 12px vertical padding. On hover, it transitions to the darker green (#01150f). The disabled state uses a muted green (#8ec18f) to signal inactivity without losing brand identity.

**`button-secondary`** — An outlined variant used for "Learn More" and "View Details" links. It inherits the canvas background (#f3efe9) with a 2px solid green border. On hover, the background fills with the accent pink (#f2bdb6), creating a warm, inviting state change. Height and padding match the primary button for alignment in forms and product cards.

**`button-pill-subscribe`** — A compact, pill-shaped button reserved for subscription upsells and "Subscribe & Save" CTAs. Uses the stronger green (#3c9342) to differentiate from the primary green, with a fully rounded shape and smaller typography. This button signals a savings or commitment action distinct from a one-time purchase.

### Text Inputs
**`text-input`** — Standard form input for checkout fields, account forms, and contact pages. Uses the warm canvas background, a 1px hairline border (#dedede), and 8px rounded corners. On focus, the border thickens to 2px and turns green (#2b361b). Height is 44px to match button heights for inline form layouts.

**`search-bar-pill`** — The site search input, rendered as a pill-shaped field with a white background and soft hairline border. Used in the header and mobile search overlay. The pill shape distinguishes search from other form inputs, following the e-commerce convention of a friendly, discoverable search affordance.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 64px height with a warm canvas background and a thin bottom border. Navigation links use 14px Rubik at 500 weight. The active link is underlined with a 2px green border and the text turns green. The bar contains the brand logo (left), main nav links (center), and account/cart icons (right). On mobile, the nav collapses into a hamburger menu.

**`nav-link-active`** — The active state for navigation items. The text color shifts to the brand green and a 2px bottom border appears, creating a clear indicator of the current section without relying on background fills.

### Product Cards
**`product-card`** — The primary content unit for product listings. A white card with 12px rounded corners and 16px padding. Each card contains a square product image (1:1 aspect ratio) with 8px rounded corners, the product title in 16px Rubik 600, and the price in 16px Rubik 400. Cards are arranged in a responsive grid — 2 columns on mobile, 3 on tablet, 4 on desktop. Hover state adds a subtle shadow (not yet extracted).

**`badge-save`** — A small green badge used to highlight subscription savings on product cards. Uses 11px uppercase Rubik 600 with tight letter-spacing, 4px rounded corners, and 2px vertical padding. Positioned at the top-left of the product image.

**`badge-new`** — A pink badge (#f2bdb6) used for new product arrivals. Same typography and dimensions as the save badge, but the pink background creates visual variety and draws attention to fresh inventory.

**`subscription-toggle`** — A pill-shaped toggle switch for selecting between one-time purchase and subscription. The inactive state is a soft gray (#f5f5f5) with body text. The active state fills with light green (#b1e4b7) and the text turns dark green. The toggle is 32px tall with 4px internal padding, containing two text labels ("One-Time" and "Subscribe & Save") that switch on selection.

### Footer
**`footer-link`** — Standard footer navigation links in 14px Rubik 400 at body color (#4f4f4f). Links are stacked vertically with 8px spacing. Hover state transitions to the brand green. The footer also contains a newsletter signup input matching the search-bar-pill shape but with a green submit button.

**`footer-newsletter-input`** — A pill-shaped email input in the footer, identical in shape to the search bar but with a green primary button attached. The input uses the white card background with a hairline border.

### Hero Section
**`hero-section`** — The full-width hero banner on the homepage, using the warm canvas background with 64px vertical padding. Contains a large heading (32px Rubik 600) and a subheading (16px Rubik 400) with 12px spacing between them. The hero may feature a product image or lifestyle photography on the right side (desktop) or below the text (mobile).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product grid goes to 2 columns; hero stacks vertically; footer links stack; search bar moves to overlay |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero has side-by-side layout; footer has 2-column link grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero with large image; footer has 3-column link grid |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can go to 4 columns; hero image scales up |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Product card tap targets are the entire card surface (not just text)
- Subscription toggle is 32px tall with 44px tap area via padding
- Search bar and newsletter input are 40px+ tall
- Nav links have 44px minimum tap area on mobile

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product filters collapse to a "Filter" button that opens a drawer on mobile
- Footer link columns collapse to accordion sections on mobile
- Product image galleries collapse to single-image swipe on mobile
- Subscription toggle collapses from side-by-side to stacked on very narrow screens (< 480px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the static HTML; transitions and shadows are inferred from common e-commerce patterns
- Error state styling for form inputs (border color, error message typography) is not confirmed — the extracted red (#d50000) is likely used but exact implementation is unknown
- Dark mode is not supported and no dark-mode tokens were found
- The exact font-weight for display-xl (32px) is inferred from common Rubik usage; the site may use 500 or 700 depending on context
- Product card shadow on hover is assumed but not confirmed from extraction
- The subscription toggle's exact active/inactive color mapping is inferred from the green tones present; the toggle may use a different green than #b1e4b7
- Checkout flow styling (Shopify checkout) was not extracted and may use different colors than the main site
- The brand's secondary pink (#f2bdb6) usage in hover states is inferred from its frequency in the extracted palette but exact component mapping is unconfirmed
- Spacing values for section padding and card gaps are estimated from common e-commerce patterns; the exact grid gap is not extracted
- The hero section's image treatment (border-radius, shadow) is not confirmed
- Mobile navigation drawer styling (background, animation) is unknown
