---
version: alpha
name: "Graza"
source_url: "https://graza.co"
captured_at: "2026-09-28T04:31:57.249412+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Graza's public CSS surfaces a warm, produce-forward palette built around
  a chartreuse-lime brand color (#D1E030) paired with a soft peachy-cream
  background (#F6E6D9) and a deep olive-green text color (#3C422E). Secondary
  accents include a mint green (#9EEF80) and a golden yellow (#FBD535),
  consistent with a citrusy, kitchen-table brand voice. Review-widget and
  search-autocomplete variables expose a supporting neutral system (grays,
  a muted slate #676986, and darker navy tones) used for secondary UI chrome
  rather than brand expression; these are treated as inferred utility roles.
  Typography combines a humanist sans (Apercu) for interface and body text
  with two distinctive display faces — ITC Garamond Condensed for large
  serif headlines and GT Alpina Typewriter for small, typewriter-style
  labels or eyebrows — layered over system-font fallbacks. Interactive
  elements (the observed .oke-button) show a pill-shaped 30px radius, 1px
  bordered lime fill with olive text, suggesting a friendly, high-contrast
  CTA pattern reused here for buttons and badges. All layout, spacing
  rhythm, and responsive behavior below are proposed interpretations, not
  measured page geometry.

colors:
  primary: "#D1E030"
  accent: "#9EEF80"
  secondary: "#FBD535"
  ink: "#3C422E"
  canvas: "#F6E6D9"
  body: "#3C422E"
  muted: "#676986"
  hairline: "#DEDEDE"
  surface-soft: "#FFF4EC"
  surface-card: "#F4F4F6"
  on-primary: "#3C422E"
  stroke: "#9FCD7A"
  sand: "#E8D6C8"
  taupe: "#CCC0B6"
  navy: "#272D45"
  overlay: "#000000"
  white: "#FFFFFF"
  teal: "#00CAAA"
  teal-light: "#B2F9E9"
  link: "#007AFF"
typography:
  display-xl: {fontFamily: "'ITC Garamond Condensed', serif", fontSize: "64px", fontWeight: 500, lineHeight: 1.05, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'ITC Garamond Condensed', serif", fontSize: "40px", fontWeight: 500, lineHeight: 1.1, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Apercu, 'Helvetica Neue', Arial, sans-serif", fontSize: "24px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Apercu, 'Helvetica Neue', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Apercu, 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'GT Alpina Typewriter', 'Courier New', monospace", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Apercu, 'Helvetica Neue', Arial, sans-serif", fontSize: "16px", fontWeight: 500, lineHeight: 1, letterSpacing: "0px"}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 30px
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.white}"
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
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.base}"
  bottle-size-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    borderColor: "{colors.stroke}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** — A pill-shaped lime CTA with dark-olive text and a matching 1px olive border, directly reflecting the observed `.oke-button` review-widget variables (backgroundColor #D1E030, textColor #3C422E, borderRadius 30px). Proposed hover/active states darken or invert fill per the same variable pattern seen in the source (`backgroundColorHover`, `backgroundColorActive`).

**button-secondary** — An outlined variant for lower-emphasis actions (e.g., "Learn more"), using the same ink border and pill radius but transparent fill, inferred to complement the primary button without competing for attention.

**text-input** — A clean white field with a light hairline border, sized for comfortable tap targets; font and sizing mirror the widget's `font-family:inherit;font-size:1em` pattern. States (focus, error) are proposed, not observed.

**nav-bar** — A cream-background bar using the site's `--color-header`/`--height-bar:60px` variables as a size cue; assumed to hold logo, primary links, and cart/search icons in olive text. Sticky/scroll behavior is inferred, not confirmed.

**product-card** — A soft neutral card (surface-card #F4F4F6) with rounded corners for bottle imagery, an ITC-Garamond-adjacent title style, and a smaller price line; grid arrangement is a proposed pattern typical of an oil/vinegar catalog, not measured.

**hero** — A full-width introductory band on the warm highlight cream (#FFF4EC) using the large condensed-serif display style for headline copy over body-sans subtext; imagery placement is inferred from category convention, not observed markup.

**footer** — An inverted dark-olive band with cream text and mint-green links, giving contrast to the light body sections; column structure (newsletter, links, social) is a proposed convention for DTC food brands.

**badge** — A small pill label in golden yellow used for tags like "New" or dietary/certification callouts, sized for the typewriter-style caption font; exact copy and placement are not observed.

**search** — A pill-shaped input styled to align with the Algolia-autocomplete CSS variables present in source (`--aa-*` tokens), using white background, navy text, and muted placeholder; dropdown/result styling is proposed.

**bottle-size-selector** — A category-specific control (e.g., 375ml vs. 750ml) styled as adjacent pill toggles, using the same lime-on-active pattern as button-primary and a light stroke border in idle state; this component is a proposed addition suited to a specialty-oil product page, not confirmed from evidence.

## Responsive Behavior

This is a proposed recommendation only; no responsive/mobile layout was observed in the supplied evidence.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | ≤ 599px | Single-column stacking; nav collapses to hamburger/menu icon |
| Tablet | 600–1023px | 2-column product grids; nav-bar shows condensed links |
| Desktop | 1024–1439px | Full nav-bar; 3–4 column product grids |
| Wide | ≥ 1440px | Max-width container centers content; hero imagery scales up |

Touch targets should maintain a minimum 44px height (matching the observed `--aa-search-input-height:44px` variable) for buttons, inputs, and size-selector pills. Navigation collapse and any drawer/menu interaction pattern are not observed and should be validated against the live site before implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/JS variables only; no live rendering, computed layout, or DOM screenshots were available.
- Semantic color roles (e.g., which neutral serves "muted" vs. "hairline") are inferred from usage context in review-widget and autocomplete selectors, not confirmed brand documentation.
- All pixel sizes for typography scale (display-xl, title-md, body-sm, etc.) beyond the explicitly observed 16px button/base font size are proposed estimates.
- Font files for Apercu, ITC Garamond Condensed, and GT Alpina Typewriter were referenced by name only; availability, licensing, and exact weights/styles were not verified.
- No hover, focus, error, or loading interaction states were observed beyond the `.oke-button` CSS variable hooks; all other component states are proposed.
- Mobile/tablet layout, navigation collapse behavior, and grid structures are not observed and are offered only as category-typical recommendations.
