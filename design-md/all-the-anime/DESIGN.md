---
version: alpha
name: "All the Anime"
source_url: "https://www.alltheanime.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #2d8fce — the exact shade of a clear summer sky seen through an airplane window — acts as the brand's primary voltage, appearing on every add-to-cart button, collection header, and navigation highlight. This is not the electric cyan of gaming or the navy of prestige streaming; it's a calm, confident blue that signals trust and quality in physical media. The palette is anchored by a near-black ink (#121212) for body text and a warm light-gray canvas (#f3f3f3) that softens the shopping experience, while a secondary blue (#334fb4) appears in footer links and secondary actions, creating a subtle gradient of authority. Assistant and Cabin — two clean, geometric sans-serifs — handle all typography, with Assistant taking the heavier lifting for body copy and Cabin appearing in display contexts. Product cards use generous whitespace and a consistent 12px radius ({rounded.md}), giving each Blu-ray or art book the breathing room of a gallery display. The checkout flow inherits Shopify's standard widget colors, but the brand's own interface maintains a disciplined two-blue system: the sky primary and the indigo secondary, with no tertiary accent to distract from the product photography. Badges for "Pre-order" and "Exclusive" appear in the primary blue on white, while sold-out items fade to #dedede — a muted gray that respects the customer's time without shouting.

