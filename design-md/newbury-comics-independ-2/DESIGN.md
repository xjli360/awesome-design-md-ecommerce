---
version: alpha
name: "Newbury Comics"
source_url: "https://www.newburycomics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-white grid with a single electric jolt of red — #121212 ink on #eeeeee canvas, punctuated by the brand's signature crimson accent that appears in the logo, the "Add to Cart" button, and the sale badges that dot every product grid. The site reads like a punk zine translated into e-commerce: dense product tiles with sharp 1px hairlines (#dedede), all-caps category headers in a condensed sans, and a sticky top bar that never lets you forget you're in a record store that sells Funko Pops, band tees, and vinyl reissues alongside each other. The hero section on the homepage is a full-bleed black-and-white photo with the brand's "Wicked Good Time" tagline overlaid in white type — no gradient, no softness, just contrast. Product cards use a clean white surface (#ffffff) with the product image filling the full width, price in bold 16px body, and a quick-add button that appears on hover. The search bar is a simple white rectangle with a magnifying glass icon, no pill shapes, no rounded corners beyond {rounded.sm} — this is a brand that values directness over friendliness. Navigation is a two-tier system: a thin utility bar with "Sign In / Cart / Store Locator" in {colors.muted} 12px type, and below it the main nav with department links in all-caps 14px bold. The overall feel is Boston basement show meets mall chain — utilitarian, loud in its product density, but with a consistent black-red-white tricolor discipline that holds the chaos together.

