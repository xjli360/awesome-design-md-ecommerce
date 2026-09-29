---
version: alpha
name: "Lemme"
source_url: "https://lemmelive.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A vitamin and supplement brand that wraps functional wellness in a pastel-lavender glow, anchored by `#f7f1f9` — a chalky lilac that reads more like a powdered-sugar dusting than a medical aisle. The brand's true voltage comes from `#a5f057`, an electric lime-green that appears on CTAs, badges, and accent elements, creating a jolt of unexpected energy against the soft violet canvas. Type pairs Recoleta — a warm, serifed display face with generous curves — against Assistant, a clean sans-serif for body copy, giving the system a hybrid personality: editorial warmth meets clinical clarity. Product cards use `{rounded.lg}` corners and sit on `#f4f4f6` surfaces, while the primary ink `#272d45` (a deep navy) provides contrast without the harshness of pure black. The checkout flow and trust badges introduce `#3b31ce` and `#0e7a82` — a deep indigo and teal — suggesting a sub-brand or payment-partner layer. What makes Lemme distinctive is the tension between `#f7f1f9`'s softness and `#a5f057`'s neon punch: the brand feels like a wellness studio that happens to sell pills, not a supplement company trying to look clinical. The `{rounded.full}` pill shape appears on primary buttons and ingredient badges, reinforcing the product form factor itself.

