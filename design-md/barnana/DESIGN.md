---
version: alpha
name: "Barnana"
source_url: "https://barnana.com"
captured_at: "2026-09-29T04:00:16.989323+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Barnana's storefront runs on a Shopify theme with a warm, snack-food palette built around a
  deep teal (#108474), reinforced by the Judge.me review widget's primary/star color variables,
  paired with softer botanical greens (#12543f, #1b7e5f) and an earthy orange-tan family
  (#dc954d, #d88838, #eed9c2, #f7ecdb) that reads as tropical-fruit packaging. Neutral ink
  (#212121), body gray (#333333), and a muted brown-gray (#625e59, used as --text-light on the
  hero product upsell) carry body copy against cream surfaces (#faf3e8, #faeddb) rather than
  pure white. Typography is inferred from the theme's loaded font stack: Figtree is assigned to
  headings/buttons as a confident geometric sans, and Nunito Sans to body copy as a legible
  companion; Baskerville and monospace appear in the font list but no selector evidence ties them
  to a specific role, so they are omitted from the type scale. Border-radius is largely flat
  (--jdgm-border-radius: 0) with one observed 8px radius fragment reused for soft card/button
  corners. All sizing, weights, and component patterns below are proposed interpretations
  consistent with the evidence, not measured production values.

colors:
  primary: "#108474"
  primary-deep: "#12543f"
  accent: "#dc954d"
  accent-deep: "#d88838"
  ink: "#212121"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#625e59"
  hairline: "#dddddd"
  surface-soft: "#faf3e8"
  surface-card: "#f7ecdb"
  surface-warm: "#eed9c2"
  on-primary: "#ffffff"
  star: "#ecb935"
  error: "#d02e2e"
typography:
  display-xl: {fontFamily: "Figtree, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Figtree, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "77px"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    accentColor: "{colors.primary}"

## Components

**button-primary** — The teal (#108474) fill matches the Judge.me `--jdgm-write-review-bg-color` variable observed in the CSS, so it is proposed as the primary CTA color for "Add to Cart" and "Subscribe" actions, paired with white text for contrast.

**button-secondary** — An outline treatment using the same teal for border and label text, proposed for lower-emphasis actions (e.g., "Learn More") alongside the primary fill button, keeping a single accent hue across button states.

**text-input** — A flat white field with a light hairline border (#dddddd, drawn from the neutral gray set observed), used for newsletter, search, and account forms; focus/error states are proposed, not observed.

**nav-bar** — Sized to the measured `--HEADER-HEIGHT: 77px` custom property, with a white background and dark ink text; the mobile height variable (63px) suggests a compressed header is used below the desktop breakpoint, though its visual treatment was not observed.

**product-card** — A warm cream card background (#f7ecdb) intended to echo the hero product-upsell `--bg: #faeddb` variable, housing product imagery, name, and price in body typography; rounding and border are proposed for visual separation in a grid layout.

**hero** — Uses the same soft cream tone as the hero section's custom `--bg` variable, with large display typography for the plantain/cassava chip messaging seen in the page copy; layout (image-left/text-right or stacked) is not confirmed from static CSS.

**footer** — A deep green (#12543f) footer block with white text is proposed to bookend the page and reinforce the botanical/tropical color story; actual footer content and column structure were not observed.

**badge** — A pill-shaped accent-orange badge (#dc954d) for merchandising labels such as "Organic" or "Non-GMO," reflecting claims in the page text excerpt; shape and exact copy are proposed.

**search** — A rounded, cream-toned search affordance is proposed for the header search icon/overlay referenced in the page text ("Search Search Clear"), using the same hairline border as other inputs for consistency.

**subscription-card** — A snack-specific "Subscribe & Save" component proposed in a tan surface tone (#eed9c2) with teal accents, appropriate to a DTC snack brand offering recurring orders; no subscription UI was directly observed in the supplied evidence.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column stacking; header collapses to the `--HEADER-HEIGHT-MOBILE: 63px` value observed in CSS custom properties. |
| Small | 480–768px | Product grid narrows to 2 columns, matching the observed `--COLUMNS-SMALL: 2` variable on a column section. |
| Medium | 768–1024px | Product grid at `--COLUMNS-MEDIUM: 3` as observed; header height near `--HEADER-HEIGHT-MEDIUM: 66px`. |
| Desktop | ≥ 1024px | Full 3-column grid (`--COLUMNS: 3`); header at full `77px` height. |

Touch targets should be at least 44px; nav and search affordances should collapse into a hamburger/icon pattern below the medium breakpoint. This table is a recommendation derived from CSS custom-property values present in the source, not a record of measured rendered behavior across devices.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS custom properties, a color list, font-family declarations, and page text — no rendered screenshots, computed styles, or interaction states were captured. Color **roles** (primary vs. accent vs. surface) are inferred from variable names (e.g., Judge.me's `--jdgm-primary-color`) and contextual reuse, not from a confirmed brand style guide. Typography **sizes, weights, and letter-spacing** are proposed values consistent with a snack-DTC aesthetic; only the font-family names (Figtree, Nunito Sans, Baskerville, Arial, Helvetica) are directly observed, and Baskerville/monospace could not be confidently assigned to a role and were omitted. Border-radius values beyond the single observed 8px fragment and the explicit `0` for Judge.me elements are proposed defaults. No hover, focus, error, loading, or mobile-menu states were observed; all interaction states in the components above are proposed. Licensing and hosting/availability of Figtree and Nunito Sans were not verified from the supplied evidence.
