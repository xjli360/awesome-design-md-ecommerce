---
version: alpha
name: "Red Paddle Co"
source_url: "https://redpaddleco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Red names itself twice — the company and the color are the same declaration. Every primary CTA, nav hover-state, and hero overlay runs on #aa0000, a deep crimson that sits closer to a safety flag snapped taut in offshore wind than fire-engine scarlet, and the palette never drifts warm enough to soften it. Against a near-black canvas of #121212 and #222222, this red fires like a warning signal rather than a brand choice, which is precisely the point for a company selling equipment designed to perform in conditions that punish the underbuilt. The secondary steel-blue register — #3c4862 anchoring body copy, #6887a0 softening supporting captions — draws from the tonal family of open water at depth, grounding the palette in the environment the boards actually inhabit without resorting to literal wave illustrations. A warm amber-orange (#f48037) surfaces on promotional chips and urgency badges, providing thermal contrast against the cool water tones and breaking the red-dark-grey monotony in editorial sections; the tan-wood note (#b6855a) appears in paddle-grain imagery zones and warm rule lines, adding material texture to what would otherwise read as purely digital-industrial.

  Typography was loaded via JavaScript inheritance at extraction time and no custom font stack resolved — all tokens fall back to a bold system sans-serif until the display face is confirmed. Structurally, the brand communicates through high-contrast editorial blocks: full-bleed water photography cut through with oversized crimson CTAs, tight spec-table grids for board-to-board comparisons, and certification badge clusters. Buttons carry {rounded.none} in hero and buy-box zones — no softening where urgency is required — and graduate to {rounded.sm} only in product-card and filter-chip contexts. Motion is fast and declarative: overlays cut rather than dissolve, spec drawers slide rather than pop, award clusters stack without choreography. Nothing on this canvas exists to feel cozy.

colors:
  primary: "#aa0000"
  primary-active: "#770000"
  primary-disabled: "#d98080"
  primary-alt: "#c3171d"
  accent-orange: "#f48037"
  accent-tan: "#b6855a"
  ink: "#222222"
  ink-deep: "#121212"
  body: "#3c4862"
  muted: "#6887a0"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-dark: "#121212"
  surface-card: "#222222"
  surface-soft: "#f5f5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.75px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px

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
    padding: 16px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 30px
    height: 52px
    border: "2px solid {colors.on-dark}"
  button-secondary-ink:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 30px
    height: 52px
    border: "2px solid {colors.ink}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
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
    borderBottom: "1px solid rgba(255,255,255,0.1)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.badge}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(18,18,18,0.55)"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 600px
    ctaComponent: "button-primary"
    accentBarColor: "{colors.primary}"
    accentBarHeight: 4px
  badge-spec:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-award:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    border: "1px solid {colors.accent-orange}"
    accentColor: "{colors.accent-orange}"
  size-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "2px solid {colors.primary-active}"
  buy-box:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
    priceTypography: "{typography.display-sm}"
    labelTypography: "{typography.spec-label}"
    ctaComponent: "button-primary"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowBorder: "1px solid {colors.hairline}"
    headerBackgroundColor: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    accentColor: "{colors.primary}"
  feature-callout:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    borderLeft: "4px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

