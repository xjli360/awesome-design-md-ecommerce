---
version: alpha
name: "Burga"
source_url: "https://www.burga.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A confident accessories brand that wraps everyday tech in saturated color blocks and a glossy, almost lacquered finish — #f8494a (a high-voltage coral-red) is the primary voltage that punches through a system built on #f5f5f5 canvases and #111111 ink. The brand’s visual signature is the contrast between hard, protective cases and soft, almost playful color stories: #ffcf2a marigold accents, #009758 emerald badges, and #be4dc4 orchid highlights appear as surprise hits against a predominantly neutral base of #888888 muted text and #e5e5e5 hairlines. Typography runs Diatype, a geometric sans with a slight humanist warmth, set at moderate weights — display headlines sit at 24–32px in weight 500, trusting the color blocks and product photography to carry energy rather than heavy type. Product cards use {rounded.md} corners that feel protective without being bulky, while CTAs use {rounded.sm} with a full-height fill that reads as decisive. The nav bar anchors at 64px with a translucent scrim effect (#111111 at 90% opacity on scroll), and the cart icon badge uses {rounded.full} in #f8494a to signal count. The overall mood is urban, glossy, and slightly rebellious — a phone case as a fashion accessory, not a utility item.

colors:
  primary: "#f8494a"
  primary-active: "#d63a3b"
  primary-disabled: "#fccccc"
  ink: "#111111"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#a89b79"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-strong: "#f4f4f6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-marigold: "#ffcf2a"
  accent-emerald: "#009758"
  accent-orchid: "#be4dc4"
  accent-orange: "#fe7b19"
  accent-blue: "#2332e6"
  accent-sky: "#83ceec"
  accent-sage: "#b2f9e9"
  accent-sand: "#e6ded5"
  accent-cream: "#e8dfd3"
  accent-ivory: "#f7f6f2"
  accent-navy: "#20427a"
  star-rating: "#ffcf2a"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Diatype', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-scrolled:
    backgroundColor: "rgba(17, 17, 17, 0.9)"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.accent-emerald}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-original-price:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  product-card-rating:
    color: "{colors.accent-marigold}"
    size: 14px
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  newsletter-input:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid rgba(255, 255, 255, 0.2)"
  newsletter-input-focus:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    border: "1px solid {colors.on-dark}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 48px
    padding: "12px 24px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  hero-secondary-cta:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 31px"
    border: "1px solid {colors.on-dark}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-tile-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  color-swatch-out-of-stock:
    opacity: 0.3
    border: "2px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: "0 {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, filled with #f8494a and white text. Uses {rounded.sm} and 14px vertical padding for a compact, decisive feel. On hover, shifts to `primary-active` (#d63a3b). Disabled state uses `primary-disabled` (#fccccc) with no border, maintaining the filled silhouette. Used for "Add to Cart", "Checkout", and primary hero CTAs.

**`button-secondary`** — Outlined variant on a white background with {colors.hairline} border. Active state darkens the border to {colors.ink} and adds a light fill. Used for "View Details", "Compare", and secondary actions in cart and product pages.

**`button-tertiary-text`** — Text-only button with no background or border. Used for "Cancel", "Clear", and inline navigation links where a full button would be too heavy.

**`button-pill-primary`** — Fully rounded pill variant of the primary button, used for filter tags, collection navigation, and promotional badges. Smaller typography ({typography.button-sm}) and tighter padding for inline use.

**`button-pill-outline`** — Outlined pill variant for secondary filter tags and "Shop All" links. Transparent background with {colors.hairline} border.

### Cards
**`product-card`** — The core product display unit. White background with {rounded.md} corners. The image area maintains a 1:1 aspect ratio with {rounded.md} corners. Below the image: product title in {typography.body-sm}, price in {typography.title-sm}, and optional sale price in {colors.primary} with original price struck through. A {colors.accent-emerald} badge overlays the top-left of the image for "New" or "Sale" labels. Star ratings render in {colors.accent-marigold} at 14px.

**`category-tile`** — Used for collection navigation (e.g., "Phone Cases", "AirPods Cases", "Laptop Sleeves"). Light gray background ({colors.surface-soft}) with {rounded.md} and {spacing.lg} padding. Active state fills with {colors.primary} and white text. Typically displayed in a horizontal scroll strip on mobile, grid on desktop.

### Navigation
**`top-nav`** — Fixed header at 64px height on desktop, 56px on mobile. White background at rest, transitions to a semi-transparent dark scrim (rgba(17, 17, 17, 0.9)) on scroll for product pages. Contains the Burga logo (left), navigation links (center), and icon buttons for search, account, and cart (right). Active nav links use {colors.primary}, inactive use {colors.muted}.

**`search-bar`** — Light gray input field with {rounded.sm} and 44px height. On focus, the border switches to {colors.primary} and the background becomes white. Placeholder text in {colors.muted}. Used in the nav bar and on the search results page.

### Forms
**`text-input`** — Standard form input for checkout, account, and newsletter. Uses {colors.surface-soft} background, {rounded.sm}, and 44px height. Focus state mirrors the search bar with {colors.primary} border. Error state uses {colors.primary} border with red helper text.

**`newsletter-input`** — Footer-specific input on dark background. Semi-transparent white background (rgba(255, 255, 255, 0.1)) with a subtle white border. On focus, background lightens and border becomes solid white. Paired with `newsletter-submit` button in {colors.primary}.

### Badges & Indicators
**`product-card-badge`** — Small uppercase label in {colors.accent-emerald} with white text. {rounded.xs} with 2px vertical padding. Used for "NEW", "SALE", "BESTSELLER" tags. Positioned absolutely at the top-left of product images.

**`cart-icon-badge`** — Circular badge on the cart icon showing item count. {rounded.full} in {colors.primary} with micro-label typography. 18px height, min-width 18px. Positioned at the top-right of the cart icon.

**`color-swatch`** — Circular swatch for product variant selection. 32px diameter with {rounded.full}. Selected state shows a 2px {colors.ink} border. Out-of-stock swatches render at 30% opacity with a {colors.hairline} border.

### Footer
**`footer-section`** — Full-width dark section (#111111 background) with white text. Contains link columns, social icons, newsletter signup, and legal text. Links use {colors.muted-soft} (#a89b79) and lighten to white on hover. Padding uses {spacing.section} for top/bottom and {spacing.xl} for sides.

### Hero
**`hero-section`** — Full-bleed section on dark background (#111111) with large display typography ({typography.display-xl}). Contains a primary CTA (`hero-cta`) in {colors.primary} and an optional secondary outline CTA (`hero-secondary-cta`) with white border. Background may feature product imagery or lifestyle photography with a dark overlay.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text scales to {typography.display-lg}; category tiles stack vertically; footer columns stack; search bar expands full-width on focus |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses {typography.display-xl}; category tiles in 2-3 column grid; footer in 2 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full width with left-aligned text; category tiles in 4-column grid; footer in 4 columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px; category tiles in 5-column grid |

### Touch Targets
- All buttons and interactive elements: minimum 44px height (48px preferred for primary actions)
- Icon buttons: 40px × 40px minimum
- Color swatches: 32px × 32px (44px tap area via padding)
- Nav links: 44px tap height
- Quantity selector: 44px height
- Search bar: 44px height

### Collapsing Strategy
- **Mobile (< 744px)**: Full nav collapses to hamburger menu; search bar collapses to icon that expands on tap; product filters collapse to a "Filter" button that opens a bottom sheet; footer columns collapse to accordion sections
- **Tablet (744–1128px)**: Secondary nav links collapse to a "More" dropdown; search bar remains visible but shrinks to icon on scroll
- **Desktop (1128–1440px)**: No collapsing; all elements visible
- **Wide (> 1440px)**: Content max-width at 1440px; margins increase proportionally

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only active/resting colors for buttons and links. Hover transitions (ease, duration) were not reliably captured from the live site. Assumed 200ms ease-in-out for all interactive elements.
- **Error styling**: Form error states (border color, helper text color, icon) were not extracted. Assumed {colors.primary} for error borders and {colors.primary} for error text, consistent with the brand's accent-driven approach.
- **Dark mode**: No dark mode variant was detected on the live site. The brand uses a dark footer and dark hero sections, but there is no system-preference-driven dark mode. If implemented, would need a separate palette.
- **Sub-brand palettes**: Burga may have collection-specific color stories (e.g., "Crystal Clear", "Marble", "Floral") that were not captured. These would use the accent colors listed but may have additional custom hexes per collection.
- **Typography scale**: Only Diatype was found in font-family declarations. Weight and size values were inferred from common usage patterns on the site. Actual line-height and letter-spacing values may vary slightly across components.
- **Animation & motion**: No animation tokens (duration, easing, keyframes) were extracted. The brand likely uses subtle micro-interactions on hover and scroll that are not documented here.
- **Checkout flow**: Shopify checkout uses its own design system (Shopify Checkout UI) which overrides brand styles. The extracted colors include some Shopify Pay and payment-widget colors that were filtered out. The checkout experience will not match the brand's design system.
- **Accessibility**: Contrast ratios were not verified. The {colors.muted-soft} (#a89b79) on {colors.ink} (#111111) footer background may have insufficient contrast for WCAG AA compliance. The {colors.primary} (#f8494a) on white passes AA for large text but should be verified for body text usage.
