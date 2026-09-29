---
version: alpha
name: "Molten"
source_url: "https://www.moltenusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated blue (#003399) anchors the entire brand — not as a quiet background but as an active, confident primary that appears on every product page, navigation element, and primary CTA. This is not the generic blue of a thousand startups; it is a specific, almost electric ultramarine that carries the weight of precision sports equipment. A secondary purple (#221155) adds a layer of depth and sophistication, appearing in footer backgrounds, secondary badges, and hover states, creating a two-tone system that feels both athletic and premium. The brand trusts its color to do the heavy lifting: white canvas (#ffffff) provides clean breathing room, while the deep blue and purple create a visual tension that suggests performance and durability. There are no gradients, no decorative flourishes — every design decision serves clarity and hierarchy. The typography system is built on a single sans-serif stack, with display sizes at 32px and 24px using a weight of 700 for maximum impact, while body text at 16px and 14px stays at 400 for readability. Buttons are generously padded at 16px 32px with a subtle 8px radius, making them feel substantial and trustworthy. The overall impression is of a brand that knows exactly what it is: serious about sports, confident in its heritage, and unwilling to compromise on visual clarity.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99bbff"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  brand-purple: "#221155"
  brand-purple-active: "#1a0f44"
  brand-purple-soft: "#443388"
  accent-gold: "#d4a017"
  accent-gold-active: "#b8860b"
  success: "#28a745"
  error: "#dc3545"
  warning: "#ffc107"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px

rounded:
  none: 0px
  xs: 2px
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
    padding: 16px 32px
    height: 52px
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
    padding: 15px 31px
    height: 52px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-purple:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-purple-active:
    backgroundColor: "{colors.brand-purple-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary}"
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
    boxShadow: "0 0 0 3px rgba(0,51,153,0.15)"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-section-purple:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.on-primary}"
    opacity: 0.9
    marginBottom: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  search-bar-focus:
    boxShadow: "0 4px 16px rgba(0,0,0,0.15)"
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-purple:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
    border: "1px solid {colors.primary}"
  section-heading:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 2px
    margin: "{spacing.lg} 0"
  spinner:
    color: "{colors.primary}"
    size: 24px
  spinner-sm:
    color: "{colors.primary}"
    size: 16px
  checkbox:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    width: 44px
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    width: 20px
    height: 20px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
  tab-inactive-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 600
  alert-info:
    backgroundColor: "#e6f0ff"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid #b3d4ff"
  alert-success:
    backgroundColor: "#e6f9e6"
    textColor: "#155724"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid #b3e6b3"
  alert-error:
    backgroundColor: "#fce6e6"
    textColor: "#721c24"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid #f5b3b3"
  alert-warning:
    backgroundColor: "#fff9e6"
    textColor: "#856404"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid #ffeab3"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  icon-button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-primary-hover:
    backgroundColor: "{colors.primary-active}"
  avatar:
    rounded: "{rounded.full}"
    size: 40px
  avatar-sm:
    rounded: "{rounded.full}"
    size: 32px
  avatar-lg:
    rounded: "{rounded.full}"
    size: 56px
  rating-stars:
    color: "{colors.accent-gold}"
    size: 16px
  rating-stars-sm:
    color: "{colors.accent-gold}"
    size: 12px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill-purple:
    backgroundColor: "{colors.brand-purple}"
    rounded: "{rounded.full}"
    height: 8px
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"
    animation: "pulse 1.5s infinite"

## Components

### Buttons
**`button-primary`** — The workhorse CTA of the system. A solid #003399 rectangle with 8px radius, white text at 16px/600 weight, and 16px 32px padding. On hover, it darkens to #002277. The disabled state uses a pale blue #99bbff to signal inactivity without disappearing. Height is a generous 52px, making it feel substantial on both desktop and mobile.

**`button-secondary`** — An outlined variant for secondary actions. White background with a 2px solid #003399 border and matching blue text. On hover, the background shifts to #f5f5f5 and the border darkens. Padding is 15px 31px to account for the border offset, keeping the overall height at 52px.

