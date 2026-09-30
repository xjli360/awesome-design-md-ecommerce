---
version: alpha
name: "Mindzai"
source_url: "https://www.mindzai.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  #ff5268 arrives in Mindzai's grid the way a chase variant surfaces inside a sealed blind box — unexpected, electric, snapping an otherwise near-monochrome layout into focus. The store trades in designer toys, blind boxes, and art objects from labels spanning Kidrobot to dozens of independent studios, and the visual system honors that collectible logic: a controlled palette of off-blacks (#111111, #1e1e1e, #121212) and neutral grays (#888888, #dedede) acts as the neutral vitrine, while the coral-red primary is deployed only where intent matters — add-to-cart calls, sale badges, hover borders, checkout rails. Nothing competes with the product photography. The canvas is white with occasional warm off-white surfaces (#e5e3df, #f2f4f6) that read like gallery walls rather than sterile boxes. Product cards carry hard, unrounded corners — no softening — signaling editorial seriousness: each toy is an art object catalogued, not merchandised. Dark-field hero panels (#1e1e1e) handle feature drops and limited releases, contrasting against the bright grid below with the tonal shift of an announcement rather than decoration. Font extraction returned nothing, meaning all typeface tokens load client-side via JavaScript; from visual inspection the store favors a clean system sans-serif at modest weights, display text settling around 700 weight while body copy sits at 400, creating a sharp hierarchy without custom letterforms. Uppercase micro-labels on badge elements and filter controls carry tight letter-spacing, borrowing the vocabulary of streetwear and art-print labels that share shelf space here. Navigation runs two rails: a thin announcement strip in near-black for shipping notices, then the main bar in white with logo, category links, and icon cluster for search, wishlist, and cart. The footer inverts to a dark field with warm gray text, reinforcing the two-tone grammar of the whole site. Blind-box products surface an additional mystery indicator in the badge system — the same coral used for sale flags — because in collectible culture, the unknown is precisely the selling point.

colors:
  primary: "#ff5268"
  primary-active: "#e03050"
  primary-disabled: "#ffb3bc"
  ink: "#111111"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#5d5b5b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-subtle: "#f2f4f6"
  surface-warm: "#e5e3df"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-field: "#1e1e1e"
  near-black: "#121212"
  mid-dark: "#2a2a2a"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.75px
    textTransform: uppercase
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.75px
    textTransform: uppercase
  announcement:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px

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
    padding: 13px 28px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 12px 27px
    height: 46px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.canvas}"
    padding: 12px 27px
    height: 46px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.dark-field}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-label}"
    height: 60px
  announcement-bar:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.canvas}"
    typography: "{typography.announcement}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm}"
    gap: "{spacing.xs}"
  product-card-hover:
    outlineColor: "{colors.primary}"
    outlineWidth: 2px
    outlineStyle: solid
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  product-badge-new:
    backgroundColor: "{colors.dark-field}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  product-badge-mystery:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
    label: "BLIND BOX"
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xxl}"
    ctaButton: "button-ghost-dark"
  hero-banner-light:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  category-tile:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    imageOverlay: "rgba(17, 17, 17, 0.38)"
    hoverOverlay: "rgba(17, 17, 17, 0.20)"
    aspectRatio: "4 / 5"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "none"
    focusBorder: "1px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    height: 44px
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    activeIndicatorColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    width: 120px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    checkoutButtonBackground: "{colors.primary}"
    checkoutButtonTextColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.dark-field}"
    textColor: "{colors.surface-warm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.mid-dark}"

---

## Components

### Buttons

