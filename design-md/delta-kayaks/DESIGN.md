---
version: alpha
name: "Delta Kayaks"
source_url: "https://www.deltakayaks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-navy hull (#143a57) meets a single electric-green accent (#83e20c) — the brand voltage of a company that builds lightweight thermoform kayaks in North America and trusts the product photography to do the selling. The extracted palette is dominated by a cool navy primary, a near-black ink (#222222), and a family of warm grays (#ededed, #ebebeb, #eeeeee) that form a soft, almost tactile canvas — the kind of surface that suggests a boat hull under your fingers. The accent green (#83e20c) appears sparingly: a CTA button, a badge, a link hover — never more than one per viewport. The typography stack runs Roboto and Bebas Neue, the latter used for display-weight headlines that read as condensed, athletic, and purposeful — a font choice that echoes the streamlined shape of a touring kayak. Buttons are pill-shaped (`{rounded.full}`) in the primary navy, with the green reserved for the single strongest action. Product cards use generous whitespace, a soft shadow, and a `{rounded.lg}` corner that mirrors the rounded bow of the boats themselves. The footer is dense and dark (`{colors.ink}`), anchoring the page like a keel. There is no hero video, no parallax — the brand trusts a single hero image of a kayak on flat water, the horizon line clean, the color temperature cool. The extracted hex list is heavy on grays and blues, but the green (#83e20c) is the tell: it is not a social-icon color, not a checkout widget — it is the brand's deliberate accent, used with restraint.

colors:
  primary: "#143a57"
  primary-active: "#0f2d44"
  primary-disabled: "#a0b8cc"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#888888"
  hairline: "#d9d9d9"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#83e20c"
  accent-green-hover: "#6bbf0a"
  accent-blue: "#0caeff"
  accent-blue-hover: "#0693e3"
  badge-sale: "#da4c26"
  badge-new: "#003388"
  star-rating: "#55acee"
  footer-bg: "#1e2a36"
  footer-text: "#b2b2b2"

