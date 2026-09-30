---
version: alpha
name: "Rad Power Bikes"
source_url: "https://www.radpowerbikes.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single marigold-amber — #fcbc3d — does the work that most vehicle brands spread across an entire primary/secondary/tertiary palette: it appears on every CTA button, category tab highlight, price-accent chip, and configurator swatch, anchoring a storefront that sells $1,500–$2,000 electric bikes with the warmth of outdoor gear rather than the clinical sheen of automotive tech. The canvas is not pure white but #faf9f5, a faint cream that makes product photography read like print catalog pages; ink is near-black #282a2c rather than true black, softening the contrast just enough to feel approachable. Marfa, a geometric sans-serif with humanist apertures, is the sole typeface — all hierarchy is built from weight and size contrast alone, with display headlines sitting wide and confident at 56px/700 weight while spec labels drop to 11px uppercase for stat-dense comparison rows. Corners are consistently 8px across buttons, inputs, and product cards — modern without going fully pill-shaped. Burnt orange (#cb4e17) and coral (#f3743c) are reserved for urgency surfaces: sitewide sale banners, low-stock alerts, countdown timers. A disciplined teal (#078466) handles positive confirmation states — in-stock dots and checkout success marks — without expanding into a second brand color. The primary amber has a formal warm tint ramp stepping through #ffca60, #fddd9e, and #fff8ec for hover washes, disabled states, and promotional fills. Dark grays (#404040, #4a4e52) carry secondary body copy and spec metadata, keeping the color energy focused on the amber-anchored CTA system rather than dispersed across the grid.

colors:
  primary: "#fcbc3d"
  primary-hover: "#ffca60"
  primary-active: "#e8a820"
  primary-disabled: "#fddd9e"
  primary-wash: "#fff8ec"
  primary-wash-mid: "#fef2d8"
  primary-wash-strong: "#feebc5"
  accent-orange: "#cb4e17"
  accent-coral: "#f3743c"
  accent-teal: "#078466"
  accent-red: "#d32027"
  accent-red-dark: "#b52025"
  ink: "#282a2c"
  body: "#404040"
  muted: "#808080"
  dark-mid: "#4a4e52"
  hairline: "#dedede"
  hairline-soft: "#e7e7e7"
  canvas: "#faf9f5"
  surface-soft: "#f1efe5"
  surface-card: "#f3f1f2"
  on-primary: "#282a2c"
  on-dark: "#faf9f5"

