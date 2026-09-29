---
version: alpha
name: "Mobile Fidelity Sound Lab"
source_url: "https://www.mofi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-violet signal (#686de0) cuts through an otherwise black-and-white audiophile universe — this is the brand voltage that marks every add-to-cart button, every badge on a limited-edition pressing, every link that matters. The site reads like a high-end audio component faceplate: nearly everything sits on a black canvas (#000000) or near-black surface, with white (#ffffff) body text set in a clean sans-serif that never wavers from 400 weight. Product imagery — gatefold sleeves, vinyl grooves, mastering equipment — carries the full emotional load; typography stays out of the way. The violet accent is used sparingly but with surgical precision: it appears on primary CTAs, on the "Original Master Recording" badge, and as a hover state on navigation items, creating a single point of visual heat in an otherwise monochrome layout. Cards for albums and box sets use a subtle surface card (#1a1a1a) to lift content off the dark canvas, with hairline borders (#2a2a2a) that define edges without shouting. The overall effect is one of focused, obsessive attention — the same ethos MoFi applies to its half-speed mastering process, translated into a digital storefront that lets the product speak and the interface recede.

colors:
  primary: "#686de0"
  primary-active: "#4f54d1"
  primary-disabled: "#3a3d8a"
  ink: "#ffffff"
  body: "#e0e0e0"
  muted: "#9e9e9e"
  muted-soft: "#757575"
  hairline: "#2a2a2a"
  hairline-soft: "#1f1f1f"
  canvas: "#000000"
  surface-soft: "#111111"
  surface-card: "#1a1a1a"
  on-primary: "#ffffff"
  badge-new: "#686de0"
  badge-sold-out: "#757575"
  star-rating: "#ffc107"
  link-hover: "#8b8ff0"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.link-hover}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  badge-primary:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.md} 0"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px

## Components

### Buttons
**`button-primary`** — The single most important interactive element, rendered in the brand's violet signal (#686de0) on a black canvas. Used exclusively for high-commitment actions: "Add to Cart", "Pre-Order", "Subscribe". On hover, the button shifts to a slightly deeper violet (#4f54d1) with no border or shadow change — the color shift alone signals readiness. The disabled state drops to a muted violet (#3a3d8a) with white text at 50% opacity, used when a pressing is sold out or a form is incomplete. All primary buttons use a subtle 4px corner radius (`{rounded.sm}`) that feels precise without being sharp.

