---
version: alpha
name: "Stonemaier Games"
source_url: "https://stonemaiergames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A board-game publisher whose visual system is built around a deep, confident blue (#003388) that reads as both premium and approachable — the same blue that anchors the header, the footer, and the primary call-to-action buttons, with a secondary voltage of #cf4e28 (a warm, slightly desaturated orange) used for sale badges, price highlights, and accent elements that signal urgency without aggression. The site runs on a light gray canvas (#eeeeee) rather than pure white, giving it a softer, more tactile feel that distinguishes it from the stark-white ecommerce norm, while product cards float on white (#ffffff) with subtle shadows to create depth. Typography leans on PT Sans and PT Serif — a serif/sans-serif pairing that nods to the brand's literary, narrative-driven game design (each game has a story) while keeping body text clean and readable at 16px. The orange #cf4e28 appears in the "Add to Cart" button and sale badges, creating a consistent accent language that says "this is actionable" without the shrillness of pure red. Navigation is a fixed top bar with the brand's logo left-aligned and a compact utility row (search, cart, account) on the right, all on the deep blue field (#003388) with white text — a high-contrast, authoritative header that gives way to a light, airy content area. The overall mood is that of a well-curated game library: organized, colorful but controlled, with enough white space to let the game box art (which varies wildly in palette) be the hero of each product page.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099bb"
  ink: "#222222"
  body: "#444444"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#d1d1d1"
  hairline-soft: "#e5e5e5"
  canvas: "#eeeeee"
  surface-soft: "#f2f4f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#cf4e28"
  accent-orange-active: "#b03d1e"
  accent-blue-light: "#579af6"
  accent-green: "#468847"
  accent-green-soft: "#00d084"
  accent-blue-bright: "#4199fd"
  accent-blue-medium: "#4386e2"
  accent-blue-pale: "#2ea3f2"
  accent-blue-deep: "#0693e3"
  accent-gray-dark: "#3f4b5b"
  accent-gray-mid: "#546360"
  accent-gray-light: "#bfc3c8"
  accent-gray-pale: "#dedfe0"
  accent-gray-soft: "#e1e1e1"
  accent-gray-lighter: "#e8e8e8"
  accent-gray-lightest: "#eaeaea"
  accent-gray-ultra-light: "#ecf0f5"
  accent-gray-near-white: "#efefef"
  accent-gray-warm: "#b2b2b3"
  accent-gray-cool: "#b3b3b1"
  accent-dark: "#313131"
  accent-darker: "#32373c"
  accent-error: "#b94a48"

