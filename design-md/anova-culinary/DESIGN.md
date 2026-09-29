---
version: alpha
name: "Anova Culinary"
source_url: "https://anovaculinary.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision-first brand that lives at the intersection of sous-vide science and home-kitchen warmth. Anova Culinary's design system is anchored on a crisp white canvas (`#ffffff`) and a bold, appetite-waking orange (`#ff8b01`) that serves as the primary voltage for every purchase CTA, navigation accent, and product-highlight badge. The palette draws from the kitchen itself — cool steel grays (`#d9d9d9`, `#dedede`, `#eceef0`) for surfaces and hairlines, deep charcoal (`#2b2b2b`) for body text, and near-black (`#121212`) for high-impact headlines. A secondary blue spectrum (`#256bc1`, `#1990c6`, `#136f99`) echoes the precision of water-temperature control, appearing in secondary buttons, informational badges, and link states. The typography runs Pluto Sans and Pluto Sans Light — a geometric humanist face that feels both technical and approachable, with display sizes at 28–32px and body text at 14–16px. Rounded corners are generous but not pillowy: cards use `{rounded.md}` (12px), buttons use `{rounded.sm}` (8px), and only search inputs and badge elements reach `{rounded.full}`. The system trusts generous whitespace (`{spacing.section}` at 64px) and high-contrast photography over decorative flourishes, letting the product — a precision cooker, a combi oven, a perfectly cooked steak — speak for itself.

colors:
  primary: "#ff8b01"
  primary-active: "#e67a00"
  primary-disabled: "#ffd9a3"
  ink: "#121212"
  body: "#2b2b2b"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#d9d9d9"
  hairline-soft: "#eceef0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#256bc1"
  accent-blue-hover: "#1a52a1"
  accent-cyan: "#1990c6"
  accent-cyan-hover: "#136f99"
  success: "#2ecc71"
  error: "#e74c3c"
  warning: "#f39c12"
  star-rating: "#ff8b01"
  scrim: "#000000"
  ios-blue: "#007aff"

typography:
  display-xl:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Pluto Sans Light', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Pluto Sans Light', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Pluto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
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
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-blue-active:
    backgroundColor: "{colors.accent-blue-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 28px
    height: 48px
  button-pill:
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
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-input-focus:
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-logo:
    height: 32px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price-display}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.star-rating}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-info:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.base} {spacing.lg} {spacing.base}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  tab-hover:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  stepper-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  stepper-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  stepper-connector:
    backgroundColor: "{colors.hairline}"
    height: 2px
  stepper-connector-active:
    backgroundColor: "{colors.primary}"
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  rating-stars-empty:
    textColor: "{colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-Order", and "Shop Now" actions. It uses the brand's signature orange (`{colors.primary}`) with white text (`{colors.on-primary}`) and a subtle 8px rounded corner (`{rounded.sm}`). On hover, it shifts to `{colors.primary-active}` (#e67a00) for a darker, more grounded state. When disabled, it fades to `{colors.primary-disabled}` (#ffd9a3) with reduced contrast.

**`button-secondary`** — An outlined alternative for less prominent actions like "Learn More" or "View Details". It maintains a white background with a 2px hairline border (`{colors.hairline}`) and dark text (`{colors.ink}`). On active/hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`.

**`button-accent-blue`** — Used for secondary brand actions, particularly those related to the Anova app or precision cooking technology. It uses `{colors.accent-blue}` (#256bc1) and transitions to `{colors.accent-blue-hover}` (#1a52a1) on hover.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip". It inherits `{colors.ink}` and maintains the same padding and typography as primary buttons for alignment.

**`button-pill`** — A fully rounded variant (`{rounded.full}`) used for promotional badges, filter tags, and quick-select options. It uses a smaller font size (`{typography.button-sm}`) and tighter padding.

**`button-pill-outline`** — The outlined version of the pill button, used for filter options and category tags. It has a 1px hairline border and transparent background.

### Cards
**`product-card`** — The primary product display component, used on collection pages and search results. It features a white background, 12px rounded corners (`{rounded.md}`), and no padding on the container itself. The image area uses `{rounded.md}` on top corners only, with a 1:1 aspect ratio. Title, price, and rating are stacked below with consistent padding from `{spacing.base}`.

**`hero-banner`** — A full-width promotional section with a minimum height of 400px, using `{colors.surface-soft}` as background. It features large display typography (`{typography.display-xl}`) and generous section padding. An optional overlay (`{colors.scrim}` at 30% opacity) can be applied over background images for text readability.

### Navigation
**`top-nav`** — A fixed or sticky navigation bar at 72px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). The logo is centered at 32px height. Navigation links use `{typography.nav-link}` at 15px with 0.2px letter spacing. Active links show the brand orange (`{colors.primary}`) with a 2px bottom border. Hover states also transition to orange.

**`footer`** — A dark footer section using `{colors.ink}` (#121212) as background with white text. Links use `{colors.muted-soft}` (#929292) and lighten to white on hover. The newsletter signup combines a standard text input with a primary-colored submit button.

### Forms
**`text-input`** — Standard form input with a white background, 1px hairline border, 8px rounded corners, and 48px height. On focus, the border thickens to 2px and turns `{colors.primary}`. Error states use a red border (`{colors.error}`).

**`search-input`** — A pill-shaped input (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`) and a subtle border. Used in the site search and filter bars. On focus, it gains a 2px primary-colored border.

