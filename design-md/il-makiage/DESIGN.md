---
version: alpha
name: "Il Makiage"
source_url: "https://www.ilmakiage.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Il Makiage is a high-performance, direct-to-consumer makeup brand that marries a sophisticated, almost clinical precision with a bold, unapologetic glamour. The brand's digital presence is a study in contrasts: a pristine, predominantly white canvas (`#ffffff`) is punctuated by a signature, vibrant hot pink (`#ff0283`) that acts as its primary voltage, appearing in key CTAs, promotional badges, and interactive highlights. This is not a soft, pastel pink; it is a confident, saturated statement. Supporting this are accents of a deep, almost-black ink (`#0d0c0c`), a clean primary blue (`#1890ff`) for informational links and secondary actions, and a warm, inviting gold (`#faad14`) for loyalty or special status indicators. The palette is further enriched by a range of sophisticated neutrals: soft greys like `#e8e8e8`, `#f5f5f5`, and `#d9d9d9` create subtle surfaces and hairlines, while `#787878` and `#727272` provide muted text tones. A hint of blush (`#e6d8d8`) and error reds (`#f5222d`, `#ffc4c2`) round out the system, ensuring every state from active to disabled is clearly communicated. The typography leans on a custom primary face, "Maison Neue", appearing in both Book and Light weights, which gives the brand a refined, editorial feel without sacrificing legibility. This is a system built for a brand that knows its product is the hero; the design is clean, confident, and deliberately restrained, allowing the vibrant product imagery and the signature pink to command attention. The overall mood is one of accessible luxury—precise, modern, and deeply feminine, but with a sharp, contemporary edge.

colors:
  primary: "#ff0283"
  primary-active: "#cc0269"
  primary-disabled: "#ffb3d9"
  ink: "#0d0c0c"
  body: "#3c3c3c"
  muted: "#787878"
  muted-soft: "#a0a0a0"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1890ff"
  accent-blue-hover: "#40a9ff"
  accent-blue-active: "#096dd9"
  accent-gold: "#faad14"
  accent-green: "#52c41a"
  error: "#f5222d"
  error-soft: "#ffe1e1"
  success: "#52c41a"
  blush: "#e6d8d8"
  star-rating: "#faad14"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue Light', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue Light', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-active:
    textColor: "{colors.primary}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
  color-swatch-selected:
    borderColor: "{colors.primary}"
  rating-stars:
    textColor: "{colors.star-rating}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature hot pink (`{colors.primary}`) with white text. Used for "Add to Bag", "Checkout", and key conversion points. On hover, it shifts to a deeper active state (`{colors.primary-active}`), and when disabled, it fades to a soft pink (`{colors.primary-disabled}`). The button is uppercase with generous letter-spacing, giving it a confident, editorial feel.
**`button-secondary`** — A clean, white button with dark text, used for less prominent actions like "View Details" or "Continue Shopping". Its active state uses a soft grey background (`{colors.surface-soft}`) to indicate press.
**`button-text`** — A minimal, text-only button that uses the primary pink for its text color. Used for inline actions like "Learn More" or "Remove".
**`button-pill-primary`** — A smaller, fully rounded pill button in the primary pink. Used for promotional badges, filter tags, or quick-add actions.
**`button-pill-outline`** — A pill button with a transparent background and dark text, used for secondary filter options or "Shop by Category" links.

### Cards
**`product-card`** — The core product display unit. A white card with a softly rounded image area (`{rounded.md}`) and a clean layout for the product title, price, and a small, hot pink badge for promotions or newness. The card itself has no background color, relying on the white canvas and subtle shadows to create separation.
**`product-card-badge`** — A small, uppercase badge pinned to the top corner of a product image. Uses the primary pink background and white text, with tight padding and a minimal rounded corner.

### Navigation
**`nav-bar`** — A fixed, 72px tall white navigation bar. Links are set in uppercase with a 0.5px letter-spacing. The active link state switches the text color to the primary pink, creating a clear visual indicator for the current section.
**`search-bar`** — A fully rounded, pill-shaped search input with a soft grey background (`{colors.surface-soft}`). It uses muted placeholder text and is designed to be unobtrusive yet always accessible.

### Forms
**`text-input`** — A standard text input with a white background, dark text, and a subtle border. On focus, the border transitions to the primary pink. An error state uses a red border (`{colors.error}`) and a soft red background (`{colors.error-soft}`) for the error message.

### Footer
**`footer`** — A dark, full-width footer with a deep ink background (`{colors.ink}`) and white text. Links are rendered in a muted grey (`{colors.muted-soft}`) to reduce visual weight, and the overall layout is clean and minimal.

### Other
**`accordion`** — Used for product details (e.g., "How to Use", "Ingredients"). Each item is a simple text block with a bottom border. The active state highlights the title in the primary pink.
**`color-swatch`** — A circular swatch for product color variants. The selected state is indicated by a pink border (`{colors.primary}`) around the swatch.
**`rating-stars`** — A gold (`{colors.star-rating}`) star rating component, used on product cards and detail pages.
**`quantity-selector`** — A compact, horizontally aligned input for adjusting product quantities. It has a soft grey background and a subtle rounded corner.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, search bar collapses to icon, hero banner stacks text above image, footer links stack vertically. |
| Tablet | 744–1128px | Two-column product grid, top nav shows key links, search bar is a compact pill, hero banner is side-by-side. |
| Desktop | 1128–1440px | Three or four-column product grid, full top nav with all links, expanded search bar, hero banner is full-width with overlay text. |
| Wide | > 1440px | Maximum content width is capped at 1440px, product grid can show up to 5 columns, hero banner uses a wider aspect ratio. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card images and color swatches are at least 48x48px for easy tapping.
- Accordion headers have a minimum height of 48px.
- The mobile hamburger menu button is 48x48px.

### Collapsing Strategy
- The top navigation collapses into a hamburger menu on mobile.
- The multi-column product grid collapses to a single column on mobile.
- The footer's multi-column link layout collapses to a single vertical stack on mobile.
- The search bar collapses to a search icon that expands into a full-width input on tap.
- The hero banner's side-by-side layout collapses to a stacked layout on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components (e.g., `button-secondary`, `text-input`) are inferred from common patterns and may not match the live site precisely.
- Specific font sizes for all typography levels (e.g., `display-xl`, `body-md`) are estimated based on common DTC brand scales and may not be pixel-perfect.
- The exact padding and height values for components like `search-bar` and `quantity-selector` are best-guess approximations.
- Error state styling for forms (e.g., error message text color, iconography) is not fully defined.
- Dark mode or high-contrast mode styling is not present.
- The specific animation and transition curves (e.g., ease-in-out, duration) are not captured.
- Sub-brand or seasonal palette variations (e.g., for "Makiage" vs. "Il Makiage Pro") are not defined.
- The exact shadow values (box-shadow) for cards and modals are not extracted.
- The `star-rating` component's empty state color is not defined.
- The `color-swatch` component's border width for the selected state is not specified.
