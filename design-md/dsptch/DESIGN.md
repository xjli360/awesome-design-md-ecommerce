---
version: alpha
name: "DSPTCH"
source_url: "https://www.dsptch.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the tension between raw utility and a single, unignorable red — #d20000, the color of a warning light on industrial machinery, of a tactical flashlight's low-battery indicator, of the exact moment a system demands attention. This red is the brand's only color voltage; it appears on the primary CTA, on sale badges, on the "Add to Cart" button, and nowhere else in the UI. The rest of the palette is a study in grayscale: #222222 for ink, #404040 for body text, #4f4f4f for muted states, #f4f4f2 and #f2f2f2 for surfaces, and #e6e6e6 for hairlines. The canvas is pure white (#ffffff). The typography system is equally restrained — Trade Gothic Next and IBM Plex Mono dominate, the latter a nod to code, to specs, to the kind of technical documentation that accompanies a precision tool. Headlines are set in Trade Gothic Next at 700 weight, tight tracking, no serifs, no sentiment. Body copy runs IBM Plex Mono at 400 weight, 14px, 1.5 line height — it reads like a product spec sheet, not a lifestyle blog. Corners are sharp: {rounded.none} on cards, {rounded.xs} on buttons, {rounded.sm} on inputs. There is no pill shape, no softness, no warmth. The nav bar is a thin strip of {colors.canvas} with {colors.ink} text, 60px tall, no background color, no shadow — just a floating utility belt. Product cards are flat white rectangles with a single hairline border (#e6e6e6), no elevation, no hover lift. The brand trusts the product photography — bags, cases, straps shot against white or concrete — to do all the emotional work. The design system is a toolbelt, not a living room.

colors:
  primary: "#d20000"
  primary-active: "#a00000"
  primary-disabled: "#f2b2b2"
  ink: "#222222"
  body: "#404040"
  muted: "#4f4f4f"
  muted-soft: "#6a6a6a"
  hairline: "#e6e6e6"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f4f4f2"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  badge-sale: "#d20000"
  badge-new: "#1f873d"
  error: "#ea0606"
  success: "#00730b"

typography:
  display-xl:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'IBM Plex Mono', Consolas, monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'IBM Plex Mono', Consolas, monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'IBM Plex Mono', Consolas, monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  link:
    fontFamily: "'IBM Plex Mono', Consolas, monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Trade Gothic Next', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The single call-to-action in the system. Solid #d20000 fill, white uppercase Trade Gothic Next at 14px with 1px letter-spacing. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to #a00000 (darkened red). Disabled state fades to a pale pink #f2b2b2. No icon, no shadow, no animation — just the color of urgency.

