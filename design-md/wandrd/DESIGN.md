---
version: alpha
name: "Wandrd"
source_url: "https://wandrd.com"
captured_at: "2026-09-29T04:16:25.000871+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in CSS extracted from wandrd.com's storefront and its embedded review widget (Okendo). The confirmed color palette centers on a warm orange-red accent (#ed5338, reused for the review widget's button background, border, and hover states) against a near-black ink (#111111) used as the widget's primary text color. Canvas is pure white (#ffffff). A muted slate-blue (#676986) appears as a secondary text color in review metadata, and light neutrals (#f7f7f8, #f4f4f6, #dedede, #e5e5eb) are inferred as soft surface and hairline tones consistent with a minimal ecommerce shell. Product swatch colors (clay, green, tan) are also present in the palette and are proposed here as optional accent roles rather than confirmed UI colors.
  Typography is a significant gap: the only concrete font-family token observed in the CSS is "monospace" (from Okendo's icon-font fallback chain), while the storefront's own body and display type reference unresolved CSS custom properties (--font-typeface-body, --font-typeface-display) whose actual values were not captured. This spec therefore uses monospace with sans-serif fallback as the sole documented family across all text roles, flagged explicitly as a coverage limitation rather than a stylistic choice. Layout patterns (buttons, uppercase tracking, 0-radius controls) are drawn directly from .btn--primary and Okendo button rules; all other components are proposed, not observed.

colors:
  primary: "#ed5338"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#272d45"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  on-primary: "#ffffff"
  accent-sale: "#ff3f28"
  accent-clay: "#a46630"
  accent-green: "#476b5c"
  surface-alt: "#e5e5eb"
  border-neutral: "#999999"
typography:
  display-xl: {fontFamily: "monospace, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "monospace, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "monospace, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "monospace, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "monospace, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "monospace, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "monospace, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.7px}
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
    padding: "{spacing.lg} {spacing.xxl}"
    textTransform: "uppercase (observed in .btn--primary)"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-neutral}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    proposed: true
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
    proposed: true
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "proposed, not measured"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    saleColor: "{colors.accent-sale}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    proposed: true
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    proposed: true
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
    proposed: true
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
    proposed: true
  color-swatch-selector:
    size: "24px, proposed"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
    swatchColors: ["{colors.accent-clay}", "{colors.accent-green}", "#d1c79d", "#a15325"]
    proposed: true

## Components
**button-primary** reflects the one directly observed interactive pattern in the CSS: `.btn--primary` uses uppercase text, 0.05em letter-spacing, a bold display-weight font, and generous horizontal padding (3.5rem), rendered here with the confirmed orange accent as background.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Add to Wishlist"), inferred from typical ecommerce patterns since no secondary button CSS was captured.

**text-input** is proposed for search and account forms; no live input styling was present in the evidence, so border, radius, and padding are conservative defaults.

**nav-bar** represents the site header implied by the page-text navigation (Backpacks, Slings, Accessories, Sale) but no header CSS (height, background, sticky behavior) was captured, so all layout values are proposed.

**product-card** models the repeating product grid shown in page text (PRVKE, ROGUE, CARRYALL, TRANSIT with swatches and pricing), using the light card surface and hairline border inferred from the neutral palette.

**hero** represents the "AWARD WINNING PRVKE" banner referenced in the text excerpt; typography and layout are proposed since no hero-specific CSS was supplied.

**footer** is proposed using an inverted dark-on-light treatment; no footer CSS rules were present in the evidence.

**badge** covers "Sale," "Best Seller," and "New" tags visible in the page text, using the confirmed sale-red accent color.

**search** is a proposed lightweight input treatment for the site's search icon/overlay, referenced only by the word "Search Search Search" in page text with no accompanying styles.

**color-swatch-selector** is a category-appropriate proposed component for the many bag color options (Black, Aegean Blue, Wasatch Green, Sedona Orange, etc.) enumerated in the text; circular swatches with an accent-colored active ring are a common pattern for this product type, not a captured style rule.

## Responsive Behavior
This is a recommendation, not measured site behavior, since no media queries or breakpoint values were present in the supplied evidence.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, sticky "Add to Cart" bar |
| Tablet | 600–1024px | 2-column product grid, condensed nav |
| Desktop | >1024px | Full mega-menu nav (Backpacks/Slings/Accessories), 3–4 column product grid |

Touch targets should be at least 44×44px for swatch selectors and buttons; the mega-menu (visible in page text as nested Backpacks/Slings/Accessories submenus) should collapse to an accordion pattern on mobile. All figures are proposed defaults, not measured from the live site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS/text extraction does not capture rendered layout, so header height, grid columns, hero imagery, and mobile menu behavior are unobserved and marked proposed.
- The site's actual body/display font is set via unresolved CSS custom properties (`--font-typeface-body`, `--font-typeface-display`); no concrete font name was present in the evidence, so `monospace` (the only literal family string captured, from an icon-font fallback chain) is used uniformly with a generic sans-serif fallback. This is a coverage limitation, not a confirmed brand typeface.
- Many palette hexes originate from Okendo's review-widget CSS variables or product color-swatch data rather than confirmed core UI chrome; semantic role assignments (surface, hairline, muted) are inferred from context, not verified against rendered screenshots.
- Interaction states (hover, focus, active) beyond the Okendo button rules were not observed for native storefront components.
- No custom font licensing or webfont loading was verified; if a proprietary display font exists, it is not evidenced here.
- Spacing scale and border-radius values are proposed conventions except where `border-radius:0` was directly observed on Okendo buttons.
