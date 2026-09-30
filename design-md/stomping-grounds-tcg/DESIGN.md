---
version: alpha
name: "Stomping Grounds TCG"
source_url: "https://www.stompinggroundstcg.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-energy trading card marketplace that runs on a neon-laced palette anchored by #006fcf — a confident, almost electric blue that carries every primary CTA, cart badge, and search bar. The brand doesn't whisper; it shouts through a secondary voltage of #ffb74e (a warm amber) and #dbee10 (a lime-green jolt), creating a visual language that feels more like a gaming arcade than a card shop. Type runs Roboto at clean, readable weights — display sits at 22–28px in weight 500, letting the product photography and card art do the heavy lifting. The top nav uses a dark ink (#231f20) canvas with white text, a deliberate inversion of the standard white-header approach, signaling that this is a destination for collectors who know what they want. Product cards use {rounded.md} corners and generous {spacing.base} padding, while badges for condition, rarity, and sale status pop in #fb7000 and #f48120 — oranges that read as urgency and value. The checkout flow borrows Shopify's standard widget colors (#4285f4, #5f6368), but the brand's own identity is unmistakable in the lime-green "SOLD" badges and the amber "HOT" tags that pulse across the grid. There is no softness here — every corner is either sharp or gently rounded, every color choice optimized for contrast and speed. The search bar sits front and center, a full-width pill in #006fcf with white text, inviting immediate discovery. Footer links stack in #616161 on a #212121 canvas, a muted but legible hierarchy that keeps focus on the product. Stomping Grounds TCG is a store that knows its audience: competitive players and collectors who scan fast, buy faster, and want the dopamine hit of a lime-green discount badge before they click.

colors:
  primary: "#006fcf"
  primary-active: "#005bb5"
  primary-disabled: "#b3d4f0"
  ink: "#231f20"
  body: "#212121"
  muted: "#616161"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ffb74e"
  accent-lime: "#dbee10"
  accent-orange: "#fb7000"
  accent-orange-soft: "#f48120"
  accent-gold: "#ff9900"
  badge-sold: "#e2ff3f"
  badge-hot: "#f89f20"
  badge-new: "#3086c8"
  star-rating: "#ffcd80"
  footer-bg: "#212121"
  footer-text: "#616161"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Segoe UI', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    padding: 12px 24px
    height: 44px
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  badge-sold:
    backgroundColor: "{colors.badge-sold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-hot:
    backgroundColor: "{colors.badge-hot}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-rarity:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  price-sale:
    typography: "{typography.title-md}"
    textColor: "{colors.accent-orange}"
  rating-stars:
    color: "{colors.star-rating}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site, rendered in #006fcf with white text and a subtle 6px corner radius. On hover, it deepens to #005bb5 (`{colors.primary-active}`) for a clear state change. The disabled state uses a pale blue (#b3d4f0) that still reads as "belongs to the brand" rather than generic gray. Padding is generous at 12px 24px, giving the button a solid, clickable presence at 44px height.

**`button-secondary`** — A white button with #231f20 text, used for "View All" links, secondary actions in modals, and cancel flows. The border is implied by the white canvas contrast; no outline stroke is needed. Same 44px height as primary for alignment in button groups.

