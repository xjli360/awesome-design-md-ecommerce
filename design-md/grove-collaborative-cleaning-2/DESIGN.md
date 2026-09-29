---
version: alpha
name: "Grove Collaborative"
source_url: "https://grove.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A muted, grounded palette anchored on #303030 ink against a #f7f3e4 canvas — the color of unbleached parchment — gives Grove Collaborative the feel of a well-edited pantry rather than a sterile ecommerce storefront. The brand’s primary voltage is #1f3521, a deep forest green that appears on add-to-cart buttons, sustainability badges, and the “Made in USA” seal, while #bf339d (a confident magenta) cuts across the system as a limited-use accent for sale tags and promotional banners. Typography runs ValueSans and ValueSerif Bold — the sans at Regular weight for body copy and Medium for navigation, the serif reserved for editorial headlines that read like a natural-products magazine. Corners are soft but not pillowy: buttons use {rounded.sm} (8px), product cards use {rounded.md} (12px), and the search bar uses {rounded.lg} (20px) — a gentle rounding that avoids the hyper-friendly full-pill of consumer apps. The checkout flow leans on #e0e0e0 and #eeeeee for dividers and disabled states, while #cdec85 (a pale chartreuse) and #aaf2f3 (a minty cyan) appear in ingredient callouts and eco-score graphics, suggesting a brand that trusts color-coded information over dense copy. The overall mood is restrained, credible, and slightly editorial — a cleaning-supply brand that wants you to read the label, not just scan the price.

colors:
  primary: "#1f3521"
  primary-active: "#142315"
  primary-disabled: "#a3b8a5"
  ink: "#303030"
  body: "#707070"
  muted: "#aaaaaa"
  muted-soft: "#e0e0e0"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f7f3e4"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-magenta: "#bf339d"
  accent-sale: "#d12121"
  accent-sale-soft: "#c70000"
  accent-terracotta: "#cc6328"
  eco-chartreuse: "#cdec85"
  eco-mint: "#aaf2f3"
  deep-teal: "#033b4c"
  star-rating: "#303030"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'ValueSerif Bold', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ValueSerif Bold', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ValueSerif Bold', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  micro-label:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.15px
  link:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-magenta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  button-accent-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-sale}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
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
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-eco:
    backgroundColor: "{colors.eco-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
    marginTop: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  category-tile-active:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  sustainability-badge:
    backgroundColor: "{colors.eco-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  promo-banner:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  cart-quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  checkout-progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep forest green (#1f3521) with white text. Used for "Add to Cart", "Subscribe & Save", and "Checkout" actions. On hover, shifts to `{colors.primary-active}` (#142315). Disabled state uses `{colors.primary-disabled}` (#a3b8a5) to indicate inactivity without visual noise.

**`button-secondary`** — An outlined variant on the warm canvas background, with a 2px solid `{colors.primary}` border and green text. Used for "Learn More", "View Details", and secondary checkout options. Hover fills the background with `{colors.primary}` at 10% opacity.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel", "Skip", and inline navigation links within forms and modals. Hover applies a subtle underline.

