---
version: alpha
name: "BioLite"
source_url: "https://www.bioliteenergy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A teal #008fa1 voltage runs through every primary action on BioLite's off-grid marketplace — that single distinctive hex, pulled from the brand's product-line accent and solar-charger LEDs, is the only saturated color in an otherwise muted system of warm grays (#c9c5be, #f0f0f0, #e3e3e3) and near-blacks (#050505, #1c1c1c). The palette reads like camping gear at dusk: the teal glows, the grays recede, and a single red #a70100 appears only for sale badges and error states, never for primary CTAs. Typography mixes Fraunces (a soft, slightly condensed serif with optical-size contrast) for display headlines with Arimo (a neutral, highly legible sans-serif) for body and UI — a pairing that signals both outdoor editorial warmth and technical reliability. EB Garamond appears in limited editorial contexts, likely pull-quotes or heritage copy. Buttons are generously pill-shaped (`{rounded.full}`) at 48px height, with the teal fill on primary and a transparent outline on secondary that uses the same teal stroke. Product cards use a soft `{rounded.md}` (12px) and sit on a `{colors.surface-soft}` (#fafafa) canvas, with the product image bleeding edge-to-edge and the title set in Fraunces at 16px. The nav bar is a fixed 80px band of `{colors.canvas}` (#ffffff) with a centered logo lockup and a right-aligned cart icon that inherits the teal badge dot. The overall effect is a design system that trusts one color and three typefaces to do the work of ten — it feels intentional, not sparse.

colors:
  primary: "#008fa1"
  primary-active: "#068491"
  primary-disabled: "#c9c5be"
  ink: "#050505"
  body: "#414141"
  muted: "#808080"
  muted-soft: "#c9c5be"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-red: "#a70100"
  sale-red-active: "#d02f2e"
  accent-green: "#478947"
  accent-gold: "#a77a06"
  accent-sage: "#798c5e"
  accent-teal-dark: "#00343b"
  accent-teal-mid: "#008f9d"
  accent-teal-light: "#068491"

typography:
  display-xl:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Arimo', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  pull-quote:
    fontFamily: "'EB Garamond', 'Georgia', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    fontStyle: italic

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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.sale-red}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with `{colors.primary}` (#008fa1) and set in Arimo 15px weight 600 with 0.5px letter-spacing. The pill shape (`{rounded.full}`) and generous 14px 28px padding make it feel substantial without being aggressive. On hover, it shifts to `{colors.primary-active}` (#068491); disabled state uses `{colors.primary-disabled}` (#c9c5be) with `{colors.muted}` text. The secondary variant uses a transparent fill with a 2px `{colors.primary}` stroke and teal text, inverting to filled teal on hover. A tertiary text-only button exists for less prominent actions like "Cancel" or "Learn more."

**`button-pill-teal`** — A smaller, compact pill used for inline actions like "Add to cart" on product cards or "Shop now" in category strips. Same `{rounded.full}` and teal fill, but uses `{typography.button-sm}` (13px) and tighter 10px 20px padding. Hover state matches `button-primary-active`.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` (12px) and no padding at the card level — the product image bleeds edge-to-edge to the top and sides, with title and price stacked below in a padded inner container. The title uses `{typography.title-md}` (Fraunces 16px weight 500) and the price uses `{typography.body-md}` (Arimo 16px weight 400) in `{colors.body}`. Badges overlay the top-left corner of the image area with `{rounded.xs}` and 2px 8px padding. Three badge types exist: sale (red `#a70100`), sold-out (muted-soft `#c9c5be`), and eco/accent (sage `#798c5e`).

### Navigation
**`top-nav`** — A fixed 80px white bar (`{colors.canvas}`) with the BioLite logo centered or left-aligned (depending on viewport) and a right-aligned cart icon. Nav links use `{typography.nav-link}` (Arimo 14px weight 500) with `{colors.body}` default and `{colors.primary}` active. The cart icon carries a small `{rounded.full}` badge dot in `{colors.primary}` with white text showing the item count. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

**`category-strip`** — A horizontal scrollable strip of category tabs (e.g., "Charging," "Cooking," "Lighting") below the hero. Tabs use `{typography.nav-link}` with `{colors.body}` default and `{colors.primary}` active, indicated by a 2px `{colors.primary}` bottom border on the active tab. The strip has no background color (inherits from section) and `{spacing.sm}` vertical padding.

### Forms
**`text-input`** — A standard input field with `{colors.canvas}` background, `{rounded.sm}` (8px), and a 1px `{colors.hairline}` (#dedede) border. On focus, the border thickens to 2px `{colors.primary}`. Error state uses 2px `{colors.sale-red}` (#a70100). Height is 48px with 12px 16px padding. The search bar variant uses a pill shape (`{rounded.full}`) with `{colors.surface-soft}` background and a 1px `{colors.hairline}` border, switching to 2px `{colors.primary}` on focus.

### Footer
**`footer`** — A dark band (`{colors.ink}` #050505) with white text (`{colors.canvas}`) and muted link colors (`{colors.muted-soft}` #c9c5be) that brighten to `{colors.canvas}` on hover. Content is organized in a multi-column grid with headings in Fraunces and links in Arimo 14px. Social icons appear as white outlines on the dark background. The footer uses `{spacing.xxl}` (48px) vertical padding and `{spacing.lg}` (24px) horizontal padding.

### Badges
**`badge-new`** — A small `{rounded.xs}` badge with `{colors.accent-green}` (#478947) background and white text, used for newly launched products. **`badge-sale`** uses `{colors.sale-red}` (#a70100) for discounted items. **`badge-eco`** uses `{colors.accent-sage}` (#798c5e) for sustainable or eco-friendly products. All badges use `{typography.badge}` (Arimo 11px weight 700 uppercase) with 2px 8px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-lg}`; category strip becomes horizontal scroll; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded with reduced link spacing; hero uses `{typography.display-xl}` at 28px; footer uses 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero uses `{typography.display-xl}` at 36px; footer uses 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 4 columns; hero uses 36px display with wider padding |

### Touch Targets
- All buttons and interactive elements maintain a minimum 48px height for touch accessibility.
- Icon buttons are 40px with `{rounded.full}` and adequate hit area.
- Category strip tabs have 44px minimum height for tap targets.
- Search bar pill is 48px tall with 12px 20px padding.

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; the slide-out drawer contains all nav links plus cart icon.
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks.
- Hero section reduces font size and padding on mobile; the CTA button remains full-width on small screens.
- Category strip becomes a horizontal scrollable row on mobile, with no wrapping.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site; the active states listed are inferred from common patterns and the brand's color logic.
- Error, success, and warning form states beyond the error border are unknown; no error message typography or iconography was observed.
- Dark mode is not supported on the current live site; no dark palette tokens exist.
- The exact font sizes for `display-xl` and `display-lg` are estimated based on typical hero text ranges for the brand's category; the extracted CSS did not include explicit font-size declarations for these levels.
- The `pull-quote` typography token is inferred from the presence of EB Garamond in the font stack; its exact usage context (size, weight, italic) is speculative.
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) are not captured.
- Animation and transition timing values (durations, easing curves) were not extracted.
- The `quantity-selector` component is assumed from e-commerce patterns; its exact styling (increment/decrement buttons, layout) is not confirmed from the live site.
- The `accordion` component is assumed from common product-page patterns; its exact border, padding, and iconography are speculative.
