---
version: alpha
name: "Proper Cloth"
source_url: "https://propercloth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The configurator is the product. Where most menswear sites layer editorial photography over a thin e-commerce shell, Proper Cloth's entire interface is organized around a multi-step shirt builder — fabric grid, collar selector, cuff style, monogram placement — that makes the browse experience feel closer to CAD software than a lookbook. The Smart Sizes algorithm accepts five body measurements and returns a recommended size without requiring the customer to ever try a shirt on, which means the site must earn trust through precision language and clear data display rather than lifestyle aspiration. Visually, the brand inhabits a deep navy-and-white axis — a primary somewhere in the range of #1c3557, clean white canvas, and warm mid-gray body text — with no decorative color noise to distract from the product selector states. Typography reads as a refined humanist sans at moderate weight; extracted stacks defaulted to Arial suggesting brand fonts load via JS behind anti-bot gates, so all type values here are conservative reconstructions. Buttons are full-width in the mobile configurator context and precise rectangular pills on desktop, with no rounding beyond a subdued 4–6px — hard corners would feel too aggressive against fabric imagery, but full pills would infantilize a precision-purchase interface. The fabric swatch grid, rendered at roughly 80×80px, is the most visually dense surface on the site and carries its own hover-zoom logic. A thin gold-tone accent — approximately #c8a96e — surfaces in premium fabric callouts and monogram previews, the only warm note in an otherwise cool, architectural palette. Given very sparse extraction (no hex colors, single Arial fallback font), all token values below are brand-knowledge estimates; see Known Gaps.

colors:
  primary: "#1c3557"
  primary-active: "#142742"
  primary-hover: "#1e3d65"
  primary-disabled: "#8ea7c0"
  accent-gold: "#c8a96e"
  accent-gold-muted: "#e8d5a8"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#767676"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f5"
  surface-card: "#ffffff"
  surface-warm: "#faf9f7"
  on-primary: "#ffffff"
  swatch-border: "#c8c8c8"
  swatch-selected: "#1c3557"
  error: "#c0392b"
  success: "#2d7a4f"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.2px
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-strong:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  label-step:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.2px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  swatch-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 14px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
  text-input-error:
    border: "1.5px solid {colors.error}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    fontWeight: 700
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  swatch-grid:
    swatchSize: 80px
    gap: "{spacing.sm}"
    border: "1px solid {colors.swatch-border}"
    borderSelected: "2px solid {colors.swatch-selected}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.swatch-label}"
    labelColor: "{colors.muted}"
  swatch-grid-hover:
    border: "1.5px solid {colors.primary}"
    boxShadow: "0 2px 6px rgba(0,0,0,0.12)"
  configurator-step-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    stepLabelTypography: "{typography.label-step}"
    stepLabelColor: "{colors.muted}"
    padding: "{spacing.lg} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  configurator-step-nav:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
    typography: "{typography.label-step}"
    inactiveColor: "{colors.muted}"
    activeColor: "{colors.ink}"
  measurement-input-group:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    helpTextTypography: "{typography.caption}"
    helpTextColor: "{colors.muted}"
    inputComponent: "{components.text-input}"
  size-recommendation-card:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    accentBar: "4px solid {colors.accent-gold}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
  fabric-zoom-overlay:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.18)"
    maxWidth: 320px
    padding: "{spacing.sm}"
  badge-premium:
    backgroundColor: "{colors.accent-gold-muted}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-configurator:
    backgroundColor: "{colors.surface-warm}"
    minHeight: 480px
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    ctaButton: "{components.button-primary}"
    layout: "split — text left, configurator preview right"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-strong}"
    borderTop: none
    padding: "{spacing.xxl} 0"
  accordion-item:
    borderBottom: "1px solid {colors.hairline}"
    triggerTypography: "{typography.title-sm}"
    triggerColor: "{colors.ink}"
    triggerPadding: "{spacing.base} 0"
    contentTypography: "{typography.body-sm}"
    contentColor: "{colors.body}"
    iconColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — Flat-topped rectangular CTA in deep navy `#1c3557` with only 2px radius, uppercase tracking-wide label at 14px. Hover lifts to `#1e3d65`, active steps down to `#142742`; disabled washes out to a blue-gray `#8ea7c0`. In the configurator context, primary buttons frequently span full container width on mobile.

**`button-secondary`** — Same geometry as `button-primary` but inverted: white fill with a 1.5px navy border. Hover adds a whisper of `surface-soft` behind the label to acknowledge the interaction without breaking the frame. Used primarily for secondary actions adjacent to configurator steps ("Save & Continue Later", "Start Over").

**`button-ghost`** — Hairline-bordered, transparent-fill, lowercase subdued label. Appears in size-guide dialogs, filter toggles, and measurement help modals where an action exists but should not compete visually with the main flow.

