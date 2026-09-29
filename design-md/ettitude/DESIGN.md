---
version: alpha
name: "Ettitude"
source_url: "https://www.ettitude.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ettitude is a sanctuary of calm, a luxury bamboo bedding brand that speaks in hushed, earthy tones rather than loud declarations. The palette is drawn from the quiet corners of nature — the deep ink of a forest at dusk (`#212121`), the soft charcoal of river stones (`#3f3d3d`), and the muted sage of dried leaves (`#464f4d`). Against this grounding, the brand uses a warm, desaturated gold (`#ab8c52`) as its primary accent, a subtle nod to the sun filtering through bamboo leaves. The canvas is not a stark white but a gentle off-white (`#f2f3ef`), a surface that feels tactile and lived-in, like well-worn linen. This is a system built on restraint: `{colors.ink}` for bold headlines, `{colors.body}` (`#494742`) for comfortable reading, and `{colors.muted}` (`#3c3a36`) for secondary information that never shouts. The typography leans on the clean, geometric lines of Figtree and the approachable warmth of Inter, with Montserrat reserved for refined display moments. The signature design move is the absence of hard edges — every corner is softly rounded (`{rounded.sm}` to `{rounded.lg}`), every card feels like a pillow, and the overall mood is one of serene, sustainable luxury. The brand trusts its material story — the cool touch of bamboo, the promise of a perfect night's sleep — over aggressive marketing, letting the `{colors.hairline}` (`#e5e5e5`) and `{colors.hairline-soft}` (`#ebede5`) borders gently frame the product without distraction.

colors:
  primary: "#ab8c52"
  primary-active: "#9e812e"
  primary-disabled: "#e8d4ae"
  ink: "#212121"
  body: "#494742"
  muted: "#3c3a36"
  muted-soft: "#676986"
  hairline: "#e5e5e5"
  hairline-soft: "#ebede5"
  canvas: "#f2f3ef"
  surface-soft: "#f5f2ec"
  surface-card: "#ffffff"
  surface-strong: "#f4f4ef"
  on-primary: "#ffffff"
  on-dark: "#f2f3ef"
  accent-gold: "#a18538"
  accent-sage: "#7cb2a6"
  accent-warm: "#dbccbc"
  accent-deep: "#1f2a27"
  star-rating: "#ab8c52"
  scrim: "#1a1515"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-photo:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
  footer-section:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    size: 32px
  color-swatch-selected:
    rounded: "{rounded.full}"
    size: 32px
    outline: 2px solid "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and key conversion points. It uses the warm gold `{colors.primary}` background with white text, a soft `{rounded.sm}` corner, and `{typography.button-md}`. On hover, it shifts to `{colors.primary-active}`. In its disabled state, it fades to `{colors.primary-disabled}` with white text, signaling unavailability without visual noise.

**`button-secondary`** — A clean, understated alternative for less prominent actions like "Learn More" or "View Details". It uses a white `{colors.canvas}` background with `{colors.ink}` text, a subtle border (implied by the background), and the same `{rounded.sm}` and `{typography.button-md}` as the primary button. On hover, it may gain a light border or background shift.

**`button-tertiary-text`** — A text-only button for the most subdued actions, such as "Cancel" or "Skip". It has no background, uses `{colors.ink}` text, and relies on the `{typography.button-md}` font weight for clarity. It is the quietest option in the button hierarchy.

**`button-pill`** — A fully rounded button used for promotional badges, filter tags, or secondary CTAs in hero sections. It uses `{colors.primary}` background and `{colors.on-primary}` text, with `{rounded.full}` and `{typography.button-sm}` for a compact, friendly appearance.

### Cards
**`product-card`** — The primary product display unit, used in collection grids and related product sections. It has a white `{colors.canvas}` background, `{rounded.md}` corners, and `{typography.body-sm}` for product names and prices. The photo area is also softly rounded (`{rounded.md}`) to maintain the brand's soft aesthetic. On hover, the card may lift slightly with a subtle shadow.

**`product-card-badge`** — A small, uppercase badge overlaid on product cards to denote "New", "Best Seller", or "Eco-Friendly". It uses `{colors.accent-sage}` background with `{colors.on-dark}` text, `{rounded.xs}`, and `{typography.badge}` for a compact, informative label.

### Navigation
**`top-nav`** — The main site navigation bar, fixed at the top of the page. It has a `{colors.canvas}` background, `{colors.ink}` text, and `{typography.nav-link}` for menu items. The height is 72px, providing ample space for the logo and key links. Active links use `{colors.ink}`, while inactive links use `{colors.muted}`.

**`nav-link-active`** and **`nav-link-inactive`** — These define the state of navigation links. Active links are bold and dark (`{colors.ink}`), while inactive links are lighter (`{colors.muted}`). Both use `{typography.nav-link}` for consistent spacing and uppercase styling.

