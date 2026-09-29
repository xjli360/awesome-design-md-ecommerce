---
version: alpha
name: "Kano"
source_url: "https://kano.me"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the idea that making a computer should feel like building a LEGO set, Kano uses a saturated, almost candy-colored palette anchored on a vivid orange (#ff6900) that reads as energy and play, not corporate tech. This primary orange appears on the site's primary CTAs, the product hero imagery, and the brand's signature "Make" button — a bright invitation to create rather than consume. The supporting palette is a deliberate departure from the grayscale-and-blue of conventional computing: a deep purple (#8a59c6) for secondary actions, a warm yellow (#ffc100) for badges and highlights, and a coral-pink (#ff5266) for error states and sale markers. The neutral system is a warm charcoal (#414a51) for body text rather than pure black, keeping the interface approachable. Typography runs a geometric sans-serif at moderate weights — display headlines sit at 24–32px in weight 600, never heavy enough to intimidate. Cards use a soft 12px radius (`{rounded.md}`), buttons are pill-shaped (`{rounded.full}`) at 48px height, and the entire interface avoids sharp corners except on data-heavy tables. The brand's signature design move is the "kit" metaphor: every product page shows components as individual, colorful modules arranged in a grid, each with its own subtle drop shadow and a 2px hairline (`{colors.hairline}`) that reads as a construction diagram. The footer is a dense, colorful grid of links and illustrations, more like a toy box than a legal document. Kano's voice is direct, instructional, and celebratory — "You made this" appears after every build step, rendered in the brand orange on a white canvas.

colors:
  primary: "#ff6900"
  primary-active: "#e05a00"
  primary-disabled: "#ffb380"
  ink: "#414a51"
  body: "#5a636a"
  muted: "#8a9299"
  muted-soft: "#b0b6bc"
  hairline: "#d0d4d8"
  hairline-soft: "#e5e8eb"
  canvas: "#ffffff"
  surface-soft: "#f5f6f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#8a59c6"
  accent-purple-active: "#7346a8"
  accent-yellow: "#ffc100"
  accent-yellow-active: "#e0a800"
  accent-pink: "#ff5266"
  accent-pink-active: "#e04556"
  accent-blue: "#1093f5"
  accent-blue-active: "#0d7ed4"
  success: "#2ecc71"
  warning: "#ffc100"
  error: "#ff5266"
  star-rating: "#ffc100"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-accent-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-purple-active:
    backgroundColor: "{colors.accent-purple-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  button-icon-circle-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.error}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 12px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: "600px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "2px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    textTransform: uppercase
  step-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
    padding: "0 16px"
  step-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  step-indicator-complete:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-coming-soon:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  kit-module:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline-soft}"
  kit-module-icon:
    height: 48px
    width: 48px
    rounded: "{rounded.sm}"
  kit-module-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  kit-module-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  rating-stars:
    color: "{colors.star-rating}"
    height: 16px
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 48px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
  toggle-switch-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  checkbox:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio-button:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "2px solid {colors.hairline}"
  radio-button-selected:
    border: "6px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand orange (#ff6900) with white text and a full pill shape. Used for "Make", "Get Started", "Buy Now", and "Add to Kit" actions. On hover, darkens to `{colors.primary-active}`. Disabled state uses a pale orange (`{colors.primary-disabled}`) to signal inactivity without losing brand recognition. Height is fixed at 48px for touch accessibility.

**`button-secondary`** — A white button with a 2px hairline border and dark text, used for secondary actions like "Learn More" or "View Details". On hover, the background shifts to `{colors.surface-soft}` and the border darkens to `{colors.ink}`. Maintains the full pill shape and 48px height for consistency with primary buttons.

**`button-accent-purple`** — The secondary brand color (`{colors.accent-purple}`) used for "Save to Kit", "Wishlist", and "Share" actions. Provides visual variety on pages where multiple orange buttons would be overwhelming. On hover, darkens to `{colors.accent-purple-active}`.

**`button-tertiary-text`** — A text-only button in the brand orange, used for "Skip", "Cancel", and "See All" links that need button behavior without a filled background. On hover, shifts to `{colors.primary-active}`. No padding or height constraints — inherits from parent layout.

