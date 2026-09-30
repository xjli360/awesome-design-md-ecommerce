---
version: alpha
name: "Tylko"
source_url: "https://tylko.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Tylko is a Polish furniture brand that has redefined the modular shelving and storage category through a lens of quiet, architectural precision. The brand's visual identity is anchored on a single, deep charcoal tone — `#313131` — which serves as both the primary ink for all typography and the dominant accent color across buttons, icons, and structural UI elements. This near-black hue, paired with a generous white canvas (`{colors.canvas}`), creates a high-contrast, editorial atmosphere that feels more like a design studio than a furniture retailer. The typographic system relies on system-native sans-serif stacks (`-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, system-ui`), avoiding custom fonts to keep the interface fast, clean, and universally legible. Rounded corners are used sparingly — `{rounded.sm}` (8px) for buttons and `{rounded.md}` (12px) for cards — lending a subtle softness to an otherwise sharp, grid-based layout. The brand's signature design move is the configurator interface: a full-screen, step-by-step builder that lets customers customize shelf dimensions, colors, and configurations in real time. This tool is the beating heart of the experience, and the design system supports it with minimal chrome, high-density information display, and a restrained palette that never competes with the product photography. The overall mood is calm, confident, and utilitarian in the best sense — every pixel feels intentional, every interaction purposeful. Tylko does not shout; it invites scrutiny.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-wood: "#c8a96e"
  accent-green: "#4a7c59"
  error: "#d32f2f"
  success: "#2e7d32"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
  section: 80px

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
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
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base}"
  configurator-step:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.xl} {spacing.lg}"
  configurator-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"
  configurator-option-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  configurator-option-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
    opacity: 0.5
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-image:
    rounded: "{rounded.none}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base}"
  stepper-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  stepper-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  stepper-indicator-complete:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 600px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Tylko experience, rendered in the brand's signature `#313131` charcoal on a white background. On hover, it deepens to `{colors.primary-active}` (`#1a1a1a`) for tactile feedback. The disabled state uses `{colors.primary-disabled}` (`#a0a0a0`) to signal non-interactivity while maintaining readability. All primary buttons use `{rounded.sm}` (8px) for a soft, approachable corner that contrasts with the otherwise sharp grid.

**`button-secondary`** — An outlined variant that inverts the primary relationship: a white fill with a 2px `{colors.primary}` border and charcoal text. On hover, the background shifts to `{colors.surface-soft}` (`#f5f5f5`) and the border deepens to `{colors.primary-active}`. This button is used for "Configure" or "Learn More" actions where the primary CTA is reserved for cart or checkout.

**`button-tertiary-text`** — A text-only button with no background or border, used for low-emphasis actions like "Cancel" or "Skip." The text color is `{colors.primary}` and it inherits the `button-md` typography. On hover, it may underline or slightly darken, though this state is not fully captured in the extracted data.

**`button-pill-primary`** — A fully rounded (`{rounded.full}`) pill button used in the configurator for dimension selection or color swatch confirmation. It uses `{colors.primary}` background with white text and `button-sm` typography for compact sizing. The pill shape signals a toggle or selection action rather than a navigation event.

**`button-pill-outline`** — The outlined counterpart to the pill primary, used for unselected options in the configurator. It has a white background, charcoal text, and a 1px `{colors.hairline}` border. On selection, it transitions to the pill-primary style.

### Cards
**`product-card`** — The standard product card for the catalog grid, featuring a white background, `{rounded.md}` (12px) corners, and no internal padding (images bleed to the top edge). The card contains an image area with top-rounded corners (`{rounded.md} {rounded.md} 0 0`), a title using `{typography.title-sm}`, and a price using `{typography.body-md}`. Cards are typically displayed in a 3- or 4-column grid on desktop, collapsing to 2 columns on tablet and a single column on mobile.

**`property-card`** (not explicitly defined but implied by product-card structure) — A variant of the product card used for material or color swatches in the configurator. These are smaller, square-format cards with a `{rounded.sm}` corner and a 1px `{colors.hairline}` border. The selected state uses a 2px `{colors.primary}` border and a subtle shadow.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 64px tall, with a white background and a 1px `{colors.hairline-soft}` bottom border. It contains the Tylko logo on the left, primary navigation links (Products, Configurator, Inspiration, About) in the center, and utility icons (Search, Cart, Account) on the right. The nav uses `{typography.nav-link}` (14px, weight 500) for link text.

**`nav-link-active`** — The active navigation link state, indicated by a 2px `{colors.primary}` bottom border. The text remains `{colors.ink}` (`#313131`). Inactive links use `{colors.muted}` (`#757575`) to visually recede.

### Forms
**`text-input`** — Standard text input fields used in the checkout and account flows. They have a white background, `{rounded.sm}` (8px) corners, a 1px `{colors.hairline}` border, and 12px/16px padding. On focus, the border thickens to 2px `{colors.primary}`. Error states use a 2px `{colors.error}` border.

