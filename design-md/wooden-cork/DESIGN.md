---
version: alpha
name: "Wooden Cork"
source_url: "https://woodencork.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A strand of gold (#cc9f53) threads through every significant moment on Wooden Cork — appearing in price callouts, featured-bottle highlights, and hover accents — bridging the deep-oak darkness of the canvas (#0d0b09, #1c1712) with warm cream surfaces (#f6efe2, #fcf4f1). The primary red, #ba4444, carries every principal CTA and navigation highlight, with #9d1e1e as the pressed state and #d73030 signaling urgency in discount ribbons and stock alerts. Arpona, a display serif with old-world editorial weight, sets Wooden Cork apart from the grotesque stacks common across Shopify liquor stores — its bracketed serifs read like ink printed directly on a label rather than pixels rendered on a screen. The resulting palette reads as the interior of a premium bottle shop at closing hour: near-black warmth in the shell (#0d0b09, #1c1712), crimson voltage on the signage, candlelight gold on featured items, and cream paper (#f6efe2, #fcf4f1) where product copy lives. Corner radii stay tight throughout — `{rounded.xs}` on buttons, `{rounded.sm}` on cards — rejecting the pill-shaped softness of mass-market beverage brands in favor of something closer to a catalog or auction house print aesthetic. The dark navy #263644 surfaces in footer regions and alternate section backgrounds, lending maritime depth suited to whisky provenance storytelling. Small uppercase Arpona badge tags in `{colors.accent-gold}` on dark backgrounds or `{colors.ink}` on cream carry the physical price-sticker logic of a brick-and-mortar wine shop onto the digital shelf — vintage year, proof, and region compressed into a single composable label unit.

colors:
  primary: "#ba4444"
  primary-active: "#9d1e1e"
  primary-hover: "#d73030"
  primary-disabled: "#d4a0a0"
  accent-gold: "#cc9f53"
  accent-cream: "#f3efa1"
  accent-navy: "#263644"
  ink: "#0d0b09"
  body: "#1c1712"
  muted: "#303030"
  muted-soft: "#0f0f0f"
  hairline: "#dedede"
  hairline-soft: "#e8e8e1"
  canvas: "#fcf4f1"
  surface-soft: "#f2f2f2"
  surface-card: "#f6efe2"
  surface-warm: "#e8e8e1"
  dark-canvas: "#1c1712"
  dark-deep: "#0d0b09"
  dark-section: "#131e29"
  on-primary: "#ffffff"
  on-dark: "#f6efe2"

typography:
  display-xl:
    fontFamily: "'Arpona', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge-label:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arpona', Georgia, serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1.5px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.dark-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid rgba(204,159,83,0.25)"
    logoAccentColor: "{colors.accent-gold}"
  nav-bar-scrolled:
    backgroundColor: "{colors.dark-canvas}"
    borderBottom: "2px solid {colors.accent-gold}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBorderRadius: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 16px rgba(186,68,68,0.15)"
  hero:
    backgroundColor: "{colors.dark-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "rgba(13,11,9,0.6)"
    minHeight: 520px
  section-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
  section-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
  age-gate-modal:
    backgroundColor: "{colors.dark-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-gold}"
  vintage-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  provenance-badge:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.accent-gold}"
    border: "1px solid {colors.accent-gold}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.muted}"
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  price-tag:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
  price-tag-original:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  footer:
    backgroundColor: "{colors.dark-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-gold}"
    borderTop: "2px solid {colors.accent-gold}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The main crimson CTA (#ba4444) carries white Arpona type at 15px/600 weight with 0.5px tracking, tight `{rounded.xs}` corners, and 12px 28px padding yielding a 44px height. Hover lifts to #d73030 (`{colors.primary-hover}`), press deepens to #9d1e1e (`{colors.primary-active}`), and disabled washes to the muted `{colors.primary-disabled}`. The slight letter-spacing keeps the label crisp at small button sizes common on product grids.

**`button-secondary`** — Transparent fill with a 1.5px crimson border and matching crimson Arpona type, identical height and padding to primary. Used for secondary actions (View Details, Add to Wishlist) when the primary slot is held by Add to Cart. On dark section backgrounds, swap for `button-ghost-dark`, which replaces the crimson border and text with cream (`{colors.on-dark}`) for contrast.

