---
version: alpha
name: "Jazz Messengers"
source_url: "https://www.jazzmessengers.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three bold chords define the palette before a note plays — an emerald #00b87c that presses through the grid like a highlight marker across a club setlist, a sapphire #0067b8 carrying authority without the cold of corporate blue, and a coral #ff6666 landing exactly where heat is needed: a sold-out badge, a price alert, an impulse buy. The system runs on system-level Arial rather than a commissioned typeface, a choice that reads less like budget constraint and more like function-first record-store pragmatism — the same legibility as a handwritten bin card, rendered on a desktop product listing. PingFang SC in the font stack signals a Chinese-market presence, pointing to a store that treats Asia-Pacific listeners as a primary audience rather than an afterthought.

  Cards arrive at `{rounded.sm}` — enough softness to feel digital, not enough to feel decorative. The canvas stays white and the surface system deploys two quiet gray grades to separate sections without visual weight. Green takes the action layer: primary buttons, in-stock indicators, active genre pills, and filter chips all draw from `{colors.primary}`. Blue rotates in as the informational register — artist biography links, pagination controls, external streaming callouts. Coral handles urgency and negative states exclusively — its saturation is high enough that overuse tips the register into alarm, so the system reserves it for limited-edition alerts, sale pricing, and low-stock warnings only.

  Spacing is tight at the component level — 8–12px internal padding in chips and badges — then opens into 48–64px breathing room between catalog rows and editorial strips. Navigation is flat: a horizontal top bar carries genre links, a search input, and a cart icon. No mega-menu, no accordion. The catalog runs a responsive grid collapsing from four columns at wide desktop down to two on mobile, with card image ratios locked at 1:1 — the square vinyl cover convention applied across all digital formats. The footer darkens the canvas to near-black and lets the green reappear as a link accent, closing the visual loop with the same primary that opened it.

