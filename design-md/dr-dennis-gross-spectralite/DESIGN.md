---
version: alpha
name: "Dr. Dennis Gross (Spectralite)"
source_url: "https://drdennisgross.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical-grade skincare brand that communicates efficacy through a stark black-and-white canvas punctuated by a single electric orange accent — #fe6728, the brand's primary voltage that fires across every CTA, badge, and product-highlight dot. The palette is deliberately restrained: near-black backgrounds (#050505, #1b1b1b) against warm off-white surfaces (#fafafa, #f5f5f5) create a dermatologist's-office precision, while a secondary orange (#ff651b) and a cautionary red (#cc0000) handle urgency signals. Typography runs a dual system — the serifed JHATimesNow-Light for aspirational display headlines (the "Spectralite" product name, ingredient stories) and AvenirNextLTPro-Regular for body copy, creating a tension between luxury editorial and clinical clarity. Buttons are sharp-cornered rectangles ({rounded.sm} at 8px) rather than pills, reinforcing the brand's no-nonsense medical credibility. Product cards use generous {spacing.lg} padding and {rounded.md} corners, with the Spectralite device rendered heroically against pure black — the only color allowed to compete with the orange is the device's own LED glow. The brand trusts negative space over decorative elements: there are no illustrations, no gradients, no decorative borders. Every design decision reads as "this product has been tested, this claim is proven."

colors:
  primary: "#fe6728"
  primary-active: "#e0551a"
  primary-disabled: "#ffc9a8"
  ink: "#050505"
  body: "#1b1b1b"
  muted: "#53585b"
  muted-soft: "#868a89"
  hairline: "#c4c4c4"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#ff651b"
  caution-red: "#cc0000"
  caution-red-light: "#ff5742"
  success-green: "#00b84a"
  link-blue: "#0018ff"
  link-blue-soft: "#b4d5fe"
  teal-accent: "#4efac0"
  teal-accent-dark: "#3cfecf"
  device-black: "#050505"
  device-gray: "#3b3d3f"

