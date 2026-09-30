---
version: alpha
name: "Crave Direct"
source_url: "https://www.cravedirect.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four tones — near-black #121212, dark charcoal #222222, mid-gray #404040, and pale silver #dedede — constitute the entire extracted palette for Crave Direct, with the white (#ffffff) meta theme-color providing the browsing canvas. The absence of any accent color is the system's defining choice: a warehouse-direct accessories operation that trusts product photography and price clarity over brand color drama. Buttons, cards, and input fields resolve to the same monochromatic stack, using weight shifts and surface contrast rather than hue to establish hierarchy. The `{rounded.sm}` radius on primary CTAs and `{rounded.xs}` on badges reads as purposeful — a clean-shouldered edge that matches the utilitarian promise of the category. The nav occupies a white ground at the top, grounding the browser experience before the catalog shifts into darker surface territory for promotional moments, a split that separates discovery from conversion. Type runs on a system-UI fallback stack since no custom font families were detectable — a move that trades distinctiveness for universal rendering speed, appropriate for a catalog that may span hundreds of SKUs across phone cases, chargers, cables, and screen protectors. Display headlines sit at weight 700 with tight letter-spacing to compress visual density, product titles land at 600 for scanning legibility, and body copy drops to 400 — a three-rung ladder that communicates without a signature typeface. Hover and active states deepen toward #121212 on the light canvas, or flip to a lighter fill on dark grounds, keeping interactions legible across both surface modes. The overall system is engineered for catalog throughput: dense grids, fast-add affordances, and sale badges that snap to the top-left corner of every card.

colors:
  primary: "#404040"
  primary-active: "#222222"
  primary-disabled: "#a8a8a8"
  ink: "#121212"
  body: "#222222"
  muted: "#666666"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  surface-dark-raised: "#222222"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-sale: "#404040"
  badge-sale-text: "#ffffff"
  badge-new: "#222222"
  badge-new-text: "#dedede"
  star-fill: "#404040"
  price-strike: "#a8a8a8"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  price-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  badge-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
    border: none
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
    padding: 13px 23px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  nav-bar-icon:
    color: "{colors.ink}"
    size: 24px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  announcement-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBorderRadius: "{rounded.sm} {rounded.sm} 0 0"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    strikethroughColor: "{colors.price-strike}"
  product-card-hover:
    border: "1px solid {colors.body}"
    shadow: "0 4px 16px rgba(0,0,0,0.10)"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    position: top-left
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    position: top-left
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: button-primary
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: button-primary
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "12px {spacing.base}"
    height: 44px
    iconColor: "{colors.muted}"
    iconSize: 18px
  search-bar-active:
    border: "1.5px solid {colors.body}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  category-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.display-sm}"
    itemTitleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    ctaVariant: button-primary
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    buttonColor: "{colors.body}"
    height: 40px
    width: 120px
  star-rating:
    fillColor: "{colors.star-fill}"
    emptyColor: "{colors.hairline}"
    size: 14px
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-dark-raised}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-md}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "1px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — A solid #404040 fill with white uppercase text at 15px weight 600, set on an `{rounded.sm}` 8px corner — a square-shouldered slab that signals directness over friendliness. Hover deepens to `{colors.primary-active}` (#222222) with no animation delay, keeping interactions snappy for catalog-speed browsing. Disabled state desaturates to `{colors.primary-disabled}` (#a8a8a8), preserving the monochromatic logic throughout. Height locks at 48px across all breakpoints for consistent touch ergonomics on mobile-first shopping sessions.

**`button-secondary`** — White fill with a 1.5px `{colors.ink}` border and the same uppercase `{typography.button-md}` treatment as primary. Hover fills to `{colors.surface-soft}` for a shallow depth signal that doesn't compete with primary. Used for secondary actions — "Learn More," "View Details," "Add to Wishlist" — placed alongside primary CTAs on product pages and campaign banners.

