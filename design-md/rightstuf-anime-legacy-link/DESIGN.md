---
version: alpha
name: "RightStuf Anime (Legacy link)"
source_url: "https://www.rightstufanime.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage collector's bazaar where #ff5e00 — a searing safety-orange — ignites every add-to-cart button, sale badge, and urgency banner against a deep #181818 ink field. The palette is a deliberate collision of anime-merchandise energy: #fab818 marigold for limited-edition callouts, #029ddf cyan for pre-order highlights, and #ea001e crimson for clearance fire-sales, all riding on a #f3f3f3 canvas that keeps product photography from drowning in the noise. Typography runs two distinct voices — Nutmeg for display headlines that carry the weight of series titles and franchise names, and Lato for body copy and navigation, both set at modest weights (400–600) to let the art and price tags do the selling. The site's architecture is a dense grid of product thumbnails with hard 4px corners ({rounded.xs}) on cards and sharp 0px on the main nav, creating a no-nonsense browsing experience that prioritizes catalog density over editorial whitespace. Search is a full-width bar anchored in the top nav, while category strips use pill-shaped filters ({rounded.full}) in #23252b against the dark header. The checkout flow introduces a secondary palette of #2e844a (success green) and #0176d3 (action blue), likely inherited from Shopify or payment widgets, but the brand's own voice remains unmistakably orange — the color of limited stock, flash sales, and the thrill of the hunt for out-of-print steelbooks and import editions.

colors:
  primary: "#ff5e00"
  primary-active: "#e05200"
  primary-disabled: "#ffb080"
  ink: "#181818"
  body: "#1a1918"
  muted: "#5c5c5c"
  muted-soft: "#747474"
  hairline: "#d1d1d1"
  hairline-soft: "#eeeeee"
  canvas: "#f3f3f3"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fab818"
  accent-cyan: "#029ddf"
  accent-crimson: "#ea001e"
  accent-green: "#2e844a"
  accent-blue: "#0176d3"
  dark-surface: "#23252b"
  dark-header: "#141519"
  badge-orange: "#ff640a"
  badge-red: "#fe5c4c"
  badge-yellow: "#f79e1b"
  badge-green: "#cdefc4"
  badge-pink: "#f5cccc"

typography:
  display-xl:
    fontFamily: "'Nutmeg', 'Lato', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nutmeg', 'Lato', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nutmeg', 'Lato', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Lato', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.primary}"

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
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.dark-header}"
    textColor: "{colors.surface-card}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-item:
    backgroundColor: transparent
    textColor: "{colors.surface-card}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-item-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  search-bar-mobile:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.xs} {rounded.xs} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 4px 12px
  product-card-price:
    typography: "{typography.price}"
    padding: 0px 12px 8px 12px
  product-card-sale-price:
    typography: "{typography.price-sale}"
    padding: 0px 12px 8px 12px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-preorder:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-clearance:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  category-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  category-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  hero-banner:
    backgroundColor: "{colors.dark-header}"
    textColor: "{colors.surface-card}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.dark-header}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 32px 24px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
  pagination:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, saturated in #ff5e00 with white text and a tight 4px radius. Used for "Add to Cart," "Checkout," and primary conversion paths. On hover, darkens to #e05200; disabled state fades to a soft peach #ffb080. The 44px height meets touch-target minimums, and the 12px 24px padding gives enough weight without feeling bloated.

