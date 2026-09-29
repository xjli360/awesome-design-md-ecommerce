---
version: alpha
name: "Vaja Cases"
source_url: "https://www.vajacases.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Argentine leather craftsmanship meets a digital storefront that lets the material speak — the site runs on a near-monochrome scaffold of #222222, #363636, and #151515, punctuated by a single warm accent: #ee7d53, a burnt-orange that appears on add-to-cart buttons, sale badges, and the hover state of product thumbnails. The palette is deliberately restrained; the extracted color list is dominated by grays (#5f5f5f, #8b8b8b, #b3b3b3, #dbdbdb, #f4f4f4) because the brand trusts its product photography — close-ups of stitched leather, patina, and grain — to supply all the warmth and texture. Typography runs Avenir Next and Helvetica Neue at modest weights (400–600), never competing with the imagery. Buttons use {rounded.sm} corners (8px) rather than pills, a subtle nod to the precision of leather cutting. The nav bar is a thin, fixed strip at 48px height — barely there — and the product grid uses generous {spacing.xl} gutters so each case floats in its own white space. The checkout flow inherits Shopify's default blue (#00adef) and red (#e50122) for payment widgets, a visual break that the brand accepts rather than overrides. The overall effect is a gallery for objects, not a marketplace — quiet, deliberate, and anchored in the tactility of the material.

colors:
  primary: "#ee7d53"
  primary-active: "#da6e46"
  primary-disabled: "#fca98a"
  ink: "#151515"
  body: "#222222"
  muted: "#5f5f5f"
  muted-soft: "#8b8b8b"
  hairline: "#c7c7c7"
  hairline-soft: "#dbdbdb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#f04f36"
  accent-checkout: "#00adef"
  accent-error: "#e50122"
  dark-bg: "#1d1d1d"
  dark-surface: "#363636"

typography:
  display-xl:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  button-md:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
  section: 80px

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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    border: "none"
  nav-bar-item:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-bar-item-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  footer-section:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: "1px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.dark-surface}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in burnt-orange `{colors.primary}` (#ee7d53) with white text. Uses `{typography.button-md}` (14px uppercase, 600 weight) and `{rounded.sm}` (8px) corners. On hover, shifts to `{colors.primary-active}` (#da6e46). Disabled state uses `{colors.primary-disabled}` (#fca98a). Height is 44px with 12px vertical padding.

**`button-secondary`** — Outlined variant with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Active state darkens the border to `{colors.ink}` and adds a light gray fill. Same sizing and typography as primary.

**`button-dark`** — Used on dark backgrounds (e.g., footer or dark hero sections). Solid `{colors.ink}` (#151515) background with white text. Same sizing as primary.

**`button-sale`** — Compact badge-button for sale items. Uses `{colors.accent-sale}` (#f04f36) background, `{typography.button-sm}` (12px uppercase), and smaller padding (8px 16px, 32px height). Appears on product cards and collection pages.

### Navigation
**`nav-bar`** — A thin, fixed top bar at 48px height with a white background and no border. Navigation links use `{typography.nav-link}` (13px uppercase, 500 weight, 0.5px letter spacing). Active links are `{colors.ink}`, inactive are `{colors.muted}` (#5f5f5f). The bar collapses to a hamburger menu on mobile.

**`nav-bar-item`** — Individual nav link with horizontal padding of `{spacing.base}` (16px). No background or border. Active state simply changes text color to `{colors.ink}`.

### Product Cards
**`product-card`** — A minimal, borderless card with no rounding. The image fills the full width with no corner radius. Below the image, the title uses `{typography.title-md}` (18px, 600 weight) and the price uses `{typography.body-md}` (16px, 400 weight) in `{colors.muted}`. Sale items show a `{product-card-badge}` in the top-left corner.

**`product-card-badge`** — A small, sharp-cornered (`{rounded.xs}`, 2px) label using `{colors.accent-sale}` background and `{typography.badge}` (11px uppercase, 700 weight). Padding is 2px top/bottom, 8px left/right.

### Forms
**`text-input`** — Standard input field with a white background, 1px `{colors.hairline}` border, `{rounded.sm}` (8px) corners, and `{typography.body-sm}` (14px). Height is 44px with 10px vertical padding. Focus state swaps the border to `{colors.ink}`.

### Hero
**`hero-section`** — Full-width section with generous vertical padding (`{spacing.section}`, 80px). Uses `{typography.display-xl}` (32px, 600 weight) for the headline. The primary CTA uses `{hero-cta}`, a larger version of `button-primary` with 14px vertical padding and 48px height.

### Footer
**`footer-section`** — Dark background (`{colors.dark-bg}`, #1d1d1d) with white text. Section headings use `{typography.caption}` (13px, 500 weight) in white with 1px letter spacing and uppercase. Links use `{typography.link}` (14px, 400 weight) in `{colors.muted-soft}` (#8b8b8b). Dividers between sections use `{divider-dark}` (1px, `{colors.dark-surface}`).

### Dividers
**`divider`** — A 1px horizontal line in `{colors.hairline}` (#c7c7c7). Used between sections on light backgrounds.
**`divider-dark`** — A 1px horizontal line in `{colors.dark-surface}` (#363636). Used within the footer and other dark sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; hero font drops to 24px; button padding reduces to 10px 20px; section padding drops to 48px |
| Tablet | 744–1128px | Product grid shows 2 columns; nav links remain visible but compact; hero font at 28px |
| Desktop | 1128–1440px | Product grid shows 3 columns; full nav; standard spacing |
| Wide | > 1440px | Max-width container at 1440px; product grid shows 4 columns; increased whitespace |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (WCAG 2.1 compliant)
- Nav bar items have at least 48px touch area (full nav bar height)
- Product card images are tappable with no minimum size constraint (linked to product page)
- Search bar has 40px height, acceptable for touch but at the lower boundary

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px; the logo remains centered, cart icon remains visible
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer sections stack vertically on mobile, with headings acting as accordion toggles
- Hero section reduces vertical padding from 80px to 48px on mobile
- Secondary navigation (breadcrumbs, filters) collapses into a "Filter" button on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not reliably extractable from the live site; the `-active` variants above are inferred from common patterns
- Error state styling for form inputs (border color, icon, message typography) could not be determined
- Dark mode is not present on the live site; the `dark-bg` and `dark-surface` tokens are inferred from footer usage only
- Sub-brand or collection-specific color palettes (e.g., limited edition leather colors) are not captured
- The extracted font list is a generic system font stack; the actual brand font (likely Avenir Next or Helvetica Neue) is inferred from common usage in the leather goods DTC space
- Checkout widget colors (#00adef, #e50122, #4266b2) are Shopify/third-party defaults, not brand choices — they are noted in the palette but not used in brand components
- The extracted color list is heavily skewed toward grays and neutrals; the burnt-orange `#ee7d53` was selected as primary based on its distinctive presence in the list and its common use as an accent in leather goods e-commerce
- Animation and transition durations/easings were not extractable
- Spacing values are estimated from common e-commerce patterns; the actual grid may use different breakpoints
