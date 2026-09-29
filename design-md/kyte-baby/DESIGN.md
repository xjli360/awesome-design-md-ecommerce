---
version: alpha
name: "Kyte Baby"
source_url: "https://kytebaby.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A baby brand built on a muted, earthy palette where #e3ded2 — a warm, dusty beige — serves as the foundational canvas, wrapping the site in a soft, tactile atmosphere that feels more like a nursery than a storefront. The signature bamboo sleep bag, a flagship product, is echoed in the brand's visual language: gentle curves, generous whitespace, and a restrained use of color that prioritizes comfort over stimulation. The primary accent, #2e9e7b, a deep, calming sage green, appears on key CTAs and interactive elements, providing a quiet but confident anchor against the neutral backdrop. Typography leans on Lexend, a modern, geometric sans-serif with a friendly, open character, set at moderate weights (400-600) to maintain readability and a sense of calm. Product imagery is given prominence, often isolated on white or the #fbf6f3 blush-toned background, allowing the texture of the bamboo fabric to be the hero. The overall effect is one of serene, considered simplicity — a digital space that feels safe, clean, and inherently soft, avoiding the bright, primary-colored chaos of many competitors in the category.

colors:
  primary: "#2e9e7b"
  primary-active: "#2a8468"
  primary-disabled: "#8f917d"
  ink: "#1a1a1a"
  body: "#222222"
  muted: "#676986"
  muted-soft: "#858585"
  hairline: "#e5e5e4"
  hairline-soft: "#f2f2f2"
  canvas: "#e3ded2"
  surface-soft: "#fbf6f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#475e66"
  accent-stone: "#777968"
  accent-warm: "#ff8717"
  accent-error: "#de2a2a"
  accent-success: "#55d7ae"
  ink-soft: "#737373"

typography:
  display-xl:
    fontFamily: "'Lexend', 'Lexend Deca', 'Libre Baskerville', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Lexend', 'Lexend Deca', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.accent-error}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.ink}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and key conversion points. Rendered in the brand's sage green (`{colors.primary}`) with white text and an uppercase, weight-600 label. On hover, it shifts to a darker `{colors.primary-active}`. Disabled state uses a muted olive (`{colors.primary-disabled}`) to signal inactivity without visual noise.

**`button-secondary`** — An outlined alternative for less prominent actions like "View Details" or "Learn More". Uses a white background with a thin `{colors.hairline}` border. On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. The uppercase label matches the primary button's typography for consistency.

**`button-ghost`** — A text-only button for inline actions within cards or modals. No background or border, relying solely on the `{typography.button-md}` uppercase style. Used for "Cancel", "Clear", or "See All" links.

**`button-pill-primary`** — A smaller, fully rounded variant of the primary button, used for filter tags, quick-add actions, or promotional badges. The pill shape (`{rounded.full}`) and compact padding make it feel like a friendly, clickable tag.

### Cards
**`product-card`** — The core product display unit. A white card with a 1:1 aspect ratio image area (`{rounded.md}`) and text details below. The image area is the hero, with the product name, price, and a color-swatch row beneath. A sale price uses `{colors.accent-error}`. A warm-orange `{product-card-badge}` can be overlaid on the image for "New" or "Best Seller" flags.

**`hero-banner`** — A full-width section for seasonal campaigns or new collections. Uses a soft blush background (`{colors.surface-soft}`) with a large headline (`{typography.display-xl}`) and a single, prominent `{hero-banner-cta}` button. The layout is centered with generous padding, creating a calm, editorial feel.

### Navigation
**`nav-bar`** — A sticky top bar at 72px height, using the warm beige canvas (`{colors.canvas}`) as its background. The logo sits left, with category links in uppercase `{typography.nav-link}` centered or right-aligned. On scroll, the background switches to white (`{colors.surface-card}`) with a subtle shadow for depth.

**`search-bar`** — A pill-shaped input field (`{rounded.full}`) with a magnifying glass icon. It sits prominently in the nav or on the hero banner. The white background and thin border keep it clean, while the full rounding softens the interaction point.

### Forms
**`text-input`** — Standard form input for checkout, account creation, and newsletter signups. A white field with a light gray border. On focus, the border turns sage green (`{colors.primary}`). Error states use a red border (`{colors.accent-error}`). Padding and font size are generous for readability and touch targets.

**`select-input`** — A dropdown variant of the text input, used for size, quantity, or country selection. Shares the same visual structure, with a custom arrow icon.

**`quantity-selector`** — A compact, bordered control for adjusting item quantities. Two square buttons flank a central numeric display. The buttons use a muted text color, and the whole unit is a `{rounded.sm}` rectangle.

### Footer
**`footer-section`** — A full-width footer on the beige canvas, organized into columns of links. The `{footer-link}` typography is a medium-weight, muted gray that darkens on hover. An accordion pattern (`{accordion-trigger}` and `{accordion-content}`) is used on mobile to collapse link groups.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav-bar collapses to hamburger menu. Product cards stack in a 2-column grid. Footer links collapse into accordions. Hero banner text scales down to `{typography.display-md}`. |
| Tablet | 744–1128px | Two-column product grid. Nav-bar shows limited category links. Footer displays in a 2-column grid. Hero banner remains full-width with centered text. |
| Desktop | 1128–1440px | Three-column product grid. Full nav-bar with all category links. Footer in a 4-column layout. Hero banner uses `{typography.display-xl}`. |
| Wide | > 1440px | Max-width container (1440px) centered on screen. Product grid expands to 4 columns. All other layouts remain consistent with desktop. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px.
- Icon buttons and swatches are at least 32px x 32px.
- Accordion triggers have a minimum tap area of 48px.
- Nav-bar links have a minimum tap area of 44px.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a full-screen overlay.
- The footer's multi-column link groups collapse into vertically stacked accordion panels.
- Product filters (size, color, price) collapse into a single "Filter" button that opens a bottom sheet.
- The secondary navigation (help, account, search) collapses into a single icon bar.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., `text-input`, `select-input`, `product-card`) were not fully extractable from the live site CSS. The states defined above are best-guess based on common patterns.
- Error styling for forms (validation messages, error icons) is not documented. The `text-input-error` border color is inferred from the presence of `#de2a2a` in the extracted palette.
- Dark mode is not supported and no dark-mode tokens are defined.
- Sub-brand or promotional palettes (e.g., for holiday collections) are not captured.
- The specific font weights and sizes for `display-xl` and `display-md` are inferred from common usage in the baby/lifestyle space, as the extracted font stack did not include specific size or weight data.
- The `color-swatch` component's selected state border is a standard pattern, but the exact implementation (e.g., checkmark icon) is unknown.
- The `product-card-badge` position (top-left, top-right) and exact padding are not confirmed.
- The `nav-bar-scrolled` boxShadow value is a standard approximation.
- The `button-secondary` border thickness on hover is assumed to be 1px, but could be 2px.
