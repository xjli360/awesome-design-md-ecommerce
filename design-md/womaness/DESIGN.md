---
version: alpha
name: "Womaness"
source_url: "https://womaness.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A matte, deliberate canvas of #f6f6f6 and #eeeeee — near-white surfaces that feel more like uncoated paper than a sterile screen — grounds a brand that treats aging as an art, not a problem to solve. The extracted palette is restrained: near-black ink (#141414) for body copy, a softer #545454 for secondary text, and a single accent of #1199ff that appears sparingly, likely in interactive elements or editorial links, never overwhelming the quiet authority of the greyscale. The site runs on Inter, a clean, slightly condensed sans-serif that reads as modern but not trendy — it has the legibility of a medical journal and the warmth of a well-designed newsletter. Product photography and editorial imagery do the heavy lifting of emotion; the UI stays out of the way. Cards and buttons use soft corners ({rounded.sm} ~8px) that feel approachable without being childish, and the generous use of hairline borders (#dedede, #e2e2e2) creates a subtle grid that organizes content without shouting. This is a brand that trusts its audience to appreciate nuance — there are no aggressive CTAs, no bright sale banners, no visual noise. The checkout experience, likely powered by Shopify, introduces third-party widgets (Klarna, Afterpay) that sit in their own visual system, a pragmatic concession to commerce that doesn't dilute the brand's editorial calm. Womaness speaks in the language of a trusted friend who happens to be a doctor: informed, warm, and utterly unflappable.