**`button-accent-magenta`** — A compact button using `{colors.accent-magenta}` (#bf339d) for promotional actions like "Shop Sale" or "Limited Edition". Smaller padding and height (38px) to sit alongside product cards without competing with primary CTAs.

**`button-accent-sale`** — A tight, urgent button in `{colors.accent-sale}` (#d12121) for clearance and flash-sale items. Used exclusively on product cards and promo banners, never in the main navigation or checkout flow.

### Cards
**`product-card`** — A white card on the warm canvas background, with 12px rounded corners and 16px internal padding. The product image occupies a 1:1 aspect ratio with matching corner rounding. Title uses `{typography.title-sm}`, price uses `{typography.body-md}`, and rating stars sit below in `{typography.caption}`. Badges (eco, sale, subscription) overlay the top-left of the image.

**`category-tile`** — A bordered tile for department navigation (Cleaning, Kitchen, Bath, etc.). Active state gains a 2px green border and a soft background fill. Used in horizontal scroll strips on the homepage and category landing pages.

### Navigation
**`nav-bar`** — A 64px fixed bar on the warm canvas background, with a subtle bottom border. Logo sits left, category links center, and account/cart icons right. Active nav links underline in `{colors.primary}`. On mobile, collapses to a hamburger menu with a full-screen overlay.

**`search-bar`** — A white input with 20px rounded corners and a 1px hairline border. Sits in the nav bar on desktop, expands to full width on mobile. Placeholder text in `{colors.muted}` (#aaaaaa). Focus state swaps border to 2px `{colors.primary}`.

### Forms
**`text-input`** — Standard form input with 8px rounded corners, 48px height, and 16px horizontal padding. Error state uses a red border (`{colors.accent-sale}`) and a helper text in `{colors.accent-sale-soft}` (#c70000). Focus state uses a 2px green border.

### Badges & Indicators
**`product-card-badge`** — A small green badge for "Made in USA", "Non-Toxic", or "Vegan" labels. Uses uppercase `{typography.badge}` with tight padding and 4px corners.

**`product-card-badge-eco`** — A chartreuse variant for "Climate Neutral", "Plastic-Free", or "Recyclable" certifications. Same typography and sizing as the green badge, but with a lighter, more playful color to differentiate certification types.

**`sale-badge`** — A red badge for percentage-off or clearance items. Always paired with a strikethrough original price on the product card.

**`sustainability-badge`** — A standalone badge used in the footer and product detail pages to highlight Grove's carbon-neutral shipping and plastic-negative commitments.

### Footer
**`footer-section`** — A deep green footer spanning the full viewport width. Links are white at 85% opacity, increasing to full opacity on hover. Contains columns for "Shop", "Learn", "About", and "Support", plus a newsletter signup form.

### Promotional Elements
**`promo-banner`** — A full-width magenta banner at the top of the page for site-wide promotions ("Free shipping on orders $49+"). Uses `{typography.body-sm}` and is dismissible via an X icon.

**`hero-banner`** — The homepage hero section on the warm canvas background, featuring a serif headline, a short body paragraph, and a single green CTA button. The hero image (lifestyle photography of cleaning products in a bright, airy home) sits beside or behind the text depending on viewport.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero stacks text above image; search bar expands to full width; footer columns stack vertically; promo banner text truncates to one line |
| Tablet | 744–1128px | Nav shows category links as dropdown; product cards in 2-column grid; hero uses 50/50 split; search bar remains in nav but shortens; footer shows 2-column layout |
| Desktop | 1128–1440px | Full nav with all category links visible; product cards in 3- or 4-column grid; hero uses 60/40 split with image dominant; search bar at full width in nav; footer shows 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero uses 55/45 split; all elements centered within max-width; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, add-to-cart) are at least 48px tall
- Nav links have 48px touch area on mobile (full height of nav bar)
- Category tiles are minimum 80px × 80px on touch devices
- Search bar tap target is 48px tall on all viewports
- Quantity selectors in cart are 40px × 40px minimum

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; category links move to a full-screen overlay with a green background
- Product card grid collapses from 4 columns → 2 columns → 1 column as viewport narrows
- Hero banner collapses from side-by-side layout to stacked layout at < 744px
- Footer collapses from 4 columns → 2 columns → 1 column
- Category tile strip collapses from horizontal scroll to vertical list at < 744px
- Search bar collapses from inline nav element to full-width input below nav at < 744px
- Promo banner collapses from multi-line to single-line at < 744px, with "Learn More" link hidden

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from common patterns; exact opacity values and transition durations were not extractable from the live site
- Error styling for forms (helper text color, icon placement) is estimated based on the extracted red palette; exact error state tokens are not confirmed
- Dark mode is not present on the live site; no dark-mode color tokens exist in the extracted data
- Sub-brand palettes (Grove Kids, Grove Home, etc.) were not distinguishable from the extracted color list
- The extracted hex list includes several grays (#6b7280, #777777, #2b2b2b, #121212) that may be checkout-widget or social-icon colors rather than brand tokens; these have been omitted from the palette
- Font weights beyond Regular (400) and Medium (500) for ValueSans were not extractable; Bold (700) is confirmed for ValueSerif only
- The extracted font list includes "inherit" and "monospace" which are likely fallbacks or code artifacts, not brand fonts
- Spacing values are estimated based on common ecommerce patterns; exact padding/margin tokens from the design system were not extractable
- Animation durations, easing curves, and shadow tokens were not extractable from the live site
- The checkout flow may use Shopify's default styling; Grove-specific checkout tokens are unconfirmed
- Accessibility contrast ratios between `{colors.canvas}` (#f7f3e4) and `{colors.body}` (#707070) should be verified against WCAG 2.1 AA standards
