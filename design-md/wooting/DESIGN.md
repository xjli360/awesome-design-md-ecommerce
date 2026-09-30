---
version: alpha
name: "Wooting"
source_url: "https://wooting.io"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A performance-first keyboard brand built on a raw, industrial aesthetic where function dictates form and every pixel serves a purpose. The brand lives in the tension between high-end gaming hardware and minimalist Scandinavian design — a black-on-black palette anchored by `#000000` ink and `#ffffff` canvas, with a single electric accent in `#00ff00` that pulses through keycaps, switch housings, and software UI elements like a heartbeat monitor. Wooting's signature is the analog keyboard — a product that redefines input by measuring keypress depth rather than binary on/off — and the visual system mirrors this philosophy: nothing is decorative, everything is calibrated. Typography runs a monospaced or clean sans-serif at modest weights (400–600), with display sizes rarely exceeding 24px, letting the product photography of exposed circuit boards, aluminum cases, and custom keycap sets carry the emotional weight. Corners are sharp (`{rounded.none}`) on hardware imagery and industrial components, while software surfaces use `{rounded.sm}` for buttons and `{rounded.md}` for cards — a subtle distinction between the physical and digital layers of the experience. The color palette is deliberately restrained: ink (`#000000`), body (`#1a1a1a`), muted (`#666666`), muted-soft (`#999999`), hairline (`#333333`), hairline-soft (`#444444`), canvas (`#ffffff`), surface-soft (`#f5f5f5`), surface-card (`#ffffff`), on-primary (`#000000`), with the primary green (`#00ff00`) used sparingly for CTAs, active states, and performance indicators. This is not a brand that shouts — it whispers in voltage, then delivers a shock.

colors:
  primary: "#00ff00"
  primary-active: "#00cc00"
  primary-disabled: "#66ff66"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#333333"
  hairline-soft: "#444444"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#000000"
  on-dark: "#ffffff"
  performance-green: "#00ff00"
  analog-blue: "#0066ff"
  error-red: "#ff3333"
  warning-yellow: "#ffcc00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  code-block:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  button-icon-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.error-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
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
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-old-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  hero-cta-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 31px"
    height: 48px
    border: "1px solid {colors.on-dark}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
    width: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.warning-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  switch-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  switch-track-active:
    backgroundColor: "{colors.primary}"
  switch-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  slider-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  slider-track-active:
    backgroundColor: "{colors.primary}"
  slider-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "2px solid {colors.primary}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  tab-panel:
    padding: "{spacing.lg} 0"
  dropdown-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  dropdown-item:
    padding: "{spacing.sm} {spacing.base}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  dropdown-item-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  keycap:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code-block}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  keycap-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  keycap-analog:
    backgroundColor: "{colors.analog-blue}"
    textColor: "{colors.on-dark}"
  switch-housing:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` green with `{colors.on-primary}` black text. Used for key actions like "Add to Cart", "Pre-order", and "Configure". On hover, shifts to `{colors.primary-active}` for a subtle darkening effect. Disabled state uses `{colors.primary-disabled}` with reduced contrast. The `{rounded.sm}` corners keep the button feeling precise and technical rather than soft.

**`button-secondary`** — An outlined variant with white background, black text, and a `{colors.hairline}` border. Used for secondary actions like "Learn More" or "View Details". On hover, the border darkens to `{colors.ink}` and background shifts to `{colors.surface-soft}`. Maintains the same `{rounded.sm}` and `{typography.button-md}` sizing for visual consistency.

**`button-tertiary`** — A text-only button with no background or border. Used for less prominent actions like "Cancel" or "Skip". On hover, gains a `{colors.surface-soft}` background. The `{typography.button-md}` weight ensures it remains legible against the canvas.

**`button-ghost`** — A minimal icon or text button with `{colors.muted}` text that darkens to `{colors.ink}` on hover. Used in toolbars, settings panels, and dense UI areas where visual noise must be minimized.

**`button-icon`** — A square 36×36px icon button with transparent background. On hover, fills with `{colors.surface-soft}`. Used for actions like search, cart, and menu toggles in the navigation bar.

### Cards
**`product-card`** — The primary product display component, featuring a white background, `{rounded.md}` corners, and a `{colors.hairline-soft}` border. On hover, the border strengthens to `{colors.hairline}` and a subtle box shadow lifts the card. The image area uses `{rounded.md}` on top corners only, creating a clean break between photo and content. Price is rendered in `{typography.title-md}` with old prices in `{typography.body-sm}` with strikethrough. Badges (New, Sale, Limited) sit in the top-left corner of the image area.

### Navigation
**`nav-bar`** — A fixed 64px header with white background and a `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` with `{colors.muted}` text that becomes `{colors.ink}` on hover. The active link is underlined with a 2px `{colors.primary}` green border. The logo sits left-aligned, with primary navigation centered and utility icons (search, cart, account) right-aligned.

**`nav-link-active`** — The active navigation state, distinguished by a 2px `{colors.primary}` bottom border and `{colors.ink}` text color. This creates a clear visual anchor for the current section.

**`nav-link-inactive`** — Default navigation state with `{colors.muted}` text. On hover, text transitions to `{colors.ink}` without the bottom border, providing a subtle interactive cue.

### Forms
**`text-input`** — A standard text input with white background, `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border becomes a 2px `{colors.primary}` green line with no outline. Error state uses `{colors.error-red}` border. Disabled state uses `{colors.surface-soft}` background and `{colors.muted-soft}` text. Height is 44px for comfortable touch interaction.

