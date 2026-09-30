---
version: alpha
name: "Pura"
source_url: "https://www.trypura.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pura is a warm, sensory-first brand that lives in the intersection of home fragrance and modern technology. The brand's visual identity is built on a foundation of earthy, muted tones anchored by a deep almost-black ink (`#1d1b1b`) and a soft cream canvas (`#fbf8f5`). This palette creates a calm, sophisticated backdrop that lets the product — scent diffusers and their vibrant fragrance oils — take center stage. The primary accent is a burnished gold (`#cfa363`) that reads as both premium and natural, like honeyed light catching on a ceramic vessel. Supporting accents include a sage green (`#708265`), a dusty rose (`#f1dac8`), and a warm terracotta (`#724d39`), all of which echo the botanical and artisanal qualities of the brand's fragrance notes. The typography system pairs a clean, geometric sans-serif (Apercu) for UI and body text with a classic serif (ITC Garamond) for editorial moments, creating a tension between modern utility and timeless elegance. Buttons and interactive elements use soft rounded corners (`{rounded.sm}`), while cards and containers employ a more generous rounding (`{rounded.md}`) that feels tactile and inviting, like a smooth pebble. The overall mood is one of quiet luxury — the interface never shouts, instead relying on generous whitespace, a restrained color story, and the subtle glow of the product photography to communicate value. The brand's Shopify roots are visible in the clean, card-based product grid and the prominent, pill-shaped search and filter controls.

colors:
  primary: "#cfa363"
  primary-active: "#a6824f"
  primary-disabled: "#f7dfbb"
  ink: "#1d1b1b"
  body: "#4f4c4a"
  muted: "#74716f"
  muted-soft: "#a39c98"
  hairline: "#cec6c2"
  hairline-soft: "#eae5e2"
  canvas: "#fbf8f5"
  surface-soft: "#f4efd1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#708265"
  accent-green-soft: "#c8d3c1"
  accent-rose: "#f1dac8"
  accent-terracotta: "#724d39"
  accent-gold-light: "#d9b582"
  accent-warm-yellow: "#fef9c3"
  accent-amber: "#eab308"
  accent-amber-dark: "#a16207"
  accent-amber-deep: "#714505"
  accent-olive: "#756a4e"
  error: "#ef4444"
  error-soft: "#fee2e2"
  error-strong: "#b91c1c"
  error-deep: "#811414"
  success: "#22c55e"
  warning: "#f97316"
  star-rating: "#cfa363"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'ITC Garamond', 'Georgia', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ITC Garamond', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Apercu', 'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
  section: 80px

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
    textColor: "{colors.muted}"
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
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  icon-button-circle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.primary}"
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
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-info:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-accent:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-best-seller:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Shop Now" actions. It uses the brand's warm gold (`{colors.primary}`) on a white background (`{colors.on-primary}`) with a soft 8px rounding (`{rounded.sm}`). On hover, the background deepens to `{colors.primary-active}`. The disabled state fades to a pale gold (`{colors.primary-disabled}`) with muted text, signaling the action is unavailable.

**`button-secondary`** — A outlined or ghost alternative for less prominent actions like "Learn More" or "View Details". It sits on the cream canvas (`{colors.canvas}`) with a subtle hairline border (`{colors.hairline}`). On active state, the border becomes the full ink color and the background shifts to `{colors.surface-soft}`.

**`button-tertiary-text`** — A text-only button used for inline actions like "Cancel" or "Clear Filters". It carries the primary gold color and underlines on hover, providing a lightweight interactive cue without a container.

**`button-pill-primary`** and **`button-pill-outline`** — Pill-shaped buttons (`{rounded.full}`) used in promotional banners, the newsletter signup, and as quick-add controls. The primary variant uses the gold fill; the outline variant uses a transparent background with a hairline border.

### Cards
**`product-card`** — The core product display unit on the Shopify-powered grid. It has no background fill (inheriting the canvas) and uses a 12px rounding (`{rounded.md}`). The image area is rounded at the top, while the info area below contains the product title (`{typography.title-sm}`), price (`{typography.body-md}`), and color swatches (`{rounded.full}` circles at 24px). The card is designed to let the product photography breathe.

**`review-card`** — A customer review block with a light border (`{colors.hairline-soft}`) and 12px rounding. It contains the star rating (rendered in `{colors.star-rating}`), the reviewer's name, and the review text in `{typography.body-sm}`.

