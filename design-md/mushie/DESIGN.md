---
version: alpha
name: "Mushie"
source_url: "https://mushie.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Swedish-born baby brand that paints its world in #fcfaf7 — a warm, almost chalky off-white that feels like unbleached cotton rather than sterile hospital white. Against this canvas, #d2815f (a dried-clay terracotta) and #c35121 (a deeper burnt sienna) appear as accent notes, not primary statements, giving the brand a grounded, earthy pulse without shouting "baby pink" or "pastel blue." The palette leans heavily on #4e4e50 and #575757 — soft charcoals that read as gentle ink rather than harsh black — while #f3ece7 and #f8f0e7 layer in as surface tones that mimic the warmth of sanded wood or unglazed ceramic. Product photography carries the weight: toys, bibs, and pacifiers sit in generous whitespace with soft shadows, the brand trusting object silhouette over decorative clutter. Rounded corners hover at {rounded.sm} to {rounded.md} — never pill-shaped, never sharp — suggesting softness without the saccharine. Navigation stays minimal: a single logo mark, a search icon, a cart badge, and a hamburger menu on mobile, all in #0f0f0f against the warm canvas. The checkout flow, likely powered by Shopify, introduces #007aff (a standard platform blue) that breaks the earthy contract — a known gap the brand tolerates for conversion. Type is absent from extracted CSS beyond swiper-icons, suggesting a system font stack or a single weight of a geometric sans-serif, letting materiality and color do the emotional work.

