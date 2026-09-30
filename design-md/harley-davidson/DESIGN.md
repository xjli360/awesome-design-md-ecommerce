---
version: alpha
name: "Harley-Davidson"
source_url: "https://harley-davidson.com"
captured_at: "2026-09-28T04:30:17.975643+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation reflects the Harley-Davidson USA site's motorcycle-parts storefront, built on a stark black/white/orange foundation. The dominant accent, `#fa6600`, appears on the newsletter heading and on primary CTA buttons (cookie-consent "accept" action), with `#e65200` as its confirmed hover/focus state. A secondary neutral action uses `#4e4e4e` with `#626262` hover, suggesting a paired primary/secondary button system. Borders and disabled/secondary UI elements use mid-grays (`#757575`, `#cccccc`, `#e1e1e1`), while panel backgrounds in the parts-fitment widget use light off-white surfaces (`#f4f4f4`). Canvas is pure white; ink is pure black, consistent with a high-contrast industrial brand.

  Typography is confirmed as Franklin Gothic ATF across body copy and interactive controls, with sans-serif system fallbacks (Arial, Helvetica, Noto Sans) for non-Latin locales. Buttons render bold and uppercase/capitalized, reinforcing a rugged, mechanical tone appropriate to motorcycle hardware.

  Body text color, card surfaces, and most spacing/type scale values are not directly observed and are marked inferred/proposed below, built from the nearest plausible palette entries and Harley's utilitarian, high-contrast aesthetic.

colors:
  primary: "#fa6600"
  primary-hover: "#e65200"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#757575"
  hairline: "#e1e1e1"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  surface-dark: "#141414"
  on-primary: "#ffffff"
  neutral-deny: "#4e4e4e"
  neutral-deny-hover: "#626262"
  accent-info: "#0067f4"
  accent-success: "#468600"
  accent-danger: "#c30000"
typography:
  display-xl: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Franklin Gothic ATF, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px, textTransform: uppercase}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    hover: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.neutral-deny}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    hover: "{colors.neutral-deny-hover}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.muted}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    height: "2.25rem"
    typography: "{typography.body-sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    width: "11.125rem"
    padding: "{spacing.base} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  part-fitment-panel:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"

## Components
**button-primary** is the confirmed CTA style, sourced from the cookie-consent accept button: orange fill, white uppercase text, with a darker orange hover state observed directly in CSS.

**button-secondary** mirrors the consent "deny" control — a dark-gray fill with a slightly lighter gray hover — proposed here as the general secondary-action pattern for cart/wishlist or "compare" actions on part listings.

**text-input** is proposed; no explicit input styling was captured, so border and radius are inferred from the nearby `.navbar-secondary-sub-container-right-options-search-button` treatment for visual consistency.

**nav-bar** height (2.25rem) and hairline border are directly observed on the header search trigger; overall nav-bar chrome (logo placement, mega-menu) is not observed and is proposed as a standard fixed white header.

**search** reproduces the observed search-button dimensions and 1px `#757575` border with 2px radius; the unusually large vertical padding (1rem) is taken as-is from the source declaration.

**product-card** is proposed for parts/accessories listings, using the light `#f4f4f4` surface seen in the ARI parts-fitment widget as a plausible card background, with standard hairline border and mid-scale radius.

**hero** is proposed as a full-bleed black band with large white display type, consistent with Harley's high-contrast black/white/orange identity; no hero markup or imagery was captured in evidence.

**footer** is proposed as a near-black (`#141414`) band with small white/gray body text, following the brand's dark-surface convention seen in `surface-dark`; actual footer structure is unobserved.

**badge** (e.g., "New," "In Stock," sale tags) is proposed using the primary orange as a compact pill, a common e-commerce pattern not directly evidenced but consistent with the CTA color usage.

**part-fitment-panel** is a category-specific component modeled on the observed `#ariPartStream` motorcycle-model/part-selection widget, using its light gray background and black border-accent utility classes as a base for a "select your bike" fitment tool.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <480px | single-column, nav collapses to hamburger + icon search |
| tablet | 480–1024px | 2-column product grids, search bar may collapse to icon |
| desktop | 1024–1440px | full nav-bar with visible search field (11.125rem) |
| wide | >1440px | max-width content container, expanded hero |

Touch targets should be a minimum of 44×44px, exceeding the observed 2.25rem (36px) search-button height for mobile contexts. Navigation and fitment-panel filters are expected to collapse into accordions or drawers on narrow viewports; this collapse behavior was not observed and is a proposed pattern only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted from static CSS/HTML sources; no live rendering, computed layout, or viewport testing was performed.
- Body text color (`#272727`) and several surface roles (`surface-soft`, `surface-card`) are inferred from the nearest plausible neutral in the observed palette, not confirmed as body/copy colors.
- Type scale sizes beyond the observed `13px` (ari part-line text) are proposed estimates for a typical retail/e-commerce hierarchy.
- Interaction states (focus rings, disabled inputs, form validation colors) beyond the two documented button hover rules are proposed, not observed.
- Mobile/responsive layout, navigation collapse, and touch behavior were not observed and are recommendations only.
- Franklin Gothic ATF availability, licensing, and web-font delivery were not verified; fallback stack assumes standard system sans-serif support.
- Additional palette entries (e.g., `#0067f4`, `#468600`, `#c30000`) appear in evidence without confirmed semantic role; they are mapped here as plausible info/success/danger accents pending verification.
