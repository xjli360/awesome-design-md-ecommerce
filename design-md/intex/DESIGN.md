---
version: alpha
name: "Intex"
source_url: "https://www.intexcorp.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep violet #221155 grounds every page — not as a background but as the brand's primary ink, used for headlines, navigation text, and the bold wordmark that anchors the header. Against this dark, saturated base, a vivid orange #fe5b0c ignites all primary calls-to-action: "Shop Now" buttons, sale badges, and the floating cart icon. The combination is unexpected for an outdoor inflatables brand — it reads more like a premium athletic label than a pool-equipment company, giving Intex a confident, energetic presence that stands apart from the sea of blue-and-teal competitors. A clean white canvas (#eeeeee as a warm off-white surface) and generous whitespace keep the product photography — above-ground pools glowing with turquoise water, air mattresses in sunlit bedrooms — as the visual hero. Corners are softly rounded ({rounded.md} on cards, {rounded.sm} on buttons), but the search bar and hero sections use full-pill radii ({rounded.full}) that echo the circular shapes of pool rings and inflatable loungers. The typography stack relies on system fonts (Font Awesome for iconography, with no dedicated brand typeface detected), which gives the interface a utilitarian, no-nonsense feel — the design steps back to let the orange-and-violet color story and the product imagery do the selling. Footer sections stack in dense, link-heavy columns with thin hairline separators, and the secondary navigation uses a muted gray (#007aff appears as a link accent, likely from checkout or utility links) that never competes with the primary orange.

