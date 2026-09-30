---
version: alpha
name: "Nemo Equipment"
source_url: "https://www.nemoequipment.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  An olive-drab #424336 anchors Nemo Equipment’s digital storefront — the same hue as a rainfly at dusk — and it appears as the browser chrome’s theme-color, the primary button fill, and the footer’s full-bleed band, creating a continuous outdoor-light boundary around the shopping experience. Against that military-olive ground, a sharp marigold #c4c117 acts as the brand’s voltage: it powers sale badges, star-ratings on product tiles, and the “Add to Cart” CTA’s hover state, a color borrowed from the high-visibility zipper pulls and stuff-sack drawcords on actual Nemo tents. The palette is deliberately earthen — #907458 (saddle leather), #94745c (bark), #d6a73e (dried grass), #68695d (lichen) — and the canvas is a warm off-white #f2f1ee rather than pure #ffffff, as if the whole interface were printed on recycled paper. Typography runs a mix of Oakes (a clean, modern sans with moderate contrast) for display headlines and Sofia Pro for body copy, both at modest weights (400–600) — the brand trusts its product photography (tents pitched against granite, sleeping bags in alpine meadows) over typographic drama. Buttons are softly rectangular at {rounded.sm} (8px), while product cards use {rounded.md} (12px) and the search bar takes a pill shape at {rounded.full}. The top nav is compact at 64px, with a sticky header that collapses on scroll, and the footer is a dense information hub in #424336 with white text. Every component feels built for the trailhead: durable, legible, and unpretentious.

colors:
  primary: "#424336"
  primary-active: "#5f604f"
  primary-disabled: "#8c8d82"
  ink: "#191919"
  body: "#555555"
  muted: "#707070"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#dbd7cd"
  canvas: "#f2f1ee"
  surface-soft: "#dddad3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#c4c117"
  accent-marigold-hover: "#d6a73e"
  accent-saddle: "#907458"
  accent-bark: "#94745c"
  accent-lichen: "#68695d"
  star-rating: "#c4c117"
  sale-badge: "#c4c117"
  error: "#c13515"
  success: "#5f604f"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Oakes', 'Sofia Pro', 'Ash', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Oakes', 'Sofia Pro', 'Ash', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Oakes', 'Sofia Pro', 'Ash', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Oakes', 'Sofia Pro', 'Ash', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Sofia Pro', 'Oakes', 'Ash', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
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
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-accent-hover:
    backgroundColor: "{colors.accent-marigold-hover}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(66, 67, 54, 0.15)"
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(66, 67, 54, 0.15)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: "400px"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: "0.3"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: "0.8"
  footer-link-hover:
    opacity: "1"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "{spacing.sm} {spacing.lg} {spacing.lg} {spacing.lg}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 6px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with olive-drab #424336 and white text. Used for “Add to Cart,” “Checkout,” and “Submit.” On hover, it shifts to #5f604f, a slightly lighter olive. The disabled state uses #8c8d82, a muted gray-green. All primary buttons are 44px tall with 8px corner rounding and 15px semibold type.

**`button-secondary`** — An outlined variant on the warm off-white canvas, with a 1px hairline border. Used for “Learn More,” “View Details,” and secondary form actions. Hover adds a primary-colored border and a soft surface background. Height matches the primary at 44px for alignment in forms.

**`button-accent`** — The marigold #c4c117 variant, reserved for high-visibility actions like “Shop Sale” or “Limited Edition.” Uses dark ink text for contrast. Hover deepens to #d6a73e. Same dimensions as primary.

**`button-pill`** — A fully rounded, compact button (40px tall) used for filter tags, category pills, and “Quick Add” on product cards. Uses primary fill with white text, or can be used as an outline variant with the filter-chip component.