**`quantity-selector`** — A compact input group for adjusting product quantities, with a central text display flanked by two square buttons. The container has a 1px hairline border and 8px rounded corners.

### Badges
**`badge-new`** — A small, fully rounded badge using the brand orange for "New" or "Just Launched" indicators. Uses uppercase typography (`{typography.badge}`) with 0.5px letter spacing.

**`badge-sale`** — A red badge (`{colors.error}`) for sale or discount indicators. Same typography and shape as the new badge.

**`badge-info`** — A cyan badge (`{colors.accent-cyan}`) for informational tags like "Best Seller" or "Top Rated".

**`badge-outline`** — A subtle outlined badge for secondary tags like material or size indicators. Uses muted text and a 1px hairline border.

### Stepper & Progress
**`stepper-indicator`** — Circular step indicators used in multi-step flows (e.g., checkout, setup wizard). Inactive steps use a soft gray background with muted text. Active steps switch to the brand orange with white text. Connectors between steps use a 2px hairline line that turns orange when active.

**`progress-bar`** — A thin, full-width progress bar with 4px height and fully rounded ends. The track uses `{colors.hairline-soft}` and the fill uses `{colors.primary}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack in 1-column grid; hero banners reduce to 280px min-height; footer links stack vertically; search input becomes full-width; buttons go full-width on forms |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero banners at 360px min-height; footer uses 2-column layout; side filters become collapsible accordions |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero banners at 400px min-height; footer uses 4-column layout; persistent side filters on collection pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banners can extend to 500px; additional whitespace on sides; larger product card images |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target size
- Icon buttons are 40x40px with 44x44px tap area via padding
- Product card tap targets extend to full card area
- Quantity selector buttons are 44x44px
- Bottom nav items (mobile) are 48px tall with 44px wide tap targets
- Accordion headers are 48px tall for easy tapping

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-out drawer containing all links
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections
- Multi-column content sections (features, testimonials) collapse to single column or carousel
- Sidebar content (related products, recently viewed) moves below main content on mobile
- Table layouts convert to stacked card layouts below 744px
- Hero banner text overlays collapse to below-image placement on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover state colors for secondary and ghost buttons (assumed from brand behavior)
- Focus ring styles and colors for keyboard navigation
- Error message styling (text color, background, iconography)
- Loading state designs (skeleton screens, spinners)
- Empty state designs for carts, wishlists, and search results
- Dark mode color palette (not present on current site)
- Sub-brand palettes for Anova Precision Oven vs. Anova Sous Vide vs. Anova App
- Animation timing curves and transition durations
- Dropdown menu styles (mega menu, account menu)
- Mobile bottom navigation bar design
- Cookie consent banner styling
- Accessibility contrast ratios for all color combinations
- Print stylesheet specifications
- Specific Shopify theme customization overrides
- Custom select/option styling beyond basic input
- Date picker and calendar component styles
- Table and data grid styling
- Pagination component design
- Toast/notification component design
- Tooltip arrow positioning and animation
- Modal close button positioning and styling
- Video player component styling
- Image gallery/lightbox component design
- Social media icon set and colors
- Payment method icon set and colors
