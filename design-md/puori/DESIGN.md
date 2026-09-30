---
version: alpha
name: "Puori"
source_url: "https://puori.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Nordic vitamin and supplement brand that uses teal (#00938d) as its primary signal — not as a health-industry green, but as a cold, clean Scandinavian fjord color that appears on every CTA, every product badge, and the site’s persistent top bar. The brand pairs this with a deep navy (#001a41) for headings and heavy text, creating a high-contrast, clinical-but-warm reading experience. The extracted palette includes a bright mint accent (#00daaf) used for hover states and secondary badges, and a soft silver-gray (#dde4e6) that functions as the primary hairline and surface-soft color across the interface. Typography runs Apercu, a geometric sans-serif with a slight humanist warmth, at moderate weights — display headlines sit at 600 weight rather than the heavy 700+ common in supplement ecommerce, letting product photography and white space carry the brand’s “pure, natural, superior” positioning. The site uses a clean white canvas (#ffffff) with generous padding, pill-shaped buttons (`{rounded.full}`) for primary actions, and softly rounded product cards (`{rounded.md}`) that feel approachable without being childish. The overall mood is that of a premium health store in Copenhagen: minimal, trustworthy, with every design decision feeling intentional and restrained.

colors:
  primary: "#00938d"
  primary-active: "#007a75"
  primary-disabled: "#80c9c6"
  ink: "#001a41"
  body: "#121212"
  muted: "#5a5a5a"
  muted-soft: "#8a8a8a"
  hairline: "#dde4e6"
  hairline-soft: "#e8edef"
  canvas: "#ffffff"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-mint: "#00daaf"
  accent-mint-hover: "#00c49e"
  badge-cert: "#001a41"
  badge-cert-text: "#ffffff"
  star-rating: "#00938d"
  error: "#c13515"
  success: "#00daaf"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.2px
    textTransform: uppercase
  badge:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link-active:
    fontFamily: "'Apercu', 'Apercu_fallback', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-tertiary-text-hover:
    textColor: "{colors.primary-active}"
  button-pill-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link-active}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-badge-cert:
    backgroundColor: "{colors.badge-cert}"
    textColor: "{colors.badge-cert-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-lg}"
    color: "{colors.body}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    accentColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  radio:
    accentColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.hairline}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  cart-item:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  cart-item-title:
    typography: "{typography.title-md}"
  cart-item-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  cart-total:
    typography: "{typography.title-lg}"
    color: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  checkout-button-hover:
    backgroundColor: "{colors.accent-mint-hover}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button with teal fill and white text. Uses `{rounded.full}` to create a friendly, approachable feel. On hover, shifts to `{colors.primary-active}` (#007a75). Disabled state uses `{colors.primary-disabled}` (#80c9c6) with reduced opacity. Used for "Add to Cart", "Subscribe", and "Shop Now" actions.

**`button-secondary`** — An outlined variant with a white fill and teal border. Maintains the same pill shape and typography as primary but communicates a secondary action like "Learn More" or "View Details". On hover, the background shifts to `{colors.surface-soft}` and the border darkens to `{colors.primary-active}`.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Read more" or "Cancel". The text color matches `{colors.primary}` and underlines on hover for accessibility.

