---
version: alpha
name: "Scotch Porter"
source_url: "https://www.scotchporter.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Scotch Porter is a modern men's grooming brand built on a foundation of deep, confident hues and warm, earthy accents. The brand's visual identity is anchored by a rich navy ink (`{colors.ink}`: #272d45) and a muted slate (`{colors.body}`: #676986), creating a sophisticated and grounded canvas for its product storytelling. A vibrant, energetic red (`{colors.primary}`: #eb001b) serves as the primary call-to-action, injecting a pulse of passion and urgency into the otherwise calm palette. This red is balanced by a warm, terracotta-like accent (`#b97648`) and a soft, approachable beige (`{colors.canvas}`: #f4f4f6), which together evoke natural ingredients and a tactile, premium feel. The brand's typography relies on the clean, geometric lines of Montserrat, often paired with the reliable legibility of Source Sans Pro and Arial for body copy. This combination communicates a sense of clarity, purpose, and no-nonsense efficacy. Design elements are generously spaced, with `{spacing.lg}` and `{spacing.xl}` creating breathing room around product shots and editorial content. Buttons and cards feature soft, approachable corners (`{rounded.sm}`: 8px), while badges and certain interactive elements may use a more pronounced radius (`{rounded.md}`: 12px). The overall feel is one of intentional, modern masculinity—neither overly aggressive nor minimalist, but rather warm, trustworthy, and aspirational. Subtle highlights of teal (`#00caaa`) and a muted gold (`#ffcf2a`) appear in secondary elements and badges, adding depth and a touch of unexpected color that hints at the brand's holistic approach to grooming.

colors:
  primary: "#eb001b"
  primary-active: "#ad311b"
  primary-disabled: "#f7a0a8"
  ink: "#272d45"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#b0b0b2"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#b97648"
  accent-gold: "#ffcf2a"
  accent-teal: "#00caaa"
  success: "#4cad6a"
  error: "#ff2626"
  badge-new: "#4fc3f7"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  title-lg:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  title-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0px
  body-md:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  body-sm:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Source Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Source Sans Pro', Arial, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0px
    height: auto
  button-tertiary-hover:
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
    border: "2px solid {colors.ink}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0px {spacing.lg}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-best-seller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "0px {spacing.lg}"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg} 0px"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    paddingTop: "{spacing.md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 48px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "0px {spacing.md}"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, from "Add to Cart" to "Shop Now". It uses a bold red (`{colors.primary}`) background with white text, set in uppercase Montserrat for a commanding presence. On hover, it deepens to a rich burgundy (`{colors.primary-active}`), and when disabled, it fades to a soft pink (`{colors.primary-disabled}`). The button has a subtle 8px corner radius (`{rounded.sm}`) and generous 14px/32px padding for a substantial, clickable feel.
**`button-secondary`** — An outlined button used for less prominent actions like "Learn More" or "View Details". It features a white background with a 2px solid ink (`{colors.ink}`) border and ink-colored text. On hover, the background and text colors invert, with the button filling with the ink color for a satisfying state change.
**`button-tertiary`** — A minimal, text-only button used for inline actions or links styled as buttons. It is transparent with red (`{colors.primary}`) text, and on hover, the text shifts to a darker red (`{colors.primary-active}`). It has no padding on the sides, allowing it to sit flush with surrounding text.

### Cards
**`product-card`** — The standard container for displaying products in grid layouts. It is a white card with a soft 8px corner radius (`{rounded.sm}`) and 16px padding. The product image sits at the top with the same corner radius, followed by the product title in `title-md` and the price in `body-md` with a muted body color. The card has no border, relying on the contrast between the white surface and the soft canvas (`{colors.canvas}`) background of the page.
**`hero-banner`** — A full-width promotional banner typically found at the top of landing pages. It uses a deep navy background (`{colors.ink}`) with white text, creating a dramatic and immersive canvas for hero imagery and taglines. The banner includes a semi-transparent overlay (`{colors.scrim}` at 40% opacity) to ensure text readability over background images. Content is padded with `section` spacing for a spacious, editorial feel.

### Navigation
**`nav-bar`** — The primary site navigation, a fixed or sticky bar at the top of the page. It is 72px tall with a white background and uses uppercase, 13px Montserrat for nav links. Links are spaced with `lg` padding on the sides. The active link is highlighted with the brand's signature red (`{colors.primary}`), providing a clear visual indicator of the user's current section.

### Forms
**`text-input`** — Standard text input fields used in forms, search, and checkout. They have a soft canvas background (`{colors.canvas}`), a 1px hairline border (`{colors.hairline}`), and 8px corner radius. On focus, the border thickens to 2px and changes to the ink color (`{colors.ink}`) for a clear, accessible focus state. Error states are indicated by a 2px red border (`{colors.error}`).
**`select-input`** — Dropdown select fields styled consistently with text inputs, using the same canvas background, hairline border, and corner radius. The typography matches `body-md` for consistency across form elements.
**`quantity-selector`** — A compact, horizontally arranged input for adjusting product quantities. It consists of a central numeric display flanked by two buttons. The container has a white background, a 1px hairline border, and an 8px corner radius. The buttons are transparent with ink-colored text and provide a clear hit area for incrementing or decrementing the quantity.

### Badges
**`badge`** — Small, pill-shaped labels used to highlight product attributes like "New", "Sale", or "Best Seller". The default "New" badge uses a light blue (`{colors.badge-new}`) background. A "Sale" badge uses the primary red (`{colors.primary}`) for urgency, while a "Best Seller" badge uses a warm gold (`{colors.accent-gold}`) with dark text for a premium feel. All badges use uppercase, 10px Montserrat with tight padding.

### Footer
**`footer`** — The site footer is a large, dark section with a deep navy background (`{colors.ink}`) and white text. It uses `body-sm` for general content and `link` typography for navigation links, which are initially a muted gray (`{colors.muted-soft}`) and turn white on hover. The footer is padded with `section` spacing, creating a strong visual anchor at the bottom of the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts, stacked product cards, hamburger menu for navigation, reduced hero padding, buttons become full-width. |
| Tablet | 744–1128px | Two-column product grids, expanded navigation (if space permits), increased hero padding, side-by-side form layouts. |
| Desktop | 1128–1440px | Three or four-column product grids, full top-level navigation visible, standard hero banner padding, multi-column footer. |
| Wide | > 1440px | Max-width container (e.g., 1440px) centered on the page, increased whitespace and padding on hero and sections, larger typography scales may be used. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Icon buttons and quantity selector buttons are at least 48px tall.
- Nav links in the mobile menu have increased padding to ensure easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, revealing a full-screen or slide-out overlay.
- Multi-column footers collapse into a single-column accordion on mobile and tablet.
- Product image galleries switch from a grid to a single-image carousel on smaller screens.
- Side-by-side form fields (e.g., first/last name) stack vertically on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for many components (e.g., product cards, footer links) were inferred from common patterns but not directly extracted.
- Error and success styling for forms (e.g., inline validation messages, input icons) were not fully captured.
- The specific typography scale for display and title variants (e.g., `display-sm`, `title-sm`) was estimated based on the extracted fonts and common brand patterns.
- Dark mode or high-contrast mode styles are not defined.
- Sub-brand or collection-specific color palettes (e.g., for "Smooth & Shave" vs "Hair") were not identified.
- The exact border-radius for all component variants (e.g., `button-secondary` active state) was inferred.
- Animation and transition durations/easings were not extracted.
- The specific font weights for Montserrat and Source Sans Pro used in different contexts were estimated based on common usage (e.g., headings use 600/700, body uses 400).
