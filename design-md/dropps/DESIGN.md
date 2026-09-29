---
version: alpha
name: "Dropps"
source_url: "https://dropps.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A direct-to-consumer laundry and dish brand that uses a stark black-and-navy palette — `#141414` for ink, `#000d8c` for primary voltage — to signal a no-nonsense, ingredient-first ethos that feels more like a modern CPG startup than a detergent company. The signature move is a bright marigold accent (`#f4bc51`) that appears on the "Add to Cart" button, subscription badges, and promotional banners, providing the only warmth against a cold blue-and-white system. The site runs on a clean `#f0f4ff` canvas that reads as a very pale periwinkle — not pure white — giving the entire experience a soft, airy quality that contrasts with the heavy navy CTAs. Typography is set in Inter and Silka, both geometric sans-serifs that lean slightly condensed at display sizes, with body copy at 14–16px in 400 weight for readability. Product cards use `{rounded.lg}` (20px) corners on pod-package imagery, while buttons use `{rounded.sm}` (8px) for a crisp, functional feel. The subscription model drives the UI: every product page features a toggle between one-time purchase and subscribe-and-save, with the latter highlighted in `#f4bc51` and accompanied by a "Save up to 30%" badge. The nav bar is minimal — logo left, cart right, with a hamburger on mobile — and the footer is dense with trust signals (carbon-neutral shipping, plastic-free packaging, B Corp certification). The overall mood is clinical but approachable: the navy says "we take ingredients seriously," the marigold says "this is the fun part (saving money and the planet)."

colors:
  primary: "#000d8c"
  primary-active: "#000a6b"
  primary-disabled: "#b8ccff"
  ink: "#141414"
  body: "#545454"
  muted: "#90a4ae"
  muted-soft: "#bacdff"
  hairline: "#e2e2e2"
  hairline-soft: "#f6f6f6"
  canvas: "#f0f4ff"
  surface-soft: "#f5f7fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#f4bc51"
  accent-marigold-active: "#e0a83a"
  accent-teal: "#00847b"
  accent-teal-soft: "#dcfffb"
  social-facebook: "#3b5998"
  social-twitter: "#00aced"
  social-pinterest: "#cb2027"
  apple-pay: "#000000"
  shopify-pay: "#007aff"
  klarna-pink: "#ffb3c7"
  afterpay-blue: "#b2fce4"

