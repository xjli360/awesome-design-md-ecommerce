---
version: alpha
name: "Yellowbird"
source_url: "https://yellowbirdsauce.com"
captured_at: "2026-09-28T10:05:05.875060+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Yellowbird's storefront pairs a saturated brand yellow (#ffe845) with high-contrast black (#000000) to create a bold, condiment-aisle-ready identity. The observed body background renders on the yellow field, with black used for text, borders, and inverted button states, giving the interaction system a stamped, high-visibility look appropriate for a hot-sauce brand. A warm off-white (#fbfaf2) appears as a secondary canvas, likely for content sections that need to rest the eye between yellow blocks; this role is inferred from its low-saturation, paper-like value relative to the primary yellow.
  Typography splits duties clearly: Gooper is the observed display serif for H1 (86px, tight -2.58px tracking, 90% line-height), giving headlines an editorial, slightly vintage voice against the punchy palette. ABC Monument Grotesk is the observed body/default UI font (18px, 130% line-height), while Pitch Sans appears specifically on secondary/uppercase button treatments (16px, 700 weight), suggesting a three-tier type system: serif for brand voice, grotesk for reading, condensed sans for tactile UI labels.
  Additional palette values — deep teal (#10312b), orange-red (#ff4713), blues (#1990c6/#136f99), and a peach tint (#ffefe1) — are not tied to confirmed roles in the supplied CSS but plausibly map to product-line accents (Classic/Organic/Small Batch), given the site's segmented shop navigation. Their assignment below is explicitly inferred, not observed.

colors:
  primary: "#ffe845"
  ink: "#000000"
  canvas: "#fbfaf2"
  body: "#000000"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#000000"
  accent-warm: "#ff4713"
  accent-deep: "#10312b"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  surface-peach: "#ffefe1"
  ink-secondary: "#272d45"
  overlay: "#00000066"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "Gooper, serif", fontSize: 86px, fontWeight: 400, lineHeight: 0.9, letterSpacing: -2.58px}
  display-md: {fontFamily: "Gooper, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.05, letterSpacing: -1px}
  title-md: {fontFamily: "ABC Monument Grotesk, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.2px}
  body-md: {fontFamily: "ABC Monument Grotesk, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.3, letterSpacing: -0.19px}
  body-sm: {fontFamily: "ABC Monument Grotesk, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Pitch Sans, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "Pitch Sans, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0em}
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
    padding: "{spacing.sm} {spacing.lg}"
    border: "3px solid {colors.ink}"
  button-secondary:
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "2px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "70px"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-deep}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  heat-level-indicator:
    backgroundColor: "{colors.surface-peach}"
    activeColor: "{colors.accent-warm}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** reflects the observed default `.button`/`button` rule: black-bordered, yellow-filled, inverting to black-on-yellow on hover per the supplied `:hover` rule. This is the site's primary call-to-action treatment (e.g., "Shop Now," "Add").

**button-secondary** reflects the observed `.secondary` button variant: transparent background, black text, Pitch Sans uppercase label, no fill — proposed for lower-emphasis actions like "Read more" or filter toggles.

**text-input** is a proposed pattern, not directly observed in the supplied CSS. It assumes a white card surface and hairline border consistent with the site's clean, high-contrast aesthetic, sized for newsletter/email capture and account forms referenced in the page text.

**nav-bar** uses the observed `--header-height` and `--header-height-desktop` CSS variables (60px/70px) to size a sticky header. Background is inferred as the primary yellow since it matches the observed body background token; actual header background was not directly confirmed in the supplied rules.

**product-card** is proposed for the grid of sauces/gallons seen in the page text (e.g., "Classic Habanero Hot Sauce 2.2 oz."). It uses a white surface and hairline border for separation from the yellow page background, with title and price typography drawn from observed heading/body styles.

**hero** models the large "THIS WORLD'S TASTIEST HOT SAUCE" headline treatment, using the observed Gooper display-xl typography at full scale on the primary yellow field, consistent with the brand's bold above-the-fold pattern.

**footer** is proposed and uses the deep teal accent (#10312b) as an unobserved but palette-consistent dark surface, since no footer-specific rules were supplied. This is a stylistic inference, not a confirmed layout.

**badge** is proposed for merchandising labels such as "Made with Organic" or sale tags, using the orange-red accent for attention without relying on unverified brand meaning.

**search** models the header search affordance mentioned in the page text ("SEARCH Search Search"), using a soft neutral surface for contrast against the yellow header, since no dedicated search-field CSS was supplied.

**heat-level-indicator** is a category-appropriate, fully proposed component for communicating spice intensity across the Classic/Organic/Small Batch lines (Jalapeño through Ghost Pepper), using the orange-red accent for "filled" heat units and hairline gray for "unfilled" ones. No such component was observed in the supplied evidence.

## Responsive Behavior

This is a recommendation based on the observed `--screen-break: 768px` token, not measured site behavior:

| Breakpoint | Width      | Notes                                      |
|------------|------------|---------------------------------------------|
| Mobile     | < 768px    | Single-column product grid, header 60px    |
| Desktop    | ≥ 768px    | Multi-column grid, header 70px             |

Touch targets should be a minimum of 44px in height for buttons and nav items on mobile. Primary navigation likely collapses into a hamburger/menu overlay below 768px, consistent with the "MENU CLOSE" toggle text observed in the page copy, though the actual collapsed layout was not inspected.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically from supplied CSS and page text; no live rendering, computed layout, or DOM interaction states (hover/focus/active beyond the two documented button rules) were observed.
- Several palette colors (teal #10312b, blues #1990c6/#136f99, peach #ffefe1, navy #272d45) have no confirmed semantic role in the supplied CSS; their assignment to footer, accents, or product-line theming is inferred only.
- Two conflicting button typography rules were present in the supplied CSS (Pitch Sans 16px vs. ABC Monument Grotesk 27px uppercase on the same selector family); `button-md` here follows the more specific `.secondary` rule, but the discrepancy suggests possible cascade/theme-variant differences not resolvable from static evidence.
- Rounded and spacing scales follow a standard proposed system rather than being derived pixel-for-pixel from every observed radius/padding value; only the 10px/6px button radii and stated paddings were directly observed.
- Mobile menu, cart drawer, and search overlay layouts were referenced in page text but not present in the supplied CSS, so their visual structure is unverified.
- Custom font availability, licensing, and actual weight/style coverage for Gooper, ABC Monument Grotesk, and Pitch Sans were not verified beyond the declared `font-family` values.
