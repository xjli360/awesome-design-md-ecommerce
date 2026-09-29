---
version: alpha
name: "dbrand"
source_url: "https://www.dbrand.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A matte-black canvas (#000000) and a single electric-yellow accent (#ffbb00) form the entire visual vocabulary of dbrand — a brand that sells precision-cut device skins with the confidence of a hardware company. The black is not a background; it is the product. Every skin, every phone silhouette, every unboxing shot sits on or against absolute black, making the yellow read as a signal flare: the “Add to Cart” button, the “Shop Now” link, the accent on the navigation bar. There is no gradient, no soft shadow, no rounded card — the brand uses hard corners (`{rounded.none}`) on product tiles and sharp 4px radii (`{rounded.xs}`) on buttons, mirroring the precision-cut vinyl it sells. Typography runs a bold sans-serif at heavy weights (700–900) with tight tracking, matching the industrial, no-nonsense tone of the copy: “Don’t be a hero. Be a dbrand.” The site avoids photography of people; instead, it shows macro shots of textured skins (carbon fiber, titanium, dragon skin) against the black canvas, with the yellow used sparingly for CTAs and the cart badge. This is a brand that sells a thin layer of adhesive vinyl, but it presents itself with the visual weight of a premium electronics manufacturer — all because of the black-and-yellow binary.

colors:
  primary: "#ffbb00"
  primary-active: "#e6a800"
  primary-disabled: "#ffe680"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#333333"
  hairline-soft: "#444444"
  canvas: "#000000"
  surface-soft: "#111111"
  surface-card: "#1a1a1a"
  on-primary: "#000000"
  on-dark: "#ffffff"
  yellow-light: "#fff4cc"
  yellow-dark: "#cc9900"
  badge-red: "#e63946"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
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
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.on-dark}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
  search-bar-focus:
    border: "1px solid {colors.primary}"
  skin-swatch:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.hairline}"
    height: 48px
    width: 48px
  skin-swatch-selected:
    border: "2px solid {colors.primary}"
  skin-swatch-hover:
    border: "2px solid {colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The single call-to-action across the site, rendered in electric yellow (#ffbb00) with black text. Used for “Add to Cart,” “Shop Now,” and primary checkout flows. On hover, darkens to `{colors.primary-active}` (#e6a800). Disabled state uses `{colors.primary-disabled}` (#ffe680) with black text, signaling the action is unavailable without ambiguity. Uppercase 14px Inter at weight 700 with 0.5px tracking gives the button an industrial, no-nonsense feel. Sharp 4px corners (`{rounded.xs}`) match the precision-cut product aesthetic.

**`button-secondary`** — An outlined variant with a transparent background, yellow border, and yellow text. Used for secondary actions like “View Details” or “Compare.” On hover, fills with yellow and switches text to black. The 2px solid border maintains visual weight parity with the primary button.

### Cards
**`product-card`** — A sharp-cornered (`{rounded.none}`) card on a dark surface (#1a1a1a) with a 1px hairline border (#333333). The product image sits on absolute black (`{colors.canvas}`), making the skin texture pop. On hover, the border switches to yellow (`{colors.primary}`), creating a subtle selection state without a shadow or lift effect. The title uses `{typography.title-md}` (18px, weight 700) and the price uses `{typography.body-md}` in yellow — the only place body copy appears in the accent color.

### Navigation
**`nav-bar`** — A 64px fixed bar on absolute black with a 1px bottom hairline. Navigation links are uppercase 13px Inter at weight 600 with 0.5px tracking. Active links render in yellow; inactive links in muted gray (#666666). The cart icon carries a `{rounded.full}` yellow badge with the item count. The bar is intentionally thin — no mega-menu, no dropdown previews — reflecting the brand’s direct, no-frills approach.

### Forms
**`text-input`** — Dark-surface inputs (#111111) with a 1px hairline border (#333333) and 4px corners. On focus, the border switches to yellow. Placeholder text uses `{colors.muted-soft}` (#999999). The input height (48px) matches the primary button for visual alignment in forms.

### Footer
**`footer`** — A dark section (#111111) with muted gray links (#666666) that turn yellow on hover. The footer uses `{typography.body-sm}` (14px) for all content, with section headers in `{typography.caption}` (12px, weight 500, 0.25px tracking). No social media icons — the brand directs all attention to the product grid above.

### Badges
**`badge-new`** — A yellow badge with black text, 4px corners, and uppercase 10px Inter at weight 700. Used for new skin releases. **`badge-sale`** uses a red (#e63946) background with white text for discount indicators. Both badges are compact (2px 8px padding) to sit unobtrusively on product cards.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, full-width hero, stacked CTAs |
| Tablet | 744–1128px | Two-column product grid, top nav collapses to icon-only, hero text scales down |
| Desktop | 1128–1440px | Three-column product grid, full nav visible, hero uses max width |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero text at 48px |

### Touch Targets
- All buttons and links: minimum 44px height (WCAG 2.1 compliant)
- Product card tap targets: full card is tappable, minimum 120px height
- Skin swatches: 48px × 48px minimum tap area
- Nav links: 44px minimum tap height with 8px padding
- Cart badge: 20px minimum, but wrapped in a 44px touch area

### Collapsing Strategy
- Top nav: full text links collapse to icon-only at tablet breakpoint; hamburger menu at mobile
- Product grid: 4-column → 3-column → 2-column → 1-column
- Hero section: side-by-side text and image stack vertically below 744px
- Footer: 4-column link layout collapses to 2-column at tablet, single column at mobile
- Skin selector: horizontal swatch row wraps to 4-per-row grid at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; Inter is an informed assumption based on the brand’s visual tone and common usage in DTC hardware-adjacent brands. Actual font may differ.
- Only one accent color (#ffbb00) was extracted; the full palette (especially hover states, disabled states, and secondary accents) is inferred from common dark-theme patterns.
- No hover, focus, or active state colors were extractable; these are estimated based on standard dark-theme interactions.
- Error state styling (form validation, out-of-stock indicators) could not be determined.
- Dark mode is the default and only mode; no light mode variant was observed.
- Sub-brand or collection-specific palettes (e.g., limited edition skins) were not extractable.
- Animation and transition durations/easings were not extractable.
- Icon set and illustration style were not extractable.
- Checkout flow styling (Shopify Pay, Klarna, Afterpay buttons) may introduce colors not in this palette.
