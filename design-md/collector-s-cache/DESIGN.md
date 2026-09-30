---
version: alpha
name: "Collector's Cache"
source_url: "https://www.collectorscache.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's marketplace that wears its inventory's patina in its palette — the deep #1a1718 of a well-handled card sleeve, the tarnished gold of #a58e4a on a vintage booster pack, and the urgent #cd0a0a of a "Buy Now" button that reads like a red sticker slapped on a display case. The site is a dark, dense grid of product tiles on a #222222 canvas, each card image floating on a #302b2c surface-card with a subtle #363636 hairline. Typography runs Arial at modest weights — there is no hero type, no display face, no brand voice beyond the functional: "Add to Cart" and "View Details" in 14px body-sm. The navigation is a persistent top bar of #212121 with a gold-accented logo and a search field that opens into a full-screen overlay, the only moment the canvas goes to #111111. Badges for "Hot" and "Sold" use #cd0a0a and #b21f0f, while condition labels ("NM", "LP", "HP") sit in #5a6572 chips. The checkout flow introduces #146ff8 links and #f38300 sale tags, but the core experience is a monochrome stage for high-res card scans — the brand's real design move is getting out of the way.

colors:
  primary: "#cd0a0a"
  primary-active: "#b21f0f"
  primary-disabled: "#fef1ec"
  ink: "#1a1718"
  body: "#222222"
  muted: "#555555"
  muted-soft: "#9e9e9e"
  hairline: "#363636"
  hairline-soft: "#474040"
  canvas: "#222222"
  surface-soft: "#302b2c"
  surface-card: "#302b2c"
  on-primary: "#ffffff"
  gold-accent: "#a58e4a"
  gold-light: "#dfbd6b"
  gold-soft: "#fcefa1"
  condition-badge: "#5a6572"
  condition-badge-text: "#fbf9ee"
  hot-badge: "#cd0a0a"
  sold-badge: "#b21f0f"
  sale-tag: "#f38300"
  sale-tag-soft: "#de6227"
  link: "#146ff8"
  scrim: "#111111"
  surface-overlay: "#111111"
  card-border: "#363636"
  card-border-hover: "#a58e4a"