**`button-secondary`** — An outlined or ghost variant on the light canvas (#f3f3f3) with #181818 text. Used for "View Details," "Wishlist," and secondary actions. Active state fills with the hairline gray (#d1d1d1). The same 44px height and 4px radius keep the button family consistent.

**`button-pill-primary`** — A smaller, fully rounded pill variant (36px tall) used for filter tags, "Shop Now" quick-links, and mobile-optimized CTAs. The full-radius shape contrasts with the otherwise angular button system, signaling a more casual, scannable interaction.

**`button-pill-outline`** — The ghost counterpart to the pill primary, used for inactive category filters and secondary mobile actions. Transparent background with #181818 text, full radius.

### Cards
**`product-card`** — The core browsing unit: a white card with a 4px radius, no padding on the container itself. The product image fills the top with the same radius clipped to the top corners. Title uses 16px/600 Lato, price uses 16px/700 Lato, both with 8–12px internal padding. Sale prices render in #ff5e00. Badges overlay the image or sit inline below the title.

**`product-card-sale-price`** — Price text rendered in the primary orange (#ff5e00) to signal discount urgency. Used alongside or replacing the standard price token when a product is on sale.

### Navigation
**`nav-bar`** — A dark, high-contrast header bar at 56px tall, set against #141519. Navigation links are uppercase Lato 14px/600 with 0.5px letter spacing, white text. Active or hover states shift to the primary orange. The bar is fixed or sticky, carrying the brand logo, search bar, account icon, and cart.

**`nav-bar-item-active`** — Active navigation link highlighted in #ff5e00 against the dark surface (#23252b) background. Used for the current section or page indicator.

**`search-bar`** — A standard 44px text input with 4px radius, white background, and #181818 text. Sits within the nav bar on desktop, expands to full width on mobile. Focus state draws a #ff5e00 border.

**`search-bar-mobile`** — Mobile variant that sits on the dark header surface (#23252b) with white text, maintaining the same dimensions and radius.

### Forms
**`text-input`** — Standard form input at 44px height with 4px radius, white background, #d1d1d1 border, and #181818 text. Focus state shifts border to #ff5e00. Used for search, checkout fields, account forms, and newsletter signups.

**`quantity-selector`** — A compact 40px input with border, used on product detail pages for adjusting purchase quantity. Maintains the same 4px radius and typography as text inputs.

### Badges
**`badge-sale`** — Orange (#ff5e00) badge with white uppercase text, 4px radius, and tight 2px 8px padding. Used to flag discounted items in the product grid.

**`badge-preorder`** — Cyan (#029ddf) badge signaling upcoming releases available for pre-order. Same shape and typography as the sale badge.

**`badge-limited`** — Marigold (#fab818) badge with dark text, used for limited-edition or exclusive items. The yellow-orange stands out against the white card background.

**`badge-clearance`** — Crimson (#ea001e) badge for deep-discount clearance items. High urgency signal.

**`badge-out-of-stock`** — Gray (#747474) badge with white text, used to indicate unavailable items without removing them from the grid.

### Footer
**`footer`** — A dark footer matching the header (#141519), with muted gray (#747474) links and body text. Links shift to #ff5e00 on hover. Padding is generous at 32px 24px, with stacked columns on mobile and a multi-column layout on desktop.

### Pagination
**`pagination`** — Standard numbered page navigation at 40px height, white background, #181818 text, 4px radius. Active page fills with #ff5e00 and white text. Used on category browse pages and search results.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 items per row); nav collapses to hamburger menu; search bar expands full-width below logo; category filters stack vertically; footer collapses to single column; hero banner reduces padding to 24px 16px |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; search bar sits inline in nav; category filters wrap in a horizontal scrollable strip; footer shows 2–3 columns |
| Desktop | 1128–1440px | Three-to-four-column product grid; full nav with all links visible; search bar at standard width; category filters in a single row; footer at full multi-column layout |
| Wide | > 1440px | Four-to-five-column product grid; max-width container (~1440px) centers content; nav and footer remain at full width with increased horizontal padding |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (36px for pill filters, which are less critical)
- Product cards are tappable as a single unit (no small hit areas within)
- Category filter pills are 36px tall with 16px horizontal padding, exceeding the 44px tap target recommendation when including padding
- Pagination numbers are 40px square, comfortably tappable

### Collapsing Strategy
- Top nav collapses to a hamburger icon at < 744px; the search bar moves below the logo row
- Category filter strip becomes a horizontally scrollable row at tablet widths, then stacks vertically on mobile
- Product grid reduces from 4–5 columns on wide screens to 2 columns on tablet and 1–2 columns on mobile
- Footer collapses from 4–5 columns on desktop to a single stacked column on mobile
- Hero banner reduces typography from display-lg (28px) to display-md (24px) on mobile, with reduced padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is heavily polluted with payment-widget colors (Klarna pink #ff7262, Afterpay blue #a259ff, Shopify green #0acf83, PayPal blue #033389) and social-icon colors (YouTube red #f24e1e, etc.). The brand's true primary (#ff5e00) was identified as the most distinctive non-generic accent, but secondary brand colors may be more limited than the full extracted list suggests.
- No meta theme-color was found; the browser chrome/taskbar color is unknown.
- Hover and focus states for most components were inferred from common patterns (darken primary, show border) rather than extracted from live CSS.
- Error states (form validation, out-of-stock messaging, payment failures) were not observed and are not represented.
- Dark mode is not supported; the site uses a fixed light canvas with dark header/footer.
- The "Crunchyroll" brand identity (crunchyroll atyp fonts) appears in the extracted font list but is likely a parent-company artifact or redirect; the legacy RightStuf site uses Nutmeg and Lato as its primary typefaces.
- Sub-brand or seasonal color palettes (holiday sales, convention exclusives, publisher-specific themes) were not captured.
- Animation and transition timing (hover fades, card lift, loading states) were not extracted.
- The checkout flow was not fully observed; payment-form styling, address-entry fields, and order-confirmation components are inferred from standard e-commerce patterns.
- Accessibility contrast ratios between #ff5e00 on white and #181818 on #f3f3f3 have not been verified against WCAG 2.1 AA standards.