colors:
  primary: "#2d8fce"
  primary-active: "#1f6fa3"
  primary-disabled: "#b3d9f0"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f3f3f3"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#334fb4"
  secondary-active: "#263d8a"
  badge-preorder: "#2d8fce"
  badge-exclusive: "#334fb4"
  badge-soldout: "#dedede"
  badge-on-primary: "#ffffff"
  footer-bg: "#121212"
  footer-text: "#c6e5f9"
  star-rating: "#2d8fce"
  error: "#d32f2f"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Cabin', 'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cabin', 'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cabin', 'Assistant', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  footer-link:
    fontFamily: "'Assistant', 'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    color: "{colors.footer-text}"

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
    border: none
    cursor: pointer
    transition: background-color 0.2s ease
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
    cursor: pointer
    transition: background-color 0.2s ease, color 0.2s ease
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 24px
    height: 48px
    border: none
    cursor: pointer
  button-large:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
    border: none
    cursor: pointer
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
    border: none
    cursor: pointer
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
    transition: border-color 0.2s ease
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
    transition: box-shadow 0.2s ease, transform 0.2s ease
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)"
    transform: "translateY(-2px)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    objectFit: contain
    backgroundColor: "{colors.canvas}"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
    display: flex
    alignItems: center
    justifyContent: center
  hero-banner-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.3)"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.06)"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.badge-on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-exclusive:
    backgroundColor: "{colors.badge-exclusive}"
    textColor: "{colors.badge-on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    fontWeight: 700
    padding: "{spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.lg} 0"
  pagination-active:
    textColor: "{colors.primary}"
    fontWeight: 700
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
    cursor: pointer
    transition: background-color 0.2s ease, border-color 0.2s ease
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
    cursor: pointer
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, rendered in sky blue (#2d8fce) with white text and an 8px radius ({rounded.sm}). On hover, it deepens to #1f6fa3 ({colors.primary-active}) with a 0.2s ease transition. The disabled state uses a pale blue (#b3d9f0) with a not-allowed cursor, signaling unavailability without visual noise. Height is fixed at 48px with 12px/24px padding for comfortable tap targets.

**`button-secondary`** — An outlined variant with a white background and a 2px solid border in the primary blue. Text matches the primary color. On hover, the background fills with primary blue and text inverts to white, creating a satisfying reveal. Used for "View Details" and secondary checkout actions.

**`button-tertiary`** — A text-only button with no background or border, using the primary blue for text. Reserved for inline actions like "Clear filters" or "Cancel" where a full button would feel heavy. Maintains the same 48px height and padding for alignment consistency.

**`button-large`** — A taller (56px) variant of the primary button, used in hero sections and the main "Add to Cart" on product pages. Uses 18px bold text ({typography.button-lg}) and 16px/32px padding for visual weight.

**`button-small`** — A compact 36px variant with 4px radius ({rounded.xs}) and 14px text. Used for quantity adjustments in the cart and inline "Apply" actions on filters.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px radius ({rounded.md}) and a soft hairline border. The image area uses `object-fit: contain` on a light gray (#f3f3f3) background, ensuring product art is never cropped awkwardly. On hover, the card lifts 2px with a subtle box shadow. The title sits below the image in 16px bold, followed by the price in 16px semibold. Badges (Pre-order, Exclusive, Sold-out) are absolutely positioned at the top-left with 4px radius and uppercase 11px text.

**`hero-banner`** — A full-width section with a minimum height of 400px, centered content, and a light gray background. When an overlay is present (for dark background images), a 30% black scrim ensures white text remains legible. The display text uses 36px Cabin bold with tight letter spacing.

### Navigation
**`nav-bar`** — A fixed 72px white header with a soft bottom border. Navigation links use 15px semibold Assistant, with the active page underlined in primary blue. Inactive links render in muted gray (#666666). The search bar sits as a pill-shaped input with a subtle shadow, inviting exploration.

**`breadcrumb`** — A secondary navigation element using 13px medium-weight text in muted gray, with the current page rendered in near-black. Spaced at 8px top/bottom for breathing room.

### Forms
**`text-input`** — A 48px white input with an 8px radius and a 1px hairline border. On focus, the border thickens to 2px and turns primary blue. Placeholder text is a soft gray (#999999). Error states use a red (#d32f2f) border with matching error message below.

**`select-input`** — Matches the text-input dimensions and styling, with a custom dropdown arrow in primary blue. Used for sorting and filtering options.

### Badges
**`badge-preorder`** — Sky blue background with white uppercase 11px text, 4px radius. Positioned on product cards to indicate upcoming releases.

**`badge-exclusive`** — Indigo (#334fb4) background, used for limited editions and convention exclusives. Same typography and radius as preorder badge.

**`badge-soldout`** — Light gray (#dedede) background with muted text (#666666). Communicates unavailability without the urgency of red.

### Footer
**`footer`** — A dark (#121212) full-width section with light blue (#c6e5f9) text links. Links hover to white. Uses 14px regular-weight Assistant for readability against the dark background. Padding is generous at 48px vertical and 32px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger, hero banner reduces to 300px min-height, search bar moves to full-width below nav, buttons become full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 col), nav links visible but condensed, hero banner at 350px min-height, search bar remains in nav but narrower, buttons maintain inline layout |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav with all links, hero banner at 400px min-height, search bar at standard width, side filters visible on collection pages |
| Wide | > 1440px | Four-column product grid (4 col) on collection pages, max-width container at 1440px for readability, hero banner scales to 500px min-height, additional whitespace around all elements |

### Touch Targets
- All buttons and interactive elements maintain a minimum 48px height for touch accessibility
- Filter chips are 36px tall with 16px horizontal padding for easy tapping
- Product card tap targets extend to the full card area, not just the title
- Nav links have 44px minimum tap area (exceeds WCAG 2.1 AA)
- Quantity selector buttons are 40px squares with centered icons
- Search bar is 48px tall with full-width tap area on mobile

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product filters collapse to a bottom sheet on mobile, triggered by a "Filter" button
- Footer link columns stack vertically below 744px, with accordion-style expand/collapse for each section
- Breadcrumbs truncate to "Home > ... > Current Page" on mobile
- Product descriptions collapse to a "Read more" toggle below 744px
- Cart sidebar becomes a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary and secondary button hover states were reliably extracted. Hover states for product cards, filter chips, and footer links are inferred from common patterns.
- **Error styling**: Error text color (#d32f2f) is inferred from common web conventions, not extracted from the live site. Error message placement and animation are not documented.
- **Focus states**: Focus ring styles (color, width, offset) were not extractable. WCAG 2.1 AA recommends a 2px solid outline in a contrasting color.
- **Dark mode**: No dark mode implementation was detected. The footer uses a dark background (#121212) with light text (#c6e5f9), but this is a section-level treatment, not a system-wide dark mode.
- **Sub-brand palettes**: The brand may have sub-brand color variations for specific anime series or collections (e.g., Studio Ghibli, Attack on Titan). These were not extractable from the main store.
- **Animation timing**: Transition durations (0.2s for buttons, 0.2s for cards) are inferred from common patterns. Actual values may vary.
- **Typography scale**: Font sizes for display-xl (36px) and display-lg (28px) are inferred from common e-commerce patterns. The extracted fonts (Assistant, Cabin) are confirmed, but exact size/weight combinations are estimated.
- **Checkout flow**: The checkout page uses Shopify's default styling, which may include colors not in the brand palette (e.g., Shopify green for success states). These were excluded from the design system.
- **Accessibility**: ARIA labels, skip-to-content links, and screen reader announcements were not extractable. These should be audited separately.
- **Image aspect ratios**: Product card images use `object-fit: contain`, but specific aspect ratios (e.g., 3:4 for Blu-ray cases, 16:9 for art books) were not confirmed.
