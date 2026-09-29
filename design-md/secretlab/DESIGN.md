---
version: alpha
name: "Secretlab"
source_url: "https://secretlab.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, aggressive red — #a72a2f — is the brand's primary voltage, appearing on every primary CTA, the logo mark, and the stitching of the flagship Titan Evo chair; it reads as performance-oriented rather than playful, closer to a supercar's brake caliper than a gaming peripheral's LED strip. The palette is anchored by a near-black ink (#18181b) and a warm off-white canvas (#fafafa), with a secondary accent of muted gold (#e8d087) that appears on limited-edition stitching and badge details — a nod to the brand's "Stealth" and "SoftWeave Plus" fabric tiers. Typography runs din-2014 for display and Soleil for body, giving the interface a condensed, technical feel: headlines sit at 28–32px with tight letter-spacing, while body copy stays at 14–16px with generous line-height for readability. The brand's signature design move is the "pillar" layout — a full-width hero section with a single product image floating above a gradient backdrop, flanked by spec badges and a sticky "Configure" bar that follows the user as they scroll. Cards use sharp corners ({rounded.none}) for product imagery and soft 8px radii ({rounded.sm}) for feature callouts, creating a contrast between precision and approachability. The "NEO Hybrid" foam and "PRISM" fabric names are treated as badge-level typography, often set in uppercase with a hairline border (#d4d4d8) and a subtle drop shadow. The overall mood is industrial but refined — a showroom for high-end ergonomic gear rather than a typical gaming aisle.

colors:
  primary: "#a72a2f"
  primary-active: "#862226"
  primary-disabled: "#d39597"
  ink: "#18181b"
  body: "#27272a"
  muted: "#52525b"
  muted-soft: "#71717a"
  hairline: "#d4d4d8"
  hairline-soft: "#e4e4e7"
  canvas: "#fafafa"
  surface-soft: "#f4f4f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#e8d087"
  accent-green: "#117937"
  accent-cyan: "#22d3ee"
  accent-amber: "#f59e0b"
  accent-red: "#dc2626"
  badge-bg: "#f2f2f2"
  badge-text: "#3f3f46"
  star-rating: "#f59e0b"
  scrim: "#121417"

typography:
  display-xl:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Soleil, 'Noto Sans KR', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Soleil, 'Noto Sans KR', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Soleil, 'Noto Sans KR', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Soleil, 'Noto Sans KR', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.8px
    textTransform: uppercase
  price-md:
    fontFamily: "'din-2014', 'Noto Sans KR', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: 1/1
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 40px
    height: 52px
  hero-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  sticky-config-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 64px
  sticky-config-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    rounded: "{rounded.none}"
  text-input-error:
    borderColor: "{colors.accent-red}"
    rounded: "{rounded.none}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Secretlab red (#a72a2f) with white text and sharp corners ({rounded.none}). Uses uppercase din-2014 at 16px with 0.5px letter-spacing for a performance-oriented feel. On hover, the background deepens to #862226. The disabled state uses #d39597 with reduced opacity. Height is 48px with 32px horizontal padding.

