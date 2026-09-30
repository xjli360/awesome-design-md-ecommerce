---
version: alpha
name: "Salt Oral Care"
source_url: "https://www.saltoralcare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, clinical-yet-warm oral care brand that balances the crisp authority of a dentist’s office with the approachable softness of a modern DTC wellness label. The palette is anchored by a deep teal primary {colors.primary} (#108474) — a color that reads as both hygienic (think antiseptic mouthwash) and natural (sea salt, seaweed, mint). This teal appears on primary buttons, navigation accents, and key product badges, always paired with a bright white canvas {colors.canvas} (#ffffff) and soft gray surfaces like {colors.surface-soft} (#f9fafb) and {colors.surface-card} (#fafafa). The brand’s secondary voltage comes from a warm yellow accent {colors.accent-yellow} (#fed716) used sparingly for sale tags, star ratings, and promotional highlights — a surprising jolt of optimism against the cool teal. Typography relies on Nunito Sans, a rounded sans-serif that feels friendly and legible at small sizes (product descriptions, ingredient lists), while display headings occasionally use EB Garamond or Baskerville for a touch of editorial sophistication in hero sections. Buttons are softly rounded at {rounded.sm} (8px), product cards use {rounded.md} (12px), and the overall spacing system is generous — {spacing.section} (64px) between major blocks, with {spacing.lg} (24px) gutters inside cards. The brand avoids harsh lines: hairline borders use {colors.hairline} (#dddddd) and {colors.hairline-soft} (#e9e9e9), creating a subtle grid that never competes with product photography. Salt Oral Care’s design language says “trust us, we’re experts” without feeling cold — the teal warmth, the yellow spark, the soft corners, and the airy layout all conspire to make daily oral care feel less like a chore and more like a small act of self-care.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#c1e6e6"
  ink: "#333333"
  body: "#555555"
  muted: "#6d7278"
  muted-soft: "#888888"
  hairline: "#dddddd"
  hairline-soft: "#e9e9e9"
  border-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  accent-yellow: "#fed716"
  accent-yellow-active: "#fbcd0a"
  accent-orange: "#ff7744"
  accent-green: "#12b985"
  accent-green-whatsapp: "#25d366"
  star-rating: "#fed716"
  error-text: "#ff7744"
  scrim: "#000000"
  badge-new: "#338fb1"
  badge-sale: "#ff7744"
  badge-eco: "#12b985"
  footer-bg: "#eeeeee"
  footer-text: "#666666"
  nav-link-active: "#108474"
  nav-link-inactive: "#555555"

typography:
  display-xl:
    fontFamily: "'EB Garamond', 'Baskerville', 'Caslon', 'Garamond', serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'EB Garamond', 'Baskerville', 'Caslon', 'Garamond', serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  nav-link-mobile:
    fontFamily: "'Nunito Sans', 'Arial', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1.5px solid {colors.primary}"
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-circle-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-mobile}"
    height: 60px
  nav-link-active:
    textColor: "{colors.nav-link-active}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.nav-link-active}"
  nav-link-inactive:
    textColor: "{colors.nav-link-inactive}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.error-text}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.error-text}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  badge-eco:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 28px
    width: 28px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
    width: "100%"
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  trust-badge-icon:
    color: "{colors.primary}"
    fontSize: "20px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and "Shop Now". Rendered in the brand teal {colors.primary} (#108474) with white text and 8px rounded corners. On hover, it deepens to {colors.primary-active} (#0d6b5d); disabled state uses a pale teal {colors.primary-disabled} (#c1e6e6). The button has a 48px height with 14px/28px padding for comfortable tap targets.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". White background with a 2px solid teal border. Active state shifts the border to the darker teal and adds a soft gray background {colors.surface-soft}. Height matches the primary button at 48px.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Cancel" or "Skip" actions in checkout flows. No background or border, just the teal text with button typography. Ideal for inline actions that shouldn't compete with primary CTAs.

