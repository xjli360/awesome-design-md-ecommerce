---
version: alpha
name: "Astrid & Miyu"
source_url: "https://www.astridandmiyu.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Parchment-warm cream (#f6ede6) floods every background layer on this London demi-fine storefront — the meta theme-color set at the document root, so even the browser chrome blushes before a single product image loads. Cormorant, a high-contrast editorial serif whose hairline strokes run as thin as a fine-gauge chain, handles all display headings at light weight 300, letting generous negative space carry the editorial register that a heavier cut would shout. Tenor Sans governs navigation and labels in spaced uppercase, its even stroke width sitting in cool contrast to Cormorant's modulated forms; Montserrat picks up body copy and price strings with utilitarian neutrality below the fold. CTAs fire in terracotta #cb7f64 — a warm copper-rose calibrated to read as an extension of yellow-gold and rose-gold metal tones rather than a marketing alarm. Against the blush canvas the contrast ratio is deliberately intimate; this is a brand where "add to cart" feels like an invitation rather than a demand. A companion dusty-slate #676986 handles filter pill selections and secondary link states, its blue-lavender undertone maintaining cool tension with the warm neutral field. The broader palette maps to precious metals and gemstone adjacents: burnished sand (#e2c4ac), dusty rose (#e6c0b3), warm blush (#dba593), sage mist (#d4dcd0), and a deep navy-charcoal (#272d45) that anchors the footer and announcement bar in stark contrast to the body warmth. Corner radii follow jewelry-counter logic: product images and primary buttons sit at {rounded.none}, placing them in the same visual register as a ring box or folded tissue; filter chips and metal-swatch circles use {rounded.full}, mirroring the round forms of the pieces themselves. Spacing is generous — heroes breathe at {spacing.section}, product grids run at {spacing.xl} gutter. The Okendo review widget inherits star fills in the terracotta primary, maintaining tonal continuity across third-party social proof.

colors:
  primary: "#cb7f64"
  primary-active: "#b3674f"
  primary-disabled: "#e2c4ac"
  ink: "#191919"
  body: "#2b2f2e"
  muted: "#8f8f8f"
  muted-soft: "#a0a0a0"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#fff7f3"
  surface-soft: "#f6ede6"
  surface-warm: "#f1e2d7"
  surface-card: "#f7f7f8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  slate-accent: "#676986"
  slate-deep: "#272d45"
  blush-mid: "#dba593"
  blush-sand: "#e2c4ac"
  blush-rose: "#e6c0b3"
  sage-mist: "#d4dcd0"

typography:
  display-xl:
    fontFamily: "'Cormorant', 'Cormorant Garamond', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "'Cormorant', 'Cormorant Garamond', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Cormorant', 'Cormorant Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.22
    letterSpacing: 0.015em
  display-sm:
    fontFamily: "'Cormorant', 'Cormorant Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.28
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Tenor Sans', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Tenor Sans', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Tenor Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Tenor Sans', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Tenor Sans', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Tenor Sans', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  label-xs:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.12em
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
    padding: 14px 32px
    height: 48px
    border: none
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
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
    textDecoration: underline
  button-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    position: sticky
    top: 0
    zIndex: 100
  nav-utility-icon:
    color: "{colors.ink}"
    size: 20px
    gap: "{spacing.base}"
  announcement-bar:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    imageOverflow: hidden
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.primary}"
  product-card-price-original:
    typography: "{typography.price}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-card-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.none}"
    padding: 3px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.slate-accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.blush-sand}"
    textColor: "{colors.ink}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    minHeight: 600px
    textAlign: center
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    textColor: "{colors.ink}"
    paddingY: "{spacing.section}"
  category-nav-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    height: 44px
    overflowX: auto
  filter-chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 16px
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: 6px 16px
    height: 32px
  metal-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "2px solid transparent"
    outlineOffset: 2px
  ring-size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    size: 44px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    activeColor: "{colors.ink}"
    gap: "{spacing.sm}"
  review-stars:
    fillColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    size: 14px
  review-summary-bar:
    fillColor: "{colors.blush-mid}"
    trackColor: "{colors.hairline}"
    height: 4px
    rounded: "{rounded.full}"
  image-gallery-dot:
    activeColor: "{colors.ink}"
    inactiveColor: "{colors.hairline}"
    size: 6px
    rounded: "{rounded.full}"
  image-gallery-thumbnail:
    border: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    rounded: "{rounded.none}"
    size: 64px
  sticky-atc-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
    position: fixed
    bottom: 0
  footer:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    paddingY: "{spacing.xxl}"
  newsletter-input:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid rgba(255,255,255,0.4)"
    padding: 12px 16px
    height: 44px

## Components

### Buttons

**`button-primary`** — Flat terracotta #cb7f64 fill with zero corner radius, spaced uppercase Tenor Sans at 12px/0.15em tracking. Height is fixed at 48px with 32px horizontal padding; on hover the fill steps to `primary-active` (#b3674f) with no transition delay, matching the instant tactile feel of a physical toggle. The disabled state uses `primary-disabled` (#e2c4ac), a pale blush that reads as "softened" rather than "broken."

