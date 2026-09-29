---
version: alpha
name: "The Container Store"
source_url: "https://www.containerstore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The Container Store is a brand built on the promise of a perfectly organized life, where every drawer, closet, and shelf has a designated place. The visual language is clean, approachable, and utilitarian, favoring clarity over decoration. The primary brand voltage is a confident red (`#ce0e2d`), used sparingly but decisively on primary actions and key navigational elements, creating a sense of urgency and purpose. This red is anchored by a vast, almost clinical white canvas (`#fafbfc`), which gives the brand a sense of order and cleanliness. Secondary surfaces and soft dividers use a near-white grey (`#f0f1f2`), while subtle, warm greys (`#f0eeee`) and muted tones (`#b1b5b8`) provide gentle hierarchy without adding visual noise. Typography relies on the dependable, geometric clarity of Roboto, set in a restrained weight range that prioritizes readability and a no-nonsense, functional feel. The system uses soft, friendly corners (`{rounded.sm}`) for cards and buttons, but avoids the extreme pill shapes of consumer lifestyle brands, staying grounded in a practical, slightly squared-off aesthetic. The overall mood is one of calm, capable efficiency — the brand feels like a helpful, knowledgeable expert who has already solved your storage problems, not a flashy trendsetter. The signature design move is the use of the red (`#ce0e2d`) as a single, powerful accent against a sea of white and light grey, often in the form of a bold, rectangular button or a prominent top navigation bar. This creates a clear visual hierarchy that guides the user's eye directly to the most important actions, mirroring the brand's core promise of bringing order to chaos.

colors:
  primary: "#ce0e2d"
  primary-active: "#a00b23"
  primary-disabled: "#fcf0f2"
  ink: "#222222"
  body: "#3f3f3f"
  muted: "#6a6a6a"
  muted-soft: "#b1b5b8"
  hairline: "#dddddd"
  hairline-soft: "#f0eeee"
  canvas: "#fafbfc"
  surface-soft: "#f0f1f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#ce0e2d"
  sale-badge-text: "#ffffff"
  error: "#ce0e2d"
  success: "#2e7d32"
  link: "#ce0e2d"
  link-hover: "#a00b23"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "0 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  category-tile-active:
    border: "2px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  breadcrumb-link:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link-active:
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature red (`#ce0e2d`) with white text. It uses a slightly squared-off corner (`{rounded.sm}`) and a medium weight Roboto font with subtle letter-spacing for a confident, actionable feel. On hover or active press, it shifts to a deeper red (`#a00b23`). When disabled, it fades to a soft pink background (`#fcf0f2`) with muted grey text, signaling inactivity without visual clutter.

**`button-secondary`** — A secondary action button with a white fill and a thin grey border (`{colors.hairline}`). It matches the primary button's height and padding for consistent alignment in forms and action groups. On active state, the border thickens and turns to the ink color, providing a clear visual cue for interaction without relying on the primary red.

**`button-tertiary-text`** — A text-only button used for less prominent actions like "Cancel" or "Learn More". It uses the primary red for its text color, maintaining brand consistency while offering a low-affordance interaction. The active state darkens the text to the primary-active shade.

### Cards
**`product-card`** — The core product display unit, built on a white surface with a soft shadow and a subtle, 4px corner radius. The card contains a square-ratio product image, a title in medium weight, and pricing information. Sale prices are rendered in the primary red to draw immediate attention. A small, red `sale-badge` can be pinned to the top corner of the image for promotional items.

**`category-tile`** — Used for browsing product categories, these tiles have a white background, a light grey border, and a centered title. The active state adds a red border, visually linking the selection back to the primary brand color. They are designed to be tapped or clicked, leading to a subcategory or product listing page.

### Navigation
**`nav-bar`** — The primary site navigation, a fixed-height bar at the top of the page. It uses a clean white background and uppercase, medium-weight Roboto for link text, conveying a sense of order and authority. A subtle box-shadow is applied when the bar becomes sticky on scroll, providing a visual anchor for the user.

**`breadcrumb-link`** — Secondary navigation links styled in small, muted grey text. The active breadcrumb (the current page) is rendered in the darker ink color to indicate the user's final location in the site hierarchy.

### Forms
**`text-input`** — Standard form input fields with a white background, a thin grey border, and a 4px corner radius. On focus, the border doubles in thickness and turns red, providing a clear and brand-consistent state indicator. Error states also use a red border, ensuring the user can quickly identify problematic fields.

### Search
**`search-bar`** — The primary search input, styled as a pill-shaped (`{rounded.full}`) field with a white background and a thin grey border. On focus, the border becomes a thicker red, matching the text-input pattern and reinforcing the brand's visual language for interactive elements.

### Footer
**`footer-section`** — The page footer uses a soft grey background (`{colors.surface-soft}`) to visually separate it from the main content. Links within the footer are styled in a muted grey, darkening on hover to the ink color for a subtle interactive cue. The section uses generous vertical padding to create a sense of breathing room and closure at the bottom of the page.

### Hero
**`hero-banner`** — A full-width promotional banner with a soft grey background and large, bold headline text. It features a single, prominent primary red CTA button, making the desired action unmistakable. The banner's simplicity and high contrast ensure it serves as a powerful visual anchor for marketing campaigns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to a hamburger menu. Product cards stack in a single column. Hero banner text and CTA stack vertically. Search bar becomes full-width. |
| Tablet | 744–1128px | Navigation links remain visible but may be truncated. Product cards display in a 2-column grid. Hero banner uses a side-by-side layout for text and image. |
| Desktop | 1128–1440px | Full navigation bar is displayed. Product cards use a 3 or 4-column grid. Hero banner is at its maximum width with generous padding. |
| Wide | > 1440px | Content is centered within a max-width container. All elements scale proportionally with increased whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Primary buttons are 48px tall to provide a comfortable tap area.
- Product card tap targets are the entire card surface.

### Collapsing Strategy
- The top navigation bar collapses into a hamburger menu on mobile viewports.
- The secondary category navigation collapses into a select dropdown or a horizontally scrollable strip on mobile.
- The footer's multi-column link layout collapses into a single-column accordion on mobile.
- Product filters are hidden behind a "Filter" button on mobile and tablet viewports.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Precise hover and focus ring styles for all interactive elements (e.g., `outline` color and offset for keyboard navigation) were not reliably extracted.
- Specific error and success messaging styles for form validation (e.g., inline error text color, iconography) are inferred.
- The exact typography scale for smaller screens (mobile-specific `fontSize` values) was not captured.
- The brand's approach to dark mode or high-contrast mode is unknown.
- The specific color and style for promotional badges other than the sale badge (e.g., "New", "Exclusive") are not defined.
- The precise box-shadow values for cards, modals, and the sticky nav bar are placeholders and should be verified against the live site's CSS.
- The color palette for sub-brands or specific marketing campaigns (e.g., "Elfa", "Poppin") is not included.
