---
version: alpha
name: "Solaris Japan"
source_url: "https://solarisjapan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A teal-and-gold import marketplace (#108474 primary, #f5af19 accent) that reads like a Tokyo electronics district translated into a clean Shopify grid — the brand's voltage comes from the contrast between a cool, trustworthy teal and a warm, urgent gold that powers every "Add to Cart" and sale badge. The canvas is a near-white #f9fafb, with product cards floating on #ffffff against hairline borders at #e9e9e9, creating a dense but legible catalog layout. Type runs Nunito Sans at modest weights — display headlines sit at 24px weight 600, body at 14px weight 400 — letting the product photography and price tags do the heavy selling. The search bar is a pill-shaped input (`{rounded.full}`) with a teal border on focus, and category navigation uses a horizontal scroll strip with active tabs underlined in the primary teal. Badges for "Pre-order", "Sale", and "Limited" use the gold accent (#f5af19) on white, while sold-out indicators shift to a muted #7b7b7b. The footer stacks social icons (Facebook #3b5998, Twitter #1da1f2, Instagram #e60023, Pinterest #e60023) in a tight row, and the checkout flow inherits Shopify's default widget colors (#c8102e for error states, #ffff00 for Klarna). The overall feel is utilitarian but warm — a marketplace that trusts its teal-gold signal over decorative flourishes.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d4c9"
  ink: "#555555"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#e9e9e9"
  hairline-soft: "#f2f2f2"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f5af19"
  accent-gold-active: "#d2920f"
  accent-gold-soft: "#fbcd0a"
  badge-sale: "#c8102e"
  badge-sold-out: "#7b7b7b"
  badge-preorder: "#108474"
  star-rating: "#f5af19"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-instagram: "#e60023"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"
  error: "#c8102e"
  success: "#108474"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.body-sm}"
    color: "{colors.badge-sale}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  social-icon:
    height: 32px
    width: 32px
    rounded: "{rounded.full}"
    backgroundColor: "{colors.muted-soft}"
  social-icon-facebook:
    backgroundColor: "{colors.social-facebook}"
  social-icon-twitter:
    backgroundColor: "{colors.social-twitter}"
  social-icon-instagram:
    backgroundColor: "{colors.social-instagram}"
  social-icon-pinterest:
    backgroundColor: "{colors.social-pinterest}"
  social-icon-linkedin:
    backgroundColor: "{colors.social-linkedin}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    color: "{colors.primary}"
    fontWeight: 600
  pagination-disabled:
    color: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand teal (#108474) and white text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to a darker teal (#0d6b5d). Disabled state uses a muted teal (#a3d4c9) with white text. Padding is 12px 24px with 8px rounded corners.

**`button-secondary`** — An outlined variant with a white background and teal border. Used for "View Details", "Continue Shopping", and secondary actions. On hover, fills with the primary teal and white text. Matches the primary button's height and padding for alignment in button groups.

**`button-gold`** — The accent call-to-action, filled with gold (#f5af19) and dark text (#555555). Used for "Sale", "Limited Offer", and promotional CTAs. On hover, darkens to #d2920f. This button carries the brand's urgency signal — it's the visual equivalent of a yellow price tag in a Tokyo electronics store.

### Cards
**`product-card`** — The core product display unit, a white card with 8px rounded corners and 16px padding. Contains a 1:1 aspect ratio image with matching rounded corners, a title in 14px weight 600, and a price in teal. On hover, gains a subtle box shadow (0 4px 12px rgba(0,0,0,0.1)). Sale prices render in red (#c8102e). Sold-out items show a gray badge and muted price.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background, with uppercase nav links in 14px weight 600. On scroll, gains a subtle bottom shadow. The nav contains the brand logo (left), category links (center), and search/cart icons (right). Active category links are underlined with a 2px teal border.

**`category-strip`** — A horizontal scrollable strip of category tabs below the nav bar. Tabs are uppercase 14px weight 600, with active tabs showing a teal underline and inactive tabs in muted gray (#7b7b7b). The strip scrolls horizontally on mobile with a fade-out gradient at the edges.

### Forms
**`text-input`** — Standard text input with white background, 8px rounded corners, 10px 16px padding, and a light gray border (#e9e9e9). On focus, the border thickens to 2px teal (#108474). Used for search, email signup, and checkout forms.

**`search-bar`** — A pill-shaped search input (9999px rounded) with 10px 20px padding and a light gray border. On focus, the border becomes 2px teal. Used in the nav bar and on the search results page. The pill shape is the brand's most distinctive UI element — it reads as friendly and approachable against the otherwise rectilinear product grid.

### Badges
**`badge`** — Small uppercase labels (11px weight 700, 0.5px letter spacing) with 4px rounded corners and 2px 8px padding. Gold background (#f5af19) with dark text for general badges. Red background (#c8102e) for sale badges. Gray background (#7b7b7b) for sold-out. Teal background (#108474) for pre-order. Badges overlay the top-left corner of product card images.

### Footer
**`footer`** — A dark footer (#555555) with white text, containing link columns, social icons, and legal text. Social icons are 32px circles with brand-specific colors (Facebook blue, Twitter blue, Instagram/pinterest red, LinkedIn blue). Links are 14px weight 400 with white color. Padding is 64px top/bottom and 24px sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), hamburger menu replaces nav links, search bar collapses to icon, category strip scrolls horizontally, footer stacks vertically, badges reduce to 10px font |
| Tablet | 744–1128px | Two-column product grid, nav links show as dropdown, search bar remains visible but shorter, category strip shows 4-5 visible tabs, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, full search bar, category strip shows 6+ tabs, footer uses 4-column layout, max-width container at 1200px |
| Wide | > 1440px | Four-column product grid, all elements at max-width, additional whitespace on sides, category strip can show all tabs |

### Touch Targets
- All buttons and interactive elements minimum 44px height (WCAG compliant)
- Search bar touch target minimum 44px height
- Category tabs minimum 44px height for tap targets
- Social icons 32px minimum with 44px tap area
- Product card tap target covers entire card

### Collapsing Strategy
- Nav links collapse to hamburger menu below 744px
- Search bar collapses to icon-only below 744px, expands on tap
- Category strip collapses to scrollable strip with fade gradient below 744px
- Footer columns stack vertically below 744px
- Product grid reduces columns from 4 to 1-2 below 744px
- Breadcrumbs truncate with ellipsis on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for badges and category tabs could not be reliably extracted — inferred from common patterns
- Error styling for form validation (red borders, error messages) not observed — used #c8102e as error color from extracted palette
- Dark mode not implemented on the live site — no dark palette available
- Sub-brand or seasonal color palettes not observed — only the teal-gold-primary system
- Font weights beyond 400 and 600 not confirmed — Nunito Sans may have additional weights used in specific contexts
- The extracted color list includes many social media brand colors (#3b5998, #1da1f2, etc.) and Shopify widget defaults (#c8102e, #ffff00) — these are not brand colors but are included for reference
- Animation and transition timings not extracted — standard 200-300ms ease-in-out assumed
- Focus ring styles (keyboard accessibility) not observed — standard 2px outline assumed
- The meta theme-color (#4C576A) is a muted gray-blue that doesn't match any extracted hex — may be a fallback or unused
- Checkout flow styling not observed — inherits Shopify defaults
