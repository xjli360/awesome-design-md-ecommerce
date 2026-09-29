---
version: alpha
name: "Grimm's"
source_url: "https://www.grimms.eu"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, earthy restraint governs this wooden-toy world, where #d91c01 — a single, unapologetic signal-red — cuts through a landscape of near-black charcoals (#121212, #292929) and warm, weathered grays (#c5c5c5, #ebebe4). The brand's visual system is built on contrast between dense, almost-ink backgrounds and a soft, off-white canvas (#ebebe4) that reads like raw linen or unvarnished beechwood. Rubik, a geometric sans-serif with a slight humanist warmth, runs at moderate weights — never shouting, never shrinking below a legible body size — and sits comfortably inside generously padded cards and buttons with soft, rounded corners ({rounded.md} ~12px). There are no hard edges, no glossy surfaces, no gradients: the interface mirrors the physical product — honest, tactile, and built to last. The primary CTA (#d91c01) appears sparingly, reserved for cart actions and critical confirmations, while secondary interactions live in muted grays (#6a6a6a, #a4a4a4) that recede into the background. Navigation is lean: a persistent top bar with the logo, a search icon, and a cart badge, all floating on the off-white canvas. Product cards use a clean, flat presentation — no drop shadows, no borders — relying on the natural geometry of the wooden toys and the generous whitespace ({spacing.xxl} ~48px) to create hierarchy. The checkout flow, likely powered by Shopify, introduces a cooler blue (#005bd3) that feels slightly foreign to the brand's warm palette — a known gap in the system's coherence.

colors:
  primary: "#d91c01"
  primary-active: "#b01500"
  primary-disabled: "#f5a99a"
  ink: "#121212"
  body: "#292929"
  muted: "#6a6a6a"
  muted-soft: "#a4a4a4"
  hairline: "#c5c5c5"
  hairline-soft: "#dedede"
  canvas: "#ebebe4"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#cfcfcf"
  accent-cool: "#005bd3"
  badge-new: "#d91c01"
  badge-sale: "#121212"

typography:
  display-xl:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 8px 16px
    height: 48px
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.sm}"
    borderBottom: "2px solid {colors.primary}"
  logo:
    height: 32px
    padding: "0 {spacing.sm} 0 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid transparent"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.ink}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0 0 0"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xxs} 0 0 0"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.base} 0"
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.lg} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.lg} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "4px 0"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    padding: "4px 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-small:
    color: "{colors.muted}"
    size: 16px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.base} 0"
  breadcrumb-current:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    minWidth: 40px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    minWidth: 40px
  pagination-disabled:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    minWidth: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  quantity-selector-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
    size: 16px
  checkbox:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "1px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "1px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  modal-overlay:
    backgroundColor: "rgba(18, 18, 18, 0.6)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  toast:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  toast-success:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  toast-error:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The single, high-impact call-to-action. Uses the brand's signal-red (#d91c01) on a white label. On hover, it deepens to `{colors.primary-active}` (#b01500). Disabled state fades to a soft pink (#f5a99a). Padding is generous (12px 24px) with a soft 8px corner radius — never pill-shaped, always a gentle rectangle that feels solid and intentional.

