---
version: alpha
name: "Made In"
source_url: "https://madeincookware.com"
captured_at: "2026-09-28T04:10:22.228624+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  Made In is a direct-to-consumer cookware brand that speaks to the professional home cook with a palette that balances rugged utility and restrained elegance. The brand’s core identity is anchored in a deep, almost black olive green (`#20211a`) that reads as ink across most text and structural elements, while a warm off-white canvas (`#f5f6f2`) provides a soft, tactile backdrop reminiscent of raw linen or unglazed ceramic. This is not a sterile white-box kitchen; it’s a working kitchen where steam rises and knives clatter. A single, confident blue (`#0868d5`) acts as the primary voltage for CTAs and interactive accents, cutting through the earthy tones with a cold, precise clarity. Supporting this are accents of a muted gold (`#fed134`) for badges and highlights, and a restrained sage green (`#7d8b83`) used sparingly in secondary surfaces and illustrations. The typographic voice is set in Aktiv Grotesk, a clean, utilitarian sans-serif that runs from light display weights to a bold, condensed variant for headlines, giving the brand a technical, editorial feel. Corners are softly rounded (`{rounded.sm}`) on buttons and cards, avoiding the harshness of sharp geometry while maintaining a professional, no-nonsense stance. The overall mood is one of quiet confidence — the brand trusts its materials, its craftsmanship, and the user’s skill, never resorting to loud gradients or excessive ornamentation. The system feels built for longevity, like a well-seasoned carbon steel pan.

colors:
  primary: "#0868d5"
  primary-active: "#0552a8"
  primary-disabled: "#a3c5f0"
  ink: "#20211a"
  body: "#313130"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#d8d8d8"
  hairline-soft: "#e3e8e4"
  canvas: "#f5f6f2"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#fed134"
  accent-gold-active: "#e0b422"
  accent-red: "#c60000"
  accent-red-active: "#a30000"
  accent-sage: "#7d8b83"
  accent-olive: "#4d4d48"
  badge-new: "#0868d5"
  badge-sale: "#c60000"
  star-rating: "#fed134"
  scrim: "#20211a"

typography:
  display-xl:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.15px
  button-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 28px
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
    padding: 12px 28px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Shop Now" actions. It uses the brand's signature blue (`{colors.primary}`) on a white background with uppercase, weight-600 type. On hover, it shifts to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}` with full opacity, maintaining the same typography and rounded corners (`{rounded.sm}`).
**`button-secondary`** — A white button with dark ink text, used for secondary actions like "View Details" or "Learn More". It sits flush against the canvas background and uses the same uppercase button typography. An outline variant (`button-secondary-outline`) adds a 1px solid `{colors.hairline}` border for use on colored surfaces.
**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip". It inherits the same uppercase button typography and padding, with a hover state that adds a subtle `{colors.surface-soft}` background.

### Cards
**`product-card`** — The primary product display unit, used on collection pages and search results. It features a white background with a softly rounded image area (`{rounded.md}`) and a title below in `{typography.title-sm}`. The card has no border, relying on the contrast between the white card and the `{colors.canvas}` page background. A gold badge (`{colors.accent-gold}`) can be overlaid on the image for "Best Seller" or "New" indicators.
**`category-tile`** — A larger, image-backed tile used for navigating product categories (e.g., "Carbon Steel", "Knives"). It uses a soft gray background (`{colors.surface-soft}`) with centered text, and the image fills the tile with a dark scrim overlay for readability.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 72px height. It uses a white background with uppercase, weight-500 nav links. The logo sits left-aligned, and utility icons (search, account, cart) sit right-aligned. On scroll, a subtle 1px bottom border (`{colors.hairline-soft}`) appears.
**`footer-section`** — A dark footer using `{colors.ink}` as the background, with body-sm text in `{colors.canvas}` and links in `{colors.muted}`. It contains columns for "Shop", "Learn", "Support", and "Company", plus a newsletter signup form.

### Forms
**`text-input`** — Standard text input for forms (newsletter, checkout, account). It uses a white background with 12px padding and a 1px `{colors.hairline}` border. On focus, the border shifts to `{colors.primary}`. The height is 48px for comfortable touch interaction.
**`quantity-selector`** — A compact, inline control for adjusting product quantities. It features a minus button, a numeric display, and a plus button, all within a 40px tall container with `{rounded.sm}`.

### Search
**`search-bar`** — A pill-shaped search field (`{rounded.full}`) used in the nav bar and on mobile. It has a soft gray background (`{colors.surface-soft}`) with a search icon and placeholder text. On focus, it expands to full width on mobile or reveals a dropdown on desktop.

### Badges
**`product-card-badge`** — Small, uppercase badges overlaid on product images. The default is gold (`{colors.accent-gold}`) with dark text, used for "Best Seller". A blue variant (`{colors.badge-new}`) is used for "New Arrivals", and a red variant (`{colors.badge-sale}`) for "Sale".

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, search bar collapses to icon, footer stacks vertically, hero text reduces to `{typography.display-md}` |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links, search bar remains expanded, footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, search bar in nav, footer uses four-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero section uses larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Product cards have a minimum tap area of 120px x 120px for the image and title combined.
- Quantity selector buttons are at least 40px x 40px.
- Nav bar links have a minimum 48px tap area.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu, with the logo and cart icon remaining visible.
- The search bar collapses to a magnifying glass icon that expands to a full-screen overlay on tap.
- The footer collapses from four columns to a single vertical stack.
- Product grids collapse from three columns to two (tablet) and one (mobile).
- Hero sections reduce padding and font size, and may stack text below the image instead of overlaying.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover and focus states for all components (beyond primary button) could not be reliably extracted.
- Error styling for form inputs (border color, error message typography) is not documented.
- Sub-brand or collection-specific palettes (e.g., "Carbon Steel" vs "Knives") may exist but are not captured.
- Dark mode or high-contrast mode tokens are not present.
- Animation and transition timing values (e.g., button hover duration, card lift) are not extracted.
- Specific icon set and icon sizing conventions are not documented.
- Dropdown and modal component specifications are missing.
- The exact font weight for `aktiv-grotesk` variants (e.g., light, regular, medium, bold) could not be determined from extracted declarations.