**`button-ghost`** — A text-only button for the lightest visual weight. Transparent background with blue text. On hover, a soft gray background (#f5f5f5) appears. Used for "Cancel", "Skip", or "Learn more" links that need button semantics.

**`button-purple`** — A secondary brand accent using the deep purple #221155. Used for special promotions, premium features, or to differentiate a secondary call-to-action from the primary blue. Same dimensions and typography as `button-primary`.

**`button-gold`** — An accent CTA using gold #d4a017 with dark text. Used sparingly for high-value actions like "Add to Cart" on sale items, loyalty program sign-ups, or limited-time offers. The gold creates visual contrast against the blue/purple system.

**`button-pill`** — A fully rounded variant for filters, tags, or compact actions. Uses 14px/600 weight text, 10px 24px padding, and a 40px height. The pill shape signals a toggleable or dismissible action.

**`button-pill-outline`** — The outlined version of the pill button. White background with a 1px blue border. Used for inactive filter states or secondary pill actions.

### Cards
**`product-card`** — The primary product display unit. A white card with 12px radius, subtle shadow (0 1px 3px rgba(0,0,0,0.08)), and no padding on the container — spacing is handled by child elements. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.12). The image area uses a 1:1 aspect ratio with rounded top corners. Title uses 16px/600 weight, price uses 16px/600 weight, and badges appear as purple pills in the top-left corner.

