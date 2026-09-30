---
version: alpha
name: "June Oven"
source_url: "https://juneoven.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  June Oven’s design system is a study in deliberate warmth and precision, a digital reflection of a countertop appliance that promises to replace a dozen gadgets with one intelligent machine. The brand’s visual identity is anchored on a deep, almost ink-black canvas (`#121212`) that feels both premium and approachable, a backdrop against which its signature voltage — a vibrant, almost electric coral (`#ff5a3c`) — pulses with energy. This primary red-orange, used for primary CTAs, active states, and key product highlights, is not aggressive but confident, a warm invitation to cook. It sits alongside a cooler, more technical accent (`#1990c6`), a nod to the oven’s smart, app-connected nature. The typographic palette is a thoughtful blend: the clean, geometric sans-serif of Euclid Circular and Jost for headlines and navigation, conveying modernity and clarity, paired with the more editorial, serifed Publico Headline for body copy, adding a layer of warmth and culinary sophistication. Surfaces are rendered in soft, layered grays (`#f8f8f8`, `#dddee0`, `#dedede`) that build depth without harshness, while hairline borders (`#c3c5ce`) define cards and sections with a light touch. The overall feel is that of a high-end kitchen appliance brand that has fully embraced the digital age — minimal but not cold, technical but not sterile, with every `{rounded.sm}` corner and `{spacing.lg}` padding feeling intentional, designed to make the complex act of cooking feel simple and delightful.

colors:
  primary: "#ff5a3c"
  primary-active: "#f54b2c"
  primary-disabled: "#ffb8a6"
  ink: "#121212"
  body: "#1d252d"
  muted: "#5c5c5c"
  muted-soft: "#767a87"
  hairline: "#c3c5ce"
  hairline-soft: "#dedede"
  canvas: "#f8f8f8"
  surface-soft: "#dddee0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  accent-blue-active: "#136f99"
  badge-new: "#ff5a3c"
  badge-sale: "#1990c6"
  star-rating: "#1d252d"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Publico Headline', 'Euclid Circular', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Publico Headline', 'Euclid Circular', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Euclid Circular', 'Jost', Poppins, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px

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
    textColor: "{colors.ink}"
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
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  search-bar-active:
    borderColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
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
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for key actions like "Add to Cart" and "Pre-Order Now." It features a vibrant `{colors.primary}` background with white text, a `{rounded.sm}` corner radius, and a `{typography.button-md}` weight for a confident, clickable presence. On hover, the background shifts to `{colors.primary-active}` for a subtle state change, while the disabled state uses `{colors.primary-disabled}` to indicate inactivity.

**`button-secondary`** — A versatile alternative for less prominent actions, such as "Learn More" or "View Recipes." It uses a clean white background (`{colors.canvas}`) with `{colors.ink}` text, maintaining the same `{rounded.sm}` shape and `{typography.button-md}` sizing. Its border (if applicable) would be `{colors.hairline}`, but the default is a subtle, flat appearance.

**`button-tertiary-text`** — A text-only button for the most understated actions, like "Cancel" or "Skip." It uses `{colors.primary}` text on a transparent background, relying on the `{typography.button-md}` font weight for clarity. No background or border, just a clean, clickable label.

**`button-pill-primary`** — A fully rounded (`{rounded.full}`) variant used for promotional badges or compact CTAs, such as "Shop Sale." It uses the same `{colors.primary}` background and `{colors.on-primary}` text but with a smaller `{typography.button-sm}` font and tighter padding.

### Cards
**`product-card`** — The standard container for displaying oven models, accessories, or recipe collections. It features a white background (`{colors.surface-card}`), `{rounded.md}` corners, and `{typography.body-sm}` for descriptive text. The card image area uses a `{rounded.md}` top radius, while the content area below holds the product name, price (`{typography.title-sm}`), and a `{colors.star-rating}` element. A `{product-card-badge}` can be overlaid on the image for "New" or "Sale" indicators.

