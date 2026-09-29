---
version: alpha
name: "Synapse Films"
source_url: "https://synapsefilms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A neon-laced horror and cult cinema label that runs on a black canvas (#121212) and a single electric-green primary (#a6ffa5) — the same voltage that powers the "Add to Cart" button, the "Pre-Order" badge, and the glowing accents across product grids. The brand's visual identity is built on high-contrast collisions: a blood-red secondary (#eb001b) for limited-edition steelbook markers and sale flags, against a near-black ink (#1f1f21) that absorbs all light. Typography uses Noto Sans Display at clean weights — display headlines sit at 28px weight 600, body copy at 16px weight 400 — letting the product photography (grainy 4K scans of Argento and Fulci frames) do the atmospheric heavy lifting. Every product card is a sharp rectangle with {rounded.sm} corners, the only softness in a system that otherwise favors straight edges and tight spacing. The shopping experience is utilitarian: a sticky top nav at 64px height, a search bar with {rounded.full} pill ends, and category filters that read as horizontal tabs. Badges are the brand's punctuation — "NEW RESTORATION" in {colors.primary} on {colors.ink}, "LIMITED EDITION" in {colors.canvas} on {colors.secondary}. The footer collapses into a single column of legal links and social icons, all in {colors.muted} (#dedede). This is a storefront built for collectors who know what they want: the green glow is the beacon, the black is the void, and the red is the warning.

colors:
  primary: "#a6ffa5"
  primary-active: "#7ee67d"
  primary-disabled: "#4a7a49"
  secondary: "#eb001b"
  secondary-active: "#c50016"
  ink: "#1f1f21"
  body: "#dedede"
  muted: "#dedede"
  muted-soft: "#9e9e9e"
  hairline: "#3a3a3c"
  hairline-soft: "#2a2a2c"
  canvas: "#121212"
  surface-soft: "#1c1c1e"
  surface-card: "#1f1f21"
  on-primary: "#121212"
  on-secondary: "#ffffff"
  on-dark: "#dedede"
  accent-green: "#2bb34b"
  accent-teal: "#00fced"
  accent-blue: "#218ac1"
  accent-amber: "#412d00"
  accent-cream: "#fff1e3"
  badge-new: "#a6ffa5"
  badge-limited: "#eb001b"
  badge-preorder: "#2bb34b"
  star-rating: "#a6ffa5"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Noto Sans Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase

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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.sm}"
  button-tertiary-outline:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    objectFit: contain
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  social-icon:
    textColor: "{colors.muted}"
    height: 24px
  social-icon-hover:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in electric green ({colors.primary}) on a dark background ({colors.on-primary}). Used for "Add to Cart", "Pre-Order Now", and "Checkout" actions. On hover, shifts to a slightly dimmer green ({colors.primary-active}). Disabled state uses a muted green ({colors.primary-disabled}) with reduced contrast. All buttons use uppercase lettering with 0.3px tracking for a sharp, collector-market feel.

**`button-secondary`** — The alert or urgency button, rendered in blood red ({colors.secondary}) with white text. Used for "Limited Edition", "Sold Out", and "Notify Me" actions. Active state darkens to {colors.secondary-active}. This button signals scarcity and should be used sparingly — one per page maximum.

**`button-tertiary-outline`** — A ghost button with a 1px hairline border ({colors.hairline}) and body-colored text. Used for secondary actions like "View Details" or "Wishlist". The transparent background lets it sit comfortably on product cards and in the footer without competing with primary CTAs.

**`button-pill-primary`** and **`button-pill-secondary`** — Compact pill-shaped buttons with fully rounded ends ({rounded.full}), used for filter tags, collection links, and quick-add actions. The pill shape is the only fully rounded element in the system, making it a deliberate accent shape.

### Cards
**`product-card`** — A sharp-cornered card ({rounded.sm}) on a slightly lighter dark surface ({colors.surface-card}). The card has no padding at the container level — the image fills the top with {objectFit: contain}, and title/price are padded internally. The card is the primary browsing unit, used in grid layouts of 3–4 columns on desktop.

**`product-card-title`** — The film title, set in {typography.title-sm} with body-colored text. Truncates to one line on mobile. The title is the only text element that links to the product detail page.

