---
version: alpha
name: "Supergiant Games Store"
source_url: "https://store.supergiantgames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A storefront that feels less like a shop and more like a developer’s personal table at a convention, built on a foundation of soft, airy pastels and the quiet confidence of a studio that lets its games speak first. The palette is anchored not by a single brand color but by a constellation of gentle tones — `#c1e9ff` and `#e1fcff` read as morning sky, `#eceafb` and `#f0edfe` as faint lavender, `#bde7ff` as a slightly deeper breath of blue — all set against a `#f4f5f6` canvas that is barely-there warm gray. The most distinctive accent, `#5b5b5b`, a warm dark charcoal, serves as the primary ink for body copy and UI text, avoiding the harshness of pure black and keeping the overall mood soft and approachable. Buttons and interactive elements use `{rounded.full}` pill shapes, echoing the friendly, hand-drawn quality of Supergiant’s character art. The typography runs Shopify Sans Medium and Regular, a clean, modern sans-serif that stays out of the way of the product photography and game key art. There are no hard corners on CTAs or badges — every interactive edge is softened, every surface feels like it’s been lightly brushed. The store’s design trusts the emotional weight of the game worlds (the warm golds of *Hades*, the neon pinks of *Transistor*, the deep greens of *Bastion*) to provide the visual drama, while the UI itself remains a calm, neutral container. This is a store that knows its audience is here for the art and the story, not the checkout flow.

colors:
  primary: "#5b5b5b"
  primary-active: "#3d3d3d"
  primary-disabled: "#b0b0b0"
  ink: "#5b5b5b"
  body: "#5b5b5b"
  muted: "#8a8a8a"
  muted-soft: "#a0a0a0"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#f4f5f6"
  surface-soft: "#f0f1f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sky: "#c1e9ff"
  accent-lavender: "#eceafb"
  accent-mint: "#e1fcff"
  accent-deep-sky: "#bde7ff"
  accent-soft-lavender: "#f0edfe"
  accent-warm-lavender: "#e9e8fb"
  accent-light-cyan: "#ecf7fc"