**`button-icon-circle`** — A 40px circular icon button with a soft gray background, used for close, menu, and utility actions. The primary variant uses the brand orange background for high-visibility icon actions like "Play" or "Start".

### Cards
**`product-card`** — A white card with a 12px radius (`{rounded.md}`) and a subtle drop shadow (`0 2px 12px rgba(0,0,0,0.06)`). The card image occupies the top portion at a 4:3 aspect ratio with rounded top corners. Below the image, the title uses `{typography.title-md}` with standard padding, and the price is rendered in the brand orange. Badges (New, Sale, Coming Soon) are positioned absolutely at the top-left of the card image.

**`kit-module`** — A component card representing a single piece of a build kit. Features a 48px icon, a title, and a description. Uses a white background with a 1px hairline border and a slightly larger shadow (`0 4px 16px rgba(0,0,0,0.08)`) to suggest a physical module you can pick up. Arranged in a responsive grid on product pages.

### Navigation
**`nav-bar`** — A fixed 64px white navigation bar with a soft bottom border. On scroll, gains a subtle shadow (`0 2px 8px rgba(0,0,0,0.08)`). Navigation links are uppercase, 14px, weight 600, with the active link underlined in the brand orange. The bar contains the Kano logo on the left, primary nav links in the center, and utility icons (search, cart, account) on the right.

### Forms
**`text-input`** — A 48px tall input field with a 2px hairline border and 8px radius. On focus, the border switches to the brand orange with no outline. Error state uses the coral-pink (`{colors.error}`) border. Labels use `{typography.caption}` in muted gray above the input.

**`checkbox`** and **`radio-button`** — Small interactive elements with a 2px hairline border. Checked/selected states fill with the brand orange. Checkboxes have a 4px radius; radio buttons are fully round.

### Feedback & Progress
**`progress-bar`** — An 8px tall pill-shaped track in soft gray, filled with the brand orange. Used on build steps and onboarding flows to show completion progress.

**`step-indicator`** — A 32px tall pill-shaped badge used in multi-step flows. Default state is soft gray with dark text. Active state fills with brand orange. Completed steps fill with the accent purple to signal progression without using orange for every state.

### Badges
**`badge-new`** — A coral-pink badge for new products or features. **`badge-sale`** — A warm yellow badge for promotional pricing. **`badge-coming-soon`** — A blue badge for upcoming releases. All use `{typography.badge}` (11px, weight 700, uppercase) with 2px horizontal and 6px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero section reduces padding to 32px; kit modules display in a single column; search bar moves to a full-width overlay |
| Tablet | 768–1024px | Two-column product grid; nav links reduce to icons; hero section uses 48px padding; kit modules display in a 2-column grid; search bar remains in nav but collapses to icon |
| Desktop | 1024–1440px | Three-column product grid; full nav links visible; hero section uses 64px padding; kit modules display in a 3-column grid; search bar is a full-width input in the nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1280px; hero section uses 80px padding; kit modules display in a 4-column grid; additional whitespace around content |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility
- Icon buttons are 40px × 40px minimum
- Navigation links have a minimum tap area of 44px × 44px
- Product card CTAs are 48px tall for easy tapping
- Badges and small indicators are 24px minimum height

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 768px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces padding and stacks CTA buttons vertically on mobile
- Kit module grid collapses from 3 columns to 1 column on mobile
- Footer link columns collapse to a single column on mobile
- Search bar collapses to an icon on tablet and expands to full-width overlay on mobile
- Step indicators hide labels on mobile, showing only numbers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography block uses "GT America" based on the brand's historical design language, but this should be verified against the actual production CSS.
- Hover and active states for all components are inferred from common patterns and may differ from the actual implementation.
- Error styling for forms (error messages, validation icons) could not be extracted.
- Dark mode or high-contrast mode variants are not documented.
- The exact box-shadow values for cards and modules are estimated and may differ from the live site.
- Sub-brand or campaign-specific color variations are not captured.
- The meta theme-color was not set on the live site; the browser chrome color is unknown.
- Animation and transition durations/easings are not documented.
- The exact font stack (including system fallbacks) could not be confirmed from the extracted data.
- Checkout and cart-specific components (quantity selectors, cart items, payment forms) are not documented.
- The brand's icon set and illustration style are not captured in this document.
