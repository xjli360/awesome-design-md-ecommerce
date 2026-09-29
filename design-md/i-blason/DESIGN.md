---
version: alpha
name: "i-Blason"
source_url: "https://www.i-blason.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand that sells armor for your phone, i-Blason lives in the tension between #108474 (a deep, confident teal) and #fbcd0a (a sharp, warning-yellow accent) — colors that feel more industrial than fashionable, more tool than accessory. The palette is dominated by a spectrum of grays (#eeeeee, #fafafa, #555555, #121212) that form a neutral, no-nonsense backdrop for product photography of rugged cases and screen protectors. The meta theme-color #261e1b, a near-black brown, sets the browser chrome itself to match the brand's dark, serious tone. Typography runs on a mix of Jost and Nunito Sans — clean, geometric sans-serifs that read as modern but not trendy, with Arial and Helvetica as fallbacks for maximum compatibility. The design system is built for e-commerce efficiency: pill-shaped buttons (`{rounded.full}`), generously padded product cards (`{rounded.sm}`), and a sticky top nav that prioritizes category navigation over brand storytelling. The teal `{colors.primary}` drives primary CTAs and the cart badge, while the yellow `{colors.accent}` appears sparingly — sale badges, promotional banners, and the occasional highlight — giving the site the visual language of a hardware store crossed with a tech accessories brand. There is no softness here; corners are either sharp (`{rounded.none}`) or fully rounded (`{rounded.full}`), with no intermediate radius that might suggest luxury or whimsy. The brand's voice is direct, functional, and protective — it sells confidence in a drop, not style on a shelf.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c9"
  accent: "#fbcd0a"
  accent-active: "#d9b008"
  ink: "#121212"
  body: "#555555"
  muted: "#747474"
  muted-soft: "#888888"
  hairline: "#d1d1d1"
  hairline-soft: "#dedede"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#121212"
  meta-theme: "#261e1b"
  badge-sale: "#fbcd0a"
  badge-new: "#108474"
  star-rating: "#fbcd0a"
  error: "#dd4b39"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"

