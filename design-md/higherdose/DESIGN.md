---
version: alpha
name: "HigherDOSE"
source_url: "https://higherdose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A black canvas (#141414) and a single neon-green voltage (#4efac0) define HigherDOSE — a wellness-tech brand that sells infrared saunas, red-light panels, and PEMF mats as if they were luxury electronics. The site reads like a hardware launch: hero sections stack full-bleed product photography against white body text (#f5f5f5), with the brand's signature green used only for the primary CTA button, a few accent underlines, and the occasional progress bar. The effect is deliberate restraint — the green is never decorative, always functional. Secondary surfaces shift between true black (#121212) and near-black (#1a1a1a), while card backgrounds and form fields sit at #fafafa, creating a three-tier depth system without shadows. Typography runs Brown and Suisse Int'l at moderate weights (400–600), with display sizes around 28–32px and body copy at 14–16px — no heavy 700+ weights, no uppercase shouting. Buttons are softly rounded (`{rounded.sm}` ~8px), product cards use `{rounded.md}` ~12px, and the search bar adopts `{rounded.full}` for a pill-like feel. The checkout flow introduces a secondary accent — a bright blue (#0018ff) — that appears in the cart drawer and payment buttons, suggesting a sub-brand or partnership integration. The overall mood is dark, clinical, and aspirational: a spa that sells hardware, not a supplement company that sells hope.

colors:
  primary: "#4efac0"
  primary-active: "#3cfecf"
  primary-disabled: "#9da1a0"
  ink: "#141414"
  body: "#f5f5f5"
  muted: "#9da1a0"
  muted-soft: "#868a89"
  hairline: "#545454"
  hairline-soft: "#7e7e7e"
  canvas: "#141414"
  surface-soft: "#1a1a1a"
  surface-card: "#fafafa"
  on-primary: "#141414"
  on-dark: "#f5f5f5"
  accent-blue: "#0018ff"
  accent-green: "#00b84a"
  error: "#e61b1b"
  error-soft: "#ff5742"
  star-rating: "#f5f5f5"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: 1px solid "{colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: 80px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  cart-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  cart-checkout-button:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 16px 0px
    borderBottom: 1px solid "{colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: 12px 0px
  accordion-content:
    typography: "{typography.body-sm}"
    padding: 8px 0px 16px 0px

## Components

### Buttons
**`button-primary`** — The brand's single voltage point. Filled with `{colors.primary}` (#4efac0) against `{colors.on-primary}` (#141414) text, this button carries every primary CTA across the site — "Add to Cart", "Shop Now", "Get Your Dose". On hover, it shifts to `{colors.primary-active}` (#3cfecf), a slightly brighter green that reads as energized. The disabled state drops to `{colors.primary-disabled}` (#9da1a0), a muted gray-green that signals inactivity without ambiguity. Padding is generous at 14px 28px, and the 8px corner (`{rounded.sm}`) keeps the button feeling modern but not playful.