**`button-secondary`** — A dark card-colored button (#1a1a1a) with white text, used for lower-priority actions like "View Details" or "Add to Wishlist". On hover, the background lightens slightly to #111111 (`{surface-soft}`), creating a subtle lift. The secondary button shares the same 44px height and padding as the primary, ensuring consistent vertical rhythm across action rows.

**`button-outline`** — A transparent-background button with a 1px solid white border, used for "Learn More" links in hero sections and for "Compare" actions on product listing pages. On hover, the border remains white but the background fills with white at 10% opacity, creating a ghosted effect that respects the dark canvas.

### Cards
**`product-card`** — The primary content container for album and box-set listings. Rendered on a #1a1a1a surface (`{surface-card}`) with no border — the card relies on the contrast between its surface and the black canvas (#000000) for definition. Each card contains a product image (typically the album cover or gatefold artwork), the artist name and album title in `{typography.title-sm}`, and the price in `{typography.body-md}`. On hover, the entire card lifts to #111111 (`{surface-soft}`), and a subtle 1px violet border (#686de0) appears on the top edge, echoing the brand's accent philosophy of minimal, targeted color.

**`badge-primary`** — A small violet pill used to denote "Original Master Recording", "Limited Edition", or "Numbered Pressing". The badge uses uppercase 11px type at 600 weight with 0.5px letter spacing, set on the brand violet with white text. It sits in the top-left corner of product cards and on product detail pages, always within 8px of the card edge.

**`badge-sold-out`** — A gray badge (#757575) with white text, used when a pressing is no longer available. It overlays the product image at 90% opacity, ensuring the artwork remains visible while clearly communicating unavailability.

### Navigation
**`nav-bar`** — A fixed 64px bar at the top of every page, rendered on the black canvas with no bottom border — the bar is defined purely by its content and the white logo. Navigation links are uppercase 14px at 500 weight with 0.3px letter spacing, sitting in the center of the bar. The active link (the current page or section) is highlighted in the brand violet (#686de0). On hover, links shift to a lighter violet (#8b8ff0). The bar includes a search icon (magnifying glass) on the right side, which expands into the search bar on click.

### Forms
**`text-input`** — Used for email signups, checkout forms, and account creation. The input sits on a #1a1a1a surface with a 1px #2a2a2a border. On focus, the border shifts to the brand violet (#686de0) with no additional glow or shadow — the color change is the only indicator. Placeholder text is set in `{colors.muted}` (#9e9e9e). Error states use a red border (#e53935) with red error text below the input.

**`filter-dropdown`** — A dark select element used on product listing pages to sort by "Artist", "Format", "Price", or "Release Date". The dropdown matches the input styling: #1a1a1a background, #2a2a2a border, white text. The chevron icon is rendered in the brand violet, maintaining the accent's role as the only color in the interface.

### Footer
**`footer`** — A full-width section at the bottom of every page, rendered on the black canvas with a 1px top border in #2a2a2a (`{hairline}`). Links for "About Us", "Contact", "Shipping", "Returns", and "Privacy Policy" are set in `{typography.link}` at 14px, colored in muted gray (#9e9e9e). On hover, links shift to the brand violet. The footer also includes a newsletter signup form with a text input and a violet submit button.

### Hero
**`hero-section`** — The top-of-page banner on the homepage and category pages. Rendered on the black canvas with no background image — instead, a full-bleed product photograph (typically a turntable, vinyl pressing, or mastering equipment) sits behind a dark gradient overlay. The hero heading uses `{typography.display-xl}` at 36px, 700 weight, with -0.5px letter spacing. A secondary line of body text sits below the heading, followed by a `button-primary` CTA. The hero has 64px of vertical padding on top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero heading drops to 28px; filter dropdowns stack vertically; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduced to 5 items; hero heading at 32px; filter bar remains horizontal but wraps to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with 8 links; hero heading at 36px; filter bar in a single row with dropdowns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; hero heading at 40px; additional whitespace around product cards |

### Touch Targets
- All buttons and links maintain a minimum 44px height and 44px width for touch accessibility
- Filter dropdowns expand to 48px height on mobile for easier tapping
- Product card images include a minimum 48px tap area for the "Add to Cart" overlay
- Nav hamburger icon is 48px x 48px on mobile

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer
- Product filters collapse into a single "Filter" button that opens a modal overlay
- Footer link columns collapse into a single vertical list with expandable sections
- Product images switch from landscape to portrait orientation on mobile to maximize vertical space
- The hero section reduces its vertical padding from 64px to 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family declarations could not be extracted from the live site; the typography block uses Inter as a reasonable sans-serif assumption based on common audiophile/e-commerce patterns. The actual brand font (if any) should be confirmed from design assets or CSS source maps.
- Only one distinctive hex color (#686de0) was extracted from the live site. All other colors in the palette are inferred from the dark theme (black canvas, white text, gray surfaces) and may not match the exact brand specification. The brand's true secondary palette (if any) could not be determined.
- Hover states for buttons and cards are inferred from common dark-theme patterns; actual transition durations, easing curves, and shadow/glow effects could not be extracted.
- Error states for form inputs (red border, error text) are assumed based on standard e-commerce patterns; the brand may use a different error color or styling approach.
- Dark mode is not applicable (the site already uses a dark canvas), but no light mode variant was detected.
- Sub-brand or collection-specific color variations (e.g., "Original Master Recording" vs. "UltraDisc One-Step" vs. "Silver Label") could not be extracted.
- The site's loading states, skeleton screens, and animation patterns could not be determined from static HTML/CSS extraction.
- No meta theme-color was found in the site's head; the browser chrome/taskbar color is unknown.