colors:
  primary: "#cc0000"
  primary-active: "#990000"
  primary-disabled: "#ff9999"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#cc0000"
  sale-badge-text: "#ffffff"
  sold-out: "#999999"
  star-rating: "#121212"
  footer-bg: "#121212"
  footer-text: "#cccccc"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
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
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link-utility:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
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
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
  button-quick-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-nav-utility:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link-utility}"
    height: 32px
  top-nav-main:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
  product-card-image:
    aspectRatio: "1:1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.body-md}"
    fontWeight: 400
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 700
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    color: "{colors.primary}"
    typography: "{typography.body-md}"
    fontWeight: 700
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 400px
    minHeight: 300px
  hero-overlay:
    backgroundColor: "rgba(18, 18, 18, 0.4)"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    color: "{colors.ink}"
    fontWeight: 700
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, used for "Add to Cart", "Checkout", and "Sign Up" flows. Solid red (#cc0000) background with white uppercase bold text, 4px corner radius, and 44px height. On hover, darkens to #990000; disabled state fades to #ff9999 with white text. The uppercase letter-spacing (0.5px) gives it a confident, retail-floor presence — no pill shapes, no gradients.

**`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Apply Filter". White background with black text and a 1px #dedede border. Active state fills the background with #f5f5f5 and switches border to black. Same 44px height and uppercase treatment as primary, maintaining visual rhythm across the button set.

**`button-tertiary`** — Text-only link styled as a button, used for "Clear All" filters or "Cancel" in modals. No background, no border, 12px uppercase bold text. The only button without a height constraint — it sits inline with its surrounding content.

**`button-quick-add`** — Compact add-to-cart button that appears on product card hover. Smaller 36px height, 8px/16px padding, no rounded corners. Uses the same red/white scheme as primary but in a tighter package. Disappears on mobile where the full button is always visible.

### Cards
**`product-card`** — The core shopping unit: a white card with a 1:1 product image, title in 16px regular weight, and price in 16px bold. No rounded corners, no shadow — just a soft #eeeeee border that darkens to #dedede on hover. Sale prices render in red; sold-out items get a gray badge overlay. The quick-add button is hidden until hover on desktop, always visible on mobile. Cards stack in a 2-column grid on mobile, 3-4 columns on desktop.

**`product-card-badge`** — Red rectangle badge pinned to the top-left of product images. Used for "SALE", "NEW", or "EXCLUSIVE" labels in 11px uppercase bold white text. Sold-out items swap to a gray (#999999) badge. No corner rounding — the badge is a hard rectangle that matches the brand's no-nonsense attitude.

### Navigation
**`top-nav-utility`** — A thin 32px bar at the very top of the page, light gray background (#f5f5f5), containing "Sign In", "My Account", "Store Locator", and the cart icon. Text is 12px regular weight in #666666 — intentionally low-contrast to let the main navigation below take visual priority. On mobile, this collapses into a hamburger menu.

**`top-nav-main`** — The primary navigation bar at 56px tall, white background with a 1px bottom border. Department links (Vinyl, Music, Movies, Pop Culture, etc.) are 14px uppercase bold with 0.5px letter-spacing. The Newbury Comics logo sits on the left, cart icon on the right. On scroll, this bar becomes sticky with a subtle shadow. Mobile collapses all links into a full-screen overlay menu.

### Forms
**`text-input`** — Standard form input for search, email signup, and checkout fields. White background, 44px height, 4px corner radius, 1px #dedede border. Focus state switches border to black. Error state uses the brand red border. No floating labels — placeholder text is 16px regular weight. The simplicity matches the brand's direct, no-frills approach.

**`select-input`** — Dropdown selector for sorting (Price Low-High, Newest, etc.) and filtering. Same dimensions and border treatment as text-input. The dropdown arrow is a simple SVG chevron, not a custom icon.

### Search
**`search-bar`** — A straightforward white rectangle with a magnifying glass icon on the left. 44px height, 4px radius, 1px #dedede border. Focus state turns the border black. No pill shape, no rounded-full treatment — this is a record store search, not a travel app. On mobile, the search bar expands to full width below the nav.

### Footer
**`footer`** — Full-width black (#121212) footer with white text (#cccccc). Organized into columns: "Shop", "Help", "About", "Connect" — each with a 14px uppercase bold heading and 14px regular link stack. Links lighten to white on hover. Bottom bar contains copyright, privacy policy, and terms in 12px gray text. Social media icons (from Font Awesome) sit in the Connect column at 20px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; utility bar hidden; search bar moves below nav; hero section reduces to 250px height; filter/sort becomes a bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav links truncate with "More" dropdown; utility bar shows icons only; hero at 350px; filters sit in a left sidebar that can be toggled |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; utility bar shows text labels; hero at 400px; persistent left filter sidebar on category pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with auto margins; hero image scales but height stays 400px; additional whitespace on left/right of product rows |

### Touch Targets
- All buttons and interactive elements minimum 44px height (exceeds Apple's 44pt guideline)
- Product card tap targets: entire card is clickable, not just the title or image
- Filter chips: 32px minimum height with 12px horizontal padding
- Nav links: 56px tap area within the main nav bar
- Cart icon: 44x44px minimum tap area (icon is 24px centered within)
- Quantity selector +/- buttons: 44x44px tap targets

### Collapsing Strategy
- Utility nav (Sign In, Store Locator) collapses entirely on mobile — only cart icon remains in the main nav
- Main nav links collapse into a hamburger menu on mobile; the menu opens as a full-screen overlay with department links in 24px bold type
- Product grid goes from 4 columns on wide desktop to 1 column on mobile
- Filter sidebar collapses into a "Filter" button that opens a bottom sheet on mobile
- Search bar moves from the nav bar (desktop) to a full-width bar below the nav (mobile)
- Footer columns stack vertically on mobile, 2-column grid on tablet, 4-column on desktop
- Breadcrumbs truncate on mobile — only show current page and "Home" link

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font-family declarations only returned Font Awesome icon fonts — no body or heading font was detected. The system font stack used in this spec (`'Helvetica Neue', Helvetica, Arial, sans-serif`) is an educated guess based on common e-commerce patterns and the brand's utilitarian aesthetic. The actual brand font may differ.
- The extracted hex colors (#eeeeee, #dedede, #121212) are all grayscale — no brand accent color was detected in the extraction. The red (#cc0000) used as primary is inferred from the brand's known logo color and common e-commerce patterns; the live site may use a different accent or no accent at all.
- Hover states for buttons and cards are estimated based on common darkening patterns — actual hover colors were not extractable.
- Error states for form inputs (border color, error message styling) are not confirmed from the live site.
- Mobile navigation behavior (hamburger menu, full-screen overlay) is based on common Shopify patterns — the actual mobile nav implementation may differ.
- Hero section height and overlay treatment are estimated — the live site may use different dimensions or no overlay.
- Footer link hover colors are estimated — actual hover treatment may differ.
- Dark mode support is unknown — the site may or may not have a dark mode implementation.
- Checkout flow styling (Shopify checkout) is not captured — the extracted colors may include checkout widget colors that were not fully filtered.
- The brand may use custom icons or illustrations beyond Font Awesome — these were not extractable.
- Product card hover effects (shadow, scale, border change) are estimated — actual hover treatment may be different or nonexistent.
- The brand's "Wicked Good Time" tagline and its typographic treatment in the hero are based on the page title, not extracted from the live site's CSS.
