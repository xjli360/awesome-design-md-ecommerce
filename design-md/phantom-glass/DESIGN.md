---
version: alpha
name: "Phantom Glass"
source_url: "https://www.phantom.glass"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the tension between near-black obsidian and a single blood-red accent — #191919 as the infinite void of a turned-off screen, #a42121 as the alert, the heartbeat, the warning light that says this glass is alive. The extracted palette reads like a hardware spec sheet: #101010 for deepest shadow, #5f5f5f and #d6d6d6 for the graduated greys of a precision-machined edge, #e7ff14 as a neon-yellow jolt that appears in badges and highlights, and #1a7ac4 / #67b2ff as the cool blue of a tempered surface under studio lighting. The brand's typography stack splits between DM Sans (the clean, geometric sans for product names and navigation) and Playfair Display (the serif for hero headlines that want to feel like engraved steel). Every corner is either razor-sharp at `{rounded.none}` or softly radiused at `{rounded.sm}` — there is no pill shape, no friendliness. The canvas is `#ffffff` but the real canvas is `#191919`: dark mode is the default, light mode is the exception. Product cards float on `{colors.surface-card}` with `{colors.hairline}` borders that feel like the edge of a screen protector. The primary CTA is `{colors.primary}` (#a42121) on `{colors.on-primary}` (#ffffff), a red that reads as urgency, not warmth — this is a brand that sells protection, not comfort.

colors:
  primary: "#a42121"
  primary-active: "#8a1a1a"
  primary-disabled: "#d48a8a"
  ink: "#191919"
  body: "#5f5f5f"
  muted: "#9ca3af"
  muted-soft: "#d6d6d6"
  hairline: "#e5e7eb"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-yellow: "#e7ff14"
  accent-blue: "#1a7ac4"
  accent-blue-light: "#67b2ff"
  dark-canvas: "#101010"
  dark-surface: "#191919"
  dark-hairline: "#2a2a2f"
  error: "#a23026"
  link: "#007eff"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  badge:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  hero-subtitle:
    fontFamily: "'DM Sans', -apple-system, BlinkMacSystemFont, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 10px
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
  section: 72px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-dark-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
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
  nav-bar-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.dark-hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.muted-soft}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.dark-hairline}"
  product-card-dark-hover:
    border: "1px solid {colors.muted}"
  hero-section:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-feature:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.dark-hairline}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.dark-hairline}"
    height: 1px
  rating-stars:
    color: "{colors.accent-yellow}"
    size: 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.6)"
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-card-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action on a light canvas. Uses `#a42121` as a confident, urgent red that demands attention without feeling aggressive. On hover, it deepens to `#8a1a1a`. The disabled state fades to `#d48a8a`, signaling the action is unavailable. All primary buttons use `{rounded.sm}` (6px) — a subtle radius that feels precise, not friendly.

**`button-secondary`** — An outlined button for secondary actions on light backgrounds. White fill with `#191919` text and a `#e5e7eb` border. On hover, the background shifts to `#f0f0f0` and the border to `#d6d6d6`. Used for "Learn More" and "Compare" actions.

**`button-ghost`** — A text-only button with no background or border. Used for tertiary actions like "Cancel" or "Skip". On hover, the text remains `#191919` but the cursor signals interactivity.

**`button-dark`** — The primary button for dark-mode sections. Uses `#191919` fill with white text. On hover, it shifts to `#101010`. Used on hero sections and dark product detail pages.

**`button-accent-yellow`** — A high-visibility accent button using `#e7ff14`. Used for promotional badges, limited-time offers, and "Add to Cart" on product cards where the red primary would compete with other red elements. Text is `#191919`.

**`button-accent-blue`** — A secondary accent button using `#1a7ac4`. Used for support links, warranty registration, and "Find My Device" actions. Text is white.

### Text Inputs
**`text-input`** — A standard text input with white background, `#191919` text, and a `#e5e7eb` border. On focus, the border switches to `#191919` for clear visual feedback. Error state uses `#a23026` border. Height is 48px with 12px/16px padding for comfortable typing.

**`select-input`** — Matches the text input in dimensions and styling. Used for dropdowns like device model selection and screen protector size.

