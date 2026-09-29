---
version: alpha
name: "Grab Green"
source_url: "https://grabgreenhome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A laundry and home-cleaning brand that uses a deep forest green (#1f3521) as its environmental anchor — not as a primary CTA color but as a persistent brand signature on packaging, badges, and accent elements, while the actual interactive system runs on a warm charcoal (#303030) and a sandy beige (#dfd5c4) that reads more like a natural-fiber textile than a typical cleaning aisle. The palette is deliberately low-contrast: body text sits at #707070 on a #f7f7f7 canvas, avoiding the harsh black-on-white of most CPG sites, and the hairline (#e0e0e0) is soft enough to feel like a pencil sketch. A single red alert (#d12121) and a muted coral (#cc6328) provide the only heat in the system, used sparingly for sale badges and error states. Typography runs ValueSans across all weights — a clean, slightly condensed geometric that avoids the friendly roundness of a brand like Method or the clinical sans of Seventh Generation. The site reads as a Grove Collaborative sub-brand (the page title confirms it), which means the navigation and checkout are inherited from Grove's ecosystem, but Grab Green's own product cards use a distinctive {rounded.sm} corner on a white (#ffffff) surface with the forest-green badge pinned to the top-left. The overall feeling is of a brand that trusts its ingredients list more than its marketing — the design steps back and lets the "plant-powered" messaging breathe on a quiet, beige-tinted stage.

colors:
  primary: "#303030"
  primary-active: "#1a1a1a"
  primary-disabled: "#aaaaaa"
  ink: "#2b2b2b"
  body: "#707070"
  muted: "#777777"
  muted-soft: "#bbbbbb"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#f7f7f7"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  brand-green: "#1f3521"
  brand-sand: "#dfd5c4"
  accent-coral: "#cc6328"
  alert-red: "#d12121"
  alert-red-hover: "#c70000"
  badge-pink: "#bf339d"
  badge-gold: "#dbb27d"
  star-rating: "#dbb27d"

