---
version: alpha
name: "Prequel"
source_url: "https://prequelskin.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Prequel is a modern dermatologist-developed skincare brand that feels like a clean, clinical consultation translated into a warm, approachable digital experience. The brand's visual identity is anchored on a deep teal `#00303c` — a color that reads as both medical authority and spa-like calm — which appears across the primary navigation, key CTAs, and the site's `theme-color` meta tag. This is balanced against a soft, almost powdery blue `#d1e2ef` that surfaces in backgrounds and secondary elements, evoking the clean, sterile feel of a dermatologist's office without being cold. The canvas is a bright `#f2f2f2` that shifts to a near-white `#fefefe` for product cards and content areas, creating a layered, airy hierarchy. A subtle but distinctive accent palette emerges in the form of a pale butter `#fffee1` used for highlights and special offers, and a muted sage `#4d6e77` that provides a secondary text and icon color. The brand's typography relies on a mix of `din-2014` for clean, geometric headlines that convey precision and `montserrat` for body text, lending a modern, slightly European sensibility. Signature design moves include generous use of `{rounded.full}` for pill-shaped buttons and search bars, soft `{rounded.md}` for product cards, and a consistent `{spacing.lg}` padding rhythm that gives the interface room to breathe. The overall feel is one of informed, gentle authority — a brand that trusts its clinical credentials but communicates through soft corners, muted tones, and a restrained, almost editorial layout. Error states use a warm red `#721c24` on a `#f8d7da` background, while success and informational cues lean into the primary teal and a brighter `#00aad5`, ensuring that feedback is clear but never jarring. The brand's voice is educational and reassuring, with a visual system that supports long-form ingredient storytelling and before-and-after photography without ever feeling cluttered or promotional.

colors:
  primary: "#00303c"
  primary-active: "#00596f"
  primary-disabled: "#4d6e77"
  ink: "#1a1a1a"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f2f2f2"
  surface-soft: "#f7f9fa"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  accent-blue: "#d1e2ef"
  accent-blue-soft: "#e3edf5"
  accent-yellow: "#fffee1"
  accent-yellow-soft: "#fffdc7"
  accent-teal: "#00aad5"
  accent-teal-soft: "#1990c6"
  error-bg: "#f8d7da"
  error-border: "#f5c6cb"
  error-text: "#721c24"
  error-text-hover: "#d02e2e"
  star-rating: "#1a1a1a"
  badge-new: "#a45cec"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0
  body-md:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.4px
  link:
    fontFamily: "'montserrat', 'AvenirRegular', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'din-2014', 'montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.3px

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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error-border}"
    backgroundColor: "{colors.error-bg}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
    borderColor: "{colors.hairline}"
  search-bar-pill-focus:
    borderColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-alt:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.accent-blue}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.error-text}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline-soft}"
  accordion-open:
    backgroundColor: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    borderColor: "{colors.hairline}"
  cart-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
  cart-item:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button with a deep teal `{colors.primary}` background and white text. On hover, it shifts to `{colors.primary-active}` for a subtle darkening effect. The disabled state uses a muted sage `{colors.primary-disabled}` to indicate inactivity without visual noise. The button uses `{typography.button-md}` with 14px 28px padding and a 48px height for a comfortable, accessible tap target.

**`button-secondary`** — A ghost-style button with a white `{colors.canvas}` background and dark `{colors.ink}` text, bordered by a 1px solid `{colors.hairline}`. On active/hover, the background fills with the soft accent blue `{colors.accent-blue}`. This button is used for "Add to Cart" secondary actions and "Learn More" links within product cards.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` for the text color. It is used for less prominent actions like "Cancel", "Clear Filters", or "View All" in navigation contexts. The text color shifts to `{colors.primary-active}` on hover.

**`button-pill-accent`** — A special accent button using the pale butter `{colors.accent-yellow}` background, reserved for promotional CTAs, limited-time offers, and sale banners. It uses `{typography.button-sm}` for a slightly tighter fit and is always `{rounded.full}`.

### Cards
**`product-card`** — The primary product display card, using a white `{colors.surface-card}` background with `{rounded.md}` corners. It contains a product image with `{rounded.sm}`, a title using `{typography.title-sm}`, a price using `{typography.body-md}`, and a rating using `{typography.caption}`. On hover, a subtle box-shadow is applied to lift the card. The card uses `{spacing.base}` padding for internal content.

**`cart-item`** — A compact card used within the cart drawer, with a soft `{colors.surface-soft}` background and `{rounded.sm}` corners. It displays a small product thumbnail, title, quantity selector, and price. Padding is `{spacing.md}` for a dense but readable layout.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height with a solid `{colors.primary}` background. It contains the brand logo, navigation links using `{typography.nav-link}`, and a search icon. On scroll, the bar transitions to a white `{colors.surface-card}` background with dark text, creating a clean, unobtrusive header for content pages.

**`nav-bar-scrolled`** — The scrolled state of the navigation bar, which collapses to 64px height and uses a white background. This state is used to reduce visual weight when the user is deep into content.

### Forms
**`text-input`** — A standard text input field with a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` for clear visual feedback. Error states use a red border `{colors.error-border}` and a light red background `{colors.error-bg}` to indicate validation issues.

