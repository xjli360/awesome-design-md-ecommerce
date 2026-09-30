---
version: alpha
name: "Frey"
source_url: "https://frey.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, eco-friendly laundry care brand that uses a deep slate (#35434e) as its primary ink — an unusual choice for a category that typically defaults to bright whites and pastels — paired with a teal accent (#108474) that reads as fresh water rather than synthetic detergent. The palette is restrained: the slate anchors product photography and body text, while the teal appears in secondary CTAs and hover states, and a coral-red (#d43747) provides occasional urgency for sale badges and limited-time messaging. The canvas is a warm off-white (#f9fafb) rather than pure white, softening the overall impression and aligning with the brand's natural positioning. Typography runs on Instrument Sans, a geometric sans-serif with subtle humanist curves, set at moderate weights — display headlines use 500–600 weight rather than heavy 700, letting the product imagery and eco-certification badges carry visual weight. Buttons are softly rounded (`{rounded.md}` ~12px), not pill-shaped, and the search bar follows the same radius — the brand avoids extreme roundness in favor of a gentle, approachable geometry. The checkout flow uses a light blue-gray (#deecf2) for informational banners, and the footer collapses into a dense column of links in muted gray (#707070). Frey's design language is one of deliberate restraint: the slate ink, the teal accent, and the off-white canvas create a system that feels trustworthy, calm, and environmentally conscious without resorting to green-washing clichés.

colors:
  primary: "#35434e"
  primary-active: "#108474"
  primary-disabled: "#b3b3b3"
  ink: "#35434e"
  body: "#485c6d"
  muted: "#707070"
  muted-soft: "#9a9a9a"
  hairline: "#e6e6e6"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-coral: "#d43747"
  accent-gold: "#f8d88e"
  info-bg: "#deecf2"
  info-border: "#b9d7e4"

