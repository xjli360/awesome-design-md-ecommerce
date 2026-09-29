---
version: alpha
name: "First Lite"
source_url: "https://www.firstlite.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A backcountry performance system built on a near-black canvas (#141414) and a single, unmistakable voltage of burnt orange (#ff6319) that fires every primary CTA, add-to-cart button, and category badge. The palette is deliberately narrow — deep charcoal (#1a1a1a) and true black (#121212) for body text and structural elements, a cool mid-gray (#888888) for secondary information, and a warm off-white (#f9fafb) for surface cards that reads as snow light rather than sterile white. Heron Sans Condensed carries the brand's voice across every weight from Light to Bold Italic, its compressed letterforms evoking the tight, efficient packing of a hunting pack; Archivo Narrow appears as a secondary sans for dense product specs and filter labels. The system uses generous rounded corners at {rounded.lg} (20px) on product cards and {rounded.full} on the persistent search orb, but keeps navigation and text inputs at {rounded.sm} (8px) — a distinction that reads as "approachable but not soft." The signature design move is the "thermal" badge: a small, pill-shaped label in the brand orange with white text that sits on the top-left corner of product photography, mimicking the heat-signature patches on high-end merino base layers. Every product page uses a full-bleed hero image with a dark gradient scrim (#141414 at 60%) and the product name set in Heron Sans Cond Bold at 28px, creating a silhouette effect that prioritizes the garment's form over fabric detail. The checkout flow strips all chrome — no top nav, no footer — leaving only the orange CTA against the charcoal canvas, a moment of pure conversion focus.

colors:
  primary: "#ff6319"
  primary-active: "#e55514"
  primary-disabled: "#ffb08c"
  ink: "#141414"
  body: "#1a1a1a"
  muted: "#888888"
  muted-soft: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-warm: "#edf5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#ff6118"
  accent-terracotta: "#e56c34"
  badge-bg: "#ff6319"
  badge-text: "#ffffff"
  scrim: "#141414"
  error: "#c13515"
  success: "#108474"

typography:
  display-xl:
    fontFamily: "'Heron Sans Cond Bold', 'Heron Sans Cond', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Heron Sans Cond Bold', 'Heron Sans Cond', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Heron Sans Cond Semibold', 'Heron Sans Cond', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Heron Sans Cond Medium', 'Heron Sans Cond', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Heron Sans Cond Medium', 'Heron Sans Cond', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Heron Sans Cond Regular', 'Heron Sans Cond', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo Narrow', 'Heron Sans Cond Regular', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo Narrow', 'Heron Sans Cond Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Heron Sans Cond Bold', 'Heron Sans Cond', Georgia, serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Heron Sans Cond Semibold', 'Heron Sans Cond', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Heron Sans Cond Medium', 'Heron Sans Cond', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  link:
    fontFamily: "'Archivo Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Heron Sans Cond Medium', 'Heron Sans Cond', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link-active:
    fontFamily: "'Heron Sans Cond Semibold', 'Heron Sans Cond', Georgia, serif"
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
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
    padding: 13px 23px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 22px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-orange:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link-active}"
    padding: 8px 12px
  search-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
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
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-thermal:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    position: "top-left"
  badge-sale:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    height: 480px
  hero-scrim:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-active}"
    border-bottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.on-dark}"
    typography: "{typography.title-sm}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  review-star:
    color: "{colors.ink}"
    size: 16px
  review-star-empty:
    color: "{colors.hairline}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's burnt orange (#ff6319) with white uppercase text in Heron Sans Cond Semibold. Used for "Add to Cart," "Checkout," and primary form submissions. On hover, shifts to `button-primary-active` (#e55514) for a subtle darkening; disabled state uses `button-primary-disabled` (#ffb08c) with reduced contrast. The 8px corner radius (`{rounded.sm}`) keeps the button feeling precise rather than playful.

**`button-secondary`** — A white canvas button with dark ink text, used for "View Details," "Learn More," and secondary actions alongside the primary. The outline variant (`button-secondary-outline`) adds a 1px hairline border for situations where the button needs to sit on a colored surface without a white background. Both maintain the same 48px height and uppercase Heron Sans Cond Medium typography.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel," "Clear Filters," and inline navigation. Inherits the same uppercase Heron Sans Cond Medium treatment but at a smaller weight, relying on the brand's charcoal ink color for visibility.

**`button-pill-orange`** — A fully pill-shaped variant (`{rounded.full}`) used for filter chips, category tags, and quick-add actions. Smaller at 32px height with tighter padding, this button reads as a badge-like interactive element rather than a full CTA.

