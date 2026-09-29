---
version: alpha
name: "Dough"
source_url: "https://www.dough.tech"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  #fbe548 — the flattest, most saturated marigold in consumer display hardware — is Dough's single-volt brand identifier: every primary CTA and product-launch countdown runs on this electric yellow against an otherwise strict near-black (#363636) and graduated-gray scaffold. The brand name, slang for cash, winks at accessible pricing without cheapening the product photography; full-bleed monitor renders sit on dark canvas where backlit panel edges read as product authenticity rather than composited glamour. Alegreya Sans carries the type system — an unlikely selection, a humanist editorial face originally engineered for long-form reading, now stretched to 48px weight 700 for product headlines and compressed to 12px captions for spec notation; the humanist optical corrections give Dough's interface warmth that cold geometric sans-serifs common to monitor hardware cannot replicate. Body text runs at 16px weight 400 with generous line-height, practical on pages where specification tables, community forum excerpts, and comparison grids all compete for legibility. Corners are sharp-moderate: {rounded.sm} at 8px on cards and inputs, {rounded.xs} at 4px on spec badges, {rounded.full} on pill-shaped availability tags. A secondary cyan accent ({colors.accent}, #00adef) appears in feature callouts — a literal screen-glow reference that anchors the palette to the panels' own display output — while {colors.steel} (#4a5764) surfaces in secondary navigation and comparison column headers, bridging the electric yellow and charcoal body without a third accent hue. Product cards show monitors at 16:9 crop with a {colors.primary} pricing badge anchored bottom-left, community review scores appear in steel-fill chips with weight-600 numerals, and checkout surfaces stay on pure white ({colors.canvas}) with yellow focus rings on form fields, placing the brand color at the exact moment a purchase decision is made.

colors:
  primary: "#fbe548"
  primary-active: "#e0c800"
  primary-disabled: "#f9ef9a"
  accent: "#00adef"
  accent-active: "#0096cc"
  steel: "#4a5764"
  ink: "#222222"
  body: "#363636"
  muted: "#7a7a7a"
  muted-soft: "#969696"
  hairline: "#d4d4d4"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#363636"
  on-primary: "#222222"
  on-dark: "#ffffff"
  success: "#099e4d"
  error: "#de3618"
  error-dark: "#b33a3a"

typography:
  display-xl:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  button-md:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Alegreya Sans', 'Avenir Next', Avenir, -apple-system, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
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
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
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
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.on-dark}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBg: "{colors.surface-dark}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
  spec-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  availability-pill:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  availability-pill-oos:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    minHeight: 560px
    paddingV: "{spacing.section}"
  feature-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  comparison-table:
    headerBg: "{colors.steel}"
    headerText: "{colors.on-dark}"
    headerTypography: "{typography.spec-label}"
    rowBg: "{colors.canvas}"
    rowAltBg: "{colors.surface-soft}"
    cellTypography: "{typography.body-sm}"
    highlightBorder: "2px solid {colors.primary}"
  community-score:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  countdown-timer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    digitTypography: "{typography.display-md}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — Filled marigold ({colors.primary}, #fbe548) with near-black text ({colors.on-primary}), weight-600 at 15px, 48px tall, {rounded.sm} radius. Hover shifts fill to {colors.primary-active} (#e0c800), a 10% darkened yellow that sustains accessible contrast on the dark text. Disabled state drains to {colors.primary-disabled} with {colors.muted} text — the shape is unchanged so disabled reads as paused rather than removed.

**`button-secondary`** — Transparent fill, 2px solid ink border, dark text; same height and radius as primary so the two sit naturally side-by-side. The `-on-dark` variant swaps border and text to white for use inside {colors.surface-dark} hero and promotional sections, enabling a yellow-primary + white-outline two-CTA pattern without a third button style.

**`button-ghost`** — Text-only, no border or fill, used for tertiary actions (skip, view all, cancel) where visual weight must fully recede from a crowded spec page.

### Inputs
**`text-input`** — White canvas fill, 1px {colors.hairline} border at rest, 2px solid {colors.primary} on focus. The yellow focus ring is the only appearance of the brand color on checkout pages, reinforcing identity at the exact moment of purchase commitment. Placeholder text uses {colors.muted}; height 48px matches button height for aligned row layouts.

### Navigation
**`nav-bar`** — White canvas at 64px tall with a 1px {colors.hairline} bottom border on light pages. The `nav-bar-dark` variant inverts to {colors.surface-dark} with white {typography.nav-link} type for hero sections that extend full-bleed to the top edge. Logo sits left-anchored; cart and account icons right-anchored with 44px tap zones.

### Product Card
**`product-card`** — White card, 1px {colors.hairline} border, {rounded.sm} corners. The image well uses {colors.surface-dark} as background fill so monitor renders on dark scenes avoid white-halo compositing artifacts. Title uses {typography.title-md} at weight 600; price uses {typography.price-display} at 28px weight 700. A {colors.primary}-filled {spec-badge} anchors bottom-left of the image well for promotional pricing, sale labels, or flagship callouts.

### Spec Badge
**`spec-badge`** — Dark fill ({colors.ink}) with yellow text ({colors.primary}), {typography.spec-label} at 11px uppercase weight 700, {rounded.xs} corners. Used inline on product cards and PDP hero rows to surface key panel specs (4K · 144Hz · HDR600) without rendering a full specification table. The dark-on-yellow inversion of the primary button creates immediate visual anchoring.