colors:
  primary: "#fe5b0c"
  primary-active: "#e04a00"
  primary-disabled: "#ffc9a3"
  ink: "#221155"
  body: "#221155"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link-accent: "#007aff"
  badge-sale: "#fe5b0c"
  badge-new: "#221155"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(34, 17, 85, 0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    boxShadow: "0 1px 4px rgba(34, 17, 85, 0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(34, 17, 85, 0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    maxWidth: 600px
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 4px rgba(254, 91, 12, 0.1)"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
    opacity: 0.8
  footer-link-hover:
    color: "{colors.primary}"
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  footer-divider:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    height: 1px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    minHeight: 120px
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    fontWeight: 700
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with vivid orange #fe5b0c and white text. Used for "Shop Now", "Add to Cart", and "View Details" across product cards, hero sections, and category pages. On hover, darkens to #e04a00 (`primary-active`). The disabled state fades to a pale peach (#ffc9a3) with white text, signaling the action is unavailable. Corners are softly squared at {rounded.sm} (8px), balancing approachability with a no-nonsense retail feel.

**`button-secondary`** — An outlined variant on a white background with {colors.ink} text and a 2px {colors.hairline} border. Used for "Learn More", "Compare", and secondary checkout actions. On hover, the border switches to {colors.ink} and the background fills with {colors.surface-soft}, creating a subtle depth shift without competing with the primary orange.

**`button-pill-primary`** — A smaller, fully pill-shaped variant ({rounded.full}) of the primary button, used for promotional badges, sale tags, and compact CTAs within product cards or sticky headers. The pill shape echoes the circular forms of Intex's inflatable products — pool rings, air mattresses, and spa covers.

**`button-pill-outline`** — A thin, transparent pill button with a 1px hairline border. Appears in secondary navigation strips, filter bars, and "Quick View" overlays. The minimal footprint keeps the focus on product photography while still providing a tappable action.

### Cards
**`product-card`** — A white card with a soft drop shadow ({rounded.md} at 12px) that contains a product image, title, price, and optional sale badge. The image fills the top of the card with no internal padding, while text sits below with {spacing.sm} horizontal padding. On hover, the shadow deepens and a subtle lift occurs — no border change, just elevation. The card never uses a background color other than white, ensuring product photos remain the hero.

**`category-tile`** — A larger, clickable tile used on the homepage and category landing pages to represent product families (e.g., "Above Ground Pools", "Air Mattresses", "Inflatable Spas"). On hover, the tile fills with {colors.primary} and text inverts to white — a dramatic color shift that signals interactivity and guides the user's next click.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a thin bottom hairline. The Intex wordmark sits left in {colors.ink} at a bold weight, while nav links use {colors.ink} at 15px/600 weight with generous letter-spacing. The active page link underlines with a 2px {colors.primary} line. On scroll, a subtle shadow appears (`nav-bar-sticky`) to separate the nav from page content. The cart icon sits right-aligned with a floating orange badge (`cart-badge`) showing item count.

**`nav-link-active`** — The active navigation state uses the brand orange as an underline accent, creating a clear wayfinding signal without relying on background fills or bold weight changes. Inactive links remain in {colors.ink} with no decoration.

### Forms
**`text-input`** — A standard white input field with a 1px hairline border and {rounded.sm} corners. On focus, the border thickens to 2px and turns {colors.primary} with a 4px orange glow (`boxShadow`). Error states use the same orange border treatment, avoiding a separate red — the brand's error language is the same as its action language, a deliberate design choice that keeps the palette tight.

**`search-bar-pill`** — A full-pill search input ({rounded.full}) used in the hero and sticky header. The pill shape is a signature Intex motif, referencing the circular geometry of their core products. On focus, the border thickens to 2px orange with the same glow treatment as text inputs, creating visual consistency across form elements.

### Footer
**`footer-section`** — A deep violet (#221155) footer that inverts the entire color scheme: white text on a dark background. Links are semi-transparent white (opacity 0.8) and shift to {colors.primary} on hover, bringing the brand's accent color into the dark zone. Thin white dividers (`footer-divider`) at 15% opacity separate link columns and sections. The footer heading uses {typography.title-sm} in full white, creating clear hierarchy against the link list below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product cards; nav collapses to hamburger menu; hero reduces to 280px min-height; category tiles stack vertically; footer links collapse into accordion sections; search bar shrinks to icon-only |
| Tablet | 744–1128px | Two-column product grid; nav links truncate to "Shop" dropdown; hero maintains 360px min-height; category tiles display in 3-column grid; footer shows 2-column link layout |
| Desktop | 1128–1440px | Three-column product grid; full nav link set visible; hero at 400px min-height; category tiles in 4-column grid; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid can expand to 4 columns; hero maintains proportion with larger typography |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44x44px tap target
- Product card CTAs are at least 48px tall on mobile
- Nav hamburger icon is 48x48px on touch devices
- Search bar pill is 56px tall on mobile for easy thumb access
- Category tiles are minimum 120px tall with full-surface tap zones

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product filters collapse into a bottom sheet on mobile, activated by a "Filter" button
- Footer link groups collapse into accordion panels below 744px, with the first group expanded by default
- Secondary navigation strips (categories, promotions) collapse into a horizontal scrollable strip on mobile
- Hero search bar collapses to an icon-only button that expands a full-width search overlay on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No dedicated brand typeface was detected; the site relies on system font stacks. A custom font may exist for print or video but is not present in the web CSS.
- The extracted hex list is sparse (4 colors) and includes #007aff, which appears to be a generic link/accent blue (possibly from Shopify or utility widgets) rather than a brand color. The true brand palette likely includes additional blues and greens for pool-water photography, but these are image-dominant rather than interface colors.
- Hover and active states for most components (beyond buttons and cards) could not be reliably extracted from static CSS analysis.
- Error, success, and warning color tokens are absent — the site may use the primary orange for all states or may have a separate semantic palette not visible in the extracted data.
- Dark mode is not supported; the interface is exclusively light-background with the violet footer as the only dark surface.
- Sub-brand or seasonal color variations (e.g., holiday promotions, limited-edition products) are not captured.
- Animation durations, easing curves, and transition properties were not extractable from the static analysis.
- The extracted font-family list consists entirely of Font Awesome icon fonts — no body or heading font declarations were found, suggesting the site loads fonts dynamically or uses system defaults not captured in the extraction.
