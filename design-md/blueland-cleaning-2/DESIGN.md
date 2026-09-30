---
version: alpha
name: "Blueland"
source_url: "https://blueland.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cleaning brand that treats its signature blue — #133cd1, a saturated, almost electric ultramarine — as a visual disinfectant, saturating buttons, badges, and the primary navigation with a color that feels more like a chemical reaction than a corporate choice. The palette is overwhelmingly aqueous: #f0f7ff and #deeaff form the background atmosphere, while #a0ddff and #e1f2ff appear as secondary accents, creating a visual ecosystem that mirrors the brand's core promise of turning tablets into cleaning solutions. The typography stack is a deliberate collision of old and new — GT-Pressura (a sharp, geometric sans) and Sailec (a warm, humanist sans) sit alongside Hermann and Self-Modern, with Cambria and Georgia providing editorial gravity for longer-form content. This is not a brand that whispers; the primary CTA button uses {rounded.sm} corners and the full voltage of #133cd1 against white text, while secondary actions retreat into {colors.surface-soft} backgrounds with {colors.muted} text. The checkout flow introduces a secondary blue family — #2c53c9 through #7d9ce8 — suggesting a tiered trust hierarchy where deeper blues signal commitment points. Error states borrow from the extracted #ce4947, a coral-red that appears only in the extracted list, likely reserved for validation and destructive actions. The overall system reads as clinical but not cold, with the #fffcbb yellow and #c8faa1 green appearing as rare, celebratory accents — perhaps for "eco-friendly" badges or subscription savings callouts.

colors:
  primary: "#133cd1"
  primary-active: "#001589"
  primary-disabled: "#b8caef"
  ink: "#000175"
  body: "#2c53c9"
  muted: "#587bda"
  muted-soft: "#7d9ce8"
  hairline: "#deeaff"
  hairline-soft: "#e3eafd"
  canvas: "#ffffff"
  surface-soft: "#f0f7ff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fffcbb"
  accent-green: "#c8faa1"
  accent-coral: "#ce4947"
  accent-pink: "#fce5ff"
  accent-peach: "#fff2dd"
  secondary-blue-deep: "#0033a7"
  secondary-blue-mid: "#2d56d2"
  secondary-blue-light: "#587bda"
  secondary-blue-pale: "#cbd9f7"
  scrim: "#000175"

typography:
  display-xl:
    fontFamily: "'GT-Pressura', 'Sailec', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Sailec', 'GT-Pressura', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Sailec', 'GT-Pressura', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sailec', 'GT-Pressura', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Sailec', 'Georgia', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Sailec', 'Georgia', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sailec', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sailec', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Sailec', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-lg:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Sailec', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT-Pressura', 'Sailec', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-coral}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  subscription-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
  subscription-card-selected:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.secondary-blue-light}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.md} {spacing.base}"
  stepper-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
  stepper-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
  stepper-indicator-complete:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  rating-stars:
    textColor: "{colors.accent-yellow}"
    fontSize: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, saturated in #133cd1 with white text and {rounded.sm} corners. On hover, it deepens to #001589; disabled state uses #b8caef with white text. The 14px 28px padding and 48px height create a substantial, confident footprint that anchors every conversion point — from "Add to Cart" to "Subscribe & Save". **`button-secondary`** — An outlined variant with a white background and #133cd1 text, maintaining the same 48px height and {rounded.sm} corners. The 1px border (not shown in extracted data, assumed) provides hierarchy without competing with the primary. **`button-tertiary-text`** — A text-only link styled as a button, using #133cd1 text on a transparent background, reserved for secondary actions like "Learn More" or "View Details" within cards. **`button-pill-primary`** — A pill-shaped variant using {rounded.full} for promotional banners and hero sections, with 10px 24px padding for a more compact profile. **`button-pill-secondary`** — The same pill shape but with a #f0f7ff background and #000175 text, used for filter tags and category toggles.

### Navigation
**`top-nav`** — A 72px white bar housing the brand logo, navigation links, and utility icons (search, cart, account). Links use `{typography.nav-link}` — 14px GT-Pressura with 0.3px letter spacing and uppercase transformation, creating a crisp, industrial feel. Active links shift to #133cd1; inactive links sit at #587bda. The cart icon likely carries a badge count using {rounded.full} in #133cd1. **`nav-link-active`** and **`nav-link-inactive`** define the two states, with the active state using the primary blue for emphasis.

