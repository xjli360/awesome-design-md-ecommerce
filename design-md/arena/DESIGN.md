---
version: alpha
name: "Arena"
source_url: "https://arena.fit"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A fitness ecosystem that uses a pale, almost clinical palette of #c1e9ff, #e1fcff, and #bde7ff to create a sense of clean air and open space — the brand equivalent of a gym at 6am before anyone else arrives. The primary accent #5b5b5b is an unexpected choice: a warm mid-gray that reads as equipment metal, not brand energy, suggesting Arena trusts its photography of athletes and movement to supply the color. Shopify Sans Medium and Regular run the typography at modest weights, with no display-heavy boldface — the system lets the product grid and workout imagery do the heavy lifting. The extracted palette includes #eceafb and #f0edfe, lavender-tinged neutrals that soften the industrial gray, and #f4f5f6 as a near-white canvas. There are no hard corners in the UI: buttons use `{rounded.sm}`, cards use `{rounded.md}`, and the search bar uses `{rounded.full}`. The brand feels like a white-box gym repurposed for digital — clean, uncluttered, with the equipment (the product catalog, the class schedule, the trainer profiles) arranged in neat, accessible rows.

colors:
  primary: "#5b5b5b"
  primary-active: "#4a4a4a"
  primary-disabled: "#c4c4c4"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#f4f5f6"
  surface-soft: "#f0edfe"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-light-blue: "#c1e9ff"
  accent-ice: "#e1fcff"
  accent-sky: "#bde7ff"
  accent-lavender: "#eceafb"
  accent-lavender-soft: "#f0edfe"
  accent-lavender-mid: "#e9e8fb"

