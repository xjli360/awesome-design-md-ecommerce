---
version: alpha
name: "Hers"
source_url: "https://forhers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A clinical-calm women's health brand that uses a single dark gray anchor — #313131 — as its primary color, an unusual choice for a category that typically leans pink, lavender, or pastel. That gray appears on primary buttons, navigation text, and key headings, lending a serious, pharmaceutical-grade authority to a brand that sells prescription treatments for hair loss, dermatology, and sexual wellness. The typography stack is the Apple system default — -apple-system, Helvetica Neue, and sans-serif — which means Hers deliberately avoids custom type in favor of maximum legibility and zero friction on iOS devices where most of its audience browses. White canvas (#ffffff) dominates the page, with soft gray dividers and hairline borders creating clean sectional breaks. The brand's visual language is closer to a modern telehealth dashboard than a beauty retailer: high-contrast text on white, generous vertical spacing, and a complete absence of decorative flourishes. Primary CTAs use the #313131 fill with white text at {rounded.sm} radius — not pill-shaped, not oversized, just a straightforward rectangle that says "this is a medical transaction, not a shopping spree." Product cards use {rounded.md} corners and thin 1px borders, with product imagery doing all the emotional work while the UI stays out of the way. The overall effect is trustworthy, unpretentious, and distinctly un-pink — a women's health brand that presents itself as medicine first, lifestyle second.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  link: "#1565c0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
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
    border: "1px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    fontWeight: 600
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: 16px
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheader:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  legal-text:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"
    lineHeight: 1.5
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  stepper-indicator:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  stepper-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  stepper-indicator-complete:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
  modal-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.5)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 480px
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  cart-item:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  cart-item-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    fontWeight: 600
  cart-summary:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  cart-summary-row:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  cart-summary-total:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    fontWeight: 700
  notification-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  notification-banner-success:
    backgroundColor: "#e8f5e9"
    textColor: "{colors.success}"
  notification-banner-error:
    backgroundColor: "#ffebee"
    textColor: "{colors.error}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline-soft}"
  tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
  toggle-switch-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  toggle-switch-knob-active:
    transform: "translateX(20px)"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with #313131 and white text at 16px/600 weight. Used for "Start Your Visit," "Add to Cart," and "Continue" flows. On hover, the fill deepens to {colors.primary-active} (#1a1a1a). Disabled state uses {colors.primary-disabled} (#a0a0a0) with white text. Height is fixed at 48px with 14px vertical and 24px horizontal padding.

**`button-secondary`** — An outlined alternative with white background, #313131 text, and a 1px {colors.hairline} border. Used for "Learn More," "Cancel," and secondary checkout actions. Hover state adds a subtle shadow. Same 48px height as primary for alignment in form layouts.

**`button-tertiary-text`** — A text-only button with no background or border, using {colors.primary} text at 16px/600 weight. Used for "Skip," "View Details," and inline navigation within multi-step flows. Hover state adds underline.

**`button-pill`** — A smaller, fully rounded variant at 40px height with 10px vertical and 20px horizontal padding. Used for filter tags, category pills, and compact CTAs in mobile navigation. Uses {typography.button-sm} at 14px/600 weight.

### Cards
**`product-card`** — The primary product display container, a white card with 1px {colors.hairline-soft} border and {rounded.md} corners. Contains a product image (200px height, {rounded.sm} top corners), title in {typography.title-sm}, and price in 16px/600 weight. Hover state adds a subtle box-shadow and darker border. Internal padding is 16px.

**`product-card-badge`** — A small uppercase label pinned to product cards, using {colors.surface-soft} background and {colors.muted} text at 11px/600 weight. Used for "NEW," "BEST SELLER," or "RX REQUIRED" indicators. {rounded.xs} corners with 2px vertical and 8px horizontal padding.

### Navigation
**`nav-bar`** — A fixed-height 64px bar with white background, 1px bottom border in {colors.hairline-soft}, and navigation links in {typography.nav-link} at 14px/500 weight. Active links use {colors.primary} text; inactive links use {colors.muted}. The bar contains the brand logo on the left, primary nav links in the center, and utility icons (cart, account) on the right.