**`button-pill-mint`** — A special accent button using `{colors.accent-mint}` (#00daaf) as background with dark ink text. Used for promotional CTAs, sale badges, or checkout flows where the brand wants to signal urgency or a special offer.

### Navigation
**`top-bar`** — A thin 36px bar at the very top of the page with `{colors.primary}` background and white uppercase caption text. Contains trust signals like "Free shipping over $50" or "100% money-back guarantee". This bar is sticky on mobile.

**`nav-bar`** — The main 72px navigation bar with white background and a subtle bottom border using `{colors.hairline}`. Contains the logo, product category links, search icon, and cart icon. Links use `{typography.nav-link}` at 500 weight. Active nav items get `{colors.primary}` text and a 2px bottom border in the same teal.

**`search-bar`** — A pill-shaped search input with `{colors.surface-soft}` background and `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`. The input uses `{typography.body-sm}` and has a search icon on the left side.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners and a soft `{colors.hairline-soft}` border. Contains a product image with rounded top corners, a title using `{typography.title-md}`, and a price using `{typography.body-md}`. On hover, the border becomes slightly darker and a subtle box shadow appears. Cards are typically displayed in a 3-4 column grid on desktop.

**`product-badge-cert`** — A small dark navy badge with white text, using `{typography.badge}` (11px uppercase). Used to indicate certifications like "Non-GMO", "Organic", or "Vegan". Positioned at the top-left of product images.

**`product-badge-sale`** — A mint-green badge with dark text, used for sale or discount indicators. Same typography and sizing as the cert badge but with `{colors.accent-mint}` background.

### Forms
**`text-input`** — Standard text input with white background, `{rounded.sm}` corners, and `{colors.hairline}` border. Focus state uses `{colors.primary}` border. Error state uses `{colors.error}` (#c13515) border. Used for email signups, search, and checkout forms.

**`select-input`** — Dropdown select styled identically to text inputs with the same border, padding, and rounded corners. The dropdown arrow is styled in `{colors.primary}`.

**`checkbox`** — Custom checkbox with `{colors.primary}` accent color and `{rounded.xs}` corners. Used in subscription forms and filter panels.

### Footer
**`footer`** — A full-width footer with `{colors.ink}` (#001a41) background and white text. Contains columns for product categories, customer service, and social links. Links use `{colors.hairline}` color with hover state switching to white. Section headings use `{typography.caption-bold}` (13px uppercase). The footer has generous padding of `{spacing.section}` (64px) top and bottom.

### Cart & Checkout
**`cart-item`** — Individual cart line items with white background and a soft bottom border. Each item shows the product thumbnail, title using `{typography.title-md}`, price using `{typography.body-md}`, and a quantity selector.

**`quantity-selector`** — A compact horizontal control with `{colors.surface-soft}` background and `{rounded.sm}` corners. Contains minus and plus buttons (40x40px) flanking the current quantity number. Used in cart and product detail pages.

**`checkout-button`** — The final checkout CTA using `{colors.accent-mint}` background with dark ink text. Same pill shape as primary buttons but with a brighter, more urgent color. On hover, shifts to `{colors.accent-mint-hover}` (#00c49e).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; top-bar text truncates; product cards stack vertically; footer columns stack; hero section reduces padding to 32px; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only; footer shows 2 columns; hero section uses 48px padding; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; footer shows 3 columns; hero section uses 64px padding; search bar in nav with full width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section uses 80px padding; all elements centered within max-width |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px minimum
- Quantity selector buttons are 40x40px
- Nav links have 48px touch area (padding + height)
- Checkbox and radio inputs have 44x44px clickable area
- Accordion headers have 48px touch target

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Footer columns collapse from 4 to 2 to 1
- Hero section text stack collapses from side-by-side to stacked
- Search bar moves from inline nav to full-width below nav on mobile
- Top-bar text truncates to single line on mobile
- Product card badges stack vertically on mobile if multiple badges exist

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for many components (product card, footer links, accordion) were inferred from common patterns rather than extracted from live CSS
- Error styling for forms (validation messages, error icons) could not be reliably extracted
- Dark mode is not present on the live site and no dark mode tokens exist
- Sub-brand or product-line-specific color variations (e.g., "Puori PW1" vs "Puori CP1") could not be distinguished
- Animation durations and easing curves (transitions, hover effects) were not extractable
- The exact font weights available in Apercu (400, 500, 600, 700) were inferred; the live site may use additional weights
- Letter-spacing values for typography are estimated based on common Apercu usage patterns
- The `#dedede` extracted color appears to be a Shopify checkout widget default and is not used in the brand palette
- The `#121212` extracted color is used as body text but may have a specific brand name (e.g., "ink" or "charcoal") that could not be confirmed
- Focus ring styles (outline, color, offset) were not extractable
- Loading states and skeleton screen patterns were not observed
- Toast/notification styling (success, error, info) could not be extracted
