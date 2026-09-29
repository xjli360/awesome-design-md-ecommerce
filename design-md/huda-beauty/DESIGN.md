---
version: alpha
name: "Huda Beauty"
source_url: "https://hudabeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bold, glamorous, and unapologetically maximalist beauty brand that commands attention through high-contrast color, sculptural typography, and a deep sense of luxury. The brand’s foundation is a stark white canvas (`{colors.canvas}`) that amplifies the intensity of its signature dark ink (`{colors.ink}`: #313131), a near-black that appears in headlines, product descriptions, and the fine print of ingredient lists. This is not a soft, muted palette; the `{colors.muted}` (#6a6a6a) and `{colors.muted-soft}` (#929292) tones serve as quiet supporting players, allowing the primary voltage of the brand—a rich, warm pink—to dominate every CTA, badge, and promotional banner. The `{colors.primary}` (#e91e63) is a confident, saturated rose that feels both feminine and powerful, with an active state (`{colors.primary-active}`: #c2185b) that deepens the intensity on hover. The `{colors.hairline}` (#dddddd) and `{colors.hairline-soft}` (#ebebeb) provide delicate separation between product cards and editorial content, while the `{colors.surface-soft}` (#f7f7f7) and `{colors.surface-card}` (#ffffff) create a clean, layered hierarchy. The brand’s typography relies on a system-native stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif`) that feels crisp and modern, with display sizes ranging from 28px to 18px in weights that balance readability with editorial flair. Every corner is softened—from the `{rounded.sm}` (8px) on buttons to the `{rounded.lg}` (20px) on product cards—creating a tactile, approachable feel that contrasts with the high-glamour imagery. The overall effect is a brand that feels both aspirational and accessible: a beauty empire built on precision, confidence, and the belief that makeup is a form of self-expression.

colors:
  primary: "#e91e63"
  primary-active: "#c2185b"
  primary-disabled: "#f8bbd0"
  ink: "#313131"
  body: "#3f3f3f"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  star-rating: "#313131"
  scrim: "#000000"
  success: "#4caf50"
  error: "#f44336"
  warning: "#ff9800"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.star-rating}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  accordion-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  dropdown-item-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
  swatch:
    rounded: "{rounded.full}"
    height: 32px
  swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    border: "2px solid {colors.ink}"
  swatch-ring:
    rounded: "{rounded.full}"
    height: 40px
    border: "2px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature rose pink (`{colors.primary}`) with white text. Uses an 8px rounded corner (`{rounded.sm}`) and a compact 44px height with 12px vertical and 24px horizontal padding. The active state (`button-primary-active`) deepens to `{colors.primary-active}` (#c2185b) for tactile feedback, while the disabled state (`button-primary-disabled`) fades to a soft pink (`{colors.primary-disabled}`: #f8bbd0) with white text, signaling non-interactivity. Typography is set in `{typography.button-md}` (14px, weight 600, uppercase) for a confident, editorial feel.

