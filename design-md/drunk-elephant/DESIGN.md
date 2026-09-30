---
version: alpha
name: "Drunk Elephant"
source_url: "https://www.drunkelephant.com"
captured_at: "2026-09-28T04:09:58.947281+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A biocompatible skincare brand that feels like a clean, clinical apothecary crossed with a playful, colorful candy shop. The canvas is a crisp, almost clinical white (`#fefefe`) that gives way to a warm, muted gray (`#f7f8fa`) on soft surfaces, creating a sense of hygienic calm. The brand's signature voltage comes from a bold, confident red (`#c8102e`), used sparingly but powerfully on primary actions and key accents, with a deeper, more serious crimson (`#af0813`) for active states. This is balanced by a surprisingly playful palette: a zesty lime green (`#84bd00`), a soft pastel pink (`#f6dcff`), a vibrant coral (`#f68f5b`), and an electric yellow (`#e6fe52`) that appear in product badges, ingredient callouts, and limited-edition packaging. The typography system is a study in contrast: the elegant, serifed "Sentinel" for display headings lends a touch of editorial sophistication, while the clean, geometric "Brown" and "Lato" families handle body copy and UI with a modern, approachable clarity. The overall effect is one of informed, joyful efficacy—a brand that trusts its science but never forgets to have fun with its colors.

colors:
  primary: "#c8102e"
  primary-active: "#af0813"
  primary-disabled: "#e0e0e0"
  ink: "#45474a"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#fefefe"
  surface-soft: "#f7f8fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#84bd00"
  accent-coral: "#f68f5b"
  accent-pink: "#f6dcff"
  accent-yellow: "#e6fe52"
  accent-beige: "#be9170"
  badge-red: "#990000"
  badge-green: "#64772d"
  star-rating: "#c8102e"
  link-blue: "#00629b"
  scrim: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "'SentinelMedium', 'SentinelSemiBold', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'SentinelMedium', 'SentinelSemiBold', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Brown', 'BrownBold', 'BrownRegular', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown', 'BrownBold', 'BrownRegular', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'OpenSans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'OpenSans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'OpenSans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Brown', 'BrownBold', 'BrownRegular', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Brown', 'BrownBold', 'BrownRegular', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Lato', 'OpenSans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brown', 'BrownBold', 'BrownRegular', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Brown', 'BrownBold', 'BrownRegular', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  link-inline:
    color: "{colors.link-blue}"
    typography: "{typography.link}"
  link-footer:
    color: "{colors.canvas}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using a bold, confident red (`{colors.primary}`) with white text (`{colors.on-primary}`). The button has no border-radius (`{rounded.none}`), giving it a sharp, clinical feel that aligns with the brand's scientific positioning. On hover, the background shifts to a deeper crimson (`{colors.primary-active}`). The disabled state uses a light gray (`{colors.primary-disabled}`) with muted text (`{colors.muted}`), signaling the action is unavailable.

**`button-secondary`** — An outlined or ghost variant on a white canvas (`{colors.canvas}`) with dark ink text (`{colors.ink}`). It shares the same sharp corners and uppercase typography as the primary button, but inverts the color relationship. This is used for less prominent actions like "Learn More" or "Add to Wishlist."

**`button-pill`** — A smaller, fully rounded (`{rounded.full}`) button used for badges, filters, or promotional tags. It retains the brand red (`{colors.primary}`) but uses a smaller uppercase font (`{typography.button-sm}`) and tighter padding, making it feel like a playful accent rather than a primary action.

### Cards
**`product-card`** — A clean, white (`{colors.surface-card}`) card with no border-radius, used to display product thumbnails. The card relies on generous whitespace and a subtle shadow (not defined in tokens) to create depth. Typography is minimal, using `{typography.body-sm}` for product names and `{typography.caption}` for prices.

**`product-card-badge`** — A small, colored badge pinned to the top corner of a product card. It uses a vibrant green (`{colors.accent-green}`) with dark text (`{colors.ink}`) to signal "New," "Bestseller," or "Limited Edition." The badge has a slight rounding (`{rounded.sm}`) to soften its appearance.

