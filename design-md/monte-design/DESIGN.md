---
version: alpha
name: "Monte Design"
source_url: "https://montedesign.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Monte Design crafts modern luxurious furniture for nursery and home, where a serene, sophisticated palette of soft greys and muted tones creates a calm, nurturing atmosphere. The brand's identity is built on a foundation of understated elegance, using a primary blue accent (#1990c6) that acts as a gentle focal point against a canvas of warm whites and light greys (#dedede, #747474). This isn't a loud or trendy aesthetic; it's a considered, timeless approach where the quality of materials and the purity of form take center stage. The typography, set in the refined Chap typeface, reinforces this quiet confidence with its clean, slightly geometric lines, appearing in both light weights for airy body text and bolder weights for impactful headlines. Signature design moves include the use of soft, pill-shaped buttons (`{rounded.full}`) and generously rounded corners on product cards (`{rounded.lg}`), which echo the gentle curves of the furniture itself. The deep, almost-black ink (#121212) provides necessary contrast without harshness, while the muted greys (#333333, #747474) create a layered, tactile experience that feels both premium and approachable. The overall mood is one of curated calm — a space where every element, from the `{colors.surface-card}` white of a crib to the `{colors.hairline}` grey of a drawer pull, is chosen to foster a sense of peace and security, perfectly suited for the modern nursery or any room seeking a touch of luxurious serenity.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#b0d4e8"
  ink: "#121212"
  body: "#333333"
  muted: "#747474"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-warm-grey: "#dedede"

typography:
  display-xl:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Chap', Georgia, 'Times New Roman', serif"
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary-active}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button with a solid blue background (`{colors.primary}`) and white text. On hover or active, it transitions to a deeper blue (`{colors.primary-active}`). The disabled state uses a muted blue-grey (`{colors.primary-disabled}`) to indicate non-interactivity.

**`button-secondary`** — An outlined button with a transparent background, dark ink text, and a 2px solid border. It provides a less emphatic but equally important action, often used for "Learn More" or "View Details" links. The active state fills the background with a soft grey (`{colors.surface-soft}`).

**`button-tertiary`** — A text-only button styled as a link, using the primary blue for its text. It's used for supplementary actions like "Cancel" or "Read More". On hover, it gains a subtle soft grey background.

### Navigation
**`nav-bar`** — A clean, white header bar (`{colors.canvas}`) that spans the full width of the viewport. It contains the brand logo, navigation links, and utility icons. The height is fixed at 72px, and the typography for links is set in uppercase Chap with a 0.3px letter-spacing.

**`nav-link-active`** — The active state for a navigation link, indicated by a 2px bottom border in the primary blue. This provides a clear, understated visual cue for the current page or section.

### Cards
**`product-card`** — A product display card with a white background and soft, generous rounding (`{rounded.lg}`). The card itself has no padding, allowing the product image to bleed to the edges. Title and price typography are applied to the text overlay within the card.

**`product-card-title`** — The product name, set in `{typography.title-sm}` with a dark ink color for strong readability.
**`product-card-price`** — The product price, set in `{typography.body-md}` with a muted grey color to keep the focus on the product name and image.

### Forms
**`text-input`** — A standard text input field with a white background, subtle border (`{colors.hairline}`), and soft corners (`{rounded.sm}`). On focus, the border thickens to 2px and turns primary blue. An error state uses a 2px border in the darker active blue.

**`search-bar`** — A full-height, pill-shaped search input used in the site header or on search pages. It features a white background, a 1px hairline border, and placeholder text in the body font. On focus, the border becomes a 2px primary blue line.

### Footer
**`footer`** — A full-width footer with a deep, near-black background (`{colors.ink}`) and white text. Links within the footer are styled in a lighter muted grey (`{colors.muted-soft}`) and transition to white on hover, creating a clean, readable hierarchy.

### Badges
**`badge-new`** — A small, pill-shaped badge with a primary blue background, used to highlight new arrivals. The text is set in uppercase, bold Chap.
**`badge-sale`** — A similar badge using the darker active blue, reserved for sale or promotional items.

### Icon Buttons
**`icon-button`** — A circular, transparent button used for utility icons (e.g., search, cart, account). It has a muted grey icon color and expands to a 40px diameter. On hover, it gains a soft grey background and darkens the icon to the ink color.

### Quantity Selector
**`quantity-selector`** — A pill-shaped control for adjusting product quantities, featuring a white background, a hairline border, and centered typography. It contains minus, number, and plus elements.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding; footer links stack. |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar remains visible but may condense; hero section uses medium padding. |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; standard hero padding. |
| Wide | > 1440px | Max-width container (1440px) centered; product grid may expand to four columns; increased whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Icon buttons are at least 40x40px.
- Quantity selector controls are at least 44x44px.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile.
- The footer link columns collapse into a single vertical stack on mobile.
- Hero section text and images may stack vertically on smaller screens.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are not fully documented (e.g., subtle shadow or scale effects on product cards).
- Error and success states for forms (e.g., input validation messages, success banners) are not extracted.
- Dark mode or high-contrast mode color overrides are not defined.
- Specific animation durations and easing curves (e.g., button hover transitions, card entrance animations) are unknown.
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) are not captured.
- The exact font weight and size for the brand logo in the nav-bar is not specified.
- Spacing values for specific component internals (e.g., padding within product card text areas) are inferred from common patterns.
- The `textTransform: uppercase` on button and nav-link typography is an assumption based on common DTC furniture brand patterns, not a direct extraction.