**`button-secondary`** — A quiet alternative for less critical actions. Rests on the off-white canvas with a thin hairline border. On hover, the border thickens to ink and the background shifts to `{colors.surface-soft}` (#e5e5e5). Used for "Add to Wishlist," "View Details," and secondary form submissions.

**`button-tertiary-text`** — A text-only button for the most subdued interactions. No background, no border — just the body-gray label. On hover, it shifts to the primary red, signaling a subtle activation. Used for "Cancel," "Clear Filters," and "Learn More" links.

**`button-pill-primary`** — A compact, fully rounded variant reserved for mobile filters, category tags, and quick-apply actions. Smaller typography (14px) and tighter padding (10px 20px) make it feel like a chip rather than a full button.

**`button-pill-outline`** — The outline counterpart to the pill primary. Used for inactive filter tags and "Show All" toggles. The hairline border keeps it visually light.

### Text Inputs & Forms
**`text-input`** — A clean, bordered field on the canvas background. Focus state swaps the hairline border for a solid ink border, providing a clear but understated focus indicator. Error state uses the primary red for the border, paired with red error text below the field. Height is a comfortable 48px, with 12px 16px padding for readability.

**`select-input`** — Matches the text-input dimensions and styling. The dropdown arrow is rendered as a subtle icon in `{colors.muted}`. On focus, the border becomes ink.

**`textarea`** — Same border and background as text-input but without a fixed height. Used for customer messages, product reviews, and contact forms.

**`checkbox`** — A small, squared checkbox (20px) with a 4px corner radius. Checked state fills with the primary red and displays a white checkmark. The unchecked state shows a hairline border on the canvas background.

**`radio`** — A circular radio button (20px). Checked state shows a filled primary-red center with a white dot. Unchecked state is a hairline circle on canvas.

**`toggle`** — A pill-shaped toggle switch (44px wide, 24px tall). Active state fills with primary red; the knob (20px circle) slides to the right. Inactive state shows a hairline gray fill with the knob on the left.

### Navigation
**`nav-bar`** — A fixed-height (64px) bar on the canvas background. The logo sits on the left, navigation links in the center (or right on mobile), and the search icon plus cart badge on the right. On scroll, a thin soft hairline border appears at the bottom to separate it from the page content.

**`nav-link`** — A text link with 8px 12px padding and a soft 8px hover background. The active state is indicated by a 2px primary-red underline — no bold weight change, just the underline.

**`search-bar`** — A pill-shaped input (40px tall) embedded in the nav bar. The background is `{colors.surface-soft}` (#e5e5e5) to distinguish it from the canvas. On focus, it expands slightly and the border becomes ink.

**`cart-badge`** — A small, fully rounded pill (20px height) with the item count. Uses primary red background and white text. Positioned at the top-right of the cart icon.

### Cards
**`product-card`** — A flat card on the canvas background with a soft 12px corner radius. No drop shadow, no border — the card relies on the whitespace around it and the product image's natural geometry. On hover, the background shifts to `{colors.surface-soft}` (#e5e5e5) for a subtle lift. The product image has a 1:1 aspect ratio with a 8px corner radius.

**`product-card-badge`** — An absolutely positioned badge (4px radius) in the top-left corner of the product image. Uses primary red for "New" and ink for "Sale." The typography is uppercase, 11px, with tight padding.

### Hero & Sections
**`hero-section`** — A full-width section on the canvas background with 64px vertical padding. The title uses `{typography.display-xl}` (32px, weight 500) with a generous bottom margin. The subtitle is in `{typography.body-lg}` (18px) in muted gray. A single primary CTA button anchors the bottom.

**`section-header`** — A 24px, weight-500 title in ink, with 24px bottom padding. Used to introduce product grids, category lists, and content blocks.

### Footer
**`footer`** — A dark, ink-colored footer (#121212) with white text. Links are in `{colors.muted-soft}` (#a4a4a4) and shift to white on hover. The footer uses 48px vertical padding and is divided into columns for navigation, legal, and social links.

### Feedback & States
**`loading-spinner`** — A 24px circular spinner in primary red. A smaller 16px variant in muted gray is used for inline loading states (e.g., adding to cart).

**`tooltip`** — A small, dark tooltip (ink background, white text) with a 4px corner radius. Appears on hover for icon buttons, truncated text, and product details.

**`toast`** — A dark, full-width notification bar at the top or bottom of the viewport. Success toasts use the primary red background; error toasts use the darker primary-active red. Disappears after 3–5 seconds or on tap.

**`modal-overlay`** — A semi-transparent black overlay (60% opacity) behind modal dialogs. The modal content is a white card with a 12px corner radius and 24px padding.

### Misc
**`accordion`** — A border-bottom-only container for expandable content. The header uses `{typography.title-sm}` (16px, weight 500) with a subtle chevron icon. The content area uses `{typography.body-sm}` (14px) with 12px bottom padding.

**`breadcrumb`** — A horizontal list of links in `{typography.caption}` (13px). Current page is in ink; previous pages are in muted gray. Separators are thin hairline slashes.

**`pagination`** — A row of 40px square buttons. The active page uses the primary red background; inactive pages are transparent with body-gray text. Disabled pages (e.g., "next" on the last page) are in muted-soft gray.

**`quantity-selector`** — A bordered container (40px height) with a minus button, a number display, and a plus button. The buttons are 40px squares with a soft hover background.

**`rating-stars`** — A row of 16px star icons. Filled stars are primary red; empty stars are hairline gray. Used on product cards and review sections.

**`divider`** — A 1px horizontal line in `{colors.hairline}` (#c5c5c5). A softer variant uses `{colors.hairline-soft}` (#dedede) for less visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to a hamburger menu. Product cards stack in a single column. Hero section reduces padding to 32px. Search bar moves to a full-width overlay. Footer columns stack vertically. |
| Tablet | 744–1128px | Navigation links remain visible but condensed. Product cards display in a 2-column grid. Hero section uses 48px padding. Footer columns display in a 2x2 grid. |
| Desktop | 1128–1440px | Full navigation with all links. Product cards in a 3-column grid. Hero section at full 64px padding. Footer in a 4-column layout. |
| Wide | > 1440px | Content max-width caps at 1440px, centered with auto margins. Product cards can expand to a 4-column grid. Hero section may include a larger hero image or video. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 40px and a minimum width of 40px.
- Icon buttons and cart badges are 40px x 40px to meet touch-target guidelines.
- Quantity selector buttons are 40px x 40px.
- Toggle switches are 44px wide and 24px tall, with a 20px knob.
- Checkboxes and radio buttons are 20px x 20px, with an invisible 40px touch area around them.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The logo remains centered or left-aligned.
- The search bar collapses into a full-screen overlay with a prominent input field and a cancel button.
- Product filters collapse into a bottom sheet or a slide-in drawer.
- Footer columns collapse into a single vertical stack.
- The hero section reduces its vertical padding from 64px to 32px.
- Product cards move from a 3-column grid to a single column.
- Breadcrumbs are hidden on mobile; the back button or a simplified "Home > Category" is shown instead.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only from CSS declarations found on the live site. Some hover states (e.g., for footer links, accordion headers, and pagination) are inferred from common patterns and may not match the exact brand implementation.
- **Error states**: Form error styling (text color, border color, icon placement) is based on the primary red but the exact error message typography and iconography are not confirmed.
- **Focus states**: The focus ring style (color, width, offset) is not documented. The current implementation uses an ink border on focus for text inputs, but a dedicated focus ring may exist.
- **Dark mode**: No dark mode detected on the live site. The brand's dark footer (#121212) suggests a potential dark mode, but no system-level or toggle-based dark theme is implemented.
- **Sub-brand palettes**: The extracted colors include a cool blue (#005bd3) that appears in the checkout flow (likely Shopify Pay or a payment widget). This color is not part of the brand's core palette and is noted as a gap in system coherence.
- **Animation & transition**: No transition durations, easing curves, or animation keyframes were extracted. The brand likely uses subtle transitions (e.g., 200ms ease-in-out for hover states), but these are not confirmed.
- **Typography scale**: The exact font sizes for all 15+ typography tokens are inferred from the extracted Rubik font and common e-commerce patterns. The brand may use a slightly different scale (e.g., 30px for display-xl instead of 32px).
- **Spacing scale**: The spacing tokens (xxs through section) are based on common 4px and 8px increments. The brand may use a custom scale (e.g., 6px, 14px, 20px) that was not extractable from the live site.
- **Iconography**: No icon set or icon style is documented. The brand likely uses a custom set of line icons for navigation, social media, and product features, but the exact style (stroke width, corner radius, color) is unknown.
- **Product image treatment**: The aspect ratio (1:1) and corner radius (8px) are inferred from common product-card patterns. The brand may use a different ratio (e.g., 4:5) or no corner radius on images.
- **Checkout flow**: The checkout is powered by Shopify and may introduce additional colors, typography, and components that are not part of the brand's core design system. The cool blue (#005bd3) is one such example.
- **Accessibility**: No contrast ratios, focus indicators, or screen-reader-specific styles were extracted. The brand's use of dark ink on off-white canvas likely meets WCAG AA standards, but this is not confirmed.