### Navigation
**`top-nav`** — A fixed-height (72px) navigation bar with a `{colors.canvas}` background and `{colors.ink}` text for brand and primary links. Active nav items are underlined with a 2px `{colors.primary}` border, while inactive items use `{colors.muted}` text. The nav is designed to be responsive, collapsing into a hamburger menu on mobile.

### Forms
**`text-input`** — A standard input field for search, account forms, or checkout. It has a white background (`{colors.surface-card}`), `{rounded.sm}` corners, and `{typography.body-md}` text. On focus, the border (if present) changes to `{colors.primary}`, and an error state uses `{colors.primary}` for both the border and text to indicate validation issues.

### Footer
**`footer`** — A dark, grounding section with a `{colors.ink}` background and `{colors.muted-soft}` text. It uses `{typography.caption}` for general information and `{typography.link}` for navigation links. Links hover to `{colors.on-primary}` for a clear, accessible interaction. The footer is padded with `{spacing.section}` on top and bottom.

### Hero
**`hero-section`** — The primary brand introduction area, typically featuring a large product image or lifestyle shot. It uses a `{colors.ink}` background with `{colors.on-primary}` text, employing `{typography.display-xl}` for the headline. The `{hero-cta}` button is prominently placed within, using the `{button-primary}` style but with larger padding for visual weight.

### Badges
**`badge-new`** and **`badge-sale`** — Small, uppercase labels used to highlight product attributes. `{badge-new}` uses `{colors.primary}` to signal a new arrival, while `{badge-sale}` uses `{colors.accent-blue}` for promotional items. Both use `{typography.badge}` with `{rounded.xs}` corners and tight padding.

### Search
**`search-bar`** — A fully rounded (`{rounded.full}`) search input with a white background, used on the product listing or recipe pages. It uses `{typography.body-md}` for the placeholder text and, when active, gets a `{colors.primary}` border. The `{icon-button}` for the search icon sits inside, using a `{rounded.full}` shape.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero section uses `{typography.display-lg}`; search bar becomes full-width; footer links stack. |
| Tablet | 744–1128px | Two-column grid for product cards; top-nav shows all links; hero uses `{typography.display-xl}`; search bar is centered with max-width. |
| Desktop | 1128–1440px | Three-column grid for product cards; full top-nav with dropdowns; hero uses `{typography.display-xl}` with larger padding; search bar is fixed-width. |
| Wide | > 1440px | Max-width container (1440px) centered; product cards can expand to four columns; hero uses `{typography.display-xl}` with `{spacing.section}` padding; all elements scale proportionally. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility.
- Icon buttons are at least 40px x 40px.
- Product card tap targets are the entire card area.
- Nav links have a minimum tap area of 44px x 44px.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px).
- Product card grid collapses from 3 columns to 2 on tablet, to 1 on mobile.
- Footer link columns collapse to a single column on mobile.
- Hero section reduces padding and font size on mobile.
- Search bar becomes full-width on mobile, losing its fixed-width constraint.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., text-input, icon-button) are inferred from primary color usage but not explicitly documented.
- Error styling for forms (e.g., validation messages, error icons) is not fully extracted.
- Dark mode is not supported; the design relies on a light canvas and dark ink.
- Sub-brand palettes for seasonal promotions or limited editions are not captured.
- Specific animation and transition durations (e.g., button hover, card lift) are not defined.
- Typography line-height and letter-spacing values for some variants (e.g., caption, badge) are estimated based on common brand patterns.
- The exact border width and style for text-input and search-bar are not specified (assumed 1px solid `{colors.hairline}`).
- The `{product-card-badge}` positioning (e.g., top-left) is not defined.
- The `{rating-stars}` component's exact implementation (e.g., SVG, unicode) is not known.
- The `{hero-section}` background image or video treatment is not captured.
- The `{footer}` link hover color is inferred from `{colors.on-primary}` but may differ.
- The `{button-secondary}` border style is not explicitly defined (assumed none or `{colors.hairline}`).