typography:
  display-xl:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0px
  button-ghost-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(16, 132, 116, 0.15)"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    boxShadow: "0 1px 3px rgba(0, 0, 0, 0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
    gap: "{spacing.xxs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  banner-promo:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: "center"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    height: 40px
    width: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a teal pill (`{rounded.full}`) with white uppercase text. Used for "Add to Cart", "Buy Now", and primary checkout actions. On hover, darkens to `{colors.primary-active}`. Disabled state uses a muted teal `{colors.primary-disabled}` with reduced opacity.

**`button-secondary`** — An outlined variant with a white fill and gray border (`{colors.hairline}`). Used for "View Details", "Learn More", and secondary actions alongside primary buttons. Active state swaps the border to `{colors.ink}` for clear differentiation.

**`button-accent`** — The yellow variant (`{colors.accent}`) reserved for promotional urgency: "Shop Sale", "Limited Time Offer", and banner CTAs. Uses dark text (`{colors.on-accent}`) for contrast against the bright yellow fill.

**`button-ghost`** — A text-only button with no background or border, colored in the brand teal. Used for "See All", "Clear Filters", and dismissible actions. Hover state darkens the text to `{colors.primary-active}`.

### Cards
**`product-card`** — A white card with a subtle shadow and `{rounded.sm}` corners. The product image fills the top with `{rounded.sm}` top corners and a 1:1 aspect ratio. Title and price sit below with standard padding. On hover, the shadow deepens to signal interactivity. Sale badges (`{colors.badge-sale}`) and new-arrival badges (`{colors.badge-new}`) are positioned absolutely at the top-left of the image area.

**`product-card-badge`** — A small yellow pill (`{rounded.xs}`) with uppercase "SALE" text, positioned absolutely over the product image. Uses `{colors.accent}` background and `{colors.on-accent}` text for high contrast.

**`product-card-badge-new`** — A teal badge variant for "NEW" labels, using `{colors.primary}` background and white text.

### Navigation
**`nav-bar`** — A 64px white bar with a subtle bottom border. Contains the logo, category links in uppercase Jost, and utility icons (search, account, cart). On scroll, gains a box shadow and becomes sticky. Active nav links show a 2px teal bottom border.

**`search-bar`** — A pill-shaped (`{rounded.full}`) input with a light gray fill (`{colors.surface-soft}`) and subtle border. On focus, the border switches to the brand teal with a soft glow ring. Placeholder text in `{colors.muted}`.

### Forms
**`text-input`** — Standard form input with a white fill, gray border, and `{rounded.sm}` corners. Focus state adds a teal border and a 3px teal ring at 15% opacity. Error state swaps the border to `{colors.error}` (#dd4b39).

**`quantity-selector`** — A compact input group with a decrement button, number display, and increment button. The buttons are square (40x40px) with a light gray fill, while the number display is white with a border.

### Footer
**`footer`** — A dark section (`{colors.ink}` background) with light gray text. Column headings are white and bold. Links are muted gray and turn white on hover. The footer spans the full width with generous padding.

### Other
**`cart-badge`** — A small teal circle (`{rounded.full}`) with white text, positioned on the cart icon. Shows the item count. Minimum 20px diameter with horizontal padding for double-digit counts.

**`banner-promo`** — A full-width yellow strip (`{colors.accent}`) with dark uppercase text. Used for site-wide announcements, free shipping offers, and seasonal promotions. Centered text with compact padding.

**`breadcrumb`** — A simple text navigation row with muted gray links and a darker active state. Uses caption typography. Separators (">") are in `{colors.hairline}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 items per row), hamburger menu replaces top nav links, search bar collapses to icon-only, footer stacks vertically, product card badges scale down to 9px font |
| Tablet | 744–1128px | Two-column product grid, top nav shows 4-5 category links, search bar is full-width but hidden behind an icon toggle, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all categories visible, persistent search bar, footer uses 4-column layout, product cards show hover shadow |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, additional whitespace on product cards, larger product images |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile
- Product card tap area covers the entire card, not just the title/price
- Quantity selector buttons are 40x40px, just under the 44px recommendation but acceptable for the compact layout
- Nav bar icons (search, account, cart) are 40x40px tap targets
- Accordion headers are full-width with 44px minimum height

### Collapsing Strategy
- Top nav category links collapse into a hamburger menu below 744px
- Search bar collapses to an icon toggle on mobile, expanding to full-width on tap
- Product filters collapse into a slide-out drawer on mobile and tablet
- Footer columns stack vertically on mobile (single column), expand to 2 columns on tablet, and 4 columns on desktop
- Secondary navigation (breadcrumbs) hides on mobile, replaced by a back button
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards are inferred from common e-commerce patterns; exact transition durations and easing curves were not extractable
- Error state styling for forms (red border) is assumed from the presence of #dd4b39 in the palette; exact error message typography and iconography are unknown
- The extracted font list includes "JudgemeIcons" (a review widget icon font) which is not a brand typeface; it has been excluded from the typography system
- Social media icon colors (#3b5998, #1da1f2, #e60023, #0073b1) are platform defaults, not brand choices; they are included for reference but should not be used outside social icon contexts
- The accent yellow (#fbcd0a) appears in the extracted palette but its exact usage (sale badges, promotional banners, or star ratings) is inferred from common e-commerce patterns
- Dark mode styling is not present in the extracted data; the brand likely does not support it
- Loading states, skeleton screens, and spinner animations were not extractable
- Mobile navigation drawer (hamburger menu) styling — exact width, animation, and overlay behavior — is assumed from Shopify default patterns
- Product variant selector (size/color swatches) styling was not extractable; the brand may use dropdowns or visual swatches
- Checkout flow styling is handled by Shopify's default checkout, not the brand's custom design system
- The extracted palette includes #a89cc8 (a lavender) and #c1e6e6 (a pale mint) which may be seasonal or promotional colors; their usage is unknown
