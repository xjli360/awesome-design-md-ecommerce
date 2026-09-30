---
version: alpha
name: "MARA Beauty"
source_url: "https://themarabeauty.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  MARA Beauty is a clean, ocean-inspired skincare brand that marries clinical efficacy with an earthy, spa-like serenity. The brand's visual language is anchored by a deep, almost-black teal (`#041e29`) that reads as both luxurious and grounded — it's the color of deep sea water at midnight, used generously across headers, footers, and primary text. Against this dark canvas, a muted, warm taupe (`#979492`) and a soft, creamy off-white (`#f6f4f3`) create a gentle, organic contrast, while a restrained coral-red (`#a91f1f`) provides the only real voltage, used sparingly for sale badges, error states, or accent links. The palette is completed by a series of soft neutrals (`#dedede`, `#c8c8c8`, `#ece5dd`) that form the hairline borders and surface cards, and a single, surprising pop of bright green (`#3ed660`) reserved for "clean" or "vegan" certification badges. Typography leans on the elegant, serifed Cormorant for display headings — a choice that whispers editorial sophistication rather than shouting — paired with the clean, approachable Muli for body copy. The overall mood is one of quiet confidence: generous whitespace, soft pill-shaped buttons (`{rounded.full}`), and product cards with gentle rounding (`{rounded.md}`) that feel tactile and organic, like smooth sea stones. There are no hard edges, no aggressive gradients — just a calm, ingredient-first narrative that lets the algae-green (`#006400`) and ocean-blue (`#1990c6`) accents do the storytelling.

colors:
  primary: "#041e29"
  primary-active: "#0a2e3d"
  primary-disabled: "#8a9ba3"
  ink: "#041e29"
  body: "#121212"
  muted: "#979492"
  muted-soft: "#c8c8c8"
  hairline: "#dedede"
  hairline-soft: "#ece5dd"
  canvas: "#f6f4f3"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#f6f4f3"
  accent-coral: "#a91f1f"
  accent-green: "#3ed660"
  accent-ocean: "#1990c6"
  accent-ocean-dark: "#136f99"
  badge-sale: "#a91f1f"
  badge-clean: "#3ed660"
  badge-new: "#1990c6"
  star-rating: "#ee9441"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Muli', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  button-icon-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
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
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    textDecoration: underline
  badge-clean:
    backgroundColor: "{colors.badge-clean}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the deep teal (`#041e29`) with soft off-white text (`#f6f4f3`). Uses uppercase Muli at 15px with 0.5px letter-spacing for a clean, editorial feel. On hover, the background shifts to a slightly lighter teal (`#0a2e3d`). The disabled state uses a muted gray-blue (`#8a9ba3`) to visually indicate inactivity.

**`button-secondary`** — An outlined variant with a transparent fill, a 2px solid teal border, and teal text. Maintains the same pill shape and uppercase typography. On hover, the background fills with teal and text inverts to off-white, providing a clear interactive state.

**`button-tertiary`** — A text-only button with no background or border, using teal text and the same uppercase Muli style. Used for secondary actions like "Learn More" or "Cancel" within forms.

### Navigation
**`top-nav`** — A fixed-height (72px) navigation bar with a soft off-white background (`#f6f4f3`) and a subtle bottom border (`#ece5dd`). Navigation links use uppercase Muli at 14px with 0.3px letter-spacing. Active links are teal (`#041e29`), inactive links are muted taupe (`#979492`). The brand logo, typically set in Cormorant, sits on the left.

**`nav-link-active` / `nav-link-inactive`** — Defines the two states for top-level navigation items. No background, just color and typography changes.

### Cards
**`product-card`** — A white card with 12px rounded corners (`{rounded.md}`) and no shadow, relying on the contrast against the soft canvas background. The product image occupies the top with rounded top corners, followed by the title in Muli 16px semibold, the price in muted 14px, and optional badges (sale, clean, new) pinned to the top-left of the image.

**`product-card-badge`** — A small, uppercase badge with 4px rounding, used to highlight promotions (coral `#a91f1f`), clean ingredients (green `#3ed660`), or new arrivals (ocean `#1990c6`).

### Forms
**`text-input`** — A standard input field with a white background, 8px rounding, and a light gray border (`#dedede`). On focus, the border thickens to 2px and turns teal. Padding is generous at 12px vertical and 16px horizontal, with a 48px height for comfortable touch targets.

**`search-bar`** — A pill-shaped search input with full rounding, a 1px hairline border, and 44px height. Designed to sit comfortably in the top nav or hero section.

### Footer
**`footer`** — A full-width footer with a deep teal background (`#041e29`) and white text. Links are underlined and inherit the white color. The footer uses generous vertical padding (`{spacing.xxl}`) and is divided into columns for navigation, social links, and legal text.

### Hero
**`hero-section`** — A full-width hero banner with a teal background, using the largest Cormorant display type (48px) for the headline. The call-to-action button is a white pill with teal text, creating a strong, clean contrast. Padding is generous at 64px vertical and 24px horizontal.

### Accordion
**`accordion`** — A vertically stacked list of expandable sections, each with a bottom border (`#ece5dd`). The header uses Muli 16px semibold, and the body uses Muli 16px regular. Used for product descriptions, FAQs, and ingredient lists.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero text reduces to 32px; footer columns stack; search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links; hero uses 40px display; footer splits into two rows |
| Desktop | 1128–1440px | Full top-nav with all links; three-column product grid; hero at full 48px display; footer in four columns |
| Wide | > 1440px | Max-width container (1440px) centered; increased whitespace on sides; hero may use 56px display |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height.
- Icon buttons are 40px x 40px with full rounding.
- Product card badges are at least 20px tall.
- Accordion headers have 16px padding for easy tapping.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), hiding all nav links and the search bar behind a slide-out drawer.
- Product grid collapses from three columns (desktop) to two (tablet) to one (mobile).
- Footer columns collapse from four (desktop) to two (tablet) to a single stack (mobile).
- Hero section reduces font size and padding on mobile to maintain readability.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components (e.g., text-input focus ring color, button hover transitions).
- Error and success styling for forms (e.g., input validation colors, error message typography).
- Dark mode palette and behavior.
- Sub-brand or seasonal color palettes (e.g., holiday collections).
- Specific shadow values (box-shadow) for cards or modals — not reliably extracted.
- Animation and transition timing (e.g., button hover duration, accordion slide speed).
- Iconography system (e.g., stroke width, size tokens, color usage).
- Modal and overlay component specifications.
- Typography scale for mobile (e.g., reduced display sizes).
- Specific Shopify-specific component overrides (e.g., cart drawer, product variant selector).
