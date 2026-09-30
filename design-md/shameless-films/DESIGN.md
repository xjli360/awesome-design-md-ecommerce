---
version: alpha
name: "Shameless Films"
source_url: "https://www.shameless-films.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cinema-obsessed digital storefront where #fbd616 — a hot, unapologetic yellow — acts as the single voltage that powers every primary CTA, price badge, and sale flag, cutting through a near-total black-and-charcoal canvas (#212121, #1f1f1f, #101010, #060606). The brand treats color as a rare resource: the yellow appears in tight, deliberate doses — a button, a tag, a star — never flooding the layout, always earning its attention. Typography runs on a system of monospaced and serif faces (Consolas, Menlo, Monaco, Courier) that evoke film-script formatting, title cards, and the technical language of cinema, while body copy defaults to Arial and Helvetica for readability. Product cards stack in dense, information-rich grids where every pixel carries weight: price, format, stock status, and a "NEW" or "SOLD OUT" badge sit within a single card, often with a yellow accent bar or filled badge. The overall mood is that of a repertory cinema lobby crossed with a collector's basement — dark walls, yellow signage, and the sense that every title has been hand-selected. Corners are mostly sharp ({rounded.xs} or {rounded.none}), with only the occasional pill-shaped badge or button ({rounded.full}) to break the rectilinear discipline. The extracted palette includes a wide range of blues (#003388, #0693e3, #0757fe, #0a7aff) and a green (#00d084) that likely belong to third-party payment widgets (Klarna, Afterpay, Shopify Pay) and social-icon sets rather than the brand itself; the true brand identity is built on the yellow-black binary, with #1a1a1a and #181818 as the primary canvas tones and #eeeeee and #f5f5f5 for body text on dark surfaces.

colors:
  primary: "#fbd616"
  primary-active: "#e2bd00"
  primary-disabled: "#ffff57"
  ink: "#ffffff"
  body: "#eeeeee"
  muted: "#949494"
  muted-soft: "#555555"
  hairline: "#3f3f3f"
  hairline-soft: "#444444"
  canvas: "#212121"
  surface-soft: "#1f1f1f"
  surface-card: "#1a1a1a"
  surface-strong: "#181818"
  on-primary: "#1a1a1a"
  on-dark: "#ffffff"
  badge-new: "#fbd616"
  badge-sold-out: "#555555"
  badge-sale: "#fbd616"
  star-rating: "#fbd616"
  scrim: "#000000"
  accent-blue: "#003388"
  accent-green: "#00d084"

