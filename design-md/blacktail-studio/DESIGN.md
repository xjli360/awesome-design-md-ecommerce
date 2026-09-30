---
version: alpha
name: "Blacktail Studio"
source_url: "https://blacktailstudio.com"
captured_at: "2026-09-28T09:32:15.681667+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Blacktail Studio is a Portland, Oregon custom-furniture and epoxy-resin
  woodworking studio that also sells courses, tools, and a small hard-goods
  line. The observed palette is anchored by true black and white with a
  cluster of warm rust-to-coral accents (#b72e00, #f15723, #f6774c, #e04b4b)
  that read as burnt-epoxy / charred-wood tones appropriate to the brand's
  "trial by fire" and resin-pour content. A near-black (#222222) is used in
  observed CSS for a product-status badge, and a pale blue-gray (#e7ebee) is
  the only light neutral supplied, so it is repurposed here as a soft
  section/hairline tone since no true gray exists in evidence. The single
  observed font family, EB Garamond, is a classic serif and is applied across
  the full type scale with system-sans fallbacks noted as inferred for any
  UI chrome, since no secondary sans face was captured.
  This interpretation treats the rust/coral cluster as the primary
  call-to-action and highlight family, black/white as the dominant
  editorial base (matching the photography-led, blog-and-video-heavy
  content), and #222222 as a reusable dark-surface and badge color per the
  one concrete component rule captured (`.product-mark`). Muted text reuses
  body ink at reduced emphasis since no distinct mid-gray was observed.
  All sizing, spacing, and radii below are proposed defaults for a
  craft/e-commerce hybrid layout, not measured page metrics.

colors:
  primary: "#b72e00"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#333333"
  hairline: "#e7ebee"
  surface-soft: "#e7ebee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f15723"
  accent-warm: "#f6774c"
  accent-coral: "#e04b4b"
  surface-dark: "#222222"
typography:
  display-xl: {fontFamily: "EB Garamond, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "EB Garamond, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "EB Garamond, serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "EB Garamond, serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "EB Garamond, serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "EB Garamond, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "EB Garamond, serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  workshop-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    typography: "{typography.title-md}"

## Components

**button-primary** is proposed for the dominant commerce actions (Add to Cart, View the Bundle, course purchases), using the rust primary against white text to stand out from the black/white editorial base; hover/pressed states are not observed and are proposed only.

**button-secondary** is an outlined variant for lower-emphasis actions (Learn More links on project builds), keeping the rust accent as text/border on a white field so it reads lighter next to primary CTAs; state is proposed.

**text-input** covers the sign-in, account, and email-signup fields implied by the nav content; a plain hairline border on white with body typography is a conservative default since no form styling was captured in evidence.

**nav-bar** models the persistent header implied by the repeated menu structure (Courses, N3 Nano, Tools, Blog, About, Cart, Sign In). A white background with black text and a light hairline rule is inferred from the neutral palette; no sticky/scroll behavior was observed.

**product-card** is proposed for shop grid items (marking knives, N-ZERO cleaner, bundle products), using a white surface with a hairline border to separate items without introducing unobserved shadow values.

**hero** targets the homepage lead area ("Hand Crafted Furniture | Epoxy Resin Tables | Portland Oregon") — a black field with white display type is inferred from the observed white H1 color rules, giving a photo-forward, high-contrast banner treatment.

**footer** groups the About/Contact/Tools/Email-signup links seen in the extracted footer content, using the darker `#222222` surface (the only dark neutral in evidence beyond pure black) with white text for separation from the hero's pure-black tone.

**badge** directly reflects the observed `.product-mark` rule (`background:#222; color:#fff; uppercase; padding:6px 8px`), reused here for "Sold Out"/"New" style product flags — this is the most concretely observed component pattern in the evidence.

**search** is a proposed pill-shaped input for site/shop search, styled consistently with text-input but rounded fully; no search UI was directly observed.

**workshop-card** is a category-appropriate addition for the course/workshop listings (My Epoxy Workshop, Finishing Workshop, Creator Course), using the soft light-blue-gray surface with a rust top border as a craft-oriented accent; entirely proposed, not observed.

## Responsive Behavior

Recommended breakpoints (not measured):

| Range | Target | Notes |
|---|---|---|
| < 480px | Mobile | Single-column stacks; nav collapses to hamburger (proposed) |
| 480–768px | Large mobile / small tablet | Product/workshop cards shift to 2-column grid |
| 768–1024px | Tablet | 2–3 column grids; nav may remain collapsed |
| > 1024px | Desktop | Full multi-column grids; nav-bar shows inline menu |

Touch targets should be a minimum of 44×44px for buttons and nav items. Collapse behavior, hamburger iconography, and any scroll/sticky header states are recommendations only; no mobile layout or interaction was observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot, not a rendered or interactive audit. The semantic role assignments for `muted` (reused body color, no distinct mid-gray was in the observed palette) and `hairline`/`surface-soft` (both mapped to the single light neutral `#e7ebee`) are inferred, not confirmed. Font sizes, weights, spacing, and radii across the typography/spacing/rounded scales are proposed defaults, not measured from live computed styles, aside from the literal `.product-mark` badge padding/colors which are directly observed. No hover, focus, active, or error states were observed; all interaction states referenced are proposed. Mobile/responsive layout, breakpoints, and navigation collapse behavior were not observed and are recommendations only. EB Garamond is the only font family confirmed in evidence; its licensing and availability as a webfont on the live site were not verified here. Additional palette colors (`#f15723`, `#f6774c`, `#e04b4b`) were present in the supplied swatch list without accompanying selector context, so their specific UI roles (illustration, gradient, hover accents) are inferred rather than confirmed.