### Text Input / Search
**`text-input`** — Warm canvas fill (`{colors.canvas}`, #fcf4f1) with a 1px `{colors.hairline}` border that snaps to `{colors.primary}` on focus. Arpona body-md at 16px keeps input type optically consistent with surrounding editorial copy. The 44px height aligns exactly with button height for clean inline form rows.

**`search-bar`** — A slightly warmer surface (`{colors.surface-card}`, #f6efe2) than the page canvas, with a magnifier icon in `{colors.muted}`. The `{rounded.xs}` radius is deliberately catalog-flat rather than pill-shaped. On desktop it sits inline in the nav bar; on mobile it expands into a full-width overlay drawer triggered by an icon tap.

### Navigation
**`nav-bar`** — Deep black-oak background (#0d0b09) with cream type and a gold bottom border at 25% opacity at rest, snapping to full `{colors.accent-gold}` on page scroll. The logo mark renders in `{colors.accent-gold}` against the dark field, reinforcing the gold-as-prestige signal. Links use Arpona 15px/500 with 0.3px tracking. A mega-dropdown opens on Browse by Category and Browse by Spirit on desktop, providing the same bottle-shop aisle logic a physical store would use.

### Product Card
**`product-card`** — Warm cream surface (`{colors.surface-card}`) with a 1px warm-gray border (`{colors.hairline-soft}`) and `{rounded.sm}` corners, lifting to a crimson border and 16px red shadow glow on hover (`product-card-hover`). Product name renders in `{typography.title-sm}`, price in `{typography.price-display}` using `{colors.primary}`, and the bottle image occupies the upper two-thirds of the card. Badge overlays (vintage year, sale percentage) sit in the top-left corner using `vintage-badge` or `sale-badge` tokens.

### Hero
**`hero`** — Full-bleed dark canvas (#0d0b09) with a bottle or cellar photograph behind a 60% dark overlay. Headline in `{typography.display-xl}` (Arpona 52px/700) in `{colors.on-dark}` cream; subhead in `{typography.body-md}`. A `button-primary` CTA sits below with generous vertical spacing. Minimum height 520px; on wide viewports the layout shifts to a 50/50 text-image split and the overlay is removed since text sits on the dark half only.

### Badges
**`vintage-badge`** — Gold fill (`{colors.accent-gold}`) with near-black Arpona type in `{typography.badge-label}` (10px uppercase, 1px tracking), zero radius. The gold-on-dark color mirrors the foil and neck labels on actual bottles, completing a visual rhyme between shelf and screen. **`sale-badge`** uses crimson fill to signal price urgency without competing with the gold prestige signal. **`provenance-badge`** inverts to dark-canvas fill with a gold outline and gold text, reserved for allocated or limited bottles that merit special status distinct from a discount marker.

### Age Gate
**`age-gate-modal`** — Full-viewport dark scrim with a centered panel in `{colors.dark-deep}`, framed by a thin `{colors.accent-gold}` border that reads as a formal threshold rather than a warning dialog. Headline in `{typography.display-md}` Arpona in cream. Two buttons: `button-primary` (I am of legal drinking age) and `button-ghost-dark` (Exit). The gold border is the sole UI moment that directly mirrors the brand's bottle-label gold before the user reaches the catalog.

### Footer
**`footer`** — Deep black-oak background (`{colors.dark-deep}`) anchored by a 2px `{colors.accent-gold}` top rule — the same gold accent that runs through the nav and badges. Section headings in Arpona `{typography.title-sm}` in cream; links in `{typography.body-sm}` warming to `{colors.accent-gold}` on hover. An inline newsletter row pairs `text-input` with `button-primary`. Legal text, state-specific compliance notices, and license information render in `{colors.muted}` caption.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; search expands full-width overlay drawer; hero stacks to image-over-text with 56vw image crop; age-gate fills full screen |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + search + cart icons with category links in a horizontally scrollable pill row below; hero shifts to 60/40 text-image split |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with mega-dropdown on hover; sidebar filter panel on category pages; hero 50/50 split no overlay |
| Wide | > 1440px | Four-column product grid; content max-width 1360px centered; hero image bleeds edge-to-edge with text constrained to left 640px |

### Touch Targets
- All buttons and nav links maintain minimum 44px height
- Product card tap area covers the full card surface, not just the title link
- Mobile search trigger is a 44×44px icon button in the collapsed nav bar
- Age gate buttons are full-width on mobile with 52px height for a clear tap affordance
- Category filter pills scroll horizontally on mobile with `{spacing.sm}` gap; individual pill height minimum 36px

### Collapsing Strategy
- Nav mega-dropdowns become a full-screen category drawer (slides in from left) on mobile and tablet
- Product card price and badge row stacks vertically below the product name on cards narrower than 160px
- Footer three-column layout collapses to single stacked accordion sections on mobile
- Desktop sidebar filters migrate to a bottom sheet on mobile, triggered by a fixed "Filter & Sort" bar at the bottom of the viewport
- Hero dual-column collapses to stacked (text below image) on mobile; the dark overlay is restored at full opacity on the image crop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one typeface (Arpona) was detected; weight range, italic availability, and licensed variant names are unconfirmed — fallback serif stack is inferred
- Disabled button color (`{colors.primary-disabled}`, #d4a0a0) is derived by lightening primary; not directly observed on site
- No icon set style (stroke weight, fill vs. outline, SVG library) was extractable
- Sale price vs. original price vs. price-range formatting rules are inferred from category norms, not observed
- Age gate implementation details (cookie TTL, geolocation-gated vs. always-shown, birth-date vs. yes/no confirmation) not confirmed
- Dark-mode support is unconfirmed; dark-canvas and dark-deep tokens represent explicit dark section backgrounds, not a system-level prefers-color-scheme toggle
- Mobile navigation transition style (slide, fade, push) and timing curves not observed
- Hover animation timing on product cards (transition duration/easing) not extractable