typography:
  display-xl:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  badge-new:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  cart-line-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    padding: "{spacing.base} 0"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 52px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button with `{rounded.full}` corners and a `{colors.primary}` dark charcoal background. Text is white (`{colors.on-primary}`) set in `{typography.button-md}`. On hover, the background shifts to `{colors.primary-active}` (#3d3d3d). The disabled state uses `{colors.primary-disabled}` (#b0b0b0) with reduced opacity. Padding is 12px top/bottom and 28px left/right, giving it a comfortable, substantial feel.

**`button-secondary`** — A bordered pill button with a white background (`{colors.surface-card}`), `{colors.ink}` text, and a 2px `{colors.hairline}` border. On hover, the border thickens in visual weight by switching to `{colors.ink}`. Same `{rounded.full}` shape and `{typography.button-md}` sizing as the primary, maintaining visual consistency across the action hierarchy.

**`button-tertiary-text`** — A text-only button with no background or border, using `{typography.button-md}` in `{colors.ink}`. On hover, the text color shifts to `{colors.primary-active}`. Used for secondary actions like "Cancel" or "View details" where a full button would be too heavy.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` (12px) corners and `{spacing.base}` (16px) padding. The product image sits at the top with `{rounded.sm}` (8px) corners and a 1:1 aspect ratio. Below, the title uses `{typography.title-md}` and the price uses `{typography.body-md}` in `{colors.body}`. On hover, the card lifts with a subtle box-shadow (0 4px 12px rgba(0,0,0,0.08)), creating a gentle elevation effect.

### Navigation
**`nav-bar`** — A fixed-height (64px) top bar on a `{colors.canvas}` background, separated from the page content by a 1px `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` (14px, medium weight) in `{colors.ink}`. The bar is intentionally minimal — no background color shift, no heavy shadows — keeping focus on the store content.

### Forms
**`text-input`** — A standard text input with a white background, `{colors.body}` text, `{rounded.sm}` (8px) corners, and a 1px `{colors.hairline}` border. Padding is 12px vertical and 16px horizontal, with a height of 48px to match button sizing. On focus, the border switches to `{colors.ink}` for clear visual feedback.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-limited`** — Small, pill-shaped (`{rounded.full}`) labels used to tag products with status indicators. Each uses a different accent color from the palette: `{colors.accent-sky}` for "New", `{colors.accent-lavender}` for "Sale", and `{colors.accent-mint}` for "Limited". Text is set in `{typography.badge}` (11px, uppercase, medium weight) in `{colors.ink}`, with 2px vertical and 8px horizontal padding.

### Footer
**`footer`** — A full-width footer on a `{colors.canvas}` background, separated from the main content by a 1px `{colors.hairline-soft}` top border. Text uses `{typography.body-sm}` in `{colors.muted}`. Links use `{typography.link}` in `{colors.muted}`, shifting to `{colors.ink}` on hover. Padding is `{spacing.xxl}` (48px) vertical and `{spacing.lg}` (24px) horizontal.

### Cart & Checkout
**`cart-line-item`** — A horizontal row in the cart showing product details, quantity, and price. Uses `{typography.body-sm}` in `{colors.ink}` on a white background, with `{spacing.base}` (16px) vertical padding and a 1px `{colors.hairline-soft}` bottom border between items.

**`quantity-selector`** — A compact, bordered control for adjusting item quantities. Uses `{rounded.sm}` (8px) corners, a 1px `{colors.hairline}` border, and 40px height. The plus/minus buttons are square (40x40px) with transparent backgrounds, sitting flush within the selector container.

**`checkout-button`** — The primary checkout CTA, styled identically to `button-primary` but full-width (100%) and slightly taller (52px) for emphasis. Uses `{rounded.full}` pill shape and `{colors.primary}` background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row). Nav bar collapses to hamburger menu. Hero section reduces padding to `{spacing.lg}`. Product card images remain 1:1 but scale to full width. Footer links stack vertically. |
| Tablet | 744–1128px | Two-column product grid. Nav bar shows limited links (store, cart, account). Hero section uses `{spacing.xl}` padding. Product cards show in a 2-column layout. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all links visible. Hero section uses `{spacing.section}` padding. Standard layout as designed. |
| Wide | > 1440px | Four-column product grid. Content max-width capped at 1440px, centered with auto margins. Hero section remains full-width with max-width content container. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Quantity selector buttons are 40x40px, meeting the 44px tap target recommendation when accounting for padding.
- Nav bar links have a minimum 44px tap area (height 64px with vertical centering).
- Product card tap targets (title, price, image) are nested within the card's clickable area.

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger menu icon. All navigation links move to a slide-out drawer.
- The product grid collapses from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile).
- Footer link columns stack vertically on mobile, becoming a single column of links.
- Hero section text reduces font size on mobile (`{typography.display-xl}` drops to `{typography.display-md}` equivalent).
- Badges remain visible on all breakpoints but may truncate text on very small screens (e.g., "Limited Edition" becomes "Limited").

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors are heavily weighted toward pastel blues, lavenders, and grays, which may include Shopify checkout-widget colors (Shopify Pay, Klarna, Afterpay) and stock-image dominant tones. The true brand palette for Supergiant Games may include warmer, game-specific accent colors (e.g., the golds and reds from *Hades*, the pinks from *Transistor*) that were not captured in the extraction. The `{colors.primary}` of `#5b5b5b` was chosen as the most distinctive non-pastel color in the list, but this may not be the brand's intended primary.
- Hover and focus states for all components are inferred from common patterns; actual extracted hover/focus styles were not available.
- Error styling (form validation, error messages, empty states) was not extracted.
- Dark mode or high-contrast mode styles are not documented.
- Sub-brand or game-specific color palettes (e.g., *Hades* gold, *Transistor* pink) are not included.
- Font weights beyond "Medium" (500) and "Regular" (400) were not found; the brand may use additional weights (e.g., Bold, Light) that were not extracted.
- The `font-family` declarations found ("Shopify Sans Medium", "Shopify Sans Regular") may be Shopify platform defaults rather than intentional brand choices. The brand may use a custom or different typeface for display headings.
- Spacing and sizing values (padding, heights, border widths) are estimated based on common Shopify store patterns and may not match the exact live implementation.
- The `page title` extracted ("Maak een e-commercewebsite...") is a Shopify default in Dutch, indicating the extraction may have captured a non-customized or default template state. The actual brand may have customized titles and meta descriptions.
- No meta theme-color was extracted, suggesting the brand may not have set one, or it was not captured.
- The extracted data may represent a default Shopify "Dawn" theme or similar, rather than a fully custom Supergiant design. The design system above assumes a custom implementation but notes this uncertainty.
