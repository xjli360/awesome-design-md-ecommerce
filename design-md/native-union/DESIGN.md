---
version: alpha
name: "Native Union"
source_url: "https://www.native-union.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A charcoal-and-sulfur brand identity built on the tension between #6f6f6f — a warm, mid-tone gray that reads as stone, concrete, or raw aluminum — and #ffff00, a pure signal-yellow that arrives like a safety vest on a minimalist electronics accessory. The brand sells phone cables, wireless chargers, and carrying cases, but the design language borrows from industrial hardware and heritage luggage: woven nylon braids, leather wraps, and anodized-metal finishes. Typography splits between Playfair Display for editorial headings (a serif that suggests a luxury-goods catalog) and Montserrat for interface labels (a geometric sans-serif that keeps the UI from feeling precious). Buttons are pill-shaped (`{rounded.full}`) but rendered in the charcoal gray rather than the yellow, making the yellow a rare accent — used only for select highlights, badges, and the occasional CTA. The product grid favors generous whitespace and single-column hero shots, letting the texture of the materials (braided cable, matte silicone, woven fabric) carry the visual weight. There is no gradient, no drop shadow, no decorative illustration — the brand trusts material photography and a strict two-color palette to signal quality. The result is a digital storefront that feels more like a precision-tool catalog than a phone-accessory shop: restrained, tactile without being "tactile" in the marketing sense, and utterly dependent on the contrast between warm gray and cold yellow.

colors:
  primary: "#ffff00"
  primary-active: "#e6e600"
  primary-disabled: "#ffff99"
  ink: "#1a1a1a"
  body: "#2b2b2b"
  muted: "#6f6f6f"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#1a1a1a"
  accent-yellow: "#ffff00"
  accent-charcoal: "#6f6f6f"
  badge-new: "#ffff00"
  badge-sale: "#6f6f6f"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Source Sans Pro', arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
  section: 80px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.accent-charcoal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary-active:
    backgroundColor: "#5a5a5a"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-charcoal}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-logo:
    height: 28px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  social-icon:
    height: 24px
    color: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in signal yellow (#ffff00) with uppercase Montserrat 14px/600 and full-pill rounding. On hover, the yellow deepens to #e6e600; the disabled state fades to #ffff99 with muted text. The button carries 14px vertical padding and 32px horizontal padding, giving it a substantial, weighty feel that contrasts with the otherwise restrained palette.

**`button-secondary`** — A charcoal-gray (#6f6f6f) pill with white text, used for secondary actions like "Learn More" or "Add to Cart" when the primary yellow would overwhelm. Active state darkens to #5a5a5a. Same dimensions as primary to maintain rhythm.

**`button-outline`** — A transparent button with a 2px solid black border and black text, used for tertiary actions or when the background is already yellow or gray. The outline variant preserves the full-pill shape and uppercase typography, ensuring all buttons read as a coherent family.

### Navigation
**`nav-bar`** — A white, 72px-tall fixed header with a thin bottom border (#e6e6e6). Navigation links are set in Montserrat 13px/600 with 0.8px letter spacing and uppercase — a deliberate choice that reads more like a fashion label's menu than a tech accessory store. The logo sits left-aligned at 28px height. On scroll, the nav gains a subtle box-shadow (not specified in tokens but observed in production).

**`nav-logo`** — The Native Union wordmark or monogram, rendered at 28px height. The logo itself is typically black or dark gray, maintaining the brand's low-contrast, industrial aesthetic.

### Product Cards
**`product-card`** — A minimal, borderless card with no rounding, relying entirely on the product photography and whitespace for structure. The image area sits on a soft gray (#f5f5f5) background to handle transparent PNGs or product shots with white backgrounds. Below the image, the product title appears in Montserrat 18px/600, followed by the price in 16px/400 in muted gray (#6f6f6f). No rating stars, no reviews count, no "add to cart" button on the card — the brand trusts the product detail page for conversion.

**`badge-new`** — A yellow (#ffff00) pill badge with uppercase 10px/700 Montserrat, used sparingly to denote new arrivals. The badge sits at the top-left corner of the product image, overlapping the photo area.

**`badge-sale`** — A charcoal-gray (#6f6f6f) badge with white text, used for sale or clearance items. Same dimensions and typography as the new badge, but the color swap signals a different category of attention.

### Forms
**`text-input`** — A white input field with a 1px light-gray border (#d4d4d4) and 8px rounding. On focus, the border thickens to 2px and shifts to charcoal (#6f6f6f), creating a subtle but clear active state. The input height is 48px, matching the button height for aligned form layouts.

**`search-bar`** — A full-pill search input with a soft-gray background (#f5f5f5) and a 1px hairline border. The pill shape mirrors the button family, making the search bar feel like an action rather than a passive field. Placeholder text is set in Montserrat 16px/400.

### Footer
**`footer`** — A black (#1a1a1a) footer with white body text and muted-gray (#9e9e9e) links. The footer uses the section spacing token (80px) for vertical padding, creating a generous breathing room that matches the brand's overall whitespace philosophy. Social icons are rendered in the muted-gray tone, not white, to avoid visual competition with the text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero heading drops to 28px; buttons go full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero heading at 36px; buttons remain inline but may stack in forms |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; hero at 42px; standard button sizing |
| Wide | > 1440px | Max-width container at 1440px, centered; product grid may expand to four columns; hero remains centered with generous margins |

### Touch Targets
- All buttons and interactive elements maintain a minimum 48px height for touch accessibility.
- Nav links have 44px minimum tap targets (padding + link height).
- Search bar is 56px tall on mobile, 48px on desktop.
- Product card images are tappable with no minimum size requirement (the entire card is a link).

### Collapsing Strategy
- Primary nav collapses to a hamburger menu at < 744px.
- Product grid collapses from 3 columns → 2 columns → 1 column as viewport shrinks.
- Footer link columns collapse to a single stacked column on mobile.
- Hero section reduces vertical padding from 80px to 48px on mobile.
- Search bar remains visible at all breakpoints (does not collapse into an icon).

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two extracted hex colors (#6f6f6f and #ffff00) were available from the live site scan. The brand likely uses additional shades (e.g., a lighter gray for hover states, a darker gray for footer backgrounds, a specific white for cards) — these have been inferred from common patterns and the brand's industrial aesthetic but should be verified against the actual design system.
- Hover, focus, and active states for most components are inferred from standard accessibility patterns rather than extracted from the site.
- Error states (form validation, 404 pages, empty states) are not documented.
- The brand may use a secondary accent color (e.g., a muted blue or green) that was not captured in the extraction.
- Font weights and exact sizes for Playfair Display and Montserrat are estimated based on common web usage; the actual type scale may differ.
- The brand's dark mode (if any) is not documented.
- Spacing tokens are based on standard design-system patterns and may not match the exact grid used in production.
- The `textTransform: uppercase` on button and nav-link typography is inferred from the brand's aesthetic; the actual site may use mixed case.
