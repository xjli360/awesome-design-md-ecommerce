---
version: alpha
name: "Digital Storm"
source_url: "https://www.digitalstorm.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-performance PC builder that communicates through dark, machined surfaces and a single accent — #313131, a near-black charcoal that serves as both background and primary color, creating a visual environment closer to a server room than a retail storefront. The brand's design language is defined by absence: no hero gradients, no lifestyle photography bleeding into text, no decorative flourishes. Every pixel is either structural (grid lines at {colors.hairline}, card borders at {colors.hairline-soft}) or informational (spec badges, configurator steps, price tags). Typography runs system-native — the stack is -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Noto Sans, Helvetica Neue, Arial, sans-serif — with no custom typeface investment, signaling that the brand's identity lives in hardware photography and technical copy rather than letterforms. Buttons are sharp-cornered ({rounded.sm} ~4px), inputs are flat rectangles with no shadow, and the configurator UI uses a two-column layout where the left pane (options) is {colors.surface-soft} and the right pane (preview) is {colors.canvas}. The checkout flow is the only place where color shifts — a lighter {colors.surface-card} background with {colors.primary} (#313131) used sparingly for "Add to Cart" and "Configure" CTAs. The overall effect is industrial, no-nonsense, and deeply technical: a design system built for enthusiasts who want to see the specs, not the brand.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#6b6b6b"
  ink: "#1a1a1a"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#d0d0d0"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#e53935"
  badge-sale: "#43a047"
  rating-star: "#ffb300"
  link: "#1565c0"
  link-visited: "#6a1b9a"
  error: "#d32f2f"
  success: "#388e3c"
  warning: "#f57c00"
  info: "#1976d2"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.47
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: -0.25px

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
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-lg-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  button-sm-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
    height: 32px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-item:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 64px
  nav-bar-item-active:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.canvas}"
  nav-bar-item-hover:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.canvas}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-display}"
    marginTop: "{spacing.xs}"
  product-card-specs:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    marginTop: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-spec:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
    marginTop: "{spacing.md}"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg}"
    rounded: "{rounded.md}"
  configurator-preview:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.lg}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  configurator-step:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  configurator-step-active:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  configurator-step-complete:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.success}"
  configurator-step-number:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    width: 24px
    height: 24px
  configurator-step-number-complete:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
  configurator-step-number-inactive:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
  link-inline:
    color: "{colors.link}"
    typography: "{typography.link}"
  link-inline-visited:
    color: "{colors.link-visited}"
  link-inline-hover:
    textDecoration: underline
  alert-error:
    backgroundColor: "#fdecea"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.error}"
  alert-success:
    backgroundColor: "#e8f5e9"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.success}"
  alert-warning:
    backgroundColor: "#fff3e0"
    textColor: "{colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.warning}"
  alert-info:
    backgroundColor: "#e3f2fd"
    textColor: "{colors.info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.info}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 16px rgba(0, 0, 0, 0.15)"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    width: 32px
    height: 32px
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    width: 18px
    height: 18px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    width: 18px
    height: 18px
  radio-checked:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    width: 44px
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    width: 20px
    height: 20px
  pagination-item:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  pagination-item-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  breadcrumb-item:
    color: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-item-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"
    animation: "pulse 1.5s infinite"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Configure", and "Buy Now". Rendered in {colors.primary} (#313131) with white text, {rounded.sm} corners, and 44px height. On hover, shifts to {colors.primary-active} (#1a1a1a). Disabled state uses {colors.primary-disabled} (#6b6b6b) with no hover change.
**`button-secondary`** — An outlined alternative for secondary actions like "Compare" or "Save for Later". White background with {colors.ink} text and a 1px {colors.hairline} border. Active state swaps border to {colors.primary}. Hover fills background with {colors.surface-soft}.
**`button-tertiary-text`** — A text-only button for low-emphasis actions like "Cancel" or "Learn More". Transparent background, {colors.primary} text, no border. Hover adds underline.
**`button-lg-cta`** — A larger, more prominent CTA used in hero sections and landing pages. Same color scheme as `button-primary` but at 56px height with {typography.button-lg} and wider padding (16px 32px).
**`button-sm-outline`** — A compact outlined button for inline actions like "Apply Filter" or "Reset". 32px height, {typography.button-sm}, 1px {colors.primary} border. Hover fills background with {colors.primary} and text becomes white.