typography:
  display-xl:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  spec-label:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.2px
  button-lg:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  button-md:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'Marfa', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    padding: 14px 28px
    height: 52px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 52px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 52px
  button-cta-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 18px 40px
    height: 60px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1.5px solid {colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 12px rgba(40,42,44,0.10)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    boxShadow: "0 8px 32px rgba(40,42,44,0.14)"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    overflow: hidden
    imageAspectRatio: "4 / 3"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    color: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 600px
    layout: full-bleed with centered text overlay
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.title-lg}"
    color: "{colors.on-dark}"
    opacity: 0.85
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 18px 40px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  sale-banner:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  spec-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 5px 10px
  spec-grid:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    layout: "2-column grid on desktop, 1-column on mobile"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    valueColor: "{colors.ink}"
  range-stat-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    statTypography: "{typography.display-sm}"
    statColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
  in-stock-badge:
    backgroundColor: transparent
    textColor: "{colors.accent-teal}"
    typography: "{typography.spec-label}"
    dotColor: "{colors.accent-teal}"
  low-stock-badge:
    backgroundColor: transparent
    textColor: "{colors.accent-orange}"
    typography: "{typography.spec-label}"
    dotColor: "{colors.accent-orange}"
  color-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border-inactive: "2px solid transparent"
    border-active: "2px solid {colors.ink}"
    margin: "{spacing.xs}"
  promo-badge:
    backgroundColor: "{colors.primary-wash}"
    textColor: "{colors.accent-orange}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sticky-buy-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    position: fixed
    bottom: 0
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  category-pill-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Amber (#fcbc3d) fill with near-black ink text, pairing for accessible contrast without defaulting to white-on-color convention. On hover it brightens to #ffca60; on press the surface cools to #e8a820. Disabled primaries pull from the pale-amber tint ramp at #fddd9e with muted gray text. Used on all shop, configure, and add-to-cart CTAs across the site.

**`button-secondary`** — A 2px near-black outline button on the cream canvas, inverting to filled ink (#282a2c) with cream text on hover. Appears alongside the primary CTA on product detail pages where two actions share a row (e.g., "Shop Now" / "Compare Models"). Height and padding match the primary for clean side-by-side pairing.

**`button-ghost-light`** — The same outline treatment reversed to white-on-dark, used inside hero sections and sale banners where an ink border would disappear into the background. Common on full-bleed hero overlays and the announcement bar CTA link.

**`button-cta-lg`** — Oversized 60px amber button for primary page conversions. Typography steps up to `{typography.button-lg}` (18px/600 weight). Used at the bottom of PDP hero sections and inside the sticky buy bar for thumb-reachable checkout entry.

**`category-pill-active`** / **`category-pill-inactive`** — Pill-shaped filter chips for the shop category rail. Active state fills amber; inactive sits on soft surface gray. Used to filter models by ride type (City, Cargo, Off-Road).

### Navigation
**`nav-bar`** — A 72px cream bar with logo left, utility icons (search, account, cart) right, and full-width category dropdowns in the center. On scroll it acquires a soft shadow without any color shift. On mobile the height reduces to 60px and the category links collapse behind a hamburger icon.

**`nav-dropdown`** — Mega-menu panels with product thumbnail grids alongside category link columns. Cards show model image, name, and starting price. The dropdown opens on hover/focus; there is no underline or indicator on the parent tab — the opening panel is the affordance. `{rounded.md}` container with a pronounced box-shadow to lift it off the page.

### Product Cards
**`product-card`** — White card with 1px soft hairline border and `{rounded.sm}` (8px) radius, set on a cream background grid. Image is full-bleed at 4:3 aspect ratio. Below: model name in `{typography.title-md}`, price in `{typography.price-display}`, and a horizontal row of spec-pill chips for range, speed, and payload. On hover the card lifts with a 12px blur shadow and the image scales to 103%.

**`product-card-badge`** — Amber pill in `{typography.spec-label}` uppercase for "BEST SELLER", "NEW", or sale callouts. Positioned absolute top-left over the product image with 12px inset.

### Hero
**`hero-section`** — Full-bleed near-black (#282a2c) or lifestyle photography background with centered or left-aligned headline stack. The CTA is always the amber `hero-cta` button. Text overlay uses `on-dark` (#faf9f5) at full opacity for headlines and 85% opacity for subheads. On mobile the hero collapses to stacked text-above-image layout with the headline reduced to `{typography.display-md}`.

### Spec & Range Display
**`spec-grid`** — A 2-column label/value grid on warm soft surface (#f1efe5), used inside the "Key Specs" accordion on PDPs. Labels in `{typography.spec-label}` (11px uppercase, 600 weight) in muted gray; values in `{typography.body-md}`. Collapses to 1-column on mobile with alternating surface-tinted rows for scannability.

**`range-stat-card`** — Spotlight stat cards used in mid-page feature sections: large number (e.g., "45 mi") in `{typography.display-sm}`, unit or descriptor label in `{typography.spec-label}` below. White card with hairline border. Rendered in 3–4 column rows on desktop, 2-column on tablet, single-column on mobile.

**`spec-pill`** — Small uppercase chips in `{typography.spec-label}` on soft surface background. Used inside product cards and comparison rows to surface key numbers — range, top speed, max load — at grid density.

### Badges & Status
**`in-stock-badge`** — Teal text (#078466) with a small preceding filled dot. No background fill — typography-only badge signaling availability in cart, PDP, and shop grid rows.

**`low-stock-badge`** — Same format, color swapped to accent-orange (#cb4e17). Triggers at a defined inventory threshold to create purchase urgency without aggressive visual disruption.

**`sale-banner`** — Full-width burnt-orange (#cb4e17) bar pinned above the nav bar. Off-white text in `{typography.button-md}` centered. Used for sitewide promotions; a dismiss control appears at the right edge.

**`announcement-bar`** — Near-black version of the site-wide top bar for shipping thresholds, new-model announcements, and non-promotional messages. Same geometry as the sale-banner but in `{colors.ink}` background to signal informational rather than urgency content.

**`promo-badge`** — Inline pale-amber wash (#fff8ec) background with terracotta text for contextual savings callouts ("Save $300") on product cards and comparison rows. Softer than the sale-banner — designed to coexist with product imagery without competing for attention.

### Customization
**`color-swatch`** — 32px circular swatches in a horizontal wrap row. Inactive: no visible ring (transparent border). Active: 2px solid ink ring at `{rounded.full}` with 2px outline-offset gap. Used on the PDP color selector, comparison grid rows, and the swatch quick-view on product cards.

### Sticky Buy Bar
**`sticky-buy-bar`** — Fixed to viewport bottom on PDPs, appearing once the hero CTA scrolls out of view. Displays model name, selected color chip, price in `{typography.price-display}`, and the full amber `button-cta-lg`. Cream background (#faf9f5) with a top hairline separator. Hidden on desktop until scroll threshold; always visible on mobile PDP.

### Footer
**`footer`** — Near-black (#282a2c) background with cream body text and muted gray (#808080) links. Four-column link grid on desktop (Bikes, Support, Company, Social), collapsing to tap-to-expand accordions on mobile. All link text in `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero collapses to stacked text-above-image; nav reduces to logo + hamburger + cart icon; sticky buy bar always visible; spec-grid becomes 1-column; range-stat-cards stack vertically; color swatch row wraps |
| Tablet | 744–1128px | 2-column product grid; nav shows logo and compact horizontal links or hamburger; hero uses landscape crop with left-aligned text overlay; range-stat-cards in 2×2 grid |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with mega-menu dropdowns; hero full-bleed with centered overlay; range-stat-cards in 4-column row; spec-grid 2-column |
| Wide | > 1440px | Content column caps at 1440px max-width, centered; hero photography extends edge-to-edge behind a constrained text and CTA column |

### Touch Targets
- All primary and secondary buttons are minimum 52px tall
- `button-cta-lg` and sticky buy bar CTA are 60px tall for thumb-zone reach
- Color swatches are 32px with `{spacing.xs}` margins yielding 40px effective tap region
- Nav hamburger and utility icons are 44×44px touch targets
- Product card entire surface is tappable as a single link

### Collapsing Strategy
- Desktop 4-column range-stat-card rows → 2×2 grid on tablet → single-column stacked on mobile
- Nav mega-menu dropdown → full-screen slide-in drawer panel behind hamburger on mobile
- Spec-grid 2-column → 1-column with alternating tinted rows on mobile
- Footer 4-column link grid → stacked tap-to-expand accordions on mobile with hairline dividers between sections
- Announcement and sale banners persist across all breakpoints at reduced horizontal padding
- Category pill rail on shop page becomes horizontally scrollable on mobile rather than wrapping to multiple rows

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Primary hover (#ffca60) is mapped from the extracted palette; pressed/active state (#e8a820) is derived at 10% luminance reduction — not directly extracted from computed CSS
- Only one font family (Marfa) was detected; no variable axis data, optical sizing variants, or exact weight integer values were available — weight values estimated from DTC e-commerce conventions
- No explicit border-radius tokens were confirmed from CSS; 8px (sm) for interactive elements is inferred from visual appearance
- Exact nav height, sticky-bar height, and breakpoint trigger offsets not available from static extraction
- Animation durations and easing curves (hover transitions, dropdown timing, scroll-triggered reveals) not extractable from static page inspection
- No dark mode or alternate theme detected; single warm light-mode surface system assumed throughout
- Flag-palette colors (#0052b4 US blue, #b31942 US red, #0a3161 US navy) appear in the extracted set but their UI role is unclear — likely used in a country/region selector or nationality badge component rather than brand surfaces; excluded from the primary color system
- Exact font loading mechanism (self-hosted vs. third-party CDN) for Marfa not confirmed; fallback stack may need adjustment based on licensing
