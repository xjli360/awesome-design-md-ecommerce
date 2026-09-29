---
version: alpha
name: "Ministry of Supply"
source_url: "https://ministryofsupply.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sk-Modernist — an angular, narrowly-spaced geometric sans-serif that Shopify sites almost never carry — cuts through the Ministry of Supply product grid with the same efficiency-first logic the brand applies to its fabrics: no humanist warmup, no ornamental curve. The primary CTA lands in #ff3d3d, a red that reads urgent against the near-white #fafafa canvas but cools quickly into surrounding charcoal (#202020) and slate (#4d565e) text hierarchies. Deep purple-indigo (#5b2dcf) surfaces as a secondary accent on hover states, selected filters, and the occasional badge — pairing purple with red is unusual in workwear, but Ministry of Supply is not a conventional apparel brand; it is a materials-science company that makes trousers. The palette carries its own internal weather system: #f59e0b amber for restocked-soon notices, #22c55e green for in-stock, #38bdf8 sky-blue for technical-feature callouts — all pulled from Tailwind system tokens visible in the extracted hex set, suggesting a utility-first frontend build sitting under the Shopify shell. Rounded corners are minimal; product cards and input fields sit on a near-square radius ({rounded.xs}) while only badges reach {rounded.full}. Spacing is compact, the product grid uses tightly packed cards with minimal gutter breathing room, reflecting the site's position as a high-conversion, feature-dense DTC store rather than an editorial lifestyle platform. The Sk-Modernist Mono variant surfaces in technical specs and material-weight callouts, treating fabric composition data the way a finance dashboard would treat a stock ticker — monospaced precision as a deliberate signal of engineering seriousness. On mobile the nav collapses to a hamburger with a full-screen overlay that preserves the left-aligned Sk-Modernist brand wordmark at 24px, keeping header identity clean even at 375px width.

colors:
  primary: "#ff3d3d"
  primary-active: "#e22120"
  primary-disabled: "#f59e9e"
  secondary: "#5b2dcf"
  secondary-active: "#4a22b0"
  secondary-soft: "#899df1"
  accent-amber: "#f59e0b"
  accent-green: "#22c55e"
  accent-sky: "#38bdf8"
  accent-electric: "#0517f4"
  error: "#fc0000"
  error-dark: "#630000"
  ink: "#202020"
  ink-deep: "#121212"
  body: "#4d565e"
  body-dark: "#1f2937"
  muted: "#777777"
  hairline: "#dedede"
  hairline-soft: "#d1d5db"
  canvas: "#fafafa"
  surface-soft: "#ededed"
  surface-card: "#f8f8f8"
  surface-light: "#f0f9ff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  mono-spec:
    fontFamily: "'Sk-Modernist Mono', 'SFMono-Regular', Menlo, Consolas, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-tag:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Sk-Modernist', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-announcement:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageFit: cover
    imageAspect: 3/4
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    textAlign: left
    paddingX: "{spacing.xxl}"
  performance-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  stock-badge-instock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  stock-badge-low:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  material-spec-chip:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.body-dark}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: "1px solid {colors.hairline-soft}"
  size-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    width: 48px
  size-selector-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  size-selector-button-soldout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  filter-tag-active:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.secondary}"
    padding: 6px 12px
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Solid #ff3d3d fill on a near-square {rounded.xs} corner, uppercase Sk-Modernist at 15px/600 weight with 0.3px letter-spacing, white label. The narrow radius signals technical precision over lifestyle softness. Active state darkens to #e22120; disabled washes to the desaturated #f59e9e. Used for primary purchase, add-to-cart, and checkout actions throughout the funnel.

**`button-secondary`** — Transparent fill with a 1.5px solid #202020 border, matching primary sizing and typography exactly. On hover the background fills lightly with {colors.surface-soft}. This pattern keeps CTA hierarchy clear on white-canvas pages: red for buy, outlined for secondary actions like "Save to Wishlist," "Shop All," or size-guide triggers.

**`button-ghost`** — No border, transparent background, uses {typography.button-sm} in {colors.body}. Appears as filter-clear actions, inline text links within product specs, and "See All" nudges at section edges.

### Navigation

**`nav-bar`** — 64px tall on {colors.canvas} with a 1px {colors.hairline-soft} bottom border. Logo sits far left, primary nav links center in {typography.nav-link} (14px/500), utility icons (search, account, cart) far right. Above it, a 36px {nav-bar-announcement} strip in {colors.ink-deep} carries promo text in {typography.caption} — the dark-over-light two-tier header structure is consistent across all pages. Cart icon receives a small red count pip in {colors.primary} when populated.

### Product Card

**`product-card`** — 3:4 portrait image on {colors.surface-card} with {rounded.xs} on the card container. Title renders in {typography.title-sm}, price in {typography.body-md} immediately below. On hover a full-width {button-primary} strip slides up from the card base as a quick-add overlay. {performance-badge} labels pin to the top-left corner of the image frame. Color swatch dots ({color-swatch}) render in a horizontal row beneath the title when multiple colorways exist.

### Hero

**`hero`** — Full-bleed dark-field section in {colors.ink-deep} or a brand photography backdrop, left-aligned headline in {typography.display-xl}, single-sentence descriptor in {typography.body-md} at {colors.on-dark}, and a single {button-primary} CTA. Minimum height 560px with padding-x at {spacing.xxl}. The dark hero maximizes the red button's legibility — {colors.primary} pops against #121212 far more cleanly than it does against the white-canvas editorial sections further down the page.

### Badges

