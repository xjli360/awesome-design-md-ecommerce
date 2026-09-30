---
version: alpha
name: "AverMedia"
source_url: "https://www.avermedia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep indigo #2f3192 powers the brand's primary voltage — a saturated, almost electric blue-violet that appears on the main navigation bar, primary call-to-action buttons, and the hero section's background, giving the streaming-hardware site a confident, tech-forward presence. This distinctive indigo is paired with a secondary blue #374ea3 for hover states and supporting accents, while a bright green #00c31e serves as a live/streaming indicator and status badge, creating a clear semantic color language. The canvas is a warm off-white #f6f6f6 rather than pure white, lending a softer, more approachable feel than typical gaming or streaming brands. Typography runs Arial and Helvetica at modest sizes — body text at 14px (0.875rem) keeps product specs and descriptions dense and scannable, while the generous use of #777777 for secondary text and #aaaaaa for muted labels creates a clear information hierarchy. Product cards use soft rounded corners (`{rounded.md}`) and subtle shadows, while the search bar adopts a pill shape (`{rounded.full}`) that echoes the friendly, accessible tone. The brand's AI.STREAMING tagline signals a shift toward intelligent streaming solutions, reflected in the clean, utilitarian layout that prioritizes product photography and spec sheets over decorative elements.

colors:
  primary: "#2f3192"
  primary-active: "#374ea3"
  primary-disabled: "#d6d1e7"
  ink: "#222222"
  body: "#454545"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#d8d8d8"
  hairline-soft: "#ececec"
  canvas: "#f6f6f6"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  status-live: "#00c31e"
  status-live-active: "#41db00"
  status-error: "#ff5b5b"
  status-warning: "#ffdb00"
  link-default: "#5a91cb"
  link-hover: "#6d9ed1"
  badge-new: "#ffdb7e"
  badge-sale: "#ff5b5b"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    rounded: "{rounded.md}"
    padding: 10px 20px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 40px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-live:
    backgroundColor: "{colors.status-live}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 28px
  button-live-active:
    backgroundColor: "{colors.status-live-active}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "1px solid {colors.status-error}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.1)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "16/9"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginTop: "{spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-live:
    backgroundColor: "{colors.status-live}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination:
    typography: "{typography.button-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  tab-primary:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    padding: "8px 16px"
  tab-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  tab-hover:
    textColor: "{colors.primary-active}"
  dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  dropdown-item:
    padding: "8px 16px"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "6px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-thumb:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  modal:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.15)"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  notification-success:
    backgroundColor: "{colors.status-live}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
  notification-error:
    backgroundColor: "{colors.status-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
  notification-warning:
    backgroundColor: "{colors.status-warning}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "12px 16px"

## Components

### Buttons
**`button-primary`** — The primary action button uses the brand's distinctive indigo #2f3192 as its background, with white text and a subtle 8px rounded corner. On hover, it shifts to the slightly lighter #374ea3, providing a clear interactive state. When disabled, it fades to a muted lavender #d6d1e7 with light gray text, signaling unavailability without visual noise.

**`button-secondary`** — An outlined variant with a white background and indigo border, matching the primary button's height and corner radius. The 2px stroke maintains visual weight parity with the filled primary. Hover state deepens both the border and text color to #374ea3 with a light gray background fill.

**`button-ghost`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Learn More." Hover adds a subtle light gray background for touch feedback without competing with primary actions.

**`button-live`** — A compact pill-shaped button using the bright green #00c31e, reserved exclusively for live streaming status indicators and "Go Live" CTAs. The full rounded shape and small padding make it feel badge-like and urgent. Active state shifts to the brighter #41db00.

