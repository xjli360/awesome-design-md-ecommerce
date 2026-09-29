---
version: alpha
name: "Lalo"
source_url: "https://meetlalo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Lalo is a modern baby and toddler brand that balances playful optimism with a grounded, trustworthy aesthetic. The brand’s visual language is anchored by a deep, confident navy (`#0f234c`) and a vibrant primary blue (`#3057a7`) that together signal reliability and warmth — a far cry from the pastel pinks and baby blues of conventional nursery brands. A signature accent of electric lime (`#d4fb41`) and a sunny yellow (`#fffb00`) inject moments of joy and energy, while a rich forest green (`#376b52`) and deep teal (`#01392c`, `#004f49`) ground the palette in nature and sustainability. The brand uses a clean white canvas (`#ffffff`) with soft surfaces (`#f6f6f6`, `#ecf3ff`) and warm, peachy tones (`#faeadf`) for a gentle, approachable feel. Typography relies on Inter and Nunito Sans, giving a clean, readable, and slightly friendly character — neither too corporate nor too whimsical. Corners are soft but not pill-like: buttons use `{rounded.sm}` (8px) and cards use `{rounded.md}` (12px), while badges and accent elements can go to `{rounded.full}` for a playful touch. The overall mood is one of considered, modern parenthood — products that parents are proud to own, not just functional necessities.

colors:
  primary: "#3057a7"
  primary-active: "#0f234c"
  primary-disabled: "#828282"
  ink: "#141414"
  body: "#333333"
  muted: "#545454"
  muted-soft: "#828282"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#d4fb41"
  accent-yellow: "#fffb00"
  accent-orange: "#fd5b29"
  accent-green: "#376b52"
  accent-teal-dark: "#01392c"
  accent-teal: "#004f49"
  accent-blue-light: "#1990c6"
  accent-blue-dark: "#136f99"
  surface-blue-soft: "#ecf3ff"
  surface-green-soft: "#e4eddd"
  surface-warm: "#faeadf"
  ink-dark: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  link:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-blue-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
    padding: 10px 22px
    height: 48px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 11px 15px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-orange}"
    padding: 11px 15px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    box-shadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    box-shadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    box-shadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.surface-blue-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  hero-cta-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "12px 30px"
    height: 52px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: "11px 19px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-lime}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base}"
  testimonial-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-grid-item:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-grid-icon:
    backgroundColor: "{colors.surface-blue-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 48px
    width: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for key actions like "Add to Cart" and "Shop Now". On hover, it shifts to `{colors.primary-active}` for a deeper, more confident state. The disabled state uses `{colors.primary-disabled}` to visually communicate inactivity while maintaining brand consistency.

**`button-secondary`** — An outlined variant for secondary actions, featuring a 2px solid border in `{colors.primary}` on a white background. On hover/active, the background fills with `{colors.surface-blue-soft}` and the border deepens to `{colors.primary-active}`, providing a subtle but clear interactive cue.

**`button-accent-lime`** and **`button-accent-yellow`** — High-energy accent buttons used sparingly for promotional or celebratory CTAs, such as limited-time offers or loyalty sign-ups. The lime (`{colors.accent-lime}`) and yellow (`{colors.accent-yellow}`) backgrounds paired with dark ink text create a bold, playful contrast against the otherwise restrained palette.

**`button-ghost`** — A text-only button with no background or border, used for less prominent actions like "Learn More" or "Cancel". The text color matches `{colors.primary}` and the button respects the same typography and padding as other buttons for alignment consistency.

### Cards
**`product-card`** — The standard product display card, with a white background, soft shadow, and `{rounded.md}` corners. The image area uses a 1:1 aspect ratio with rounded top corners. On hover, the shadow deepens to create a subtle lift effect. The card includes a title (`{typography.title-sm}`), price (`{typography.body-md}`), and an optional badge overlay.

**`testimonial-card`** — A warm, peach-toned card (`{colors.surface-warm}`) used for customer reviews and social proof. The soft background color and `{rounded.md}` corners create a friendly, trustworthy container for quote-style content.

