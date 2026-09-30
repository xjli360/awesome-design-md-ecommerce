---
version: alpha
name: "The Laundress"
source_url: "https://thelaundress.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, dusty terracotta (#8c564b) anchors a brand that treats laundry as a ritual of care rather than a chore — this singular brown-rose appears on every primary CTA, product badge, and checkout button, grounding the experience in a warmth that feels more like a heritage apothecary than a detergent company. The palette pairs this earthy anchor with a soft lavender (#413389) used sparingly for sale tags and editorial accents, while a clean white canvas (#f0f0f0) and near-black ink (#121212) keep the system legible and premium. Typography runs a deliberate contrast: Bodoni Moda and Didot LT Pro for display — serifed, editorial, recalling a 1950s French laundry manual — paired with Futura and Jost for body and buttons, their geometric sans-serif forms adding a crisp, modern utility. Product cards use a generous {rounded.md} with soft shadows, while buttons round at {rounded.sm}, never fully pill-shaped, preserving a tailored, not playful, personality. The top nav is a simple, centered logo on white with a thin {colors.hairline} bottom border — no mega-menu, no search bar, just a single "Shop" dropdown and a cart icon. The brand trusts its product photography (bottles on marble, linen in sunlight) over illustration or pattern, letting the #8c564b bottle cap and label do the heavy lifting of recognition.

colors:
  primary: "#8c564b"
  primary-active: "#73443a"
  primary-disabled: "#d4b9b2"
  ink: "#121212"
  body: "#2d2d2d"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f0f0f0"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lavender: "#413389"
  accent-sage: "#2ca02c"
  accent-gold: "#bcbd22"
  star-rating: "#121212"
  error: "#d62728"
  sale-badge: "#413389"
  new-badge: "#8c564b"