### Cards
**`product-card`** — A white card with {rounded.md} (12px) corners, containing a product image, title, price, and a badge. The image area uses a #f0f7ff placeholder background with {rounded.md} applied to the image container. Cards stack in a responsive grid, with hover states likely adding a subtle shadow (not extracted). **`product-card-badge`** — Small labels using {rounded.xs} (4px) and `{typography.badge}` (11px uppercase GT-Pressura). Three badge variants exist: yellow (#fffcbb) for general promotions, green (#c8faa1) for eco-friendly claims, and pink (#fce5ff) for new arrivals. Each uses 4px 8px padding for a compact, tag-like appearance.

### Forms
**`text-input`** — A 48px tall input field with white background, #000175 text, and {rounded.sm} corners. The active state likely uses a #133cd1 border (assumed, not extracted). **`text-input-error`** — The error state shifts the border to #ce4947, the coral-red accent, with the same internal padding. **`select-dropdown`** — Matches the text input dimensions and styling, with a dropdown arrow icon in #587bda. **`quantity-selector`** — A compact 40px tall control with {rounded.sm} corners, used on product detail pages for adjusting item counts in the cart.

### Hero & Subscription
**`hero-section`** — A full-width section with a #f0f7ff background, using `{typography.display-xl}` (48px GT-Pressura) for the headline and `{spacing.section}` (64px) vertical padding. The hero CTA uses `{typography.button-lg}` (18px) with 16px 32px padding and 56px height — larger than standard buttons to anchor the page. **`subscription-card`** — A white card with {rounded.md} corners used in the subscription flow. The selected state shifts to #f0f7ff background, indicating the active plan tier. Cards likely include a price, frequency selector, and a "Subscribe" button.

### Footer & Misc
**`footer-section`** — A dark footer using #000175 as background with white text. Links use #587bda (secondary-blue-light) for a softer contrast against the dark background. **`accordion-header`** and **`accordion-content`** — Used for FAQ sections and product details, with the header at 16px Sailec (600 weight) and content at 16px body weight. **`stepper-indicator`** — A 32px circular indicator for multi-step flows (checkout, subscription setup). Three states: default (#f0f7ff background, #587bda text), active (#133cd1 background, white text), and complete (#c8faa1 background, #000175 text). **`divider`** and **`divider-soft`** — 1px horizontal rules using #deeaff and #e3eafd respectively, separating sections and card content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; hero font drops to 32px; subscription cards stack vertically; quantity selector becomes full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (Shop, Subscribe, About); hero uses 40px display; subscription cards in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero at 48px display; subscription cards in 3-column layout; side-by-side accordion sections |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero content centered with 60% max-width; subscription cards in 4-column layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons use 40px diameter circles with {rounded.full}
- Quantity selector buttons are 40px tall with 12px internal padding
- Accordion headers have 16px vertical padding for comfortable tapping
- Stepper indicators are 32px circles with adequate spacing between steps

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-out drawer for links
- Product grid reduces from 4 columns (wide) to 1 column (mobile)
- Hero section reduces vertical padding from 64px to 32px on mobile
- Subscription cards shift from 4-column grid to single-column stack
- Footer link columns collapse to a single column with accordion-style headers
- Search bar becomes full-width on mobile, replacing the inline search icon

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (buttons, inputs, links) are inferred from common patterns; exact extracted hover colors are not available
- Error state styling for text inputs uses #ce4947 for border, but the exact error message typography and iconography are unknown
- Dark mode is not present in the extracted data; all colors assume a light theme
- Shadow values (box-shadow, drop-shadow) for cards, modals, and dropdowns are not extracted
- Border widths for secondary buttons and text inputs are assumed at 1px; exact values unknown
- The extracted font list includes Hermann and Self-Modern, which may be used for specific editorial or display contexts, but their exact usage (weights, sizes) is not confirmed
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted list but are not part of the brand design system
- Social media icon colors and stock image dominant tones may be present in the extracted hex list; the brand's true primary (#133cd1) was selected as the most distinctive and frequently appearing blue
- Animation durations, easing curves, and transition properties are not extracted
- Modal and overlay styling (background scrim opacity, close button placement) is not documented
- The extracted palette includes many blue variants (#001589, #0033a7, #2c53c9, #2d56d2, #587bda, #7d9ce8, #b8caef, #cbd9f7, #e3eafd, #f1f5fd, #f4f8fe) that suggest a comprehensive blue system, but the exact hierarchy (which blue maps to which component state) is inferred
- Accent colors (#fffcbb, #c8faa1, #ce4947, #fce5ff, #fff2dd) are assumed to be used for badges, alerts, and decorative elements, but their exact application is not confirmed
- The typography stack includes monospace fonts (Consolas, Courier New, Liberation Mono, Menlo, Monaco, SFMono-Regular) which may be used for code snippets or technical content, but their usage is not documented
