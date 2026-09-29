---
version: alpha
name: "Melissa Joy Manning"
source_url: "https://melissajoymanning.com"
captured_at: "2026-09-28T09:50:25.765466+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Melissa Joy Manning is a Certified Green California jewelry studio producing handmade,
  heirloom-quality earrings, rings, necklaces and bridal pieces. The observed CSS is Shopify
  theme output (theme.css with flickity carousels, EasyLockdown gating, model-viewer support)
  layered over a neutral, gallery-like palette: near-white canvas (#ffffff, #fafafa, #f7f7f7),
  soft warm-grey borders (#d0d0ce, #dedede), and charcoal-to-black text (#000000, #212121,
  #333333). A muted brass/gold tone (#ab8c52) appears in the supplied palette and is inferred
  here as the brand's primary accent, consistent with fine-jewelry positioning; this role is
  not directly confirmed by a labeled CSS declaration. Soft blush and mauve tones (#f9dee5,
  #775155, #af7b88) are inferred as secondary accents for bridal/collection callouts. Two font
  families are observed in evidence — Atkinson (Bold/Regular) and Figtree/Montserrat — used
  here as display and body/UI pairings respectively, with generic sans-serif fallbacks since
  no @font-face or licensing data was supplied. Root CSS variables expose structural values
  (menu-height 143px, header-height 100px, footer-height 500px, announcement 33px) which are
  treated as evidence of a sticky-header, generous-footer layout, not as fully verified visual
  behavior. All component patterns below are proposed interpretations for a restrained,
  editorial handmade-jewelry storefront.

colors:
  primary: "#ab8c52"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#d0d0ce"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-blush: "#f9dee5"
  accent-mauve: "#775155"
  accent-clay: "#af7b88"
  link: "#1990c6"
  border-light: "#dedede"
  overlay-scrim: "#0000004d"
typography:
  display-xl: {fontFamily: "Atkinson Bold, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Atkinson Bold, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.6px}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "100px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.accent-mauve}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  appointment-cta:
    backgroundColor: "{colors.accent-clay}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg} {spacing.xl}"

## Components
**button-primary** is proposed as the main add-to-cart / shop-now call to action, using the inferred brass accent against a white label, matching the fine-jewelry, low-saturation feel of the observed palette.

**button-secondary** proposes an outlined variant for lower-emphasis actions (e.g. "Explore Custom Jewelry," "Shop Sapphire") using the observed hairline grey (#d0d0ce) as the border, keeping the ink text on a transparent field.

**text-input** covers search fields and form inputs (contact, newsletter signup). Border color reuses the hairline token; no focus-state color was observed in evidence, so focus styling is left undefined/proposed.

**nav-bar** reflects the root CSS variable `--header-height: 100px` and `--menu-height: calc(143px)` found in evidence, interpreted here as a two-tier header (utility bar + primary nav) on a white background with black text/links, consistent with the `--link`/`--link-hover: #000000` declarations observed.

**product-card** is a proposed pattern for grid listings (Earrings, Necklaces, Rings, Bracelets) using a slightly off-white card surface (#fafafa) and hairline border, since no explicit card-shadow value was supplied beyond the flickity button's box-shadow reference.

**hero** models the homepage banner pattern ("Elegant & Enchanting," "Redesign an Heirloom") on the soft surface background, using the display-xl type scale; exact hero height/imagery was not observed and is proposed.

**footer** is inferred from the `--footer-height: 500px` root variable, styled here as a dark, high-contrast band to visually anchor the extensive footer link list (Company, Orders, Connect) noted in the page text; the dark footer treatment itself is a proposed choice, not confirmed by a background-color declaration.

**badge** proposes a soft blush pill for merchandising labels such as "New Arrivals" or birthstone callouts, drawing on the observed #f9dee5/#775155 pairing.

**search** models the header search affordance ("Search / Clear") referenced in the page text, styled as a bordered field on the soft surface tone.

**appointment-cta** is a category-appropriate component for the "Virtual Shopping Appointment" and custom/bridal booking prompts repeated throughout the evidence, using the clay/mauve accent (#af7b88) to differentiate service-oriented CTAs from product CTAs.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <768px | Collapsed hamburger, single-column stacked menu | 1–2 col product grid |
| Tablet | 768–1023px | Condensed horizontal nav or hamburger | 2–3 col grid |
| Desktop | ≥1024px | Full mega-menu (multi-level, per page text) | 3–4 col grid |

Touch targets should be at least 44×44px for nav, cart, and search icons. Given the deep multi-level menu structure implied by the repeated "Show menu / Exit menu" text (Jewelry → Shop by Collection → Custom Jewelry → Design Your Own, etc.), mobile should collapse into an accordion/drill-down pattern rather than flyout hover menus. None of this nesting behavior was directly observed in rendered layout, only inferred from menu label repetition in the text excerpt.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered screenshots, computed styles, or DOM measurements were available. Several CSS custom properties (`--COLOR-BG`, `--COLOR-PRIMARY`, `--COLOR-LINK`, etc.) reference theme-level variables whose resolved hex values were not present in the supplied evidence, so color-role assignments above (primary, accent, link) are best-effort inferences from the flat palette list, not confirmed mappings. The `--RADIUS` variable used in `.flickity-prev-next-button` was not resolved to a pixel value, so the rounded scale is proposed. Root variables for header/footer/announcement height (100px, 500px, 33px, 143px) are taken as structural evidence but full page layout, spacing rhythm, and grid columns were not observed. No hover/focus/active interaction states, mobile menu animation, or cart drawer behavior were observed. Atkinson, Figtree, and Montserrat are used as the literal font-family names found in evidence; actual font files, weights available, and licensing terms were not verified.
