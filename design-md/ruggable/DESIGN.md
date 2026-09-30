---
version: alpha
name: "Ruggable"
source_url: "https://ruggable.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the premise that rugs should be washable, Ruggable's design system is a study in earthy warmth and pragmatic clarity. The palette is anchored by deep, grounded tones like #282521 (a near-black brown that reads as ink) and #1a1817 (a softer, warmer charcoal), set against a canvas of #f6f4ef and #f7f7f7 that feels like natural linen. The brand's signature voltage comes from a single accent — #f5ce4e, a warm golden yellow that appears on badges, sale tags, and select CTAs, injecting a note of optimism into the otherwise neutral landscape. A secondary accent of #9fe3ba (a soft mint) and #ff816f (a coral) appear sparingly, often on product badges or promotional elements. Typography is a two-family system: the primary display face is `aprisRuggable`, a custom sans-serif with a slightly condensed, elegant character, while body copy relies on `Manrope`, a geometric sans-serif that provides clean readability. The system avoids hard corners — cards and buttons use `{rounded.sm}` (8px) and `{rounded.md}` (12px), while the primary search bar and hero CTAs lean into `{rounded.full}` pill shapes, creating a friendly, approachable interface. The overall mood is one of reliable comfort — the brand trusts its product photography and generous whitespace to convey quality, while the design system provides a quiet, consistent framework that never competes with the rugs themselves.

colors:
  primary: "#f5ce4e"
  primary-active: "#e0b93a"
  primary-disabled: "#f5e8b0"
  ink: "#282521"
  body: "#4d4d4d"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#f6f4ef"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#1a1817"
  accent-gold: "#f5ce4e"
  accent-mint: "#9fe3ba"
  accent-coral: "#ff816f"
  badge-red: "#b30000"
  badge-brown: "#934b32"
  link-blue: "#2563eb"
  star-rating: "#f5ce4e"

typography:
  display-xl:
    fontFamily: "'aprisRuggable', 'Manrope', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'aprisRuggable', 'Manrope', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'aprisRuggable', 'Manrope', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'aprisRuggable', 'Manrope', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    padding: 14px 24px
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
    padding: 13px 23px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 22px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    color: "{colors.surface-soft}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.surface-card}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  swatch-selector:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  swatch-selector-selected:
    border: "2px solid {colors.ink}"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  size-selector-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    border: "1px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for add-to-cart, checkout, and key conversion points. Filled with `{colors.primary}` gold against `{colors.on-primary}` dark text. On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text. **`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Learn More." Uses `{colors.canvas}` background with `{colors.ink}` text. **`button-secondary-outline`** — A bordered variant with a 2px `{colors.ink}` stroke, used when a clear visual boundary is needed against light backgrounds. **`button-pill-primary`** — The hero CTA shape, using `{rounded.full}` for a friendly, approachable feel. Used in the main hero banner and promotional sections. **`button-pill-secondary`** — Pill-shaped secondary button, often paired with the primary pill for dual-CTAs.

### Cards
**`product-card`** — The primary product display unit, a white card with `{rounded.md}` corners. Contains a product image with `{rounded.md}` top corners, product title, price, rating stars, and swatch/size selectors. The card has no border, relying on the white surface against `{colors.canvas}` for separation. **`product-card-badge`** — Small gold badge anchored to the top-left of product images, using `{colors.primary}` background. Variants include `product-card-badge-sale` (red, `{colors.badge-red}`) and `product-card-badge-new` (mint, `{colors.accent-mint}`). All badges use `{typography.badge}` with uppercase tracking.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 64px height, using `{colors.canvas}` background. Contains the Ruggable logo, category links in uppercase `{typography.nav-link}`, and utility icons (search, account, cart). On scroll, transitions to `{colors.surface-card}` with a subtle box-shadow. **`category-pill`** — Pill-shaped category filters used in the product grid header. Active state inverts to `{colors.ink}` background with white text.

### Forms & Inputs
**`text-input`** — Standard text input with `{rounded.sm}`, 48px height, and a 1px `{colors.hairline}` border. Focus state gains a 2px `{colors.primary}` border. Error state uses `{colors.badge-red}`. **`search-bar`** — Full-width pill-shaped search bar at 56px height, used in the hero and sticky header. White background with `{rounded.full}` and a subtle border. Focus state mirrors the text-input pattern.

### Footer
**`footer`** — Full-width dark footer using `{colors.ink}` background with `{colors.surface-soft}` text. Contains link columns, newsletter signup, and social icons. Links use `{typography.link}` with hover underlines. Section headings use `{typography.title-sm}` with uppercase transformation.

### Product Selection
**`swatch-selector`** — Circular color swatches at 32px, used for rug color/pattern selection. Selected state shows a 2px `{colors.ink}` border. **`size-selector`** — Rectangular size chips with `{rounded.sm}`, used for rug dimensions. Selected state inverts to `{colors.ink}` background.

### Accordion
**`accordion`** — Collapsible sections used for product details, shipping info, and FAQs. Uses `{colors.canvas}` background with `{rounded.sm}`. Headers use `{typography.title-sm}`, content uses `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero layout, full-width cards, reduced heading sizes |
| Tablet | 744–1128px | Two-column product grid, persistent top nav with condensed links, side-by-side hero content |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, multi-column footer, max-width container |
| Wide | > 1440px | Four-column product grid, expanded whitespace, larger hero imagery, max-width 1440px container centered |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height
- Swatch selectors at 32px are paired with larger tap areas via padding
- Mobile nav hamburger icon has 48px tap target
- Category pills have 40px minimum height on touch devices

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-out drawer overlay
- Product grid reduces columns from 4 to 1 on mobile
- Multi-column footer collapses to single-column accordion on mobile
- Hero section stacks vertically on mobile, with CTA buttons full-width
- Category filter strip collapses to horizontal scroll on mobile
- Product image gallery collapses to single-image carousel with dots

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary buttons and text inputs were not fully extracted — assumed patterns based on primary button behavior
- Error and success states for form validation (colors, icons, messaging) were not observed on the live site
- Dark mode palette is not defined — the brand appears to use only light mode
- Sub-brand or collection-specific color palettes (e.g., "Outdoor," "Kids") were not extracted
- Animation and transition timing values (durations, easing curves) were not reliably extracted
- Icon set and iconography guidelines are not documented — SVG icons observed but no sizing or color tokens extracted
- Dropdown and select menu styling was not observed on the live site
- Modal and overlay component styling (backdrop, close button, padding) was not extracted
- The `aprisRuggable` font family appears to be a custom brand font — no weight or style variants were extracted beyond the family name
- Shopify platform integration patterns (cart drawer, checkout buttons) were not fully analyzed
