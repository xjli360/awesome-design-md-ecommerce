---
version: alpha
name: "Apex"
source_url: "https://apexride.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A 3px crimson left-border accent — and nothing else — separates a scheduled workout from a product tile in Apex's library. That single mark does the taxonomic work that another brand would assign to color fills, background swaps, or icon sets, and it reveals the design logic operating underneath the entire system: maximum signal, minimum surface. The canvas runs near-black (#0A0A0A), dark enough that product photography reads as emitted light rather than reflected; component surfaces step up in 8–10 luminance points at a time ({colors.surface-soft}, {colors.surface-card}), creating a depth hierarchy that feels like instrument layers on a head-unit display rather than a conventional page stack. Into that compressed field, a single performance-red primary (#FF2D20) carries every CTA, active pill, data-accent, and progress-fill — there is no secondary brand hue, no gradient, no tint palette. Secondary actions defer to white outlines on the dark field, and the outline disappears entirely for ghost variants that only need a red text label. Typography runs in two registers: a condensed grotesque at heavy weight and wide uppercase tracking for display and button copy — the kind of letterform that reads at sprint pace on a class-room screen — and a monospaced data stack for wattage figures, resistance percentages, and session counts. The condensed display scale starts at 80px on desktop (weight 800, uppercase, −1.5px letter-spacing) and compresses to 40px at mobile, maintaining optical mass at every breakpoint. The monospaced data-readout (32px, weight 700) sits beside the prose stack on product detail pages, giving specs the instrument-panel authority that raw text weight cannot provide. Corner radii are minimal: {rounded.xs} (4px) on buttons and inputs signals engineering precision; {rounded.md} (12px) on cards adds enough curve to prevent the grid from reading as a dashboard error panel. Spacing pulses between tight component density and generous {spacing.section} (64px) section breaks, structuring the page like an interval session — compressed effort, deliberate recovery. Badge language is blunt and uppercase: RIDE, TRAIN, COMPETE — no subtitle, no icon, no soft qualifier anywhere in the system.

