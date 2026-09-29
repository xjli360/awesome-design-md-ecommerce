---
version: alpha
name: "Thinx"
source_url: "https://thinx.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A neon-lime #e6ff55 voltage cuts across a warm peach #fceee3 canvas — Thinx uses this improbable acid-green as its primary signal, a color more common to energy drinks or rave flyers than underwear, and it works because the brand is selling permission to bleed, leak, and sweat without shame. The palette is deliberately small: the lime for CTAs and badges, the peach for backgrounds and hover states, a near-black #121212 for body text, and a soft #dedede for borders and dividers. There are no pastel pinks or blush tones — the brand rejects the euphemistic femininity that dominates the category. Typography runs a clean sans-serif at moderate weights; display headlines sit at 24–32px in weight 600, body copy at 16px weight 400. Buttons are squat rectangles with {rounded.sm} corners — no pills, no softness — and the lime fills them completely, with white text that reads "SHOP NOW" or "TAKE THE QUIZ" in all-caps. Product cards float on white with a thin {colors.hairline} border and a single lime accent on the "NEW" badge or the "ADD TO CART" button. The nav bar is a thin strip of {colors.canvas} with the brand wordmark in {colors.ink} and a lime-highlighted "SALE" link. The overall feel is utilitarian, direct, and slightly confrontational — the opposite of the whispery, floral language of legacy period-care brands.

colors:
  primary: "#e6ff55"
  primary-active: "#d4f03a"
  primary-disabled: "#f0ffb0"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#fceee3"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-primary-active: "#121212"
  on-primary-disabled: "#666666"
  accent-warm: "#fceee3"
  accent-gray: "#dedede"
  sale-badge: "#e6ff55"
  new-badge: "#e6ff55"
  error: "#cc0000"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    textColor: "{colors.on-primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary-disabled}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 11px 15px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.error}"
    padding: 11px 15px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  sale-nav-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.error}"
  product-card-original-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: "line-through"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  quiz-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 28px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-trigger-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base} 0"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 40px
  size-selector-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: "8px 12px"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 40px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-total:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled entirely with the signature lime #e6ff55. Text is uppercase, weight 700, in near-black #121212. On hover, the fill shifts to a slightly deeper lime #d4f03a. Disabled state drops to a pale yellow-green #f0ffb0 with gray text. Corners are a modest 8px — no pills, no softness. Used for "SHOP NOW", "ADD TO CART", and "SUBSCRIBE" actions.

**`button-secondary`** — An outlined variant with a 2px solid black border on a white background. Hover fills the background with the warm peach #fceee3. Used for "LEARN MORE" and "VIEW DETAILS" — secondary actions that still carry weight.

**`button-tertiary-text`** — A text-only button with no background or border. The uppercase label sits directly on the canvas. Hover shifts the text to the active lime. Used for "SKIP" or "CANCEL" in modals and for "SEE ALL" links in product strips.

### Cards
**`product-card`** — A white card with a 1px #dedede border and 8px rounded corners. The product image sits flush to the top corners. Below: product name in body-sm, price in title-sm, and a size selector row. On hover, the border turns lime and a subtle shadow lifts the card. A lime badge ("NEW", "BESTSELLER", "SALE") can appear in the top-left corner of the image.

**`product-card-badge`** — A small lime rectangle with black uppercase text, 4px rounded, positioned absolutely over the product image. The badge is the brand's primary signal — it's the first thing the eye lands on.

### Navigation
**`top-nav`** — A 64px white strip with the Thinx wordmark left-aligned and nav links right-aligned. Links are uppercase, weight 600, 14px. The active page gets a 2px lime underline. The "SALE" link is always lime-colored. On mobile, the nav collapses to a hamburger with a lime icon.

**`nav-link-active`** — The active state uses a lime bottom border as the only indicator — no background fill, no pill shape. This keeps the nav clean and lets the lime act as a directional signal.

### Forms
**`text-input`** — A white input with a 1px #dedede border and 8px rounded corners. On focus, the border thickens to 2px and turns lime. Error state uses a red border. Height is 48px for comfortable touch targeting. Used for email signup, search, and checkout fields.

**`select-input`** — Matches the text-input styling but includes a custom dropdown arrow. The lime focus ring is the only color accent.

**`size-selector`** — A 40px tall pill-shaped button group for size selection (XS–3XL). Selected state fills with lime and black text. Unselected state has a gray border. The active size is unmistakable.

### Footer
**`footer`** — A near-black #121212 footer with white text. Links are muted gray #999999 and turn white on hover. The footer contains the brand's mission statement, product categories, support links, and social icons. The lime is absent here — the footer is the brand's serious, trustworthy anchor.

### Cart & Checkout
**`cart-item`** — A white row with a bottom border, showing product image, name, size, quantity selector, and price. The layout is utilitarian — no decorative elements, just clear pricing and a remove link.

**`checkout-button`** — A taller (56px) version of the primary button, used as the final CTA in the cart. It fills the full width of the cart panel on mobile.

### Trust & Information
**`trust-badge`** — A small peach #fceee3 rectangle with centered caption text. Used for "FREE RETURNS", "CLIMATE NEUTRAL", and "FSA/HSA ELIGIBLE" badges. The peach provides a warm, reassuring counterpoint to the aggressive lime.

**`accordion-trigger`** — A text-only trigger for FAQ and product-detail accordions. The trigger is title-sm weight 600 with no background. On open, a lime plus/minus icon rotates. Content slides open below in body-md.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; hero text reduces to display-lg; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4–5 links; hero uses display-xl; buttons remain inline |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero uses display-xl with larger padding; product cards show hover effects |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to 4 columns; hero has generous whitespace on sides |

### Touch Targets
- All buttons and interactive elements are minimum 48px tall (exceeds Apple's 44px guideline)
- Size selector buttons are 40px tall with 12px horizontal padding
- Accordion triggers have 16px vertical padding for comfortable tapping
- Nav links have 8px vertical padding within the 64px nav bar
- Quantity selector buttons are 40px x 40px square targets

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; the hamburger icon is lime
- Product filters collapse to a "FILTER" button that opens a slide-in panel on mobile
- Footer columns (5 on desktop) collapse to a single stacked column on mobile
- Product image galleries collapse from thumbnail strip to swipeable dots
- Accordion content is collapsed by default on all screen sizes
- Cart drawer replaces full cart page on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the typography block uses Inter as a reasonable sans-serif default for a modern DTC brand, but the actual brand font (possibly a custom or licensed typeface) is unknown
- Hover states for most components were inferred from common DTC patterns; actual Thinx hover transitions (duration, easing) could not be extracted
- Error styling (form validation, error messages, input error states) is assumed based on standard web conventions; Thinx may use a different error color or pattern
- The extracted color list (#e6ff55, #fceee3, #dedede, #121212) is sparse — only 4 colors. The brand may use additional accent colors (e.g., for bladder-leak product lines, seasonal collections, or sub-brands) that were not captured
- Dark mode support is unknown; the brand may not implement it
- The meta theme-color was absent, suggesting no browser chrome theming
- Shopify-specific checkout widget colors (Shopify Pay, Klarna, Afterpay buttons) may have been filtered from the extracted colors; the actual checkout flow may introduce additional brand colors
- Animation and motion design tokens (durations, easings, micro-interactions) are not captured
- The brand's illustration style, icon set, and photography treatment are not represented in the color/typography tokens
- Accessibility contrast ratios for the lime-on-black and lime-on-white combinations have not been verified against WCAG standards
