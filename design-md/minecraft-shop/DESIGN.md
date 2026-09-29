---
version: alpha
name: "Minecraft Shop"
source_url: "https://shop.minecraft.net"
captured_at: "2026-09-29T04:14:12.276925+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Minecraft Shop presents official game-branded merchandise on a clean, neutral
  Shopify storefront. The observed base palette is restrained: white canvas
  (#ffffff), a warm charcoal body/ink color (#454442) set on html/body, and a
  soft off-white border tone (#e8e8e1) used for secondary buttons. Primary
  call-to-action buttons use an emerald green (#0e8543) with white text and
  uppercase, widely-tracked labels, while product-grid "quick view" buttons
  use a distinct sky blue (#35aeef) — both are treated here as brand action
  colors, with green as primary and blue as a secondary/interactive accent.
  Additional palette values (#ffb439, #d02e2e, #52a535, #86d562) appear in the
  broader evidence set without confirmed component roles; they are mapped here
  to plausible badge/alert uses and explicitly labeled inferred. Typography
  uses SegoePro-Bold for headings (rendered at font-weight 400 per observed
  CSS) and SegoePro-Regular/NotoSans-Regular for body copy at a small 13.6px
  base size with generous 1.6 line-height. Buttons are square-cornered
  (border-radius:0) and heavily letter-spaced, giving the interface a blocky,
  game-merch personality distinct from typical soft-rounded ecommerce UI.

colors:
  primary: "#0e8543"
  ink: "#454442"
  canvas: "#ffffff"
  body: "#454442"
  muted: "#717171"
  hairline: "#e8e8e1"
  surface-soft: "#f6f6f6"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-blue: "#35aeef"
  accent-warm: "#ffb439"
  accent-alert: "#d02e2e"
  surface-alt: "#f2f2f2"
typography:
  display-xl: {fontFamily: "SegoePro-Bold, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1, letterSpacing: 0em}
  display-md: {fontFamily: "SegoePro-Bold, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1, letterSpacing: 0em}
  title-md: {fontFamily: "SegoePro-Bold, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  body-md: {fontFamily: "SegoePro-Regular, sans-serif", fontSize: 13.6px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0em}
  body-sm: {fontFamily: "SegoePro-Regular, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0em}
  caption: {fontFamily: "SegoePro-Regular, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "SegoePro-Bold, sans-serif", fontSize: 13px, fontWeight: 700, lineHeight: 1.42, letterSpacing: 0.3em}
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
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentButton: "{colors.accent-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    ctaBackground: "{colors.primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-chart-trigger:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: "underline"
    padding: "{spacing.sm} {spacing.none}"

## Components
**button-primary** reflects the confirmed `.btn` rule: emerald green (#0e8543) fill, white uppercase text, square corners (border-radius:0), and very wide 0.3em letter-spacing — used for primary purchase/CTA actions like "Shop Now" and "Add to Cart."

**button-secondary** mirrors `.btn--secondary`: transparent background, ink-colored text, and a light hairline border (#e8e8e1), proposed for "View Details" or filter-adjacent actions.

**text-input** is a proposed pattern (not directly observed) using the same hairline border and canvas background as buttons, for search and account forms, with small rounding for visual softness against the otherwise square button system.

**nav-bar** is inferred from the extensive "Products / Characters & Mobs / Collections" mega-menu text content; structure, sticky behavior, and exact spacing are not measured, only the canvas background and ink text are grounded in the base theme rule.

**product-card** combines the observed light surface tone (#eeeeee, drawn from the general palette) with the confirmed accent-blue (#35aeef) "quick view" button seen repeatedly in grid-item selectors, used for the plush/apparel/collectible listing grids.

**hero** is a proposed large promotional band (e.g., "Dungeons II — The official collection is live!") using display-md heading typography and the primary button; visual proportions are not observed, only typographic and color tokens are grounded.

**footer** is inferred — no footer-specific CSS was supplied — so it reuses the neutral surface-soft background and hairline border already confirmed elsewhere in the theme, avoiding invented brand-dark treatments.

**badge** is a proposed small pill for "New" and sale flags implied by repeated "New Quick view" content, using the warm accent (#ffb439) which is present in the palette but has no confirmed component binding.

**search** proposes a standard bordered field consistent with the site's input/button hairline treatment; no dedicated search-bar CSS was supplied.

**size-chart-trigger** reflects real third-party CSS (`scr-open-size-chart`) for an underlined, transparent-background text link used on apparel product pages — a category-appropriate pattern for a clothing/merch storefront, mapped to the closest available ink hex since the exact `rgb(61,66,70)` value isn't in the supplied hex list.

## Responsive Behavior
This is a recommendation only; no live responsive behavior was observed.

| Breakpoint | Width      | Layout guidance                              |
|-----------|------------|-----------------------------------------------|
| sm        | ≤480px     | Single-column product grid, collapsed nav     |
| md        | 481–768px  | 2-column product grid, hamburger nav          |
| lg        | 769–1024px | 3-column grid, inline top nav with dropdowns  |
| xl        | ≥1025px    | 4-column grid, full mega-menu on hover        |

Touch targets should be at least 44×44px, applying to `button-primary`/`button-secondary` padding. Mega-menu categories (Apparel, Accessories, Home & Office, Toys & Books, Characters & Mobs, Collections) should collapse into an accordion on mobile. None of this is measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
Evidence is static CSS/text extraction only; no rendered layout, breakpoints, hover/focus states, or JS-driven interactions (mega-menu, cart drawer, quick-view modal) were observed. Font availability and licensing for `Minecraft-Seven`, `Minecraft-Ten`, `SegoePro-Bold/Regular`, and `NotoSans-Bold/Regular` are unverified proprietary/custom families; fallbacks assume standard sans-serif. Roles for several palette colors (#ffb439, #d02e2e, #52a535, #86d562, #9bf00b, #299da6, etc.) are inferred rather than confirmed against specific components, since no selectors tying them to badges/alerts were supplied. The `size-chart-trigger` color mapping is an approximation from an RGB value not present in the supplied hex palette. All sizing outside explicitly quoted CSS (13.6px body, 13px button, letter-spacing 0.3em, line-height 1.6/1.42/1) is proposed. Mobile/tablet layouts, grid column counts, and hero proportions are design proposals, not measurements.