colors:
  primary: "#a5f057"
  primary-active: "#8cdb3a"
  primary-disabled: "#d4f7b0"
  ink: "#272d45"
  body: "#676986"
  muted: "#9a9bb0"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5eb"
  hairline-soft: "#f4f4f6"
  canvas: "#f7f1f9"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#272d45"
  accent-lavender: "#dfc8ef"
  accent-lavender-soft: "#dfc8e7"
  accent-lime-soft: "#c5ff89"
  accent-magenta: "#f57eb6"
  accent-yellow: "#fbe01a"
  accent-red: "#ec3a42"
  accent-indigo: "#3b31ce"
  accent-teal: "#0e7a82"
  star-rating: "#fbe01a"
  error: "#ec3a42"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Mier A', arial, helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-lime:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    position: "top-left"
  product-card-badge-sold-out:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    position: "top-left"
  ingredient-badge:
    backgroundColor: "{colors.accent-lavender-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  ingredient-badge-lime:
    backgroundColor: "{colors.accent-lime-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  star-rating:
    color: "{colors.star-rating}"
    size: "16px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.surface-card}"
  footer-link-hover:
    textColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 48px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} {spacing.lg} {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  checkout-button:
    backgroundColor: "{colors.accent-indigo}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 52px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a pill-shaped button in electric lime `#a5f057` against deep navy `#272d45` text. On hover, shifts to `#8cdb3a`; disabled state fades to `#d4f7b0`. Used for "Add to Cart", "Subscribe & Save", and primary checkout actions. The pill shape (`{rounded.full}`) echoes the supplement capsule form factor.

**`button-secondary`** — An outlined pill button on the lavender canvas `#f7f1f9` with a `#e5e5eb` hairline border. Active state gains a `#272d45` border. Used for "Learn More", "View Details", and secondary navigation actions.

**`button-tertiary-text`** — A text-only button with no background or border, using the same `{typography.button-md}` weight. Used for "Cancel", "Skip", and inline links within product descriptions.

**`button-pill-lime`** — A smaller pill button in the primary lime, used for ingredient tags, filter chips, and quick-add actions on product cards.

**`button-pill-lavender`** — A smaller pill button in `#dfc8ef`, used for "Sold Out" badges, informational tags, and category filters.

### Navigation
**`top-nav`** — A fixed-height 72px bar on the lavender canvas `#f7f1f9`. Logo sits left, nav links center, cart and account icons right. Active nav link has a 2px bottom border in `#a5f057`. On scroll, the nav gains a subtle shadow and the background shifts to `#ffffff` for contrast.

**`nav-link-active`** — Underlined with the lime accent; text in deep navy `#272d45`.

**`nav-link-inactive`** — Muted body color `#676986`, no underline.

### Cards
**`product-card`** — A white card with `{rounded.lg}` (20px) corners, containing a 1:1 product image with matching top-radius rounding. Title uses `{typography.title-sm}` in `#272d45`, price in `{typography.body-md}` in `#676986`. Badges overlay at the top-left corner.

**`product-card-badge`** — A lime pill badge for "New", "Best Seller", or "Limited Edition" labels.

**`product-card-badge-sold-out`** — A lavender pill badge for "Sold Out" or "Coming Soon" states.

### Forms
**`text-input`** — Standard input with white background, `{rounded.sm}` (8px) corners, and a `#e5e5eb` border. Focus state swaps to a 2px `#a5f057` border. Error state uses 2px `#ec3a42` border.

**`search-bar-pill`** — A pill-shaped search input with white background and `#e5e5eb` border. Focus state gains a 2px lime border. Used for product search and ingredient lookup.

**`newsletter-input`** — A pill-shaped email input in the footer, white background, paired with a lime submit button.

### Footer
**`footer`** — A deep navy `#272d45` section with white text. Links are `{typography.link}` in white, hover to lime `#a5f057`. Contains brand info, product links, support links, and newsletter signup.

### Badges & Tags
**`ingredient-badge`** — A small lavender pill tag used to highlight ingredients (e.g., "Probiotics", "Vitamin C", "Ashwagandha").

**`ingredient-badge-lime`** — A lime variant for hero ingredients or "Key Active" labels.

### Cart & Checkout
**`cart-item`** — A white card row with bottom hairline separator. Contains product image, name, quantity selector, and price.

**`quantity-selector`** — A pill-shaped control on `#f4f4f6` background with minus/plus buttons and a centered number.

**`checkout-button`** — A deep indigo `#3b31ce` button with white text and `{rounded.sm}` corners. Used specifically in the checkout flow, likely for Shopify Payments integration.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 32px; buttons become full-width; product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded; hero uses 48px padding; search bar appears in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 64px padding; sticky nav on scroll |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero centered with generous margins |

### Touch Targets
- All buttons and interactive elements minimum 44px height (exceeds WCAG 2.1 2.5.5)
- Icon buttons 40px × 40px minimum
- Quantity selector plus/minus buttons 36px × 36px
- Nav links have 48px tap area (padding extends hit area)
- Product card CTAs 52px height for easy tapping

### Collapsing Strategy
- Top nav collapses to hamburger icon at < 744px, revealing a full-screen overlay menu
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces heading from 48px to 32px on mobile
- Footer links collapse into accordion sections on mobile
- Search bar hides behind an icon on mobile, expands to full-width overlay when tapped
- Product description accordion collapses all sections by default on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button hover (`#8cdb3a`) and footer link hover (`#a5f057`) were extractable. Secondary button, text input, and card hover states are inferred from common patterns but not confirmed.
- **Error styling**: Error state for text inputs uses `#ec3a42`, but error message typography, iconography, and animation timing are unknown.
- **Dark mode**: No dark mode detected on the live site. The brand may not support it.
- **Sub-brand palettes**: The extracted colors include `#3b31ce` (indigo) and `#0e7a82` (teal) which appear in checkout widgets and trust badges — these may be Shopify Pay / Afterpay / Klarna colors rather than brand tokens.
- **Social icon colors**: `#f57eb6` (magenta), `#fbe01a` (yellow), `#ec3a42` (red), and `#ff4736` (orange-red) may be social platform brand colors (Instagram, Snapchat, YouTube, Pinterest) rather than Lemme's design tokens.
- **Animation**: No animation timing, easing curves, or transition durations were extractable. The brand likely uses subtle fades and slides but specifics are unknown.
- **Typography scale**: Font sizes for display-xl (48px), display-lg (36px), display-md (28px), and display-sm (24px) are estimated from common Recoleta usage patterns. Actual values may vary by viewport.
- **Spacing scale**: The spacing tokens are based on common 4px/8px systems. Actual component padding may differ.
- **Component states**: Focus-visible outlines, active press states, and disabled opacity values are not extractable from static HTML/CSS.
- **Checkout flow**: The `checkout-button` uses `#3b31ce` which may be a Shopify Payments default rather than a Lemme design decision.
- **Star rating**: `#fbe01a` (yellow) is used for star ratings, but the exact rendering (filled, half, empty states) is unknown.