### Forms
**`search-field`** — A standard text input for search and form fields. It has a `{colors.canvas}` background, `{colors.ink}` text, `{rounded.sm}` corners, and `{typography.body-md}`. Padding is 12px 16px, and the height is 48px, making it easy to interact with on all devices.

**`search-bar-pill`** — A specialized, fully rounded search bar used in the hero or header. It has a `{colors.surface-soft}` background, `{colors.ink}` text, `{rounded.full}` corners, and `{typography.body-sm}`. It is designed to be a prominent but gentle entry point for site search.

### Footer
**`footer-section`** — The site footer, which uses a deep, dark background (`{colors.accent-deep}`) to ground the page. Text is `{colors.on-dark}` for readability, and `{typography.body-sm}` is used for general content. Links within the footer use `{typography.link}` for a clean, accessible appearance.

**`footer-link`** — A link style specifically for the footer, using `{colors.on-dark}` text and `{typography.link}`. It is designed to be legible against the dark background without being overly bright.

### Other Components
**`hero-banner`** — The main hero section on the homepage or landing pages. It uses a deep, immersive background (`{colors.accent-deep}`) with light text (`{colors.on-dark}`) and `{typography.display-xl}` for the headline. It has no rounded corners, creating a full-bleed, immersive experience.

**`hero-cta`** — The call-to-action button within the hero banner. It uses `{colors.primary}` background, `{colors.on-primary}` text, `{rounded.sm}`, and `{typography.button-md}`. It is larger than standard buttons (16px 32px padding) to draw attention.

**`accordion-header`** and **`accordion-content`** — Used for product descriptions, FAQs, and expandable sections. The header uses `{colors.canvas}` background, `{colors.ink}` text, and `{typography.title-sm}`. The content area uses `{colors.body}` text and `{typography.body-sm}`. Both have no rounded corners, maintaining a clean, linear layout.

**`rating-stars`** — Star ratings for product reviews, using `{colors.star-rating}` (the warm gold) for filled stars. The size is 16px, aligning with `{typography.body-sm}` for a cohesive look.

**`quantity-selector`** — A compact input for selecting product quantities. It has a `{colors.canvas}` background, `{colors.ink}` text, `{rounded.sm}` corners, and `{typography.body-md}`. The height is 40px, making it easy to use on mobile.

**`color-swatch`** and **`color-swatch-selected`** — Circular swatches for product color options. They are 32px in size with `{rounded.full}`. The selected state has a 2px outline in `{colors.ink}` to clearly indicate the active choice.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero banner text scales down to `{typography.display-md}`; search bar becomes full-width; footer links stack. |
| Tablet | 744–1128px | Two-column grid for product cards; top-nav remains visible but may condense; hero banner uses `{typography.display-lg}`; search bar is centered but not full-width. |
| Desktop | 1128–1440px | Full multi-column grid; top-nav shows all links; hero banner uses `{typography.display-xl}`; search bar is a pill in the header; product cards are in a 3-4 column grid. |
| Wide | > 1440px | Max-width container (1440px) centered; all elements scale proportionally; hero banner may have a wider image; product cards maintain a 4-column grid. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet accessibility standards.
- Icon buttons are 40px x 40px, providing a comfortable tap area.
- Color swatches are 32px, with a 44px tap target via padding.
- Navigation links have a minimum tap area of 44px x 44px.
- Quantity selectors are 40px tall, with 44px tap targets for increment/decrement buttons.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu on mobile (< 744px), hiding all links except the logo and cart icon.
- Product filters collapse into an accordion or slide-out panel on mobile.
- The footer's multi-column layout collapses to a single column on mobile, with accordion-style sections for links.
- Hero banners may reduce text size and hide secondary CTAs on mobile.
- Product image galleries switch from a grid to a single-image carousel on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links beyond the primary active/disabled states could not be reliably extracted; a subtle opacity or background shift is assumed.
- Error styling for form inputs (e.g., red borders, error messages) was not observed; a standard red (`#c13515`) is assumed for error text.
- Sub-brand or seasonal palettes (e.g., for "Ettitude Kids" or holiday collections) were not captured.
- Dark mode styling is not present on the live site; all tokens assume a light theme.
- Specific font weights for each typography token were inferred from common usage; exact weights may vary slightly.
- Animation and transition durations (e.g., for hover effects, accordion toggles) were not extracted; a standard 200-300ms ease-in-out is assumed.
- The exact `fontFamily` stack for `Newsreader` and `Poppins` was not observed in use; they are omitted from the primary typography tokens.
- The `oke-widget-icons` font is used for product reviews (Okendo) and is not included in the main typography stack.
- The `#0143e6` hex value (a bright blue) was extracted but not observed in the primary design; it may be used for legal links or secondary accents.
