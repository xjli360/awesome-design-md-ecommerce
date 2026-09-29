---
version: alpha
name: "Blue Orange Games"
source_url: "https://www.blueorangegames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A primary blue (#65afe0) and a marigold yellow (#f5c400) that feel like a playground floor and a sunbeam — this is a brand that signals "simply fun for all" through color contrast alone, without needing a single illustration. The blue carries the header, navigation, and primary CTAs as a calm, trustworthy anchor, while the yellow bursts through as the accent voltage on sale badges, price highlights, and hover states. The site reads as a clean, white-canvas grid with generous spacing between game tiles, each product card a soft rectangle with the blue used sparingly — a border, a button, a category tag. There is no hard geometry: corners are gently rounded ({rounded.sm} on cards, {rounded.md} on buttons) to keep the mood approachable for both kids and adults. The typography leans on a system sans-serif stack (likely system-ui or a web-safe fallback, as no custom font declarations were found), set at modest weights — body copy at 16px/1.5, game titles at 20px/1.3, and category headers in a slightly bolder weight. The brand's voice is direct and inclusive: "Award-winning games for the whole family" appears in the hero, and the navigation is flat and shallow — Shop, About, Blog, and a search icon — no mega-menus, no clutter. The footer is a simple three-column layout with social icons, a newsletter signup, and a "Made with love" tagline. The overall feel is that of a well-organized toy store shelf: everything has its place, the colors are cheerful but not chaotic, and the white space lets each game breathe.

colors:
  primary: "#65afe0"
  primary-active: "#4a9bd0"
  primary-disabled: "#b3d9f0"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#f5c400"
  accent-yellow-active: "#d4a800"
  accent-yellow-soft: "#fce680"
  badge-new: "#f5c400"
  badge-sale: "#e74c3c"
  star-rating: "#f5c400"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary-active}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
    height: 48px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
    height: 40px
  social-icon:
    textColor: "{colors.muted}"
    height: 24px
  social-icon-hover:
    textColor: "{colors.primary}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  age-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  player-count:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand blue (#65afe0) and white text. Used for "Add to Cart", "Shop Now", and primary navigation actions. On hover, shifts to a slightly darker blue (`{colors.primary-active}`). Disabled state uses a lighter blue (`{colors.primary-disabled}`) with reduced opacity. Corners are rounded at {rounded.md} (12px) for a friendly, approachable feel.

**`button-secondary`** — An outlined variant with a white fill and blue border. Used for secondary actions like "Learn More" or "View Details". On hover, the background fills with the soft surface color (`{colors.surface-soft}`) and the border darkens to the active blue. Maintains the same 12px corner radius and 44px height as the primary button for visual consistency.

**`button-accent-yellow`** — The brand's accent button, filled with marigold yellow (#f5c400) and dark text. Used sparingly for high-urgency CTAs like "Sale" promotions, "Limited Edition" calls, or the hero banner's primary action. On hover, darkens to a deeper gold (`{colors.accent-yellow-active}`). This button carries the brand's playful energy.

**`button-pill`** — A smaller, fully rounded pill button used for filter tags, category navigation, and compact actions. Filled with the primary blue and white text. The pill shape (`{rounded.full}`) reinforces the brand's friendly, non-intimidating character. Also available in an outlined variant (`button-pill-outline`) for secondary filter states.

### Cards
**`product-card`** — The core product display unit, a white card with a soft border and 8px corner radius. Contains a product image (full-width, no internal padding), the game title, price, and optional badges. On hover, the card gains a blue border and a subtle drop shadow to indicate interactivity. The card is designed to work in a grid layout with consistent spacing between tiles.

**`product-card-badge`** — A small, yellow badge (`{colors.accent-yellow}`) overlaid on the product card image, used to denote "New", "Award Winner", or "Staff Pick". The badge uses uppercase, bold, 11px type with tight tracking. A red variant (`product-card-badge-sale`) is reserved for sale/discount indicators.

### Navigation
**`nav-bar`** — A fixed-height, white navigation bar with a soft bottom border. Contains the brand logo (left), navigation links (center), and utility icons (right: search, cart, account). Links are set in 15px medium weight. The active page link is underlined with a 2px blue line and the text turns blue. On hover, links also turn blue without the underline.

**`category-tag`** — A pill-shaped filter tag used in the category strip below the hero. Inactive tags have a soft gray background and muted text. Active tags switch to the primary blue background with white text. These tags allow users to filter games by category (e.g., "Strategy", "Family", "Card Games").

### Forms
**`text-input`** — A standard text input with a white background, 1px hairline border, and 8px corner radius. Used for the newsletter signup, search bar, and any form fields. On focus, the border thickens to 2px and turns blue. Error states use a red border (`{colors.badge-sale}`) with an accompanying error message in red text.

**`search-bar`** — A fully rounded, pill-shaped search input with a white background and hairline border. On focus, the border thickens to 2px and turns blue. The search icon is positioned on the left, and a clear button appears on the right when text is entered.

### Footer
**`footer`** — A three-column layout on a soft gray background (`{colors.surface-soft}`). Contains links to support pages, social media icons, and a newsletter signup form. Footer links are muted gray and turn blue on hover. The newsletter input and submit button sit side by side, with the button using the primary blue.

### Badges & Labels
**`age-badge`** — A small, gray badge indicating the recommended age range for a game (e.g., "Ages 8+"). Uses 12px type and 4px corner radius. Placed below the game title on product cards.

**`player-count`** — A text label indicating the number of players (e.g., "2-4 Players"). Uses 12px type in muted gray. Placed next to the age badge on product cards.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards; nav collapses to hamburger menu; hero banner reduces padding; category tags scroll horizontally; footer stacks vertically; search bar becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce font size to 14px; hero banner uses 24px display type; category tags wrap to two rows; footer uses two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero banner at full size; category tags in a single row; footer in three columns |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero banner with larger 32px display type; all elements use maximum spacing |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 44px (48px on mobile) to meet touch target guidelines
- Product cards have a minimum tap area of 120px x 120px on mobile
- Category tags are at least 32px tall with 16px horizontal padding
- Search bar is 44px tall on all breakpoints
- Nav links have a minimum 44px tap area on mobile (expanded from 32px on desktop)

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-out drawer
- The category tag strip becomes a horizontally scrollable row on mobile, with snap points at each tag
- The product grid collapses from 3-4 columns to a single column on mobile
- The hero banner image stacks below the text on mobile (text first, image second)
- The footer collapses from three columns to a single stacked column on mobile
- The newsletter signup form stacks vertically on mobile (input above button)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font family declarations were found on the live site; the brand likely uses a system font stack. A custom brand font (if any) would need to be identified and added to the typography block.
- Only two brand colors were extracted from the live site (#65afe0 and #f5c400). Additional brand colors (secondary accents, error states, success states) may exist but were not detected. The red used for sale badges (#e74c3c) is a common web color and may not be official brand.
- Hover and active states for all components are inferred from common patterns; actual brand-specific hover animations, transitions, and micro-interactions are unknown.
- The extracted colors may include Shopify checkout widget colors or social media icon colors that were not fully filtered. The primary blue (#65afe0) and accent yellow (#f5c400) appear to be intentional brand colors based on their consistent use across the site.
- No dark mode or high-contrast mode styles were detected.
- Error state styling for forms (colors, icons, animation) is not documented.
- Loading states, skeleton screens, and empty state designs are unknown.
- The brand's illustration style and icon set (if any) are not captured in this document.
- Sub-brand or collection-specific color palettes (e.g., for specific game lines) are not documented.
