---
version: alpha
name: "Velvet Caviar"
source_url: "https://www.velvetcaviar.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A phone-case brand that wraps its protective shells in a pastel-and-neon color story anchored by a cool, confident cyan (#38b0de) — the single hue that appears on every primary CTA, the site’s floating cart badge, and the hero section’s accent line. That cyan sits alongside a warm blush (#e9c5bd) and a dusty rose (#e3c1ab), creating a palette that feels both sweet and sharp, like a candy store that also sells leather goods. The brand’s typography leans on Apris for display headlines — a rounded, friendly serif that gives the site a boutique editorial feel — while Messina Sans handles body copy with a clean, slightly condensed efficiency. Product cards use generous white space and a soft rounded corner (`{rounded.md}` ~12px), letting the case colors do the selling. The navigation bar is a thin, nearly invisible strip of white with a cyan search icon and a cart badge that pulses in the brand’s signature blue. Below the fold, a marquee of product images scrolls horizontally, each case rendered in a flat, almost vector-like style against a white background — no shadows, no gradients, just pure color and form. The footer collapses into a single column of links in muted gray (#b5b5b5), with a newsletter signup that uses the same cyan button as the rest of the site. The overall effect is clean, playful, and unapologetically feminine without being saccharine — a phone case brand that treats its product as a fashion accessory, not a utility.

colors:
  primary: "#38b0de"
  primary-active: "#2a8bb0"
  primary-disabled: "#a3d8f0"
  ink: "#1e1d1f"
  body: "#373737"
  muted: "#b5b5b5"
  muted-soft: "#dedede"
  hairline: "#ededed"
  hairline-soft: "#f5eacc"
  canvas: "#ffffff"
  surface-soft: "#f6ecd7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  blush: "#e9c5bd"
  dusty-rose: "#e3c1ab"
  marigold: "#e2c630"
  neon-green: "#9ef788"
  hot-pink: "#f2b5c4"
  deep-rose: "#814c4c"
  lavender: "#9a66cc"
  coral: "#ff8041"
  bubblegum: "#ff9ce3"
  lemon: "#fcf95b"
  amber: "#cd9402"
  error: "#ec3939"
  secondary-blue: "#327ed5"

typography:
  display-xl:
    fontFamily: "'Apris', 'Merriweather', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Apris', 'Merriweather', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Apris', 'Merriweather', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Messina Sans', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-cyan:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px {spacing.base}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "2px solid {colors.canvas}"
    boxShadow: "0 0 0 1px {colors.hairline}"
  product-card-swatch-selected:
    border: "2px solid {colors.ink}"
    boxShadow: "0 0 0 1px {colors.ink}"
  badge-new:
    backgroundColor: "{colors.hot-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
  badge-best-seller:
    backgroundColor: "{colors.marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
  badge-limited:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    textAlign: center
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    textAlign: center
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
  category-tab:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.full}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-newsletter-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
    height: 44px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 {spacing.xs}"
  color-swatch-grid:
    display: flex
    gap: "{spacing.sm}"
    flexWrap: wrap
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.canvas}"
    boxShadow: "0 0 0 1px {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
    boxShadow: "0 0 0 1px {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered in the signature cyan (#38b0de) with white uppercase text. Used for “Add to Cart,” “Shop Now,” and checkout entry points. On hover, it darkens to `{colors.primary-active}` (#2a8bb0). The disabled state fades to a pale cyan (#a3d8f0) with white text, signaling the action is unavailable.

**`button-secondary`** — A white button with a thin hairline border and dark ink text. Used for secondary actions like “View Details” or “Continue Shopping.” The active state swaps the border to ink and adds a soft cream background (`{colors.surface-soft}`).

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for filter tags, category toggles, and quick-add actions. Smaller padding and font size keep it compact.

**`button-pill-outline`** — The outline version of the pill button, used for inactive filter states and secondary tag selections. White background with a hairline border.

**`icon-button-circle`** — A 40px circular icon button with a white background and ink icon. Used for search, wishlist, and account icons in the navigation. The cyan variant (`icon-button-cyan`) uses the brand primary for the background and white for the icon, reserved for the search orb and cart badge.

### Navigation
**`top-nav`** — A thin, 64px white bar with a bottom hairline border. Contains the brand logo (left), navigation links (center), and icon buttons (right). Navigation links are uppercase, 13px, with 0.8px letter spacing. The active link gets a 2px cyan underline.

**`nav-link`** — Uppercase, tightly tracked text at 13px. Inactive links are ink; the active state shifts to cyan. Padding of 16px on each side keeps tap targets generous.

**`search-bar`** — A pill-shaped search input with a soft cream background (`{colors.surface-soft}`) and a hairline border. On focus, the background turns white and the border becomes 2px cyan. Placeholder text is muted gray.

