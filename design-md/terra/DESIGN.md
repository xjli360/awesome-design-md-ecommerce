---
version: alpha
name: "Terra"
source_url: "https://terra.co.nz"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A New Zealand baby-care brand that paints its digital canvas in a warm, earthy palette anchored by the deep teal of #108474 — a primary that reads as clean water and native bush rather than the pastel pink or powder blue typical of the category. That teal is the brand's single voltage: it fills the primary button, the cart badge, the newsletter signup bar, and the floating "add to bag" orb. Against a backdrop of #eeeeee and #f9fafb surfaces, the accent system introduces two distinct energies — a marigold #fed716 for sale badges and promotional highlights, and a terracotta #de3813 for error states and urgent calls like "low stock" warnings. Typography runs Figtree at moderate weights (400–600), with display headlines at 24px weight 600 and body copy at 15px weight 400, creating a calm, readable hierarchy that never shouts. The product grid uses softly rounded cards (`{rounded.md}` ~12px) with generous padding (`{spacing.lg}` 24px) and a subtle hairline (`{colors.hairline}` #dedede) that separates items without visual noise. Every interactive element — from the pill-shaped search bar to the circular "add to cart" button — carries `{rounded.full}` treatment, reinforcing a brand ethos that is gentle, approachable, and distinctly Aotearoa.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#c1e6e6"
  ink: "#112233"
  body: "#555555"
  muted: "#6d7278"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fed716"
  accent-terracotta: "#de3813"
  accent-sage: "#12b985"
  accent-coral: "#ff7744"
  badge-sale: "#fed716"
  badge-new: "#12b985"
  badge-low-stock: "#de3813"
  star-rating: "#fed716"
  error: "#d02e2e"
  success: "#009900"
  review-highlight: "#a89cc8"
  scrim: "#151515"

