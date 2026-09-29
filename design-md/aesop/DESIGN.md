---
version: alpha
name: "Aesop"
source_url: "https://www.aesop.com"
captured_at: "2026-09-28T04:09:52.675206+00:00"
evidence_status: "historical_unverified"
description: |-
  Aesop’s visual language is one of deliberate restraint, where every element earns its place through texture, weight, and quiet authority. The brand operates on a near-monochromatic palette anchored by a deep, almost-black ink (#313131) that reads as sophisticated rather than severe — it’s the color of well-worn leather, of apothecary jars, of a perfectly bound notebook. This single dark tone carries the entire typographic system, from display headlines to the smallest caption, creating a reading experience that feels like a private consultation rather than a broadcast. The canvas is always white, always clean, with no competing colors, no gradients, no decorative flourishes — just the stark beauty of type on page. Rounded corners are used sparingly and subtly: a soft `{rounded.sm}` on buttons, a gentle `{rounded.md}` on product cards, but never the pill-shaped extremes of consumer brands. The typography relies on the system-native stack — `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`, `Noto Sans`, `system-ui`, `sans-serif`, plus the emoji and symbol fallbacks — which gives the site a chameleon-like quality: it feels native and familiar on every device, never fighting the operating system’s own type rendering. This is not a brand that shouts; it’s a brand that speaks in a low, measured tone, trusting that the quality of its products and the precision of its prose will hold attention. The `{spacing.section}` of 64px creates generous breathing room between content blocks, while `{spacing.base}` of 16px governs the internal rhythm of cards and buttons. There is no primary color in the traditional sense — no red CTA, no blue link — because Aesop doesn’t need to direct your eye; it assumes you are already looking. The only visual punctuation comes from product photography and the occasional botanical illustration, which sit against the white canvas like specimens in a vitrine. The result is a design system that feels less like a system and more like a philosophy: reduce until only the essential remains, then polish that essence until it gleams.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c13515"
  error-soft: "#fce4e0"
  success: "#2e7d32"
  success-soft: "#e8f5e9"
  badge-new: "#313131"
  badge-sale: "#c13515"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
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
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.3px
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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-image:
    rounded: "{rounded.none}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "{spacing.base} 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    border: 1px solid "{colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    width: 44px
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered as a solid dark rectangle with a soft 4px corner radius. Its text is set in uppercase 14px medium weight with 0.5px letter spacing, white on the dark background. On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#b0b0b0) to signal non-interactivity while maintaining the brand’s restrained palette. No drop shadows, no gradients, no iconography — just a clean, authoritative rectangle.

**`button-secondary`** — An outlined variant that mirrors the primary button’s dimensions and typography but uses a white fill with a 1px solid border in `{colors.primary}`. On hover, the background shifts to `{colors.surface-soft}` (#f5f5f5) and the border deepens. This button is used for secondary actions like “Add to Wishlist” or “Learn More” where visual hierarchy is needed without the full weight of the primary button.

**`button-ghost`** — A text-only button with no background or border, using the same uppercase typography as the other buttons. It appears as a simple line of text in `{colors.primary}` and is used for tertiary actions, navigation links within content, or “View All” links in product strips. The lack of container makes it the quietest option in the button family.

### Text Inputs
**`text-input`** — A clean, border-defined rectangle with no rounded corners, reflecting Aesop’s preference for sharp, honest geometry. The input uses `{typography.body-md}` at 16px with 1.625 line height for comfortable reading. The default border is `{colors.hairline}` (#d4d4d4), switching to `{colors.primary}` on focus. Error states use `{colors.error}` (#c13515) for the border, with an optional error message in the same color set in `{typography.caption}`. The placeholder text is `{colors.muted-soft}` (#a0a0a0) to maintain legibility without competing with entered text.

### Navigation
**`nav-bar`** — A fixed-height 64px bar with a white background and a subtle 1px bottom border in `{colors.hairline-soft}` (#e8e8e8). Navigation links use `{typography.nav-link}` — 13px uppercase medium weight with 0.3px letter spacing — creating a refined, editorial feel. Active links are rendered in `{colors.primary}`, inactive in `{colors.muted}`. The bar may include a centered logo mark and a right-aligned icon group (search, cart, account). On scroll, the bar gains a sticky position and a slightly stronger bottom shadow (or remains border-only depending on context).

### Product Cards
**`product-card`** — A white card with a soft 8px corner radius containing a product image and text details. The image occupies the top portion with its own rounded corners matching the card’s top radius. Below, the product name appears in `{typography.title-sm}` (16px medium), followed by the price in `{typography.body-sm}` at `{colors.muted}` (#7a7a7a). An optional badge in the top-left corner uses `{typography.badge}` — 10px uppercase semibold with 0.5px letter spacing — on a `{colors.badge-new}` background. Cards have no internal padding on the image; text sections use `{spacing.base}` (16px) for internal padding.

### Hero Banner
**`hero-banner`** — A full-width section anchored by a large product or lifestyle image, with overlaid or adjacent text. The headline uses `{typography.display-xl}` (32px regular weight with tight letter-spacing), while the subtitle uses `{typography.body-md}` in `{colors.muted}`. The banner’s padding is `{spacing.section}` (64px) top and bottom, with `{spacing.lg}` (24px) on the sides. No decorative elements, no overlays — just type and image in quiet conversation.

### Search
**`search-bar`** — A border-defined rectangle with no rounded corners, set on a `{colors.surface-soft}` (#f5f5f5) background for subtle distinction from the white canvas. The input uses `{typography.body-md}` at 16px. On focus, the border switches to `{colors.primary}`. The search bar may include a magnifying glass icon at the left edge and a clear button on the right when text is present. Dropdown suggestions appear below in a white card with `{typography.body-sm}`.

### Footer
**`footer`** — A full-width section on a `{colors.surface-soft}` background, using `{typography.body-sm}` for body text and `{typography.link}` for links. Links are set in `{colors.muted}` and underline on hover, transitioning to `{colors.primary}`. The footer typically contains columns for customer service, about, and social links, with a copyright line at the bottom. Padding is `{spacing.section}` (64px) top and bottom.

### Accordion
**`accordion`** — A vertically stacked series of expandable sections, each with a title in `{typography.title-sm}` and a bottom border in `{colors.hairline-soft}`. The expanded content area uses `{typography.body-sm}` in `{colors.body}` with `{spacing.base}` padding. The title area is clickable and may include a plus/minus or chevron icon to indicate state. No background color change on hover — the interaction is communicated solely through the icon rotation and content reveal.

### Quantity Selector
**`quantity-selector`** — A compact horizontal control with a minus button, a numeric display, and a plus button, all contained within a 44px tall border-defined rectangle. The buttons are 44px wide squares with `{typography.button-sm}` text in `{colors.primary}`. The numeric display uses `{typography.body-md}` centered in the remaining space. Used on product detail pages for cart quantity adjustment.

### Breadcrumbs
**`breadcrumb`** — A horizontal navigation trail using `{typography.caption}` (12px regular with 0.2px letter spacing) in `{colors.muted}`. The current page is rendered in `{colors.primary}`. Items are separated by a forward slash or chevron character in `{colors.hairline}`. No background, no container — just inline text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically at full width; hero banner text overlays image at reduced size; footer columns stack; search bar becomes full-width; accordion becomes primary navigation pattern for product categories |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with hamburger for overflow; hero banner maintains side-by-side layout; footer shows 2-3 columns; search bar has fixed width; product detail page shows side-by-side image and description |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero banner at full width with generous padding; footer shows 4 columns; search bar has maximum width; product detail page has generous whitespace around content |
| Wide | > 1440px | Maximum content width of 1440px with centered layout; product grid may expand to 4 columns; hero banner uses maximum width with increased padding; all other components maintain their desktop behavior within the centered container |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile and tablet
- Icon buttons in the nav-bar (search, cart, account) are 44x44px with adequate padding
- Accordion headers are 48px tall for comfortable tapping
- Quantity selector buttons are 44x44px
- Product card links are full-card tap targets on mobile

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu at 744px breakpoint
- Product grid reduces from 3 columns to 2 at 744px, then to 1 at 480px
- Footer columns collapse from 4 to 2 at 744px, then to 1 at 480px
- Hero banner switches from side-by-side to stacked layout at 744px
- Search bar transitions from fixed-width to full-width at 744px
- Product detail page switches from side-by-side to stacked at 744px
- Accordion sections remain expanded on desktop, collapse on mobile

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover states for secondary and ghost buttons could not be fully verified from extracted data; the active states provided are best estimates based on the brand’s darkening pattern
- Error styling for form validation (error messages, iconography, animation) could not be extracted; the error border color is inferred from common e-commerce patterns
- Sub-brand or seasonal palette variations (e.g., limited edition colorways, holiday treatments) are not captured
- Dark mode preferences or alternate themes are not present in the extracted data
- Animation and transition timing values (duration, easing curves) could not be reliably extracted
- Focus ring styles for keyboard navigation are not documented; a 2px solid outline in `{colors.primary}` with 2px offset is recommended
- Loading states (skeleton screens, spinners) are not defined
- The exact font stack order and any font-weight-specific font files (e.g., 300, 700 weights) could not be verified; the system-native stack is used as extracted
- Dropdown and popover component specifications (z-index, positioning, shadow) are not captured
- Video player controls and styling are not documented
- Print stylesheet specifications are not available
- The brand’s approach to accessibility (contrast ratios, ARIA patterns, skip links) could not be extracted from the static analysis