### Navigation
**`top-nav`** — A fixed 64px bar on the near-black ink background (#141414) with white navigation links set in Heron Sans Cond Medium uppercase. The brand logo sits left-aligned as a white wordmark; the center holds 4-5 category links (Men's, Women's, Gear, Sale, About). The right side contains a search orb and a cart icon, both in the brand orange. On scroll, the bar remains fixed with a subtle 1px bottom border in a slightly lighter dark (#2a2a2a).

**`nav-link`** — Standard navigation links in white uppercase Heron Sans Cond Medium with 8px vertical padding. Active state (`nav-link-active`) switches to the brand orange and a semibold weight, signaling the current section without an underline or background change.

**`category-strip`** — A secondary horizontal scroll strip below the hero, containing product categories (e.g., "Base Layers," "Insulation," "Rainwear"). Inactive tabs use the muted gray (#888888); active tab uses ink (#1a1a1a) with a 2px orange underline. This strip collapses to a dropdown on mobile.

### Cards
**`product-card`** — A white card with 20px rounded corners (`{rounded.lg}`) containing a full-width product image, title, and price. The image area uses the same top corner radius, creating a continuous curve from image to card. No shadow — the card relies on the contrast between the white surface and the off-white canvas (#f9fafb) background of the grid. Hover state adds a 1px orange border (#ff6319) and a subtle scale transform (1.02).

**`badge-thermal`** — The brand's signature badge: a small orange pill with white uppercase text, positioned at the top-left of product images. Mimics the heat-signature patches found on high-end merino base layers. Used for "NEW," "BEST SELLER," and "LIMITED EDITION" labels. Sale badges use the green (#108474) and "New Arrivals" use the ink (#141414).

### Forms
**`text-input`** — A standard 48px input field with 8px rounded corners, white background, and a 1px hairline border (#dedede). On focus, the border switches to the brand orange (#ff6319) for clear active state. Used for email signup, search queries, and checkout forms.

**`size-selector`** — A pill-shaped button group for product size selection (S, M, L, XL). Inactive buttons have a white background with hairline border; active button fills with ink (#141414) and white text. The active state mirrors the brand's high-contrast approach — no orange needed for selection feedback.

**`quantity-stepper`** — A compact 40px control with minus, number, and plus buttons, bordered by a hairline stroke. Used on product pages and cart items. The number display uses body-md typography; the buttons use a lighter weight for visual hierarchy.

### Footer
**`footer`** — A full-width section on the ink background (#141414) with white headings and muted gray (#7b7b7b) links. Organized in a 4-column grid: Shop, Support, About, and Connect. The bottom bar contains legal links and a copyright notice in caption-sm. No orange accents — the footer is purely informational, letting the brand's dark canvas do the work.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; category-strip becomes a dropdown; hero height reduces to 320px; product cards stack vertically |
| Tablet | 744–1128px | 2-column product grid; top-nav shows 3 center links; category-strip remains horizontal scroll; hero at 400px |
| Desktop | 1128–1440px | 3-column product grid; full top-nav with all links; category-strip fully visible; hero at 480px |
| Wide | > 1440px | 4-column product grid; max-width container at 1440px; hero at 520px with larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px touch target height
- Search orb is 40px × 40px with 12px internal padding for finger clearance
- Size selector pills are 44px tall with 16px width per size
- Quantity stepper buttons are 40px × 40px tap areas
- Accordion triggers have 48px minimum touch height

### Collapsing Strategy
- Top navigation collapses to a hamburger icon at < 744px; the menu slides in from the left with a dark overlay
- Category strip collapses to a single "Shop All" dropdown at < 744px
- Product grid collapses from 3 columns to 2 at tablet, then 1 at mobile
- Footer collapses from 4 columns to 2 at tablet, then a single vertical stack at mobile
- Accordion sections (product details, shipping info) are collapsed by default on mobile, expanded on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary buttons and text inputs were inferred from common patterns; exact extracted values not available
- Error styling for form validation (border colors, error message typography) could not be reliably extracted
- Dark mode preferences or alternate color schemes not detected
- Sub-brand or collection-specific palette variations (e.g., "First Lite Women's" or "First Lite Pro") not extracted
- Animation durations and easing curves (button hover, card hover, nav transitions) not captured
- Dropdown menu styling (mega-menu, flyout) not extracted from live site
- Checkout flow styling (Shopify checkout overrides) not captured — may use default Shopify colors
- Product swatch colors (for color variants) not extracted; only the brand's primary orange and green were detected
- Loading states (skeleton screens, spinner colors) not available
- Focus ring styles (outline, offset) not extracted
- Print stylesheet behavior not documented
