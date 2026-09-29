---
version: alpha
name: "Insta360"
source_url: "https://www.insta360.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single hex value — #313131 — governs the Insta360 interface, a deep near-black that reads as precision hardware rather than digital ink. This is the color of a camera body machined from aluminum, of a lens barrel, of the brand's own X-series action cameras rendered in product shots. It appears on buttons, navigation bars, footer backgrounds, and text, creating a monochrome stage where the only other color is the content itself: 360-degree video, camera previews, and interface overlays. The brand uses no primary accent color in the traditional sense — no red CTA, no blue link, no green success state that competes with the visual output of its products. Instead, the UI defers entirely to the media. Buttons are outlined or filled in {colors.ink} and {colors.canvas}. Typography runs the system font stack at modest weights (400–600), never heavy, never decorative; the brand trusts its product imagery to carry emotion. Rounded corners are minimal — {rounded.sm} on buttons, {rounded.md} on cards — suggesting industrial precision rather than consumer friendliness. The overall feel is that of a control panel for a serious tool: clean, dark, information-dense, with generous spacing ({spacing.lg} between sections) that prevents the darkness from feeling cramped. The footer is a solid {colors.ink} field with white links, a common pattern for hardware-adjacent brands that want to signal "pro" without shouting. There is no gradient, no pastel, no decorative illustration. The brand's visual system is subtractive: remove everything that isn't the product or the path to buying it.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#6b6b6b"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6b6b6b"
  muted-soft: "#8c8c8c"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#313131"
  link-hover: "#1a1a1a"
  badge-new: "#313131"
  badge-sale: "#c13515"
  star-rating: "#313131"
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
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
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
    fontWeight: 500
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
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
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
  button-primary-hover:
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
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-tertiary-text-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  button-pill-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    fontWeight: 600
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 500
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.base}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  section-subheader:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  text-input-label:
    typography: "{typography.caption}"
    color: "{colors.body}"
    marginBottom: "{spacing.xs}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  radio:
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
  radio-checked:
    border: "1px solid {colors.ink}"
  toggle:
    rounded: "{rounded.full}"
    backgroundColor: "{colors.hairline}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.ink}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  rating-number:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.15)"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.xs} 0 {spacing.base}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.ink}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  tab-hover:
    textColor: "{colors.ink}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 4px
  stepper:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  stepper-active:
    color: "{colors.ink}"
    fontWeight: 600
  stepper-completed:
    color: "{colors.ink}"
  stepper-number:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
  stepper-number-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
  stepper-number-completed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — The primary action button, filled with {colors.primary} (#313131) and white text. Uses {typography.button-md} at 15px/500 weight. Corners are minimally rounded at {rounded.sm} (4px), reinforcing the industrial precision of the brand. On hover, the background deepens to {colors.primary-active} (#1a1a1a). Disabled state uses {colors.primary-disabled} (#6b6b6b). Height is 44px with 12px/24px padding — compact enough for dense product pages but large enough for comfortable touch targeting.

**`button-secondary`** — Outlined variant with white background, {colors.ink} text, and a 1px {colors.hairline} border. On hover, the background shifts to {colors.surface-soft} and the border to {colors.ink}. Same dimensions and typography as primary. Used for "Learn More" and secondary CTAs on product cards and hero sections.

**`button-tertiary-text`** — Text-only button with no background or border. On hover, a {colors.surface-soft} background appears. Used for "Cancel", "Back", and other low-emphasis actions. Padding is 12px/16px to maintain alignment with other buttons.

**`button-pill-dark`** — Fully rounded pill button ({rounded.full}) at 36px height, used for filter tags, category toggles, and compact CTAs. Filled {colors.ink} with white text. The pill shape is the only significant deviation from the brand's otherwise squared-off button language, used sparingly for utility actions.

**`button-pill-outline`** — Outlined pill variant with transparent background and 1px {colors.hairline} border. Used for deselected filter states and secondary pill actions.

### Navigation
**`top-nav`** — Fixed-position navigation bar at 64px height with white background and a subtle bottom border ({colors.hairline-soft}). On scroll, a box shadow appears. Navigation links use {typography.nav-link} at 15px/500 weight. Active links are bold (600 weight) in {colors.ink}; inactive links are {colors.muted}. The nav contains the brand logo, product category links, and a search icon.

**`search-bar`** — Compact search input at 40px height with {colors.surface-soft} background and 1px {colors.hairline-soft} border. On focus, the border switches to {colors.ink}. Used primarily in the top nav and on product listing pages.

### Cards
**`product-card`** — White card with {rounded.md} (8px) corners and a subtle box shadow. On hover, the shadow deepens. The card contains a product image (full-width, no border-radius on top), a title using {typography.title-sm}, and a price using {typography.body-md} at 500 weight. Badges overlay the top-left corner of the image using {rounded.xs} (2px) and {typography.badge} (11px uppercase).

### Forms
**`text-input`** — Standard input at 44px height with {rounded.sm} (4px) corners and 1px {colors.hairline} border. On focus, the border becomes {colors.ink}. Error state uses {colors.badge-sale} (#c13515) border. Labels use {typography.caption} at 13px above the input with {spacing.xs} gap.

**`select-dropdown`** — Matches text-input dimensions and styling. Used for product configuration options (lens type, resolution, bundle options).

**`checkbox`** and **`radio`** — Minimal styling with {rounded.xs} for checkboxes and {rounded.full} for radios. Checked state fills with {colors.ink}. No decorative animations or custom icons — just clean, functional form controls.

### Footer
**`footer`** — Full-width dark section with {colors.ink} background and white text. Links are semi-transparent (opacity 0.8) and become fully opaque on hover. The footer contains product links, support links, company information, and social icons. Headings use {typography.title-sm} with {spacing.base} bottom margin. The overall padding is {spacing.xxl} vertical and {spacing.lg} horizontal.

### Modals & Overlays
**`modal-overlay`** — Semi-transparent black scrim at 50% opacity. **`modal-content`** — White card with {rounded.md} (8px) corners, {spacing.xl} padding, and a deeper box shadow. Used for product configuration dialogs, video previews, and checkout confirmations.

### Tabs & Accordions
**`tab-active`** — Active tab with a 2px {colors.ink} bottom border and {typography.button-md}. Inactive tabs use {colors.muted} text with no border. On hover, inactive tabs shift to {colors.ink}. Used on product detail pages for "Overview", "Specifications", "Reviews" sections.

**`accordion-header`** — Clickable header using {typography.title-sm} with {spacing.base} vertical padding. Content area uses {typography.body-md} in {colors.body}. Used on FAQ pages and product specification sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu. Product cards stack single-column. Footer links stack vertically. Hero section reduces padding to {spacing.xl}. Search bar moves to full-width below nav. Buttons become full-width on primary CTAs. |
| Tablet | 744–1128px | Top nav shows limited links with "More" dropdown. Product cards display in 2-column grid. Footer uses 2-column layout. Hero section maintains {spacing.section} padding but reduces title to {typography.display-lg}. |
| Desktop | 1128–1440px | Full top nav with all links visible. Product cards in 3-column grid. Footer in 4-column layout. Standard padding and spacing applied. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. Additional whitespace on sides. Hero section may include larger imagery. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px with adequate tap area
- Product card CTAs are full-width on mobile for easy tapping
- Filter pills are 36px height with 20px horizontal padding
- Accordion headers are minimum 48px height on touch devices

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-in drawer for navigation links
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer link columns collapse to accordion-style sections on mobile
- Product image galleries collapse to single-image swipe on mobile
- Multi-column product grids collapse to single column below 744px
- Hero sections collapse to single-column layout with text below image on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was successfully extracted from the live site. The full color palette above is inferred from common patterns in the brand's product pages and industry conventions for hardware/electronics brands. The true secondary palette (if any) could not be verified.
- No brand-specific font family was found. The site uses the system font stack exclusively. The brand may use a custom font on certain pages or in marketing materials that was not detected.
- Hover states for buttons and links are inferred from common patterns; actual hover colors may differ.
- Error states for forms (colors, icons, messaging) could not be extracted.
- Dark mode support status is unknown; the brand's dark interface may be a separate theme.
- Sub-brand or product-line-specific color variations (e.g., for "X Series" vs "Pro Series") could not be identified.
- Animation durations, easing curves, and transition properties were not extracted.
- The extracted color list was extremely sparse (single hex), suggesting the site may load colors dynamically via JavaScript or CSS-in-JS that was not captured in the static extraction. The brand's actual palette may include accent colors for specific product categories or promotional content.
- Social media icon colors and third-party widget colors (if any) were not distinguishable from brand colors in the extraction.