### Text Input
**`text-input`** — Single-pixel hairline border upgrades to 1.5px primary navy on focus; no box-shadow, relying purely on the border weight shift for state feedback. Measurement inputs for the Smart Sizes flow inherit this component and add inline unit labels ("in" / "cm") as right-aligned suffix text in `muted` tone.

### Nav Bar
**`nav-bar`** — 60px fixed bar on white with a single hairline bottom border. Wordmark sits left in ink black. Category nav links center in `nav-link` type at 13px; no mega-menu hover animations — dropdowns appear as flat panels with no rounding. A "My Shirts" account link and cart icon sit right-rail. The bar does not go transparent over imagery.

### Product Card
**`product-card`** — No border-radius, clean edges. 3:4 portrait image, product name in `title-sm` bold, price in `price-display` at 18px bold. No hover card-lift animation — instead the fabric name underlines on hover. A premium badge renders in `badge-premium` (gold-muted background) in the card top-left corner for curated collections.

### Swatch Grid
**`swatch-grid`** — The densest UI surface, rendering fabric swatches at 80×80px in a responsive grid. Each swatch is 1px hairline-bordered; on hover it thickens to 1.5px primary navy. Selected state is 2px primary with a faint drop shadow. Below each swatch, fabric name in 11px `swatch-label` at muted tone. A hover overlay triggers a `fabric-zoom-overlay` panel showing a 320px close-up of the weave texture.

### Configurator Step Header
**`configurator-step-header`** — A soft-gray header band spanning the full configurator width, carrying step number in `label-step` uppercase and step title in `display-sm`. A sticky step navigation strip (`configurator-step-nav`) below it uses 2px navy underline to indicate the active step; completed steps render as muted.

### Size Recommendation Card
**`size-recommendation-card`** — After measurement entry, the Smart Sizes result surfaces in a navy-filled card with a 4px gold accent bar on the left edge. Size designation in `display-sm` white, explanatory fit notes in `body-md` white. This is the single component where the gold accent `#c8a96e` appears at structural weight rather than as a micro-badge.

### Badges
**`badge-premium`** — Gold-muted fill, ink text, uppercase 12px tracking. Used for "Signature", "Limited Run", and curated collection labels.
**`badge-new`** — Inverted ink-fill, white text. Appears on recently added fabric lines.

### Hero / Configurator Intro
**`hero-configurator`** — Split-panel layout on desktop: headline and sub-copy left, interactive shirt preview or configurator step right. Background is `surface-warm` (barely-warm white `#faf9f7`), keeping the shirt photography high-contrast. Headline in `display-xl` at 36px light weight — the low weight is the typographic signature here.

### Footer
**`footer`** — Full-width ink-black band. Section headings in `caption-strong` uppercase cream, links in 14px `body-sm` soft-white. No decorative dividers between column groups; generous vertical spacing does the separation work.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column configurator; swatch grid drops to 3 columns at 70px each; primary buttons full-width; nav collapses to hamburger + wordmark |
| Tablet | 744–1128px | Configurator splits into 2-column (step nav left, content right); swatch grid 4 columns; nav links shown, dropdowns compressed |
| Desktop | 1128–1440px | Full split hero layout; swatch grid 6–8 columns; sticky configurator step nav visible; measurement panel appears as right-rail |
| Wide | > 1440px | Max-width container (~1440px) centered; hero gains proportional padding; swatch grid caps at 8 columns |

### Touch Targets
- All configurator step buttons minimum 48px height
- Swatch tiles minimum 44×44px on mobile, expanded to 70×70px with increased tap margin
- Accordion triggers minimum 48px height to prevent mis-taps in measurement flow
- Nav hamburger icon 44×44px hit zone

### Collapsing Strategy
- Multi-step configurator collapses to single full-screen step view on mobile with "Step X of Y" breadcrumb
- Fabric zoom overlay reflows to bottom-sheet on mobile rather than floating panel
- Size recommendation card stacks vertically (accent bar moves to top edge) on mobile
- Footer columns stack to single column at mobile; headings convert to accordion triggers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site returned a bot-verification page; all color values are reconstructed from brand knowledge of Proper Cloth's visual identity and should be verified against the actual site
- **No brand fonts extracted** — only Arial (system fallback) was found; Proper Cloth likely loads a custom or licensed typeface via JS; all `fontFamily` stacks here are fallback-only estimates
- **Exact button radius** — Proper Cloth's corner treatment appears near-square but the precise px value (2–6px) was not confirmed
- **Gold accent hex** — `#c8a96e` is an informed estimate for the warm metallic tone seen in premium fabric callouts; actual value unconfirmed
- **Configurator interaction states** — multi-step state transitions, loading skeletons, and error states were not observable through extraction
- **Mobile nav behavior** — hamburger menu structure and panel animation not verified
- **Dark mode** — no data on whether a dark theme exists
