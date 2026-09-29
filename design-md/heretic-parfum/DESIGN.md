---
version: alpha
name: "Heretic Parfum"
source_url: "https://hereticparfum.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A darkly romantic, naturally-derived fragrance house that speaks in whispers of ink-black rebellion and botanical purity. The palette is anchored in near-black charcoals — `#030303` for the deepest shadows, `#222222` for body text, `#333333` for secondary elements — against a canvas of warm off-whites (`#f5f5f5`, `#f3f3f3`, `#eeeeee`) that feel like aged parchment rather than sterile white. The brand's signature voltage comes from unexpected accents: a teal `#0d6160` that reads as forest shadow, a muted gold `#ffc863` like amber catching light, and a restrained coral `#d02e2e` used sparingly for editorial emphasis. Typography runs lean on Work Sans and PT Sans at modest weights — there is no heavy display face, no bold declaration; the brand trusts its botanical photography, its apothecary-vessel product shots, and generous whitespace (`{spacing.section}`) to carry mood. Every corner is softly radiused (`{rounded.sm}` for cards, `{rounded.md}` for modals, `{rounded.full}` for badges and ingredient pills), evoking hand-blown glass and worn stone rather than industrial precision. The result is a system that feels both ancient and contemporary — a digital storefront for a perfumer who works with rare essences and refuses to use synthetics.

colors:
  primary: "#0d6160"
  primary-active: "#094d4c"
  primary-disabled: "#8cb5b4"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#808080"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  canvas: "#f5f5f5"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ffc863"
  accent-coral: "#d02e2e"
  accent-blue: "#1990c6"
  accent-blue-deep: "#136f99"
  accent-pink: "#e72860"
  accent-green: "#1a7b3c"
  accent-green-soft: "#f0fdf4"
  accent-green-mint: "#bbf7d0"
  accent-purple: "#94a4ff"
  accent-purple-deep: "#4f61f8"
  badge-new: "#d72c0d"
  scrim: "#030303"
  surface-dark: "#121212"

typography:
  display-xl:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'PT Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'PT Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'PT Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'PT Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif"
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-coral}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  nav-link:
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.base}"
    maxWidth: 500px
  hero-cta:
    marginTop: "{spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-eco:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  ingredient-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  ingredient-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(13,97,96,0.15)"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
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
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.15)"
  modal-overlay:
    backgroundColor: "rgba(3,3,3,0.6)"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  rating-stars:
    color: "{colors.accent-gold}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    width: 44px
    height: 44px
  slider:
    trackColor: "{colors.hairline}"
    trackActiveColor: "{colors.primary}"
    thumbColor: "{colors.primary}"
    thumbSize: 20px
  tooltip:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature teal `#0d6160` with white text and uppercase Work Sans at 14px. On hover, it deepens to `#094d4c`; when disabled, it fades to a muted sage `#8cb5b4`. The 8px corner radius (`{rounded.sm}`) keeps it approachable without sacrificing the brand's refined edge.

**`button-secondary`** — An outlined variant on a white canvas with a single-pixel hairline border (`{colors.hairline}`). Active state fills the background with `{colors.surface-soft}` and darkens the border to `{colors.muted}`. Used for "Add to Wishlist" and secondary cart actions.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Learn More" or "Read Ingredients". Active state gains a subtle `{colors.surface-soft}` background. The uppercase lettering and 0.5px tracking maintain consistency with the primary button.

**`button-pill`** — A fully rounded pill variant for compact contexts like filter bars or quick-add actions. Available in filled teal or outline-only (`button-pill-outline`) for secondary filter states. At 36px tall, it's smaller than the primary button but retains the same uppercase typographic voice.

### Cards
**`product-card`** — The core product display unit, a white card with 8px radius, 16px padding, and a whisper-thin shadow (`0 1px 3px rgba(0,0,0,0.06)`). On hover, the shadow lifts to `0 4px 12px rgba(0,0,0,0.1)`. The image area is a perfect 1:1 square with 4px radius, echoing the apothecary bottle proportions. Title sits in `{typography.title-sm}` (16px/500 weight) with price below in `{typography.body-sm}` at `{colors.muted}`.

### Navigation
**`nav-bar`** — A fixed 72px bar on a white canvas with a soft bottom border (`{colors.hairline-soft}`). On scroll, it gains a subtle box-shadow. Navigation links are set in uppercase Work Sans at 13px with 0.8px tracking — the active state drops a 2px teal underline. The bar houses the brand wordmark, product category links, search icon, and cart icon.

