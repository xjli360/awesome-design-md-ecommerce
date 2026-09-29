---
version: alpha
name: "Fellow"
source_url: "https://fellowproducts.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fellow is a design-driven kitchen appliance brand that brings a quiet, considered warmth to the daily ritual of coffee brewing. The brand's visual language is anchored in a deep, almost-black ink (`#1e1e1f`) and a soft, warm white canvas (`#f9f9f9`), creating a high-contrast stage for its sculptural products. Signature moves include the use of a muted, earthy palette — from the subtle warmth of `#f6ede0` and the soft greys of `#efefed` and `#e0e0dd` to the rich, toasted copper of `#9d523a` — that feels both premium and approachable. A distinctive accent of `#88acc3` (a dusty, muted blue) and a brighter `#1990c6` provide moments of cool relief, often used for key product details or interactive elements. The typography is a deliberate mix of the proprietary, rounded "Fellow Solar" for display and the clean, neutral "Sohne" for body text, creating a tension between playful warmth and functional clarity. Buttons and cards use `{rounded.sm}` (8px) and `{rounded.md}` (12px) radii, avoiding extreme pill shapes in favor of a refined, slightly soft geometry that mirrors the brand's product design philosophy. The overall feel is one of "everyday magic" — a space where the utilitarian act of making coffee is elevated through thoughtful materiality, generous whitespace, and a color story that whispers rather than shouts.

colors:
  primary: "#1e1e1f"
  primary-active: "#121212"
  primary-disabled: "#767474"
  ink: "#1e1e1f"
  body: "#4c4c4c"
  muted: "#767474"
  muted-soft: "#a7a5a5"
  hairline: "#d0cfcb"
  hairline-soft: "#dedede"
  canvas: "#f9f9f9"
  surface-soft: "#efefed"
  surface-card: "#ffffff"
  on-primary: "#f9f9f9"
  accent-copper: "#9d523a"
  accent-copper-light: "#f6ede0"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-dusty-blue: "#88acc3"
  surface-warm: "#f6ede0"
  border-light: "#e0e0dd"
  border-strong: "#b3b2b1"
  star-rating: "#1e1e1f"

typography:
  display-xl:
    fontFamily: "'Fellow Solar', 'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fellow Solar', 'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fellow Solar', 'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fellow Solar', 'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Sohne', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-copper:
    backgroundColor: "{colors.accent-copper}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-copper-active:
    backgroundColor: "#8a4732"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.accent-copper}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(30, 30, 31, 0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-copper}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-dusty-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: "0 12px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  price-compare:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep ink (`#1e1e1f`) with white text. Uses an 8px rounded corner (`{rounded.sm}`) and uppercase Sohne at 14px/600 weight with 0.5px letter spacing. On hover, it deepens to `{colors.primary-active}` (`#121212`). The disabled state fades to `{colors.primary-disabled}` (`#767474`), signaling an inactive action without harsh visual noise.

**`button-secondary`** — An outlined variant with a white fill and ink border, used for less prominent actions like "Learn More" or "Add to Wishlist." On hover, the background shifts to `{colors.surface-soft}` (`#efefed`), providing a subtle tactile response.

**`button-copper`** — A warm accent button using `{colors.accent-copper}` (`#9d523a`), reserved for premium or limited-edition product actions. Its active state darkens to `#8a4732`. This button carries the brand's material warmth and is often paired with copper-toned product photography.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip." Inherits the primary ink color and uppercase typography, with a hover state that adds a subtle underline or opacity shift.

**`button-icon-circle`** — A 40px circular icon button on a soft grey (`{colors.surface-soft}`) background, used for utility actions like search, cart, or menu toggles. The full roundness (`{rounded.full}`) makes it feel friendly and tactile.

### Cards
**`product-card`** — A white card with a soft 8px radius and a light hairline border (`{colors.hairline-soft}`). The product image sits flush to the top corners (`{rounded.sm} {rounded.sm} 0 0`), while text content is padded inside. On hover, the card gains a subtle shadow and a stronger border (`{colors.hairline}`), creating a gentle lift effect.

**`product-card-hover`** — The elevated state of the product card, adding a `boxShadow` of `0 4px 12px rgba(30, 30, 31, 0.08)` to the base card styling. This is the primary interaction feedback for product browsing.

### Navigation
**`nav-bar`** — A fixed 72px white navigation bar with a soft bottom border (`{colors.hairline-soft}`). Links use Sohne at 14px/500 weight with 0.3px letter spacing. Active links are underlined with a 2px ink border, while inactive links sit in `{colors.muted}`.

**`nav-link-active`** — The active state for navigation links, distinguished by a 2px bottom border in the primary ink color. This provides a clear, understated wayfinding signal.

**`nav-link-inactive`** — Default navigation links in `{colors.muted}` (`#767474`), ensuring the active link stands out without needing a background pill or heavy weight.

