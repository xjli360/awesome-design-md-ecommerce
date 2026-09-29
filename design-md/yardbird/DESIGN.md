---
version: alpha
name: "Yardbird"
source_url: "https://yardbird.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Yardbird is outdoor furniture for people who actually live outside — not a stiff wicker set behind glass, but deep-seated sofas, fire-pit sectionals, and dining tables that look like they belong in a real home. The brand lives in a warm, earthy palette anchored by a slate-like ink (`#333333`) and a soft body gray (`#4d4d4d`), with accents of teal (`#7bc7c7`), steel blue (`#7396a2`), and a signature sky blue (`#5487a0`) that feels like a clear afternoon. Buttons and key CTAs pulse in a vivid cobalt (`#1c64f6`) that reads as confident and modern, not aggressive. The canvas is a clean white (`#ffffff`) with soft surfaces (`#f7f7f7`) and hairline borders (`#dedede`) that keep the layout airy. Typography runs Montserrat — a geometric sans-serif that balances approachability with a touch of architectural precision. Display sizes sit at moderate weights (500–600) rather than heavy 700+, letting product photography and generous whitespace carry the mood. Rounded corners are gentle but present: cards and inputs use `{rounded.sm}` (8px), buttons use `{rounded.md}` (12px), and the search bar goes full pill (`{rounded.full}`). The overall feel is relaxed, durable, and subtly premium — like a well-made Adirondack chair that only gets better with weather.

colors:
  primary: "#1c64f6"
  primary-active: "#0e84c1"
  primary-disabled: "#a8a8a8"
  ink: "#333333"
  body: "#4d4d4d"
  muted: "#656565"
  muted-soft: "#a8a8a8"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#7bc7c7"
  accent-steel: "#7396a2"
  accent-sky: "#5487a0"
  accent-light-sky: "#d8edf5"
  accent-deep-sky: "#1990c6"
  accent-dark-sky: "#136f99"
  accent-warm: "#230d0d"
  accent-gray-light: "#cccccc"
  accent-gray-mid: "#c9c9c9"
  accent-dark: "#121212"
  star-rating: "#1c64f6"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Glyphicons Halflings', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0

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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 16px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-photo:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "rgba(0,0,0,0.2)"
    textColor: "{colors.on-primary}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "12px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: "2px solid #c13515"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
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
    border: "2px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"
  tab-primary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "2px solid transparent"
  tab-primary-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  tab-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  tab-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
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
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  toast-success:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  toast-error:
    backgroundColor: "#c13515"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loading:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Yardbird experience. Uses a vivid cobalt (`{colors.primary}`) background with white text (`{colors.on-primary}`) and a moderate 12px corner radius (`{rounded.md}`). On hover, it shifts to a deeper sky blue (`{colors.primary-active}`); the disabled state fades to a neutral gray (`{colors.primary-disabled}`). The 48px height and 12px/24px padding give it a solid, grounded feel that matches the furniture's durability.
**`button-secondary`** — A bordered alternative for less prominent actions. Rendered on a white canvas with ink text and a 2px hairline border. On active state, the border deepens to ink and the background picks up a soft surface tint (`{colors.surface-soft}`).
**`button-tertiary-text`** — A text-only button for inline or subtle actions. Transparent background with primary blue text, used for "Learn More" or "View Details" links within product cards.
**`button-pill-primary`** — A fully rounded pill variant for search filters, category tags, or compact CTAs. Uses primary blue fill with white text, 10px/20px padding, and `{rounded.full}`.
**`button-pill-outline`** — The outlined counterpart to the pill button, used for filter chips and secondary tag actions. White background with ink text and a hairline border.

### Cards
**`product-card`** — The core product display unit across category pages and search results. A white card with a soft hairline border and 8px corner radius (`{rounded.sm}`). The photo area uses a top-only radius (`{rounded.sm} {rounded.sm} 0 0`). On hover, the card gains a subtle drop shadow and a slightly stronger border to signal interactivity. Price is set in `{typography.title-md}` with ink color; ratings use the primary blue star color.
**`product-card-badge`** — Overlaid on product photos to flag new arrivals, sale items, or sold-out status. Uses `{typography.badge}` (10px uppercase) with tight 2px/8px padding and a 4px corner radius. New items get a teal badge (`{colors.accent-teal}`), sale items use primary blue, and sold-out uses muted-soft gray.

### Navigation
**`top-nav`** — A fixed 72px white bar with a soft bottom border (`{colors.hairline-soft}`). Navigation links use 14px medium-weight Montserrat (`{typography.nav-link}`). Active links are indicated by a 2px primary blue underline; inactive links render in muted gray. The nav houses the logo, category links, search icon, and account/cart icons.
**`category-strip`** — A horizontal scrollable strip below the top nav for browsing product categories. Uses white background with a soft bottom border. Active categories are rendered as filled pills (`{rounded.full}`) on a soft surface background; inactive categories are transparent with muted text.
**`nav-link-active`** — The active state for top navigation links, distinguished by a 2px primary blue bottom border that sits flush with the nav bar's bottom edge.
**`nav-link-inactive`** — Inactive navigation links rendered in muted gray (`{colors.muted}`) with no underline.

