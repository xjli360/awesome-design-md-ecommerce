---
version: alpha
name: "Qanba"
source_url: "https://www.qanba.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A fighting-game hardware brand that announces itself in high-contrast red and black — #dd1111 as the primary voltage, a saturated, almost aggressive crimson that appears on every product badge, add-to-cart button, and sale flag, set against a deep #222222 ink background that gives the storefront the weight of a tournament-grade arcade stick. The palette is deliberately limited: #dd1111 for action, #222222 for structure, #f5f5f5 and #f7f7f7 for the canvas, and a single accent of #ff6600 that surfaces on limited-edition or high-margin items. Typography runs GothamBook-Regular at display sizes and OpenSans-Regular for body copy, both sans-serif faces that read clean and utilitarian — no serif flourishes, no decorative weight, just the functional legibility of a control panel label. Product cards use a soft {rounded.sm} corner on thumbnails and a {rounded.md} on the card container itself, while the primary CTA button takes a {rounded.sm} that feels purposeful without being soft. The nav bar is a solid band of #222222 with white text, and the footer repeats the same dark mass with muted #888888 links. There is no hero imagery, no lifestyle photography — the site leads with product grids, spec tables, and compatibility badges, treating the hardware as its own best visual. The overall mood is that of a pro-gear catalog: direct, high-contrast, and built for people who already know what they want.

colors:
  primary: "#dd1111"
  primary-active: "#cc0000"
  primary-disabled: "#e4e4e4"
  ink: "#222222"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#ff6600"
  badge-red: "#bd362f"
  badge-blue: "#005ab0"
  badge-blue-active: "#0066ff"
  error: "#e52f16"
  error-soft: "#ee5f5b"
  dark-surface: "#363636"
  dark-muted: "#6c6c6c"
  dark-hairline: "#454545"

typography:
  display-xl:
    fontFamily: "'GothamBook-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'GothamBook-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0
  display-md:
    fontFamily: "'GothamBook-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'OpenSans-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'OpenSans-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'OpenSans-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
  badge:
    fontFamily: "'OpenSans-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
  price:
    fontFamily: "'OpenSans-Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-compatibility:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    padding: 64px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and primary checkout flows. Rendered in #dd1111 with white text, 4px corner radius, and 44px height. On hover, shifts to #cc0000. Disabled state uses #e4e4e4 background with #aaaaaa text, signaling the button is non-interactive.
**`button-secondary`** — An outlined or ghost alternative for secondary actions like "View Details" or "Learn More". Uses white background with #222222 text, same 44px height and 4px corner radius as primary. Hover adds a thin #222222 border.
**`button-accent-sale`** — Reserved for limited-time offers and clearance items. Uses #ff6600 background to visually distinguish from the standard red primary. Same dimensions and corner radius as `button-primary`.
**`button-pill`** — A compact, fully rounded variant used for filter tags, category pills, and small inline actions. Uses `{typography.button-sm}` at 12px bold, 8px vertical padding, and 20px horizontal padding.

### Navigation
**`top-nav`** — A full-width 60px bar in #222222 containing the brand logo on the left and navigation links on the right. Links use `{typography.nav-link}` at 14px semibold with 0.5px letter spacing. The active link state shifts text color to #dd1111.
**`nav-link`** — Individual navigation items with 8px 16px padding. Default color is white, active state is #dd1111. No background on hover — the brand relies on color change alone for feedback.

### Cards
**`product-card`** — The primary product display unit, a white card with 8px corner radius and 16px padding. Contains a product image with 4px corner radius, a title in `{typography.title-sm}`, and a price in `{typography.price}` at 18px bold. Badges overlay the top-left of the image area.
**`product-card-image`** — The image container within a product card, using #f5f5f5 as a placeholder background and 4px corner radius. Images are typically square or 4:3 ratio.

### Badges
**`badge-sale`** — An orange (#ff6600) badge with white text, 2px 8px padding, and 2px corner radius. Used to flag discounted items. Text is 11px bold.
**`badge-new`** — A blue (#005ab0) badge with white text, same dimensions as `badge-sale`. Used for newly released products.
**`badge-compatibility`** — A neutral badge in #f7f7f7 with #555555 text, 4px 12px padding, and 4px corner radius. Used to display platform compatibility (e.g., "PS5", "PC", "Xbox") on product cards.

### Forms
**`text-input`** — Standard text input field for search, newsletter signup, and form fields. White background, 44px height, 4px corner radius, 10px 16px padding. Focus state adds a 2px #dd1111 border.
**`search-bar`** — A compact 40px search input used in the top nav or mobile menu. Same styling as `text-input` but reduced height.

### Footer
**`footer-section`** — A full-width dark band in #222222 with 48px vertical padding. Contains columns of links and brand information. Text defaults to #aaaaaa, with headings in white.
**`footer-link`** — Footer navigation links in #aaaaaa at 14px regular weight. Hover shifts to white.
**`footer-heading`** — Column headings in the footer, rendered in white at 16px semibold.

### Hero
**`hero-banner`** — A full-width promotional banner in #222222 with white text. Uses `{typography.display-lg}` at 28px. Typically contains a headline, optional subtitle, and a `hero-cta` button. Padding is 64px vertical, 24px horizontal.
**`hero-cta`** — The primary call-to-action within a hero banner. Same styling as `button-primary` but with 14px 32px padding for a more prominent appearance.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero padding reduced to 32px vertical; product cards stack full-width; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero maintains 48px vertical padding; search bar moves to nav overlay |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; standard hero padding; search bar visible in nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are each at least 48px tall
- Nav links have 44px minimum tap area despite 14px text
- Badge tap targets are wrapped in larger parent containers for accessibility

### Collapsing Strategy
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Top nav collapses to hamburger menu at < 744px; the menu overlay contains all nav links plus search
- Footer columns collapse from 4 columns (desktop) to 2 (tablet) to 1 (mobile)
- Hero banner reduces vertical padding by 50% on mobile; CTA button remains full-width below headline

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site; the values above (e.g., `button-primary-active`) are inferred from the extracted palette and common patterns
- Error state styling (form validation, out-of-stock messaging) was not observed; `error` and `error-soft` colors are extracted but their usage is speculative
- Dark mode is not supported; the site uses a light canvas (#f5f5f5) with dark nav/footer sections
- Sub-brand or limited-edition color palettes (e.g., special edition arcade sticks) were not captured
- The extracted font list includes multiple variants of OpenSans and GothamBook, but exact usage per component (e.g., which weight for which heading level) is inferred from common patterns
- Animation and transition timing values were not extracted
- The extracted hex list is heavily weighted toward grays and reds; the brand's true primary (#dd1111) is the most distinctive color in the set, but the palette may include additional accent colors not present in the extraction
- Shopify Pay, Klarna, and other checkout-widget colors may be present in the extracted list but were not isolated
