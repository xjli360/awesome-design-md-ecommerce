---
version: alpha
name: "Ciele Athletics"
source_url: "https://cieleathletics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built for runners who treat their gear as equipment, not fashion — and yet the electric #00bbff (Ciele Blue) hits like a shock of cold water on a hot pavement, the single color that owns every cap brim, every zipper pull, every "C" logo mark. That blue, paired with safety-cone orange-red #ff3442 and a near-black #111111, forms a three-color system that reads as urgent, athletic, and completely indifferent to trends. The site runs on a white #ffffff canvas with a soft gray #f5f5f5 surface for product cards, and uses #e8e8e8 hairline strokes to separate sections without visual weight. Typography leans on Montserrat at 400–600 weight — no heavy 700+ anywhere — giving headlines a clean, slightly compressed readability that matches the technical-fit language of the product copy. Buttons are full-bleed rectangles with {rounded.sm} corners, not pills; the brand avoids the friendly-orb aesthetic of lifestyle apps in favor of a more utilitarian, kit-like feel. Product photography is high-contrast, often shot against white or near-white backgrounds, with the Ciele Blue appearing as a deliberate accent — a cap worn backward, a reflective stripe, a logo hit. The footer collapses into a dense, single-column stack of legal and support links, and the nav bar uses a sticky white header with the logo centered and cart icon right-aligned. There is no hero slider, no lifestyle video autoplay — just a grid of product tiles, a search bar, and the implicit promise that the gear will outlast the run.

colors:
  primary: "#00bbff"
  primary-active: "#0099d6"
  primary-disabled: "#80ddff"
  ink: "#111111"
  body: "#333333"
  muted: "#aaaaaa"
  muted-soft: "#cccccc"
  hairline: "#e8e8e8"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ff3442"
  accent-red-dark: "#c31818"
  accent-red-darker: "#a70100"
  badge-green: "#62a667"
  badge-green-dark: "#478947"
  badge-gold: "#a77a06"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Century Gothic', 'League Spartan', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.ink}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-logo:
    height: 32px
  nav-cart-icon:
    height: 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.badge-green}"
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
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  social-icon:
    height: 24px
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Shop Now" actions. Filled with Ciele Blue {colors.primary} and white text in uppercase Montserrat 600. On hover, shifts to {colors.primary-active} (#0099d6). Disabled state uses {colors.primary-disabled} (#80ddff) with white text, signaling the action is unavailable. The button is a compact rectangle at 44px height with {rounded.sm} corners — no pill shapes, no gradients.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". White background with a 2px solid {colors.ink} border and {colors.ink} text. Hover state inverts to {colors.ink} background with white text. Same 44px height and {rounded.sm} corners as the primary button for visual consistency.

**`button-accent-red`** — Used sparingly for high-urgency actions like "Final Sale" or limited-edition drops. Filled with {colors.accent-red} (#ff3442) and white text. Same dimensions and typography as `button-primary`. Hover state darkens to {colors.accent-red-dark} (#c31818).

### Cards
**`product-card`** — A minimal, borderless card with no rounded corners. The product image sits on a {colors.surface-soft} (#f5f5f5) background, with the title set in {typography.title-sm} and price in {typography.body-md} below. There is no shadow, no border — the card relies on the white canvas and the product photography to create separation. On hover, the image may scale slightly (1.02x) but the card itself remains static.

**`product-badge-sale`** — A small, rectangular badge pinned to the top-left corner of the product image. Uses {colors.accent-red} background with white uppercase text at 11px. Tight padding (2px 8px) and {rounded.xs} corners keep it from competing with the product.

**`product-badge-new`** — Same shape and size as the sale badge, but uses {colors.badge-green} (#62a667) to signal new arrivals. The green is muted enough to not clash with the Ciele Blue system.

**`product-badge-sold-out`** — Uses {colors.muted} (#aaaaaa) background with white text. Indicates the item is unavailable without the urgency of the red badge.

### Navigation
**`nav-bar`** — A sticky white header at 64px height with a thin {colors.hairline} bottom border. The Ciele Athletics logo is centered, with a search icon and cart icon on the right. On mobile, the nav collapses to a hamburger menu with a full-screen overlay. The logo is 32px tall and uses the Ciele Blue for the "C" mark.

**`nav-link`** — Used in the mobile menu and footer. Set in Montserrat 500 at 14px with no letter-spacing. In the footer, links are {colors.muted} and turn white on hover.

### Forms
**`text-input`** — A standard input field for search, email signup, and checkout forms. White background with a 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border switches to {colors.primary}. Height is 48px with 12px 16px padding for comfortable typing.

**`search-bar`** — A pill-shaped search input with {rounded.full} corners, used in the header and on collection pages. Background is {colors.surface-soft} with a 1px {colors.hairline} border. The placeholder text is {colors.muted} and the input text is {colors.body}. Height is 44px with 10px 20px padding.

### Footer
**`footer`** — A dark section with {colors.ink} background and white text. Contains columns for support, about, and social links. Headings use {typography.title-sm} in white, links use {typography.link} in {colors.muted}. On mobile, the columns stack vertically with {spacing.lg} between sections. Social icons are 24px and use {colors.muted} as the default fill, turning white on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; footer stacks vertically; search bar moves below nav; badges remain but scale down slightly |
| Tablet | 744–1128px | Nav shows full links (Shop, Explore, About); product grid is 2–3 columns; footer shows 2-column layout; search bar is inline in header |
| Desktop | 1128–1440px | Full nav with all links; product grid is 3–4 columns; footer shows 4-column layout; search bar is prominent in header |
| Wide | > 1440px | Max-width container at 1440px; product grid may show 4 columns; all elements centered with generous margins |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px
- Nav hamburger icon is 48x48px
- Cart icon is 48x48px
- Search bar has 44px height for easy tapping
- Product card images are tappable with no minimum size, but the card itself is at least 200px wide on mobile

### Collapsing Strategy
- Nav links collapse to hamburger menu below 744px
- Product grid collapses from 4 columns to 2 columns at tablet, to 1 column at mobile
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile
- Search bar collapses from inline to below the nav on mobile
- Product badges remain visible but may overlap differently on smaller cards

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (image zoom percentage, shadow depth) could not be reliably extracted
- Error styling for form inputs (validation colors, error message typography) not found in extraction
- Active/visited states for footer links not confirmed
- Sub-brand or collection-specific color palettes (e.g., "Ciele x [collaborator]") not extracted
- Dark mode or high-contrast mode not detected
- Loading states and skeleton screens not observed
- The extracted font list includes multiple candidates (Montserrat, Poppins, Roboto, Century Gothic, League Spartan); Montserrat is the most frequently declared and is used as the primary, but the exact fallback stack may differ
- The extracted hex list is large (17+ colors) and includes probable Shopify checkout widget colors (#478947, #62a667 for green; #a77a06 for gold) and social icon defaults — the true brand palette is likely smaller: #00bbff (primary), #111111 (ink), #ff3442 (accent), #ffffff (canvas), #f5f5f5 (surface), #e8e8e8 (hairline)
- Button hover transitions (duration, easing) not extracted
- Cart drawer or mini-cart styling not observed
- Mobile menu animation (slide, fade, overlay) not confirmed
