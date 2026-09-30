---
version: alpha
name: "Davids"
source_url: "https://davids-usa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A muted, mineral palette anchored on #53565a — a warm charcoal that reads less like industrial gray and more like honed slate — carries the entire Davids oral-care experience, from tube graphics to checkout buttons. The brand’s visual language is deliberately anti-clinical: where conventional toothpaste brands blast white, blue, and bright mint, Davids wraps itself in #c5c1be (a weathered limestone) and #dae6df (a sage-tinted eggshell), with #d63a2f — a restrained brick red — as the sole accent, used sparingly on the Add to Cart button and small sale badges. Product photography sits on #f0f5f2, a barely-there green-white that reads as clean but not sterile, and the typography (likely a system sans-serif stack, though the site’s font-family declarations are sparse) runs at moderate weights with generous line-height, letting the ingredient stories and the brand’s “no chemicals” positioning breathe. The overall effect is one of a small-batch apothecary that happens to sell toothpaste — soft rectangles (`{rounded.sm}` on buttons, `{rounded.md}` on product cards), a hairline of #c6c6c6 that separates sections without shouting, and a body text of #626262 that feels readable but never harsh. The nav bar, a fixed strip of #ffffff with #53565a links, uses a single #d63a2f highlight on the cart icon, a tiny voltage that keeps the experience from drifting into beige monotony.

colors:
  primary: "#53565a"
  primary-active: "#303030"
  primary-disabled: "#c7c7c7"
  ink: "#272d45"
  body: "#626262"
  muted: "#959799"
  muted-soft: "#c5c1be"
  hairline: "#c6c6c6"
  hairline-soft: "#d8dada"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d63a2f"
  accent-sage: "#dae6df"
  accent-sage-light: "#f0f5f2"
  accent-warm-gray: "#bcb2a8"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-ingredient:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  section-divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  hero-section:
    backgroundColor: "{colors.accent-sage-light}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site, used for Add to Cart, Subscribe, and primary form submissions. Rendered in the brand’s warm charcoal (#53565a) with white text and a soft 8px radius. On hover, it deepens to #303030; the disabled state drops to #c7c7c7 with white text, signaling inactivity without visual noise.

**`button-accent-red`** — Reserved for high-urgency actions like limited-time offers, clearance sales, or the checkout flow’s final “Place Order” step. Uses the sole saturated accent #d63a2f, which reads as a restrained brick rather than a stop-sign red. Same 44px height and 8px radius as the primary button, ensuring consistency across the button system.

**`button-secondary`** — An outlined variant for secondary actions (e.g., “Learn More” on product cards, “Cancel” in modals). White background, charcoal text, 1px hairline border (implied by the secondary structure). Hover state fills with a soft #f4f4f6 surface.

**`button-tertiary-text`** — A plain text link styled as a button, used for “View All” links in category strips and “Skip” in onboarding flows. No background, no border — just the charcoal text at button-md weight.