**`button-secondary`** — Used for "Learn More" and secondary actions on dark canvases. Background is `{colors.surface-soft}` (#1a1a1a) with white text (#f5f5f5), creating a subtle depth layer above the canvas. On hover, the background deepens to true black (`{colors.canvas}`). Same 8px radius and 48px height as the primary, maintaining visual rhythm.

**`button-tertiary-text`** — A text-only link styled as a button, used for "View Details" and "Read Reviews". The text color is `{colors.primary}` (#4efac0) with no background or border. On hover, an underline appears. This is the brand's lightest touch — a whisper of green that still reads as actionable.

**`button-pill-primary`** — A fully rounded variant (`{rounded.full}`) used for newsletter signups and filter tags. Smaller padding (10px 24px) and smaller type (`{typography.button-sm}`) make it feel accessory rather than primary. The green fill is the same `{colors.primary}`, but the pill shape softens the call to action.

**`button-pill-outline`** — The inverse of the pill primary: transparent background with a 1px `{colors.hairline}` (#545454) border and white text. Used for "Clear Filters" and secondary tag actions. On hover, the border brightens to `{colors.muted}` (#9da1a0).

### Cards
**`product-card`** — The primary product display unit. A white (`{colors.surface-card}` #fafafa) card with 12px rounded corners (`{rounded.md}`) and 16px padding. The product image sits at the top with `{rounded.sm}` (8px) corners, creating a subtle nested-radius effect. Below the image: title in `{typography.title-sm}`, price in `{typography.body-md}`, and a rating row with `{colors.star-rating}` stars. The card has no shadow — the brand relies on the contrast between the white card and the dark canvas (#141414) for separation.

**`product-card-badge`** — A small green badge (`{colors.primary}` fill, `{colors.on-primary}` text) pinned to the top-left of product images. Uses `{typography.badge}` (11px, uppercase, 0.5px letter-spacing) and `{rounded.xs}` (4px) for a tight, precise label. Common text: "NEW", "BEST SELLER", "LIMITED".

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on a `{colors.canvas}` (#141414) background. Logo sits left-aligned, navigation links center-aligned, and utility icons (search, cart, account) right-aligned. Links use `{typography.nav-link}` (14px, uppercase, 0.5px letter-spacing) in `{colors.muted}` (#9da1a0) for inactive states, shifting to `{colors.primary}` (#4efac0) on hover and active. The bar has a 1px bottom border in `{colors.hairline}` (#545454) for subtle separation from the hero.

**`nav-link-active`** — The active or hovered state of a navigation link. Text color shifts to `{colors.primary}` (#4efac0), creating a green underline effect (the brand uses a 2px bottom border in green, not a traditional underline). No background change — the brand keeps the nav bar clean.

### Forms
**`text-input`** — Standard input field on a white background (`{colors.surface-card}` #fafafa) with 8px rounded corners (`{rounded.sm}`) and a 1px `{colors.hairline}` (#545454) border. On focus, the border switches to `{colors.primary}` (#4efac0) — the green voltage appears only when the user engages. Error state uses `{colors.error}` (#e61b1b) for the border and `{colors.error-soft}` (#ff5742) for the error message text. Height is 48px, matching the button height for alignment.

**`quantity-selector`** — A compact 40px-tall control used on product pages and in the cart. Background is `{colors.surface-soft}` (#1a1a1a) with white text. The minus and plus buttons sit at either end, with the quantity number centered. Uses `{rounded.sm}` (8px) and `{typography.body-md}`.

### Footer
**`footer`** — A full-width section at `{colors.surface-soft}` (#1a1a1a) with 48px padding top and bottom. Links are `{colors.muted}` (#9da1a0) in `{typography.link}` (14px, regular weight), with hover states shifting to `{colors.body}` (#f5f5f5). The footer is organized into columns: Shop, Learn, Support, and Social. A horizontal rule in `{colors.hairline}` (#545454) separates the link columns from the copyright and payment icons row.

### Cart
**`cart-drawer`** — A slide-in drawer from the right side of the screen. Background is `{colors.surface-card}` (#fafafa) with `{colors.ink}` (#141414) text. The drawer has 12px rounded corners (`{rounded.md}`) on the top-left and bottom-left only (the right edge is flush with the viewport). Inside: a list of cart items with thumbnails, titles, quantities, and prices. The checkout button uses `{colors.accent-blue}` (#0018ff) — a notable departure from the green primary, suggesting this is a Shopify Payments integration or a partnership checkout flow.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically at full width; hero text reduces to 24px; buttons become full-width; cart drawer becomes full-screen overlay |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains 28px display; cart drawer slides in at 400px width |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at 32px display; cart drawer at 480px width |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero text scales to 36px; cart drawer at 520px width |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height for touch accessibility
- Nav bar links have 44px minimum tap targets
- Quantity selector buttons are 40px × 40px (meets WCAG 2.1 touch target recommendations)
- Product card CTAs are 48px tall with 16px internal padding
- Search bar is 48px tall with 20px horizontal padding
- Cart drawer close button is 44px × 44px

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu with a slide-in drawer for navigation links
- The product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- The footer collapses from 4 columns (desktop) → 2 columns (tablet) → stacked single column (mobile)
- Hero sections collapse from side-by-side (image + text) to stacked (image above text) on mobile
- Cart drawer collapses from a slide-in panel (desktop/tablet) to a full-screen overlay (mobile)
- The category filter strip collapses from horizontal scroll (desktop) to a dropdown select (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns; the live site may use different transitions or animations
- Error styling for forms (error messages, validation icons) is assumed based on standard patterns; exact error colors and messaging were not extracted
- Dark mode is not explicitly supported — the site is already dark-themed, but no alternate theme was detected
- Sub-brand or collection-specific palettes (e.g., "Red Light Therapy" vs "Infrared Sauna" product lines) may exist but were not extracted
- The accent-blue (#0018ff) used in the checkout button may be a Shopify Payments default color rather than a brand choice; verify against the live checkout flow
- Font weights for Brown and Suisse Int'l are inferred from common usage; the exact weight values (400, 500, 600) may vary by platform
- Letter-spacing values for display typography are estimated; the live site may use tighter or looser tracking
- Animation durations and easing curves were not extracted; the site likely uses 200–300ms ease-in-out for hover/focus transitions
- The star-rating component color (#f5f5f5) is assumed to match body text; the live site may use a different shade for ratings
- Scrim overlay opacity for modals and drawers was not extracted; a common value of 0.6–0.8 is assumed
- The `!important` flag on Inter suggests a third-party integration (e.g., a widget or app) overriding the brand's font stack; the intended primary font is likely Brown or Suisse Int'l
