---
version: alpha
name: "NCLA Beauty"
source_url: "https://nclabeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A candy-toned bath-and-body brand that runs on a blush-pink current of #f2aead — not a shy whisper of pink but a saturated, almost coral rose that appears on product labels, site badges, and the primary CTA button, giving the entire storefront a warm, Valentine-adjacent glow. The palette is surprisingly restrained for a beauty brand: a cool slate #676986 anchors body text, while #272d45 (a deep navy-charcoal) handles headings and strong ink, creating a crisp, editorial contrast against the soft pink. The canvas is #f4f4f6, a barely-there lavender-gray that reads as cleaner than pure white and avoids the sterile clinic feel of many beauty sites. Accent colors arrive sparingly: a marigold #fce7a8 for sale badges, a true red #c8232c for error states or limited-edition drops, and a muted coral #d59998 that echoes the primary at half saturation. Typography leans on a serif/didone pair — Big Caslon and Bodoni MT for display headings, lending a vintage-apothecary dignity to product names, while Jost (a geometric sans) handles body copy and buttons with a clean, modern counterpoint. Product cards use generous {rounded.md} corners and a soft shadow, making each item feel like a wrapped gift. The nav bar is compact at 60px, with a sticky header that collapses on scroll, and the search icon sits in a pill-shaped field with {rounded.full} ends. The overall impression is a beauty brand that trusts its product photography to do the heavy lifting — the design stays out of the way, offering just enough pink warmth and serif elegance to signal "indie, vegan, cruelty-free" without shouting.

colors:
  primary: "#f2aead"
  primary-active: "#d59998"
  primary-disabled: "#fadfde"
  ink: "#272d45"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#b9b9b9"
  hairline: "#e5e5eb"
  hairline-soft: "#f4f4f6"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#fce7a8"
  accent-error: "#c8232c"
  accent-coral: "#d59998"
  accent-blue: "#4469af"
  accent-social-twitter: "#00aced"
  accent-social-facebook: "#047bd5"
  star-rating: "#fce7a8"
  scrim: "#191919"

typography:
  display-xl:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', Oswald, 'Myriad', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.accent-error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.on-primary}"
    textTransform: uppercase
    letterSpacing: "0.5px"
  hero-banner:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's signature pink #f2aead and white text. Used for "Add to Cart," "Shop Now," and primary checkout actions. On hover, shifts to the deeper coral `{colors.primary-active}` (#d59998). Disabled state uses a washed-out pink `{colors.primary-disabled}` (#fadfde). All primary buttons use `{rounded.sm}` (8px) corners and `{typography.button-md}` (15px, weight 600, 0.5px letter-spacing).

**`button-secondary`** — An outlined variant on a transparent or canvas background with a 1px hairline border. Text is `{colors.ink}` (#272d45). Used for "Learn More," "View Details," and secondary actions. Active state darkens the border to `{colors.muted}` and adds a soft surface tint.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` for the text color. Used for inline links like "Cancel" or "Skip" in forms and modals.

**`button-pill-primary`** — A fully rounded pill button (`{rounded.full}`) using the primary pink fill. Used for promotional banners, email signup CTAs, and sticky mobile cart buttons. Uses `{typography.button-sm}` (13px) for a compact fit.

**`button-pill-outline`** — A pill-shaped outline button with a transparent fill and 1px hairline border. Used for filter tags, "Clear All" actions, and secondary promotional links.

### Navigation
**`nav-bar`** — A compact 60px sticky header with a canvas background and a subtle bottom border. The brand logo sits left-aligned, with navigation links in uppercase `{typography.nav-link}` (14px, weight 500, 0.3px letter-spacing). Active links use `{colors.primary}`; inactive links use `{colors.muted}`. The nav collapses on mobile into a hamburger menu.

**`search-bar-pill`** — A pill-shaped search field with a soft surface background and `{rounded.full}` corners. On focus, the background switches to white and gains a 1px primary-pink border. Used in the header and on the search results page.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.06)). Contains a product image (full-width, no internal padding), a title using `{typography.title-sm}`, and a price in `{typography.body-sm}` with `{colors.muted}`. On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.1). Badges overlay the top-left corner of the image.

**`product-badge-sale`** — A small uppercase badge with a marigold background (#fce7a8) and dark ink text. Used to indicate discounted items. `{rounded.xs}` (4px) corners keep it sharp and legible.

**`product-badge-new`** — A pink-filled badge (#f2aead) with white text for "NEW" arrivals. Same size and shape as the sale badge.

### Forms
**`text-input`** — Standard text input with a canvas background, 1px hairline border, and `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}`. Error state uses a red border (#c8232c). Height is 44px for comfortable touch targeting.

**`select-dropdown`** — Matches the text-input styling but includes a dropdown arrow. Used for variant selection (size, scent, quantity) on product pages.

**`quantity-selector`** — A compact 40px input with +/- buttons flanking a numeric field. Uses `{rounded.sm}` corners and a hairline border. The buttons use `{colors.muted}` text on hover.

### Footer
**`footer-section`** — A dark navy (#272d45) footer with light gray text (#b9b9b9). Links use `{typography.link}` and turn pink on hover. Section headings are uppercase captions with 0.5px letter-spacing. The footer includes newsletter signup, social icons, and legal links.

### Hero
**`hero-banner`** — A full-width banner with a washed-pink background (#fadfde) and dark ink text. Uses `{typography.display-lg}` for the headline and a `{colors.primary}` CTA button. Padding is generous at `{spacing.section}` (64px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in 2-column grid; hero padding reduces to 32px; search bar moves to full-width below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav links remain visible but compact; product cards in 3-column grid; hero retains full padding; search bar remains in header |
| Desktop | 1128–1440px | Full nav with all links; product cards in 4-column grid; hero at full width with centered content; search bar in header with dropdown |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid with increased whitespace; hero content centered within max-width |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (buttons, inputs, selectors)
- Icon buttons are 36px × 36px with 44px touch area via padding
- Nav links have 44px tap targets on mobile
- Product card tap targets include the entire card surface
- Quantity selector +/- buttons are 40px tall

### Collapsing Strategy
- Mobile nav collapses to a hamburger menu with a slide-out drawer
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer columns stack vertically on mobile (single column)
- Hero banner reduces padding on mobile (from 64px to 32px)
- Search bar moves from inline header to full-width below the nav on mobile
- Product image galleries collapse from thumbnail strip to swipeable carousel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges and footer links are inferred from common patterns, not extracted from live CSS
- Error state styling for forms (red border) is assumed based on the presence of #c8232c in the palette, but exact error message typography and iconography are unknown
- Dark mode is not supported and no dark-mode tokens were extracted
- The extracted font list includes multiple serif and sans-serif options; the exact pairing (Big Caslon for display, Jost for body) is inferred from typical usage patterns in beauty e-commerce and may differ from the live site's actual CSS cascade
- Checkout widget colors (Shopify Pay, Afterpay, Klarna) were filtered from the extracted palette but may appear in the live checkout flow
- Social icon colors (#00aced for Twitter, #047bd5 for Facebook) are standard brand colors, not NCLA-specific
- The star-rating color (#fce7a8) is inferred from the extracted marigold accent; actual star colors may vary by review widget
- No animation or transition durations were extracted; all motion defaults are assumed at 200-300ms ease
- The exact border radius for product cards (12px) is estimated from the extracted palette and common e-commerce patterns; the live site may use a different value
- No data on focus-visible styles for keyboard navigation
- Sub-brand or collection-specific color variations (e.g., holiday collections) are not captured