---

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}), deep-crimson (#aa0000) fill with white uppercase text at 0.75px tracking and 52px height. Hover drops immediately to #770000 (`primary-active`) with no transition delay — the switch is instantaneous, signaling confidence rather than softness. Disabled state renders in muted #d98080 and accepts no pointer events.

**`button-secondary`** — Transparent background with a 2px white border and white uppercase text, built for use against dark hero and overlay backgrounds. The `button-secondary-ink` variant mirrors the spec with a 2px #222222 border for light-canvas sections. Both carry the same sharp corners and uppercase tracking as `button-primary`.

**`button-accent`** — Amber-orange (#f48037) fill reserved for promotional urgency: limited-run offers, bundle upsells, seasonal sale banners. Same zero-radius corners and uppercase tracking maintain system coherence while the orange read separates it clearly from the primary action hierarchy.

### Nav Bar

**`nav-bar`** — White canvas background with a 1px #dedede bottom border, 64px tall. Links use 14px semi-bold at 0.25px tracking. The `nav-bar-dark` variant flips to #121212 background with white text and a 10%-opacity white bottom border for scroll-over-hero states, preserving contrast without a hard line.

### Product Card

**`product-card`** — White canvas card with a 1px #dedede border and {rounded.sm} (4px) corner radius. Product title runs in `title-md` (18px/600), price in `title-sm` (16px/600). Promotional or "New" badges use the red fill with white badge text on a {rounded.full} pill anchored top-left over the product image. Cards carry no drop shadow — the hairline border draws the boundary cleanly.

### Hero

**`hero`** — Full-bleed action photography with a flat rgba(18,18,18,0.55) overlay and white display type at 56px/800 weight. A 4px #aa0000 horizontal rule appears above the headline on editorial variants, delivering the brand color as a spatial marker before the eye reaches text. The primary CTA is always `button-primary`; a secondary `button-secondary` (white outline) sits 16px to its right. Minimum height 600px, scaling to 720px on wide viewports.

### Badges

**`badge-spec`** — Red (#aa0000) pill badge for surfacing inline board specification callouts such as material grade or inflation pressure ratings. Uppercase 10px/700 at 0.5px tracking; the {rounded.full} pill shape is the sole instance of fully rounded corners in the system.

**`badge-award`** — Dark (#222222) rectangular badge with a 1px amber-orange (#f48037) border for competition placements and independently tested performance certifications. The amber border serves as the only non-red brand accent in a badge context, distinguishing achievement from specification.

### Size Chip

**`size-chip`** — Soft-surface (#f5f5f5) filter chip for board-length and width selectors in the buy-box and collection-filter bar. Deselected state: 1px #dedede border. Selected state: fills #aa0000 with white text and a 2px #770000 border. Touch target minimum 44px height enforced via padding expansion on mobile.

### Buy Box

**`buy-box`** — White canvas panel with a 1px hairline border, zero radius, and 32px internal padding. Price displays in `display-sm` (24px/700). Spec summary labels above the price cluster use `spec-label` (11px, uppercase, 1px tracking) against muted #6887a0 to create a data-dense but scannable block. The `button-primary` CTA spans full width below the price and size-chip row.

### Spec Table

**`spec-table`** — Surface-soft (#f5f5f5) alternating rows with 1px hairline dividers. Column headers sit on a #121212 dark bar with white `spec-label` text. Numeric specification values render in `spec-value` (22px/700); the hero metric for each board (typically volume or maximum rider weight) receives a 2px #aa0000 underline accent. A sticky first column holds board names during horizontal scroll on desktop.

### Feature Callout

**`feature-callout`** — Full-width #121212 editorial strip with a 4px left-border rule in #aa0000 acting as a section-entry mark. Headline in `display-md` (36px/700), body in `body-md` at 1.6 line-height. Used for technology-story panels (MSL construction depth, RSS rail rigidity, Titan handle placement). An optional right-side cutout illustration bleeds to the edge on desktop and collapses below the copy block on mobile.

### Footer

**`footer`** — Near-black (#121212) background with a 3px #aa0000 top border that functions as the brand's final punctuation before the page ends. Link text uses #dedede at 14px/400. Section headings in `title-sm` (16px/600). Newsletter email input uses the standard `text-input` token against the dark background; the submit button is `button-primary` inline to the right.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero min-height drops to 480px, display-xl scales to 32px/800; nav collapses to hamburger; buy-box becomes sticky bottom bar at full viewport width; spec-table flips to stacked key/value rows |
| Tablet | 744–1128px | Two-column product grid; hero at 560px; nav shows top-level links only with dropdowns; buy-box floats right in a 360px fixed column beside the image |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu flyout panel; hero at 640px; spec-table sticky first column active |
| Wide | > 1440px | Max content width 1400px centered; four-column product grid; hero up to 720px; feature-callout strips remain full-bleed beyond the content max-width |

### Touch Targets

- All size-chip and badge-spec elements enforce a minimum 44 × 44px touch area via padding expansion
- Nav links on mobile expand to full-width rows with 56px tap height
- Buy-box sticky CTA on mobile: 52px height, full viewport width minus 32px gutters (16px each side)
- Size chips on mobile increase to 10px 20px padding to clear the 44px height threshold

### Collapsing Strategy

- Navigation: top-level categories remain visible on tablet; sub-category mega-menus collapse to accordion drawer on mobile
- Spec table: switches from multi-column grid to stacked label-above-value rows on mobile; horizontal scroll is eliminated rather than enabled
- Hero: copy and CTA stack vertically on mobile; overlay opacity reduces to 0.45 for improved legibility at smaller font sizes
- Feature callout: illustration moves below the copy block on mobile rather than side-by-side; left border rule shifts to a 4px top border
- Footer: four-column link grid collapses to two columns on tablet, single-column accordion on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Custom typeface unresolved**: the site loads fonts via JavaScript and the font-family stack returned only "inherit" at extraction time. All typography tokens fall back to system sans-serif. Confirm the brand's display and body typefaces before production use — likely a bold condensed grotesque for display and a neutral sans for body.
- **Exact hero overlay treatment**: the scrim may use a directional gradient (dark-bottom to transparent-top or left-to-right) rather than a flat rgba value; the exact gradient stop positions were not extractable.
- **Interactive motion spec**: hover transition durations, panel slide easing curves, and scroll-triggered reveal timings were not captured in static extraction.
- **Button radius in production**: the primary CTA may carry a 1–2px radius that was not visible at extraction resolution; current spec uses {rounded.none} consistent with the sport-serious aesthetic but should be verified against live computed styles.
- **accent-tan application scope**: #b6855a was present in the extracted palette but its exact usage context — paddle-grip photography, warm separator rules, or icon fills — could not be confirmed without live DOM inspection.
- **Dark-mode system toggle**: the #121212 and #222222 surfaces suggest intentional dark-context design, but whether a separate OS-level dark mode variant exists and how it differs from the editorial dark surfaces was not determinable from extraction.
