---
version: alpha
name: "Milk Makeup"
source_url: "https://www.milkmakeup.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Milk Makeup is a clean, vegan, and cruelty-free cosmetics brand that lives in the tension between industrial grit and soft, dewy glow. The brand's visual language is anchored on a near-black ink (`#121212`) against a raw, almost utilitarian canvas (`#dedede`), a palette that evokes concrete, steel, and the backstage of a fashion show. This is not a brand of pastels and soft pinks; its signature voltage comes from a piercing, almost electric blue (`#1990c6`) that acts as the primary CTA and accent color, a deliberate jolt against the monochrome backdrop. A deeper, more grounded navy (`#136f99`) provides active and hover states, adding depth without losing the edge. Typography is set in a clean, geometric sans-serif stack led by Calibre, with generous tracking and a mix of bold, all-caps display weights for headlines and a lighter, airier weight for body copy. The system relies on hard, unrounded corners (`{rounded.none}`) for buttons and cards, reinforcing the brand's no-fuss, "just roll it on" ethos, while pill-shaped applicator tips and product caps introduce the only organic curves (`{rounded.full}`). The overall mood is confident, minimalist, and slightly rebellious — a makeup brand that feels more like a streetwear label than a beauty counter.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#a0d4eb"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#dedede"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  badge-new: "#1990c6"
  badge-sale: "#121212"
  star-rating: "#121212"
  error: "#c13515"
  success: "#136f99"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0
  title-lg:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  body-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Calibre', 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.20
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
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
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.display-xl}"
    height: 600px
  hero-banner-image-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-ink}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  swatch-color:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  swatch-color-selected:
    border: "2px solid {colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a solid blue (`{colors.primary}`) rectangle with hard corners (`{rounded.none}`) and bold, uppercase typography (`{typography.button-md}`). On hover, it shifts to the deeper navy (`{colors.primary-active}`). The disabled state uses a muted, desaturated blue (`{colors.primary-disabled}`) with the same white text. **`button-secondary`** — An outlined button with a transparent fill, a 2px solid black (`{colors.ink}`) border, and the same hard-cornered, uppercase treatment. On hover, the background fills with black and text inverts to white. **`button-tertiary-text`** — A text-only button with no background or border, used for less prominent actions like "View All" or "Cancel". It uses the same bold uppercase style but with no container. **`button-pill`** — A pill-shaped variant (`{rounded.full}`) reserved for product badges, filter tags, or secondary CTAs in hero banners. It uses the primary blue background with a smaller, tighter uppercase font (`{typography.button-sm}`).

### Cards
**`product-card`** — The core product display unit, a white (`{colors.surface-card}`) rectangle with no rounding, containing a product image on a soft gray (`{colors.surface-soft}`) background, a title in `{typography.title-sm}`, and a muted price in `{typography.body-sm}`. The card has no padding at the container level; spacing is handled internally. **`product-card-badge`** — A small, hard-cornered tag overlaid on the product image, typically in the primary blue for "NEW" or black for "SALE", using the `{typography.badge}` style.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar with a raw canvas background (`{colors.canvas}`), a single hairline bottom border (`{colors.hairline}`), and uppercase, tightly-spaced nav links (`{typography.nav-link}`). The bar is 64px tall. **`nav-link-active`** — The active state of a navigation link, indicated by a 2px solid black (`{colors.ink}`) bottom border. **`nav-link-inactive`** — Inactive links are rendered in a muted gray (`{colors.muted}`) with no underline or border.

### Forms
**`text-input`** — A standard text input field with a white background, a 1px hairline border (`{colors.hairline}`), and hard corners. On focus, the border thickens to 2px and turns primary blue (`{colors.primary}`). Error states use a red border (`{colors.error}`). **`select-input`** — A styled select dropdown matching the text input's dimensions and border treatment. **`textarea`** — A multi-line text input with the same styling as `text-input`, but with a taller default height and no fixed height constraint. **`quantity-selector`** — A compact, bordered control with a central numeric display and two square buttons on either side for increment/decrement, all with hard corners.

### Hero & Search
**`hero-banner`** — A full-width, 600px tall hero section with a black (`{colors.ink}`) background and white text, featuring a large, uppercase headline (`{typography.display-xl}`) and a primary blue CTA button. A semi-transparent black overlay (`{colors.scrim}` at 30% opacity) sits over the background image for readability. **`search-bar`** — A standard search input styled identically to `text-input`, used in the navigation or on search results pages. On focus, it adopts the primary blue border.

### Footer
**`footer`** — A full-width footer with a black (`{colors.ink}`) background and white text. Links are styled as `{typography.link}` with no underline by default, gaining an underline on hover. The footer uses generous vertical padding (`{spacing.section}`) and horizontal padding (`{spacing.lg}`).

### Badges & Swatches
**`badge-new`** and **`badge-sale`** — Small, hard-cornered rectangular tags used to flag product attributes. "NEW" uses the primary blue background; "SALE" uses black. Both use the `{typography.badge}` style. **`swatch-color`** — A circular color swatch (32x32px) used for shade selection. The selected state is indicated by a 2px black (`{colors.ink}`) border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, hero banner height reduces to 400px, font sizes scale down by 2-4px, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, top nav remains but with condensed link spacing, hero banner at 500px, side-by-side footer columns |
| Desktop | 1128–1440px | Three- or four-column product grid, full top nav with all links visible, hero banner at 600px, standard footer layout |
| Wide | > 1440px | Max-width container (1440px) centered on screen, product grid can expand to four or five columns, hero banner content is centered within the max-width container |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Icon buttons are 40x40px, meeting the minimum touch target.
- Product card images and titles are tappable, with the entire card area acting as a link.
- Swatches are 32x32px, which is below the 44px minimum; they are wrapped in a larger touch-friendly container.

### Collapsing Strategy
- The top navigation collapses into a hamburger menu on mobile (< 744px). The menu overlay slides in from the left or right, containing all primary and secondary links.
- The product grid collapses from multi-column to single-column on mobile.
- The footer's multi-column layout collapses to a single vertical stack on mobile.
- Hero banner content (headline, subtitle, CTA) stacks vertically on mobile, with the CTA button expanding to full width.
- Accordion components are used on mobile to collapse sections like product details, shipping information, and FAQ content.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components (e.g., subtle color shifts, box shadows) could not be fully extracted from the live site.
- Error and success styling for forms (e.g., error messages, success indicators) is inferred from common patterns but not confirmed.
- Dark mode or high-contrast mode styles are not present on the live site and are not defined.
- Sub-brand or collection-specific palettes (e.g., limited edition drops) are not captured.
- The exact font weight for `Calibre` in different contexts (e.g., 500 vs 600) is an approximation based on visual inspection.
- Animation and transition durations (e.g., button hover, menu slide-in) are not specified.
- The `meta theme-color` tag is absent, so the browser chrome color is not defined.
- The `hairline` color (`#dedede`) is very close to the `canvas` color, which may cause contrast issues on some screens; this is a known brand choice.
