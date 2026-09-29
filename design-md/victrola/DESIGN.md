---
version: alpha
name: "Victrola"
source_url: "https://www.victrola.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Victrola drops a needle onto a near-black canvas (#1c1c1c, #202125) and lets a single signal carry — a warm-vinyl orange (#fb661f) lands on every primary CTA, promotional badge, and add-to-cart button across the store. The contrast is deliberate: dark platter-weight hero backgrounds let the orange read as the center label on a 45rpm single, drawing the eye directly to conversion points. Secondary accents are not decorative — they map one-to-one onto product finish variants. Turntables sold in limited colorways surface directly as UI swatch circles: mustard-gold (#facd34, #e8db34), dust-rose (#db5b70), midnight teal (#025f70), maritime navy (#00247a), cognac brown (#5f3f3f), and a vintage warm-cream (#edebdf) that evokes the texture of kraft paper inner sleeves. The palette is the catalog. Type runs entirely on system font stacks (Arial, Helvetica Neue, -apple-system) with display headlines pushed to weight 700 and body copy held at 400 — a narrow range that favors shelf-tag legibility over typographic personality. The absence of a custom typeface is offset by strong product photography: turntables against dark environments carry the aesthetic weight that proprietary type would otherwise need to provide. Button and card corners use modest radii ({rounded.sm} 8px to {rounded.md} 12px) — direct enough for a hardware retailer, soft enough to avoid grid-catalog austerity. The neutral gray skeleton (#e5e5e5, #ededed, #c8c8c8) manages hairlines, input borders, and card separators, while the off-cream wash (#edebdf) recurs as a warm section background — an analog surface cue inside a digital catalog.

colors:
  primary: "#fb661f"
  primary-active: "#d94f0a"
  primary-disabled: "#fcc09a"
  accent-gold: "#facd34"
  accent-gold-alt: "#e8db34"
  accent-rose: "#db5b70"
  accent-navy: "#00247a"
  accent-teal: "#025f70"
  accent-cream: "#edebdf"
  accent-brown: "#5f3f3f"
  accent-green: "#5bdb86"
  ink: "#1c1c1c"
  body: "#2c2c2c"
  muted: "#454545"
  hairline: "#c8c8c8"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f1f1f1"
  surface-dark: "#202125"
  surface-darker: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#ff0000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.6px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.on-dark}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  hero-dark:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  promo-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  color-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
  color-swatch-active:
    border: "2px solid {colors.ink}"
    rounded: "{rounded.full}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-tile-label:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  section-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.xl}"
  warm-section:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  newsletter-input:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
    padding: 10px 14px
    height: 44px

## Components