**`select-input`** — A dropdown select styled identically to `text-input` for visual consistency. The dropdown arrow is rendered in `{colors.muted}`.

**`textarea`** — A multi-line text input with the same styling as `text-input` but without a fixed height. Used for longer form entries like reviews or contact messages.

### Hero
**`hero-section`** — A full-width section with `{colors.ink}` black background and `{colors.on-dark}` white text. Uses `{typography.display-xl}` for the headline with generous `{spacing.section}` padding. The primary CTA (`{colors.primary}` green) sits alongside a secondary outlined CTA (white border on black). Background may feature product photography or abstract circuit-board patterns at low opacity.

### Search
**`search-bar`** — A 44px search input with white background, `{colors.hairline}` border, and a search icon in `{colors.muted}`. On focus, the border becomes 2px `{colors.primary}` green. The input placeholder uses `{colors.muted-soft}` text. Results dropdown uses the `dropdown-menu` component styling.

### Footer
**`footer`** — A full-width section with `{colors.ink}` background and `{colors.on-dark}` white text. Links use `{colors.muted-soft}` that brighten to `{colors.on-dark}` on hover. Section headings use `{typography.title-sm}` in white. The footer includes columns for product categories, support, company info, and social links, with a copyright line at the bottom.

### Badges
**`badge-new`** — A small `{colors.primary}` green badge with black text, used to indicate newly released products. Uses `{typography.badge}` (10px uppercase monospace) for a technical, data-driven feel.

**`badge-sale`** — A `{colors.error-red}` badge with white text for sale or discount indicators. Maintains the same typography and sizing as `badge-new` for consistency.

**`badge-limited`** — A `{colors.warning-yellow}` badge with black text for limited edition or limited stock indicators. The yellow provides a visual hierarchy alongside the green and red badges.

### Interactive Controls
**`switch-track`** — A 44×24px pill-shaped track with `{colors.hairline}` background. When active, fills with `{colors.primary}` green. The thumb is a 20×20px white circle that slides horizontally.

**`slider-track`** — A 4px tall track with `{colors.hairline}` background. Active portion fills with `{colors.primary}` green. The thumb is a 20×20px white circle with a 2px `{colors.primary}` border.

**`progress-bar`** — A 4px tall track with `{colors.hairline-soft}` background. The fill uses `{colors.primary}` green, animating smoothly on state changes.

### Tooltips & Modals
**`tooltip`** — A dark tooltip with `{colors.ink}` background and white text. Uses `{typography.caption}` (12px) with 6px horizontal and 12px vertical padding. Appears on hover with a 200ms delay.

**`modal`** — A white modal with `{rounded.md}` corners and a 32px box shadow. The overlay uses `{colors.scrim}` at 60% opacity. Content padding is `{spacing.lg}` (24px). The modal header includes a title in `{typography.title-md}` and a close icon button.