**`button-secondary`** — Transparent fill with a 1px `ink` (#191919) border and identical Tenor Sans uppercase type. The border-inset approach avoids layout shift between primary and secondary pairings on PDPs. Hover darkens the border to match a subtle focus ring.

**`button-ghost`** — Transparent, no border, `primary` text color with an underline decoration. Used for inline "view all," "read more," and breadcrumb-adjacent actions where a full button would overweight the reading flow.

**`button-pill` / `button-pill-active`** — Fully rounded lozenges (`{rounded.full}`) in surface-soft fill switching to ink fill when active. Used exclusively for filter chips, metal selectors, and content category toggles — never for primary conversion actions.

### Navigation

**`nav-bar`** — Sticky at 64px with `canvas` (#fff7f3) background and no bottom hairline, creating a seamless bleed into page content. Left-aligned logo, centered category links in `nav-link` (12px spaced uppercase Tenor Sans), and right-side utility row (search, wishlist, bag) with 20px icon targets spaced at `{spacing.base}`. The absence of a bottom border is intentional — the warm canvas bleeds from nav into hero with no seam.

**`announcement-bar`** — 36px deep `slate-deep` (#272d45) strip sitting above the nav, functioning as the velvet tray beneath the jewelry. Caption-scale spaced uppercase in white, single-line marquee text or static promotional copy.

**`category-nav-strip`** — 44px horizontal scroll strip below the hero on collection pages; muted gray links step to `ink` on active state. No underline indicator — the color shift alone signals selection. On mobile, scrollable with momentum scrolling and hidden scrollbar.

### Product Card

**`product-card`** — Transparent background, hard-edged (`{rounded.none}`) image container at 3:4 aspect ratio. On hover, the product image cross-fades to an alternate angle via opacity transition at ~300ms. Title runs `body-sm` Montserrat below the image, price runs `price` weight-500 Montserrat. The card has no shadow, border, or background fill — negative space and the warm page canvas do the framing work.

**`product-card-badge`** — Absolute-positioned flat chip at top-left, 3px/8px padding, zero radius. `badge-new` uses the distinctive slate-accent (#676986) fill — the only place this color appears as a background rather than text, making newness immediately readable against warm-toned imagery. `badge-bestseller` uses blush-sand (#e2c4ac).

### Product Detail

**`metal-swatch`** — 24px circles (`{rounded.full}`) filled with the actual metal color (filled by JS from product variant data). Active state adds a 2px `ink` border with 2px offset gap, creating a selection halo that reads clearly without obscuring the swatch color.

**`ring-size-selector`** — 44px square tiles with 1px hairline border, switching to `ink` fill and `on-dark` text on selection. Zero radius keeps the selector aligned with the card and button aesthetic — no softening here.

**`sticky-atc-bar`** — Fixed-bottom bar appearing after the primary CTA scrolls out of viewport. Holds product name (`display-sm` Cormorant), price, and a full-width `button-primary` within the `canvas` background. Top hairline border is the only visual boundary.

### Review System

**`review-stars`** — 14px fills in `primary` (#cb7f64), carrying the terracotta into the social proof layer. `review-summary-bar` uses a 4px fully-rounded track in `blush-mid` (#dba593) fill, so the review distribution chart reads as warm and brand-aligned rather than default gray.

### Footer

**`footer`** — Deep `slate-deep` (#272d45) background provides the maximum contrast break at page end. Column headers in `title-sm` Tenor Sans uppercase; links in `caption` scale. The dark field creates a visual anchor that grounds the warm, light-dominant page above it — a jeweler's black cloth beneath the tray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen drawer; hero text stacks above image with reduced `display-lg` heading; `sticky-atc-bar` always visible; `category-nav-strip` horizontally scrollable |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + 3 primary category links + utility icons; hero runs 50/50 image-text split |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with mega-menu dropdowns; `filter-chip` row visible inline on collection pages |
| Wide | > 1440px | Max-width container (~1400px) centered; grid stays at 4 columns; hero images expand to bleed edge with content constrained to inner grid |

### Touch Targets

- `ring-size-selector` tiles: 44px minimum — already spec'd, do not reduce for density
- `metal-swatch` circles: bump to 36px diameter on mobile (desktop is 24px)
- `nav-utility-icon` hit area: 44×44px with negative-margin expansion even though visual icon is 20px
- `filter-chip` height: minimum 44px on mobile despite 32px desktop spec
- Swipe gestures on `image-gallery` override tap targets — ensure 10px dead zone at image edge prevents accidental swipe during scroll

### Collapsing Strategy

- Nav mega-menu collapses to full-screen slide-over drawer at < 1128px; secondary nav categories demoted to drawer accordion
- `category-nav-strip` transitions from inline pill row to horizontal scroll with momentum; active chip scrolled into view on page load
- Hero layout shifts from side-by-side (tablet+) to stacked image-over-text on mobile; heading scale drops from `display-xl` to `display-lg`
- Filter sidebar (if present on desktop) collapses to bottom sheet on mobile, triggered by a filter icon button in the fixed utility bar
- Footer 4-column link grid collapses to single-column accordion on mobile; `slate-deep` background maintained at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact mega-menu structure and hover animation timings not extractable from static crawl
- Product card hover transition duration and easing curve (image swap timing) not confirmed
- Whether the primary button uses a subtle background transition or an instant color swap on hover — no computed animation data available
- Ring-size guide modal design (dimensions, overlay color, typography scale) not observed
- Loyalty / piercing-studio booking UI components not captured
- Cart drawer vs. dedicated cart page routing — Shopify theme variant unclear from static hints
- Exact Okendo review widget override CSS depth (whether star color is truly `#cb7f64` or a close match injected via widget config)
- `#ffcf2a` (bright yellow) and `#b2f9e9` (mint) appear in extracted palette but no clear component usage observed — likely campaign-specific or badge/promo overrides not present during crawl
- `#0e7a82` (teal) similarly isolated in palette; possible gift-wrap or sustainability badge accent