**`select-input`** — Dropdown select fields styled identically to text inputs, with a custom chevron icon in `{colors.muted}`. The dropdown menu itself uses `{colors.canvas}` with `{rounded.sm}` corners and a subtle shadow.

**`textarea`** — Multi-line text input for contact forms or order notes, sharing the same styling as `text-input` but with a taller default height and resizable by the user.

### Configurator
**`configurator-step`** — The full-screen step container for the product configurator. Each step (Dimensions, Configuration, Color, Summary) is presented as a white panel with `{spacing.xl}` horizontal padding and `{spacing.lg}` vertical padding. The step title uses `{typography.title-md}`.

**`configurator-option`** — Individual selectable options within a configurator step (e.g., shelf depth, material finish). They have a `{colors.surface-soft}` background, `{rounded.sm}` corners, a 1px `{colors.hairline}` border, and `{spacing.md}` / `{spacing.base}` padding. The selected state (`configurator-option-selected`) switches to a white background with a 2px `{colors.primary}` border. Disabled options are dimmed to 50% opacity with `{colors.muted-soft}` text.

**`stepper-indicator`** — Circular step indicators (32px diameter) that show the user's progress through the configurator. Inactive steps use `{colors.surface-soft}` background with `{colors.muted}` text. The active step uses `{colors.primary}` with white text. Completed steps use `{colors.success}` (`#2e7d32`) with white text.

### Badges
**`badge-new`** — A small, uppercase badge used to flag new product lines or features. It uses `{colors.primary}` background, white text, `{typography.badge}` (11px, weight 600, uppercase), and `{rounded.xs}` (4px) corners. Padding is minimal at 2px/8px.

**`badge-sale`** — A red badge (`{colors.error}`) for sale or discount items, following the same typography and corner styling as `badge-new`.

**`badge-eco`** — A green badge (`{colors.accent-green}`) for sustainable or eco-friendly product options, following the same styling pattern.

### Footer
**`footer-section`** — The site footer, rendered as a full-width `{colors.primary}` (`#313131`) background with white text. It contains columns for company information, customer service, legal links, and social media icons. Links use `{typography.link}` (14px, weight 400) in white. The section has `{spacing.section}` (80px) vertical padding.

### Modals
**`modal-overlay`** — A semi-transparent black overlay (`{colors.scrim}` at 50% opacity) that covers the viewport behind a modal dialog.

**`modal-content`** — The modal dialog container, with a white background, `{rounded.md}` (12px) corners, `{spacing.xl}` padding, and a maximum width of 600px. It contains a close button (an `icon-button-circle` variant), a title using `{typography.title-lg}`, and body content using `{typography.body-md}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; configurator steps stack vertically; footer columns stack to single column; hero banner reduces padding to `{spacing.lg}`; search bar becomes full-width; product cards show 2-up grid; stepper indicators become smaller (24px) |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows all links but with reduced horizontal padding; configurator uses a two-panel layout (options on left, preview on right); footer shows 2-column layout; hero banner uses `{spacing.xl}` padding |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; configurator uses full two-panel layout; footer shows 4-column layout; hero banner uses `{spacing.section}` padding |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; configurator panel has max-width constraints; hero banner content centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Icon buttons (search, cart, account) are 44px x 44px with `{rounded.full}` corners.
- Configurator options have a minimum tap area of 48px x 48px.
- Stepper indicators are 32px x 32px with 8px of touch padding on mobile.
- Nav-bar links have 16px horizontal padding and 12px vertical padding for comfortable tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer. The drawer contains all primary links, utility icons, and a condensed search bar.
- The product grid collapses from 3-4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- The configurator collapses from a two-panel layout (options + preview) on desktop to a single-column, step-by-step flow on mobile.
- Footer columns collapse from 4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- Hero banners collapse from full-width imagery with overlaid text to stacked layouts (image above text) on mobile.
- Accordion components (used in FAQs and product details) are always collapsed by default on mobile and expand on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary text buttons (underline vs. color shift) could not be reliably extracted.
- Error styling for form validation messages (color, typography, iconography) is inferred from common patterns but not confirmed from the live site.
- Focus ring styles (outline vs. box-shadow, color, offset) for keyboard navigation are not captured.
- Dark mode or high-contrast mode color overrides are not defined.
- Sub-brand or regional palette variations (e.g., EU vs. US market) are unknown.
- Animation and transition timing values (e.g., button hover duration, configurator step transitions) are not extracted.
- The exact font stack for the Tylko logo (which may use a custom or proprietary typeface) is not captured; the system font stack is used as a fallback.
- Loading states (skeleton screens, spinners) and their specific styling are not defined.
- The configurator's 3D preview rendering styles (canvas, controls, lighting) are outside the scope of this design system.
- Print stylesheet overrides are not available.
- The `meta theme-color` value was not present on the extracted page, so the browser chrome color on mobile is undefined.
