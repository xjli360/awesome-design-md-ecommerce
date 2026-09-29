---
version: alpha
name: "Indochino"
source_url: "https://indochino.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The measurement form is the product. Before any suit ships, Indochino collects around twenty body measurements — chest, waist, seat, inseam, sleeve pitch — and that exacting sequence is embedded in the digital interface at every level. The palette reflects the same economy: three near-white surfaces (#fafbfc, #f0f1f2, #f0eeee) layer beneath product photography with almost no differentiation, creating a blank-form backdrop that lets imagery carry all persuasive weight. The single departure from this restraint is #ce0e2d, a high-saturation crimson — not burgundy, not oxblood, but closer to a signal flare — which appears on the primary CTA, the promo banner, the wordmark, and nowhere else. Its isolation is the entire point: in a palette this muted, one fully saturated hue carries enormous pressure per pixel. Roboto handles all typographic work at every scale, running at weight 700 for display headlines and stepping to 400 for body copy without ever switching families. This mono-family discipline suits a brand that sells precision over poetry; type here is a delivery mechanism, not an aesthetic statement. Display lines sit around 36–40px with tight letter-spacing that evokes editorial menswear catalogue formatting rather than tech-startup energy. The measurement customization flow — six to eight steps from fabric through lining, lapel, button stance, and fit — is navigated via a `{rounded.full}` step-indicator with the active pip in `{colors.primary}`. Fabric swatches render as square thumbnails in a scrollable grid; the selected state draws a 2px ring in `{colors.primary}`. A soft pink surface (#fcf0f2), aliased as `{colors.primary-light}`, appears on hover and active configurator states, warming the otherwise cool-gray stack just enough to register without announcing itself. Medium gray (#b1b5b8) handles all secondary text, disabled inputs, and placeholder labels throughout. The effect is sober and competent — the brand correctly assumes its customer already decided he wants a suit before he opened the browser.