colors:
  primary: "#FF2D20"
  primary-active: "#CC1A0F"
  primary-disabled: "#7A1A13"
  ink: "#FFFFFF"
  body: "#E0E0E0"
  muted: "#9A9A9A"
  hairline: "#2A2A2A"
  canvas: "#0A0A0A"
  surface-soft: "#141414"
  surface-card: "#1C1C1C"
  on-primary: "#FFFFFF"
  data-positive: "#22C55E"
  data-warning: "#F59E0B"
  data-mono: "#94A3B8"
  scrim: "rgba(10,10,10,0.55)"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Impact, sans-serif"
    fontSize: 80px
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -1.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Barlow', 'Inter', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', 'Inter', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Barlow', 'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  data-readout:
    fontFamily: "'Roboto Mono', 'JetBrains Mono', 'Courier New', monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  data-label:
    fontFamily: "'Roboto Mono', 'JetBrains Mono', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow Condensed', 'Barlow', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', 'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Barlow', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 14px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageAspect: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeRounded: "{rounded.xs}"
    badgeTypography: "{typography.badge}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "{colors.scrim}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  stat-badge:
    backgroundColor: "{colors.surface-soft}"
    valueColor: "{colors.data-positive}"
    labelColor: "{colors.data-mono}"
    valueTypography: "{typography.data-readout}"
    labelTypography: "{typography.data-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  workout-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    accentBorder: "3px solid {colors.primary}"
    accentSide: left
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.base}"
  performance-meter:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    trackHeight: 4px
    valueTypography: "{typography.data-readout}"
    valueColor: "{colors.data-mono}"
    labelTypography: "{typography.data-label}"
    labelColor: "{colors.muted}"
  testimonial-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    accentBorder: "2px solid {colors.primary}"
    accentSide: left
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — A full-bleed performance-red (#FF2D20) block using `{typography.button-md}` (uppercase, 1.5px letter-spacing), which gives short labels like "RIDE NOW" a billboard presence even at 48px height. Active state compresses to `{colors.primary-active}` (#CC1A0F) with no easing delay — the response reads as mechanical, not animated. Disabled state uses `{colors.primary-disabled}`, a dark muted crimson that signals unavailability without a generic gray. The `{rounded.xs}` (4px) radius is the tightest curve in the component system.

**`button-secondary`** — Transparent field with a 1px `{colors.ink}` stroke on the dark canvas. Uses the same `{typography.button-md}` uppercase stack as primary, maintaining command hierarchy: red fills primary actions, white outlines secondary ones. Hover state intensifies the stroke to full white but never fills. Padding is inset 1px on each axis to optically match the primary height without the fill.

**`button-ghost`** — Transparent with `{colors.primary}` stroke and label. Used for in-content CTAs within dark surface tiles where a red fill would dissolve into product photography. On hover, the background receives `{colors.primary}` at ~12% opacity — a blush of commitment before the click confirms.

### Navigation

**`nav-bar`** — 68px height, `{colors.canvas}` (#0A0A0A) fill, with a single 1px `{colors.hairline}` bottom border that delineates chrome from page content without adding luminance or shadow. Logo anchors left; nav links in `{typography.nav-link}` (14px, weight 600, 0.5px tracking) run center or right depending on link count; a `button-primary` CTA locks the far-right position. No dropdown mega-menu — category navigation is delegated to inline pill filters on collection pages.

### Product Card

**`product-card`** — `{colors.surface-card}` (#1C1C1C) container, `{rounded.md}` corners, 4:3 image crop that privileges studio machine photography. Title renders in `{typography.title-md}` (18px, weight 600); price in `{typography.title-sm}` at `{colors.body}`. A `{typography.badge}` capsule in `{colors.primary}` with `{rounded.xs}` sits top-left of the image on new or promoted SKUs. On hover, a 2px `{colors.primary}` bottom border emerges on the card — the sole card animation, marking the intent boundary precisely.

### Hero Banner

**`hero-banner`** — Full-width, full-bleed image with a 55% dark scrim (`{colors.scrim}`) preserving the photographic subject while giving the headline contrast to render in pure `{colors.ink}` at `{typography.display-xl}` scale (80px, weight 800, uppercase). Section padding is `{spacing.section}` (64px) top and bottom on desktop, collapsing to `{spacing.xxl}` (48px) on mobile. A single `button-primary` CTA lives at the base of the headline block; no secondary action is placed in the hero.

### Stat Badge

**`stat-badge`** — Instrument-panel tiles that surface live performance metrics: average watts, resistance range, session count. Value renders in `{typography.data-readout}` (32px monospace, weight 700) in `{colors.data-positive}` when the figure represents a live or improving metric; static specs render in `{colors.data-mono}`. Label below in `{typography.data-label}` (11px monospace uppercase). The `{colors.hairline}` 1px border separates the tile from the dark surface without shadow or elevation; tiles are flush-radius `{rounded.sm}` to keep the instrument-panel register.

### Workout Card

**`workout-card`** — A `{colors.surface-card}` tile distinguished from the product card by a 3px `{colors.primary}` left-border accent and a 1px `{colors.hairline}` perimeter stroke. Title in `{typography.title-md}`; metadata (duration, intensity tier, instructor name) in `{typography.caption}` at `{colors.muted}`. The left-border accent orients workout tiles as sequential schedule entries rather than shoppable products — the same red mark used in testimonials creates a visual grammar of annotation versus product display.

### Category Pill

**`category-pill`** — `{rounded.full}` filter chips for collection and program filtering. Inactive: `{colors.surface-soft}` fill, `{colors.body}` label at `{typography.badge}` uppercase. Active: `{colors.primary}` fill, `{colors.on-primary}` label. No border in either state; color swap is the entire state indicator. On mobile, chips snap-scroll horizontally on a single line without a fade mask, giving full access at one swipe cost.

### Performance Meter

**`performance-meter`** — A 4px-tall progress track used in product spec tables and workout previews to express resistance range, cadence ceiling, or completion percentage. Track is `{colors.hairline}`; fill is `{colors.primary}`. The numeric value renders in `{typography.data-readout}` above the track in `{colors.data-mono}`; the descriptor sits beside it in `{typography.data-label}`. The bar does not animate on page load — static state only, consistent with dashboard instrument convention where animated bars would read as errors.

### Testimonial Block

**`testimonial-block`** — `{colors.surface-soft}` tile, `{rounded.md}` corners, `{spacing.xl}` (32px) all-side padding. A 2px `{colors.primary}` left-border accent precedes the pull-quote in `{typography.body-md}`. Author attribution in `{typography.caption}` at `{colors.muted}`. Blocks lay out in a 3-column grid on desktop; collapse to 2 columns at tablet; stack single-column on mobile. The shared left-accent language with `workout-card` creates a consistent mark that signals "person speaking" across the system.

### Footer

**`footer`** — `{colors.surface-soft}` (#141414) background with a single `{colors.hairline}` top border. Link columns render in `{typography.body-sm}` at `{colors.body}`; hover state transitions to `{colors.primary}` — the only footer animation. Legal copy and copyright in `{typography.caption}` at `{colors.muted}`. `{spacing.section}` (64px) vertical padding maintains breathing room even on a dense link column grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; `display-xl` scales from 80px to 40px; hero padding collapses to `{spacing.xxl}` (48px); category pills snap-scroll horizontally; nav collapses to hamburger drawer + logo + `button-primary` in top bar |
| Tablet | 744–1128px | 2-column product grid; `display-xl` at 56px; hero sub-headline visible; nav shows 3–4 links with overflow hidden; stat badge row at 2-across |
| Desktop | 1128–1440px | 3–4 column product grid; full nav bar at 68px; `display-xl` at 80px full letter-spacing; stat badges in 4-across horizontal row; testimonials 3-column |
| Wide | > 1440px | Content-width container capped at 1440px and centered; canvas bleeds full viewport width; hero image maintains full-bleed with fixed scrim ratio; no further type scaling |

### Touch Targets

- All interactive elements minimum 44×44px touch area
- `button-primary` and `button-secondary` fixed at 48px height; padding adjusts for label length
- Category pills minimum 36px height on mobile; horizontal padding increased to 8px 16px
- Nav hamburger icon has 44×44px invisible tap extension beyond the visible glyph
- Product card tap area spans the full card surface, not just image or title text
- Performance meter track is non-interactive; associated CTA button handles the tap zone

### Collapsing Strategy

- Primary nav collapses at < 1024px into a right-side slide-out drawer; `button-primary` CTA remains visible in the fixed top bar at all times
- Stat badge row: 4-across on desktop → 2-across on tablet → 2-across horizontally scrollable on mobile
- Testimonial grid: 3 columns → 2 columns at tablet → 1 column stacked on mobile
- Workout card list maintains single-column at all breakpoints; card width is 100% of its column
- Footer link columns: 4 across on desktop → 2 across on tablet → accordion disclosure per column on mobile
- Hero typography: `display-xl` scales linearly; sub-headline body text is hidden at < 744px to avoid text collision with the compressed layout

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The site returned no CSS custom properties, inline color values, or computable theme tokens. Every hex value in this spec is inferred from performance fitness and indoor cycling category norms — not sourced from apexride.com. Verify and replace all palette values from live computed styles or an official brand kit before production use.
- **No font stacks extracted**: Zero font-family declarations were captured. The `'Barlow Condensed'`/`'Barlow'` display-and-body pairing and the `'Roboto Mono'` data stack are inferred from athletic brand category conventions. Inspect actual font requests (network waterfall, `document.fonts.ready`) on the live site to confirm.
- **No theme-color meta tag**: The `<meta name="theme-color">` was absent, so the primary accent cannot be cross-referenced against any browser-chrome color signal.
- **Shopify platform unconfirmed**: The platform flag returned false; component conventions for cart drawer, collection filters, and product form cannot be cross-referenced against Shopify theme defaults to separate framework markup from brand decisions.
- **Logo mark geometry unknown**: Whether Apex uses a wordmark, an icon-plus-wordmark, or an animated logotype is unconfirmed; nav-bar height (68px) may need adjustment to accommodate the actual logo bounding box.
- **Icon library style unconfirmed**: The decorative icon set style — outline, filled, duotone, or custom glyph — is unknown and not specified here.
- **Motion language absent**: Transition easing curves, animation durations, and scroll-triggered behavior patterns could not be extracted. The spec defaults to instantaneous state changes; layer in easing curves and duration tokens once audited from live CSS or a motion guidelines document.
- **Dark-mode vs. default mode ambiguity**: It is unconfirmed whether the dark canvas is the brand's only mode or the default of two (light/dark). If a light mode exists, a parallel surface token set will be required.
