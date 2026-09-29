---
version: alpha
name: "Quince"
source_url: "https://www.quince.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The 3-degree warmth in #21201f — Quince's near-black — does more brand work than any campaign line: set against a #f7f7f5 canvas that reads linen rather than paper, it signals boutique temperature without boutique pricing. IvyPresto Headline carries display text in a light-weight editorial serif that nods to luxury fashion publishing, while Grosa — a geometric sans-serif — handles navigation, labels, and product specs with utilitarian precision; the contrast between these two type voices enacts the brand's core proposition in typographic form. Primary CTAs wear the same near-black, rendered as tracked uppercase Grosa labels with barely-there {rounded.xs} corners rather than the rounded pills that soften most DTC call-to-action buttons.

  Sale and clearance surfaces pull #af3535 — a terracotta-adjacent red that avoids garish urgency and reads instead like a price markdown in a printed catalog. Green stock indicators use #2d822b, similarly desaturated enough to feel deliberate rather than traffic-light functional. A warm peach #ffa273 punctuates contextual UI elements — promotional callouts, illustrative fills — as the only high-chroma note in a palette otherwise assembled from complex warm neutrals: #e5ccbc, #e2dad5, #dfdace, and #d0d3bb appear as surface tints for category tiles and card backgrounds, collectively giving the product grid a warmer temperature than white-canvas DTC defaults. Accent blues (#c8d3f1, #a5bdd6) surface within swatch systems for blue gemstone or fabric colorways rather than as UI chrome.

  Spacing is generous without being opulent. Product images run tall at roughly 3:4 or 4:5 aspect ratios, grid gutters stay open, and even dense category pages breathe. The "Radically Low Prices" headline drops into IvyPresto display at the top of the funnel — the editorial restraint is itself the value signal, implying material quality through spacing and serif selection rather than decoration.

colors:
  primary: "#21201f"
  primary-active: "#363940"
  primary-disabled: "#a99d98"
  ink: "#21201f"
  body: "#363940"
  muted: "#757575"
  muted-soft: "#888888"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeec"
  canvas: "#f7f7f5"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#e5ccbc"
  surface-beige: "#dfdace"
  on-primary: "#f7f7f5"
  on-dark: "#f7f7f5"
  accent-sale: "#af3535"
  accent-sale-bright: "#d24343"
  accent-peach: "#ffa273"
  accent-green: "#2d822b"
  accent-rust: "#85351b"
  swatch-blue: "#c8d3f1"
  swatch-blush: "#fdd8d8"
  swatch-warm-gray: "#bdbdbc"