**`button-accent-amber`** — The amber variant (#ffb74e) used for "Add to Cart" on product detail pages and promotional banners. The warm tone against dark ink text (#231f20) creates high contrast without the coldness of blue. Same dimensions as primary.

**`button-accent-lime`** — The lime-green variant (#dbee10) reserved for flash sales, limited-time offers, and checkout urgency prompts. The high-luminance green against dark text is deliberately jarring — it's meant to stop the scroll.

### Cards
**`product-card`** — The primary inventory display unit, a white card with 10px rounded corners and 16px padding. Each card contains a product image (with `{rounded.sm}` corners), a title in `{typography.body-sm}`, a price in `{typography.title-md}`, and up to three badges stacked in the top-left corner. Cards sit on a white canvas with no shadow — the separation comes from the grid gap and the hairline dividers in list views.

**`product-card-image`** — The image container within a product card, cropped to a consistent aspect ratio (typically 1:1 for cards, 3:4 for list items). Images load with a soft 6px corner radius that matches the button treatment.

### Badges
**`badge-sold`** — A lime-green (#e2ff3f) badge with dark text, used to mark items that have been purchased. The high-visibility color ensures "SOLD" is the first thing a scanning collector sees, preventing wasted clicks.

**`badge-hot`** — An amber-orange (#f89f20) badge with white text, used for trending or high-demand items. The warm tone signals heat and urgency.

**`badge-new`** — A medium blue (#3086c8) badge with white text, used for recently listed items. The cooler tone differentiates "new" from "hot" and "sold" without relying on position alone.

**`badge-rarity`** — An orange (#fb7000) badge with white text, used for rare or limited-edition cards. The saturated orange is the most aggressive of the badge colors, reserved for the highest-value signals.

### Navigation
**`top-nav`** — A dark (#231f20) header bar at 64px height, containing the brand logo on the left, a full-width search bar in the center, and cart/account icons on the right. Navigation links use `{typography.nav-link}` in white, with a subtle underline on active state. The dark canvas creates a strong visual anchor and makes the blue search bar pop.

**`search-bar`** — A full-width pill in #006fcf with white text and placeholder, positioned centrally in the top nav. The pill shape (`{rounded.full}`) and 48px height make it the most prominent interactive element on the page. On focus, the background lightens slightly to indicate active state.

### Forms
**`text-input`** — Standard form inputs for checkout, account creation, and filtering. White background with 6px rounded corners, 44px height, and 16px horizontal padding. The border is implied by the canvas contrast; focus state adds a 2px #006fcf ring.

### Footer
**`footer`** — A dark (#212121) footer section with muted gray (#616161) text for links and body copy. Links use `{typography.link}` and lighten to white on hover. The footer is divided into columns for "Shop," "Support," "About," and "Social" with generous 64px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav links, search bar collapses to icon-only, badges stack vertically, footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links (Shop, Cart, Account), search bar remains full-width but shorter height (40px), footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, search bar at 48px height, footer in four columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, search bar expands to 600px max-width, additional whitespace around product cards |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (exceeding Apple's 44pt HIG and Google's 48dp recommendation)
- Filter pills are 32px tall (below minimum for primary actions, acceptable for secondary toggle elements)
- Cart icon and account icon in top nav are 44x44px touch targets (icon size 24x24px within)
- Product card tap targets (image, title, price) are the full card width at minimum 120px height

### Collapsing Strategy
- Top nav links collapse into a hamburger menu below 744px; the hamburger icon is 44x44px
- Search bar collapses from full-width input to a magnifying-glass icon on mobile; tapping the icon expands the input inline
- Product grid collapses from 4 columns to 1 column on mobile, ensuring each card is readable at 320px width
- Footer columns collapse from 4 to 1 on mobile, stacking vertically with section headers as accordion toggles
- Badge text truncates to "SOLD" → "S" on very narrow screens (< 400px) to prevent overflow

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is dominated by blues, grays, and oranges — likely reflecting Shopify's default widget palette (#4285f4, #5f6368) and checkout-brand colors (Klarna, Afterpay) mixed with the brand's own. The true brand palette may include additional accent colors not captured in the top 30 hex values.
- Font-family declarations only returned "Roboto" — the brand may use a secondary display font for headings or logos that wasn't captured in the extraction.
- Hover states for buttons, links, and cards are inferred from common patterns (darken primary, lighten secondary) but were not directly extracted from the live site.
- Error styling (form validation, 404 pages, empty states) was not captured and should be designed to match the brand's high-contrast, color-coded approach.
- Dark mode is not implemented; the brand uses a light canvas with dark ink throughout.
- Sub-brand or category-specific color variations (e.g., Pokémon vs. MTG vs. Lorcana sections) may exist but were not extracted.
- The meta theme-color tag is absent, meaning the browser chrome on mobile defaults to white or system color — this is a known gap for PWA-style polish.
- Animation and transition durations (button press, card hover, search expand) were not extracted; recommended defaults: 150ms for micro-interactions, 300ms for layout transitions.