**`button-secondary`** — A white button with dark text (#18181b) and a 1px hairline border (#d4d4d8). Hover fills the background with #f4f4f5. Used for "Learn More" and secondary configurator actions. Same dimensions and typography as primary.

**`button-outline`** — Transparent background with a 2px solid border in #a72a2f and red text. Hover fills the background with a 10% opacity red tint. Used for "Compare" and "Add to Wishlist" actions.

**`button-ghost`** — Text-only button with no background or border, using muted gray (#52525b) at 14px uppercase. Hover changes text to #18181b. Used for "Cancel" and "Clear Filters" in dropdowns and modals.

**`sticky-config-cta`** — A compact version of the primary button (40px height, 24px horizontal padding) used in the sticky configuration bar that follows the user during product customization. Uses 14px uppercase typography to fit the constrained space.

### Cards
**`product-card`** — A sharp-cornered card ({rounded.none}) with a white background and a 1:1 aspect ratio product image. The card contains a badge (gold for "Best Seller" or "New"), the product name in 16px din-2014, a star rating in amber (#f59e0b), and the price in 20px bold. Hover state shifts the background to #f4f4f5 and adds a subtle shadow.

**`product-card-badge`** — A small gold (#e8d087) label with dark text, set in 11px uppercase din-2014 with 0.8px letter-spacing. Used for "Best Seller," "New," "Limited Edition," and "Stealth" tier indicators. Padding is 4px top/bottom and 8px left/right.

### Navigation
**`top-nav`** — A 64px white bar with uppercase nav links in 14px din-2014. The active link is highlighted in red (#a72a2f), while inactive links are muted (#52525b). The logo sits on the left, and a search icon and cart icon sit on the right. On scroll, the nav gains a 1px bottom hairline (#d4d4d8).

**`nav-link-active`** — Red text (#a72a2f) with no background. Used for the current page or section in the top navigation.

**`nav-link-inactive`** — Muted gray text (#52525b) with no background. Hover changes text to #18181b.

### Hero
**`hero-section`** — A full-width section with a near-black background (#18181b) and white text. The hero contains a large product image (often floating), a headline in 32px din-2014, a gold badge for limited editions, and a primary CTA button. Padding is 80px top and bottom.

**`hero-cta`** — A larger version of the primary button (52px height, 40px horizontal padding) designed to stand out against the dark hero background. Same red fill and white text.

**`hero-badge`** — A gold (#e8d087) label with dark text, used to highlight "Limited Edition" or "New" status on hero products. Padding is 6px top/bottom and 12px left/right.

### Forms
**`text-input`** — A white input field with a 1px hairline border (#d4d4d8) and sharp corners. Focus state changes the border to red (#a72a2f). Error state uses red border (#dc2626). Height is 48px with 12px vertical and 16px horizontal padding.

**`select-input`** — A white dropdown with the same dimensions and border as the text input. Uses a custom chevron icon in muted gray.

**`quantity-selector`** — A compact 40px input with minus/plus buttons on either side, used in the cart and product configuration. Sharp corners and a 1px hairline border.

### Footer
**`footer-section`** — A dark footer (#18181b) with muted gray text (#71717a). Links are in 14px Soleil with hover state changing to white (#fafafa). Section headings are in 16px din-2014 white. Padding is 48px top and bottom.

**`footer-link`** — Muted gray text (#71717a) with no underline. Hover changes to white (#fafafa).

**`footer-heading`** — White text (#fafafa) in 16px din-2014, used for column titles in the footer.

### Other
**`search-bar`** — A white input field with a search icon on the left, used in the top nav and mobile search overlay. Same dimensions as text-input but with a 20px search icon in muted gray.

**`accordion-header`** — A clickable row with 16px din-2014 text and a chevron icon that rotates on expand. Used in product specifications and FAQ sections. Padding is 16px top and bottom.

**`accordion-content`** — The expandable panel below the header, containing body text in 16px Soleil. Padding is 0 on top and 16px on bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top nav collapses to hamburger menu; hero image reduces to 50% width; product cards stack vertically; sticky config bar becomes full-width with compact CTA; search bar moves to overlay |
| Tablet | 744–1128px | Two-column product grid; top nav shows limited links (logo, Products, Support, Cart); hero remains full-width but with smaller headline (28px); sticky config bar shows product name and CTA |
| Desktop | 1128–1440px | Full three-column product grid; complete top nav with all links; hero at max width with 32px headline; sticky config bar shows full product details and CTA |
| Wide | > 1440px | Max-width container at 1440px; hero centers content; product grid can show 4 columns for accessories; footer expands to 5-column layout |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile.
- Product card images are tappable and link to the product page.
- Accordion headers have a minimum height of 48px for easy tapping.
- The sticky config bar CTA is at least 40px tall.

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay with links, search, and account options.
- Product filters collapse into a slide-out drawer on mobile.
- The hero section reduces image size and stacks content vertically on mobile.
- The footer collapses from 5 columns to 2 columns on tablet, and to a single column on mobile.
- Product specifications (accordion) are collapsed by default on all screen sizes.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., text-input, select-input) are inferred from common patterns; exact values may differ.
- Error styling for forms (text-input-error, select-input-error) is not confirmed from the live site; colors are based on the extracted red (#dc2626) but may use a different shade.
- Dark mode is not present on the live site; all colors assume light mode.
- The exact font weights for Soleil are not confirmed; 400 and 500 are assumed based on common usage.
- The `sticky-config-bar` component's exact height and padding are estimated from screenshots; the live site may vary.
- The `product-card-badge` gold color (#e8d087) is extracted but may be used for other badge types (e.g., "Stealth," "SoftWeave Plus") with different text colors.
- The `hero-section` background may use a gradient or image overlay instead of a solid color; #18181b is the dominant extracted color.
- The `quantity-selector` component's exact border and hover states are not confirmed.
- The `accordion` component's animation timing and chevron icon are not specified.
- The `search-bar` overlay on mobile may have a different background or animation than assumed.
- The `footer-section` may include social media icons and newsletter signup forms not detailed here.
- The `button-outline` hover state (10% opacity red tint) is an assumption; the live site may use a different approach.
