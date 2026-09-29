---
version: alpha
name: "Igloo Coolers"
source_url: "https://www.igloocoolers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand born in 1947 that treats coolers as durable sculpture, the palette runs on a near-monochrome axis of #dedede, #e0e0e0, and #121212 — three values that describe a lifetime of use: the pale silver of a well-worn lid, the warm gray of a cooler body that has sat in sun for decades, and the deep near-black of the brand wordmark and structural details. Permanent Marker Pro, a hand-lettered display face with deliberate ink-splash irregularity, sits atop every hero headline and product badge, injecting a permanent-marker informality that contrasts with the otherwise restrained sans-serif body set in Arial. The brand trusts its own history as the primary design move — the founding year appears in the page title, on product pages, and as a persistent visual anchor. Product photography is the dominant color source, with coolers photographed in outdoor settings that introduce blues, greens, and earth tones against the neutral canvas. CTAs use the full #121212 ink as background with white text, a high-contrast binary that reads as industrial and no-nonsense. Cards and surfaces use {rounded.sm} corners — soft enough to feel intentional, tight enough to avoid any "friendly appliance" association. The overall mood is utilitarian with a collector's pride: these are objects meant to be kept, not replaced.

colors:
  primary: "#121212"
  primary-active: "#2a2a2a"
  primary-disabled: "#8a8a8a"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-red: "#c62828"
  badge-blue: "#1565c0"
  badge-green: "#2e7d32"
  badge-yellow: "#f9a825"
  rating-star: "#121212"
  sale: "#c62828"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Permanent Marker Pro', 'Permanent Marker', cursive, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  display-lg:
    fontFamily: "'Permanent Marker Pro', 'Permanent Marker', cursive, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Permanent Marker Pro', 'Permanent Marker', cursive, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Permanent Marker Pro', 'Permanent Marker', cursive, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-outline-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base} 0"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.badge-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  radio:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "2px solid {colors.hairline}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  rating-stars:
    color: "{colors.rating-star}"
    typography: "{typography.body-md}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-disabled:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  spinner:
    color: "{colors.primary}"
    height: 24px
    width: 24px
  spinner-small:
    color: "{colors.primary}"
    height: 16px
    width: 16px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  alert:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"
  alert-error:
    backgroundColor: "#fce4e4"
    textColor: "{colors.badge-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.badge-red}"
  alert-success:
    backgroundColor: "#e8f5e9"
    textColor: "{colors.badge-green}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.badge-green}"
  alert-info:
    backgroundColor: "#e3f2fd"
    textColor: "{colors.badge-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.badge-blue}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action uses full #121212 ink background with white uppercase text at 14px bold. Corners are tight at {rounded.sm} (4px), reinforcing the industrial, no-nonsense brand character. On hover, the background shifts to #2a2a2a for a subtle darkening effect; disabled state uses #8a8a8a with reduced contrast. The 44px height and 12px/24px padding provide a substantial, confident click target.

**`button-secondary`** — An outlined variant with a white background and a 2px solid #121212 border. Maintains the same typography and height as the primary button but reads as a complementary action. Active state fills the background with #f5f5f5 while keeping the border. Used for "Learn More" or "View Details" actions alongside primary CTAs.

**`button-outline`** — A lighter outlined variant using the #dedede hairline color for the border, creating a tertiary action level. Hover and active states shift to the ink border color, providing clear visual hierarchy. Suitable for "Compare" or "Save for Later" actions on product pages.

**`button-pill`** — A compact, fully rounded variant used for filters, tags, and secondary actions in dense layouts. Uses smaller 12px uppercase bold typography and 36px height. The {rounded.full} shape creates a friendly, scannable chip appearance, often used in category navigation strips or product filter bars.

### Navigation
**`top-nav`** — A fixed-height 64px white bar with a single #dedede bottom border. Navigation links use 14px uppercase bold Arial with 12px horizontal padding. Active links gain a 2px bottom border in #121212. The nav contains the Igloo wordmark (typically in #121212), primary navigation items, and a search icon. On mobile, navigation collapses into a hamburger menu with a slide-out drawer.

**`nav-link`** — Uppercase bold 14px links with 8px/12px padding. The active state adds a 2px bottom border in #121212. Hover state uses a subtle background tint or underline, maintaining the brand's direct, no-frills communication style.

**`breadcrumb`** — Small 12px regular weight links in #666666, with the active page rendered in bold #121212. Uses ">" as the separator between levels. Typically appears above product titles on category and product detail pages.

### Cards
**`product-card`** — A white card with {rounded.sm} corners containing a product image, title, price, and rating. The image area uses {rounded.sm} on top corners only, creating a clean visual break. On hover, the card lifts with a subtle box-shadow (0 4px 12px rgba(0,0,0,0.08)). Product badges overlay the image area in the top-left corner.