### Buttons
**`button-primary`** — A solid orange (#fb661f) block button with uppercase Arial at 700 weight, 0.6px letter-spacing, and {rounded.sm} corners. Active state darkens to #d94f0a; disabled washes to #fcc09a. This is the dominant CTA treatment — add-to-cart, buy-now, and hero calls all use it. The uppercase-bold combination reads as hardware-retail confident rather than app-friendly soft.

**`button-secondary`** — Transparent fill with a 2px solid #1c1c1c border and matching dark uppercase label. Paired with button-primary when two parallel actions appear side-by-side — e.g., "Add to Cart" (primary) beside "Add to Wishlist" (secondary). Shares the same height (48px) and padding for visual symmetry.

**`button-ghost-light`** — The dark-section mirror of button-secondary: transparent fill, 2px white border, white uppercase label. Lives inside hero-dark sections and the near-black footer area where dark ink would disappear against the background.

### Inputs
**`text-input`** — 44px tall, 1px #c8c8c8 hairline border, {rounded.xs} corner radius. Shopify's default field proportions. Focus state sharpens the border to #1c1c1c for clear active indication. Used in site search, email newsletter capture, and checkout form fields.

### Navigation
**`nav-bar`** — 64px tall, white canvas background with a 1px #e5e5e5 bottom border. Desktop exposes horizontal category links (Turntables, Bluetooth, Vintage, Accessories, Sale) in 14px 600-weight Arial. A sticky variant (`nav-bar-dark`) blends into near-black hero sections — transparent or #1c1c1c background, white link text — switching to the white nav-bar once the user scrolls past the hero.

### Product Card
**`product-card`** — White card with a 1px #e5e5e5 border, {rounded.sm} corners, and a square 1:1 product image. Title in {typography.title-sm} (16px/600), price in {typography.price-display} (20px/700). Product image backgrounds vary with the finish colorway — a black-cabinet turntable card shows dark photography while a cream-finish model shows light. The promo-badge (orange) anchors to the image's top-left corner on sale products; promo-badge-gold appears on limited editions.

### Hero
**`hero-dark`** — Full-width near-black (#1c1c1c) section with the headline in {typography.display-xl} (48px/700) and descriptive copy in body-md, both white. Primary CTA is button-primary (orange); optional secondary CTA uses button-ghost-light. Product photography of turntables against dark environments fills the right half or bleeds full-width at reduced opacity behind the text. This is the homepage and campaign landing treatment.

### Promotional Badges
**`promo-badge`** — Orange (#fb661f) pill with uppercase 11px/700 Arial in white, {rounded.xs} corners, and tight padding ({spacing.xxs} vertical, {spacing.sm} horizontal). Used for SALE, NEW, BESTSELLER on product cards and collection banners. **`promo-badge-gold`** swaps fill to mustard-gold (#facd34) with dark ink text for limited-run or seasonal callouts, differentiating a "Limited Edition" label from a plain discount.

### Color Swatches
**`color-swatch`** — 24px circle ({rounded.full}) representing a product finish variant. The palette of available swatches spans: black (#1c1c1c), white (#ffffff), navy (#00247a), teal (#025f70), rose (#db5b70), gold (#facd34), brown (#5f3f3f), and cream (#edebdf). Selected state (`color-swatch-active`) adds a 2px #1c1c1c outer ring with a 2px gap, the standard Shopify variant-circle active indicator. Swatches appear on both the collection card and the PDP variant row.

### Category Tiles
**`category-tile`** — Light-gray (#f7f7f7) rounded tile with a product-category image and a centered label in {typography.title-md}. Used on the homepage in a 4-across grid for "Shop by Type" navigation — Portable, Bluetooth, Record Players, Vintage, Accessories. Hover lifts the card with a subtle box-shadow. On the warm-section (cream #edebdf background), tiles use surface-card (#f1f1f1) fill to maintain contrast.

### Warm Section
**`warm-section`** — Off-cream (#edebdf) full-width band used for featured-story or editorial modules — "The Story of Victrola," brand heritage content, or curated gift guides. The warm tone breaks the all-gray/all-dark rhythm and signals content-first versus product-catalog zones.

### Footer
**`footer`** — Near-black (#202125) background with four link columns (Shop, Support, About, Social) in body-sm white text. Footer links use hairline-gray (#c8c8c8) for visual de-emphasis. A newsletter email capture block uses the newsletter-input field (dark-on-dark) paired with a button-primary. Social icons sit above the link columns or inline within the Social column.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen slide-in drawer; hero heading scales to display-sm (24px); color swatches shrink to 20px with expanded 44px tap area via padding |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + search icon + hamburger; hero heading at display-md (32px) with stacked text-then-image layout |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with category links exposed; hero at display-xl (48px) with side-by-side text and image |
| Wide | > 1440px | Max-width container (~1440px) centered; product grid stays at four columns; hero padding expands symmetrically; typography unchanged |

### Touch Targets
- button-primary and button-secondary are 48px tall, comfortably above the 44px minimum
- Color swatches are 24px visually but receive 44×44px tap areas via invisible padding
- Nav hamburger icon minimum 44×44px interactive area
- Footer accordion headers minimum 48px tap height on mobile
- Promo badges are display-only and not interactive; no touch target requirement

### Collapsing Strategy
- Full horizontal nav collapses to hamburger drawer on tablet and below; cart icon and search icon remain visible in the collapsed header bar at all breakpoints
- Four-column footer collapses to stacked accordions on mobile with disclosure chevron; social icons pin above the accordion stack
- Hero two-column layout (text left, product image right) stacks vertically on mobile — image first, text block below with left-aligned CTA buttons
- Category tile grid: 4-across (desktop) → 3-across (tablet) → 2-across (mobile)
- Product grid: 4-across (wide/desktop) → 3-across (desktop narrow) → 2-across (tablet) → 1-across (mobile)
- Color swatch rows truncate beyond 6 swatches on mobile with a "+N more" text expander

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — all font stacks resolve to system fonts (Arial, Helvetica Neue, -apple-system). A Victrola-specific display font may load via Shopify theme JS or a third-party font CDN and was not captured in static extraction.
- The Almarai font stack appears in the extracted list, indicating an Arabic-locale variant of the storefront may exist; RTL layout and locale-specific color/type overrides were not audited.
- Exact button corner radius not verified from rendered output — {rounded.sm} (8px) is inferred from Shopify default theme patterns; inspect live buttons for ground truth.
- Card box-shadow values (blur radius, spread, opacity) not captured — only border color was reliably extracted.
- Hero section layout (full-bleed image vs. split 50/50 vs. text-over-image) varies by campaign; the dark full-bleed treatment is described as the primary pattern but may not apply universally.
- Animation and transition details (hover lift timing, hero parallax, turntable spin loaders) not available from static extraction.
- The accent-green (#5bdb86) and accent-blue (#146ff8, #003eff) appear in extracted colors but their UI role — possibly cart/success state or product colorway — could not be confirmed; treat as secondary utility colors until verified.
- Sale/clearance pricing color (struck-through original price) not confirmed — #ff0000 is present in the palette and is a common sale-price color but its exact usage context was not extracted.
