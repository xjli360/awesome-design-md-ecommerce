---
version: alpha
name: "Balmuda"
source_url: "https://us.balmuda.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Balmuda’s digital presence is a study in quiet precision — a brand that sells kitchen appliances and home goods with the same hushed confidence as a perfectly boiled egg. The canvas is a near-white `#f9fafb` that feels airy and clean, punctuated by a deep, almost-black ink `#1c1d1d` that matches the meta theme-color and anchors every headline and body block. The primary voltage is a verdant teal `#108474`, a color that reads as both natural and engineered — think moss on a ceramic kettle — and it appears on primary CTAs, active navigation states, and the brand’s signature product highlights. A warm gold accent `#b19356` surfaces in badges, secondary details, and the occasional decorative line, lending a subtle artisanal warmth that keeps the brand from feeling cold. Typography relies on `Open Sans` for body and display, set at modest weights (400 for body, 600 for titles) with generous line-height (1.5–1.6) to preserve readability across product detail pages and recipe cards. Rounded corners are present but restrained: `{rounded.sm}` (8px) on buttons and `{rounded.md}` (12px) on product cards, with `{rounded.full}` reserved for the search bar and circular icon badges. The system uses a soft hairline `#dadada` for borders and dividers, and a muted `#7b7b7b` for secondary text, ensuring the interface never competes with the product photography. A bright yellow `#fbcd0a` appears sparingly — perhaps for sale badges or limited-edition callouts — while `#114499` (a deep blue) is used for legal links and footer text, a small but deliberate departure from the teal-green ecosystem. The overall mood is one of considered minimalism: every spacing token, from `{spacing.sm}` (8px) to `{spacing.section}` (64px), feels measured, as if each pixel were weighed on a kitchen scale.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c9"
  ink: "#1c1d1d"
  body: "#333333"
  muted: "#7b7b7b"
  muted-soft: "#999999"
  hairline: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#b19356"
  accent-yellow: "#fbcd0a"
  accent-blue: "#114499"
  badge-new: "#108474"
  badge-sale: "#fbcd0a"
  star-rating: "#b19356"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  legal-link:
    textColor: "{colors.accent-blue}"
    typography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for add-to-cart, checkout, and key conversions. It uses a solid `{colors.primary}` teal fill with white text, 8px rounded corners, and a 44px height for comfortable touch targeting. On hover, it shifts to `{colors.primary-active}` (a slightly darker teal `#0d6b5c`). The disabled state uses `{colors.primary-disabled}` (`#a3d4c9`), a muted pastel teal that signals non-interactivity without visual noise.

**`button-secondary`** — An outlined or ghost-style button for secondary actions like "Learn More" or "View Details." It uses a white (`{colors.surface-card}`) background with `{colors.ink}` text and a 1px `{colors.hairline}` border. On active state, the background fills with `{colors.hairline-soft}` (`#eeeeee`). Height and padding match the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button for low-emphasis actions (e.g., "Cancel", "Skip"). It has no background or border, uses `{colors.primary}` teal text, and relies on the `{typography.button-md}` font weight for clarity. Hover adds a subtle underline.

**`button-pill`** — A fully rounded pill button used for filters, tags, or compact CTAs in product grids. It uses `{colors.primary}` fill with white text, `{typography.button-sm}` sizing, and 36px height. The `{rounded.full}` shape makes it feel friendly and tactile.

### Cards
**`product-card`** — The primary product display component, used in grid and list views. It has a white (`{colors.surface-card}`) background, `{rounded.md}` (12px) corners, and a subtle `{colors.hairline}` border. The card contains a product image (with optional hover zoom), title in `{typography.title-sm}`, price in `{typography.body-md}`, and a star-rating badge using `{colors.accent-gold}`. On hover, a light box shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 64px height with a white background and `{colors.ink}` text. Links use `{typography.nav-link}` (uppercase, 14px, weight 600) with `{spacing.lg}` (24px) horizontal padding between items. The active link is underlined with `{colors.primary}` teal. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link-active`** — The active state for navigation links, using `{colors.primary}` text color and a 2px bottom border in the same teal. The typography remains `{typography.nav-link}` for consistency.

### Forms
**`text-input`** — Standard text input for search, email signup, and address forms. It has a white (`{colors.canvas}`) background, `{rounded.sm}` (8px) corners, and a 1px `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}` teal. The input height is 44px with 16px horizontal padding, using `{typography.body-md}` for entered text.

### Search
**`search-bar`** — The site-wide search component, styled as a pill (`{rounded.full}`) with a soft `{colors.surface-soft}` (`#f4f4f4`) background. It uses `{typography.body-sm}` for placeholder text and has a 44px height. A magnifying glass icon in `{colors.muted}` sits on the left. On focus, the background shifts to white and a `{colors.primary}` border appears.

