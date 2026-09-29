---
version: alpha
name: "Satechi"
source_url: "https://satechi.net"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision electronics accessories brand that uses a deep near-black ink (#222021) as its anchor, with a single electric orange (#f55a19) providing the only primary voltage — a color that reads as both industrial safety marker and premium accent, never playful. The palette is deliberately restrained: the orange appears on CTAs, price tags, and the brand's signature "S" logo mark, while everything else — typography, cards, navigation — stays in a tight range of charcoal (#1b1c21), slate (#676986), and warm stone (#cfc6bf). This is a brand that sells docking stations, hubs, and adapters for Apple and PC ecosystems, and the design language mirrors the hardware: clean, metallic, with no decorative flourish that doesn't serve function. The extracted hex list shows a surprising number of warm neutrals (#f5f2ef, #ede6e0, #c3b4a8) alongside the expected grays, suggesting a subtle warmth in surfaces that keeps the brand from feeling cold or purely utilitarian. Cards use soft corners ({rounded.sm} ~8px) rather than pills or sharp squares, and the typography stack defaults to system fonts — no custom brand typeface detected, which is common for hardware-adjacent brands that let product photography carry the visual weight. The checkout and utility colors (#00eab6, #1878b9, #e22120) are likely Shopify Pay, Klarna, and error states respectively, not brand primaries. The overall impression is of a brand that trusts its product imagery and clean layout over decorative design moves — the orange is the only moment of personality, and it's used sparingly.

colors:
  primary: "#f55a19"
  primary-active: "#e04a0f"
  primary-disabled: "#f5b89a"
  ink: "#222021"
  body: "#4c4c4c"
  muted: "#6d6d6d"
  muted-soft: "#919090"
  hairline: "#dedede"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  surface-warm: "#f5f2ef"
  surface-warm-strong: "#ede6e0"
  on-primary: "#ffffff"
  accent-slate: "#676986"
  accent-deep-slate: "#272d45"
  accent-warm-stone: "#cfc6bf"
  accent-warm-stone-strong: "#c3b4a8"
  accent-teal: "#0e7a82"
  error: "#e22120"
  success: "#00eab6"
  info: "#1878b9"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    height: 44px
  button-outline-orange:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-outline-orange-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
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
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  logo-mark:
    height: 28px
    width: auto
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(34,32,33,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-body:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  product-card-price-sale:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 500px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  feature-grid:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  feature-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  feature-icon:
    width: 32px
    height: 32px
    marginBottom: "{spacing.md}"
  feature-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  feature-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  footer-divider:
    backgroundColor: "{colors.accent-slate}"
    height: 1px
    margin: "{spacing.xl} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-trigger-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    width: 44px
    height: 44px
  quantity-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    width: 44px
    height: 44px
  quantity-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: center
    width: 48px
    height: 44px
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
    size: 16px
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline-soft}"
  tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.md} {spacing.base}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "2px solid {colors.primary}"
  tab-hover:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: "{spacing.md} {spacing.base}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  toggle-switch-knob-active:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    width: 20px
    height: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    width: 20px
    height: 20px
  checkbox-label:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    width: 20px
    height: 20px
  radio-checked:
    backgroundColor: "{colors.canvas}"
    border: "6px solid {colors.primary}"
    rounded: "{rounded.full}"
    width: 20px
    height: 20px
  radio-label:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "rgba(34,32,33,0.6)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 560px
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    width: 32px
    height: 32px
  modal-close-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    width: 32px
    height: 32px
  notification-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    minWidth: 20px
    height: 20px
    padding: "0 6px"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-small:
    color: "{colors.primary}"
    size: 16px
  loading-spinner-large:
    color: "{colors.primary}"
    size: 40px
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    animation: "pulse 1.5s ease-in-out infinite"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, using the signature orange (#f55a19) on a white background. On hover, the orange deepens to `{colors.primary-active}` (#e04a0f). Disabled state uses a muted orange `{colors.primary-disabled}` (#f5b89a) with white text. All primary buttons use `{rounded.sm}` (8px) corners — a subtle softening that prevents the hardware brand from feeling too sharp. Height is 44px with 12px vertical padding, slightly shorter than the 48px standard to feel more compact and technical.

**`button-secondary`** — An outlined button with a white fill and `{colors.hairline}` (#dedede) border. On hover/active, the border switches to `{colors.ink}` (#222021) for a crisp dark outline. Used for "Learn More" and secondary product actions where the orange primary would compete with other orange elements on the page.

**`button-tertiary`** — A text-only button with no border or background. On hover, a `{colors.surface-soft}` (#fafafa) background appears. Used for navigation links, "View All" links in category sections, and cancel actions in modals.

**`button-outline-orange`** — An outlined button using the brand orange as border and text color. On hover, the fill becomes solid orange with white text. Used for "Add to Cart" on product detail pages where the primary CTA is already orange, or for secondary purchase actions.

**`button-pill`** — A fully rounded pill button using `{rounded.full}`, smaller at 36px height with `{typography.button-sm}`. Used for filter tags, category quick-links, and promotional badges. The pill shape is reserved for these smaller utility buttons — the main CTAs stay at `{rounded.sm}`.

### Cards
**`product-card`** — A white card with a 1px `{colors.hairline-soft}` (#f0f0f0) border and `{rounded.sm}` corners. On hover, the border thickens to `{colors.hairline}` (#dedede) and a subtle box shadow appears (0 4px 12px rgba(34,32,33,0.08)). The card has no internal padding — the image fills the top with `{rounded.sm} {rounded.sm} 0 0`, and the body section uses `{spacing.base}` horizontal and `{spacing.lg}` bottom padding. Product titles use `{typography.title-sm}` (16px, 600 weight), prices use `{typography.body-md}` in the brand orange, and sale prices show a line-through `{colors.muted}` original price.

**`product-card-badge`** — Small uppercase badges that sit on product images. Three variants: orange for "Sale" or promotional, black (`{colors.ink}`) for "Sold Out", and teal (`{colors.accent-teal}` #0e7a82) for "New". All use `{typography.badge}` (11px, 600 weight, uppercase) with `{rounded.xs}` (4px) corners and 2px/8px padding.

**`feature-card`** — Used in the feature grid sections on landing pages. A `{colors.surface-soft}` (#fafafa) background with `{rounded.sm}` corners and `{spacing.lg}` padding. Contains a 32px icon, a `{typography.title-sm}` heading, and `{typography.body-sm}` description text in `{colors.body}` (#4c4c4c).

### Navigation
**`nav-bar`** — A fixed-height 64px white navigation bar with a 1px `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` (14px, 500 weight, uppercase with 0.3px letter-spacing) — the uppercase treatment gives the brand a technical, spec-sheet feel. Links default to `{colors.muted}` (#6d6d6d), hover to `{colors.primary}` (#f55a19), and active to `{colors.ink}` (#222021). The logo mark sits at 28px height.

**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) at 40px height with a `{colors.surface-soft}` background and `{colors.hairline-soft}` border. On focus, the border becomes a 2px orange line. The pill shape for search is the one place where `{rounded.full}` appears on a functional element — a subtle nod to Apple's design language that the brand's target audience would recognize.

**`breadcrumb`** — Small caption text (13px, 400 weight) in `{colors.muted}` (#6d6d6d), with the active page in `{colors.ink}` (#222021). Separators use `{colors.hairline}` (#dedede) with 4px horizontal padding.

### Forms
**`text-input`** — Standard 48px input with `{rounded.sm}` corners, a 1px `{colors.hairline}` border, and `{typography.body-md}`. On focus, the border becomes 2px `{colors.primary}`. Error state uses 2px `{colors.error}` (#e22120). Placeholder text uses `{colors.muted-soft}` (#919090).

**`select-input`** — Matches the text input styling with a 1px hairline border and 48px height. Used for quantity selectors and product variant dropdowns.

**`quantity-selector`** — A three-part control with decrement button, numeric input, and increment button. The outer container has a 1px `{colors.hairline}` border and `{rounded.sm}` corners at 44px height. Buttons are 44px wide with `{colors.muted}` icons that turn `{colors.ink}` on hover with a `{colors.surface-soft}` background. The center input is 48px wide with centered text.

**`toggle-switch`** — A 44px wide, 24px tall pill with a 20px circular knob. Off state uses `{colors.hairline}` (#dedede) background; on state uses `{colors.primary}` (#f55a19). The knob is always white.

**`checkbox`** and **`radio`** — Both use 20px dimensions with 2px `{colors.hairline}` borders and `{rounded.xs}` (4px) for checkboxes, `{rounded.full}` for radios. Checked state fills with `{colors.primary}` — checkboxes get a solid fill, radios get a 6px inner dot with white border.

### Footer
**`footer`** — A dark section using `{colors.ink}` (#222021) as background with white text. Links use `{colors.muted-soft}` (#919090) and hover to white. Section headings use `{typography.title-sm}` in white. A 1px `{colors.accent-slate}` (#676986) divider separates the link columns from the bottom legal section. The footer padding matches the section standard at 64px vertical.

### Modals and Overlays
**`modal-overlay`** — A 60% opacity black (`{colors.ink}`) scrim. The modal content is white with `{rounded.md}` (12px) corners, `{spacing.xl}` padding, and a max-width of 560px. The close button is a 32px circle with `{colors.surface-soft}` background that darkens to `{colors.hairline}` on hover.

### Loading States
**`loading-spinner`** — A 24px spinning indicator in `{colors.primary}` (#f55a19), with small (16px) and large (40px) variants. **`skeleton`** — A pulsing placeholder using `{colors.hairline-soft}` (#f0f0f0) with `{rounded.xs}` corners and a 1.5s pulse animation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger menu, hero section reduces padding to 32px vertical, footer stacks vertically, product cards use full-width images, search bar becomes full-width below nav |
| Tablet | 744–1128px | Two-column product grid (2 col), nav shows limited links with "More" dropdown, hero uses 48px vertical padding, feature grid goes 2x2, footer shows 2-column link layout |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav bar visible, hero uses 64px padding, feature grid goes 3x3 or 4x2, footer shows 4-column link layout |
| Wide | > 1440px | Four-column product grid (4 col), max-width container at 1440px centered, hero content max-width at 600px, feature grid can go 4x2 |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons and close buttons are minimum 32px with 44px touch area via padding
- Quantity selector buttons are 44px wide to accommodate tap targets
- Toggle switches are 44px wide with 24px height — the full width is tappable
- Checkboxes and radios use 20px with 44px click area via label association
- Mobile nav hamburger target is minimum 44px x 44px

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px — all nav links move to a slide-out drawer
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Feature grid collapses from 4 columns to 2 columns to single column on mobile
- Footer link columns collapse from 4 to 2 on tablet, to single column on mobile
- Product detail page moves from side-by-side (image + details) to stacked on mobile
- Accordion sections replace tabbed content on mobile for product specs and reviews
- Search bar collapses from inline in nav to full-width below nav on mobile
- Breadcrumbs truncate on mobile, showing only current page and "Home" link

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — the site uses system font inheritance (`inherit`). The actual font-family stack may be set at a higher level (body tag) that wasn't captured in extraction. The typography block uses a standard system font stack as fallback.
- Hover states for most components are inferred from common patterns — actual hover transitions (duration, easing) were not extractable.
- Error state styling for forms (error messages, error icon placement) was not observed.
- Dark mode is not present on the live site — no `prefers-color-scheme` media queries detected.
- The extracted hex list contains 30+ colors, many of which are likely Shopify checkout widgets (Klarna pink #ffb3c7 not present, but #00eab6 is Shopify Pay green, #1878b9 is likely a payment badge blue, #e22120 is standard error red). These are noted as non-brand colors.
- The brand's secondary accent colors (slate #676986, warm stone #cfc6bf, teal #0e7a82) are inferred from frequency in the extracted list — their exact usage context (badges, icons, dividers) may vary.
- No animation or transition timing values were extractable — all motion is assumed at 200-300ms ease-in-out as standard.
- The extracted font-family declarations only returned `inherit` and widget-specific fonts — no custom typeface was found.