typography:
  display-xl:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Shopify Sans Regular', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Shopify Sans Medium', 'Shopify Sans', -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    padding: 11px 23px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-accent-light-blue:
    backgroundColor: "{colors.accent-light-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  button-accent-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-light-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-section-accent:
    backgroundColor: "{colors.accent-ice}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.accent-lavender-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  checkbox:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  radio:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  toggle:
    backgroundColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-handle:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  avatar:
    backgroundColor: "{colors.accent-light-blue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  avatar-sm:
    backgroundColor: "{colors.accent-light-blue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  avatar-lg:
    backgroundColor: "{colors.accent-light-blue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 64px
  badge-new:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  loading-spinner:
    color: "{colors.primary}"
    height: 24px
  loading-spinner-sm:
    color: "{colors.primary}"
    height: 16px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  modal-overlay:
    backgroundColor: "{colors.ink}"
    opacity: 0.5
  modal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  toast-success:
    backgroundColor: "{colors.accent-light-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  toast-error:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  star-rating:
    color: "{colors.primary}"
    size: 16px
  star-rating-sm:
    color: "{colors.primary}"
    size: 12px
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  price-display-sale:
    typography: "{typography.title-md}"
    textColor: "{colors.muted}"
  price-display-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (#5b5b5b) with white text. Uses `{typography.button-md}` at 16px/500 weight. On hover, shifts to `{colors.primary-active}` (#4a4a4a). Disabled state uses `{colors.primary-disabled}` (#c4c4c4). Height is 48px with 12px 24px padding and `{rounded.sm}` corners.

**`button-secondary`** — An outlined or ghost-style button on `{colors.canvas}` (#f4f5f6) background with `{colors.ink}` (#1a1a1a) text. Same dimensions as primary but with a 1px border (not defined in tokens, but implied). Used for secondary actions like "Cancel" or "Learn More".

**`button-tertiary-text`** — A text-only button with no background or border. Uses `{colors.ink}` text and `{typography.button-md}`. Used for inline actions like "View all" or "See details".

**`button-accent-light-blue`** — An accent button using `{colors.accent-light-blue}` (#c1e9ff) background with `{colors.ink}` text. Uses `{typography.button-sm}` at 14px. Used for promotional CTAs, category filters, or secondary actions within cards.

**`button-accent-lavender`** — An accent button using `{colors.accent-lavender}` (#eceafb) background with `{colors.ink}` text. Same dimensions as the light blue accent button. Used for alternate promotional contexts or to create visual variety in a row of accent buttons.

### Navigation
**`top-nav`** — The main navigation bar, 72px tall, on `{colors.canvas}` (#f4f5f6) background. Contains the brand logo, nav links, and utility icons (search, cart, account). Nav links use `{typography.nav-link}` at 15px/500 weight. Active links use `{colors.ink}`, inactive links use `{colors.muted}` (#6b6b6b). The bar is fixed at the top on desktop, collapsing to a hamburger menu on mobile.

**`nav-link-active`** — Active navigation link with `{colors.ink}` text. No background or border — the active state is indicated by text color alone.

**`nav-link-inactive`** — Inactive navigation link with `{colors.muted}` (#6b6b6b) text. On hover, transitions to `{colors.ink}`.

**`search-bar-pill`** — A pill-shaped search bar with `{rounded.full}` corners, 48px tall, on `{colors.surface-card}` (#ffffff) background. Uses `{typography.body-sm}` at 14px. Includes a search icon on the left and a subtle drop shadow (not defined in tokens, but implied). On focus, the bar gets a `{colors.primary}` border.

### Cards
**`product-card`** — A product card with `{colors.surface-card}` (#ffffff) background, `{rounded.md}` (12px) corners, and 16px padding. Contains a product image (with `{rounded.sm}` corners), title, price, and optional badge. The card has a subtle shadow on hover (not defined in tokens, but implied).

**`product-card-image`** — The image within a product card, with `{rounded.sm}` (8px) corners. Aspect ratio is typically 1:1 or 4:3.

**`product-card-badge`** — A small badge overlaid on the product image, using `{colors.accent-light-blue}` (#c1e9ff) background with `{colors.ink}` text. Uses `{typography.badge}` at 11px uppercase. Padding is 4px 8px with `{rounded.xs}` (4px) corners. Used for "New", "Sale", or "Limited Edition" labels.

### Hero & Sections
**`hero-section`** — A full-width hero section on `{colors.canvas}` (#f4f5f6) background. Uses `{typography.display-xl}` at 32px/500 weight. Padding is 64px 24px. Contains a headline, optional subheadline, and a primary CTA button.

**`hero-section-accent`** — A variant hero section using `{colors.accent-ice}` (#e1fcff) background. Same typography and padding. Used for promotional campaigns or seasonal landing pages.

### Category Strip
**`category-strip`** — A horizontal scrollable strip of category tabs. Background is `{colors.canvas}`. Tabs use `{typography.button-sm}` at 14px.

**`category-tab-active`** — Active category tab with `{colors.accent-lavender-soft}` (#f0edfe) background and `{colors.ink}` text. Pill-shaped with `{rounded.full}` corners and 8px 16px padding.

**`category-tab-inactive`** — Inactive category tab with transparent background and `{colors.muted}` (#6b6b6b) text. Same pill shape and padding. On hover, background shifts to `{colors.hairline-soft}` (#e8e8e8).

### Footer
**`footer`** — The site footer on `{colors.ink}` (#1a1a1a) background with white text. Uses `{typography.body-sm}` at 14px. Padding is 48px 24px. Contains columns of links, social icons, and copyright information.

**`footer-link`** — A link within the footer, using `{colors.on-primary}` (#ffffff) text and `{typography.link}` at 14px. On hover, text becomes `{colors.accent-light-blue}` (#c1e9ff).

### Forms
**`text-input`** — A standard text input field on `{colors.surface-card}` (#ffffff) background with `{colors.ink}` text. Uses `{typography.body-md}` at 16px. Height is 48px with 12px 16px padding and `{rounded.sm}` (8px) corners. Has a 1px `{colors.hairline}` (#d4d4d4) border.

**`text-input-focus`** — Focus state of the text input. Border shifts to `{colors.primary}` (#5b5b5b).

**`text-input-error`** — Error state of the text input. Border shifts to a red (not defined in tokens, but implied as #e74c3c or similar). Error message appears below in `{typography.caption-sm}`.

**`select-input`** — A select dropdown input. Same dimensions and styling as `text-input`. Includes a dropdown arrow icon.

**`checkbox`** — A standard checkbox with `{colors.surface-card}` background and `{rounded.xs}` (4px) corners. When checked, uses `{colors.primary}` background with white checkmark.

**`checkbox-checked`** — Checked state of the checkbox. Background is `{colors.primary}` (#5b5b5b) with white checkmark icon.

**`radio`** — A standard radio button with `{colors.surface-card}` background and `{rounded.full}` corners. When checked, uses `{colors.primary}` fill.

**`radio-checked`** — Checked state of the radio button. Background is `{colors.primary}` (#5b5b5b) with white inner dot.

**`toggle`** — A toggle switch with `{colors.muted-soft}` (#9e9e9e) background and `{rounded.full}` corners. Height is 24px. When active, background shifts to `{colors.primary}`.

**`toggle-active`** — Active state of the toggle switch. Background is `{colors.primary}` (#5b5b5b).

**`toggle-handle`** — The circular handle of the toggle switch. Background is `{colors.surface-card}` (#ffffff) with `{rounded.full}` corners. Height is 20px.

### Dividers
**`divider`** — A horizontal divider line, 1px tall, using `{colors.hairline}` (#d4d4d4).

**`divider-soft`** — A softer horizontal divider line, 1px tall, using `{colors.hairline-soft}` (#e8e8e8).

### Avatars
**`avatar`** — A circular avatar with `{colors.accent-light-blue}` (#c1e9ff) background and `{colors.ink}` text. Uses `{rounded.full}` corners. Height is 40px. Contains a user's initials or a placeholder icon.

**`avatar-sm`** — Small avatar variant, 32px tall.

**`avatar-lg`** — Large avatar variant, 64px tall.

### Badges
**`badge-new`** — A "New" badge using `{colors.accent-lavender}` (#eceafb) background with `{colors.ink}` text. Uses `{typography.badge}` at 11px uppercase. Padding is 2px 6px with `{rounded.xs}` (4px) corners.

**`badge-sale`** — A "Sale" badge using `{colors.accent-sky}` (#bde7ff) background with `{colors.ink}` text. Same dimensions as `badge-new`.

### Loading & Feedback
**`loading-spinner`** — A circular loading spinner in `{colors.primary}` (#5b5b5b). Height is 24px. Animates rotation.

**`loading-spinner-sm`** — Small spinner variant, 16px tall.

**`tooltip`** — A tooltip with `{colors.ink}` (#1a1a1a) background and white text. Uses `{typography.caption-sm}` at 12px. Padding is 6px 10px with `{rounded.xs}` (4px) corners. Appears above or below the target element.

### Modal
**`modal-overlay`** — The semi-transparent overlay behind a modal. Uses `{colors.ink}` (#1a1a1a) at 50% opacity.

**`modal-card`** — The modal content card on `{colors.surface-card}` (#ffffff) background. Uses `{rounded.md}` (12px) corners with 24px padding. Contains a title, content, and action buttons.

### Toast
**`toast-success`** — A success toast notification using `{colors.accent-light-blue}` (#c1e9ff) background with `{colors.ink}` text. Uses `{typography.body-sm}` at 14px. Padding is 12px 16px with `{rounded.sm}` (8px) corners.

**`toast-error`** — An error toast notification using `{colors.primary}` (#5b5b5b) background with white text. Same dimensions as success toast.

### Progress
**`progress-bar`** — A progress bar track using `{colors.hairline-soft}` (#e8e8e8) background. Uses `{rounded.full}` corners. Height is 4px.

**`progress-bar-fill`** — The filled portion of the progress bar using `{colors.primary}` (#5b5b5b). Same rounded and height.

### Ratings
**`star-rating`** — A star rating component using `{colors.primary}` (#5b5b5b) for filled stars. Size is 16px. Empty stars use `{colors.hairline}` (#d4d4d4).

**`star-rating-sm`** — Small star rating variant, 12px.

### Price Display
**`price-display`** — The current price using `{typography.title-md}` at 18px/500 weight with `{colors.ink}` text.

**`price-display-sale`** — The sale price using `{typography.title-md}` with `{colors.muted}` (#6b6b6b) text.

**`price-display-original`** — The original (strikethrough) price using `{typography.body-sm}` at 14px with `{colors.muted-soft}` (#9e9e9e) text and `textDecoration: line-through`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Top nav collapses to hamburger menu. Product cards stack vertically. Category strip becomes horizontally scrollable. Hero section padding reduces to 32px 16px. Search bar moves to a full-width row below the nav. Footer columns stack. |
| Tablet | 744–1128px | Two-column grid for product cards. Top nav remains visible but with reduced padding. Category strip shows 4-5 visible tabs. Hero section uses 48px 24px padding. Search bar is in the nav bar. |
| Desktop | 1128–1440px | Three-column grid for product cards. Full top nav with all links visible. Category strip shows all tabs. Hero section uses 64px 24px padding. Standard layout. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Four-column grid for product cards. Hero section uses 80px 48px padding. Additional whitespace around all sections. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile.
- Icon buttons are 40px × 40px minimum.
- Category tabs have 8px 16px padding, making them easily tappable.
- Toggle switches are 24px tall with a 20px handle.
- Search bar is 48px tall on all breakpoints.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The menu slides in from the left or right, overlaying the content.
- The category strip collapses to a horizontally scrollable row on mobile, with a "See all" option at the end.
- Product cards stack vertically on mobile, switching to a 2-column grid on tablet and 3-column on desktop.
- The footer collapses to a single column on mobile, with accordion-style sections for each link group.
- Hero sections reduce padding on mobile, and may stack the CTA button below the headline.
- Search functionality moves from an inline bar to a full-screen overlay on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are limited to 9 values and appear to be a mix of Shopify checkout-widget colors (Klarna, Afterpay) and stock-image dominant tones. The primary #5b5b5b is the most distinctive color in the list, but it's a neutral gray — the brand's true primary may be a more vibrant color not captured in the extraction. The lavender and blue accents (#eceafb, #c1e9ff, #e1fcff, #bde7ff) are likely secondary brand colors or UI accents.
- Hover states for buttons and links are inferred from common patterns; actual hover colors may differ.
- Error state colors for form inputs are not extracted; a red (#e74c3c or similar) is assumed.
- Focus ring styles (outline, offset, color) are not extracted.
- Shadow values (box-shadow for cards, modals, dropdowns) are not extracted.
- Border widths for inputs and cards are not extracted; 1px is assumed.
- Font weights for Shopify Sans Medium (500) and Regular (400) are assumed based on common usage; actual weights may vary.
- Line heights and letter spacing values are estimated based on standard typography scales; actual values may differ.
- Dark mode styles are not present in the extracted data.
- Sub-brand or campaign-specific palettes are not captured.
- Animation durations and easing curves are not extracted.
- Iconography style (line weight, corner radius, stroke width) is not captured.
- The brand's actual primary color may be a more distinctive hue (e.g., a vibrant blue, green, or orange) that was not present in the extracted HTML+CSS colors due to the site being a Shopify generic template. The extracted palette is heavily weighted toward checkout-widget and social-icon colors.
