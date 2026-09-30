---
version: alpha
name: "Totallee"
source_url: "https://www.totalleecase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A matte-black obsession that reduces the phone case to its absolute minimum — a 0.35mm polypropylene film that feels like nothing at all. The brand’s identity is built on absence: no logos, no branding, no bulk, just a near-invisible shell that preserves the phone’s original silhouette. The palette is anchored in near-black (#231f20) and deep charcoal (#121212), with a single electric-blue accent (#36ace3) that appears only in the cart badge and a few hover states — a tiny voltage that keeps the minimalism from feeling cold. The site runs on a white canvas (#ffffff) with hairline-thin dividers (#dedede) and soft gray surfaces (#efefef, #eeeeee) that create depth without shadows. Typography uses Lato at modest weights (400 for body, 700 for headlines), set at generous line heights that give the sparse product pages room to breathe. Every product photo is a hero shot on a pure white background — no lifestyle, no hands, no context — just the case floating in negative space. The checkout flow uses Shopify’s default blue (#0b76a8) and a secondary gray (#555555) for utility text, but the brand’s own voice stays resolutely monochrome. The result is a site that feels more like a design studio’s portfolio than an e-commerce store: quiet, precise, and utterly confident in its restraint.

colors:
  primary: "#231f20"
  primary-active: "#121212"
  primary-disabled: "#555555"
  ink: "#231f20"
  body: "#444444"
  muted: "#555555"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#efefef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#36ace3"
  accent-blue-hover: "#0b76a8"
  badge-bg: "#36ace3"
  badge-text: "#ffffff"
  footer-bg: "#121212"
  footer-text: "#eeeeee"

typography:
  display-xl:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0
  button-cart:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-cart-active:
    backgroundColor: "{colors.accent-blue-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-sold-out:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.accent-blue}"
  cart-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  accordion-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px 0
  accordion-trigger:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a solid near-black (#231f20) rectangle with zero border-radius and white uppercase Lato text. On hover, it deepens to #121212. The disabled state drops to #555555 with no opacity change — the brand avoids transparency as a state signal. **`button-secondary`** — An outlined variant with a white fill and near-black text, used for secondary actions like "View Details" or "Learn More." The hover state adds a #efefef surface tint. **`button-ghost`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Clear." **`button-cart`** — The checkout-specific CTA, using the brand’s only accent color (#36ace3) to draw immediate attention. On hover, it shifts to #0b76a8. This is the only place the electric blue appears in the primary UI — it signals transaction completion.

### Cards
**`product-card`** — A pure white card with no border, no shadow, and no rounded corners. The product image fills the top area on a white background, with the title and price stacked below in Lato. On hover, the card remains visually unchanged — the brand trusts the product photography to do the work. **`product-card-title`** uses 16px bold Lato in near-black, while **`product-card-price`** uses 16px regular Lato in #444444. There is no rating, no review count, no badge by default — only the product name and price.

### Navigation
**`nav-bar`** — A fixed white bar at 64px height, containing the brand logo (left) and nav links (right) in uppercase Lato at 14px bold. On scroll, the bar shrinks to 56px. **`nav-link-active`** uses near-black text, while inactive links render in #555555. The cart icon sits at the far right with a **`cart-badge`** — a 20px circle filled with #36ace3 containing the item count in white.

### Forms
**`text-input`** — A rectangular input field with no border-radius, a 1px #dedede border, and 16px Lato text. On focus, the border switches to near-black (#231f20). **`select-input`** follows the same pattern with a custom dropdown arrow. **`quantity-selector`** is a compact 40px-tall input used in the cart, with increment/decrement buttons flanking the numeric value.

### Footer
**`footer`** — A deep near-black (#121212) section with white text (#eeeeee) set in 14px Lato. Links are white by default and shift to #36ace3 on hover. The footer contains columns for support, company info, and legal links, with a copyright line at the bottom. No social icons appear in the extracted data — the brand may omit them.

### Badges
**`badge`** — A small blue (#36ace3) pill with white text, used for "New" or "Sale" indicators on product cards. **`badge-sold-out`** uses the near-black primary instead, signaling unavailability without a red or gray — the brand avoids conventional error colors. Badges are 2px padding horizontally and 8px vertical, with 4px border-radius.

### Accordion
**`accordion-item`** — Used on product detail pages for specs, shipping info, and returns. Each item has a 1px #dedede bottom divider, a bold 16px trigger, and 16px body content below. The accordion expands inline without animation — the brand favors instant disclosure over motion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), nav collapses to hamburger, hero text reduces to 24px, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero at 28px, footer in two rows |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at 36px, footer in four columns |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid may expand to four columns |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Cart badge is 20px — borderline for touch; consider 24px minimum on mobile
- Quantity selector buttons are 40px × 40px, meeting touch targets
- Accordion triggers are 48px tall on mobile for easy tapping

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product filters (if present) collapse to a "Filter" button that opens a drawer
- Footer columns collapse to a single stacked column below 744px
- Product image gallery collapses from thumbnail strip to swipeable dots on mobile
- Accordion items remain expanded by default on desktop, collapsed on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs could not be reliably extracted — the focus border color (#231f20) is inferred from the brand palette
- Error states (validation, out-of-stock messaging) were not visible in the extracted data
- The Shopify checkout overlay uses its own blue (#0b76a8) which may not match the brand’s accent — the relationship between brand and checkout styling is unclear
- Social media icon colors and placement could not be determined
- Mobile hamburger menu animation and overlay behavior were not captured
- Product variant selectors (color swatches, size pickers) were not visible in the extracted data
- The brand may use a secondary accent color for seasonal or limited-edition products — none was found
- Dark mode is not supported; the site is light-only
- Loading states and skeleton screens were not captured
- The extracted font list includes Font Awesome (icons) and Lato — it’s possible the brand uses a second web font for headings that wasn’t detected
- The extracted hex list contains #36ace3 and #0b76a8 — the latter is likely Shopify’s default checkout blue, not a brand color. The brand’s true accent is #36ace3