typography:
  display-xl:
    fontFamily: "'PT Serif', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'PT Serif', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'PT Serif', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'PT Serif', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  body-lg:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'PT Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
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
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-logo:
    height: 40px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.accent-orange}"
  nav-utility-icon:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px 0px 16px 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "8px 16px 4px 16px"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0px 16px"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    margin: "8px 16px 0 16px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
  footer-link-hover:
    textColor: "{colors.accent-blue-light}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-preorder:
    backgroundColor: "{colors.accent-blue-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sold-out:
    backgroundColor: "{colors.accent-gray-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-hover:
    textColor: "{colors.accent-blue-light}"
  cart-count-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and main form submissions. Rendered on the deep blue (#003388) background with white text and 8px rounded corners. On hover, shifts to `button-primary-active` (#002266). Disabled state uses `button-primary-disabled` (#8099bb) to indicate non-interactivity. **`button-accent`** — The orange variant (#cf4e28) used for sale items, limited-time offers, and high-urgency actions. Same shape and sizing as primary but with a warm, energetic color that draws the eye. **`button-secondary`** — An outlined variant with a white background, blue text, and a 2px blue border. Used for "Learn More", "View Details", and secondary actions alongside primary buttons. On hover, fills solid blue. **`button-ghost`** — A text-only button with no background or border, used for "Cancel", "Back", and tertiary actions. On hover, gains a light gray background. **`button-pill`** and **`button-pill-accent`** — Fully rounded pill buttons used for filters, tags, and compact actions in navigation or card overlays.

### Cards
**`product-card`** — The core content unit for displaying games in grid layouts. A white card with 12px rounded corners, containing a product image (top-rounded), title, price, optional badge, and an "Add to Cart" button. Cards sit on the light gray canvas (#eeeeee) with subtle shadow separation. The badge overlays the top-left of the image area. **`product-card-badge`** — Small uppercase labels (e.g., "SALE", "NEW", "PRE-ORDER", "SOLD OUT") with 4px rounded corners, color-coded by type: orange for sale, green for new, bright blue for pre-order, dark gray for sold out.

### Navigation
**`nav-bar`** — A fixed 60px header on the deep blue (#003388) background. The brand logo sits left-aligned, followed by main navigation links in uppercase PT Sans bold. Utility icons (search, cart, account) are right-aligned as circular icon buttons. **`nav-link`** — Uppercase 15px bold text with 8px horizontal padding. Active state has a 3px orange (#cf4e28) bottom border. **`nav-utility-icon`** — Circular 36px icon buttons for search, cart, and account. Cart shows a `cart-count-badge` — a small orange pill with the item count.

### Forms
**`text-input`** — Standard text input with white background, 1px hairline border, 8px rounded corners, and 44px height. On focus, the border thickens to 2px blue. Error state uses a 2px red (#b94a48) border. **`select-input`** — Dropdown select styled identically to text inputs. **`textarea`** — Multi-line text area with the same base styling. **`search-bar`** — A fully rounded (pill-shaped) search input with a 44px height, used in the header and on search pages. On focus, the border becomes 2px blue. The `search-icon` is a circular blue button with a magnifying glass icon.

### Footer
**`footer`** — A full-width deep blue (#003388) footer with white text. Contains columns of links, social icons, and legal text. **`footer-link`** — White text links that turn light blue (#579af6) on hover. **`footer-heading`** — Bold 14px uppercase headings for link columns. **`social-icon`** — Circular 32px white icon buttons for social media links, turning light blue on hover.

### Hero
**`hero-banner`** — A full-width banner section used on the homepage and campaign pages. Deep blue background with white text, generous padding (64px vertical). **`hero-banner-accent`** — An orange variant for special promotions and announcements.

### Dividers
**`divider`** — A 1px horizontal line in the standard hairline color (#d1d1d1). **`divider-soft`** — A lighter 1px line (#e5e5e5) for subtler separation within cards or sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner reduces padding; search bar moves to expandable toggle; footer stacks vertically; product card badges scale down |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero banner maintains moderate padding; footer shows 2-column link layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; standard hero padding; footer shows 4-column link layout |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) with centered content; nav and footer remain at full width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav utility icons (search, cart, account) are 36px circular targets
- Product card "Add to Cart" buttons are 44px tall with 16px horizontal padding
- Search bar is 44px tall with 20px horizontal padding
- Footer links have 8px vertical padding for comfortable tapping

### Collapsing Strategy
- On mobile (< 744px), the main navigation collapses into a hamburger menu with a slide-out drawer
- The search bar collapses into an icon toggle that expands to a full-width input on tap
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse from 4 columns (desktop) to 2 (tablet) to a single vertical stack (mobile)
- Hero banner padding reduces from 64px (desktop) to 32px (mobile)
- Product card badges may hide or reduce font size on very small screens

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns rather than extracted from the live site — the extracted CSS did not include pseudo-class styles
- Error state styling for forms (red border, error message placement) is based on standard ecommerce patterns, not site-specific extraction
- The exact font sizes and line heights for typography are estimated from the extracted font families and common web usage — the live site may use different values
- Dark mode is not supported on the live site and is not defined in this system
- Sub-brand or campaign-specific color palettes (e.g., for individual game launches) were not extracted and may exist
- The extracted color list contains many similar grays and blues, making it difficult to determine exact usage for each — the palette above represents the most likely assignments based on frequency and context
- Animation and transition durations, easing functions, and micro-interaction details were not extractable
- The exact border radius for product cards (12px) is an estimate based on common Shopify themes — the live value may differ by 2-4px
- Checkout-specific styling (Shopify Pay button, cart drawer, payment form) was not extracted and may follow Shopify defaults rather than brand tokens
