---
version: alpha
name: "Westman Atelier"
source_url: "https://www.westman-atelier.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Westman Atelier is clean luxury makeup that feels like skincare, built on a philosophy of "curation over collection." The brand's visual language mirrors its product ethos: refined, restrained, and resolutely sophisticated. The palette is anchored in deep, almost-black ink (`#141414`) and soft charcoal (`#333333`), creating a sense of quiet authority that never shouts. Against this, a canvas of pure white (`#f6f6f6`) and warm off-white (`#dedede`) provides a luminous backdrop, while the signature accent — a precise, cerulean blue (`#1990c6`) — appears sparingly, like a single stroke of color on a minimalist painting. This blue, deepened to `#136f99` on interaction, is the brand's only chromatic gesture, used for primary actions and select editorial highlights. The typography is set in Inter, a clean, neo-grotesk typeface that carries the brand's clinical-yet-warm precision. There are no decorative flourishes, no heavy weights, no loud gradients. Instead, the system relies on generous whitespace, hairline-thin borders (`#e2e2e2`), and a carefully calibrated hierarchy where `{spacing.section}` (64px) creates breathing room between product stories. The overall effect is one of a high-end apothecary: tactile, trustworthy, and deeply intentional. Every component — from the pill-shaped buttons (`{rounded.full}`) to the softly rounded product cards (`{rounded.md}`) — feels like it was designed for a single, perfect application.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#8fc9e3"
  ink: "#141414"
  body: "#333333"
  muted: "#545454"
  muted-soft: "#8c8c8c"
  hairline: "#e2e2e2"
  hairline-soft: "#dedede"
  canvas: "#f6f6f6"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#1990c6"
  accent-blue-active: "#136f99"
  badge-new: "#1990c6"
  badge-sold-out: "#545454"
  star-rating: "#141414"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02px
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01px
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01px
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid #c13515"
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
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3/4"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-swatch:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-dark}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "none"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  swatch-selector:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  swatch-selector-active:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a pill-shaped button in the signature cerulean blue (`{colors.primary}`). The uppercase, letter-spaced typography (`{typography.button-md}`) conveys a sense of deliberate, editorial authority. On hover, the button deepens to `{colors.primary-active}` (`#136f99`), and in its disabled state, it fades to a muted `{colors.primary-disabled}` (`#8fc9e3`). The generous horizontal padding (32px) and full border-radius (`{rounded.full}`) give it a tactile, almost cosmetic-tool-like quality.

**`button-secondary`** — A ghost button with a white fill (`{colors.canvas}`) and a single hairline border (`{colors.hairline}`). It shares the same pill shape and uppercase typography as the primary button, but reads as quieter and more utilitarian. On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`, creating a subtle elevation. This button is used for secondary actions like "Add to Wishlist" or "View Details."

**`button-tertiary-text`** — A text-only button with no background or border, used for the most subdued actions (e.g., "Cancel," "Skip"). The typography remains uppercase and letter-spaced, but the lack of container makes it feel like an editorial link. On hover, the text color shifts to `{colors.primary}`, introducing the brand's accent blue as a sign of interactivity.

### Text Inputs & Forms
**`text-input`** — A clean, rectangular input field with a soft border (`{colors.hairline}`) and a white background (`{colors.canvas}`). The typography is set in `{typography.body-md}` (16px Inter regular), ensuring readability. On focus, the border switches to `{colors.primary}`, providing a clear, brand-aligned indicator of active state. Error states use a red border (`#c13515`) — a rare chromatic departure from the brand's restrained palette. The input height (48px) and padding (12px 16px) are designed for comfortable touch interaction.

**`select-input`** — Shares the same visual DNA as the text input: white background, hairline border, 48px height. The dropdown arrow is rendered in `{colors.muted}` and switches to `{colors.primary}` on focus. The typography matches `{typography.body-md}` for consistency across form elements.

