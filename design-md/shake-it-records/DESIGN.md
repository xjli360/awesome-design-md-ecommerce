---
version: alpha
name: "Shake It Records"
source_url: "https://www.shakeitrecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Cincinnati institution since 1999, Shake It Records lives in a world of burnt orange and deep charcoal — #f48120 is the brand's unmistakable voltage, appearing across sale badges, category markers, and footer accents against a #dedada canvas that reads like worn concrete. The palette is unapologetically heavy: #444444 body text on #dedede surfaces, with #231f20 ink for headlines and #847c7c muted tones for secondary information, creating a visual density that mirrors the weight of vinyl crates and the grit of a well-loved storefront. Navigation is utilitarian and direct — a single row of genre links (Rock, Punk, Hip Hop, Soul, Jazz) rendered in all-caps at modest weight, with the search bar tucked into a compact pill (`{rounded.full}`) that doesn't compete with the merchandise. Product cards use soft corners (`{rounded.sm}`) and generous padding (`{spacing.base}`) to let album art breathe, while the shopping cart badge pulses with that signature orange. The checkout flow introduces a secondary blue (#006fcf) for action buttons — a deliberate contrast that separates browsing from buying. There is no hero imagery, no lifestyle photography; the site trusts the album covers themselves to sell the inventory. The footer is dense with links and store hours, anchored by the orange logo mark and a newsletter signup that mirrors the search bar's pill shape. Every design decision reads as practical rather than precious — this is a store that has been selling records for twenty-five years and knows exactly what its customers need to see.

colors:
  primary: "#f48120"
  primary-active: "#e16f27"
  primary-disabled: "#f89f20"
  ink: "#231f20"
  body: "#444444"
  muted: "#847c7c"
  muted-soft: "#dedede"
  hairline: "#dedada"
  hairline-soft: "#dedede"
  canvas: "#dedada"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#006fcf"
  accent-blue-active: "#3086c8"
  accent-red: "#eb001b"
  accent-yellow: "#f79e1b"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px
  product-card-title:
    typography: "{typography.body-sm}"
    fontWeight: 600
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    borderColor: "{colors.hairline}"
  category-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.muted}"
    padding: 4px 8px
  category-link-active:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    borderColor: "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature burnt orange (#f48120) with white uppercase text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to a deeper orange (`{colors.primary-active}`). Disabled state uses a lighter orange (`{colors.primary-disabled}`) with reduced contrast. The sharp 4px corner (`{rounded.xs}`) keeps the button feeling utilitarian and direct, not playful.

**`button-secondary`** — A contrasting blue action button (`{colors.accent-blue}`) used primarily in the checkout flow to differentiate purchasing actions from browsing actions. Same typography and corner radius as primary, but the blue signals a different intent — payment, confirmation, or navigation to cart. Active state deepens to `{colors.accent-blue-active}`.

**`button-ghost`** — A text-only button with no background, used for secondary actions like "Clear Cart" or "Cancel". Matches the body text color and uses the same uppercase button typography. Hover state adds a subtle underline or opacity shift.

### Navigation
**`nav-bar`** — A compact 56px top bar on the `{colors.canvas}` background. Contains the store logo on the left, genre category links in the center, and utility icons (search, cart, account) on the right. No sticky positioning — the nav scrolls with the page, keeping the focus on content.

**`nav-link`** — Genre links rendered in all-caps 13px with 1px letter-spacing. Active state highlights in the brand orange. Links are tightly packed with 8px horizontal padding, maximizing the number of visible categories without wrapping.

**`category-link`** — Secondary navigation links used in sidebar or footer genre lists. More subdued than primary nav links, using `{colors.muted}` text color. Active state switches to orange.

### Product Cards
**`product-card`** — A white card (`{colors.surface-card}`) with soft 8px corners (`{rounded.sm}`) and 8px padding. Album art fills the top of the card at a 1:1 aspect ratio. Below the art, the artist and album title appear in 14px semibold, with the price in muted gray below. Cards are displayed in a responsive grid with 16px gaps.

**`product-badge-sale`** — A small orange pill badge overlaid on the top-left corner of product card images. Uses 11px uppercase bold text. Indicates items on sale or clearance.

**`product-badge-sold-out`** — A dark badge (`{colors.ink}`) for out-of-stock items. Same size and placement as the sale badge, but communicates unavailability rather than a deal.

### Forms & Inputs
**`text-input`** — Standard form input with white background, 8px corner radius, and a `{colors.hairline}` border. On focus, the border shifts to the brand orange. Used in checkout forms, account creation, and contact pages.

**`search-bar-pill`** — A compact, fully rounded search input (`{rounded.full}`) at 40px height. White background with a subtle hairline border. The pill shape is the only fully rounded element in the system, making it visually distinct from all other inputs.

**`newsletter-input`** — Matches the search bar's pill shape and dimensions, used in the footer for email signup. Accompanied by a `{button-primary}` submit button.

### Cart & Quantity
**`cart-badge`** — A small orange circle (`{rounded.full}`) displaying the item count. Positioned on the cart icon in the nav bar. Uses 11px bold white text. Minimum 20px width ensures single digits look centered.

**`quantity-selector`** — A compact input with increment/decrement buttons, used on product detail pages and cart. White background with hairline border and 4px corners. 36px height keeps it from dominating the product layout.

### Footer
**`footer-section`** — A full-width footer on the `{colors.canvas}` background with 64px vertical padding. Contains store information, hours, link columns, and the newsletter signup. Links use `{colors.muted}` to keep the footer visually subordinate to the main content.

**`footer-link`** — Standard 14px link in muted gray. No underline by default; hover adds underline for discoverability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product grid goes single-column; search bar moves below nav; footer links stack vertically; category sidebar becomes horizontal scroll strip |
| Tablet | 744–1128px | Nav shows abbreviated genre links; product grid shows 2-3 columns; search bar remains in nav but shrinks; footer shows 2-column link layout |
| Desktop | 1128–1440px | Full nav with all genre links; 4-column product grid; sidebar category navigation visible; full footer with 4-column links |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 5-6 columns; additional whitespace on sides; no functional changes |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Nav links have 8px padding on each side, ensuring adequate tap area
- Quantity selector buttons are 36px minimum with 44px tap area via padding
- Cart badge is 20px minimum but sits within a 44px icon container
- Mobile hamburger menu button is 44x44px

### Collapsing Strategy
- Genre navigation collapses into a hamburger menu below 744px
- Search bar moves from inline nav position to a dedicated row below the nav on mobile
- Product grid collapses from 4-6 columns to 1 column on mobile
- Footer link columns stack vertically on mobile, with accordion-style expand/collapse for each section
- Sidebar category navigation becomes a horizontal scrollable strip on tablet and mobile
- Newsletter signup moves from footer to below the nav on mobile for visibility

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; Helvetica Neue is assumed as a common system font for record store sites, but the actual brand typeface is unknown
- Hover and focus states for most components could not be reliably extracted; active states for buttons are inferred from the extracted color palette
- Error state styling for form inputs (validation errors, required field indicators) was not observed
- Dark mode or high-contrast mode variants are not present in the extracted data
- The checkout flow uses multiple third-party payment widgets (Shopify Pay, Klarna, Afterpay) whose colors appear in the extracted palette but are not part of the brand system — these have been excluded from the design tokens
- Product card hover states (scale, shadow, border change) were not observable from static extraction
- Mobile navigation drawer styling (background, animation, close button) could not be determined
- The exact spacing between grid items and section padding values are inferred from common e-commerce patterns rather than extracted measurements
- Sub-brand or seasonal color palettes (if any) are not represented in the extracted data