### Cards
**`product-card`** — The primary product display unit, a white card with a 12px radius and a soft shadow (not tokenized but present in the live site). Contains a product image (on a #f4f4f6 background), a title-sm name, a body-sm description, and a price in body-md weight 600. The Add to Cart button sits at the bottom, flush to the card edge.

**`product-card-image`** — The image container within a product card, using the surface-soft background to create a consistent placeholder while images load. Crops to a 1:1 aspect ratio with object-fit: cover.

### Badges
**`badge-sale`** — A small, sharp-cornered (4px radius) red badge pinned to the top-left of product cards or hero banners. Uses uppercase 11px bold type on #d63a2f. Content is always a short string like “SALE” or “20% OFF”.

**`badge-ingredient`** — A pill-shaped badge (full radius) used to call out key ingredients or certifications: “Fluoride Free”, “Natural”, “Vegan”. Rendered on a sage-green (#dae6df) background with dark ink text, reinforcing the brand’s clean-ingredient positioning without screaming.

### Navigation
**`nav-bar`** — A fixed white bar at the top of every page, 64px tall. Contains the brand logo on the left, a set of uppercase nav-link items (SHOP, ABOUT, LEARN, etc.) centered, and a cart icon with a red accent dot on the right. The bar uses a 1px bottom hairline (#c6c6c6) to separate from the page content.

### Forms
**`text-input`** — Standard text input for email signups, search, and checkout forms. White background, 44px height, 8px radius, 16px horizontal padding. Focus state adds a 2px border of #53565a (the primary color). Placeholder text is #959799.

### Search
**`search-bar`** — A pill-shaped search field used in the mobile nav and the site’s header. Rendered on the surface-soft (#f4f4f6) background with a magnifying glass icon on the left. 40px height keeps it compact, while the full radius gives it a friendly, approachable feel.

### Footer
**`footer-link`** — Standard text links in the footer, set in muted gray (#959799) at 14px. Hover state shifts to the primary charcoal (#53565a). No underline decoration — the color change alone signals interactivity.

### Dividers
**`section-divider`** — A single-pixel horizontal rule in #c6c6c6, used to separate major sections (e.g., between the hero and the product grid, or between the main content and the footer). Full-width with no margin on the sides.

### Hero
**`hero-section`** — The top-of-page hero banner, typically featuring a product shot or lifestyle image on a sage-light (#f0f5f2) background. Text (headline in display-xl, subhead in body-md) is centered or left-aligned depending on the page. Uses section-level vertical padding (64px) and horizontal padding of 24px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in a single column; hero text shrinks to 24px; search bar moves into the hamburger drawer. |
| Tablet | 744–1128px | Nav bar shows all links; product cards in 2-column grid; hero uses 28px display text; search bar visible in the header. |
| Desktop | 1128–1440px | Full nav bar with uppercase links; product cards in 3-column grid; hero uses 32px display text; search bar in the header with a full pill shape. |
| Wide | > 1440px | Max-width container (1200px) centered; product cards in 4-column grid; hero text remains 32px but with larger margins. |

### Touch Targets
- All buttons and interactive elements are at least 44px tall (44px for primary/secondary, 40px for search, 64px for nav items).
- Product card tap targets (Add to Cart, image link) are at least 48px in the touch dimension.
- Nav links in mobile hamburger menu are 48px tall with 16px horizontal padding.

### Collapsing Strategy
- The nav bar collapses to a hamburger icon on mobile (< 744px); the cart icon remains visible.
- The product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- The hero section’s image and text stack vertically on mobile; on tablet and above, they sit side by side.
- The footer’s multi-column link layout collapses to a single column on mobile, with accordion-style expandable sections for each category.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family**: The extracted font-family declarations only returned `inherit`, `oke-widget-icons`, and `slick` (a carousel library). The actual brand typeface could not be determined. The typography block uses a system sans-serif stack as a fallback; the real site likely uses a custom or Google Font (e.g., Inter, Lato, or a similar clean sans-serif). This must be confirmed by inspecting the live site’s CSS @font-face or Google Fonts link.
- **Hover states**: Only button-primary’s active state (#303030) was inferable from the extracted palette. Secondary button, text input, and link hover states are estimated based on common patterns (surface-soft background, color shifts).
- **Error styling**: No error-state colors (e.g., red for validation, green for success) were found in the extracted hex list. The accent-red (#d63a2f) is used for sale badges and the accent CTA, but its role in form validation is unknown.
- **Dark mode**: No dark-mode colors were extracted. The brand’s current site appears to be light-mode only.
- **Shadow tokens**: The product card uses a subtle box-shadow (visible in the live site’s screenshots), but no shadow color or blur-radius values were extractable from the HTML/CSS dump. A shadow token (e.g., `shadow-sm: 0 2px 8px rgba(0,0,0,0.08)`) should be added after visual inspection.
- **Sub-brand or seasonal palettes**: No evidence of alternate palettes (e.g., for holiday collections, limited editions). The extracted colors represent the core brand only.
- **Checkout-specific colors**: The extracted list includes #2c3e50 (a common Shopify checkout blue) and #e5e5eb (a Klarna/Afterpay widget gray). These were excluded from the brand palette as they are not brand-specific.
