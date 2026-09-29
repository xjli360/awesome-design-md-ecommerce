---
version: alpha
name: "Microjig"
source_url: "https://microjig.com"
captured_at: "2026-09-29T04:11:38.851671+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Microjig's stylesheet exposes a small, deliberate palette anchored by a deep
  slate-green (--slate-green #00635b, --dark-slate-green #003e39) that the CSS
  itself assigns to the primary `.button` component, plus a brighter sea-green
  (--sea-green #009677) used as a hover/active state on the same button family.
  Neutral structure comes from near-black (--black #111) body copy on white
  canvas, with light gray (--gainsboro #ddd, --white-smoke #f7f7f7) hairlines
  and soft surfaces. A warm burlywood (--debc8b) tints a "ghost.gold" button
  variant, and isolated accents — gold (#ffc72c/#f8cd49), crimson (#cc0033),
  and two blues (#3898ec from the legacy Webflow default button, #0066cc as a
  named --royal-blue token) — appear in the source but are not clearly tied to
  primary navigation; their role here is inferred as secondary/alert accents
  rather than brand-defining colors.

  Typography is dominated by "Neue Haas Grotesk Display Pro 65 Md," which the
  CSS applies to both body text and headings (h1 at 44px/62px line-height),
  suggesting a single medium-weight display face carries most of the site's
  voice, with "Neue Haas Grotesk Text Pro 55 Rg" reserved for lighter body
  copy. Arial/Helvetica/sans-serif remain as reset fallbacks. The interpretation
  below extrapolates a restrained industrial-tool aesetic — functional buttons,
  clear hairlines, generous whitespace — appropriate to a precision-hardware
  storefront, while explicitly flagging sizes and states not present in the
  supplied CSS as proposed.

colors:
  primary: "#00635b"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-gold: "#ffc72c"
  accent-burlywood: "#debc8b"
  success-hover: "#009677"
  alert: "#cc0033"
  link-blue: "#0066cc"
  legacy-blue: "#3898ec"
  deep-teal: "#003e39"
  navy: "#004183"
typography:
  display-xl: {fontFamily: "'Neue Haas Grotesk Display Pro 65 Md', sans-serif", fontSize: 44px, fontWeight: 500, lineHeight: 1.41, letterSpacing: 0px}
  display-md: {fontFamily: "'Neue Haas Grotesk Display Pro 65 Md', sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  title-md: {fontFamily: "'Neue Haas Grotesk Display Pro 65 Md', sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Neue Haas Grotesk Display Pro 65 Md', sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Neue Haas Grotesk Display Pro 65 Md', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.71, letterSpacing: 1px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
    hoverBackgroundColor: "{colors.success-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: "2px"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-tertiary-gold:
    backgroundColor: "{colors.accent-burlywood}"
    textColor: "{colors.ink}"
    borderWidth: "0px"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    height: "64px"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "0 1px 3px {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-compatibility-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    headerBackgroundColor: "{colors.surface-card}"
    headerTypography: "{typography.body-sm}"
    cellTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** reflects the observed `.button` rule directly: slate-green
fill (`--slate-green`), white text, a large `2rem` border-radius mapped here
to `{rounded.full}`, and uppercase 14px/1px-tracked type. The `success-hover`
color (`--sea-green`) is applied as a hover state on similar buttons elsewhere
in the CSS (restock-notification button), so it is reused here as an inferred
hover token rather than a separately observed `.button:hover` rule.

**button-secondary** mirrors the observed `.button.ghost` pattern: transparent
background, 2px slate-green border, smaller 14px type. No hover/active state
was present in the evidence, so any state beyond default is proposed.

**button-tertiary-gold** is drawn from `.button.ghost.gold`, which swaps the
ghost border for a solid burlywood fill with no border — likely a limited or
promotional CTA treatment (e.g., "NEW PRODUCT" callouts) given the site copy's
references to limited-edition releases.

**text-input** is proposed; no dedicated input styling was present besides
generic reset rules (`button,input,...{color:inherit;font:inherit}`), so
border, radius, and padding are inferred from the site's overall restrained,
hairline-bordered aesthetic.

**nav-bar** is proposed as a white bar with hairline underline, consistent
with the reset `body{background:#fff}` and gray hairline tokens; the mega-menu
structure implied by the page text (Systems, Products, Bits, Specials) is not
verifiable from static CSS alone.

**product-card** is proposed to hold the many SKU listings (GRR-RIPPER
variants, MatchFit clamps, etc.) implied in the page text, using the light
`surface-card` tone and hairline border observed elsewhere as a general
surface pattern.

**hero** is proposed to house the "Work Safer. Work Smarter.®" headline using
the observed h1 scale (44px/62px) and a primary CTA button, consistent with
the "Explore NEW product releases! Shop now" copy.

**footer** uses the darker `deep-teal` (`--dark-slate-green`) as an inferred
brand-anchored footer background with gold link accents; no footer-specific
CSS rule was supplied, so background, link color, and layout are proposed.

**badge** is proposed for promotional flags such as "★ NEW PRODUCT" or
"Limited to 1,500 sets," using the crimson (`--crimson`) token observed in the
palette as an attention color, though its original applied context in the CSS
was not captured.

**search** is proposed for the "Search for products, topics, or keywords."
overlay referenced in the page text, styled with the soft-gray surface and
pill radius consistent with the button family's rounded language.

**spec-compatibility-table** is a category-appropriate addition for a
precision-tool brand: a compact table for listing kerf sizes, kit contents,
or bit/system compatibility (e.g., "STEEL PRO: 1/8" Kerf" vs. "Thin Kerf"),
styled with the same hairline borders and soft surface tones used elsewhere.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed)                              |
|-----------:|-------------|------------------------------------------------|
| mobile     | 0–479px     | single-column, nav collapses to `.w-nav-button` |
| tablet     | 480–767px   | 2-column product grid                          |
| small-desk | 768–991px   | 2–3 column grid, visible nav                   |
| desktop    | 992px+      | full nav, 3–4 column product grid              |

The `.w-nav-button` class present in the shared stylesheet confirms a
Webflow-style collapsing mobile nav exists, but its breakpoints, animation,
and open/closed visual treatment were not observed directly. All column
counts, touch-target sizing (recommend ≥44px), and stacking behavior above
are proposed conventions for a Webflow e-commerce site, not measured
behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS/text extraction only; no rendered layout, JavaScript-driven
  states, or interaction behavior (menu open/close, cart drawer, hover
  animations) were observed.
- Semantic role assignment for several palette colors (e.g., `#3898ec`,
  `#0066cc`, `#ffc72c`, `#f8cd49`, `#cc0033`) is inferred from adjacent selector
  names/usage context, not confirmed page placement.
- Typography sizes for `display-md`, `title-md`, `body-sm`, `caption`, and all
  letter-spacing/weight values not explicitly present in the supplied CSS are
  proposed, scaled from the one observed h1 and `.button` rule.
- Mobile/tablet layout, grid column counts, and breakpoint pixel values are
  proposed conventions, not measured from the live site.
- "Neue Haas Grotesk Display Pro 65 Md" and "Neue Haas Grotesk Text Pro 55 Rg"
  are proprietary commercial fonts; availability, licensing, and exact
  fallback behavior on the live site were not verified here.
- Component states (focus, disabled, error) for text-input and search are
  entirely proposed; none were present in the supplied evidence.
