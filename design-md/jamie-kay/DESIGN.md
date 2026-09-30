---
version: alpha
name: "Jamie Kay"
source_url: "https://jamiekay.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A muted gold #977547, pulled from the brand's meta theme-color, sets the tone for Jamie Kay — not as a primary CTA voltage but as a quiet atmospheric warmth that tints buttons, borders, and the soft glow of a site built for new parents. The true primary is a deep crimson #cc142b, a bold but controlled accent that appears on sale badges, cart indicators, and the rare moment the brand needs to say "look here." The canvas is a creamy off-white #fffcf9, warmer than hospital white, while the secondary surface #f0ede5 reads like unbleached linen. Typography splits between two worlds: EB Garamond for display headings — a serif with genuine gravitas, not a decorative afterthought — and Inter for body and UI, giving the product pages a clean, legible structure that doesn't compete with the photography. The site's signature move is the product-card grid: softly rounded images at {rounded.md}, a crimson "SALE" badge pinned to the top-left corner, and a three-line price block that separates "was" from "now" with a hairline #e3dfd3 strike-through. Navigation is minimal — a left-aligned logo, a centered category strip (New Arrivals, Baby, Toddler, Sale), and a right-aligned icon cluster (search, account, cart with a #cc142b dot). The footer runs six columns of thin links in #766456 on #f0ede5, ending with a newsletter signup that uses a pill-shaped input and a gold #977547 submit button. There is no dark mode, no hero carousel, no video — just still photography of babies in organic cotton, held by mothers whose hands are always in frame.

colors:
  primary: "#cc142b"
  primary-active: "#a81022"
  primary-disabled: "#f0b0b8"
  ink: "#191008"
  body: "#3d4246"
  muted: "#636666"
  muted-soft: "#868a89"
  hairline: "#e3dfd3"
  hairline-soft: "#f0efeb"
  canvas: "#fffcf9"
  surface-soft: "#f8f0e7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold: "#977547"
  gold-light: "#a0917c"
  gold-soft: "#baaa95"
  sale-badge: "#cc142b"
  sale-text: "#cc142b"
  price-strikethrough: "#9da1a0"
  footer-bg: "#f0ede5"
  footer-text: "#766456"
  newsletter-input-bg: "#ffffff"
  newsletter-input-border: "#e3dfd3"

typography:
  display-xl:
    fontFamily: "'EB Garamond', Garamond, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'EB Garamond', Garamond, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'EB Garamond', Garamond, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  footer-link:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price-current:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-original:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.gold}"
  newsletter-input:
    backgroundColor: "{colors.newsletter-input-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.newsletter-input-border}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-category-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price-current:
    typography: "{typography.price-current}"
    textColor: "{colors.ink}"
  product-card-price-original:
    typography: "{typography.price-original}"
    textColor: "{colors.price-strikethrough}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
  footer-column-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  footer-newsletter-button:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.gold}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, used for "Add to Cart" and checkout flows. Fills with deep crimson #cc142b and white text, with a soft 8px radius. On hover, darkens to #a81022. Disabled state drops to a pale pink #f0b0b8. **`button-gold`** — A secondary CTA reserved for newsletter signups and "Shop the Sale" banners. Uses the brand's muted gold #977547, which reads as warm but not urgent. **`button-secondary`** — An outlined variant with a 1px hairline border on white canvas, used for "View Details" links and secondary actions. **`button-tertiary-text`** — A text-only button with no background or border, used for "Close" and "Cancel" in modals and mobile menus.

### Cards
**`product-card`** — The core shopping unit. A white card with no border or shadow — the product photograph does all the work. Images are softly rounded at 12px (`{rounded.md}`). A crimson badge pins to the top-left corner of the image for sale items. Below the image, the product name sits in 16px Inter semibold, followed by a two-line price block: the current price in 16px semibold, and the original price in 14px regular with a line-through in muted gray #9da1a0. No rating stars, no color swatches, no "quick add" — the card is intentionally sparse.

### Navigation
**`nav-bar`** — A 72px fixed header on white canvas. The logo sits left-aligned (a wordmark in EB Garamond, likely). Center-aligned category links (New Arrivals, Baby, Toddler, Sale) use 14px Inter medium. The active category gets a 2px crimson underline. Right-aligned icons (search, account, cart) are 40px circular touch targets. The cart icon carries an 18px circular badge in crimson with white text showing the item count. **`nav-category-strip`** — A secondary 48px strip below the main nav on category pages, showing subcategories like "Onesies," "Sleepwear," "Accessories."

### Forms
**`text-input`** — Standard form input with a 1px hairline border, 8px radius, and 48px height. On focus, the border shifts to gold #977547. Used for account forms, checkout fields, and search. **`newsletter-input`** — A pill-shaped input (9999px radius) with a white background and hairline border, paired with a gold submit button. The input and button sit side by side in the footer, creating a single 48px row.

### Footer
**`footer-section`** — A six-column grid on warm beige #f0ede5. Each column has a heading in 16px Inter semibold (#191008) and a stack of thin links in muted brown #766456. The last column contains the newsletter signup form. Below the columns, a thin bar with copyright text, payment icons, and social links. The footer is dense but quiet — no bold colors, no large typography.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product grid goes to 2 columns; footer stacks to single column; newsletter input and button stack vertically; category strip hides behind a "Shop" dropdown |
| Tablet | 744–1128px | Nav shows all categories but subcategory strip may collapse; product grid at 3 columns; footer at 3 columns; newsletter input and button remain inline |
| Desktop | 1128–1440px | Full nav with category strip; product grid at 4 columns; footer at 6 columns; newsletter input and button inline |
| Wide | > 1440px | Max-width container at 1440px; product grid may expand to 5 columns; all elements at full layout |

### Touch Targets
- All icon buttons in nav: minimum 40px diameter
- Category links: minimum 44px tap height
- Product card tap area: entire card is clickable
- Newsletter submit button: 40px height
- Cart badge: 18px diameter (minimum readable touch target for count)

### Collapsing Strategy
- Primary nav collapses to hamburger menu on mobile
- Category strip collapses to a single "Shop" dropdown on mobile
- Footer collapses from 6 columns to 1 column on mobile
- Product grid collapses from 4 columns to 2 columns on mobile
- Newsletter input and button stack vertically on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for product cards, nav links, and footer links could not be reliably extracted from the live site. The button-primary hover (#a81022) is inferred from typical darkening patterns.
- **Error styling** for form inputs (validation errors, required field indicators) was not visible in the extracted data.
- **Dark mode** — the site does not appear to support dark mode. No dark-mode tokens were found.
- **Sub-brand palettes** — Jamie Kay may have seasonal or collection-specific color palettes (e.g., holiday, gender-neutral) that were not captured.
- **Typography scale** — font sizes for display-xl, display-lg, etc., are estimated from typical e-commerce patterns and the brand's use of EB Garamond for headings. The exact scale may differ on the live site.
- **Spacing values** — section padding, grid gaps, and margin values are inferred from common patterns. The brand may use a custom spacing scale.
- **Shadow tokens** — no box-shadow values were found in the extracted CSS. The site may use subtle shadows on cards or modals that were not captured.
- **Animation/transition** — no transition durations or easing curves were extracted. The brand may use subtle fades or slide-ins.
- **Icon set** — the specific icon library (custom SVG, Font Awesome, etc.) was not identified. Icon colors and sizes are estimated.
- **Checkout flow** — Shopify checkout styling (Shopify Pay, Klarna, Afterpay buttons) was partially visible in the extracted colors but not fully documented. These may override brand colors during checkout.