typography:
  display-xl:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-mono:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  icon-button:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 40px
  dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
  star-rating:
    color: "{colors.star-rating}"
  loading-spinner:
    color: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in yellow (#fbd616) with dark text (#1a1a1a) and zero border radius. Uses monospaced uppercase type (Consolas) at 14px with 0.5px letter-spacing, giving it the feel of a film-clapper label or a cinema ticket stub. On hover, shifts to a deeper gold (#e2bd00). Disabled state uses a washed-out yellow (#ffff57) that still reads as yellow but lacks contrast. **`button-secondary`** — An outlined variant on the dark canvas (#212121) with a 2px yellow border and yellow text. On hover, fills solid yellow. **`button-tertiary-text`** — A text-only yellow link with no background or border, used for "View All" links and secondary actions. **`button-pill`** — A fully rounded pill variant used for small utility actions like "Add to Cart" on mobile or filter resets; same yellow fill, smaller padding.

### Cards
**`product-card`** — The core content unit, a dark rectangle (#1a1a1a) with no border radius. Contains a full-bleed product image (no rounding), a title in white (#ffffff) at 16px weight 600, a price in yellow (#fbd616) at 16px weight 400, and a badge strip along the top or bottom edge. Badges are sharp-cornered rectangles in yellow (NEW, SALE) or gray (#555555, SOLD OUT) with uppercase monospaced type at 11px. The card stacks information densely — format, release year, stock status, and price all visible without hover. On hover, the card may show a subtle border or shadow shift, but the extracted data does not confirm a specific hover state.

### Navigation
**`top-nav`** — A fixed 64px bar on the dark canvas (#212121) with uppercase monospaced nav links at 14px. Active links are yellow (#fbd616); inactive links are muted gray (#949494). The nav likely includes a logo on the left and a search icon on the right. No border radius on any nav element. **`nav-link-active`** and **`nav-link-inactive`** define the two states. The nav may collapse to a hamburger menu on mobile, but the extracted data does not confirm the exact breakpoint.

### Forms
**`search-bar`** — A sharp-cornered input field on a slightly lighter dark surface (#1f1f1f) with a 1px hairline border (#3f3f3f). Body text is Arial at 14px. On focus, the border thickens to 2px and turns yellow (#fbd616). **`quantity-selector`** — A compact, sharp-cornered input for cart quantities, on the same dark surface with body text. **`dropdown`** — A standard select dropdown on the card surface (#1a1a1a) with a hairline border. Hovered items get the soft surface background (#1f1f1f).

### Footer
**`footer`** — A dark bar (#212121) with muted gray links (#949494) that turn yellow on hover. Typography is Arial at 14px for links and 12px for copyright text. No border radius. Likely contains columns for categories, customer service, and social links.

### Badges & Tags
**`product-card-badge`** — A sharp-cornered yellow rectangle with uppercase monospaced type, used for "NEW" and "SALE" indicators. **`product-card-badge-sold-out`** — Same shape but gray fill (#555555) with white text, used for out-of-stock items. **`filter-tag`** — A pill-shaped tag on the soft surface (#1f1f1f) with body text; active state fills yellow.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; search bar moves to a toggle; badges stack vertically; buttons go full-width; hero banner reduces to single image with smaller type |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links; search bar is visible but compact; filter tags wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; search bar at full width; filter tags in a single horizontal row; hero banner at full width with two images |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero banner expands to full viewport height with parallax effect (assumed) |

### Touch Targets
- All buttons and links: minimum 44px height (buttons) and 44x44px tap area for icon-only controls.
- Filter tags: minimum 32px height with 14px horizontal padding.
- Quantity selector: 40px height with 40px minimum width.
- Product card links: entire card is tappable (no separate "View" button).

### Collapsing Strategy
- Top nav: links collapse to hamburger menu below 744px; search icon remains visible, expands to full-width input on tap.
- Product grid: collapses from 4 columns to 3 to 2 to 1 as viewport shrinks.
- Filter tags: horizontal row wraps to two rows on tablet, collapses to a single "Filter" button on mobile that opens a modal or drawer.
- Footer: multi-column layout collapses to single column on mobile; link lists become accordions or stacked lists.
- Hero banner: dual-image layout collapses to single image on mobile; text overlay reduces from display-xl to display-lg.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is large (30+ colors) and includes many blues (#003388, #0693e3, #0757fe, #0a7aff) and a green (#00d084) that are almost certainly third-party widget colors (Klarna, Afterpay, Shopify Pay, social icons) rather than brand colors. The brand's true primary is #fbd616 (yellow), with #212121, #1f1f1f, #1a1a1a, and #181818 as the dark canvas tones. The white (#ffffff) and near-whites (#eeeeee, #f5f5f5) are body text colors on dark backgrounds.
- Font-family declarations found are generic (Arial, Helvetica, Consolas, Menlo, Monaco, serif, star). The brand likely uses a custom or more specific font stack for display type (possibly a film-script or title-card face), but it was not extracted. The monospaced stack (Consolas, Menlo, Monaco) is used for buttons, badges, and nav links based on the brand's cinema aesthetic.
- Hover states for product cards (shadow, border, scale) are not confirmed from extracted data.
- Error states for forms (validation messages, error borders) are not extracted.
- Dark mode is not applicable — the brand already uses a dark canvas as default.
- Sub-brand or category-specific color variations (e.g., horror, comedy, documentary sections) are not confirmed.
- The hero banner's exact layout (dual image, single image, video background) is inferred from common patterns in the film retail space, not extracted.
- Loading states (skeleton screens, spinners) are not extracted; a yellow spinner is assumed.
- The checkout flow (cart, payment, confirmation) likely uses third-party widgets (Shopify Checkout, Klarna, Afterpay) and is not part of the brand's design system.
