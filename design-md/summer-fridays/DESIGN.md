---
version: alpha
name: "Summer Fridays"
source_url: "https://summerfridays.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Summer Fridays is a skincare brand that feels like a cool, calm exhale — a clean white canvas (#f4f4f6) punctuated by soft, muted neutrals (#e5e5eb, #dbdde4) and the occasional pop of unexpected color. The brand's voice is one of gentle efficacy, not aggressive transformation; it's the skincare equivalent of a lazy afternoon. The palette is anchored by a slate of sophisticated blues and grays (#676986, #2c3e50, #272d45) that lend a sense of quiet luxury, while accents like a vibrant teal (#0e7a82), a warm coral (#fd6210), and a playful yellow (#ffcf2a) inject moments of energy, often reserved for limited-edition packaging or special ingredients. Typography relies on the geometric, slightly retro Expressa, set in a range of weights that feel editorial yet approachable. The design system is defined by its generous use of soft, pill-shaped buttons (`{rounded.full}`) and cards with gentle rounding (`{rounded.lg}`), creating a tactile, human-friendly interface. There are no sharp corners or harsh contrasts; even primary actions, rendered in the deep blue-gray `{colors.primary}`, feel inviting rather than demanding. The overall mood is one of curated calm — a digital space that mirrors the brand's promise of skin that looks healthy, rested, and effortlessly radiant.

colors:
  primary: "#676986"
  primary-active: "#2c3e50"
  primary-disabled: "#d3d4dd"
  ink: "#272d45"
  body: "#2c3e50"
  muted: "#9a9db1"
  muted-soft: "#dbdde4"
  hairline: "#e5e5eb"
  hairline-soft: "#f4f4f6"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#0e7a82"
  accent-coral: "#fd6210"
  accent-yellow: "#ffcf2a"
  accent-mint: "#b2f9e9"
  accent-pink: "#ea3333"
  accent-sky: "#acd5e9"
  accent-navy: "#000418"

typography:
  display-xl:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Expressa', futura-pt, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
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
    border: "1px solid {colors.accent-pink}"
  text-input-placeholder:
    textColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
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
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    position: "absolute"
    top: "8px"
    left: "8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-image:
    rounded: "{rounded.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-best-seller:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    height: 48px
    padding: "0 {spacing.base}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  rating-stars:
    color: "{colors.accent-yellow}"
    size: 16px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full pill shape in the brand's signature muted blue-gray (`{colors.primary}`). The uppercase, letter-spaced label sits on a white background (`{colors.on-primary}`). On hover, the background deepens to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}`, a soft gray that visually lowers contrast without disappearing entirely.

**`button-secondary`** — A ghost-style button with a white background (`{colors.canvas}`) and a thin `{colors.hairline}` border. The text remains in `{colors.ink}`. On hover, the background shifts to `{colors.surface-soft}`. This button is used for less prominent actions, like "Learn More" or "Add to Wishlist."

**`button-tertiary-text`** — A text-only button with no background or border. It uses `{colors.ink}` by default and transitions to `{colors.primary}` on hover. Used for inline actions like "View Details" or "Cancel."

**`button-accent-teal`** and **`button-accent-coral`** — Variant buttons that use the brand's accent colors (`{colors.accent-teal}` and `{colors.accent-coral}`) as backgrounds. These are reserved for promotional or limited-edition contexts, such as a "Shop the Drop" CTA or a "New Arrival" highlight.

### Cards
**`product-card`** — The primary container for product listings. A white card (`{colors.surface-card}`) with soft, generous rounding (`{rounded.lg}`). The card has no internal padding at the root level; instead, its child elements (image, title, price) are stacked with their own spacing. The product image is clipped to the top corners of the card. A `product-card-badge` can be positioned absolutely over the image, using `{colors.accent-teal}` for "Best Seller" or `{colors.accent-yellow}` for "New."

### Navigation
**`nav-bar`** — A fixed or sticky top bar, 72px tall, with a white background and a subtle bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — a compact, uppercase, letter-spaced style. The active link is underlined with a 2px `{colors.primary}` border. On scroll, the nav bar gains a light box-shadow for depth.

### Forms
**`text-input`** — A standard input field with a white background, `{rounded.sm}` corners, and a `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`. Error states are indicated by a `{colors.accent-pink}` border. Placeholder text uses `{colors.muted}`.

**`select-input`** — Styled identically to `text-input` but with a custom dropdown arrow. The same focus and error state patterns apply.

### Footer
**`footer`** — A full-width section with a `{colors.surface-soft}` background. Links are set in `{colors.muted}` and transition to `{colors.ink}` on hover. The footer uses generous vertical padding (`{spacing.section}`) and is organized into columns for navigation, social links, and legal text.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-best-seller`** — Small, pill-shaped tags that overlay product cards or hero images. Each uses a distinct accent color: yellow for newness, coral for sale, teal for best-seller. The text is uppercase and tightly tracked (`{typography.badge}`).

### Hero
**`hero-section`** — A full-width promotional area with a `{colors.surface-soft}` background. It pairs a large headline (`{typography.display-lg}`) with a softly rounded hero image (`{rounded.lg}`). The section uses `{spacing.section}` for vertical padding, creating a spacious, editorial feel.

### Accordion
**`accordion`** — A vertically stacked list of expandable sections, commonly used for product details or FAQs. Each item has a `{colors.hairline-soft}` bottom border. The header uses `{typography.title-sm}`, and the content area uses `{typography.body-sm}` with `{spacing.sm}` padding.

### Quantity Selector
**`quantity-selector`** — A pill-shaped control for adjusting product quantities in the cart. It has a `{colors.hairline}` border and contains two icon buttons (minus/plus) flanking a central numeric value. The buttons are `{rounded.full}` and use `{colors.muted}` for their icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; search bar moves to a dedicated overlay. |
| Tablet | 744–1128px | Two-column product grid; nav bar shows key links but collapses secondary items under a "More" dropdown; hero section uses `{spacing.xxl}` padding. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar visible; hero section at full `{spacing.section}` padding; search bar is always visible in the nav. |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero section remains centered with generous whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 48px and a minimum width of 48px on touch devices.
- Icon buttons are 40x40px, with a 48x48px touch area via transparent padding.
- Product card badges are at least 24px tall for easy tapping.

### Collapsing Strategy
- The top navigation collapses into a hamburger menu on mobile (< 744px). The hamburger icon is a 48x48px touch target.
- The footer's multi-column layout collapses to a single column on mobile, with accordion-style sections for each category.
- Product filters (if present) collapse into a slide-out drawer on mobile and tablet.
- The search bar collapses into a full-screen overlay on mobile, triggered by a search icon in the nav bar.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., `text-input`, `select-input`, `product-card`) were not fully extractable from the live site and have been inferred from common patterns.
- Error and success styling for forms (e.g., error messages, success banners) is not reliably documented.
- The exact font weight and size for `display-xl` and `display-lg` are estimates based on typical editorial headings; the live site may use different values.
- Dark mode is not supported by the current design system.
- The `accent-pink` (#ea3333) and `accent-navy` (#000418) colors were observed but their specific use cases (e.g., error states, special promotions) are inferred.
- The `oke-widget-icons` font family was found in the CSS but its usage (likely for reviews/ratings) is not documented here.
- Sub-brand or collection-specific palettes (e.g., for limited-edition drops) are not captured.