typography:
  display-xl:
    fontFamily: "'JHATimesNow-Light', 'JHATimesNow-SemiLightIT', Georgia, serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'JHATimesNow-Light', 'JHATimesNow-SemiLightIT', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'JHATimesNow-Light', 'JHATimesNow-SemiLightIT', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'AvenirNextLTPro-Regular', 'AvenirNextProRegular', 'Inter', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
  section: 80px

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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-dark-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.caution-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.success-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-limited:
    backgroundColor: "{colors.caution-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.ink}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  device-hero:
    backgroundColor: "{colors.device-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
  price-display:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
  price-display-sale:
    backgroundColor: transparent
    textColor: "{colors.caution-red}"
    typography: "{typography.title-md}"
  price-display-original:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    textDecoration: "line-through"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in electric orange (#fe6728) with white text. Uses AvenirNext at 14px/600 weight with 0.3px letter spacing for a precise, clinical feel. Corners are softly squared at {rounded.sm} (8px) — never pill-shaped — reinforcing the medical-grade positioning. On hover, the background shifts to `primary-active` (#e0551a). Disabled state uses `primary-disabled` (#ffc9a8). Height is 48px with 14px/28px padding.

**`button-secondary`** — An outlined variant with a 2px solid black border on a transparent background. Text matches the `ink` (#050505). Active state fills the button with black and inverts text to white. Used for "Learn More" and secondary product actions where the orange primary would compete.

**`button-dark`** — A solid black button (#050505) with white text, used exclusively on light backgrounds for "Add to Cart" in product cards and checkout flows. Active state shifts to `body` (#1b1b1b). This button carries the same typography and corner radius as `button-primary` to maintain system consistency.

**`button-ghost`** — A text-only button with no background or border. Text is `ink` (#050505). On hover, a `surface-soft` (#f3f3f3) background appears. Used for tertiary actions like "Cancel," "Clear Filters," and "View Details" links within cards.

### Text Inputs & Forms
**`text-input`** — A clean, bordered input field with a white background (`canvas`), `ink` text, and a `hairline` (#c4c4c4) border. Height is 48px with 12px/16px padding. On focus, the border switches to `ink` (#050505) for a high-contrast state. Error state uses `caution-red` (#cc0000) border. Typography is `body-md` (16px/400) for readability.

**`select-dropdown`** — Matches the `text-input` structure visually — same height, padding, border, and typography. The dropdown arrow is rendered in `ink` (#050505). Used for product variant selection (size, formula) and shipping country picker.

### Navigation
**`top-nav`** — A fixed-position navigation bar at 72px height on a white (`canvas`) background. Links use `nav-link` typography: 13px/600 weight with 0.5px letter spacing in uppercase — a deliberate choice that reads as clinical and authoritative rather than friendly. Active and hover states shift the link color to `primary` (#fe6728). On scroll, the nav shrinks to 64px and gains a subtle 1px shadow.

**`nav-link-active`** — The active navigation link inherits the same uppercase 13px/600 typography but switches to `primary` orange. No underline or background indicator — the brand trusts color alone to signal the current section.

### Product Cards
**`product-card`** — A white card with `rounded.md` (12px) corners and 16px padding. The product image occupies a 1:1 aspect ratio with matching corner radius. On hover, a soft shadow (0 4px 12px rgba(0,0,0,0.1)) lifts the card. Typography is `body-sm` (14px) for product names and `title-sm` (16px/600) for pricing.

**`product-badge`** — Small rectangular badges (4px/8px padding, `rounded.xs` at 2px) using `badge` typography: 11px/700 weight, uppercase with 0.5px letter spacing. Four variants exist: `product-badge` (orange primary for "Best Seller"), `product-badge-sold-out` (muted gray), `product-badge-new` (green #00b84a), and `product-badge-limited` (red #cc0000). These badges sit in the top-left corner of product images.

### Hero & Device Sections
**`hero-section`** — A full-width black background (#050505) section with white text using `display-xl` (48px/300 weight serif). Padding is 80px top/bottom with 24px sides. Used for the Spectralite device hero, clinical study results, and brand storytelling. A light variant (`hero-section-light`) inverts to white background with black text for ingredient education panels.

**`device-hero`** — A specialized hero for the Spectralite device, using pure black (`device-black` #050505) as the background. The device is rendered as a high-contrast product shot against this void, with only the orange accent (#fe6728) and the device's own LED glow providing color. Typography uses `display-lg` (36px/300 weight serif) for the product name.

### Footer
**`footer-section`** — A full-width black footer (80px padding) with white text. Links use `muted-soft` (#868a89) at 14px/500 weight, shifting to white on hover. The footer contains three columns: product categories, customer service links, and social/legal links. No background color change on hover — only text color shifts.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details. The header is a transparent button with `title-sm` typography (16px/600) and 16px vertical padding. No background or border — the brand relies on the content's weight and spacing to create hierarchy. The accordion content uses `body-md` (16px/400) with 16px bottom padding.

### Quantity Selector
**`quantity-selector`** — A compact 40px-tall input with `rounded.sm` (8px) corners, a white background, and a `hairline` border. Used in cart and product detail pages for adjusting purchase quantity. The plus/minus buttons are rendered as text symbols in `ink` (#050505).

### Price Display
**`price-display`** — The standard product price uses `title-md` (18px/600) in `ink` (#050505). Sale pricing uses `caution-red` (#cc0000) with the same typography, while the original (strikethrough) price uses `muted-soft` (#868a89) at 14px/400 with `textDecoration: line-through`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; hero type drops to 28px; product cards stack full-width; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4-5 links; hero type at 36px; product cards at 50% width; footer in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero type at 48px; product cards at 33% width; footer in 3-column layout |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero type at 48px with larger margins; footer in 4-column layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets are the entire card surface, not just text links
- Quantity selector plus/minus buttons are 40px × 40px minimum
- Accordion headers are 44px minimum tap height
- Mobile hamburger menu icon is 44px × 44px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer for full navigation
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Product description accordions are collapsed by default on all breakpoints
- Footer columns stack vertically below 744px
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Multi-step checkout collapses to a single-page scroll on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and ghost buttons could not be reliably extracted from the live site — the `button-secondary-active` and `button-ghost-active` tokens are inferred from common DTC patterns rather than observed behavior
- Error styling for form validation (error messages, iconography, animation) was not observed — only the border color change was extracted
- The exact font weights for AvenirNextLTPro-Regular and JHATimesNow-Light are inferred from the font names (Light = 300, Regular = 400) but the actual CSS `font-weight` declarations were not always present
- Dark mode styling is not present on the live site — all pages use the light/white canvas with black ink
- Sub-brand palettes (for product lines like Alpha Beta, Spectralite, C+Collagen) were not extracted — the orange primary may shift per product line
- Animation and transition durations (button hover, card lift, nav scroll) were not extracted — the shadow values are estimated from common 0.2-0.3s ease transitions
- The `SpeziaMonoTrial-Medium` font was found in the extracted declarations but its usage context (code snippets, footnotes, ingredient labels) could not be determined
- The `Brown` font family was found but appears to be a legacy or fallback — it is not included in the typography system as its usage was not observed on primary pages
- Checkout flow components (payment forms, shipping selectors, order summary) were not extracted as they exist behind authentication
- The exact `boxShadow` values for product card hover and nav scroll are estimated — the live site may use different spread/blur values