typography:
  display-xl:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0

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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-teal}"
    border: "1px solid {colors.accent-teal}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-active:
    textColor: "{colors.accent-teal}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.accent-teal}"
  text-input-error:
    border: "1px solid {colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.accent-teal}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.accent-teal}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-teal}"
  info-banner:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.info-border}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, used for "Add to Cart", "Subscribe", and "Checkout". Uses the deep slate ink (#35434e) as background with white text. On hover, the background shifts to the teal accent (#108474), signaling a transition from trust to action. Disabled state uses a muted gray (#b3b3b3) with white text. Corners are softly rounded at 12px (`{rounded.md}`), avoiding the extreme pill shape in favor of a gentle, approachable geometry.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white background with the slate ink for text and a 1px hairline border. On hover, the border and text shift to teal, and the background takes a soft surface tint (#f7f7f7). This button sits alongside the primary in product cards and informational sections.

**`button-tertiary-text`** — A text-only button for low-emphasis actions such as "Cancel" or "Skip". No background or border; only the slate ink text. On hover, the text color shifts to teal. Used in forms and modals where visual weight should be minimal.

**`button-pill`** — A fully rounded variant used for subscription toggles and filter chips. Uses the slate background with white text, but the radius is `{rounded.full}` (9999px) for a pill shape. Smaller padding (8px 20px) and smaller typography (`{typography.button-sm}`) make it suitable for inline use.

### Cards
**`product-card`** — The primary product display card, used on collection pages and search results. A white background (`{colors.surface-card}`) with softly rounded corners (`{rounded.md}`). The product image sits at the top with the same corner radius, and below it the title uses `{typography.title-sm}` in the slate ink, while the price uses `{typography.body-md}` in the same ink. The card has no border — it relies on the white surface against the off-white canvas for separation.

**`product-card-image`** — The image container within a product card. Uses the same `{rounded.md}` as the card itself, ensuring the image corners match the card corners. No additional padding — the image sits flush to the card edges.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height with a white background. Contains the brand logo, product category links, and utility icons (search, account, cart). Navigation links use `{typography.nav-link}` (15px, weight 500) in the slate ink. The active link or hover state shifts to the teal accent. On mobile, the nav collapses into a hamburger menu.

**`nav-link-active`** — The active state for navigation links. Text color shifts to `{colors.accent-teal}` (#108474), providing a clear visual indicator of the current page or section.

### Forms
**`text-input`** — Standard text input fields used in the checkout flow, account forms, and search. White background with a 1px hairline border (#e6e6e6) and 12px padding. On focus, the border shifts to the teal accent. Error state uses the coral-red (#d43747) border. Height is 48px for comfortable touch targeting.

**`text-input-focus`** — The focused state for text inputs. The border color changes to `{colors.accent-teal}` (#108474), providing a clear visual cue for the active field.

**`text-input-error`** — The error state for text inputs. The border color changes to `{colors.accent-coral}` (#d43747), and an error message appears below the field in the same coral color using `{typography.caption}`.

### Badges
**`badge-sale`** — A small, high-visibility badge for sale or discount items. Uses the coral-red (#d43747) background with white text, set in uppercase 11px weight 600. Corners are minimally rounded at 4px (`{rounded.xs}`). Positioned at the top-left corner of product card images.

**`badge-eco`** — A badge for eco-friendly or sustainable product attributes. Uses the teal (#108474) background with white text, same typography and radius as the sale badge. Used to highlight "Plastic-Free", "Biodegradable", or "Plant-Based" claims.

**`badge-new`** — A badge for newly launched products. Uses the gold (#f8d88e) background with the slate ink for text. Same typography and radius as other badges. The gold provides a warm, celebratory accent against the otherwise cool palette.

### Search
**`search-bar`** — The search input field, used in the navigation bar and on the search results page. White background with a 1px hairline border and 12px rounded corners (`{rounded.md}`). On focus, the border shifts to teal. Height is 44px, slightly shorter than form inputs, to fit comfortably in the nav bar.

**`search-bar-focus`** — The focused state for the search bar. The border color changes to `{colors.accent-teal}` (#108474), matching the text input focus behavior for consistency.

### Footer
**`footer`** — The site footer, using the deep slate (#35434e) as background with white text. Contains link columns for support, about, and sustainability information. Links use `{typography.link}` (14px, weight 400) and shift to teal on hover. The footer is divided into sections with generous padding (`{spacing.xl}`) between columns.

**`footer-link`** — Standard footer links in white text. Uses `{typography.link}` for consistent sizing and weight.

**`footer-link-hover`** — The hover state for footer links. Text color shifts to `{colors.accent-teal}` (#108474), providing a clear interactive cue against the dark background.

### Banners
**`info-banner`** — An informational banner used for shipping announcements, subscription details, and eco-certification highlights. Uses a light blue-gray background (#deecf2) with a matching border (#b9d7e4) and the standard body text color (#485c6d). Corners are rounded at 12px (`{rounded.md}`), and padding is 12px 16px. This banner sits above the product grid or within the cart page.

### Hero
**`hero-section`** — The full-width hero section at the top of the homepage and collection pages. White background with the slate ink for headlines and body text. Padding is 64px (`{spacing.section}`) top and bottom, with 24px (`{spacing.lg}`) on the sides. The hero contains a headline using `{typography.display-xl}`, a subheading using `{typography.body-md}`, and a primary CTA button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in single column; hero padding reduces to 32px; footer columns stack vertically; search bar moves to expandable overlay |
| Tablet | 744–1128px | Nav shows all links; product cards in 2-column grid; hero padding at 48px; footer in 2-column layout; search bar visible in nav |
| Desktop | 1128–1440px | Nav fully expanded; product cards in 3-column grid; hero at full padding; footer in 4-column layout; search bar in nav with full width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 1200px; footer columns evenly spaced |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility.
- Icon buttons in the nav (search, account, cart) are 44x44px with `{rounded.md}` for easy tapping.
- Product card CTAs are 48px tall with 12px padding for comfortable finger placement.
- Footer links have 8px vertical padding to create 44px touch targets.

### Collapsing Strategy
- On mobile (< 744px), the navigation bar collapses to a hamburger menu with a slide-out drawer.
- The product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- The footer collapses from 4 columns to 2 to a single vertical stack on mobile.
- The search bar collapses from a visible input in the nav to an expandable overlay on mobile.
- Hero sections reduce padding and font sizes on mobile to maintain proportion.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from the extracted color palette; actual hover transitions (e.g., opacity, shadow) were not extractable from the static HTML/CSS.
- Error and success states for forms (validation messages, success banners) are not present in the extracted data; the coral-red (#d43747) is used as a best-guess for error states.
- Dark mode styling is not present on the live site; no dark mode tokens are defined.
- The extracted font list includes multiple Font Awesome versions (5 and 6) and JudgemeStar (a review app) — these are not brand typography and are excluded from the typography block. Instrument Sans is the primary brand font.
- The extracted color list is heavily weighted toward grays and neutrals (20+ of 30 colors are grays, silvers, or off-whites). The teal (#108474) and coral (#d43747) are the only distinctive brand accents. The gold (#f8d88e) appears only once and may be a one-off badge color rather than a system token.
- Shopify checkout widget colors (e.g., Klarna, Afterpay) may be present in the extracted list but are not included as brand colors.
- Sub-brand or seasonal color palettes (e.g., holiday collections, limited editions) are not captured.
- Animation and transition timing values (e.g., hover fade duration, menu slide speed) are not extractable from static assets.
- The exact font sizes and weights for Instrument Sans are estimated from common web patterns; the live site may use different values.
