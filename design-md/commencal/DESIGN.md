---
version: alpha
name: "Commencal"
source_url: "https://www.commencal.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A raw, unapologetic mountain-bike brand that uses #d7ca9e — a pale, sun-bleached khaki — as its primary, a color that evokes dusty trails and aluminum frames rather than the glossy black or electric neons of the cycling mainstream. The palette is built on contrasts: #008827 as a deep forest-green accent for "green" product lines, #cc0000 as a racing-red alert for sale badges and limited drops, and a full range of muted earth tones (#706952, #383d41, #444444) that keep the interface grounded. The canvas is #f9f9f9, a near-white that reads as workshop concrete rather than sterile paper, while #eae7e4 and #ede6d2 provide warm surface tones. Typography defaults to system fonts — Helvetica, Arial, Roboto — a deliberate non-choice that prioritizes performance and global rendering over brand-typedesign. The site's architecture is brutalist in its honesty: full-bleed product imagery, hard-cornered cards with {rounded.none} or at most {rounded.sm}, and a navigation that stacks categories (BIKES, SNOW, LIFESTYLE) in a heavy, uppercase, all-caps system. There is no decorative filigree, no gradient hero — just a product grid, a search bar with {rounded.full} pill shape, and the occasional badge in #008827 or #cc0000 to signal urgency. The brand trusts its photography — bikes in mud, riders in motion — to carry emotion, leaving the UI as a functional chassis.

colors:
  primary: "#d7ca9e"
  primary-active: "#c8b67a"
  primary-disabled: "#ede6d2"
  ink: "#222222"
  body: "#444444"
  muted: "#706952"
  muted-soft: "#818182"
  hairline: "#c8cbcf"
  hairline-soft: "#eae7e4"
  canvas: "#f9f9f9"
  surface-soft: "#ede6d2"
  surface-card: "#ffffff"
  on-primary: "#222222"
  green-accent: "#008827"
  green-accent-active: "#005518"
  red-accent: "#cc0000"
  red-accent-active: "#990000"
  dark-surface: "#383d41"
  dark-ink: "#1b1e21"
  badge-new: "#008827"
  badge-sale: "#cc0000"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "Helvetica, Arial, 'Noto Sans', system-ui, sans-serif"
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-green:
    backgroundColor: "{colors.green-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-green-active:
    backgroundColor: "{colors.green-accent-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-red:
    backgroundColor: "{colors.red-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-red-active:
    backgroundColor: "{colors.red-accent-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-uppercase}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-uppercase}"
  hero-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
    height: 44px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, rendered in the brand's distinctive khaki (#d7ca9e) with hard corners and uppercase, bold type. On hover, it shifts to the darker #c8b67a; disabled state fades to #ede6d2 with muted text. Used for "Add to Cart", "Shop Now", and primary checkout actions.

**`button-secondary`** — An outlined variant with a 2px solid ink border on a white canvas. Hover inverts to solid ink fill with white text. Used for "Learn More", "View Details", and secondary navigation actions where the primary khaki would compete with product imagery.

**`button-green`** — A high-contrast green (#008827) button reserved for "Green" product lines, eco-friendly messaging, and sustainability badges. Hover darkens to #005518. Never used for primary commerce actions — only for brand-specific category signaling.

**`button-red`** — Racing red (#cc0000) for urgency: "Sale", "Limited Edition", "Last Chance". Hover deepens to #990000. Used sparingly to preserve its alert power.

### Cards
**`product-card`** — A minimal, hard-cornered card with no border or shadow — just a full-bleed product image, title in `title-sm`, and price in `body-md`. The card relies entirely on the photography to sell; no decorative frame, no rating stars, no badge by default. Badges (`badge-new`, `badge-sale`, `badge-out-of-stock`) are overlaid on the image when applicable.

### Navigation
**`nav-bar`** — A white 72px bar with a single hairline-soft bottom border. Navigation links use `nav-link` typography: 14px, bold, uppercase with 1px letter spacing. The active category (e.g., "BIKES") gets a 2px primary underline. The bar is fixed on desktop, collapsing to a hamburger on mobile.

**`category-strip`** — A secondary horizontal scroll strip below the nav bar for subcategories (e.g., "Enduro", "Trail", "Downhill"). Uses `caption-uppercase` (11px, bold, spaced) with active tabs underlined in primary.

### Forms
**`text-input`** — A hard-cornered input with a 1px hairline border. On focus, the border thickens to 2px and turns primary khaki. Used for search, newsletter signup, and filter fields.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input, 40px tall, with a 1px hairline border. On focus, the border becomes a 2px primary line. The pill shape is the only rounded element in the system — a deliberate contrast to the otherwise hard-cornered UI.

**`filter-dropdown`** — A hard-cornered dropdown with a 1px hairline border. Active state uses a primary border. Used for sorting (Price, Newest, Name) and filtering by category or size.

### Footer
**`footer-link`** — Standard link in muted (#706952) that shifts to ink on hover. No underline decoration — the color change is the only affordance.

### Hero
**`hero-section`** — A full-width, dark-surface (#383d41) section with white text in `display-xl`. An optional overlay scrim at 50% opacity sits behind the text for readability. Used for category landing pages and seasonal campaigns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; product grid goes single-column; hero section reduces padding to 32px; search bar becomes full-width; filter strip becomes a single dropdown; footer stacks vertically. |
| Tablet | 744–1128px | Nav bar remains full but nav links reduce to 12px; product grid shows 2 columns; hero padding at 48px; filter strip remains horizontal but scrollable. |
| Desktop | 1128–1440px | Full nav bar with all categories; product grid at 3 columns; hero at full section padding (64px); filter strip fully visible. |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero content centered with max-width 1200px. |

### Touch Targets
- All buttons and interactive elements: minimum 44px height, 44px width for icon-only targets.
- Search bar: 40px height on desktop, 48px on mobile for easier tapping.
- Nav bar hamburger icon: 48px x 48px tap target.
- Filter dropdowns: 44px minimum height.
- Product card links: entire card is tappable (no separate link target).

### Collapsing Strategy
- Nav bar: categories collapse into a hamburger menu on mobile; sub-category strip collapses into a single "Filter" dropdown.
- Product grid: collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer: multi-column layout collapses to a single vertical stack on mobile.
- Hero section: full-width background remains, but text padding reduces and font size drops from 32px to 24px on mobile.
- Search bar: expands to full width on mobile, losing its pill shape's side margins.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary, secondary, green, and red button hovers were extractable. Hover states for nav links, footer links, and product cards are inferred from common patterns but not confirmed from the live site.
- **Error styling**: No error states for text inputs, validation messages, or form submission feedback were found in the extracted data.
- **Dark mode**: No dark-mode palette was detected. The site appears to be light-mode only.
- **Sub-brand palettes**: Commencal may have distinct palettes for its "Snow" and "Lifestyle" categories, but these were not separable from the extracted data.
- **Typography weights**: The exact font weights for each size are inferred from common system-font usage (Helvetica/Arial). The site may use variable fonts or specific weights not captured in the extraction.
- **Spacing values**: Padding and margin values for components are estimated from common e-commerce patterns and the brand's general aesthetic, not extracted from the live site's computed styles.
- **Animation and transitions**: No transition durations, easing functions, or animation properties were extractable.
- **Accessibility**: Focus ring styles, skip-to-content links, and screen-reader-only text patterns are not documented.
- **Icon system**: The site may use custom icons for categories or social links, but these were not captured in the extraction.
