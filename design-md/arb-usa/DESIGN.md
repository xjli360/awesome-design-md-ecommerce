---
version: alpha
name: "ARB USA"
source_url: "https://arbusa.com"
captured_at: "2026-09-28T09:09:26.087518+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  ARB USA's storefront CSS exposes a Bootstrap-derived design system layered with brand-specific overrides. The dominant brand color is a saturated red (#ed1c24), declared as `--primary` in the theme's root variables, paired with a near-black secondary (#202227). Body copy renders in Inter, a neutral grotesque sans-serif, at a base of 1rem/400 with a body-text color of #343841 on a white (#ffffff) canvas. Headings use a declared `navigo, sans-serif` family at weight 700 in pure black (#000000); navigo's availability and licensing are not verifiable from static CSS and are treated as inferred/unconfirmed. The palette also carries a full Bootstrap utility set (success, info, warning, danger, and their pale/dark table variants), which this spec treats as system/status colors rather than brand identity. Several darker red tones (#c61017, #af0e14, #7b0f13) appear alongside the primary red and are mapped here as plausible hover/active states for interactive red elements, though no direct hover-rule evidence was supplied. The overall interpretation favors a rugged, high-contrast, utilitarian aesthetic consistent with off-road/4x4 hardware merchandising: bold red CTAs, dark neutrals, generous whitespace, and dense category/product grids.

colors:
  primary: "#ed1c24"
  primary-hover: "#c61017"
  primary-active: "#af0e14"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#343841"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#202227"
  secondary-dark: "#111214"
  danger: "#dc3545"
  success: "#28a745"
  warning: "#ffc107"
  info: "#17a2b8"
  border-strong: "#ced4da"
typography:
  display-xl: {fontFamily: "navigo, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "navigo, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "navigo, sans-serif", fontSize: "22px", fontWeight: 700, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0.4px"}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.secondary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  vehicle-fitment-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    optionTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** — The main call-to-action treatment, using the observed `--primary` red at full opacity with white text. Proposed for "SHOP AWNINGS," "LEARN MORE," and add-to-cart actions. Hover/focus states using `primary-hover`/`primary-active` are proposed, not observed.

**button-secondary** — A dark, near-black alternate action button using `--secondary` (#202227), for lower-emphasis actions like "VIEW BUILD" links inside custom-build sections. Border and fill match to keep contrast against light backgrounds.

**text-input** — A standard form field (search, account, checkout) with white fill, hairline border (#dee2e6), and body typography. States (focus ring, error border using `danger`) are proposed conventions, not confirmed from supplied CSS.

**nav-bar** — Top utility/navigation bar inferred from "Account / Cart / Search" text in the excerpt. Modeled as a white bar with black text and a bottom hairline, consistent with the light canvas and dark heading color observed in theme.css.

**product-card** — Repeating unit for best-seller and category grids (compressors, bumpers, suspension, camping). White card surface, subtle border, medium rounding, with a bold title and regular-weight price line, reflecting the dense catalog structure in the page text.

**hero** — Full-bleed promotional band for slides like "HARD CASE AWNINGS BACK IN STOCK" and "$300+ IN FREE RECOVERY GEAR." Dark secondary background with large display typography and white text for strong contrast; exact hero styling not measured, layout is proposed.

**footer** — Dark, near-black footer (#111214, an observed swatch close to secondary) carrying social links (Facebook, Instagram, YouTube, LinkedIn) and support content, set in small body typography on white text for legibility against the dark fill.

**badge** — Small pill label for merchandising flags such as "TOP RATED," "TOP SELLER," and "Out of Stock." Modeled in primary red with white caption text and full rounding; actual badge color-coding (e.g., gray for out-of-stock) is a proposed refinement, not confirmed.

**search** — Header search affordance implied by "Search Submit Search Submit Search," styled as a soft light-gray field with hairline border, distinguishing it from the pure-white nav-bar background.

**vehicle-fitment-selector** — A category-specific proposed component for the "SHOP BY BUILD" grid (Tacoma, Land Cruiser, 4Runner, Jeep, Ford, Tundra, FJ Cruiser generations). Soft surface background, card border, and a title/option typography pairing to support scanning long lists of generation-specific fitments.

## Responsive Behavior
Recommended breakpoints (not measured from live layout), aligned to the Bootstrap-style variables present in theme.css (`--breakpoint-*`):

| Name | Width | Notes (proposed) |
|---|---|---|
| xs | 0px | Single-column stacks; nav collapses to menu icon |
| sm | 576px | 2-column product grids begin |
| md | 768px | Category tiles move to 3–4 columns |
| lg | 992px | Full nav bar with inline search/account/cart |
| xl | 1200px | Max content width reached |
| xxl | 1440px | Wide hero and multi-row build selectors |

Touch targets should target a minimum 44px height for buttons and nav items on small viewports; the "SHOP BY BUILD" and category grids should collapse to horizontally scrollable or stacked cards below `md`. This behavior is a design recommendation only and was not observed in a live responsive audit.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted statically from theme.css/vendor.css and page text; no live-rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed.
- The `navigo` heading font's actual availability, weight range, and licensing terms are unverified; it may be a custom/proprietary asset not confirmed as web-safe.
- Hover/active red shades (#c61017, #af0e14, #7b0f13) are inferred pairings with `--primary` based on palette proximity, not confirmed via explicit `:hover`/`:active` selectors.
- Component padding, sizing, and breakpoint values are proposed conventions based on typical Bootstrap-derived patterns, not measured pixel values from the live site.
- Mobile navigation collapse behavior, cart/search dropdown mechanics, and product-card grid responsiveness were not present in the supplied CSS rules and are marked proposed.
- Status colors (success/warning/danger/info and their table variants) are assumed to be inherited Bootstrap utility defaults rather than bespoke ARB brand decisions.
