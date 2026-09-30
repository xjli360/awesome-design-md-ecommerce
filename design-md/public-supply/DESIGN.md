---
version: alpha
name: "Public - Supply"
source_url: "https://public-supply.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The golden pull of #e9be33 — close kin to a No. 2 pencil's lacquer or an unlined legal pad held to morning light — is Public Supply's single charged signal. Every sale badge, accent rule, and primary CTA carries it as annotation rather than advertisement; pressed against a near-charcoal ink layer (#31373d) and a flat institutional mid-gray (#6c6c6c), the marigold reads like a felt-tip correction mark left on proofed copy. Typography stays entirely within the system-font stack — Helvetica Neue, Arial, sans-serif — deployed with widened letter-spacing at display sizes that gives headlines the measured cadence of a government form or memo header rather than the compressed urgency of retail fashion. Rounding is absent across the full system: buttons, inputs, cards, badges, and filter controls all render at {rounded.none}, with no corner relief to soften the rectilinear grid. The angularity signals utilitarian precision — a supply-closet indexing logic rather than consumer softness. A steel blue (#479ccf) enters as the accent for links and informational states, carrying the same flat institutional tone as ballpoint on white-ruled stock; it is the one cool note in an otherwise warm-neutral palette. Product photography isolates objects against {colors.hairline} or pure white, foregrounding surface texture — the tooth of recycled pulp, the matte face of chipboard, the wire coil's ridged metal — rather than lifestyle staging. Spacing throughout is generous: wide gutters and vertical breathing room between grid rows let each SKU read as an object under examination rather than an item in a stack. The footer descends into {colors.dark-canvas} territory, all links reversed to {colors.on-dark}, anchoring the page without any further marigold presence. Public Supply disciplines its palette so thoroughly that the golden always lands exactly where the eye should arrive — a restraint that reads as editorial confidence.

colors:
  primary: "#e9be33"
  primary-active: "#c9a020"
  primary-disabled: "#f2d98a"
  ink: "#31373d"
  body: "#3d4349"
  muted: "#6c6c6c"
  hairline: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#31373d"
  on-dark: "#eaeaea"
  accent: "#479ccf"
  accent-active: "#2d7fb0"
  dark-canvas: "#31373d"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0.04em
  display-md:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.03em
  title-md:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.01em
  body-md:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.07em
    textTransform: uppercase
  button-md:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.09em
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.09em
    textTransform: uppercase
  nav-link:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.05em
  price-display:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  footer-heading:
    fontFamily: "Helvetica Neue, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: "button-primary"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.md}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: "{spacing.xs} {spacing.md}"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-tag-sale:
    textColor: "{colors.primary-active}"
    typography: "{typography.price-display}"
  price-tag-original:
    textColor: "{colors.muted}"
    typography: "{typography.price-display}"
    textDecoration: line-through
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.footer-heading}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 380px
    borderLeft: "1px solid {colors.hairline}"
  cart-line-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 36px

## Components

