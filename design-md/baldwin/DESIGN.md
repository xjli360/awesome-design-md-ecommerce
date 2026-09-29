---
version: alpha
name: "Baldwin"
source_url: "https://baldwinhardware.com"
captured_at: "2026-09-28T09:05:29.916065+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Baldwin Hardware's site CSS confirms a neutral, high-contrast system: white canvas (#ffffff), near-black body copy (#212529), and pure black (#000000) as the primary action color used on .btn-primary and .btn-black. Bootstrap-derived utility colors (grays #6c757d/#343a40/#f8f9fa, borders #dee2e6, status reds/greens/yellows) remain in the CSS variable set alongside three brand-named custom properties — --estate (#af4640), --prestige (#de9c5c), --reserve (#45707e) — and --gold (#98846d), which map to Baldwin's Estate, Reserve, and cabinet/brass product portfolios referenced in the page copy. These portfolio colors are treated as accent/identifier tones rather than primary UI color, since no selector usage was supplied beyond the :root declaration.
  Typography is confirmed only through the body and heading rules: the system font stack (-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif) at 16px/1.5 for body text, with headings set to font-weight:500 and line-height:1.2 via `font-family: inherit`. Although the asset list contains Montserrat, Gotham SSm, Lato, and condensed display fonts, no CSS rule in evidence applies them, so this spec does not assign them to any typographic role — all tokens below use the confirmed system stack. The resulting interpretation is a restrained, brass-and-black luxury-hardware aesthetic: black CTAs on white surfaces, warm portfolio accents used sparingly for badges/category tags, and generous whitespace suited to a durable-goods catalog.

colors:
  primary: "#000000"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark: "#343a40"
  estate: "#af4640"
  prestige: "#de9c5c"
  reserve: "#45707e"
  gold: "#98846d"
  danger: "#dc3545"
  success: "#28a745"
  warning: "#ffc107"
  info: "#17a2b8"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.estate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  finish-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** reflects the confirmed `.btn-primary`/`.btn-black` rule (`background-color:#000; color:#fff; border-color:#000`), used for the main hover/active states as documented in CSS; treated as the site's principal call-to-action (e.g., "Start Designing," "Shop Now").

**button-secondary** is proposed from the `.btn-secondary` rule (`background-color:#6c757d`), a Bootstrap-derived secondary action style likely used for lower-emphasis actions such as "Compare Portfolios."

**text-input** is an inferred pattern for search and form fields; no explicit input CSS was supplied, so border and padding values are proposed defaults consistent with the Bootstrap-based `--gray-200`/hairline tones observed in the palette.

**nav-bar** is inferred from the extensive multi-level menu structure in page text (Products, Portfolios, Support, etc.); a white background with hairline bottom border is proposed for a clean utility-hardware catalog header.

**product-card** is proposed for catalog/grid listings (knobs, levers, handlesets); card surface and border use observed neutral tones, with title/body typography mapped to confirmed heading/body rules.

**hero** models the homepage's large brand statement ("Baldwin. Crafted Legacy. Enduring Luxury.") as a dark, full-bleed band; ink background with white text is proposed since no hero-specific CSS was supplied.

**footer** is proposed using the darker gray (`--dark:#343a40`) for a conventional dense-link footer, consistent with the site's multi-section navigation described in page text.

**badge** repurposes the brand portfolio color `--estate` (#af4640) as a small labeling chip for portfolio tags (Estate/Reserve/Prestige), a proposed reuse of an observed CSS variable rather than a confirmed component.

**search** is an inferred lightweight input pattern for the header search affordance implied by "Wishlist / Where To Buy / Customer Portal" navigation, styled with the light surface tone.

**finish-swatch-selector** is a category-specific, proposed component for selecting hardware finishes (referenced in page text via "Accessory Finish"), styled as small circular swatches with a black active-state ring, using only palette-observed colors.

## Responsive Behavior
Recommended, not measured:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| xs | 0–575px | Single-column stack; collapsed hamburger nav; full-width buttons |
| sm | 576–767px | Two-column product grid; inline search icon |
| md | 768–991px | Three-column product grid; horizontal top nav begins |
| lg | 992–1199px | Full mega-menu nav; four-column grid |
| xl | ≥1200px | Max-width container; five-column grid, expanded hero |

Breakpoints reuse the confirmed Bootstrap `--breakpoint-*` custom properties (576/768/992/1200px). Touch targets are recommended at a minimum 44×44px for nav and swatch controls; mobile nav collapse behavior is proposed, not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived solely from static CSS/text extraction; no rendered layout, hover/focus states, animation, or JavaScript-driven interaction (e.g., Lock Designer configurator) was observed. Font-family roles are restricted to the system stack confirmed in the `body`/`h1–h6` rules; Montserrat, Gotham SSm, Lato, and condensed families appear only in the raw font-asset list without an accompanying selector, so they are excluded from all typography tokens pending further evidence. Semantic color roles (ink/muted/hairline/surface tones) are inferred groupings of Bootstrap-style CSS variables, not brand-declared design-system names. All pixel sizes in the typography scale beyond the confirmed 16px body/500-weight headings are proposed placeholders. Mobile/responsive behavior, breakpoint-specific component states, and custom-font licensing/availability have not been verified against the live site.
