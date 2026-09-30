---
version: alpha
name: "Click and Grow"
source_url: "https://www.clickandgrow.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Click and Grow's most telling choice is treating terracotta — the literal clay-pot color (#b23f0d) — as its primary action voltage, in a category where competitors default to the predictable bottle-green. The rest of the palette reads like a vertical soil sample: dark olive depths (#43431e, #34312e), warm cream at the surface (#fcfaf6, #f0ebe1), and an arresting chartreuse spike (#dcea54) that appears only when something is growing, rewarded, or on sale. These aren't chosen for decoration — they map to the physical objects the brand sells, making the palette feel inevitable rather than styled. New Spirit Condensed occupies the display register, a bracketed serif that opens like a seed catalog printed on uncoated stock. Headlines at 56–72px with moderate weight (600) hold a horticultural earnestness without tipping into nostalgia. Figtree handles everything interactive and informational — its soft apertures and generous x-height suit the accessible, kitchen-counter mood of indoor growing kits. There is no aggressive type contrast: the system leans on spacing and color bands rather than weight swings to create hierarchy. Cards sit on warm parchment (#f0ebe1) with `{rounded.md}` corners, leaving enough roundness to feel organic without dissolving into the pill-heavy language of wellness brands. The chartreuse (#dcea54) is rationed: it signals grow-phase progress, highlights ecological claims, and surfaces on hover states for sustainability callouts — never as a primary button, always as a moment of biological emphasis. Dark soil-toned bands (#34312e) break the page into sections, alternating warmth and depth without decoration — the typographic equivalent of turning a compost row. Navigation runs lean: a sticky cream bar, text-only category links, the cart reduced to a number. Pricing and grow-kit specs in Figtree medium at 13–14px, separated by `{colors.hairline}` rules. No gratuitous animation, no parallax theater — the interface clears a path to the physical object and steps aside.

colors:
  primary: "#b23f0d"
  primary-active: "#8a2e08"
  primary-disabled: "#e8b89e"
  ink: "#141416"
  body: "#34312e"
  muted: "#84817e"
  hairline: "#dedede"
  hairline-soft: "#e1dbd0"
  canvas: "#fcfaf6"
  surface-soft: "#f0ebe1"
  surface-card: "#fafad5"
  on-primary: "#fcfaf6"
  growth: "#dcea54"
  growth-dark: "#43431e"
  parchment: "#f4f1c9"
  parchment-mid: "#efeba3"
  earth: "#6b5a3e"
  soil: "#34312e"
  soil-deep: "#2f2c28"
  forest: "#414f33"
  olive: "#4e4e26"
  olive-mid: "#6a6a3f"
  wine: "#81354b"
  amber: "#f49a13"
  amber-light: "#ff8329"
  blue-accent: "#338fb1"
  on-dark: "#fcfaf6"

typography:
  display-xl:
    fontFamily: "'new-spirit-condensed', 'new-spirit', Georgia, serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -1px
  display-lg:
    fontFamily: "'new-spirit-condensed', 'new-spirit', Georgia, serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'new-spirit', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'new-spirit', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-xs:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  badge-label:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  button-md:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Figtree', 'hanken-grotesk', Inter, sans-serif"
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  button-growth-accent:
    backgroundColor: "{colors.growth}"
    textColor: "{colors.growth-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    position: sticky
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    imageRounded: "{rounded.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    ctaSpacing: "{spacing.lg}"
  soil-band:
    backgroundColor: "{colors.soil}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  grow-kit-badge:
    backgroundColor: "{colors.growth}"
    textColor: "{colors.growth-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  sustainability-badge:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  seed-count-tag:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.earth}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  grow-phase-indicator:
    trackColor: "{colors.parchment-mid}"
    fillColor: "{colors.growth}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 6px
  collection-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    width: 400px
  botanical-spec-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelTypography: "{typography.label-xs}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.soil-deep}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.amber}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The terracotta CTA, #b23f0d fill with warm cream text on a softly rounded ({rounded.sm}) 48px-tall target. Hover deepens to `{colors.primary-active}` (#8a2e08); disabled washes to a muted clay (#e8b89e) that retains the same rounded form. Padding is generous at 14px vertical / 28px horizontal to give the earthy hue room to read on cream backgrounds.

**`button-secondary`** — Cream canvas with a 1.5px terracotta border and terracotta type, same geometry as primary. Signals an alternative action without competing visually — useful for "Add to Wishlist" or "View All" alongside a primary "Shop Now."

**`button-ghost`** — Transparent background, `{colors.body}` text, no border. Used for tertiary actions inside cards and within grow-phase UI where visual noise must stay minimal.