colors:
  primary: "#d2815f"
  primary-active: "#c35121"
  primary-disabled: "#eecba5"
  ink: "#0f0f0f"
  body: "#4e4e50"
  muted: "#575757"
  muted-soft: "#747477"
  hairline: "#dedede"
  hairline-soft: "#e7e7e7"
  canvas: "#fcfaf7"
  surface-soft: "#f3ece7"
  surface-card: "#f8f0e7"
  on-primary: "#fcfaf7"
  accent-terracotta: "#d2815f"
  accent-sienna: "#c35121"
  accent-sand: "#eecba5"
  accent-stone: "#748cab"
  accent-denim: "#3f6493"
  accent-rose: "#e4d8ce"
  badge-red: "#ff2a00"
  cart-count: "#0f0f0f"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.link}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "1px solid {colors.ink}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "1px solid {colors.badge-red}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-logo:
    height: 24px
    maxWidth: 120px
  nav-icon:
    height: 24px
    width: 24px
    color: "{colors.ink}"
  cart-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: 0 4px
  search-icon:
    height: 20px
    width: 20px
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(15, 15, 15, 0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-sand}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.sm}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted-soft}"
    padding: "{spacing.base} 0"
  breadcrumb-active:
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in terracotta (#d2815f) with uppercase 14px type on the warm canvas. On hover, it deepens to burnt sienna (#c35121); when disabled, it fades to a muted sand (#eecba5) with soft-gray text. The 8px corner radius keeps it friendly without tipping into pill-shaped playfulness.

**`button-secondary`** — An outlined variant on the warm canvas with a single hairline border (#dedede) that darkens to ink on hover. Used for "Add to Cart" on product cards and secondary checkout actions. The 1px border and 11px vertical padding (to account for the border) keep it visually balanced alongside the primary button.

**`button-tertiary`** — A text-only link styled as a button, used for "View All" links and cancel actions. No background, no border — just body-gray type at 14px with a subtle hover color shift to ink. The 8px horizontal padding provides a generous tap target without visual weight.

### Cards
**`product-card`** — A clean, borderless card on the warm canvas with a 12px corner radius. The product image fills the top with a 1:1 aspect ratio and rounded top corners; title and price stack below with 8px/16px padding. On hover, a soft shadow (4px blur, 8% opacity on #0f0f0f) lifts the card without breaking the flat aesthetic. No badge by default — badges appear only for "New" or "Sale" items.

**`product-card-image`** — The image container uses `object-fit: cover` to crop uniformly. The rounded top corners match the card's 12px radius; the bottom is square to meet the text block cleanly.

### Navigation
**`nav-bar`** — A 64px fixed bar on the warm canvas with a single hairline-soft bottom border (#e7e7e7). The logo sits left (max 120px wide, 24px tall), with a search icon and cart icon on the right. The cart badge is a small ink circle (#0f0f0f) with white type, positioned at the top-right of the cart icon. On mobile, a hamburger icon replaces the search icon.

**`nav-logo`** — The brand's wordmark or logomark, rendered at 24px height. On the warm canvas, it reads in ink (#0f0f0f) with no additional decoration.

### Forms
**`text-input`** — A 48px tall input on the warm canvas with a 1px hairline border (#dedede) and 12px corner radius. Placeholder text is muted-soft (#747477); on focus, the border switches to ink (#0f0f0f). Error state swaps the border to badge-red (#ff2a00). Used for email capture, search, and checkout fields.

**`quantity-selector`** — A compact 44px tall control with a hairline border and two 32px circular buttons (minus/plus) flanking the numeric value. Used on product pages and cart line items. The buttons have no background — just the body-gray icon and a subtle hover state.

### Footer
**`footer`** — A full-width ink (#0f0f0f) section with white type. Links render in muted-soft (#747477) and shift to white on hover. The footer uses 48px vertical padding and 24px horizontal padding, with accordion-style sections on mobile. Social icons (if present) are white with 24px height.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column (100% width); hero banner reduces to 300px min-height; footer accordions replace multi-column links; text-inputs go full-width; quantity-selector stacks below product image |
| Tablet | 744–1128px | Nav shows search icon + cart; product cards in 2-column grid; hero at 400px min-height; footer shows 2-column link layout; side padding reduces to 24px |
| Desktop | 1128–1440px | Full nav with search icon, cart icon, and optional country selector; product cards in 3- or 4-column grid; hero at 400px min-height; footer shows 3- or 4-column link layout; max-width container at 1128px centered |
| Wide | > 1440px | Same as desktop but container max-width may expand to 1440px; product cards may show 4- or 5-column grid; hero may add decorative imagery on either side |

### Touch Targets
- All buttons and interactive elements: minimum 44px height (WCAG AAA for touch)
- Icon buttons (search, cart, hamburger): 44x44px tap area, even if icon is smaller
- Color swatches: 32x32px with 44px tap area via padding
- Quantity selector buttons: 32x32px with 44px tap area
- Accordion headers: 44px minimum height with full-width tap target
- Footer links: 44px minimum height on mobile

### Collapsing Strategy
- Top nav: hamburger menu replaces all nav links on mobile; search icon may move into the hamburger drawer
- Product grid: 4-column → 2-column → 1-column as viewport shrinks
- Footer: multi-column link layout collapses to stacked accordion panels on mobile
- Hero banner: full-width image/text side-by-side on desktop stacks vertically on mobile
- Cart drawer: slides in from right on all breakpoints; full-screen on mobile
- Product filters: horizontal strip on desktop collapses to a "Filter" button + modal drawer on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted font-family beyond `swiper-icons` (likely a carousel library) — the typography block uses a system-ui stack as a safe fallback; the brand may use a custom typeface (e.g., a geometric sans) that wasn't captured
- Hover and focus states for most components are inferred from common patterns; actual extracted CSS may differ
- Error styling (form validation, 404 page, error boundaries) not extracted
- Dark mode: not observed; the brand likely uses a single light theme
- Sub-brand or collection-specific palettes (e.g., seasonal drops) not captured
- Checkout flow colors (#007aff) are Shopify defaults, not brand choices — noted but excluded from the palette
- The extracted color list includes many near-whites and grays; the true brand palette may have additional accent colors (e.g., a sage green or muted yellow) that weren't frequent enough in the extraction
- Animation/transition timing and easing not extracted
- Icon set and illustration style not documented
- Print stylesheet not available
- Accessibility contrast ratios not verified against the extracted palette
- The `badge-red` (#ff2a00) is unusually bright and may be a Shopify error/warning color rather than a brand choice
