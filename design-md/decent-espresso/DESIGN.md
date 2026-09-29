---
version: alpha
name: "Decent Espresso"
source_url: "https://decentespresso.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pressure-profile graphs rendered in real-time cyan on a dark tablet screen — that single UX motif defines Decent's entire visual identity. The brand's signature teal (#47cdd9) doesn't function as a decorative accent; it behaves like an instrument readout, a color that says "data is flowing." The site pairs Lato — geometric, unadorned, legible at small sizes on technical dashboards — with Courier New monospace for spec tables, firmware version strings, and the shot-graph overlays that espresso enthusiasts obsess over. This duality (humanist sans-serif for marketing copy, monospace for machine data) mirrors the product itself: a consumer appliance that exposes industrial-grade telemetry. Canvas is almost always pure white (#fcfcfc / #f8f8f8), letting photography of brushed-steel frames and walnut accents carry warmth without competing with the teal. Corners stay sharp or barely softened (`{rounded.xs}` to `{rounded.sm}`); nothing is pill-shaped, nothing is playful — the geometry reads as machined aluminum, not lifestyle brand. A secondary warm cream (#faeed7) appears in community-facing sections and the Decent Diaspora forums, grounding the otherwise clinical palette. Supporting teals (#5cd3dd, #32c7d5, #75f6ff, #d1f2f5) form a luminosity ramp used in hover states, gradient washes behind hero sections, and the characteristic glow effect on interactive pressure charts. Ink sits at #222222 with body copy at #545454, ensuring comfortable reading on long-form pages that explain extraction physics. Spacing is generous vertically (`{spacing.section}` between content blocks) but tight horizontally in spec grids, echoing the information-dense tablet UI that ships with every machine.

colors:
  primary: "#47cdd9"
  primary-active: "#32c7d5"
  primary-disabled: "#b5ebef"
  primary-highlight: "#75f6ff"
  ink: "#222222"
  body: "#545454"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#d1d2d4"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#fcfcfc"
  surface-warm: "#faeed7"
  surface-teal: "#d1f2f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#ddbb66"
  accent-olive: "#aaaa66"
  accent-error: "#884444"
  accent-pink: "#ffaaf6"
  navy: "#000080"
  charcoal: "#3d4045"
  charcoal-mid: "#494d53"
  gray-mid: "#646464"
  gray-light: "#949494"

typography:
  display-xl:
    fontFamily: "'Lato', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px
  mono-md:
    fontFamily: "'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  mono-sm:
    fontFamily: "'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-lg:
    fontFamily: "'Courier New', monospace"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: 2px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  text-input-mono:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline-soft}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.charcoal}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 3px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.primary}
    hoverShadow: 0 4px 20px rgba(71,205,217,0.15)
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xl}"
    accentColor: "{colors.primary}"
  hero-section-light:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowBorder: 1px solid {colors.hairline-soft}
    rowPadding: "{spacing.md} 0"
  pressure-graph-card:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    lineColor: "{colors.primary-highlight}"
    gridColor: "{colors.charcoal-mid}"
    axisTypography: "{typography.mono-sm}"
    labelTypography: "{typography.caption-bold}"
  firmware-badge:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary-active}"
    typography: "{typography.mono-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  model-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 2px solid {colors.hairline}
    selectedBorder: 2px solid {colors.primary}
    selectedBackground: "{colors.surface-teal}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    headerBackground: "{colors.surface-soft}"
    cellPadding: "{spacing.md} {spacing.base}"
    columnBorder: 1px solid {colors.hairline-soft}
  community-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: none
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
    divider: 1px solid {colors.charcoal-mid}
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 36px
    padding: 0 {spacing.base}
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorder: 2px solid transparent
    thumbnailActiveBorder: 2px solid {colors.primary}
  tooltip-spec:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
    maxWidth: 220px

---

## Components

### Buttons