### Text Inputs
**`text-input`** — Standard form fields use a white background, 1px hairline border (#d8d8d8), and 8px corner radius. Focus state swaps the border to a 2px indigo stroke with no outline, matching the brand's primary color. Error state uses a red border (#ff5b5b) while maintaining the same structural dimensions.

### Navigation
**`nav-bar`** — The top navigation bar is a solid indigo (#2f3192) strip 64px tall, with uppercase white navigation links in 14px bold Arial. On scroll, the bar transitions to a white background with a subtle drop shadow, and links switch to dark text. Active page links are underlined with a 2px white (or dark) border.

**`nav-link-active`** — Active navigation items are distinguished by a 2px bottom border in the parent bar's text color, creating a clear current-page indicator. Inactive links use a muted gray (#aaaaaa) to de-emphasize secondary pages.

### Cards
**`product-card`** — Product cards are white with a subtle drop shadow (0 1px 3px rgba(0,0,0,0.08)) and 8px rounded corners. Each card contains a 16:9 product image with 6px corner radius, a bold 16px title in #222222, and the price displayed in the brand indigo at 16px bold. Hover elevates the shadow to 0 4px 12px rgba(0,0,0,0.12) for a gentle lift effect.

### Search
**`search-bar`** — The search input is a pill-shaped field (full rounded) with a white background and 1px hairline border. At 44px tall with comfortable 16px horizontal padding, it's large enough for touch interaction but compact enough for the header. Focus state uses a 2px indigo border, matching the text input pattern.

### Hero
**`hero-section`** — Hero areas use the indigo #2f3192 as a full-width background with generous vertical padding (64px). The title uses the largest display type (32px bold white), while the subtitle sits in a lighter gray (#aaaaaa) at 16px. This high-contrast layout ensures the product photography or feature imagery remains the focal point.

### Badges
**`badge-new`** — A warm yellow (#ffdb7e) badge with dark text, used to flag newly released products. The 11px uppercase bold type and 6px horizontal padding keep it compact and legible at small sizes.

**`badge-sale`** — A red (#ff5b5b) badge with white text for sale or discount indicators. Same typography and padding as the new badge, but with a slightly smaller corner radius for visual distinction.

**`badge-live`** — A green pill badge using #00c31e, reserved for live streaming status. The full rounded shape and compact padding make it feel like a real-time indicator light.

### Breadcrumbs
**`breadcrumb`** — Breadcrumb navigation uses 13px gray (#777777) text with the final item bolded in dark (#222222). Items are separated by a forward slash or chevron (not specified in extraction), providing clear hierarchical context for product category pages.

### Pagination
**`pagination`** — Page numbers appear as 13px bold gray text, with the active page highlighted in an indigo background pill (8px corner radius, 4px vertical / 10px horizontal padding). This creates a clear visual anchor for the current page without overwhelming the layout.

### Tabs
**`tab-primary`** — Tab navigation uses 14px bold gray text with 16px horizontal padding. The active tab is underlined with a 2px indigo border and switches to the brand's primary color. Hover state uses the lighter indigo (#374ea3) for subtle feedback.

### Dropdowns
**`dropdown`** — Dropdown menus are white cards with a 1px hairline border and a 4px shadow for depth. Items have 8px vertical padding for comfortable touch targets, and hover adds a light gray (#f3f3f3) background. The 8px corner radius matches the card system.

### Form Controls
**`checkbox`** — Checkboxes use a 2px hairline border with 4px corner radius. Checked state fills the box with indigo and replaces the border with the same color, creating a solid filled square.

**`radio`** — Radio buttons are fully rounded with a 2px hairline border. Checked state shows a 6px indigo inner circle, maintaining the circular metaphor while using the brand color.

**`toggle`** — Toggle switches are 24px tall pill shapes with a gray background. Active state fills with indigo, and the 20px white thumb slides to the right, providing clear on/off visual feedback.

### Progress
**`progress-bar`** — Progress bars use a light gray (#ececec) background track with an indigo fill. The 8px height and full rounded corners create a soft, friendly loading indicator that matches the brand's approachable tone.

### Tooltips
**`tooltip`** — Tooltips appear as dark (#222222) pills with white text, using 12px regular type and 8px corner radius. The compact 4px vertical / 8px horizontal padding keeps them unobtrusive while remaining readable.

### Modals
**`modal`** — Modal dialogs are white cards with 12px corner radius and a 8px shadow for depth. A 50% opacity black overlay dims the background, focusing attention on the modal content. The generous corner radius softens what could otherwise feel like an interruption.

### Notifications
**`notification-success`** — Success notifications use the bright green #00c31e as a full background with white text, creating an immediate positive visual cue. The 8px corner radius and 12px padding provide comfortable reading space.

**`notification-error`** — Error notifications use #ff5b5b with white text, matching the error state of text inputs for visual consistency. Same structural dimensions as success notifications.

**`notification-warning`** — Warning notifications use #ffdb00 with dark text, providing a high-contrast alert that doesn't rely on the brand's primary or error colors.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces top nav, product cards stack vertically, hero text reduces to 24px, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links with "More" dropdown, hero maintains 28px title, search bar remains full-width |
| Desktop | 1128–1440px | Full top nav with all links visible, three-column product grid, hero at 32px title, search bar in header |
| Wide | > 1440px | Max-width container (1440px) centered, four-column product grid, additional whitespace on hero sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Navigation links have 48px minimum touch area (64px bar height provides comfortable spacing)
- Product card tap targets (title, price, image) are at least 48px tall
- Search bar at 44px meets minimum touch target guidelines
- Dropdown items at 40px height (8px padding + 14px text + 8px padding = 30px content + 10px breathing room) — note this is below the 44px recommendation for mobile, consider increasing to 44px for touch devices
- Toggle switches at 24px height are below touch target minimum; consider 32px for mobile

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for full navigation
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Hero section reduces vertical padding from 64px to 32px on mobile
- Footer links collapse from multi-column layout to single-column stacked list below 744px
- Breadcrumbs truncate with ellipsis on mobile, showing only the current page and a "Back" link
- Tab navigation collapses to a horizontal scrollable strip on mobile, with no visible overflow indicator (consider adding fade gradient)
- Search bar collapses to a search icon that expands to full-width input on tap
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Table data (spec sheets) collapses to a stacked card layout on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex color list is heavily weighted toward grays (#f6f6f6, #777777, #ececec, #222222, #f3f3f3, #555555, #aaaaaa, #a6a6a6, #d8d8d8, #f5f5f5, #404040, #c5c5c5, #454545, #2b2b2b) with a few distinctive accents (#2f3192, #374ea3, #00c31e, #ff5b5b, #ffdb00, #5a91cb, #5f3f3f, #6d9ed1, #ffdb7e, #d6d1e7, #003eff, #dad55e, #fffa90, #777620). The brand's true primary (#2f3192) was identified as the most distinctive non-gray color, but the abundance of grays suggests either a minimal design or extraction noise from framework defaults and images.
- Font-family declarations were sparse — only Arial and Helvetica were found at 0.875rem (14px). No custom or web font was detected, which may indicate the site uses a standard system font stack or the extraction missed @font-face declarations. The typography system above assumes Arial as the primary font, but the brand may use a custom font that wasn't captured.
- Hover states for buttons, cards, and links were inferred from common patterns rather than extracted from the live site. The specific transition timing and easing functions are unknown.
- Error states for form inputs (validation messages, error icons) were not extracted. The red #ff5b5b was assumed as the error color based on its presence in the extraction list.
- The meta theme-color tag was absent, meaning the browser chrome/tab color on mobile is not explicitly set. This could be a gap in the extraction or a deliberate omission.
- No dark mode variant was detected. The color palette above assumes a light theme only.
- The extracted list includes colors like #003eff (a bright blue) and #5f3f3f (a dark brown) that don't clearly map to the brand's identity — these may be from third-party widgets, social icons, or stock photography. They were excluded from the palette.
- The green #00c31e and its variant #41db00 are assumed to be live/streaming indicators, but their exact usage context (button backgrounds, status dots, progress fills) was not confirmed.
- The yellow #ffdb00 and its variant #ffdb7e are assumed to be warning and "new" badge colors respectively, but their specific application (badge backgrounds, highlight borders, sale tags) was not extracted.
- The blue #5a91cb and #6d9ed1 are assumed to be link colors, but their exact usage (default vs. visited vs. hover) was not confirmed.
- The purple-gray #d6d1e7 is assumed to be the disabled state for primary buttons, but its exact opacity or overlay behavior is unknown.
- The brown #777620 and yellow-green #dad55e and #fffa90 are unusual and may be from specific product images or promotional banners rather than core design tokens. They were excluded from the palette.
- No animation or transition timing values were extracted. The system assumes 200-300ms ease transitions as a reasonable default.
- The extraction did not capture any box-shadow values, so all shadow definitions are inferred from common e-commerce patterns.
- No specific icon set or SVG styling was extracted. The brand may use custom streaming-related icons (cameras, microphones, live indicators) that aren't reflected in the design system.
- The product card aspect ratio (16:9) is assumed based on typical webcam product photography, but the actual ratio may vary by product type.
- The navigation bar's scroll behavior (transition from indigo to white) is inferred from common patterns and may differ from the actual implementation.
- No footer-specific colors or layouts were extracted beyond the general color palette. The footer design above is a reasonable assumption based on the brand's minimal aesthetic.