**`nav-link-active`** — Active navigation state with {colors.primary} text and 600 font weight. Underline indicator on hover or active page.

**`nav-link-inactive`** — Default navigation state with {colors.muted} text and 500 font weight. Hover transitions to {colors.primary}.

### Forms
**`text-input`** — Standard text input field at 48px height with white background, 1px {colors.hairline} border, {rounded.sm} corners, and 12px vertical / 16px horizontal padding. Uses {typography.body-md} at 16px. Focus state switches to a 2px {colors.primary} border. Error state uses a 1px {colors.error} border.

**`select-dropdown`** — Matches text-input styling for visual consistency. Same height, padding, border, and corner radius. Used for treatment selection, dosage, and frequency fields in the consultation flow.

**`checkbox`** — A 20px square with {rounded.xs} corners, white background, and 1px {colors.hairline} border. Checked state fills with {colors.primary} and displays a white checkmark icon.

**`radio`** — A 20px circle with {rounded.full} corners, white background, and 1px {colors.hairline} border. Checked state shows a 6px {colors.primary} inner circle.

**`toggle-switch`** — A 44px wide by 24px tall pill-shaped switch with {colors.hairline} background. Active state fills with {colors.primary}. The 20px white knob animates 20px to the right on activation.

### Hero
**`hero-section`** — The full-width top section with white background and 64px vertical padding. Contains a heading in {typography.display-xl} at 32px/700 weight, a subheading in {typography.body-md} at 16px with {colors.muted} text, and a primary CTA button. Content is centered or left-aligned depending on layout variant.

**`hero-cta`** — The hero's primary button, identical to `button-primary` but with 32px horizontal padding for visual prominence. Used for "Start Your Free Visit" or "Get Started" actions.

### Footer
**`footer`** — A full-width footer with {colors.surface-soft} background, 48px vertical padding, and a 1px top border in {colors.hairline-soft}. Contains link columns in {typography.link} at 14px/500 weight with {colors.muted} text, a legal text section in {typography.caption-sm} at 12px with {colors.muted-soft} text, and social/trust badges.

**`footer-link`** — Footer navigation links in {colors.muted} text at 14px/500 weight. Hover state transitions to {colors.primary}.

### Modals
**`modal-overlay`** — A semi-transparent black overlay at 50% opacity covering the full viewport. Centers the modal content vertically and horizontally.

**`modal-content`** — A white container at max-width 480px with {rounded.md} corners and 32px padding. Contains a close button in the top-right corner (32px circle, transparent background, {colors.muted} icon). Used for treatment details, consultation summaries, and confirmation dialogs.

### Progress & Steps
**`progress-bar`** — A 4px tall pill-shaped bar with {colors.hairline-soft} background. The fill portion uses {colors.primary} at the same 4px height and {rounded.full} corners. Used in multi-step consultation flows.

**`stepper-indicator`** — A 32px circle showing step numbers, with {colors.hairline-soft} background and {colors.muted} text. Active steps use {colors.primary} background with white text. Completed steps also use {colors.primary} with a checkmark icon.

### Tags & Badges
**`tag`** — A small pill-shaped label at 12px with {colors.surface-soft} background and {colors.muted} text. Used for category filters, treatment types, and informational labels. Active state fills with {colors.primary} and white text.

**`tag-active`** — The selected state of a tag, using {colors.primary} background and {colors.on-primary} text.