typography:
  display-xl:
    fontFamily: "'Bebas Neue', 'Arial Narrow', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
  display-lg:
    fontFamily: "'Bebas Neue', 'Arial Narrow', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Bebas Neue', 'Arial Narrow', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.25px
  title-lg:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
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
  button-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-green-hover}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  button-pill-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
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
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: 500px
  hero-overlay:
    backgroundColor: "rgba(20, 58, 87, 0.6)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  search-bar-icon:
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-green}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full-pill in deep navy (`{colors.primary}`) with white uppercase Roboto at 15px/600. Used for "Shop Now", "Add to Cart", and "View Details" across product cards and the hero section. On hover, shifts to `{colors.primary-active}` (#0f2d44). Disabled state uses `{colors.primary-disabled}` (#a0b8cc).

**`button-accent`** — The single electric-green (`{colors.accent-green}`) button reserved for the most urgent action on the page: "Get a Quote", "Limited Stock", or "Sale". Uses dark ink text (`{colors.ink}`) for contrast against the bright green. Hover shifts to `{colors.accent-green-hover}` (#6bbf0a). Use no more than one per viewport.

**`button-secondary`** — An outlined pill with a white fill, navy border (`2px solid {colors.primary}`), and navy text. Used for "Learn More" or "Compare Models" — actions that are secondary to the primary CTA but still on-brand. Hover inverts to a filled navy button.

**`button-tertiary`** — A text-only button with no background or border, used for "Cancel", "Back to Results", or "Read Reviews". Inherits navy text and uppercase button typography. Hover adds a subtle underline.

### Cards
**`product-card`** — A white card with a `{rounded.lg}` corner (16px), a soft shadow (`0 2px 8px rgba(0,0,0,0.08)`), and no padding on the image area. The product image fills the top, with a `{rounded.lg}` top radius. Below, the title uses `{typography.title-md}` with 16px padding on all sides, and the price uses `{typography.price}` (20px/600 Roboto). On hover, the shadow deepens to `0 8px 24px rgba(0,0,0,0.12)`.

**`product-card-badge`** — A small, sharp-cornered (`{rounded.xs}`) badge overlaid on the product image. Sale badges use `{colors.badge-sale}` (#da4c26), new-arrival badges use `{colors.badge-new}` (#003388). Text is 11px/700 uppercase Roboto in white.

### Navigation
**`nav-bar`** — A 72px white bar with a subtle bottom border (`1px solid {colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — 14px/500 Roboto, uppercase, with 0.3px letter spacing. The active page is indicated by a 2px navy bottom border on the link. Hover shifts the link text to `{colors.primary}`.

**`breadcrumb`** — Small gray (`{colors.muted}`) caption text at 13px/400, used above product titles. The active (current) breadcrumb uses `{colors.ink}`.

### Forms
**`text-input`** — A white input field with a `{rounded.sm}` corner (8px), 1px `{colors.hairline}` border, and 16px body text. On focus, the border thickens to 2px `{colors.primary}`. Error state uses a 1px `{colors.badge-sale}` border.

**`select-input`** — Matches the text-input styling but includes a dropdown arrow icon in `{colors.primary}`. Used for sorting and filtering product listings.

### Hero
**`hero-section`** — A 500px tall section with a `{colors.primary}` background, overlaid with a semi-transparent navy scrim (`rgba(20, 58, 87, 0.6)`) on the background image. Headlines use `{typography.display-xl}` (48px Bebas Neue). A single `{typography.body-md}` paragraph sits below the headline. The hero contains one `button-primary` and one `button-secondary`.

### Search
**`search-bar`** — A full-pill white search field with a 56px height, 24px horizontal padding, and a prominent shadow (`0 4px 16px rgba(0,0,0,0.1)`). The search icon is `{colors.primary}`. Placeholder text uses `{typography.body-md}` in `{colors.muted}`.

### Footer
**`footer`** — A dark section (`{colors.footer-bg}` #1e2a36) with light gray text (`{colors.footer-text}` #b2b2b2). Column headings use `{typography.title-md}` in white. Links hover to `{colors.accent-green}`. Padding is 48px top/bottom, 24px left/right.

### Accordion
**`accordion-header`** — A soft-gray (`{colors.surface-soft}`) bar with `{rounded.sm}` corners, 12px padding top/bottom, 16px left/right. Uses `{typography.title-md}` (18px/500 Roboto). Click toggles the accordion content below.

**`accordion-content`** — A white panel with 16px padding on all sides, using `{typography.body-md}`. Used for product specifications, shipping details, and FAQ sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero height reduces to 300px. Product cards stack in single column. Nav-bar collapses to hamburger menu. Button padding reduces to 12px 24px. Footer columns stack. Search bar width becomes 100%. |
| Tablet | 744–1128px | Hero height at 400px. Product cards in 2-column grid. Nav-bar shows top-level links only. Footer in 2-column layout. Search bar at 60% width. |
| Desktop | 1128–1440px | Full hero at 500px. Product cards in 3-column grid. Full nav-bar visible. Footer in 4-column layout. Search bar at 40% width. |
| Wide | > 1440px | Max-width container at 1440px, centered. Hero image scales to fill. Product cards in 4-column grid. All proportions maintain. |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px standard).
- Nav-bar links have 48px touch targets (padding + height).
- Product card tap targets: entire card is clickable, minimum 200px height.
- Search bar: 56px height for easy thumb access.
- Accordion headers: 48px minimum tap target.

### Collapsing Strategy
- Nav-bar collapses to hamburger menu on mobile (< 744px). Secondary nav links move to a slide-out drawer.
- Product filters collapse to a single "Filter" button on mobile, opening a modal overlay.
- Footer columns stack vertically on mobile, with accordion-style expand/collapse for each column.
- Hero text overlay reduces font size and padding on mobile, with the CTA buttons stacking vertically.
- Product card badges shift from top-left to top-center on mobile for better visibility.
- Breadcrumbs truncate to "Home > ... > Current Page" on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex list is heavily weighted toward grays, blues, and one bright green (#83e20c). The green is the most distinctive accent, but its exact usage (hover states, disabled variants, text-on-green contrast) is inferred, not extracted. The brand may use additional accent colors not captured.
- Font-family extraction returned a mix of system fonts (Arial, Helvetica, Georgia) and two named fonts (Roboto, Bebas Neue). Bebas Neue is assumed to be the display/headline font based on common usage in the watersports industry, but its exact weight and spacing are inferred. Roboto is the most likely body font.
- No meta theme-color was found — the brand may not use a browser chrome color, or it may be set dynamically.
- Hover states for buttons, cards, and links are inferred from common patterns (darken primary, lighten accent, deepen shadow). Exact extracted values are not available.
- Error states for forms (validation messages, error icons) are not extracted. The error border color (#da4c26) is taken from the extracted badge-sale color, which may or may not be the intended error color.
- Dark mode is not detected. The brand may not support it.
- Sub-brand or seasonal color palettes (e.g., holiday sales, new model year) are not captured.
- The extracted color list may include colors from Shopify widgets, social media icons, or stock photography that are not part of the brand's design system. The navy (#143a57) and green (#83e20c) are the most likely brand colors, but this is an inference.
- No spacing or rounded corner values were extractable from CSS — all values are set to common e-commerce defaults and should be verified against the live site's computed styles.
- The brand's logo color (if different from the primary) is not extracted.