### Forms
**`text-input`** — Standard text input for forms, search fields, and checkout. A white background with 8px corner radius (`{rounded.sm}`), 12px/16px padding, and a hairline border. On focus, the border becomes a 2px primary blue stroke. Error states use a red border (#c13515).
**`select-input`** — Dropdown select styled consistently with text inputs: white background, 8px radius, hairline border, and matching 48px height.
**`checkbox`** — Square checkbox with 4px radius and a 2px hairline border. When checked, the fill switches to primary blue with a white checkmark.
**`radio`** — Circular radio button with a 2px hairline border. The checked state shows a primary blue outer ring with a filled center.
**`toggle`** — A pill-shaped toggle switch, 44px wide and 24px tall. The off state uses a hairline gray fill; the on state switches to primary blue. The 20px circular knob is white.
**`newsletter-input`** — A dedicated email input for the footer newsletter signup. Matches the standard text input styling but sits alongside a primary blue submit button in a compact row.

### Footer
**`footer`** — A dark footer section using ink (`{colors.ink}`) as the background with white text. Links render in muted-soft gray (`{colors.muted-soft}`) using `{typography.link}`. Section headings use `{typography.title-sm}` in white. The footer includes the newsletter signup, brand story links, customer service links, and social icons.
**`footer-link`** — Footer navigation links in muted-soft gray with 14px regular weight. Hover state would transition to white (not captured in extracted data).
**`footer-heading`** — Footer column headings in white with 14px medium weight.

### Badges & Tags
**`badge-new`** — A teal badge (`{colors.accent-teal}`) for flagging new product arrivals. Uses 10px uppercase bold text with a 4px corner radius.
**`badge-sale`** — A primary blue badge for sale or promotional items. White text on blue background.
**`badge-sold-out`** — A muted gray badge for out-of-stock items. White text on a muted-soft background.

### Feedback & Loading
**`toast-success`** — A success notification toast with teal background and ink text. Used for "Added to Cart" confirmations.
**`toast-error`** — An error notification toast with red background and white text. Used for form validation or API errors.
**`loading-spinner`** — A 24px spinning indicator in primary blue, used during async operations.
**`skeleton-loading`** — A soft surface gray placeholder with 4px radius for content that is still loading.
**`progress-bar`** — A 4px tall pill-shaped progress indicator. The track is soft surface gray; the fill is primary blue.

### Modals & Overlays
**`modal-overlay`** — A semi-transparent black overlay (50% opacity) that covers the viewport behind modals.
**`modal-card`** — The modal container with white background, 12px corner radius (`{rounded.md}`), 24px padding, and a subtle drop shadow. Used for quick-view product modals, size guides, and confirmation dialogs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; category strip becomes horizontally scrollable; hero banner reduces padding to 32px; footer columns stack; search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; category strip remains scrollable; hero banner uses 48px padding; footer shows 2-column layout |
| Desktop | 1128–1440px | Full top-nav with all links visible; three-column product grid; category strip shows all items; hero banner uses section-level padding; footer shows 4-column layout |
| Wide | > 1440px | Max-width container (1440px) centered; four-column product grid; additional whitespace around hero and sections; footer remains 4-column with more generous padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px x 40px with 40px touch targets
- Product cards have full-card tap targets on mobile
- Category pills are 36px+ tall with 16px horizontal padding
- Search bar is 48px tall for easy tapping
- Toggle switches are 44px wide with a 20px knob

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay menu
- Category strip collapses from visible tabs to a horizontally scrollable row on tablet and mobile
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 4 columns to 2 columns on tablet, stacking to a single column on mobile
- Hero banner collapses from side-by-side text and image to stacked layout on mobile
- Search bar collapses from a full input field to an icon-only button on mobile, expanding to a full overlay on tap
- Product filters collapse from a persistent sidebar to a bottom sheet or modal on tablet and mobile
- Accordion-style sections (product details, reviews) remain collapsed by default on all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, cards, links) were not reliably extracted from the live site CSS; the active states documented above are inferred from common patterns
- Error styling for form inputs (red border, error message typography) is assumed based on standard e-commerce patterns, not extracted from Yardbird's specific implementation
- Dark mode tokens are not present; the brand currently ships a light-only experience
- Sub-brand or collection-specific palettes (e.g., "Coastal Collection," "Modern Collection") could not be extracted
- Animation and transition timing values (durations, easing curves) are missing
- Focus ring styles for keyboard accessibility are not documented
- The `Glyphicons Halflings` font family appears in extracted CSS but is likely used for iconography, not body text; its usage is preserved in the typography stack for compatibility
- Specific font weights beyond 400, 500, and 600 could not be confirmed; the brand may use 700 for some display elements
- Letter-spacing values for display typography are estimated based on common Montserrat usage
- Box-shadow values for cards and modals are inferred from visual inspection, not extracted from CSS
- The `#53b8d4` and `#0e84c1` hex values appear in the extracted palette but their specific usage (links, accents, hover states) could not be determined
- Mobile-specific typography scale (smaller font sizes on narrow viewports) is not documented
