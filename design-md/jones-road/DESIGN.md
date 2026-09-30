---
version: alpha
name: "Jones Road"
source_url: "https://jonesroadbeauty.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A beauty brand that trusts the quiet authority of a single accent — #ff5742, a coral-red that appears only on the primary CTA and the occasional badge, never in the hero imagery or product photography. The rest of the palette is a study in near-neutral: #9da1a0, #868a89, #6c706f, #7e7e7e, #8f8f8f, #b6b9b8 — a dozen grays and greiges that read as "clean" without shouting "minimal." The canvas is #fafafa, a warm off-white that avoids the sterile glare of #ffffff, while #121212 and #1a1a1a provide ink-weight for headlines. Articulat CF and Ringside Wide carry the typographic load — condensed, architectural sans-serifs that feel editorial rather than cosmetic. The brand's signature move is restraint: product cards use {rounded.sm} corners, buttons use {rounded.sm}, and the only pill shape is the search bar at {rounded.full}. There is no hero carousel of models; instead, product shots float on {surface-soft} panels with generous whitespace. The checkout flow introduces #4efac0 (a minty accent) and #0018ff (a saturated blue) — likely Shopify Pay and Klarna widgets, not brand colors. The overall effect is a storefront that feels more like a gallery than a beauty counter: muted, deliberate, and letting the product be the color.

colors:
  primary: "#ff5742"
  primary-active: "#e04a37"
  primary-disabled: "#f5b8b0"
  ink: "#121212"
  body: "#1a1a1a"
  muted: "#7e7e7e"
  muted-soft: "#9da1a0"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-mint: "#4efac0"
  accent-blue: "#0018ff"
  badge-green: "#00b84a"
  badge-red: "#e61b1b"
  star-rating: "#121212"

typography:
  display-xl:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Articulat CF', 'Ringside Wide', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: 1px solid "{colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.ink}"
  text-input-error:
    border: 1px solid "{colors.badge-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-subheading:
    typography: "{typography.display-sm}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.ink}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The single brand voltage. A coral-red (#ff5742) rectangle with white text, 8px corners, and 14px vertical padding. Used for "Add to Bag," "Checkout," and primary form submissions. On hover, darkens to `{colors.primary-active}` (#e04a37). Disabled state fades to a pale coral `{colors.primary-disabled}` (#f5b8b0) with no border change. **`button-secondary`** — An outlined variant on a white canvas with ink text and a 1px hairline border. Used for "Learn More" and secondary actions. Hover adds a subtle shadow or darkens the border. **`button-tertiary-text`** — A text-only button with no background or border. Used for "Cancel," "Clear," and inline actions. Hover underlines or shifts opacity. **`button-pill-primary`** — A fully rounded pill version of the primary button, used for "Subscribe" or "Shop Now" in hero sections. Smaller padding (10px 20px) and smaller type.

### Cards
**`product-card`** — A white card on `{colors.surface-soft}` with 8px corners and 16px padding. The product image sits in a `{colors.surface-soft}` panel with matching 8px corners. Title uses `{typography.title-sm}` (16px/500), price uses `{typography.body-sm}` in `{colors.muted}`. Badges (New, Sale) are small uppercase labels in green or red with 4px corners. Cards are laid out in a responsive grid with generous gutters. No shadow — the brand trusts flat design and whitespace over depth.

### Navigation
**`nav-bar`** — A 72px white bar with uppercase nav links in 14px/500. Active links have a 2px ink underline. Inactive links are `{colors.muted}`. The logo sits left, links center or right. On mobile, the nav collapses into a hamburger menu with a full-screen overlay. **`nav-link-active`** and **`nav-link-inactive`** define the two states.

### Forms
**`text-input`** — A 48px white input with 8px corners and a 1px hairline border. On focus, the border switches to `{colors.ink}`. Error state uses `{colors.badge-red}` (#e61b1b). Placeholder text is `{colors.muted-soft}`. Used for email, search, and address fields. **`quantity-selector`** — A smaller 40px input for cart quantities, with plus/minus buttons on either side.

### Search
**`search-bar`** — A 48px pill-shaped input with a full rounded border. White background, ink text, and a 1px hairline border. On focus, the border becomes ink. Used in the nav bar and on the search results page. The pill shape is the only `{rounded.full}` element in the system, making it distinctive.

### Footer
**`footer-section`** — A `{colors.surface-soft}` (#f3f3f3) section with `{colors.muted}` links and body text. Links are 14px/400. On hover, links shift to `{colors.ink}`. The footer includes columns for Customer Service, About, and Social links. No background image or heavy decoration — just clean typography and spacing.

### Badges
**`badge-new`** — A small uppercase label in `{colors.primary}` with white text, 4px corners, and 2px 8px padding. Used on new arrivals. **`badge-sale`** — Same structure but in `{colors.badge-red}` (#e61b1b). Both use `{typography.badge}` (11px/600/uppercase).

### Accordion
**`accordion-header`** — A clickable row with a title in `{typography.title-sm}` and a chevron icon. Bottom border is `{colors.hairline-soft}`. On click, the `accordion-content` panel slides open with body text in `{typography.body-sm}`. Used for product descriptions, ingredients, and FAQ sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero heading drops to 32px; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero heading at 40px; buttons remain inline |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero heading at 48px; standard button sizing |
| Wide | > 1440px | Max-width container (1440px) centered; four-column product grid; hero heading at 52px; extra whitespace on sides |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (48px preferred) to meet WCAG touch target guidelines.
- Nav links have 48px tap areas even if the text is smaller.
- Quantity selector plus/minus buttons are 40px × 40px.
- Search bar is 48px tall with 20px horizontal padding for easy tapping.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger icon. The full nav menu appears as a full-screen overlay with vertical links and 48px tap targets.
- Product grids collapse from 3 columns to 2 (tablet) to 1 (mobile).
- Footer columns stack vertically on mobile, with accordion-style expandable sections for each column.
- Hero sections reduce padding from 64px to 32px on mobile.
- Badges remain visible but may shift to a smaller size on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from common patterns; exact color transitions (e.g., `primary-active`) are estimated from the extracted primary.
- Error styling for forms (border color, error message typography) is assumed; no error-specific hexes were extracted.
- Dark mode is not present on the live site; no dark-mode palette is available.
- Sub-brand or collection-specific palettes (e.g., limited-edition drops) are not captured.
- The extracted font list includes "Base Mono" and "Brown" and "Canela" — these may be used for specific editorial sections or product descriptions, but their usage context is unknown.
- The extracted colors include #4efac0 (mint) and #0018ff (blue) — these are likely Shopify Pay/Klarna/Afterpay checkout widgets, not brand colors. They are noted as `accent-mint` and `accent-blue` but should be used sparingly.
- No animation or transition timing values were extracted (e.g., button hover duration, accordion slide speed).
- The `star-rating` color is assumed to match `ink` (#121212) based on common patterns; the actual rating color may differ.
- No data on focus-visible styles, keyboard navigation outlines, or accessibility skip-links.
