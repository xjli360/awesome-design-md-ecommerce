---
version: alpha
name: "KRK Systems"
source_url: "https://www.krkmusic.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A studio-monitor brand that uses its own product as the interface metaphor — the signature yellow cone of the Rokit series becomes the brand’s primary voltage (#f8c423), a high-visibility accent that appears on every CTA, badge, and interactive element against a near-black chassis (#202223) and deep ink (#111111). The brand lives in extremes of contrast: pure white canvas (#f8f8f8) against the dark body, with a muted mid-tone (#6d7175) and a soft structural gray (#c5c8d1) for borders and secondary text. Inter runs across the system at clean, modest weights — no display faces, no decorative typography — letting the product photography and the yellow cone do all the emotional work. Buttons are sharp-cornered rectangles with tight padding, echoing the physical shape of a monitor enclosure. The nav bar is a thin, dark strip with white text, and product cards sit on white with a yellow accent strip, mimicking the physical product’s front baffle. The system trusts high contrast and a single accent color over any secondary palette — there is no gradient, no illustration, no decorative flourish. The yellow is not warm or playful; it is functional, industrial, and precise, like a reference monitor’s calibration mark.

colors:
  primary: "#f8c423"
  primary-active: "#d4a81e"
  primary-disabled: "#fce89a"
  ink: "#111111"
  body: "#202223"
  muted: "#6d7175"
  muted-soft: "#c5c8d1"
  hairline: "#c5c8d1"
  hairline-soft: "#e0e1e5"
  canvas: "#f8f8f8"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#111111"
  on-dark: "#ffffff"
  badge-yellow: "#f8c423"
  badge-text: "#111111"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.body}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
  button-yellow-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #d32f2f"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
  product-card-accent-strip:
    backgroundColor: "{colors.primary}"
    height: 4px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "#d32f2f"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s signature yellow (#f8c423) against dark text (#111111). Sharp corners and tight 12px vertical padding give it a precise, industrial feel. On hover, the yellow deepens to #d4a81e. The disabled state uses a pale yellow (#fce89a) with muted text (#6d7175), signaling inactivity without visual noise.
**`button-secondary`** — A white button with a thin gray border (#c5c8d1) and dark body text (#202223). Used for secondary actions like “Learn More” or “Compare.” On hover, the border darkens to the body color and the background shifts to a soft gray (#f0f0f0). The ghost variant removes the border entirely for text-only actions.
**`button-yellow-pill`** — A compact, fully rounded pill button in yellow, used for small badges, filter tags, or inline actions. Uses the smaller button typography (12px, 600 weight) and 8px vertical padding. This is the only pill-shaped element in the system — a deliberate departure from the otherwise sharp-cornered aesthetic.

### Navigation
**`nav-bar`** — A thin, 56px-high dark strip (#111111) with white uppercase navigation links. The nav uses 13px type at 600 weight with 0.5px letter spacing — tight and technical. Active links switch to the brand yellow (#f8c423). The bar spans full width and sits fixed at the top. No dropdowns, no mega-menus — just a flat list of product categories and support links.
**`nav-link`** — Uppercase, 13px, 600 weight, with 0.5px letter spacing. Inactive links are white; active links are yellow. No underline or background change — only color signals state.

### Cards
**`product-card`** — A white card with a 1px soft gray border (#e0e1e5) and no border radius. Each card features a 4px yellow accent strip at the top, mimicking the physical front baffle of a KRK monitor. On hover, the border darkens to #c5c8d1. The card contains a product image (using `object-fit: contain`), the product name in title-md, a price in body-md, and a badge-new or badge-sale if applicable.
**`badge-new`** — A small yellow rectangle with uppercase 11px bold type and 2px horizontal padding. Used to flag new products. The sale variant uses red (#d32f2f) with white text.

### Forms
**`text-input`** — A white input field with a 1px gray border (#c5c8d1) and no border radius. On focus, the border becomes a 2px yellow line (#f8c423). Error state uses a 2px red border (#d32f2f). The input height is 48px with 12px vertical padding, matching the button height for alignment in forms.
**`quantity-selector`** — A compact input for cart quantities, matching the text-input style but at 44px height. Used alongside buttons in product detail views.

### Footer
**`footer`** — A dark section (#111111) with white body text and gray links (#c5c8d1). Links turn yellow on hover. The footer uses 14px body-sm type for text and 14px link type for navigation. Padding is 48px top/bottom with 24px left/right. Dividers between sections use the hairline color (#c5c8d1) at 1px.

### Accordion
**`accordion-header`** — A white row with 14px bold type and 16px padding. No border radius. The header toggles the content panel below. The content panel uses body-sm type with 12px padding on sides and 24px at the bottom. Used for product specifications and FAQ sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in single column. Hero section reduces display-xl to 24px. Footer links stack vertically. |
| Tablet | 744–1128px | Nav bar shows all links but reduces font size to 12px. Product cards display in 2-column grid. Hero section uses 28px display type. |
| Desktop | 1128–1440px | Full nav bar with 13px links. Product cards in 3-column grid. Hero section uses 32px display type. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. Hero section remains at 32px but with larger padding. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav bar hamburger icon is 48px × 48px on mobile.
- Quantity selector and text inputs are 44px and 48px respectively, exceeding the 44px minimum.
- Footer links have 24px vertical padding between items on mobile for easy tapping.

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu with a slide-out drawer. The drawer uses the same dark background (#111111) and white/yellow link colors.
- Product detail accordions are collapsed by default on all breakpoints, expanding on click.
- The hero section’s secondary text (body-md) is hidden on mobile, showing only the headline and primary CTA.
- Footer link columns collapse into a single vertical list below 744px, with each section separated by a hairline divider.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is sparse and heavily weighted toward grayscale (#202223, #111111, #f8f8f8, #6d7175, #c5c8d1) with a single yellow accent (#f8c423). This is consistent with a minimal, industrial brand, but hover states for secondary elements (e.g., product-card-hover) were inferred from the general design language rather than extracted.
- Font-family declarations returned only "Inter" and "object-fit: contain". No fallback stacks or additional weights were found. The typography block uses a standard system fallback chain.
- No meta theme-color was found, so the browser chrome color is unknown.
- No error, success, or warning color tokens could be extracted beyond the red inferred for sale badges.
- Dark mode is not supported on the live site; all extracted colors assume a light theme.
- The `object-fit: contain` declaration was found on product images but no specific image aspect ratios or container sizes could be extracted.
- No animation or transition durations were found in the extracted CSS.