### Forms
**`text-input`** — Standard text fields with white background, 8px radius, and a hairline border. Focus state swaps the border to `{colors.primary}` and adds a 3px teal-tinted ring (`rgba(13,97,96,0.15)`). Error state uses `{colors.accent-coral}` (`#d02e2e`). Disabled fields drop to `{colors.surface-soft}` background with muted text.

**`select-input`** — Matches text-input dimensions and styling but includes a custom dropdown arrow. The chevron is rendered in `{colors.muted}` and flips on open.

**`textarea-input`** — Same styling as text-input but with no fixed height, allowing multi-line content for fields like "Gift Message" or "Notes".

### Footer
**`footer`** — A dark section anchored in `#121212` (`{colors.surface-dark}`) with muted gray text (`{colors.muted-soft}`). Links are underlined on hover and transition to white. Section headings use `{typography.title-sm}` in white. The footer spans the full width with 64px vertical padding and houses newsletter signup, navigation columns, and legal text.

### Badges & Pills
**`badge`** — Small, fully rounded labels for product attributes. The default badge uses the amber gold `#ffc863` for "Best Seller" or "Limited Edition" tags. A red variant (`#d72c0d`) signals "New". A gray variant marks "Sold Out". An eco variant uses a soft green background (`#f0fdf4`) with deep green text (`#1a7b3c`) for "Naturally Derived" or "Vegan" labels.

**`ingredient-pill`** — Filter chips for the ingredient directory, rendered in `{colors.surface-soft}` with body text. Active state fills with the primary teal and white text. Used in the "Shop by Note" or "Shop by Ingredient" navigation strips.

### Modals
**`modal`** — A white card with 12px radius, 32px padding, and a substantial shadow (`0 8px 32px rgba(0,0,0,0.15)`). The overlay uses a 60% opacity black scrim (`rgba(3,3,3,0.6)`). Used for quick-add to cart, ingredient detail popups, and size selection.

### Accordion
**`accordion`** — Collapsible sections with a 1px soft hairline border and 8px radius. Headers use `{typography.title-sm}` with 16px horizontal padding and a rotating chevron icon. Content area pads at 12px bottom with 24px horizontal padding. Used for product descriptions, fragrance notes, and shipping details.

### Quantity Selector
**`quantity-selector`** — A compact 44px tall control with a hairline border and 8px radius. The minus/plus buttons sit on a `{colors.surface-soft}` background at 44px square. The center value displays in `{typography.body-md}`. Used on product detail pages and cart line items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), nav collapses to hamburger, hero text centers, product cards stack vertically, footer columns stack, search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid (2-up), nav shows top-level links, hero maintains left-aligned text, footer splits into 2 columns, search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid (3-up), full nav with all links visible, hero with large imagery, footer in 4 columns, persistent search bar |
| Wide | > 1440px | Four-column product grid (4-up), max-width container at 1440px, hero scales with viewport, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Product card tap targets include the entire card surface, not just text
- Filter pills and ingredient badges are minimum 36px tall for comfortable tapping
- Quantity selector buttons are 44px square
- Mobile nav hamburger icon is 48x48px
- Cart icon and search icon in nav are 44x44px

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px, revealing a full-screen drawer overlay
- Product filters collapse to a "Filter" button that opens a bottom sheet on mobile
- Footer navigation columns collapse to accordion-style sections below 744px
- Product image galleries collapse from thumbnail strip to swipeable carousel on mobile
- Multi-column ingredient lists collapse to single column below 744px
- Hero sections reduce padding from 64px to 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom effect, alternate image reveal) could not be reliably extracted
- Error state styling for forms beyond border color (error message typography, icon placement) is inferred
- Dark mode palette is not present on the live site; all dark surfaces use `#121212` as an approximation
- Sub-brand or collection-specific palettes (e.g., "Dirty" collection, "Botanical" line) may exist but were not detected
- Animation timing and easing curves (transition durations, spring physics) are not documented
- Focus ring styles beyond the text-input pattern (e.g., for buttons, links, cards) are not confirmed
- Loading states (skeleton screens, spinner designs) were not observed on the live site
- Cart and checkout flow components (cart drawer, checkout button, shipping form) are inferred from Shopify defaults
- Mobile-specific gesture behaviors (swipe to dismiss, pull to refresh) are not documented
- Print stylesheet behavior is unknown
