---
version: alpha
name: "Pininfarina Hybrid"
source_url: "https://www.pininfarina-hybrid.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The cursive "f" that graced Ferrari 275 GTB flanks and Lancia Aurelia coupes reappears here at 42mm scale, anchoring a watch face where Swiss mechanics and Milanese software share the same dial. Pininfarina Hybrid carries the studio's ninety-year coachbuilding vocabulary — surfaces shaped by aerodynamic logic, proportions that reward prolonged study — into connected wearables. The palette, inferred from the brand's documented automotive identity rather than live extraction, runs deep: a near-black carbon canvas (#111111) hosting surfaces that step up in small luminosity increments (#1a1a1a, #222222), with Italian Racing Red (#cc0000) reserved for a single primary CTA voltage and no secondary warmth anywhere on the page. Silver-platinum (#c4c4c4) provides the material analogue for chrome trim, appearing in border tokens, icon fills, and the metallic caption tier that enumerates case specifications. Type inhabits a neutral geometric sans-serif in the Futura or Helvetica Neue lineage: display sizes set at light weights (300–400) so product photography dominates, body copy in near-white (#e0e0e0) at 16px, specification data in muted silver (#9a9a9a) at 13px with wide uppercase tracking that echoes an instrument dashboard. Motion should feel mechanical rather than elastic — no bounce curves, just smooth deceleration that mirrors the feel of a well-oiled crown being wound. Product cards place the watch image over a dark field with a minimal data row below: movement type, case diameter, battery life, separated from price by a 1px hairline at #2a2a2a. Buttons carry zero corner radius throughout, reading as precision-engineered rather than consumer-app. The overall register is controlled and cool-industrial: a design-house credential brought to e-commerce with the restraint one expects from a Pininfarina concept first rendered in clay.

