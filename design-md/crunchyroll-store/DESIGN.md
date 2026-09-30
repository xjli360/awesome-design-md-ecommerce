---
version: alpha
name: "Crunchyroll Store"
source_url: "https://store.crunchyroll.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  An orange voltage — #ff5e00 — pulses through every primary action, every add-to-cart button, every search bar, and every promotional banner across this anime marketplace, making the store feel less like a checkout funnel and more like a convention floor lit by neon. The brand's custom typeface Crunchyroll Atyp carries the weight of display headlines in bold weights while body copy settles into Lato at 14–16px, a pragmatic pairing that lets the orange sing without competing for attention. Product cards stack on a near-black canvas (#181818) with white surfaces (#ffffff) floating above, each card softly contained by {rounded.sm} corners and a thin hairline (#d1d1d1) that separates items without visual noise. Badges — "Sale", "Exclusive", "Pre-order" — appear as compact pills in orange (#ff5e00) or a secondary blue (#029ddf) or red (#ea001e), each one a tiny signal that the catalog is event-driven, not static. The top navigation bar runs the full width of the viewport, a dark strip (#1a1918) with white text and a prominent search bar that uses {rounded.full} to feel approachable, not technical. Category links (Anime, Manga, Figures, Apparel, Home & Living) sit in a horizontal scrollable strip below the nav, each link underlined on hover with a 2px orange rule. The footer is dense and dark (#141519), with columns of links in muted gray (#747474) and social icons that inherit their brand colors (YouTube red, Twitter blue, Instagram pink) — the only place the system relaxes its orange grip. What makes the Crunchyroll Store feel distinct is the way orange acts as both accent and structure: it fills buttons, borders, sale badges, and even the loading spinner, but never overwhelms the product photography. The palette's secondary colors — a cool blue (#029ddf), a warm yellow (#fab818), and a restrained green (#2e844a) — handle status signals (in-stock, pre-order, sold-out) while orange owns conversion. The result is a store that feels urgent without being aggressive, collectible without being precious, and unmistakably tied to the Crunchyroll brand identity across streaming, events, and merchandise.

colors:
  primary: "#ff5e00"
  primary-active: "#e05200"
  primary-disabled: "#ffb380"
  ink: "#181818"
  body: "#23252b"
  muted: "#747474"
  muted-soft: "#a0a0a0"
  hairline: "#d1d1d1"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-bg: "#1a1918"
  footer-bg: "#141519"
  accent-blue: "#029ddf"
  accent-red: "#ea001e"
  accent-yellow: "#fab818"
  accent-green: "#2e844a"
  badge-sale: "#ff5e00"
  badge-exclusive: "#029ddf"
  badge-preorder: "#ea001e"
  star-rating: "#fab818"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Crunchyroll Atyp', 'Nutmeg', Lato, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Crunchyroll Atyp', 'Nutmeg', Lato, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Crunchyroll Atyp', 'Nutmeg', Lato, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Crunchyroll Atyp', 'Nutmeg', Lato, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Lato, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Lato, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Lato, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Lato, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Lato, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Lato, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Lato, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "Lato, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Lato, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  category-link:
    fontFamily: "Lato, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    padding: 12px 24px
    height: 48px
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
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 24px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.category-link}"
    height: 48px
  category-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.category-link}"
    borderBottom: "2px solid {colors.primary}"
  category-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.category-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.body-sm}"
    color: "{colors.primary}"
    fontWeight: 700
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.sm}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The workhorse of the store, rendered in #ff5e00 with white text and {rounded.sm} corners. On hover, it shifts to #e05200 with a subtle darkening. The disabled state uses #ffb380, signaling the action is unavailable without the visual weight of the active state. Height is 48px with 12px top/bottom padding and 24px horizontal padding, giving it a substantial feel that matches the bold typography.

**`button-secondary`** — A white button with a 2px #ff5e00 border, used for "Add to Wishlist", "View Details", and secondary checkout actions. On hover, the background shifts to #f8f8f8 and the border remains orange. The text color is #181818 in the default state, matching the ink token.

**`button-tertiary`** — A text-only button with no background or border, used for "Cancel", "Clear Filters", and other low-emphasis actions. The text is #ff5e00, and on hover it gains a subtle underline. This preserves the orange voltage without competing with primary buttons.

**`button-pill-primary`** — A compact, fully rounded pill used for "Shop Now" promotions in hero banners and category headers. Uses {rounded.full} and smaller typography ({typography.button-sm}) to fit into tight promotional spaces while maintaining the orange identity.