**`button-growth-accent`** — Chartreuse (#dcea54) fill with dark olive text, reserved for ecological milestones, seasonal promotions, and grow-phase completion calls to action. Never used as a default CTA — its brightness is earned context.

### Inputs

**`text-input`** — Warm canvas background, hairline border at rest, terracotta border on focus. Figtree body-md at 16px. 48px height matches button height for inline form rows (email capture, search). Placeholder in `{colors.muted}`.

### Navigation

**`nav-bar`** — Sticky cream bar, 64px tall, hairline-soft bottom border. Text links in Figtree 500 weight, 15px. Cart rendered as a numeric badge over a minimal icon; no hamburger animation on desktop. The simplicity is deliberate — the brand image carries emotional weight; the nav stays out of the way.

### Product Cards

**`product-card`** — Warm parchment (#f0ebe1) surface, {rounded.md} corners, 16px padding on all sides. Product image fills the top in a 4:3 aspect ratio with {rounded.sm} corners. Title in `{typography.title-sm}`, price in `{typography.price-display}` (bold, 18px). A `grow-kit-badge` in chartreuse floats top-left when the kit includes a smart soil pod. Cards cast a subtle shadow on hover (0 4px 16px rgba(52,49,46,0.10)).

### Hero

**`hero`** — Warm surface-soft background, New Spirit Condensed headline at 64px/600 weight, subhead in New Spirit regular at 24px. CTA row uses `button-primary` left-aligned with optional `button-secondary` beside it. Section padding {spacing.section} top and bottom. On mobile the headline collapses to `{typography.display-lg}`.

### Soil Bands

**`soil-band`** — Full-bleed dark (#34312e) sections that separate product rows. Headline in New Spirit 36px/500 weight in `{colors.canvas}`, body in Figtree 16px. These sections carry editorial copy about sustainability, certifications, and the brand's plant-science story. They create visual rhythm without imagery.

### Badges & Tags

**`grow-kit-badge`** — Chartreuse pill ({rounded.full}), dark olive text, 12px Figtree semibold. Labels kit inclusions ("Smart Soil", "3-Pod Kit"). Rarely used; its brightness punches hard against the muted card backgrounds.

**`sustainability-badge`** — Forest green pill, cream text, same geometry as grow-kit-badge. Marks certified organic, plastic-neutral, and carbon-offset claims.

**`seed-count-tag`** — Parchment (#f4f1c9) rectangle with {rounded.xs}, uppercase Figtree at 11px/600 in `{colors.earth}`. Used inside product cards to show pod count or seed variety.

### Grow Phase Indicator

**`grow-phase-indicator`** — A 6px-tall progress bar in `{colors.parchment-mid}` track, filled in chartreuse. Used on grow-kit landing pages and account dashboards to show germination → seedling → harvest phase. Labeled above in `{typography.caption}` muted text. {rounded.full} on both track and fill.

### Collection Filter

**`collection-filter-chip`** — Pill-shaped chips ({rounded.full}) in warm surface-soft at rest, terracotta fill when active. Figtree caption (13px) text. Used in the shop collection header row for filtering by plant type (herbs, vegetables, fruits, flowers). Active state uses `{colors.primary}` + `{colors.on-primary}`.

### Cart Drawer

**`cart-drawer`** — Slides in from the right, 400px wide on desktop. Canvas background, hairline-soft left border. Line items in Figtree body-sm, prices in price-display. Checkout CTA uses full-width `button-primary` pinned to the bottom of the drawer.

### Botanical Spec Row

**`botanical-spec-row`** — Used in product detail pages to list grow specs (light needs, water frequency, grow time, pod count). Surface-card (#fafad5) background rows, label in label-xs uppercase muted, value in body-sm. Hairline bottom border between rows, 8px/16px padding.

### Footer

**`footer`** — Deep soil (#2f2c28) background, warm surface-soft text, amber (#f49a13) link color. Figtree body-sm for body copy, caption for nav links. Three columns: product links, sustainability links, support — collapsing to accordion panels on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to display-lg (48px); nav-bar collapses to logo + hamburger + cart count; collection filter chips scroll horizontally; cart-drawer goes full-width; soil-bands reduce to {spacing.xl} padding |
| Tablet | 744–1128px | Two-column product grid; hero switches to side-by-side image/text split; nav expands but secondary links may hide behind "More" overflow; filter chips wrap rather than scroll |
| Desktop | 1128–1440px | Three-column product grid; sticky nav shows all categories; hero at full 64px display-xl; soil-band editorial copy limited to 640px max-width centered |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centers all content; hero background image bleeds edge-to-edge while content stays in grid; footer shifts to five-column layout |

### Touch Targets

- All buttons minimum 48px height, 44px minimum width
- Filter chips minimum 36px height with 12px horizontal padding
- Nav links in mobile hamburger drawer minimum 52px tap row height
- Cart icon tap area padded to 44×44px regardless of visible icon size
- Grow-phase indicator includes a 32px-tall interaction zone above the 6px visual bar

### Collapsing Strategy

- Product card grid: 4 → 3 → 2 → 1 columns as breakpoints descend
- Hero layout: side-by-side (desktop) → stacked image-above-text (mobile), image aspect ratio fixed at 16:9
- Footer: multi-column grid → stacked accordion with terracotta expand/collapse arrows on mobile
- Botanical spec rows: table layout on desktop → definition list with label above value on mobile
- Collection filters: horizontal flex row with overflow-x scroll and fade-out mask at edges on mobile
- Soil band typography: display-md (36px) → display-sm (24px) on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius in production may differ from the {rounded.sm} (8px) inference — the Shopify theme may override to 4px or 6px; verify in computed styles
- New Spirit and New Spirit Condensed license details not confirmed; fallback to Georgia/serif may display differently than the live site
- Animation/transition values (hover timing, drawer slide duration) not extractable from static hex analysis
- Dark-mode palette not observed — the extracted colors suggest a light-only theme but no explicit `prefers-color-scheme` data was captured
- Icon set (nav icons, grow-phase icons, sustainability glyphs) not described — brand likely uses a custom SVG library not derivable from color extraction
- Mobile navigation pattern (hamburger vs. tab bar vs. scrollable top nav) not confirmed from extraction
- Exact product card shadow values not extracted; the 0 4px 16px estimate is inferred from the warm palette logic
- wine (#81354b) token extracted but no clear UI role confirmed — possibly used for sale-price text or limited-edition product accents