colors:
  primary: "#cc0000"
  primary-active: "#a80000"
  primary-disabled: "#550000"
  primary-text: "#ff4444"
  silver: "#c4c4c4"
  silver-muted: "#8a8a8a"
  ink: "#f0f0f0"
  body: "#e0e0e0"
  muted: "#9a9a9a"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  canvas: "#111111"
  surface-soft: "#161616"
  surface-card: "#1a1a1a"
  surface-raised: "#222222"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  spec-value: "#c4c4c4"
  badge-tech: "#1e3a5f"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1px
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0.1px
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 1.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Futura, 'Arial Nova', sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.silver}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.silver}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.silver}"
  nav-bar-scrolled:
    backgroundColor: "rgba(17,17,17,0.95)"
    backdropFilter: "blur(12px)"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    specTypography: "{typography.caption}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    imageScale: 1.03
  hero-full:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    layout: "full-bleed image, centered text overlay"
    overlayGradient: "linear-gradient(to bottom, transparent 40%, rgba(17,17,17,1))"
  watch-configurator:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.title-sm}"
    activeSwatchBorder: "2px solid {colors.silver}"
    inactiveSwatchBorder: "2px solid {colors.hairline}"
    rounded: "{rounded.none}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    rowSeparator: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.spec-value}"
    padding: "{spacing.md} {spacing.lg}"
  tech-badge:
    backgroundColor: "{colors.badge-tech}"
    textColor: "{colors.silver}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  material-chip:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  movement-indicator:
    iconColor: "{colors.silver}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.title-sm}"
    valueColor: "{colors.ink}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    activeTextColor: "{colors.ink}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    activeBorderBottom: "1px solid {colors.silver}"
  toast-notification:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    borderLeft: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    linkColor: "{colors.silver}"
    linkHoverColor: "{colors.ink}"
    columnHeadTypography: "{typography.spec-label}"
    columnHeadColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — Sharp-cornered (`{rounded.none}`) filled rectangle in `{colors.primary}` Italian Racing Red with `{typography.button-md}` uppercase at 1.5px tracking, 48px tall. This is the only red element in the UI; the zero-radius corner treatment reads as precision-engineered, not consumer-app. Hover darkens to `{colors.primary-active}` (#a80000) with no geometric change; disabled collapses fill to `{colors.primary-disabled}` with muted text.

**`button-secondary`** — Transparent fill with a 1px `{colors.silver}` border and `{colors.ink}` text; identical uppercase tracking and height to the primary. Hover fills with `{colors.surface-raised}` and intensifies the border to full ink weight. Used for "Learn More" and "Compare Models" CTAs where the red primary would overwhelm a composed editorial layout.

**`button-ghost`** — Minimal tertiary action with `{colors.hairline}` border and `{colors.muted}` text in `{typography.button-sm}`. For low-stakes actions: save to wishlist, share, download spec sheet.

### Text Input

**`text-input`** — Square-edged field (`{rounded.none}`) on `{colors.surface-card}` with a resting `{colors.hairline}` border that steps to `{colors.silver}` on focus. Placeholder in `{colors.muted}`. The absence of radius reinforces the precision-instrument aesthetic that runs across every interactive element on the site.

### Navigation Bar

**`nav-bar`** — Fixed 64px dark bar at `{colors.canvas}` with the Pininfarina script logo in `{colors.silver}` and category links rendered in `{typography.nav-label}` (11px, 1.8px letter-spacing, uppercase). A bottom hairline at `{colors.hairline}` provides separation without visual weight. On scroll, `nav-bar-scrolled` activates a blur-backed semi-opaque version that preserves the dark register while confirming depth. Cart and account icons sit right-aligned as 20px stroke outlines.

### Product Card

**`product-card`** — Zero-radius card on `{colors.surface-card}`, padded `{spacing.lg}` on all sides. Watch image fills a 1:1 square centered in the card's upper zone; below: title in `{typography.title-sm}`, specs row (movement type, case diameter) in `{typography.caption}` at `{colors.muted}`, then price in `{typography.price-display}` (20px weight-300) at full `{colors.ink}`. Hover reveals a `{colors.hairline}` border outline and the image scales 1.03× — subtle enough to feel mechanical rather than animated.

### Hero Full

**`hero-full`** — Full-bleed product photograph with text overlay centered in the lower third. Headline in `{typography.display-xl}` (52px weight-300, −1.5px tracking) over a gradient scrim from transparent at 40% to solid `{colors.canvas}` at the bottom edge. The light weight at large scale recalls the fine construction lines of Pininfarina automotive sketches.

### Watch Configurator

**`watch-configurator`** — Inline option-selector on the PDP for strap material and dial color. Section labels in `{typography.spec-label}` (uppercase, 1.2px tracking) sit above a horizontal row of square swatches: active swatch carries a 2px `{colors.silver}` border, inactive carries `{colors.hairline}`. No radius on swatch containers. Renders as a full matrix on desktop; horizontally scrollable single row on mobile.

### Spec Table

**`spec-table`** — Two-column row layout for technical detail: case diameter, water resistance, battery life, connectivity protocol, strap lug width. Row labels in `{typography.spec-label}` at `{colors.muted}`; values in `{typography.body-sm}` at `{colors.spec-value}`. Rows separated by 1px `{colors.hairline}`. Designed to handle 8–12 rows without visual noise; the near-zero label size and subdued palette keep the table from competing with the product photography above it.

### Tech Badges

**`tech-badge`** — Small rectangular label for connectivity and feature callouts (GPS, BLE 5.0, NFC, Activity Tracking). Dark blue fill at `{colors.badge-tech}` with `{colors.silver}` text in `{typography.spec-label}` at `{rounded.xs}` corner. Rendered as a horizontal row beneath the product title on collection pages, giving a quick-scan tech summary before the user clicks through.

### Movement Indicator

**`movement-indicator`** — Icon + label + value unit callout for movement type (Swiss Quartz, Swiss Hybrid Automatic). Icon stroke in `{colors.silver}`, label in `{typography.spec-label}` at `{colors.muted}`, value in `{typography.title-sm}` at `{colors.ink}`. Appears on PDPs above the spec table as the primary credential marker.

### Footer

**`footer`** — Canvas-dark background matching `{colors.canvas}`, separated from the last page section by a 1px top border at `{colors.hairline}`. Column heads in `{typography.spec-label}` (uppercase, tracked) at `{colors.ink}`; body links in `{typography.caption}` at `{colors.muted}`, hover transitions to `{colors.ink}`. Legal and copyright text in `{typography.caption-sm}`. Four-column layout on desktop.

### Collection Filter

**`collection-filter`** — Horizontal tab strip for filtering by collection tier or case size. Active tab uses a 1px `{colors.silver}` bottom border with `{colors.ink}` text; inactive tabs in `{colors.muted}`. All labels in `{typography.spec-label}` to maintain tonal consistency with the nav layer above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `{typography.display-md}` (28px weight-400); nav collapses to hamburger with full-screen dark overlay; watch configurator becomes horizontally scrollable swatch row; spec table becomes accordion |
| Tablet | 744–1128px | Two-column product grid; hero text left-aligned over image; spec table retains two columns; nav shows primary categories, utility icons remain right-anchored |
| Desktop | 1128–1440px | Three-column product grid; hero at full `{typography.display-xl}`; watch configurator expands to full matrix; nav reveals all category labels and secondary utilities |
| Wide | > 1440px | Grid caps at 1440px max-width, centered; hero background image bleeds to viewport edge; outer whitespace expands proportionally to preserve automotive-proportion margins |

### Touch Targets

- All interactive elements maintain 48px minimum height
- Swatch selectors in the watch configurator are 44×44px minimum with `{spacing.sm}` gaps between them
- Mobile nav trigger is 44×44px centered within the 64px bar
- Collection filter tabs maintain 44px height with `{spacing.lg}` horizontal padding per tab

### Collapsing Strategy

- Product card spec row collapses from three data points (movement, case, battery) to two (case, battery) on mobile to prevent label truncation
- Spec table converts to a collapsed accordion on mobile; each row group taps to expand
- Hero headline letter-spacing reduces from −1.5px to −0.4px at mobile scale to prevent inter-character collision on narrow viewports
- Footer compresses from four columns to two at tablet, single column at mobile; column heads remain as visible separators

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors extracted from the live site — the domain appears to block automated extraction or renders design tokens via JavaScript. All color values above are inferred from Pininfarina's documented automotive brand identity and should be verified against the actual live site before production use.
- No font stacks extracted. Typography tokens use Helvetica Neue / Futura as proxies for the luxury Italian design house register; the actual typeface (possibly a commissioned or licensed geometric sans) must be confirmed.
- Meta theme-color absent — dark-mode behavior and OS-level status bar treatment are unconfirmed.
- Platform is confirmed non-Shopify; cart architecture, variant selector patterns, and add-to-cart flow are inferred from hybrid watch category norms rather than observed implementation.
- `{colors.badge-tech}` (#1e3a5f) and `{colors.spec-value}` (#c4c4c4) are design-judgment defaults, not extracted values — verify against actual PDP.
- Specific photography art direction (studio vs. lifestyle, white vs. dark sweep) unconfirmed; hero and card layout assumptions may require adjustment once real imagery is accessible.
- Animation easing curves, transition durations, and scroll behavior are approximated from the brand's mechanical-precision positioning; no motion spec was extractable.