colors:
  primary: "#00b87c"
  primary-active: "#009e68"
  primary-disabled: "#99dfc2"
  accent-blue: "#0067b8"
  accent-blue-active: "#00519a"
  accent-coral: "#ff6666"
  accent-coral-active: "#e84f4f"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-blue: "#ffffff"
  on-dark: "#ffffff"
  stock-low: "#ff6666"
  badge-new: "#0067b8"
  badge-sale: "#ff6666"
  footer-bg: "#111111"
  footer-divider: "#333333"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'PingFang SC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
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
    border: "1px solid {colors.hairline}"
    padding: 9px 19px
    height: 40px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 8px 12px
    height: 38px
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    focusBackground: "{colors.canvas}"
    padding: 8px 12px
    height: 38px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    linkActiveColor: "{colors.primary}"
    linkHoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    artistTypography: "{typography.body-sm}"
    artistColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    padding: "{spacing.md}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.08)"
  genre-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-stock-low:
    backgroundColor: "{colors.stock-low}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  price-block:
    currentPriceTypography: "{typography.price-display}"
    currentPriceColor: "{colors.ink}"
    salePriceColor: "{colors.accent-coral}"
    originalPriceTypography: "{typography.price-original}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
  catalog-grid:
    columns: 4
    gap: "{spacing.base}"
    paddingHorizontal: "{spacing.lg}"
    backgroundColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.hairline}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 400px
    imageOverlay: "rgba(0,0,0,0.45)"
  artist-spotlight:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    linkHoverColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    dividerColor: "{colors.footer-divider}"
    legalTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The core purchase action: 40px tall, `{rounded.xs}` corners, emerald `{colors.primary}` (#00b87c) fill with white text in `{typography.button-md}` (bold 14px). Used for Add to Cart, Checkout, and Subscribe. Hover deepens to `{colors.primary-active}` (#009e68); the disabled state bleaches to `{colors.primary-disabled}` without altering opacity.

**`button-secondary`** — White canvas with a `{colors.hairline}` border, ink text, identical height and padding to the primary for side-by-side grid alignment. Serves wishlist, preview-listen, and back-navigation roles where the green primary would compete with a nearby CTA.

**`button-ghost`** — Transparent fill, `{colors.primary}` border and text, for tertiary actions inside filter sidebars and modal footers. Keeps the green accent present at lower visual weight.

**`button-accent-blue`** — Sapphire `{colors.accent-blue}` (#0067b8) for informational or outbound CTAs: streaming platform links, label pages, artist interviews. Strictly separated from purchase flows to avoid color-function confusion.

### Text Input & Search

**`text-input`** — 38px, white canvas, `{rounded.xs}`, `{colors.hairline}` border that transitions to `{colors.primary}` on focus — the green focus ring mirrors the primary CTA register and confirms intent. Placeholder text in `{colors.muted}`.

**`search-bar`** — Rendered inline in the nav bar on a `{colors.surface-soft}` background. A magnifier icon at `{colors.muted}` left-anchors the field. On focus, the border upgrades to `{colors.primary}` and the background lifts to white canvas. On mobile, the search collapses behind a magnifier icon that opens a full-drawer input.

### Navigation

**`nav-bar`** — 56px, white, `{colors.hairline}` bottom border. Genre links use `{typography.nav-link}` (600-weight Arial 14px) and shift to `{colors.primary}` on hover or active state. Logo anchors left; search bar sits center-left; cart icon and account controls sit right. No mega-menu — hover reveals a flat, single-column dropdown list only. The nav stays sticky on scroll.

### Product Cards

**`product-card`** — Square 1:1 image at top, card body below carrying title in `{typography.title-sm}`, artist name in `{typography.body-sm}` at `{colors.muted}`, and price block beneath. Overlapping badge stack (`badge-sale`, `badge-new`, `badge-stock-low`) floats top-left over the image corner. Cards lift with `0 4px 12px rgba(0,0,0,0.08)` on hover. The 1:1 image ratio is non-negotiable — it enforces the vinyl cover convention across CDs, digital downloads, and merchandise.

### Genre Pills

**`genre-pill`** — `{rounded.full}` chips for genre browsing: Bebop, Modal, Free Jazz, Fusion, Latin, Contemporary, Avant-Garde. Inactive: `{colors.surface-soft}` background, `{colors.body}` text, `{colors.hairline}` border. Active: `{colors.primary}` fill, white text. Rendered as a horizontally scrollable strip below the nav bar on all viewport widths.

### Badges

**`badge-sale`** — Coral `{colors.badge-sale}` (#ff6666) rectangle tag for price promotions. `{typography.label-sm}` uppercase, 2px × 6px padding, `{rounded.xs}`. Floats over product card image.

**`badge-new`** — Sapphire `{colors.badge-new}` (#0067b8) for recent arrivals, using identical sizing. Color distinction from `badge-sale` prevents conflation of sale and newness signals.

**`badge-stock-low`** — Reuses coral `{colors.stock-low}` for inventory alerts. Copy reads "LAST FEW" or a unit count ("2 LEFT"). Displayed on both card overlay and product detail page near the add-to-cart button.

### Price Block

**`price-block`** — Current price in `{typography.price-display}` (20px/700) at `{colors.ink}`. When on sale, current price shifts to `{colors.accent-coral}` and original price renders in `{typography.price-original}` with line-through at `{colors.muted}`. No badge duplication — the price color change carries the sale signal; the `badge-sale` appears only on the card.

### Hero Banner

**`hero-banner`** — Dark `{colors.ink}` canvas with full-bleed artist photography behind a 45% black overlay, minimum 400px tall. Title in `{typography.display-xl}` (bold 36px), subtitle in `{typography.body-md}` at `{colors.hairline}` for legibility over dark imagery. Primary CTA uses emerald `{colors.primary}` fill at `{rounded.xs}`. Used for new release announcements, label spotlights, and festival editorial features.

### Artist Spotlight

**`artist-spotlight`** — Off-white `{colors.surface-soft}` section breaking up the catalog grid. Title in `{typography.display-md}`, body copy in `{typography.body-md}` at `{colors.body}`. A green `{colors.primary}` left-border accent or underline rule marks the section header. Contains a read-more link using `button-ghost` or an inline text link at `{colors.accent-blue}`.

### Footer

**`footer`** — Near-black `{colors.footer-bg}` (#111111) ground, white body text, `{colors.primary}` link accents. The green that drives the action layer at the top of the page reappears here as the only active color against dark — a deliberate echo. Five-column link grid: About, Genres, Labels, Help, Social. Legal line in `{typography.caption}` at 60% opacity.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Catalog at 2 columns; genre pills scroll horizontally; nav collapses to hamburger + logo + cart; hero shrinks to 260px with stacked text; search moves into hamburger drawer |
| Tablet | 744–1128px | Catalog at 3 columns; nav shows top-level genre links, hides secondary items; search bar full-width in a strip below nav |
| Desktop | 1128–1440px | Catalog at 4 columns; full inline nav with genre links and search bar; hero at 400px with side-by-side text and image variant available |
| Wide | > 1440px | Grid max-width 1440px with expanding gutters; hero can extend to 560px; `{typography.display-xl}` may scale to 42px |

### Touch Targets

- All buttons minimum 40px tall; primary CTAs expand to 44px on mobile
- Genre pill chips minimum 36px tall on mobile with 10px vertical padding
- Product card tap zone covers the full card surface, not just the image
- Nav icons hold a minimum 44 × 44px tap area regardless of rendered icon size

### Collapsing Strategy

- Genre filter strip moves from optional sidebar (desktop) to mandatory horizontal pill scroll (tablet and mobile)
- Four-column grid collapses 4 → 3 → 2; single-column reserved for artist biography detail pages only
- Search collapses to a magnifier icon trigger on mobile, revealing a full-width drawer input
- Footer five-column grid collapses to two-column stacked layout on tablet, single-column accordion on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface detected — system stack (Arial / Helvetica / PingFang SC) may not reflect a licensed font loaded via JavaScript or a CDN with bot protection in place
- Only three hex values extracted; shadow depths, overlay tints, hover states, and dark-mode surface tokens are derived from convention, not measured from the live site
- No `meta theme-color` tag found — true canvas color and any dark-mode primary values are unconfirmed
- Exact button radii, input heights, and card padding are estimated from genre-store norms, not pixel-measured
- Whether the store offers a dark-mode toggle or operates exclusively in light-mode is unknown
- PingFang SC in the font stack suggests Chinese-locale support; whether RTL languages or other locale-specific layout variants are active is not documented
- Platform is not Shopify — checkout and cart UI tokens may deviate significantly from the catalog styling documented here
- No imagery CDN or color-naming convention detected; illustration or icon style (if any) is undocumented