### Navigation
**`nav-bar`** — A 64px fixed navigation bar with white background and a subtle `#f0f0f0` bottom border. Navigation links use `{typography.nav-link}` (14px, 500 weight, uppercase with 0.5px letter spacing). Active links show a 2px `#a42121` bottom border. In dark mode (`nav-bar-dark`), the background becomes `#191919` with a `#2a2a2f` border.

**`nav-link-active`** — Active navigation state with `#a42121` text and a 2px red underline. Inactive links use `#9ca3af` muted text.

### Cards
**`product-card`** — A product card with white background, `#e5e7eb` border, and `{rounded.sm}` (6px). On hover, the border shifts to `#d6d6d6` and a subtle shadow appears. In dark mode (`product-card-dark`), the background is `#191919` with a `#2a2a2f` border.

### Badges
**`badge-new`** — A yellow (`#e7ff14`) badge for new products. Uses uppercase 11px bold type with 0.5px letter spacing. `{rounded.xs}` (2px) for a sharp, technical feel.

**`badge-sale`** — A red (`#a42121`) badge for sale items. Same typography and radius as the new badge.

**`badge-feature`** — A blue (`#1a7ac4`) badge for featured products or warranty badges.

### Hero
**`hero-section`** — A full-width hero section with `#101010` background and white text. Uses `{typography.display-xl}` (Playfair Display, 48px, 700 weight) for the headline and `{typography.hero-subtitle}` (DM Sans, 18px, 400 weight) for the subtitle. Padding is 72px top/bottom and 24px sides.

### Search
**`search-bar`** — A standard search input with white background and `#e5e7eb` border. In dark mode (`search-bar-dark`), the background becomes `#191919` with a `#2a2a2f` border. Height is 44px with 10px/16px padding.

### Footer
**`footer`** — A dark footer with `#101010` background and white text. Links use `#d6d6d6` with hover state to white. Padding is 48px top/bottom and 24px sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Product cards stack vertically. Navigation collapses to hamburger menu. Hero text reduces to 32px. Buttons become full-width. Footer links stack. |
| Tablet | 744–1128px | Two-column product grid. Navigation shows 4-5 links. Hero text at 40px. Sidebar filters appear. |
| Desktop | 1128–1440px | Three-column product grid. Full navigation visible. Hero text at 48px. Multi-column footer. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px. Hero text at 52px. Additional whitespace. |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 44px for mobile touch targets.
- Icon buttons are 40x40px with adequate spacing.
- Navigation links have 48px tap targets on mobile.
- Product card CTAs are minimum 48px tall.

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px.
- Product filters collapse to a "Filter" button that opens a modal on mobile.
- Footer columns collapse to a single column on mobile.
- Hero sections reduce padding from 72px to 40px on mobile.
- Product image galleries switch from row to single-image swipe on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; actual extracted hover data was not available.
- Error styling for forms (error messages, validation icons) is based on the extracted `#a23026` error color but exact implementation details are unknown.
- Dark mode color values for `dark-canvas`, `dark-surface`, and `dark-hairline` are inferred from the extracted `#101010`, `#191919`, and `#2a2a2f` colors; full dark mode palette may include additional tones.
- The extracted color list includes several blues (`#1a7ac4`, `#67b2ff`, `#007eff`) that may be checkout-widget or social-icon colors rather than brand colors. The primary red (`#a42121`) is the most distinctive brand signal.
- Font weights for DM Sans and Playfair Display are assumed based on common usage; exact weight values from the live site were not extracted.
- Spacing values for `section` (72px) and component padding are estimated from common e-commerce patterns; exact extracted values were not available.
- The `#e7ff14` yellow appears in badges and highlights but its exact usage context (limited-time offers, new products, or sale indicators) is inferred.
- No data was extracted for: animation durations, transition easings, box-shadow values, z-index layers, or focus-visible styles.
- The brand may use additional fonts not captured in the extracted list (e.g., for icons or special characters).
- No sub-brand or variant-specific color palettes were extracted (e.g., for Phantom Glass Pro, Phantom Glass Edge, etc.).