**`quantity-selector`** — A compact input for adjusting product quantities, with a white background, `{rounded.sm}` corners, and a 40px height. It includes minus and plus buttons flanking the numeric value, all styled with `{typography.body-md}`.

### Footer
**`footer`** — The site footer, using a deep teal `{colors.primary}` background with white text. It contains columns of links, social media icons, and legal text. Links use `{colors.accent-blue}` for a soft, readable contrast against the dark background. The footer uses `{spacing.xxl}` vertical padding and `{spacing.lg}` horizontal padding.

### Badges
**`badge-new`** — A pill-shaped badge with a purple `{colors.badge-new}` background, used to indicate new product arrivals. It uses `{typography.badge}` with uppercase text and tight padding.

**`badge-sale`** — A pill-shaped badge with a red `{colors.error-text}` background, used for sale or discount indicators. It follows the same styling as the new badge but with a different color to signal urgency.

### Accordion
**`accordion`** — A collapsible content panel used for product descriptions, ingredient lists, and FAQs. It has a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline-soft}` border. The header uses `{typography.title-sm}` and includes a chevron icon that rotates on open. When expanded, the background shifts to `{colors.surface-soft}` for visual distinction.

### Cart Drawer
**`cart-drawer`** — A slide-in panel from the right side of the screen, using a white background. It contains a list of `cart-item` components, a subtotal line, and a checkout button. The drawer uses `{spacing.lg}` padding and has a maximum width of 400px on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.lg}`; search bar becomes full-width; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains visible but reduces link font size to `{typography.nav-link}` at 14px; hero section uses `{spacing.xl}` padding; search bar is centered with 60% width |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; hero section uses `{spacing.section}` padding; search bar is 40% width; footer displays in multi-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section uses `{spacing.section}` padding with larger `{typography.display-xl}` at 42px; search bar is 30% width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for mobile touch targets.
- Icon buttons and quantity selectors maintain a 40px minimum dimension.
- Product card tap targets (image, title, add-to-cart) are at least 48px in height.
- Nav-bar links have a minimum tap area of 44px x 44px.

### Collapsing Strategy
- The primary navigation collapses into a hamburger menu on mobile (< 744px), with a slide-in drawer for links.
- Product descriptions and ingredient lists use accordion components on all breakpoints, but on mobile they are collapsed by default to save vertical space.
- The cart drawer slides in from the right on all breakpoints, but on mobile it takes the full screen width.
- The footer's multi-column layout collapses to a single column on mobile, with accordion-style sections for link groups.
- Hero sections reduce their vertical padding on mobile to avoid excessive scrolling.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors.
- Error styling for form inputs is inferred from common patterns; exact error message typography and iconography are not confirmed.
- Sub-brand or collection-specific palettes (e.g., for "Prequel Skin" vs. "Prequel MD") are not captured.
- Dark mode is not supported and no dark mode tokens are defined.
- Animation and transition durations (e.g., for hover effects, accordion open/close, cart drawer slide-in) are not specified.
- The exact font weights for `din-2014-narrow` and `montserrat-alternates` are not confirmed; only the primary font families are used.
- The `AvenirRegular` font family is declared but its usage context is unclear; it may be a fallback for specific components.
- The `star-rating` color is assumed to be `{colors.ink}` but could be a brand-specific gold or yellow.
- The `badge-new` color `#a45cec` is extracted from a single instance; its usage may be more limited.
- The `scrim` color `#121212` is assumed for modal overlays but its exact opacity is not confirmed.
- The `button-pill-accent` component's hover state is not defined; it may use a darker shade of `{colors.accent-yellow}`.
- The `nav-bar-scrolled` component's transition duration and easing are not specified.
- The `cart-drawer` component's close button and overlay styling are not defined.
- The `quantity-selector` component's button hover and active states are not captured.
- The `accordion` component's open/close animation duration and icon rotation are not specified.
