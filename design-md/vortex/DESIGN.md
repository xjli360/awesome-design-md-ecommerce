---
version: alpha
name: "Vortex"
source_url: "https://vortexgear.tw"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four accent swatches — sage #83b579, gold #dfb52c, periwinkle #788fe2, and burgundy #93353e — map to Vortex's keycap colorways before they map to any UI convention, turning the product catalog into a color reference for enthusiasts who already know what PBT doubleshot means. The canvas flips between two registers: a warm off-white (#eeede9) for editorial and product-listing surfaces, and a near-black (#121212) for hero sections and banner moments, giving the site a film-negative quality as pages load. Manuale, a bracketed serif, carries the display headings at modest weights — its serifs echo the sculptured profile of SA and MT3 keycap rows — while Noto Sans handles body copy and spec labels in a clean, utilitarian register that won't compete with hardware photography. Rounded corners are minimal to nonexistent: product cards sit at `{rounded.xs}` (4px), buttons at `{rounded.sm}` (8px), and filter pills at `{rounded.full}` — the only soft form in the system, borrowing its pill shape from the legends printed on keycap stems. Colorway selectors use 28px circular swatches with a hairline ring that activates on selection, referencing the physical act of choosing a keycap set from a catalog. The footer runs a dark (#121212) background, anchoring the page with the same gravity as a solid aluminum board base. Accent colors appear sparingly as badge fills and active-state signals — never as background floods — preserving the palette's role as a catalog of actual products rather than a branding assertion.