colors:
  primary: "#1199ff"
  primary-active: "#0077cc"
  primary-disabled: "#b3d9ff"
  ink: "#141414"
  body: "#545454"
  muted: "#8a8a8a"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f6f6f6"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  warning: "#f57c00"
  link: "#1199ff"
  link-visited: "#551a8b"
  star-rating: "#141414"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  checkbox:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    borderColor: "{colors.primary}"
  radio:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    borderColor: "{colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
  toggle-checked:
    backgroundColor: "{colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  section-subheader:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "2px solid {colors.ink}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
  breadcrumb-current:
    textColor: "{colors.ink}"
  rating-stars:
    textColor: "{colors.star-rating}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  snackbar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  snackbar-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
  snackbar-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
  skeleton:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for key actions like "Add to Cart", "Subscribe", and "Shop Now". On hover, it shifts to `{colors.primary-active}` (#0077cc) for a subtle depth cue. When disabled, it fades to `{colors.primary-disabled}` (#b3d9ff) to indicate non-interactivity while maintaining brand color association. The 8px corner radius (`{rounded.sm}`) keeps it approachable without being overly pill-shaped.

**`button-secondary`** — A white-background button with dark text for secondary actions like "Learn More" or "View Details". Uses a 1px `{colors.hairline}` border to define its shape against the canvas. On hover, the background shifts to `{colors.surface-soft}` (#eeeeee) for a subtle lift.

**`button-secondary-outline`** — A transparent-background button with a 1px `{colors.ink}` border and dark text. Used for tertiary actions where a full button would be too heavy, such as "Cancel" in modals or "Clear Filters". On hover, the background fills with `{colors.surface-soft}`.

**`button-tertiary-text`** — A text-only button with no background or border, styled in `{colors.primary}` blue. Used for inline actions like "Read More" or "See All" within editorial content. On hover, text color shifts to `{colors.primary-active}`.

**`button-pill`** — A fully rounded button (`{rounded.full}`) used sparingly for promotional badges or filter tags. Smaller padding and font size (`{typography.button-sm}`) allow it to sit compactly in category strips or product detail sections.

### Navigation
**`top-nav`** — A fixed or sticky navigation bar at 72px height, using `{colors.canvas}` (#f6f6f6) to blend with the page background. Navigation links are uppercase, 14px, weight 500 (`{typography.nav-link}`) with 0.3px letter spacing — a deliberate editorial choice that reads as magazine-like rather than e-commerce pushy. The active link is underlined with a 2px `{colors.ink}` border.

**`nav-link-active`** — The currently selected navigation item, distinguished by a bottom border rather than a background change. This keeps the nav visually clean and aligned with the brand's editorial sensibility.

**`nav-link-inactive`** — Non-selected navigation items rendered in `{colors.muted}` (#8a8a8a) to recede visually. On hover, they shift to `{colors.ink}`.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with 8px rounded corners (`{rounded.sm}`) and a subtle shadow (not extracted, assumed 0-2px elevation). Contains a product image, title, price, and optional badges. The card uses generous internal padding (`{spacing.base}` ~16px) and a 1px `{colors.hairline}` border when in a grid context.

**`product-card-image`** — The product image area, cropped to a consistent aspect ratio (likely 1:1 or 4:5) with 8px rounded corners at the top of the card. Images are the primary emotional driver — the UI steps back to let the product speak.

**`product-card-badge`** — A small, uppercase badge (11px, weight 600, 0.5px letter spacing) in `{colors.primary}` blue with white text. Used for "NEW", "BESTSELLER", or "LIMITED EDITION" labels. Positioned absolutely over the top-left corner of the product image.

**`product-card-sold-out`** — A dark badge (`{colors.ink}`) with white text for sold-out items. Uses the same typography and positioning as the primary badge but communicates unavailability through color contrast.

### Forms
**`text-input`** — A standard text input field with white background, 8px rounded corners, and a 1px `{colors.hairline}` border. On focus, the border shifts to `{colors.primary}` (#1199ff) for clear visual feedback. Height is 48px for comfortable touch targeting.

**`text-input-focus`** — The focused state of a text input, distinguished by a `{colors.primary}` border. No inner shadow or glow — the brand avoids decorative effects in favor of clean, functional feedback.

**`text-input-error`** — The error state of a text input, using a `{colors.error}` (#d32f2f) border. An error message in `{colors.error}` appears below the input in `{typography.caption}` size.

**`select-input`** — A dropdown select styled identically to `text-input` with a custom chevron icon in `{colors.muted}`. The selected value appears in `{colors.ink}`.

**`textarea`** — A multi-line text input with the same styling as `text-input` but with a minimum height of 120px and vertical resize enabled.

**`checkbox`** — A small (16x16px) square checkbox with 4px rounded corners (`{rounded.xs}`) and a 1px `{colors.hairline}` border. When checked, the background fills with `{colors.primary}` and a white checkmark appears.

**`radio`** — A circular radio button (16x16px) with a 1px `{colors.hairline}` border. When selected, the inner circle fills with `{colors.primary}`.

**`toggle`** — A pill-shaped toggle switch (36x20px) with a `{colors.hairline}` background and a white circular knob. When active, the background shifts to `{colors.primary}`.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` (#141414) background and white text. Organized into columns with newsletter signup, navigation links, and social media icons. Uses `{typography.body-sm}` for link text and `{typography.title-sm}` for column headings.

**`footer-link`** — Footer navigation links in `{colors.muted-soft}` (#aaaaaa) on the dark background. On hover, they lighten to `{colors.on-dark}` (#ffffff) for clear interaction feedback.

**`footer-heading`** — Column headings in the footer, using `{typography.title-sm}` (16px, weight 600) in white. These are not interactive — they serve as structural labels.

**`newsletter-input`** — A text input specifically for the newsletter signup form in the footer. Styled identically to `text-input` but with a placeholder that reads "Enter your email" and a companion `newsletter-button` to submit.

**`newsletter-button`** — The submit button for the newsletter form, using `{colors.primary}` background with white text. Positioned inline with the input field for a seamless signup experience.

### Miscellaneous
**`accordion`** — A collapsible content panel used for FAQs and product details. The header uses `{colors.canvas}` background with `{colors.ink}` text in `{typography.title-sm}`. An expand/collapse chevron icon sits on the right. The panel body uses `{colors.body}` (#545454) text in `{typography.body-md}`.

**`tab-active`** — The active tab in a tabbed interface (e.g., product details: Description, Ingredients, Reviews). Distinguished by a 2px `{colors.ink}` bottom border and `{colors.ink}` text.

**`tab-inactive`** — Inactive tabs rendered in `{colors.muted}` (#8a8a8a) with no bottom border. On hover, text shifts to `{colors.ink}`.

**`badge`** — A small, standalone badge component used for status indicators (e.g., "Free Shipping", "Money Back Guarantee"). Uses `{colors.primary}` background with white text, 4px rounded corners, and uppercase 11px typography.

**`badge-outline`** — An outlined variant of the badge, used for secondary status indicators. Transparent background with a 1px `{colors.primary}` border and `{colors.primary}` text.

**`badge-sale`** — A sale badge using `{colors.error}` (#d32f2f) background to signal discounts or promotions. Same typography and shape as the primary badge.

**`badge-new`** — A "New" badge using `{colors.success}` (#2e7d32) background for newly launched products.

**`modal`** — A centered overlay dialog with white background, 12px rounded corners (`{rounded.md}`), and 32px padding (`{spacing.xl}`). Used for confirmations, product quick-views, and newsletter signups. A semi-transparent `{colors.scrim}` overlay sits behind it at 50% opacity.

**`snackbar`** — A temporary notification bar that appears at the bottom of the screen. Dark background (`{colors.ink}`) with white text in `{typography.body-sm}`. Variants include `snackbar-success` (green background) and `snackbar-error` (red background).

**`progress-bar`** — A thin (4px) progress indicator used for multi-step checkout or subscription flows. The track is `{colors.hairline}` and the fill is `{colors.primary}`, both with fully rounded ends.

**`skeleton`** — A loading placeholder with `{colors.surface-soft}` (#eeeeee) background and 4px rounded corners. Used for product cards, images, and text blocks during page load.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero banner reduces to 24px font; footer columns stack; search bar becomes full-width; accordions expand by default |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (Shop, About, Journal) with hamburger for rest; hero banner uses 28px font; footer shows 2-column layout; search bar is 50% width |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero banner uses 36px font; footer shows 4-column layout; search bar is 360px fixed width; product cards show hover zoom effect |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero banner uses 42px font; additional whitespace on sides; footer remains 4-column but with more padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Product card tap targets are the entire card, not just the title or image
- Accordion headers are 48px tall for easy tapping
- Tab items are 44px tall with 16px horizontal padding
- Checkbox and radio targets are 44x44px (the visual element is 16x16px but the hit area is expanded)
- Toggle switches are 36x20px visual with 44x44px hit area
- Close buttons on modals are 44x44px

### Collapsing Strategy
- **Top Navigation**: On mobile (< 744px), the full nav collapses into a hamburger menu. The logo remains centered. Cart and account icons remain visible. The hamburger opens a full-screen overlay menu with all links, search, and account options.
- **Product Grid**: On mobile, the grid collapses to a single column. On tablet, it expands to 2 columns. On desktop, 3 columns. On wide, 4 columns.
- **Footer**: On mobile, footer columns collapse into a single vertical stack with accordion-style expandable sections for each column heading. On tablet, 2 columns. On desktop and wide, 4 columns.
- **Hero Banner**: On mobile, the hero banner collapses to a single image with text overlay below. On tablet and above, text overlays the image.
- **Search Bar**: On mobile, the search bar expands to full width and may collapse into an icon that expands on tap. On tablet and above, it remains visible as a fixed-width input.
- **Sidebar Filters**: On mobile, filter options collapse into a "Filter" button that opens a bottom sheet or modal. On tablet and above, filters are visible in a sidebar.
- **Breadcrumbs**: On mobile, breadcrumbs collapse to show only the current page and a "Back" link. On tablet and above, full breadcrumb trail is visible.
- **Product Image Gallery**: On mobile, the gallery collapses to a single image with swipeable thumbnails below. On tablet and above, a thumbnail strip on the side is visible.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only from inferred behavior (button-primary-active, link colors). Actual hover transitions (duration, easing) not captured.
- **Focus states**: Keyboard focus indicators (outline styles, ring colors) not extracted. Assumed to use `{colors.primary}` with 2px outline offset.
- **Error states**: Error message styling (icon, placement, animation) not extracted. Assumed standard form validation patterns.
- **Success states**: Success confirmation styling (checkmarks, banners) not extracted.
- **Dark mode**: No evidence of a dark mode variant. The brand's light, matte aesthetic suggests it may not be a priority.
- **Sub-brand palettes**: No evidence of distinct palettes for sub-brands or product lines (e.g., skincare vs. supplements).
- **Typography scale**: Font sizes and weights are estimated based on Inter's standard scale and common editorial e-commerce patterns. Actual site values may vary.
- **Spacing scale**: Spacing tokens are based on a standard 4px/8px grid system. Actual site spacing may use different increments.
- **Shadow/elevation**: No shadow values extracted. Product cards and modals likely use subtle box-shadows (0-2px) but values are unknown.
- **Animation/transition**: No timing functions or durations extracted. Assumed 200-300ms ease transitions for hover/focus states.
- **Icon system**: Social media icons (Font Awesome) detected but no custom icon set or sizing guidelines extracted.
- **Checkout flow**: Shopify checkout likely uses its own design system (Shopify Polaris) which may differ from the brand's front-end styling.
- **Third-party widgets**: Klarna, Afterpay, and other payment widgets have their own visual systems that may not match brand tokens.
- **Accessibility**: No contrast ratios, focus order, or ARIA patterns extracted. Assumes WCAG 2.1 AA compliance as baseline.
- **Custom fonts**: Inter is the primary detected font. No evidence of custom display fonts or variable font axes beyond standard weights.