**`product-card-price`** — The price, rendered in {colors.primary} green to draw the eye. Uses {typography.body-md} for readability. Sale prices appear in {colors.secondary} red with the original price struck through in {colors.muted-soft}.

### Badges
**`badge-new`** — A small uppercase badge in electric green on dark background. Used for "NEW RESTORATION", "NEW RELEASE", and "JUST ADDED" labels. The badge is the system's primary attention-grabber, appearing at the top-left of product card images.

**`badge-limited`** — A small uppercase badge in blood red on white. Used for "LIMITED EDITION", "STEELBOOK", and "EXCLUSIVE" labels. This badge overrides the green badge when both conditions apply — limited editions always take precedence.

**`badge-preorder`** — A small uppercase badge in accent green ({colors.accent-green}) on dark background. Used for "PRE-ORDER" labels. This badge is visually distinct from the primary green to avoid confusion with in-stock items.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, rendered on the black canvas with a 1px hairline bottom border. Contains the brand logo (left), navigation links (center), and cart/search icons (right). Navigation links use {typography.nav-link} with 0.5px letter spacing and uppercase transformation.

**`nav-link-active`** — Active navigation link rendered in electric green. The active state is the only colored nav element, creating a clear wayfinding signal against the otherwise monochrome nav bar.

**`nav-link-inactive`** — Inactive navigation link rendered in muted gray. On hover, links transition to body-colored text with a subtle opacity shift.

### Forms
**`text-input`** — A dark input field on {colors.surface-soft} with a 1px hairline border. Used for email signups, search queries, and checkout forms. On focus, the border shifts to {colors.primary} green, creating a clear active state.

**`search-bar`** — A pill-shaped search input ({rounded.full}) with the same dark surface treatment. The pill shape is a deliberate departure from the system's otherwise sharp corners, making search feel like an action rather than a form field.

### Footer
**`footer`** — A full-width footer on the black canvas with a 1px hairline top border. Contains legal links, social media icons, and copyright text in {colors.muted}. Social icons shift to {colors.primary} on hover. The footer collapses to a single column on mobile with centered text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid collapses to 2 columns; nav bar reduces to hamburger menu; footer stacks to single column; search bar moves to full-width below nav; badges scale down to 9px font |
| Tablet | 744–1128px | Product grid shows 3 columns; nav links remain visible but compact; search bar sits in nav row; footer splits into 2 columns |
| Desktop | 1128–1440px | Product grid shows 4 columns; full nav link set visible; search bar at 400px max-width; footer splits into 3 columns |
| Wide | > 1440px | Product grid shows 4 columns with increased whitespace; nav bar max-width at 1440px centered; search bar at 480px max-width; footer max-width at 1440px centered |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav bar links have 48px minimum tap targets on mobile
- Product card images link to product pages with 48px minimum tap area
- Quantity selector buttons have 44px x 44px tap targets
- Social media icons in footer have 44px x 44px tap targets

### Collapsing Strategy
- Nav bar collapses to hamburger menu on mobile (< 744px), with slide-in drawer from left
- Product grid collapses from 4 columns to 2 columns on mobile
- Footer collapses from 3 columns to single column on mobile
- Search bar collapses from inline to full-width below nav on mobile
- Category tabs collapse to horizontal scroll on mobile with overflow hidden
- Product card metadata (format, year, runtime) collapses to single line on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (scale, shadow, or border effects) could not be reliably extracted from the live site
- Error states for form inputs (validation, error messages) were not observed in the extracted data
- Loading states (spinners, skeleton screens) were not present in the extracted color or font data
- Dark mode is not applicable — the site already uses a dark canvas as its default theme
- Sub-brand or collection-specific color variations (e.g., "Vinegar Syndrome" collab, "Terror Vision" crossovers) could not be confirmed
- The extracted hex list includes several colors (#0f6908, #1c5621, #218ac1, #00fced, #fff1e3, #412d00) that may be stock image dominant tones or Shopify widget colors rather than intentional brand palette — these have been included as accent tokens but should be verified against the brand's actual design assets
- Font weight variations beyond 400 and 600 could not be confirmed — the system uses Noto Sans Display but may support 300, 500, 700, 800, 900 weights
- Animation durations and easing curves were not extractable from static CSS analysis
- Focus ring styles (outline, offset, color) for keyboard navigation were not observed
- Print stylesheet behavior could not be determined