typography:
  display-xl:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'ValueSans', 'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'ValueSans', 'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'ValueSans', 'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.2px
  badge:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'ValueSans', 'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.3px
  price-md:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  price-sm:
    fontFamily: "'ValueSans', 'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0

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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.muted-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-green:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.alert-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-content:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-badge:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-best:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-md}"
    textColor: "{colors.alert-red}"
  product-card-price-original:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-star:
    color: "{colors.star-rating}"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
  product-card-add-to-cart-hover:
    backgroundColor: "{colors.primary-active}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-green:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-sand:
    backgroundColor: "{colors.brand-sand}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 24px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  filter-chip-hover:
    border: "1px solid {colors.muted-soft}"
  badge-count:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "2px 6px"
    minWidth: 20px
    height: 20px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a dark charcoal (#303030) rectangle with {rounded.sm} corners and white uppercase ValueSans Medium at 14px. On hover, it deepens to near-black (#1a1a1a). The disabled state drops to a mid-gray (#aaaaaa) that sits quietly on the canvas. Used for "Add to Cart", "Subscribe & Save", and primary checkout actions.

**`button-secondary`** — An outlined variant with a white fill and a single-pixel hairline border (#e0e0e0). The text remains charcoal. On hover, the background shifts to the soft surface tone (#f3f3f3) and the border thickens visually to muted-soft (#bbbbbb). Used for "Learn More" and secondary product actions.

**`button-green`** — A brand-specific variant using the forest green (#1f3521) as background. Identical shape and typography to `button-primary` but carrying the environmental brand signal. Used on hero banners and eco-badge CTAs.

**`button-coral`** — A warm accent variant using #cc6328. Used sparingly for limited-time offers or seasonal promotions where the brand wants heat without the alarm of red.

**`button-ghost`** — A text-only button with no background or border. Uses body-gray (#707070) text and 12px horizontal padding. Used for "Cancel", "Clear filters", and inline utility actions.

### Cards
**`product-card`** — The core product display unit. A white surface card with {rounded.sm} corners, no shadow (the brand relies on the hairline grid for separation). The image area occupies the top with its own {rounded.sm} top corners. Content padding follows the base spacing token (16px) on sides and bottom, with 24px at the bottom to give the price and add-to-cart room to breathe. Badges are pinned to the top-left of the image area.

**`product-card-badge-*`** — Four badge variants: green (#1f3521) for "Plant Powered" or standard product flags, red (#d12121) for sale, pink (#bf339d) for new arrivals, and gold (#dbb27d) for bestseller. All use 11px uppercase ValueSans Medium with 0.5px letter-spacing, {rounded.xs} corners, and 4px/8px padding.

### Navigation
**`nav-bar`** — A 64px white bar with the brand logo left-aligned and nav links in 14px ValueSans Medium. On scroll, a subtle 1px/3px shadow appears. The nav is inherited from Grove Collaborative's ecosystem, so the Grab Green-specific elements are limited to the logo and product category links.

### Forms
**`text-input`** — A 44px-tall white input with {rounded.sm} corners and a single hairline border. Focus state swaps the border to charcoal (#303030). Error state uses alert-red (#d12121). The typography is 16px ValueSans Regular for readability.

**`search-bar`** — A pill-shaped ({rounded.full}) input at 48px height with a hairline border. The full roundness is the only place the brand uses maximum radius — it signals the search function as a friendly entry point. Focus state matches the text-input pattern.

**`quantity-selector`** — A compact 40px-high control with a hairline border and {rounded.sm} corners. The increment/decrement buttons are 24px transparent squares. Used on product detail pages for subscription quantity adjustment.

### Filters
**`filter-chip`** — Pill-shaped ({rounded.full}) chips at 32px height with hairline borders and 12px caption-bold text. Active state fills with charcoal and inverts text to white. Used on collection pages for scent, size, and product-type filtering.

### Footer
**`footer`** — A full-width charcoal (#303030) footer with white text. Links are 14px ValueSans Regular with no underline by default, gaining underline on hover. Padding is generous at 48px vertical and 32px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col). Nav collapses to hamburger. Filter chips stack vertically. Hero banner reduces to 48px vertical padding. Product card badges shrink to 10px font. |
| Tablet | 744–1128px | Two-column product grid. Nav links visible but condensed. Filter chips wrap in a horizontal row. Hero banner uses 56px vertical padding. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with all links. Filter chips in a single horizontal scrollable row. Hero banner at full 64px section padding. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px centered. Hero banner may use a wider background with constrained content. |

### Touch Targets
- All interactive elements (buttons, inputs, chips) maintain minimum 44px height for touch accessibility.
- Icon-only buttons within quantity selectors are 40px × 40px to exceed the 44px tap target recommendation.
- Filter chips are 32px tall with 14px horizontal padding — the touch target is the chip itself plus the 8px gap between chips.
- Product card "Add to Cart" buttons are 36px tall — this is below the 44px recommendation and should be noted as a Known Gap.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product filter panel collapses into a bottom sheet or modal on mobile.
- The footer accordion sections (Customer Service, Learn, Connect) collapse into expandable accordions on mobile and tablet.
- Product image galleries collapse from a row of thumbnails to a single swipeable carousel on mobile.
- The hero banner collapses from a two-column layout (text + image) to a single stacked column on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary`, `button-ghost`, and `filter-chip` are inferred from common patterns — the live site may use different transitions or no hover state at all.
- Error styling for form inputs (text-input-error) is assumed from the alert-red color — no error state was visible in the extracted data.
- The `nav-bar-scrolled` shadow is a common e-commerce pattern but was not confirmed from the live site.
- Dark mode is not supported and no dark-mode tokens were extracted.
- The brand's sub-brand palette (if any exists for product lines like "Baby", "Kitchen", "Pet") was not extractable — only the main brand colors are captured.
- The `loading-spinner` and `skeleton-loader` components are standard patterns — no specific animation or color was extracted from the live site.
- The `star-rating` color (#dbb27d) is inferred from the extracted hex list — it may be a different shade or use a different color for filled vs. empty stars.
- The `badge-pink` (#bf339d) appears in the extracted colors but its specific usage (new arrival vs. limited edition vs. subscription-only) is unconfirmed.
- The `accent-coral` (#cc6328) may be a seasonal or promotional color rather than a permanent brand token.
- Touch target size for product-card-add-to-cart (36px) is below the WCAG 2.2 recommended 44px minimum — this should be validated against the live site's actual implementation.
- The font-family "ValueSerif Bold" was extracted but no usage context was found — it may be used for editorial content, blog posts, or packaging mockups that were not captured in the page scan.