### Buttons
**`button-primary`** — A flat, square-cornered rectangle filled with marigold {colors.primary}, labeled in {typography.button-md} — all-caps, 0.09em tracked — in dark charcoal {colors.on-primary}. Zero border radius makes it read as a printed stamp rather than a digital affordance. Hover deepens to {colors.primary-active} (#c9a020); disabled washes to {colors.primary-disabled} with {colors.muted} text, communicating unavailability without drama.

**`button-secondary`** — White {colors.canvas} fill with a 1px solid {colors.ink} border, identical dimensions and uppercase {typography.button-md} to the primary. On hover it inverts fully — charcoal fill, white text — producing a clean two-state toggle that relies on contrast rather than color accent. Maintains {rounded.none} throughout.

**`button-text`** — Bare inline link in {colors.accent} (#479ccf) with underline. Used for lower-priority actions within copy blocks ("view all", "learn more") where a boxed button would overweight the hierarchy.

### Text Input
**`text-input`** — Zero-radius field, 44px tall, with a 1px {colors.hairline} border that sharpens to 1px {colors.ink} on focus. Typeset in {typography.body-md}; no floating label — placeholder disappears on entry. Validation feedback delivered via border color change and inline {typography.caption} message below the field.

### Navigation
**`nav-bar`** — 56px fixed bar on {colors.canvas} with a single 1px {colors.hairline} rule along its bottom edge. Logo sits left; primary category links run center in {typography.nav-link} at 0.05em tracking; cart icon with numeral count sits right. No hover underlines — active state is conveyed by weight increase only, maintaining the system's tonal discipline.

### Product Card
**`product-card`** — A flush grid cell with no chrome: no shadow, no border, no rounding. Image fills at 1:1 aspect ratio, edge to edge. Below it, product name in {typography.title-sm} runs one or two lines; price in {typography.price-display} follows immediately with minimal gap. Sale badge ({sale-badge}) positions absolutely at the top-left corner of the image — marigold on the photograph, not below it. Out-of-stock state applies a {colors.muted} overlay with "SOLD OUT" in {typography.caption} centered over the image.

### Badges
**`sale-badge`** — Marigold {colors.primary} rectangle with {colors.on-primary} text in {typography.caption} uppercase. Sharp corners, snug padding (3px top/bottom, 7px sides), positioned flush to product image corners. Used for SALE, percentage-off, and clearance designations — the one place the primary yellow appears without interactive intent.

**`new-badge`** — Same geometry as the sale badge; {colors.ink} fill with {colors.canvas} text. Marks recent additions without competing with the golden sale signal. The two badges should not coexist on the same card.

### Hero
**`hero`** — Full-width panel on {colors.canvas}. Headline in {typography.display-xl} with 0.04em letter-spacing; supporting line in {typography.body-md}. Primary CTA uses `button-primary`. Default hero is text-only — typography and negative space carry the statement. Product-focused heroes may place a single isolated object image right-aligned against white, never cropped or lifestyle-staged.

### Search
**`search-bar`** — Inline bar or drawer-mounted input rendered on {colors.surface-soft} with 1px {colors.hairline} border. No radius, 40px height, magnifier glyph left-aligned inside the field. Suggestion dropdown renders as a flat, borderless list immediately below the bar with {typography.body-sm} items and a 1px {colors.hairline} bottom separator per row.

### Collection Filter
**`filter-pill`** — Zero-radius outlined chip in {typography.button-sm} uppercase. Inactive: {colors.canvas} fill with 1px {colors.hairline} border. Active: inverted to {colors.ink} fill with {colors.canvas} text and {colors.ink} border. Multiple active filters stack visually, readable at a glance as a state record. On mobile they scroll horizontally in a single strip; on desktop they wrap into a row above the product grid.

### Pricing
**`price-tag`** — Default price in {typography.price-display}, {colors.ink}. Sale price swaps to {colors.primary-active} while the original price renders in {colors.muted} with line-through — the darkened golden keeps the sale signal warm without using the full primary yellow reserved for interactive elements.

### Footer
**`footer`** — Dark {colors.dark-canvas} (#31373d) panel; all text reverses to {colors.on-dark}. Column headings use {typography.footer-heading} (11px, 700 weight, 0.10em tracked, uppercase). Body links in {typography.body-sm}, no underline at rest, underline on hover. The marigold primary does not appear here — the dark surface stands without any brand accent, a deliberate pause from the page's golden tension.

### Cart Drawer
**`cart-drawer`** — 380px right-anchored panel sliding over page content on {colors.canvas}, separated from the page by a single 1px {colors.hairline} left border. Line items divided by {colors.hairline} rules; quantity controlled by `quantity-stepper`. Checkout CTA is a full-width `button-primary` pinned to the drawer bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger left + centered logo; filter pills scroll horizontally as a single strip; hero stacks text above image; cart drawer expands to full viewport width |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links, hamburger for secondary; hero unlocks side-by-side layout |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all links visible; filter row renders above grid as wrapping chip strip |
| Wide | > 1440px | Grid caps at ~1280px max-width and centers; outer gutters grow proportionally; column count holds at four |

### Touch Targets
- All interactive elements minimum 44×44px on touch viewports
- Filter pills expand vertical padding to meet 44px tap height on mobile
- Nav links inside the mobile drawer achieve 48px tap height via padding
- Cart and search icons extend tap area to full nav-bar height (56px)
- Quantity stepper buttons are minimum 36×36px; outer touch target padded to 44px

### Collapsing Strategy
- Nav: hamburger + logo on mobile; full link row on tablet and above
- Product grid: 1 col → 2 col → 3 col → 4 col across breakpoints
- Filters: horizontal scroll strip on mobile; full wrap row on desktop
- Footer: single-column stack on mobile; 3–4 column grid on desktop
- Hero: text stacked above image on mobile; side-by-side on tablet and above
- Cart drawer: full-width panel on mobile; fixed 380px on tablet and above

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned "This store is unavailable" at extraction time — color and font data sourced from static HTML/CSS only; JavaScript-loaded design tokens were not captured
- No custom brand typeface detected; Helvetica Neue/Arial system stack may not reflect the deployed brand — Public Supply may use a licensed grotesque (e.g., Suisse Int'l, GT America, Akkurat) that loads client-side and was absent during extraction
- Only five hex values extracted; hover, disabled, and surface-state shades are inferred extrapolations, not observed computed values
- No favicon, og:image, or meta theme-color present — browser chrome color treatment unconfirmed
- Dark mode support unknown — no prefers-color-scheme overrides were captured in static CSS
- Illustration style, iconography weight, and motion/animation properties entirely undocumented
- Mobile navigation pattern (hamburger drawer vs. bottom tab bar) not confirmed from extraction
- Secondary and tertiary typeface weights and their specific use cases not confirmed — weight assignments above are reasoned estimates from the system-font stack