### Navigation
**`nav-bar`** — A fixed-position top navigation bar with a white background (`{colors.canvas}`) and a subtle bottom border (`{colors.hairline-soft}`). The nav links are set in `{typography.nav-link}` — uppercase, letter-spaced, 13px — giving the bar a refined, editorial feel. Active links are indicated by a 2px bottom border in `{colors.ink}`, while inactive links sit in `{colors.muted}`. The bar height (72px) provides ample vertical space for the brand logo and up to six navigation items.

**`nav-link-active` / `nav-link-inactive`** — These tokens define the active and inactive states of navigation links. Active links use `{colors.ink}` with a bottom border, while inactive links use `{colors.muted}` with no border. The typography remains consistent across both states.

### Product Cards
**`product-card`** — The primary product display component, featuring a 3:4 aspect ratio image with softly rounded corners (`{rounded.md}`) at the top, and a text block below with `{spacing.md}` padding. The card has no background color (transparent by default) but gains a subtle box shadow (`0 4px 12px rgba(0,0,0,0.08)`) on hover. The product title uses `{typography.title-sm}` (14px, medium weight), while the price is set in `{typography.body-sm}` (14px, regular weight) in `{colors.muted}`. This hierarchy ensures the product name is the primary visual anchor.

**`product-card-info`** — The text container within a product card, padded with `{spacing.md}` on the sides and `{spacing.base}` on the bottom. It houses the product title, price, and any badges (e.g., "NEW" or "SOLD OUT").

### Badges
**`badge-new`** — A small, pill-shaped badge in the brand's cerulean blue (`{colors.badge-new}`), used to flag new arrivals. The typography is set in `{typography.badge}` — 10px, uppercase, with 0.5px letter spacing — ensuring it reads as a subtle editorial note rather than a promotional shout. The badge is positioned at the top-left of product card images.

**`badge-sold-out`** — Identical in shape and typography to `badge-new`, but rendered in `{colors.badge-sold-out}` (`#545454`). This muted gray communicates unavailability without visual aggression, maintaining the brand's calm, curated tone.

**`badge-swatch`** — A circular color swatch (24px diameter) used to display product shade options. The swatch has a white background and a hairline border (`{colors.hairline}`), and is filled with the actual product color via inline styles. Active swatches are indicated by a 2px `{colors.ink}` border.

### Hero Section
**`hero-section`** — A full-width section with a white background (`{colors.canvas}`) and generous vertical padding (`{spacing.section}`). The hero title uses `{typography.display-xl}` (36px, light weight, tight letter-spacing) for a refined, editorial headline. The subtitle is set in `{typography.body-md}` (16px) in `{colors.muted}`, with a `{spacing.xl}` gap before the primary CTA button. This section is designed to feature a single product or collection hero image alongside minimal text.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and hairline border. The typography matches `{typography.body-md}` for consistency with other form elements. On focus, the border switches to `{colors.primary}`, providing a clear interactive cue. The 48px height and 20px horizontal padding ensure comfortable text entry.

**`search-bar-focus`** — The focused state of the search bar, identical to the default but with a `{colors.primary}` border. This is the only visual change, maintaining the brand's minimal interaction design.

### Footer
**`footer-section`** — A dark footer section with a deep ink background (`{colors.ink}`) and white text (`{colors.on-dark}`). The footer uses `{spacing.section}` for vertical padding, creating a strong visual anchor at the bottom of the page. Links are set in `{typography.link}` (14px, regular weight) and shift to `{colors.primary}` on hover, introducing the brand's accent blue as a sign of interactivity against the dark background.

**`newsletter-input`** — A pill-shaped email input with a white background and no border, designed to sit within the dark footer. The typography uses `{typography.body-sm}` (14px) for a slightly smaller, more discreet input. The adjacent **`newsletter-button`** is a pill-shaped primary button in `{colors.primary}`, completing the sign-up flow.

