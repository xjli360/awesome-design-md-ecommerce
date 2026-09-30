---
version: alpha
name: "Free League Publishing"
source_url: "https://freeleaguepublishing.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue (#003388) the color of a midnight sky over a Nordic forest anchors Free League Publishing’s digital storefront, a hue that appears nowhere in the extracted palette as a generic web default and instead reads as the brand’s deliberate, atmospheric primary. That blue saturates the primary button, the top navigation bar, and the hero section’s background, while a secondary accent of muted crimson (#cf6363) appears sparingly — perhaps on sale badges or limited-edition callouts — offering a single point of warmth against the cool, scholarly greys (#393939, #313131, #444444) that form the body and ink layers. The typography stack is a hybrid of the familiar and the bespoke: Eksell Display Small, a quirky, slightly condensed display face with a hand-drawn quality, appears for headlines and game titles, while the body and UI rely on the workhorse Open Sans and the more geometric futura-pt. Beaufort-pro, a serifed typeface often associated with fantasy and historical settings, hints at the brand’s tabletop RPG catalog — games like *The One Ring* and *Forbidden Lands* — and likely appears in product descriptions or chapter headers. The canvas is a clean, near-white (#f9f9f9) with soft surfaces (#eeeeee, #eaeaea) and hairline-thin borders (#dcdcdc) that keep the layout airy despite the dense information load of game listings, rulebook previews, and expansion announcements. Buttons are softly rounded (`{rounded.sm}`) and the search bar adopts a pill shape (`{rounded.full}`), a gesture toward approachability that tempers the brand’s otherwise serious, lore-heavy identity. The overall impression is of a publisher that treats its digital presence as a library or a guild hall — orderly, trustworthy, and lit by the glow of a single, unwavering blue.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#b3c6e6"
  ink: "#313131"
  body: "#393939"
  muted: "#444444"
  muted-soft: "#b8b8b8"
  hairline: "#dcdcdc"
  hairline-soft: "#e3e3e3"
  canvas: "#f9f9f9"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#cf6363"
  accent-green: "#00d084"
  accent-blue: "#0693e3"
  accent-purple: "#7a00df"
  accent-cyan: "#34e2e4"
  accent-pink: "#faaca8"
  accent-sage: "#67a671"

typography:
  display-xl:
    fontFamily: "'Eksell Display Small', 'beaufort-pro', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Eksell Display Small', 'beaufort-pro', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'futura-pt', 'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'futura-pt', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Open Sans', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'futura-pt-bold', 'futura-pt', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'futura-pt-bold', 'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.4px
  link:
    fontFamily: "'Open Sans', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'futura-pt', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'futura-pt-bold', 'futura-pt', sans-serif"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-accent-warm:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar-link-active:
    textColor: "{colors.on-primary}"
    borderBottom: "2px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 51, 136, 0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand’s deep blue (#003388) and white text. Used for “Add to Cart,” “Pre-order Now,” and “Explore” actions on product cards and hero sections. On hover, it deepens to `{colors.primary-active}` (#002266). The disabled state uses a lighter, desaturated blue (`{colors.primary-disabled}`) to signal inactivity.