### Notifications
**`notification-banner`** — A full-width banner at the top of content sections with {colors.surface-soft} background, {colors.body} text, and 8px vertical / 16px horizontal padding. Success variant uses a green background (#e8f5e9) with {colors.success} text. Error variant uses a red background (#ffebee) with {colors.error} text.

**`notification-banner-success`** — Success state with green tint and {colors.success} (#2e7d32) text.

**`notification-banner-error`** — Error state with red tint and {colors.error} (#d32f2f) text.

### Tabs
**`tab-bar`** — A horizontal tab container with white background and 1px bottom border in {colors.hairline-soft}. Tabs are evenly spaced.

**`tab-active`** — Active tab with {colors.primary} text, 2px bottom border in {colors.primary}, and 8px vertical / 16px horizontal padding. Uses {typography.button-sm} at 14px/600 weight.

**`tab-inactive`** — Inactive tab with {colors.muted} text and same padding as active. Hover transitions to {colors.primary}.

### Cart & Checkout
**`cart-item`** — A cart line item with white background, 16px padding, and a 1px bottom border in {colors.hairline-soft}. Contains product image, title in {typography.title-sm}, price in 16px/600 weight, and a quantity selector.

**`cart-summary`** — A summary panel with {colors.surface-soft} background, {rounded.sm} corners, and 16px padding. Displays subtotal, shipping, and total rows. The total row uses {typography.title-sm} at 16px/700 weight.

**`quantity-selector`** — A compact 44px height control with 1px {colors.hairline} border and {rounded.sm} corners. Contains a minus button, the current quantity, and a plus button, each 44px wide. Buttons use {colors.primary} text on transparent background.

### Loaders
**`loading-spinner`** — A 24px circular spinner in {colors.primary}. Used for async actions like form submission and page transitions.

**`skeleton-loader`** — A placeholder rectangle at 16px height with {colors.hairline-soft} background and {rounded.xs} corners. Used for content loading states. Multiple skeleton loaders stack to represent card or list layouts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack full-width; hero padding reduces to 32px vertical; buttons go full-width; text-input height reduces to 44px; footer columns stack; modal-content uses full width minus 16px margins |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with "More" dropdown; hero uses 48px vertical padding; side-by-side form layouts; footer shows 2-column link grid |
| Desktop | 1128–1440px | Full nav-bar with all links visible; three-column product grid; hero uses 64px vertical padding; multi-column form layouts; footer shows 4-column link grid; max-width container at 1128px |
| Wide | > 1440px | Same as desktop with content max-width at 1128px; background canvas extends full width; additional whitespace on sides; nav-bar remains centered |

### Touch Targets
- All interactive elements (buttons, links, inputs, toggles) maintain minimum 44px height on mobile
- Icon buttons and stepper indicators are minimum 32px with 44px touch area via padding
- Checkbox and radio targets are 20px with 44px invisible touch area via padding
- Quantity selector buttons are 44px x 44px
- Tab touch targets are minimum 44px tall
- Toggle switch is 44px wide with 24px height

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px; the hamburger icon is 44px x 44px
- Product grid collapses from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Footer link columns collapse from 4 columns to 2 columns to stacked single column
- Hero section reduces vertical padding from 64px to 32px on mobile
- Form layouts shift from side-by-side to stacked on mobile
- Accordion sections remain collapsed by default on all breakpoints, expanding on tap
- Cart summary moves from sidebar to below cart items on mobile
- Modal content uses full viewport width minus 16px margins on mobile
- Tab bars may scroll horizontally on mobile if tabs exceed viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site; the full color palette (secondary accents, hover states, error/success colors, link colors) has been inferred from common healthcare e-commerce patterns and may not match the actual brand implementation
- No custom font family was detected; the site uses the Apple system font stack. If Hers has a custom typeface (e.g., for logo or display headings), it was not extracted
- No meta theme-color was found; mobile browser chrome color is unknown
- The site showed a "Just a moment..." page title, suggesting Cloudflare or similar protection was active during extraction; the actual page title and meta tags may differ
- Hover states for buttons, cards, and links are inferred from common patterns; actual hover transitions (duration, easing, shadow values) are unknown
- Error state styling for forms (error message typography, icon placement, animation) is inferred
- Focus ring styles (color, width, offset) for accessibility were not extracted
- Dark mode or high-contrast mode variants, if they exist, were not detected
- Sub-brand or treatment-specific color variations (e.g., for hair, skin, sexual wellness categories) are unknown
- Animation durations, easing curves, and micro-interaction details were not extracted
- Icon set style (line weight, fill vs outline, size system) is unknown
- The extracted color list was extremely sparse (single hex); this may indicate the extraction tool was blocked or the site uses CSS-in-JS or dynamic theming that wasn't captured
- Shopify-specific checkout widget colors (Klarna, Afterpay, etc.) were not detected but may be present on cart pages
- Print stylesheet and email-specific styling are unknown
