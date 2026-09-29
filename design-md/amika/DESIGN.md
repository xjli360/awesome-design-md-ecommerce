---
version: alpha
name: "Amika"
source_url: "https://loveamika.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Amika is a professional haircare brand that feels like a playful, confident friend who also happens to be a brilliant chemist. The brand lives in a warm, off-white world anchored by `{colors.canvas}` (#fefaf0), a creamy parchment tone that softens everything it touches. This is not a sterile white lab — it's a boudoir, a backstage, a vanity lit by golden hour. The primary voltage comes from `{colors.primary}` (#d74f64), a dusty rose-red that appears on every CTA, badge, and accent, supported by a deeper `{colors.primary-active}` (#a8263a) for hover states. Amika's palette is deliberately expansive and eclectic: electric `{colors.accent-hot-pink}` (#ff29b8) and `{colors.accent-orange}` (#ff580a) sit alongside deep plums like `{colors.accent-plum}` (#3c2c53) and `{colors.accent-deep-plum}` (#322546), while cool `{colors.accent-blue}` (#2e88d5) and `{colors.accent-lavender}` (#a49cfb) provide contrast. The typography system leans on two distinct faces: Breno, a sophisticated serif likely used for display and editorial moments, and Futura ND Book/Medium, a geometric sans-serif that brings mid-century modern clarity to body text and navigation. Rounded corners are generous but not cartoonish — `{rounded.sm}` (8px) on buttons, `{rounded.md}` (12px) on cards — and the `{rounded.full}` pill shape is reserved for search bars and badges. The overall effect is a brand that feels simultaneously luxurious and irreverent, like a high-end salon that plays punk music.

