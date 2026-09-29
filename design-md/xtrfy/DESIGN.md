---
version: alpha
name: "Xtrfy"
source_url: "https://xtrfy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A competitive gaming hardware brand that uses #e50043 as its primary voltage — a red that sits between cherry and stop-sign, deployed as the sole accent across an otherwise monochrome palette of #eeeeee, #f7f7f7, #222222, and #36383a. The brand's visual system is built on contrast: pure white (#ffffff) canvases against deep near-black (#161e22) product photography backdrops, with #ede939 (a sharp yellow) and #d90001 (a darker crimson) appearing as secondary accents for limited-edition drops and badge highlights. Typography runs din-2014 at display sizes — a geometric sans-serif with military precision — paired with Arial/Helvetica Neue for body copy, creating a hierarchy where headlines feel engineered and body text recedes. Navigation is a full-width black bar (#222222) with white text, no logo mark visible at the top level, signaling that the brand trusts its product imagery and red dot to do the identification work. Buttons are pill-shaped ({rounded.full}) with the primary red fill, while secondary actions use outlined or ghost treatments against the dark nav. The overall mood is industrial, competitive, and unadorned — there is no gradient, no shadow play, no decorative illustration. Every design decision reads as a performance choice.

colors:
  primary: "#e50043"
  primary-active: "#d90001"
  primary-disabled: "#f7f7f7"
  accent-yellow: "#ede939"
  accent-yellow-soft: "#ffff99"
  accent-yellow-dark: "#dcd836"
  ink: "#222222"
  body: "#36383a"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#e2e2e2"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#161e22"
  surface-nav: "#222222"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-nav: "#ffffff"
  badge-red: "#b91d47"
  badge-blue: "#5bbad5"
  badge-gray: "#888888"

typography:
  display-xl:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'din-2014', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    padding: 12px 32px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 44px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 44px
  button-ghost-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-nav}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-nav}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-blue:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
    height: 36px
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 40px"
    height: 48px
  hero-cta-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 40px"
    height: 48px
    border: "2px solid {colors.on-dark}"
  footer:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.on-nav}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "2px solid {colors.primary}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  section-heading-on-dark:
    typography: "{typography.display-md}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.lg} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand red (#e50043) fill with white uppercase din-2014 text at 14px, fully pill-shaped ({rounded.full}). Hover transitions to the darker active state (#d90001). Disabled state drops to a light gray (#f7f7f7) fill with muted text, signaling non-interactivity. Found on product cards, hero sections, and cart actions.

**`button-secondary`** — An outlined variant with a 2px solid ink (#222222) border on a transparent background. Used for secondary actions like "Learn More" or "View All" in contexts where the primary button is already present. Active state fills the button with ink and inverts text to white.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip." On dark backgrounds (hero, nav), the ghost variant uses white text (`button-ghost-on-dark`).

### Cards
**`product-card`** — A minimal, borderless card with a white background and no rounding. The product image sits flush against the top edge, with the title, badge, price, and add-to-cart button stacked below. Badges use the brand red (`product-card-badge`) for "New" or "Sale," yellow (`product-card-badge-yellow`) for limited editions, and blue (`product-card-badge-blue`) for "Pre-order" or "Exclusive."

### Navigation
**`nav-bar`** — A full-width black (#222222) bar at 64px height, housing the brand logo (left) and nav links (right). Links are uppercase din-2014 at 14px with 0.5px letter-spacing. The active link uses the brand red (#e50043) for its text color. No dropdown menus are present at the top level — navigation is flat and direct.

### Forms
**`text-input`** — Standard input fields with a white background, 1px hairline (#e2e2e2) border, and 8px rounding. On focus, the border thickens to 2px and switches to the brand red. Used in search, newsletter signup, and checkout flows.

### Hero
**`hero-section`** — A full-width section with a dark (#161e22) background, used for product launches and campaign headers. The primary CTA uses the red pill button, while a secondary ghost button sits beside it for supplementary actions. Headlines are display-xl (48px) din-2014 in white.

### Footer
**`footer`** — A dark (#222222) footer with muted gray (#aaaaaa) links and body text. Links hover to white. No decorative elements — just a column layout of product categories, support links, and legal text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack single-column; hero text reduces to 28px; buttons become full-width; footer links stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero text at 36px; side padding reduces to 24px |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero at full width with 48px headline; standard side padding of 32px |
| Wide | > 1440px | Max-width container at 1440px centered; product cards in 4-column grid; hero content centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Nav links have 44px minimum tap area (padding included)
- Product card add-to-cart buttons are 36px height on desktop, 44px on mobile
- Search bar maintains 44px height across all breakpoints

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-in drawer from the left
- Product grids collapse from 4-column → 2-column → 1-column as viewport shrinks
- Hero sections stack vertically on mobile (headline above CTA, no side-by-side layout)
- Footer links collapse from inline rows to stacked columns below 744px
- Badges remain visible on all breakpoints but reduce font size to 10px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow, scale, or border change) could not be reliably extracted from the live site
- Error states for form inputs (red border, error message styling) were not observed in the extracted data
- Dark mode is not present on the live site; all pages use light canvas (#ffffff) or dark nav (#222222) as fixed backgrounds
- Sub-brand palettes (e.g., CHERRY XTRFY collaborations) may use additional accent colors not captured in the top hex list
- The extracted font list includes "dearflip" and "themify" which appear to be plugin-specific fonts, not part of the brand's core typography system
- Loading states (spinners, skeletons) were not observed in the extracted data
- The brand may use animation or transition timing values (e.g., 200ms ease-in-out) that could not be extracted
- Accessibility contrast ratios for the yellow accent (#ede939) on white backgrounds have not been verified
- The extracted hex list includes many near-identical grays (#eeeeee, #efefef, #f1f1f1, #f3f3f3, #f7f7f7) — the exact surface-soft value may vary by context
- Checkout flow styling (Shopify-specific) was not fully captured; the extracted list may include widget colors from third-party payment providers
