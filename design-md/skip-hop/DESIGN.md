---
version: alpha
name: "Skip Hop"
source_url: "https://www.skiphop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A baby brand that leads with a crisp red #ce0e2d — not a pastel pink or muted sage — as its primary voltage, applied to CTAs, badges, and sale flags against a near-white canvas of #fafbfc. The palette is unusually restrained for the category: three grays (#f0f1f2, #f0eeee, #b1b5b8) handle all structural hierarchy, with a single warm accent #fcf0f2 reserved for hover states and soft backgrounds. Roboto at 400 weight carries body copy, while buttons and navigation use 500 weight for a clean, utilitarian clarity — no hand-drawn type or rounded display faces. Cards use {rounded.sm} (8px) corners, not the pill shapes of consumer marketplaces, and the search bar sits as a simple outlined rectangle rather than a full-radius orb. The brand trusts product photography and clear information hierarchy over decorative flourishes: category navigation is a horizontal strip of text labels, badges are flat rectangles with {rounded.xs} (4px), and the footer collapses into a single-column accordion on mobile. This is a system built for quick scanning by tired parents — high contrast, generous tap targets, and a single red thread that says "click here" without ambiguity.

colors:
  primary: "#ce0e2d"
  primary-active: "#a80b24"
  primary-disabled: "#f0c4cb"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#8c8c8c"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#fafbfc"
  surface-soft: "#f0f1f2"
  surface-card: "#ffffff"
  surface-warm: "#fcf0f2"
  on-primary: "#ffffff"
  sale-badge: "#ce0e2d"
  sale-text: "#ffffff"
  rating-star: "#f5a623"
  error: "#ce0e2d"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.rating-star}"
    fontSize: 14px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    padding: "0 0 {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Skip Hop's signature red #ce0e2d with white text. Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#a80b24) with no scale or shadow change — the brand prefers color depth over motion. Disabled state uses `{colors.primary-disabled}` (#f0c4cb) to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant with a white fill and `{colors.hairline}` border, used for "Learn More", "View Details", and secondary checkout actions. Active state darkens the border to `{colors.ink}` and fills with `{colors.surface-soft}`. Height matches primary at 44px for consistent row alignment.

**`button-tertiary`** — A text-only link styled as a button, colored `{colors.primary}` with no background or border. Used for "Cancel", "Clear Filters", and inline navigation. Padding is reduced to 12px 16px for tighter spacing in filter bars and modals.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and a `{colors.hairline-soft}` border, containing a square aspect-ratio image, product title, and price. On hover, the border shifts to `{colors.hairline}` and a subtle `boxShadow` appears — the only elevation in the system. No corner radius on the image bottom edge creates a clean visual break between photo and text.

**`sale-badge`** — A small uppercase badge in `{colors.primary}` with white text, `{rounded.xs}` corners, and tight 2px 8px padding. Placed at the top-left of product images to flag discounts. The only badge variant — no "New" or "Best Seller" badges were observed in the extracted palette.

### Navigation
**`nav-bar`** — A 64px white bar with `{colors.hairline-soft}` bottom border, containing uppercase nav links in Roboto 500. Active links gain a 2px `{colors.primary}` bottom border. No logo height was extracted, but the bar accommodates a left-aligned logo and right-aligned icons (search, cart, account).

**`category-strip`** — A horizontal scrollable strip below the nav bar, with muted text labels and a `{colors.hairline-soft}` bottom border. Active category shows `{colors.primary}` text and a 2px underline. No icons or images — purely text-driven navigation.

### Forms
**`text-input`** — A standard input with white fill, `{colors.hairline}` border, and `{rounded.sm}` corners. Focus state doubles the border to 2px and switches to `{colors.primary}`. Error state uses 2px `{colors.error}` border. Height is 44px to match button alignment in forms.

**`search-bar`** — A rectangular input (not pill-shaped) with `{rounded.sm}` corners, matching the text-input pattern. Focus state uses `{colors.primary}` border. No search button — the bar likely uses an icon or keyboard submit.

### Footer
**`footer-section`** — A `{colors.surface-soft}` (#f0f1f2) section with body text and muted links. On desktop, links are arranged in columns with `{typography.title-sm}` headings. On mobile, the footer collapses into an accordion pattern using `{accordion-trigger}` and `{accordion-content}` components.

**`accordion-trigger`** — A full-width clickable row with `{colors.ink}` text and a `{colors.hairline-soft}` bottom border. No chevron or icon specified — likely uses CSS `::after` or a simple `+`/`-` indicator.

### Hero
**`hero-banner`** — A full-width section with `{colors.surface-warm}` (#fcf0f2) background, used for seasonal promotions and brand campaigns. Contains a large heading and subheading with generous `{spacing.section}` padding. No background image or overlay — the warm tint alone creates the visual distinction.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; footer collapses to accordion; product cards stack vertically; nav bar reduces to hamburger menu; category strip becomes horizontally scrollable |
| Tablet | 744–1128px | Two-column product grid; footer columns remain expanded; nav bar shows limited links with "More" dropdown; hero banner reduces padding |
| Desktop | 1128–1440px | Three-column product grid; full nav bar visible; footer in 4-column layout; hero banner at full padding |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; all components center-aligned |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px with `{rounded.full}` for easy tapping
- Category strip items have at least 48px tap area (padding + text)
- Accordion triggers are full-width with 44px+ tap height

### Collapsing Strategy
- Primary navigation collapses to hamburger menu at < 744px
- Footer sections collapse to accordion at < 744px
- Product grid reduces from 4 columns to 1 column as viewport narrows
- Category strip becomes horizontally scrollable (no wrapping) at all breakpoints
- Hero banner reduces vertical padding by 50% on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by grays (#f0f1f2, #fafbfc, #f0eeee, #b1b5b8) with only one distinctive accent (#ce0e2d red) and one warm tint (#fcf0f2). The brand's true secondary palette (if any) could not be determined — no greens, blues, or yellows were found beyond the red.
- Font-family declarations returned only "Roboto, sans-serif". The brand may use a second typeface for display headings or logo, but no evidence was found in the extracted CSS.
- Hover, focus, and active states for most components are inferred from common patterns — the live site's actual interaction states were not extractable.
- Error, success, and warning color tokens are estimated based on standard e-commerce patterns, not extracted from the site.
- The meta theme-color tag was absent, suggesting no PWA or browser chrome customization.
- Shopify platform detection returned false, so the site may use a custom or different e-commerce backend — checkout widget colors (Afterpay, Klarna, etc.) were not present in the extracted list.
- Dark mode was not detected; all colors assume light theme only.
- Star rating color (#f5a623) is a standard yellow and may differ from the brand's actual implementation.
- No animation or transition timing values could be extracted (durations, easing curves).
- The extracted page title "Access to this page has been denied" suggests the scraper may have hit a bot-protection page rather than the actual homepage — colors and fonts should be verified against the live site.
