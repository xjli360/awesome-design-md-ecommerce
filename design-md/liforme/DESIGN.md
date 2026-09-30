---
version: alpha
name: "Liforme"
source_url: "https://liforme.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A yoga equipment brand that stakes its identity on a single, unmistakable voltage: #ea5c8e, a hot pink that appears nowhere in nature but everywhere on the site — primary buttons, add-to-cart triggers, sale badges, and the thin accent line that runs along the top of every product photo. The brand pairs this pink with a near-black ink (#2d2d2d) for body text and a warm off-white canvas (#fef9ea) that reads as unbleached paper rather than sterile white, giving the whole experience a handcrafted, studio-lit feel. Typography runs Figtree at modest weights — display sits at 24–32px in weight 500, never shouting, while body copy stays at 14–16px with generous line height. Product cards use soft corners ({rounded.md}) and a subtle shadow, but the real signature move is the "sale" badge: a hot-pink pill ({rounded.full}) with white text that appears on nearly every product tile, creating a persistent sense of urgency. The nav bar is a dark band (#2d2d2d) with white links, a rare inversion that makes the header feel like a grounded anchor rather than a floating strip. Secondary actions — size selectors, quantity pickers — use a muted gray (#b1b0b8) border and no fill, keeping the visual hierarchy clean: pink means "act now," gray means "configure," white means "browse."

colors:
  primary: "#ea5c8e"
  primary-active: "#d44a7a"
  primary-disabled: "#f2dce5"
  ink: "#2d2d2d"
  body: "#504f60"
  muted: "#b1b0b8"
  muted-soft: "#c7c7c7"
  hairline: "#e7e5e5"
  hairline-soft: "#ebebeb"
  canvas: "#fef9ea"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#ea5c8e"
  sale-badge-text: "#ffffff"
  error: "#c44646"
  error-soft: "#ff0000"
  accent-dark: "#8f1354"
  accent-light: "#f192b3"
  accent-warm: "#fff4ce"

typography:
  display-xl:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Proxima Nova W05 Regular', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.muted-soft}"
  size-selector-active:
    border: "2px solid {colors.ink}"
    backgroundColor: "{colors.surface-soft}"
  quantity-picker:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call to action across the site, filled with #ea5c8e hot pink and white text. Used for "Add to Cart," "Shop Now," and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#d44a7a). Disabled state uses `{colors.primary-disabled}` (#f2dce5) with muted text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined button with a dark (#2d2d2d) border on the warm canvas background. Used for secondary actions like "View Details" or "Learn More." The 2px stroke keeps it visible without competing with the primary pink. Hover fills the background with `{colors.surface-soft}`.

**`button-tertiary-text`** — A text-only button in hot pink, used for "Cancel," "Clear Filters," or inline "Shop Sale" links. No background or border — just the brand voltage as a text link.

**`button-pill-sale`** — A tiny, fully rounded pill badge in hot pink with uppercase white text. Applied to product cards to mark discounted items. The badge sits at the top-left of the product image, creating a persistent urgency signal across the catalog.

### Cards
**`product-card`** — A white card with soft 12px corners and a subtle shadow. The image fills the top with matching corner radius on the top edges only. Below: title in `{typography.title-sm}`, price in `{typography.body-md}` (or sale price in hot pink if discounted), and a size selector row. The sale badge overlays the image at top-left when applicable.

**`product-card-badge`** — The hot pink pill that appears on sale items. Positioned absolutely over the product image, 8px from the top and left edges. Uses `{typography.badge}` (12px, bold, uppercase) for maximum legibility at small sizes.

### Navigation
**`nav-bar`** — A dark (#2d2d2d) horizontal bar, 64px tall, with white uppercase nav links. The logo sits left-aligned in white. Active links turn hot pink. The bar is fixed to the top of the viewport, creating a grounded anchor that contrasts with the warm canvas page background.

**`nav-link-active`** — Hot pink text on the dark nav background. Used for the current page or section. The color shift is the only indicator — no underline or background change.

### Forms
**`text-input`** — A warm canvas background input with a light gray (#e7e5e5) border and 12px padding. On focus, the border thickens to 2px and turns hot pink. Error state uses a red (#c44646) border. Used for email signup, search, and checkout fields.

**`size-selector`** — A compact 40px-tall button group for selecting mat size or thickness. Inactive options have a light gray border; the active option gets a 2px dark border and a light gray fill. The hot pink is deliberately absent here — size selection is a utility action, not a conversion action.

**`quantity-picker`** — A compact row with minus/plus buttons and a center number, bordered in light gray. Used on product detail pages. The buttons are text-only with no background fill.

### Footer
**`footer-section`** — A dark (#2d2d2d) full-width band with white body text. Links are light gray (#c7c7c7) and turn hot pink on hover. The footer contains columns for customer service, about links, social icons, and a newsletter signup form. The newsletter input uses the standard `text-input` style but with a hot pink submit button.

### Hero
**`hero-section`** — A full-width section on the warm canvas background, featuring a large headline in `{typography.display-xl}`, a supporting paragraph, and a single hot pink CTA button. No background image — the brand trusts the warm canvas and the pink button to create the visual anchor. The hero is centered with generous padding top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in single column. Hero text scales down to `{typography.display-md}`. Size selectors become full-width. Footer columns stack vertically. |
| Tablet | 744–1128px | Nav links remain visible but compact. Product cards display in 2-column grid. Hero maintains single-column layout with reduced padding. |
| Desktop | 1128–1440px | Full nav bar with all links. Product cards in 3-column grid. Hero has generous padding and larger display type. |
| Wide | > 1440px | Max-width container (1440px) centers content. Product cards in 4-column grid. Hero has maximum padding and largest type. |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px standard).
- Nav links have 48px tap targets on mobile (full height of nav bar).
- Size selectors and quantity pickers maintain 40px height with 44px minimum tap area.
- Product card images are tappable with no minimum size constraint (image fills card width).

### Collapsing Strategy
- On mobile, the nav bar collapses to a hamburger icon with a slide-out drawer.
- Product filters collapse into a "Filter" button that opens a modal overlay.
- Footer columns collapse from 4-column to single-column stacked layout.
- Size selector options collapse from row to vertical list on very small screens (< 480px).

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, image zoom) could not be reliably extracted from static CSS.
- Error message styling for form validation (color, iconography, position) was not visible in the extracted data.
- The exact shadow token values for product cards and modals are unknown — only presence was detected.
- Sub-brand or collection-specific palettes (e.g., "Pro" series, "Travel" mats) may exist but were not extracted.
- Dark mode is not supported — the brand uses a warm light canvas exclusively.
- The checkout flow uses Shopify's default widget colors (including #c44646 and #ff0000 for error states) which may not match the brand system.
- Social media icon colors (#504e60, #504f60) appear in the extracted list but are likely from SVG fills, not brand palette tokens.
- The exact font weight for Figtree at display sizes could not be confirmed — 500 is inferred from common usage patterns.
