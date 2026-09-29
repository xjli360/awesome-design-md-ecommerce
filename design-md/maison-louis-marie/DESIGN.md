---
version: alpha
name: "Maison Louis Marie"
source_url: "https://maisonlouismarie.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Maison Louis Marie is a luxury clean fragrance house that speaks in whispers rather than shouts, using a restrained palette of deep charcoals and warm neutrals to let the product — and the story behind each scent — command attention. The brand's visual language is anchored on a near-black ink (`#191919`) and a soft, almost-white canvas (`#fafafa`), with accents of a vivid, slightly orange-leaning red (`#d72c0d`) that appears sparingly on primary actions and select product details, lending a subtle warmth against the otherwise cool, monochromatic backdrop. Secondary reds (`#e8144b`, `#ea0202`) and a muted slate (`#b1b7c3`) add depth to badges and dividers, while the occasional whisper of pale mint (`#e6f7f4`) or blush (`#fff4fa`) surfaces in promotional banners, suggesting a brand unafraid of quiet color when the story calls for it. Typography relies on a single, clean sans-serif family (likely a refined geometric or neo-grotesk) set in modest weights — body copy at 14–16px in regular (`{typography.body-md}`), headlines at 24–32px in medium (`{typography.display-md}`), and buttons in a compact 14px medium (`{typography.button-md}`) — creating a calm, editorial rhythm that prioritizes readability over typographic spectacle. Corners are gently softened: cards and inputs use a 4px radius (`{rounded.xs}`), while CTAs and badges round to 8px (`{rounded.sm}`), a subtle cue that this is a tactile, considered brand rather than a purely digital one. The overall effect is one of understated luxury — a clean, almost monastic white space punctuated by rich, dark typography and the occasional red accent, mirroring the brand's philosophy of clean ingredients and timeless, unisex fragrances.

colors:
  primary: "#d72c0d"
  primary-active: "#b32505"
  primary-disabled: "#f5c4b8"
  ink: "#191919"
  body: "#262626"
  muted: "#5e5e5e"
  muted-soft: "#9b9b9b"
  hairline: "#d3d3d3"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f4f4f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e8144b"
  accent-red-dark: "#ea0202"
  accent-mint: "#e6f7f4"
  accent-mint-strong: "#13a165"
  accent-blush: "#fff4fa"
  accent-slate: "#b1b7c3"
  accent-slate-dark: "#999ea8"
  badge-sale: "#d72c0d"
  badge-new: "#13a165"
  star-rating: "#191919"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  body-md:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Maison Neue', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    size: 20px
  radio:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 20px
  radio-checked:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    size: 20px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    size: 20px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    borderBottom: "2px solid {colors.ink}"
  nav-link-hover:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
  product-card-add-to-cart:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  product-card-add-to-cart-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.15
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-out-of-stock:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    height: 24px
    width: 24px
  quantity-selector-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 24px
    width: 24px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link-hover:
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 20px
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  star-rating:
    textColor: "{colors.star-rating}"
    size: 16px
  star-rating-empty:
    textColor: "{colors.hairline}"
    size: 16px
  swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.ink}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  size-selector-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.ink}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
  pagination-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
  pagination-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
  pagination-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 360px
  drawer-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  drawer-footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"
  notification-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 4px
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
  skeleton-animation:
    backgroundColor: "{colors.surface-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's signature red (`{colors.primary}`) on a white background. Uppercase 14px medium type (`{typography.button-md}`) sits centered within a 48px tall, softly rounded (`{rounded.sm}`) rectangle. On hover, the background deepens to `{colors.primary-active}`. The disabled state uses a pale, desaturated red (`{colors.primary-disabled}`) to signal inactivity while maintaining brand consistency.
