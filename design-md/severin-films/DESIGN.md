---
version: alpha
name: "Severin Films"
source_url: "https://severin-films.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A crimson pulse — #b62030 — runs through every Severin Films page like a genre-movie blood spatter, the meta-theme color that stains the browser chrome and resurfaces in hover states, price tags, and the "Entertainment With Sharp Edges" tagline. The palette is deliberately gritty: #0f0f0f and #121212 create a near-black canvas for product photography, while #eeeeee and #fefefe provide high-contrast text on dark surfaces. A surprising teal-adjacent #aadddd appears as an accent — possibly a nod to vintage VHS tape labels or retro horror typography — and #a24e4e offers a desaturated secondary red that keeps the brand from feeling like a single-note slasher. Roboto runs the typography at moderate weights, giving the site a utilitarian, no-nonsense readability that lets the absurdist cover art and genre descriptions do the theatrical work. Buttons use hard corners ({rounded.sm}) rather than pills, and product cards stack with tight spacing ({spacing.md}) and thin hairline borders (#444444), evoking the crowded shelves of a video store. The overall effect is a digital exploitation-label storefront: dark, loud when it needs to be, and unapologetically niche.

colors:
  primary: "#b62030"
  primary-active: "#a24e4e"
  primary-disabled: "#808080"
  ink: "#0f0f0f"
  body: "#121212"
  muted: "#444444"
  muted-soft: "#888888"
  hairline: "#444444"
  hairline-soft: "#303030"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#1e1e1e"
  on-primary: "#ffffff"
  accent-teal: "#aadddd"
  accent-red-soft: "#a24e4e"
  accent-bright: "#ec5c52"
  text-light: "#eeeeee"
  text-muted-light: "#bdbdbd"
  badge-new: "#ec5c52"
  badge-sale: "#b62030"
  star-rating: "#fefefe"
  footer-bg: "#0f0f0f"
  footer-text: "#9e9e9e"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.text-muted-light}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-light}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  button-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.text-light}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.text-light}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1.4"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.text-light}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.text-light}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.ink}"
    opacity: 0.6
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.text-light}"
    textTransform: uppercase
    letterSpacing: 1px
  footer-link-active:
    textColor: "{colors.text-light}"
    typography: "{typography.footer-link}"
  footer-link-inactive:
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-light}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.lg}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.text-light}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature crimson #b62030 with white uppercase text. On hover, it shifts to the desaturated red #a24e4e, and in disabled state it fades to #808080 with muted text. The compact 44px height and 4px corner radius ({rounded.sm}) keep the button feeling utilitarian and direct — no pill shapes, no gradients.

**`button-secondary`** — A dark outlined variant for less prominent actions, using the surface-card background (#1e1e1e) with a thin #444444 border. On hover, the background deepens to #1a1a1a. This button sits alongside the primary in product listings and filter bars, providing a clear visual hierarchy without competing with the crimson.

**`button-accent-teal`** — The unexpected #aadddd accent button, used sparingly for special actions like "Add to Wishlist" or "View Trailer." The teal against the dark canvas creates a retro VHS-store vibe, a deliberate design quirk that signals this isn't a standard e-commerce site.

**`button-badge-sale` / `button-badge-new`** — Tiny uppercase badges pinned to product cards. Sale badges use the primary crimson, while "New" badges use the brighter #ec5c52. Both are compact at 4px padding and 11px font, designed to overlay product images without obscuring the artwork.

### Cards
**`product-card`** — The core product display unit: a dark card (#1e1e1e) with a 1px #444444 border and 4px radius. Each card contains a product image at a 1:1.4 aspect ratio (evoking Blu-ray/DVD proportions), the title in body-sm, and the price in title-sm colored crimson. On hover, the card background shifts to #1a1a1a and the border turns crimson — a subtle but clear selection state.

**`product-card-image`** — The image container within the card, cropped to the standard movie-poster aspect ratio. Images are loaded with a dark placeholder to maintain layout stability.

### Navigation
**`nav-bar`** — A fixed 60px dark bar (#0f0f0f) housing the brand logo and category links in uppercase Roboto. Active links glow crimson; inactive links stay white. The bar is deliberately compact — no search field, no mega-menu — keeping the focus on the product grid below.

**`category-strip`** — A secondary navigation row below the hero, using the surface-soft background (#1a1a1a). Category tabs are pill-less rectangles with 4px radius; the active tab fills with crimson, while inactive tabs remain transparent with white text.

### Forms
**`text-input`** — Dark input fields matching the site's overall mood: #1e1e1e background, #444444 border, white text. On focus, the border switches to crimson. Error states also use crimson borders, creating a consistent visual language for validation.

**`search-bar`** — A dedicated search input styled identically to text-input but with a search icon (not shown in tokens). The focus state mirrors the input focus, using the crimson border to indicate active search.

### Footer
**`footer`** — A deep black (#0f0f0f) footer with muted gray (#9e9e9e) links. Section headings are uppercase captions in white with 1px letter-spacing, creating a clear information hierarchy. Links lighten to white on hover. The footer uses generous padding ({spacing.xxl}) to create breathing room at the bottom of the dark page.

### Badges
**`badge-new` / `badge-sale`** — Small, uppercase, crimson or bright-red badges that overlay product images to indicate new releases or sale items. Their compact size (2px vertical padding, 11px font) ensures they don't compete with the product artwork.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), nav-bar collapses to hamburger menu, hero banner reduces to 250px min-height, category-strip becomes horizontal scrollable, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav-bar shows limited links (logo + 3-4 categories), hero banner at 350px min-height, category-strip shows 5-6 tabs |
| Desktop | 1128–1440px | Three-column product grid, full nav-bar with all categories, hero banner at 400px min-height, category-strip shows all tabs |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero banner at 450px min-height, additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav-bar links have 48px tap targets (padding extends touch area)
- Product cards have 100% width tap targets on mobile
- Search bar and text inputs maintain 44px height minimum
- Category tabs have 36px height with 8px padding for comfortable tapping

### Collapsing Strategy
- Nav-bar collapses to hamburger menu on mobile (< 744px), with slide-out drawer for full navigation
- Category-strip collapses to horizontal scroll on mobile, hiding overflow tabs
- Footer collapses from 4-column grid to single-column stacked layout on mobile
- Hero banner reduces min-height and may hide secondary text on mobile
- Product grid collapses from 3-4 columns to 1-2 columns on mobile
- Search bar may collapse to icon-only on mobile, expanding on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from extracted colors and common patterns; actual hover transitions (ease, duration) are unknown
- Error states for forms (validation messages, error icons) are not extracted
- Sub-brand or collection-specific color palettes (e.g., "Severin Kids," "Severin 4K") are not present in extracted data
- Dark mode is not applicable — the site already uses a dark canvas by default
- Font weights beyond 400, 500, 600, 700 are not confirmed; Roboto may appear at 300 (light) in some contexts
- Animation and transition timing values (e.g., hover fade duration, card entrance animations) are not extracted
- Specific icon set or iconography style is not captured; social-media icon colors (#3498db, #323232) appear in extracted list but may be from embedded widgets rather than brand design
- The #aadddd accent is inferred as teal from hex value; its exact usage context (background, text, border) is speculative
- Checkout flow styling (Shopify cart, payment buttons) is not captured — may use different colors than the main site
- Product image aspect ratio (1:1.4) is an assumption based on standard movie-poster dimensions; actual ratio may vary
- The #fff1e3 and #412d00 colors appear in extracted list but are likely from product photography or embedded content, not brand palette
