---
version: alpha
name: "Dark Horse Direct"
source_url: "https://www.darkhorsedirect.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A collectibles storefront that wraps its premium statues, figures, and art prints in a deep plum-and-blue palette — `#54496d` as the signature voltage, a moody violet-gray that appears nowhere else in the top extracted colors and reads as the brand's true identity, with `#006fcf` as a crisp accent for CTAs and links. The canvas is near-black (`#171616`), not white, making every product image glow like a gallery piece against a dark wall. Typography runs Figtree at moderate weights — body copy at 400, buttons and nav at 500–600 — with generous letter-spacing on display sizes that suggests a premium, unhurried reading experience. Cards and buttons use soft corners (`{rounded.sm}` for buttons, `{rounded.md}` for product cards), avoiding the pill shapes of mass-market ecommerce in favor of a more reserved, collectible-shop feel. The top navigation is a dark bar (`#121212`) with white text, and the search icon sits as a simple line icon rather than an orb, reinforcing the brand's quiet confidence. Badges for "Exclusive" or "Pre-Order" appear in `#006fcf` on dark backgrounds, creating a small but insistent pop of blue against the plum-and-charcoal system. The overall effect is of a specialty gallery that happens to sell online — not a toy store, but a serious destination for collectors.

colors:
  primary: "#54496d"
  primary-active: "#4a3f61"
  primary-disabled: "#8a7fa5"
  ink: "#ffffff"
  body: "#dedede"
  muted: "#a0a0a0"
  muted-soft: "#808080"
  hairline: "#3a3a3a"
  hairline-soft: "#2a2a2a"
  canvas: "#171616"
  surface-soft: "#1e1e1e"
  surface-card: "#222222"
  on-primary: "#ffffff"
  accent-blue: "#006fcf"
  accent-blue-hover: "#005bb5"
  badge-new: "#006fcf"
  badge-sold-out: "#808080"
  star-rating: "#dedede"
  error: "#cf3a3a"
  success: "#3acf6a"

typography:
  display-xl:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-hover:
    backgroundColor: "{colors.accent-blue-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "#121212"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-item:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-item-hover:
    textColor: "{colors.accent-blue}"
  nav-link-item-active:
    textColor: "{colors.accent-blue}"
    borderBottom: "2px solid {colors.accent-blue}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.accent-blue}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-exclusive:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-preorder:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "#121212"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    border: "2px solid {colors.accent-blue}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  cart-item-remove:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  cart-item-remove-hover:
    textColor: "{colors.error}"
  checkout-button:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `#54496d` (the brand's signature plum) with white text and a 6px corner radius. On hover, it deepens to `#4a3f61`; disabled state uses `#8a7fa5`. Used for "Add to Cart", "Pre-Order Now", and primary form submissions. **`button-secondary`** — An outlined variant with transparent background, white text, and a 2px `#3a3a3a` border. Hover fills the background with `#1e1e1e` and brightens the border to white. Used for "Learn More", "View Details", and secondary actions. **`button-accent`** — The accent CTA in `#006fcf` blue, used sparingly for high-priority actions like "Shop Now" on hero banners and "Checkout". Hover shifts to `#005bb5`.

### Cards
**`product-card`** — A dark card (`#222222`) with 12px corners and 16px padding, containing a square product image with 6px rounded corners, a title in `{typography.title-sm}`, and a price in `{typography.body-md}`. Hover state adds a 1px `#3a3a3a` border and shifts background to `#1e1e1e`. Badges overlay the top-left of the image area. **`cart-item`** — A compact card for the cart drawer, with 12px rounded corners and 12px padding. Contains a thumbnail, title, quantity selector, price, and a remove link that turns red on hover.

### Navigation
**`nav-bar`** — A fixed 64px bar at `#121212` with white uppercase nav links in `{typography.nav-link}` (14px, 500 weight, 0.5px letter-spacing). Active and hover states highlight the link in `#006fcf` blue, with an optional 2px bottom border on the active item. The search bar sits as a right-aligned element within the nav. **`nav-link-item`** — Individual navigation links with 8px vertical and 12px horizontal padding, uppercase styling, and blue accent on interaction.

### Forms
**`text-input`** — A dark input field (`#222222` background) with `#dedede` text, 6px rounded corners, and a `#3a3a3a` border. Focus state swaps to a 2px `#006fcf` blue border. Error state uses a 2px `#cf3a3a` red border. Used for email signups, search, and checkout forms. **`filter-dropdown`** — A compact 40px dropdown for product filtering, matching the input styling with a `#3a3a3a` border and blue focus state.

### Footer
**`footer`** — A `#121212` bar with `#808080` muted text in `{typography.body-sm}`. Links are `#808080` and lighten to white on hover. Contains columns for customer service, about links, social icons, and legal text. Padding is 48px vertical and 24px horizontal.

### Hero
**`hero-section`** — A full-width section on the `#171616` canvas with a large display heading (`{typography.display-xl}`), a supporting subtitle in `{typography.body-md}`, and a single `#006fcf` accent CTA button. Padding is 64px vertical and 24px horizontal. The hero may feature a full-bleed product image or a dark gradient overlay.

### Badges
**`badge-exclusive`** — A small `#006fcf` blue pill with white uppercase text at 11px, 0.5px letter-spacing, and 2px rounded corners. Used to flag limited-edition items. **`badge-sold-out`** — Gray (`#808080`) badge for out-of-stock items. **`badge-preorder`** — Plum (`#54496d`) badge for upcoming releases.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 column), nav collapses to hamburger menu, hero text scales to `{typography.display-md}`, buttons become full-width, footer stacks vertically, search bar hides behind icon |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but reduced to 4–5 items, hero text at `{typography.display-lg}`, footer splits into 2 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at full `{typography.display-xl}`, footer in 3–4 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero may feature larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px.
- Product card tap targets are the entire card surface.
- Nav links have 8px vertical padding for comfortable tapping.
- Quantity selector buttons are 40px × 40px minimum.
- Filter dropdowns and pagination buttons are 36px–40px tall.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-out drawer.
- The search bar collapses to a search icon that opens an overlay input on tap.
- The product grid collapses from 3–4 columns to 1 column.
- The footer collapses from 3–4 columns to a single stacked column.
- Hero sections reduce padding and font size.
- Filter controls collapse into a single "Filter" button that opens a modal or dropdown.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; exact extracted hover colors were not available from the static extraction.
- Error and success states for forms (validation messages, borders) were not extracted; colors are best guesses based on accessibility standards.
- The exact font sizes and line heights for typography tokens were not extractable from the static CSS; values are estimated based on common Figtree usage at similar brand scales.
- The brand may use additional accent colors (e.g., for limited-edition drops, seasonal themes) that were not captured in the top extracted hex list.
- Dark mode is not applicable as the brand already uses a dark canvas; no light mode variant was extracted.
- Sub-brand or franchise-specific color palettes (e.g., for specific collectible lines) were not extracted.
- Animation durations, easing curves, and transition properties were not extracted.
- Iconography style (line vs. filled, stroke weights) was not extracted.
- The Shopify checkout flow may introduce additional colors (Shopify Pay buttons, Klarna badges) that are not part of the brand's design system.
- The extracted hex list (`#006fcf`, `#54496d`, `#dedede`, `#171616`, `#121212`) is sparse and likely represents only the most dominant colors on the homepage; the brand may use additional tones for hover states, gradients, or decorative elements that were not captured.
