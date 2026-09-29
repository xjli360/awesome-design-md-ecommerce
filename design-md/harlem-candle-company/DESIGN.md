---
version: alpha
name: "Harlem Candle Company"
source_url: "https://www.harlemcandlecompany.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sophisticated, narrative-driven home fragrance brand that channels the cultural and artistic energy of the Harlem Renaissance through scent. The brand’s visual identity is anchored on a deep, almost-black ink (`#121212`) that provides a dramatic, museum-quality backdrop for product photography and typography. Against this rich darkness, a vibrant cerulean blue (`#1990c6`) acts as the primary voltage, appearing in key CTAs, navigation accents, and decorative elements — a color that evokes both the jazz-age optimism and the enduring legacy of Harlem’s creative spirit. A softer, secondary blue (`#136f99`) provides depth and hover states, while a warm, light gray (`#dedede`) serves as the primary canvas for cards and surfaces, creating a gentle contrast against the dark ink. The typographic palette is distinctly editorial, drawing from a curated selection of serif and sans-serif faces: `Apple Garamond`, `Baskerville`, `Iowan Old Style`, and `Source Serif Pro` lend a classic, literary gravitas to headings and body text, while `Montserrat` and `Figtree` provide a clean, modern counterpoint for navigation and UI elements. The overall mood is one of curated elegance — generous whitespace (`{spacing.section}`) and soft rounded corners (`{rounded.sm}`) on cards and buttons prevent the dark palette from feeling austere, while the use of `{rounded.full}` pill shapes for search and badges keeps the experience approachable. The design system feels like a beautifully designed gallery or a well-crafted book, where every element — from the `{colors.hairline}` borders to the `{colors.muted}` secondary text — is intentional and evocative.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#7cb8d9"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#5a5a5a"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  accent-gold: "#c9a96e"
  accent-cream: "#f5f0e8"
  badge-new: "#1990c6"
  badge-sale: "#c13515"
  star-rating: "#c9a96e"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Apple Garamond', 'Baskerville', 'Iowan Old Style', 'Source Serif Pro', 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Apple Garamond', 'Baskerville', 'Iowan Old Style', 'Source Serif Pro', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Apple Garamond', 'Baskerville', 'Iowan Old Style', 'Source Serif Pro', 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'Iowan Old Style', 'Source Serif Pro', 'Times New Roman', 'Georgia', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Iowan Old Style', 'Source Serif Pro', 'Times New Roman', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  caption-sm:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Iowan Old Style', 'Source Serif Pro', 'Times New Roman', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Montserrat', 'Figtree', 'Arial', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-pill-primary:
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
    padding: 10px 24px
    border: 1px solid "{colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-active:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-pill-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.on-ink}"
    rounded: "{rounded.full}"
    height: 36px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and key checkout flows. Rendered in the brand's vibrant cerulean blue (`{colors.primary}`) with white text and a soft 8px corner radius (`{rounded.sm}`). On hover, it shifts to the deeper secondary blue (`{colors.primary-active}`). The disabled state uses a muted version of the primary blue (`{colors.primary-disabled}`) to maintain brand consistency while signaling inactivity. All button text is set in `Montserrat` with uppercase tracking for a refined, editorial feel.

**`button-secondary`** — A white button with dark ink text, used for less prominent actions like "Learn More" or "View Details". It shares the same dimensions and typography as the primary button but relies on a 1px `{colors.hairline}` border for definition. The active state fills the background with `{colors.surface-soft}` for a subtle pressed effect.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Clear Filters". It inherits the same typographic treatment as other buttons but remains transparent, relying on spacing and alignment for visual weight.

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for promotional badges, "Subscribe" CTAs, and quick-add actions. Its compact padding and full-radius shape make it feel more casual and approachable than the standard button.

**`button-pill-outline`** — An outlined pill button with a `{colors.hairline}` border, used for filter tags, "Clear All" actions, and secondary promotional links. It maintains the same compact sizing as the pill primary but with a lighter visual footprint.

### Cards
**`product-card`** — The core product display unit, featuring a product image with `{rounded.sm}` corners, a title set in `{typography.title-sm}` (uppercase Montserrat), and a price in `{typography.body-sm}`. The card itself has a white background and soft rounded corners, creating a clean, gallery-like presentation. On hover, a subtle shadow or border color change could indicate interactivity, though this is a known gap.

**`hero-banner`** — A full-width, full-bleed section used for hero imagery and featured collections. The background is the deep ink color (`{colors.ink}`) with white text, allowing product photography to pop. A semi-transparent overlay (`{colors.scrim}` at 40% opacity) ensures text readability over images. The banner uses generous `{spacing.section}` padding top and bottom.