**`button-yellow`** — A promotional variant used for limited-time offers, sale banners, or "Get 20% Off" CTAs. Uses the warm yellow accent {colors.accent-yellow} (#fed716) with dark ink text. Active state darkens to {colors.accent-yellow-active} (#fbcd0a). Same dimensions as the primary button.

**`button-pill-primary`** and **`button-pill-outline`** — Pill-shaped variants (9999px radius) used for subscription toggle, filter chips, or "Best Seller" tags. The pill-primary is filled teal; the pill-outline has a 1.5px teal border on white. Both use smaller button typography and 10px/24px padding for compact placement.

### Cards
**`product-card`** — The primary product display card, used on collection pages and search results. White background with 12px rounded corners, 16px padding, and a subtle box shadow (0 2px 8px rgba(0,0,0,0.06)). On hover, the shadow deepens to 0 4px 16px for a gentle lift effect. The card contains a square image area with 8px rounded corners, a title in {typography.title-sm}, and a price in {typography.body-md}. Badges overlay the top-left of the image.

**`product-card-badge`** — Small uppercase labels (e.g., "NEW", "SALE", "ECO") that sit on product card images. Backgrounds vary by type: {colors.badge-new} (#338fb1) for new arrivals, {colors.badge-sale} (#ff7744) for discounts, {colors.badge-eco} (#12b985) for sustainable products. All use white text, 4px rounded corners, and tight 2px/8px padding.

### Navigation
**`top-nav`** — The main site header, 72px tall on desktop, white background with a soft bottom border. Contains the brand logo on the left, nav links in the center, and cart/search icons on the right. Active nav links show a 2px teal underline. On mobile, the nav collapses to a 60px hamburger menu with full-screen overlay.

**`nav-link-active`** and **`nav-link-inactive`** — Navigation link states. Active links use teal text with a 2px bottom border in the same teal. Inactive links use a medium gray {colors.nav-link-inactive} (#555555). Both use 15px font size with 600 weight for clear hierarchy.

### Forms
**`text-input`** — Standard form input for checkout fields, newsletter signup, and account forms. White background, 48px height, 8px rounded corners, 1px hairline border. On focus, the border becomes 2px solid teal. Error state uses a 2px orange border {colors.error-text} (#ff7744).

**`search-bar`** — A pill-shaped search field (9999px radius) with a soft gray background {colors.surface-soft} and 1px hairline border. On focus, it switches to a white background with a 2px teal border. Height is 44px for a compact but tappable target.

**`newsletter-input`** and **`newsletter-submit`** — Paired components for email capture in the footer. The input is a standard text field with 8px rounded corners; the submit button is a teal primary button with 8px rounded corners. Both are 44px tall for alignment.

### Footer
**`footer-section`** — The site footer with a light gray background {colors.footer-bg} (#eeeeee) and medium gray text {colors.footer-text} (#666666). Contains link columns, social icons, and a newsletter signup. Links use the footer text color with a teal hover state. Padding is generous at 48px top/bottom.

### Cart & Checkout
**`cart-item`** — Individual line items in the cart drawer or page. White background with a soft bottom border. Contains product image, title, quantity selector, and price. Quantity selector uses a 40px height with soft gray buttons for increment/decrement.

**`checkout-button`** — A full-width primary button (100% width, 56px height) used in the cart and checkout flow. Same teal styling as the primary button but with extra height and padding for prominence. Active state darkens to {colors.primary-active}.

### Trust & Accents
**`trust-badge`** — Small informational badges used near checkout or on product pages to convey security, free shipping, or money-back guarantees. Soft gray background with a 1px hairline border, 8px rounded corners, and a teal icon. Text is in caption typography.

**`rating-stars`** — Star ratings displayed on product cards and review sections. Uses the yellow accent {colors.star-rating} (#fed716) at 16px font size. Empty stars render in a light gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to 60px hamburger; product cards stack full-width; hero section reduces padding to 32px; search bar moves to mobile menu; footer links stack vertically; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav remains full but reduces link spacing; hero uses 48px padding; sidebar filters appear as horizontal strip; newsletter stays inline |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero uses 64px section padding; sticky cart drawer; multi-column footer |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; expanded hero with larger typography; additional whitespace in margins |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Icon buttons (cart, search, hamburger) are 40px × 40px circles
- Quantity selector buttons are 28px × 28px within a 40px container
- Nav links have 32px minimum tap area on mobile
- Form inputs are 48px tall for easy tapping

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px; full-screen overlay with vertical link list
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer multi-column layout collapses to single column below 744px
- Hero section reduces padding and font sizes below 744px
- Search bar moves from inline in top-nav to a dedicated mobile search panel
- Sidebar filters on collection pages become a horizontal scrollable strip on tablet, then a bottom sheet on mobile
- Cart drawer becomes a full-screen overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, text inputs, and nav links were inferred from common DTC patterns but not verified against live site interactions
- Error styling for forms (validation messages, error icons) was not fully extracted; error text color (#ff7744) is an assumption based on its presence as an accent
- Dark mode is not supported; no dark palette tokens were found on the live site
- Sub-brand or seasonal color palettes (e.g., holiday promotions, limited editions) were not captured
- Specific font weights for Nunito Sans beyond 400, 500, 600, 700 were not confirmed; all weights used are common web-safe values
- Line heights and letter spacing values are editorial estimates based on typical DTC patterns, not extracted from CSS
- Box shadow values for product cards are editorial; exact shadow tokens were not found in extracted data
- Animation and transition timings (ease curves, durations) were not extracted
- Focus ring styles for keyboard navigation were not found
- Loading states (skeleton screens, spinners) were not captured
- Mobile bottom navigation or tab bar patterns were not observed
- Checkout flow specific components (shipping form, payment form) are inferred from Shopify defaults
- The "Judgeme" font declarations suggest a review widget integration, but its exact styling tokens were not extracted