### Availability Pill
**`availability-pill`** — Full-radius pill ({rounded.full}) in {colors.success} green for in-stock status; {colors.muted} gray for out-of-stock or waitlist states. 12px caption text on dark fill. Sits directly beneath the product title on cards and the PDP hero, surfacing inventory status before price in the visual hierarchy.

### Hero
**`hero`** — Full-width {colors.surface-dark} section, minimum 560px tall to accommodate 16:9 or 21:9 monitor renders. White headline at {typography.display-xl} (48px, 700), white body copy at {typography.body-md}, and a {colors.primary}-filled CTA button. Vertical padding at {spacing.section} (64px) top and bottom. On mobile the headline drops to {typography.display-md} and the monitor render repositions below the text block.

### Feature Tile
**`feature-tile`** — {colors.surface-soft} tile with {colors.accent} cyan (#00adef) for iconography and sub-labels, {rounded.md} at 12px. Deployed in 3-column grids on product pages (Panel Technology · Color Accuracy · Response Time). The cyan accent creates a controlled 'screen-glow' association without appearing in primary interactive controls.

### Comparison Table
**`comparison-table`** — Steel-filled column headers ({colors.steel}, white {typography.spec-label} uppercase) above alternating white/soft-surface rows. The flagship or recommended column receives a 2px solid {colors.primary} left-border stripe as the only highlight mechanism — no full-cell color flood, keeping the table scannable at a glance. Horizontal scroll on tablet and mobile with sticky first column.

### Community Score
**`community-score`** — Compact {colors.steel}-fill chip, white weight-600 numerals at {typography.title-sm}, {rounded.xs} corners. Displays aggregate community rating as "9.1 / 10 · 847 reviews" on product cards and the PDP sidebar. Avoids star-icon patterns that read as third-party aggregator widgets imported from mass-market retail.

### Countdown Timer
**`countdown-timer`** — Yellow fill ({colors.primary}) with {colors.on-primary} dark text. Digit blocks use {typography.display-md} (32px, 700) with {typography.caption} labels beneath (DAYS · HRS · MIN · SEC). Used for product launch windows and limited-inventory sale events; the yellow fill makes the timer unmissable without a separate alert banner.

### Footer
**`footer`** — {colors.surface-dark} band with white section headings at {typography.title-sm} and {colors.muted-soft} (#969696) link text. The dark band flows directly from page content with no top border. Newsletter input renders as a white-canvas {text-input} inset against the dark background, retaining the yellow focus ring behavior so the brand color appears even in the footer interaction.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline drops to {typography.display-md} (32px); spec badges stack vertically below product title; comparison table becomes horizontal-scroll with sticky first column |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level links with dropdowns; hero splits text left / monitor render right at 50:50; feature tile grid drops to 2 columns |
| Desktop | 1128–1440px | 3-column product grid; full nav with mega-dropdown panel; comparison table displays all columns simultaneously; hero render scales to 60% width right-aligned |
| Wide | > 1440px | All content max-width capped at 1440px with balanced gutters; no additional grid columns; hero render gains subtle parallax offset |

### Touch Targets
- All buttons minimum 48px height; icon-only controls (cart, hamburger, account) minimum 44×44px tap zone with invisible padding extension
- Spec badges are display-only on mobile — if linked to a PDP anchor, tap zone expands to 36px height via padding
- Availability pills not tappable unless linked to waitlist flow; add {spacing.sm} padding on both axes if interactive
- Comparison table row labels on mobile get 44px tap height for row-expand interactions

### Collapsing Strategy
- Comparison table: horizontal scroll with sticky product-name first column on tablet and mobile; row-by-row swipe with momentum scroll
- Feature tile grid: 3-col → 2-col at tablet → single full-width stacked card at mobile
- Navigation mega-dropdown: full overlay panel on desktop → accordion inside hamburger drawer on mobile; steel-colored active section indicators persist across both states
- Countdown timer: 4-digit horizontal row on desktop and tablet → 2×2 grid on mobile with larger digit size to compensate for narrower viewport

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Alegreya Sans is present in extracted font stacks but may serve only body copy while display text falls back to Avenir or -apple-system; inspect loaded `@font-face` declarations at runtime to confirm weight variants (400, 600, 700) are all embedded
- Primary hover and disabled hex values (#e0c800, #f9ef9a) are interpolated from the extracted primary — actual computed values not present in the palette extraction
- The cyan accent family (#00adef, #00b3ff, #00b3ff) produced three near-identical blues; it is unclear which is the brand accent versus a payment-provider badge tint versus a partner logo; #00adef used here as best candidate
- Surface-soft is assigned #eeeeee (closest extracted match) rather than a confirmed computed value; may differ from live computed background
- Nav height (64px), card border-radius, and exact button padding are inferred from Shopify-category conventions, not confirmed from computed CSS
- Dark-mode variant palette not confirmed — Shopify platform supports it but Dough may not implement a custom dark-mode token set
- Animation and transition tokens (CTA hover fade duration, hero scroll parallax speed, countdown digit flip animation) not extractable from static snapshot
- Social icon colors (#1da1f1, #4266b2, #e50122, #f14336) included in extraction — these are third-party brand colors, not Dough palette tokens, and are excluded from the design system above