### Accordion
**`accordion-trigger`** — A full-width clickable row with no background, using `{typography.title-sm}` (14px, medium weight) for the trigger text. A bottom border (`{colors.hairline-soft}`) separates each accordion item. The trigger has `{spacing.base}` vertical padding, providing a comfortable tap target.

**`accordion-content`** — The expandable content area below the trigger, using `{typography.body-sm}` (14px, regular weight) in `{colors.body}`. The content is padded with `{spacing.base}` on the bottom, creating visual separation from the next trigger.

### Ratings & Quantity
**`rating-stars`** — A 16px star icon rendered in `{colors.star-rating}` (`#141414`). The brand uses filled and empty star icons to represent product ratings, with the filled stars in the deep ink color. This maintains the monochromatic, refined aesthetic.

**`quantity-selector`** — A compact, rectangular control (40px height) with a white background and hairline border. The typography matches `{typography.body-md}` for the numeric value. Plus/minus buttons are rendered as text symbols in `{colors.muted}`, switching to `{colors.ink}` on hover.

### Swatch Selector
**`swatch-selector`** — A 32px circular color swatch with a hairline border (`{colors.hairline}`). The swatch is filled with the product's shade color via inline styles. This component is used in product detail pages to allow users to select from multiple shades.

**`swatch-selector-active`** — The active state of the swatch selector, identical in size and shape but with a 2px `{colors.ink}` border. This provides a clear, brand-aligned indicator of the selected shade.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; search bar moves to sticky header; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows 4-5 links; hero section uses 50/50 split for text and image; footer links in two columns; search bar remains in header |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; hero section uses 60/40 split with larger image; footer links in three columns; search bar in header with full-width option |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero section centers content with max-width; all other components scale proportionally within the container |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 44px to meet WCAG touch target guidelines.
- Nav-bar links have a minimum tap area of 48px x 48px, even if the text is smaller.
- Product card images are tappable with a minimum area of 120px x 160px on mobile.
- Accordion triggers have a minimum height of 48px for comfortable tapping.
- Swatch selectors are 32px, which is below the recommended 44px minimum; on mobile, they are wrapped in a scrollable strip with increased padding.

### Collapsing Strategy
- On mobile (< 744px), the nav-bar collapses to a hamburger menu icon, with the full navigation appearing as a slide-in drawer from the left.
- Product filters (e.g., shade, category, price) collapse into a single "Filter" button that opens a bottom sheet.
- The footer's multi-column link layout collapses to a single column with accordion-style expandable sections.
- The search bar collapses from a full-width input to an icon button that expands on tap.
- Product detail page sections (e.g., ingredients, how to use) collapse into accordion panels on all screen sizes.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components could not be fully extracted; the provided hover tokens are based on observed patterns and brand logic.
- Error styling for forms (e.g., validation messages, error icons) was not reliably extracted; the red border (`#c13515`) is inferred from common e-commerce patterns.
- Dark mode tokens are not defined; the brand currently uses a light-only palette.
- Sub-brand or collection-specific palettes (e.g., limited edition colors) were not captured.
- Animation and transition durations (e.g., button hover, accordion expand) were not extracted; a default of 200ms ease-in-out is recommended.
- Focus ring styles for keyboard navigation were not observed; a 2px `{colors.primary}` outline with 2px offset is recommended for accessibility.
- The exact font weights for Inter (e.g., 300, 400, 500) are inferred from the brand's editorial feel; the actual site may use additional weights.
- Spacing values for specific components (e.g., product card gap, grid gutter) are based on common e-commerce patterns and may differ from the live site.
- The newsletter input and button combination in the footer is inferred; the exact layout (inline vs. stacked) may vary.
- The quantity selector's plus/minus button styling (e.g., hover, active) was not extracted.
- The swatch selector's active state border color (`{colors.ink}`) is inferred; the brand may use a different indicator (e.g., checkmark icon).