**`product-badge`** — Small uppercase 11px bold labels with 2px/8px padding and {rounded.xs} corners. Color-coded by type: red (#c62828) for general badges, blue (#1565c0) for "New" labels, and red (#c62828) for sale indicators. These badges sit directly on product images, using white text for maximum readability against any background.

### Forms
**`text-input`** — Standard 44px input fields with white background, 1px #dedede border, and {rounded.sm} corners. Focus state uses a 2px #121212 border. Error state switches to a 2px #c62828 border. Internal padding of 10px/16px provides comfortable text entry. Used across search, checkout, and account forms.

**`select-input`** — Matches text-input styling with a custom dropdown arrow in #121212. The same height, border, and corner treatment ensures visual consistency across all form elements.

**`checkbox`** and **`radio`** — 20px square (checkbox) or circular (radio) controls with 2px #dedede border. Checked state fills with #121212 background. The checked indicator uses white for maximum contrast. Radio buttons use {rounded.full} for the circular shape.

**`toggle`** — A 44px wide, 24px tall pill-shaped toggle with #dedede background. Active state fills with #121212. The 20px circular thumb slides between left and right positions, using white for clear visibility.

### Feedback & Data Display
**`alert`** — Information messages with {rounded.sm} corners, 1px #dedede border, and #f5f5f5 background. Error alerts use a light red background (#fce4e4) with #c62828 text and border. Success alerts use light green (#e8f5e9) with #2e7d32 text. Info alerts use light blue (#e3f2fd) with #1565c0 text. All maintain consistent padding and typography.

**`rating-stars`** — Five-star display using #121212 for filled stars and #dedede for empty stars. Stars are rendered at body-md font size. Half-star ratings use a partial fill approach. Typically appears below product titles on cards and detail pages.

**`pagination`** — Page number buttons with 36px height and width. Active page uses #121212 background with white text. Inactive pages use transparent background with #121212 text. Disabled pages use #8a8a8a. Previous/Next arrows follow the same styling pattern.

### Modals & Overlays
**`modal`** — A white container with {rounded.sm} corners, 24px padding, and a 0 8px 32px rgba(0,0,0,0.12) box-shadow. The overlay uses #000000 at 50% opacity. Modal content follows standard typography hierarchy with a bold title and regular body text. Close button appears in the top-right corner as an icon button.

**`tooltip`** — Small information popups with #121212 background, white text, and {rounded.xs} corners. Uses 12px regular weight typography with 4px/8px padding. Appears on hover for icons, truncated text, and form field labels.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger navigation, stacked product cards, full-width CTAs, reduced hero typography to display-md, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid, expanded navigation with dropdowns, side-by-side product details, hero maintains display-lg |
| Desktop | 1128–1440px | Three-column product grid, full top-nav with all links visible, multi-column footer, hero uses display-xl |
| Wide | > 1440px | Max-width container at 1440px, centered layout with generous margins, four-column product grid on category pages |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons use 40px minimum dimensions
- Form inputs and buttons use 44px height as standard
- Product card tap targets (title, price, add-to-cart) are spaced at least 8px apart
- Navigation links have 12px horizontal padding for comfortable tapping

### Collapsing Strategy
- Top navigation collapses to hamburger menu at < 744px, with full-screen slide-out drawer
- Product filters collapse to accordion panels on mobile, with a "Filter" button triggering the panel
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Product image galleries collapse to single-image carousel with dot indicators on mobile
- Multi-column text layouts (product descriptions, specifications) collapse to single column
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are limited to three values (#dedede, #e0e0e0, #121212) which appear to be the brand's primary structural palette. The extracted list may be missing brand accent colors, seasonal palettes, or promotional colors that exist in images but not in the extracted CSS. The badge colors (#c62828, #1565c0, #2e7d32, #f9a825) are inferred from common e-commerce patterns rather than extracted from the live site.
- Font-family declarations found: Arial, inherit, permanent-marker-pro, sans-serif, serif ! important. The "Permanent Marker Pro" font weight and exact letter-spacing values are estimated based on typical display font behavior. The actual font may have additional weights or stylistic alternates not captured.
- Hover, focus, active, and disabled states for all components are inferred from common patterns rather than extracted from the live site. Actual interaction states may differ.
- Error, success, and info alert colors are not extracted — the values provided are standard implementations that should be verified against the brand's actual design system.
- Box-shadow values, transition durations, and animation timing are not extracted and use standard e-commerce defaults.
- Dark mode support is not confirmed — the brand may or may not have a dark theme.
- The brand's Shopify platform may introduce platform-specific UI elements (cart drawer, checkout buttons, payment icons) that follow Shopify's design system rather than Igloo's brand guidelines.
- Sub-brand or collection-specific color palettes (e.g., "Trailmate", "Marine", "Sport" cooler lines) are not captured in the extracted data.
- Accessibility contrast ratios have not been verified against WCAG standards. The #121212 on #ffffff combination provides strong contrast, but other combinations should be tested.
- The extracted "meta theme-color: (none)" indicates no browser chrome color is set, which may be an oversight in the brand's implementation.