### Accordion & Tabs
**`accordion`** — A vertically stacked list of expandable sections. Each item has a `{colors.hairline-soft}` bottom border. The header uses `{typography.title-md}` with 16px vertical padding. Content area collapses with a smooth height animation.

**`tab-active`** — The active tab state with `{colors.ink}` text and a 2px `{colors.primary}` bottom border. Inactive tabs use `{colors.muted}` text with no border. Tab panels have 24px padding.

### Dropdown
**`dropdown-menu`** — A white dropdown with `{rounded.sm}` corners, `{colors.hairline-soft}` border, and a 16px box shadow. Items have 8px vertical and 16px horizontal padding. On hover, items fill with `{colors.surface-soft}`. The active item uses `{colors.primary}` background with black text.

### Keycap & Switch Components
**`keycap`** — A visual representation of a keyboard key, rendered in `{colors.ink}` with white text and a `{colors.hairline}` border. Uses `{typography.code-block}` (13px monospace) for the key label. Active state fills with `{colors.primary}` green. Analog keys (Wooting's signature feature) use `{colors.analog-blue}` background.

**`switch-housing`** — A container for switch information, using `{colors.surface-soft}` background with a `{colors.hairline-soft}` border. Used in product configuration and comparison views.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; footer columns stack; search bar becomes full-width; buttons expand to full width; keycap grid becomes 2 columns |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links with "More" dropdown; hero maintains `{typography.display-lg}`; footer uses 2-column layout; search bar remains in nav; product cards show 2 per row |
| Desktop | 1128–1440px | Full nav with all links; three-column product grid; hero at full `{typography.display-xl}`; footer uses 4-column layout; search bar in nav with keyboard shortcut hint; product cards show 3 per row |
| Wide | > 1440px | Max-width container at 1440px; content centered; nav remains full; product grid can expand to 4 columns; hero uses larger imagery; additional whitespace around content sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44×44px touch target
- Icon buttons are 36×36px with 44×44px touch area via padding
- Product card tap targets (add to cart, configure) are minimum 48px height
- Slider thumbs are 20×20px with 44×44px touch area
- Switch toggles are 44×24px with 44×44px touch area
- Dropdown items are 44px minimum height
- Tab items are 44px minimum height
- Accordion headers are 44px minimum height

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with full-screen overlay menu
- Product filters collapse to a "Filter" button with slide-out panel on mobile
- Product description sections use accordion pattern on mobile (Specifications, Features, Reviews)
- Footer columns collapse to single column below 744px
- Hero section reduces padding and font size on mobile
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Product image galleries collapse to single-image view with swipe navigation on mobile
- Comparison tables collapse to card-based layout on mobile
- Keyboard configuration tools collapse to single-column layout on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations could not be extracted from the live site; `JetBrains Mono` and `Inter` are inferred from common Wooting design patterns and may differ from actual implementation
- No meta theme-color was found; the brand may not use a theme-color meta tag
- Extracted hex colors were not available from the live site; the color palette is reconstructed from Wooting's known brand identity (black, white, green) and may not match the exact live site values
- Hover, active, and focus states for all components are inferred from common patterns and may not match the exact implementation
- Error styling for form validation (error messages, error icons, error animations) is not documented
- Dark mode styling is not documented; Wooting may support a dark mode that inverts the palette
- Sub-brand or product-specific color variations (e.g., Wooting 60HE vs Wooting 80HE) are not documented
- Animation durations, easing curves, and transition properties are not specified
- Loading states (skeleton screens, spinners, progress indicators) are not documented
- Empty states for search results, cart, and wishlist are not documented
- Keyboard shortcut patterns (e.g., Cmd+K for search) are not documented
- Accessibility contrast ratios for all color combinations have not been verified
- Print styles and reduced-motion preferences are not documented
- The `code-block` typography token is inferred from the brand's technical nature and may not be an official token
- Shopify-specific components (cart drawer, checkout button, product variant selector) are not documented
- The exact border-radius values for `rounded.xs` through `rounded.xl` are estimated and may differ from the actual design system