colors:
  primary: "#d74f64"
  primary-active: "#a8263a"
  primary-disabled: "#f0a0ae"
  ink: "#3c2c53"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9ca3af"
  hairline: "#e0e3e5"
  hairline-soft: "#f6f1e2"
  canvas: "#fefaf0"
  surface-soft: "#f6f1e2"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-hot-pink: "#ff29b8"
  accent-orange: "#ff580a"
  accent-blue: "#2e88d5"
  accent-lavender: "#a49cfb"
  accent-plum: "#3c2c53"
  accent-deep-plum: "#322546"
  accent-rose: "#da5d70"
  accent-dark-rose: "#d33c53"
  accent-cyan: "#8cdbf1"
  star-rating: "#d74f64"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Breno', 'Futura ND Medium', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Breno', 'Futura ND Medium', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Futura ND Book', 'Futura ND Medium', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Futura ND Book', 'Futura ND Medium', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Futura ND Book', 'Futura ND Medium', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Futura ND Book', 'Futura ND Medium', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Futura ND Medium', 'Futura ND Book', Helvetica, Arial, sans-serif"
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
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-orange}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-hot-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-best-seller:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for add-to-cart, checkout, and key conversions. It uses a solid `{colors.primary}` (#d74f64) fill with white text, set in uppercase Futura ND Medium with 1px letter-spacing. On hover, it shifts to `{colors.primary-active}` (#a8263a). The disabled state uses `{colors.primary-disabled}` (#f0a0ae). All primary buttons have `{rounded.sm}` (8px) corners and a 44px height for comfortable touch targets.

**`button-secondary`** — An outlined alternative used for less prominent actions like "Learn More" or "View All". It features a `{colors.canvas}` (#fefaf0) background with a 2px `{colors.ink}` (#3c2c53) border and matching ink text. Hover state inverts the colors with an ink background and white text. Same 44px height and uppercase typography as primary.

**`button-tertiary-text`** — A text-only button used for inline actions like "Cancel" or "Clear". It uses transparent background with `{colors.primary}` text. On hover, it gains a subtle `{colors.surface-soft}` background. No rounded corners or padding — it sits inline with content.

**`button-pill-primary`** — A smaller, pill-shaped button used for filters, tags, and quick-select options. Uses `{colors.primary}` fill with `{rounded.full}` corners and a compact 36px height. The typography is `{typography.button-sm}` (12px uppercase). Active state uses `{colors.primary-active}`.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for unselected filter options. It has a transparent background with a 1px `{colors.hairline}` (#e0e3e5) border and `{colors.ink}` text. Selected state transitions to `{colors.primary}` border and text.

### Cards
**`product-card`** — The primary product display component on collection pages and search results. It features a white (`{colors.surface-card}`) background with `{rounded.md}` (12px) corners and `{spacing.base}` (16px) padding. The product image sits at the top with `{rounded.sm}` (8px) corners. The title uses `{typography.title-sm}` in `{colors.ink}`, while the price is set in `{typography.body-md}` in `{colors.primary}`. On hover, the card gains a subtle shadow and a 1px `{colors.hairline}` border.

**`hero-section`** — The full-width hero banner on the homepage and key landing pages. It uses a `{colors.surface-soft}` (#f6f1e2) background with `{typography.display-xl}` for the headline. The section has `{spacing.section}` (64px) vertical padding. The CTA button is a larger version of `button-primary` with 48px height and 32px horizontal padding.

### Navigation
**`nav-bar`** — The sticky top navigation bar, 72px tall with a `{colors.canvas}` background. It contains the brand logo, navigation links, and utility icons (search, account, cart). Links use `{typography.nav-link}` (14px uppercase Futura ND Medium). The active link is underlined with a 2px `{colors.primary}` border. On scroll, the nav bar gains a 1px `{colors.hairline}` bottom border.

### Forms
**`text-input`** — Standard text input for forms, search, and checkout. It has a `{colors.canvas}` background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. The focused state switches to a 2px `{colors.primary}` border. Error state uses a 2px `{colors.accent-orange}` (#ff580a) border. Height is 48px with 12px/16px padding.

**`search-bar`** — The prominent search bar, typically found in the nav or on search pages. It uses `{rounded.full}` pill shape with a 1px `{colors.hairline}` border. On focus, it gains a 2px `{colors.primary}` border. The placeholder text is `{colors.muted}` (#777777). Height is 48px with generous padding.

**`quantity-selector`** — A compact input for adjusting product quantities on the PDP and cart. It has a `{colors.canvas}` background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. The height is 40px with minimal padding. It contains a minus button, the quantity value, and a plus button, all in `{colors.ink}`.

### Badges
**`badge-new`** — A small, pill-shaped badge indicating new arrivals. Uses `{colors.accent-hot-pink}` (#ff29b8) background with white text. Typography is `{typography.badge}` (11px uppercase with 0.5px letter-spacing). Padding is 2px vertically and 8px horizontally.

**`badge-sale`** — Indicates sale or promotional pricing. Uses `{colors.accent-orange}` (#ff580a) background. Same typography and dimensions as `badge-new`.

**`badge-best-seller`** — Highlights top-selling products. Uses `{colors.accent-plum}` (#3c2c53) background. Same typography and dimensions as other badges.

### Footer
**`footer-section`** — The site footer, using a dark `{colors.ink}` (#3c2c53) background with white text. It contains link columns, social icons, and legal text. Links use `{typography.link}` in `{colors.muted-soft}` (#9ca3af) and hover to `{colors.primary}`. The section has `{spacing.section}` vertical padding.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details. It has a `{colors.surface-soft}` background with `{typography.title-sm}` in `{colors.ink}`. Padding is `{spacing.md}` vertically and `{spacing.base}` horizontally. Corners are `{rounded.sm}`. On click, it expands to reveal `accordion-content`.

**`accordion-content`** — The expandable content area below the header. Uses `{colors.canvas}` background with `{typography.body-md}` in `{colors.body}`. Padding is `{spacing.base}` all around.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `display-md`; search bar moves to full-width below nav; footer links stack in single column; quantity selector becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links with "More" dropdown; hero uses `display-lg`; sidebar filters become horizontal scroll; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; three-column product grid; hero uses `display-xl`; persistent sidebar filters; footer uses 4-column layout; search bar in nav |
| Wide | > 1440px | Max-width container at 1440px; expanded whitespace; four-column product grid; hero may include video background; additional navigation tiers visible |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile
- Icon buttons are 40px x 40px minimum
- Badges and pill buttons are 36px minimum height
- Nav links have 48px touch area (padding + height)
- Quantity selector buttons are 40px x 40px
- Accordion headers are 48px minimum height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a horizontal scroll strip on mobile, with a "Filters" button opening a modal
- Footer link columns collapse to a single column on mobile, with accordion-style expandable sections
- Product image galleries collapse from thumbnail strip to single-image swipe on mobile
- Multi-column text layouts collapse to single column below 744px
- Hero sections reduce font size and may hide secondary text on mobile
- Search bar moves from inline nav position to full-width below the nav on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for many components (secondary button, text links, product cards) could not be reliably extracted from the static site analysis
- Focus ring styles and keyboard navigation patterns are not documented — assume a 2px `{colors.primary}` outline offset by 2px until verified
- Error state styling for forms beyond the border color (e.g., error message typography, icon placement) is not captured
- Dark mode is not supported by the current brand implementation — all colors assume a light theme
- Sub-brand or collection-specific color palettes (e.g., "The Good Stuff" or "Kure") may exist but are not included in this global system
- Animation and transition timing values (e.g., button hover duration, card lift speed) are not documented — assume 150-200ms ease-in-out
- Dropdown and mega-menu patterns for navigation are not fully captured
- Loading states (skeleton screens, spinners) are not defined
- The exact font weights for Breno (likely 400, 600, 700) and Futura ND (Book vs Medium) need verification from the actual font files
- Letter-spacing values for display typography are estimated based on common brand patterns and should be verified against live screenshots
- The `textTransform: uppercase` on nav-link and button typography is inferred from the brand's aesthetic and should be confirmed
- Checkout-specific component styles (e.g., cart summary, payment form) are not included
- Accessibility contrast ratios for text on various backgrounds (especially accent colors) need formal verification