**`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Continue Shopping". Transparent background with a 1px #e6e6e6 border. On hover, the border becomes #222222 and the background shifts to #f4f4f2. Same typography as primary — uppercase, 14px, 1px tracking.

**`button-tertiary-text`** — Text-only link styled as a button. No background, no border, no padding beyond 12px vertical. Used for "Cancel" or "Clear" actions within forms. Same uppercase Trade Gothic Next typography. Hover state adds no underline — the brand avoids decorative text treatments.

### Navigation
**`nav-bar`** — A 60px-tall white strip with no background color, no shadow, no border-bottom. Logo sits left-aligned, navigation links right-aligned. Links are uppercase Trade Gothic Next at 13px, 1px letter-spacing. Active link uses #d20000. The bar is fixed at the top on desktop, collapses to a hamburger on mobile. No search bar in the nav — search is a separate element below the hero.

**`nav-link-active`** — The only color shift in the nav. Red text on white, no underline, no background pill. The active state is declared by color alone — a subtle but unmistakable signal.

### Product Cards
**`product-card`** — A flat white rectangle with a 1px #e6e6e6 border and zero border-radius. No shadow, no hover lift, no overlay. The product image fills the top half at a 1:1 aspect ratio with `object-fit: cover`. Below the image, the title in Trade Gothic Next 16px/600, then the price in IBM Plex Mono 14px/400 in #404040. The card is a container for the product, not a decorative object.

**`product-card-image`** — The only visual element that carries emotional weight. Shot against white or concrete, the product is the subject. No models, no lifestyle scenes — just the bag, the case, the strap, centered and cropped square.

### Badges
**`badge-sale`** — A small, sharp red rectangle applied to the top-left corner of product images. #d20000 fill, white uppercase text at 10px. No rounded corners. The red badge is the only sale indicator — no strikethrough pricing, no percentage-off callouts.

**`badge-new`** — Same shape and typography as the sale badge, but filled with #1f873d (green). Used for new arrivals or restocked items. The green is the only non-red accent in the system.

### Forms
**`text-input`** — A 44px-tall input with a 1px #e6e6e6 border, 4px border-radius, and IBM Plex Mono 14px placeholder text. On focus, the border becomes #222222. Error state uses #ea0606. No floating labels — placeholder text is the label. Used for email, search, and address fields.

**`quantity-selector`** — A compact input for cart quantity adjustments. 44px tall, 1px #e6e6e6 border, 4px radius. Contains a minus button, the current quantity (IBM Plex Mono 14px), and a plus button. No color changes — just the structural grid of the form.

### Footer
**`footer`** — A full-width section with #f4f4f2 background. Links are IBM Plex Mono 14px in #4f4f4f. Columns for "Shop", "Support", "About", and "Legal". No social icons in the extracted palette — the brand may link to social but does not display icon buttons. A thin #e6e6e6 divider separates the footer from the main content.

### Accordion
**`accordion-header`** — Used on product detail pages for "Details", "Shipping", "Returns" sections. A white background row with the section title in Trade Gothic Next 16px/600 and a chevron icon. A 1px #e6e6e6 border-bottom separates each row. No background change on hover — the chevron rotates on expand.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero image full-width; footer links stack vertically; search bar moves below hero |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; footer in 2-column layout; search bar remains in nav area |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; footer in 4-column layout; search bar in dedicated header row |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; whitespace increases on sides; nav remains 60px |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px.
- Nav hamburger icon is 44x44px tap area.
- Quantity selector buttons are 44x44px tap area.
- Accordion headers are 44px tall for tap.
- Badges are small (10px text) but positioned on product images — not standalone tap targets.

### Collapsing Strategy
- On mobile, the nav bar collapses to a hamburger menu with a slide-in drawer.
- Product filters (if present) collapse into a "Filter" button that opens a modal or drawer.
- Footer links collapse from 4 columns to 2 columns to a single vertical stack.
- Accordion sections are collapsed by default on mobile, expanded on desktop.
- Search bar moves from a dedicated header row on desktop to a hidden toggle on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards could not be reliably extracted — the live site may use a subtle border color change or image zoom, but no CSS was found.
- Error and success form states are inferred from extracted hex values (#ea0606, #00730b) but their exact application (border color, background tint, icon placement) is unknown.
- The brand may use a secondary accent color for "pre-order" or "limited edition" badges — not found in extraction.
- Dark mode is not supported — no dark-theme CSS or meta tags were detected.
- The extracted font list includes `tgn-soft-round`, `tgn-soft-round-comp`, and `tgn-soft-round-con` — these may be used for specific marketing pages or sub-brands, but the primary system appears to use Trade Gothic Next and IBM Plex Mono.
- Social media icon colors (#3b5998 Facebook, #00aced Twitter, #cb2027 Pinterest) were extracted but may be from embedded widgets, not the brand's design system.
- The `#651818` hex appears in extraction — likely a secondary red or hover state for the primary red, but its exact usage is unconfirmed.
- Checkout-specific colors (Shopify Pay buttons, Klarna badges) were filtered but may still appear in the extracted list — the brand's true checkout palette is unknown.
- Animation and transition durations (e.g., hover fade, drawer slide speed) were not extracted.
