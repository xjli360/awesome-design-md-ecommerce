---
version: alpha
name: "Beacon Hill Books"
source_url: "https://www.beaconhillbooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single hex — #313131 — anchors the entire Beacon Hill Books experience, a deep charcoal that reads as ink on paper rather than digital UI, giving the storefront the gravity of a well-stocked library shelf. The brand resists the common bookstore palette of warm cream and forest green, instead building its identity around this near-black primary, using it for navigation bars, footer blocks, and primary buttons with white text that feels like a book's title stamped on a cloth cover. The system font stack — -apple-system, BlinkMacSystemFont, Helvetica Neue, system-ui — runs unadorned, letting the typography disappear into readability; there is no custom typeface, no display font, no decorative lettering competing with the books themselves. The site reads as a single column of content on a white canvas ({colors.canvas}), with generous vertical spacing ({spacing.section}) between sections — featured titles, staff picks, events — each separated by a thin {colors.hairline} rule. Buttons use a modest {rounded.sm} radius, avoiding the pill shapes of e-commerce giants, and product cards carry a soft {rounded.md} that suggests paper edges rather than digital corners. The overall mood is one of editorial restraint: the books are the color, the books are the texture, and the interface steps back to let them speak.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-bookmark: "#c0392b"
  accent-event: "#2980b9"
  badge-new: "#27ae60"
  badge-sale: "#c0392b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', system-ui, sans-serif"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.accent-bookmark}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
  nav-link-active:
    textDecoration: underline
    textUnderlineOffset: 4px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 2px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    shadow: 0 1px 3px rgba(0,0,0,0.08)
  product-card-hover:
    shadow: 0 4px 12px rgba(0,0,0,0.12)
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: 1/1.5
  product-card-title:
    typography: "{typography.title-md}"
    padding: 12px 16px 4px
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: 0 16px 8px
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: 0 16px 12px
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-link-hover:
    textDecoration: underline
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: 0 0 24px
    borderBottom: 1px solid "{colors.hairline}"
  event-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 20px
    borderLeft: 4px solid "{colors.accent-event}"
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 32px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
    minHeight: 400px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep charcoal {colors.primary} with white text. Used for "Add to Cart", "Checkout", and "Subscribe" actions. On hover, darkens to {colors.primary-active} for a subtle press effect. The disabled state uses {colors.primary-disabled} to signal inactivity without visual noise. Vertical padding of 12px and horizontal of 24px give the button a balanced, bookish proportion.

**`button-secondary`** — An outlined variant with a white fill and a 1px {colors.primary} border. Used for "Learn More" and "View Details" actions that sit alongside primary buttons. On hover, the background shifts to {colors.surface-soft} for a gentle lift. The 11px/23px padding accounts for the border width to match the primary button's 44px height.

**`button-tertiary`** — A text-only button with no background or border, used for "Cancel" and "Back" navigation. On hover, a {colors.surface-soft} background appears to indicate interactability. The 12px/16px padding keeps the touch target generous while maintaining a minimal visual footprint.

### Cards
**`product-card`** — A clean white card with a soft {rounded.md} radius and a subtle drop shadow (0 1px 3px rgba(0,0,0,0.08)). The image occupies the top half with a 1:1.5 aspect ratio, cropped to the book cover. Title, author, and price stack below with 12px/16px/4px padding. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.12), creating a gentle lift that suggests picking the book off the shelf.

**`event-card`** — A left-accented card with a 4px {colors.accent-event} blue border on the left edge. Used for author readings, book signings, and store events. The 20px padding and white background keep the content readable, while the colored border provides visual categorization without competing with the book covers.

### Navigation
**`nav-bar`** — A full-width {colors.primary} bar at 64px height, containing the store name (left) and navigation links (right). Links use {typography.nav-link} in uppercase with 0.3px letter spacing, a typographic choice that evokes library catalog cards. The active link is underlined with a 4px offset, a subtle nod to hand-annotated shelf markers.

**`search-bar`** — A pill-shaped ({rounded.full}) input field with a 1px {colors.hairline} border and 10px/20px padding. On focus, the border thickens to 2px {colors.primary}, providing clear focus indication without relying on colored shadows or outlines. The 44px height matches the button height for visual consistency in search-and-filter toolbars.

### Forms
**`text-input`** — Standard form input with a 1px {colors.hairline} border and 12px/16px padding. On focus, the border becomes 2px {colors.primary}. Error states use a 1px {colors.accent-bookmark} red border, reserved for critical validation (credit card, email format). The 48px height provides a comfortable touch target for mobile users.

**`newsletter-signup`** — A contained form block on a {colors.surface-soft} background with 32px padding and {rounded.sm}. The email input sits inside with a white background and 1px {colors.hairline} border, paired with a {button-primary} for submission. The soft gray background distinguishes this module from the white product grid without introducing a new color.

### Footer
**`footer`** — A full-width {colors.primary} block with 48px/24px padding. Links are white with underline on hover, maintaining readability against the dark background. The footer typically contains store hours, address, social links, and a small "© Beacon Hill Books" line in {typography.body-sm}. No decorative elements — the dark block serves as a visual bookend to the white page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; hero padding reduces to 48px 16px; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible (5 max); hero at 64px padding; search bar collapses to icon |
| Desktop | 1128–1440px | Three-column product grid; full nav with 7-8 links; hero at 80px padding; search bar expanded with placeholder text |
| Wide | > 1440px | Max-width container at 1280px; three-column grid centered; hero max-width 1120px; extra whitespace on sides |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Product card tap targets (title, author, price) are individually tappable with 44px minimum hit area
- Nav hamburger icon is 48x48px on mobile
- Search icon button is 44x44px on tablet
- Newsletter submit button matches input height at 48px

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; menu overlay slides from left with {colors.primary} background
- Product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Hero section reduces vertical padding from 80px to 48px on mobile; background image (if present) crops to center
- Footer link columns stack vertically below 744px; social icons remain in a single row
- Search bar collapses to icon-only below 744px; expands to full-width input on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site; the full palette above (accents, badges, surface tones) is inferred from common bookstore design patterns and may not match the actual site. The site may use additional colors not captured in the extraction.
- No font-family declarations beyond the system stack were found; the site may use a custom typeface (e.g., a serif for headings) that wasn't loaded during extraction.
- Hover and focus states for all components (especially product cards, event cards, and footer links) are inferred from common patterns; actual site behavior may differ.
- Error styling for forms (text-input-error) is speculative; the site may use inline validation with different colors or patterns.
- Dark mode support is unknown; the site may or may not have a dark theme.
- The site's actual spacing scale, border radii, and component heights are inferred from the single extracted color and common bookstore e-commerce patterns; a full visual audit would be needed for accuracy.
- The "Just a moment..." page title suggests the site may use a Cloudflare challenge or similar protection, which may have prevented full CSS extraction.