typography:
  display-xl:
    fontFamily: "'Silka', 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Silka', 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Silka', 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Silka', 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.15px
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  price:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-strikethrough:
    fontFamily: "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
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
  button-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.social-pinterest}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    height: 56px
  hamburger-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  logo:
    height: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  subscription-toggle-active:
    backgroundColor: "{colors.accent-teal-soft}"
    border: "2px solid {colors.accent-teal}"
  subscription-save-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-headline:
    typography: "{typography.display-xl}"
    maxWidth: 600px
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 500px
  feature-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
  trust-badge:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption-sm}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    height: 36px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    height: 36px
    width: 36px
  quantity-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: center
    width: 40px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-icon:
    textColor: "{colors.muted}"
    height: 16px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  spinner:
    color: "{colors.primary}"
    height: 24px
  toast-success:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  toast-error:
    backgroundColor: "{colors.social-pinterest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  modal-overlay:
    backgroundColor: "rgba(20, 20, 20, 0.6)"
  modal-content:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The default CTA, filled with `{colors.primary}` navy and white text. Used for "Add to Cart," "Subscribe Now," and primary checkout actions. On hover, shifts to `{colors.primary-active}` (#000a6b). Disabled state uses `{colors.primary-disabled}` (#b8ccff) with white text. Height is 44px with `{rounded.sm}` corners.

**`button-accent`** — The marigold variant (`{colors.accent-marigold}`) used for promotional CTAs, "Save with Subscription" toggles, and limited-time offers. Text is `{colors.ink}` (#141414) for contrast. Active state darkens to `{colors.accent-marigold-active}` (#e0a83a).

**`button-secondary`** — Outlined variant with `{colors.canvas}` background, `{colors.primary}` text, and a 2px navy border. Used for "Learn More" links, secondary checkout options, and "One-Time Purchase" toggles alongside subscription buttons.

**`button-tertiary-text`** — Ghost button with no background or border, only `{colors.primary}` text. Used for "Cancel," "Skip," and "View Details" links within cards and modals.

**`button-pill-marigold`** — Full-pill shape (`{rounded.full}`) in marigold, used for "Save 30%" badges on product cards and subscription upsells. Smaller padding (8px 16px) and `{typography.button-sm}`.

### Cards
**`product-card`** — White card (`{colors.surface-card}`) with `{rounded.lg}` corners and no border. Contains a 1:1 aspect ratio product image with top-rounded corners, a title in `{typography.title-sm}`, and price in `{typography.price}`. A `{colors.accent-marigold}` badge may overlay the image corner for subscription savings.

**`feature-badge`** — Pill-shaped (`{rounded.full}`) badge with `{colors.surface-soft}` background and `{typography.caption}`. Used for "Plastic-Free," "Carbon Neutral," and "Vegan" feature callouts on product detail pages.

### Navigation
**`nav-bar`** — Fixed top nav at 64px height on desktop, 56px on mobile. Background is `{colors.canvas}` with a soft bottom border (`{colors.hairline-soft}`). Logo left, cart icon right. On mobile, the hamburger icon replaces any nav links.

**`nav-bar-mobile`** — Reduced height (56px) with hamburger and cart icons only. Logo remains centered or left-aligned.

### Forms
**`text-input`** — Standard input field with white background, `{rounded.sm}` corners, and a `{colors.hairline}` border. Focus state uses a 2px `{colors.primary}` border. Error state uses a 2px `{colors.social-pinterest}` (#cb2027) border.

**`select-dropdown`** — Matches `text-input` styling but with a dropdown arrow. Used for "Scent," "Size," and "Frequency" selectors on product pages.

**`checkbox`** — Square (`{rounded.xs}`) with 2px `{colors.hairline}` border. Checked state fills with `{colors.primary}`. Used in subscription preference forms and cart add-ons.

**`radio`** — Circular (`{rounded.full}`) with 2px `{colors.hairline}` border. Checked state shows a 6px `{colors.primary}` inner circle. Used for "One-Time" vs "Subscribe" toggle.

### Subscription Toggle
**`subscription-toggle`** — A segmented control with `{colors.surface-soft}` background and `{rounded.sm}` corners. Contains two options: "One-Time Purchase" and "Subscribe & Save." The active option gets `{colors.accent-teal-soft}` background with a 2px `{colors.accent-teal}` border. A `{colors.accent-marigold}` badge reading "Save up to 30%" appears next to the subscription option.

### Hero
**`hero-section`** — Full-width section with `{colors.canvas}` background, `{spacing.section}` vertical padding. Contains `hero-headline` (`{typography.display-xl}`, max-width 600px) and `hero-subheadline` (`{typography.body-md}`, `{colors.body}`, max-width 500px). Used on homepage and category landing pages.

### Footer
**`footer-section`** — Dark footer with `{colors.ink}` background and white text. Contains columns of `footer-link` items in `{colors.muted-soft}` and `footer-heading` titles in white. Trust badges for carbon-neutral shipping, plastic-free packaging, and B Corp certification sit at the bottom.

### Quantity Selector
**`quantity-selector`** — Horizontal control with `{colors.surface-soft}` background and `{rounded.sm}` corners. Contains left/right `quantity-button` elements (36x36px) and a centered `quantity-input` (40px wide). Used on cart and product detail pages.

### Accordion
**`accordion-header`** — Clickable row with `{colors.ink}` text in `{typography.title-sm}`, no background, and a soft bottom border. Used for FAQ sections and product details (ingredients, usage, shipping). `accordion-content` reveals below with `{typography.body-sm}` in `{colors.body}`.

### Toast Notifications
**`toast-success`** — Green toast (`{colors.accent-teal}`) with white text, `{rounded.sm}` corners, and 12px/16px padding. Used for "Added to Cart" and subscription confirmation messages.

**`toast-error`** — Red toast (`{colors.social-pinterest}`) with white text. Used for out-of-stock notifications and payment failures.

### Modal
**`modal-overlay`** — Semi-transparent black overlay (60% opacity) behind modal content. `modal-content` is white with `{rounded.lg}` corners and 32px padding. A `modal-close` icon button sits in the top-right corner.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger + cart only. Product cards stack in single column. Hero section reduces padding to 32px. Footer columns stack vertically. Subscription toggle switches to full-width buttons. Quantity selector reduces to smaller touch targets. |
| Tablet | 744–1128px | Nav bar shows logo + cart only (no nav links). Product cards display in 2-column grid. Hero headline reduces to 28px. Footer shows 2-column layout. |
| Desktop | 1128–1440px | Full nav bar with links. Product cards in 3-column grid. Hero at full size. Footer in 4-column layout. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. Hero content max-width increases to 700px. |

### Touch Targets
- All buttons and interactive elements minimum 44px height (exceeds Apple HIG 44pt minimum).
- Quantity selector buttons are 36x36px — slightly below recommended 44px but acceptable for non-primary interactions.
- Checkbox and radio inputs are 20x20px with 44px tap area via padding.
- Hamburger icon and cart icon have 44x44px tap targets via padding.
- Accordion headers are full-width with minimum 44px tap height.

### Collapsing Strategy
- Nav links collapse into hamburger menu below 1128px.
- Product card grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks.
- Hero section reduces vertical padding by 50% on mobile.
- Subscription toggle switches from horizontal segmented control to stacked full-width buttons on mobile.
- Accordion content remains collapsed by default on all breakpoints.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons not fully extracted — assumed standard opacity/border changes.
- Error styling for form inputs inferred from common patterns; actual error message styling (color, position, icon) not confirmed.
- Dark mode not present on live site — no `prefers-color-scheme` media queries detected.
- Sub-brand or collection-specific palettes (e.g., "Free & Clear" vs "Fresh Scent" product lines) not extracted.
- Animation and transition timing values (e.g., button hover duration, accordion slide speed) not available.
- Font weights beyond 400, 500, 600, 700 not confirmed for Inter and Silka — assumed standard variable font support.
- Actual font sizes for display and body text inferred from common Shopify patterns; may vary by page template.
- Spacing values for specific components (e.g., product card padding, footer column gaps) estimated from layout analysis.
- Checkout flow styling (Shopify checkout override) not extracted — may use default Shopify theme.
- Accessibility contrast ratios not verified against WCAG 2.1 AA standards.
- Custom dropdown arrow icon not extracted — assumed default browser or SVG icon.
- Star rating component (if present on reviews) not found in extracted data.
- Loading skeleton or placeholder states for product images not observed.
