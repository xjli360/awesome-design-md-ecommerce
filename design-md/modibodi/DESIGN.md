---
version: alpha
name: "Modibodi"
source_url: "https://modibodi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy canvas at #272d45 sets the tone for a brand that treats period and incontinence care with the same seriousness as premium activewear — no pastels, no euphemisms, just a confident, body-positive palette anchored on a dark, almost indigo primary. The orange accent at #f65934 cuts through that navy like a safety flare, appearing on size-selection badges, cart indicators, and promotional banners; it’s the brand’s single moment of heat against an otherwise cool spectrum of slate (#676986), charcoal (#1d1d1d), and off-white (#f4f4f6). Founders Grotesk runs the typography with a slightly condensed, utilitarian feel — display sizes sit at 24–32px with generous tracking, while body copy at 14–16px stays legible and unfussy. Product cards use a soft {rounded.sm} corner radius and a clean white surface (#ffffff) that lifts the product photography, while the primary CTA button — a solid navy rectangle with {rounded.sm} — never competes with the imagery. The brand’s signature move is the “Leak-Free Guarantee” badge: a {rounded.full} pill in orange (#f65934) or yellow (#ffcf2a) that sits on the product image, a visual shorthand for performance that the customer scans before reading any copy. Navigation is a fixed top bar with a dark background (#1d1d1d), white text, and a search icon that expands into a full-width input on focus — utilitarian, no decorative flourishes. The footer repeats the dark canvas with dense link columns and a sustainability callout in the brand’s muted green (#67c116), a secondary accent used sparingly for eco-badges and carbon-neutral shipping labels. Every surface — from the sticky cart drawer to the size-guide modal — uses {rounded.sm} or {rounded.md}, never a hard corner, but never a pill either; the brand avoids the “friendly” associations of extreme rounding in favor of a precise, technical feel. The overall mood is one of quiet competence: the navy says “trust us,” the orange says “this works,” and the white space says “we know you’re here for function, not frills.”