### Navigation
**`top-nav`** — A full-width dark strip (#1a1918) at 64px height, containing the Crunchyroll logo, navigation links in white, and the search bar. The background is nearly black, creating a strong contrast with the white canvas below. Navigation links use {typography.nav-link} (14px, weight 600) and gain an orange underline on hover.

**`category-strip`** — A horizontal scrollable strip below the top nav, 48px tall with a white background. Category names are uppercase 14px weight 600 in #747474 (inactive) or #ff5e00 (active), with a 2px orange bottom border on the active category. This strip is the primary way users navigate between Anime, Manga, Figures, Apparel, and Home & Living.

**`search-bar-pill`** — A compact, fully rounded search input at 40px height, sitting inside the top nav. The background is white, text is #181818, and the placeholder text is #a0a0a0. On focus, the border shifts to 2px #ff5e00. The pill shape ({rounded.full}) makes it feel friendly and approachable, not like a database query.

### Cards
**`product-card`** — The fundamental content unit of the store, a white card with {rounded.sm} corners and 8px padding. Each card contains a 1:1 aspect ratio product image with {rounded.xs} corners, a title in {typography.title-sm} (16px weight 600), and a price in {typography.body-sm}. On hover, the card gains a subtle box shadow (0 4px 12px rgba(0,0,0,0.1)) to indicate interactivity. Sale prices render in #ff5e00 with weight 700.

**`product-card-image`** — The product image within a card, cropped to a 1:1 square with {rounded.xs} corners. Images are the primary visual element, and the subtle corner rounding prevents them from feeling too sharp against the card's {rounded.sm} container.

### Badges
**`badge`** — A compact pill badge in #ff5e00 with white text, using {typography.badge} (11px weight 700, uppercase, 0.5px letter spacing). Used for "Sale" and "Deal" labels. The pill shape ({rounded.full}) with 2px vertical and 8px horizontal padding makes it unobtrusive but visible.

**`badge-blue`** — A blue variant (#029ddf) for "Exclusive" and "Limited Edition" labels, distinguishing collectible items from sale items.

**`badge-red`** — A red variant (#ea001e) for "Pre-order" labels, signaling urgency and future availability.

**`badge-green`** — A green variant (#2e844a) for "In Stock" and "Available" labels, providing positive confirmation for shoppers.

### Forms
**`text-input`** — A standard text input with white background, 1px #d1d1d1 border, and {rounded.sm} corners. On focus, the border becomes 2px #ff5e00, maintaining the orange voltage. Height is 48px with 12px vertical padding, matching the primary button height for alignment in forms.

**`select-dropdown`** — A dropdown selector with the same visual treatment as text inputs but at 44px height. Used for sorting (Price Low-High, Newest, Best Sellers) and filtering (Category, Price Range). The dropdown arrow is rendered in #747474.

### Footer
**`footer-section`** — A dense, dark footer (#141519) with columns of links in #747474. The footer heading uses {typography.title-sm} in white, and links use {typography.link} in #747474. On hover, links shift to #ff5e00. The footer contains links to Help, About, Terms, Privacy, and Social Media, plus a newsletter signup form.

**`footer-link`** — Standard footer links in #747474 with {typography.link} (14px weight 400). On hover, the color shifts to #ff5e00, providing a subtle orange accent in the otherwise muted footer.

### Hero
**`hero-banner`** — A full-width promotional banner with a near-black (#181818) background and white text. The banner uses {typography.display-lg} for the headline and contains a {rounded.sm} orange CTA button. The banner may include background imagery (anime key art) with a dark overlay for readability.

**`hero-banner-cta`** — The primary call-to-action button inside hero banners, using #ff5e00 with white text and {rounded.sm} corners. The button is larger than standard buttons (12px 32px padding) to draw attention, and sits below the headline with {spacing.lg} margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; category strip becomes a single-row scroll; product cards go to 2-column grid; hero banner reduces to 200px height; search bar collapses to icon-only |
| Tablet | 744–1128px | Top nav shows limited links (Anime, Manga, Figures); category strip is fully visible; product cards in 3-column grid; hero banner at 300px height |
| Desktop | 1128–1440px | Full top nav with all links; category strip with all categories; product cards in 4-column grid; hero banner at 400px height |
| Wide | > 1440px | Maximum content width of 1440px with centered layout; product cards in 5-column grid; hero banner at 450px height |

### Touch Targets
- All buttons and interactive elements are minimum 44px height for touch accessibility
- Category strip links are minimum 48px height for easy tapping
- Product cards have a minimum 80px touch area for the entire card
- Search bar is 40px height on mobile, expanding to full width on tap

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay with all navigation links, search, and account options
- Category strip collapses to a single horizontal scroll on mobile, with the active category pinned to the left
- Product cards go from 5-column grid on wide screens to 2-column on mobile, with single-column on very small screens (< 480px)
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections
- Hero banner reduces height significantly on mobile, with text overlay becoming more compact

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes many framework and third-party widget colors (Shopify Pay blue #0176d3, Klarna pink #a259ff, Afterpay blue #016fd0, Figma green #0acf83, social media brand colors) that are not part of the Crunchyroll Store design system. These have been excluded from the color palette.
- The exact font weights and sizes for Crunchyroll Atyp could not be reliably extracted from the CSS. The values provided are estimates based on common usage patterns and the Lato fallback.
- Hover, focus, and active states for most components (beyond buttons) could not be extracted. The provided hover states for product cards and footer links are reasonable defaults.
- Error styling for form inputs (red border, error message typography) could not be extracted.
- The exact spacing values for product card grids (gap between cards) could not be determined.
- Dark mode is not supported; the store uses a light canvas with dark nav and footer.
- The loading spinner animation details (speed, stroke width) could not be extracted.
- The newsletter signup form in the footer could not be fully analyzed for its styling.
- The mobile hamburger menu animation and overlay styling could not be extracted.
- The exact border radius for product card images ({rounded.xs}) is an estimate based on the card's {rounded.sm} value.