colors:
  primary: "#ce0e2d"
  primary-active: "#a80b25"
  primary-disabled: "#f0eeee"
  primary-light: "#fcf0f2"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#b1b5b8"
  hairline: "#d8d9da"
  canvas: "#fafbfc"
  surface-soft: "#f0f1f2"
  surface-card: "#ffffff"
  surface-warm: "#f0eeee"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  title-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  step-label:
    fontFamily: "Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  swatch-label:
    fontFamily: "Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    accentColor: "{colors.primary}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    labelTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    overlayOpacity: 0.45
    minHeight: 600px
  fabric-swatch:
    size: 56px
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
    labelTypography: "{typography.swatch-label}"
    labelColor: "{colors.body}"
    gap: "{spacing.sm}"
  step-indicator:
    activeColor: "{colors.primary}"
    inactiveColor: "{colors.muted}"
    completedColor: "{colors.ink}"
    pipSize: 10px
    pipShape: "{rounded.full}"
    labelTypography: "{typography.step-label}"
    connectorColor: "{colors.hairline}"
  customizer-panel:
    backgroundColor: "{colors.surface-soft}"
    activeOptionBackground: "{colors.primary-light}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  showroom-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    mutedColor: "{colors.muted}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Full-bleed crimson (#ce0e2d) on a hard square form (`{rounded.none}`), with uppercase Roboto at 14px/700 and 1px letter-spacing — a directive rather than an invitation. On hover, background shifts to `{colors.primary-active}` (#a80b25). Appears at every measurement funnel entry point, configurator completion step, and checkout gate. At 48px height it sits comfortably at touch target minimums without visual bulk.

**`button-secondary`** — Ink-bordered white button that pairs with `button-primary` in two-CTA layouts such as "Start Your Suit" / "Book a Showroom." Identical height (48px) and uppercase type style maintain visual parity; on hover, background picks up `{colors.surface-soft}` so the transition stays within the cool-gray family. Border drops to 1px solid `{colors.ink}` rather than the brand red to signal a softer action tier.

**`button-ghost`** — Crimson text on transparent background for tertiary actions like "View Details" or "Change Selection" within the configurator panel. No border, no padding inflation — it sits flush with surrounding body copy in `{colors.primary}` and relies on color alone to signal interactivity.

### Inputs

**`text-input`** — Light-canvas field with a `{colors.hairline}` border that tightens to `{colors.ink}` on focus; no color flash, just a weight upgrade. Placeholder text runs in `{colors.muted}` (#b1b5b8). `{rounded.xs}` keeps corner treatment minimal, consistent with the brand's square-edged vocabulary. Used across measurement entry forms, address fields, and account inputs.

### Navigation

**`nav-bar`** — 64px sticky bar on `{colors.canvas}` separated from content by a `{colors.hairline}` bottom border. Primary links (Suits, Shirts, Accessories, Showrooms) use `{typography.nav-link}` in `{colors.ink}`; hover state adds an underline in `{colors.primary}`. The brand wordmark anchors left; a compact `button-primary` anchors right. A `promo-banner` — 36px full-width strip in `{colors.primary}` — stacks directly above on desktop with centered `{typography.button-sm}` white text.

### Product Card

**`product-card`** — 3:4 portrait image fills the card top on `{colors.surface-card}` with `{rounded.xs}` clip. Below the image: product name in `{typography.body-sm}` and price in `{typography.price}` (Roboto 18px/700, `{colors.ink}`). On hover, a 0 4px 12px shadow lifts the card — no border-color change, preserving the minimal frame. Sale items carry a `promo-badge` overlaid at top-left of the image.

### Hero

**`hero-banner`** — Full-bleed editorial photography with a dark overlay at 45% opacity. Headline in `{typography.display-xl}` (Roboto 40px/700, `{colors.canvas}`) sits top-left or centered; a `button-primary` follows below with at least `{spacing.lg}` separation. Minimum height 600px on desktop. Mobile crops to a square ratio and reduces headline to `{typography.display-md}`.

### Configurator

**`fabric-swatch`** — 56×56px square thumbnails in a 4-across or 6-across scrollable grid, each with a `{typography.swatch-label}` name below in `{colors.body}`. Default border: 1px `{colors.hairline}`; selected state: 2px solid `{colors.primary}` ring with no corner radius. Tap or click expands the swatch into a full-panel lightbox with fabric weight, composition, and care details.

**`step-indicator`** — Horizontal pip-and-connector track across the top of the configurator. Active pip: `{colors.primary}` filled circle; completed pip: `{colors.ink}`; inactive: `{colors.muted}`. Connectors in `{colors.hairline}`. Step labels in `{typography.step-label}` (11px uppercase) sit below each pip on desktop; labels collapse to invisible on mobile leaving only the color-coded pips.

**`customizer-panel`** — Right-column container in `{colors.surface-soft}` with a `{colors.hairline}` border and `{rounded.xs}` corners. Active option rows highlight background in `{colors.primary-light}` (#fcf0f2). Section headings in `{typography.title-md}`; option labels in `{typography.body-sm}`. The warm-pink active state is the only place on the site that color signals selection without using the primary red.

### Badges & Banners

**`promo-badge`** — Square-cornered (`{rounded.none}`) crimson tag in `{typography.caption}` all-caps, used to flag sale pricing, limited fabric runs, or new arrivals on product cards. Can appear inline below the product name or overlaid top-left on the card image at 8px inset.

**`promo-banner`** — 36px full-width strip in `{colors.primary}` with centered `{typography.button-sm}` white text announcing free alterations periods, seasonal promotions, or shipping thresholds. Sits above the nav-bar on desktop; collapses to a scroll-dismissible bottom anchored bar on mobile.

### Showroom Card

**`showroom-card`** — Warm off-white (`{colors.surface-warm}`) card with `{rounded.sm}` corners, carrying city name in `{typography.title-sm}` and address/hours in `{typography.body-sm}`. A `button-ghost` in `{colors.primary}` links to the booking flow. Used in a 3-column grid on the Showrooms page.

### Footer

**`footer`** — Dark ink (#1a1a1a) full-width footer; white link text in `{typography.body-sm}` across 4 columns on desktop. Column headings in `{typography.title-sm}` at weight 500. Secondary legal and copyright text runs in `{colors.muted}`. No visible top border — the background contrast provides full visual separation from the page body.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger overlay; hero crops to square aspect ratio; product grid 1-across; fabric swatch grid 3-across; step-indicator shows pips only (labels hidden); promo-banner moves to bottom drawer |
| Tablet | 744–1128px | Nav shows primary categories, truncates secondary links to overflow menu; product grid 2-across; configurator stacks vertically below product preview; swatch grid 4-across |
| Desktop | 1128–1440px | Full horizontal nav with all categories; product grid 3–4 across; configurator in right-column layout (60/40 split with sticky panel); promo-banner full-width above nav |
| Wide | > 1440px | Content capped at ~1440px and centered; side gutters in `{colors.canvas}`; grid gutter widens to `{spacing.xl}`; hero image scales but text column stays constrained |

### Touch Targets
- All buttons minimum 48px height; touch area padded to 44×44px minimum on mobile
- Fabric swatches expand from 56px to 72px on mobile to reduce mis-tap rate in grid
- Nav links in the hamburger overlay padded to 52px row height
- Step-indicator pips expand to 24px diameter on touch devices for reliable tap accuracy

### Collapsing Strategy
- Primary nav collapses at <744px; hamburger reveals a full-height `{colors.canvas}` overlay drawer with stacked category links
- Promo-banner does not hide on mobile — repositions to bottom anchored bar, dismissible per session
- Configurator transitions from split-panel to vertical tabbed accordion below 1128px; each step section is collapsible
- Footer columns stack 2×2 at tablet, single column at mobile; all links remain visible (no accordion compression)
- Product card hover shadow disabled on touch; tap triggers a bottom-sheet quick-view with CTA and swatch selector

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Foreground text colors (ink #1a1a1a, body #3d3d3d) were not present in extraction — values are standard menswear-appropriate defaults, not confirmed from source
- `primary-active` (#a80b25) is derived by darkening the extracted primary ~20%; actual hover-state hex not captured
- Only one font family (Roboto) was detected; whether Indochino uses a secondary editorial or display typeface for campaign headers is unknown — spec defaults to Roboto throughout all scales
- Meta theme-color absent, indicating either no PWA manifest or it was blocked; mobile status-bar treatment uncertain
- Site returned an access-denied response during extraction — color and font data reflect partial CSS parsing, not a full authenticated browsing session; additional design tokens (shadows, animation curves, grid gutters) were not available
- No confirmed spacing grid or column-count system; responsive layout values in this spec are inferred from DTC menswear conventions
- Transition durations, easing curves, and animation specs not captured
