---
version: alpha
name: "Puracy"
source_url: "https://puracy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cleaning brand that wraps its plant-based chemistry in a palette of deep teal (#035c68) and sage green (#6fac83), where the primary color reads less like a corporate blue and more like a tide pool at dusk. That teal anchors every primary CTA, the site header, and the product-badge system, while the sage surfaces as a secondary accent on hover states and illustrative backgrounds. The canvas is a soft off-white (#f1f6f6) rather than pure white, giving the entire experience a humid, botanical warmth — like a clean kitchen after steam has settled. Typography runs Figtree and Jazmin, the former doing heavy lifting for body and button copy at modest 400–500 weights, the latter appearing in display contexts with a slightly condensed, modern sans-serif feel. Product cards use generous padding and a subtle hairline (#eeeeee) that barely registers; the brand trusts ingredient photography and white space over decorative borders. Badges for "Plant-Based" and "Free & Clear" sit in small pill shapes with the teal as fill, and the footer collapses into a dense, link-heavy grid on a darker teal ground (#134048). The overall mood is earnest, scientific but not clinical — a brand that wants you to feel good about what you're spraying on your countertops.

colors:
  primary: "#035c68"
  primary-active: "#134048"
  primary-disabled: "#b3d4d8"
  ink: "#134048"
  body: "#3d5a5e"
  muted: "#6a8a8e"
  muted-soft: "#9bb5b8"
  hairline: "#eeeeee"
  hairline-soft: "#f1f1f1"
  canvas: "#f1f6f6"
  surface-soft: "#f9fbf0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#6fac83"
  accent-sage-soft: "#c4dfcb"
  badge-plant: "#6fac83"
  badge-free: "#035c68"
  footer-bg: "#134048"
  footer-text: "#b3d4d8"

typography:
  display-xl:
    fontFamily: "'Jazmin', 'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Jazmin', 'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.15px
  link:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Figtree', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-badge:
    backgroundColor: "{colors.badge-plant}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-badge-free:
    backgroundColor: "{colors.badge-free}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 0
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Shop Now" actions. Filled with the deep teal `{colors.primary}` and white text, it sits on a 44px height with 12px vertical padding and 24px horizontal. On hover, it shifts to the darker `{colors.primary-active}`. The disabled state uses a muted teal `{colors.primary-disabled}`.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a 2px solid border of `{colors.primary}` on a transparent background. On hover, the background fills with `{colors.surface-soft}` and the border darkens to `{colors.primary-active}`.

**`button-sage`** — A smaller, accent-toned button using `{colors.accent-sage}` for actions like "Free Sample" or "Get Offer". Uses `{typography.button-sm}` at 38px height, appearing as a lighter, friendlier alternative to the primary button.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.md}` corners and 16px padding. The product image sits inside with `{rounded.sm}` corners. Text uses `{typography.body-sm}` for the product name and price. The card has no border — it relies on the white surface against the `{colors.canvas}` background for separation.

**`product-badge`** — Small pill-shaped labels that sit on product cards or images. The "Plant-Based" badge uses `{colors.accent-sage}` fill, while the "Free & Clear" badge uses `{colors.badge-free}`. Both use `{typography.badge}` with uppercase tracking and 4px/10px padding.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on `{colors.canvas}` background. Navigation links use `{typography.nav-link}` at 14px with 500 weight. The active state underlines with a 2px `{colors.primary}` border. The bar contains the logo, main links (Shop, About, Ingredients), and a cart icon.

**`search-bar`** — A pill-shaped search input with `{rounded.full}` corners, 48px height, and a 1px `{colors.hairline}` border. Used in the header for product search, with placeholder text in `{colors.muted}`.

### Footer
**`footer-section`** — A dark teal `{colors.footer-bg}` footer with `{colors.footer-text}` links. Organized in a multi-column grid with headings for "Shop", "Learn", "Support", and "Connect". Links hover to white `{colors.on-primary}`. The footer includes a newsletter signup with a `{colors.accent-sage}` submit button.

### Forms
**`text-input`** — Standard form input for checkout, subscription, and contact forms. Uses `{colors.canvas}` background with a 1px `{colors.hairline}` border. On focus, the border thickens to 2px of `{colors.primary}`. Height is 44px with 12px/16px padding.

### Accordion
**`accordion-header`** — Used in FAQ and ingredient detail sections. A clickable row with `{typography.title-md}` and 16px vertical padding. The content area below uses `{typography.body-sm}` with no top padding, creating a clean reveal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-md}`; footer stacks to single column; product cards use full width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero retains `{typography.display-xl}`; footer in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full width with `{typography.display-xl}`; footer in four columns |
| Wide | > 1440px | Max-width container at 1440px; product grid remains three-column; hero content centered with max-width |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links have 48px tap area on mobile
- Accordion headers have 48px minimum tap height
- Icon buttons (cart, search, hamburger) are 40px circles with 44px tap area

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, to 1 at mobile
- Footer collapses from 4 columns to 2 at tablet, to 1 at mobile
- Hero section reduces font size and padding at mobile
- Search bar moves from inline to full-width overlay on mobile
- Accordion content collapses by default on all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are limited to 7 values; the brand may use additional accent colors (e.g., for seasonal promotions or specific product lines) that weren't captured
- Font-family declarations include "Jazmin" and "Figtree" but exact weight assignments for display vs. body text are inferred from common usage patterns
- Hover and focus states for text inputs, links, and secondary buttons are inferred from the primary color system
- Error state styling for forms (red borders, error messages) was not extractable
- Dark mode is not present on the live site; no dark palette tokens are defined
- The "Free & Clear" badge color is assumed to match the primary teal based on brand consistency, but may have a distinct hex
- Checkout flow (Shopify-powered) may use platform-default button styles that differ from the brand system
- Social media icon colors and Afterpay/Klarna widget colors were filtered from extraction and may not reflect brand intent