**`button-secondary`** — An outlined variant with a white fill and blue border, used for secondary actions like “View Details” or “Read More.” The border matches `{colors.primary}`, and on hover the background shifts to `{colors.surface-soft}` (#eeeeee) while the border deepens to `{colors.primary-active}`.

**`button-accent-warm`** — A smaller, warm-toned button using `{colors.accent-warm}` (#cf6363) as its fill. Reserved for limited-edition callouts, sale badges, or “Last Chance” prompts. Uses `{typography.button-sm}` to fit tighter spaces.

### Cards
**`product-card`** — The primary container for game listings. A white card (`{colors.surface-card}`) with a soft border (`{colors.hairline-soft}`) and `{rounded.md}` corners. On hover, the border shifts to `{colors.primary}` and a subtle blue box shadow appears. The title uses `{typography.title-sm}` in `{colors.ink}`, while the price is set in `{typography.body-md}` in `{colors.primary}`. Padding is `{spacing.base}` (16px) on all sides.

**`badge-new`**, **`badge-sale`**, **`badge-preorder`** — Small, uppercase labels that sit in the top-right corner of product cards or thumbnails. Each uses a distinct accent color: green for new releases, warm red for sales, and purple for pre-orders. Typography is `{typography.badge}` with `{rounded.xs}` corners and tight padding.

### Navigation
**`nav-bar`** — A full-width top navigation bar filled with `{colors.primary}` (#003388). Links are set in white using `{typography.nav-link}` with `{spacing.sm}` (8px) vertical and `{spacing.md}` (12px) horizontal padding. The active link is underlined with a 2px white border. The bar has a fixed height of 64px and horizontal padding of `{spacing.xl}` (32px).

**`search-bar-pill`** — A pill-shaped search input (`{rounded.full}`) with a white background and `{colors.muted}` placeholder text. On focus, the border becomes a 2px blue stroke (`{colors.primary}`). Height is 48px with `{spacing.sm}` (8px) vertical and `{spacing.lg}` (24px) horizontal padding.

### Forms
**`text-input`** — Standard text input for forms (newsletter signup, account fields). White background, `{colors.hairline}` border, `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}`. Height is 44px with 10px vertical and 16px horizontal padding.

### Hero
**`hero-section`** — A full-width hero banner with a `{colors.primary}` background and white text. Used for featured game launches or seasonal promotions. The title uses `{typography.display-xl}` in Eksell Display Small, while the subtitle is `{typography.body-md}` at 85% opacity. Padding is `{spacing.xxl}` (48px) vertical and `{spacing.xl}` (32px) horizontal.

### Footer
**`footer`** — A dark footer (`{colors.ink}`) with muted gray links (`{colors.muted-soft}`). Links use `{typography.link}` and turn white on hover. The divider between sections is a 1px `{colors.hairline}` line with `{spacing.lg}` (24px) margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards stack in single column; hero padding reduces to `{spacing.lg}` (24px); search bar becomes full-width; badges shrink to `{typography.badge}` at 10px. |
| Tablet | 744–1128px | Nav-bar links remain visible but reduce font size to 14px; product cards display in 2-column grid; hero title reduces to `{typography.display-md}` (28px). |
| Desktop | 1128–1440px | Full nav-bar with all links; product cards in 3-column grid; hero uses `{typography.display-xl}` (36px). |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; hero padding increases to `{spacing.section}` (64px). |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px.
- Search bar pill is 48px tall for easy tapping.
- Nav-bar links have 8px vertical padding, ensuring a comfortable 32px+ tap area.

### Collapsing Strategy
- On mobile (< 744px), the top nav-bar collapses into a hamburger icon. The slide-out menu uses `{colors.primary}` background with white links.
- Product card grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Hero section text stacks vertically on mobile; on wider screens, it may sit alongside a featured image.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is unusually large (30+ hex values), many of which are likely checkout-widget colors (Shopify Pay, Klarna, Afterpay) or social-icon brand colors. The true brand palette is inferred from the most distinctive and repeated hues (#003388, #cf6363, #393939, #eeeeee, #dcdcdc). A full audit of the live site’s CSS variables or design tokens would confirm the exact palette.
- Font-family declarations include multiple fallback stacks; the exact pairing of Eksell Display Small for headlines and futura-pt/Open Sans for body is an educated guess based on frequency and brand context. The actual usage of beaufort-pro and serif is unclear — it may be reserved for specific game sub-brands.
- Hover states for buttons and cards are inferred from common patterns; the actual live site may use different colors or transitions.
- Error states for forms (validation, error messages) are not present in the extracted data.
- Dark mode is not supported or detected; the palette assumes a light theme.
- Sub-brand palettes (e.g., for *The One Ring*, *Alien*, *Blade Runner*) are not captured and may use distinct accent colors.
- The exact border radius for product cards (`{rounded.md}` = 12px) is a reasonable default; the live site may use a different value.
- Spacing tokens (xxs, xs, sm, etc.) are set to standard values; the live site may use a custom scale (e.g., 4px, 8px, 16px, 24px, 32px, 48px, 64px).