typography:
  display-xl:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0px
  display-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  title-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  title-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  body-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  caption-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0px
  badge:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0px
  button-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0px
  button-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  link:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  nav-link:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0px

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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-gold:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.gold-accent}"
  search-input:
    backgroundColor: "{colors.surface-overlay}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    textColor: "{colors.gold-accent}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px
  product-card-hover:
    border: 1px solid "{colors.card-border-hover}"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.gold-accent}"
  condition-badge:
    backgroundColor: "{colors.condition-badge}"
    textColor: "{colors.condition-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hot-badge:
    backgroundColor: "{colors.hot-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sold-badge:
    backgroundColor: "{colors.sold-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sale-tag:
    backgroundColor: "{colors.sale-tag}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.base}"
  search-overlay:
    backgroundColor: "{colors.surface-overlay}"
    textColor: "{colors.body}"
    padding: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action on product detail pages and in the cart. Uses `{colors.primary}` (#cd0a0a) for a high-contrast red that stands out against the dark `{colors.canvas}`. On hover, shifts to `{colors.primary-active}` (#b21f0f). Disabled state uses `{colors.primary-disabled}` (#fef1ec) with `{colors.muted}` text. Height is 40px with `{rounded.sm}` corners.

**`button-secondary`** — Used for "View Details" and "Add to Watchlist" actions. Rests on `{colors.surface-card}` (#302b2c) with `{colors.body}` (#222222) text. Same 40px height and `{rounded.sm}` as primary, but no background color change on hover — instead, a subtle `{colors.hairline}` border appears.

**`button-ghost`** — Text-only button for "Clear Filters" and "Cancel" in modals. Transparent background, `{colors.muted-soft}` (#9e9e9e) text at `{typography.button-sm}` size. Hover state adds a `{colors.hairline-soft}` underline.

**`button-gold`** — Used for premium actions like "Make Offer" or "Bid Now". Uses `{colors.gold-accent}` (#a58e4a) background with `{colors.ink}` (#1a1718) text. Same dimensions as `button-primary`.

### Cards
**`product-card`** — The core inventory unit. A `{colors.surface-card}` (#302b2c) container with `{rounded.md}` (8px) corners and 8px padding. The card image sits in a `{colors.surface-soft}` (#302b2c) area with `{rounded.sm}` (4px). Below, the title uses `{typography.title-sm}` (14px/600) and the price uses `{typography.price}` (18px/700) in `{colors.gold-accent}`. On hover, a 1px `{colors.card-border-hover}` (#a58e4a) border appears around the card.

**`condition-badge`** — A small chip for card condition (NM, LP, MP, HP, DMG). Uses `{colors.condition-badge}` (#5a6572) background with `{colors.condition-badge-text}` (#fbf9ee) text. `{typography.badge}` (11px/700/uppercase) with `{rounded.xs}` (2px) and 2px/6px padding.

**`hot-badge`** — Red badge for trending items. `{colors.hot-badge}` (#cd0a0a) background, white text. Same typography and sizing as condition-badge.

**`sold-badge`** — Darker red badge for sold-out items. `{colors.sold-badge}` (#b21f0f) background, white text.

**`sale-tag`** — Orange tag for discounted items. `{colors.sale-tag}` (#f38300) background with `{colors.ink}` (#1a1718) text. Slightly wider padding (2px/8px) for emphasis.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height on `{colors.canvas}` (#222222). Contains the brand logo (gold-accented text), nav links, and a search icon. The bar uses `{typography.nav-link}` (14px/600) for all text items.

**`nav-link`** — Inactive links use `{colors.muted-soft}` (#9e9e9e) with 8px/12px padding. Active or hover state shifts to `{colors.gold-accent}` (#a58e4a). No underline or background change — color is the only signal.

**`search-overlay`** — A full-screen overlay triggered by the search icon. Background is `{colors.surface-overlay}` (#111111) with `{spacing.xl}` (32px) padding. The search input inside uses `{typography.body-md}` (16px/400) with a `{colors.hairline}` (#363636) bottom border.

### Forms
**`text-input`** — Standard input for checkout forms and filters. `{colors.surface-card}` (#302b2c) background, `{colors.body}` (#222222) text, 1px `{colors.hairline}` (#363636) border. On focus, the border shifts to `{colors.gold-accent}` (#a58e4a). Height is 40px with `{rounded.sm}` (4px).

### Footer
**`footer`** — A dark footer on `{colors.canvas}` (#222222) with `{colors.muted}` (#555555) text at `{typography.caption}` (12px/400). Links use `{colors.muted-soft}` (#9e9e9e). Padding is `{spacing.xl}` (32px) vertical, `{spacing.base}` (16px) horizontal.

### Hero
**`hero-banner`** — A full-width banner on category pages and the homepage. Background is `{colors.surface-soft}` (#302b2c) with `{typography.display-md}` (22px/600) text. Padding is `{spacing.section}` (64px) vertical, `{spacing.base}` (16px) horizontal. No image background — relies on product grid below for visual interest.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger, search overlay is full-screen, hero banner reduces to 32px padding |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, search overlay is a dropdown panel |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, search overlay is a centered modal |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, search overlay remains centered modal |

### Touch Targets
- All buttons and interactive elements: minimum 40px height (primary, secondary, ghost)
- Nav links: 44px touch area (padding + height)
- Search icon: 48px touch area
- Product card images: tap-to-zoom on mobile

### Collapsing Strategy
- Nav links collapse into hamburger menu below 744px
- Search bar collapses to icon-only on mobile, expands to full input on tap
- Product grid collapses from 4 columns to 1 column on mobile
- Footer links collapse into accordion sections on mobile
- Hero banner text reduces from display-md to title-md on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (button-secondary, button-ghost, text-input) could not be reliably extracted from the live site — the extracted CSS may not include all pseudo-class styles
- Error styling for form inputs (red border, error text) is not present in the extracted data
- Dark mode is not applicable — the brand already uses a dark canvas as default
- Sub-brand palettes (e.g., for specific TCGs like Pokémon, Magic, Yu-Gi-Oh!) are not captured — the site may use game-specific accent colors that were not extracted
- The extracted hex list includes many grays and a few accent colors — the brand's true primary is likely #cd0a0a (red) based on its use in buttons and badges, but this is an inference from component context, not a confirmed design token
- Font-family declarations only show Arial, FontAwesome, Keyrune, Verdana, sans-serif — Keyrune is a Magic: The Gathering icon font, suggesting the site uses custom iconography for card symbols, but the exact implementation is unknown
- Animation and transition timings (hover fades, modal open/close) are not extracted
- The checkout flow may use Shopify's default styling — extracted colors may include Shopify Pay widget colors that are not part of the brand's design system