### Navigation
**`top-nav`** — A fixed-height (72px) navigation bar with a cream background (`{colors.canvas}`) and a subtle bottom border. Navigation links are set in `{typography.nav-link}` (uppercase, 14px, weight 500). The active link is indicated by a 2px gold underline. The nav collapses to a hamburger menu on mobile.

**`nav-link-active`** and **`nav-link-inactive`** — Define the active and inactive states for top-level navigation items. Active links are full ink with a gold underline; inactive links are muted (`{colors.muted}`).

### Forms & Inputs
**`text-input`** — Standard text input for forms (email, name, address). It has a white background, 8px rounding, and a hairline border. On focus, the border switches to the primary gold. Error state uses a red border (`{colors.error}`).

**`search-bar-pill`** — The main search input, styled as a pill with a full rounding (`{rounded.full}`). It appears in the header and on the search results page. On focus, the border transitions from hairline to primary gold.

**`select-dropdown`** — A compact dropdown for filtering (e.g., "Sort by", "Scent Type"). It has a 44px height, 8px rounding, and a hairline border.

**`newsletter-input`** and **`newsletter-submit`** — The email signup combo in the footer. The input is a pill with a hairline border; the submit button is a gold pill that sits adjacent to it.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-limited`**, **`badge-best-seller`** — Small, uppercase, pill-shaped badges that overlay product cards. Each uses a distinct background color from the brand palette: green for new, red for sale, amber for limited, and terracotta for best-seller. They are set in 11px bold uppercase type.

### Footer
**`footer`** — A dark section anchored by the deep ink color (`{colors.ink}`) with white text. Links are set in a muted gray (`{colors.muted-soft}`) and transition to full white on hover. The footer contains the newsletter signup, navigation columns, and social links.

### Filtering
**`filter-chip`** and **`filter-chip-active`** — Used in the product listing page for scent notes, price ranges, and other attributes. Inactive chips are outlined with a hairline border; active chips are filled with the primary gold.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top nav collapses to hamburger; hero section stacks text and image; filter chips become a horizontal scrollable strip; footer columns stack vertically. |
| Tablet | 744–1128px | Two-column product grid; top nav remains expanded but with reduced link spacing; hero section uses a 50/50 split; filter sidebar becomes a top bar. |
| Desktop | 1128–1440px | Three-column product grid; full top nav with all links; hero section uses a 60/40 split with larger typography; filter sidebar is persistent. |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero section uses a 70/30 split with display-xl typography. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile.
- Icon buttons are 40px x 40px with a 40px touch area.
- Filter chips are 36px tall with 16px horizontal padding.
- Product card swatches are 24px with a 32px touch area.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu at < 744px. The hamburger icon is a 40px icon button.
- The product filter sidebar collapses to a horizontal chip strip at < 744px, with a "Filter" button that opens a full-screen overlay.
- The hero section stacks vertically at < 744px, with the image taking full width below the text.
- The footer collapses from four columns to a single column at < 744px.
- The product grid collapses from four columns to one column at < 744px.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover States**: While active and disabled states are defined for primary and secondary buttons, hover states for tertiary text buttons, filter chips, and navigation links could not be fully extracted from the live site CSS.
- **Error & Validation Styling**: Error styling for text inputs is defined, but the exact error message typography, iconography, and animation (e.g., shake) are not confirmed.
- **Dark Mode**: No dark mode implementation was detected. The brand may not support it, but if it does, the palette would need significant adjustment (e.g., inverting the canvas and ink).
- **Sub-brand Palettes**: Pura may have sub-brands or seasonal collections (e.g., "Pura Luxe", "Pura Home") with distinct accent colors. These were not observed.
- **Loading & Skeleton States**: The design for loading spinners, skeleton screens, or shimmer animations is not documented.
- **Modal & Overlay Patterns**: The design for modals (e.g., quick-view, size guide) and their scrim opacity is not confirmed.
- **Typography Scale**: The exact font sizes for display-xl and display-lg are inferred from the brand's use of ITC Garamond in hero sections. The actual values may vary.
- **Spacing Scale**: The `section` spacing value (80px) is an estimate based on the generous whitespace observed. The exact value may be 64px or 96px.
- **Component Height Consistency**: The heights for buttons (48px) and inputs (48px) are consistent, but the height for the search bar (48px) and newsletter input (48px) may differ in production.
- **Animation & Transition**: No transition durations or easing curves were extracted. The brand likely uses subtle fades and slides (e.g., 200ms ease-in-out), but this is unconfirmed.