**`feature-grid-item`** — A neutral, soft-background card (`{colors.surface-soft}`) used in feature grids and benefit sections. Each item includes an icon in a circular blue-tinted container (`{colors.surface-blue-soft}`) and descriptive body text.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a white background and subtle bottom border. At rest, it stands 72px tall; on scroll, it shrinks to 64px and gains a light box-shadow for depth. Active nav links are underlined with a 2px `{colors.primary}` border, while inactive links use `{colors.muted}`.

**`nav-link-active`** and **`nav-link-inactive`** — Define the two states for top-level navigation items. Active links use `{colors.primary}` with an underline, while inactive links use `{colors.muted}`. Both use `{typography.nav-link}` for consistent sizing and weight.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px hairline border, and `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}`. Error states use a 2px `{colors.accent-orange}` border to clearly signal validation issues.

**`select-input`** — Dropdown selectors styled consistently with text inputs, using the same border, padding, and corner radius. The chevron icon uses `{colors.muted}` by default.

**`quantity-selector`** — A compact input for adjusting product quantities, with a 1px hairline border and `{rounded.sm}` corners. Used on product detail pages and cart.

### Footer
**`footer-section`** — A full-width footer with a deep navy background (`{colors.primary-active}`) and white text. Links are white by default and shift to `{colors.accent-lime}` on hover, creating a bright, accessible contrast against the dark background.

### Badges
**`badge-new`** — A yellow pill-shaped badge (`{colors.accent-yellow}`) used to flag new arrivals. The dark ink text ensures readability against the bright background.

**`badge-sale`** — An orange pill-shaped badge (`{colors.accent-orange}`) for sale or clearance items. White text provides strong contrast.

**`badge-eco`** — A green pill-shaped badge (`{colors.accent-green}`) for eco-friendly or sustainable products. White text on the deep green background communicates environmental consciousness.

**`product-card-badge`** — A lime pill-shaped badge (`{colors.accent-lime}`) overlaid on product card images for promotional flags like "Best Seller" or "Bundle & Save".

### Hero
**`hero-section`** — The primary hero banner area, using a soft blue background (`{colors.surface-blue-soft}`) with large display typography. The hero includes two CTAs: a primary filled button (`{hero-cta}`) and a secondary outlined button (`{hero-cta-secondary}`), both slightly taller (52px) than standard buttons for visual prominence.

### Accordion
**`accordion-header`** and **`accordion-content`** — Used for FAQ sections and product details. Headers use `{typography.title-sm}` with a bottom border, while content sections use `{typography.body-md}` with generous padding for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; buttons go full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grids; nav remains visible but condensed; hero uses `{typography.display-lg}`; side-by-side feature grids |
| Desktop | 1128–1440px | Three-column product grids; full nav with all links visible; hero at full `{typography.display-xl}`; multi-column footer |
| Wide | > 1440px | Max-width container at 1440px; centered content; product grids can expand to four columns; hero remains centered with generous whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40x40px with `{rounded.full}` for easy tapping
- Nav links have 48px tap targets (padding + height)
- Quantity selector and search bar maintain 48px height on mobile
- Accordion headers have 48px minimum tap targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grids collapse from 3-4 columns on desktop to 2 columns on tablet, then 1 column on mobile
- Hero section stacks vertically on mobile, with CTA buttons stacking below the headline
- Footer links collapse from multi-column layout to a single stacked column
- Feature grids shift from 3-column to 2-column to single-column as viewport shrinks
- Search bar remains visible on all breakpoints but may reduce in width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all interactive elements (only primary button and product card hover were reliably extracted)
- Error styling for forms beyond the orange border (no error message typography or iconography captured)
- Focus ring styles and keyboard navigation indicators
- Dark mode or high-contrast mode variants
- Sub-brand or collection-specific palette variations (e.g., seasonal or collaboration colors)
- Animation and transition timing values (ease, duration)
- Dropdown and modal component styles
- Loading states and skeleton screen patterns
- Tooltip and popover component specifications
- Star rating component styling and sizing
- Mobile navigation drawer animation and overlay styles
- Checkbox and radio button component styles
- Toggle switch component specifications
- Table and data display component styles
- Pagination component styling
- Breadcrumb component specifications
- Progress indicator styles (loading bars, spinners)
- Video player and media component styles
- Cookie consent banner styling
- Newsletter signup form specific styling
- Social media icon specifications and colors
- Print stylesheet specifications
- Reduced motion preferences handling