### Navigation
**`nav-bar`** — The primary site navigation, fixed at 72px height with a white background. Navigation links are set in `{typography.nav-link}` — 13px Montserrat with 0.8px letter spacing and uppercase — giving the nav a clean, editorial hierarchy. On scroll, the nav compresses to 64px for a more compact reading experience. The logo or brand name sits left-aligned, with primary links centered or right-aligned.

**`search-bar-pill`** — A fully rounded search input that sits prominently in the navigation or hero area. In its default state, it appears as a subtle `{colors.surface-soft}` pill with muted placeholder text. On focus, it expands with a white background and a `{colors.primary}` border, signaling active input.

### Forms
**`text-input`** — Standard form input used for checkout fields, account creation, and contact forms. It features a white background, 1px `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}`. Error states use a red border (`{colors.badge-sale}`) for clear validation feedback.

**`newsletter-input`** — A pill-shaped input specifically for the newsletter signup in the footer. It sits alongside a `newsletter-submit` button, both using `{rounded.full}` for a cohesive, friendly appearance against the dark footer background.

**`quantity-selector`** — A compact input for adjusting product quantities on the cart or product detail page. It has a white background, `{colors.hairline}` border, and `{rounded.sm}` corners, with buttons for increment and decrement flanking the numeric value.

### Footer
**`footer`** — A full-width, dark section (`{colors.ink}`) containing navigation links, social media icons, and a newsletter signup. Text is white (`{colors.on-ink}`) with links in `{colors.muted-soft}` for a subtle, legible hierarchy. Social icons are rendered as circular buttons (`{rounded.full}`) with transparent backgrounds. The newsletter area uses the pill-shaped input and button combination for visual cohesion.

### Badges
**`badge-new`** — A small, fully rounded pill badge used to denote new products or collections. It uses the brand's primary blue (`{colors.badge-new}`) with white text, set in 10px uppercase Montserrat with tight padding.

**`badge-sale`** — A similar pill badge for sale or promotional items, using a warm red (`{colors.badge-sale}`) to draw attention. Both badges share the same typography and rounded shape for consistency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero-banner text reduces to `{typography.display-lg}`; footer links stack; search-bar-pill moves to a persistent bottom bar or hidden behind an icon |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains visible but may hide secondary links behind a "More" dropdown; hero-banner uses `{typography.display-xl}`; footer columns collapse to 2 |
| Desktop | 1128–1440px | Full three- or four-column product grid; nav-bar displays all primary links; hero-banner uses `{typography.display-xl}` with larger padding; footer displays full multi-column layout |
| Wide | > 1440px | Max-width container (1440px) centers content; increased whitespace and `{spacing.section}` padding; product cards may show additional hover details |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile and tablet.
- `button-primary` and `button-secondary` are 48px tall, exceeding the minimum.
- `search-bar-pill` is 44px tall, meeting the minimum.
- `icon-button-circle` and `social-icon` are 36px tall, which is below the 44px minimum; consider increasing to 44px on touch devices.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, with the logo remaining centered or left-aligned.
- The product grid collapses from 3-4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- The footer collapses from a 4-column layout on desktop to 2 columns on tablet and a single column on mobile.
- The hero banner reduces its padding and font size on mobile to accommodate smaller viewports.
- Secondary navigation links (e.g., "About Us", "Our Story") may be hidden behind a "More" dropdown on tablet.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., product cards, social icons, accordion headers) could not be reliably extracted from the live site. These should be defined with subtle shadow or color changes.
- Error and success states for forms (e.g., validation messages, success toasts) are not fully documented. Error text color (`{colors.badge-sale}`) is assumed.
- Dark mode is not supported; the current system relies on a white canvas and dark ink. A future dark mode would need to invert the canvas/ink relationship.
- Sub-brand or seasonal palettes (e.g., holiday collections, limited editions) are not captured. These may introduce new accent colors beyond the core blue and gold.
- The exact `fontWeight` and `lineHeight` values for serif fonts (Apple Garamond, Baskerville) are inferred from typical editorial usage; actual site values may vary.
- The `rounded` values for product cards and buttons are inferred from common patterns; the site may use slightly different radii.
- The `height` and `padding` values for components are estimated based on standard e-commerce patterns and may not match the exact site implementation.
- The `textTransform: uppercase` on button and title typography is inferred from the brand's editorial feel; the site may use mixed case in some contexts.
- The `accent-gold` and `accent-cream` colors are inferred from common luxury candle brand patterns and may not be present on the live site.
- The `star-rating` color is assumed to be gold for consistency with the accent palette.
- The `scrim` color is assumed to be the same as `ink` for overlay purposes.