### Badges
**`badge-new`** — A small, uppercase badge for "New" or "Limited Edition" labels on product cards. It uses `{colors.badge-new}` teal background with white text, `{rounded.xs}` (4px) corners, and `{typography.badge}` (11px, weight 700, uppercase). Padding is 2px 8px for a compact fit.

**`badge-sale`** — A sale or discount badge using `{colors.badge-sale}` yellow (`#fbcd0a`) with `{colors.ink}` text. Same sizing and typography as `badge-new`, but the yellow background creates urgency and contrast against the teal ecosystem.

### Footer
**`footer-section`** — The site footer, using a deep `{colors.ink}` (`#1c1d1d`) background with white text. It contains columns of links, a newsletter signup form, and legal text. Links use `{colors.muted-soft}` (`#999999`) for a subdued appearance, while legal links switch to `{colors.accent-blue}` (`#114499`) for differentiation.

**`footer-link`** — Footer navigation links, styled in `{typography.link}` (14px, weight 400) with `{colors.muted-soft}` text. Hover changes the color to `{colors.canvas}` white.

### Hero
**`hero-banner`** — The full-width hero section on the homepage or category pages. It uses a `{colors.surface-soft}` (`#f4f4f4`) background with `{colors.ink}` text, `{typography.display-xl}` for the headline, and `{spacing.section}` (64px) vertical padding. The hero often includes a large product image or lifestyle photo, with a `{colors.primary}` CTA button centered below the headline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; hero padding reduces to 32px; buttons become full-width; font sizes drop one step (display-xl → display-lg). |
| Tablet | 744–1128px | Nav remains horizontal but with reduced link padding; product grid uses 2 columns; hero uses 40px padding; search bar shrinks to 36px height. |
| Desktop | 1128–1440px | Full nav with 24px link padding; product grid uses 3–4 columns; hero uses 64px padding; all components at default sizes. |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; product grid can expand to 5 columns; hero may include parallax or video. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch-target guidelines.
- Icon buttons and badge pills are at least 36px tall with 40px width.
- Nav links have 24px horizontal padding and 44px touch area.
- Search bar and text inputs use 44px height for comfortable tapping.

### Collapsing Strategy
- The top navigation collapses into a hamburger menu on mobile (< 744px), with a full-screen overlay for link selection.
- Product grids collapse from 4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- The hero banner reduces padding and font size on mobile, and may stack the CTA below the headline.
- Footer columns stack vertically on mobile, with each link group becoming a collapsible accordion.
- Search bar becomes a full-width input on mobile, replacing the pill shape with a standard rectangle.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors.
- Error styling for form inputs (red borders, error messages) was not observed on the live site; assumed to follow standard patterns (e.g., red `#c13515` for error text).
- Dark mode is not supported; all tokens assume a light theme.
- Sub-brand palettes (e.g., for Balmuda Japan vs. USA) may exist but were not detected.
- Animation and transition durations (e.g., button hover, card lift) are not specified; a default 200ms ease-in-out is assumed.
- The `FontAwesome` and `JudgemeStar` font families are used for icons and star ratings but are not defined in the typography system; they are loaded externally.
- Specific spacing for nested components (e.g., card inner padding, grid gaps) was inferred from the `{spacing}` scale but not directly observed.
- The `#007bff` hex color appeared in the extracted hints but is likely a default Bootstrap link color; it is not used in the Balmuda design system.
