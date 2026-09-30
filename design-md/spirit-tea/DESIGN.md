---
version: alpha
name: "Spirit Tea"
source_url: "https://spirittea.co"
captured_at: "2026-09-28T10:20:45.446007+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Spirit Tea's markup exposes an editorial, tea-house identity built on CSS
  custom properties rather than a documented style guide, so mappings below
  are evidence-based inferences. A deep navy (#2b4163, echoed by a darker
  #1e304e) reads as the primary identity color — #2b4163 appears explicitly
  as a themeColor in an embedded widget config, suggesting brand intent even
  though no button rule confirms it as the default CTA fill. Canvas and
  surface tones are warm and low-contrast: #fcfaf8 and #f6efe9 (the latter
  observed repeatedly as outline-button text/border and hover-overlay color
  across several sections), with #f2f2f2 and #dddddd serving conventional
  card/hairline duty. Two serif families are declared directly in :root —
  "Dala Moa" for headings and "Fern" for body copy — at generous sizes
  (h1 48–64px, h2 48px, h3 32px, body 17px) with tracking utilities
  (--letter-lg/md/sm) suggesting wide-tracked display type over tighter body
  text. A lilac accent (#c99cc9, paired with #dfc5d9) is confirmed on a
  ".btn--lilac" rule; teal (#339999) is the Judge.me review-widget color and
  is treated as third-party, not brand, chrome. Warm earth hues (#efa54b,
  #b95e2f, #751e41, #a36710) and a sage (#8d997f) have no confirmed CSS
  selector role; they are speculatively assigned to tea-category accents
  given the site's White/Green/Black/Oolong/Matcha/Yellow/Herbal structure.
  Social-network brand hexes present in the raw palette are excluded as
  share-icon artifacts.

colors:
  primary: "#2b4163"
  ink: "#1e304e"
  canvas: "#fcfaf8"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f6efe9"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-teal: "#339999"
  accent-lilac: "#c99cc9"
  accent-lilac-soft: "#dfc5d9"
  accent-sage: "#8d997f"
  accent-amber: "#efa54b"
  accent-terracotta: "#b95e2f"
  accent-wine: "#751e41"
  border-strong: "#000000"
typography:
  display-xl: {fontFamily: "'Dala Moa', serif", fontSize: "64px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0.01em"}
  display-md: {fontFamily: "'Dala Moa', serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "0.01em"}
  title-md: {fontFamily: "'Dala Moa', serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0.01em"}
  body-md: {fontFamily: "'Fern', serif", fontSize: "17px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.005em"}
  body-sm: {fontFamily: "'Fern', serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.005em"}
  caption: {fontFamily: "'Fern', serif", fontSize: "11px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.1em"}
  button-md: {fontFamily: "'Fern', serif", fontSize: "13px", fontWeight: 600, lineHeight: 1, letterSpacing: "0.1em"}
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
    backgroundColor: "transparent"
    borderColor: "{colors.surface-soft}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-lilac:
    backgroundColor: "{colors.accent-lilac}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    height: "80px"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    overlay: "linear-gradient(0deg, rgba(0,0,0,0) 50%, rgba(0,0,0,0.5) 100%)"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: "calc(100vw - 120px - 140px)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  category-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.accent-lilac-soft}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xl}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

**button-primary** — the default filled CTA, using the inferred navy `primary` fill against white text; no direct `.btn--std` fill color was captured beyond a `var(--color-blue)` reference, so navy is a reasoned stand-in pending confirmation of that variable's resolved value.

**button-secondary** — modeled on the repeated `.btn--outline--black` / `.btn--outline--white` rules, which consistently pair a transparent background with `#f6efe9` text/border and a `#f6efe980` hover fill; this pattern is directly observed across multiple template sections.

**button-lilac** — derived from the single `.btn--lilac` rule (`color:#f6efe9`) plus the `#c99cc9` icon/accent color found elsewhere; the fill itself is proposed since only the text color was captured.

**text-input** — no form-field CSS was present in the evidence; styling is proposed to match the editorial serif-and-hairline aesthetic, with a bottom-weighted border proposed as a common pattern for this theme family (not confirmed).

**nav-bar** — height is directly observed from `--height-header-bar: 80px` and `--height-header: 120px`; color and typography choices are inferred to match the surrounding canvas/ink palette.

**hero** — height is calculated from the observed `--height-hero` formula referencing header and a 140px offset; the dark overlay gradient is copied verbatim from a captured `background: linear-gradient(...)` rule, though its exact application context (hero image overlay) is inferred from naming and position in the source.

**product-card** — no dedicated product-card selector was captured; structure (image, title, price) is a standard commerce pattern proposed for a Shopify catalog organized by tea type, using surface/hairline tokens already observed elsewhere in the theme.

**category-badge** — proposed to represent the site's White/Green/Black/Oolong/Matcha/Yellow/Herbal groupings; the amber fill is speculative since no CSS ties any hex to these labels — a rotating set of the accent tones could serve each category instead.

**subscription-card** — proposed for the "Spirit Tea Club" quarterly box callout described in the page text; uses the soft cream/lilac pairing observed in button and icon contexts to suggest a distinct, gentler promotional surface.

**footer / search** — both proposed from conventional patterns; no footer or search-input selectors were present in the supplied CSS rules.

## Responsive Behavior

| Breakpoint | Approx. width | Notes (proposed) |
|---|---|---|
| Mobile | < 640px | Single-column stacking; nav collapses to a hamburger/drawer pattern (not observed). |
| Tablet | 640–1023px | Two-column product grids; header likely retains the 80px bar height variable. |
| Desktop | 1024–1279px | Full nav visible; `--gutter` widens from 20px to 60px per captured `:root` variants. |
| Wide | ≥ 1280px | Hero height governed by the `--height-hero` calc; max content width not captured. |

Touch targets should default to a minimum 44×44px hit area for buttons and nav icons per general accessibility guidance; this is a recommendation only and was not measured from the live site. Header/nav collapse behavior, drawer transitions, and exact grid column counts were not observed in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only — no rendered layout, computed styles, or DOM screenshots were available. The `primary` role assigned to `#2b4163` rests on its appearance as a widget `themeColor`, not a confirmed button or heading rule, and should be validated against live rendering. Category-badge and several accent colors (amber, terracotta, wine, sage) have no confirmed CSS selector tying them to tea-type sections; that mapping is a plausible but unverified guess. The Judge.me teal (`#339999`) is app-injected chrome and may not represent authored brand color at all. No hover/focus/active states beyond the few captured `:hover` rules were observed, and no mobile menu, cart drawer, or animation behavior was documented. The custom display/body fonts "Dala Moa" and "Fern" are taken as given from `:root` declarations, but their licensing, loading method (self-hosted vs. third-party), and fallback rendering were not verified. Spacing and rounded-corner scales are proposed conventions, not measured values, since no `border-radius` or margin/padding scale was present in the supplied rules.