**`button-primary`** — Solid coral-red (#ff5268) fill, all-caps spaced type at 13px/700 weight, zero border-radius. This is the dominant CTA throughout the Shopify flow: add-to-cart, checkout, newsletter subscribe. Active state deepens to `#e03050`; disabled washes out to `#ffb3bc` while keeping white text. The hard-edged rectangle is a deliberate contrast to the soft product photography and reads as a functional stamp rather than a decorative element.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` outline and matching uppercase type. Used for secondary actions (wishlist, share, view-all links) where the coral would oversaturate the page. Active state inverts to black fill with white text, avoiding the primary coral to maintain its scarcity.

**`button-ghost-dark`** — Transparent fill with 1px white outline, used exclusively inside dark hero panels. Mirrors the secondary button geometry so hero layouts can include a CTA without breaking the dark-field aesthetic.

### Product Cards

**`product-card`** — Square (1:1) image crop, hard corners, minimal padding. Title renders in `{typography.body-sm}` at `{colors.ink}` with price below in `{typography.price-sm}` at 600 weight. Hover state draws a 2px `{colors.primary}` outline around the full card — a clean signal that doesn't disturb layout. Badges stack in the top-left corner of the image area; multiple badges tile vertically.

**`product-badge` / `product-badge-mystery` / `product-badge-new` / `product-badge-sale`** — Flat rectangular chips with no radius. Coral (#ff5268) for sale, mystery/blind-box markers; near-black (#1e1e1e) for new arrivals. The shared badge vocabulary unifies collectible-specific labels (BLIND BOX, MYSTERY) with standard retail labels (NEW, SALE) under one legible system.

### Navigation

**`nav-bar`** — White background, 60px tall, fine `{colors.hairline-soft}` bottom border. Logo left, category links centered, icon cluster (search, wishlist, cart) right. Collapses to a hamburger at mobile. A second `nav-bar-dark` variant with `{colors.dark-field}` background activates on collection pages with dark hero imagery, maintaining legibility without an abrupt modal or scroll-triggered change.

**`announcement-bar`** — 36px near-black strip pinned above the nav. Centered caption-scale type in white, used for free-shipping thresholds and limited-time promotions. Single-line only; rotates if multiple messages are queued.

### Hero

**`hero-banner`** — Full-width, dark-field (`#121212`) background with display-xl headline and optional body copy. The `{colors.primary}` accent may highlight a word in the headline or drive a CTA button in ghost-dark style. Used for product drops, collaborations, and seasonal pushes. A light variant (`hero-banner-light`) swaps the dark field for `{colors.surface-warm}` (#e5e3df) for editorial series and softer promotional moments.

### Search & Filtering

**`search-bar`** — Light gray fill (`{colors.surface-soft}`), no border at rest; 1px `{colors.primary}` border on focus. Zero radius. Appears as an expanding inline element in the nav on desktop and a full-width block below the nav on mobile.

**`collection-filter`** — Horizontal scrollable chip row or sidebar panel depending on viewport. Active filter label renders in `{colors.primary}`; an underline indicator in the same color marks the active state. Bottom border in `{colors.hairline}` separates filters from the product grid.

### Cart & Checkout

**`cart-drawer`** — Slides in from the right at 380px width. White background, `{colors.hairline}` left border. Item rows use `{typography.body-sm}`. The checkout CTA button at the bottom is full-width `button-primary` in `{colors.primary}`.

**`quantity-selector`** — Minus/input/plus layout inside a 40px-tall `{colors.surface-soft}` container with 1px `{colors.hairline}` border. Matches the geometry of the text input — no rounding.

### Supporting

**`category-tile`** — Full-bleed image with a dark overlay (`rgba(17,17,17,0.38)`) and centered uppercase `{typography.title-sm}` label in white. Hover lightens the overlay. Used in the homepage category grid and collection landing pages.

**`breadcrumb`** — Small caption-scale path in `{colors.muted}` with `/` separators in `{colors.hairline}`. Active (current) page segment renders in `{colors.ink}`.

**`footer`** — Dark-field background with warm-gray body text and lighter hover state for links. Column headings use `{typography.title-sm}` (uppercase, tracked). Bottom strip includes social icons (Twitter, Facebook, Pinterest, Instagram) and legal copy in `{typography.caption}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; announcement bar wraps to two lines; hero padding reduces to `{spacing.xl}`; category tiles stack vertically; filters move to a drawer behind a "Filter" button |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + icons, hides text links; hero maintains dark-field layout with reduced type size; category tiles render in 2×2 grid |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with text links; hero at full display-xl scale; sidebar filter panel visible by default |
| Wide | > 1440px | Max content width capped ~1400px, centered; five-column grid optional on wide collection pages; hero hero image scales but text block stays constrained |

### Touch Targets

- All buttons minimum 44px tall; quantity selector and cart icon 44×44px
- Mobile nav icons spaced at least 44px apart horizontally
- Filter chip row is horizontally scrollable with momentum scroll on iOS
- Swipe-to-close supported on cart drawer on mobile

### Collapsing Strategy

- Top nav text links collapse to hamburger drawer first; icon cluster (search, wishlist, cart) persists at all widths
- Announcement bar hides on the smallest viewport breakpoint to recover vertical space for product content
- Product grid steps down: 4-col → 3-col → 2-col → 1-col
- Hero subtitle body copy hidden below 744px; headline and CTA remain
- Footer four-column layout collapses to single accordion-expandable column on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extractable — the site loads typefaces via JavaScript after initial paint, likely via a Shopify theme asset or Google Fonts script. All typography tokens use the system sans stack as a neutral fallback; actual brand fonts (name, weights, optical sizes) should be verified by inspecting loaded network requests or the Shopify theme's `settings_data.json`.
- Exact corner-radius values could not be confirmed from extraction; the spec assumes zero-radius (sharp corners) throughout based on the editorial/collectible aesthetic, but actual theme settings should be verified.
- Animation and transition timing (hover durations, drawer slide timing, skeleton loading states) were not captured and would require live interaction testing.
- Specific typographic scale for product title truncation rules (one-line vs two-line clamp on card) not confirmed.
- Social icon set and icon style (line, filled, colored vs monochrome) not extractable from color data alone.
- Exact grid gutter widths and column counts per breakpoint not confirmed; values in Responsive Behavior are inferred from category norms and Shopify theme defaults.
