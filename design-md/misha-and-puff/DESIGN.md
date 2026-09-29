---
version: alpha
name: "Misha & Puff"
source_url: "https://misha-and-puff.com"
captured_at: "2026-09-29T04:03:41.273105+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Misha & Puff's storefront CSS shows a restrained, editorial system built on Shopify theme variables:
  --color-foreground and --color-button both resolve to rgb(18,18,18) (#121212), --color-background and
  --color-button-text resolve to white, and badge tokens reuse the same near-black on white pairing. This
  points to a deliberately monochrome interface — black type and controls on a white canvas — with color
  reserved for occasional accent use. The supplied palette includes warm, muted accent hues (#fae3b1,
  #edea62, #ec5123, #3c96ee, #101820) that are not tied to specific selectors in the evidence; their
  application here (badges, sale/alert states, decorative accents) is inferred, not confirmed.
  Two typefaces are directly observed in header CSS: 'Overpass Mono Custom' (with 'Courier New', monospace
  fallback) drives top-level and level-2 navigation labels in uppercase, tightly tracked mono type — a
  distinctive, slightly technical counterpoint for a heirloom/craft-positioned kids brand. 'Inter Custom'
  (Arial, sans-serif fallback) is used for deeper submenu links and is inferred here as the general body/UI
  sans-serif, since var(--font-body-family) itself is not resolved in the evidence. The Judge.me review
  widget sets --jdgm-border-radius: 0, suggesting the brand favors square, unrounded UI edges; this is
  treated as a signal, not a confirmed global rule, so a light rounding scale is still offered for
  flexibility. All layout figures below (hero, card, breakpoints) are proposed conventions for an ecommerce
  kids-apparel site, not measured observations.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#7b7b7b"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#fae3b1"
  accent-citrus: "#edea62"
  accent-coral: "#ec5123"
  accent-blue: "#3c96ee"
  deep-navy: "#101820"
  border-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "'Inter Custom', Arial, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Inter Custom', Arial, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.2px}
  title-md: {fontFamily: "'Overpass Mono Custom', 'Courier New', monospace", fontSize: 14px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.2px}
  body-md: {fontFamily: "'Inter Custom', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0.6px}
  body-sm: {fontFamily: "'Inter Custom', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.1px}
  caption: {fontFamily: "'Overpass Mono Custom', 'Courier New', monospace", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "'Overpass Mono Custom', 'Courier New', monospace", fontSize: 12px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid transparent"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-strong}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** renders the near-black/white pairing taken directly from --color-button and
--color-button-text, in the uppercase monospace button typography implied by the mono nav styling.
**button-secondary** proposes an outlined inverse for tertiary actions (e.g., "Continue shopping"), using
the same ink color as border and text on a white field; the outline treatment is inferred, not observed.
**text-input** is a proposed form/newsletter field using the observed hairline gray for a subtle border and
body-sm type; focus/error states are not observed and are proposed conventions only.
**nav-bar** reflects the header CSS directly: level-1 and level-2 mega-menu links use Overpass Mono Custom,
uppercase, tightly tracked, while the header background is transparent until scroll (per
.scrolled-past-header), at which point it switches to the solid background token — this scroll-state
behavior is evidenced in CSS but its visual timing/animation is not observed.
**product-card** is a standard commerce pattern proposed for listing kids/baby/adult apparel; the flat
hairline border and square corners align with the jdgm zero-radius signal, though card geometry itself is
not directly measured.
**hero** proposes a soft-tinted (surface-soft) banner for campaigns like "The Fall Collection," pairing a
large display headline with body copy; exact hero sizing and imagery treatment are not in the evidence.
**footer** inverts to the primary ink background with white text, mirroring the button color inversion
already established in the token set; link density and column layout are proposed, not observed.
**badge** models sale/new labels using the same foreground-on-background/border logic as
--color-badge-foreground, --color-badge-background, and --color-badge-border, kept flat-edged per the
zero-radius signal.
**search** is a proposed lightweight input matching text-input styling, since no distinct search-specific
CSS was supplied.
**size-selector** is the category-appropriate component for kids apparel, modeling the site's explicit
"Shop by Size" groupings (e.g., 2-4 Years, 0-6 Months) as a chip/pill row using caption-scale mono type,
with an inverted (ink-on-white → white-on-ink) selected state; interaction states are proposed, not observed.

## Responsive Behavior
| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| Mobile    | < 480px     | Single-column product grid, nav collapses to drawer (menu-drawer classes observed in CSS support this) |
| Tablet    | 480–959px   | Two-column product grid, condensed mega-menu |
| Desktop   | ≥ 960px     | Full mega-menu with level-2/level-3 indents (--mp-drawer-indent-l2/l3 observed), multi-column grids |

Touch targets are recommended at a minimum 44×44px for buttons and size-selector chips. The presence of
menu-drawer__menu-item classes in the CSS confirms a drawer pattern exists for mobile navigation, but its
open/close animation, breakpoint trigger, and exact collapse width are not observed and are proposed here
as reasonable defaults for a Shopify-based storefront.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties, selector rules, and page text only — no
rendered screenshots, computed layouts, or interaction traces were available. The resolved value of
var(--font-body-family) was not present in evidence, so body/display typography using "Inter Custom" is an
inferred choice based on its confirmed use in submenu links, not a confirmed global body font. Several
palette colors (e.g., #fae3b1, #edea62, #ec5123, #3c96ee, #2a0001) appear in the supplied palette without a
selector tying them to a specific UI role; their assignment to accents/alerts above is inferred and should
be verified against live rendering. Rounded and spacing scales follow a generic proposed system, informed
only loosely by the observed --jdgm-border-radius: 0 signal. Hover, focus, error, and mobile-drawer
animation states are not observed and are marked proposed throughout. Custom font family availability,
licensing, and actual file sources ('Overpass Mono Custom', 'Inter Custom', etc.) were not verified beyond
their appearance as CSS variable names.