typography:
  display-xl:
    fontFamily: "'Bodoni Moda', 'Didot LT Pro', Georgia, serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Bodoni Moda', 'Didot LT Pro', Georgia, serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Bodoni Moda', 'Didot LT Pro', Georgia, serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  body-lg:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  product-name:
    fontFamily: "'Bodoni Moda', 'Didot LT Pro', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  product-price:
    fontFamily: "'Futura', 'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-info:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-name:
    typography: "{typography.product-name}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 28px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 48px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "0 12px"
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-heading:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in {colors.primary} (#8c564b) with white text and uppercase Futura tracking at 1px. On hover, it deepens to {colors.primary-active} (#73443a). The disabled state fades to {colors.primary-disabled} (#d4b9b2), a muted rose that signals unavailability without visual noise. Padding is generous (14px 28px) to match the brand's unhurried, premium feel.

**`button-secondary`** — An outlined variant on a white background with a {colors.hairline} border. Active state swaps the border to {colors.ink} and the background to {colors.surface-soft}. Used for "Add to Cart" on product pages and secondary form actions.

**`button-tertiary-text`** — A text-only button in {colors.primary} with no background or border. Used for "Learn More" links and inline actions. Active state shifts to {colors.primary-active}.

### Text Inputs & Forms
**`text-input`** — Standard form field with a white background, {colors.hairline} border, and {rounded.sm}. On focus, the border switches to {colors.primary}. Error state uses {colors.error} (#d62728) for the border. Placeholder text is {colors.muted-soft} (#9e9e9e). Height is 48px for comfortable touch interaction.

**`select-dropdown`** — Matches the text-input styling but includes a custom dropdown arrow. Used for size, quantity, and filter selections.

**`newsletter-input`** — A dedicated input for the email signup in the footer, styled identically to text-input but paired with a {colors.primary} submit button.

### Navigation
**`top-nav`** — A clean, minimal bar at 72px height with a white background and a single {colors.hairline} bottom border. The logo sits centered, flanked by "Shop" (with dropdown) on the left and a cart icon on the right. No search bar in the top nav — search is relegated to a dedicated page or footer.

**`nav-link`** — Uppercase Futura at 14px with 0.5px letter-spacing. Active state uses {colors.primary}. The dropdown menu (`nav-dropdown`) appears on hover with a soft shadow and white background.

### Product Cards
**`product-card`** — A white card with {rounded.md} (12px) and no border — the product image does the heavy lifting. The image area rounds at the top corners only, while the info section below uses {spacing.base} padding on sides and {spacing.lg} at the bottom. Product name is set in Bodoni Moda at 18px, price in Futura at 16px.

**`product-card-badge`** — A small {rounded.xs} badge in {colors.new-badge} (#8c564b) for "New" items, or {colors.sale-badge} (#413389) for sale items. Text is uppercase Futura at 11px.

### Hero & Section Headers
**`hero-banner`** — A full-width section on {colors.canvas} (#f0f0f0) with generous padding ({spacing.section} top/bottom). The heading uses {typography.display-xl} (Bodoni Moda, 42px), the subheading uses {typography.body-lg} (Futura, 18px), and the CTA is a {colors.primary} button.

**`section-heading`** — Uppercase Futura at 20px with 0.5px letter-spacing, used for "Best Sellers", "New Arrivals", and editorial sections. Includes {spacing.section} top padding to create visual breathing room.

### Footer
**`footer`** — A full-width section on {colors.canvas} with {colors.body} text. Links are Futura at 14px with a hover state in {colors.primary}. The newsletter signup sits prominently in the footer with a dedicated input and submit button.

### Accordion
**`accordion-trigger`** — Used for FAQ sections and product details (ingredients, instructions). The trigger is uppercase Futura at 16px with a {colors.hairline} bottom border. Content area uses {typography.body-md} with {spacing.sm} top padding.

### Quantity Selector
**`quantity-selector`** — A compact control with a white background, {colors.hairline} border, and {rounded.sm}. The plus/minus buttons are text-only with no background. Used on product pages and cart.

### Cart Icon & Badge
**`cart-icon`** — A simple outline icon at 24px height in {colors.ink}. The `cart-count-badge` is a small {rounded.full} pill in {colors.primary} with white text, positioned at the top-right of the icon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero padding reduces to {spacing.xl}; section-heading font-size drops to 18px; footer links stack; newsletter input and button stack vertically |
| Tablet | 744–1128px | Two-column product grid; top-nav remains visible but "Shop" dropdown becomes a tap-to-open; hero uses 32px display font; section padding at {spacing.xl} |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with hover dropdowns; hero at full 42px display; section padding at {spacing.section} |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to four columns if needed; hero remains centered with max-width on text |

### Touch Targets
- All buttons and interactive elements maintain a minimum 48px height for touch accessibility
- Nav links have 44px minimum touch area (padding + height)
- Quantity selector buttons are 48px tall with 44px wide touch targets
- Accordion triggers have 48px minimum touch height

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px; the "Shop" dropdown becomes a full-screen overlay
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Footer sections stack vertically on mobile; newsletter input and button stack instead of sitting inline
- Hero banner reduces padding and font size on mobile; CTA button remains full-width
- Accordion content collapses by default on all breakpoints; triggered by tap/click

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors include many that appear to be Shopify checkout widget defaults (e.g., #1f77b4, #ff7f0e, #2ca02c, #d62728, #9467bd, #e377c2, #7f7f7f, #bcbd22, #17becf, #ffbb78, #98df8a, #ff9896) — these are likely from payment icons (Afterpay, Klarna, PayPal) and have been excluded from the palette. The true brand palette appears to be #8c564b (primary terracotta), #dedede (hairline), #413389 (accent lavender), #f0f0f0 (canvas), and #121212 (ink).
- Hover and focus states for all components are inferred from common DTC patterns; actual extracted hover colors were not available.
- Error styling (text-input-error, form validation messages) is based on standard patterns; brand-specific error colors were not extracted.
- Dark mode is not supported by the current site; no dark-mode tokens are defined.
- Sub-brand or seasonal palette variations (e.g., holiday packaging, limited editions) were not extracted.
- The exact font weights and sizes for Bodoni Moda and Didot LT Pro are inferred from typical usage; the site may use specific weights not captured.
- The `textTransform: uppercase` on many typography tokens is inferred from the brand's use of Futura in headings and buttons; actual CSS may vary.
- The `product-card-badge` and `sale-badge` colors (#8c564b and #413389) are inferred from the extracted palette; actual badge colors on the live site may differ.
- The `star-rating` color is set to {colors.ink} as a default; the actual star color on product pages was not extracted.
- The `search-bar` component is inferred to exist based on common ecommerce patterns; the actual search implementation on the site may differ.
- The `accordion` component is inferred from common product-detail patterns; the site may use tabs or other disclosure patterns.
- The `quantity-selector` styling is inferred from standard ecommerce patterns; actual implementation may vary.
