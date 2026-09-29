---
version: alpha
name: "Beardbrand"
source_url: "https://www.beardbrand.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A rugged yet refined men's grooming destination that balances dark, grounded utility with flashes of unexpected brightness. The brand lives on a warm off-white canvas of `#f9f8f6` and `#f9fafb`, where nearly every surface — from product cards to navigation bars — carries a soft, tactile warmth that contrasts with the deep ink of `#101010` and `#111111` used for primary text and bold headlines. The signature voltage comes from a rich teal `#108474` that appears on primary buttons, badges, and accent elements, often paired with a surprising neon yellow `#e5ff52` and a more muted `#fbcd0a` gold that suggest premium, adventurous energy. Typography leans on a mix of Space Grotesk for display and Nunito Sans for body, with occasional use of a proprietary HW_Pano_Bold for hero moments. Corners are generally soft but not pill-like — `{rounded.sm}` (8px) for buttons, `{rounded.md}` (12px) for cards — while the search bar and certain badges go full pill at `{rounded.full}`. The overall mood is workshop-meets-barbershop: utilitarian, masculine, with deliberate moments of polish (the teal CTAs, the yellow accents) that keep the experience from feeling austere. The brand trusts product photography and generous whitespace over decorative flourishes, and its muted palette of `#555555`, `#666666`, `#7b7b7b`, and `#888888` for secondary text and hairlines ensures the grooming products remain the hero.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5cc"
  ink: "#101010"
  body: "#333333"
  muted: "#555555"
  muted-soft: "#7b7b7b"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#f9f8f6"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#e5ff52"
  accent-gold: "#fbcd0a"
  accent-teal-light: "#c1e6e6"
  accent-purple: "#a89cc8"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  star-rating: "#ffff00"
  badge-new: "#e5ff52"
  badge-sale: "#108474"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Space Grotesk', 'HW_Pano_Bold', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Space Grotesk', 'HW_Pano_Bold', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Space Grotesk', 'HW_Pano_Bold', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Space Grotesk', 'HW_Pano_Bold', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Space Grotesk', 'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Space Grotesk', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Space Grotesk', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Space Grotesk', 'Nunito Sans', Arial, sans-serif"
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
    padding: 12px 24px
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
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-yellow-active:
    backgroundColor: "#d4e648"
    textColor: "{colors.ink}"
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
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  badge-category-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.base}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature teal `#108474` with white text. Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, shifts to a deeper `#0d6b5d`; disabled state uses a muted teal `#a3d5cc`. The 8px corner radius (`{rounded.sm}`) keeps the button feeling modern but not overly playful.

**`button-secondary`** — An outlined variant with a transparent background, dark ink text, and a 2px solid hairline border. Used for "Learn More" and secondary actions alongside primary buttons. Active state fills with `#eeeeee` surface-soft background.

**`button-tertiary-text`** — A text-only button styled in the primary teal with no background or border. Used for inline actions like "View Details" or "Cancel" within forms and modals.

**`button-accent-yellow`** — A high-energy variant using the brand's neon yellow `#e5ff52` with dark ink text. Deployed sparingly for limited-time offers, flash sales, or promotional banners where urgency is needed. Active state darkens to `#d4e648`.

### Cards
**`product-card`** — The core product display unit, a white card with 12px rounded corners (`{rounded.md}`) and no padding at the card level — spacing is handled by internal sub-components. The image area uses top-only rounding (`{rounded.md} {rounded.md} 0 0`) to create a natural photo-to-content transition. Title uses `{typography.title-sm}` (16px, 600 weight) and price uses `{typography.body-md}` (16px, 400 weight), both with 16px horizontal padding.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on the warm canvas background, with a subtle bottom border in `#eeeeee`. Navigation links use `{typography.nav-link}` — 14px Space Grotesk at 600 weight with 0.5px letter-spacing. Active link state underlines with a 2px teal border. The bar collapses to a hamburger menu on mobile.

### Badges
**`badge-new`** — A full-pill badge in the brand's signature neon yellow `#e5ff52` with dark ink text, used to flag new arrivals. Compact at 4px/10px padding with 11px uppercase bold type.

**`badge-sale`** — A teal `#108474` pill badge with white text for sale or promotional items. Same sizing and typography as the new badge, but the teal background signals value rather than novelty.

**`badge-category`** — Filter/tag badges used in category navigation strips. Rendered as pills on a `#f9fafb` surface with muted `#555555` text. Active state inverts to dark ink background with light canvas text.

### Forms
**`text-input`** — Standard text input with 48px height, 8px rounding, and a 1px `#dddddd` hairline border on the warm canvas background. On focus, the border thickens to 2px and shifts to the primary teal `#108474`. Padding is 12px vertical, 16px horizontal.

**`quantity-selector`** — A compact control for adjusting product quantities, built as a 40px tall container with a 1px hairline border. The increment/decrement buttons are 40px squares with a `#f9fafb` background, flanking the numeric value in the center.

### Search
**`search-bar-pill`** — The site's search entry point, rendered as a full-pill input on a white card background with a 1px hairline border. At 56px tall with generous 24px horizontal padding, it's designed to be immediately tappable. Focus state switches to a 2px teal border.

### Footer
**`footer`** — A dark inversion of the main canvas, using `#101010` as background and white text. Links are rendered in `#7b7b7b` and lighten to full white on hover. The section uses 48px vertical padding with 24px horizontal gutters.

### Accordion
**`accordion`** — Collapsible content panels with a white background, 8px rounding, and a 1px `#eeeeee` border. Headers use `{typography.title-sm}` with 16px/24px padding; content areas use 0/24px/16px padding to maintain visual rhythm.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero layout, reduced heading sizes (display-xl drops to 32px), full-width cards, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid, expanded nav links (no hamburger), hero text remains centered, search bar visible but shorter (48px height), category badges wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid, full nav bar visible, hero uses 48px display-xl, search bar at full 56px height, product cards show hover zoom effects |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) with centered content, hero can accommodate larger imagery, additional whitespace around card grids |

### Touch Targets
- All interactive elements (buttons, inputs, badges) maintain minimum 44px height for touch accessibility
- Product card tap targets are the full card surface, not just text links
- Quantity selector buttons are 40px squares — meets minimum touch target recommendations
- Search bar pill at 56px height provides generous tap area
- Nav links have minimum 44px tap area through padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column as viewport narrows
- Hero section stacks vertically on mobile (heading above subheading above CTA)
- Category filter badges collapse into a horizontal scrollable strip on mobile
- Footer link columns stack to single column below 744px
- Search bar reduces to icon-only trigger on mobile, expanding to full input on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns — exact color transitions and timing are not extracted
- Error styling for form inputs (border colors, error message typography) not observed on live site
- Dark mode palette not present — all observed pages use light canvas
- Sub-brand or collection-specific color variations not captured (e.g., limited edition packaging colors)
- Loading states and skeleton screen patterns not observed
- Modal/dialog overlay styling (backdrop opacity, close button placement) not extracted
- Tooltip and popover styling not present in extracted data
- Animation timing curves and transition durations not available
- Focus ring styles (outline color, offset) not reliably extracted from the DOM
- Mobile-specific navigation drawer (hamburger menu) styling not observed in detail
- Checkbox and radio button custom styling not present in extracted data
- Dropdown/select menu styling not observed
- Pagination component styling not extracted
- Breadcrumb component not present on observed pages
