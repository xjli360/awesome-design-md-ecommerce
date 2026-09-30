---
version: alpha
name: "Parade Organics"
source_url: "https://parade.ca"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baby-clothing brand that builds its visual identity around a soft, almost powdery blue (#9ebadc) — not the pastel pink or sage green you might expect from organic infant wear, but a cool, airy tone that appears on buttons, badges, and hover states throughout the site. This blue sits against a canvas of warm off-white (#fff7f2) and layered grays (#dedede, #e5e5e5, #f5f5f5) that give the interface a laundered-soft feel, like well-worn cotton sheets. The brand's secondary accent is a muted olive (#729311) — an unexpected, earthy counterpoint to the blue, used sparingly for sale badges and price highlights. Typography runs DM Sans at moderate weights (400–500 for body, 600 for buttons and headings), with generous line spacing that keeps the reading rhythm slow and gentle — appropriate for sleepwear and loungewear. Cards use soft rounding (`{rounded.sm}` ~8px) rather than pills, and the primary button sits at `{rounded.md}` (12px), a shape that reads as approachable but not infantilizing. The overall mood is calm, clean, and slightly Scandinavian — white space is used generously, borders are thin and gray (`{colors.hairline}` #e6e6e6), and the only bright voltage comes from a coral-red (#ff6d6d) used for error states and a deep navy (#2c2a41) for footer backgrounds. The brand trusts its product photography (sleeping babies, soft fabrics) to carry warmth rather than relying on decorative illustration or heavy typography.

colors:
  primary: "#9ebadc"
  primary-active: "#4b556c"
  primary-disabled: "#d4d2e2"
  ink: "#2c2a41"
  body: "#3c3c3c"
  muted: "#777575"
  muted-soft: "#979797"
  hairline: "#e6e6e6"
  hairline-soft: "#eeeeee"
  canvas: "#fff7f2"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-olive: "#729311"
  accent-coral: "#ff6d6d"
  accent-navy: "#2c2a41"
  accent-blue-light: "#a3daff"
  accent-purple: "#7069bc"
  accent-orange: "#ec8816"
  accent-red: "#d10000"

typography:
  display-xl:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.2px
  badge:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.muted}"
  button-olive:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.accent-coral}"
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
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sold-out-badge:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 1
  badge-new:
    backgroundColor: "{colors.accent-blue-light}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.base} 0"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with the signature powder blue (#9ebadc) and white text. Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, the background shifts to a deeper slate blue (#4b556c) via `button-primary-active`. Disabled state uses a muted lavender-gray (#d4d2e2). All primary buttons use 12px rounding (`{rounded.md}`) — soft but not pill-shaped, keeping the interface feeling gentle without being childish.

**`button-secondary`** — An outlined variant on the warm off-white canvas (#fff7f2), with ink text (#2c2a41) and a thin hairline border (#e6e6e6). Used for "View Details", "Learn More", and secondary actions. Active state fills the background with the soft surface tone (#f5f5f5) and darkens the border to muted gray (#777575).

**`button-olive`** — A compact, low-height button using the earthy olive accent (#729311). Reserved for sale badges, price callouts, and small utility actions. Uses smaller typography (`{typography.button-sm}`) and tighter padding, making it feel like a tag or label rather than a full CTA.

### Cards
**`product-card`** — A clean, white card with soft 8px rounding (`{rounded.sm}`) and no border — the card floats on the surface-soft (#f5f5f5) or canvas (#fff7f2) background. The product image fills the top with matching corner rounding, followed by the product title in `title-sm` and price in `price` typography. Sale items show an olive badge (`product-card-sale-badge`) in the top-left corner of the image; sold-out items show a gray badge (`product-card-sold-out-badge`).

### Navigation
**`nav-bar`** — A fixed-height 64px bar on the warm canvas background, with a subtle bottom border in the softest hairline (#eeeeee). Navigation links use `nav-link` typography (14px, weight 500, slight letter-spacing). The active link switches to the primary blue (#9ebadc). On scroll, the bar gains a thin shadow and a slightly stronger border via `nav-bar-sticky`.

### Forms
**`text-input`** — Standard input fields with 8px rounding, a thin hairline border, and generous 12px/16px padding. Focus state swaps the border to the primary blue. Error state uses the coral accent (#ff6d6d) for the border — the only place this bright red appears in the interface.

### Footer
**`footer`** — A deep navy (#2c2a41) full-width section that anchors the bottom of every page. White text at 80% opacity for links, with full opacity on hover. The dark background provides strong contrast against the otherwise light, airy interface.

### Badges
**`badge-new`** — A light blue (#a3daff) badge for "New Arrivals" and recently added products. Uses uppercase 11px type with 0.5px letter-spacing. **`badge-sale`** uses the olive accent (#729311) for discount callouts. Both are compact (2px/8px padding) with minimal 4px rounding.

### Search
**`search-bar`** — A pill-shaped input field (`{rounded.full}`) with a thin hairline border, sitting on the warm canvas background. On focus, the border shifts to the primary blue. The pill shape is the only fully rounded element in the system, making the search action feel distinct and inviting.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero section reduces to 300px min-height; footer stacks vertically; buttons go full-width; search bar moves to persistent header |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 400px min-height; footer splits into two columns; search bar in header with icon trigger |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at 400px min-height; footer in four columns; search bar expanded in header |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero scales to 480px min-height; all spacing tokens scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain minimum 44px touch target height
- Icon buttons are 40x40px with full rounding
- Quantity selector and text inputs are 48px tall for comfortable tapping
- Product card images link to product pages with full-card tap zones on mobile

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer sections stack: 4 columns → 2 columns → 1 column
- Hero section text and CTA stack vertically on mobile
- Search bar collapses to an icon trigger on mobile, expanding on tap
- Accordion-style product descriptions replace side-by-side layouts on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary`, `text-input`, and `nav-link` are inferred from common patterns — exact extracted values not available
- Error styling for forms (text-input-error border color) is based on the coral accent (#ff6d6d) appearing in the extracted palette, but exact error text color and helper text styling are unknown
- Dark mode is not present on the live site and has not been designed
- Sub-brand or collection-specific color variations (e.g., seasonal palettes) could not be extracted
- The extracted hex list contains many generic grays and checkout-widget colors (e.g., #e74c3c, #199800, #e51c23 are likely Shopify Pay/Afterpay/Klarna colors and have been excluded from the brand palette)
- Font weights beyond 400, 500, and 600 are not confirmed — DM Sans may be used at weight 700 for some headings, but no evidence was found
- Spacing tokens (xxs through section) are estimated from common e-commerce patterns; exact extracted values were not available
- The meta theme-color tag is absent from the live site, so the browser chrome color is unknown
- Product card hover states (image zoom, shadow lift) are not extracted and follow common e-commerce conventions
- The accent-orange (#ec8816) and accent-purple (#7069bc) appear in the extracted palette but their specific usage (possibly social icons or decorative elements) is unconfirmed