**`performance-badge`** — Pill-shaped ({rounded.full}) in {colors.secondary} (#5b2dcf), white uppercase Sk-Modernist at 11px/700 with 0.5px letter-spacing. Labels like "MACHINE WASHABLE," "MOISTURE-WICKING," or "WRINKLE-FREE" render directly over product imagery. The purple-over-dark-photo combination distinguishes technical performance claims from promotional discounts, which stay in the red {colors.primary} register.

**`stock-badge-instock`** / **`stock-badge-low`** — Same pill geometry as the performance badge; #22c55e fill for in-stock, #f59e0b fill for low-stock. Both colors correspond exactly to Tailwind's `green-500` and `amber-400` defaults, confirming a deliberate status-color convention shared across inventory, shipping ETA, and availability UI sitewide.

### Material Spec Chip

**`material-spec-chip`** — Small rectangle in {colors.surface-light} (#f0f9ff) with a {colors.hairline-soft} border, text in {typography.mono-spec} (Sk-Modernist Mono). Used in product-detail technical panels to surface fabric composition ("88% Nylon / 12% Spandex"), weight in GSM, and stretch percentage. The monospace font and cool-blue tint borrow from developer-tooling aesthetics to frame fabric engineering as an exact science rather than a lifestyle attribute.

### Size & Color Selectors

**`size-selector-button`** — 40×48px near-square tile, 1px {colors.hairline} border on {colors.canvas}, label in {typography.body-sm}. Active variant inverts to {colors.ink} fill with {colors.on-dark} label and a matching 1px {colors.ink} border. Sold-out variant fills {colors.surface-soft} with {colors.muted} text; a diagonal CSS strike line overlays the tile.

**`color-swatch`** — 28px circle at {rounded.full}, no text label. Active state receives a 2px {colors.ink} outline with 2px offset to preserve the color visibility. Tooltip on hover surfaces the color name in {typography.caption}.

### Search

**`search-bar`** — {colors.surface-soft} background, {rounded.xs} corners, 44px tall. Border transitions from transparent to 1px {colors.hairline} on focus, then to 1.5px {colors.ink} on active input. Magnifier icon sits left-inside in {colors.muted}. On desktop the search field expands inline within the nav row; on mobile it opens a full-screen overlay with the same soft-background field centered at the top.

### Filter Tags

**`filter-tag`** / **`filter-tag-active`** — Uppercase 11px/600 Sk-Modernist label in a {rounded.xs} bordered chip. Default state: {colors.canvas} background, {colors.hairline} border, {colors.body} text. Active state fills with {colors.secondary} (#5b2dcf) and white text, matching the performance-badge purple register. The active-filter purple creates a persistent visual inventory of selections without consuming grid real estate.

### Footer

**`footer`** — {colors.ink-deep} full-width band with {colors.on-dark} text. Column headings in {typography.title-sm} (600 weight), links in {typography.body-sm} (400 weight). Four-column grid layout covers Shop, About, Sustainability, and Support; below sits a newsletter input field and social icon row. Vertical padding at {spacing.xxl}. On mobile, column groups collapse into stacked accordions with full-width tap toggles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen overlay; hero headline scales to {typography.display-md}; hero padding-x reduces to {spacing.base}; footer collapses to stacked accordions; quick-add overlay replaced by sticky add-to-cart bottom bar on PDP |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + icon tray only, text links hidden; hero at {typography.display-md}; filter panel moves to bottom-sheet modal |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav visible; hero at {typography.display-xl}; left-sidebar filter panel on PLP |
| Wide | > 1440px | Max-width container (~1440px) centered on page; grid holds four columns; hero gains additional left padding to align with the content rail |

### Touch Targets

- All interactive controls (buttons, size tiles, filter tags, swatch circles) maintain a minimum 44×44px touch target on mobile via padding compensation
- Color swatches (28px visual diameter) receive 8px padding on all sides to reach a 44px tap region without enlarging the visual element
- Footer accordion toggles span full row width — no icon-only tap zone
- Nav hamburger button uses a 44×44px hit area regardless of icon size

### Collapsing Strategy

- Primary nav text links are hidden at tablet-and-below; hamburger opens a full-screen overlay with the complete link tree and the brand wordmark at top-left
- PLP filter panel moves from left sidebar (desktop) to a bottom-sheet modal triggered by a "Filter & Sort" button pinned to the PLP header on mobile and tablet
- Announcement bar content that exceeds one line at mobile widths collapses to a horizontally scrolling marquee
- Material spec chips in the product detail panel wrap to a two-column grid on tablet and a single-column stacked list on mobile
- Hero CTA button reduces from 48px to 44px height on mobile to conserve vertical rhythm

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Multiple red variants (#ff3d3d, #fc0000, #e22120) present in extracted set — unclear whether all are intentional brand tokens or partially Shopify/app-injected UI states; {colors.primary} anchored to #ff3d3d as the brightest and first-listed occurrence
- Button and card border-radius not confirmed from live DOM audit; {rounded.xs} (4px) inferred from the near-square technical aesthetic typical of performance-workwear DTC brands
- Exact nav bar height (64px used here) and sticky-scroll shrink behavior not confirmed without live scroll inspection
- Sk-Modernist available font-weight subset not determinable from font-family stack alone — weights 300/400/500/600/700 assumed but full range unknown
- Hero section treatment (static image, video background, or parallax) could not be determined from extracted tokens
- Dark-mode support unknown — no `prefers-color-scheme` tokens extracted and no meta theme-color present
- Product card hover animation specifics (scale factor, shadow depth, slide-up CTA distance) not confirmed; common Shopify DTC patterns assumed
- No confirmed brand token for nav-link active/selected underline color — {colors.primary} assumed as the active indicator