**`button-secondary`** — An outlined alternative to the primary button, using a white background (`{colors.canvas}`) with dark ink text (`{colors.ink}`) and a 1px solid hairline border (`{colors.hairline}`). Maintains the same 44px height and 8px rounded corners as the primary variant. On hover/active, the background shifts to `{colors.surface-soft}` (#f7f7f7) and the border darkens to `{colors.ink}`, creating a subtle but clear state change.

**`button-tertiary-text`** — A text-only button with no background or border, using the primary rose pink (`{colors.primary}`) for text. Used for secondary actions like "View All" or "Learn More" within content sections. Inherits the same uppercase button typography for consistency.

**`button-pill-primary`** — A fully pill-shaped variant (`{rounded.full}`) of the primary button, used for promotional banners, sale tags, and compact CTAs. Uses smaller typography (`{typography.button-sm}`: 12px, weight 600, uppercase) and tighter padding (8px vertical, 20px horizontal) for a more contained footprint.

### Cards
**`product-card`** — The primary container for product listings, featuring a white background (`{colors.canvas}`) with large 20px rounded corners (`{rounded.lg}`). On hover, a subtle box shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card, providing a clear interactive signal. The card image area uses top-only rounding (`{rounded.lg} {rounded.lg} 0 0`) to maintain a clean edge where the image meets the content.

**`product-card-title`** — Product names are set in `{typography.title-sm}` (14px, weight 600) in dark ink (`{colors.ink}`), ensuring strong readability at small sizes.

**`product-card-price`** — Pricing information uses `{typography.body-sm}` (14px, weight 400) in muted gray (`{colors.muted}`), creating a clear visual hierarchy below the product name.

**`product-card-rating`** — Star ratings and review counts are displayed in `{typography.caption}` (12px, weight 400) using the dark ink color (`{colors.star-rating}`), matching the product title for visual consistency.

**`product-card-badge`** — Promotional badges (e.g., "NEW", "SALE", "BESTSELLER") are rendered as small, sharp-cornered pills with a primary pink background (`{colors.primary}`) and white text. Uses `{typography.badge}` (11px, weight 700, uppercase) with tight padding (2px vertical, 6px horizontal) and 4px rounded corners (`{rounded.xs}`).

### Navigation
**`top-nav`** — The main site navigation bar, fixed at 72px height with a white background (`{colors.canvas}`). Navigation links use `{typography.nav-link}` (14px, weight 600, uppercase) in dark ink, with an active state indicated by a 2px solid primary pink underline (`{colors.primary}`). Inactive links are rendered in muted gray (`{colors.muted}`) to de-emphasize secondary pages.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`) and 44px height. On focus, the background shifts to white and a 1px solid primary pink border (`{colors.primary}`) appears, providing a clear active state. Typography uses `{typography.body-sm}` (14px, weight 400) for placeholder and entered text.

### Forms
**`newsletter-input`** — A pill-shaped email input (`{rounded.full}`) with a white background, 44px height, and 10px vertical / 16px horizontal padding. Uses `{typography.body-sm}` for placeholder text. The adjacent submit button (`newsletter-submit`) is a pill-shaped primary pink button with `{typography.button-sm}` (12px, weight 600, uppercase) and matching 10px/20px padding.

**`quantity-selector`** — A compact, horizontally laid-out control with a soft gray background (`{colors.surface-soft}`), 36px height, and 8px rounded corners (`{rounded.sm}`). The increment/decrement buttons are transparent with dark ink icons, maintaining a clean, minimal appearance.

**`dropdown`** — A standard select dropdown with a white background, 8px rounded corners, and a 1px solid hairline border (`{colors.hairline}`). Hovered items use `{colors.surface-soft}` background, while selected items use the primary pink (`{colors.primary}`) with white text for clear visual feedback.

### Footer
**`footer`** — The site footer uses a dark ink background (`{colors.ink}`) with white text for maximum contrast. Footer links are rendered in muted gray (`{colors.muted-soft}`: #929292) using `{typography.link}` (14px, weight 500), and shift to white on hover for clear interactivity. The newsletter signup form within the footer uses the same pill-shaped input and button components described above.

### Swatches
**`swatch`** — Color swatches for product variants (e.g., lipstick shades, eyeshadow palettes) are rendered as 32px circles (`{rounded.full}`). The selected state adds a 2px solid dark ink border (`{colors.ink}`) around the swatch. A larger ring variant (`swatch-ring`) at 40px with a 2px hairline border (`{colors.hairline}`) is used for swatch previews in the product detail view.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack in single column (full width); hero banner reduces to 28px display text; search bar moves to persistent bottom bar; footer links stack vertically; quantity selector becomes full-width; swatches reduce to 28px diameter |
| Tablet | 744–1128px | Top nav shows limited links (Shop, Explore, About); product cards display in 2-column grid; hero banner uses 24px display text; search bar remains in top nav but collapses to icon; footer uses 2-column layout |
| Desktop | 1128–1440px | Full top nav with all links visible; product cards in 3-column grid; hero banner at full 28px display text; search bar expanded with placeholder text; footer uses 4-column layout |
| Wide | > 1440px | Maximum content width of 1440px with centered layout; product cards in 4-column grid; hero banner may include full-width imagery; additional whitespace around all sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44px height for mobile accessibility
- Icon buttons and swatches are at least 36px in diameter for reliable tapping
- Quantity selector buttons are 36px tall with adequate spacing between increment/decrement
- Dropdown items have a minimum height of 44px for easy selection on touch devices

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer for full navigation
- Search bar collapses to a search icon on mobile, expanding to full-width overlay on tap
- Product filters collapse to a bottom sheet or modal on mobile, with a "Filter" button trigger
- Footer sections collapse to accordion-style expandable panels on mobile, with the newsletter signup remaining visible
- Product description sections (details, ingredients, how to use) collapse to accordion tabs on all breakpoints
- Secondary navigation (category strips, sub-menus) collapses to horizontal scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all interactive components could not be fully extracted; the above represents best-effort based on common patterns
- Error styling for form inputs (validation messages, error borders) was not reliably captured from the live site
- Sub-brand palettes (e.g., Huda Glow, Huda Matte, limited edition collections) were not analyzed and may introduce additional accent colors
- Dark mode styling is not present on the live site and has not been defined
- Animation and transition timings (ease-in-out durations, spring curves) were not extracted
- Specific iconography (SVG paths, stroke widths, icon sizes) was not cataloged
- Typography scale for mobile (smaller font sizes, adjusted line heights) was not reliably extracted
- Color contrast ratios for accessibility compliance (WCAG AA/AAA) have not been verified
- Shadow tokens (box-shadow values for cards, modals, dropdowns) were not fully extracted beyond the product card hover state
- Loading states (skeleton screens, spinner designs) were not captured
- Modal and overlay component styling (backdrop, close button, animation) was not extracted