### Navigation
**`nav-bar`** — A fixed top navigation bar on a white canvas (`{colors.canvas}`) with a height of 72px. Links use `{typography.nav-link}`, which is an uppercase, semi-bold sans-serif. The bar may include a subtle bottom border (`{colors.hairline-soft}`) to separate it from the page content. The logo is typically centered or left-aligned, with the cart icon and search bar on the right.

### Forms
**`text-input`** — A standard input field with a white background (`{colors.canvas}`) and no border-radius (`{rounded.none}`). The border uses `{colors.hairline}` and the placeholder text is `{colors.muted}`. On focus, the border may change to `{colors.primary}`. The input height is 48px for comfortable touch interaction.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input used in the navigation or on the search results page. It has a white background (`{colors.canvas}`) and uses `{typography.body-md}` for the entered text. The placeholder text is `{colors.muted}`. The pill shape contrasts with the sharp corners of buttons, adding a friendly touch to the search experience.

### Footer
**`footer`** — A dark footer section with a background of `{colors.ink}` and white text (`{colors.canvas}`). It uses `{typography.body-sm}` for links and copyright information. Links are styled with `{typography.link-footer}` and may have a hover state that underlines or changes color to `{colors.primary}`. The footer is divided into columns for navigation, customer service, and social media links.

### Accordion
**`accordion-header`** — A clickable header for collapsible sections, often used in FAQ or product details. It has a white background (`{colors.canvas}`) and uses `{typography.title-md}` for the title. Padding is 16px top and bottom with no horizontal padding, creating a clean, minimal look. A chevron icon (not defined in tokens) indicates the collapsed/expanded state.

**`accordion-content`** — The expandable content area below the header. It shares the same white background (`{colors.canvas}`) and uses `{typography.body-md}` for the text. Padding is 0 on top and 16px on the bottom, ensuring the content is flush with the header.

### Hero Section
**`hero-section`** — A full-width banner section at the top of key pages. It uses a soft gray background (`{colors.surface-soft}`) and `{typography.display-xl}` for the main headline. The section may include a background image or video, with text overlaid. The hero typically has a large padding (`{spacing.section}`) on top and bottom to create a spacious, impactful layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero text scales down to `{typography.display-md}`; search bar becomes full-width. |
| Tablet | 744–1128px | Two-column grid for product cards; nav bar shows limited links; hero section maintains two-column layout; accordions remain single-column. |
| Desktop | 1128–1440px | Full nav bar visible; three-column product grid; hero section uses full-width background; sidebars or filters appear on category pages. |
| Wide | > 1440px | Max-width container (1440px) centered; additional whitespace on sides; product grid may expand to four columns; hero text may increase to 40px. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile to meet accessibility guidelines.
- The `button-primary` and `button-secondary` components are 48px tall, exceeding the minimum.
- Icon buttons (e.g., cart, search) are at least 44x44px on mobile.
- Accordion headers are at least 48px tall to ensure easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, hiding all links except the logo and cart icon.
- Product filters on category pages collapse into a "Filter" button that opens a modal or drawer.
- The footer's multi-column layout collapses into a single column, with accordion-style sections for each category.
- Hero sections may reduce height and stack text below the image on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover states for secondary buttons, text inputs, and links were not reliably extracted from the live site.
- Error styling for form inputs (e.g., red border, error message typography) is not defined.
- Sub-brand or limited-edition color palettes (e.g., holiday collections) are not captured.
- Dark mode or high-contrast mode styles are not present in the extracted data.
- Shadow tokens (box-shadow, drop-shadow) were not extracted and are not defined.
- Transition and animation durations/easings are not specified.
- The exact font weights for "Brown" and "Sentinel" families are inferred from naming conventions (e.g., "BrownBold" implies 700).
- The `textTransform: uppercase` on button and nav-link typography is an assumption based on common DTC skincare patterns, not directly extracted.
- The `star-rating` component color is assumed to match the primary red, but actual implementation may vary.
- The `link-blue` color (`#00629b`) is extracted but its specific usage (e.g., inline links vs. footer links) is inferred.