### Forms
**`text-input`** — A standard text input with a white background, 8px radius, and a light hairline border. On focus, the border switches to the primary ink color, providing clear focus indication. Error states use the copper accent (`{colors.accent-copper}`) for the border.

**`text-input-active`** — The focused state of the text input, where the border color changes to `{colors.primary}` (`#1e1e1f`). No other visual change, keeping the interaction clean and minimal.

**`text-input-error`** — The error state for text inputs, using `{colors.accent-copper}` (`#9d523a`) for the border. This warm error color is less jarring than a pure red and aligns with the brand's material palette.

**`select-dropdown`** — A styled select element matching the text input's dimensions and border, using `{typography.body-sm}` for the selected value. The dropdown arrow is typically rendered as a custom icon in the ink color.

### Badges
**`badge-new`** — A small, full-rounded badge in the copper accent (`#9d523a`), used to flag new arrivals. Uses uppercase Sohne at 11px/600 weight with tight padding.

**`badge-sale`** — A blue accent badge (`{colors.accent-blue}` / `#1990c6`) for sale or promotional items. The cool tone provides contrast against the warm copper badges.

**`badge-eco`** — A dusty blue badge (`{colors.accent-dusty-blue}` / `#88acc3`) for sustainable or eco-friendly product attributes. This softer blue sits quietly in the palette without competing with the primary blue.

### Footer
**`footer-section`** — A full-width footer with the primary ink background (`#1e1e1f`) and white text. Links are rendered in `{colors.muted-soft}` (`#a7a5a5`) and transition to white on hover. The footer uses generous section padding (`{spacing.section}`) to create breathing room.

**`footer-link`** — Standard footer links in a soft grey (`{colors.muted-soft}` / `#a7a5a5`), using Sohne at 14px/500 weight. The muted tone keeps the footer from feeling heavy.

**`footer-link-hover`** — The hover state for footer links, transitioning to white (`{colors.on-primary}`) for clear interactivity against the dark background.

### Search
**`search-bar`** — A full-rounded search bar with a white background and hairline border, used in the navigation or hero sections. On focus, the border switches to the primary ink color. The 44px height is slightly shorter than buttons, signaling its utility role.

**`search-bar-active`** — The focused state of the search bar, with the border changing to `{colors.primary}`. This is the only visual change, maintaining the clean, minimal aesthetic.

### Accordion
**`accordion-header`** — A clickable header for expandable content sections, using `{typography.title-sm}` with a bottom border. The header has no background, relying on the border and typography to define the interaction zone.

**`accordion-content`** — The expandable content area below the accordion header, using `{typography.body-sm}` in the body color. Padding is applied only to the bottom, keeping the layout tight.

### Quantity Selector
**`quantity-selector`** — A compact input for adjusting product quantities, using a soft grey background (`{colors.surface-soft}`) and 8px radius. The 44px height matches the search bar, creating visual consistency across utility elements.

### Ratings & Pricing
**`rating-stars`** — Star icons rendered in the primary ink color at 16px. The brand uses a simple filled/empty star system without fractional stars, keeping the visual language clean.

**`price-display`** — The current product price, using `{typography.title-md}` in the ink color. No currency symbol styling is applied; the price stands alone.

**`price-compare`** — The original or compare-at price, rendered in `{colors.muted}` with a line-through. This is used for sale items to show the discount.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, hamburger menu, stacked product cards, reduced hero padding, full-width buttons |
| Tablet | 744–1128px | Two-column product grid, persistent top nav with condensed links, search bar collapses to icon, hero text scales down |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, search bar expands, hero uses display-xl |
| Wide | > 1440px | Max-width container (1440px) centered, four-column product grid, increased whitespace, hero uses larger display sizing |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons are 40px with 44px touch padding.
- Product cards have a minimum 80px tap area for the "Add to Cart" action.
- Accordion headers have a minimum 48px tap height.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-out drawer.
- The search bar collapses to a magnifying glass icon on mobile, expanding to a full-width input on tap.
- Product grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer link columns stack vertically on mobile, with each section becoming an accordion.
- Hero sections reduce padding and font sizes on mobile, often removing background imagery.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors.
- Error styling for forms is inferred from the brand's accent palette; actual error messages, validation icons, and error text colors are not confirmed.
- Dark mode is not present on the live site; no dark mode tokens or strategies are available.
- Sub-brand or collection-specific palettes (e.g., "Stagg," "Ode," "Opus") may exist but were not extracted.
- Animation and transition durations (ease-in-out, spring curves) are not documented.
- Focus ring styles (outline, offset, color) are not confirmed.
- Dropdown menu and modal overlay styles (scrim opacity, z-index) are not extracted.
- The exact font weight for "Fellow Solar" is assumed to be 400; actual weight values may vary.
- The `textTransform: uppercase` on button typography is inferred from the brand's visual language but not confirmed from CSS.
- Star rating fractional rendering (half-stars, empty states) is not documented.
- The `boxShadow` value for product card hover is an educated guess based on common design patterns.