**`cart-badge`** — A small cyan pill that floats over the cart icon, displaying the item count in white badge text. Minimum 20px wide to accommodate double digits.

### Cards
**`product-card`** — A white card with 12px rounded corners and 8px padding. The product image fills the top with a 1:1 aspect ratio and 8px rounded corners. Below, the title uses `{typography.title-md}` (16px, semibold), followed by the price in `{typography.price}` (16px, semibold, body color). A row of color swatches sits below the price, each a 24px circle with a white border and a thin hairline shadow. The selected swatch swaps the border to ink.

**`product-card-swatch`** — A 24px circular swatch representing a case color. The white border and subtle shadow create a “floating” effect against the card. Selected state uses an ink border for clear distinction.

### Badges
**`badge-new`** — A hot pink (#f2b5c4) pill with ink text, signaling newly arrived products. Compact at 10px uppercase with 2px vertical padding and 8px horizontal padding.

**`badge-sale`** — A coral (#ff8041) pill with white text, used for discounted items. Same compact sizing as the new badge.

**`badge-best-seller`** — A marigold (#e2c630) pill with ink text, highlighting top-performing products.

**`badge-limited`** — A lavender (#9a66cc) pill with white text, indicating limited-edition drops.

### Forms
**`text-input`** — A standard input field with a white background, 12px rounded corners, and a hairline border. On focus, the border thickens to 2px cyan. Error state uses a 2px red (#ec3939) border.

**`quantity-selector`** — A compact horizontal control with a central number display and two circular increment/decrement buttons. The buttons are 28px circles with a hairline border. Used on product detail pages.

**`footer-newsletter-input`** — A soft cream input field paired with a cyan submit button. The input has 12px rounded corners and a hairline border. The button uses `{typography.button-sm}` (12px uppercase) and matches the primary button’s height (44px).

### Hero
**`hero-section`** — A full-width white section with generous vertical padding (64px top and bottom). The headline uses `{typography.display-xl}` (36px, bold serif) centered, with a subheadline in `{typography.body-md}` (16px) below. A single cyan CTA button anchors the bottom.

**`hero-cta`** — A larger variant of the primary button (14px vertical padding, 32px horizontal) used exclusively in the hero section. Same cyan background and white uppercase text.

### Footer
**`footer`** — A white section with a top hairline border and 64px vertical padding. Links are 14px in muted gray (#b5b5b5) with 4px vertical spacing. The newsletter signup combines a soft cream input with a cyan submit button, laid out horizontally on desktop and stacked on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; product cards go to 2-column grid; hero padding reduces to 32px; footer links stack in single column; search bar becomes full-width |
| Tablet | 744–1128px | Navigation links remain visible but condensed; product cards in 3-column grid; hero maintains 48px padding; footer uses 2-column layout for links |
| Desktop | 1128–1440px | Full navigation with all links; product cards in 4-column grid; hero at 64px padding; footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5-column grid; hero content centered with max-width 800px |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Icon buttons are 40px circles, exceeding the 44px tap target guideline when including padding.
- Navigation links have 16px horizontal padding, creating comfortable tap zones.
- Color swatches are 32px on mobile (up from 24px on desktop) for easier tapping.
- Quantity selector buttons are 28px circles — slightly below guideline but compensated by the surrounding container padding.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px, hiding all nav links behind a slide-out drawer.
- The category strip (filter tags) collapses to a horizontal scrollable row on mobile, with a “See All” expand button.
- The product grid collapses from 5 columns on wide screens to 2 columns on mobile.
- The footer collapses from 4 columns to a single stacked column on mobile.
- The hero section reduces vertical padding from 64px to 32px on mobile, and the headline font size drops from 36px to 28px.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is large (22 colors) and likely includes checkout-widget colors (Klarna pink #ff9ce3, Afterpay blue #327ed5, Shopify Pay cyan #38b0de) and social-icon colors. The brand’s true primary is assumed to be #38b0de (the most frequently occurring distinctive color), but this may be Shopify Pay’s brand color rather than Velvet Caviar’s own. The blush (#e9c5bd) and dusty rose (#e3c1ab) are more likely to be the brand’s authentic accent palette.
- Font-family declarations found Apris, Merriweather, and Messina Sans, but exact font weights and sizes are inferred from typical usage patterns — not extracted from live CSS.
- Hover and focus states for most components are inferred from common e-commerce patterns, not observed on the live site.
- Error and validation styling for forms (error text color, icon placement, success states) is not confirmed.
- Dark mode is not supported and no dark-mode tokens exist.
- The brand’s logo color and exact typographic hierarchy (especially for mobile) are not extracted.
- Color swatch values for individual phone case colors are not extracted — the swatch grid uses the brand’s accent palette as placeholders.
- The site uses Shopify’s default cart drawer, which may have its own styling not captured here.
- No animation or transition tokens (duration, easing) were extracted.