colors:
  primary: "#83b579"
  primary-active: "#428445"
  primary-disabled: "#acaca2"
  ink: "#121212"
  body: "#4d4d4d"
  muted: "#9ca3af"
  hairline: "#e2e2e2"
  hairline-soft: "#ececec"
  canvas: "#eeede9"
  surface-soft: "#f5f5f5"
  surface-card: "#f3f3f3"
  on-primary: "#eeede9"
  on-dark: "#eeede9"
  dark-canvas: "#121212"
  dark-surface: "#4f4f4f"
  accent-gold: "#dfb52c"
  accent-blue: "#788fe2"
  accent-red: "#93353e"
  accent-teal: "#6e8686"
  accent-tan: "#96857d"
  error: "#ea3335"
  warning: "#f2a73b"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Manuale', 'Noto Serif JP', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Manuale', 'Noto Serif JP', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Manuale', 'Noto Serif JP', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  label-mono:
    fontFamily: "'Consolas', 'Liberation Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Manuale', Georgia, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Noto Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  announcement-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: "8px {spacing.lg}"
    textAlign: center
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  colorway-swatch:
    shape: circle
    size: 28px
    border: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    rounded: "{rounded.full}"
    gap: "{spacing.xs}"
  keycap-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
  filter-pill:
    backgroundColor: transparent
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelTypography: "{typography.title-sm}"
    valueTypography: "{typography.body-sm}"
    monoTypography: "{typography.label-mono}"
    rowBorder: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} {spacing.base}"
  accent-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accent-badge-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accent-badge-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accent-badge-sage:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Sage green (#83b579) fill with warm off-white (#eeede9) text, 8px radius, 44px tall. The green signals an affirmative action without the urgency of red or the convention of blue; hover/active deepens to #428445 (`{colors.primary-active}`), a forest-floor shift that reads as physically pressing. On dark hero backgrounds, `button-dark` replaces it — near-black fill on dark ground — reserving the sage for product-page CTAs where it reads most clearly against the warm canvas.

**`button-secondary`** — Transparent ground with a 1.5px ink border, same height and radius as primary. Used for secondary catalog actions ("Compare", "Add to Wishlist") where hierarchy must defer to the sage CTA without disappearing entirely.

**`button-ghost`** — No border, sage (#83b579) text on transparent ground. Used inline for "See All" expansions, pagination links, and within-section navigational nudges.

### Navigation
**`nav-bar`** — 60px tall on the warm #eeede9 canvas with a single 1px #e2e2e2 hairline underline. Links use `{typography.nav-link}` (Noto Sans 14px/500). A mega-dropdown for product categories deploys as a full-width overlay panel with a product grid inside. `nav-bar-dark` swaps to #121212 on pages where the hero image bleeds to the viewport top edge, maintaining contrast without a visible bar seam.

### Product Card
**`product-card`** — Surface-card (#f3f3f3) ground, 4px radius, 4:3 image aspect ratio to frame keyboard photography consistently across landscape board shots. Title in `{typography.title-md}`, price in `{typography.price-display}` (Manuale serif 20px/700) — the serif face on the price gives it a distinct register from the utility labels around it. A colorway swatch row appears below the title when multiple colorways exist; a `keycap-badge` strip lists switch type below the swatches in monospace.

### Colorway Swatch
**`colorway-swatch`** — 28px circles spaced 4px apart in a horizontal row. The selected swatch gains a 2px ink-colored outline ring; unselected swatches carry a transparent border that transitions to the hairline color on hover. Colors are filled with actual colorway hex values drawn from the accent palette (gold, periwinkle, sage, burgundy) or custom colorway-specific colors. On mobile the circles expand to 36px for thumb accuracy.

### Keycap Badge
**`keycap-badge`** — Monospace `{typography.label-mono}` chip on soft surface (#f5f5f5) with a 1px hairline border and 4px radius. Used for switch type ("Cherry MX Blue"), layout shorthand ("75%", "65%", "TKL"), and material callouts ("PBT", "ABS"). The monospace face connects to terminal and typewriter culture native to the mechanical keyboard community, making specs feel like they belong in a datasheet rather than a marketing brochure.

### Accent Badges
**`accent-badge-gold`**, **`accent-badge-blue`**, **`accent-badge-red`**, **`accent-badge-sage`** — Four chip variants corresponding to the four keycap-colorway accent colors. Gold (#dfb52c) uses ink text for contrast; blue, red, and sage use off-white. Applied as small product-page tags for limited editions, new arrivals, and colorway-specific callouts. Never used as background surface floods — badge size is the boundary of their use.

### Filter Pills
**`filter-pill`** and **`filter-pill-active`** — Full-radius pills for catalog facet filtering across switch type, form factor, and layout. Inactive state is a hairline-bordered ghost on warm canvas; active state flips to ink (#121212) fill with off-white text. The binary selected/unselected read is unambiguous without using the brand green, which is reserved for primary CTAs.

### Spec Table
**`spec-table`** — Two-column label/value layout on surface-card (#f3f3f3) with hairline-soft (#ececec) row dividers. Labels in `{typography.title-sm}` (Noto Sans 14px/600); prose values in `{typography.body-sm}`; technical values (actuation force, travel distance, PCB dimensions) in `{typography.label-mono}` for immediate visual differentiation from prose. Row padding 12px vertical × 16px horizontal — dense enough for a spec sheet, open enough to scan without a ruler.

### Hero Banner
**`hero-banner`** — Near-black (#121212) ground, minimum 560px tall. Heading in `{typography.display-xl}` (Manuale 48px/700) in warm off-white; body in `{typography.body-md}`. The dark ground maximizes contrast for lit keycap photography, particularly for colorway launches where the keycap color is the hero. CTA is either `button-primary` (sage green) or `button-dark` depending on surrounding hierarchy.

### Announcement Bar
**`announcement-bar`** — Full-width strip in #121212 with caption-size warm off-white text, centered. Used for shipping thresholds, limited-run notices, and new-arrival drops. No dismiss button by default; collapses to a single horizontally scrolling marquee line below 744px.

### Footer
**`footer`** — Dark (#121212) ground with body-sm links in muted (#9ca3af), organized in a 4-column grid on desktop (Products, Support, Community, About). The dark footer anchors the page with the same visual weight as a solid aluminum board base — a deliberate echo of the hardware the brand sells. Copyright and legal lines use `{typography.caption}` in the same muted gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero min-height drops to 360px; announcement bar becomes scrolling marquee; spec table stacks label above value full-width; colorway swatches expand to 36px |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level items, sub-menus in slide-over drawer; hero scales to 460px; filter pills scroll horizontally below search bar |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with mega-dropdown overlay; hero 560px; filter sidebar appears left of catalog grid |
| Wide | > 1440px | Layout caps at 1440px max-width with auto margins; hero image scales to fill; type sizes unchanged — no fluid scaling applied |

### Touch Targets
- All buttons minimum 44×44px on mobile
- Colorway swatches expand from 28px to 36px on touch viewports
- Filter pills minimum 36px tall, scrollable row with 8px gap between chips
- Nav hamburger icon 44×44px tap target
- Keycap badges are display-only; no interactive tap target required

### Collapsing Strategy
- Desktop filter sidebar collapses to a "Filter" modal sheet on mobile and tablet
- Spec table on mobile: label row stacked above value row as paired full-width blocks
- Colorway swatch row wraps to a second line if more than 6 variants exist
- Announcement bar text truncates to single marquee line below 744px
- Footer 4-column grid → 2-column at tablet → single-column accordion at mobile with collapsed sections

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font confirmed; Manuale and Noto Sans are inferred from extracted font-family stacks but weight variants (italic, condensed) are unverified
- Button border-radius not pixel-confirmed from extraction; `{rounded.sm}` (8px) inferred from hardware-category Shopify theme conventions
- Hover transition timing not extracted; 150ms ease assumed throughout
- Dark mode or theme toggle behavior unknown — site may be static single-register
- Currency display format (TWD / USD toggle) and locale-switching UI not confirmed
- Checkout, cart drawer, and account page styling not extracted — component specs apply to catalog and PDP surfaces only
- Icon system unidentified; no SVG sprite or icon font detected in extraction
- Exact mega-dropdown column structure and product-hierarchy depth not confirmed
- Whether #788fe2, #93353e, and #dfb52c are persistent brand accent colors or per-product colorway fills is ambiguous from extraction alone