**`button-primary`** — Solid teal (#47cdd9) fill with white text, 4px radius that reads as barely-softened rather than rounded. On hover, darkens to the active teal (#32c7d5) with no transition longer than 150ms. Disabled state fades to the pale teal (#b5ebef) at reduced opacity. Used for primary CTAs: "Buy Now," "Add to Cart," "Download App."

**`button-secondary`** — Transparent background with a 2px solid ink (#222222) border. On hover, inverts to solid ink fill with white text — a clean mechanical toggle that suits the brand's engineering tone. Same 4px radius and 44px height as primary.

**`button-ghost`** — Text-only with underline decoration in the primary teal. Used for inline actions within body copy: "Learn more," "View specs," "Compare models." No background or border on any state.

### Inputs

**`text-input`** — 44px height with a 1px hairline border that transitions to teal on focus. The focus ring is a single-pixel border swap, not a glow — consistent with the brand's no-frills instrument aesthetic. Placeholder text in muted gray (#888888).

**`text-input-mono`** — Variant using Courier New on a light gray surface, designed for firmware version entry, serial number lookup, or profile-code inputs where monospace alignment matters.

### Navigation

**`nav-bar`** — 64px fixed header with uppercase Lato Bold links at 14px with generous letter-spacing (0.5px). Clean white background with a subtle bottom hairline that disappears on scroll in favor of a soft drop-shadow. Logo sits left; navigation links center or right depending on viewport.

### Product Display

**`product-card`** — White card with a 1px soft hairline border and 8px radius. On hover, the border transitions to teal and a faint teal box-shadow appears (rgba(71,205,217,0.15)), creating a glow-edge effect that echoes the tablet UI's active-element highlighting. Interior padding at 24px keeps imagery breathing.

**`model-selector`** — Radio-card pattern for choosing between DE1, DE1+, DE1XL, and DE1XXL. Unselected cards have a 2px gray border; the selected card swaps to teal border with a soft teal background wash (#d1f2f5). Title typography in bold 16px Lato.

**`comparison-table`** — Multi-column spec comparison with a gray header row, thin column dividers, and alternating white/surface-soft row backgrounds. Cell text is 14px Lato; header text is 16px bold.

### Data Visualization

**`pressure-graph-card`** — Dark charcoal (#3d4045) container with bright cyan (#75f6ff) plot lines, mid-charcoal grid lines, and monospace axis labels. This component is the brand's signature visual — the real-time pressure/flow/temperature shot graph rendered for marketing purposes. Rounded at 8px.

**`spec-table`** — Light gray surface with two-column rows: left column is an 11px uppercase label (Lato Bold, 0.8px letter-spacing), right column is a 14px Courier New value. Row dividers are soft hairlines. Used for weight, dimensions, boiler specs, pump type, and similar technical attributes.

### Badges & Indicators

**`firmware-badge`** — Small inline badge with teal-tinted background (#d1f2f5) and darker teal text, using monospace type at 12px. Communicates firmware versions, software compatibility, or feature availability flags.

**`announcement-bar`** — Full-width 36px bar in solid primary teal with white bold caption text. Used for shipping notifications, sale events, or new model launches. Sits above the nav-bar.

### Community & Content

**`community-card`** — Warm cream (#faeed7) background card for forum highlights, user profiles, or Diaspora community content. The warm surface differentiates community/social content from the clinical product pages.

**`tooltip-spec`** — Compact dark tooltip with monospace text for hover-revealed technical details (e.g., explaining what "9-bar pre-infusion" means on a spec line).

### Media

**`image-gallery`** — Light gray container with small-radius thumbnails below a main image. Active thumbnail gets a 2px teal border. The gallery container itself uses 8px radius. No lightbox overlay — images expand in-page, consistent with the brand's flat information hierarchy.

### Footer

**`footer`** — Dark charcoal background with muted text and teal link color. Divided into columns by thin charcoal-mid dividers. Contains legal links, community links, support resources, and firmware download shortcuts.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger menu. Hero text drops to `display-md` (28px). Spec tables stack label above value. Pressure graph cards scroll horizontally. Product cards stack vertically with full-bleed images. |
| Tablet | 744–1128px | Two-column product grid. Nav links visible but condensed spacing. Comparison table allows horizontal scroll with sticky first column. Hero maintains large type at `display-lg`. |
| Desktop | 1128–1440px | Three-column product grid. Full comparison table visible. Spec tables return to side-by-side layout. Pressure graph cards display at full width with interactive hover states. Navigation fully expanded. |
| Wide | > 1440px | Content max-width caps at 1440px, centered on canvas. Additional horizontal padding at `section` scale. Image galleries may show 2-up side-by-side. Graph cards gain extra padding for data density. |

### Touch Targets

- All interactive elements maintain minimum 44px tap target on mobile and tablet
- Ghost buttons gain additional vertical padding on touch devices (12px vs 8px)
- Thumbnail gallery items space at minimum 8px gap to prevent mis-taps
- Spec table rows gain 48px minimum height on mobile for row-tap interactions

### Collapsing Strategy

- Navigation collapses to a slide-out drawer at mobile breakpoint, with full-height dark charcoal background and teal active-state indicators
- Comparison tables become horizontally scrollable with a fixed first column (model name) and swipeable feature columns
- Spec tables stack vertically: label on its own line (uppercase, muted), value below (monospace, ink)
- Pressure graph cards maintain aspect ratio but reduce padding; axis labels hide on mobile, replaced by tap-to-reveal tooltips
- Footer columns collapse to an accordion pattern with teal chevron indicators

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom properties or design tokens were publicly exposed; color extraction relied on computed styles and asset analysis
- Exact font weights for Lato on the live site could not be confirmed beyond Regular (400) and Bold (700) — Light (300) usage on display headings is inferred from visual weight
- The pressure-graph visualization likely uses a JS canvas/SVG library (possibly D3 or custom WebGL); exact line weights, bezier smoothing, and animation easing could not be extracted
- Icon system appears to use FontAwesome but may include custom SVG icons for machine-specific UI elements (portafilter, steam wand, etc.) — icon set is undocumented
- Motion/animation tokens are not defined; the site appears minimal in transitions but the tablet app UI has characteristic easing curves that may apply to web interactions
- The accent pink (#ffaaf6) and olive (#aaaa66) appeared in extraction but their specific use-case contexts are unclear — possibly used in community content or limited promotional material
- Dark-mode behavior is not documented; the pressure-graph dark cards suggest partial dark-UI usage but no full dark theme was detected
- Form validation states and error styling beyond the error red (#884444) could not be confirmed