typography:
  display-xl:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Figtree', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  review-stars:
    fontFamily: "'JudgemeStar', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
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
    outline: none
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(17,34,51,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(17,34,51,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(17,34,51,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.accent-terracotta}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
  badge-low-stock:
    backgroundColor: "{colors.badge-low-stock}"
    textColor: "{colors.on-primary}"
  badge-review:
    backgroundColor: "{colors.review-highlight}"
    textColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.md}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"
  newsletter-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.xl} {spacing.lg}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  footer-social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  footer-social-icon-hover:
    textColor: "{colors.canvas}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"
  cart-icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
  accordion-content:
    padding: "{spacing.sm} 0 {spacing.lg} 0"
  review-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  review-stars:
    typography: "{typography.review-stars}"
    color: "{colors.star-rating}"
  review-author:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  review-date:
    typography: "{typography.caption-sm}"
    color: "{colors.muted-soft}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-disabled:
    textColor: "{colors.muted-soft}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-link-hover:
    textColor: "{colors.primary}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  quantity-button-hover:
    backgroundColor: "{colors.surface-soft}"
  quantity-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: center
    width: 48px
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 52px
  add-to-cart-bar-active:
    backgroundColor: "{colors.primary-active}"
  floating-cart-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 56px
    width: 56px
    boxShadow: "0 4px 12px rgba(17,34,51,0.15)"
  floating-cart-orb-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    position: "top-right"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  toast-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  toast-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  toast-warning:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's teal `{colors.primary}` (#108474) and set in white Figtree weight 600. Rounded fully (`{rounded.full}`) to echo the brand's gentle, approachable ethos. On hover, shifts to `{colors.primary-active}` (#0d6b5d); disabled state uses `{colors.primary-disabled}` (#c1e6e6) with muted text. The `button-secondary` variant inverts to a white fill with a 2px teal border, while `button-tertiary-text` is a bare text link in teal. A `button-pill-accent` in marigold `{colors.accent-marigold}` (#fed716) with dark ink text is reserved for promotional actions like "Shop Sale" or "Claim Offer."

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners, subtle shadow (`0 1px 3px rgba(17,34,51,0.06)`), and `{spacing.base}` (16px) padding. The product image sits in a 1:1 aspect ratio with `{rounded.sm}` (8px) corners. Title uses `{typography.title-sm}` (14px weight 500), price uses `{typography.price}` (16px weight 600). Sale prices render in `{colors.accent-terracotta}` (#de3813). Badges overlay the image corner — `badge-sale` (marigold), `badge-new` (sage #12b985), `badge-low-stock` (terracotta). On hover, the card shadow deepens to `0 4px 12px rgba(17,34,51,0.1)`.

### Navigation
**`nav-bar`** — A 72px white bar with a single `1px solid {colors.hairline-soft}` (#eeeeee) bottom border. Nav links are 14px weight 500 Figtree in `{colors.muted}` (#6d7278) by default, shifting to `{colors.primary}` with a 2px teal bottom border when active. The sticky variant adds a subtle shadow (`0 2px 8px rgba(17,34,51,0.08)`). The `cart-icon-button` is a 40px circular transparent button; its `cart-badge` is a teal pill (20px height) with white count text, positioned at the top-right corner.

### Forms
**`text-input`** — White background, 44px height, `{rounded.sm}` (8px), 1px `{colors.hairline}` (#dedede) border. On focus, the border thickens to 2px teal. Error state swaps to `{colors.error}` (#d02e2e). Disabled inputs use `{colors.surface-soft}` (#f9fafb) background with `{colors.muted-soft}` (#9e9e9e) text. Checkboxes and radios are 20px squares/circles with 2px hairline borders, filling teal when checked.

### Search
**`search-bar-pill`** — A fully rounded (`{rounded.full}`) 44px bar on `{colors.surface-soft}` (#f9fafb) background with a 1px hairline border. On focus, the border becomes 2px teal. The pill shape mirrors the button treatment, maintaining the brand's no-hard-corners rule.

### Footer
**`footer`** — A dark section on `{colors.ink}` (#112233) with `{colors.muted-soft}` (#9e9e9e) body text and white headings. Links are 14px weight 400 in muted-soft, lightening to white on hover. Social icons are 36px circular transparent buttons that fill white on hover. The newsletter bar above the footer inverts to teal background with white text and a white input pill.

### Badges & Tags
**`product-card-badge`** — Small uppercase 11px weight 600 labels with `{rounded.sm}` (8px) and 2px/8px padding. Three variants: `badge-sale` (marigold #fed716 on ink), `badge-new` (sage #12b985 on white), `badge-low-stock` (terracotta #de3813 on white). A `badge-review` variant uses `{colors.review-highlight}` (#a89cc8) for "Top Rated" tags.

### Reviews
**`review-card`** — A `{colors.surface-soft}` (#f9fafb) card with `{rounded.md}` (12px) and `{spacing.lg}` (24px) padding. Star ratings render in `{colors.star-rating}` (#fed716) using the JudgemeStar icon font at 16px. Author name and date sit below in `{typography.caption}` (12px) and `{typography.caption-sm}` (11px) respectively.

### Quantity Selector
**`quantity-selector`** — A 40px row with a 1px hairline border and `{rounded.sm}` (8px). Minus and plus buttons are 40px squares with no rounding; the center input is 48px wide, center-aligned, with transparent background. On hover, the buttons get a `{colors.surface-soft}` background.

### Toast Notifications
**`toast-success`** — Green (#009900) background with white text, `{rounded.sm}` (8px), and `{spacing.md}`/`{spacing.lg}` padding. `toast-error` uses red (#d02e2e), `toast-warning` uses marigold (#fed716) with dark ink text. All use `{typography.body-sm}` (13px weight 400).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger, hero banner reduces to 32px padding, search bar shrinks to icon-only, footer stacks vertically, floating cart orb appears |
| Tablet | 744–1128px | Two-column product grid (2 col), nav links visible but condensed, hero banner at 48px padding, search bar full-width with icon, footer in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav with all links, hero banner at 64px padding, search bar in nav, footer in 4-column layout |
| Wide | > 1440px | Four-column product grid (4 col), max-width container at 1440px centered, hero banner full-width with 80px padding |

### Touch Targets
- All interactive elements (buttons, inputs, icons) maintain minimum 44px height for touch accessibility
- Floating cart orb at 56px for thumb reach on mobile
- Quantity selector buttons at 40px × 40px
- Nav hamburger icon at 44px × 44px
- Social icons at 36px minimum

### Collapsing Strategy
- Top nav: On mobile (< 744px), full nav links collapse into a hamburger menu; search bar collapses to a magnifying glass icon that expands on tap
- Product grid: Columns reduce from 4 → 3 → 2 → 1 as viewport narrows
- Footer: 4-column layout collapses to 2 columns on tablet, single column on mobile
- Hero banner: Padding reduces from 80px (wide) → 64px (desktop) → 48px (tablet) → 32px (mobile)
- Newsletter bar: Inline input+button row stacks vertically on mobile
- Review cards: Side-by-side layout on desktop collapses to single column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from the static HTML/CSS analysis; hover colors for secondary buttons, links, and icons are inferred from brand logic
- Error styling for forms (error messages, validation icons) was not observed on the live site
- Dark mode is not implemented on the current site; no dark-mode tokens exist
- Sub-brand or seasonal palette variations (e.g., holiday, Earth Day) were not detected
- The exact font stack for Figtree could not be confirmed — the site declares "Figtree" but may also load "Nunito Sans" as a secondary; weights beyond 400/500/600 are assumed
- Shopify checkout widget colors (Shopify Pay, Klarna, Afterpay buttons) appear in the extracted hex list but are not part of Terra's brand system
- Social icon colors (e.g., Facebook blue, Instagram gradient) appear in extracted colors but are platform defaults, not brand tokens
- The `{typography.review-stars}` token uses the JudgemeStar icon font, which may not be available outside the Shopify/Judgeme ecosystem
- Animation durations, easing curves, and transition properties were not extracted
- Focus-visible styles (keyboard navigation outlines) were not observed
- The `{colors.scrim}` (#151515) is assumed for modals/overlays but was not directly observed in use
- Print stylesheet behavior is unknown