### Navigation
**`nav-bar`** — The top-level site navigation, a dark strip at {colors.ink} (#1a1a1a) spanning full width at 64px height. Items use {typography.nav-link} (15px, 600 weight) in white. Active item has a 2px white bottom border. Hover state adds a subtle white overlay at 10% opacity.
**`nav-bar-item`** — Individual navigation links with horizontal padding of {spacing.base}. No background in default state. Active state uses `nav-bar-item-active` with bottom border indicator.
**`breadcrumb-item`** — Secondary navigation for product category pages. Uses {typography.caption} in {colors.muted} with a separator character between items. Active (current page) item uses {colors.ink}. Separators are {colors.muted-soft} with 4px horizontal margin.

### Cards
**`product-card`** — The core content container for product listings. White background, {rounded.md} (8px) corners, 1px {colors.hairline-soft} border, 16px padding. Hover elevates with a subtle shadow (0 2px 8px rgba(0,0,0,0.08)) and border shifts to {colors.hairline}. Contains an image area at 4:3 aspect ratio, title at {typography.title-sm}, price at {typography.price-display} (22px, 700 weight), and spec list at {typography.caption} in {colors.muted}.
**`configurator-panel`** — The left-side options panel in the PC configurator. {colors.surface-soft} background, {rounded.md} corners, 24px padding. Contains step groups (`configurator-step`) that are white cards with 1px {colors.hairline-soft} borders. Active step gets a {colors.primary} border. Completed step gets a {colors.success} border and slightly darker background.
**`configurator-preview`** — The right-side preview panel showing the configured system. White background, {rounded.md} corners, 24px padding, 1px {colors.hairline-soft} border. Displays a live-updating image of the selected components and a running total price.

### Forms
**`text-input`** — Standard single-line text input for search, filters, and form fields. White background, {rounded.sm} (4px) corners, 44px height, 10px 12px padding, 1px {colors.hairline} border. Focus state swaps border to {colors.primary}. Error state uses {colors.error} border.
**`select-input`** — Dropdown selector for options like "Sort By" or "Filter By". Same dimensions and styling as `text-input` but with a custom dropdown arrow in {colors.muted}.
**`textarea`** — Multi-line text input for contact forms or support requests. Same styling as `text-input` but with 12px padding on all sides and no fixed height.
**`checkbox`** — 18px square checkbox with {rounded.xs} (2px) corners. White background, 1px {colors.hairline} border. Checked state fills with {colors.primary} and shows a white checkmark.
**`radio`** — 18px circular radio button with {rounded.full} corners. White background, 1px {colors.hairline} border. Checked state shows a {colors.primary} dot on white background.
**`toggle`** — 44x24px pill-shaped toggle switch. Default state is {colors.hairline-soft}. Active state fills with {colors.primary}. The 20px circular knob is white.

### Alerts & Feedback
**`alert-error`** — Error notification with light red background (#fdecea), {colors.error} (#d32f2f) text, and a 1px {colors.error} border. Uses {typography.body-sm} and {rounded.sm} corners.
**`alert-success`** — Success notification with light green background (#e8f5e9), {colors.success} (#388e3c) text, and a 1px {colors.success} border.
**`alert-warning`** — Warning notification with light orange background (#fff3e0), {colors.warning} (#f57c00) text, and a 1px {colors.warning} border.
**`alert-info`** — Informational notification with light blue background (#e3f2fd), {colors.info} (#1976d2) text, and a 1px {colors.info} border.
**`tooltip`** — Small floating label for UI hints. Dark background ({colors.ink}), white text, {rounded.xs} (2px) corners, 4px 8px padding. Appears on hover with a 200ms delay.
**`modal-overlay`** — Semi-transparent black overlay at 50% opacity behind modal dialogs. Uses {colors.scrim} (#000000).
**`modal-content`** — White dialog container with {rounded.md} (8px) corners, 24px padding, and a subtle shadow (0 4px 16px rgba(0,0,0,0.15)). Close button is a 32px circle with {colors.muted} icon, hover fills with {colors.surface-soft}.

### Badges & Labels
**`badge-new`** — Red badge for "New" products. {colors.badge-new} (#e53935) background, white text, {rounded.xs} (2px) corners, 2px 6px padding. Uses {typography.badge} (11px, 700 weight, uppercase).
**`badge-sale`** — Green badge for sale items. {colors.badge-sale} (#43a047) background, white text. Same dimensions as `badge-new`.
**`badge-spec`** — Gray badge for spec labels like "RTX 4090" or "32GB RAM". {colors.surface-soft} background, {colors.muted} text, {rounded.xs} corners, 2px 8px padding. Uses {typography.spec-label} (12px, 700 weight, uppercase).

### Hero & Layout
**`hero-section`** — Full-width hero banner with dark background ({colors.ink}) and white text. Contains a title at {typography.display-xl} (32px, 700 weight), a subtitle at {typography.body-md} in {colors.muted-soft}, and a white CTA button (`hero-cta`) styled as a secondary button on dark background.
**`footer`** — Full-width footer with dark background ({colors.ink}) and light gray text ({colors.muted-soft}). Uses {typography.body-sm} for body text and {typography.title-sm} for column headings (white). Links start at {colors.muted-soft} and hover to white.
**`divider`** — A 1px horizontal rule in {colors.hairline-soft} for separating content sections. `divider-strong` uses {colors.hairline} for more visual weight.
**`skeleton-loader`** — Placeholder loading animation using {colors.hairline-soft} background with a pulsing animation. {rounded.sm} corners. Used for product cards, images, and text blocks during data fetch.

### Pagination
**`pagination-item`** — Page number buttons in pagination controls. Transparent background, {colors.muted} text, {rounded.sm} corners, 6px 12px padding. Active page uses {colors.primary} background with white text. Hover uses {colors.surface-soft} background with {colors.ink} text.

### Progress
**`progress-bar`** — Horizontal progress indicator for configurator steps or loading states. 8px height, {rounded.full} corners, {colors.hairline-soft} background. Fill uses {colors.primary} at the same height and corner radius.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; configurator becomes single-column with preview below options; hero text centers; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; configurator remains two-column but narrower; nav items reduce padding; hero maintains left alignment with smaller type |
| Desktop | 1128–1440px | Three-column product grid; full configurator two-column layout; nav at full width with all items visible; hero at max-width 1128px centered |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; configurator panels get more horizontal space; hero content max-width 1128px remains centered |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Nav bar items have 64px touch target height
- Checkboxes and radios are 18px with 44px minimum click area via padding
- Toggle switches are 44px wide with 24px height
- Pagination items have 44px minimum click area (6px padding on 32px text)

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; menu slides in from left with {colors.ink} background
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Configurator switches from two-column to single-column below 744px; preview panel moves below options
- Footer columns collapse from 4 (desktop) to 2 (tablet) to 1 (mobile); column headings become accordion toggles on mobile
- Hero section reduces padding on mobile (from 64px to 32px) and centers text alignment
- Search bar expands to full width on mobile (versus fixed width on desktop)
- Product card image aspect ratio remains 4:3 across all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site; the full color palette (primary-active, disabled, semantic colors, etc.) has been inferred based on common e-commerce patterns and WCAG contrast requirements. These inferred colors should be validated against the actual brand style guide.
- No custom font family was detected; the site uses a system font stack. If the brand later adopts a custom typeface, typography tokens will need updating.
- Hover, focus, and active states for all components are inferred from common patterns; actual interaction states may differ.
- Error, success, warning, and info colors are standard Material Design values and may not match the brand's actual semantic palette.
- Dark mode support is not confirmed; all tokens assume light mode only.
- Animation durations, easing curves, and transition properties were not extracted and use common defaults (200-300ms, ease-in-out).
- Box shadows for cards and modals are estimated; actual shadow values may vary.
- The configurator UI is described based on common PC builder patterns; actual layout and component names may differ.
- No data on form validation styling (error messages, success indicators, character counts).
- No data on loading states beyond skeleton loaders (spinners, progress indicators).
- No data on empty states (no results, empty cart, etc.).
- No data on responsive breakpoints beyond standard ranges; actual breakpoints may differ.
- No data on print styles or reduced-motion preferences.