**`button-secondary`** — A ghost-style button with a white background (`{colors.canvas}`), dark text (`{colors.ink}`), and a thin hairline border (`{colors.hairline}`). On hover, the background shifts to `{colors.surface-soft}` and the border strengthens to `{colors.ink}`, creating a subtle but clear interactive cue. Same 48px height and uppercase typography as the primary variant.
**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.ink}` for default state and `{colors.primary}` on hover/active. Used for secondary actions like "View All" or "Cancel" where visual weight should be minimal.

### Cards
**`product-card`** — A clean, minimal card with a white background (`{colors.canvas}`), a 1:1 aspect ratio product image with `{rounded.xs}`, and a simple layout of title (`{typography.title-md}` in `{colors.ink}`), price (`{typography.body-sm}` in `{colors.body}`), and an "Add to Cart" button (`{colors.ink}` background, `{colors.on-primary}` text) that shifts to `{colors.primary}` on hover. No border or shadow — the card relies on generous whitespace and the product photography to create visual separation.
**`hero-banner`** — A full-width, 480px tall section with a `{colors.surface-soft}` background, a dark scrim overlay (`{colors.scrim}` at 15% opacity) over the background image, and a single primary CTA button (`{colors.primary}`) using `{typography.display-xl}` for the headline. The banner is intentionally restrained — no secondary text, no decorative elements — letting the hero image and the brand's typographic voice carry the message.

### Navigation
**`nav-bar`** — A fixed-position, 72px tall white bar (`{colors.canvas}`) with uppercase 13px medium nav links (`{typography.nav-link}`) in `{colors.muted}`. The active link is underlined with a 2px `{colors.ink}` border. On scroll, the bar shrinks to 64px and gains a stronger bottom border (`{colors.hairline}`). The search bar is a pill-shaped input (`{rounded.full}`) with a `{colors.surface-soft}` background, expanding to a white background with an ink border on focus.
**`footer`** — A dark, full-width footer using `{colors.ink}` as the background and `{colors.canvas}` for text. Links use `{colors.muted-soft}` and shift to white on hover. The newsletter signup combines a standard text input (`{colors.canvas}` background, `{rounded.xs}`) with a primary-colored submit button (`{colors.primary}`), maintaining the brand's clean, editorial feel even in conversion-focused areas.

### Forms
**`text-input`** — A 48px tall input with a white background (`{colors.canvas}`), `{colors.ink}` text, and a `{colors.hairline}` border. On focus, the border switches to `{colors.ink}`. Error state uses `{colors.primary}` for the border. Placeholder text is set in `{colors.muted-soft}`. The overall simplicity — no icons, no floating labels — keeps the focus on the content.
**`checkbox`** and **`radio`** — Small, 20px interactive elements with a white background and `{colors.hairline}` border. When selected, the background fills with `{colors.ink}` (checkbox) or the border switches to `{colors.ink}` with a filled center (radio). The `{rounded.xs}` on checkboxes and `{rounded.full}` on radios follows standard UI patterns while staying true to the brand's clean aesthetic.
**`toggle`** — A 44px wide, 24px tall pill (`{rounded.full}`) with a `{colors.hairline}` background and a white 20px knob. When active, the background shifts to `{colors.ink}`, creating a high-contrast, binary state indicator.

### Badges & Indicators
**`badge`** — Small, 11px uppercase labels (`{typography.badge}`) with `{rounded.sm}` and 4px 8px padding. The default badge uses `{colors.surface-soft}` background with `{colors.muted}` text. Sale badges use `{colors.badge-sale}` (the brand red) with white text. New badges use `{colors.badge-new}` (a clean green, `#13a165`). Out-of-stock badges use the default muted style. Badges are intentionally compact — they inform without competing with the product.
**`star-rating`** — A simple row of 16px stars in `{colors.star-rating}` (ink) for filled stars and `{colors.hairline}` for empty ones. No numeric rating, no decorative flourishes — just a clear, binary visual of customer satisfaction.
**`notification-badge`** — An 18px tall, fully rounded pill (`{rounded.full}`) using `{colors.primary}` background and white text. Used on cart icons and other notification triggers. The small size and vibrant red ensure it's noticed without overwhelming the interface.