**`product-card-badge`** — A small purple badge (#221155) with white uppercase 11px/600 text, 4px 8px padding, and 2px radius. Used to indicate "New", "Sale", "Limited Edition", or "Best Seller" status. Positioned absolutely within the card image area.

### Navigation
**`nav-bar`** — A fixed top navigation at 72px height with white background and a soft bottom border (#e6e6e6). On scroll, a subtle shadow appears (0 2px 8px rgba(0,0,0,0.08)). Links use 15px/600 weight with 8px 16px padding. Active links show a 2px blue bottom border and blue text. Hover state also turns text blue.

**`nav-link`** — Individual navigation items. Transparent background, dark text, 15px/600 weight. Active state adds a 2px blue underline and blue text. Hover state transitions text to blue.

### Forms
**`text-input`** — Standard text input at 48px height with 12px 16px padding, 8px radius, and a 1px #cccccc border. On focus, the border becomes 2px #003399 with a 3px blue glow (rgba(0,51,153,0.15)). Error state uses a 2px red border (#dc3545). Placeholder text uses #999999.

**`select-input`** — Same dimensions and styling as text-input but with a custom dropdown arrow. The arrow is a blue (#003399) chevron icon positioned on the right.

**`textarea`** — Same styling as text-input but without a fixed height. Minimum height of 100px with vertical resize enabled.

**`checkbox`** — A 20px square with 2px #cccccc border and 2px radius. Checked state fills with #003399 and shows a white checkmark. Focus state includes the same blue glow as text inputs.

**`radio`** — A 20px circle with 2px #cccccc border. Checked state shows a 6px solid #003399 inner circle. Focus state includes blue glow.

**`toggle`** — A 44px wide, 24px tall pill with #cccccc background. Active state fills with #003399. The thumb is a 20px white circle that slides horizontally.

### Badges
**`badge-primary`** — Blue (#003399) background with white uppercase text at 11px/600 weight. 4px 8px padding with 2px radius. Used for status indicators, category labels, or metadata tags.

**`badge-purple`** — Purple (#221155) background with white text. Same dimensions as primary badge. Used to differentiate premium or exclusive content.

**`badge-gold`** — Gold (#d4a017) background with dark text. Used for promotional badges, sale indicators, or loyalty program tags.

**`badge-outline`** — Transparent background with a 1px blue border and blue text. Used for secondary or inactive badge states.

### Alerts
**`alert-info`** — Light blue background (#e6f0ff) with blue text (#003399) and a blue border (#b3d4ff). 8px radius with 16px padding. Used for informational messages.

**`alert-success`** — Light green background (#e6f9e6) with dark green text (#155724) and green border (#b3e6b3). Used for success confirmations.

**`alert-error`** — Light red background (#fce6e6) with dark red text (#721c24) and red border (#f5b3b3). Used for error messages.

**`alert-warning`** — Light yellow background (#fff9e6) with dark yellow text (#856404) and yellow border (#ffeab3). Used for warning messages.

### Navigation Elements
**`breadcrumb-link`** — Gray (#666666) text at 13px/500 weight. The current page uses dark text (#333333) at 600 weight. Separators are forward slashes in the muted color.

**`pagination-button`** — White background with dark text, 8px 12px padding, 8px radius, and a 1px #cccccc border. Active page uses blue background with white text. Disabled pages use light gray background with #999999 text.

**`tab-active`** — Blue (#003399) background with white text at 14px/600 weight. 10px 20px padding with 8px radius. Used for the currently selected tab in a tab group.

**`tab-inactive`** — Light gray (#f5f5f5) background with gray (#666666) text. On hover, background becomes slightly darker (#e6e6e6) and text becomes darker (#333333).

### Feedback & Loading
**`spinner`** — A 24px rotating circle with a #003399 stroke. The spinner-sm variant is 16px. Used for loading states on buttons, content areas, or full-page loads.

**`skeleton`** — A pulsing gray (#e6e6e6) rectangle with 8px radius. Uses a 1.5s infinite pulse animation. Used as a placeholder for loading content.

**`progress-bar`** — A 8px tall pill with #e6e6e6 background. The fill uses #003399 (or #221155 for purple variants) and animates width transitions.

### Modals & Tooltips
**`modal-overlay`** — A semi-transparent black (rgba(0,0,0,0.5)) backdrop that covers the viewport. Clicking outside the modal content dismisses it.

**`modal-content`** — A white card with 12px radius, 32px padding, and a deep shadow (0 8px 32px rgba(0,0,0,0.12)). Contains a close button in the top-right corner.

**`tooltip`** — A dark (#111111) background with white text at 13px/500 weight. 8px 12px padding with 8px radius. Appears on hover with a 200ms delay.

### Icons & Avatars
**`icon-button`** — A 40px circle with transparent background and dark icon. On hover, a light gray (#f5f5f5) background appears. The primary variant uses blue (#003399) background with white icon.

**`avatar`** — A 40px circle for user profile images. The sm variant is 32px, the lg variant is 56px. Fallback shows initials on a light gray background.

**`rating-stars`** — Gold (#d4a017) star icons at 16px. The sm variant is 12px. Half-star ratings are supported with a clipped fill.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger navigation, full-width buttons, stacked product cards, reduced padding (16px gutters), hero sections collapse to 300px min-height, font sizes scale down (display-xl becomes 24px) |
| Tablet | 744–1128px | Two-column product grid, sticky top nav, 24px gutters, hero sections at 360px min-height, search bar becomes visible in nav |
| Desktop | 1128–1440px | Three-column product grid, full navigation visible, 32px gutters, hero sections at 400px min-height, multi-column footer |
| Wide | > 1440px | Max-width container at 1440px, four-column product grid, expanded hero sections, additional whitespace in layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height
- Icon buttons are 40px with 44px clickable area via padding
- Product card tap targets (title, price, badge) are at least 44px tall
- Navigation links have 48px tap height on mobile
- Form inputs maintain 48px height for comfortable tapping
- Toggle switches are 44px wide for thumb accessibility

### Collapsing Strategy
- Top navigation collapses to hamburger menu on mobile (< 744px), with a slide-out drawer for navigation links
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer multi-column layout collapses to single column on mobile, with accordion-style section headers
- Search bar collapses from full input to icon-only on mobile, expanding on tap
- Hero sections collapse from side-by-side content to stacked on mobile
- Tab groups collapse to horizontal scroll on mobile, with arrow indicators for overflow
- Breadcrumb navigation truncates to show only the current and parent page on mobile
- Table layouts collapse to stacked card layouts on mobile
- Multi-step forms collapse to single-step vertical layout on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site. The typography system uses Inter as a reasonable modern sans-serif fallback, but the actual brand font may differ. If Molten uses a custom or licensed typeface, it should replace the Inter stack.
- Only two hex colors were extracted from the live site (#003399 and #221155). The full color palette (including accent gold, success green, error red, warning yellow, and all gray tones) has been inferred from common e-commerce patterns and may not match the actual brand system.
- Hover, active, focus, and disabled states for all components are inferred from standard interaction patterns. Actual brand-specific transitions, animations, and micro-interactions are unknown.
- Error, success, warning, and info alert styles are based on common web conventions. The brand may use different colors or iconography for these states.
- No meta theme-color was found, so the browser chrome color on mobile is unknown.
- The platform is not Shopify (platform-shopify: False), so the checkout and cart components may differ from Shopify's default patterns.
- Dark mode support is unknown. The current system assumes a light theme only.
- Sub-brand or product-line-specific color variations (e.g., for different sports equipment categories) are not documented.
- The actual spacing scale, border radius values, and component dimensions are inferred from common e-commerce patterns. The brand may use different values.
- No photography or illustration style guidance is available. The system assumes clean product photography on white backgrounds.
- Animation durations, easing curves, and transition timing functions are not documented.
- The actual button loading state (spinner position, text replacement behavior) is unknown.
- Form validation message styling (position, color, animation) is not documented.
- The brand's approach to accessibility (minimum contrast ratios, focus indicators, screen reader text) is unknown.