typography:
  display-xl:
    fontFamily: "'IvyPresto Headline', 'ivy-headline', Georgia, serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'IvyPresto Headline', 'ivy-headline', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'IvyPresto Headline', 'ivy-headline', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'IvyPresto Headline', 'ivy-headline', Georgia, serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Grosa', 'grosa', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  price-display:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  badge:
    fontFamily: "'Grosa', 'grosa', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em

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
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
    width: 100%
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 48px
    padding: 12px 16px
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 0 {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-price-compare:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    minHeight: 480px
  hero-editorial:
    backgroundColor: "{colors.surface-warm}"
    titleTypography: "{typography.display-lg}"
    titleColor: "{colors.ink}"
  sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  sale-badge-bright:
    backgroundColor: "{colors.accent-sale-bright}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  stock-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 40px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    selectedBorder: "1px solid {colors.ink}"
    height: 40px
    minWidth: 40px
  color-swatch:
    rounded: "{rounded.full}"
    size: 24px
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 {spacing.base}"
  category-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: none
    rounded: "{rounded.full}"
    padding: 6px 16px
  rating-stars:
    filledColor: "{colors.ink}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"

---

## Components

### Buttons
**`button-primary`** — Full-width near-black (#21201f) at 48px height with {rounded.xs} (2px) corners — the barely-there radius resists the pill-softness common to DTC. Typography is Grosa at 14px/500 weight in tracked uppercase, giving CTAs a label-like precision rather than marketing warmth. Active state deepens to the cooler #363940; disabled state uses the warm taupe {colors.primary-disabled} (#a99d98), suggesting absence without alarming red.

**`button-secondary`** — Same geometry as primary, rendered as a 1px #21201f outline on transparent fill. Used when a primary CTA already dominates — "Add to Wishlist," "View All," or secondary PDP actions. Maintains identical uppercase Grosa typography for visual rhythm across button tiers.

**`button-ghost`** — Text-only Grosa in muted (#757575), no border or background. Used for dismissal actions, in-line navigation links, or within modals where a full button would over-weight the surface.

### Text Inputs
**`text-input`** — Clean rectangular field with 1px hairline border (#d9d9d9) and {rounded.xs} — no ornamental rounding. Focus state upgrades to a 1px solid ink border with no shadow or glow, reinforcing a minimal-signal aesthetic. Used uniformly across search, email capture, and checkout fields.

### Navigation
**`nav-bar`** — 60px tall on the warm white canvas (#f7f7f5), separated from page content by a 1px hairline bottom border. Logo anchors left, category links span center in Grosa 13px with modest tracking, and utility icons (search, account, cart) sit right. On sticky scroll a hairline shadow replaces the border without adding background weight. Dropdowns float as light white panels with subtle shadow rather than colored megamenu panels.

### Product Cards
**`product-card`** — No border-radius on the card container, creating a grid where gutters define separation rather than card borders. Images fill a 3:4 aspect ratio. Beneath the image: product name in Grosa body-sm, then price in {typography.price-display}, and where applicable a compare-at price in {typography.price-compare} with strikethrough in muted gray. Badges overlay the top-left image corner: sale in {colors.accent-sale}, new-arrival in {colors.primary}, in-stock in {colors.accent-green}.

### Hero Sections
**`hero`** — Large editorial surface with IvyPresto Headline at display-xl (48px, weight 300). The lightweight serif reads grand without requiring weight 700 authority. Often paired with a Grosa body-md subtitle in muted gray. The editorial variant (`hero-editorial`) swaps the canvas for {colors.surface-warm} (#e5ccbc), used for seasonal or category campaigns — a beige warmth that shifts the entire page temperature.

### Badges
**`sale-badge`** — Flat rectangular label in #af3535 at 11px/500 Grosa with 0.04em tracking and {rounded.none} geometry, deliberately catalog-like rather than pill-shaped. The brighter variant in #d24343 appears for higher-urgency markdown moments.

**`stock-badge`** — Same flat geometry in #2d822b. The desaturated green reads horticultural rather than traffic-signal, fitting the brand's quality-over-urgency register.

### Size & Color Selectors
**`size-selector`** — Square chips at 40px height, 1px hairline border at rest, 1px ink border on selection, {rounded.none} corners. Sold-out states render a diagonal strikethrough line over the chip. No toggle animation — the border swap is the full state signal.

**`color-swatch`** — 24px circular discs using {rounded.full}, with a 2px ink selection ring offset 2px from the disc edge so the swatch fill remains fully visible in selected state. The swatch palette draws from the extracted warm neutrals (#e5ccbc, #dfdace, #fdd8d8) and cooler tones (#c8d3f1, #bdbdbc).

### Category Pills
**`category-pill`** — Small filter chips with 1px hairline border, {rounded.full}, and label-uppercase Grosa. Inactive state: canvas background. Active state: {colors.primary} fill with {colors.on-primary} text. Used in horizontal filter strips on category pages.

### Promotional Banner
**`promo-banner`** — 40px full-width strip in near-black with on-primary text in label-uppercase Grosa. Carries sitewide offers — free shipping thresholds, limited-time pricing claims, seasonal events. Single-line static or marquee content only.

### Trust Strip
**`trust-strip`** — Slim {colors.surface-soft} band above the footer with a 1px hairline top border. Grosa caption text at {colors.muted} lists trust signals (free returns, quality guarantee, certifications). Low visual weight ensures it reads as footnote, not feature.

### Footer
**`footer`** — Inverts the page: {colors.primary} (#21201f) background with {colors.on-primary} (#f7f7f5) text. Section headings in label-uppercase Grosa; body links in body-sm regular weight. The near-black footer creates a strong visual bracket that separates the brand mark from the warm off-white product surfaces above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; button-primary spans full width; nav collapses to hamburger + logo + cart; hero headlines drop to display-md (28px); size chips expand to 44px touch height |
| Tablet | 744–1128px | 2-column product grid; nav shows primary category links with sub-nav in drawer; hero at display-lg (36px); PDP uses side-by-side price and add-to-cart |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with hover dropdowns; hero at display-xl (48px); PDP sticky add-to-cart panel in right column |
| Wide | > 1440px | Content capped at ~1440px with balanced side margins; product grid may extend to 5 columns; hero imagery spans full canvas width |

### Touch Targets
- Minimum 44×44px for all interactive elements on mobile
- Size selector chips expand to at least 44px height on mobile regardless of grid constraints
- Color swatches expand to 32px diameter on mobile with additional invisible tap zone padding
- Nav icons use 44px touch target area regardless of visible icon size

### Collapsing Strategy
- Primary nav collapses to hamburger drawer below 1128px; top-level categories remain as horizontally scrollable strip at tablet
- PDP sticky add-to-cart panel converts to fixed bottom bar on mobile
- Footer multi-column grid collapses to accordion sections on mobile
- Category filter sidebar converts to bottom-sheet modal on mobile and tablet
- Promo banner text may truncate with ellipsis at narrow widths; marquee scroll used for long messages

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Button corner radius is inferred as {rounded.xs} (2px) based on the minimal aesthetic; site may use fully square {rounded.none} corners on primary CTAs
- Grosa font weight availability is unconfirmed; weight 500 for medium-emphasis elements may fall back to 400 if only regular/bold cuts are loaded
- Whether Quince uses IvyPresto Headline vs. IvyPresto Display or IvyOra is unconfirmed — both share the `ivy-headline` CSS stack
- The role of #ffa273 (warm peach) is ambiguous — could be a sale/promo accent, an illustration fill, or a seasonal campaign color rather than a permanent UI token
- The blue cluster (#c8d3f1, #a5bdd6, #e3e9f8) most likely belongs to jewelry swatch colorways (blue topaz, aquamarine) rather than general UI chrome; their UI role is unverified
- Animation and transition durations not extracted — hover state timings, cart slide-in duration, and filter panel animations are estimated
- Exact PDP layout column proportions and sticky panel behavior inferred from DTC norms rather than measured
- Dark-mode support not confirmed; all tokens assume light-mode only
- Grid gutter widths and per-breakpoint column counts are estimated; no source-of-truth measurements available from extraction