**`button-ghost`** — A lighter 40px variant with a `{colors.hairline}` border and transparent background, rendered in `{typography.button-sm}`. Used for filter chips, sort dropdowns, and low-emphasis utility actions in the catalog browse context where visual weight must stay subordinate to product imagery.

### Search

**`search-bar`** — A `{rounded.full}` pill on a `{colors.surface-soft}` ground, 44px tall, with an 18px muted search icon inset at left. The pill shape is the only place the full-radius token appears in the browse UI, deliberately contrasting the square-shoulder button system to communicate "exploration" versus "commitment." Active state sharpens to a `{colors.body}` border and lifts the background to white.

### Navigation

**`nav-bar`** — White canvas, 64px tall, with a bottom `{colors.hairline}` divider separating the nav shelf from the catalog below. Logo and all navigation links render in `{colors.ink}`. Links use `{typography.nav-link}` at weight 500 — deliberately lighter than the 600-weight product titles beneath so the nav frame recedes and product content leads. Cart, search, and account icons render at 24px with 44px hit-area padding.

**`announcement-bar`** — A 36px near-black (#121212) strip that sits above the nav, carrying promotional copy — free shipping thresholds, sale countdowns, new arrivals — in `{typography.caption}` white text. No radius, no padding variation: a hard full-width shelf that frames the top of the session and is the first brand impression before any product imagery loads.

**`nav-dropdown`** — A white panel with a 1px `{colors.hairline}` border and `{rounded.sm}` corners, appearing below the triggering nav link. Sub-links render in `{typography.body-sm}` `{colors.body}`. No mega-menu imagery is assumed — text-only columns for category navigation.

### Product Cards

**`product-card`** — A white card with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. The product image fills the full card width with matching top radius; below it, product name in `{typography.title-sm}` weight 600, current price in `{typography.price-md}` weight 700, and a struck-through compare-at price in `{colors.price-strike}`. Hover deepens the border to `{colors.body}` and lifts a 10% black shadow — the strongest interaction cue in the system, signaling actionability without an accent color. Star rating and review count sit below the price in `{typography.caption}` `{colors.muted}`.

**`badge-sale`** — A 4px-radius pill anchored to the top-left corner of the product image, filling with `{colors.badge-sale}` (#404040) and printing white text in `{typography.badge-label}` (11px, uppercase, 0.5px tracking). The badge is visually distinct against product photography but stays within the monochromatic stack — no red or orange, which would introduce an accent color the rest of the system doesn't support.

**`badge-new`** — Same geometry as `badge-sale`, using `{colors.badge-new}` (#222222) fill with `{colors.badge-new-text}` (#dedede) text to create a subtle light-on-dark differentiation from the sale badge without breaking the palette.

### Category Navigation

**`category-pill`** — A `{rounded.full}` filter chip deployed on collection and browse pages. Inactive: white fill, `{colors.hairline}` border, `{colors.body}` text in `{typography.title-sm}`. Active inverts to `{colors.ink}` fill with `{colors.on-primary}` white text — the starkest selection affordance in the system, and given the absence of an accent hue, the most "branded" interaction pattern in the UI.

### Cart

**`cart-drawer`** — A 400px panel sliding in from the right edge, white background with a left `{colors.hairline}` border. The cart header uses `{typography.display-sm}` (22px, weight 600); line items carry `{typography.title-sm}` product names and `{typography.price-md}` pricing. A full-width `button-primary` anchors the drawer footer as the checkout CTA. On mobile the drawer expands to 100vw with a bottom-fixed checkout rail.

**`quantity-stepper`** — A 120×40px pill control with `{rounded.sm}` corners on a `{colors.surface-soft}` background. Minus and plus buttons are `{colors.body}` (#222222), the quantity value center-aligns in `{typography.title-sm}`. Paired with `button-primary` ("Add to Cart") on product detail pages.

### Hero

**`hero-banner`** — Full-width dark hero on `{colors.surface-dark}` (#121212), with headline at `{typography.display-xl}` (40px, weight 700, −0.5px tracking) in white and body copy at `{typography.body-md}`. The dark-on-dark layering — near-black background with charcoal-fill CTA — is the system's most intense surface moment, reserved for sale events and flagship campaigns. A `button-primary` CTA sits below the subhead with `{spacing.md}` vertical gap.

**`hero-banner-light`** — A softer promotional variant on `{colors.surface-soft}` background. Same typographic scale as the dark hero but with `{colors.ink}` headline text. Used for secondary feature moments — new arrivals, category spotlights — where dark drama would overpower the message.

### Footer

**`footer`** — A dark raised surface (`{colors.surface-dark-raised}`, #222222) with a 1px top border in `{colors.primary}` (#404040), one of the only places the primary color appears as a decorative line rather than a fill. Section headings in `{typography.title-md}` weight 600 white; navigation links in `{typography.body-sm}` `{colors.hairline}` gray. Four-column layout on desktop collapses to stacked accordions on mobile.

### Ratings

**`star-rating`** — 14px stars filled in `{colors.star-fill}` (#404040) with empty stars rendered in `{colors.hairline}`. Review count in `{typography.caption}` `{colors.muted}` sits inline to the right of the stars. The charcoal star color holds contrast against both white card backgrounds and the dark surface hero without requiring a separate star token per surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero drops to `display-md` headline (28px); cart-drawer expands to 100vw; category pills scroll horizontally with overflow-x |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with tap-to-expand dropdowns; hero retains dark layout with reduced horizontal padding |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with hover-triggered dropdowns; cart-drawer fixed at 400px; announcement bar shows full promotional copy |
| Wide | > 1440px | Content max-width ~1400px centered; product grid holds at four columns; hero uses wider image crop with text left-aligned at 50% column |

### Touch Targets
- All interactive controls (buttons, pills, steppers, icon buttons) enforce a minimum 44×44px touch target
- Cart, search, and account icons in `nav-bar` are padded to 44px hit area even at 24px visual render size
- `category-pill` uses 36px height; minimum 44px horizontal span for comfortable single-thumb tap
- `quantity-stepper` minus and plus buttons are each minimum 40×40px
- `badge-sale` and `badge-new` are display-only; no tap target required

### Collapsing Strategy
- Navigation collapses to hamburger at < 744px; the mega-menu becomes a full-screen slide-in overlay from the left edge
- Product grid: 1 column (mobile) → 2 columns (tablet) → 3–4 columns (desktop/wide)
- Hero headline: `display-xl` (40px) → `display-md` (28px) on mobile; subhead line-count may be clamped to two lines
- `announcement-bar` persists across all breakpoints; text truncates with ellipsis below 375px viewport width
- Footer four-column link grid collapses to single-column tap-to-expand accordion on mobile
- `search-bar` collapses to an icon tap that expands a full-width overlay input on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font family detected from live extraction; system-UI stack applied throughout — actual brand typeface (if any) may differ and would significantly change typographic character
- Only four hex values extracted (#404040, #222222, #dedede, #121212), all in the gray/near-black range; no accent, highlight, success, warning, or error colors confirmed from crawl data
- No confirmation of exact button border-radius, spacing scale, or grid gutter values — all inferred from Shopify defaults and tech-accessories category conventions
- Hover and focus interaction states are reasoned estimates; no live state data was extractable from static crawl
- Sale badge exact placement, color, and shape not observed — design above is inferred from Shopify theme conventions for accessories stores
- No breakpoint values confirmed from source; column counts and nav collapse points are estimated from Dawn/Shopify theme defaults
- Price display format (currency symbol position, decimal handling, "From $X" pattern for variant pricing) not observed
- Product image aspect ratio not confirmed — card image proportions assumed 1:1 square; actual ratio may differ
- No confirmation of whether a sticky nav, scroll-triggered announcement bar hide, or lazy-load shimmer exists in the live experience