### Layout & Structure
**`accordion-header`** — A full-width, transparent clickable area with `{typography.title-md}` in `{colors.ink}` and a 16px vertical padding. A `{colors.hairline-soft}` bottom border separates each accordion item. The content area uses `{typography.body-sm}` in `{colors.body}` with 16px bottom padding. The accordion is a key pattern for product descriptions, ingredient lists, and FAQ sections.
**`divider`** — A 1px horizontal line using `{colors.hairline-soft}` for subtle separation and `{colors.hairline}` for stronger visual breaks. Used throughout the site to organize content without adding visual noise.
**`modal-overlay`** — A full-screen scrim at 50% opacity (`{colors.scrim}`), creating a focused, distraction-free environment for the modal content. The modal itself uses `{colors.canvas}` background with `{rounded.sm}`, 32px padding, and a close button in the top-right corner.
**`drawer`** — A 360px wide slide-in panel from the right side of the screen, typically used for the shopping cart or mobile navigation. The header and footer use `{colors.canvas}` with `{colors.ink}` text, separated by `{colors.hairline-soft}` borders. The main content area scrolls independently.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero banner height reduces to 320px; footer links stack; search bar moves to a full-width drawer; product images remain 1:1 but cards use full width; accordions expand by default for key sections |
| Tablet | 744–1128px | Two-column product grid; nav bar shows condensed links (icons + abbreviated labels); hero banner at 400px; footer uses 2-column layout; search bar remains in nav but collapses to icon on scroll; product cards show 2 per row |
| Desktop | 1128–1440px | Full nav bar with all links visible; three-column product grid; hero banner at 480px; footer uses 4-column layout; search bar fully expanded; product cards show 3–4 per row depending on collection |
| Wide | > 1440px | Max-width container (1440px) for content; nav bar remains full width with background color extending to edges; product grid can show 4 columns; hero banner content is centered within the max-width container; extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height to meet WCAG touch target guidelines.
- Icon buttons are 40px × 40px with a `{rounded.full}` hit area, ensuring comfortable tapping on mobile.
- Product card "Add to Cart" buttons are 40px tall, placed at the bottom of the card for easy thumb access.
- Nav bar links have 8px 12px padding, with the full 72px bar height serving as the effective touch target.
- Quantity selector buttons are 24px × 24px within a 40px tall container, providing clear tap targets for increment/decrement actions.

### Collapsing Strategy
- **Primary Navigation**: On mobile (< 744px), the full nav bar collapses into a hamburger menu that opens a full-height drawer from the left. The drawer uses the same `{colors.canvas}` background and `{typography.nav-link}` styling, with accordion-style sub-menus for collections.
- **Search**: On mobile, the search bar collapses to a search icon in the nav. Tapping it opens a full-width search drawer with an auto-focused input. On tablet, the search bar shows as an icon that expands on tap.
- **Product Grid**: The grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile). Product cards maintain their aspect ratio and padding across all breakpoints.
- **Footer**: The 4-column desktop footer collapses to 2 columns on tablet and a single column on mobile, with accordion-style toggles for each section to save vertical space.
- **Hero Banner**: The banner height reduces from 480px (desktop) to 400px (tablet) to 320px (mobile). Text size scales down proportionally, and the CTA button remains full-width on mobile for easier tapping.
- **Cart Drawer**: On mobile, the cart drawer expands to full screen width, using the entire viewport for a more immersive shopping experience.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While primary and secondary button hover states are defined, hover states for many other components (product card links, footer links, accordion headers) are inferred from general brand behavior and may not match the exact live implementation.
- **Error styling**: Form error states (error messages, input border colors, iconography) are partially defined but the exact error message typography, icon set, and animation behavior could not be extracted.
- **Focus states**: Keyboard focus styles (outline colors, widths, offsets) are not reliably extractable from the live site and should be implemented following WCAG 2.1 AA guidelines with a 2px `{colors.primary}` outline.
- **Dark mode**: No dark mode implementation was detected. The brand's heavy use of `{colors.ink}` backgrounds in the footer suggests a potential dark mode could use inverted colors, but no specific tokens exist.
- **Sub-brand palettes**: Maison Louis Marie may have seasonal or collection-specific color palettes (e.g., holiday, limited editions) that are not captured in the core system.
- **Animation & transitions**: Timing functions, durations, and easing curves for hover effects, page transitions, and drawer animations are not defined. The brand likely uses subtle transitions (0.2s–0.3s ease-in-out) consistent with its understated aesthetic.
- **Loading states**: Skeleton loading patterns are defined but the exact shimmer animation, timing, and component-specific skeletons (e.g., product card skeleton, hero skeleton) are not fully specified.
- **Typography scale**: Font sizes and weights are inferred from common patterns in the fragrance/luxury space and the extracted hex colors. The exact font family name ("Maison Neue") is a best-guess based on the brand's identity; the actual font may differ.
- **Iconography**: The brand likely uses a custom icon set for nav, social media, and UI elements, but specific icon styles (stroke width, size, color) are not captured.
- **Spacing scale**: While the spacing scale follows a standard 4px/8px progression, specific component padding and margin values are inferred from common e-commerce patterns and may not match the live site exactly.
- **Color contrast**: Some combinations (e.g., `{colors.muted-soft}` on `{colors.canvas}`) may need adjustment to meet WCAG AA contrast ratios, especially for body text. The brand's aesthetic leans toward low contrast, which may require careful implementation for accessibility.