### Cards
**`product-card`** — A white card with 12px rounding and a subtle 1px/3px shadow. The image area occupies the top 4:3 ratio with matching top rounding. Below, the title (16px semibold), price (16px regular), and star rating (marigold #c4c117) stack with 8–16px padding. On hover, the shadow deepens to 4px/12px. Sale items receive a marigold badge in the top-left corner.

**`hero-banner`** — A full-width 400px-tall section with a primary olive background and white display text. Used for seasonal collections and new arrivals. An optional dark scrim overlay at 30% opacity sits over background imagery to ensure text readability.

### Navigation
**`nav-bar`** — A 64px sticky header on the warm off-white canvas, with uppercase 14px medium-weight nav links. The active page is underlined with a 2px primary olive bar. On scroll, the bar collapses to 56px with a subtle drop shadow. The mobile menu replaces links with a hamburger icon and a full-screen overlay drawer.

**`breadcrumb`** — A simple horizontal list of 13px muted links separated by a gray bullet or slash. The current page is plain muted text, while ancestor pages are primary olive links. Used on product detail and collection pages.

### Forms
**`text-input`** — A 48px-tall input with 8px rounding, off-white background, and a 1px hairline border. Focus state adds a primary olive border and a subtle 2px ring. Error state swaps the border to #c13515. Used for email, search, and address fields.

**`select-input`** — Matches the text-input dimensions and styling, with a custom dropdown arrow. Used for size, quantity, and sort-by selections.

**`quantity-selector`** — A compact 40px input with increment/decrement buttons, used on product detail pages and cart line items. Styled as a simple bordered rectangle with 8px rounding.

### Footer
**`footer`** — A full-width band in primary olive #424336 with white text at 80% opacity. Contains link columns, social icons, and legal text. Links brighten to full opacity on hover. Padding is 48px on top/bottom and 32px on sides. The footer is the brand’s second most prominent olive surface after the hero banner.

### Badges & Chips
**`sale-badge`** — A small marigold #c4c117 pill with uppercase 11px bold black text, 4px rounding, and 4px/8px padding. Positioned absolutely over product images.

**`filter-chip`** — A 40px-tall pill with a 1px hairline border, used in collection filters. Active state fills with primary olive and white text. Multiple chips can be selected simultaneously.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger + logo; product cards stack in 1 column; hero banner reduces to 280px; footer columns stack vertically; filter chips become a horizontal scrollable strip; search bar moves to a full-width drawer |
| Tablet | 744–1128px | Product cards display in 2 columns; nav links remain visible but reduce font size to 12px; hero banner at 340px; filter chips wrap to 2 rows; footer splits into 2 columns |
| Desktop | 1128–1440px | Product cards in 3 columns; full nav bar with all links; hero banner at 400px; filter chips in a single row; footer in 4 columns; sticky nav at 64px |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards can expand to 4 columns; hero banner may include parallax or full-bleed imagery; footer columns at fixed max-width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (Apple HIG guideline).
- Filter chips are 40px tall with 14px horizontal padding for easy tapping.
- Mobile nav hamburger icon is 48x48px.
- Quantity selector increment/decrement buttons are 40x40px.
- Search bar pill is 48px tall on all breakpoints.

### Collapsing Strategy
- Top nav collapses from 64px to 56px on scroll, with a shadow.
- On mobile, the full nav link set collapses into a hamburger menu; the drawer overlays the content with a primary olive background.
- Product card image aspect ratio remains 4:3 on all breakpoints; on mobile, the title and price stack more tightly (8px padding instead of 16px).
- Filter chips collapse from a full row to a horizontal scrollable strip on mobile.
- Footer columns collapse from 4 columns to 2 on tablet, to 1 on mobile.
- Hero banner text scales down proportionally: 28px on mobile, 32px on tablet, 36px on desktop.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and filter chips are inferred from common patterns; actual transitions (ease, duration) not extracted.
- Error styling for forms (red border, error message placement) is a best-guess based on the extracted error hex #c13515; actual validation patterns not observed.
- Dark mode is not present on the live site; no dark palette tokens exist.
- Sub-brand or collection-specific color variants (e.g., "Trail" vs "Summit" lines) not extracted.
- Font weights for Oakes and Sofia Pro are inferred from common usage; actual font files may include additional weights (300, 700, 800) not seen in the extracted CSS.
- The exact font stack order (Oakes vs Sofia Pro vs Ash) is a best-guess based on extracted declarations; the brand may use a different priority.
- Star rating icon style (filled, half, outline) not confirmed; assumed filled marigold based on accent color.
- Mobile nav drawer animation (slide vs fade) not extracted.
- Cart and checkout flow components (quantity stepper, coupon input, payment forms) are inferred from Shopify defaults; actual Nemo-specific styling may differ.
- The extracted color list includes #007aff (likely a Shopify Pay or iOS default blue) and several grays that may be stock-image tones; these are excluded from the palette. The true brand colors are the distinctive olive #424336, marigold #c4c117, saddle #907458, and the warm off-white #f2f1ee.