colors:
  primary: "#272d45"
  primary-active: "#1d1d1d"
  primary-disabled: "#676986"
  ink: "#1d1d1d"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#e5e5eb"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f65934"
  accent-yellow: "#ffcf2a"
  accent-green: "#67c116"
  badge-new: "#f65934"
  badge-guarantee: "#ffcf2a"
  badge-eco: "#67c116"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Founders Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 14px 28px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-orange-active:
    backgroundColor: "#d94a2a"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill-guarantee:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 28px
  button-pill-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 28px
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
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-mobile:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-expanded:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 56px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-badge-guarantee:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  size-selector-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  size-selector-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  cart-item-quantity:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Shop Now,” and checkout entry points. A solid navy rectangle with {rounded.sm} and white Founders Grotesk at 15px with 0.5px letter spacing. On hover and active states, the background deepens to {colors.primary-active} (#1d1d1d). The disabled state uses {colors.primary-disabled} (#676986) with no border, signaling the button is non-interactive without visual clutter.

**`button-secondary`** — An outlined variant for secondary actions like “Learn More” or “View Sizing Guide.” White background with a 2px solid {colors.primary} border and navy text. Active state swaps to {colors.surface-soft} background and {colors.primary-active} border. Height and padding match the primary button to maintain alignment in form layouts.

**`button-accent-orange`** — Used for high-visibility promotions, limited-time offers, and the “Leak-Free Guarantee” CTA in hero sections. Solid {colors.accent-orange} (#f65934) background with white text. Active state darkens to #d94a2a. This button is the brand’s visual exclamation point — used sparingly, once per page maximum.

**`button-pill-guarantee`** and **`button-pill-eco`** — Small pill-shaped badges that sit on product cards and detail pages. The guarantee badge uses {colors.accent-yellow} (#ffcf2a) with dark text; the eco badge uses {colors.accent-green} (#67c116) with white text. Both use {rounded.full}, uppercase 11px bold type, and tight 6px 16px padding. These are not clickable CTAs — they are static trust signals.

### Cards
**`product-card`** — The primary product display unit, used in collection grids, search results, and cross-sells. A white surface with {rounded.sm} containing a product image (also {rounded.sm}), title in {typography.title-sm}, price in {typography.body-md}, and up to three badge positions (new, guarantee, eco). No shadow on the card itself — the brand relies on the white surface against {colors.surface-soft} (#f4f4f6) page backgrounds for separation. Hover state adds a subtle 1px {colors.hairline} border.

**`product-card-badge`** — Positioned absolutely on the top-left of the product image. Three variants: orange for “New,” yellow for “Leak-Free Guarantee,” green for “Eco” or “Sustainable.” All use {rounded.full} pill shape, uppercase 11px bold type, and 4px 10px padding. Only one badge appears per card, prioritized in the order: guarantee > new > eco.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height on desktop, 56px on mobile, with a dark {colors.ink} (#1d1d1d) background. Contains the brand logo (left), navigation links in {typography.nav-link} (center), and utility icons for search, account, and cart (right). The search icon triggers an expandable `search-bar` that pushes the nav links into a hamburger menu on mobile. The cart icon displays a count badge in {colors.accent-orange}.

**`search-bar`** — A standard input with {rounded.sm}, 1px {colors.hairline} border, and 44px height. On focus, the bar expands to 56px height and the border switches to {colors.primary}. On mobile, the search bar takes full width below the nav bar when activated.

### Forms
**`text-input`** — Used in checkout, account creation, and size-guide forms. A 48px tall input with {rounded.sm}, 1px {colors.hairline} border, and 12px 16px padding. Focus state swaps the border to {colors.primary}. Error state (not fully extracted) likely uses a red border — noted in Known Gaps.

**`size-selector-pill`** — A pill-shaped button for size selection (XS–4XL) on product detail pages. White background with 1px {colors.hairline} border, 36px height, and 8px 16px padding. Active state fills with {colors.primary} and white text. Multiple pills can be active for multi-pack purchases.

### Footer
**`footer-section`** — A full-width dark section with {colors.ink} background, containing link columns, a newsletter signup, and sustainability callouts. Links use {colors.muted-soft} (#e5e5eb) for legibility against the dark background. Column headings are in {typography.title-sm} with uppercase transformation. The newsletter input follows `text-input` styling but with a white border on the dark background.

### Modals & Drawers
**`cart-drawer`** — A slide-in panel from the right side of the viewport, using {rounded.sm} on the top-left and bottom-left corners. White background with a semi-transparent {colors.scrim} overlay behind it. Contains cart items, quantity selectors (`cart-item-quantity`), and the `button-primary` checkout CTA.

**`modal-content`** — Used for size guides, product quick-views, and promotional popups. A white surface with {rounded.md} (12px) — the only component using this radius. Includes a close button in the top-right corner. The overlay uses `modal-overlay` at 60% opacity black.

### Accordion
**`accordion-header`** — Used in FAQ sections and product detail “Details & Care” panels. A {colors.surface-soft} background with {rounded.sm}, 16px 24px padding, and {typography.title-sm} text. Clicking toggles the `accordion-content` panel, which uses white background and {typography.body-sm} with the same horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; product grid goes single-column; search bar becomes full-width below nav; size-selector pills stack vertically; cart drawer takes full width |
| Tablet | 744–1128px | Nav links visible but condensed; product grid at 2 columns; search bar remains inline; footer columns collapse to 2 |
| Desktop | 1128–1440px | Full nav with all links; product grid at 3–4 columns; search bar in nav; footer at 4 columns |
| Wide | > 1440px | Max-width container at 1440px; product grid at 4 columns; whitespace increases on left/right margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height on mobile.
- Size-selector pills are 36px tall — slightly below the 44px recommendation but acceptable for a non-primary action.
- Cart drawer close button is 44x44px.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px.
- Product grid collapses from 4 columns (desktop) to 2 (tablet) to 1 (mobile).
- Footer link columns collapse from 4 to 2 to a single stacked layout.
- Search bar collapses from inline to full-width overlay on mobile.
- Cart drawer slides in from the right on all breakpoints but takes full width on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states:** Only primary and secondary button hover states were reliably extracted. Hover states for links, badges, and footer items are inferred from standard web patterns but not confirmed.
- **Error states:** Form validation styling (red borders, error messages) was not present in the extracted data. The error state for `text-input` is assumed to use a red border (#c13515 or similar) but not confirmed.
- **Dark mode:** No dark mode implementation was detected. The brand uses a dark nav and footer but the main canvas is always white.
- **Sub-brand palettes:** Modibodi may have sub-brand color variations (e.g., for Modibodi Kids or Modibodi Men) that were not captured in the extraction.
- **Animation & transitions:** No timing or easing values were extracted. The cart drawer likely uses a 300ms ease-in-out slide, but this is unconfirmed.
- **Font weights:** Founders Grotesk weights were inferred from common web usage (400, 500, 600). The exact weight for each token may vary slightly from the live site.
- **Spacing tokens:** The spacing scale is a standard 4px grid system. Exact padding/margin values for specific components (e.g., product card gap, footer column gap) were not extracted and use reasonable defaults.
- **Checkout flow:** Shopify checkout styling (Shopify Pay button, Klarna/Afterpay widgets) was filtered from the extracted colors. The brand’s checkout may use different colors than the main site.
- **Accessibility:** Focus ring styles, skip-to-content links, and ARIA labels were not extracted. The brand likely follows standard accessibility practices but this is unconfirmed.
- **Image treatment:** Product images appear to use a white background with no overlay or gradient. Lifestyle photography styling was not extracted.
